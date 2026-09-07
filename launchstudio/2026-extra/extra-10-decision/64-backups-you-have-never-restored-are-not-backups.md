---
Title: "Backups You Have Never Restored Are Not Backups"
Keywords: SaaS backup restore testing, point in time recovery, RPO RTO small startup, backup file storage, restore drill procedure, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Backups You Have Never Restored Are Not Backups

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Backups You Have Never Restored Are Not Backups",
  "description": "Almost every founder believes they have backups because their hosting provider says so. What that actually covers, what it does not, how much data loss you are implicitly accepting, and why a restore you have never performed is a hope rather than a plan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/backups-you-have-never-restored-are-not-backups" }
}
</script>

Ask a founder whether they have backups and the answer is almost always yes, delivered with the confidence of someone who ticked a box during setup or read it in a hosting provider's feature list. Ask two follow-up questions and the confidence usually evaporates: how much work would your customers lose if you restored right now, and how long would the restore take? Most people do not know, which means the honest answer to the original question is "I have something, and I have never found out what."

This is not negligence. Backups are the definitive example of work that produces nothing visible until the day it produces everything. But there is a specific, cheap piece of work — performing one restore, once, before launch — that converts a belief into a fact, and the founders who do it invariably discover something they did not expect.

## The Two Numbers That Define Your Actual Position

Strip away the terminology and there are two questions.

**How much data can you afford to lose?** If your last usable backup is 24 hours old, a failure means every customer redoing a day's work — assuming they can remember it. For a product where customers enter a few records a week, that may be genuinely acceptable. For one where a business runs its daily operations through you, it is not.

**How long can you be down while restoring?** Not the moment the restore command finishes — the moment customers can use the product again, including reconnecting the application, verifying data, and confirming nothing else broke. Founders who have never done it estimate twenty minutes. The real figure for someone doing it for the first time under pressure, without a written procedure, is usually several hours.

Write both numbers down as targets, then check whether your current setup actually meets them. The gap between the two is usually where the surprise is, and it is much better encountered on a quiet Tuesday than during an incident.

## What Your Provider's Backups Actually Cover

Managed platforms — Supabase, Railway, Render, most managed Postgres services — do take backups, and this is genuinely valuable. It is also more limited than the marketing implies, in ways worth knowing before you rely on it.

**Frequency and retention vary sharply by plan.** Free and entry tiers commonly mean daily snapshots kept for seven days, sometimes less. Point-in-time recovery, which lets you restore to any moment rather than to yesterday's snapshot, is typically a paid feature. Check what your actual plan provides rather than what the product page says.

**Backups cover the database, not everything.** Uploaded files in object storage are usually a separate matter with its own configuration. So are any configuration values, environment secrets, and third-party state. A database restore that leaves every customer's uploaded documents missing has restored the index and lost the library.

**A backup in the same account as the thing it protects is partial protection.** It covers accidental deletion and corruption, which are the common cases. It does not cover a compromised or suspended account, where the backups are just as gone as the data. One periodic copy held somewhere else — a different provider, or at minimum a different account — closes that gap cheaply.

**A deleted project may take its backups with it.** On several platforms, removing a project removes everything associated with it, immediately.

## The Failures Backups Are Actually For

The dramatic scenario — the provider's data centre burns down — is the one people imagine and the least likely. The real causes are mundane and much more frequent.

**Someone runs a query without a condition.** An update or delete intended for one row that reaches every row. This is the single most common serious data incident in small companies.

**A migration goes wrong.** A schema change that drops or transforms a column incorrectly, discovered after it has run against production.

**A bug deletes data slowly.** A cascade rule removing more than intended, running quietly for two weeks before anyone notices. This one is particularly nasty, because backups from within those two weeks contain the same problem — which is exactly why retention length matters more than backup frequency.

**A customer deletes something and wants it back.** Not a disaster, just a Tuesday, and one your customers will consider a reasonable request.

That last category deserves its own answer, because restoring an entire database to recover one customer's records is disproportionate and destroys everyone else's recent work. Soft deletion — marking records as deleted rather than removing them, with a purge after a defined period — handles the overwhelming majority of these requests without touching backups at all, and is far cheaper to implement before launch than after.

## The Restore Drill

Here is the work that matters, and it takes an afternoon.

Take your most recent backup. Restore it somewhere that is not production — a separate database, a staging environment. Point a copy of your application at it. Log in. Check that customer records are present, that uploaded files resolve, that the most recent data is as recent as you expected. Write down every step you took and every thing that went wrong.

Almost nobody completes this without finding at least one problem. Common discoveries: the backup contains the database but the application cannot start because a secret or configuration value lives only in the production environment; uploaded files are missing entirely because storage was never included; the restore takes forty minutes rather than five; the most recent data is eighteen hours old rather than the assumed one hour; or the restore requires a permission only one person has, and that person is on holiday.

The output is a written procedure with real timings. Under pressure, at 2am, with customers waiting, the difference between a procedure and improvisation is the difference between an incident and a catastrophe.

Setting up backup coverage that includes file storage and configuration, adding an off-platform copy, and producing a tested restore procedure is a small, bounded piece of production work. LaunchStudio, backed by Manifera's 11+ years of production engineering, includes it in launch preparation, because a product carrying real customer data without a verified restore path is not finished regardless of how well it works. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Reasonable Targets for a Small Product

Sensible defaults, adjusted for what your customers would lose.

**Frequency:** daily automated backups as a floor. Point-in-time recovery if customers do substantial work within a single day, which is most business products.

**Retention:** thirty days at minimum. Seven is too short to survive a slow-acting bug, which is precisely the scenario where you need to reach further back than you expected.

**Scope:** database, uploaded files, and a record of configuration and environment values — the last kept securely, since it contains secrets.

**Location:** at least one copy outside the account holding production.

**Verification:** one full restore drill before launch, then repeat after any significant infrastructure change, and once or twice a year regardless.

**Monitoring:** an alert when a backup fails. Silent failure is the norm; backup processes stop working for ordinary reasons — a changed credential, a full disk — and nobody notices until the day it matters.

## Real example

### The Backups That Were Six Weeks Behind Reality

Emre Kaplan ran Loonstrook, a payroll-document portal for small Dutch employers, built in Lovable and running on a managed database with automated daily backups enabled. He considered the question settled.

A cascade rule introduced during a schema change began deleting document metadata whenever an employee record was updated — quietly, affecting a handful of records a day. It was discovered five weeks later when a customer reported that older payslips had disappeared.

Two things then became apparent. Backup retention on his plan was fourteen days, so every available backup already contained the deletions. And the backups covered the database only: the payslip PDFs themselves lived in object storage that had never been included in any backup configuration at all. The files were still there, but the records linking them to employees were gone from every copy he had.

Reconstruction was possible only because the storage filenames encoded an employer reference and a date, allowing a partial rebuild over four days of careful work. Roughly 7% of documents could not be confidently matched and had to be re-requested from customers.

**Result:** point-in-time recovery enabled, retention extended to 90 days, object storage brought into a nightly backup with its own retention, an off-platform weekly copy added, soft deletion introduced for all customer-visible records, and a documented restore procedure tested end to end in 35 minutes.

> "I had backups. I had never once asked what was in them, and the answer turned out to be about half of what I thought."
> — **Emre Kaplan, Founder, Loonstrook**

**Cost & Timeline:** backup coverage, soft deletion, and tested restore procedure delivered in 3 business days.

## Frequently Asked Questions

### Are my hosting provider's automatic backups enough?

They are a good starting point and usually cover the database only. Uploaded files, configuration, and secrets are typically separate, retention on entry-level plans is often short, and backups held in the same account do not protect against losing that account.

### How often should backups run for a small product?

Daily as a floor, with point-in-time recovery if customers do meaningful work within a single day. Retention matters as much as frequency: thirty days minimum, because slow-acting bugs contaminate recent backups.

### What is a restore drill and how long does it take?

Restoring a real backup into a non-production environment, pointing an application at it, and verifying the data. It takes an afternoon and almost always uncovers something — missing files, missing configuration, or a restore far slower than assumed.

### How do I handle a customer asking to recover something they deleted?

With soft deletion rather than backups. Marking records as deleted and purging them after a defined period handles almost all such requests without a restore that would discard everyone else's recent work.

### Should backups be stored with a different provider?

At least one copy outside the account holding production is worth having. Same-account backups protect against deletion and corruption but not against losing access to the account itself.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Are my hosting provider's automatic backups enough?", "acceptedAnswer": { "@type": "Answer", "text": "They are a starting point and usually cover the database only. Uploaded files, configuration, and secrets are typically separate, entry-tier retention is often short, and same-account backups do not protect against losing the account." } },
    { "@type": "Question", "name": "How often should backups run for a small product?", "acceptedAnswer": { "@type": "Answer", "text": "Daily as a floor, with point-in-time recovery if customers do meaningful work within a day. Retention matters as much as frequency: thirty days minimum, since slow-acting bugs contaminate recent backups." } },
    { "@type": "Question", "name": "What is a restore drill and how long does it take?", "acceptedAnswer": { "@type": "Answer", "text": "Restoring a real backup into a non-production environment, pointing an application at it, and verifying the data. It takes an afternoon and almost always uncovers missing files, missing configuration, or unexpected slowness." } },
    { "@type": "Question", "name": "How do I handle a customer asking to recover something they deleted?", "acceptedAnswer": { "@type": "Answer", "text": "With soft deletion rather than backups. Marking records deleted and purging after a defined period handles almost all such requests without discarding everyone else's recent work." } },
    { "@type": "Question", "name": "Should backups be stored with a different provider?", "acceptedAnswer": { "@type": "Answer", "text": "At least one copy outside the production account is worth having. Same-account backups protect against deletion and corruption but not against losing access to the account." } }
  ]
}
</script>
