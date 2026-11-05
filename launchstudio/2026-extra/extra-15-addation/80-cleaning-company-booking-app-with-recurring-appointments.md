---
Title: "Cleaning Company Booking App With Recurring Appointments"
Keywords: schoonmaak app laten bouwen, cleaning booking software, recurring appointments app, schoonmaakbedrijf planning software, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Cleaning Company Booking App With Recurring Appointments

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cleaning Company Booking App With Recurring Appointments",
  "description": "Cleaning companies serving homes and offices live on recurring appointments: weekly, fortnightly or monthly visits with the same cleaner, exceptions for holidays and changing client needs. This guide explains what a production-ready cleaning booking app needs: recurrence rules and exceptions, cleaner assignment and travel, secure handling of keys and access codes, checklists and quality control, billing per visit or subscription, SEPA direct debit, cancellations and privacy in clients' homes.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-06",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cleaning-company-booking-app-with-recurring-appointments" },
  "citation": [
    { "@type": "CreativeWork", "name": "RFC 5545: iCalendar recurrence rules", "url": "https://www.rfc-editor.org/rfc/rfc5545" },
    { "@type": "CreativeWork", "name": "Rijksoverheid: Regeling dienstverlening aan huis", "url": "https://www.rijksoverheid.nl/onderwerpen/arbeidsovereenkomst-en-cao/dienstverlening-aan-huis" },
    { "@type": "CreativeWork", "name": "Mollie: Recurring payments", "url": "https://docs.mollie.com/docs/recurring-payments" },
    { "@type": "CreativeWork", "name": "OWASP Cryptographic Storage Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html" }
  ]
}
</script>

Cleaning is one of the most recurring services there is. A household books a cleaner every Tuesday morning. An office is cleaned every weekday evening. A holiday home is cleaned after every guest. A doctor's practice needs a thorough clean every Friday. Cleaning companies, from a single entrepreneur with three employees to firms with hundreds of cleaners, spend enormous effort on planning, rescheduling, key management, quality checks and billing.

Founders with experience in the sector build booking and planning apps with Lovable, Bolt or Cursor. A one-off booking with a date picker is easy. Recurring appointments are where the difficulty lies: the schedule that repeats weekly until a client goes on holiday, the cleaner who is ill next Tuesday, the bank holiday that falls on a regular visit, the client who switches from weekly to fortnightly, and the invoice that must reflect what actually happened.

This guide explains what a production-ready cleaning app needs.

## Key Takeaways

- **Recurring appointments should be stored as rules plus exceptions,** not as thousands of individual rows generated once and never updated.
- **Clients value the same cleaner,** so assignment should prefer continuity while handling absence and substitutes.
- **Keys, alarm codes and access instructions are highly sensitive** and must be encrypted, access-restricted and logged.
- **Billing should follow completed visits** or a subscription model, with SEPA direct debit common in the Netherlands.
- **Cancellation rules, quality checks and communication** keep clients and cleaners satisfied.

## Recurring Appointments Done Right

A recurring schedule has three parts:

1. **The rule:** for example every Tuesday from 09:00 to 12:00, every two weeks, starting on a date, optionally ending on a date. The iCalendar standard's recurrence rules are a well-established way to express these patterns.
2. **Exceptions:** skipped dates, moved visits, extra visits, changed times.
3. **Occurrences:** the actual visits, generated from the rule within a planning horizon, such as the next eight weeks.

Common mistakes in AI-built apps:

- **Generating all visits for a year at once** and never updating them when the rule changes, leaving ghost appointments
- **Editing the rule without handling future exceptions,** losing manual adjustments
- **Ignoring time zones and daylight saving,** shifting appointments by an hour twice a year
- **No distinction** between "change this visit" and "change all future visits"

A robust design stores the rule and exceptions, generates occurrences for a rolling horizon, and when a rule changes, regenerates future occurrences while preserving explicitly modified ones. Our guide on [timezone and date bugs](https://launchstudio.eu/en/blog/timezone-and-date-bugs-in-ai-built-apps) explains the time handling.

## Holidays and Seasonal Changes

- **Public holidays:** decide per client whether visits on a holiday are skipped, moved or kept.
- **Client holidays:** clients pause visits for a period, ideally through the app.
- **Cleaner holidays:** substitutes are assigned, and clients are informed.
- **Seasonal changes:** some clients want extra visits before events or reduced visits in summer.

## Cleaner Assignment and Continuity

Clients strongly prefer the same cleaner, who knows the home, the client's preferences and where things are. Assignment logic should:

- **Assign a regular cleaner** per recurring schedule
- **Handle absence** by proposing substitutes with the right skills, availability and proximity
- **Inform clients** when a substitute comes, with the substitute's name
- **Respect constraints:** working hours, maximum hours per week, travel time between clients, transport mode and language
- **Balance workloads** across cleaners

Planners need a clear overview of the week, with gaps, conflicts and travel times visible.

## Keys, Alarm Codes and Access Instructions

This is the most sensitive data a cleaning app holds. A cleaner may have a key, a key safe code, an alarm code, a gate code or instructions such as "the back door is unlocked when the dog walker leaves". If this data leaks, clients' homes and offices are at risk.

Protect it rigorously:

- **Encrypt access codes at rest,** using strong, well-established encryption with keys managed separately from the database where possible.
- **Show codes only to the assigned cleaner, only on the day of the visit,** and to a small number of authorised staff.
- **Log every view** of access information.
- **Never include codes in notifications,** emails or exported reports.
- **Track physical keys:** key labels without addresses, a record of who holds which key and a check-in and check-out process.
- **Remove access** when a cleaner leaves the company, and prompt clients to change codes when appropriate.

The OWASP cryptographic storage guidance describes good practices for storing secrets.

## Checklists and Quality Control

- **Task lists per client,** such as "kitchen, bathrooms, vacuum all rooms, change bed linen every other week"
- **Room-based checklists** for larger homes and offices
- **Completion confirmation** by the cleaner, optionally with photos for specific tasks
- **Client feedback** after visits, with a simple rating and comments
- **Quality inspections** by supervisors, especially for business clients

Photos in clients' homes require care: take them only when needed, avoid capturing personal items or people, store them privately and delete them after a defined period.

## Billing Models

| Model | How it works | Suited for |
| --- | --- | --- |
| Per visit | Each completed visit is billed at a rate per hour or per visit | Households with variable schedules |
| Monthly subscription | Fixed monthly amount based on the schedule, adjusted for skipped visits by policy | Regular households and offices |
| Contract invoicing | Monthly invoice per contract with agreed scope | Business clients |
| Prepaid packages | Bundles of visits or hours paid in advance | New clients, holiday homes |

For households, SEPA direct debit with a mandate collected at sign-up, for example through a first iDEAL payment, is common in the Netherlands. Bill based on completed visits or apply clear rules for skipped visits. Business clients usually receive invoices with payment terms.

Calculate amounts on the server, record visit durations accurately and keep invoices consistent with what happened. Our guide on [money and rounding bugs](https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas) explains why.

## Cancellations

Define and enforce cancellation windows:

- **Client cancels well in advance:** no charge, visit removed
- **Client cancels late:** charge according to terms
- **Cleaner cannot come:** substitute or rescheduling, with client consent
- **Client not home or no access:** defined fee and a record of the attempt

Let clients cancel or reschedule in the app within the rules, and notify the cleaner immediately.

## Household Services and Employment Rules

Some cleaning platforms connect independent cleaners with households rather than employing cleaners themselves. In the Netherlands, households hiring someone to work in their home on fewer than four days a week may fall under a specific scheme for household services, with lighter employer obligations. Platforms and cleaning companies should understand which arrangement applies to their model, and how employment and self-employment rules affect them. These questions shape contracts, payments and responsibilities, so get legal advice before building payment flows.

## Communication

- **Visit reminders** for clients, with the cleaner's name
- **Notifications** for changes, substitutes and cancellations
- **Messaging** between client and company, with history per client
- **Cleaner app** with today's schedule, addresses, travel information, checklists and access information on the day

Cleaners often speak several languages; offering the cleaner app in the languages of the team improves adoption and quality.

## Hours, Travel and Cleaner Pay

Behind every visit is a cleaner's working time, and accurate hours matter for payroll, invoicing and fairness. A cleaner app can record start and end times per visit, with a simple check-in and check-out, and calculate travel time between clients. Planners then see planned versus actual hours, spot visits that consistently overrun and adjust schedules or prices. If cleaners are paid per hour, exports for payroll save hours of office work each month. Keep location features privacy-friendly, for example recording check-in at the client's address rather than tracking cleaners continuously.

## Office and Commercial Cleaning

Business clients bring different requirements from households:

- **Contracts with scope definitions,** such as frequency per area, specific tasks and quality levels
- **Cleaning outside office hours,** with access arrangements for buildings and alarm systems
- **Multiple locations** per client, with location-specific instructions
- **Quality reports and inspections** shared with the client's facility manager
- **Additional work requests,** such as window cleaning or deep cleaning, quoted and scheduled separately
- **Invoices per contract and location,** with purchase order references

Supporting these features is often what lets a cleaning company grow from households into the more stable commercial market.

## Onboarding New Clients

Most new clients start with an intake: a visit or call to understand the home or office, agree on tasks and frequency, arrange keys or codes and set expectations. Capturing this in the app, with checklists, access arrangements and a first visit scheduled, gives the assigned cleaner everything they need from the very first appointment.

## Roles and Access

| Role | Access |
| --- | --- |
| Client | Own schedule, visits, invoices, feedback |
| Cleaner | Own schedule, client addresses and checklists for assigned visits, access codes on the day |
| Planner | All schedules and assignments |
| Supervisor | Quality checks and feedback for their team |
| Finance | Billing, payments, invoices |
| Administrator | Settings, users, keys register |

Enforce with Row Level Security, use MFA for office staff and keep cleaners' access limited to their assignments.

## Measuring Service Quality

Owners benefit from a few indicators: share of visits completed by the regular cleaner, client ratings per cleaner, late cancellations, no-access attempts, overruns per client and churn by client type. Reviewing them monthly shows where scheduling, pricing or training needs attention.

## How LaunchStudio Helps

LaunchStudio takes cleaning booking apps from prototype to production: recurrence rules with exceptions and rolling occurrence generation, time zone handling, cleaner assignment with continuity and substitutes, encrypted access codes with day-of-visit visibility and logging, checklists and quality feedback, billing models with SEPA direct debit and invoices, cancellation rules and role-based access.

Cleaning platforms typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink's cybersecurity background is reflected in how we handle sensitive access data. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Alarm Codes in Plain Text

Sandra Pijnenburg runs a cleaning company in Breda with around 40 cleaners serving households and small offices. She built Poetsplanner with Bolt and Supabase: clients book recurring cleaning, cleaners see their schedule on their phones and clients pay monthly. It replaced a paper schedule and a lot of phone calls.

Several problems surfaced as the client base grew to around 350 households. Recurring visits had been generated for a full year when each schedule was created, so clients who changed from weekly to fortnightly still had weekly visits in the system, and cleaners occasionally turned up at the wrong homes. After the switch to summer time, many visits showed an hour later than agreed. Alarm codes and key safe codes were stored in plain text in a notes field visible to every cleaner and included in the daily schedule email. Invoices were based on the schedule rather than completed visits, so skipped visits were billed.

LaunchStudio replaced the generated visits with recurrence rules and exceptions, generating occurrences for an eight-week rolling horizon, with clear choices for changing one visit or all future visits. Times were stored with the Europe/Amsterdam time zone. Access codes moved to an encrypted field, visible only to the assigned cleaner on the day of the visit and to two office staff, with every view logged, and codes were removed from emails and exports. Clients were advised to change codes that had been exposed. Cleaner assignment preferred the regular cleaner with substitute suggestions during absence, and billing switched to completed visits with monthly SEPA direct debit through Mollie, with late cancellations charged according to the terms.

**Result:** Wrong-address visits and time confusion disappeared, invoice disputes dropped sharply, and two office clients signed larger contracts after reviewing the new approach to access codes. Sandra uses the logs to answer client questions about who accessed their access information.

> *"My clients trust us with their homes. The app was treating their alarm codes like a shopping list."*
> - **Sandra Pijnenburg, Founder, Poetsplanner (Breda)**

**Cost & Timeline:** €5,700 (Launch & Grow package: recurrence engine, time zone fixes, encrypted access codes with logging, assignment logic and completed-visit billing with SEPA direct debit) - completed in 14 business days.

## Frequently Asked Questions

### How should recurring cleaning appointments be stored?

Store the recurrence rule and exceptions, and generate actual visits for a rolling period, such as eight weeks. When the rule changes, regenerate future visits while keeping explicitly modified ones. Avoid generating a year of visits once and never updating them.

### How should a cleaning app protect alarm and key safe codes?

Encrypt them at rest, show them only to the assigned cleaner on the day of the visit and a few authorised staff, log every view, never include them in emails or exports, and prompt clients to change codes when cleaners leave.

### Should clients pay per visit or monthly?

Both work. Per-visit billing suits variable schedules; monthly subscriptions suit regular schedules, with clear rules for skipped visits. For households, SEPA direct debit with a mandate is common; business clients usually receive invoices.

### How does Manifera's experience help with service scheduling apps?

Manifera has built scheduling and service systems for clients for 11+ years, and its CEO comes from cybersecurity. LaunchStudio applies that experience to recurring schedules and to the sensitive access data cleaning companies hold.

### Does a booking app help a cleaning company get found?

It can. Clear service pages with areas, prices and online booking, plus reviews from satisfied clients, help people find the company through search engines and AI answer engines, and convert visitors into recurring clients.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How should recurring cleaning appointments be stored?",
      "acceptedAnswer": { "@type": "Answer", "text": "As rules plus exceptions with visits generated for a rolling horizon, regenerating future visits on change." }
    },
    {
      "@type": "Question",
      "name": "How should a cleaning app protect alarm and key safe codes?",
      "acceptedAnswer": { "@type": "Answer", "text": "Encrypt, show only to the assigned cleaner on the day, log views, keep out of emails and prompt code changes." }
    },
    {
      "@type": "Question",
      "name": "Should clients pay per visit or monthly?",
      "acceptedAnswer": { "@type": "Answer", "text": "Both work; SEPA direct debit is common for households and invoices for business clients." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with service scheduling apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built scheduling systems for 11+ years with a cybersecurity-led approach to sensitive access data." }
    },
    {
      "@type": "Question",
      "name": "Does a booking app help a cleaning company get found?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can, through clear service pages, online booking and reviews that search and AI engines surface." }
    }
  ]
}
</script>
