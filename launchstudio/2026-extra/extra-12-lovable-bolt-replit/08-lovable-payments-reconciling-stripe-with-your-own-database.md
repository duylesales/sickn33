---
Title: "Lovable Payments: Reconciling Stripe With Your Own Database"
Keywords: lovable payments, reconciliation, Stripe payouts, webhook failures, revenue reporting, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Payments: Reconciling Stripe With Your Own Database

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Reconciling Stripe With Your Own Database",
  "description": "Your provider's dashboard and your application will disagree eventually. How to find the gap monthly, why webhooks miss events, and the small job that keeps revenue figures, entitlements and bank statements in step.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-reconciling-stripe-with-your-own-database" }
}
</script>

Three numbers should describe the same month: what your payment provider says it processed, what your database says was paid, and what actually arrived in your bank account. In most AI-built products, nobody has ever compared them.

They will not match, and the interesting part is that the reasons are almost always mundane. A webhook that failed while your app was redeploying. A refund issued in the dashboard at eleven at night. A dispute that reversed a payment your application still considers successful. None of these is dramatic on its own. Together they produce an application whose idea of who has paid drifts steadily away from reality, and the drift is invisible until something forces you to look.

## Why the Gap Opens

Webhooks are not guaranteed the way founders assume. Your endpoint can be down during a deploy, return a 500 because of an unrelated bug, time out under load, or reject an event because a signature check was misconfigured after a key rotation. Providers retry, generously, and then they stop.

Manual actions in the dashboard are the second source. Every refund, cancellation or subscription edit made by a human in the provider's interface is a change your application learns about only through a webhook — which is the same mechanism that just failed.

The third is your own code. An event handler that throws part-way through leaves the provider believing the event was delivered, because it returned a 200 before the work finished, or leaves your database half-updated because there was no transaction around the writes.

And the fourth is time. Disputes, reversed direct debits and delayed settlements arrive days or weeks after the original payment, long after anyone is watching that customer.

## The Monthly Job That Finds It

Reconciliation sounds like an accounting function. Practically it is a query you run once a month and a short list you read.

Pull every charge, refund and dispute the provider recorded in the period. Pull the same from your database. Compare on the provider's reference, which is why every payment row in your application must store it. Then look at three lists.

**In the provider, not in your database.** Someone paid and your application does not know. This is the one that costs you a customer, because they have paid for access they do not have.

**In your database, not at the provider.** Usually a record created optimistically before confirmation — a pending payment that never completed but was written as though it had.

**In both, but different.** Different amount, different status, refunded on one side only. These are the ones that quietly corrupt revenue figures.

For a product doing a few hundred transactions a month this runs in seconds and the output is normally empty. The value is entirely in the months where it is not.

## Reconcile Against the Bank as Well

Provider and database agreeing is not the end of it, because what reaches your bank is the provider's payout — a batched amount, arriving days later, net of fees, refunds and sometimes disputes from a different period.

Founders trying to match individual payments to bank lines find it impossible and conclude that reconciliation is beyond a small company. The correct unit is the payout: each bank deposit corresponds to one payout report listing exactly which transactions it contains and what was deducted.

Store payout records too, with their transactions linked. Then a deposit of €4,182.47 is explainable in one query rather than an afternoon, and your accountant stops asking.

## Make the Webhook Handler Recoverable

Some of this is prevented rather than detected, and the fixes are small.

Record the event before processing it. Write the raw event and its identifier to a table first, then do the work, then mark it handled. An event that arrives twice is recognised; an event that fails mid-processing is visible as unhandled rather than lost.

Return success quickly and process asynchronously where you can, so a slow database write does not turn into a timeout the provider records as a failure.

Wrap the database changes in a transaction, so a failure leaves nothing half-applied.

And keep the failures somewhere you will see them. An unhandled events list with three rows in it is a five-minute fix; the same list discovered a year later is a reconstruction project.

## Backfilling What Was Missed

When reconciliation finds a gap, resist the temptation to correct it by hand in the database.

Every provider lets you retrieve historical events and replay them into your endpoint. Because your handler is idempotent — it is, isn't it — replaying is safe: events already processed are recognised and skipped, missing ones are applied through exactly the same code path that would have run originally.

This matters because hand-written corrections do not run your business logic. An access grant made with an UPDATE statement skips the email, the audit record and the entitlement calculation, so the row looks right and the customer still cannot use the feature.

## The Reports That Should Agree

Once reconciliation exists, three numbers become trustworthy, and it is worth naming them because founders frequently quote a figure from whichever source is nearest.

Recognised revenue, from your own invoices and credit notes, is the figure for your accountant. Cash received, from payouts, is the figure for your bank balance and your runway. Active subscription value, from your database, is the figure for how the business is doing right now.

They are different numbers legitimately — an annual plan paid in January is cash in January and revenue across twelve months. What reconciliation gives you is confidence that the differences are the real ones rather than accumulated errors.

## Do This Before You Need an Investor

There is a version of this article that only matters when something goes wrong. There is another version that matters when something goes right.

Any serious diligence — an investor, an acquirer, a bank, a larger customer's procurement team — will ask for revenue figures and then test whether your systems produce them consistently. A founder who can show that provider, application and bank agree every month, with the reconciliation output to prove it, answers the question in one exchange. A founder who cannot spends three weeks reconstructing two years of history under time pressure, and every discrepancy found becomes a question about everything else.

The work is the same in both cases. Only the circumstances differ.

## Test Clocks and the Failures You Cannot Wait For

The uncomfortable thing about billing bugs is that most of them only appear on a date in the future. A renewal that fails, a trial that converts, an annual plan that comes round again — you cannot reasonably wait eleven months to find out whether your code handles it.

Providers solve this with test clocks: a simulated time in the sandbox that you advance deliberately. Create a subscription, move the clock forward a month, and watch what your application does with the renewal. Move it again with a card configured to fail, and watch the past-due path. Advance it through the whole retry schedule and see whether access actually ends.

An afternoon with a test clock exercises a year of billing behaviour, and it routinely finds three things: a renewal that creates a duplicate invoice, a past-due state that never resolves because the recovery event is unhandled, and an annual plan that renews at the price stored at signup rather than the current one.

Do it once before launch and again after any change to billing code. It is the only realistic way to know that the parts of your system which run unattended will still be correct in six months, when nobody is watching them run.

## Keep a Record of Every Reconciliation

Run the check, then write down that you ran it and what it found — a dated line in a file, or a row in a table. Three words when it is clean.

This costs nothing and does two things. It proves the routine is actually happening, which matters when the person running it is you and the month has been busy. And when a discrepancy is eventually found in an old period, the log tells you when it appeared, which narrows the cause from everything you have ever deployed to whatever changed in one particular month.

## Setting This Up

For a product already taking payments this is one to two days: the provider reference stored on every payment record, a reconciliation query producing the three difference lists, payout records with their transactions linked, an event log written before processing with an unhandled-events view, transactional and idempotent handlers, a documented replay procedure for missed events, and the monthly routine written down so it survives being done by somebody else.

LaunchStudio includes reconciliation in payment work rather than treating it as an accounting concern, and under the €49 per month managed arrangement the monthly check runs as part of operations. Behind it is Manifera: eleven years, 160+ projects, and financial systems delivered from Amsterdam, Singapore and Ho Chi Minh City.

[Ask us to run one month's reconciliation on your product](https://launchstudio.eu/en/#contact) — the first one usually finds something.

## Real example

### Seventeen Payments the Application Never Saw

Joost Berkhout built Inschrijfpunt with Lovable: registration and payment handling for running events and cycling tours, used by 22 organisers who charge entry fees of €12 to €45.

His webhook handler worked. It had also been down for eleven minutes during a deploy on a Saturday morning in May, which happened to be the morning registration opened for the largest event of his year.

Seventeen people paid during those eleven minutes. Their money reached the provider and his bank account. His application had no record of them, so they did not appear on the start list, and the organiser found out on race day when seventeen runners arrived with confirmation emails from a payment provider and no bib numbers.

Two business days of work afterwards: the provider reference added to every payment row; a reconciliation query producing the three difference lists, run monthly and after every deploy; payout records stored with their constituent transactions so bank deposits explain themselves; the webhook handler rewritten to record each event before processing, wrapped in a transaction, and made idempotent on the event identifier; an unhandled-events list visible on his admin page; and a replay procedure documented, which was then used to recover the seventeen registrations through the normal code path — issuing the confirmations and start-list entries that had never been created.

**Result:** the seventeen runners were reinstated correctly rather than typed in by hand, and over the following year reconciliation caught four further gaps, all small, all within a month. The organiser renewed.

> *"Eleven minutes of downtime on a Saturday morning, and I found out about it on a Sunday in September with seventeen people standing at a registration desk."*
> — **Joost Berkhout, Founder, Inschrijfpunt (Apeldoorn)**

**Cost & Timeline:** €1,850 (payment references, reconciliation queries, payout records, event logging with idempotent transactional handling, unhandled-events view, replay procedure and recovery) — completed in 2 business days.

## Frequently Asked Questions

### How often should I reconcile?

Monthly as a routine, and after any deploy that touched payments or caused downtime. Monthly catches drift while it is still small; the post-deploy check catches the specific failure that produces the worst gaps.

### Are webhooks not guaranteed to arrive?

They are retried, not guaranteed. A deploy, a timeout, an unrelated 500 or a misconfigured signing secret after a key rotation will each lose events, and after the retry window the provider stops.

### Why not fix a missing payment directly in the database?

Because an UPDATE skips your business logic — the confirmation email, the entitlement calculation, the audit record. Replay the event through your webhook endpoint so the normal code path runs.

### How do I match my bank deposits to payments?

Not individually. Match at the payout level: each deposit corresponds to one payout report listing its transactions and deductions. Store payouts with their transactions linked and every deposit becomes explainable in one query.

### Is this worth it for a product with fifty customers?

The setup is one to two days and the monthly run is minutes. At fifty customers a single missed payment is one percent of your revenue and a lost customer, so yes — and the habit is far easier to establish now than at five hundred.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How often should I reconcile payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Monthly as a routine, plus after any deploy touching payments or causing downtime — that is where the largest gaps come from."
      }
    },
    {
      "@type": "Question",
      "name": "Are webhooks guaranteed to arrive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, they are retried within a window and then abandoned. Deploys, timeouts, unrelated errors and rotated signing secrets all lose events."
      }
    },
    {
      "@type": "Question",
      "name": "Why not fix a missing payment directly in the database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A manual update skips the confirmation email, entitlement logic and audit record. Replay the provider's event so the normal code path runs."
      }
    },
    {
      "@type": "Question",
      "name": "How do I match bank deposits to individual payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You do not. Reconcile at payout level: each deposit maps to one payout report listing its transactions and deductions."
      }
    },
    {
      "@type": "Question",
      "name": "Is reconciliation worth it for a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — one to two days to set up, minutes per month to run, and at fifty customers one missed payment is a meaningful share of revenue."
      }
    }
  ]
}
</script>
