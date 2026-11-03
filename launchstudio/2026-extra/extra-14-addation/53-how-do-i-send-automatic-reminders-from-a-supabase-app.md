---
Title: "How Do I Send Automatic Reminders From a Supabase App?"
Keywords: automatic reminders supabase, pg_cron supabase, scheduled jobs lovable, email reminders ai app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Send Automatic Reminders From a Supabase App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Send Automatic Reminders From a Supabase App?",
  "description": "Appointment reminders, renewal notices and follow-up emails need scheduled jobs. This guide shows how to build reliable reminders in a Supabase-backed Lovable or Bolt app with pg_cron, edge functions, a reminders table, time zones and duplicate protection.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-01",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase Cron", "url": "https://supabase.com/docs/guides/cron" },
    { "@type": "CreativeWork", "name": "PostgreSQL documentation", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" }
  ]
}
</script>

**Short answer:** schedule a job with Supabase Cron (built on the `pg_cron` extension) that runs every few minutes and calls an edge function. The function looks up reminders that are due, sends them through your email or SMS provider, and marks each one as sent so it never goes out twice. Store times in UTC, convert to the user's time zone for display and scheduling logic, and monitor that the job keeps running.

## Key Takeaways

- **Reliable reminders need an outbox table, a scheduler and an idempotent sender,** not a function that runs inside a web request.
- **Supabase Cron, built on PostgreSQL's pg_cron extension,** can trigger edge functions on a schedule.
- **Store timestamps in UTC and schedule in the user's time zone;** daylight saving changes in March and October are a classic source of reminders an hour off.
- **Mark reminders as processing before sending** to prevent duplicates from overlapping runs or retries.
- **Monitor the scheduler itself,** because scheduled jobs fail silently.

## The Building Blocks

| Piece | Role |
| --- | --- |
| `reminders` table | What to send, to whom, when, and whether it was sent |
| Supabase Cron job | Triggers processing every few minutes |
| Edge function | Picks due reminders, sends them, records results |
| Email/SMS provider | Delivers the message |
| Monitoring | Alerts if the job stops or failures pile up |

## Step 1: A Reminders Table

Columns such as `id`, `user_id`, `type`, `send_at` (timestamp with time zone), `payload`, `status` (pending, sent, failed), `attempts` and `sent_at`. When a booking is created, insert its reminders, for example 24 hours and 2 hours before. When it is cancelled or moved, update or cancel them.

This "outbox" approach is easier to reason about than calculating reminders on the fly, and it gives you a history of what was sent.

## Step 2: Schedule the Job

Create a cron job that runs every five minutes and calls your edge function. Keep the function's URL and a secret header in configuration, so only the scheduler can trigger it.

## Step 3: Process Safely

The edge function:

1. Selects pending reminders where `send_at <= now()`, in small batches
2. Marks them as processing in the same step, so a parallel run does not pick them up again
3. Sends each message through the provider, using an idempotency key where supported
4. Marks success or failure, increments attempts and schedules a retry for temporary failures

## Step 4: Get Time Zones Right

Store timestamps with time zone, in UTC. Decide reminder times in the user's time zone ("9:00 the day before" means 9:00 in Amsterdam, not in UTC). Daylight saving changes in March and October are a classic source of reminders an hour off.

## Step 5: Respect the Recipient

- Include only necessary details; avoid sensitive information in SMS
- Offer an opt-out for non-essential reminders
- Do not send at night unless the user asked for it

## Step 6: Monitor the Scheduler

Scheduled jobs fail silently. Alert if no job has run in the last 30 minutes or if failed reminders exceed a threshold. Our guide on [knowing when your app goes down](https://launchstudio.eu/en/blog/how-do-i-know-when-my-ai-built-app-goes-down) covers this kind of silent-failure check.

## Why Reminders Fail in AI-Built Apps

Generated reminder code often takes shortcuts that work in a demo: a timer in the browser, a check that runs when a page loads, or a function triggered every minute that recalculates who should receive a message. These approaches break in production. Browsers close, pages are not loaded at the right time, functions overlap, and nothing records what was already sent. The result is missed reminders, duplicates or both. A small amount of structure - an outbox, a scheduler and a sender - fixes all three.

## The Outbox Pattern

The outbox pattern separates deciding what to send from actually sending it. When an event happens, such as a booking being created, you write one or more rows to a reminders table with the intended send time. A separate process sends due reminders and records the result. This pattern has several advantages:

- Reminders survive restarts and deployments because they live in the database
- You can see exactly what is scheduled and what was sent
- Cancelling or rescheduling is a database update
- Retries are explicit and safe
- Reports and audits come for free

## Time Zones Done Right

Store all timestamps as `timestamp with time zone` in UTC. Store each user's or organisation's time zone, such as `Europe/Amsterdam`. When calculating a reminder like "9:00 the day before the appointment", compute it in the user's time zone and convert to UTC for storage. PostgreSQL's time zone functions handle daylight saving correctly when you use named time zones rather than fixed offsets. Test reminders that fall on the dates when clocks change; those are where bugs hide.

## Scheduling With Supabase Cron

Supabase Cron lets you schedule SQL or calls to edge functions using familiar cron expressions, such as every five minutes. For reminders, a common setup is a job every five minutes that calls a sending function, which processes due reminders in small batches. Protect the function with a secret so only the scheduler can call it, and keep the schedule in a migration so it exists in every environment.

## Sending Reliably

The sending function should:

1. Select a batch of due, pending reminders
2. Mark them as processing in the same transaction, so a parallel run skips them
3. Send each through the email or SMS provider
4. Record success with a timestamp, or failure with an error message and attempt count
5. Reschedule temporary failures with a delay, and give up after a set number of attempts

Using the provider's idempotency features, where available, adds protection against duplicates when a network error hides a successful send.

## Content and Consent

Reminders are usually transactional - they relate to a service the user requested - which means they generally do not need marketing consent. Still, respect users: let them choose channels where sensible, avoid sensitive information in SMS, send at reasonable hours and offer opt-outs for non-essential reminders. Under the GDPR, the phone numbers and emails used for reminders are personal data; include your messaging providers in your processor list.

## SMS Versus Email Versus Push

| Channel | Strengths | Considerations |
| --- | --- | --- |
| Email | Cheap, rich content, easy to log | May be read late or land in spam |
| SMS | High open rates, good for time-critical reminders | Cost per message, limited content, phone numbers are personal data |
| Push notifications | Instant, free per message | Requires app installation and permission |

Many apps combine them: email for confirmations and summaries, SMS or push for time-critical reminders.

## Monitoring Scheduled Work

Record each scheduler run with a timestamp. Alert if no run happened in the last 30 minutes, if failures exceed a threshold or if pending reminders pile up past their send time. Without these checks, a broken scheduler can go unnoticed until customers complain about missed appointments.

## A Reminder Schema You Can Adapt

A practical reminders table often includes: `id`, `organisation_id`, `user_id`, `related_type` and `related_id` (for example a booking), `channel` (email, SMS, push), `template`, `send_at` (UTC), `status` (pending, processing, sent, failed, cancelled), `attempts`, `last_error`, `sent_at` and `created_at`. Protect it with Row Level Security so users can see their own scheduled reminders if you expose them, while only server code can change status. Index `status` and `send_at` together so the scheduler finds due reminders quickly.

## Rescheduling and Cancellation

When a booking moves, update its pending reminders rather than creating new ones; when it is cancelled, mark them cancelled. Doing this in the same transaction as the booking change keeps reminders consistent with reality. A common bug in generated code is creating new reminders on every edit, so customers receive one for each version of the booking.

## Testing Reminders

Test with reminders scheduled a few minutes ahead in staging, including one on a daylight saving transition date, one for a cancelled booking and one where the provider is temporarily unreachable. Verify that exactly one message arrives at the right local time for each valid case, none for the cancelled one and a successful retry after the outage.

## The Bottom Line

Reminders look simple and quietly fail in many AI-built apps. An outbox table, a scheduled sender, correct time zones, idempotent sending and monitoring turn them into a reliable feature customers can depend on.

## Beyond Reminders: Other Scheduled Work

The same pattern serves other scheduled tasks: monthly reports, trial expiry notices, data retention clean-up, renewal warnings and nightly data syncs. Use one scheduler, one jobs log and consistent monitoring for all of them rather than a different mechanism per feature. When something stops running, you will know immediately and know where to look.

## Costs

Scheduled functions and database storage for reminders cost little. The main costs are SMS fees, which vary by country and provider, and the time to set up the system properly. Compared with the revenue lost to missed appointments or the support time spent on duplicate messages, the investment pays back quickly for most booking and service businesses.

## Related Reading

Reminders depend on reliable email delivery and on knowing when something breaks. Our guides on Supabase emails not arriving and on monitoring AI-built apps cover both.

## Questions to Ask Before Building Reminders

Which events trigger reminders, and how many per event? In which time zones do your users live? Which channels do customers prefer, and what does each cost? What should happen when an appointment changes or is cancelled? How will you know if reminders stop? Answering these five questions first makes the implementation straightforward.

## A Note on Load

If you send thousands of reminders at the same moment, such as 9:00 every morning, spread them over a few minutes and process in batches to respect provider rate limits and keep your database responsive.

## Summary

Outbox table, scheduled sender, UTC storage, local-time scheduling, idempotent sends and monitoring: six ingredients for reminders customers can rely on.

## Getting It Built

Reminders are a common LaunchStudio addition to booking and SaaS apps, usually two to four days within a fixed-price engagement. LaunchStudio is powered by Manifera, which has built scheduling systems for enterprise and logistics clients for 11+ years, with engineers in Ho Chi Minh City and client contact in Amsterdam; see [Manifera's portfolio](https://www.manifera.com/portfolio/). Supabase documents [Cron](https://supabase.com/docs/guides/cron) and scheduling edge functions.

## Real example

### An AI-Native Founder in Action: The Driving School Reminders That Arrived an Hour Late

Kees Bakkenes runs a driving school in Emmen with six instructors and built Rijlesrooster in Bolt: students book lessons, instructors manage availability and everyone receives SMS reminders. In winter, reminders worked. After the clocks changed in March, every reminder arrived an hour late, and some students missed lessons.

Bolt had generated a scheduled function that compared local times stored as text with UTC server time. It also ran every minute and re-sent reminders when the SMS provider responded slowly, so some students received the same message three times. When the function failed after a provider outage, nobody noticed for two days.

LaunchStudio created a reminders table with UTC timestamps and Europe/Amsterdam scheduling logic, moved scheduling to Supabase Cron every five minutes, made sending idempotent with status tracking, added retries for temporary failures and alerts for stalled jobs.

**Result:** Through the October clock change and the following year, reminders arrived on time without duplicates, and missed lessons fell noticeably according to Kees's instructor reports.

> *"The reminders worked perfectly for five months. Then the clocks changed and so did my students' attendance."*
> - **Kees Bakkenes, Founder, Rijlesrooster (Emmen)**

**Cost & Timeline:** €1,400 (Launch Ready package: reminders outbox, cron scheduling, time zone fixes, idempotency, retries and alerts) - completed in 5 business days.

## Frequently Asked Questions

### How do I schedule jobs in Supabase?

Use Supabase Cron, which builds on the Postgres `pg_cron` extension, to run SQL or call edge functions on a schedule. For sending emails or SMS, the cron job typically calls an edge function that does the work.

### Why are my reminders sent twice?

Usually because overlapping job runs pick up the same reminders, or retries resend messages that were actually delivered. Marking reminders as processing before sending and using idempotency keys prevents duplicates.

### Why are my reminders an hour off?

Time zone handling. Storing local times without time zone information, or mixing UTC and local times, breaks around daylight saving changes. Store UTC and schedule in the user's time zone.

### How does Manifera make scheduled jobs reliable?

By treating them as monitored infrastructure: an outbox table, idempotent processing, retries and alerts for stalled jobs. Manifera's 11+ years of logistics and scheduling systems informed these patterns.

### Can reminder emails affect my email reputation?

Yes, positively or negatively. Wanted, well-timed reminders from an authenticated domain build reputation. Duplicates, night-time messages and missing opt-outs generate complaints that hurt it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I schedule jobs in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use Supabase Cron, built on pg_cron, to run SQL or call edge functions on a schedule." }
    },
    {
      "@type": "Question",
      "name": "Why are my reminders sent twice?",
      "acceptedAnswer": { "@type": "Answer", "text": "Overlapping runs or retries resend messages; mark reminders as processing and use idempotency keys." }
    },
    {
      "@type": "Question",
      "name": "Why are my reminders an hour off?",
      "acceptedAnswer": { "@type": "Answer", "text": "Time zone handling around daylight saving; store UTC and schedule in the user's time zone." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera make scheduled jobs reliable?",
      "acceptedAnswer": { "@type": "Answer", "text": "With an outbox table, idempotent processing, retries and stalled-job alerts." }
    },
    {
      "@type": "Question",
      "name": "Can reminder emails affect my email reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Well-timed, authenticated reminders build reputation; duplicates and missing opt-outs hurt it." }
    }
  ]
}
</script>
