---
Title: "Duplicate Records and the Cleanup You Will Eventually Need"
Keywords: duplicate records SaaS, preventing duplicate entries database, merge duplicate customers, unique constraint email, double submit form, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Duplicate Records and the Cleanup You Will Eventually Need

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Duplicate Records and the Cleanup You Will Eventually Need",
  "description": "Duplicates arrive from double-clicked buttons, retried requests, imports, and the same person spelled two ways. Why a database constraint is the only prevention that works, when to merge rather than block, and how duplicates quietly corrupt every number you report.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/duplicate-records-and-the-cleanup-you-will-eventually-need" }
}
</script>

Duplicates are the least dramatic data problem and one of the most corrosive. Nothing crashes. No error appears. Your customer simply has two records for the same client, sends two invoices, sees an inflated total, and slowly loses confidence in the numbers your product shows them. By the time anyone investigates, the duplicates are months old, referenced by other records, and cannot be removed by deleting one of each pair.

They arrive from more directions than founders expect, and only one form of prevention actually holds. Understanding which is the difference between a product that stays clean and one that requires a cleanup project every quarter.

## The Five Sources, in Order of Frequency

**A button pressed twice.** Someone clicks Save, nothing visibly happens for a second on a slow connection, they click again. Two records. This is the most common source by a wide margin, and it is entirely predictable.

**A retried request.** A request times out from the browser's perspective but succeeds on the server. The browser, or the customer, retries. The server processes it twice, unaware the first attempt landed.

**Imports.** A file imported twice, usually because the first attempt appeared to fail, or a file containing rows that already exist in the account.

**The same thing entered two ways.** "Jansen BV", "Jansen B.V.", "jansen bv". Three records, one company, no technical fault at all — and the hardest kind to prevent without irritating people.

**Two people acting at once.** Two team members creating the same client in the same minute, each unaware of the other. Rare in a two-person team, routine in a ten-person one.

Each has a different remedy, and the mistake is trying to solve all five with one mechanism — usually a check in the application that reads before writing, which is the mechanism that reliably fails under exactly the conditions that produce duplicates.

## Why the Application-Level Check Does Not Hold

The natural implementation is: look for an existing record with this email; if none, create one. It reads correctly and it is wrong under concurrency.

Two requests arriving milliseconds apart both perform the lookup before either has written. Both find nothing. Both create. You now have two records, produced by code that explicitly checks for duplicates.

Under ordinary use this happens rarely enough to look like it works. Under the exact conditions that generate duplicates — a double-clicked button firing two requests, an automatic retry, an import running in parallel — it happens constantly. And the check is doubly ineffective in AI-generated products, where it typically lives in the frontend, which means it does not run at all for anything reaching the server another way.

The only prevention that holds is a **unique constraint in the database**. The database is the single place where two simultaneous writes are genuinely serialised; it will accept the first and reject the second, regardless of how the requests arrived or how many application instances are running. Everything else is a usability improvement layered on top of that guarantee.

This is why "add a check for duplicates" is not the right instruction. The right instruction is "add a unique constraint on this column, and handle the rejection gracefully" — and the second half matters, because a constraint violation surfaced to the customer as a raw database error is its own failure.

## Deciding What Uniqueness Means

Before adding a constraint you have to answer a question that is sometimes uncomfortable: what makes two records the same?

For user accounts, email is usually the answer, with a wrinkle: `Anna@example.com` and `anna@example.com` are the same mailbox, so store and compare a normalised form, or the constraint permits the exact duplicate it was meant to prevent.

For business records the answer is rarely a single field. Two clients with the same name may be genuinely different companies; two invoices with the same amount and date are usually distinct. A combination — customer plus invoice number, or organisation plus email — is often the honest key, and it may not be unique globally but unique *within an account*, which is a different constraint and the one most multi-tenant products actually need.

For some records, nothing should be enforced. Two identical time entries on the same day may be perfectly legitimate. Forcing uniqueness where duplicates are valid produces a product that refuses correct data, which customers find considerably more annoying than an occasional duplicate.

## Prevent, Warn, and Merge: Three Different Answers

Not every duplicate should be blocked, and matching the response to the case is what makes this feel considerate rather than obstructive.

**Prevent** where sameness is unambiguous and enforceable: one account per email, one invoice per number per customer. Constraint in the database, clear message in the interface.

**Warn** where sameness is likely but uncertain. When someone creates "Jansen B.V." and "Jansen BV" already exists, the right behaviour is not rejection — it is "a similar client already exists: [Jansen BV]. Use that one, or create a new record?" This catches the largest category, the near-duplicate, without ever refusing legitimate data.

**Merge** for what gets through anyway, and something always does. A merge function needs to combine two records, keep the fuller information, and — the part that makes it real work — repoint everything referencing the discarded record: invoices, notes, history, attachments. A merge that deletes one record and leaves twelve invoices pointing at nothing is worse than the duplicate was.

On the interface side, two cheap measures remove most double-submissions: disable the submit button immediately on click and keep it disabled until the request resolves, and give each submission an identifier the server can recognise so a retry of the same submission is ignored rather than processed again. Neither replaces the constraint; both prevent the customer from ever seeing the constraint do its job.

Adding unique constraints to a live database, cleaning existing duplicates, and building a merge that repoints references correctly is a well-defined piece of engineering with a sharp edge: the constraint cannot be added until the existing duplicates are resolved. LaunchStudio, backed by Manifera's 11+ years of production engineering, does this as part of preparing AI-built products for real use. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## The Damage Runs Through Your Numbers

The visible cost of duplicates is minor irritation. The real cost is that every aggregate becomes unreliable.

Customer counts inflate. Revenue per customer deflates, because the same revenue is spread across two records. Usage limits are evaded, since each duplicate carries its own allowance. Churn calculations distort, as one departing customer registers as two. Email sends double, which affects both your costs and your sending reputation. And segmentation quietly breaks: a customer with two records may appear in a "never activated" list because one of the two never was.

This is why duplicates are worth addressing before the numbers start informing decisions rather than after. Founders who discover a duplicate problem after eight months typically also discover that eight months of reporting was wrong, and that the correction changes what they thought they knew about their own business.

## Real example

### One Company, Four Records, and an Invoice Sent Twice

Marijke Sanders launched Offertepro, a quoting tool for construction subcontractors, built in Bolt. Clients were created through a form with a check that looked for an existing client with the same name before inserting.

Nine months in, a customer complained that they had sent the same quote to a client twice, at different prices, from two records that both appeared in search. The review found 1,847 client records covering roughly 1,100 real companies. Around 60% of the duplicates came from double-submitted forms on mobile connections — the check ran in the browser and two requests reached the server before either finished. The rest came from imports and from name variations the exact-match check never caught.

Because clients were referenced by quotes, invoices, and notes, no duplicate could simply be deleted. Several companies had their history split across three or four records, so no single one showed a complete picture — which is how the same client received two different quotes for the same job.

**Result:** normalised email plus account-scoped unique constraints in the database, submit-button and request-level protection against double submission, fuzzy warning on similar names at creation, and a merge function repointing quotes, invoices, notes, and attachments. The existing duplicates were merged over two days with a report for the customer to review before anything was applied.

> "My product had been telling me I had 1,847 clients. I had about 1,100, and I had been making decisions with the bigger number for most of a year."
> — **Marijke Sanders, Founder, Offertepro**

**Cost & Timeline:** deduplication, constraints, and merge tooling delivered in 4 business days.

## Frequently Asked Questions

### Why do duplicates appear even though my code checks for them?

Because a check that reads before writing does not hold when two requests arrive at once: both read, both find nothing, both write. Only a unique constraint in the database serialises simultaneous writes reliably.

### Should duplicates be blocked or just flagged?

Block where sameness is unambiguous, such as one account per email. Warn where it is likely but uncertain, such as similar company names, since refusing legitimate data annoys customers more than an occasional duplicate.

### What makes merging duplicates difficult?

Everything referencing the discarded record — invoices, notes, attachments, history — must be repointed to the surviving one. A merge that deletes a record and leaves references pointing nowhere causes more damage than the duplicate.

### How do double-clicked buttons create duplicate records?

A slow response leaves no visible feedback, the customer clicks again, and two identical requests reach the server. Disabling the button until the request resolves and giving each submission an identifier the server can recognise prevents most of it.

### Do duplicates affect anything besides tidiness?

They distort every aggregate: customer counts, revenue per customer, usage limits, churn, and segmentation. Products that discover a duplicate problem late usually find their reporting has been wrong for months.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do duplicates appear even though my code checks for them?", "acceptedAnswer": { "@type": "Answer", "text": "A check that reads before writing fails when two requests arrive at once: both read, both find nothing, both write. Only a database unique constraint serialises simultaneous writes reliably." } },
    { "@type": "Question", "name": "Should duplicates be blocked or just flagged?", "acceptedAnswer": { "@type": "Answer", "text": "Block where sameness is unambiguous, such as one account per email. Warn where it is likely but uncertain, such as similar company names, since refusing legitimate data annoys customers more." } },
    { "@type": "Question", "name": "What makes merging duplicates difficult?", "acceptedAnswer": { "@type": "Answer", "text": "Everything referencing the discarded record must be repointed to the survivor. A merge that leaves invoices or notes pointing nowhere causes more damage than the duplicate did." } },
    { "@type": "Question", "name": "How do double-clicked buttons create duplicate records?", "acceptedAnswer": { "@type": "Answer", "text": "A slow response gives no feedback, the customer clicks again, and two identical requests reach the server. Disabling the button until the request resolves and identifying each submission prevents most cases." } },
    { "@type": "Question", "name": "Do duplicates affect anything besides tidiness?", "acceptedAnswer": { "@type": "Answer", "text": "They distort customer counts, revenue per customer, usage limits, churn, and segmentation. Late discovery usually means months of incorrect reporting." } }
  ]
}
</script>
