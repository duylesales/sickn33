---
Title: "Time Zones and Dates: The Quiet Source of Wrong Answers"
Keywords: timezone bugs SaaS, store UTC display local, daylight saving bug booking, date only vs timestamp, recurring events timezone, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Time Zones and Dates: The Quiet Source of Wrong Answers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Time Zones and Dates: The Quiet Source of Wrong Answers",
  "description": "Date handling is where products produce confidently wrong answers: reports off by a day, bookings an hour out twice a year, deadlines that expire early. The rules that prevent it, and why AI-generated code gets this wrong in a predictable way.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/time-zones-and-dates-the-quiet-source-of-wrong-answers" }
}
</script>

Most bugs announce themselves. Date and time bugs do not: they produce an answer, the answer looks reasonable, and it is wrong. A monthly report that includes one day too many. A booking confirmed for 10:00 that the customer attends at 09:00. A trial that expires a day early for everyone east of you. Nothing errors, nothing is logged, and the defect is usually reported by a customer who has already acted on the wrong information.

It is also uniquely likely in AI-generated products, for a structural reason. Date handling has correct answers that depend on intent — is this a moment in time or a calendar day? — and a code generator working from a one-line prompt cannot know which you meant. It picks one, plausibly, and the consequence surfaces months later, typically at the end of a month or the start of daylight saving.

## The One Rule That Prevents Most Problems

Store every moment in UTC. Convert to a timezone only when displaying it to a person, and always store the timezone the event belongs to when it matters.

That sentence eliminates the majority of timezone bugs, and the reason is that UTC is the only representation that is unambiguous, comparable, and unaffected by daylight saving. Two events stored in UTC can be sorted and subtracted correctly, always. Two events stored in local time cannot: 02:30 occurs twice on the night European clocks go back and does not exist at all on the night they go forward.

The corollary matters as much: never store a time that came from the browser without converting it. A form submitted at "14:00" means 14:00 in the timezone the person was sitting in, which is information the browser has and the server does not, unless it is sent explicitly. Prototypes routinely store the string as given, and the record is then unusable for anyone in another timezone — including the same person after they travel.

The last part — storing the timezone alongside the moment — is what people skip. For a meeting scheduled at 14:00 Amsterdam time, UTC alone is not sufficient information, because if that meeting recurs weekly, the correct UTC time changes when the clocks do. The intent is "14:00 in Amsterdam", and only storing the timezone preserves it.

## Not Everything Is a Moment

The second major error is treating dates that are not moments as if they were.

A birth date is not a moment in time. Neither is an invoice date, a holiday, or a contract start date. These are calendar dates that mean the same thing everywhere, and storing them as timestamps introduces a bug immediately: `1985-06-14` stored as a timestamp becomes midnight, in some timezone, and displayed in a timezone one hour behind it becomes 23:00 on 13 June. The customer's birthday is now a day earlier than it is.

Databases have a date type without a time component. Using it for calendar dates is the entire fix, and it is skipped constantly because a generated schema tends to make everything a timestamp by default.

The same distinction governs comparisons. "Show invoices from March" is a calendar question, and answering it requires knowing whose March — the customer's, most likely, not the server's. A query that filters on UTC boundaries returns a March that starts and ends an hour off for a customer in Amsterdam, quietly moving a small number of records between months. In a financial product that discrepancy eventually reaches an accountant.

## Daylight Saving Breaks Things Twice a Year

Two nights a year, arithmetic on local times stops working, and the failures are specific.

**Adding 24 hours is not the same as adding a day.** On the night clocks change, a day is 23 or 25 hours long. Code that computes "tomorrow at the same time" by adding 86,400 seconds will be an hour out for everyone affected. Deadlines, reminders, and expiries all inherit this.

**Recurring events drift or jump.** A weekly 09:00 appointment stored as a fixed UTC time becomes 10:00 after the clocks change. Stored with its timezone and recomputed, it stays at 09:00, which is what everyone expects.

**Some local times do not exist, and some occur twice.** A recurring 02:30 job does not run on the spring transition and runs twice on the autumn one unless something prevents it — which is how duplicate invoices get issued in the small hours of one Sunday in October.

The practical defences are not exotic: store the timezone with recurring events, use a date library that does timezone-aware arithmetic rather than adding seconds, and avoid scheduling anything for the hours around 02:00 to 03:00 local time. And test with the transitions deliberately, because they are two of the very few dates on which a product predictably behaves differently.

## Display, Input, and Not Confusing Anyone

Two decisions determine whether customers trust what they see.

**Whose timezone do you display?** For most products, the viewer's — detected from their browser, with the ability to override in settings, because a laptop set to the wrong zone is common. For products where events belong to a place — a booking at a physical location — displaying the location's time, labelled, is less confusing. What is never acceptable is displaying a time without any indication of which timezone it is in when your customers might not share yours.

**How are dates entered and read?** `03/04/2027` is 3 April in the Netherlands and 4 March in the United States. For a European product, a date picker removes the ambiguity entirely; where text entry is needed, an unambiguous format and a visible interpretation ("3 April 2027") prevents a class of silent error. The same applies to imports, where a column of ambiguous dates should be interpreted according to a stated rule and shown in the preview.

Getting storage, arithmetic, comparison boundaries, and display right across a product is unglamorous and consequential, and it is one of the more common defects found when AI-built products are reviewed before launch — precisely because nothing about it produces a visible error. LaunchStudio, backed by Manifera's 11+ years of production engineering, audits and corrects date handling as part of launch preparation. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Testing for Bugs That Only Appear Somewhere Else

The difficulty is that this class of bug is invisible from where you sit: your machine, your timezone, and the current month all conspire to make everything look correct.

Four cheap tests catch most of it. Change your computer's timezone to somewhere several hours away and use the product — bookings, reports, and deadlines that shift are the bugs. Set the date near a month boundary and generate a report, checking whether the first and last day are included correctly for a customer in a different zone. Set the clock to the night of a daylight saving transition and exercise anything recurring. And create a record at 23:30 local time, then check which day it appears under in your own reporting.

Each takes minutes and finds problems that would otherwise be reported by a customer who has already made a decision based on the wrong number.

## Real example

### The Reports That Were All Off by One Day

Fatima Zahra ran Uurtje, a time-tracking and invoicing tool for consultancies, built in Bolt, with customers across the Netherlands, Spain, and one in Dubai.

The complaint came from the Dubai customer: monthly invoices did not match their own records, consistently by a few hours' work. Entries logged late on the last day of a month appeared in the following month's invoice.

Time entries were stored as timestamps generated in the browser and inserted without conversion, so their meaning depended on where the person had been sitting. Monthly totals were then computed against UTC month boundaries. For a consultant in Dubai, four hours ahead, anything logged after 20:00 on the 31st fell into the next month. For the Spanish customers the same defect existed one hour wide and had been dismissed as rounding.

A second issue surfaced during the review: recurring weekly reminders stored as fixed UTC times had shifted by an hour at the last clock change, and several customers had adjusted their calendars manually rather than reporting it.

**Result:** all timestamps converted and stored in UTC with the originating timezone retained, reporting boundaries computed in each account's configured timezone, calendar dates moved to a date type, recurring schedules stored with their timezone and recomputed per occurrence, and the existing 14 months of entries corrected through a verified backfill.

> "Every invoice we had produced for one customer was wrong by a few hours, for fourteen months, and the product never once showed an error."
> — **Fatima Zahra, Founder, Uurtje**

**Cost & Timeline:** date and timezone audit, correction, and historical backfill delivered in 4 business days.

## Frequently Asked Questions

### Should all timestamps be stored in UTC?

Yes for moments in time, converting only for display. Where the local timezone carries meaning, such as a recurring appointment, store the timezone alongside it so the correct local time survives daylight saving changes.

### Why do monthly reports include the wrong days for some customers?

Because the month boundary is computed in UTC or the server's timezone rather than the customer's. Records created near midnight then fall into the adjacent month for anyone in a different zone.

### What breaks at daylight saving transitions?

Anything that adds 24 hours to get "the same time tomorrow", recurring events stored as fixed UTC times, and scheduled jobs set for the hour that either does not exist or occurs twice.

### Should birth dates and invoice dates be stored as timestamps?

No. Calendar dates should use a date type without a time component. Stored as timestamps they shift by a day when displayed in a different timezone.

### How do I find timezone bugs before customers do?

Change your machine's timezone and use the product, test around month boundaries and near midnight, and exercise recurring behaviour with the clock set to a daylight saving transition.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should all timestamps be stored in UTC?", "acceptedAnswer": { "@type": "Answer", "text": "Yes for moments in time, converting only for display. Where the local timezone carries meaning, such as a recurring appointment, store the timezone alongside it so the local time survives clock changes." } },
    { "@type": "Question", "name": "Why do monthly reports include the wrong days for some customers?", "acceptedAnswer": { "@type": "Answer", "text": "The month boundary is computed in UTC or the server's timezone rather than the customer's, so records created near midnight fall into the adjacent month." } },
    { "@type": "Question", "name": "What breaks at daylight saving transitions?", "acceptedAnswer": { "@type": "Answer", "text": "Anything adding 24 hours to get the same time tomorrow, recurring events stored as fixed UTC times, and jobs scheduled for the hour that does not exist or occurs twice." } },
    { "@type": "Question", "name": "Should birth dates and invoice dates be stored as timestamps?", "acceptedAnswer": { "@type": "Answer", "text": "No. Calendar dates should use a date type without a time component, otherwise they shift by a day when displayed in another timezone." } },
    { "@type": "Question", "name": "How do I find timezone bugs before customers do?", "acceptedAnswer": { "@type": "Answer", "text": "Change your machine's timezone and use the product, test around month boundaries and near midnight, and exercise recurring behaviour with the clock set to a daylight saving transition." } }
  ]
}
</script>
