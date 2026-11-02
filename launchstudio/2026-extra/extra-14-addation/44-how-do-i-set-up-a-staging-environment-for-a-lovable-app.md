---
Title: "How Do I Set Up a Staging Environment for a Lovable App?"
Keywords: lovable staging environment, staging supabase project, test before production lovable, lovable preview vs production, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Set Up a Staging Environment for a Lovable App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Set Up a Staging Environment for a Lovable App?",
  "description": "A staging environment lets you test Lovable changes before customers see them. This guide shows a practical setup with GitHub branches, a separate Supabase project, a staging deployment, migrations and test data, plus the workflow that keeps it useful.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-set-up-a-staging-environment-for-a-lovable-app" }
}
</script>

**Short answer:** use two Supabase projects (staging and production), deploy your Lovable code from GitHub to two environments on a host such as Vercel or Netlify, apply database changes as migrations to staging first, and promote to production only after testing. Lovable itself becomes your editing tool, while what customers see is controlled by your deployment, not by the "Publish" button.

## Why Lovable Apps Need This

Every Lovable prompt can change many files. Without staging, each prompt is a live experiment on your customers. Staging gives you a safe copy where you can check that a new feature works and that nothing else broke, especially login, payments and data access.

## The Setup

| Component | Staging | Production |
| --- | --- | --- |
| Git branch | `main` (Lovable syncs here) | `production` or release tags |
| Supabase project | Separate staging project, test data only | Production project, real data |
| Hosting | Staging site, e.g. `staging.yourapp.nl` | `yourapp.nl` |
| Environment variables | Staging keys (Supabase, Stripe test mode) | Production keys (Stripe live mode) |
| Payments | Stripe or Mollie test mode | Live mode |
| Email | Sandbox or restricted recipients | Real sending |

Lovable keeps syncing with `main`. Your host deploys `main` to staging automatically. When staging looks good, you merge `main` into `production`, and the host deploys that to your live domain.

## Database Changes as Migrations

Lovable stores Supabase changes as migration files in `supabase/migrations`. Apply them to staging first, test, then to production. Avoid changing the production database by hand in the dashboard; changes made outside migrations create drift, and staging stops being a reliable copy.

## Test Data Without Real People

Staging should not contain copies of real customer data. Use a seed script with realistic but fictional users, organisations and records. If you must reproduce a production issue, anonymise data before copying it. This also keeps you on the right side of the GDPR.

## A Release Routine That Takes 15 Minutes

1. Build the feature in Lovable; it lands on staging automatically
2. Log in to staging as two different test users and try the feature
3. Check the critical paths: login, a payment in test mode, a core action
4. Review migrations in the pull request from `main` to `production`
5. Merge, watch the production deploy, check monitoring for errors
6. If something is wrong, roll back to the previous deployment

## Common Mistakes

- **Staging using production keys.** A "test" sends real emails or charges real cards.
- **Publishing from Lovable to the live domain.** Bypasses staging entirely.
- **Staging database drifting.** Manual changes in production that staging never received.
- **Nobody actually testing on staging.** A staging site no one opens is just an extra bill.

## Getting It Set Up

A staging setup is included in most LaunchStudio launches; on its own it typically takes two to four days within a Launch Ready package. Our engineers have shipped 160+ projects for enterprise clients through Manifera, where separate environments are standard; see [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/). Supabase's guide to [managing environments](https://supabase.com/docs/guides/deployment/managing-environments) explains the migration workflow. If you have not connected GitHub yet, start with our guide to [exporting Lovable code to GitHub](https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building).

## Real example

### An AI-Native Founder in Action: The Booking App That Broke on a Saturday Morning

Wessel Jansen runs a padel and squash centre in Hoorn and built Baanboeker in Lovable: members book courts, pay per session and join waiting lists. On a Friday evening, he asked Lovable to add a "bring a guest" option and published. On Saturday morning, the busiest booking time, nobody could book: the new guest field was required in the database but not sent by the older booking form still used on mobile.

Wessel had no staging, no previous version to roll back to and no idea which change had caused it. He reverted manually by prompting, which took four hours of lost bookings.

LaunchStudio created a staging Supabase project with seeded test members and courts, set up Vercel deployments for `main` (staging) and `production`, configured Mollie test mode on staging, moved schema changes into migrations, and wrote a one-page release routine. Instant rollbacks became available through the host.

**Result:** Over the next three months, Wessel shipped 14 changes through staging. Two would have broken bookings; both were caught on staging and fixed before members noticed.

> *"Publishing on a Friday night felt efficient. Losing Saturday morning showed me what efficient really costs."*
> - **Wessel Jansen, Founder, Baanboeker (Hoorn)**

**Cost & Timeline:** €1,250 (Launch Ready package: staging project, seed data, dual deployments, test-mode payments, migrations and release routine) - completed in 4 business days.

## Frequently Asked Questions

### Isn't Lovable's preview already a staging environment?

Not quite. The preview usually talks to the same backend as your published app, so database changes affect real data. A proper staging setup has its own database, its own keys and test-mode payments.

### Do I need a second Supabase project for staging?

Yes, for meaningful staging. A separate project keeps test data away from customers and lets you apply migrations safely before production. Smaller plans make this affordable for most founders.

### Can I keep using Lovable with a staging and production setup?

Yes. Lovable syncs with your main branch, which deploys to staging. You promote to production through a merge or release, so Lovable remains your editor while you control what reaches customers.

### Why does Manifera treat staging as non-negotiable?

Because in 11+ years of client work, most production incidents came from untested changes. A staging environment turns many of those incidents into ordinary bug fixes found before customers notice.

### Should my staging site be indexed by search engines?

No. Protect staging with a password or block indexing, so search engines and AI crawlers do not index duplicate or test content alongside your real site.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Isn't Lovable's preview already a staging environment?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not quite; it usually shares the production backend. Staging needs its own database, keys and test-mode payments." }
    },
    {
      "@type": "Question",
      "name": "Do I need a second Supabase project for staging?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, to keep test data separate and apply migrations safely before production." }
    },
    {
      "@type": "Question",
      "name": "Can I keep using Lovable with a staging and production setup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Lovable syncs to main, which deploys to staging, and production is promoted by merge or release." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera treat staging as non-negotiable?",
      "acceptedAnswer": { "@type": "Answer", "text": "In 11+ years of client work, most incidents came from untested changes that staging catches." }
    },
    {
      "@type": "Question",
      "name": "Should my staging site be indexed by search engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Password-protect or block indexing to avoid duplicate or test content being indexed." }
    }
  ]
}
</script>
