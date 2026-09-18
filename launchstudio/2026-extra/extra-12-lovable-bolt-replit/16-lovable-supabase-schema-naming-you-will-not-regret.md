---
Title: "Lovable Supabase: Schema Naming You Will Not Regret"
Keywords: lovable supabase, schema design, naming conventions, database modelling, technical debt, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Supabase: Schema Naming You Will Not Regret

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Schema Naming You Will Not Regret",
  "description": "An AI-built database accumulates three names for the same idea. Why inconsistent naming makes every later change expensive, the conventions worth fixing early, and how to rename without downtime.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-schema-naming-you-will-not-regret" }
}
</script>

Open the table list of a Lovable project that has been extended for a year and you will find `users`, `profiles`, `user_profiles` and `customer`. Three of them have a name column, spelled three ways. One of them is empty and nobody remembers why it exists.

This is not carelessness. It is what happens when a schema is built one request at a time by a tool with no memory of the requests before, each of which produced something reasonable in isolation. The result is a database where knowing what a thing is called requires knowing when it was added.

It matters for one practical reason. Every future change — by you, by a contractor, by another AI session — starts with understanding what is there, and an inconsistent schema makes that expensive every single time.

## What Inconsistency Actually Costs

Three costs, and the third is the one founders feel.

Queries become guesswork: is the column `created_at`, `createdAt`, `date_created` or `inserted_at`? Every join needs checking rather than knowing, and mistakes are silent when two similarly named columns both exist.

Tooling degrades. Generated types, admin panels and API layers all read your schema, and what they produce reflects what they find. Inconsistent input, inconsistent output, in every consumer.

And AI assistance gets worse, which is the compounding one. An agent working on a clean schema infers the pattern and follows it. An agent working on an inconsistent one has no pattern to follow, so it invents a fourth convention — and next quarter you have four. The schema teaches whoever works on it next, including the machine.

## Conventions Worth Adopting

Any consistent set beats an inconsistent one. If you have no preference, these are conventional in Postgres and will not surprise anyone.

**Tables named in the plural, lower case, words separated by underscores:** `invoices`, `project_members`. Mixed case in Postgres requires quoting forever, which is a small annoyance repeated for the life of the product.

**Primary key called `id`.** Foreign keys named for what they reference plus `_id`: `organisation_id`, `invoice_id`. A join you can write without looking anything up.

**Timestamps `created_at` and `updated_at`**, always with time zone, always in UTC. Never a bare date-time without a zone; the day your first customer in another country appears is the day that decision costs you.

**Booleans phrased positively:** `is_active` rather than `is_not_disabled`. Negative names produce double negatives in queries and a bug nobody sees while reading.

**One name per concept across the whole schema.** If the entity is an organisation, it is never also a company, an account or a tenant. Pick the word your customers use and use it everywhere, including in your code and interface.

## Say What a Column Means, Not What It Holds

The names that cause the most trouble are the vague ones: `status`, `type`, `data`, `value`, `flag`.

A column called `status` on five tables means five different things, and the query joining two of them is unreadable. `invoice_status`, or better, a name describing the actual dimension — `payment_state`, `approval_state` — is worth the extra characters.

Similar care with amounts. `amount` invites the question everyone eventually asks at the wrong moment: is it in euros or cents, and does it include VAT? `amount_cents_excl_vat` is ugly and answers the question permanently. Money stored as a floating point number is its own article; store it as an integer of minor units or as a decimal, never as a float.

And avoid columns whose meaning depends on another column's value. A `value` column holding a number when `type` is one thing and a date when it is another is a design that cannot be constrained, indexed or trusted.

## The Structural Problems Hiding Behind Names

Sometimes bad names are a symptom. Three patterns are worth looking for while you are in there.

**Duplicated entities.** `users`, `profiles` and `customers` all holding a name and an email means the same person exists three times and can disagree with themselves. One table, with the extra fields where they belong.

**Comma-separated lists in a text column.** A `tags` column containing "urgent,finance,q3" cannot be indexed, filtered reliably or constrained. It needs to be its own table, and converting it later is more work than doing it now.

**Missing foreign keys.** An `organisation_id` column that is not declared as a foreign key permits rows pointing at organisations that do not exist, and AI-generated schemas omit the declaration regularly. Adding them finds the orphans you already have, which is unpleasant and better than not knowing.

## Renaming Without Breaking Anything

The reason people live with bad names is fear of the rename, and the fear is reasonable if you do it in one step.

The safe sequence has four stages and no downtime. Add the new column. Change the application to write to both old and new, and backfill the existing rows. Change every read to use the new column and deploy. Then, once you are confident, drop the old one in a later release.

The same works for tables: create the new one, write to both, migrate reads, remove the old. For a small product each stage is minutes, and at no point do the running code and the database disagree.

What to avoid is renaming in place while the previous version of your application is still running, which is the classic way to take a product down during a deploy that looked trivial.

## How Far Is Worth Going

You do not have to fix everything, and a founder with customers should not spend a week on tidiness.

Prioritise by what you touch. The tables behind your main screens, the ones a contractor will meet first, and anything you are about to build on: fix those. A legacy table written once by a feature nobody uses can keep its odd names forever.

The other prioritisation is by danger. Ambiguous money columns, missing foreign keys, timestamps without time zones and duplicated entities are correctness problems wearing a naming costume. Those are worth fixing regardless of how often you look at them.

## Write It Down Where the Tools Will Find It

Once conventions exist, record them in the repository — a short file, ten lines, stating the rules.

This is what makes them survive. A human contractor reads it. An AI assistant reads it too, if your project keeps a rules or instructions file, and the difference in what a coding agent produces when it has been told the conventions is substantial and immediate.

Include the vocabulary as well as the syntax: the words your product uses for its concepts, and the words it deliberately does not. That single paragraph prevents the fourth synonym from being introduced.

## Identifiers: The Choice You Make Once

One schema decision is genuinely hard to reverse, and AI tools make it for you without mentioning it: what your primary keys are.

Sequential integers are compact, sort naturally and read easily in a support conversation. They also reveal your volume — a customer whose invoice is numbered 412 knows roughly how many invoices you have issued — and they make identifiers guessable, which matters for anything that appears in a URL.

Random identifiers such as UUIDs do not leak anything and can be generated by the client before a row exists, which simplifies some flows. The older random variants scatter writes across an index, which hurts on large tables; the newer time-ordered ones avoid that and are the sensible default for a new project.

The practical middle ground that most products end up wanting: a random identifier as the primary key, plus a separate human-facing reference for things people talk about — an invoice number, a ticket number, an order code — generated from its own counter and formatted for reading aloud over the phone.

Decide this early, because changing a primary key type on a table with real data and several foreign keys pointing at it is one of the few migrations that is genuinely painful rather than merely tedious.

## Setting This Up

For an existing project this is typically one to two days: a full inventory of tables and columns with duplicates and synonyms identified, a chosen convention documented in the repository, high-traffic tables renamed through the add-write-both-migrate-drop sequence, duplicated entities consolidated, comma-separated lists normalised into their own tables, missing foreign keys declared with orphan data resolved, timestamps corrected to time zone aware UTC, money columns given unambiguous names and correct types, and generated types and admin tooling regenerated so everything downstream reflects the new schema.

LaunchStudio does this when taking over an AI-built codebase, because every other piece of work goes faster afterwards. The engineers are Manifera's: eleven years, 160+ projects, and a great many schemas inherited from someone else.

[Send us your table list](https://launchstudio.eu/en/#contact) and we will tell you where the duplicates are.

## Real example

### Three Tables, One Customer

Barend Kloosterman built Serviceplan in Lovable: maintenance contract administration for installation companies, 44 companies managing around 9,000 service addresses.

Across fourteen months the schema had grown to 31 tables. Customers existed in three of them: `clients` from the original build, `customers` added when invoicing arrived, and `contacts` added for the portal. Each held a name and an email; two held a phone number, in differently named columns, with different formatting.

The bug that forced the work: an installer updated a customer's address in the portal, the invoice generated that evening carried the old address, and the service engineer was dispatched to a third address held somewhere else entirely. Three tables, three answers, no way to say which was right.

Four business days: a full schema inventory naming every duplicate and synonym; a convention file committed to the repository covering table and column naming, timestamps, booleans, money and the product's vocabulary; the three customer tables consolidated into one `customers` table with a contacts table beneath it, migrated through the add-write-both-migrate-drop sequence with no downtime; eleven columns renamed for consistency; a comma-separated `services` text column normalised into a proper table with a join; nine missing foreign keys declared, which surfaced 340 orphaned service records that were reviewed and either reattached or archived; four timestamp columns converted to time zone aware; two `amount` columns renamed and converted from floating point to integer minor units, which resolved a long-standing one-cent discrepancy in invoice totals; and generated types regenerated across the application.

**Result:** the three-address bug became structurally impossible. Barend reports that the more valuable outcome was speed of change — a contractor he hired the following month was productive on day one rather than spending two days asking which table was authoritative, and his AI sessions stopped inventing new column names because the convention file is now part of the project's instructions.

> *"I had three tables of customers because each time I asked for a feature I got a new table, and each one was a reasonable answer to the question I had asked that day."*
> — **Barend Kloosterman, Founder, Serviceplan (Doetinchem)**

**Cost & Timeline:** €3,400 (schema inventory, convention documentation, entity consolidation with zero-downtime migration, normalisation, foreign key remediation, timestamp and money type corrections, type regeneration) — completed in 4 business days.

## Frequently Asked Questions

### Does naming really matter if the app works?

It matters for every change after this one. An inconsistent schema slows humans, degrades generated tooling, and causes AI assistants to invent yet another convention — which is how you get four names for one idea.

### What naming convention should I use?

Any consistent one. Conventionally in Postgres: plural lower-case table names with underscores, `id` primary keys, `thing_id` foreign keys, `created_at` and `updated_at` with time zones, and positively phrased booleans.

### How do I rename a column without downtime?

Add the new one, write to both and backfill, migrate reads and deploy, then drop the old column in a later release. Each stage is safe on its own.

### Should I fix the whole schema at once?

No. Fix what you touch — the tables behind your main screens — plus anything dangerous: ambiguous money columns, missing foreign keys, timestamps without zones, duplicated entities.

### How do I stop the inconsistency returning?

Write the conventions into a file in the repository, including your product's vocabulary. Contractors read it, and so do coding agents, which changes what they generate.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does database naming matter if the app already works?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It affects every future change — human speed, generated tooling, and what AI assistants produce when there is no pattern to follow."
      }
    },
    {
      "@type": "Question",
      "name": "What naming convention should a Supabase project use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Any consistent one. Conventionally: plural lower-case tables with underscores, id primary keys, thing_id foreign keys, created_at and updated_at with time zones, positive booleans."
      }
    },
    {
      "@type": "Question",
      "name": "How do I rename a column without downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Add the new column, write to both and backfill, migrate reads and deploy, then drop the old column in a later release."
      }
    },
    {
      "@type": "Question",
      "name": "Should I fix an entire schema at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — fix the tables you actually touch, plus genuinely dangerous items: ambiguous money columns, missing foreign keys, zoneless timestamps, duplicated entities."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop schema inconsistency coming back?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Commit a short conventions file including your product's vocabulary. Contractors and coding agents both read it, which changes what gets generated."
      }
    }
  ]
}
</script>
