---
Title: "Lovable Supabase: Seed and Test Data You Can Trust"
Keywords: lovable supabase, seed data, test data, staging anonymisation, database snapshots, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Seed and Test Data You Can Trust

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Seed and Test Data You Can Trust",
  "description": "Why AI-built apps break only in production: development data is too small, too clean and too new. Building a seed set that reproduces real problems, and anonymising production data safely for staging.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-seed-and-test-data-you-can-trust" }
}
</script>

There is a category of bug that only ever appears in production, and founders tend to explain it with words like flaky or intermittent. It is neither. It is the predictable consequence of testing against eleven rows of data you typed in yourself, all created this week, all belonging to the same account, none of which contains an apostrophe, an umlaut, a very long name, or a deliberately empty field.

Your development database is not a small version of production. It is a different thing, with different shapes, and the differences are exactly where your product fails.

Fixing this is unglamorous and it removes an entire class of incident.

## What Real Data Has That Yours Does Not

Six properties, and every one of them breaks something in a typical AI-built application.

**Volume.** Enough rows for a missing index to matter, a list page to need pagination and an export to time out.

**Unevenness.** One customer with 4,000 records and forty with nine. Nearly every performance problem in a multi-tenant product lives in the largest account, and a seed set giving every account the same amount hides it perfectly.

**Age.** Records from last year, from before you added a required column, from before you changed how status worked. Old rows are a running record of every schema decision you have revised.

**Awkward characters.** Names with apostrophes and diacritics — Van 't Hoff, Peña, Müller — which break string handling, exports and search. Dutch names alone will find most of it.

**Emptiness.** Optional fields nobody filled in, relationships that point at deleted things, half-finished records abandoned mid-form.

**Extremes.** The absurdly long company name, the 200-character email, the note somebody pasted a whole document into.

A seed set that contains all six will catch more bugs than any amount of additional test-writing, because it produces failures in the code you already have.

## Seed Data Belongs in the Repository

Make your seed a script, checked in, that builds a database from empty to useful in one command.

The value is not only that new environments are quick. It is that everyone — you, a contractor, a future employee, an AI session — works against the same data, so "it works for me" becomes a meaningful statement rather than a coincidence. And when a bug is found, the fix is to add a row to the seed that reproduces it, which means it can never silently return.

Keep it deterministic. Random generators that produce different data each run make failures unreproducible, which is the opposite of what a seed is for. Fixed identifiers, fixed values, fixed dates relative to a known reference point.

And give it a defined set of accounts with known roles: an administrator, an ordinary user, a user in a second organisation who should never see the first one's data, and a deactivated account. Those four cover most of what you need to check manually before a release, and having them ready by name means you actually do.

## Anonymised Production Data for Staging

Seed data is right for development. Staging is where you want the real shapes, because it is the last place to notice that a customer's peculiar data breaks the new feature.

Never point staging at the production database. It is one mistaken delete away from an incident, and it means test emails go to real customers — a mistake almost every company makes exactly once.

Instead, copy production and anonymise it. Replace names, emails, phone numbers and addresses with generated values, redact free-text fields that may contain anything, and neutralise every email address so nothing can reach a real person. Keep the structure: same row counts, same distribution, same ages, same relationships.

Two rules make this safe rather than theatrical. Anonymise during the copy, not after — a staging database that is real for twenty minutes is a real database. And treat the result as still sensitive: it has production's shape, which is itself informative, so it deserves the same access control.

## The Fields People Forget to Anonymise

Reviews of anonymisation scripts find the same misses.

Free-text notes, which contain anything a user typed and are the single richest source of personal data in most products. Uploaded file contents, which are usually not covered at all. Audit and event logs recording who did what. Stored email bodies from your notification history. External identifiers such as payment provider customer IDs, which link a fake name back to a real person in somebody else's system. And backups of the staging database, which quietly preserve whatever was there before you improved the script.

The test to apply: pick three customers you know in the anonymised copy and try to identify them. If you can, it is not anonymised — it is renamed.

## Make Sending Impossible, Not Unlikely

Configuration that prevents email in non-production environments is worth building at the level where it cannot be overridden by a forgotten variable.

The reliable arrangement has two layers. The environment has no credentials for your real email provider, so nothing can send even if the code tries. And every address in the anonymised copy is rewritten to a domain you control that discards or captures mail.

The same applies to payment providers, SMS, webhooks to customers' systems, and anything that pushes to a third party. Non-production keys only, and where no test mode exists, no keys at all.

The failure this prevents is specific and memorable: a staging run of a notification job emailing every customer a duplicate of something from three months ago.

## Snapshots Make Everything Cheap

Once seeding exists, add the ability to restore a known state quickly — a database snapshot you can reset to in seconds.

This changes how you work more than it sounds. Destructive changes become safe to try. A migration can be run, inspected, rolled back and run again. Reproducing a customer's bug becomes a matter of restoring the snapshot rather than a careful sequence of clicks you must not get wrong.

For local development this is a container and a dump file. For staging it is the platform's own restore. Either way, the property you want is that wrecking the data is a five-second inconvenience rather than an afternoon.

## Keep It Alive

A seed script written once and never updated becomes a liability within months: it fails against the current schema, so people stop running it, so environments diverge again.

Two habits prevent that. Any migration that changes shape updates the seed in the same commit. And the seed runs in whatever automated checks you have, so a break is noticed immediately rather than by the next person who tries to set up the project.

The same for anonymisation: a new table containing personal data needs a rule in the script, and the easiest way to enforce that is a check that fails when an unrecognised table appears.

## Reproducing One Customer's Problem

The hardest support tickets are the ones where a customer describes something your product does not do, and every attempt to reproduce it works fine.

Almost always the difference is their data. They have a record with an unusual combination of fields, a relationship that should not exist, or a volume that changes which code path runs. Guessing is slow; copying is fast.

Build the ability to extract one account's data from production — anonymised, structurally complete, with everything it references — and load it into a development database beside your ordinary seed. A single command, ten minutes of work the first time, and the difference between reproducing a bug in a minute and speculating about it for an afternoon.

Two constraints keep it honest. The extract must be anonymised the same way staging is, since it is production data on a laptop otherwise. And it should be deleted when the investigation is finished rather than accumulating in a folder of old customer exports — which is exactly how a company ends up holding personal data it cannot account for.

For products with a support obligation this is close to essential. A bug you cannot reproduce is a bug you fix by guessing, and guessing at production data is how the second incident gets created while fixing the first.

## Setting This Up

For an existing product this is typically one to two days: a deterministic seed script in the repository covering volume, uneven distribution, historical rows, awkward characters, empty fields and extremes; a defined set of test accounts including a second organisation for isolation checks; an anonymisation script covering every field holding personal data, including free text, logs, files and external identifiers; a staging refresh that anonymises during the copy; hard prevention of outbound email and third-party calls in non-production; snapshot and restore for fast reset; and both scripts wired into your checks so they cannot rot.

LaunchStudio sets this up as part of production readiness, and it is usually the change that makes every subsequent change safer. The engineers are Manifera's — eleven years, 160+ projects, and staging environments that do not email customers.

[Ask us what your staging environment is connected to](https://launchstudio.eu/en/#contact). The answer is occasionally alarming.

## Real example

### The Umlaut That Broke the Export

Sanne Verkerk built Deelnemerslijst in Lovable: registration and attendance for training providers, 73 providers, around 11,000 participants a year.

Her development database had 30 participants, all created by her, all with names like Test User and Jan Jansen. Every feature worked perfectly before release and then produced a support ticket within a fortnight.

The one that finally forced the issue was the certificate export. A training provider in Limburg ran a course with participants named Müller, Peña and Van 't Hoff. The export generated a CSV where those three rows were malformed, which the provider only discovered after sending 84 certificates to a corporate client with three of them blank. It was, from the client's perspective, the provider's mistake.

Two business days: a seed script producing 4,000 participants across twelve providers with deliberately uneven distribution — one provider holding 2,600 of them; names including apostrophes, diacritics and a 180-character company name; records dated across two years including some predating two schema changes; 15 percent with empty optional fields and a handful with dangling references; four named test accounts including a second provider for isolation checks and one deactivated user; a staging refresh that copies production and anonymises during the copy, covering participants, free-text notes, uploaded certificates, audit logs and payment provider identifiers; email credentials removed from staging entirely with every address rewritten to a capture domain; and a local snapshot and restore taking four seconds.

**Result:** the export bug reproduced on the first run of the new seed, along with two others nobody had reported — a list page that timed out for the largest provider and a search that missed diacritics entirely. Support tickets attributable to data shape fell from roughly three a week to two in the following quarter.

> *"I had tested everything. I had just tested it all against thirty people I invented, who were all called Jan and had all signed up last Tuesday."*
> — **Sanne Verkerk, Founder, Deelnemerslijst (Venlo)**

**Cost & Timeline:** €2,300 (seed script with realistic distribution and edge cases, test accounts, anonymisation for staging including free text and logs, outbound prevention, snapshot and restore, CI wiring) — completed in 2 business days.

## Frequently Asked Questions

### Can I point staging at my production database?

No. One mistaken delete becomes a real incident and test runs email real customers. Copy production and anonymise during the copy instead.

### What makes seed data realistic enough to be useful?

Volume, uneven distribution between accounts, historical rows predating schema changes, names with apostrophes and diacritics, empty optional fields, and a few extreme values. Those six find most data-shape bugs.

### Which fields get missed when anonymising?

Free-text notes, uploaded file contents, audit logs, stored email bodies and external identifiers like payment provider customer IDs. Test by trying to identify three customers you know in the anonymised copy.

### Should seed data be random?

No. Deterministic data means a failure reproduces. Random generators produce bugs that appear once and cannot be investigated.

### How do I stop staging emailing real customers?

Two layers: no credentials for your real email provider in that environment, and every address rewritten to a domain you control. Configuration alone is not enough, because configuration gets forgotten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can staging point at my production database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. A test deletion becomes real and test runs reach real customers. Copy production and anonymise during the copy."
      }
    },
    {
      "@type": "Question",
      "name": "What makes seed data realistic enough to be useful?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Volume, uneven distribution between accounts, historical rows, names with apostrophes and diacritics, empty optional fields and a few extremes."
      }
    },
    {
      "@type": "Question",
      "name": "Which fields are usually missed when anonymising?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Free-text notes, uploaded files, audit logs, stored email bodies and external identifiers such as payment provider customer IDs."
      }
    },
    {
      "@type": "Question",
      "name": "Should seed data be randomly generated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — deterministic data means failures reproduce. Random generation produces bugs that appear once and cannot be investigated."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop a staging environment emailing real customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Remove the real email provider's credentials from that environment and rewrite every address to a capture domain. Configuration alone gets forgotten."
      }
    }
  ]
}
</script>
