---
Title: "Lovable Supabase: Soft Deletes, Archiving and What You Keep"
Keywords: lovable supabase, soft delete, data retention, archiving, gdpr erasure, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Soft Deletes, Archiving and What You Keep

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Soft Deletes, Archiving and What You Keep",
  "description": "Delete means four different things: hide it, keep it for us, keep it because the law says so, and remove it permanently. Building all four, and resolving the conflict between retention and erasure.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-soft-deletes-archiving-and-what-you-keep" }
}
</script>

A customer clicks delete. What should happen?

In an AI-built product the answer is nearly always the same: the row is removed immediately and permanently, because that is what delete means in code and nobody asked for anything else.

In a real business, delete means at least four different things depending on who clicked it and what they clicked, and getting them confused produces two opposite and equally serious failures: data destroyed that you were obliged to keep, and data kept that you were obliged to destroy.

## Four Meanings of Delete

**Hide it from my view.** A user tidying up. They expect it gone from their screen and would be horrified to learn it was irrecoverable — "I didn't mean permanently" is the most common support message in any product without an undo.

**Remove it from active use, but we may need it.** A cancelled order, a former employee's record, a closed project. The business still refers to these.

**Keep it because we are obliged to.** Invoices, payroll records, contracts. In the Netherlands, business administration generally must be retained for seven years, with longer periods for some categories such as records relating to immovable property. Verify what applies to your data with an accountant rather than assuming.

**Erase it permanently, because someone has a right to that.** A GDPR erasure request, or your own retention policy expiring.

A product that implements only the last one while believing it implements the first is the common and dangerous case.

## Soft Delete as the Default

For anything a user can delete, the sensible default is a marker rather than a removal: a timestamp column recording when it was deleted, with your queries excluding those rows.

Three things make this work properly.

**Filter it in one place.** If every query must remember to exclude deleted rows, one will forget, and a deleted record will reappear in a report. Handle it in your access policies or in a view, so it applies everywhere including queries written later by an agent session.

**Give users a way back.** A visible bin, restorable for a defined period. This turns your most common support request into a self-service action.

**Clean up on a schedule.** Soft-deleted rows are still rows: they occupy space, they slow queries, and they contain personal data you no longer need. Purge them after the recovery window, automatically.

The cost of soft delete is that every query has an extra condition and every unique constraint needs thought — a deleted record should usually not block a new one with the same email address.

## Archiving Is a Different Problem

Soft delete answers "the user removed it". Archiving answers "this is finished and we do not need it in the way".

Closed projects, previous years, terminated contracts. They stay available and stop occupying the working set. The mechanisms differ in effort: a status column that your default views exclude is the simple version; moving rows to separate archive tables, or partitioning by date so old data lives in separate physical chunks, is the version that matters once volume is real.

The performance argument is the one founders respond to. A product where every query filters over five years of history when customers only ever look at this one is doing five times the work for no benefit, and the fix is structural rather than a matter of adding indexes.

## Where Retention and Erasure Collide

The genuinely difficult part, and where honest advice is hedged.

A customer asks you to erase their data. Some of that data sits in invoices you are required to keep. These obligations point in opposite directions, and the resolution is not to pick one.

The shape of the answer is usually that the right to erasure does not override a legal obligation to retain, so the retained records stay, and everything not covered by that obligation is erased. Practically this means separating the data that carries an obligation — the invoice, with the details required on it — from the data that does not: activity history, preferences, uploaded documents, analytics, support conversations.

Products that store everything in one table cannot do this, which is why the separation is a design decision rather than a policy one. Build it before you receive the request.

What that separation looks like in practice: financial records in their own tables with their own retention, personal profile data separable from them, and a documented list of what is erased, what is retained and why. The specifics depend on your data and situation, so verify current requirements with a lawyer or accountant rather than relying on a general description.

## Erasure Has to Reach Everywhere

When you do erase, the row is the easy part.

Uploaded files in object storage. Entries in your audit trail, which raises its own question — the fact that a change happened is frequently legitimate to keep even when the personal detail in it is not, so consider recording actor identifiers that can be dissociated rather than names. Search indexes. Caches. Backups, which hold a copy until their retention window expires — which is acceptable provided your retention period is defined, documented and honoured. And any third party you sent the data to, which is what your subprocessor list is for.

Anonymisation is frequently the better tool than deletion: replacing identifying fields while keeping the record's shape preserves your aggregate figures and your referential integrity, and properly anonymised data is no longer personal data. Properly is doing work in that sentence — a record with the name removed but a unique reference intact is not anonymous.

## What to Build, and in What Order

Soft delete with a visible bin and scheduled purging for anything users delete. A separation between records carrying retention obligations and everything else. Archiving for finished work, before volume forces it. An erasure operation that reaches rows, files, indexes, caches and processors. A written retention policy stating what is kept, for how long, and what deletion actually removes. And an audit record of erasures performed, since demonstrating compliance requires evidence.

That is a few days on a product that already works, and it is the part of a security questionnaire that most small suppliers cannot answer.

## When a Whole Customer Leaves

Individual records are the easy case. A customer ending their contract is the one nobody designs for, and it arrives with a deadline attached.

**They want their data out, in a usable form.** Not a screenshot, not a report — their records, in a format another system can read. Build this before you need it: a per-tenant export producing standard files, available to the customer without you being involved. It is a procurement question before it is a leaving question, and being able to answer it during a sales conversation is worth more than it costs.

**There should be a grace period.** Immediate deletion on the day a contract ends is legally tidy and commercially foolish: customers change their minds, invoices get disputed, and someone always remembers a document they needed a week later. A defined window — stated in your terms — where the account is closed but recoverable serves everybody.

**Then deletion has to actually happen.** On a schedule, automatically, reaching rows, files, search indexes, caches and the third parties you sent data to. A dormant tenant kept indefinitely because nobody wrote the cleanup is personal data you are holding with no basis, and it is the finding that turns an otherwise fine data protection review uncomfortable.

**Keep what you are obliged to keep, separately.** Invoices to that customer remain under your retention obligations; their operational data does not. This is the same separation as for individual erasure, applied one level up.

**Say all of it in your terms.** What happens at termination, what format the export takes, how long the grace period is, when deletion occurs, and what is retained. Customers rarely read it before signing and always read it when leaving, and a supplier whose answer is already written is treated very differently from one improvising.

## Getting Deletion Right Before Someone Asks

For a running product this is bounded work: soft delete implemented with filtering applied in one place so later queries inherit it, a recovery window and automatic purging, archiving introduced for closed records, financial and obligated data separated from erasable personal data, a complete erasure operation covering storage, indexes, caches and third parties, anonymisation used where it preserves your figures, retention documented per category, and the whole thing recorded so you can demonstrate it.

LaunchStudio does this alongside the access model, since the two together are what a Dutch business customer's questionnaire actually probes. The engineers are Manifera's: eleven years of production data work for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us what your product stores](https://launchstudio.eu/en/#contact) for a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Deleted Employee and an Invoice That Went With Them

Wendy Bosman built Personeelsdossier with Lovable: personnel file management for small companies, used by 29 businesses around Hengelo and Enschede — contracts, absence records, review notes, payslip archives.

Delete removed the row. There was no bin, no archive, no separation between personnel data and the payroll documents attached to it.

Two failures arrived within a month. A bookkeeper at a customer deleted a former employee's file intending to remove them from the active list, and removed seven years of payslip records with them — records the company was obliged to retain and could not reconstruct, since Wendy's product had been the only place they lived after the company changed payroll providers.

Then a former employee at a different customer made a GDPR erasure request. Wendy had no way to comply partially: everything about that person was in one table, including the payroll records her customer was obliged to keep. Her options were to refuse the request or to destroy her customer's legal records.

Eleven business days of work: soft delete implemented across all user-deletable records with a 90-day bin, restorable by administrators, with filtering applied in the access policies so later queries inherit it automatically; scheduled purging after the window; personnel records separated from documents carrying retention obligations, with the two linked rather than combined; archiving introduced for former employees so files leave the active list without leaving the system; an erasure operation built covering rows, stored documents, search entries and the audit trail, with actor identifiers made dissociable rather than named; anonymisation used where aggregate absence statistics needed to survive; a retention policy written per category in consultation with an accountant and confirmed with the 29 customers; and an erasure log added so each request and its scope is recorded.

The seven years of payslips were partially recovered from a backup that happened to predate the deletion by nine days. The gap was documented and reported to the customer honestly.

**Result:** the erasure request was handled in a way both the individual and the customer accepted — personal data removed, obligated payroll records retained with a documented basis — and the retention policy is now sent to every new customer during onboarding.

> *"One click removed a person and seven years of payslips my customer was legally required to keep. The same week, someone asked me to erase them, and I could not do it without destroying the same kind of records for somebody else."*
> — **Wendy Bosman, Founder, Personeelsdossier (Hengelo)**

**Cost & Timeline:** €5,100 (soft delete with recovery window and policy-level filtering, archiving, separation of obligated records, full erasure operation, anonymisation, retention policy, erasure logging) — completed in 11 business days.

## Frequently Asked Questions

### Should delete remove the row?

Usually not. Most users clicking delete mean "hide this from my view" and expect to be able to undo it. Use a deletion timestamp, filter it in one place so later queries inherit it, offer a bin, and purge on a schedule.

### How do I stop a deleted record reappearing in a report?

Apply the exclusion once — in your access policies or in a view — rather than in every query. Anything relying on each query remembering will eventually be contradicted by a query written later.

### What happens when retention obligations conflict with an erasure request?

They usually do not override each other: records you are legally obliged to keep are retained, and everything else is erased. That is only possible if obligated data is stored separately from the rest, which is a design decision you make before the request arrives.

### Does erasure only mean deleting database rows?

No. It must reach uploaded files, search indexes, caches, your audit trail and any third party you sent the data to. Backups hold a copy until their retention window expires, which is acceptable if that period is defined and documented.

### Is anonymisation better than deletion?

Often, yes. Replacing identifying fields preserves your aggregate figures and referential integrity, and properly anonymised data is no longer personal data — but a record with the name removed and a unique reference intact is not anonymous.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should delete remove the row?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not — most users mean 'hide this'. Use a deletion timestamp filtered in one place, offer a bin, and purge on a schedule."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop a deleted record reappearing in a report?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Apply the exclusion once in access policies or a view, rather than relying on every query — including future ones — to remember."
      }
    },
    {
      "@type": "Question",
      "name": "What happens when retention obligations conflict with an erasure request?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Obligated records are retained and everything else is erased — which requires storing obligated data separately, a decision made before the request arrives."
      }
    },
    {
      "@type": "Question",
      "name": "Does erasure only mean deleting database rows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it must reach files, search indexes, caches, audit trails and third parties, with backups covered by a defined retention window."
      }
    },
    {
      "@type": "Question",
      "name": "Is anonymisation better than deletion?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often, since it preserves aggregates and integrity — but only if done properly; a removed name with a unique reference intact is not anonymous."
      }
    }
  ]
}
</script>
