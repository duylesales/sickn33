---
Title: "Replit and Supabase: Wiring a Database That Survives"
Keywords: Replit, lovable supabase, supabase security, persistent storage, connection pooling, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit and Supabase: Wiring a Database That Survives

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit and Supabase: Wiring a Database That Survives",
  "description": "Storage that disappears on redeploy is the most common data loss in Replit projects. How to connect an external managed database properly: region, keys, access rules, pooling, migrations and what stays on the platform.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-and-supabase-wiring-a-database-that-survives" }
}
</script>

The most expensive sentence in a Replit project is "it was working yesterday". It usually means data was being written somewhere that felt like storage and was not — a file beside the application, a local database created inside the environment, an in-memory structure that survived exactly as long as the process did.

Then something restarts. A redeploy, a platform maintenance window, a crash, a change to the run configuration. The application comes back perfectly and the data does not, and the loss is silent: no error, no warning, simply a product that has forgotten everything since the last time you looked.

Connecting an external managed database is the fix, and doing it properly takes an afternoon. Doing it carelessly moves the problem rather than solving it.

## Why the Convenient Storage Is a Trap

Three patterns appear in Replit projects, and all three fail the same way.

**Files written next to the code.** Uploads, generated documents, a JSON file used as a database. The filesystem in a development environment is not durable across rebuilds, and the platform rebuilds more often than founders expect.

**A database created inside the environment.** Convenient during development and tied to that environment's lifecycle.

**In-memory state.** Fine for a session, gone on restart, and particularly deceptive because it works flawlessly while you are testing.

The common property is that none of them separate the data's lifecycle from the application's. That separation is the whole point of an external database.

## What Supabase Adds Beyond Durability

Choosing a managed Postgres service rather than any persistent store brings four things that matter later.

**A region you chose,** which is what you will be asked about by any Dutch business customer with a procurement process.

**Backups you can verify,** with a retention window and a restore you can rehearse.

**Access rules in the database itself,** so protection does not depend on every query being written correctly.

**Portability.** Standard Postgres means your data can move to another host later without a rewrite, which is the opposite of the platform-tied options.

## Connecting Them Properly

Four decisions, in this order.

**Create the project in the right region first.** For a Dutch product with EU customers, an EU region. Changing it later means exporting, restoring and cutting over; choosing it now is one dropdown.

**Put the credentials in the platform's secrets mechanism,** never in a file in the project. Replit provides one; use it consistently so there is exactly one place to rotate.

**Use the right key on the right side.** The public key belongs in anything running in a browser and relies on your access rules for protection. The privileged key belongs only in server-side code — and in a Replit project, where frontend and backend frequently live in the same repository, this distinction is easy to lose. If your project serves a frontend directly, assume anything it can read is public.

**Enable row level security on every table and write the policies before you have real data.** A table without policies, reachable through the automatically generated API, is readable by anyone holding your public key. This is the single most common serious finding in AI-built projects, and it costs nothing to prevent and a week to retrofit.

## Connection Pooling, and Why Your App Breaks at Thirty Users

The failure that surprises people who did everything else correctly.

Each connection to Postgres consumes a slot, and the number of slots is finite. A development environment holding one or two connections never approaches the limit; an application serving concurrent visitors, particularly one where each request opens its own connection, exhausts it quickly. The symptom is not a clean error message — it is an application that works for the first several people and fails for everyone afterwards, intermittently, in a way that looks like the platform being unreliable.

The fix is pooling: connect through the pooled endpoint your provider offers, reuse connections rather than creating one per request, and close them when work finishes. Supabase provides a pooled connection string for exactly this purpose, and using it is a configuration change rather than a rewrite.

Check this before launch rather than during one. It is the difference between a busy morning and an incident.

## Migrations and Who Owns the Schema

Once your database is external, the question of where its structure is defined becomes real.

Changes made by clicking in a dashboard exist only in that database. Your project has no record of them, a collaborator's environment does not match, and nobody can say what changed or when. On a platform where environments are recreated regularly, that divergence bites sooner than elsewhere.

Keep migrations as files in the project. It makes changes reviewable, reproducible in every environment, and visible to whatever tooling — human or agent — you work with next.

## What Should Stay on Replit

This is not an argument for moving everything.

The application itself, the development environment, the collaboration and the deployment can all reasonably stay where they are. What moves is the data: the database, and any files users upload, which belong in object storage with per-owner access rather than on a filesystem that gets rebuilt.

That split — application on the platform, state outside it — is what makes a Replit project survivable without giving up the thing that made it pleasant to build.

## Testing That It Actually Survives

Four checks, none requiring tooling.

**Restart the project and confirm your data is still there.** Obvious, and frequently the first time anyone tries it deliberately.

**Redeploy and check again,** because a restart and a rebuild are different events.

**Upload a file, redeploy, and try to retrieve it.** This is where the second half of the problem lives, and it is the one people fix later than the database.

**Open your app in two browsers as two different accounts and try to read each other's records** by changing an identifier. A connected database with no access rules is durable and exposed, which is not an improvement.

## Moving the Data You Already Have

Most projects reaching this decision are not empty. There is real information in the temporary store, and moving it is a small project of its own.

**Export before you change anything.** Whatever the current store is — a file, a local database, an in-memory structure dumped on demand — get a copy out and keep it somewhere that is not the project. This is the step people skip because they intend to do the migration in one sitting, and it is the step that saves them when the sitting does not go as planned.

**Expect the data to be messier than the code implies.** Records written by earlier versions of the application frequently lack fields the current version assumes, because the shape changed and nothing migrated the old rows. Dates may be stored in two formats. The same customer may appear twice with different capitalisation. You will find out during the import rather than before it, so plan for a pass that cleans as it loads.

**Design the destination properly rather than copying the shape.** A file-based store encourages one wide structure holding everything; a relational database wants separate tables with real relationships and real constraints. Importing the old shape verbatim carries every compromise forward and makes the next year harder. Spending an hour on the target schema is the highest-return hour in the migration.

**Add the constraints during the import, not after.** Required fields, uniqueness on email addresses, foreign keys that guarantee a record points at something real. Applied at import, they tell you exactly how much invalid data you have. Applied later, they fail against data you have to clean under time pressure.

**Verify by counting.** Number of records in, number out, plus a handful of specific records checked by eye — the oldest, the newest, one with unusual characters in a name, one with an empty optional field. Then have someone who uses the product daily look at the result, because they will notice a wrong total that no count would reveal.

**Run both for a short period if you can,** writing to the new store while the old one remains readable, and cut over once the numbers agree for a few days. For most small products a maintenance window of an hour is simpler and perfectly acceptable — announce it, do it early, and keep the export.

## Getting the Data Layer Right

For a project that already works, this is bounded work rather than a rebuild: the database created in the correct region with backups verified by restoring one, credentials consolidated into the platform's secrets mechanism and the privileged key kept server-side, access rules written per table and tested by attempting to bypass them, pooling configured so concurrency does not exhaust connections, uploads moved to object storage with per-owner access, and the schema captured as migrations so the project is the source of truth.

LaunchStudio does this without touching the interface you built, and leaves the codebase conventional and documented so you can continue working on Replit afterwards. The engineers are Manifera's: eleven years of production database work for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Describe your project](https://launchstudio.eu/en/#contact) and you will get a specific assessment of where your data actually lives, usually within one business day, or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers.

## Real example

### A Waiting List That Reset Every Deploy

Tessa Oomen built Wachtlijst on Replit: a waiting-list and intake tool for three physiotherapy practices around Tiel. Patients submitted a form, practices worked through the list, and it had been running for two months.

Submissions were stored in a file inside the project. Every redeploy — and Tessa redeployed whenever she adjusted the form — removed everything submitted since the previous one. The practices had noticed that the list "sometimes looked shorter" and assumed colleagues had processed entries.

The scale became clear only when one practice cross-referenced their own phone log: roughly 40 intake requests had been lost across six weeks, from people who had submitted a form and heard nothing.

Six business days of work: a Supabase project created in an EU region; the intake data model built properly with one table per concern and access rules restricting each practice to its own records, tested by logging in as two practices; credentials moved into the platform's secrets mechanism with the privileged key confined to server-side code; pooled connections configured after a load test showed failures at around forty concurrent submissions; uploaded referral documents moved to object storage with per-practice access and signed links; the schema captured as migration files; and backups verified with a restore timed at 17 minutes.

The lost submissions could not be recovered. The practices contacted the people they could identify from their own records and apologised.

**Result:** no data loss in the eleven months since, and the intake list survived a busy September that produced more submissions in a week than the previous system had lost in six.

> *"I thought a file in my project was a database. It behaved exactly like one right up until the moment it deleted forty people who were waiting for care."*
> — **Tessa Oomen, Founder, Wachtlijst (Tiel)**

**Cost & Timeline:** €3,200 (database setup with region and backups, access rules, pooling, storage migration, migrations) — completed in 6 business days.

## Frequently Asked Questions

### Why does my Replit project lose data when I redeploy?

Because the data is stored inside the environment — a file beside your code, a local database or in-memory state — and environments are rebuilt. Durability requires storage whose lifecycle is separate from the application's.

### Which key should my Replit app use to reach Supabase?

The public key in anything that runs in a browser, protected by row level security policies; the privileged key only in server-side code. In projects where frontend and backend share a repository, assume anything the frontend can read is public.

### Why does my app fail once several people use it at once?

Usually connection exhaustion. Each request opening its own database connection uses a finite slot. Connect through the pooled endpoint your provider offers and reuse connections, which is a configuration change rather than a rewrite.

### Should my schema live in the dashboard or in the project?

In the project, as migration files. Dashboard-only changes exist nowhere else, so environments drift apart and nobody can say what changed — which matters more on a platform where environments are recreated regularly.

### Do I have to leave Replit to have a real database?

No. The useful split is application on the platform and state outside it: the database and uploaded files in managed services, everything else where you are building. That keeps what made the platform pleasant while removing the data loss.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my Replit project lose data when I redeploy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the data sits inside the environment — a file, a local database or memory — and environments are rebuilt. Durability needs storage with a lifecycle separate from the app."
      }
    },
    {
      "@type": "Question",
      "name": "Which key should my Replit app use to reach Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The public key in browser code, protected by row level security, and the privileged key only server-side. Where frontend and backend share a repository, assume frontend-readable means public."
      }
    },
    {
      "@type": "Question",
      "name": "Why does my app fail once several people use it at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually connection exhaustion. Use the pooled connection endpoint and reuse connections rather than opening one per request."
      }
    },
    {
      "@type": "Question",
      "name": "Should my schema live in the dashboard or in the project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In the project as migration files, so changes are reviewable and environments stay aligned."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to leave Replit to have a real database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — keep the application on the platform and move state outside it: database and uploaded files in managed services."
      }
    }
  ]
}
</script>
