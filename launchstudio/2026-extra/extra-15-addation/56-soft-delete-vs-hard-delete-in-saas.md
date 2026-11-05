---
Title: "Soft Delete vs Hard Delete in SaaS"
Keywords: soft delete vs hard delete, soft delete supabase rls, gdpr erasure soft delete, restore deleted records saas, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Soft Delete vs Hard Delete in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Soft Delete vs Hard Delete in SaaS",
  "description": "When a user clicks delete, should the data disappear or merely be hidden? This guide compares soft and hard deletion for AI-built SaaS products, explains how to implement soft delete with Row Level Security and partial indexes, how to offer a trash and restore feature, how cascades and foreign keys behave, and how to reconcile soft delete with GDPR erasure, backups and retention.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-12",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/soft-delete-vs-hard-delete-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Partial indexes", "url": "https://www.postgresql.org/docs/current/indexes-partial.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Foreign keys", "url": "https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK" },
    { "@type": "CreativeWork", "name": "Supabase Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

Every SaaS product has a delete button, and behind every delete button is a decision most founders never consciously make. When a user deletes a project, an invoice, a client record or a document, should the data be removed from the database immediately and permanently, or should it be marked as deleted and hidden, so it can be restored if needed?

AI builders usually choose for you, and they almost always choose hard deletion: a `delete` query that removes the row, sometimes with cascading deletes that remove related data too. That is simple and works in demos. In production, it leads to support requests nobody can answer ("I deleted the wrong client, can you get it back?"), disputes nobody can resolve ("who deleted those invoices?") and occasionally catastrophic cascades where deleting one record removes hundreds of related ones.

Soft deletion is not automatically better. It complicates queries, can conflict with privacy obligations and lets data accumulate. This guide explains when to use each, and how to implement soft deletion safely.

## Key Takeaways

- **Hard delete removes data permanently;** soft delete marks it as deleted, usually with a `deleted_at` timestamp, and hides it.
- **Soft delete enables undo, trash and restore features,** supports investigations and protects against mistakes.
- **Soft-deleted data still exists.** It is not erasure under GDPR, so define when soft-deleted data is permanently purged.
- **Implement soft delete in the database,** with Row Level Security or views that hide deleted rows, and partial indexes for uniqueness.
- **Review cascades.** Cascading hard deletes can remove far more than the user intended.

## Comparison

| Aspect | Hard delete | Soft delete |
| --- | --- | --- |
| Recovery after mistakes | Only from backups | Simple restore |
| Investigations and disputes | No trace, unless audit logs exist | Record remains with deletion metadata |
| Query complexity | Simple | Every query must exclude deleted rows |
| Storage | Data removed | Data accumulates until purged |
| GDPR erasure | Satisfies erasure for the live database | Not sufficient alone; needs purge |
| Uniqueness constraints | Straightforward | Need partial indexes |
| Performance | No extra filtering | Indexes and filters needed |

Many mature products use both: soft delete for user-facing deletions with a recovery period, followed by hard delete or anonymisation after that period.

## When to Use Hard Delete

Hard deletion fits:

- **Truly disposable data,** such as temporary drafts, expired sessions or cache entries
- **Data subject to erasure requests,** after any legal retention period
- **High-volume, low-value records,** such as old notifications, where keeping deleted copies has no benefit
- **Simple products** where undo is not needed and audit logs capture deletion events

## When to Use Soft Delete

Soft deletion fits:

- **Business records** such as clients, projects, invoices, contracts and documents, where mistakes are costly
- **Shared data in team products,** where one person's deletion affects others
- **Records referenced by other data,** such as a product that appears in past orders
- **Products with compliance or dispute needs,** where knowing what happened matters

## Implementing Soft Delete in Supabase

The basic pattern adds columns to tables:

- `deleted_at timestamptz`, null when the record is active
- `deleted_by uuid`, the user who deleted it

"Deleting" becomes an update that sets these fields. Then make sure deleted rows disappear from normal use.

**Option 1: Row Level Security.** Add a condition to select policies so regular users only see rows where `deleted_at is null`. A separate policy, or a separate function, gives admins access to deleted items for restoring.

**Option 2: Views.** Create views that select only active rows, and have the app query the views. Base tables remain available for admin and restore functions.

**Option 3: Application filters.** Every query adds `deleted_at is null`. This is the weakest option, because every new query, including those generated by AI tools, must remember the filter.

For AI-built apps, Row Level Security or views are preferable, because they make the safe behaviour the default.

Also prevent direct hard deletes by regular users: remove delete permissions from policies and route deletion through a function that sets `deleted_at`.

## Uniqueness With Soft Delete

A common problem: a table has a unique constraint on, for example, a project slug or an email address in a contacts list. A user deletes a record and tries to create a new one with the same value, and the constraint blocks it, because the deleted row still exists.

The solution is a **partial unique index** that only applies to active rows:

```sql
create unique index contacts_unique_active_email
  on contacts (organisation_id, email)
  where deleted_at is null;
```

When a deleted record is restored, check for conflicts with any active record created in the meantime.

## Cascades and Related Data

Foreign keys can be configured to cascade deletes, so deleting a parent removes its children. With hard deletes, cascades can be dangerous: deleting a client might remove all their projects, invoices and documents. AI-generated schemas often use `on delete cascade` liberally.

Decide deliberately:

- **Cascade** only for data that genuinely has no meaning without its parent, such as line items of an invoice.
- **Restrict** deletion of records that are referenced elsewhere, such as products used in past orders, and offer archiving instead.
- **Soft delete children with parents** where needed, using a function that marks related records consistently, and restore them together.

Review every `on delete cascade` in your schema before launch.

## Trash and Restore

Soft delete enables a feature users appreciate: a trash or recycle bin.

- **Show deleted items** in a trash view, with who deleted them and when.
- **Allow restore** by the user or an admin, depending on permissions.
- **Define a retention period,** such as 30 days, after which items are permanently deleted.
- **Allow permanent deletion** from the trash for users who need it, with confirmation.
- **Offer undo** immediately after deletion, such as a toast with an "Undo" button.

These features reduce support requests significantly and prevent the stressful "can you restore my data from backup?" conversations.

## Archiving: The Third Option

Between active and deleted, there is often a third state that users actually want: archived. A finished project, a former client or an old product is no longer relevant day to day, but nobody wants to delete it. Archiving hides the record from default views while keeping it fully available for search, reports and reference.

| State | Visible in default lists | Searchable | Restorable | Counts towards plan limits | Eventually purged |
| --- | --- | --- | --- | --- | --- |
| Active | Yes | Yes | Not applicable | Usually yes | No |
| Archived | No | Yes, with filter | Yes | Often no | No, unless retention rules apply |
| Soft deleted | No | No, except in trash | Yes, during retention | No | Yes, after retention |

Offering archive alongside delete reduces accidental deletions, because users who just want something out of the way choose archive instead. It also gives you a clean way to handle downgrades, where items above a plan limit can become archived rather than removed.

## Soft Delete and GDPR

Soft-deleted data still exists in your database. Under GDPR, when someone exercises their right to erasure, or when data is no longer needed for its purpose, hiding it is not enough. You need to:

- **Purge soft-deleted data** after a defined retention period, through a scheduled job that hard-deletes or anonymises it.
- **Handle erasure requests** by permanently deleting or anonymising personal data, unless a legal obligation, such as tax record retention, requires keeping it.
- **Consider backups.** Data persists in backups for their retention period. Document this in your privacy policy and records of processing, and make sure restored backups do not resurrect erased data, for example by reapplying erasure after a restore.
- **Anonymise where records must remain,** such as keeping an invoice for tax purposes but removing unnecessary personal details where allowed.

Our guide on [deleting a user's data in Supabase for GDPR](https://launchstudio.eu/en/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr) covers erasure in detail.

## Soft Delete and Audit Logs

Soft delete and audit logs complement each other but are not the same. Soft delete keeps the record restorable for a period; audit logs record that a deletion happened, by whom and when, even after the record is purged. Use both: soft delete for recovery, audit logs for accountability.

## Performance

As soft-deleted rows accumulate, queries that filter on `deleted_at is null` need support:

- **Partial indexes** on active rows for common queries
- **Regular purges** so tables do not grow indefinitely with deleted data
- **Analysis of query plans** if large proportions of rows are deleted

## Testing

Test the full lifecycle:

- Delete a record as a user and confirm it disappears from all lists, searches, counts and exports.
- Confirm it cannot be accessed by ID through the API.
- Restore it and confirm it reappears with related data.
- Create a new record with the same unique value after deletion.
- Run the purge job and confirm data is permanently removed after the retention period.
- Process an erasure request and confirm personal data is removed or anonymised.

Search, counts and exports are where deleted rows most often leak back into view.

## Common Mistakes in AI-Built Apps

**Hard deletes with broad cascades,** removing far more than intended.

**Soft delete via application filters only,** with some queries forgetting the filter.

**Unique constraints blocking re-creation** after soft delete.

**No purge,** so "deleted" personal data stays forever.

**Deleted items still appearing in search, counts or exports.**

**No record of who deleted what.**

## How LaunchStudio Helps

LaunchStudio designs deletion behaviour for AI-built SaaS: deciding per entity between soft and hard deletion, implementing soft delete with Row Level Security or views, partial unique indexes, safe cascade rules, trash and restore features, scheduled purges, GDPR erasure and anonymisation flows, and audit logging of deletions.

The **Launch Ready** package (€800-€3,500) covers deletion redesign along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, designing data lifecycles for enterprise systems. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Project Tool Where One Click Deleted Eighteen Months of Work

Pieter Kuiper built Bouwplanner with Bolt and Supabase: a planning tool for small construction and renovation companies, with projects, phases, tasks, photos and client communication. One morning, a project manager at a customer accidentally deleted a client record while trying to remove a duplicate. Because the schema used `on delete cascade` everywhere, the deletion removed four projects, over 600 tasks, around 1,200 photos references and all messages with that client, covering eighteen months of work.

Restoring meant a point-in-time recovery of the whole database to a copy, then manually extracting and reinserting the affected records, which took two days of engineering work. The customer was understandably shaken. A review showed the same risk across the app: every delete was a hard delete, there was no confirmation for deletions with large impact, no audit trail and no way for users to undo mistakes.

LaunchStudio introduced soft delete for clients, projects, phases, tasks, documents and messages, with `deleted_at` and `deleted_by` columns, Row Level Security policies hiding deleted rows from regular queries and a database function that soft-deleted a client together with its related records in one transaction. Cascades were replaced with restrictive foreign keys except for genuinely dependent data. Partial unique indexes allowed re-creating items with the same names, and a trash view let admins restore deleted items with their related data. Deletions with large impact showed a confirmation summarising what would be affected, an undo button appeared for ten seconds, a nightly job permanently deleted items older than 60 days in the trash, and all deletions were written to an audit log.

**Result:** In the following six months, users restored around 140 items from the trash themselves, without contacting support. Pieter has not needed a database restore since, and the customer who lost data became one of his references, citing how the problem was handled.

> *"A single click shouldn't be able to erase a year and a half of someone's work. Now it can't, and when people make mistakes, they fix them themselves."*
> - **Pieter Kuiper, Founder, Bouwplanner (Zwolle)**

**Cost & Timeline:** €3,300 (Launch Ready package: data recovery, soft delete with RLS, cascade redesign, trash and restore, purge job and audit logging) - completed in 9 business days.

## Frequently Asked Questions

### Should my SaaS use soft delete or hard delete?

For important business records, soft delete with a retention period is usually best, because it enables restore and investigation. For disposable data and for erasure after retention periods, hard delete is appropriate. Many products combine both: soft delete first, permanent deletion later.

### Is soft delete compliant with GDPR?

Soft delete alone does not satisfy erasure obligations, because the data still exists. It is compatible with GDPR if soft-deleted personal data is permanently deleted or anonymised after a defined, documented period, and if erasure requests are handled by actually removing data, subject to legal retention requirements.

### How do I hide soft-deleted records in Supabase?

Use Row Level Security policies that only return rows where `deleted_at` is null for regular users, or views that select only active rows. Avoid relying on every query to add the filter, since new queries, including AI-generated ones, may forget it.

### How does Manifera's experience help with data lifecycle design?

Manifera has designed data lifecycles for enterprise systems for 11+ years, balancing recovery, compliance and performance. LaunchStudio applies that experience so deletion in AI-built apps is safe for users, defensible in disputes and compliant with privacy rules.

### Does deletion design affect my product's reputation and visibility?

Indirectly. Data loss incidents damage trust and generate negative reviews, while easy restore features earn goodwill. Products that handle customer data carefully accumulate the positive reputation signals that buyers, search engines and AI answer engines draw on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should my SaaS use soft delete or hard delete?",
      "acceptedAnswer": { "@type": "Answer", "text": "Soft delete with retention for important records, hard delete for disposable data and after retention periods; many products combine both." }
    },
    {
      "@type": "Question",
      "name": "Is soft delete compliant with GDPR?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not alone; purge or anonymise soft-deleted personal data after a documented period and handle erasure by actually removing data." }
    },
    {
      "@type": "Question",
      "name": "How do I hide soft-deleted records in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use RLS policies or views that return only rows where deleted_at is null, rather than relying on each query." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with data lifecycle design?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has designed enterprise data lifecycles for 11+ years, making deletion safe, defensible and compliant." }
    },
    {
      "@type": "Question",
      "name": "Does deletion design affect my product's reputation and visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly; avoiding data loss and offering restore builds reputation signals buyers and AI engines draw on." }
    }
  ]
}
</script>
