---
Title: "How Do I Set Up Automatic Deployments for a Lovable or Bolt App?"
Keywords: ci/cd lovable app, automatic deployment bolt, github actions supabase migrations, vercel deploy lovable, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Set Up Automatic Deployments for a Lovable or Bolt App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Set Up Automatic Deployments for a Lovable or Bolt App?",
  "description": "A simple CI/CD pipeline turns AI-generated changes into safe, repeatable releases. This guide shows a practical setup with GitHub, a host such as Vercel or Netlify, GitHub Actions for checks and Supabase migrations, and rollbacks.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-06",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "GitHub Actions documentation", "url": "https://docs.github.com/en/actions" },
    { "@type": "CreativeWork", "name": "GitHub: About protected branches", "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches" },
    { "@type": "CreativeWork", "name": "Supabase: Managing environments", "url": "https://supabase.com/docs/guides/deployment/managing-environments" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" }
  ]
}
</script>

**Short answer:** connect your GitHub repository to a host such as Vercel or Netlify so every push builds and deploys automatically, deploying the main branch to staging and a production branch to your live domain. Add a GitHub Actions workflow that runs a build, linting and a few tests on every change, and applies Supabase migrations to staging and then production. Keep environment variables per environment on the host, and use the host's instant rollback when a release goes wrong.

## Key Takeaways

- **A CI/CD pipeline turns AI-generated changes into safe, repeatable releases:** checks on every change, automatic deployment to staging, deliberate promotion to production and instant rollback.
- **Google's DORA research has for years linked continuous delivery practices** - small changes, automated testing, deployment automation - to better software delivery performance.
- **Database migrations belong in the pipeline,** applied to staging first with the Supabase CLI, never edited by hand in production.
- **Environment variables live per environment on the host,** with secrets in server-side stores rather than frontend variables.
- **Prefer additive migrations** so rolling back the app never breaks the database.

## The Pipeline in One Picture

| Event | What happens |
| --- | --- |
| Lovable or Bolt commits to `main` | Checks run; app deploys to staging; migrations apply to staging database |
| Pull request `main` → `production` | Checks run again; preview of what will change |
| Merge to `production` | App deploys to live domain; migrations apply to production database |
| Problem in production | Roll back to previous deployment in the host dashboard |

## Step 1: Connect the Host

Import the repository into Vercel or Netlify. Set the build command (usually `npm run build`) and output directory (often `dist` for Vite). Configure branch deployments: `main` to a staging domain, `production` to your live domain.

## Step 2: Environment Variables

Add variables per environment in the host: staging Supabase URL and key for staging, production values for production, Stripe test keys for staging and live keys for production. Frontend variables need the right prefix for your framework, such as `VITE_` for Vite. Secrets for server functions belong in Supabase edge function secrets, not in the frontend.

## Step 3: A Checks Workflow

A GitHub Actions workflow on pull requests and pushes:

1. Install dependencies
2. Lint (catches errors such as case-mismatched imports)
3. Type check, if TypeScript
4. Build
5. Run a handful of end-to-end tests against staging

If any step fails, the merge to production is blocked. Our article on [testing AI-built apps](https://launchstudio.eu/en/blog/how-do-i-test-my-ai-built-app-before-launch) covers which tests to start with.

## Step 4: Database Migrations

Use the Supabase CLI in GitHub Actions to apply migrations from `supabase/migrations`: to the staging project when `main` changes, to the production project when `production` changes. Store project credentials as GitHub secrets. Never apply untested migrations directly to production.

## Step 5: Edge Functions

Deploy edge functions with the Supabase CLI in the same workflow, so functions and database changes go out together.

## Step 6: Rollback Plan

Frontend rollbacks are instant on most hosts. Database rollbacks are harder: prefer additive migrations (add columns rather than rename or drop them immediately), so you can roll back the app without breaking the database.

## What CI and CD Mean in Practice

Continuous integration (CI) means every change is automatically built and checked: linting, type checking, tests. Continuous delivery (CD) means every change that passes checks can be deployed safely and repeatably, usually first to staging and then, deliberately, to production. For founders, the practical benefits are concrete: broken builds never reach customers, every release is traceable to a specific change and rolling back takes seconds.

## Why AI-Assisted Teams Benefit Most

AI builders and assistants increase the number and size of changes. Google's DORA 2024 report found that higher AI adoption was associated with lower delivery stability when teams lacked supporting practices. CI/CD is the most direct counterweight: each change is checked automatically, regardless of who or what wrote it. A pipeline does not slow Lovable down; it makes Lovable's speed safe.

## A Minimal GitHub Actions Workflow

A starting workflow for a Lovable or Bolt project runs on every push and pull request and performs these steps:

1. Check out the code
2. Install dependencies with a clean install
3. Run the linter to catch errors such as case-mismatched imports and unused code
4. Run TypeScript type checking if the project uses TypeScript
5. Build the production bundle
6. Run a small set of end-to-end tests against staging

If any step fails, the change cannot be merged into the production branch. GitHub's documentation on Actions and protected branches explains how to require passing checks before merging.

## Migrations Without Fear

Database changes are the riskiest part of any release. A safe approach with Supabase:

- Every schema change is a migration file in `supabase/migrations`
- The pipeline applies new migrations to the staging project when `main` changes
- Production migrations run only when the production branch changes, after staging has been tested
- Migrations are additive where possible: add columns and tables first, backfill data, switch the app, and remove old structures in a later release
- Destructive migrations are reviewed by a person before merging

This "expand and contract" approach means that at every point, both the old and new versions of the app can run against the database, which makes rollbacks safe.

## Managing Secrets in Pipelines

Pipelines need credentials: Supabase access tokens, project references, hosting tokens. Store them as encrypted secrets in GitHub, scoped to the workflows that need them, and never print them in logs. Use separate credentials for staging and production. OWASP's Secrets Management Cheat Sheet recommends least privilege and rotation; apply both to CI credentials, which are attractive targets because they can change production.

## Deployment Strategies for Small Apps

Most founder apps do well with simple strategies: automatic deployment to staging, manual promotion to production and instant rollback through the host. As traffic grows, consider feature flags to release features to a subset of users first, and scheduled release windows when you can watch monitoring. Avoid deploying large changes just before weekends or busy periods.

## Measuring Delivery Health

DORA's research uses four key metrics: deployment frequency, lead time for changes, change failure rate and time to restore service. Even a solo founder can track simplified versions: how often you release, how long a change takes from idea to production, how often a release causes a problem and how quickly you recover. Improving these numbers over time is a good sign that your process is working.

## Preview Deployments for Every Change

Hosts such as Vercel and Netlify create a preview URL for every pull request. Combined with a staging backend, previews let you or a reviewer click through a single change in isolation before it merges. For non-technical founders working with developers, previews are the clearest way to approve work: open the link, test the change, approve or comment. Protect previews from public access and search engines, as they may show unfinished features.

## Notifications and Visibility

Connect your pipeline to a channel you read - email, Slack or Teams - so you see when deployments succeed, fail or roll back. Visibility builds trust in the process and helps you correlate problems with releases quickly. Combined with error tracking tagged by release, you can usually tell within minutes whether a new deployment caused an issue.

## Common Mistakes

- Pipelines that deploy to production on every push to `main`, bypassing staging
- Migrations applied manually in the production dashboard
- Secrets printed in pipeline logs
- Tests that are skipped "temporarily" and never re-enabled
- No rollback plan for database changes
- Different Node versions locally, in CI and on the host

## Getting Started This Week

Connect your repository to your host with branch deployments, add a GitHub Actions workflow that lints and builds every change, move schema changes into migrations and document your rollback steps. Those four steps capture most of the value of CI/CD, and you can add tests and automated migrations incrementally afterwards.

## Pipelines for Edge Functions

Supabase edge functions should be deployed from the repository through the same pipeline as the frontend and migrations, using the Supabase CLI. Deploying functions by hand from a laptop or editing them in a dashboard creates drift between environments and makes it impossible to know what is running in production. With functions in the pipeline, every deployment is traceable to a commit, and staging and production stay identical.

## Keeping Versions Consistent

Many deployment surprises come from version differences: Node.js locally, in CI and on the host; package versions resolved differently on different machines. Pin your Node version in a configuration file the host and CI both read, commit your lockfile and use clean installs in CI. These small steps eliminate a whole category of "works on my machine" problems that are common when code moves out of Bolt or Lovable.

## Who Can Deploy

Decide who may promote changes to production and protect the production branch accordingly. For a solo founder, that is you, with checks required. For small teams, require one review for changes to migrations, policies and payment code. Keep production credentials limited to the pipeline and a minimal set of people.

## The Payoff

With a pipeline in place, releasing becomes routine: changes are checked automatically, staging shows what is coming, production changes are deliberate and mistakes are reversed in seconds. That calm is what lets founders keep building quickly with AI tools without fearing every release.

## Related Reading

A pipeline is most useful alongside a staging environment and automated tests. Our guides on staging for Lovable apps and on testing AI-built apps before launch cover both in detail.

## Summary

Check every change automatically, deploy to staging first, promote deliberately, migrate additively and keep rollback one click away.

## One Final Tip

Write your release steps in the README, even when the pipeline automates them, so anyone can understand what happens on each deploy.

## Common Problems

- Lovable or Bolt pushing broken builds to `main`: caught by checks before production
- Migrations created by hand in the dashboard: not in git, so pipelines miss them
- Production keys used in staging: payments or emails hit real customers

## Getting It Set Up

LaunchStudio sets up CI/CD as part of most launches, usually two to three days of the engagement. Our engineers have shipped 160+ projects for enterprise clients through Manifera, with GitHub Actions, Docker and cloud pipelines as standard; see [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/). Supabase documents [deploying with GitHub Actions](https://supabase.com/docs/guides/deployment/managing-environments), and [GitHub Actions documentation](https://docs.github.com/en/actions) covers workflows.

## Real example

### An AI-Native Founder in Action: The Field Inspection App Deployed From a Laptop

Wouter van Rossum runs an inspection company in Den Helder and built Keuringsapp with Bolt: inspectors fill in checklists on tablets for fire safety installations, attach photos and generate reports for clients. Deployment meant Wouter building on his laptop and uploading files to Netlify, while database changes were made by hand in the Supabase dashboard.

One evening he deployed a new checklist version without the matching database column, which existed only in his local notes. The next morning, inspectors could not submit reports for three hours. Another time, he deployed from a branch with unfinished changes.

LaunchStudio connected the repository to Netlify with staging and production branches, moved all schema changes into migrations, added a GitHub Actions workflow with lint, build, migrations and two end-to-end tests, deployed edge functions through the CLI, and documented the rollback steps.

**Result:** Over the next quarter, Wouter released 22 updates without a failed deployment. One broken build from a Bolt change was blocked automatically before reaching inspectors.

> *"Every release depended on me remembering five manual steps. Now the pipeline remembers them for me."*
> - **Wouter van Rossum, Founder, Keuringsapp (Den Helder)**

**Cost & Timeline:** €1,500 (Launch Ready package: Netlify branches, migrations, GitHub Actions checks, edge function deployment and rollback documentation) - completed in 4 business days.

## Frequently Asked Questions

### Do I need CI/CD for a small Lovable or Bolt app?

If customers depend on it, yes. A simple pipeline prevents the most common release failures: broken builds, missing environment variables and database changes out of sync with code. It takes days to set up and saves hours per incident.

### Can Lovable deploy directly to production?

Lovable can publish your app, but publishing directly skips staging and checks. With a pipeline, Lovable's commits go to staging first, and you promote tested changes to production.

### How do I handle Supabase database changes in a pipeline?

Keep every schema change as a migration file in your repository and apply them with the Supabase CLI in your workflow, first to staging, then to production. Avoid changing production schemas in the dashboard.

### How does Manifera structure release pipelines?

With the same stages for every project: checks, staging, promotion and rollback. Manifera's 11+ years of delivery show that consistent pipelines, not heroics, keep releases boring and safe.

### Can deployment problems affect my site's visibility?

Yes. Failed deployments that leave pages broken or returning errors, even briefly during crawling, can affect indexing and AI citations. Automated checks and instant rollbacks limit that exposure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need CI/CD for a small Lovable or Bolt app?",
      "acceptedAnswer": { "@type": "Answer", "text": "If customers depend on it, yes; it prevents broken builds, missing variables and schema drift." }
    },
    {
      "@type": "Question",
      "name": "Can Lovable deploy directly to production?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can publish, but a pipeline routes commits through staging and checks first." }
    },
    {
      "@type": "Question",
      "name": "How do I handle Supabase database changes in a pipeline?",
      "acceptedAnswer": { "@type": "Answer", "text": "Keep migrations in the repository and apply them with the Supabase CLI to staging, then production." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera structure release pipelines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Consistent stages: checks, staging, promotion and rollback." }
    },
    {
      "@type": "Question",
      "name": "Can deployment problems affect my site's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Broken pages during crawls affect indexing; checks and rollbacks limit exposure." }
    }
  ]
}
</script>
