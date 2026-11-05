---
Title: "Preventing Double Bookings in a Booking App"
Keywords: prevent double booking, booking app race condition, postgres exclusion constraint booking, supabase booking system, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Preventing Double Bookings in a Booking App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Preventing Double Bookings in a Booking App",
  "description": "Double bookings are one of the most common and damaging bugs in booking apps built with AI tools. This guide explains why they happen, from race conditions to client-side checks and payment delays, and how to prevent them with database constraints, transactions, temporary holds, idempotent booking creation, capacity handling, time zones and calendar synchronisation.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-05",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/preventing-double-bookings-in-a-booking-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Exclusion constraints", "url": "https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-EXCLUSION" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Range types", "url": "https://www.postgresql.org/docs/current/rangetypes.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Explicit locking", "url": "https://www.postgresql.org/docs/current/explicit-locking.html" },
    { "@type": "CreativeWork", "name": "Stripe: Idempotent requests", "url": "https://docs.stripe.com/api/idempotent_requests" }
  ]
}
</script>

Booking apps are among the most common products founders build with Lovable, Bolt and Cursor: appointments for salons and clinics, rooms and desks, lessons and classes, rental equipment, event slots, consultations. They look simple. Show available times, let someone pick one, save the booking.

They are also home to one of the most damaging bugs in software: the double booking. Two customers book the same massage slot. Two companies reserve the same meeting room. The last place in a class is sold twice. For the business owner, it means an awkward phone call, a refund, sometimes a lost customer. For the founder, it means a support crisis and, often, a business owner who stops trusting the software.

Double bookings rarely appear in testing because they require two people acting at almost the same moment. They appear in production, usually at the worst time: when slots open, during busy periods or after a marketing campaign. This guide explains why they happen and how to prevent them properly.

## Key Takeaways

- **Double bookings are race conditions.** Two requests check availability, both see a free slot and both create a booking.
- **Checks in the browser cannot prevent them.** Only the database, or a single authoritative server process, can enforce availability reliably.
- **Postgres offers strong tools:** unique constraints for fixed slots, exclusion constraints for overlapping time ranges and transactions with row locks for capacity.
- **Payments add a timing problem.** Use temporary holds that expire if payment is not completed.
- **Make booking creation idempotent,** so retries and double clicks do not create duplicates.

## Why Double Bookings Happen

The typical AI-generated booking flow works like this:

1. The frontend loads available slots.
2. The user selects a slot.
3. The frontend checks whether the slot is still free, by querying bookings.
4. If free, the frontend inserts a booking.

Between steps 3 and 4, another user can do exactly the same. Both checks see the slot as free, both inserts succeed, and the slot is booked twice. This is called a race condition, and it is not prevented by checking more carefully, faster or twice. The gap between check and insert always exists.

Other causes:

- **Double clicks and retries** creating two identical bookings from the same user
- **Payment delays,** where a slot is shown as available while another customer is paying for it
- **Time zone errors,** where the same slot is stored with different times
- **Calendar sync delays,** when bookings also come from Google Calendar, Outlook or another system
- **Buffer and duration logic in the frontend only,** so overlapping bookings of different lengths are allowed

## The Principle: Let the Database Decide

Availability must be enforced at the point where bookings are stored, by a rule that cannot be bypassed. In a Supabase app, that means the Postgres database. There are three main tools, depending on the booking model.

## Tool 1: Unique Constraints for Fixed Slots

If bookings are for fixed slots, such as a resource at a specific start time with a fixed duration, a unique constraint is enough:

```sql
alter table bookings
  add constraint bookings_unique_slot unique (resource_id, slot_start);
```

If two requests try to insert a booking for the same resource and start time, one succeeds and the other fails with a constraint violation. The app catches the error and tells the second user the slot was just taken.

Cancellations complicate this slightly: a cancelled booking should not block the slot. A partial unique index handles that:

```sql
create unique index bookings_unique_active_slot
  on bookings (resource_id, slot_start)
  where status in ('confirmed', 'held');
```

## Tool 2: Exclusion Constraints for Overlapping Times

If bookings have variable durations, such as a 30-minute haircut and a 90-minute colouring with the same stylist, unique constraints are not enough, because bookings can overlap without starting at the same time. Postgres exclusion constraints solve this with range types:

```sql
create extension if not exists btree_gist;

alter table bookings
  add column during tstzrange generated always as (tstzrange(starts_at, ends_at, '[)')) stored;

alter table bookings
  add constraint bookings_no_overlap
  exclude using gist (resource_id with =, during with &&)
  where (status in ('confirmed', 'held'));
```

This constraint rejects any new booking for the same resource whose time range overlaps an existing active booking. The `[)` bounds mean a booking ending at 10:00 does not conflict with one starting at 10:00. Buffer times, such as cleaning time between appointments, can be included by extending the stored range.

Exclusion constraints are one of the most underused features in AI-built booking apps, and one of the most effective.

## Tool 3: Transactions and Locks for Capacity

Some bookings are not exclusive but limited: a yoga class with 15 places, a tour with 20 seats, a workshop with 30 tickets. Here, the rule is "no more than N active bookings per session".

A reliable approach uses a database function that runs in a transaction:

1. Lock the session row with `select ... for update`, so concurrent bookings for the same session wait.
2. Count active bookings, or read a capacity counter on the session.
3. If capacity remains, insert the booking and update the counter.
4. Commit.

Because the session row is locked, two concurrent requests cannot both pass the capacity check. Call this function from the frontend through a remote procedure call, rather than inserting bookings directly, and restrict direct inserts with Row Level Security.

## Temporary Holds During Payment

When customers must pay at booking, there is a gap between selecting a slot and completing payment, often a minute or more with iDEAL or card authentication. Without a hold, another customer can book the same slot during that time, and one of them pays for a slot they cannot have.

The solution is a temporary hold:

1. When the customer proceeds to payment, create a booking with status `held` and an expiry time, for example ten minutes.
2. The database constraints treat `held` bookings as occupying the slot.
3. When the payment webhook confirms payment, change the status to `confirmed`.
4. A scheduled job releases holds that expire without payment, setting them to `expired`.
5. If a payment succeeds after the hold expired and the slot was taken, refund automatically and inform the customer.

Show the hold to the customer, for example "We are holding this slot for 10 minutes", so they understand the urgency.

## Idempotent Booking Creation

Double clicks, network retries and impatient refreshes can create duplicate bookings for the same customer. Prevent this by:

- **Generating a booking request ID** in the browser when the booking form opens, and sending it with the request.
- **Storing the request ID with a unique constraint,** so a second request with the same ID returns the existing booking instead of creating a new one.
- **Disabling the submit button** while a request is in progress, as a usability measure, not as the protection.
- **Using idempotency keys with payment providers,** so a retried payment creation does not charge twice.

## Time Zones and Daylight Saving

Booking bugs often come from time handling:

- **Store timestamps with time zones** (`timestamptz`) in UTC.
- **Store the resource's time zone,** such as `Europe/Amsterdam`, and generate slots in that zone.
- **Convert for display** in the user's time zone where relevant, and make clear which zone is shown.
- **Test daylight saving transitions,** when an hour disappears in spring and repeats in autumn. Slots generated with naive arithmetic can appear twice or not at all.

Our article on [timezone and date bugs in AI-built apps](https://launchstudio.eu/en/blog/timezone-and-date-bugs-in-ai-built-apps) covers these pitfalls.

## Calendar Synchronisation

Many businesses also take bookings by phone or manage staff calendars in Google Calendar or Outlook. If your app syncs with external calendars:

- **Treat external events as blocking time** in your availability calculation.
- **Sync frequently** and use push notifications from calendar providers where possible.
- **Accept that external calendars are not transactional.** A booking in your app and an event created simultaneously in Google Calendar can conflict. Detect conflicts after sync and alert staff.
- **Write bookings back** to the external calendar so staff see them in their usual tools.

## Showing Availability

Preventing double bookings is about writes; the availability display is about reads. Keep them consistent:

- **Calculate availability on the server,** using the same rules as the constraints, including buffers and holds.
- **Refresh availability** when the user selects a slot or returns to the page.
- **Handle conflicts gracefully:** when a booking fails because the slot was taken, show nearby alternatives immediately rather than a generic error.

## Rescheduling and Cancellations

Rescheduling is where many booking systems reintroduce double bookings. A naive reschedule deletes the old booking and creates a new one in two steps, or updates the time without checking the new slot. Handle it in one database operation: update the booking's time inside a transaction, letting the same exclusion or unique constraint validate the new slot. If the new slot is taken, the update fails and the original booking stays intact.

For cancellations, change the status rather than deleting the row, so the history remains available for reporting, refunds and disputes, and the constraints stop counting the booking. If your business offers waiting lists, a cancellation can trigger an offer to the next person in line, again using a hold so the slot is not given to two waiting customers at once.

## Testing for Race Conditions

Race conditions do not appear when one person clicks through the app. Test them deliberately:

- **Concurrent requests:** send dozens of booking requests for the same slot at the same moment, using a load testing tool or a small script, and confirm exactly one succeeds.
- **Capacity tests:** send more requests than places for a class and confirm the count never exceeds capacity.
- **Payment timing:** simulate a payment confirmed after the hold expired.
- **Daylight saving dates:** generate and book slots across transition weekends.

## How LaunchStudio Helps

LaunchStudio makes booking apps reliable: moving availability enforcement into the database with unique or exclusion constraints, building booking functions with transactions for capacity, implementing temporary holds tied to payment webhooks, idempotent booking creation, time zone handling, calendar sync conflict detection and concurrency tests.

The **Launch Ready** package (€800-€3,500) covers booking reliability fixes along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds payments with holds, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with extensive experience in transactional systems where consistency is critical. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Massage Studio Where Saturday Slots Were Sold Twice

Eva Hendriks built Behandelagenda with Lovable and Supabase: an online booking system for wellness studios and massage practices, with treatments of different lengths, therapists with their own schedules and payment at booking via iDEAL. Studios liked it, until Saturdays. On popular days, studios started finding two clients booked with the same therapist at overlapping times, sometimes three or four times a weekend.

The cause was the classic pattern. Availability was checked in the browser by querying existing bookings, then a new booking was inserted directly. A 60-minute booking at 10:00 and a 90-minute booking at 10:30 for the same therapist were both accepted because the check only compared start times. During the iDEAL payment, which took one to two minutes, the slot appeared free to others. Double clicks on the pay button occasionally created two bookings and two payments, and slots generated around the end of October appeared twice because of daylight saving.

LaunchStudio added an exclusion constraint on therapist and time range, including a configurable buffer between treatments, so overlapping active bookings became impossible at the database level. Booking creation moved into a database function called from the frontend, with direct inserts blocked by Row Level Security. Bookings entered a `held` state for ten minutes during payment, confirmed by the Mollie webhook and released by a scheduled job, with automatic refunds for the rare late payments. Booking requests received client-generated IDs to prevent duplicates, slots were generated in each studio's time zone with tests covering daylight saving, and failed bookings showed the next available times.

**Result:** In the three months after the change, the studios processed around 7,800 bookings with no double bookings. Concurrency tests firing fifty simultaneous requests at one slot consistently produced exactly one booking.

> *"My studios were apologising to clients every Saturday. Now the database simply refuses the second booking, and nobody has to apologise."*
> - **Eva Hendriks, Founder, Behandelagenda ('s-Hertogenbosch)**

**Cost & Timeline:** €3,600 (Launch Ready package: exclusion constraints, booking function, payment holds, idempotency, time zone fixes and concurrency tests) - completed in 10 business days.

## Frequently Asked Questions

### Why does my booking app allow double bookings?

Usually because availability is checked in the browser or in separate steps before inserting a booking. Two users can pass the check at the same time. Enforcing availability in the database, with constraints or transactional functions, prevents this.

### What is an exclusion constraint?

A Postgres constraint that prevents rows from conflicting according to a rule, such as two bookings for the same resource with overlapping time ranges. Combined with range types, it is the most reliable way to prevent overlapping bookings of different lengths.

### How do I stop a slot from being taken while a customer is paying?

Create a temporary hold when the customer starts payment, treat it as occupying the slot, confirm it when the payment webhook arrives and release it automatically if payment is not completed within a set time.

### How does Manifera's experience help with booking systems?

Manifera has built transactional systems for enterprise clients for 11+ years, where consistency under concurrent use is essential. LaunchStudio applies that experience to booking apps, using database-level guarantees rather than hoping two users never click at the same moment.

### Do reliable bookings affect my app's visibility?

Indirectly. Businesses that trust your booking system recommend it, and their customers leave fewer complaints. Positive reviews and case studies are the kind of signals that search engines and AI answer engines draw on when recommending booking tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my booking app allow double bookings?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually availability is checked in the browser before inserting, so two users pass simultaneously. Enforce availability in the database." }
    },
    {
      "@type": "Question",
      "name": "What is an exclusion constraint?",
      "acceptedAnswer": { "@type": "Answer", "text": "A Postgres constraint preventing conflicting rows, such as overlapping time ranges for the same resource, ideal for variable-length bookings." }
    },
    {
      "@type": "Question",
      "name": "How do I stop a slot from being taken while a customer is paying?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use a temporary hold that occupies the slot, confirmed by the payment webhook and released automatically if unpaid." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with booking systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise transactional systems for 11+ years, and LaunchStudio applies database-level guarantees to booking apps." }
    },
    {
      "@type": "Question",
      "name": "Do reliable bookings affect my app's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, through recommendations, fewer complaints and positive reviews that search and AI engines draw on." }
    }
  ]
}
</script>
