---
Title: "Lovable Supabase: Background Work That Actually Finishes"
Keywords: lovable supabase, background jobs, job queue, edge functions, retries, idempotency, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Background Work That Actually Finishes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Background Work That Actually Finishes",
  "description": "Work that happens after the user clicks — emails, reports, imports, model calls — needs a queue rather than a hopeful function call. Building one in Postgres, with retries, idempotency and visibility.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-background-work-that-actually-finishes" }
}
</script>

There is a moment in every growing product where the request takes too long. The user uploads a spreadsheet and waits. They generate a report and the browser spins. They click send and the page sits there while three hundred emails go out one at a time.

The instinct is to make it faster. The correct move is usually to make it asynchronous: accept the request, tell the user you are working on it, and do the work somewhere they are not waiting.

AI tools do this badly, and the way they do it badly is specific. They call the slow function without waiting for it and return immediately. The user gets a fast response, the work sometimes happens, and nobody can tell the difference between the cases.

## Fire-and-Forget Is Not a Queue

The pattern to recognise in your own code: a function invoked with no attempt to observe the result, often with a comment saying it runs in the background.

Four things are wrong with it.

Serverless environments may terminate the instance as soon as the response is sent, so the work you started is killed part-way through, deterministically, under exactly the conditions you cannot reproduce locally.

There is no retry. Whatever failed — a provider timeout, a rate limit, a network blip — simply did not happen, and nothing knows.

There is no record. You cannot tell a customer whether their import ran, because nothing wrote down that it was attempted.

And there is no limit. A thousand records arriving at once becomes a thousand simultaneous attempts, which will exhaust your database connections, your provider's rate limit, or both.

## A Queue in the Database You Already Have

You do not need a message broker. For products at this scale a table in Postgres is the right answer, and it has the significant advantage that enqueueing a job happens in the same transaction as the change that caused it.

That property matters more than it sounds. If the user's record and the job to email them about it are written together, you cannot end up with an email about something that was rolled back, or a record with no email. Every external queue has this problem; a table does not.

The table holds what you would expect: a job type, its parameters, a status, when it should run, how many attempts have been made, the last error, and timestamps. Workers claim jobs, run them, and mark them done or failed.

The one piece of craft is claiming. Two workers must never take the same job, which in Postgres is a single statement that selects the next due job, skips rows another worker has locked, and marks it as taken — all atomically. Written correctly it is five lines; written incorrectly it produces duplicate emails at exactly the moment you least want them.

## Jobs Must Be Safe to Run Twice

Retries are the entire point of a queue, and a retry means the job may run again after partially succeeding. Every job therefore has to be safe to repeat.

Concretely: check before acting rather than assuming. If the job sends a welcome email, record that it was sent and check that record first. If it charges a card, use the provider's idempotency key. If it generates a report, write to a deterministic location so a second run overwrites rather than duplicates. If it imports rows, give each source row a natural key so re-importing updates rather than inserting again.

The test is easy and worth running on every job you have: execute it twice with the same input and confirm the second run changes nothing. Jobs that fail this test are the source of the duplicate-email and double-charge reports that otherwise defy explanation.

## Retry Thoughtfully, Then Stop

Not every failure deserves the same response.

A timeout or a rate limit is worth retrying, with an increasing delay — a few seconds, then a minute, then five, then an hour. An invalid email address or a malformed row will fail identically forever, and retrying it is only a way of filling your logs.

So distinguish the two in code: permanent failures are marked failed immediately, transient ones are rescheduled with backoff. After a handful of attempts, everything stops and lands somewhere a human will look.

That somewhere matters. A failed job table nobody reads is the same as no error handling at all. Whatever your product's size, there should be one place that tells you how many jobs failed today, and it should be checked as routinely as email.

## Running the Worker

Three ways to actually execute the queue, in ascending order of effort.

A scheduled function every minute, invoked by Supabase's own cron or an external scheduler, that claims and processes a batch. Simple, adequate for most products, and bounded by how much work fits in one invocation.

A long-running worker process on a small server, polling continuously. More throughput, more predictable, and one more thing to keep alive.

A dedicated queue service, which is the right answer when volume genuinely demands it and rarely before.

Whichever you choose, set a limit on how many jobs run concurrently. The reason to use a queue is partly to protect your database and your suppliers from bursts, and a worker that claims fifty jobs at once has given that protection away.

## Users Deserve to See It

Asynchronous work changes the interface, and this is the part most implementations skip.

The user needs to know their request was accepted, that it is in progress, and when it finished — and if it failed, what to do. A spinner that never resolves because the page has no way of learning the outcome is worse than a slow request.

The simplest pattern that works: create the job, return its identifier, and have the page poll for its status. For anything long, add an email when it completes. For anything a user initiated deliberately — an import, an export, a bulk action — keep a visible history, because the first question when something is wrong is always whether it ran at all.

## Scheduled Work Is the Same Problem

Recurring jobs — nightly reports, reminder emails, subscription checks, cleanup — belong in the same system rather than in separate scheduled functions.

The reason is visibility. A scheduled function that silently stops running is one of the most common failures in small products, and it can go unnoticed for months because nothing is expected to appear when it works. If the schedule enqueues a job instead, then the absence of that job is visible in the same place as everything else, and an alert on "the nightly job has not run in 26 hours" is trivial rather than bespoke.

Keep the schedule thin: it creates jobs, it does not do work. That way a slow run cannot overlap with the next one, and a missed window can be made up deliberately.

## Keep the History, Prune the Queue

A job table grows quickly — a product doing modest volume can accumulate hundreds of thousands of rows in a year — and a queue table that has become large is a queue table that claims jobs slowly.

Separate the two purposes. The queue holds work that is pending, running or recently finished. The history holds what happened, for as long as you need to answer questions about it.

In practice that means a cleanup job, running nightly, that moves completed jobs older than a few days into an archive table or deletes them outright if the information has no value. Failed jobs stay until someone has dealt with them, which is the point of having them.

Two details matter. Index the queue for the claiming query specifically — pending jobs due now, ordered by priority and time — and prefer a partial index covering only pending rows, so the index stays small no matter how much history exists behind it. And keep job parameters small: a job referencing a row by identifier stays useful forever, while a job carrying an entire uploaded file in its parameters makes the table enormous and the archive unusable.

The symptom of getting this wrong is distinctive and confusing when it appears — a queue that gets slower over months while processing the same amount of work per day, because every claim is searching a table that is now mostly finished jobs from last spring.

## Setting This Up

For an existing product this is typically two to three days: a job table with claiming that is safe under concurrency, jobs enqueued in the same transaction as the data change that caused them, every existing fire-and-forget call converted, idempotency verified by running each job twice, permanent and transient failures distinguished with backoff and a maximum attempt count, a visible failed-job list with an alert, a worker running on a schedule with bounded concurrency, status and history surfaced to users for anything they initiated, and recurring work moved onto the queue so its absence is detectable.

LaunchStudio builds this as part of production readiness, and it usually replaces three or four places where work was started and hoped for. The engineers are Manifera's — eleven years, 120+ engineers, and a good deal of queue code in production for clients including Vodafone and TNO.

[Tell us what your app does after the user clicks send](https://launchstudio.eu/en/#contact).

## Real example

### The Imports That Half Happened

Eva Broekhuizen built Ledenimport in Lovable: membership administration for sports associations and hobby clubs, 88 clubs, most of whom import a member list from a spreadsheet at the start of each season.

Imports of 50 members worked. Imports of 600 sometimes worked. The function was called without waiting and processed rows in a loop, so in a serverless environment it was terminated somewhere between row 200 and row 500 when the response had already been sent.

Clubs discovered this by noticing members missing. Their response was to import the file again, which created duplicates of everyone who had been processed the first time — and because the second run was also cut short, a third attempt produced a membership list nobody could trust. Two clubs spent an evening deduplicating by hand.

Three business days: a jobs table with atomic claiming; the import split into one job per batch of 50 rows, enqueued in the same transaction that records the upload, so an upload always has its jobs and a rollback leaves neither; every row keyed on the club's own membership number so re-running updates rather than inserting, making the whole import safe to repeat; transient failures retried with backoff and permanent ones — malformed rows, invalid dates — recorded against the upload with the row number and reason; a maximum of three attempts, after which the job lands on a failed list with a daily alert; the worker running every minute with a concurrency limit of five; an import status page showing progress, completion and per-row errors, with an email when a long import finishes; and the nightly membership-expiry job moved onto the same queue, where its absence became visible.

**Result:** imports of any size complete, and the largest club's 3,400-member file — which had never succeeded — ran in four minutes across 68 jobs. Duplicate-member support tickets went from the dominant category to none in the following season, and the expiry job was discovered to have not run for eleven days, which nobody had noticed.

> *"Clubs were importing three times because it never finished, and every attempt made the data worse. They thought the product was unreliable. They were right, they just had the wrong reason."*
> — **Eva Broekhuizen, Founder, Ledenimport (Amersfoort)**

**Cost & Timeline:** €3,200 (job table and claiming, import batching with transactional enqueue, idempotent row handling, retry policy with permanent failure classification, failed-job alerting, bounded worker, user-facing progress and error reporting, scheduled work migration) — completed in 3 business days.

## Frequently Asked Questions

### Why does my background function stop half way through?

Because serverless instances can be terminated once the response is sent. Work started without being awaited is killed mid-execution, and nothing records that it happened.

### Do I need a message broker for background jobs?

Not at this scale. A table in Postgres is simpler, and enqueueing in the same transaction as the data change removes a class of inconsistency that external queues introduce.

### How do I stop retries from sending duplicate emails?

Make every job idempotent: record that the email was sent and check before sending. Then test by running each job twice and confirming the second run changes nothing.

### Should every failure be retried?

No. Retry timeouts and rate limits with increasing delays; fail malformed input immediately. After a few attempts everything should stop and appear somewhere a person actually looks.

### How should users see the progress of a long task?

Return a job identifier, let the page poll its status, and email when it completes. Keep a visible history for anything the user initiated, because the first question is always whether it ran.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my background function stop half way through?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Serverless instances can be terminated once the response is sent, killing work that was started without being awaited — with no record that it was attempted."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a message broker for background jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not at small scale. A Postgres table is simpler, and enqueueing inside the same transaction as the data change prevents inconsistency."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop retries sending duplicate emails?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Make jobs idempotent — record what was sent and check before acting — then verify by running each job twice."
      }
    },
    {
      "@type": "Question",
      "name": "Should every failed job be retried?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Retry transient failures with backoff; fail permanent ones such as malformed input immediately, and surface them where someone will look."
      }
    },
    {
      "@type": "Question",
      "name": "How should users see progress on a long task?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Return a job id, poll for status, email on completion, and keep a visible history of anything the user initiated."
      }
    }
  ]
}
</script>
