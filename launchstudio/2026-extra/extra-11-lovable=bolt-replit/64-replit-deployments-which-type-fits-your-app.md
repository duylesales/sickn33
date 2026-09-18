---
Title: "Replit Deployments: Which Type Fits Your App"
Keywords: Replit, replit deployment, always on, scheduled jobs, webhooks, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Deployments: Which Type Fits Your App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Deployments: Which Type Fits Your App",
  "description": "Choosing a deployment type is really a question about what your app does when nobody is watching. Webhooks, scheduled work, sleeping processes, static sites and why the preview URL is not a deployment.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-deployments-which-type-fits-your-app" }
}
</script>

Which deployment type should you choose? Almost everybody answers by comparing prices, which is the wrong question asked in the wrong order.

The right question is what your application does when nobody is looking at it. Does it need to answer a request from another computer at three in the morning? Does it have work that must happen on a schedule whether or not a visitor is present? Does it hold anything in memory between requests? Answer those three and the choice makes itself, at which point the price is a consequence rather than a criterion.

Product names and tiers on any platform change, and Replit's have changed more than once. What follows is about the underlying shapes, which do not.

## Four Shapes of Application

Almost everything a founder builds is one of these.

**A static site.** Files that do not change per visitor: a marketing page, documentation, a landing page with a form that posts elsewhere. No server process is required, and running one is pure waste.

**A request-response application.** Someone visits, the application does work, returns a page or data, and has nothing to do until the next request. Most products are this.

**An application other systems call.** A payment provider notifying you, a form service posting a submission, a partner's system pushing an update. The distinguishing feature is that the caller is not a person and will not retry politely forever.

**Work that happens on a schedule.** Nightly exports, reminder emails, a daily summary, a synchronisation with another system. Nobody triggers it; it must run anyway.

A real product is frequently two or three of these at once, and the mistake is deploying all of them as one thing.

## What Sleeping Actually Costs You

Deployments that scale to zero are cheaper because they stop running when idle, and everything about whether that is acceptable depends on the shape above.

**For a request-response application,** it usually is. The first visitor after a quiet period waits for a cold start — often a few seconds — and everybody afterwards does not. If your traffic is a Dutch business audience during office hours, the population experiencing that delay is small.

**For an application other systems call,** it frequently is not. Some callers time out quickly and treat a slow response as a failure. Some retry; some retry a limited number of times and then give up silently. A payment notification that never arrives does not produce an error you will see — it produces a customer who paid and did not get access.

**For anything holding state in memory,** it definitely is not, and the correct fix is not a bigger deployment. State in memory is a design problem: put it in a database and the deployment question becomes easy.

## Webhooks Are Usually the Deciding Factor

If your product takes payments, receives form submissions from an external service, or integrates with anything, you have webhooks, and they deserve a paragraph of their own.

Three properties matter. They arrive without warning, including at times when your application has been idle for hours. They are frequently retried, which means the same notification can arrive twice and your code must handle that without creating two orders. And they fail invisibly — the sending system records a failure in a dashboard you never open.

The practical implications: the endpoint receiving them must be reachable and fast at all times, it must verify the signature so that anyone who discovers the URL cannot forge an event, it must record the event's identifier and ignore a repeat, and it should acknowledge receipt immediately and do slow work afterwards rather than making the sender wait.

Get this wrong and the symptom is not downtime. It is a slow accumulation of customers whose payment succeeded and whose account did nothing.

## Scheduled Work Needs Its Own Home

The pattern that breaks quietly: a timer inside the web application, firing on an interval.

It works during development because the process runs continuously. In a deployment that sleeps, the timer sleeps too. In a deployment that runs multiple copies for capacity, the timer fires in every copy, and your nightly email goes out three times.

Scheduled work belongs in a mechanism designed for it — a scheduled deployment, a platform scheduler, or an external service calling an authenticated endpoint. Whichever you choose, add the two things nobody adds initially: a record of each run so you can see whether it happened, and an alert when an expected run does not occur. A scheduled job that has been failing for three weeks is the most common silent failure in small products, because success and failure look identical from the outside.

## The Cheapest Correct Answer Is Often Static

If your public pages do not change per visitor, serving them as static files is faster, cheaper and more reliable than running a process. It also removes an entire category of failure: a static file cannot exhaust memory, cannot fail to start, and does not care how many people arrive at once.

Many founders run a whole application to serve a page that could be a file, because the tool built it that way. Splitting the public marketing pages from the logged-in application is frequently the single highest-leverage change available, and it improves search performance as a side effect.

## When Reserved Capacity Is Worth It

Paying for a process that runs continuously buys predictability: no cold starts, memory that persists, background work that keeps running, and behaviour under load you can reason about.

That is worth money when your application is the operational tool a business depends on during its working day, when integrations call you unpredictably, when you have genuinely long-running work, or when the cost of one confusing slow morning exceeds the monthly difference.

It is not worth money to avoid a two-second delay on a product that twelve people use. Founders routinely buy predictability they do not need and skip the access rules they do.

## The Preview URL Is Not a Deployment

Worth stating plainly, because it causes real incidents.

The address you use while building is tied to your development environment. It changes, it stops when you stop, and it reflects whatever you happen to be editing. Sending it to a customer means sending them a link that will break, and occasionally means a half-finished change is live in front of a real user.

A deployment is a separate, stable thing built from a known state of your code. The moment anybody outside your laptop is using the product, the deployed address is the only one to share — and it should be on your own domain.

## Choosing, in Practice

Take your product apart. Public pages: static. The application itself: request-response, scaling to zero if a cold start is acceptable and reserved if it is not. Webhook endpoints: always reachable, signature-verified, idempotent, fast. Scheduled work: its own scheduled mechanism, with logging and an alert on non-execution.

That decomposition costs an afternoon and answers the pricing question as a by-product.

## What Happens During a Deploy

The other half of the question, and the one that produces incidents on busy afternoons.

**A deploy replaces running code.** For a brief period, requests may be served by the old version, the new version, or neither. On a small product this is usually seconds and nobody notices. It stops being invisible when a database change is involved, because the old code and the new database structure have to coexist during that window.

The rule that avoids almost every deployment incident: never change the database and the code that depends on it in one step. Add the new column first, deploy code that writes to both old and new, backfill, then deploy code that reads only the new one, and remove the old column afterwards. Four boring steps instead of one exciting one, and it means no moment exists where the running code and the live schema disagree.

**Configuration must exist before the code that needs it.** A deploy that introduces a new environment variable fails if the variable was only ever set in your development environment. This is the most common cause of "it works for me and not in production", and it is why configuration should be explicit and documented rather than accumulated by hand.

**You need a way back.** Before deploying anything consequential, know how to return to the previous version and how long that takes. Platforms generally keep previous deployments available — find out where, once, when nothing is wrong. A rollback you have to discover during an outage takes three times as long.

**Deploy when you can watch.** Not on Friday at five. Not before you leave. Deploy when you can open the error tracker ten minutes later and see whether anything changed, because the failures that matter rarely announce themselves on the deployment screen — they appear as a small number of users hitting something that was fine that morning.

**Check afterwards, deliberately.** Load the live site, log in as a real user, exercise the thing you changed, and look at the error tracker. Two minutes, and it converts a deploy from an act of faith into a verified change.

## Getting the Deployment Shape Right

For a working project, this is configuration and small refactoring rather than a rebuild: public pages separated and served statically, the application deployed from a known state rather than a development environment, webhook handling made reachable, verified and idempotent, in-memory state moved into the database so the deployment can scale, scheduled work moved to a proper scheduler with run logging and failure alerts, and environment configuration made explicit so a deploy is reproducible.

LaunchStudio does this without touching the interface you built. The engineers are Manifera's: eleven years of production infrastructure for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us what your app does when nobody is watching](https://launchstudio.eu/en/#contact) and you will get a specific recommendation, usually within one business day, or look at the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Reminders That Went Out Three Times, Then Not At All

Sanne Kuipers built Bezetting on Replit: a room-booking and occupancy tool used by two shared workspaces and a physiotherapy practice in Deventer. Members booked rooms; the system sent a reminder the evening before.

Two problems arrived within a month of each other. First, some members received the same reminder three times, which looked careless in front of paying customers. Then the reminders stopped entirely for eleven days, and nobody noticed until a member missed a booking and phoned to complain.

Both traced to the same cause. The reminder was a timer inside the web application. When the deployment ran multiple copies during a busy period, every copy fired the timer — hence three emails. When traffic was quiet and the application scaled down, the timer never ran at all — hence eleven silent days. Separately, cancellation notifications from the payment provider were reaching an endpoint that had been asleep, so two cancelled memberships still had active access.

Five business days of work: reminders moved to a scheduled deployment running once nightly, with every run recorded and an alert if no run is logged by a given hour; the booking application left scaling to zero, which suits its office-hours traffic; the payment webhook moved to a reliably reachable endpoint with signature verification and event-identifier deduplication, then tested by replaying the provider's stored events; the public information pages split out and served as static files; and the two stale memberships reconciled against the provider's records.

**Result:** no duplicate reminders and no missed nights in the nine months since, and the workspace that had complained renewed its contract.

> *"The same reminder went out three times, then it stopped for eleven days, and both were the same mistake: I had put a scheduled job inside a website."*
> — **Sanne Kuipers, Founder, Bezetting (Deventer)**

**Cost & Timeline:** €2,400 (scheduled job separation with monitoring, webhook reliability and deduplication, static split, reconciliation) — completed in 5 business days.

## Frequently Asked Questions

### How do I choose a Replit deployment type?

Ask what your app does when nobody is watching. If it only answers visitors, scaling to zero is fine. If other systems call it or work must run on a schedule, those parts need to be reachable or scheduled independently of visitor traffic.

### Is a cold start a real problem?

For a business product used in office hours, rarely — one visitor waits a few seconds. For webhook endpoints it can be serious, because some senders time out quickly and record a failure you never see.

### Why do my scheduled emails send multiple times or not at all?

Because the schedule lives inside the web application. Multiple running copies each fire it; a sleeping deployment fires it never. Move it to a scheduled mechanism, log every run, and alert when an expected run does not happen.

### Can I send customers my project's preview link?

No. That address belongs to your development environment — it changes, it stops when you stop, and it can expose half-finished work. Share the deployed address, ideally on your own domain.

### When is paying for always-on capacity justified?

When the product is an operational tool a business relies on during its working day, when integrations call unpredictably, or when you have genuinely long-running work. Not merely to remove a two-second delay for a handful of users.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I choose a Replit deployment type?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask what the app does when nobody is watching. Visitor-only apps can scale to zero; webhook endpoints and scheduled work need to be reachable or scheduled independently."
      }
    },
    {
      "@type": "Question",
      "name": "Is a cold start a real problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely for office-hours business products, but potentially serious for webhook endpoints, since some senders time out quickly and fail silently."
      }
    },
    {
      "@type": "Question",
      "name": "Why do my scheduled emails send multiple times or not at all?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the schedule sits inside the web app: multiple copies each fire it, and a sleeping deployment never does. Use a scheduled mechanism with run logging and a missed-run alert."
      }
    },
    {
      "@type": "Question",
      "name": "Can I send customers my project's preview link?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it belongs to your development environment, changes, stops with you and can expose unfinished work. Share the deployed address on your own domain."
      }
    },
    {
      "@type": "Question",
      "name": "When is paying for always-on capacity justified?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When the product is operationally relied on during a working day, integrations call unpredictably, or work is genuinely long-running."
      }
    }
  ]
}
</script>
