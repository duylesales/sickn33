---
Title: "Lovable Supabase Concurrency: When Two People Edit One Record"
Keywords: Lovable, lost update problem, optimistic concurrency version column, idempotency double submit, database constraint race condition, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase Concurrency: When Two People Edit One Record

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase Concurrency: When Two People Edit One Record",
  "description": "Lost updates, double submissions and races on limited resources are invisible during development and routine in production. What each looks like, where the fix belongs, and how to test for them without special tooling.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/two-people-editing-the-same-record" }
}
</script>

A planner opens a job record at 10:14 and starts updating the address. Her colleague opens the same record at 10:15, corrects the phone number, and saves at 10:17. She saves at 10:19. The phone number correction is gone, nobody is told, and the customer is called on the old number a week later.

Nothing errored. Both saves succeeded. The database did exactly what it was asked to do, which was to take the entire form contents from whoever submitted last and write them over whatever was there.

This is the lost update problem, and it is one of three concurrency failures that AI-generated applications produce by default — invisible in development, ordinary in production, and impossible to find by reading the code.

## Why None of This Appears in Testing

You test alone. You click once, wait for the result, and click again. Every operation completes before the next begins, so the interleavings that cause these bugs cannot occur.

Production reverses that: several people, several tabs, mobile connections that make a user press a button twice because nothing appeared to happen, and background jobs running while someone edits. The code is identical; the timing is not, and timing is where the failure lives.

## Failure One: The Lost Update

The scenario above. Two users load the same record, both edit, both save, and the second save silently overwrites the first — including fields the second person never looked at, because the form submits everything it loaded.

**The cheapest reliable fix is optimistic concurrency.** Add a version number or updated-timestamp column to the record. When a user loads the form, they receive the current version; when they save, the update applies only if the version still matches. If someone else saved in between, the write affects no rows and your application can tell the user that the record changed and show them what is different.

This is a small schema change and a modest amount of application logic, and it converts a silent data loss into a visible, explainable message.

**The alternative, field-level updates,** sends only what changed rather than the whole form. It reduces collisions to the same field rather than the same record, and it is more work in the interface. For most small products, versioning is the better first move.

## Failure Two: The Double Submission

A user taps "confirm" on a train, the connection stalls, nothing appears to happen, and they tap again. Two identical requests arrive. Two bookings are created, or one payment is taken twice, or two invitation emails are sent.

Disabling the button after the first click is a courtesy, not a protection: the second request may already be in flight, and a determined or unlucky user bypasses it entirely.

**The fix is idempotency:** the client generates a unique key for the operation, sends it with the request, and the server records it. A second request carrying the same key returns the original result rather than performing the action again. Payment providers work this way for exactly this reason, and the same pattern belongs on any operation that creates something or moves money.

For simpler cases, a uniqueness constraint in the database achieves much of it — one booking per user per slot, enforced where it cannot be bypassed.

## Failure Three: The Race on a Limited Resource

Ten seats, ten tickets sold, two people clicking at the same moment, eleven tickets issued.

The generated code reads correctly: check availability, then create the booking. At runtime both checks execute before either write, both see a free seat, and both proceed. No amount of reading that function reveals the problem, because the problem is in the gap between two statements.

**The fix belongs in the database, not in your application logic.** Either perform the check and the write as a single atomic operation — a conditional update that decrements only if capacity remains — or wrap both in a transaction with appropriate locking, or express the rule as a constraint the database enforces regardless of timing.

The principle worth internalising: if correctness depends on two operations not being interleaved, application code cannot guarantee it. The database can.

## Where the Check Has to Live

This is the recurring theme. Checks in the browser protect nothing. Checks in application code protect against sequential mistakes and not against simultaneous ones. Only a constraint or an atomic operation in the database holds under concurrency, because the database is the single point through which all requests pass.

For a founder without a database background, the practical translation is: any rule where "two at once would be wrong" needs to exist as a constraint, not only as a validation. Unique bookings per slot. Stock that cannot go negative. One active subscription per account. A referral code that can only be redeemed once.

## What to Tell the User

Concurrency handling produces situations where a user's action is refused, and the message matters.

"This record was changed by someone else while you were editing. Here is what changed — would you like to reload or overwrite?" is a good message: it explains, it shows, and it offers a choice.

"Error: version mismatch" is the same protection presented as a malfunction, and it will generate support email.

Where possible, avoid the conflict rather than reporting it: show who else has the record open, or auto-save drafts so nothing is lost when a conflict does occur.

## Testing Without Tooling

Every one of these is reproducible by hand in ten minutes.

**Lost update:** open the same record in two browsers, edit different fields, save the second one first. Check whether the first save overwrites it.

**Double submission:** open your browser's network tools, throttle the connection heavily, then submit a form and click again while it is pending.

**Limited resource:** set capacity to one and have two browsers submit at the same moment. Two people helps; two tabs and fast fingers usually suffice.

Do this for every feature where the answer matters commercially. It is the highest-value hour of manual testing available to a small product, and it finds bugs no code review will.

## Which Features Actually Need This

Not everything. Applying heavy concurrency control everywhere makes a product slow and complicated for no benefit.

The features that need it share one property: two simultaneous actions would produce a wrong answer that someone would notice. Bookings against capacity. Stock. Balances and credits. Anything where a record is edited by more than one person. Payment and subscription state. Invitation and code redemption.

The features that do not: a personal profile only its owner edits, a draft nobody else can see, a log that only ever appends.

## Getting This Built Correctly

Concurrency is the clearest example of something that cannot be fixed by reading code more carefully, and that a database will handle correctly once someone expresses the rule where it belongs. LaunchStudio does this as part of taking an AI-built product to production: identifying which operations are commercially sensitive to timing, adding versioning where records are shared, implementing idempotency on creation and payment paths, moving capacity and uniqueness rules into database constraints, and writing the tests that simulate simultaneous requests so a future change cannot reintroduce it.

The interface you built in Lovable, Bolt or Cursor stays as it is, and the codebase remains documented and AI-readable. It is part of the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's engineers from Amsterdam and Ho Chi Minh City, with eleven years of production experience behind them for clients including Vodafone, TNO and CFLW.

If your product sells something with limited availability, [describe your project](https://launchstudio.eu/en/#contact) and we will tell you where it is exposed, usually within one business day.

## Optimistic or Pessimistic: Which to Reach For

There are two broad strategies, and choosing between them is simpler than the terminology suggests.

**Optimistic** assumes conflicts are rare. Everyone can start editing; the conflict is detected at save time and reported. This is what the version column approach does, and it is right for records that are occasionally edited by more than one person — a customer record, a job description, a product listing. The cost is that a user can lose work at the moment of saving, which is why showing them what changed matters.

**Pessimistic** prevents the conflict by locking: while one person is editing, others cannot. It suits records that are edited for long periods and where losing work would be severe — a detailed form, a long document. The cost is that locks must expire, or a user who closes their laptop blocks a record indefinitely, and you need a way to see and break a stale lock.

For most small products, optimistic is the correct default, with one addition worth the small effort: show presence. Displaying "Jan is also viewing this record" prevents a large share of conflicts before they occur, and it is a fraction of the work of a locking system.

Whichever you choose, do not mix them arbitrarily. A product where some screens lock and others silently overwrite teaches users that the rules are unpredictable, which is worse than either strategy applied consistently.

## Real example

### A Workshop Platform That Sold Fourteen Places in a Room for Twelve

Marloes Huisman built Ambachtsklas in Lovable: a platform selling places on craft workshops run by independent makers across Utrecht and Amersfoort. Workshops have a fixed capacity, and places sell out.

The problem appeared on a Saturday morning release of a popular pottery course. Twelve places; fourteen bookings; two participants arriving to a room with no seat. The maker refunded them and Marloes lost the relationship.

Reading the booking function showed nothing wrong: it counted existing bookings, compared with capacity, and inserted a row. Under a burst of simultaneous requests, several counts ran before any insert.

Five business days of work: capacity enforced as an atomic conditional update so a booking can only be created while remaining places are above zero; a uniqueness constraint preventing the same person booking the same workshop twice; idempotency keys on the booking and payment path so a double-tap on a slow connection cannot create two bookings; optimistic versioning on the workshop record, since makers frequently edit details while bookings arrive; user-facing messages explaining a full workshop or a changed record; and a load test simulating fifty simultaneous bookings, now part of every deploy.

**Result:** the same maker ran a sold-out series of six workshops two months later with no overbooking, and the load test has failed once — catching a regression introduced while adding a waiting list feature.

> *"I read that function twenty times looking for the bug. The bug was that two people clicked at the same moment, which is not something you can see in the code."*
> — **Marloes Huisman, Founder, Ambachtsklas (Utrecht)**

**Cost & Timeline:** €2,500 (atomic capacity handling, idempotency, versioning, concurrency tests in the pipeline) — completed in 5 business days.

## Frequently Asked Questions

### Why did my booking system oversell when the code checks availability?

Because the check and the write are two separate operations. Under simultaneous requests, several checks run before any write, and all of them see capacity available. The rule has to be enforced atomically in the database rather than in application logic.

### What is the simplest fix for two people overwriting each other's edits?

Optimistic concurrency: a version column on the record, returned when the form loads and required to match on save. If someone else saved in between, the update affects no rows and you can show the user what changed.

### Is disabling the submit button enough to prevent double submissions?

No. The second request may already be in flight, and the protection is trivially bypassed. Use an idempotency key so a repeated request returns the original result, or a database uniqueness constraint where one applies.

### Do I need this everywhere in my app?

No. It matters where two simultaneous actions would produce a wrong answer someone notices: capacity, stock, balances, shared records, payment state and redeemable codes. Personal drafts and append-only logs do not need it.

### How do I test for these without special tools?

By hand: two browsers editing the same record and saving in reverse order, a throttled connection with a double-clicked submit, and two tabs booking the last available place simultaneously. Ten minutes finds what code review cannot.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did my booking system oversell when the code checks availability?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The check and the write are separate operations, so under simultaneous requests several checks run before any write. The rule must be enforced atomically in the database."
      }
    },
    {
      "@type": "Question",
      "name": "What is the simplest fix for two people overwriting each other's edits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Optimistic concurrency — a version column returned on load and required to match on save, so a conflicting update affects no rows and can be reported."
      }
    },
    {
      "@type": "Question",
      "name": "Is disabling the submit button enough to prevent double submissions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Use an idempotency key so a repeated request returns the original result, or a database uniqueness constraint."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need this everywhere in my app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — only where simultaneous actions would produce a noticeably wrong answer: capacity, stock, balances, shared records, payment state and redeemable codes."
      }
    },
    {
      "@type": "Question",
      "name": "How do I test for these without special tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two browsers saving the same record in reverse order, a throttled connection with a double-clicked submit, and two tabs taking the last place simultaneously."
      }
    }
  ]
}
</script>
