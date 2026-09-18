---
Title: "Lovable Hosting: Cron and Work That Runs Off the Request"
Keywords: lovable hosting, cron jobs, scheduled tasks, pg_cron, job monitoring, heartbeat alerts, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Cron and Work That Runs Off the Request

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Cron and Work That Runs Off the Request",
  "description": "Scheduled work in an AI-built app fails silently, because nothing appears when nothing runs. Where to run cron, why time zones break reminders, and the heartbeat that tells you it stopped.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-cron-and-work-that-runs-off-the-request" }
}
</script>

Every failure in a product announces itself except this one. A broken page produces an error. A failed payment produces a complaint. A scheduled job that stops running produces nothing at all — no error, no alert, no support ticket — because what it was supposed to create simply does not appear, and nobody misses a thing they never saw.

Reminders stop going out. The nightly export stops arriving. Subscriptions stop being checked. And the median time to discovery, in the products we have looked at, is measured in weeks.

The engineering here is trivial. The discipline is not, and it comes down to one idea: something must complain when the job does not run.

## Where Scheduled Work Can Live

Four options, and for a Lovable and Supabase product the first two cover nearly everything.

**Supabase's own scheduler** runs SQL or calls a function on a schedule, inside the database, with no additional service. Ideal for data maintenance, cleanup, aggregation refreshes and enqueueing work.

**Your hosting platform's cron**, which invokes an endpoint in your application on a schedule. Ideal when the work needs your application's code — sending emails, calling providers, generating documents.

**An external scheduling service** that calls a URL, which has the advantage of being independent of your platform and of telling you when a call fails.

**A long-running worker** on a small server, which is the right answer only when volume justifies it.

Whichever you choose, one rule holds: the scheduled task should enqueue work rather than perform it. A schedule that creates jobs is quick, cannot overlap with itself, and leaves a record. A schedule that spends four minutes sending emails will eventually be cut off part-way through by a platform timeout, having sent an unknown proportion of them.

## Protect the Endpoint

Cron that works by calling a URL creates a URL that anyone can call.

If that endpoint sends invoices, an outsider who finds it can send them repeatedly. If it recalculates balances, they can run it a thousand times. And URLs are found — in logs, in browser history, in a repository, by scanning.

The protection is a shared secret in a header, checked before anything happens, with the request rejected otherwise. Platform-provided cron mechanisms often supply one; if yours does not, invent one. It is three lines of code and the alternative is an endpoint with real power and no door.

While you are there, make the job idempotent for the same reason as any background work: a retry, a double invocation or an accidental manual call should not produce two of anything.

## Time Zones Break Reminders Specifically

Schedules run in UTC unless told otherwise, and the Netherlands is one or two hours ahead depending on the season.

A job set to run at 08:00 goes out at 09:00 Dutch time in summer and 10:00 in winter, which for a reminder that says "your appointment is at nine" is the difference between useful and useless. Twice a year, on a Sunday in March and October, every schedule in your product shifts by an hour relative to your customers.

Two habits handle it. Schedule in UTC deliberately and convert, rather than hoping the platform's default matches your users. And for anything where the local hour matters — reminders, daily summaries, business-hours notifications — run the job more often than you need and decide inside it which recipients are due, based on their own time zone.

The second habit is what makes a product work for a customer in another country without a second implementation, and it costs nothing to adopt early.

## Overlap, Timeouts and the Job That Takes Longer Than Its Interval

A job scheduled every five minutes that starts taking six minutes will eventually be running twice at once, and the failure that follows depends on what it does — duplicate emails, double-counted rows, a deadlock.

Prevent it with a lock the job takes at the start and releases at the end, so a second invocation sees it and exits. In Postgres this is one advisory lock call; in application code it is a row in a table.

Timeouts deserve the same thought. Platform-invoked cron endpoints usually have a hard limit of seconds to a couple of minutes. A job that grows with your data will cross that limit one day, silently, in the middle of its work. Enqueueing instead of doing solves this by construction, which is why it is the recommendation.

## The Heartbeat That Makes Silence Audible

This is the part to build even if you build nothing else.

Every scheduled job records that it ran and whether it succeeded. A single check, itself running on a schedule, looks at those records and alerts if anything expected has not happened within its window.

The inversion matters: you are not alerting on failure, which you would see anyway. You are alerting on absence, which is the failure mode that actually occurs.

A table with the job name, the last successful run and an expected interval is enough. So is an external monitoring service where each job calls a unique URL when it finishes and the service notifies you when a call does not arrive — which has the advantage of still working when your entire platform is down, and is free at the volumes a small product needs.

## Write Down What Runs

Nobody can review what they cannot see, and scheduled work is invisible by nature: nothing in your application's interface mentions it.

A file in the repository listing each job, its schedule, what it does, what it touches and what should happen if it fails is ten minutes of writing that pays for itself the first time somebody else has to understand your product — or the first time you return to it after a month on something else.

The same list is what makes an annual review possible. Jobs accumulate: a cleanup for a table that no longer exists, a summary email nobody reads, a sync to a service you stopped using. Each one runs forever, consuming resources and occasionally failing, until somebody deliberately looks.

## Make Every Job Runnable by Hand

A scheduled task that can only be triggered by its schedule is a task you cannot investigate, test or recover.

Give each one a way to run on demand — an admin action, a command, a protected endpoint you can call — with two parameters worth supporting. A dry run that reports what it would do without doing it, which is how you verify a change safely. And a date or range, so a job that missed Tuesday can be run for Tuesday rather than for today.

That second parameter is what turns a missed window from an incident into a task. The reminder job that failed on the 14th can be run for the 14th; the report that did not generate for last month can be generated for last month. Without it, the only recovery is to wait for tomorrow and accept the gap, which is precisely what happens in most small products because nobody built the alternative.

The related habit: make jobs operate on a stated period rather than on "now". A job that asks for records created since the last successful run is resilient to being late, to being skipped, and to being run twice. A job that asks for records created today loses everything the moment it does not run today — which is exactly the day you needed it to be robust.

One more reason to build it: the first thing anyone does when a scheduled job misbehaves is try to reproduce it, and a job that only runs at four in the morning is a job you debug at four in the morning. A manual trigger converts that into an ordinary afternoon's work.

## Setting This Up

For an existing product this is typically half a day to a day: every scheduled task inventoried, each one converted to enqueue work rather than perform it, endpoints protected with a shared secret and made idempotent, schedules set in UTC with local-hour work driven by recipient time zones, overlap prevented with locks, a run record written by every job, an absence-based alert with expected intervals, external heartbeat monitoring for the critical ones, and the whole set documented in the repository.

LaunchStudio sets this up as part of production readiness, and under the €49 per month managed arrangement the heartbeat alerts come to us rather than to you. The engineers are Manifera's — eleven years, 160+ projects, from Herengracht 420 in Amsterdam and Ho Chi Minh City.

[Ask us when your nightly job last ran](https://launchstudio.eu/en/#contact). Most founders cannot answer.

## Real example

### Eleven Days of Missing Reminders

Casper IJsselstein built Afspraakherinnering with Lovable: appointment reminders for dental and orthodontic practices, sent the evening before by email and SMS, used by 38 practices covering roughly 1,900 appointments a week.

The reminder job ran nightly on his hosting platform's cron. In March a deploy changed a dependency, the job began failing on its first line, and the platform recorded a failed invocation in a log nobody was watching.

Eleven days later a practice manager in Bergen op Zoom called to ask whether reminders were switched off, because their no-show rate had roughly doubled. Across 38 practices that was around 3,000 reminders never sent and, by the practices' own estimates, more than 200 missed appointments.

Two business days: the reminder task converted from doing the work to enqueueing one job per practice, so a failure affects one practice rather than all of them and a timeout cannot cut the run in half; the cron endpoint protected with a shared secret, having previously been callable by anyone who knew the path; scheduling moved to hourly with recipient time zone and practice opening hours evaluated inside the job, replacing a single UTC run that had been going out an hour late since the clocks changed; an advisory lock to prevent overlap; a run record written by every job; an absence-based alert firing when the reminder run has not completed successfully within 26 hours; external heartbeat monitoring so the alert works even when the platform does not; and a document listing all six scheduled jobs, which identified two that had been doing nothing useful for months.

**Result:** the failure mode is now detected in hours rather than weeks. In the following year the absence alert fired three times — twice for genuine failures caught the same morning, once for a platform incident — and no practice has discovered a gap before Casper did.

> *"It failed every night for eleven days and my product looked completely healthy the whole time. Nothing was broken on any screen. The thing that was missing was something nobody sees."*
> — **Casper IJsselstein, Founder, Afspraakherinnering (Roosendaal)**

**Cost & Timeline:** €2,100 (task conversion to queued jobs, endpoint authentication, time zone aware scheduling, overlap locking, run records, absence alerting with external heartbeat, job documentation and cleanup) — completed in 2 business days.

## Frequently Asked Questions

### Why do scheduled jobs fail without anyone noticing?

Because their success produces something and their failure produces nothing. No error reaches a user, so the only signal is an absence — which is why the alert must be on absence rather than on failure.

### Should a cron job do the work or queue it?

Queue it. A schedule that enqueues finishes in milliseconds, cannot overlap, leaves a record and is immune to platform timeouts that would otherwise cut long runs in half.

### How do I stop strangers calling my cron endpoint?

Require a shared secret in a header and reject anything else before doing any work. A scheduled endpoint is a URL with real power and it will eventually be found.

### Why do my reminders go out an hour late in winter?

Schedules run in UTC and the Netherlands shifts between one and two hours ahead. Run the job more frequently and decide who is due inside it, based on each recipient's local time.

### What is the minimum monitoring worth having?

A record of each job's last successful run and an alert when one has not completed within its expected window. An external heartbeat service adds the case where your own platform is down.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do scheduled jobs fail unnoticed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Failure produces nothing rather than an error, so nobody sees it. Alert on absence — a job that has not run — rather than on failure."
      }
    },
    {
      "@type": "Question",
      "name": "Should a cron job perform the work or enqueue it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Enqueue it. The schedule finishes instantly, cannot overlap itself, leaves a record, and is immune to platform timeouts."
      }
    },
    {
      "@type": "Question",
      "name": "How do I protect a cron endpoint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Require a shared secret in a header and reject everything else before doing any work. The URL will eventually be discovered."
      }
    },
    {
      "@type": "Question",
      "name": "Why do scheduled reminders shift by an hour in winter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schedules run in UTC while the Netherlands moves between one and two hours ahead. Run more often and select recipients by their own local time."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum monitoring for scheduled work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A last-successful-run record per job plus an alert when one misses its window, ideally with an external heartbeat that survives platform outages."
      }
    }
  ]
}
</script>
