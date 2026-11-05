---
Title: "Plan Limits and Entitlements in SaaS"
Keywords: saas plan limits, entitlements saas, feature gating stripe, enforce subscription limits supabase, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Plan Limits and Entitlements in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Plan Limits and Entitlements in SaaS",
  "description": "Pricing plans only work if the product enforces them. This guide explains how to implement plan limits and feature entitlements in an AI-built SaaS: modelling plans and entitlements, syncing with Stripe or Mollie subscriptions, enforcing limits on the server and in the database, handling upgrades, downgrades and grace periods, and designing upgrade prompts that convert instead of frustrate.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-07",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/plan-limits-and-entitlements-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Stripe: Entitlements", "url": "https://docs.stripe.com/billing/entitlements" },
    { "@type": "CreativeWork", "name": "Stripe: Subscription webhooks", "url": "https://docs.stripe.com/billing/subscriptions/webhooks" },
    { "@type": "CreativeWork", "name": "Supabase Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" }
  ]
}
</script>

A pricing page is a promise in two directions. Customers on the Starter plan are promised certain features and limits. Customers on the Pro plan pay more because they get more. If the product does not enforce the difference, the pricing page is fiction: Starter customers use Pro features, free users create unlimited projects, and nobody has a reason to upgrade.

AI-built apps very often enforce plans only in the interface. The "Export to PDF" button is hidden for Starter users, but the export endpoint works for anyone who calls it. The project limit is checked in a React component before showing the "New project" button, but the database accepts any number of projects. A determined user, or a curious one with the browser's developer tools, can bypass both in minutes.

This guide explains how to model, enforce and communicate plan limits properly.

## Key Takeaways

- **Plans and entitlements are different things.** A plan is what the customer buys; entitlements are the specific features and limits it grants.
- **Store entitlements in your database,** synced from your payment provider, so every part of the app checks the same source of truth.
- **Enforce limits on the server and in the database,** not only in the interface. Hiding a button is a design choice, not a control.
- **Define behaviour for every subscription state:** trialing, active, past due, cancelled and paused.
- **Upgrade prompts should appear at the moment of need,** with clear value, not as surprise errors.

## Plans vs Entitlements

| Concept | Example | Changes how often |
| --- | --- | --- |
| Plan | Starter, Pro, Business | When pricing changes |
| Entitlement | `projects_max = 5`, `pdf_export = true`, `seats_max = 3`, `ai_credits_monthly = 200` | When plan definitions change |
| Subscription | Customer X is on Pro, monthly, active until a date | When the customer changes plan or pays |
| Usage | Customer X has 4 projects and used 120 AI credits this month | Constantly |

Separating these concepts makes the system flexible. You can grant a custom entitlement to one enterprise customer, run a promotion that temporarily raises limits, or rename plans without rewriting feature checks. The code asks "is this account entitled to PDF export?" rather than "is this account on Pro?"

Stripe offers an entitlements feature that associates features with products and exposes active entitlements per customer. You can use it directly or mirror entitlements into your own database, which is usually practical because your app needs to check them on almost every request.

## A Simple Data Model

A typical model in Supabase:

- **`plans`:** plan identifiers and display information
- **`plan_entitlements`:** for each plan, the features and limits it includes
- **`subscriptions`:** for each account, the current plan, status, period end and payment provider IDs
- **`account_entitlement_overrides`:** optional custom grants for specific accounts
- **`usage_counters`:** current usage for limits that reset periodically, such as monthly AI credits

A database view or function then computes the effective entitlements for each account: plan entitlements plus overrides, adjusted for subscription status.

## Syncing With Stripe or Mollie

Your payment provider is the source of truth for billing; your database is the source of truth for what the app allows. Keep them in sync through webhooks:

- **Subscription created or updated:** update plan, status and period in your database.
- **Payment succeeded:** confirm active status for the new period.
- **Payment failed:** mark as past due and start the grace period logic.
- **Subscription cancelled:** schedule or apply the downgrade.
- **Trial ending:** prepare notifications and conversion prompts.

Webhooks must be verified and processed idempotently, as with all payment events. Never update entitlements based on a redirect back from the checkout page alone; the customer may close the browser, and the redirect proves nothing about payment.

## Where to Enforce Limits

Enforcement belongs in layers:

| Layer | Purpose | Example |
| --- | --- | --- |
| Interface | Guide users and show upgrade prompts | Show "Upgrade to export PDFs" instead of the export button |
| Server functions and API | Enforce feature access | Export function checks the PDF export entitlement before running |
| Database | Enforce hard limits atomically | Insert policy or trigger prevents more projects than allowed |

**Feature entitlements** are typically checked in server functions: before generating a PDF, calling an AI model or running an integration, the function checks whether the account is entitled. If not, it returns a clear error that the interface turns into an upgrade prompt.

**Quantity limits,** such as maximum projects, seats or storage, are best enforced in the database, because they are vulnerable to race conditions. Two simultaneous requests can each see four projects and both create a fifth. A database function that locks the account row, counts and inserts within a transaction, or a trigger that rejects inserts beyond the limit, makes the limit reliable.

Row Level Security can also reference entitlements, for example allowing access to an advanced reports table only for entitled accounts. Keep such policies efficient, as described in our guide on [Row Level Security performance in Supabase](https://launchstudio.eu/en/blog/row-level-security-performance-in-supabase).

## Subscription States

Each state needs a defined behaviour:

| State | Typical behaviour |
| --- | --- |
| Trialing | Full or trial-specific entitlements, with clear trial end date |
| Active | Plan entitlements |
| Past due | Grace period with full access and payment reminders, then reduced access |
| Cancelled, period not ended | Access until period end, with reactivation option |
| Cancelled, period ended | Downgrade to free plan or read-only access |
| Paused | Read-only or limited access, data preserved |

Grace periods matter. A failed card payment is often an expired card, not an intent to stop paying. Cutting access immediately frustrates good customers. A few days of continued access with clear reminders, combined with your payment provider's retry logic, recovers many failed payments.

## Downgrades and Over-Limit Accounts

When a customer downgrades from a plan allowing 20 projects to one allowing 5, what happens to the other 15? Options:

- **Keep data, block creation:** existing projects remain accessible, but no new ones can be created until under the limit.
- **Read-only beyond the limit:** the customer chooses which 5 remain active; others become read-only.
- **Archive with restore:** extra items are archived and restored on upgrade.

Never delete customer data automatically because of a downgrade. Communicate clearly before the downgrade takes effect what will change.

## Seats and Team Limits

For B2B products, seats are a common limit. Enforce them when:

- Inviting a new member
- Accepting an invitation, in case several invitations were sent before the limit was reached
- Reactivating a deactivated member

Show admins how many seats are used and available, and make it easy to buy additional seats. Our guide on [adding teams and invites to your SaaS](https://launchstudio.eu/en/blog/how-do-i-add-teams-and-invites-to-my-saas) covers team structures.

## Designing Upgrade Prompts

Limits are also a sales tool. Good upgrade prompts:

- **Appear at the moment of need,** when the user tries to use the feature, not as constant banners.
- **Explain the value,** such as "Export reports as PDF to share with clients", rather than "This feature is not available".
- **Show the path,** with a direct link to upgrade, ideally preselecting the right plan.
- **Respect the user's work,** for example saving a draft before showing the prompt.
- **Allow admins to act,** and tell non-admin users who can upgrade.

Track how often prompts appear and convert. If a limit is hit constantly by happy customers who never upgrade, it may be set too low or the higher plan may be priced wrongly.

## Enterprise Deals and Custom Entitlements

As you sell to larger customers, plans stop fitting perfectly. An enterprise customer may need 150 seats, a higher API limit, single sign-on and a feature that is normally only in the top plan, at a negotiated price. If entitlements are hard-coded per plan, every such deal becomes a code change.

With an override table, it becomes data:

- **Grant specific entitlements** to one account, such as `sso = true` or `seats_max = 150`.
- **Set an expiry date** for trial extensions or promotional limits.
- **Record who granted the override and why,** for auditability.
- **Show overrides in your admin interface,** so support and sales see exactly what a customer has.

Contracts and invoices for enterprise deals often run outside self-service checkout, through invoices or annual agreements. Your subscriptions table should support that too, with a status set by your team rather than only by payment webhooks.

## Communicating Limits Before Customers Hit Them

Limits feel fair when they are visible and predictable. A usage panel in settings, showing for example "4 of 5 projects" and "120 of 200 AI credits this month", lets customers plan. Notifications at sensible thresholds, such as 80% of a monthly quota, give them time to upgrade before work is blocked. Customers who see a limit coming are far more likely to upgrade than customers who discover it mid-task.

## Testing Entitlements

Test each plan and state with dedicated test accounts:

- Attempt every restricted feature from the interface and directly through the API.
- Attempt to exceed each limit, including with concurrent requests.
- Simulate webhook events for upgrades, downgrades, failed payments and cancellations.
- Verify that overrides for custom customers work and expire as intended.

Automated tests for entitlements prevent regressions when AI tools add new features and forget to add checks.

## How LaunchStudio Helps

LaunchStudio implements plan limits and entitlements in AI-built SaaS: modelling plans, entitlements, subscriptions and usage in the database, syncing them with Stripe or Mollie through verified webhooks, enforcing feature access in server functions and quantity limits atomically in the database, defining subscription state behaviour with grace periods, building upgrade prompts and adding automated entitlement tests.

These implementations typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which also includes payments, managed hosting, monitoring and priority support. Smaller fixes, such as adding server-side checks to existing features, can fit within **Launch Ready** (€800-€3,500). Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including subscription and licensing systems for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Survey Tool Where Free Users Had Pro Features

Arjen Dijkstra built Enquetewerk with Lovable, Supabase and Stripe: a survey tool for schools and associations, with a free plan for up to three surveys and 100 responses, and paid plans with unlimited surveys, branding, exports and AI summaries of open answers. Revenue grew more slowly than usage, and Arjen noticed that some free accounts had dozens of surveys.

The cause was enforcement in the interface only. The "New survey" button was hidden after three surveys, but the database accepted unlimited inserts, and some users had found that duplicating a survey bypassed the check entirely. Export and AI summary buttons were hidden for free users, but the corresponding edge functions did not check plans, and AI summaries ran for everyone who called them. The plan was stored as a text field updated by the checkout success page, so a few customers who closed the browser after paying stayed on the free plan, while some who cancelled kept Pro features indefinitely.

LaunchStudio introduced a model of plans, entitlements, subscriptions and usage counters in Supabase, kept in sync by verified, idempotent Stripe webhooks. Survey creation and duplication moved into a database function that enforced limits atomically, and response limits were enforced by an insert check on responses. Every edge function for exports, branding and AI summaries checked entitlements before running, past-due subscriptions received a seven-day grace period, and downgrades kept existing surveys readable while blocking new ones above the limit. Upgrade prompts appeared at the moment users tried a paid feature, with a direct link to the right plan.

**Result:** In the two months after the change, conversions from free to paid plans roughly doubled, AI costs from free accounts fell to almost zero and no paying customer lost access because of a closed browser. Entitlement tests now run on every deployment.

> *"My pricing page said one thing and my database did another. Making the product keep the pricing page's promises was the best growth project I did that year."*
> - **Arjen Dijkstra, Founder, Enquetewerk (Leeuwarden)**

**Cost & Timeline:** €4,300 (Launch & Grow package: entitlement model, Stripe webhook sync, server and database enforcement, grace periods, upgrade prompts and tests) - completed in 11 business days.

## Frequently Asked Questions

### Is hiding features in the interface enough to enforce plans?

No. Hiding features guides users, but anyone can call your API or database directly. Feature access must be checked in server functions, and quantity limits enforced in the database, so plans cannot be bypassed.

### Where should I store a customer's plan?

In your database, in a subscriptions table synced from your payment provider through verified webhooks, with entitlements derived from the plan. Avoid setting the plan from the checkout success page, which is not proof of payment.

### What should happen when a customer's payment fails?

Usually a grace period of several days with continued access and reminders, while the payment provider retries. If payment still fails, reduce access according to defined rules, such as read-only mode, without deleting data.

### How does Manifera's experience help with subscription systems?

Manifera has built licensing and subscription systems for enterprise clients for 11+ years. LaunchStudio applies that experience to model entitlements cleanly and enforce them reliably, so pricing works as intended and customers are treated fairly.

### Do clear plan limits help with buyers and visibility?

Yes. Clear, consistent plan descriptions on your pricing page help buyers choose and reduce support questions. Structured pricing information is also something search engines and AI answer engines surface when buyers compare tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is hiding features in the interface enough to enforce plans?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Check feature access in server functions and enforce quantity limits in the database." }
    },
    {
      "@type": "Question",
      "name": "Where should I store a customer's plan?",
      "acceptedAnswer": { "@type": "Answer", "text": "In a database subscriptions table synced via verified webhooks, with entitlements derived from the plan, not from the checkout success page." }
    },
    {
      "@type": "Question",
      "name": "What should happen when a customer's payment fails?",
      "acceptedAnswer": { "@type": "Answer", "text": "A grace period with access and reminders while payments retry, then reduced access without deleting data." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with subscription systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise licensing systems for 11+ years, and LaunchStudio models and enforces entitlements reliably." }
    },
    {
      "@type": "Question",
      "name": "Do clear plan limits help with buyers and visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Clear pricing helps buyers and is structured information search and AI engines surface." }
    }
  ]
}
</script>
