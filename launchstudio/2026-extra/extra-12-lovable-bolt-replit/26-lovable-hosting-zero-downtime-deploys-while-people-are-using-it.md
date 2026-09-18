---
Title: "Lovable Hosting: Zero-Downtime Deploys While People Are Using It"
Keywords: lovable hosting, zero downtime deployment, expand and contract migrations, atomic deploys, rolling releases, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Zero-Downtime Deploys While People Are Using It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Zero-Downtime Deploys While People Are Using It",
  "description": "Deploying to a product with active users means two versions run at once. What breaks in that overlap, how expand-and-contract migrations avoid it, and why the stale browser tab is the failure nobody tests.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-zero-downtime-deploys-while-people-are-using-it" }
}
</script>

For the first months, deploying is free. Nobody is using the product, so whatever happens during those ninety seconds happens to nobody.

Then one day somebody is halfway through filling in a form when you deploy, and the assumption that a deployment is instantaneous stops being true. For a period — seconds on a good platform, minutes on a poor one — two versions of your application exist at once, and the old one is still being used by people whose browsers have not reloaded.

Most deployment incidents in small products live entirely in that overlap. They are not caused by bad code; they are caused by two correct versions disagreeing.

## What Actually Overlaps

Three things, and each fails differently.

**The browser.** A customer loaded your application an hour ago. Their tab is running the old JavaScript, which will call your API for as long as they leave it open. Some of those users will be there tomorrow.

**The server.** Requests already in flight when the new version starts complete under the old one. Serverless platforms usually handle this well; a single server restarting handles it badly unless configured to drain.

**The database.** This is the one that produces damage rather than annoyance, because a schema change applies instantly and globally to both versions at once.

## The Rule That Prevents Most of It

Every deployment should be safe in both directions: the old code must work with the new database, and the new code must work with the old database.

If that holds, the order of operations stops mattering and a rollback becomes possible. If it does not hold, you have a moment — sometimes a long one — where something is broken no matter which version is running.

This is why dropping a column is dangerous and adding one is not. The moment the column disappears, every instance of the previous version that still expects it fails, including the tab your customer has had open since this morning.

## Expand and Contract, Concretely

The pattern that makes schema changes safe has four steps spread over at least two deployments.

**Expand.** Add the new structure — a column, a table — without removing anything. Nullable, with a default if needed. Nothing uses it yet and nothing can break.

**Migrate.** Deploy code that writes to both old and new, and backfill the existing rows in batches rather than in one statement that locks the table.

**Switch reads.** Deploy code that reads from the new structure. The old one is still being maintained, so a rollback is still safe.

**Contract.** In a later release, once you are confident, stop writing to the old structure and drop it.

Renaming is the same sequence: add, write both, read new, drop old. It takes two or three deployments instead of one, each of which is individually reversible, and at no point do running code and live schema disagree.

The steps to avoid entirely in a single deployment: dropping or renaming a column still referenced by the previous version, adding a non-nullable column with no default, and adding a constraint that existing data violates — the last of which fails the migration and leaves you part-deployed.

## Backfills Need Batching

A backfill that updates a million rows in one statement holds locks for the duration, which on a live table means your product stops working while it runs.

Do it in batches of a few thousand, with a pause between them, and make it resumable so it can be stopped and restarted. Run it as a background job rather than as part of the migration, so a deployment never waits on it.

For large tables, run the backfill well before the release that depends on it. The expand step can happen days earlier; there is no requirement for the four steps to be close together, and separating them removes time pressure from the part most likely to go wrong.

## The Stale Tab Nobody Tests

Your users do not reload. A browser tab open since Monday is running Monday's JavaScript on Thursday, and it will keep calling your API.

Two consequences worth handling. An endpoint the old version depends on cannot be removed the moment nothing new calls it — leave it in place for a period, even if it does nothing useful. And a response shape the old version expects cannot change incompatibly; add fields rather than renaming or removing them.

The user-facing fix is small and worth building: when the application detects that a newer version is available — by comparing a build identifier returned from the server — show an unobtrusive prompt inviting the user to reload. Not a forced refresh, which discards whatever they were typing, but a visible offer. Most people take it within minutes, which bounds how long you must support the previous version.

## Deploy at a Time You Can Watch

The last mile is behavioural rather than technical.

Deploy when you are able to look at the result for ten minutes: not as you leave, not on a Friday evening, not just before a meeting. Most bad releases are not discovered by monitoring; they are discovered by the person who shipped them, looking.

Then actually look. Load the product as a real user, exercise the thing you changed, and check the error tracker for anything new. Ten minutes, every time, is the cheapest insurance in software delivery.

And know your way back. The rollback should be identified and timed before you need it, and if a schema change means rollback is not possible, that is worth knowing before deploying rather than during.

## Feature Flags Make the Hard Releases Easy

There is a class of change that cannot be made compatible in both directions no matter how carefully you sequence it — a redesigned flow, a replaced calculation, a new integration that changes what customers see. For these, separate the deployment from the release.

A flag is a condition checked before the new behaviour runs. The code ships, switched off, and is exercised by nobody. You turn it on for your own account, then for one friendly customer, then for a tenth of the list, then everyone. If something is wrong it goes off in seconds — no deployment, no rollback, no migration to reverse.

For a small product this need not be a platform. A row in a table with a name and a state, read at the start of a request and cached briefly, covers almost everything. The two refinements worth having are the ability to enable a flag for a specific account rather than globally, and a record of who changed it and when.

The discipline that keeps this from becoming its own problem: remove the flag once the feature is settled. Flags that survive their purpose accumulate into a codebase where every path has four conditions and nobody can safely delete any of them — which is a slower version of the problem they were introduced to solve.

Used well, flags change what a release feels like. The deployment becomes routine and uneventful, and the decision to expose something to customers becomes a separate, reversible act taken when you are watching.

One more practical benefit specific to products like these: a flag is the only safe way to ship something an AI session built quickly. The code can be in production, reviewed at leisure, exercised by you alone, and promoted or deleted on evidence rather than on confidence.

That is a genuinely different way to work, and it suits the way these products are actually built: quickly, in bursts, by a founder who cannot review everything before it ships but can absolutely decide what customers get to see.

## Setting This Up

For an existing product this is typically half a day plus a habit: migrations reviewed against the two-way compatibility rule, expand-and-contract adopted for every column removal or rename, backfills batched and run as resumable background jobs ahead of the release that needs them, API responses changed additively with old endpoints retired on a delay, a build identifier exposed so the client can detect a newer version and offer a reload, a deployment checklist short enough to follow, and rollback identified and timed.

LaunchStudio sets this up as part of production readiness and operates it under the managed arrangement at €49 per month. The engineers are Manifera's — eleven years of releasing into live systems for clients including Vodafone, TNO and CFLW, from Herengracht 420 in Amsterdam.

[Ask us whether your next migration is reversible](https://launchstudio.eu/en/#contact). It is the question that decides how bad a mistake can get.

## Real example

### The Column That Broke Everyone Still Logged In

Ferdi Aalbersberg built Routeplanning in Lovable: delivery route planning for regional bakeries and food distributors, 24 companies, whose drivers use the app on phones from five in the morning.

A tidying change renamed a column from `adres` to `address` and updated the application in the same deployment. He deployed at 06:40 on a Wednesday, believing it trivial.

Every driver already on the road had the application open. Their browsers were running the previous version, which asked for a column that no longer existed, and every route refresh returned an error. Because they were driving, most did not reload; they called their dispatchers, who called Ferdi. Around 60 drivers across nine companies were affected for the 25 minutes it took him to understand and revert — and the revert did not work either, because the old code needed a column he had dropped.

He restored the column by hand, at 07:20, from a schema he was reading under considerable pressure.

One business day afterwards: expand-and-contract adopted, with the rename redone properly across three deployments — add `address`, write both and backfill in batches of 2,000 as a resumable job, switch reads a day later, drop `adres` a week after that; a rule written down that no deployment may remove or rename a column referenced by the version currently running; API responses changed additively only, with removed endpoints kept as no-ops for 30 days; a build identifier returned from the server with a quiet "a new version is available" prompt in the app, which drivers accept at their next stop; a four-line deployment checklist including a timed rollback; and deployments moved out of the 05:00 to 09:00 window entirely, which is the one Ferdi's customers actually work in.

**Result:** twelve months without a deployment incident, including two further schema changes of similar size. The version prompt turned out to matter as much as the migration discipline — before it, Ferdi had drivers running a three-day-old build without knowing.

> *"It was a rename. I have never done anything faster or more carelessly, and sixty drivers were standing next to their vans at seven in the morning because of it."*
> — **Ferdi Aalbersberg, Founder, Routeplanning (Sneek)**

**Cost & Timeline:** €1,600 (expand-and-contract migration of the rename, batched resumable backfill, additive API policy, client version detection and reload prompt, deployment checklist with tested rollback) — completed in 1 business day.

## Frequently Asked Questions

### Why does deploying break things when the code is correct?

Because two versions run at once. Browsers hold the old JavaScript, in-flight requests finish under the old server, and a schema change applies to both versions instantly.

### How do I rename a database column safely?

Add the new one, deploy code writing to both and backfill, deploy code reading the new one, then drop the old column in a later release. Each step is individually reversible.

### Why should backfills run in batches?

A single statement updating a large table holds locks for its duration, which stops your product. Batches of a few thousand rows with pauses, run as a resumable background job, avoid it.

### What about users who never reload the page?

Support the previous version for a period: keep endpoints alive, change responses additively, and show a prompt when a newer build is detected so most users update within minutes.

### When is the best time to deploy?

When you can watch the result for ten minutes, outside your customers' busiest window. Most bad releases are found by the person who shipped them, looking — not by monitoring.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do deployments break things when the code is correct?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two versions overlap: browsers run old JavaScript, in-flight requests finish on the old server, and schema changes apply to both at once."
      }
    },
    {
      "@type": "Question",
      "name": "How do I rename a column without downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Add the new column, write to both and backfill, switch reads in a later deploy, then drop the old column once you are confident."
      }
    },
    {
      "@type": "Question",
      "name": "Why must backfills be batched?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A single large update holds locks for its duration and stops the product. Use resumable batches of a few thousand rows with pauses."
      }
    },
    {
      "@type": "Question",
      "name": "How do I handle users who never reload the page?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep old endpoints alive for a period, change responses additively, and offer a reload prompt when the client detects a newer build."
      }
    },
    {
      "@type": "Question",
      "name": "When should I deploy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When you can watch for ten minutes afterwards, outside your customers' busiest hours. Most bad releases are caught by the person looking, not by monitoring."
      }
    }
  ]
}
</script>
