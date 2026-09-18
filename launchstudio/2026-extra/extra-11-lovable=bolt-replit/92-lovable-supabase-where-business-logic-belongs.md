---
Title: "Lovable Supabase: Where Business Logic Belongs"
Keywords: lovable supabase, database functions, triggers, constraints, supabase security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Where Business Logic Belongs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Where Business Logic Belongs",
  "description": "Rules enforced only in the browser are suggestions. What belongs in the database as constraints, functions and triggers, what belongs in server code, and what should never be a trigger.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-where-business-logic-belongs" }
}
</script>

There is a rule your product depends on. A booking cannot overlap another booking. An invoice total must equal the sum of its lines. A discount cannot exceed the order value. An order belongs to exactly one customer.

Where is that rule written? In an AI-built product the answer is almost always: in the screen where a user enters the data. Which means it is a suggestion, not a rule — enforced for people who use your interface, absent for anyone using the API directly, and absent for every other path into your data.

The question of where a rule lives is not academic. It decides whether your data stays coherent as the product grows.

## Four Places a Rule Can Live

**In the browser.** Fast feedback, good for the user, and no protection at all. Anything the client enforces, the client can skip.

**In server-side code.** Real enforcement for traffic that goes through that code. The weakness is that products acquire several paths — a web app, an API, a scheduled job, an import, an admin tool — and a rule written in one is absent from the others.

**In the database as a constraint.** Enforced no matter how the data arrives. Cannot be bypassed, cannot be forgotten, and applies to your own scripts as well as your customers.

**In the database as a function or trigger.** For rules needing more than a constraint can express.

The principle that resolves nearly every case: the closer a rule lives to the data, the harder it is to violate — so put the rules that must always hold where they always apply, and put everything else where it is easiest to read.

## What Should Be a Constraint, Always

These cost nothing and prevent whole categories of corruption.

**Required fields declared not null.** An order without a customer should be impossible, not merely unusual.

**Foreign keys.** A row referring to another row should be guaranteed to refer to something that exists. AI-generated schemas frequently omit these, which is how products accumulate orphaned records nobody can explain.

**Uniqueness where it matters.** One membership per person per organisation, one email per account. Enforced in the database, this is a guarantee; enforced in code, it is a race waiting for two simultaneous requests.

**Check constraints for value rules.** A quantity above zero, a percentage between nought and a hundred, an end date after a start date. One line each.

**Sensible defaults and timestamps,** set by the database rather than hoped for from the client.

Adding these to an existing product will fail on the first attempt, because they will find data that already violates them. That is the point. The failures are a list of the problems you already have.

## Where Functions and Triggers Earn Their Place

Some rules cannot be expressed as constraints, and a few of those genuinely belong in the database.

**Guaranteed audit trails.** A trigger writing every change to an append-only table cannot be forgotten by a new code path, which is exactly the property an audit trail needs.

**Derived values that must never drift.** A stored total, a search vector, a counter. A trigger keeping them consistent is more reliable than remembering to update them everywhere.

**Atomic multi-step operations.** Transferring something between accounts, allocating a place from limited capacity, issuing a number from a sequence with no gaps. A function running inside a transaction is the correct tool, and doing it in application code invites two users receiving the same place.

**Preventing overlaps.** Bookings, reservations, shifts. Databases have facilities for this that are genuinely difficult to reproduce correctly in application code, and overlap bugs are among the most damaging in scheduling products.

## What Should Not Be a Trigger

A balancing section, because the failure mode here is real.

**Anything calling an external service.** A trigger sending an email or calling an API makes your database wait on somebody else's system, and a failure there can fail the transaction that was trying to save a record.

**Business decisions that change with policy.** Pricing rules, discount logic, eligibility. These change often and belong somewhere readable and testable.

**Anything long-running.** Triggers should be quick. Slow triggers make every write slow, including the ones that had nothing to do with the rule.

**Complex chains.** Triggers firing triggers become impossible to reason about, and debugging them is genuinely unpleasant. Two levels is usually one too many.

The heuristic: use the database for invariants — things that must be true of the data itself, always. Use code for policy — things that are true because you decided them this quarter.

## Why Generated Products Get This Wrong

Consistently, and for an understandable reason.

A generation tool builds a screen that satisfies a request. Validation in that screen is visible, immediate and demonstrably works. Constraints in the database are invisible, require a separate migration, and make no difference to the feature being demonstrated — so they are not produced unless asked for.

The result is a schema of permissive columns with the rules living in whichever screen happened to need them, and three screens implementing the same rule slightly differently. The fix is to ask explicitly: "add a foreign key", "make this column not null", "add a check constraint", "enforce this uniqueness in the database". Tools do this well when asked and never volunteer.

## Migrating From Screen Rules to Real Rules

Adding enforcement to a product with existing data is a defined exercise.

Write down the rules your product depends on, in plain language. For each, query the database to see how many existing rows violate it — this number is always higher than expected. Decide how to correct the violations, which for some will require asking customers. Fix the data, then add the constraint, then remove the now-redundant validation from wherever it was duplicated. Keep the client-side validation for the user experience, but treat it as a convenience rather than the enforcement.

Do the highest-value rules first: anything about money, anything about who owns what, anything about uniqueness.

## Keeping the Schema Where You Can See It

One more point, because it undermines everything else when it goes wrong.

Constraints, functions and triggers added by clicking in a dashboard exist only in that database. Your project has no record, environments diverge, and a restore produces a database with your data and none of your rules. Keep them in migration files in the repository, like everything else. This also makes them reviewable, which matters, because a trigger nobody has read is a behaviour nobody can explain.

## Testing the Rules You Just Added

A constraint you have not tried to violate is a belief about a constraint. Fifteen minutes of deliberate misbehaviour is what turns it into knowledge.

**Try to break each rule directly.** Not through your interface — through the API with your public key, or in the SQL editor. Insert an order with no customer. Create a second membership for the same person in the same organisation. Submit a negative quantity. Set an end date before its start date. Each attempt should fail with a clear error, and each one that succeeds is a rule you thought you had.

**Check what your application does when a constraint fires.** This is the part people skip. A database rejection arrives in your code as an error, and generated code frequently displays it raw — so a user sees a message naming your table and column, which is both confusing and a small information leak. Catch the specific violations you expect and translate them into sentences a person can act on: "This email address is already registered", not a constraint name.

**Test the race, not just the single case.** Uniqueness and capacity rules exist precisely because two things can happen at once. Submit the same form twice in rapid succession, or open two browsers and claim the last place simultaneously. Application-level checks pass this test individually and fail it under simultaneity, which is exactly why the rule belongs in the database.

**Re-run after schema changes.** Adding a column, splitting a table or introducing a new path into the data can quietly invalidate what a trigger assumed. Keep the list of attempts written down so repeating it takes minutes.

**Then write the important ones as automated tests,** so the rules that protect money and ownership are checked on every change rather than remembered.

## Getting the Data Layer to Enforce Itself

For a product already running, this is bounded work: the rules your business depends on written down, existing violations found and corrected with you, constraints and foreign keys added, uniqueness and overlap enforcement moved into the database, audit trails made trigger-guaranteed, atomic operations wrapped in functions, policy logic kept in readable code, and the whole schema captured as migrations so your repository is the source of truth.

LaunchStudio does this alongside the access model, because the two live in the same place and are usually missing together. The engineers are Manifera's: eleven years of production database work for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us what rules your product depends on](https://launchstudio.eu/en/#contact) and you will get a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Eleven Expense Claims Paid Twice

Carola Mudde built Declaratie with Lovable: expense claim handling used by two small municipalities, a housing foundation and four cultural organisations around Sittard and Geleen, processing roughly 1,400 claims a month.

The rules lived in the submission screen. A claim could not exceed €500 without approval, a receipt was required above €50, and a claim could be submitted once. All three were enforced in the browser.

Three problems arrived together. A finance officer at one municipality had been using a spreadsheet import Carola had built for bulk entry, which did not go through the screen and therefore enforced nothing — 60 claims had been imported without receipts. A double-click on a slow connection had submitted eleven claims twice, and eight of those had been paid twice before anyone reconciled. And an intern had discovered that editing the amount after approval was possible, because approval status was checked in the interface only; two claims had been altered after approval, one innocently and one not.

The database had no constraints at all: no foreign keys, no uniqueness, every column nullable.

Nine business days of work: the rules written down in plain language with all seven organisations confirming them; existing violations queried, which found 214 rows breaching at least one rule, including 31 claims with no valid organisation reference; the data corrected in consultation with each organisation; not-null and foreign key constraints added across eleven tables; a uniqueness constraint added on the combination that defines a distinct claim, which makes the double-submission impossible rather than unlikely; a check constraint on amounts and a trigger enforcing the receipt requirement regardless of entry path; approval status made immutable after approval via a trigger, with any change recorded in an append-only audit table; the spreadsheet import rewritten to go through the same validated path; and the schema captured as migration files.

The eight double payments were recovered over the following two months. The altered claim was handled by the organisation internally.

**Result:** no duplicate or unsupported claims in the fourteen months since, and the audit trail became the artefact one municipality's accountant asks for at each year end.

> *"My rules were written in a screen, and three different ways into the data did not go through that screen. One of them was an import I had built myself."*
> — **Carola Mudde, Founder, Declaratie (Sittard)**

**Cost & Timeline:** €4,900 (rule definition, violation correction across 214 rows, constraints and foreign keys, uniqueness and immutability triggers, audit trail, import rewrite, migrations) — completed in 9 business days.

## Frequently Asked Questions

### Why is validation in the browser not enough?

Because anything the client enforces, the client can skip — and products acquire other paths into the data: an API, an import, a scheduled job, an admin tool. A rule written in one screen is absent from all of them.

### What should always be a database constraint?

Required fields as not null, foreign keys so references are guaranteed valid, uniqueness where it matters, check constraints for value rules, and database-set defaults and timestamps. Each is one line and prevents a category of corruption.

### When is a trigger the right tool?

For guaranteed audit trails, derived values that must not drift, atomic multi-step operations such as allocating limited capacity, and preventing overlapping bookings — cases where being bypassed by a new code path would be a real problem.

### What should not go in a trigger?

Anything calling an external service, business policy that changes with the quarter, anything long-running, and chains of triggers firing triggers. Use the database for invariants and code for policy.

### How do I add constraints to a product that already has data?

Expect the first attempt to fail, because it will find existing violations — that list is the point. Write the rules down, query how many rows breach each, correct the data with your customers, then add the constraint and remove the now-duplicated validation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is validation in the browser not enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anything the client enforces can be skipped, and other paths into the data — API, imports, jobs, admin tools — never pass through that screen."
      }
    },
    {
      "@type": "Question",
      "name": "What should always be a database constraint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not-null on required fields, foreign keys, uniqueness where it matters, check constraints for value rules, and database-set defaults and timestamps."
      }
    },
    {
      "@type": "Question",
      "name": "When is a trigger the right tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Guaranteed audit trails, derived values that must not drift, atomic multi-step operations, and preventing overlapping bookings."
      }
    },
    {
      "@type": "Question",
      "name": "What should not go in a trigger?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "External service calls, business policy that changes often, long-running work, and chains of triggers firing triggers."
      }
    },
    {
      "@type": "Question",
      "name": "How do I add constraints to a product that already has data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Expect failures revealing existing violations, correct the data with your customers, then add the constraint and remove duplicated screen validation."
      }
    }
  ]
}
</script>
