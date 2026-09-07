---
Title: "Background Jobs: What Should Never Happen During a Web Request"
Keywords: background job idempotency, retry with exponential backoff, dead letter queue, jobs surviving deployment, async task queue design, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Background Jobs: What Should Never Happen During a Web Request

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Background Jobs: What Should Never Happen During a Web Request",
  "description": "A technical guide to background job design for founders shipping AI-generated prototypes: idempotency, retries with backoff, dead-letter queues, and how to build jobs that survive a deploy instead of vanishing mid-run.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/background-jobs-what-should-never-happen-during-a-web-request" }
}
</script>

It's 11:40 PM. You deploy a small fix — a copy change, nothing risky. Thirty seconds later, a user's checkout request, mid-flight when the deploy restarted your server, comes back with an error. They see "something went wrong," retry, and now Stripe has charged their card twice for the same order, because the webhook handler that was supposed to record the first payment never finished — it died with the process, and there was no record anywhere that it had started, let alone that it needed to be retried safely rather than just retried.

Nothing about this required exotic traffic or an edge case few users hit. It's what happens to any operation that takes real, uncertain time — sending an email, generating a report, calling a payment provider, resizing an image — when it's built to run inline during the request that triggered it, with no plan for what happens if it's interrupted, retried, or run twice.

## Why "Just Do It Inline" Breaks Under Its Own Success

AI-generated code almost universally handles slow operations the simplest possible way: the API route that creates an order also calls Stripe, also sends the confirmation email, also updates the analytics table, all inline, all before responding to the request. It works in every test, because in every test, each of those steps succeeds quickly and nothing times out.

This breaks in three specific, predictable ways as soon as real usage arrives. First, **request timeouts**: serverless platforms cap execution time (10 seconds on Vercel's default tier, longer on paid tiers, but always finite), and a slow email provider or a Stripe API blip can push a normally-fast request over that ceiling, failing the entire operation even though the order itself was fine. Second, **user-facing latency**: a checkout that waits on three sequential API calls before responding feels sluggish in a way users notice and abandon. Third, and most dangerous, **partial failure with no record**: if step two of four fails, was the order created? Was the email sent? Nothing in an inline implementation reliably answers that, because there's no persisted state describing what should have happened, only what the code path happened to execute before it died.

The fix isn't "make it faster" — it's moving anything beyond the essential, synchronous work (validate the request, write the core record, respond) into a background job that runs separately, can be retried safely, and leaves a trail of what it attempted and what happened.

## Idempotency: The Property That Makes Retries Safe Instead of Dangerous

Idempotency is a simple idea with an intimidating name: an operation is idempotent if running it twice produces the same result as running it once. A `PUT` that sets a user's name to "Alice" is idempotent — run it five times, the name is still "Alice." A background job that says "charge this card €50" is not idempotent by default — run it twice, the card is charged €100.

This matters specifically because retries are not optional in background job systems — they're the entire point. Networks fail, third-party APIs time out, servers restart mid-job. Any job worth retrying automatically needs to be safe to run more than once, and most AI-generated job logic isn't, because nothing in a demo ever actually triggers a retry to expose the gap.

The standard fix is an **idempotency key**: a unique identifier for the specific operation (an order ID, a webhook event ID Stripe already provides, a client-generated UUID) that gets checked before the job's side effect runs. Before charging a card, check whether a charge already exists for this order ID; before sending a welcome email, check whether one was already sent for this signup. Stripe's webhook events already carry a unique `event.id` for exactly this reason — the job handler should record which event IDs it has already processed and skip duplicates, rather than trusting that Stripe (or your own queue) will only ever deliver each event once. It won't; Stripe's own documentation states webhooks can be delivered more than once, by design, and the receiving code is expected to handle it.

## Retries With Backoff: Why Retrying Immediately Makes Things Worse

When a job fails — a third-party API returned a 500, a network call timed out — the instinct is to retry immediately. This is close to the worst option available, for a specific reason: if the failure was caused by the downstream service being overwhelmed, an immediate retry from every failed job adds load to a service that's already struggling, in perfect sync with every other client doing the same thing, which is exactly the mechanism behind a cascading outage.

**Exponential backoff** retries with increasing delay between attempts — 1 second, then 2, then 4, then 8, up to a reasonable ceiling — giving a struggling downstream service time to recover instead of being retried into the ground by everyone at once. Adding **jitter** — a small random variance to each delay — prevents the thundering-herd effect where every client that failed at the same moment also retries at exactly the same moment, synchronized by the same backoff formula.

A reasonable default for most background jobs: retry up to 5 times, with delays roughly doubling and jittered by ±20%, capped around a few minutes between attempts. Most managed queue systems (BullMQ, Sidekiq, AWS SQS with Lambda, Inngest, Trigger.dev) implement this as a configuration option rather than something you write by hand — but it needs to be turned on and tuned deliberately, because the default in a hand-rolled `setTimeout`-based retry loop, which is what an AI tool tends to generate if asked for "retry logic," is usually a fixed, short delay that doesn't back off at all.

## Dead-Letter Queues: Where Failed Jobs Go Instead of Vanishing

Retries need a limit, and when a job exhausts its retries — five attempts, still failing — something has to happen to it that isn't "silently disappear." A **dead-letter queue** is exactly that: a separate holding place for jobs that failed all their retry attempts, preserved with their input data and failure history instead of being discarded.

Without one, the failure mode is invisible by default: a job fails five times, gives up, and the only trace is a log line buried among thousands of others — if it was logged at all. Nobody notices a customer's export never got generated, or their invoice PDF was never created, until that customer asks where it is, and by then reconstructing what actually happened requires digging through logs rather than looking at one clear list of "these jobs failed and are waiting for attention."

A dead-letter queue turns that into an operational task with a visible surface: a place you can check (or better, get alerted on) that shows exactly what failed, why, and with what input, so a failed job becomes a five-minute manual retry or a bug fix, not a silent data gap discovered through a support ticket. Most managed queue platforms provide this natively; if you're running jobs through a simpler mechanism (a cron-triggered function, a database-backed job table), the minimum viable version is a `status` column on your jobs table that gets set to `failed` after exhausting retries, plus a query or dashboard you actually look at, or an alert that fires when that count rises above zero.

## Jobs That Must Survive a Deploy

Every deploy on most hosting platforms involves killing the old server process and starting a new one. If a background job happens to be running in-process — a `setTimeout`, an in-memory queue, a worker thread inside your main application server — when that kill signal arrives, the job simply stops, mid-execution, with no record that it was interrupted rather than completed or cleanly failed.

This is a common gap in AI-generated implementations of "background work," because the simplest way to make something run "in the background" from inside a Node.js or Python app is an in-memory mechanism — it requires no new infrastructure and works perfectly in local development, where you rarely restart the process mid-job. In production, with regular deploys, it means some percentage of jobs are silently killed every single release, with the frequency scaling with how often you ship.

The fix is externalizing job state: the job's existence and progress live in a durable store — a database table, Redis, a managed queue — independent of any single running process. A worker picks up a pending job, and if the worker process dies mid-job (a deploy, a crash), the job remains marked as in-progress or pending in that external store, and a separate mechanism (a timeout-based reclaim, or simply restarting the worker to pick up where the queue says work is outstanding) ensures it eventually runs to completion rather than vanishing with the process that was handling it. This is precisely what dedicated job queue systems are built for — the pattern is worth adopting even for a single-founder product doing a handful of background operations, because the alternative isn't "fewer background jobs," it's "background jobs that fail exactly on your busiest days, which are disproportionately the days you're also deploying fixes."

## Choosing Your Actual Job Infrastructure

You don't need a distributed systems team to get this right — the right tool depends on your scale, not your ambitions. For a solo founder or small team with moderate job volume, a managed queue service — Inngest, Trigger.dev, or a simple Postgres-backed job table processed by a scheduled worker — covers idempotency, retries, and durability without operating new infrastructure yourself. For higher volume or more complex workflows, Redis-backed queues (BullMQ, Sidekiq) give more control at the cost of running and monitoring Redis. What matters far less than the specific tool is whether the three properties above — safe retries via idempotency keys, backoff instead of immediate retry, and durable state that survives a process restart — are actually present, because a hand-rolled `setInterval` loop and a properly configured managed queue can look identical in a demo and behave completely differently the first time a deploy lands mid-job.

## What to Check Before You Trust a Background Job With Money or Data

Walk through your product's actual background operations — email sending, payment webhook handling, report generation, any scheduled task — and ask three questions of each. If this job runs twice with the same input, does anything bad happen, or is it safe? If it fails, does it retry with increasing delay, or immediately and repeatedly? If your server restarts mid-job, does the job resume, retry from a durable record, or simply disappear with no trace? A "yes, that's a problem" on any of these, on any job that touches payments, is the one to fix first — payment webhook handling is where non-idempotent background jobs cause the most expensive, hardest-to-explain-to-a-customer failures.

This is precisely the kind of infrastructure review that's fast for [Manifera's engineers](https://www.manifera.com/services/custom-software-development/) to run because the failure patterns repeat across almost every AI-generated backend — the same three gaps, in the same handful of places, product after product. If your background jobs handle anything involving money, [use the price calculator](https://launchstudio.eu/en/#calculator) to see what a proper review and fix costs before a deploy timed badly finds the gap for you.

## Real example

### An Indie Hacker's Double-Charged Customer Traces Back to a Missing Idempotency Key

Vasil Petrov built Ledgerly, a simple invoicing tool for freelancers, using Cursor, with Stripe webhook handling that updated an invoice's status directly inside the webhook route — no queue, no retry logic, just a database update run inline when the webhook arrived.

A customer complained about being charged twice for the same invoice. Investigating the logs showed Stripe had, as its own documentation warns it might, delivered the same `payment_intent.succeeded` webhook event twice within a few seconds — a normal occurrence during Stripe's own retry behavior when a receiving server responds slowly. Ledgerly's handler had no check for whether that event ID had already been processed, so it ran its "mark invoice paid and trigger the connected payout" logic twice, initiating two payouts for one payment.

The fix added an `processed_webhook_events` table keyed on Stripe's event ID, checked before any side effect runs, moved the actual payout-triggering logic into a proper background job with retry and backoff instead of running inline inside the webhook handler, and added a dead-letter path that alerts Vasil directly if a payout job fails all its retries instead of failing silently.

**Result:** the specific double-payout bug became structurally impossible, and two near-miss duplicate deliveries in the following month were silently absorbed by the idempotency check with zero customer impact and a log entry Vasil could actually see.

> "I'd read that Stripe webhooks could arrive twice and thought 'that won't happen to me.' It happened in the first month, to a real customer, for real money."
> — **Vasil Petrov, Founder, Ledgerly (Sofia)**

**Cost & Timeline:** Launch Ready engagement, webhook and background job hardening — delivered in 5 business days.

## Frequently Asked Questions

### How do I know if my background jobs are actually idempotent?

Ask, for each job, what happens if you run it twice with identical input right now. If the answer involves a duplicate charge, a duplicate email, or a duplicate database row rather than the same end state, it isn't idempotent yet, and needs a check — typically a unique key on the operation — before it can be safely retried.

### Do I need a dedicated queue system like BullMQ for a small product?

Not necessarily. A Postgres table tracking job status, processed by a scheduled worker, is a perfectly reasonable starting point for moderate volume and gives you the durability and retry tracking you need without adding Redis or a separate queue service to operate.

### What should happen when a job in the dead-letter queue needs to be fixed?

Ideally, an alert fires the moment a job exhausts its retries, so it's addressed within hours rather than discovered through a customer complaint. The job's stored input data means it can usually be manually retried or corrected without asking the customer to redo whatever action triggered it originally.

### Is exponential backoff overkill for a job that rarely fails?

No — the value of backoff isn't for the common case, it's for the rare moment when a downstream service is struggling and every client retrying immediately makes that worse. It costs nothing to configure correctly upfront and matters exactly when you'd otherwise be caught off guard.

### Can LaunchStudio fix background job reliability without touching my frontend?

Yes. This work lives entirely in backend job handling, webhook routes, and queue configuration — none of it touches the interface your AI tool built, which is consistent with LaunchStudio's approach of fixing what's underneath without rebuilding what's visible.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I know if my background jobs are actually idempotent?", "acceptedAnswer": { "@type": "Answer", "text": "Ask what happens if the job runs twice with identical input. If the result is a duplicate charge, email, or database row rather than the same end state, it isn't idempotent yet and needs a unique key check before it's safe to retry." } },
    { "@type": "Question", "name": "Do I need a dedicated queue system like BullMQ for a small product?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily. A Postgres table tracking job status, processed by a scheduled worker, is a reasonable starting point for moderate volume, providing durability and retry tracking without adding Redis or a separate queue service." } },
    { "@type": "Question", "name": "What should happen when a job in the dead-letter queue needs to be fixed?", "acceptedAnswer": { "@type": "Answer", "text": "Ideally an alert fires the moment a job exhausts its retries so it's addressed within hours. The job's stored input data usually allows manual retry or correction without asking the customer to redo the action that triggered it." } },
    { "@type": "Question", "name": "Is exponential backoff overkill for a job that rarely fails?", "acceptedAnswer": { "@type": "Answer", "text": "No. Backoff matters for the rare moment a downstream service is struggling, when every client retrying immediately makes it worse. It costs nothing to configure correctly upfront and matters exactly when you'd otherwise be caught off guard." } },
    { "@type": "Question", "name": "Can LaunchStudio fix background job reliability without touching my frontend?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. This work lives in backend job handling, webhook routes, and queue configuration, none of which touches the interface an AI tool built, consistent with fixing what's underneath without rebuilding what's visible." } }
  ]
}
</script>
