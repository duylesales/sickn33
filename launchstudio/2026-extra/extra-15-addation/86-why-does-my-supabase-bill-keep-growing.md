---
Title: "Why Does My Supabase Bill Keep Growing?"
Keywords: supabase bill too high, supabase costs, reduce supabase egress, supabase spend cap, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Does My Supabase Bill Keep Growing?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Does My Supabase Bill Keep Growing?",
  "description": "Founders of AI-built apps are often surprised by rising Supabase invoices. This guide explains how Supabase billing works, which usage drives costs, such as compute, database size, egress, storage, auth users, functions and realtime, the common causes of unexpected growth in AI-built apps, and practical ways to reduce spending without hurting the product.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-12",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-does-my-supabase-bill-keep-growing" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase pricing", "url": "https://supabase.com/pricing" },
    { "@type": "CreativeWork", "name": "Supabase: Billing and usage", "url": "https://supabase.com/docs/guides/platform/billing-on-supabase" },
    { "@type": "CreativeWork", "name": "Supabase: Spend cap", "url": "https://supabase.com/docs/guides/platform/cost-control" },
    { "@type": "CreativeWork", "name": "Supabase: Compute and disk", "url": "https://supabase.com/docs/guides/platform/compute-and-disk" }
  ]
}
</script>

**Short answer:** Supabase bills a base plan plus usage, and AI-built apps often grow usage in ways founders do not notice: large images driving storage and egress, compute upgrades made to mask slow queries, tables bloated with logs or duplicate data, extra projects and branches left running, add-ons such as point-in-time recovery, bots inflating monthly active users, and functions or realtime subscriptions running far more often than needed. Open the usage page, find which line items grew, and fix the cause rather than only upgrading or downgrading.

## Key Takeaways

- **Supabase invoices combine a plan fee with usage-based items,** such as compute, disk, egress, storage, monthly active users, function invocations and add-ons.
- **Egress from serving files is a frequent surprise,** especially with unoptimised images and videos.
- **Compute upgrades are often bought to compensate for inefficient queries,** which optimisation could fix more cheaply.
- **Several projects, branches and add-ons each add cost,** and are easy to forget.
- **Spend controls, monitoring and regular reviews** prevent bill shock.

## How Supabase Billing Works

Supabase publishes its pricing and billing documentation, which change over time, so check current details. The general structure for paid plans:

| Component | What it measures |
| --- | --- |
| Plan fee | Base subscription per organisation |
| Compute | The size of each project's database instance, billed per hour, with some compute included in paid plans |
| Database disk | Disk space provisioned for the database |
| Egress | Data transferred out from the database, storage and functions |
| Storage | Size of files in Supabase Storage |
| Monthly active users | Users authenticated through Supabase Auth in a month, beyond included quotas |
| Edge function invocations | Number of function calls beyond quotas |
| Realtime | Concurrent connections and messages beyond quotas |
| Add-ons | Options such as point-in-time recovery, custom domains, IPv4 addresses, larger compute |
| Branching | Preview branches, billed according to usage |

On paid plans, Supabase has offered a spend cap that limits charges for certain usage beyond quotas, at the cost of restricting service when quotas are reached. Understand how it works on your plan, and whether you want it on or off.

## Cause 1: Egress From Files

Every time a user loads an image or downloads a file from Supabase Storage, data leaves Supabase and counts as egress. Apps that serve original phone photos in lists, auto-play videos or let users download large files can generate a lot of egress as usage grows.

**Fixes:** resize and compress images, serve thumbnails in lists, cache public assets through a CDN, lazy-load media and consider external storage with lower egress costs for very media-heavy products. Our guide on [Supabase storage costs and CDN](https://launchstudio.eu/en/blog/supabase-storage-costs-and-cdn-for-user-files) covers the details.

## Cause 2: Database Egress From Over-Fetching

Database egress grows when queries return more data than needed: `select('*')` on wide tables, loading entire lists to filter in the browser, refreshing dashboards every few seconds or realtime subscriptions to whole tables.

**Fixes:** select only needed columns, paginate, filter on the server, refresh less often and subscribe narrowly.

## Cause 3: Compute Upgrades to Hide Slow Queries

When an app becomes slow, upgrading to a larger compute size is the quickest fix. It often works temporarily, and then the next growth step requires another upgrade. Compute is one of the largest line items for growing projects.

**Fixes:** investigate slow queries, add indexes, rewrite expensive Row Level Security policies and remove N+1 patterns before upgrading. Many apps can return to a smaller compute size after optimisation. Our guide on [finding and fixing slow Supabase queries](https://launchstudio.eu/en/blog/slow-supabase-queries-how-to-find-and-fix-them) explains how.

## Cause 4: Database Size Growth

Disk usage grows with data, but in AI-built apps it often grows with things nobody needs:

- **Log tables** written on every request and never cleaned up
- **Audit or event tables** without retention
- **Duplicate data** from repeated imports or sync bugs
- **Large JSON blobs** stored for convenience, such as full API responses
- **Soft-deleted rows** never purged
- **Bloat** from frequent updates

**Fixes:** define retention per table, move logs to dedicated logging services or archive storage, clean up duplicates, store only needed fields and purge soft-deleted data after a defined period.

## Cause 5: Extra Projects and Branches

Each Supabase project runs its own database. Founders often accumulate projects: the original prototype, a second attempt, a staging project, a demo for a customer, an experiment with a new feature. Preview branches created for pull requests may also add cost.

**Fixes:** list all projects in your organisation, delete or pause those no longer needed, keep one staging and one production project and clean up branches when pull requests close.

## Cause 6: Add-Ons

Point-in-time recovery, custom domains, IPv4 addresses and larger compute sizes are valuable, but each adds cost. Sometimes they are enabled during an incident and never reviewed.

**Fixes:** review add-ons quarterly. Keep those that matter for production, such as point-in-time recovery for important data, and remove those for projects that do not need them.

## Cause 7: Monthly Active Users From Bots

Open sign-up forms attract bots that create accounts. If each fake account signs in, it may count as a monthly active user, and large numbers can push you beyond included quotas.

**Fixes:** add CAPTCHA protection such as Turnstile to sign-up, require email confirmation, rate-limit sign-ups and periodically remove unconfirmed or suspicious accounts.

## Cause 8: Functions and Realtime Running Too Often

- **Edge functions called on every render** because of a missing dependency in a React effect
- **Polling loops** calling functions every few seconds
- **Webhooks retried endlessly** because the function returns an error
- **Realtime subscriptions** opened repeatedly without cleanup, increasing connections and messages

**Fixes:** check function invocation counts per function, fix effect dependencies, replace polling with event-driven updates where sensible, fix failing webhook handlers and clean up subscriptions.

## Cause 9: AI-Related Workloads

If your app stores embeddings for AI search, vector data can grow quickly, with large indexes consuming disk and compute. Background jobs that re-embed documents unnecessarily add load.

**Fixes:** embed only what is needed, avoid re-embedding unchanged content, choose appropriate vector dimensions and index settings and remove embeddings for deleted content.

## How to Investigate a Rising Bill

1. **Open the organisation's usage page** and compare the current period with previous ones per line item.
2. **Identify the line items that grew most:** compute, egress, storage, MAU, functions or add-ons.
3. **Drill into the project** responsible, and check database size per table, storage per bucket, function invocations and query statistics.
4. **Connect growth to product events:** a new feature, a marketing campaign, a bot attack or a bug.
5. **Fix the cause,** then watch the next billing period.

## A Cost Review Checklist

| Area | Question |
| --- | --- |
| Projects | Are all projects still needed? |
| Compute | Could the project run on a smaller size after optimisation? |
| Tables | Which tables are largest, and do they need all their data? |
| Storage | Are images resized, and are old files deleted? |
| Egress | Which endpoints or buckets transfer the most data? |
| Auth | Are there many unconfirmed or bot accounts? |
| Functions | Which functions are invoked most, and is that expected? |
| Realtime | Are subscriptions narrow and cleaned up? |
| Add-ons | Is every add-on still needed? |
| Spend controls | Is a spend cap or alerting configured as intended? |

## Costs and Pricing Your Own Product

Supabase costs are part of your cost of goods. As your product grows, know the infrastructure cost per customer or per active user. That number informs your pricing, helps you spot unprofitable usage patterns and is something investors increasingly ask about. Our article on [what it costs to run an AI-built app per month](https://launchstudio.eu/en/blog/how-much-does-it-cost-to-run-an-ai-built-app-per-month) covers the full picture beyond Supabase.

## How LaunchStudio Helps

LaunchStudio reviews and reduces infrastructure costs for AI-built apps: analysing usage, optimising queries so compute can be right-sized, fixing image and file delivery, adding retention and cleanup for large tables, removing unused projects and add-ons, protecting sign-up from bots, fixing runaway functions and subscriptions and setting up cost monitoring.

The **Launch Ready** package (€800-€3,500) covers a cost and performance review with fixes; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting with ongoing monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, operating cloud infrastructure for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Event App Paying for Four Forgotten Projects

Gijs Kramer built Evenementenhub with Bolt and Supabase: a platform where event organisers sell tickets, publish programmes and share photos with attendees. Revenue grew steadily, but the Supabase bill grew faster, eventually becoming one of the company's largest costs. Gijs had upgraded compute twice when pages became slow, and considered moving to another provider.

The review found that only part of the bill came from production. The organisation contained four other projects: two old prototypes, a staging project and a demo created for a large customer, all running on paid compute, one with point-in-time recovery enabled. In production, event photos were served at full size, generating most of the egress. A request log table, written on every page view, had grown to tens of gigabytes. A realtime subscription in the programme page reconnected on every navigation, and a webhook from the ticketing provider failed repeatedly, causing thousands of retried function invocations a day. Bots created hundreds of fake accounts weekly through the open sign-up form.

LaunchStudio deleted the two old prototypes, paused the demo project and moved staging to a smaller compute size without add-ons. Event photos were resized with variants and served through a CDN. The request log was replaced by the hosting platform's logs, and the old table was archived and dropped. The realtime subscription was fixed with proper cleanup, the webhook handler was repaired, and Turnstile was added to sign-up, with unconfirmed accounts removed after a week. With slow queries indexed and policies optimised, production returned to a smaller compute size.

**Result:** The monthly Supabase bill fell by roughly 60% while usage continued to grow, and pages became faster than before the compute downgrade. Gijs now reviews the usage page monthly and stayed with Supabase.

> *"I was paying for prototypes I'd forgotten, photos nobody needed at full size and a webhook that kept failing at night."*
> - **Gijs Kramer, Founder, Evenementenhub (Arnhem)**

**Cost & Timeline:** €2,400 (Launch Ready package: usage analysis, project cleanup, image delivery, table retention, function and realtime fixes, bot protection and query optimisation) - completed in 6 business days.

## Frequently Asked Questions

### What makes up a Supabase bill?

A plan fee plus usage-based items such as compute per project, database disk, egress, storage, monthly active users beyond quotas, edge function invocations, realtime usage and add-ons like point-in-time recovery. Check Supabase's current pricing for exact rates and quotas.

### Why is my Supabase egress so high?

Usually because files, especially unoptimised images and videos, are downloaded often, or because queries return far more data than screens need. Resizing images, using a CDN, paginating and selecting only needed columns typically reduce egress significantly.

### Should I upgrade compute when my app is slow?

Only after optimising queries, indexes and policies. Many AI-built apps are slow because of inefficient data access, and upgrading compute only postpones the problem while increasing costs.

### How does Manifera's experience help reduce infrastructure costs?

Manifera has operated cloud infrastructure for enterprise clients for 11+ years, where cost control is part of operations. LaunchStudio applies that experience to find the specific causes of growing bills in AI-built apps and fix them.

### Does lowering costs affect my app's performance or visibility?

Done well, it often improves both. Smaller images, efficient queries and fewer unnecessary requests make pages faster, which helps users, search engines and AI answer engines, while lowering infrastructure costs.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What makes up a Supabase bill?",
      "acceptedAnswer": { "@type": "Answer", "text": "A plan fee plus usage such as compute, disk, egress, storage, MAU, functions, realtime and add-ons." }
    },
    {
      "@type": "Question",
      "name": "Why is my Supabase egress so high?",
      "acceptedAnswer": { "@type": "Answer", "text": "Large files downloaded often or over-fetching queries; resize images, use a CDN and select only needed data." }
    },
    {
      "@type": "Question",
      "name": "Should I upgrade compute when my app is slow?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only after optimising queries, indexes and policies." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help reduce infrastructure costs?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has operated enterprise cloud infrastructure for 11+ years and LaunchStudio finds the specific causes of growing bills." }
    },
    {
      "@type": "Question",
      "name": "Does lowering costs affect my app's performance or visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often positively; efficient delivery makes pages faster for users and crawlers." }
    }
  ]
}
</script>
