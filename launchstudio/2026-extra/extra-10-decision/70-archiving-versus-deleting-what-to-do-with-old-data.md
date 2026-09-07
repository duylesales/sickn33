---
Title: "Archiving Versus Deleting: What to Do With Old Data"
Keywords: soft delete vs hard delete, data retention policy SaaS, archive old records, GDPR storage limitation, purging old data safely, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Archiving Versus Deleting: What to Do With Old Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Archiving Versus Deleting: What to Do With Old Data",
  "description": "Keeping everything forever is a liability and deleting eagerly loses data customers expect to have. How to decide a retention policy per data type, why soft deletion is the right default, and the legal obligations pulling in both directions.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/archiving-versus-deleting-what-to-do-with-old-data" }
}
</script>

The default retention policy of every early-stage product is to keep everything forever, and it is a default rather than a decision — nobody chose it, it is simply what happens when deletion is never implemented. For the first year it costs nothing visible. Then the consequences arrive from three directions at once: a database large enough to be slow and expensive, a GDPR principle that says personal data should not be kept longer than necessary, and a breach exposure that includes every record you have ever held, including customers who left two years ago.

The opposite error is equally real. Deleting eagerly loses information customers assumed was permanent, breaks historical reporting, and occasionally destroys records you are legally obliged to keep. The answer is neither extreme; it is a small set of stated rules, decided per data type and written down where customers can read them.

## Three Different Operations, Frequently Confused

Precision here prevents most of the mistakes.

**Archiving** means removing something from everyday view while keeping it fully intact and recoverable. The customer's decision, usually about clutter — a finished project, a former client. Nothing is lost.

**Soft deletion** means marking a record as deleted so it disappears from the product but remains in the database for a defined period. Usually invisible to the customer, who believes it is gone, and it exists so that mistakes are recoverable.

**Hard deletion** means the data is actually removed and cannot be recovered without a backup restore. Irreversible, and the only thing that satisfies an erasure request.

Products routinely present one and perform another, in both directions: a "delete" that archives, leaving customers who requested erasure with their data intact, or an "archive" that removes rows permanently. Whatever the label says should be what happens, and the customer should be able to tell which.

## Soft Deletion as the Default

For nearly every customer-facing record, the sensible default is that "delete" performs a soft deletion with a defined recovery window, followed by a real removal.

The benefit is concrete: the most common data-loss event in a small product is a customer deleting something they did not mean to. With soft deletion, that is a two-minute recovery. Without it, the options are a backup restore that discards everyone else's recent work, or telling the customer the data is gone.

The costs are worth being honest about. Every query must exclude deleted records, and forgetting that filter in one place means deleted records reappear somewhere — a real and common bug. Unique constraints interact awkwardly, since a deleted record still occupies an email address unless the constraint accounts for it. And the deleted rows still occupy space and still contain personal data, which means the purge step is not optional. Soft deletion without an eventual hard deletion is not a retention policy; it is an accumulation policy with better manners.

Retrofitting this later is significantly harder than including it from the start, because it touches every query in the product. It is one of the clearest examples of a decision that costs a day before launch and a week afterwards.

## Deciding a Retention Period Per Data Type

One policy for everything is wrong, because different data has different value and different obligations. A workable set of categories:

**Records the customer created and considers theirs** — projects, documents, clients. Retained while the account is active; on cancellation, retained for a stated period, then removed. This is the group where being generous is cheap and reassuring.

**Financial records** — invoices, payments, credit notes. Retained for the period your tax law requires, which in the Netherlands is generally seven years and elsewhere commonly five to ten. This obligation overrides a customer's deletion request for the records themselves, and saying so plainly is both correct and expected.

**Operational data** — logs, sessions, analytics events. Short retention, typically 30 to 90 days. This is the largest volume and the least valuable, and it is where most storage growth hides.

**Audit trail** — longer, one to three years, because its purpose is answering questions about the past.

**Anything highly sensitive** — health information, identity documents, payment details you should probably not be storing at all. Shortest retention that serves the purpose, and the strongest argument for not keeping it.

Write these down in a single short document, publish the customer-facing parts in your privacy policy, and — this is the part that gets skipped — implement them. A stated policy you do not actually enforce is worse than none, because it is a documented commitment you are visibly failing.

## The Legal Pull in Both Directions

Two obligations point opposite ways, and both are real.

GDPR's storage limitation principle says personal data should be kept no longer than necessary for the purpose it was collected for. There is no fixed number; the requirement is that you have decided a period, can justify it, and adhere to it. "We keep everything indefinitely because deleting is effort" does not qualify.

Meanwhile, tax and commercial law require that invoices and transaction records be retained for years, and employment or sector-specific rules may add more. So an erasure request from a customer does not mean deleting their invoices. It means removing personal data that is not subject to a retention obligation, and retaining what the law requires — often with the personal elements reduced to the minimum the obligation needs.

The practical resolution is per-field rather than per-record: when a customer is erased, their name, contact details, and content are removed, while the invoice record retains the amounts, dates, and the minimum identifying information the tax authority expects. This is more work than deleting a row, and it is what a compliant implementation looks like. Building erasure and retention that satisfy both obligations without leaving orphaned records is a well-defined piece of engineering. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements retention, purge jobs, and erasure paths that hold up to scrutiny. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Making Deletion Actually Happen

A retention policy is only real if something enforces it, which means a scheduled job that removes expired data, and that job is where the remaining risk lives.

It must be **scoped precisely**, because a purge job with a wrong condition is the most destructive piece of code in your product — it runs unattended, on a schedule, against everything. Test it against a restored copy of production before it ever runs live, and have it report what it would delete before it deletes anything.

It must be **complete**, reaching file storage, search indexes, caches, and any third-party tool holding a copy. Deleting the database row while the uploaded document remains in storage satisfies nothing.

It must be **observable**: a record of what ran, how much it removed, and whether it succeeded. Silent failure is the norm for scheduled work, and a purge job that has been failing for four months leaves you both non-compliant and unaware.

And it must be **rate-limited**, since deleting a large volume in one burst can slow the product for everyone. Removing expired data in modest batches over time is both safer and kinder to your database.

## Real example

### Four Years of Data Nobody Had Decided to Keep

Hugo Willemsen ran Bezorgd, a delivery-management tool for regional courier firms, built in Lovable and running for four years. Nothing had ever been deleted: not delivery records, not the photographs couriers took as proof of delivery, not the location traces, and not the accounts of the 40% of customers who had left.

The database had grown to a point where list queries took several seconds, and storage costs had become his third largest expense. Then an enterprise prospect's security assessment asked for his data retention policy, and there was none to provide.

The review found three specific problems. Photographs of delivery addresses and recipient signatures — personal data — were being retained indefinitely with no stated basis. Location traces from former customers' couriers, some four years old, were still present. And two customers had previously requested deletion; their accounts had been marked inactive, but their delivery records, photographs, and traces remained.

**Result:** a written retention policy per data type, with delivery photographs kept 90 days, location traces 30, delivery records 7 years for invoicing, and cancelled accounts purged 90 days after closure. Soft deletion introduced with a 30-day window, a purge job with dry-run reporting and monitoring, and the two outstanding erasure requests completed properly. Storage fell by roughly 70% and list queries returned to well under a second.

> "I had four years of photographs of people's front doors because deleting them was never something anyone decided to do."
> — **Hugo Willemsen, Founder, Bezorgd**

**Cost & Timeline:** retention policy, soft deletion, and purge implementation delivered in 4 business days.

## Frequently Asked Questions

### Should deleting a record remove it immediately?

Usually not. Soft deletion with a defined recovery window makes the most common data-loss event — a customer deleting something by mistake — recoverable, provided a real purge follows afterwards.

### How long should customer data be kept after an account closes?

A stated period, commonly 30 to 90 days, after which it is removed. What matters is deciding it, publishing it, and enforcing it, since GDPR requires a justified period rather than a specific number.

### Does a deletion request mean deleting invoices too?

No. Tax law generally requires invoices and transaction records to be retained for years, which overrides the erasure request for those records. Personal data not subject to a retention obligation is removed, and the invoice keeps the minimum the law requires.

### What is the difference between archiving and deleting?

Archiving hides something from everyday view while keeping it intact, at the customer's choice. Deleting removes it. Presenting one and performing the other, in either direction, is a common and consequential mistake.

### Why does old data cost more than storage fees?

It slows queries, enlarges backups, and expands what a breach would expose. Data from customers who left years ago carries risk with no corresponding value.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should deleting a record remove it immediately?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not. Soft deletion with a defined recovery window makes accidental deletion recoverable, provided a real purge follows afterwards." } },
    { "@type": "Question", "name": "How long should customer data be kept after an account closes?", "acceptedAnswer": { "@type": "Answer", "text": "A stated period, commonly 30 to 90 days, then removed. GDPR requires a justified, adhered-to period rather than a specific number." } },
    { "@type": "Question", "name": "Does a deletion request mean deleting invoices too?", "acceptedAnswer": { "@type": "Answer", "text": "No. Tax law generally requires invoices to be retained for years, which overrides erasure for those records. Personal data not subject to an obligation is removed and the invoice keeps the legal minimum." } },
    { "@type": "Question", "name": "What is the difference between archiving and deleting?", "acceptedAnswer": { "@type": "Answer", "text": "Archiving hides something from view while keeping it intact, at the customer's choice. Deleting removes it. Presenting one while performing the other is a common and consequential mistake." } },
    { "@type": "Question", "name": "Why does old data cost more than storage fees?", "acceptedAnswer": { "@type": "Answer", "text": "It slows queries, enlarges backups, and expands what a breach would expose. Data from long-departed customers carries risk with no corresponding value." } }
  ]
}
</script>
