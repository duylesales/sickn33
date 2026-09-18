---
Title: "Lovable Supabase: Database Functions and Triggers Worth Keeping"
Keywords: lovable supabase, database functions, Postgres triggers, business logic placement, data integrity, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Database Functions and Triggers Worth Keeping

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Database Functions and Triggers Worth Keeping",
  "description": "AI tools scatter triggers and functions through a Supabase schema until nobody can explain what happens on an insert. Which ones earn their place, which belong in application code, and how to find what is already there.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-database-functions-and-triggers-worth-keeping" }
}
</script>

A founder asked us why creating a project in his app sent two emails. It took an afternoon to answer, and the answer was that his application sent one and a database trigger — written by an AI session four months earlier, in response to a request he had forgotten making — sent the other.

That is the characteristic failure of database logic in AI-built products. Not that triggers are wrong, but that they are invisible. Nothing in the application code mentions them. They do not appear in a search for the feature. They run anyway, on every insert, forever, and the first sign of their existence is behaviour nobody can account for.

The answer is neither to ban them nor to let them accumulate. It is to know what you have and to keep only the ones that are genuinely better in the database than in your code.

## Find Out What Is Already There

Before deciding anything, list what exists. Supabase's dashboard shows database functions and triggers, and the list in a year-old AI-built project is usually longer than its owner expects.

Read each one and write a sentence next to it: what it does, what fires it, and whether anything still depends on it. This takes an hour and is the entire diagnosis.

Expect to find three categories. A few that are load-bearing and correct — timestamp maintenance, a counter, the standard profile-creation trigger on user signup. Several that duplicate something your application also does, which is where the double emails come from. And one or two that no longer do anything meaningful because the feature that needed them was removed, leaving a trigger firing into a table nobody reads.

## What Belongs in the Database

Three kinds of logic are genuinely better placed in Postgres, and moving them there makes a small product more reliable rather than more complex.

**Rules that must hold no matter what wrote the data.** A constraint that an amount cannot be negative, that a booking cannot end before it starts, that an email is unique within an organisation. These are not business logic in the interesting sense — they are statements about what a valid row is, and enforcing them in the database means they hold when data arrives through an import script, an admin action, or an AI session that forgot the rule existed.

**Derived values that must never drift.** A timestamp of last modification, a search vector, a denormalised counter that would be expensive to compute. A trigger maintaining these is genuinely better than application code, because it cannot be bypassed.

**Operations that must be atomic across several tables.** Moving an amount between balances, claiming a job from a queue, accepting an invitation that touches three tables. A single database function that does all of it inside one transaction is both faster and safer than several round trips from your application, each of which could fail in between.

## What Belongs in Your Application

Everything else, and particularly anything that reaches the outside world.

A trigger that sends an email, calls a webhook, charges a card or writes to another service is a trigger that can fail in ways the database cannot resolve. If the transaction rolls back, the email has already gone. If the external call is slow, your insert is slow. If it errors, the user sees a database error for a failure that had nothing to do with their data.

The rule that keeps this simple: the database may change the database. Anything that changes the world belongs in code you can see, retry and log.

Multi-step business processes belong in the application too, not because Postgres cannot express them but because the next person to read your product should be able to find them. A hiring workflow implemented across four triggers is a hiring workflow nobody can modify with confidence.

## Security Definer Is the Sharp Edge

Supabase functions can run with the permissions of whoever defined them rather than whoever called them, which is necessary for operations that legitimately need to bypass row-level security.

It is also how row-level security gets defeated by accident. A helper function written to "just fetch the organisation's records", marked security definer because that made an error go away, is a function that returns any organisation's records to any caller who can invoke it.

Three habits contain the risk. Use it only when there is a specific reason, and write that reason in a comment. Inside such a function, check the caller's identity explicitly rather than assuming the caller was already authorised. And set the search path explicitly on every security definer function, because without it the function can be persuaded to call something other than what its author intended.

If your project has security definer functions nobody can explain, that is the first thing to review — ahead of the policies themselves.

## Triggers and the Double-Write Problem

The most common concrete bug is simple: both the trigger and the application do the same thing.

It happens because the trigger was added in one session and the application code in another, and neither knew about the other. The symptoms are duplicated rows, doubled counters, two emails, or an audit log with every entry twice.

Finding them is mechanical. For each trigger, search the application for code doing the same work. Then decide which one stays — usually the application, unless the rule must hold for data arriving by other routes — and remove the other rather than leaving both with a condition to keep them from colliding. Conditions like that are how the situation got confusing in the first place.

## Keep Them in Migrations

Functions and triggers created by typing into the Supabase SQL editor exist only in that database. They are not in your repository, they will not be in a new environment, and a restore from backup may or may not include the version you expected.

Everything belongs in migration files, checked in, applied the same way to staging and production. For logic that already exists only in the dashboard, dump the definitions and commit them as a baseline migration — an hour of work that converts an undocumented database into a reproducible one.

This is also what makes the rest of this article possible. You cannot review what you cannot read, and a schema that lives only in a hosted dashboard is a schema nobody reviews.

## Testing Something You Cannot Step Through

Database logic is harder to debug than application code because there is no obvious place to watch it run. Two techniques cover most of it.

Write the test as SQL: insert a row, then assert that the resulting state is what you expected. Run it against a scratch database as part of your migrations. It is less elegant than a test framework and it catches the thing that matters, which is whether the trigger fires and what it leaves behind.

And use Postgres's own logging sparingly inside functions while developing, then remove it. A function emitting notices on every insert is a function making your production logs unreadable.

## Constraints Are the Cheapest Thing You Will Ever Write

If you take one habit from this, take this one: express the rules about valid data as constraints rather than as checks in application code.

A unique constraint on an email within an organisation. A check that a percentage is between zero and a hundred. A foreign key that refuses to point at a row that does not exist. A not-null on the columns your product genuinely cannot function without. Each is one line and each is permanent.

The reason this matters more in an AI-built product than elsewhere is that your application code changes constantly and unpredictably. A validation written in a component in March can disappear in an August refactor nobody reviewed, and no test will notice because the test was generated from the same code. A database constraint survives every rewrite, every new endpoint, every import script and every session where an agent decided to restructure your forms.

The objection is that constraint violations produce ugly errors. That is true and it is a presentation problem: catch the specific violation and show a sensible message. The alternative — permissive data and validation that exists only where somebody remembered — is how a product acquires rows that its own code cannot handle.

## Setting This Up

For an existing Supabase project this is one to two days: every function and trigger listed and described, duplicates between database and application resolved in one direction, anything performing external calls moved into application code, constraints and derived-value triggers kept and documented, security definer functions reviewed with explicit authorisation checks and search paths, dead logic removed, everything captured in migrations and committed, and a short note in the repository explaining what the database does on its own so the next person is not surprised by it.

LaunchStudio does this as part of taking over or hardening an AI-built codebase, and it is usually where the unexplained behaviour lives. The engineers are Manifera's — eleven years of Postgres in production, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us what your database does that your code does not mention](https://launchstudio.eu/en/#contact).

## Real example

### The Trigger That Emailed Twice

Marnix Oosterveld runs Offerteroute, built with Lovable and extended over a year by AI sessions: quotation management for kitchen and bathroom installers, 61 companies, around 900 quotations a month.

Installers complained that customers received two copies of every quotation, sometimes minutes apart and sometimes hours. Two customers had replied to both, creating duplicate follow-ups and one argument about a price that had changed between versions.

The application sent a quotation email when a quotation was marked sent. So did a trigger on the quotations table, written eight months earlier, which fired on any update where the status column changed — including the nightly job that updated expiry dates, which is why some duplicates arrived at three in the morning.

The review found more. Eleven triggers in total: four maintaining timestamps and counters correctly, two duplicating application logic, one calling an external webhook inside a transaction that had caused three timeouts, three doing nothing because their target tables had been replaced, and one security definer function fetching quotations with no authorisation check at all, callable by any authenticated user against any company's data.

Three business days: every function and trigger inventoried and described; the email trigger and the webhook trigger removed with the work moved into the application where it can be retried and logged; the duplicate-logic pairs resolved; three dead triggers dropped; the security definer function rewritten with an explicit membership check and a fixed search path; timestamp and counter triggers kept, documented and covered by SQL tests; and the whole schema — functions and triggers included — dumped into a baseline migration and committed, replacing a database that existed only in the dashboard.

**Result:** duplicate emails stopped, the intermittent timeouts stopped with them, and the exposed function was closed before anyone had used it. Marnix now has a two-page document describing what his database does without being asked, which he says is the first time he has understood his own product's behaviour since month three.

> *"Nothing in my code sent a second email. It took an afternoon to accept that the database was doing it by itself, because I had asked it to, in a chat I do not remember."*
> — **Marnix Oosterveld, Founder, Offerteroute (Waalwijk)**

**Cost & Timeline:** €2,700 (schema inventory, trigger and function review, duplicate resolution, external calls moved to application code, security definer remediation, SQL tests, baseline migration) — completed in 3 business days.

## Frequently Asked Questions

### Are database triggers a bad idea in Supabase?

No — for constraints, derived values and atomic multi-table operations they are the better place. The problem is invisibility: logic in the database that nothing in your code mentions.

### Should a trigger send email or call a webhook?

No. External calls inside a transaction cannot be rolled back, make writes slow, and surface as database errors. The database may change the database; anything touching the outside world belongs in application code.

### What is the risk with security definer functions?

They run with elevated permissions, so they bypass row-level security. Use them only with a stated reason, check the caller's authorisation inside the function, and always set an explicit search path.

### How do I find what triggers already exist?

List them in the Supabase dashboard and read each definition, writing one sentence about what it does and what fires it. In a year-old AI-built project this takes an hour and usually explains at least one mystery.

### Why do my functions need to be in migration files?

Because logic created in the SQL editor exists in one database only. It will not be in a new environment, may not survive a restore, and cannot be reviewed by anyone reading your repository.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are database triggers a bad idea in Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — constraints, derived values and atomic multi-table operations belong there. The danger is logic your application code never mentions."
      }
    },
    {
      "@type": "Question",
      "name": "Should a trigger send email or call a webhook?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. External calls cannot be rolled back with the transaction, slow every write, and appear as database errors. Keep them in application code."
      }
    },
    {
      "@type": "Question",
      "name": "What is the risk with security definer functions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They bypass row-level security. Use them deliberately, check the caller's authorisation inside the function, and set an explicit search path."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find which triggers already exist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "List them in the Supabase dashboard and describe each in one sentence. In a year-old AI-built project this usually explains at least one mystery."
      }
    },
    {
      "@type": "Question",
      "name": "Why must database functions live in migration files?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Logic created in the SQL editor exists in that one database — absent from new environments, uncertain after a restore, and invisible in your repository."
      }
    }
  ]
}
</script>
