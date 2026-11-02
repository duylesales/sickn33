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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app" }
}
</script>

**Short answer:** connect your GitHub repository to a host such as Vercel or Netlify so every push builds and deploys automatically, deploying the main branch to staging and a production branch to your live domain. Add a GitHub Actions workflow that runs a build, linting and a few tests on every change, and applies Supabase migrations to staging and then production. Keep environment variables per environment on the host, and use the host's instant rollback when a release goes wrong.

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
