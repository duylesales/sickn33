---
Title: "Lovable Supabase: Time Zones and Dates Done Correctly"
Keywords: lovable supabase, time zones, timestamptz, date handling, ai app security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Time Zones and Dates Done Correctly

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Time Zones and Dates Done Correctly",
  "description": "Time bugs are invisible for months and then wrong for everybody at once. Storing instants correctly, why summer time breaks recurring appointments, and the difference between a moment and a calendar day.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-time-zones-and-dates-done-correctly" }
}
</script>

Time bugs have a distinctive shape. Everything is correct for months. Then, on one particular Sunday in March or October, a set of appointments moves by an hour, a nightly report covers the wrong period, and a handful of customers receive reminders at a time that makes no sense.

Nobody changed anything. That is what makes these the most disorienting bugs a small product produces, and it is why they are usually diagnosed by a customer rather than by you.

The underlying cause is nearly always the same: a product that treats "a time" as one kind of thing when it is actually three.

## Three Different Things Called a Date

**An instant.** A specific moment that is the same moment everywhere — when a payment was received, when a record was changed, when a message was sent. Two people in different countries agree on it completely.

**A calendar day.** A date with no time in it: a birth date, an invoice date, a public holiday. It is not a moment, and attaching a time to it creates a bug.

**A local wall-clock time.** "The lesson is at nine on Tuesday mornings." This is a description of what a clock will read, in a specific place, and the instant it refers to changes when the clocks change.

Products go wrong by storing all three the same way. The rule that resolves most of it: store instants with a time zone, store calendar days as dates with no time, and store recurring local times as a time plus the zone they belong to rather than as a fixed instant.

## Store Instants With a Time Zone

In Postgres this means `timestamptz` rather than `timestamp`, and the distinction matters more than the names suggest.

A `timestamptz` records an actual point in time. Whatever offset it arrives in, it is stored unambiguously, and every reader gets the same moment. A plain `timestamp` stores digits with no indication of what they mean — so a value recorded by a server in one place and read by a browser in another is simply guessed at.

Generated schemas frequently produce the plain version, because the difference is invisible while everybody involved is in one country and the error only appears later. Check your columns. If you have plain timestamps holding moments, converting them is a migration that needs care — you must decide what zone the existing values were recorded in, and the honest answer is sometimes "we cannot be sure for rows before March".

Then: store in UTC, convert for display, and do the conversion at the edge. The database and your logic work in one consistent frame; only the interface shows local time.

## The Dutch Specifics That Bite

Two, and they are the ones behind almost every Dutch product's time bugs.

**The Netherlands observes summer time,** so the offset is +1 for part of the year and +2 for the rest. A product that stored "+1" once and applied it forever is wrong for roughly half the year, and it is right when you test it in winter.

**The change happens at a defined moment in the early hours on a Sunday in March and October.** On one of those days a local hour does not exist; on the other, a local hour happens twice. Any scheduled job running at that hour will either be skipped or run twice, and any appointment stored as an instant rather than as a local time will move.

The practical consequence for a scheduling product: an appointment described as "every Tuesday at 09:00" must be stored as a local time with its zone, and the instant computed for each occurrence. Storing the first occurrence as an instant and adding seven days repeatedly produces appointments that are an hour wrong after the clocks change — and the customers who notice are the ones who arrive an hour early.

## Calendar Days Are Not Moments

The second most common error, and the easiest to fix.

A birth date, an invoice date, a holiday — these have no time. Stored as a timestamp at midnight and converted between zones, they shift to the previous day for some users, which produces an invoice dated the 31st appearing as the 30th and a birthday that is wrong for anybody east of you.

Use a date type. It does not participate in conversion, which is exactly what you want.

A related case: a period like "the month of September" is a range of local days in a specific zone, and reports computed in UTC against local expectations will include or exclude the boundary days incorrectly. Decide which zone your reporting is defined in, write it down, and apply it consistently.

## Scheduled Work and the Hour That Does Not Exist

Jobs deserve their own attention.

Run them at a time that avoids the transition hours where you can — something in the middle of the night but not at the changeover — and make them idempotent, so a job that runs twice does not send two invoices. Record every run, so a skipped one is visible rather than inferred.

And be explicit about which zone a schedule is defined in. A job configured "at 02:00" on a platform whose scheduler works in UTC runs at 03:00 or 04:00 local, which is usually harmless and occasionally means a daily report covers the wrong day.

## Displaying Time to People

Three small decisions that remove most support questions.

**Show times in the viewer's own zone by default,** and say which zone you are showing. "14:00 (Amsterdam)" costs nothing and prevents an entire category of confusion in any product used across borders.

**Prefer relative phrasing for recent events** — "20 minutes ago" — which is unambiguous regardless of zone.

**Let users set a zone explicitly** rather than only inferring it from their browser. People travel, and a physiotherapist checking tomorrow's schedule from a holiday in Spain should not see their appointments shifted.

## What to Check in Your Own Product

Half an hour. Look at whether your timestamp columns carry a zone. Change your computer's clock to another zone and open your product — appointments, dates, reports — and see what moves. Check what a recurring appointment does across a clock change by creating one either side of the date. Confirm your scheduled jobs are logged and idempotent. And check that a date-only value is stored as a date.

Do this now rather than in late October, which is when the alternative schedule presents itself.

## Durations, Deadlines and Working Days

A second family of time bugs, unrelated to zones and equally damaging, because these ones produce disputes rather than confusion.

**"Within 30 days" is ambiguous until you define it.** Thirty calendar days from the moment, or from the start of the next day? Does the thirtieth day end at midnight, and in which zone? A payment term, a cancellation window, a trial period and a notice period are all deadlines somebody will eventually argue about, and the product's answer should match what your terms say rather than what a date library did by default.

**Working days are not days.** A Dutch business product promising a response "within two working days" needs to know that Saturday and Sunday do not count, and neither do public holidays. Those holidays are not a fixed list — Easter moves, King's Day falls on the 27th of April unless that is a Sunday, and some sectors observe days others do not. If a commitment depends on working days, encode a holiday calendar rather than approximating, and make it a table you can update rather than a list inside a function.

**Notice periods and renewals deserve explicit rules.** A subscription that renews on the anniversary needs a defined answer for the 31st of a month in a shorter month, and a cancellation deadline expressed in whole days needs a defined boundary. These edge cases occur in a small fraction of accounts and generate a disproportionate share of complaints, because the affected customer is always certain and always affected financially.

**Test the boundaries deliberately.** The last day, the first day, midnight, the 29th of February, the end of a month with 31 days, and both clock-change weekends. Ten minutes of deliberate edge cases finds what a year of ordinary use will eventually find for you, in front of a customer.

## Getting Time Right Across a Product

For a running product this is bounded work: timestamp columns converted to carry zones with a documented decision about what existing values meant, calendar days moved to date types, recurring events stored as local times with their zone and instants computed per occurrence, reporting periods defined in a stated zone, scheduled jobs made idempotent and logged with transition hours avoided, and the interface showing the viewer's zone with an explicit label and a user-settable preference.

LaunchStudio does this without changing your interface, and the correction of historical data is handled with you rather than guessed at. The engineers are Manifera's: eleven years of production systems across Amsterdam Herengracht 420, Singapore and Ho Chi Minh City — three time zones, which is why this article exists.

[Tell us where your times look wrong](https://launchstudio.eu/en/#contact) for a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Every Client Abroad, One Hour Early

Noortje Haan built Trainingsschema with Lovable: online coaching session scheduling used by fourteen personal trainers and physiotherapists in Utrecht and Amersfoort, about a third of whose clients live outside the Netherlands — expatriates who moved away and kept their coach.

Sessions were stored as plain timestamps with no zone. Times were displayed exactly as stored, with no label. Recurring weekly sessions were created by storing the first session and adding seven days repeatedly.

Three separate faults produced one confusing picture. Clients abroad saw the Dutch local time with no indication of what zone it was, so a client in Portugal arrived an hour late every week and had assumed she was misremembering. After the March clock change, every recurring session in the system moved by an hour relative to the trainer's calendar, so fourteen trainers spent a fortnight correcting appointments by hand and one lost two clients over missed sessions. And the weekly summary emailed to trainers on Monday mornings was computed in UTC, so sessions late on Sunday evening appeared in the following week's report — which had made the revenue figures disagree with the trainers' own records for months.

Eight business days of work: timestamp columns converted to carry zones, with existing values interpreted as Dutch local time after confirming with the trainers that all sessions had been entered from the Netherlands and documenting that assumption; recurring sessions restructured to store a local time with its zone, with the instant computed per occurrence so a clock change no longer moves anything; session times displayed in the viewer's zone with an explicit label and a user-settable preference for clients who travel; the weekly summary redefined against Dutch local days with the definition stated in the email; scheduled jobs made idempotent and moved away from the transition hour, with runs logged; and a test suite added covering both clock-change weekends.

**Result:** no time complaints across the following March and October transitions, which was the first time either had passed without manual correction. The Portuguese client, informed of what had happened, stayed.

> *"A client in Portugal turned up an hour late every single week for four months and blamed herself. My product had simply printed a number with no idea what it meant."*
> — **Noortje Haan, Founder, Trainingsschema (Utrecht)**

**Cost & Timeline:** €3,800 (column conversion with documented interpretation of historical values, recurring event restructuring, display and preference handling, reporting period definition, job idempotency, clock-change tests) — completed in 8 business days.

## Frequently Asked Questions

### Which column type should I use for times?

`timestamptz` for anything that is a moment, so the value is unambiguous regardless of who reads it. A date type for calendar days such as birth dates and invoice dates, since those are not moments and should not convert.

### Why do my appointments move when the clocks change?

Because a recurring appointment was stored as a fixed instant and repeated by adding days. "Every Tuesday at 09:00" is a local wall-clock time, so store the local time with its zone and compute the instant for each occurrence.

### Why is an invoice dated the 31st showing as the 30th?

Because a calendar day was stored as a timestamp at midnight and converted between zones. Use a date type, which does not participate in conversion.

### What should I do about scheduled jobs?

Avoid the clock-change transition hours, make jobs idempotent so a double run does not duplicate anything, log every run so a skipped one is visible, and be explicit about which zone the schedule is defined in.

### How should times be displayed?

In the viewer's own zone with the zone stated — "14:00 (Amsterdam)" — with relative phrasing for recent events, and a preference users can set explicitly rather than relying only on their browser.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which column type should I use for times?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "timestamptz for moments so values are unambiguous, and a date type for calendar days such as birth dates and invoice dates."
      }
    },
    {
      "@type": "Question",
      "name": "Why do my appointments move when the clocks change?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the recurrence was stored as a fixed instant and repeated by adding days. Store the local time with its zone and compute each occurrence's instant."
      }
    },
    {
      "@type": "Question",
      "name": "Why is an invoice dated the 31st showing as the 30th?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A calendar day was stored as a midnight timestamp and converted between zones. Use a date type, which does not convert."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do about scheduled jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Avoid transition hours, make them idempotent, log every run, and state which zone the schedule is defined in."
      }
    },
    {
      "@type": "Question",
      "name": "How should times be displayed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In the viewer's zone with the zone labelled, relative phrasing for recent events, and an explicit user-settable preference."
      }
    }
  ]
}
</script>
