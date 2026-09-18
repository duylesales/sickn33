---
Title: "Bolt and Supabase: Wiring Data Into a Bolt Prototype"
Keywords: bolt supabase, database integration, schema design, row level security, prototype to product, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt and Supabase: Wiring Data Into a Bolt Prototype

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt and Supabase: Wiring Data Into a Bolt Prototype",
  "description": "A Bolt prototype with mock data becomes a product when it has a real database behind it. Designing the schema before generating against it, the mistakes that are expensive to undo, and what to do first.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-and-supabase-wiring-data-into-a-bolt-prototype" }
}
</script>

A Bolt prototype usually starts with invented data — arrays in the code, plausible names, everything present and consistent. It demonstrates the product beautifully and it has no memory.

Connecting a real database is the step that turns it into something people can use, and it is the step where decisions get made that are cheap now and expensive in eight months. The schema you generate against will shape every screen, every query and every migration that follows.

## Design the Schema Before Generating Against It

The instinct is to ask the tool to add a database and let it decide the structure. It will produce something that works, derived from the screens rather than from the business.

An hour spent first is worth considerably more than it costs. Write down the things your product is about — the nouns a customer would use — and how they relate. Organisations have members. Projects belong to an organisation. Tasks belong to a project. Invoices reference a project and a customer.

Three decisions to make deliberately in that hour, because all three are painful to change later.

**Your tenancy model.** How is data separated between customers? Almost always an organisation identifier on every table, which is the column every query will filter by and every policy will reference.

**Your identifiers.** Random identifiers as primary keys, with separate human-readable references where people need to quote a number.

**Your naming conventions.** One word per concept, consistently, because the schema teaches whatever writes against it next — including the tool.

Give that description to Bolt rather than asking it to invent one, and the generated code will follow it.

## Start With Fewer Tables

Prototypes generate tables enthusiastically. A product with five real entities acquires fifteen tables, several of which hold one column that belongs on another table.

Start with the smallest set that represents the business, and add when a real requirement demands it. Splitting a table later is straightforward; consolidating four tables that should have been one is not, because every screen and every query has learned the wrong shape.

The same applies to columns. A field that might be useful later is a field to add later, when its meaning is known.

## Turn On Row-Level Security Immediately

The single most important thing to do when connecting Supabase to a Bolt application: enable row-level security on every table, with policies, from the first table.

Doing it at the start means every screen is built against a database that already enforces separation, and anything broken is obvious immediately. Doing it later means retrofitting policies to an application that has been assuming unrestricted access, which is both more work and much more likely to leave a gap.

Policies are conditions, and the condition for most tables is the same: the row's organisation matches the caller's organisation. Write it once, apply it consistently, and test it with two accounts before building anything on top.

## Constraints Are Not Optional

A prototype's data is created by you and is therefore reasonable. A product's data is created by users, imports, integrations and AI sessions, and will not be.

Put the rules in the database: foreign keys so a row cannot reference something that does not exist, not-null on the columns the product genuinely requires, unique constraints where duplicates would be a problem, and checks where a value has a valid range.

Each is one line and each survives every future change to your application, including the ones written by a tool that has not read your intentions.

## Replace Mock Data Deliberately

The transition from invented data to a real database is where prototypes break in ways that are hard to diagnose, because the code has been written against data that was always complete and always consistent.

Real data has missing optional fields, relationships that point at deleted things, awkward characters, and quantities that make a list page slow. Generate a seed set with those properties before connecting the real database rather than after, so the failures happen while you are looking.

And remove the mock data entirely once the database is connected. A fallback to invented data when a query returns nothing is a pattern that appears in generated code and produces the most confusing bug class there is: a product that appears to work while showing information that does not exist.

## Queries Belong Behind a Boundary

A Bolt application talks to Supabase directly from the browser, which is the arrangement that makes it quick to build and the one that spreads database knowledge across every component.

Within a week, thirty files know your table names, your column names and the shape of your joins. Renaming a column then means finding thirty places, and a schema change becomes a search-and-replace exercise with no way to be confident it is complete.

The fix is small and worth doing early: put data access behind your own functions. One module — or one per entity — that exposes what the application needs, with the queries inside it. Components ask for "the projects for this organisation" rather than constructing a query.

Three benefits, in increasing order of importance. The schema can change without touching the interface. The scoping to the current organisation happens in one place, so it cannot be forgotten in a component written later. And an AI session adding a screen reaches for an existing function rather than writing a fresh query, which is what stops the pattern from spreading again.

This is the same boundary argued for elsewhere in this series as insurance against changing platforms. Its everyday value is larger than that: it is the difference between a schema you can evolve and one that has been copied into every corner of your application.

## Storage and Auth Are Schema Decisions Too

Two Supabase features get connected during prototyping and deserve the same deliberate treatment as tables.

**Authentication** creates its own users table, and the temptation is to store everything about a person there. Keep your own table instead, with your own identifier, linked to the auth identity — because roles, organisation membership, preferences and anything else your product knows belong to you rather than to the auth provider. This also makes the provider replaceable, and it means a user's application data survives changes to how they sign in.

**Storage** needs a path structure decided before the first upload, since paths are how policies are expressed. Owner first — organisation, then user or record, then a generated file identifier — and a database row per file recording who uploaded it, when, its path, size and type. Retrofitting a layout onto files already scattered across a bucket means moving objects and rewriting every stored URL.

Both are ten-minute decisions at the start and multi-day migrations afterwards, which puts them in the same category as the tenancy model: worth the hour of thought before anything is generated against them.

The general rule behind all of this: in a prototype, the cost of a structural decision is the time it takes to say it. In a product with customers, it is the time it takes to migrate. Spend the first while you still can.

It is also the only stage where you can make them alone. Once six customers depend on the product, a schema change is a migration with a maintenance window and a rollback plan, and the hour you did not spend at the start becomes a week you spend under pressure.

A useful way to hold this in mind while prototyping: every table you create is a promise to your future self about what the product is. Make as few promises as possible, make them deliberately, and write them down where the next session can read them.

## Setting This Up

For a Bolt prototype moving to a real database this is typically one to two days: a schema designed from the business rather than from the screens, with tenancy, identifiers and naming decided deliberately; the smallest table set that represents the product; row-level security enabled with policies on every table from the start and verified with two accounts; foreign keys, not-null, unique and check constraints; a realistic seed set with missing fields, awkward characters and volume; mock data removed with no fallback; migrations in the repository rather than changes typed into a dashboard; and generated types regenerated so the application knows the real shape.

LaunchStudio does this as part of taking a prototype to production under the Launch Ready package, from €800. The engineers are Manifera's — eleven years of Postgres in production, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Send us your prototype and a description of your business](https://launchstudio.eu/en/#contact) and we will design the schema before anything is generated against it.

## Real example

### Nineteen Tables for Five Things

Hidde Kwakernaak built Ritmeester with Bolt: stable and livery management for equestrian centres — horses, owners, stalls, feeding schedules, veterinary appointments and invoicing — for six centres in Gelderland and Utrecht.

He had asked the tool to add a database as he built each screen. After three weeks the schema had 19 tables. Horses existed in two of them. Owner contact details existed in three, with different column names and, by that point, different values. There were no foreign keys, no row-level security, and one table had been created for a feature he had abandoned in week one.

The problem surfaced when the second centre started using it and their horses appeared in the first centre's stall list.

Three business days: the business described properly, producing five core entities — centres, horses, owners, stalls and appointments — with invoicing as a sixth; a schema designed around them with an organisation identifier on every table, random primary keys with a readable horse reference for people to quote, and consistent naming; 19 tables consolidated to eight, with the duplicated horse and owner records merged after reconciling the three copies of contact details by hand; row-level security enabled with policies on all eight, verified with accounts in two centres; foreign keys added, which surfaced 40 orphaned records; not-null, unique and check constraints; a seed set of 400 horses across four centres with uneven distribution, missing optional fields and diacritics in names; mock data fallbacks removed from four screens where an empty result had been silently showing invented horses; migrations committed; and types regenerated.

**Result:** the cross-centre leak was closed structurally rather than patched. Hidde reports that the consolidation was uncomfortable — three days of work that produced no visible feature — and that the six centres onboarded afterwards took a day each rather than the week the first two had taken, because nothing needed reconciling.

> *"Nineteen tables for a business with five things in it. Each one was a reasonable answer to a screen I was building that afternoon, and together they were a product where a horse could exist twice with different owners."*
> — **Hidde Kwakernaak, Founder, Ritmeester (Barneveld)**

**Cost & Timeline:** €3,200 (schema design from the business, consolidation of 19 tables to 8 with data reconciliation, row-level security with policies, constraints and orphan resolution, realistic seed data, mock data removal, migrations and type regeneration) — completed in 3 business days.

## Frequently Asked Questions

### Should I let the tool design my schema?

Give it a schema instead. An hour spent describing your business entities, tenancy model, identifiers and naming produces a structure the generated code will follow, and avoids a design derived from whichever screen you built first.

### When should row-level security be enabled?

From the first table. Building against a database that already enforces separation makes gaps obvious immediately; retrofitting to an application that assumed open access is slower and leakier.

### How many tables should I start with?

The fewest that represent the business. Splitting later is easy; consolidating tables that should have been one is not, because every screen has learned the wrong shape.

### Do I need foreign keys and constraints in a small product?

Yes. They are one line each and they hold when data arrives through imports, integrations and AI sessions that never read your intentions.

### What breaks when mock data is replaced?

Code written against data that was always complete. Generate a realistic seed set — missing fields, awkward characters, volume — before connecting, and remove mock fallbacks entirely.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should Bolt design my database schema?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Give it one instead. An hour describing entities, tenancy, identifiers and naming produces a structure the generated code follows."
      }
    },
    {
      "@type": "Question",
      "name": "When should row-level security be enabled?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "From the first table, so every screen is built against enforced separation rather than retrofitted later."
      }
    },
    {
      "@type": "Question",
      "name": "How many tables should a prototype start with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The fewest that represent the business. Splitting later is easy; consolidating tables that should have been one is not."
      }
    },
    {
      "@type": "Question",
      "name": "Are foreign keys worth it in a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — one line each, and they hold against imports, integrations and AI sessions that never read your intentions."
      }
    },
    {
      "@type": "Question",
      "name": "What breaks when mock data is replaced with a database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Code assuming complete consistent data. Seed realistically first, and remove mock fallbacks so empty results are not hidden."
      }
    }
  ]
}
</script>
