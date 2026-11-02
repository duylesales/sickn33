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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app" }
}
</script>

**Short answer:** schedule a job with Supabase Cron (built on the `pg_cron` extension) that runs every few minutes and calls an edge function. The function looks up reminders that are due, sends them through your email or SMS provider, and marks each one as sent so it never goes out twice. Store times in UTC, convert to the user's time zone for display and scheduling logic, and monitor that the job keeps running.

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
