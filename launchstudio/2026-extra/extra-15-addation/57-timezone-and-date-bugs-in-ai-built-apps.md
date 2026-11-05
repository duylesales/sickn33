---
Title: "Timezone and Date Bugs in AI-Built Apps"
Keywords: timezone bugs javascript, timestamptz vs timestamp, daylight saving bug app, date handling supabase, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Timezone and Date Bugs in AI-Built Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Timezone and Date Bugs in AI-Built Apps",
  "description": "Appointments shifted by an hour, invoices dated the day before, reminders sent at 2 a.m. and reports that miss a day: date and time bugs are among the most common problems in AI-built apps. This guide explains the root causes, from timestamp types and JavaScript Date parsing to daylight saving time and scheduled jobs, and the rules that prevent them in Supabase and React apps.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-13",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/timezone-and-date-bugs-in-ai-built-apps" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Date/Time types", "url": "https://www.postgresql.org/docs/current/datatype-datetime.html" },
    { "@type": "CreativeWork", "name": "MDN: Date", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date" },
    { "@type": "CreativeWork", "name": "MDN: Intl.DateTimeFormat", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat" },
    { "@type": "CreativeWork", "name": "IANA Time Zone Database", "url": "https://www.iana.org/time-zones" }
  ]
}
</script>

Few bugs make an app look as unreliable as date and time errors. A client books a 10:00 appointment and the confirmation says 09:00. An invoice created on the first of the month shows the last day of the previous month. A reminder that should go out at 08:00 arrives at 02:00. A weekly report silently misses Sunday. Twice a year, around daylight saving changes, a booking system shows a slot twice or not at all.

These bugs are extremely common in apps built with Lovable, Bolt, v0 and Cursor, for an understandable reason: during development, the developer, the browser, the database and the test data all sit in the same time zone, or the code runs in UTC and nobody notices because test data has no meaningful times. Real users bring real time zones, daylight saving transitions and expectations about what "today" means.

This guide explains the root causes and the rules that prevent them.

## Key Takeaways

- **Store moments in time as `timestamptz` in UTC,** and convert to local time only for display and input.
- **Store dates without times as `date`,** not as timestamps, for birthdays, due dates and invoice dates.
- **Know which time zone each part of the system uses:** browser, server, database and scheduled jobs.
- **Use IANA time zone names such as `Europe/Amsterdam`,** not fixed offsets such as `+01:00`, which change with daylight saving.
- **Test around daylight saving transitions, month ends and midnight.**

## Two Different Kinds of Time

Most date bugs come from confusing two concepts:

**Instants** are specific moments, the same everywhere in the world: when a payment happened, when a message was sent, when a meeting starts. They are best stored as UTC timestamps with time zone awareness.

**Calendar dates and local times** are human concepts that depend on location: a birthday, an invoice date, "the store opens at 09:00", "every Monday". A birthday on 12 June is 12 June regardless of where you are. A store opening at 09:00 means 09:00 local time, which is a different instant in winter and summer.

| Value | Type to use | Example |
| --- | --- | --- |
| Payment received | `timestamptz` | 2028-06-12 08:14:03 UTC |
| Appointment start | `timestamptz` plus the location's time zone | 10:00 Europe/Amsterdam, stored as UTC |
| Invoice date | `date` | 2028-06-12 |
| Due date | `date` | 2028-07-12 |
| Opening hours | `time` plus time zone | 09:00 Europe/Amsterdam |
| Recurring rule | Rule plus time zone | Every Monday at 08:00 Europe/Amsterdam |

## Postgres: `timestamp` vs `timestamptz`

Postgres has two timestamp types. `timestamp without time zone` stores a date and time with no time zone information. `timestamptz`, or `timestamp with time zone`, stores an instant, converting input to UTC internally and outputting it in the session's time zone.

For instants, use `timestamptz`. AI-generated schemas sometimes use `timestamp`, which leads to ambiguity: is "2028-06-12 10:00" in UTC or in Amsterdam time? Different parts of the app may assume different answers.

Supabase's default columns such as `created_at` use `timestamptz` with `now()`, which is correct. Problems usually appear in columns added later, such as `appointment_time` or `starts_at`.

## JavaScript Date Pitfalls

JavaScript's `Date` object is a frequent source of bugs:

- **Parsing date-only strings.** `new Date("2028-06-12")` is interpreted as midnight UTC. In the Netherlands, that displays correctly, but users in the Americas will see 11 June. Conversely, some date pickers produce local midnight, which converted to UTC becomes the previous day, so an invoice dated 1 July is stored as 30 June 22:00 UTC and shown as 30 June elsewhere.
- **Months are zero-based.** `new Date(2028, 5, 12)` is 12 June, not 12 May.
- **`toISOString()` always returns UTC,** which turns local dates into the previous or next day near midnight.
- **Server and browser differ.** The same code produces different results in a user's browser in Amsterdam and in a serverless function running in UTC.

Rules that avoid most problems:

- Treat date-only values as strings in `YYYY-MM-DD` format and store them in `date` columns, without converting through `Date`.
- For instants, send ISO strings with explicit offsets or `Z` for UTC.
- Use a library designed for time zones, such as date-fns with its time zone utilities or Luxon, or the newer Temporal API where available, for calculations involving zones.
- Format for display with `Intl.DateTimeFormat`, specifying the time zone, for example `Europe/Amsterdam`.

## Daylight Saving Time

In the EU, clocks move forward one hour on the last Sunday of March and back on the last Sunday of October. Consequences:

- **In spring, an hour does not exist.** 02:30 on that Sunday never happens in Amsterdam.
- **In autumn, an hour happens twice.** 02:30 occurs twice, an hour apart.
- **The offset changes.** Amsterdam is UTC+1 in winter and UTC+2 in summer.

Bugs that follow:

- Slots generated by adding fixed hours to a UTC timestamp shift by an hour after the transition.
- Recurring weekly events stored as a fixed UTC time move from 10:00 to 11:00 local time when summer time starts.
- "One day" calculated as 24 hours is wrong on transition days, which have 23 or 25 hours.
- Offsets stored as `+01:00` become wrong half the year.

The solution is to store the IANA time zone name, such as `Europe/Amsterdam`, alongside local times and recurring rules, and to calculate instants using time zone aware libraries or Postgres functions such as `at time zone`.

## Scheduled Jobs and Reminders

Scheduled jobs, such as cron jobs in Supabase or your hosting platform, usually run in UTC. A job scheduled at "0 7 * * *" runs at 07:00 UTC, which is 08:00 in Amsterdam in winter and 09:00 in summer.

For reminders and reports tied to local business hours:

- Run the job frequently, for example every 15 minutes, and select items whose local send time has arrived, calculated per user or organisation time zone.
- Or schedule individual reminders as UTC instants calculated from the local time and time zone when they are created, and recalculate when rules change.

Our article on [sending automatic reminders from a Supabase app](https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app) covers reminder design.

## "Today", "This Week" and "This Month"

Reports and filters such as "orders today" or "revenue this month" depend on time zone. If the query uses UTC boundaries, orders placed in Amsterdam between 00:00 and 02:00 in summer appear under the previous day. For accurate reporting:

- Define each organisation's reporting time zone.
- Calculate period boundaries in that zone and convert them to UTC for queries.
- Use ISO week numbering where relevant; Dutch businesses commonly refer to week numbers and expect weeks to start on Monday.

Month-end matters for invoicing and VAT periods. An invoice for June must not slip into July or May because of a time zone conversion.

## Users in Different Time Zones

If your users span time zones, such as a Dutch company with a team in Portugal or customers booking from abroad:

- Store a time zone per user and per organisation or location.
- Show appointment times in the location's time zone, clearly labelled, and optionally the user's own time.
- In emails, include the time zone explicitly, for example "10:00 (Amsterdam time)".
- Generate calendar invitations with proper time zone information so they appear correctly in Outlook and Google Calendar.

## Migrating Existing Data Safely

If your app already stores times incorrectly, fixing the schema means converting existing data, and that requires care. A wrong assumption during conversion moves every record by an hour, or a day.

1. **Determine what each column actually contains.** For a `timestamp without time zone` column, check how values were written: from the browser in local time, from a server in UTC, or a mix. Sample records whose real times you know, such as recent bookings confirmed by email.
2. **Write the conversion explicitly,** for example interpreting values as `Europe/Amsterdam` local time and converting to `timestamptz`, or interpreting them as UTC, according to what you found.
3. **Run it on staging first** and compare a sample of converted values with known correct times, including records from both summer and winter.
4. **Deploy code and schema together** using an expand and contract approach: add the new column, backfill, switch reads and writes, then remove the old column.
5. **Check derived data,** such as reminders already scheduled, invoices already generated and cached reports.

Taking a day to verify assumptions is far cheaper than discovering after deployment that six months of appointments shifted.

## Testing Date Logic

Date bugs hide in edge cases. Include tests for:

- Daylight saving transitions in March and October, including the missing and repeated hours
- Midnight and month-end boundaries, especially for invoices and reports
- Leap years and 29 February
- Users in time zones far from the Netherlands
- Server code running in UTC, by setting the `TZ` environment variable in tests
- Date pickers in browsers with different locale settings

## Common Mistakes in AI-Built Apps

**`timestamp` instead of `timestamptz`** for instants.

**Invoice and due dates stored as timestamps,** shifting by a day.

**`new Date("YYYY-MM-DD")` for date-only values.**

**Fixed UTC offsets** instead of time zone names.

**Cron jobs at fixed UTC times** for local business reminders.

**Reports using UTC day boundaries** for Dutch businesses.

**Emails without time zone information.**

## How LaunchStudio Helps

LaunchStudio reviews and fixes date and time handling in AI-built apps: correcting column types, migrating ambiguous timestamps, separating dates from instants, storing time zones per organisation, user and location, fixing slot generation and recurring rules for daylight saving, adjusting scheduled jobs and reports to local time, and adding tests for edge cases.

The **Launch Ready** package (€800-€3,500) covers date and time fixes along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working across offices in Amsterdam, Singapore and Ho Chi Minh City, where time zones are part of everyday work. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Driving School App That Moved Every Lesson by an Hour

Ricardo Fernandes built Rijlesplanner with Lovable and Supabase: a scheduling app for driving schools, where instructors publish availability, students book lessons and receive reminders, and schools invoice monthly. On the Monday after summer time started, dozens of students turned up an hour late, or found their instructors waiting an hour early.

The investigation revealed several date problems at once. Recurring weekly availability was stored as a fixed UTC time, so every slot moved an hour when the offset changed. Lesson times used `timestamp without time zone`, interpreted as local time in the browser but as UTC in the reminder function, so reminders arrived an hour off. Reminders were sent by a cron job at a fixed UTC time, arriving at 06:00 in winter and 07:00 in summer instead of the intended 08:00. Monthly invoices were dated using `toISOString()`, so invoices created on the first of the month at 00:30 local time were dated the last day of the previous month, and the monthly report counted lessons by UTC day boundaries.

LaunchStudio migrated lesson times to `timestamptz` with careful conversion of existing data, and stored each driving school's time zone. Recurring availability became rules in local time with `Europe/Amsterdam`, with slots generated using time zone aware functions. Reminders were calculated as UTC instants from local times when lessons were booked, and sent by a job running every five minutes. Invoice dates became `date` columns set from the school's local date, reports used local month boundaries, and emails and calendar invitations included explicit time zone information. Tests covered both daylight saving transitions, month ends and server code running in UTC.

**Result:** The October transition passed without a single displaced lesson, and the March transition the following year likewise. Support tickets about wrong times, previously a few dozen a month, dropped to almost zero.

> *"I'd never thought about time zones because everyone using my app was in the Netherlands. It turns out the Netherlands has two time zones a year."*
> - **Ricardo Fernandes, Founder, Rijlesplanner (Tilburg)**

**Cost & Timeline:** €2,900 (Launch Ready package: column migrations, time zone aware scheduling, reminder redesign, invoice and report date fixes, and edge case tests) - completed in 8 business days.

## Frequently Asked Questions

### Should I store times in UTC?

Store instants, such as payments, messages and appointment starts, as `timestamptz`, which Postgres stores in UTC. Store calendar dates, such as invoice dates and birthdays, as `date`. Store local times and recurring rules together with an IANA time zone name.

### Why do my appointments shift by an hour twice a year?

Usually because times or recurring rules are stored with a fixed UTC offset or as fixed UTC times, which do not follow daylight saving changes. Storing local times with the `Europe/Amsterdam` time zone and calculating instants with time zone aware tools fixes this.

### Why are my invoices dated the previous day?

Often because a local date is converted to a UTC timestamp, for example with `toISOString()`, which moves dates near midnight to the previous day. Store invoice dates as `date` values in the business's local calendar, without converting through timestamps.

### How does Manifera's experience help with date and time issues?

Manifera works across offices in three time zones and has built scheduling, billing and reporting systems for 11+ years. LaunchStudio applies that experience to fix the root causes of date bugs, not only their symptoms.

### Do date bugs affect my app's reputation and visibility?

Yes, indirectly. Missed appointments and wrong invoices generate complaints and negative reviews quickly. Reliable scheduling builds the trust and recommendations that customers, search engines and AI answer engines draw on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I store times in UTC?",
      "acceptedAnswer": { "@type": "Answer", "text": "Store instants as timestamptz, calendar dates as date, and local times or recurring rules with an IANA time zone name." }
    },
    {
      "@type": "Question",
      "name": "Why do my appointments shift by an hour twice a year?",
      "acceptedAnswer": { "@type": "Answer", "text": "Fixed UTC offsets or times ignore daylight saving; store local times with Europe/Amsterdam and calculate instants with time zone aware tools." }
    },
    {
      "@type": "Question",
      "name": "Why are my invoices dated the previous day?",
      "acceptedAnswer": { "@type": "Answer", "text": "Local dates converted to UTC timestamps move near midnight; store invoice dates as date values in the local calendar." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with date and time issues?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera works across three time zones and has built scheduling and billing systems for 11+ years, fixing root causes of date bugs." }
    },
    {
      "@type": "Question",
      "name": "Do date bugs affect my app's reputation and visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; missed appointments and wrong invoices create negative reviews, while reliability builds trust signals." }
    }
  ]
}
</script>
