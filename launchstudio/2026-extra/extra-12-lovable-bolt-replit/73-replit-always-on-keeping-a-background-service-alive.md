---
Title: "Replit Always-On: Keeping a Background Service Alive"
Keywords: replit always on, background service, reserved VM, cold starts, scheduled jobs, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Always-On: Keeping a Background Service Alive

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Always-On: Keeping a Background Service Alive",
  "description": "A prototype that sleeps is fine; a product that sleeps loses work. What actually stops when a project idles, which deployment type suits which workload, and how to make background jobs survive.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-always-on-keeping-a-background-service-alive" }
}
</script>

The first thing people notice when a Replit project becomes a product is that it goes to sleep. Nobody uses it for a while, it stops, and the next visitor waits several seconds for it to wake.

The slow first request is the visible symptom and the smaller problem. The larger one is what was running when it stopped: a scheduled job that did not fire, a queue that stopped being processed, a webhook that arrived at nothing, an in-progress upload that ended mid-file.

Solving this is partly a choice of deployment type and partly a design decision about where work happens.

## What Actually Stops

Three things, and founders usually consider only the first.

**The web server.** Requests are slow while it starts, or fail if the caller does not wait. For a person clicking, an unpleasant few seconds. For a payment provider's webhook with a short timeout, a delivery failure and a retry.

**Anything running in the background.** A loop polling for work, a scheduler inside the application, a long-running task. These do not resume gracefully; they simply were not running.

**In-memory state.** Anything held in a variable rather than in a database: a cache, a counter, a session, a partly assembled upload. Gone, and the code that assumed it was there behaves unpredictably.

That third one is the source of the confusing bugs — a product that works perfectly under continuous use and behaves oddly after a quiet night.

## Choosing the Deployment Type

Replit offers several, and the choice follows the workload rather than the price.

**Autoscale** starts instances in response to requests and scales to zero when idle. Correct for a web application with variable traffic, cheap when quiet, and the source of every problem above if you are relying on something running continuously.

**Reserved VM** runs continuously. Correct when you need a background process alive: a worker consuming a queue, a scheduler, a service maintaining a connection. Costs a fixed amount whether or not anyone uses it.

**Static** serves files with no server at all. Correct for a marketing site or a frontend, fastest and cheapest, and irrelevant to anything needing logic.

**Scheduled** runs on a cron schedule and exits. Correct for periodic work — a nightly report, an hourly sync — and the right answer instead of a continuously running process that sleeps most of the time.

The common mistake is running a web application on autoscale and expecting a background loop inside it to keep working. It will not, and no amount of configuration makes it.

## Design Work That Survives Sleeping

The better answer for most products is not to need something running constantly.

Move periodic work to scheduled deployments rather than to a loop inside the application. A nightly job is a scheduled run, not a process checking the time every minute.

Keep the queue in the database, as described in the background work article in this series, so that work is durable and a worker picks up whatever is pending when it next runs — rather than holding jobs in memory that disappear.

Never keep state in memory that matters. A cache is a performance improvement that may vanish; a session, a counter or a partial result must be in the database.

And make everything idempotent, so a job that was interrupted and runs again does not produce a second of anything.

Do those four and sleeping stops being a problem: work accumulates, gets processed when a worker next runs, and nothing is lost.

## When You Genuinely Need Something Alive

Some workloads do need a continuously running process, and it is worth being clear about which.

A websocket or realtime connection your product maintains. A consumer of an external event stream. Work that must begin within seconds of arriving rather than within a minute. A long-running process that cannot be broken into scheduled pieces.

For these, a reserved deployment is the right answer and the fixed cost is the price of the requirement. What to avoid is paying for a continuously running instance because a scheduled job was implemented as a loop — which is the most common reason small products end up on the more expensive option.

## Know That It Is Running

Whatever you choose, the failure mode is silence, as the cron article in this series describes at length.

A background worker that stopped produces nothing, and so does a background worker that has no work. The two are indistinguishable without a heartbeat: every run records that it happened, and something alerts when a run has not happened within its expected window.

The same for the web application: an external uptime check, from outside the platform, against a page that exercises a real database query rather than a static file.

Both take minutes and both are the difference between noticing on Tuesday morning and hearing from a customer on Friday.

## Cold Starts Are a Customer Experience Problem

Even with the architecture right, the first request after an idle period is slow, and for a product where a customer clicks a link in an email that is a real cost.

Three things reduce it.

**Keep the application small.** A server that loads six heavy libraries at startup takes longer to become ready than one that loads two. Removing unused dependencies, as the dependency article in this series recommends, shortens startup directly.

**Do work lazily.** Connecting to every external service at startup means the first request waits for all of them. Connect when first needed instead, and cache the connection.

**Serve the shell without the server.** If your marketing pages and application shell are static files, a visitor sees something immediately while the server wakes behind them. This is the single most effective change for perceived speed and it is mostly a deployment decision.

The measure that decides whether any of this matters: how often the application actually sleeps. For a product with a handful of users across a working day, rarely — someone touches it every few minutes. For one with a weekly rhythm, most of the time, and every Monday morning visitor pays the cost.

If it is the latter and the experience matters, a scheduled request every few minutes keeps it warm for considerably less than a reserved instance costs — an inelegant solution that works, and one worth knowing about before paying for continuous capacity you do not otherwise need.

## Long Tasks Need a Different Shape

One pattern deserves particular attention because it fails in a way that is hard to diagnose: a request that does a lot of work and takes a long time.

Generating a large report. Processing an uploaded file with thousands of rows. Calling a model repeatedly for each item in a list. On a prototype with small data these complete in a few seconds. In production, with a real customer's volume, they run for minutes — and then meet a platform timeout, a proxy limit, or an instance that scales down mid-execution.

The failure is partial. Half the rows imported, half the report generated, the customer seeing an error and retrying, which starts the whole thing again alongside the part that is still running.

The shape that works, described more fully in the background work article in this series: accept the request, create a job, return immediately with an identifier, process in the background in batches, and let the customer poll or receive an email when it is done.

The rule of thumb worth adopting: any request that could take more than about ten seconds for your largest customer should not be a request. It should be a job — and "your largest customer" is doing the work in that sentence, because the version that is fine for everyone else is exactly the one that fails for the account you least want to disappoint.

## Setting This Up

For a Replit product this is typically half a day to a day: the deployment type matched to the workload with static, autoscale, scheduled and reserved used for what each suits; periodic work moved to scheduled deployments rather than loops inside the application; the job queue held in the database so work survives restarts; in-memory state eliminated for anything that matters; jobs made idempotent so interruption is harmless; a reserved deployment only where something genuinely must run continuously; a run record and absence-based alerting for every scheduled and background process; and an external uptime check against a page that exercises the database.

LaunchStudio does this when taking a Replit product to production, and it frequently reduces the bill as well, by replacing a continuously running instance with scheduled work. The engineers are Manifera's — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Tell us what your product does when nobody is using it](https://launchstudio.eu/en/#contact).

## Real example

### The Reminders That Stopped on Quiet Nights

Annemarie Poortvliet built Innametool on Replit: intake and medication checking for small pharmacy chains, sending patients a reminder when a repeat prescription is due, covering around 4,000 patients across six pharmacies.

The reminder logic ran in a loop inside her web application, checking every few minutes whether anything was due. On busy days it worked. On quiet nights the application slept, the loop stopped, and reminders due between roughly two and seven in the morning were never sent — nor were they sent later, because the loop only looked at what was due at the moment it checked.

She discovered it when a pharmacy compared their own repeat prescription records against the reminders sent and found a consistent gap.

Two business days: the reminder logic moved out of the web application into a scheduled deployment running every fifteen minutes; the job rewritten to process everything due since the last successful run rather than everything due right now, so a missed window is recovered automatically; the queue moved into the database with idempotency on patient and prescription so a re-run cannot duplicate a reminder; in-memory counters replaced with database values, which had been resetting invisibly and made her sending statistics wrong; the web application left on autoscale, since nothing now depends on it running continuously, avoiding a reserved instance she had been about to buy; run records written by every execution; an alert when the reminder job has not completed successfully within an hour; and an external uptime check against a page that queries the database.

**Result:** the gap closed, and the recovery behaviour proved itself within the first fortnight when a platform incident stopped the scheduled job for three hours — the next run processed everything that had accumulated and nobody missed a reminder. Costs fell slightly rather than rising, because the reserved instance was not needed.

> *"Reminders due at four in the morning were never sent, and they were never sent later either, because the job only ever asked what was due at that exact moment."*
> — **Annemarie Poortvliet, Founder, Innametool (Delft)**

**Cost & Timeline:** €2,200 (scheduled deployment for reminder processing, since-last-run recovery logic, database queue with idempotency, in-memory state elimination, run records and absence alerting, external uptime monitoring) — completed in 2 business days.

## Frequently Asked Questions

### What stops when a Replit project sleeps?

The web server, anything running in the background, and all in-memory state. The third causes the most confusing bugs, because the product works under continuous use and misbehaves after a quiet period.

### Do I need a reserved deployment?

Only if something must genuinely run continuously — a realtime connection, an event stream consumer, or work that must start within seconds. Periodic work belongs in a scheduled deployment.

### How do I stop a loop inside my web app from being killed?

Do not put it there. Move periodic work to a scheduled deployment and keep the queue in the database, so work is durable and picked up whenever a worker runs.

### How do I recover work missed while sleeping?

Have jobs process everything due since their last successful run rather than everything due at this moment. A missed window is then recovered automatically on the next run.

### How will I know a background job has stopped?

Only if you check for absence. Record every run and alert when one has not happened within its expected window — failure produces nothing, so nothing is what you must watch for.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What stops when a Replit project idles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The web server, any background process, and all in-memory state — the last producing bugs that only appear after quiet periods."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need an always-on reserved deployment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only for work that must run continuously — realtime connections, event streams, or tasks that must start within seconds."
      }
    },
    {
      "@type": "Question",
      "name": "How do I keep a background loop from being killed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Move periodic work into a scheduled deployment and keep the queue in the database so work is durable."
      }
    },
    {
      "@type": "Question",
      "name": "How is work missed during sleep recovered?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Process everything due since the last successful run rather than what is due now, so missed windows are caught up automatically."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know a background job stopped?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Record each run and alert on absence within the expected window — failure produces nothing, so absence is the signal."
      }
    }
  ]
}
</script>
