---
Title: "Supabase Scheduled Jobs That Silently Stop Running"
Keywords: Lovable, supabase security, scheduled jobs monitoring, cron heartbeat alerting, background queue idempotency, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Scheduled Jobs That Silently Stop Running

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Scheduled Jobs That Silently Stop Running",
  "description": "Background jobs fail in a category of their own: nothing errors, the app stays up, and something simply stops happening. The four failure modes, how to monitor absence rather than presence, and how to make jobs safe to re-run.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/scheduled-jobs-that-silently-stop" }
}
</script>

Your monitoring is green. Your error tracker is quiet. Your app has been up for thirty days without an incident. And the weekly summary email that forty customers rely on has not been sent since the twelfth of last month, because a scheduled job stopped running and nothing in your product is capable of noticing an event that fails to happen.

This is the blind spot in every monitoring setup built around uptime. Uptime answers "is it responding". It says nothing about "did the thing that was supposed to happen at 03:00 actually happen", and for most small products, the answer at some point is no.

## What Actually Runs on a Schedule

More than founders expect, even in a modest product: nightly summaries and digests, reminder emails before an appointment, subscription renewal checks, data imports from a partner, cleanup of expired records and orphaned files, report generation, cache warming, retention deletion, and anything that reconciles your database against a payment provider.

Every one of them shares the same property: nobody is waiting for the result at the moment it runs, so failure is discovered later, by accident, usually by a customer.

## Why They Stop Quietly

**A free tier paused.** Several platforms suspend inactive projects or limit background execution on lower tiers. The app still serves requests; the scheduler stops.

**A deploy changed the entry point.** A renamed function, a changed path, a restructured project. The schedule still fires and calls something that no longer exists.

**A credential expired.** The job authenticates against a database or an API with a key that was rotated, and now fails on every run.

**It errored and nobody was listening.** The most common: an exception inside the job, logged to a place nobody reads, with no alert attached because the job is not a web request.

**The platform moved.** A provider deprecated a scheduling feature or changed how it is configured, in a release note you did not read.

None of these produce a symptom in your application. That is the entire problem.

## Failure One: It Did Not Run

The default failure and the hardest to detect, because the evidence is an absence.

The fix is the heartbeat pattern: your job reports that it finished successfully, and something external expects that report. If the report does not arrive within a window, you get an alert. Several services exist for exactly this, and a modest version can be built with a table recording each run plus a check that raises an alarm when the last successful run is too old.

The important inversion: you are not monitoring the job. You are monitoring the absence of its success, which is the only way to detect something that never started.

## Failure Two: It Ran Twice

Schedulers retry. Platforms occasionally fire a schedule more than once, deploys can leave two schedules configured, and a job that times out may be restarted while the first execution is still working.

If your job sends emails, that means duplicates. If it charges cards, it means double billing. If it moves records between states, it can mean corruption.

Jobs must therefore be safe to run twice. In practice: check whether the work for this period has already been done before doing it, record completion with a period identifier that cannot be duplicated, and prefer operations that reach the same end state regardless of how many times they run.

## Failure Three: It Ran Too Long, and Overlapped Itself

A nightly job takes four minutes with a hundred records and fifty minutes with ten thousand. At some point it is still running when the next scheduled execution begins, and two copies process the same queue simultaneously.

Two defences. A lock, so a second execution exits immediately if one is already running. And batching with limits, so each run processes a bounded amount of work and picks up where it left off rather than attempting everything.

This is also why jobs need a timeout and an alert on duration: a job that grows from four to forty minutes is telling you about your data growth before your users do.

## Failure Four: Time Zones and the Clock Change

The Netherlands moves between central European time and summer time twice a year, and jobs configured in local time behave strangely on those two nights — an hour skipped, or an hour repeated, which for a job scheduled at 02:30 means either not running or running twice.

The fix is to schedule in a fixed reference time, usually coordinated universal time, and convert for display rather than for scheduling. If your job genuinely must run at a local hour — a summary that should arrive before a working day starts — make the conversion explicit and test both transitions.

## Schedules Versus Queues

A distinction worth understanding, because it determines which failures you get.

**Scheduled work** happens at a time: nightly reports, weekly digests, monthly invoicing. Failures look like absence.

**Queued work** happens in response to an event, deferred so the user does not wait: sending an email after signup, generating a thumbnail after upload, calling a slow third party. Failures look like a backlog.

Queues need their own monitoring — depth, age of the oldest item, failure counts — and their own dead-letter handling so that one poisonous item does not block everything behind it. AI-built products rarely have either, because generation produces the happy path and nothing that inspects it.

## Making Jobs Safe

Six properties, none of them complicated individually.

**Idempotent:** running twice produces the same result as running once.

**Bounded:** each execution processes a limited batch, so growth does not turn a four-minute job into a two-hour one.

**Resumable:** progress is recorded, so a failure halfway does not mean starting over or skipping records.

**Observed:** every run records start, end, duration, and what it processed.

**Alerting on absence,** not only on error.

**Manually runnable:** you can trigger it yourself to verify a fix, without waiting until 03:00.

That last one is worth its own sentence: a job you cannot run on demand is a job you cannot debug.

## A Checklist for What You Already Have

- List every scheduled and background job in your product. Most founders cannot name them all, which is itself the finding.
- For each, note when it last ran successfully. If you cannot determine that, start there.
- Add a heartbeat check on the two or three that matter commercially.
- Confirm each is safe to run twice.
- Check that jobs are scheduled in a fixed reference time.
- Add a duration alert on anything processing a growing dataset.
- Verify you can trigger each one manually.

An afternoon, and it converts an invisible category of failure into a visible one.

## Building the Layer That Notices

Background work is the part of a product that fails without anyone noticing, which makes it exactly the kind of thing worth handing to someone who has seen it fail before. LaunchStudio sets this up as part of taking an AI-built product to production: an inventory of every scheduled and queued job, heartbeat monitoring with alerts on absence, idempotency and locking so repeated or overlapping runs are safe, batching and resumability for jobs over growing data, queue depth and dead-letter handling, and a way to run everything manually when you need to.

The interface you built in Lovable, Bolt or Cursor is untouched and the codebase stays documented and AI-readable. It sits inside the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's engineers from Amsterdam and Ho Chi Minh City, with eleven years of production systems behind them for clients including Vodafone, TNO and CFLW.

If something in your product happens on a schedule and you are not certain it happened last night, [describe your project](https://launchstudio.eu/en/#contact) and we will tell you what is actually running, usually within one business day.

## Queues Need Their Own Attention

If your product defers work rather than scheduling it — sending an email after signup, generating a thumbnail after upload, calling a slow third party — the failure modes differ from scheduled jobs and need their own handling.

**Depth is the primary signal.** A queue that normally holds a handful of items and now holds four thousand is telling you something is stuck or something upstream has spiked. Alert on depth, not only on errors.

**Age matters more than count.** Ten items that have been waiting two hours is worse than a thousand that arrived in the last minute. Monitor the age of the oldest unprocessed item.

**One poisonous item can block everything.** An entry that fails, gets retried, fails again and blocks the queue behind it is the classic pattern. Failed items need to move to a dead-letter place after a few attempts so the rest keeps flowing, and somebody needs to look at that place occasionally.

**Retries need limits and backoff.** Infinite retries against a failing third party turn a temporary outage into a self-inflicted one, and they can trigger rate limits that extend the problem.

**Ordering is rarely guaranteed.** If your queued work assumes events arrive in the order they were created, verify that assumption before relying on it.

For a small product this is a modest amount of instrumentation and it converts the most opaque part of a system into something you can reason about.

## Real example

### A Rental Platform Whose Reminders Stopped for Five Weeks

Steven Bogaerts built Huurmaat in Lovable: a platform managing short-term equipment rentals for around ninety small businesses across Gelderland. A nightly job sent return reminders the day before equipment was due back, and a weekly job reconciled payments against the provider.

Both stopped on a Tuesday in March, when a deploy renamed the function they pointed at. The application worked perfectly. Nobody noticed for five weeks.

The consequences arrived slowly: late returns climbed because customers had stopped being reminded, two rentals were double-charged because the reconciliation job that would have caught it was not running, and a customer complaint about a late fee was the first hint anything was wrong.

Five business days of work: an inventory identifying seven scheduled jobs, three of which nobody remembered existed and one of which had never run successfully; heartbeat monitoring on all seven with alerts when a successful run is overdue; idempotency added so a repeated run cannot duplicate reminders or charges; locking to prevent overlap; batching and resumability on the reconciliation job, which had grown past its execution window; scheduling moved to a fixed reference time after the March clock change had caused an earlier double-send; and a manual trigger for each job.

**Result:** two subsequent job failures — a credential rotation and a provider timeout — were detected within an hour instead of weeks, and late returns fell back to their previous level within a fortnight.

> *"My app was up the whole time. It just quietly stopped doing three of the things it was for, and nothing anywhere was capable of telling me."*
> — **Steven Bogaerts, Founder, Huurmaat (Arnhem)**

**Cost & Timeline:** €2,400 (job inventory, heartbeat monitoring, idempotency and locking, batching, manual triggers) — completed in 5 business days.

## Frequently Asked Questions

### Why does uptime monitoring not catch a failed scheduled job?

Because uptime checks whether your app responds to a request. A scheduled job failing produces no request and no response — the symptom is that something did not happen, which requires monitoring absence rather than presence.

### What is a heartbeat check?

Your job reports success to an external service when it finishes, and that service alerts you if the report does not arrive within an expected window. It is the standard way to detect a job that never started at all.

### How do I make a job safe to run twice?

Record what has already been processed for the period, check before acting, and prefer operations that reach the same end state regardless of repetition. Schedulers do retry, and platforms do occasionally fire twice.

### Why did my job behave strangely around the clock change?

Jobs scheduled in local time either skip or repeat an hour when summer time begins or ends. Schedule in a fixed reference time and convert only for display, then test both transitions.

### My job used to finish in minutes and now takes an hour. Is that a problem?

Yes, on two counts: it may overlap with its next execution, and the growth tells you the job is processing more data than it was designed for. Add locking, batching with limits, and an alert on duration.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does uptime monitoring not catch a failed scheduled job?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uptime checks whether the app responds to requests. A failed scheduled job produces no request — the symptom is an absence, which requires monitoring for missing success reports."
      }
    },
    {
      "@type": "Question",
      "name": "What is a heartbeat check?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The job reports success to an external service on completion, and that service alerts you if the report does not arrive within an expected window."
      }
    },
    {
      "@type": "Question",
      "name": "How do I make a job safe to run twice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Record what has been processed for the period, check before acting, and prefer operations that reach the same end state regardless of repetition."
      }
    },
    {
      "@type": "Question",
      "name": "Why did my job behave strangely around the clock change?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Jobs scheduled in local time skip or repeat an hour at summer time transitions. Schedule in a fixed reference time and convert only for display."
      }
    },
    {
      "@type": "Question",
      "name": "My job used to finish in minutes and now takes an hour. Is that a problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — it may overlap its next run and signals data growth beyond its design. Add locking, bounded batches and a duration alert."
      }
    }
  ]
}
</script>
