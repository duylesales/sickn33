---
Title: "AI Code to Production With Windsurf: What the Agent Leaves Out"
Keywords: ai code to production, windsurf, windsurf cascade, ai coding agent, production gaps, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Code to Production With Windsurf: What the Agent Leaves Out

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Code to Production With Windsurf: What the Agent Leaves Out",
  "description": "Windsurf's agentic workflow can build large parts of an app autonomously. This article covers what that agent typically leaves out when you take AI code to production: environment separation, secrets, auth boundaries, migrations, dependency sprawl and observability — and how to close each gap.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-09",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-code-to-production-with-windsurf-what-the-agent-leaves-out" }
}
</script>

Windsurf changed how many technical founders build. Instead of accepting suggestions line by line, you describe a feature and its agent plans, edits multiple files, runs commands, reads errors and iterates. Whole features appear in one session. That autonomy is precisely what makes it productive — and what makes the gap between "it runs" and "it's ready" harder to see. When you take Windsurf-built AI code to production, you are reviewing work that you watched happen but did not do.

This article covers what Windsurf's agent typically leaves out, why, and how to close each gap.

## Why Agentic Tools Leave Different Gaps

Autocomplete tools leave gaps at the level of lines: a missing check here, a hard-coded value there. Agentic tools leave gaps at the level of systems. An agent optimises for making the task succeed in the environment it can see: your local machine, your dev database, your `.env` file. Its success signal is "the command ran, the page loaded, the test passed." Anything that only matters in a different environment — production, other users, other time zones, attackers — is outside its feedback loop.

The agent also runs commands. It installs packages, runs migrations and sometimes modifies configuration. Those actions persist beyond the session in ways that are easy to miss in a long diff.

## Gap 1: One Environment for Everything

Agents build against whatever environment is configured. Often that is one Supabase or Postgres instance, one set of API keys, one `.env`. The resulting app has no separation between development, staging and production, and the agent's test runs, seed scripts and migrations have run against the same database your first users will use.

**Close it:** create separate projects or databases per environment, separate keys per environment, and make the production credentials unavailable on your development machine by default.

## Gap 2: Secrets Where the Agent Needed Them

When an agent hits an authentication error calling an API, a common fix is to place the key where the code can reach it — sometimes in client-side code, sometimes in a config file that gets committed. The agent's goal was to make the call work; it did.

**Close it:** scan the repository and history for secrets (gitleaks or trufflehog), rotate any found, move all secrets to server-side environment variables and add secret scanning to CI.

## Gap 3: Authentication Without Authorisation Boundaries

Agents implement login flows well because they are well-documented patterns. What they rarely implement unprompted is per-resource authorisation: checking that the logged-in user may access this specific record. The API routes the agent generates typically check "is there a session?" and stop.

**Close it:** define your access model explicitly, enforce it in the database (row-level security) or in a shared authorisation layer, and write tests that attempt cross-user access.

## Gap 4: Migrations Applied, Not Managed

Agents often modify the schema directly — running SQL in a session, or generating migrations and applying them immediately. The result can be a database whose state is not fully described by the migration files in the repository, making it impossible to recreate staging or production reliably.

**Close it:** reconcile the actual schema with migration files, commit a clean baseline, and from then on apply schema changes only through reviewed migrations in the deployment pipeline.

## Gap 5: Dependency Sprawl

Every time an agent solves a problem by installing a package, your dependency tree grows. Over a few weeks of agentic development, it is common to find three date libraries, two HTTP clients, abandoned packages and packages with known vulnerabilities.

**Close it:** audit dependencies, remove duplicates and unused packages, update vulnerable ones and enable automated dependency alerts.

## Gap 6: Errors Handled for the Session, Not for Users

When an agent encounters an error during its loop, it fixes it — sometimes by adding a `try/catch` that makes the error disappear. The session succeeds; in production, failures are swallowed silently.

**Close it:** review error handling, route unexpected errors to an error-tracking service, and ensure users see meaningful messages rather than silent failure.

## Gap 7: No Observability

The agent had a terminal and could see every error. In production, you have neither unless you set them up.

**Close it:** error tracking, structured logging with request identifiers, uptime monitoring and alerts to a real person.

## Keeping AI Code to Production Safe: Working With Windsurf After Hardening

None of this means you should stop using Windsurf. It means giving the agent guardrails:

- **Rules files** describing environments, secret handling and your authorisation model.
- **CI that the agent cannot bypass**: type checks, tests including negative authorisation tests, secret scanning and dependency checks on every pull request.
- **Reviewing command history**, not just diffs — what did the agent run?
- **No production credentials** on the machine where the agent works.

With those in place, the agent's speed becomes an advantage rather than a liability.

## Reconstructing What the Agent Did

When taking Windsurf-built AI code to production, the first step is understanding what the agent actually did across sessions. Sources to reconstruct it:

- **Git history:** commit messages, file changes and — importantly — added or modified configuration files, migrations and dependency manifests.
- **The agent's terminal history** where available: installed packages, executed scripts, database commands.
- **Database state versus migration files:** compare the live schema with what the migrations would produce; differences reveal manual or agent-run changes.
- **Environment variables** in each environment and on your machine.
- **Third-party dashboards:** API keys created, webhooks registered, storage buckets and their permissions.

Write a short inventory from these sources. It often reveals artefacts nobody remembers: test data in production, a webhook pointing to a local tunnel, a storage bucket made public to debug an image.

## Guardrails Configuration for Agentic Development

Once the gaps are closed, make continued agentic development safe:

| Guardrail | Purpose | How |
| --- | --- | --- |
| Rules file | Tell the agent your conventions | Environments, access model, secret handling, dependency policy |
| Separate credentials | Agent cannot reach production | Dev-only keys on the workstation; production only in CI/CD |
| Branch protection | No direct pushes to main | Required reviews and checks |
| CI checks | Catch what the agent missed | Types, tests, negative auth tests, secret and dependency scanning |
| Migration review | Schema changes are deliberate | Separate PRs, destructive-operation check |
| Dependency policy | Prevent sprawl | Allowed list or review required for new packages |

With these in place, the agent's autonomy operates inside boundaries that protect production.

## Reviewing Long Agent Sessions Efficiently

A long Windsurf session can produce hundreds of changed lines across many files. Review efficiently by reading in this order: new or changed routes and permissions; migrations and schema changes; dependency and configuration files; environment variable usage; then feature logic. Ask the agent to summarise its changes in the pull request description, including anything it installed or executed, and compare the summary with the diff. Differences between what the agent says and what it did are the most important things to catch.

## Seed Scripts, Test Data and Production

The seed-script incident in the example below is common in agent-built projects. Prevent it structurally: seed scripts check an environment variable and refuse to run unless it explicitly indicates development; production database credentials are not available where seeds run; test accounts use a reserved email domain that production blocks; and data created by tests is tagged so it can be found and removed if it ever leaks through. These measures cost minutes and prevent the kind of incident that makes customers doubt the whole product.

## Keeping Dependencies Under Control

Agents solve problems by installing packages, and each package brings maintenance and security obligations. After the initial clean-up, keep control with a simple policy: new dependencies require a line in the pull request explaining why, preference for packages already in use, periodic removal of unused packages (tools such as depcheck help) and automated vulnerability alerts. A smaller dependency tree is faster to build, easier to audit and less exposed to supply-chain risk.

## Observability for Agent-Built Apps

Agent-built apps benefit from slightly more observability than hand-built ones, because fewer people understand every path. Add request IDs to logs, report all unexpected errors to an error tracker, alert on new error types after each release and track key business events (signups, payments, core actions) so a silent break shows up as a drop in a chart. When something goes wrong, this data lets you — or the agent — find the cause quickly instead of guessing.

## Measuring Whether the Guardrails Work

Track a few signals over time: how often CI blocks agent pull requests and why, how many production incidents trace back to agent changes, and how long it takes from a problem appearing to a fix. A healthy setup shows CI catching issues regularly and production incidents becoming rare — evidence that agentic speed and production safety can coexist.

## A Windsurf Rules File Example

A concise rules file gives the agent context it otherwise lacks. An example for a Next.js and Supabase project:

```markdown
Project rules
- Environments: dev (local Supabase), staging, production. Never use production credentials.
- Data access from request handlers uses the user-scoped client; the service role client is only allowed in /server/admin.
- Every new table needs RLS policies and negative tests in /tests/access.
- Schema changes go in /supabase/migrations via a separate PR; never run SQL directly against remote databases.
- Do not add dependencies without listing them in the PR description with a reason.
- Never place secrets in client code or NEXT_PUBLIC_ variables.
- Report unexpected errors to Sentry; do not swallow exceptions.
```

Rules like these do not replace review, but they noticeably improve the first draft the agent produces.

## When to Pause Agentic Development

There are moments when it is wise to pause autonomous agent sessions: during an incident, while a data migration is in progress, in the days before a major launch and while a security review is underway. In those periods, changes should be small, deliberate and reviewed line by line. Resuming agentic work afterwards, with guardrails in place, keeps the speed benefits without mixing high-velocity changes into high-risk moments.

## The Balance to Aim For

The goal is not to slow the agent down but to let it run fast on a track with barriers. With environments separated, rules written, CI enforcing checks and observability in place, Windsurf remains one of the fastest ways to build — and AI code to production becomes a routine rather than a gamble.

## Where LaunchStudio Fits

LaunchStudio's work on Windsurf-built apps follows the seven gaps above: environment separation, secret rotation, authorisation, migration reconciliation, dependency clean-up, error handling and observability, plus CI guardrails for continued agentic development. The frontend and features you built stay. The engineering comes from Manifera — LaunchStudio brings Manifera's enterprise-grade engineering to the founder economy — with engineers in Ho Chi Minh City and European contact at Herengracht 420, Amsterdam. For the broader toolset, see [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/); for secret scanning, [gitleaks](https://github.com/gitleaks/gitleaks) is a solid open-source starting point.

If your app was mostly built by an agent, [send us your repository link](https://launchstudio.eu/en/#contact) and we will tell you which gaps apply.

## Real example

### An AI-Native Founder in Action: A Stable Management App Built in One Long Weekend

Arjen Wolters, a software developer and horse owner in Assen, built Stallenlog with Windsurf over a long weekend: an app for livery stables to manage boarding horses, feeding schedules, farrier and vet appointments, and monthly invoices to owners. It spread quickly among stables in Drenthe; 26 stables and about 700 horse owners were using it within two months.

A LaunchStudio review found the agentic pattern clearly. There was one Supabase project for everything; the agent's seed script, which created test horses and owners, had been run against production twice, and real owners had received invoices for horses named "Test Horse 3." The Postmark API key was in a committed config file. API routes checked for a session but not for stable or owner membership, so owners could see other stables' horses and vet notes. The schema had drifted from the migration files after several direct changes. The project had 214 direct dependencies, including four with known vulnerabilities. There was no error tracking.

Over nine business days, the team separated development, staging and production projects with separate keys, rotated and moved the Postmark key, implemented row-level security scoped to stables and owners with negative tests, reconciled the schema into a clean migration baseline, removed 61 unused or duplicate dependencies and updated vulnerable ones, replaced silent catches with reported errors and added Sentry and uptime checks. CI now blocks merges on tests, secret scanning and dependency alerts, and a Windsurf rules file documents environments and the access model.

**Result:** Stallenlog has continued to be developed almost entirely with Windsurf, now through pull requests guarded by CI. It grew to 58 stables in the following six months, with no further test-data leaks or cross-stable exposure.

> *"The agent built the app faster than I could have. It also ran my seed script on production, because nothing told it not to. Now something does."*
> — **Arjen Wolters, Founder, Stallenlog (Assen)**

**Cost & Timeline:** €2,500 (Launch Ready package: environments, secrets, authorisation, migrations, dependencies, observability and CI guardrails) — completed in 9 business days.

## Frequently Asked Questions

### Is Windsurf-generated code less secure than code from other AI tools?

Not inherently. Agentic tools produce different kinds of gaps — system-level rather than line-level — because they act autonomously in one environment. The same gaps appear with other agentic tools.

### How do I stop an AI agent from running commands against production?

Keep production credentials off the development machine, use separate projects per environment and deploy only through a CI pipeline. If the agent cannot reach production, it cannot change it.

### Should I review every diff Windsurf produces?

Review diffs for scope and sensitive areas, and also review the commands the agent ran. CI with tests, secret scanning and dependency checks catches much of what manual review misses.

### What does Manifera's experience add to agent-built codebases?

Manifera's engineers are used to taking over codebases written by others and establishing structure — environments, pipelines, tests — around them. Agent-built code is a new variant of a familiar task.

### Does agentic development affect SEO or AI discoverability?

Not directly. But agent-built apps often ship without metadata, sitemaps or performance care, and outages from unguarded changes hurt crawlability. Production guardrails protect visibility as well as security.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Windsurf-generated code less secure than code from other AI tools?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not inherently; agentic tools leave system-level gaps because they act autonomously in one environment." }
    },
    {
      "@type": "Question",
      "name": "How do I stop an AI agent from running commands against production?",
      "acceptedAnswer": { "@type": "Answer", "text": "Keep production credentials off the dev machine, separate environments and deploy only through CI." }
    },
    {
      "@type": "Question",
      "name": "Should I review every diff Windsurf produces?",
      "acceptedAnswer": { "@type": "Answer", "text": "Review scope and sensitive areas plus commands run; CI catches much of the rest." }
    },
    {
      "@type": "Question",
      "name": "What does Manifera's experience add to agent-built codebases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Experience establishing environments, pipelines and tests around codebases written by others." }
    },
    {
      "@type": "Question",
      "name": "Does agentic development affect SEO or AI discoverability?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly: missing metadata, poor performance and outages hurt crawlability." }
    }
  ]
}
</script>
