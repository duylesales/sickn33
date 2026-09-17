---
Title: "Lovable Supabase Migrations: Changing Your Schema After Launch"
Keywords: lovable supabase, supabase security, database migration live data, backfill strategy, schema change downtime, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase Migrations: Changing Your Schema After Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase Migrations: Changing Your Schema After Launch",
  "description": "Changing a database schema is free before launch and consequential afterwards. The three kinds of change, why transformative ones need two deployments, how to backfill safely, and the routine that keeps migrations boring.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-migrations-after-launch" }
}
</script>

Before launch, changing your database is a five-second decision. Rename a column, drop a table, restructure a relationship — nothing exists yet, and the worst outcome is that you regenerate some code.

After launch, the same action carries every record your customers have created, and the difference in consequence is total. A rename that takes five seconds can produce an application that cannot read its own data, a booking flow that fails for everyone mid-transaction, and no obvious way back other than a backup that may be hours old.

This is the discipline that turns that from a frightening act into a routine one. None of it is complicated; all of it is absent from AI-built projects by default, because nothing about describing a product to a tool implies that the shape of its data will ever change.

## Why It Gets Scary Precisely When It Matters

Three things change on launch day.

**There is data you cannot recreate.** Customer records, uploaded files, historical transactions. The cost of a mistake stops being your time.

**The application is running while you change it.** For a period — seconds or minutes — the code deployed and the schema in the database disagree with each other, and requests arriving during that window hit an inconsistent system.

**Rollback is no longer symmetric.** Reverting code is easy. Reverting a schema change that has already transformed data is frequently impossible, because the original values no longer exist.

That last asymmetry is the heart of it, and it explains why the safe approaches all avoid destroying information until the new arrangement is proven.

## The Three Kinds of Change

Almost every schema change falls into one of three categories, and knowing which one you are making determines the procedure.

**Additive.** A new column, a new table, a new index. Nothing existing is altered. The application ignores it until the code that uses it ships.

**Transformative.** Splitting a name field into two, changing a type, moving a relationship, renaming something. The data exists and must end up in a different shape.

**Destructive.** Dropping a column or table, removing a constraint, deleting rows. Information disappears.

Additive changes are nearly free. Transformative ones need care. Destructive ones need patience, and they are the ones founders perform casually because they look like tidying.

## Additive Changes Are Nearly Free

Add the column as nullable or with a sensible default, deploy it, and nothing breaks — running code does not know it exists.

Two details keep it that way. Avoid adding a column with a mandatory value and no default to a table with existing rows, because the database cannot decide what to put in them. And add indexes deliberately: on a large table, creating an index can lock writes for the duration unless created concurrently, which turns a harmless improvement into an outage.

## Transformative Changes Need Two Deployments

This is the pattern worth internalising, because it converts the most dangerous category into a sequence of safe steps. It is usually described as expand and contract.

**Step one: expand.** Add the new structure alongside the old. Both exist; nothing is removed.

**Step two: write to both.** Deploy code that writes new data to both the old and the new shape while still reading from the old. Your application is now producing correct data in both places.

**Step three: backfill.** Copy existing rows into the new shape, in batches, while the application keeps running.

**Step four: switch reads.** Deploy code that reads from the new structure. The old one is still there and still current, so if anything is wrong you revert the code and nothing is lost.

**Step five: contract.** Once you are confident — days, not minutes — stop writing to the old structure and eventually remove it.

Five deployments instead of one. In exchange, at no point does a failure destroy data, and at every point you can go back by reverting code rather than by restoring a backup.

## Destructive Changes Need a Waiting Period

Dropping something is the one action with no undo.

The safe sequence is to stop using it first, wait, then remove it. Rename it to something obviously deprecated, deploy code that no longer references it, and leave it in place for a week or two while you confirm nothing broke. A column nobody reads costs almost nothing to keep; a column you dropped and needed is a restore from backup with everything since it lost.

Before dropping anything, search your entire codebase for its name — including generated code, scheduled jobs, reports and exports, which are the places references hide.

## Migrations Belong in the Repository

The single most consequential habit, and the one AI-built projects most often lack.

Schema changes made by clicking in a dashboard exist nowhere except in that database. The consequence is that your staging environment and your production environment drift apart silently, a new developer's local setup does not match reality, and nobody can say what changed or when.

Schema changes written as migration files in your repository are reviewable, reproducible in every environment, and visible to both the next engineer and the AI tool you prompt. They also give you a history: when something behaves oddly, "what changed in the database last Tuesday" becomes an answerable question.

## The Backfill Problem

Transforming existing rows is where migrations take longer than expected.

**Batch it.** Updating a million rows in one statement locks the table and blocks your application. Updating them in batches of a few thousand, with a pause between, keeps the product responsive.

**Make it resumable.** Record progress, so a failure halfway does not mean starting over or double-processing.

**Make it safe to run twice.** Backfills get interrupted and rerun. The operation should reach the same end state either way.

**Run it outside peak hours,** and know how long it took in staging before running it in production.

**Verify afterwards** by counting: rows transformed against rows expected, and a sample checked by hand.

## Testing Against Realistic Data

A migration tested against forty tidy rows tells you the syntax is valid and nothing else.

Test against a copy of production — anonymised if it contains personal data — with the volume and the messiness your real database has: nulls where you did not expect them, duplicates, text in numeric-looking fields, encodings from an import someone did in month two. This is where migrations actually fail, and finding it in staging costs an afternoon rather than a customer-facing outage.

Time it while you are there. A backfill that takes four minutes on a copy and eleven on production is fine; one that takes four minutes on a tenth of the data is a surprise you want in advance.

## What Goes Wrong Most Often

- A column renamed in the dashboard while the deployed code still reads the old name.
- A mandatory column added to a table with existing rows, failing on arrival.
- An index created on a large table during business hours, locking writes.
- A backfill run in one statement, blocking the application for minutes.
- A column dropped that a scheduled job still referenced, breaking something nobody noticed for a week.
- Staging and production diverging until a migration that worked in one fails in the other.

Every one of these is procedural rather than technical, which is why a routine fixes them.

## A Migration Routine That Stays Boring

Write it as a file in the repository. Classify it: additive, transformative or destructive. Use expand and contract for anything transformative. Test against a realistic copy and record the timing. Take a backup immediately before running it, and know how long a restore takes. Run backfills in batches, outside peak. Verify with counts and a manual sample. Wait before dropping anything. And write one line in your deployment log saying what changed.

Ten minutes of process around a change that might take one minute to execute — which is the correct ratio once other people's data is involved.

## Getting the Foundations in Place

Most AI-built products do not need a migration expert; they need the schema captured in the repository, a staging environment with realistic data, a backup they have tested restoring, and a rehearsed routine for the first few changes.

LaunchStudio sets that up as part of taking a product live: existing schema captured as migrations so the repository becomes the source of truth, staging built with anonymised or generated data, backups verified by restoring, and the expand-and-contract pattern applied to whichever change you are facing — without touching the interface you built in Lovable.

The engineers are Manifera's: eleven years of production database work for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City. [Describe your project](https://launchstudio.eu/en/#contact) and you will get a straight answer about whether your next schema change is safe, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Telling Users, When It Matters

Most migrations are invisible and need no announcement. Three cases are worth communicating.

**Anything they will see.** A field split into two, a category renamed, a value recalculated. If the change alters what appears on their screen, a sentence in advance prevents a support message and a suspicion that something broke.

**Planned unavailability.** If a change genuinely requires a pause — rare with expand and contract, occasionally unavoidable — give a date, a duration and a reason, and choose a time based on your traffic rather than your convenience.

**Anything affecting their own records.** A correction, a deduplication, a retention deletion. People are considerably more accepting of a change to their data announced beforehand than of the same change discovered afterwards.

Two sentences is enough in each case. The purpose is not transparency for its own sake; it is that a customer who was told about a change interprets an oddity as the change, while one who was not interprets it as your product being unreliable.

## Real example

### A Rename That Took a Booking Platform Down for Forty Minutes

Joost Brand ran Ruimteplan in Lovable: a room-booking tool used by eleven community centres around Almere, with around 9,000 bookings in the database.

He needed to split a single `contact` field into a name and a phone number. On a Tuesday afternoon he renamed the column in the Supabase dashboard and added two new ones, intending to deploy the matching code immediately afterwards.

The deployment failed on a build error. For forty minutes, the live application queried a column that no longer existed, every booking page returned an error, and three centres phoned within the first ten minutes. He restored the old column name, which brought the app back, and discovered afterwards that bookings created during the window had been partially written.

Six business days of work followed: the existing schema captured as migration files so the repository became authoritative; a staging environment created with an anonymised copy of production; the field split redone properly using expand and contract — new columns added, code writing to both, a batched backfill of 9,000 rows verified by count and sample, reads switched, and the old column left in place for two weeks before removal; backups tested with a restore timed at 22 minutes; and a one-line deployment log introduced.

**Result:** the same split completed with no downtime, and the four schema changes since have each taken two deployments and gone unnoticed by the centres.

> *"I renamed a column. It felt like editing a spreadsheet. It took the booking system down for three community centres in the middle of the afternoon."*
> — **Joost Brand, Founder, Ruimteplan (Almere)**

**Cost & Timeline:** €2,450 (schema captured as migrations, staging with anonymised data, expand-and-contract field split, backup restore test) — completed in 6 business days.

## Frequently Asked Questions

### Can I just change my schema in the Supabase dashboard?

Before launch, yes. Afterwards it is the main cause of outages in small products, because the change exists nowhere except that database, environments drift apart, and deployed code can end up querying something that no longer exists.

### What is expand and contract?

A pattern for transformative changes: add the new structure alongside the old, write to both, backfill existing rows, switch reads to the new structure, and only remove the old one days later. It means a failure at any step is reverted by changing code rather than restoring data.

### How do I change a column without downtime?

Never rename in place on a live system. Add the new column, deploy code writing to both, backfill in batches, deploy code reading the new one, then drop the old column after a waiting period.

### Why do backfills cause problems?

Because updating many rows in a single statement locks the table and blocks the application. Batch the updates, make them resumable and safe to rerun, run them outside peak hours, and verify with counts afterwards.

### What should I do before running any migration on production?

Test it against a realistic copy with production-like volume and messiness, time it, take a backup immediately before, know how long a restore takes, and record what you changed in a deployment log.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just change my schema in the Supabase dashboard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before launch yes; afterwards it is a leading cause of outages, because the change exists only in that database, environments drift and deployed code can query something that no longer exists."
      }
    },
    {
      "@type": "Question",
      "name": "What is expand and contract?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Add the new structure alongside the old, write to both, backfill, switch reads, then remove the old one days later — so failures are reverted by changing code rather than restoring data."
      }
    },
    {
      "@type": "Question",
      "name": "How do I change a column without downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Never rename in place on a live system: add the new column, write to both, backfill in batches, switch reads, then drop the old column after a waiting period."
      }
    },
    {
      "@type": "Question",
      "name": "Why do backfills cause problems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Updating many rows in one statement locks the table and blocks the application; batch them, make them resumable and rerunnable, and verify with counts."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do before running any migration on production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Test against a realistic copy with production-like volume, time it, take a backup immediately before, know the restore time and log what changed."
      }
    }
  ]
}
</script>
