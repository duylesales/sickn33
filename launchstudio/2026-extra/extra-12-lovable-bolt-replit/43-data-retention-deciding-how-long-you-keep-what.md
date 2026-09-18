---
Title: "Data Retention: Deciding How Long You Keep What"
Keywords: data retention, retention policy, automated deletion, anonymisation, storage growth, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Data Retention: Deciding How Long You Keep What

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Data Retention: Deciding How Long You Keep What",
  "description": "Keeping everything forever is a decision made by not deciding. Setting retention periods per category, the tax obligations that override them, anonymising instead of deleting, and enforcing it automatically.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/data-retention-deciding-how-long-you-keep-what" }
}
</script>

Ask a founder how long their product keeps data and the answer is usually a pause. Not because the policy is complicated, but because there is no policy — everything is kept, indefinitely, because deletion was never built and nobody chose otherwise.

Keeping everything feels safe. It is not. Data you hold is data you must secure, disclose, export, produce on request and account for in a breach. Every additional year of records is more surface for the same product.

The argument for retention limits is not primarily legal. It is that a smaller pile of data is a smaller problem in every direction, including the ones nobody plans for.

## The Principle, Stated Plainly

Keep personal data only as long as necessary for the purpose it was collected for. Necessary is defined by that purpose, not by convenience and not by the possibility that it might be interesting later.

Two things follow. There must be a period per category rather than one rule for the whole product, because an invoice and a support chat transcript have genuinely different lifespans. And the period must be enforced, not merely documented — a policy stating twelve months on a database holding three years is a statement contradicted by your own data.

## Periods That Are Defensible

For a typical Dutch B2B product, the shape usually looks like this.

**Invoices and financial records: seven years.** Dutch tax law requires it, and this obligation overrides a deletion request — a customer asking to be forgotten does not remove your duty to retain their invoices.

**Customer account and contract data:** for the life of the relationship plus a period afterwards for claims and queries, commonly two years.

**Operational records** — appointments, orders, work performed — as long as the customer needs them, which for a business product is usually their decision as controller rather than yours. State a default and let them specify.

**Support correspondence:** one to two years.

**Technical logs:** 30 to 90 days, with security-relevant events kept longer in an audit trail.

**Marketing contacts:** while there is a relationship, with an unsubscribe removing them promptly.

**Backups:** a stated period, typically 30 to 90 days, after which they age out.

These are starting points rather than rules. What matters is that each is a decision you can explain.

## Anonymise Instead of Deleting

The objection to retention limits is usually about statistics: deleting three years of bookings destroys the ability to say anything about trends.

Anonymisation resolves it. Strip the identifying fields and keep the rest — the appointment happened on this date, in this category, at this duration, with the name, contact details and notes removed. The record stops being personal data and stops carrying obligations, while remaining useful for the counting you actually do.

The standard is genuine irreversibility. Replacing a name with a reference that maps back to it in another table is pseudonymisation, which is a good security measure and still personal data. If you can re-identify someone, so can anyone with the same access.

Be careful with small numbers as well: a single record in a category with a location and a date can identify a person even without a name.

## Enforce It With a Job, Not a Reminder

A retention policy that depends on someone remembering is a retention policy that has already failed.

The implementation is a scheduled job running daily or weekly, applying each rule to its category, deleting or anonymising as decided, and recording what it did. The record matters: knowing that 1,400 records were anonymised last month is how you demonstrate the policy operates.

Three practical requirements. Run it in batches so it does not lock tables. Give it a dry-run mode, and use that mode first — the first real run of a deletion job is the moment to discover that a rule was more aggressive than intended. And exclude anything under a legal hold, because a dispute or an investigation suspends ordinary retention.

Alert if the job does not run. A deletion job that silently stops is invisible for exactly as long as a backup that silently stops.

## Tell People, and Tell Your Customers

Two audiences.

Your privacy policy should state retention in terms people can understand: how long, for what, and what happens afterwards. "As long as necessary" is not informative and reads as evasion.

Your business customers need more. Their processing agreement will specify deletion on termination, and they will want to know that their data goes when they leave. Building a deletion that runs per customer, produces a confirmation, and handles the interaction with backups is what makes that clause true rather than aspirational.

## Deletion Is Not Only Rows

A complete deletion touches more than the database, and this is where implementations fall short.

Uploaded files in object storage. Cached copies and derivatives such as thumbnails. Search indexes, which hold a copy of the content. Exports generated previously and still sitting in a bucket. Third-party services holding a copy — an email provider's sending history, a support tool's tickets, an analytics service's events. And backups, which retain everything until they age out.

Write the deletion procedure as a list covering every one of those, and state the backup position explicitly: data remains in backups for the retention period and will not be restored into production without re-applying the deletion. That is an accepted position, and it is far better than silence.

## Who Decides, You or Your Customer

For a business product this question arrives early and the answer shapes the whole design.

Your customer is the controller. It is their decision how long their clients' records are kept, because it depends on their profession, their own obligations and their contracts. A physiotherapy practice has a statutory retention period for patient files; a marketing agency does not.

So the design that works is a default with a per-customer override, bounded by a maximum you are willing to hold. The default covers the customers who have never thought about it — most of them — and the override serves the ones with a specific obligation. The maximum protects you from a customer who would keep everything forever inside your product.

Two implementation details matter. The retention setting belongs in your product's interface, visible and changeable by the customer, not in a configuration file you edit on request. And changing it should apply prospectively without silently deleting what a shorter new period would have removed — a customer who reduces their retention from five years to two should be told what that will delete and asked to confirm.

State the default and the maximum in your terms, so a customer who needs eleven years knows before signing that your product is not where those records should live.

## The First Run Is the Frightening One

Every retention project reaches the same moment: the job is written, the dry run reports that it will remove 1.1 million records, and nobody wants to press the button.

Four things make that moment ordinary rather than alarming.

**Run the dry run more than once**, a week apart, and compare. A rule that selects a wildly different number on the second pass is a rule with a bug in its date arithmetic, which is the most common defect in retention jobs.

**Check a sample by hand.** Take twenty records the job intends to remove and confirm each one genuinely should go. Boundary cases — a record updated recently but created long ago, one belonging to a customer who left last week — are where the surprises are.

**Take a backup immediately before**, and keep it for its full retention period. This is not a contradiction of the policy; it is the ordinary safety net for a large irreversible operation.

**Do the first run in stages.** The oldest year first, then the next, with a pause between. If something is wrong, it is wrong about a smaller amount of data and you find out before the rest.

After the first run the job becomes routine and removes a small number of records each week, which is the steady state you want. It is only the initial catch-up that is large, precisely because the policy is being applied for the first time to years of accumulated data.

## Setting This Up

For an existing product this is typically one to two days: every category of data listed with a retention period and a reason, legal obligations such as the seven-year financial retention identified, anonymisation designed where statistics must survive, a scheduled enforcement job with batching, dry-run mode, legal hold exclusion and a record of what it did, alerting if it does not run, deletion extended beyond the database to files, caches, indexes, prior exports and third-party services, a documented backup position, per-customer deletion with confirmation for contract termination, and retention stated plainly in the privacy policy.

LaunchStudio builds retention as part of compliance work for products selling to businesses, where it is frequently the clause that makes a contract signable. Behind it is Manifera — eleven years, clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Ask us how much data your product is holding that nobody needs](https://launchstudio.eu/en/#contact).

## Real example

### Four Years of Everything

Xander Lubbers built Bezorgdienst in Lovable: delivery planning and proof of delivery for regional couriers and meal suppliers, 19 companies handling around 40,000 deliveries a month.

Four years of operation, no deletion of anything. The database held every delivery since launch with recipient names, addresses, phone numbers, delivery notes and a signature image. Around 1.6 million records and 900 GB of signature and photo files.

Two things forced the issue in the same month. A recipient submitted an access request, and answering it required searching four years of records across three systems, which took two days. And a courier company terminated and invoked their deletion clause, which Xander had no way to satisfy for one company's data without touching everyone else's.

Five business days: retention decided per category with reasons written down — delivery records and proof of delivery retained 24 months by default with each courier company able to specify a longer period within limits, signature images 12 months, delivery photos 12 months, financial records seven years, support correspondence 18 months, technical logs 60 days; anonymisation designed for delivery records past their period, keeping date, postcode area, category and duration while removing names, full addresses, phone numbers and notes, so the route analytics his customers value survived; a scheduled weekly job with batching, a dry-run mode used for the first three runs, legal hold exclusion and a record of each execution; alerting if it does not run; deletion extended to object storage, thumbnails, the search index and previously generated exports, none of which had been considered; a documented backup position with retention reduced from indefinite to 60 days; per-company deletion producing a confirmation certificate; an access request function that assembles a recipient's records in minutes; and the privacy policy rewritten to state the periods.

**Result:** the first full run anonymised 1.1 million delivery records and removed 640 GB of signature and photo files, cutting storage costs by €190 a month. The terminating company received a certificate within the contractual window. The access request that had taken two days now takes four minutes, and Xander notes that his customers' route analytics were unaffected because the fields that mattered were never the personal ones.

> *"I kept everything because deleting felt risky. It turned out that holding four years of people's home addresses and signatures was the risk, and I had chosen it by never making a choice."*
> — **Xander Lubbers, Founder, Bezorgdienst (Tilburg)**

**Cost & Timeline:** €3,700 (retention policy per category, anonymisation design preserving analytics, scheduled enforcement with dry run and legal holds, deletion across storage, caches, index and exports, backup retention, per-customer deletion with certificates, access request tooling, policy rewrite) — completed in 5 business days.

## Frequently Asked Questions

### Can I just keep everything?

It is a decision with costs: more to secure, disclose, export and account for in a breach, and a privacy policy that either says so or is inaccurate. Retention limits reduce risk in every direction.

### What about invoices when someone asks to be forgotten?

Dutch financial record obligations — seven years — override an erasure request for those records. Delete what you can, retain what you must, and explain which is which.

### How do I keep statistics if I delete the data?

Anonymise rather than delete: keep the date, category and other non-identifying fields, remove names, contact details and free text. The result is no longer personal data and remains useful for counting.

### What does deletion have to cover besides the database?

Files in object storage, thumbnails and caches, search indexes, previously generated exports, and copies held by third-party services. Backups retain data until they age out, which should be stated.

### How should retention be enforced?

A scheduled job with batching, a dry-run mode, legal hold exclusion, a record of each run and an alert if it stops. A policy relying on someone remembering has already failed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is it acceptable to keep all data indefinitely?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It increases what you must secure, disclose, export and account for in a breach, and makes an accurate privacy policy harder to write."
      }
    },
    {
      "@type": "Question",
      "name": "Do I delete invoices when someone requests erasure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Dutch financial retention obligations of seven years override erasure for those records; delete what you can and explain the rest."
      }
    },
    {
      "@type": "Question",
      "name": "How can I keep analytics if data is deleted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anonymise irreversibly — keep dates and categories, remove names, contact details and free text. The result is no longer personal data."
      }
    },
    {
      "@type": "Question",
      "name": "What must deletion cover besides database rows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Object storage, thumbnails and caches, search indexes, old exports, and third-party copies. Backups retain data until they age out."
      }
    },
    {
      "@type": "Question",
      "name": "How is a retention policy enforced?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A scheduled batched job with a dry-run mode, legal hold exclusions, a record of each run and an alert when it does not run."
      }
    }
  ]
}
</script>
