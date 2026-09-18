---
Title: "Replit and CI: Testing Before a Deployment"
Keywords: replit CI, continuous integration, automated checks, deployment gate, GitHub Actions, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit and CI: Testing Before a Deployment

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit and CI: Testing Before a Deployment",
  "description": "A one-click deploy is fast and has no gate. What to check automatically before code reaches customers, how to run it when the product lives on a prototyping platform, and the four checks worth having first.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-and-ci-testing-before-a-deployment" }
}
</script>

Deploying from Replit is a button. That is the appeal, and for a prototype it is exactly right — the shortest possible path from a change to seeing it work.

For a product with customers it is also a path with nothing on it. Whatever is in the project goes live, including the change made three minutes ago that has not been run, the syntax error in a file nobody opened, and the secret somebody pasted into a config while debugging.

Continuous integration is the gate: a set of automatic checks that run before anything reaches customers and refuse the deployment if they fail. For a small product this is a day of setup and it is the thing that makes deploying stop being a decision.

## The Four Checks Worth Having First

Order matters, because each is cheaper than the next and catches different things.

**Does it build?** The single most valuable check and the simplest. A build that fails in CI is a deployment that would have produced a broken product, caught in ninety seconds. This alone prevents the most embarrassing category of incident.

**Do the linter and type checker pass?** Undefined variables, unused imports, wrong types, columns that do not exist. Free, fast, and they catch the invented interfaces that generated code produces.

**Do the tests pass?** The proportionate suite described elsewhere in this series — authorisation, money, the main flow. This is the check that catches a behaviour change nobody intended.

**Is there a secret in the code?** A scan for credential patterns in the built output, failing the build when one appears. Given how often this series has returned to keys in frontend bundles, it earns its place.

Four checks, under three minutes, and they catch the overwhelming majority of what would otherwise reach customers.

## Where the Checks Run

The practical question for a product living on a prototyping platform: where does CI actually happen?

The realistic answer for most is a hosted repository's own automation — a workflow file in the repository that runs on every push. It is free at this scale, requires no infrastructure, and works regardless of where the product is deployed.

That implies the arrangement this series keeps recommending: the code lives in a repository, and the platform deploys from it rather than being the place the code lives. Deploying directly from an editing session means there is nothing to check before it happens.

The workflow is simple: on every push, install, build, lint, type check, test, scan. On the main branch, if all of that passes, deploy.

## Make Failure Mean Something

A check that can be ignored is not a gate.

Two decisions make it real. A failing check blocks the deployment — not a warning, not a notification, a refusal. And the checks are fast enough that waiting for them is not a reason to bypass them; if the suite takes fifteen minutes, it will be circumvented on the afternoon it matters.

The corollary is that a check which fails intermittently must be fixed or removed. A flaky test teaches you to re-run and continue, which trains you to ignore the gate entirely — and at that point you have the cost of CI with none of the benefit.

## Add Checks From Incidents

The four above are the start. The suite that actually protects a product grows from what has gone wrong.

A deployment broke because a migration was missing: add a check that the schema matches the migrations. An endpoint shipped without authorisation: add the cross-account test that walks every endpoint. A dependency with a known vulnerability reached production: add the audit to the pipeline. An image bundled at four megabytes: add a bundle size limit.

This is how a pipeline stays proportionate. Each check exists because something happened, rather than because a list somewhere recommended it, and the result is a gate that reflects your product's actual failure modes.

## Preview Deployments Are Worth More Than They Cost

One addition beyond checking: a running copy of every branch, deployed automatically, at its own URL.

For a solo founder this is the ability to look at a change in a real environment before merging it, which catches the things no automated check can — a layout that breaks on a phone, a flow that is confusing, a message in the wrong tone.

For a two-person team it is how the other person reviews without running anything locally.

And for a product with customers, it is how you show someone a proposed change and ask whether it is right, before it exists for everyone.

Protect them from indexing and from public access, as the environment article in this series describes, and give them their own non-production credentials.

## What Not to Automate Yet

A pipeline can grow into a project of its own, and for a product with a handful of customers most of what is written about CI is aimed at organisations with a different shape of problem.

Four things to leave until later.

**Browser-based end-to-end suites beyond one flow.** They are slow, they break for reasons unrelated to your code, and maintaining them costs more than they return at this size. One test covering the main journey is worth having; twenty are a part-time job.

**Deployment to multiple environments with approvals.** A staging environment is worth having; a promotion workflow with sign-off gates is ceremony for a team of one.

**Performance budgets and visual regression.** Useful eventually, noisy early, and both produce failures that require judgement rather than a fix — which is the property that makes a gate get ignored.

**Anything requiring maintenance you will not do.** A check that breaks every few weeks and needs attention is a check that will be disabled.

The proportionate pipeline for a small product is the four checks named above plus whatever incidents have added, running in three minutes, requiring no attention between failures. That is enough to remove the anxiety from deploying, which is the entire point — and every addition beyond it should earn its place by preventing something that actually happened.

## Migrations Need Their Own Gate

One category deserves separate treatment because it is where an otherwise good pipeline still lets something through: changes to the database.

Code can be rolled back. A migration frequently cannot, as the release article in this series describes, which makes it the one change where a failed deployment is not the worst outcome.

Three checks are worth adding once your product has a schema worth protecting.

**The migration runs cleanly against a copy of production's schema**, in CI, before anything is deployed. This catches the migration that works against a development database with 40 rows and fails against one with constraints and real data.

**The migration is reversible, or is explicitly marked as not.** A migration that drops a column is not reversible, and knowing that before deploying rather than during is the difference between a decision and a discovery.

**The application still works against the previous schema.** The expand-and-contract discipline in practice: deploy the schema change, confirm the running version still functions, then deploy the code. A check that the old code passes its tests against the new schema makes this verifiable rather than assumed.

Add a fourth if your data is large: that the migration completes within a sensible time on a realistic volume, since a statement that locks a table for eleven minutes is an outage regardless of whether it succeeds.

None of this is elaborate, and together they close the gap that remains after the ordinary checks — which is that the most dangerous change your product makes is the one your test suite cannot undo.

The same principle applies to any irreversible action a deployment can trigger — a bulk email, a charge, a file deletion. If a release can do it, the pipeline should know, and a human should have agreed to it deliberately.

## Setting This Up

For a Replit product this is typically one day: the code in a repository with the platform deploying from it rather than from an editing session, a workflow running on every push that installs, builds, lints, type checks, tests and scans for secrets, deployment gated on all of them passing, checks kept under about three minutes so they are never bypassed, flaky tests fixed or removed, preview deployments per branch with their own credentials and protected from public access, and a habit of adding a check whenever an incident reveals a gap.

LaunchStudio sets this up as part of production readiness, and it is usually the change that makes founders willing to deploy on a Friday. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us what currently stands between your code and your customers](https://launchstudio.eu/en/#contact). For many products the honest answer is nothing.

## Real example

### A Syntax Error at Half Past Four

Maud Terlouw built Rittenregistratie on Replit: journey and expense registration for home care organisations whose staff travel between clients, used by 11 organisations covering around 700 carers.

She deployed with the platform's button, from the editing session, several times a day. There were no tests and no checks.

On a Thursday afternoon she made a small change to the expense calculation and deployed at 16:25, then left to collect her children. The change contained a reference to a variable that did not exist in that scope — the kind of error a type checker reports instantly and a person reading quickly does not.

The application failed to start. Between 16:25 and 19:40, when a carer's message finally reached her, around 400 carers ending their shifts could not register the day's journeys. Most gave up; two organisations had staff record them on paper and re-enter them the following week.

Two business days: the code moved into a repository with the platform deploying from the main branch rather than from an editing session; a workflow running on every push that installs, builds, lints, type checks, runs tests and scans the built output for credential patterns; deployment gated on all of it; a test suite of 31 tests covering authorisation across 14 endpoints, the expense and distance calculations, and one end-to-end journey registration; the whole pipeline running in 95 seconds; preview deployments per branch with their own database and credentials, protected from public access; and an external uptime check that would have reported the outage within two minutes.

**Result:** the pipeline has blocked 14 deployments in the following year, of which 9 were build or type failures that would have broken the product exactly as the original incident did. Maud notes that she now deploys more often rather than less, because the decision has been removed from it.

> *"I deployed at twenty-five past four and went to collect my children. Four hundred carers could not register their journeys for three hours, and the error was a variable name a type checker would have caught before I left the room."*
> — **Maud Terlouw, Founder, Rittenregistratie (Gouda)**

**Cost & Timeline:** €2,600 (repository-based deployment, CI workflow with build, lint, type check, test and secret scanning, deployment gating, 31-test suite, preview deployments with isolated credentials, uptime monitoring) — completed in 2 business days.

## Frequently Asked Questions

### What is the first check worth adding?

That it builds. A build failure caught in CI is a broken deployment prevented, it takes ninety seconds, and it requires no tests to exist.

### Where do the checks run if my product is on Replit?

In your hosted repository's own automation, on every push. That requires the code to live in a repository with the platform deploying from it rather than from an editing session.

### How long should the pipeline take?

Under about three minutes. A slow pipeline is one that gets bypassed on the afternoon it would have mattered most.

### What do I do about a test that fails intermittently?

Fix it or remove it. A flaky check teaches you to re-run and proceed, which is the habit that makes the whole gate worthless.

### Which checks should I add after the basics?

Whichever ones an incident tells you to. A missing migration, an unauthorised endpoint, a vulnerable dependency, an oversized bundle — each becomes a check after it happens once.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the first CI check worth adding?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "That the project builds — ninety seconds, no tests required, and it prevents the most common broken deployment."
      }
    },
    {
      "@type": "Question",
      "name": "Where does CI run for a Replit product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In your hosted repository's automation on every push, with the platform deploying from the repository rather than from an editing session."
      }
    },
    {
      "@type": "Question",
      "name": "How fast should a CI pipeline be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Under about three minutes, or it will be bypassed exactly when it mattered."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do with a flaky test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fix it or delete it. Intermittent failures teach you to ignore the gate entirely."
      }
    },
    {
      "@type": "Question",
      "name": "Which checks come after build, lint and tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Whichever an incident calls for — migration consistency, cross-account authorisation, dependency audits, bundle size limits."
      }
    }
  ]
}
</script>
