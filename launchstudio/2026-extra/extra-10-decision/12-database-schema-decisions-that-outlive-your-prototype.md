---
Title: "Database Schema Decisions That Outlive Your Prototype"
Keywords: nullable columns database design, missing foreign keys, reversible database migrations, renaming a column in production, database schema design AI prototype, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Database Schema Decisions That Outlive Your Prototype

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Database Schema Decisions That Outlive Your Prototype",
  "description": "A technical look at the schema decisions an AI-generated database quietly gets wrong — nullable columns, missing indexes and foreign keys, irreversible migrations, and the true cost of renaming a column after launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/database-schema-decisions-that-outlive-your-prototype" }
}
</script>

Here's a claim most founders won't like: your frontend can be rewritten in a weekend, your auth provider can be swapped in an afternoon, and your hosting can migrate over a long lunch break — but your database schema, once real rows exist in it, is the one part of your stack you will be living with for years. Every other layer can be replaced without touching customer data. The schema *is* the customer data's shape, and reshaping it live is where "quick fix" projects go to become three-week projects.

AI page-builders generate schemas that pass every test a demo runs, because a demo never renames a column under load, never has a NULL where a constraint should have caught it, and never runs a migration that can't be rolled back. Production does all three, eventually. Here's what to check before it does.

## Nullable by Default: The Setting Nobody Chose

Ask most schema generators why a column is nullable and the honest answer is "because nobody said it shouldn't be." `NOT NULL` is a decision, and skipping it is also a decision — just one made by omission, and it's the default in almost every AI-generated migration.

The cost shows up gradually. A `users.email` column that's nullable lets a bug in your signup flow insert a user with no email, which then breaks your password reset and your transactional email in ways that look like *those* systems' bugs rather than the schema decision that permitted the bad row in the first place. An `orders.total_cents` column that's nullable means a `SUM()` across orders silently skips the NULL rows instead of erroring, and your revenue dashboard is quietly wrong for a percentage of orders nobody can identify without a manual audit.

The fix, done before launch, costs nothing: walk every table and ask, for each column, "can this legitimately be unknown, or is NULL standing in for 'the code path that should have set this has a bug'?" Genuinely optional fields — a middle name, an optional referral code — stay nullable. Everything the business logic depends on being present gets `NOT NULL`, plus a sensible default where one exists (`created_at timestamptz not null default now()`), so the database enforces the invariant instead of hoping every code path remembers to.

## Missing Indexes and Foreign Keys: The Two Silent Killers

These are different problems that get discovered at the same moment — the day your product has enough rows for either to matter, usually somewhere between 10,000 and 100,000 records, right when things should be getting *easier*, not harder.

**Missing indexes** don't cause errors. They cause a query that runs in 4ms on your seed data at 50 rows and 4 seconds on production at 500,000 rows, because Postgres is doing a full table scan every time. AI-generated schemas rarely add indexes beyond the primary key, because nothing in a demo dataset makes the difference visible. The columns that need one, as a baseline: any foreign key column (Postgres does not auto-index these, unlike the primary key side), any column used in a `WHERE` clause on a table that will grow (`status`, `user_id`, `created_at` for date-range queries), and any column used in `ORDER BY` on a paginated list.

**Missing foreign key constraints** don't slow anything down — they let your data become quietly inconsistent. Without a foreign key from `orders.user_id` to `users.id`, deleting a user leaves orphaned orders sitting in the table, referencing a user that no longer exists, until some report or join breaks trying to look it up. AI-generated schemas frequently model the *relationship* — the column is there, named correctly, populated correctly in the happy path — without the *constraint* that would stop a bad delete, a bad import, or a race condition from breaking it. Adding the constraint costs one line in a migration and, going forward, makes an entire category of bug structurally impossible rather than merely unlikely.

## Reversible Migrations: The Insurance You Only Notice You Skipped Once

A migration framework — Prisma Migrate, Rails migrations, Django migrations, raw SQL migration files — draws a distinction that AI-generated database work routinely ignores: every `up` should have a working `down`. Most prototype-era migrations are written once, applied once, and never tested in reverse, because nobody has needed to reverse one yet.

The day you need it is the day a migration goes out with a bug — a new `NOT NULL` column with no default that locks a large table, an index build that times out, a column type change that silently truncates data — and the fastest safe response is "roll it back while we fix it," not "write and test a second migration to undo the damage while production is degraded." A migration you can't reverse turns every deploy into a one-way door.

Two related habits matter as much as reversibility itself. First, **additive migrations before destructive ones**: when changing a column's type or splitting one column into two, add the new structure, backfill it, switch the application to use it, and only then drop the old structure in a later migration — never in the same step, because that removes your ability to roll back without data loss. Second, **never running a migration that locks a large table during business hours** — adding a `NOT NULL` column with a default on a multi-million-row Postgres table historically required a full table rewrite; modern Postgres (11+) handles constant defaults efficiently, but a computed default, a new index, or a type change often still doesn't, and testing this against a realistic data volume before deploying is the only way to find out before your users do.

## The Real Cost of Renaming a Column After Launch

This is the decision founders most underestimate, because renaming a column in a local database takes four seconds. Renaming one in production, safely, does not.

The naive approach — `ALTER TABLE users RENAME COLUMN email TO email_address` — breaks every query, every ORM model, and every API response your live application currently sends, the instant it runs, for every request in flight during the deploy. There is no version of "just rename it" that doesn't involve downtime or broken requests unless you do it in stages.

The safe sequence: add the new column alongside the old one, write to both on every insert and update (a brief dual-write period), backfill existing rows from old to new, deploy application code that reads from the new column while the dual-write continues, verify nothing still reads the old column, then drop the old column in a final migration once you're confident. That's four to five deploys for what looks, on a whiteboard, like a rename. Multiply that by every column name an AI tool chose that doesn't match your actual domain language — `data` instead of `payload`, `type` instead of `subscription_tier`, `name` on a table that turns out to need `first_name` and `last_name` — and "clean up the naming later" becomes a multi-week project with a nonzero chance of a bad backfill silently losing data in the gap between stages.

The mitigation is upstream: before you have real users, spend one afternoon reading your schema like a stranger would, renaming what needs renaming while it's a single-statement change instead of a five-deploy migration.

## Timestamps, Soft Deletes, and the Audit Trail You'll Wish You Had

Two related decisions that cost nothing at schema design time and are expensive to retrofit: whether every table tracks `created_at` and `updated_at`, and whether deletion is soft or hard.

AI-generated schemas usually add `created_at` and skip `updated_at`, which means the moment you need to answer "when did this record last change" — for a support ticket, a billing dispute, or debugging a sync issue — the honest answer is "we don't know, we never recorded it." Adding it now, for every row created going forward, is trivial; backfilling an accurate value for every row that already exists is not possible after the fact, because the information was simply never captured.

Hard deletes (`DELETE FROM orders WHERE id = ...`) are the default in most generated CRUD code, and they're fine for genuinely disposable data. They're a liability for anything a support conversation, a legal request, or your own debugging will need later — a cancelled subscription, a deleted account, a removed team member. A `deleted_at timestamptz` column and a habit of filtering `WHERE deleted_at IS NULL` in application queries turns "we accidentally deleted a customer's data and it's gone" into "we can restore it," at the cost of one column and one `WHERE` clause repeated consistently.

## A Practical Pre-Launch Schema Audit

Run this against your actual schema, not from memory — export it with `\d+` in `psql` or your ORM's schema dump, and go table by table.

For every column: is it `NOT NULL` where the business logic requires a value? Does it have an appropriate default? For every foreign key relationship implied by a column name (`user_id`, `order_id`): does an actual foreign key constraint exist, and does it specify `ON DELETE` behavior (`CASCADE`, `RESTRICT`, or `SET NULL`) deliberately rather than by accident? For every column used to filter or sort a growing table: is there an index? For every migration in your history: does a tested `down` migration exist, and was a rename ever done in a single step rather than staged? For every table: does it record `created_at` and `updated_at`, and is deletion soft where the data might matter later?

None of this requires exotic tooling. It requires one afternoon and the discipline to fix what the audit finds before, not after, the schema has real rows depending on its current shape.

## When It's Worth Paying Someone Else to Do This

A solo founder reviewing their own schema has a specific blind spot: the columns that feel obviously fine are the ones an outside reviewer flags first, because "obviously fine" usually means "I wrote the code that reads it and I know its quirks," which is exactly the knowledge a new hire, a future you, or an integration partner won't have. This is squarely inside LaunchStudio's Launch Ready scope — a schema and migration review is one to two days of focused work, well within the €800–€3,500 band, and it's the single highest-leverage review to run before you have production data that constrains what you can still change for free.

[Manifera's engineering team](https://www.manifera.com/services/custom-software-development/) has spent 11 years watching exactly this category of decision get deferred under demo pressure and paid for later at ten times the cost — which is the whole reason this kind of review exists as a standalone, fixed-price engagement rather than a footnote in a bigger rebuild.

## Fixing It Before the Data Makes It Expensive

A schema decision made with zero rows in the table costs a single migration. The same decision made with 200,000 rows costs a staged, multi-deploy migration and real risk of downtime or data loss along the way. The window where this is cheap is short and closes the moment your product has real users — which is exactly the window most AI-generated prototypes are sitting in right now, and most founders don't realize it. [Talk to an engineer who reads AI-generated code](https://launchstudio.eu/en/#contact) about your schema before that window closes.

## Real example

### An Indie Hacker Finds Out What a Missing Foreign Key Actually Costs

Elin Andersson built Ferndesk, a booking tool for small therapy practices, using Cursor with a Postgres database on Supabase. The schema had an `appointments` table with a `client_id` column, populated correctly by the AI-generated code in every normal flow — but no actual foreign key constraint linking it to the `clients` table.

It surfaced when Elin built a "merge duplicate client" feature for practices whose clients had signed up twice under slightly different emails. The merge deleted the duplicate client row and moved its data into the primary one — but with no foreign key constraint, nothing stopped it, and nothing warned her that fourteen appointment records still pointed at the now-deleted `client_id`. Those appointments silently disappeared from every practice's calendar view, which joined against `clients` and dropped any row where the join found nothing.

The fix added the missing foreign key with `ON DELETE RESTRICT`, which immediately surfaced the fourteen orphaned rows already in production so they could be manually reassigned, then made it structurally impossible for a future merge, import, or admin action to create the same problem again.

**Result:** the fourteen missing appointments were recovered and reassigned within a day, and the constraint has silently blocked three further attempted deletes-with-dependents since, each one logged instead of executed.

> "The AI wrote code that used the relationship correctly every time I tested it. It just never told me the database itself didn't know the relationship was supposed to be enforced."
> — **Elin Andersson, Founder, Ferndesk (Malmö)**

**Cost & Timeline:** Launch Ready engagement, schema and migration audit — delivered in 4 business days.

## Frequently Asked Questions

### How do I check whether my Postgres tables actually have foreign key constraints?

Run `\d+ tablename` in `psql` for each table and look at the "Foreign-key constraints" section, or query `information_schema.table_constraints` filtered to `constraint_type = 'FOREIGN KEY'`. If a column is clearly a reference to another table's ID but doesn't show up there, the relationship exists only in your application code, not in the database.

### Will adding indexes to an existing production table cause downtime?

Not if you use `CREATE INDEX CONCURRENTLY` in Postgres, which builds the index without holding a lock that blocks writes. It takes longer than a regular index build and can't run inside a transaction block, but it's the correct default for any index added to a table already receiving production traffic.

### Is it too late to fix nullable columns once I have real data?

No, but it takes an extra step: you need to backfill or clean up any existing NULL values before you can add the `NOT NULL` constraint, since Postgres will reject the constraint otherwise. Decide what a missing value should mean for existing rows — a default, a computed value, or manual review — before running the migration.

### How often should I actually revisit my schema before launch?

Once, seriously, before you have your first real users, and then again whenever you add a feature that changes how a table is used rather than just adding a column to it — a new relationship, a new access pattern, or a new scale of data you weren't designing for originally.

### Does LaunchStudio rebuild the whole database, or just review it?

Typically just review and fix — LaunchStudio's model keeps your existing frontend and data model intact wherever possible, applying targeted migrations for the specific gaps found rather than a wholesale rebuild, which is both faster and lower-risk for data you already depend on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I check whether my Postgres tables actually have foreign key constraints?", "acceptedAnswer": { "@type": "Answer", "text": "Run \\d+ tablename in psql and check the foreign-key constraints section, or query information_schema.table_constraints filtered to FOREIGN KEY. If a column clearly references another table's ID but isn't listed, the relationship only exists in application code." } },
    { "@type": "Question", "name": "Will adding indexes to an existing production table cause downtime?", "acceptedAnswer": { "@type": "Answer", "text": "Not if you use CREATE INDEX CONCURRENTLY in Postgres, which builds the index without holding a write-blocking lock. It takes longer and can't run inside a transaction, but it's the correct approach for a table already receiving production traffic." } },
    { "@type": "Question", "name": "Is it too late to fix nullable columns once I have real data?", "acceptedAnswer": { "@type": "Answer", "text": "No, but existing NULL values need to be backfilled or resolved before Postgres will accept a NOT NULL constraint. Decide what a missing value should mean for existing rows before running the migration." } },
    { "@type": "Question", "name": "How often should I actually revisit my schema before launch?", "acceptedAnswer": { "@type": "Answer", "text": "Once seriously before your first real users, and again whenever a new feature changes how a table is used rather than just adding a column — a new relationship, access pattern, or data scale you weren't originally designing for." } },
    { "@type": "Question", "name": "Does LaunchStudio rebuild the whole database, or just review it?", "acceptedAnswer": { "@type": "Answer", "text": "Typically just review and fix. LaunchStudio keeps the existing data model intact wherever possible, applying targeted migrations for specific gaps rather than a wholesale rebuild, which is faster and lower-risk for data you already depend on." } }
  ]
}
</script>
