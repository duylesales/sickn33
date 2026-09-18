---
Title: "Supabase Security: Row Level Security Policies That Hold"
Keywords: supabase security, row level security, rls policies, ai app security, Lovable, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Security: Row Level Security Policies That Hold

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: Row Level Security Policies That Hold",
  "description": "Row level security is the one control standing between your public key and your customers' data. How policies actually evaluate, the mistakes that make them decorative, and how to test them by trying to break in.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-security-row-level-security-policies-that-hold" }
}
</script>

Here is the uncomfortable shape of a Supabase-backed application. Your public key is in the browser, where anybody can read it. That key can reach the automatically generated API. The API can reach every table. And the only thing standing between a curious visitor and your entire database is a set of rules written in SQL that most founders have never read.

Those rules are row level security policies. When they are right, the architecture is genuinely sound — protection sits in the database, where it applies no matter which query arrives or who wrote it. When they are absent, partial, or written to make an error go away, the architecture is a public database with a login screen in front of it.

This is the single most consequential piece of an AI-built product, and it is the piece generation tools handle least reliably, because the rules encode your business and the tool does not know your business.

## What the Policy Actually Sees

A policy is a condition evaluated for every row, on every operation, for every request. If the condition is true, the row is visible or the change is allowed. If it is false, the row simply does not exist as far as that request is concerned — no error, no denial, just absence.

That silence matters in both directions. A policy that is too permissive produces no signal at all; everything works and too much is visible. A policy that is too restrictive produces an application where data has mysteriously vanished, which is what founders usually notice first and usually fix in the worst possible way.

The request carries an identity. For a logged-in user, that is their account and whatever claims their session token contains. For an anonymous visitor it is a limited role. For server-side code using the privileged key, policies are bypassed entirely — which is exactly why that key must never leave your server.

## Enabling Is Not the Same as Protecting

Two separate steps, and the gap between them is where breaches live.

Turning row level security on for a table means the table now denies everything by default. Writing policies means specifying what is allowed. A table with security enabled and no policies is invisible to your application, which looks broken. A table with policies and security **not** enabled is wide open, which looks fine.

The second case is the dangerous one, because nothing about the running application indicates a problem. Policies exist in the dashboard, someone remembers writing them, and they are never consulted.

Check every table individually. Not the ones you think matter — every table, including the ones a tool created that you have never opened.

## Four Ways Policies Fail in Practice

**Written to silence an error.** A feature returns nothing, the fastest fix is a policy allowing everything, and the fastest fix is what gets generated when the request is "this query returns no rows, fix it". The feature works and the table is public.

**Only covering reads.** Select is the operation people think about. Insert, update and delete each need their own treatment, and an application where anyone can read only their own records but update anybody's is a common and serious result.

**Trusting a value the client sent.** A policy comparing a row's owner against an identifier supplied in the request rather than derived from the session is decorative. The client can send any identifier it likes. Ownership must come from the authenticated session, never from a parameter.

**Trusting a claim the user controls.** A policy checking whether a token claims administrator rights is only as good as the process that put that claim there. If a role or flag lives in a table users can update, they can promote themselves — and this specific mistake appears in AI-built applications regularly, because storing a role beside the user profile is the obvious design and locking that column down is not.

## Ownership, Membership, and the Shape of Your Rules

Most products need one of two patterns.

**Ownership:** each row belongs to one account, and that account is the only one that may see or change it. Simple, and correct for personal tools.

**Membership:** rows belong to an organisation, and people belong to organisations, sometimes with different roles. This covers nearly every business product, and it requires a deliberate structure — a table of organisations, a table linking people to organisations with a role, and policies that check membership rather than ownership.

The mistake worth avoiding is starting with ownership because it is simpler and discovering six months later that customers want colleagues to share an account. Retrofitting membership touches every table and every policy. If there is any chance your customers are companies rather than individuals, build membership from the start; the extra work is an afternoon now and a fortnight later.

## The Performance Side Nobody Mentions

Policies run on every row of every query, so what they contain matters for speed.

A policy performing a lookup in another table for each row can turn a fast query into a slow one as data grows. Two remedies are standard: index the columns your policies filter on, and structure policies so the expensive part is evaluated once rather than per row. If your application became noticeably slower after policies were added, this is almost always the cause — and the wrong response is removing the policies.

## Testing Policies by Attacking Them

Reading a policy tells you what you meant. Only a test tells you what it does.

Create two accounts in two browsers, ideally belonging to different organisations. Then, systematically: open a record belonging to the other account by changing an identifier in the address. Attempt to update the other account's record. Attempt to delete it. Attempt to create a record assigned to the other account. Log out and repeat every one of those. Finally, using only your public key and a plain HTTP client, try to list every table you have — including the ones your interface never touches.

That last step is the one that finds the forgotten table, and it takes five minutes. Anything that returns data it should not is a finding, and every finding is one somebody else could have made first.

## Write the Rules Down in Plain Language First

Before any SQL, one page: for each table, who may read, who may create, who may change, who may delete, and on what basis. Twenty lines for most products.

This document does three jobs. It turns policy writing into translation rather than invention. It gives you something to test against. And it is the artefact you hand a security reviewer or a business customer who asks how access is controlled — a question that otherwise produces an uncomfortable pause.

## What Good Looks Like

Every table has security enabled, verified individually. Every table has explicit policies for select, insert, update and delete. Identity comes from the session, never from a request parameter. Roles live in a table users cannot modify. The access model exists as a written page. The whole set has been tested by attempting to bypass it from a second account and from no account. And the privileged key exists only in server-side code.

That is perhaps a day of work for a typical product, and it is the difference between a product a Dutch business can buy and one that cannot survive its first serious question.

## Keeping Policies Correct as the Product Changes

Getting the rules right once is the smaller half. Keeping them right through a year of changes is where most products quietly regress.

**Every new table needs a decision, not a default.** The moment a table is created — by you, by a colleague, or by an agent session adding a feature — somebody must decide who may read, create, change and delete its rows. A table created during a busy afternoon and protected "later" is a table that is never protected, because nothing about the running application reminds you.

Make it mechanical: a new table is not finished until security is enabled, four policies exist, and a line has been added to your written access model. Three minutes, and it is the only thing that prevents the slow accumulation of unprotected tables that every audit finds.

**Migrations should carry their policies.** If a table is created by a migration file, its policies belong in the same file. Policies applied by clicking in a dashboard exist only in that one database, so a restore, a second environment or a new developer produces a system where the data is present and the protection is not — the most dangerous possible divergence, because everything appears to work.

**Watch for policies removed rather than corrected.** When a feature breaks with a permissions error, the two available fixes are to grant the right access or to remove the check, and the second is faster. Over a year, that asymmetry erodes a well-designed model one incident at a time. Reviewing changes to policy files is worth more than reviewing almost any other part of the code.

**Re-test after structural changes.** Adding a column, splitting a table, introducing a new role or changing how organisations work can all invalidate assumptions the policies rest on. The adversarial test from two accounts takes five minutes and belongs in the routine before any release that touched the schema.

**Schedule one review a quarter.** List every table, confirm security is enabled, confirm four policies exist, and run the cross-account test. Half an hour, four times a year, and it catches the drift that no single change looked responsible for.

## Getting the Access Model Right

For an application that already has users, this is bounded work rather than a rebuild.

LaunchStudio approaches it in a fixed order: every table inventoried including the ones nobody remembers, the access model written in plain language with you, security enabled everywhere, policies written per operation with identity derived from the session, roles moved somewhere users cannot reach, indexes added so policies do not cost performance, and the whole set verified by attempting to break in from a second account — with the interface you built left untouched and the policies documented so you can extend them yourself.

The engineers are Manifera's: eleven years of production database work for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City. [Send us your project](https://launchstudio.eu/en/#contact) for a specific assessment, usually within one business day, or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers.

## Real example

### A Members Table Every Member Could Read

Koen Vermeulen built Ledenadmin with Lovable: membership administration used by five sports clubs around Helmond — two football clubs, a tennis club, a swimming club and a gymnastics association. Roughly 4,000 members in total, with names, addresses, dates of birth, bank details for direct debits, and in some cases notes about medical conditions relevant during training.

Row level security was enabled on the members table. The policy allowed any authenticated user to select from it. It had been written that way during development, when a list had returned nothing and the fastest fix was a rule that returned everything.

Every member with a login — all 4,000 — could read every other member's record, across all five clubs, by querying the API directly with the public key present in the page.

Nobody had. The problem surfaced when the tennis club's treasurer, who worked in IT, asked how the clubs were separated from each other and was not satisfied with the answer.

Nine business days of work: an organisation and membership structure introduced so each club is a tenant with roles for member, committee and administrator; policies rewritten per table and per operation with identity taken from the session; the role column moved out of the user-editable profile into a membership table users cannot write to; bank details moved into a separate table readable only by club administrators; indexes added on the membership columns after a policy-driven query slowed a list page; the access model written as a one-page document; and the whole set tested from three accounts in different clubs plus an unauthenticated client, including a direct enumeration of every table with the public key.

That last test found two further tables the application never used — an early import staging table containing an older copy of the member list, and an unused audit table — both readable and both removed.

**Result:** the five clubs signed a joint data processing agreement that had been stalled, and Koen now has a document he sends when a club's board asks who can see what.

> *"Four thousand members could read each other's bank details because eighteen months ago a list came back empty and I made the error go away."*
> — **Koen Vermeulen, Founder, Ledenadmin (Helmond)**

**Cost & Timeline:** €4,600 (organisation and membership model, policies rewritten per operation, role relocation, indexing, documentation and adversarial testing) — completed in 9 business days.

## Frequently Asked Questions

### Is enabling row level security enough on its own?

No. Enabling it makes a table deny everything; policies specify what is allowed. The dangerous case is the reverse — policies written while security was never actually enabled on the table, which looks fine and protects nothing.

### Why do policies that allow everything get written?

Because a query returning no rows is a visible bug and an over-permissive policy makes it disappear instantly. That is the fastest fix and it is what gets generated when the request is phrased as "this returns nothing, fix it".

### Can a policy trust an identifier sent by the app?

No. Anything the client sends, the client can change. Ownership and membership must be derived from the authenticated session, and roles must live somewhere the user cannot update — otherwise a user can promote themselves.

### Do I need separate policies for updates and deletes?

Yes. Each operation is governed separately, and covering only select is a common and serious gap: users who can read just their own records but modify anyone's.

### How do I know my policies actually work?

Test them adversarially. Two accounts in two browsers, attempt to read, update, delete and create across the boundary, repeat while logged out, and finally list every table using only your public key — which is how forgotten tables get found.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is enabling row level security enough on its own?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Enabling makes a table deny everything and policies specify what is allowed. The dangerous case is policies written on a table where security was never enabled."
      }
    },
    {
      "@type": "Question",
      "name": "Why do policies that allow everything get written?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because an empty result is a visible bug and a permissive policy removes it instantly — which is what gets generated when the request is 'this returns nothing, fix it'."
      }
    },
    {
      "@type": "Question",
      "name": "Can a policy trust an identifier sent by the app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Identity must come from the authenticated session, and roles must live in a table the user cannot modify, or users can promote themselves."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need separate policies for updates and deletes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — each operation is governed separately, and covering only select leaves users able to modify records they can merely read."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know my policies actually work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Attack them: two accounts attempting to read, update, delete and create across the boundary, repeated logged out, plus a direct table listing with only the public key."
      }
    }
  ]
}
</script>
