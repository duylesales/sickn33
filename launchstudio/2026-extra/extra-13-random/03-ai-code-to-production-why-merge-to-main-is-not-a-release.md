---
Title: "AI Code to Production: Why 'Merge to Main' Isn't a Release Process"
Keywords: ai code to production, cursor deployment, release process, staging environment, ci/cd for ai code, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Code to Production: Why "Merge to Main" Isn't a Release Process

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Code to Production: Why 'Merge to Main' Isn't a Release Process",
  "description": "Technical founders using Cursor often ship AI code to production by pushing to main and letting the host auto-deploy. This article explains what a minimal real release process looks like: checks, staging, migrations, rollbacks and who presses the button.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-03",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-code-to-production-why-merge-to-main-is-not-a-release" }
}
</script>

If you write your app with Cursor, your release process is probably this: accept the diff, glance at it, commit, push to main, and let Vercel or Netlify deploy it within a minute. It feels professional because there is git and there is a pipeline. It is also, for AI code to production, one of the riskiest setups a solo founder can run — not because any single step is wrong, but because nothing between "the model wrote it" and "customers are using it" is designed to say no.

This is a practical article for technical founders: what a minimal release process actually needs, why AI-generated diffs make it more important rather than less, and how to put one in place without turning a two-person product into a bureaucracy.

## What Auto-Deploy From Main Actually Gives You

Auto-deploy is a delivery mechanism, not a release process. It guarantees that whatever is on main reaches production quickly. It says nothing about whether what is on main should be there.

With hand-written code, that gap is partly covered by the developer's own understanding: you wrote each line, so you know roughly what it touches. With AI-written code, the diff is often larger than the change you asked for. Ask Cursor to fix a date format on the invoice page and it may also refactor a helper used by five other pages, update a dependency, or adjust a database query "for consistency." The diff is plausible, the tests you have (if any) pass, and the side effects arrive in production.

## The Five Gates AI Code to Production Needs

You do not need an enterprise change-advisory board. You need five gates, each of which can be automated or reduced to a checklist.

**Gate 1: Automated checks on every push.** Type-checking, linting and whatever tests exist, run in CI (GitHub Actions is fine) on a branch — not on main. If the checks fail, the merge is blocked. This catches the class of AI mistake where code looks right but references a function that no longer exists.

**Gate 2: A preview or staging deployment.** Every branch gets deployed somewhere that looks like production but is not production, connected to a staging database with fake or anonymised data. You click through the change there. Most hosts give you preview deployments for free; the missing piece is usually the separate database.

**Gate 3: Migrations as a separate, reviewed step.** Database schema changes should never ride along silently with a code deploy. AI tools are happy to generate a migration that drops and recreates a column to change its type. On staging that is harmless. On production it deletes data.

**Gate 4: A rollback you have actually tried.** Your host can probably redeploy a previous build in one click. The question is whether that still works after a migration has run. A rollback plan that ignores the database is half a plan.

**Gate 5: A human who decides to release.** Even for a solo founder, the final merge to main should be a deliberate act, done at a sensible time — not at 23:40 on a Friday because the diff looked fine.

## Why AI Diffs Need Stricter Gates, Not Looser Ones

There is an intuition that AI-generated code is "probably fine" because it is based on common patterns. Common patterns are exactly the problem. The model produces what is typical, and what is typical in public code includes permissive CORS settings, missing authorisation checks and error handlers that swallow exceptions. Industry research frequently cited by LaunchStudio suggests around 45% of AI-generated code contains a security vulnerability; you do not want the release process to be the place where that statistic gets tested on customers.

There is also a volume effect. A founder using Cursor might produce three or four times as many commits per week as they would by hand. More changes means more chances for regressions. The gates scale with that volume; your attention does not.

## Staging Is Mostly a Data Problem

Technical founders often say they "have staging" because every branch gets a preview URL. Check where that preview URL gets its data. In a surprisingly large share of the codebases LaunchStudio reviews, preview deployments point at the production database, because the environment variables were copied once and never separated.

That means a test signup on a preview branch creates a real user, a test payment in a branch with a misconfigured key can hit live Stripe or Mollie, and a migration run "just to try it" runs against real customer data. A staging environment is only staging if its data is separate. Supabase branching, a second Supabase project, or a separate Postgres instance all work; what matters is that production credentials never appear in non-production environments.

## Rollbacks and the Migration Trap

The most common production incident LaunchStudio sees in Cursor-built apps is not a crash. It is a forward-only migration that cannot be undone quickly: a column renamed, a table restructured, a default value changed. The code deploy is rolled back in seconds; the data change is not.

The simple discipline is the expand-and-contract pattern:

1. **Expand:** add the new column or table alongside the old one.
2. **Migrate:** deploy code that writes to both and reads from the new one.
3. **Contract:** once you are confident, remove the old column in a later release.

Each step is individually reversible. It takes an extra deploy, and it removes the scenario where a rollback leaves the code and the database disagreeing about what exists. The [PostgreSQL documentation on ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) is worth reading once just to see which operations lock or rewrite tables.

## A Release Checklist You Can Paste Into Your Repo

- Branch pushed, CI green (types, lint, tests)
- Preview deployed against staging data, core flow clicked through
- Any migration reviewed separately and marked reversible or not
- If not reversible: backup taken immediately before release
- Release done during hours when you can watch it for 30 minutes
- Error tracking checked 30 minutes after release
- Rollback steps written down in the pull request description

It takes about ten minutes per release once it is habit. The first time it prevents a bad release, it pays for itself for the year.

## A Minimal Pipeline, Written Out

Talking about "gates" is abstract. Here is what a minimal CI configuration for a Cursor-built Next.js and Supabase app looks like in GitHub Actions. It is deliberately short — the point is that it runs on every pull request and blocks merging when it fails:

```yaml
name: ci
on:
  pull_request:
    branches: [main]
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run typecheck
      - run: npm run lint
      - run: npm test -- --run
      - name: Scan for secrets
        uses: gitleaks/gitleaks-action@v2
      - name: Flag destructive migrations
        run: |
          if grep -RinE "drop (table|column)|alter column .* type" supabase/migrations/; then
            echo "Destructive migration found: needs explicit review"; exit 1
          fi
```

Combined with branch protection that requires this job to pass and requires your approval, AI code to production can no longer bypass the checks — not by a tired founder at midnight, and not by an agent.

The migration check is intentionally blunt. It does not stop you from dropping a column; it forces a human to acknowledge it. In practice you add an override label or a comment in the pull request for intentional destructive changes, and everything else passes through untouched.

## Supabase Migrations in Practice

For Supabase projects, the most reliable workflow keeps migrations as SQL files in the repository and applies them through the CLI rather than through the dashboard:

1. Make the schema change on a local or branch database.
2. Generate a migration file with `supabase db diff`, then read it — AI-assisted diffs often include more than you expect.
3. Commit it in its own pull request, with a note on reversibility.
4. Apply to staging via CI; run the app against it.
5. Take a backup (or confirm point-in-time recovery is active), then apply to production.

The dashboard's table editor is convenient, but every change made there is invisible to your repository and to the next person who sets up staging. Most "staging doesn't match production" problems trace back to one dashboard edit made months ago.

## Watching a Release Instead of Hoping

A release is not finished when the deploy succeeds. For the first 30 minutes, check three things: the error tracker for new error types, the response times of your two busiest endpoints, and one real user flow end to end in production. If any of the three look wrong, roll back first and investigate second. The cost of an unnecessary rollback is a few minutes; the cost of investigating while customers are affected is much higher. After a few weeks this becomes a routine that takes less time than making coffee.

## Three Release Scenarios, Handled Properly

**A copy change.** Cursor updates text on the pricing page. CI passes, the preview looks right, you merge during the day. Total effort: two minutes more than pushing to main. The process adds almost nothing for trivial changes — which is exactly why it is sustainable.

**A new feature with a schema change.** You add "frozen membership" (as in the example below). The migration goes in its own pull request that only adds a nullable column and a new status value, reviewed and applied first. The feature code follows in a second pull request, behind a feature flag if possible. Existing rows are untouched, and rolling back the code leaves the database compatible.

**An urgent fix during an incident.** Payments are failing. The fastest safe path is: roll back to the last good deploy, confirm payments work, then fix forward on a branch with CI. Resist editing directly in production "just this once" — incidents are when untested changes do the most damage.

## Signs Your Release Process Is Working

After a month you should see: fewer "what changed?" moments, CI occasionally blocking a merge (proof it is doing something), no data surprises after deploys, and rollbacks that take minutes when needed. If CI never fails, either your code is perfect or your checks are too weak; usually the latter. Add a negative test for the most important permission in your app and watch whether it ever catches something.

## When the Process Can Stay Lighter

Not every project needs every gate from day one. A marketing site with no database can deploy from main safely. An internal tool with five trusted users can skip preview deployments for a while. The gates become essential the moment real customer data, payments or contractual uptime are involved — which, for most AI-built SaaS products, is the moment they are worth launching at all.

## Where LaunchStudio Fits

For technical founders, LaunchStudio's role is usually not to write your features. It is to put the release scaffolding under your AI code to production workflow: CI configured, staging separated properly, secrets managed per environment, migrations reviewed, monitoring connected. The engineering behind it comes from Manifera, which brings enterprise-grade engineering to the founder economy and has run release pipelines for clients from Amsterdam to Singapore for more than eleven years. You keep writing code in Cursor exactly as before; the difference is what stands between your diff and your customers.

If that sounds like your setup, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact) — the first conversation is 15 minutes and ends with a fixed-price proposal. Manifera's broader [web app development practice](https://www.manifera.com/services/web-app-develop/) uses the same pipeline patterns at larger scale.

## Real example

### An AI-Native Founder in Action: The Climbing Gym App That Deployed Its Own Outage

Daan Visser, a former data analyst in Delft, built PlankPal with Cursor: a membership and check-in app used by two bouldering gyms. Members scanned a QR code at the door; gym staff saw live occupancy and expiring memberships. Daan pushed to main several times a day, and Vercel deployed each push automatically.

One Thursday evening, Daan asked Cursor to add a "frozen membership" status. The generated migration changed the membership status column from text to an enum and, in doing so, rewrote every existing row — setting statuses the enum did not recognise to null. The deploy took forty seconds. For the next two hours, members with valid passes were refused at the door because the check-in screen treated null as expired. Rolling back the code did not help, because the data had already changed.

LaunchStudio's engineers restored the affected rows from a point-in-time backup, then built the release process around Daan's workflow: GitHub Actions running type checks and a small suite of check-in tests on every branch, a separate staging Supabase project with seeded data, migrations moved into their own reviewed pull requests, and a written rollback step required in each PR template. Error tracking was wired to Daan's phone.

**Result:** Over the following four months, PlankPal shipped 212 releases. CI blocked nine of them before merge, including two migrations that would have rewritten existing data. There were no further check-in outages.

> *"I had a pipeline, so I thought I had a process. What I actually had was a very fast way to ship whatever Cursor gave me."*
> — **Daan Visser, Founder, PlankPal (Delft)**

**Cost & Timeline:** €1,600 (release pipeline, staging separation, migration workflow and data recovery) — completed in 6 business days.

## Frequently Asked Questions

### Is auto-deploy from main always a bad idea?

Not always. For a static marketing site it is perfectly reasonable. It becomes risky once the app has a database with real user data and paying customers, because code changes and data changes then need to be released and rolled back together.

### How many tests does an AI-built app need before this process makes sense?

Fewer than you think. Five to ten tests covering signup, login, the core action and payment catch most serious regressions. The CI gate is valuable even with a small suite, because it also runs type checks that catch many AI mistakes on their own.

### Can Cursor write the CI pipeline and tests for me?

It can generate a reasonable starting point. The risk is that AI-written tests often mock so much that they pass regardless of behaviour. Having an engineer review what the tests actually assert is usually a small cost with a large payoff.

### What does Manifera's experience add to a small founder's release process?

Mostly pattern recognition. Manifera's engineers have seen which release mistakes cause real incidents across 160+ projects, so the process they set up is minimal but targeted — no ceremony for its own sake, and firm gates only where data or money is at stake.

### Does a proper release process help with search visibility?

Yes, indirectly. Fewer broken releases means fewer periods where pages return errors to crawlers, fewer broken internal links and more stable response times. Search engines and AI answer engines both favour sites that stay consistently available.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is auto-deploy from main always a bad idea?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. It is fine for static sites. It becomes risky once an app has a database with real user data and paying customers, because code and data changes must be released and rolled back together." }
    },
    {
      "@type": "Question",
      "name": "How many tests does an AI-built app need before this process makes sense?",
      "acceptedAnswer": { "@type": "Answer", "text": "Five to ten tests covering signup, login, the core action and payment catch most serious regressions, and the CI gate also runs type checks that catch many AI mistakes." }
    },
    {
      "@type": "Question",
      "name": "Can Cursor write the CI pipeline and tests for me?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can produce a starting point, but AI-written tests often mock so heavily that they pass regardless of behaviour. An engineer reviewing what the tests assert is worthwhile." }
    },
    {
      "@type": "Question",
      "name": "What does Manifera's experience add to a small founder's release process?",
      "acceptedAnswer": { "@type": "Answer", "text": "Pattern recognition from 160+ projects: a minimal process with firm gates only where data or money is at stake." }
    },
    {
      "@type": "Question",
      "name": "Does a proper release process help with search visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly. Fewer broken releases mean fewer error pages served to crawlers and more stable availability, which search engines and AI answer engines favour." }
    }
  ]
}
</script>
