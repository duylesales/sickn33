---
Title: "Changing Your Database After Real Customers Are Using It"
Keywords: zero downtime migration, database migration production safely, schema change live customers, expand contract migration, backfill large table, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Changing Your Database After Real Customers Are Using It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Changing Your Database After Real Customers Are Using It",
  "description": "Before launch a schema change is a decision; after launch it is an operation performed on data people depend on. The expand-and-contract pattern, why a locked table takes a product offline, and how to change structure without a maintenance window.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/changing-your-database-after-real-customers-are-using-it" }
}
</script>

Before launch, changing your database structure is trivial: modify it, reset the data, carry on. After launch, the same change is an operation performed on records that people are actively reading and writing, that cannot be recreated, and that someone is depending on at the moment you run it. The instruction is identical. The consequences are not comparable.

This is the transition that catches founders whose products were built by AI tools, because the whole development experience up to that point trained the opposite instinct. Prompting a change to your schema during building is a five-second action. The first time you do it against live customer data with a mistaken assumption, you find out that a migration is a deployment with no undo.

## Why the Same Change Is Harder Now

Three things change the moment real data exists.

**The data must be preserved and transformed.** Splitting a `name` column into `first_name` and `last_name` is not a structure change; it is a structure change plus a rule for interpreting every existing value, including the ones with three words, a single word, or a company name.

**The application keeps running during the change.** For the seconds or minutes a migration takes, requests are still arriving. If the code expects the old structure and the database has the new one — or the reverse — those requests fail. On a large table, "seconds" can become "eleven minutes," and eleven minutes of failed requests is an outage.

**Mistakes are not reversible.** A dropped column takes its contents with it. The only recovery is a restore, which discards everything else that happened since — and if you have never tested a restore, this is a bad moment to discover its properties.

## Expand and Contract: The Pattern Worth Knowing

There is a standard approach that makes almost any schema change safe, and it works by never having the database and the code disagree.

Rather than changing a column in one step, do it in four:

**Expand.** Add the new structure alongside the old. Add `first_name` and `last_name`; leave `name` untouched. Nothing breaks, because nothing yet depends on the new columns.

**Write both.** Deploy code that writes to the old and the new structure simultaneously. Every new record now populates both. The application still reads from the old.

**Backfill.** Populate the new columns for existing rows, in batches, in the background. Nothing depends on the result yet, so it can take as long as it needs and can be paused or corrected if the transformation turns out to be wrong.

**Contract.** Once the new columns are complete and verified, deploy code that reads from them. Watch for a period. Only then remove the old column.

Each step is individually reversible, which is the entire point. If the backfill produces nonsense for names with prefixes, you notice before anything reads it, and no customer ever saw a wrong value. Compare that to the one-step version, where a bad transformation is discovered by a customer and the original data no longer exists.

The cost is that a change takes days instead of minutes, and that for a period the product carries both structures. For anything touching data you cannot recreate, that is a cheap price.

## The Lock Nobody Warns You About

There is a specific, avoidable way to take a product offline with a single line, and it catches people who have only ever worked with small tables.

Some schema operations require the database to lock the table while they run. On a table with 500 rows this is imperceptible. On a table with two million, the same operation may hold the lock for minutes, during which every query touching that table waits. Your application appears to hang, requests time out, and customers see a dead product — from a command that returned quickly in staging against a fraction of the data.

Which operations lock, and for how long, depends on your database and version. In modern Postgres, adding a nullable column is fast, adding one with a default has become much cheaper than it once was, but adding an index without the concurrent option locks writes for the duration, and changing a column's type generally rewrites the whole table. The practical rules: build indexes concurrently, add columns as nullable and populate separately, avoid type changes on large tables in favour of expand-and-contract, and always check the size of the table you are about to alter rather than assuming staging is representative.

## Test on Real Volume, Not Real Data

A migration tested against fifty rows tells you the syntax is valid and nothing else. The two things that matter — how long it takes and whether the transformation is correct for every value — only appear at scale and in variety.

The practical approach: restore a recent production backup into a separate environment and run the migration there, timing it. This gives you a genuine duration estimate and, more valuably, exposes the data you did not know you had. Real customer data always contains surprises: empty strings where you expected nulls, an email field containing two addresses separated by a semicolon, dates from 1900 that someone used as a placeholder, and text in a column your transformation assumes is numeric.

If your production data contains personal information, that copy is itself sensitive and belongs under the same protections as production, or should be anonymised before use — a detail that is easy to overlook when the goal is just to test a migration.

Every migration should also be paired, in advance, with a written answer to "what do I do if this goes wrong halfway?" For expand-and-contract steps the answer is usually simple. For anything irreversible, the answer needs to be established before you run it, not composed under pressure.

Running structural changes against live customer data without downtime is routine work for people who do it regularly and genuinely risky for people doing it for the first time. LaunchStudio, backed by Manifera's 11+ years of production engineering, plans and executes migrations on live products, including the backfills and staged deployments that keep customers from noticing. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Migrations Belong in Version Control, Not in a Console

A specific habit separates products that can be maintained from products that cannot: every schema change exists as a file in your repository, applied through a migration tool, in order, and never by typing into a database console.

Without this, nothing can be reproduced. A new environment cannot be created from scratch. Staging drifts from production in ways nobody can enumerate. And the answer to "when did this column appear and why" is lost permanently.

This is a common weak point in AI-generated products, where schema changes are often made through a platform's visual editor or by an assistant modifying the database directly. Both leave no history. Bringing an existing product into a proper migration workflow starts with capturing the current schema as a baseline — a day of work that pays back the first time you need a second environment, and a prerequisite for any staged rollout.

## Real example

### The Index That Took the Product Down for Nine Minutes

Lieke Groothuis ran Rittenboek, a trip-registration tool for Dutch delivery firms, built in Cursor. Trip queries had grown slow, and the fix was clear: add an index on the trips table.

She ran it during a quiet evening. In staging, against 900 rows, it had completed instantly. Production held 2.4 million trips, and the index build locked writes for just over nine minutes. Drivers finishing evening shifts could not register trips; the application returned timeouts. Two customers phoned. One driver's tablet retried enough times to create four duplicate entries once the lock released.

The subsequent review found a second, larger risk waiting: a planned change to split a combined address field into separate columns, written as a single migration that would drop the original after transforming it, tested against the same 900 staging rows.

**Result:** the index rebuilt concurrently without locking, migrations moved into version control with a captured baseline, a policy of testing every migration against a restored production copy for timing, and the address change re-planned as expand-and-contract. The backfill duly revealed 3,100 addresses the transformation handled incorrectly — found before anything read the new columns.

> "Nine minutes offline from one line that had taken half a second on my laptop. The staging database was a thousandth the size and I had never thought about what that meant."
> — **Lieke Groothuis, Founder, Rittenboek**

**Cost & Timeline:** migration workflow and staged schema change delivered in 3 business days.

## Frequently Asked Questions

### Why is a schema change riskier after launch than before?

Because existing data must be preserved and transformed, the application keeps serving requests during the change, and mistakes are not reversible without a restore that discards everything since.

### What is expand and contract?

Adding the new structure alongside the old, writing to both, backfilling existing rows in the background, switching reads to the new structure, and only then removing the old. Each step is individually reversible.

### Can adding an index take my product offline?

Yes. A standard index build locks writes on the table for its duration, which is imperceptible on small tables and minutes on large ones. Building indexes concurrently avoids the lock.

### How should migrations be tested?

Against a restored copy of production, for both timing and correctness. Real data contains values that small test sets do not, and duration only becomes visible at real volume.

### Is it acceptable to change the schema through a database console?

No, beyond emergencies. Changes made outside version-controlled migrations leave no history, cannot be reproduced in a new environment, and cause staging to drift from production in ways nobody can enumerate.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why is a schema change riskier after launch than before?", "acceptedAnswer": { "@type": "Answer", "text": "Existing data must be preserved and transformed, the application keeps serving requests during the change, and mistakes are not reversible without a restore that discards everything since." } },
    { "@type": "Question", "name": "What is expand and contract?", "acceptedAnswer": { "@type": "Answer", "text": "Adding new structure alongside the old, writing to both, backfilling in the background, switching reads to the new structure, and only then removing the old. Each step is individually reversible." } },
    { "@type": "Question", "name": "Can adding an index take my product offline?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. A standard index build locks writes for its duration, imperceptible on small tables and minutes on large ones. Building concurrently avoids the lock." } },
    { "@type": "Question", "name": "How should migrations be tested?", "acceptedAnswer": { "@type": "Answer", "text": "Against a restored copy of production, for both timing and correctness, since real data contains values small test sets do not and duration only appears at real volume." } },
    { "@type": "Question", "name": "Is it acceptable to change the schema through a database console?", "acceptedAnswer": { "@type": "Answer", "text": "Not beyond emergencies. Changes outside version-controlled migrations leave no history, cannot be reproduced in a new environment, and cause staging to drift from production." } }
  ]
}
</script>
