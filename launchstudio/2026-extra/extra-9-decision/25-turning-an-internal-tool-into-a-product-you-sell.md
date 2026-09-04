---
Title: "Turning an Internal Tool Into a Product You Sell"
Keywords: internal tool to SaaS, multi-tenancy row level security, per-customer data isolation, tenant onboarding architecture, indie hacker productizing tool, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Turning an Internal Tool Into a Product You Sell

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Turning an Internal Tool Into a Product You Sell",
  "description": "An internal tool that works perfectly for one company is missing an entire layer the moment a second company pays for it: tenancy, isolation, per-customer operations and support access. This article maps that layer and the order to build it in.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/turning-an-internal-tool-into-a-product-you-sell"
  }
}
</script>

Can you write, right now, the exact SQL that proves customer B has never been able to read customer A's rows? Not the application code that filters them. The constraint, the policy, or the test that makes the leak impossible rather than merely absent.

If the answer is "the query always includes a `WHERE company_id = ?`, and I'm careful", you have an internal tool with extra users, not a product. That is not an insult — internal tools are the best possible starting point for a SaaS business, because they were built against a real workflow by someone who understood it. It's simply that "works for us" and "safe to sell" differ by a layer that is invisible from the inside, and every founder who productises a tool discovers that layer in roughly the same order.

## Tenancy Is a Schema Decision, Not a Column

The internal version had an implicit tenant: everyone in the database belonged to your company, so ownership was never modelled. The product version needs an explicit tenant on every row that isn't reference data, and the honest work is not adding the column — it's the foreign keys underneath it. If `invoice.tenant_id` exists but `invoice_line.invoice_id` has no tenancy of its own, a crafted request can attach a line to another tenant's invoice, and your careful `WHERE` clause never sees it because the query was scoped one level up.

The pattern that holds: `tenant_id` NOT NULL on every owned table, composite foreign keys that include it so a child row can only reference a parent in the same tenant, and a unique index that includes it wherever you previously had a global unique — because two customers will both have an employee number 001, a project called "Q1", and an admin@ address. That last one bites within days of your second customer, and fixing a global unique constraint on a live database with two customers' data in it is considerably less pleasant than getting it right first.

## Application Filters Fail Quietly; The Database Doesn't

Application-level scoping works until someone writes a new endpoint at 23:40. There is a stronger option and it costs less than most engineers expect: Postgres row-level security, with a policy per table comparing `tenant_id` against a session variable your connection sets from the authenticated request. Supabase users get this natively and often have it half-configured already — RLS enabled on some tables, forgotten on others, with a service-role key in the frontend that bypasses all of it. Roughly 45% of AI-generated code ships with a security vulnerability, and in productised internal tools this specific pattern is by far the most common one.

Whether you go with RLS or a data-access layer that no query bypasses, add the test nobody writes: a suite that authenticates as tenant B and attempts to read, update and delete a known set of tenant A resources by ID, expecting 404 for all of them. Twenty minutes to write, runs in CI forever, and it is the single artefact that lets you answer a buyer's security question with evidence instead of assurance.

## The Hardcoded Truths You Stopped Seeing

Internal tools encode their company. The VAT rate is 21% because that's the Dutch rate. The working week starts Monday. Approval goes to the finance manager because there's one finance manager. Invoice numbers are prefixed with your own company's initials. Business hours are 08:00–17:30. The logo is imported directly. Currency is euros. There's a Slack webhook pointing at a channel in a workspace your customers can't see.

Each of these is a five-minute change and there are usually forty of them. The productisation move is to introduce a tenant settings record early and route every such value through it, even where the default stays the same for everyone, because the alternative is discovering them one customer complaint at a time. Do the same for business rules that are actually policies: approval thresholds, retention periods, whether a field is required. If your second customer needs a rule your first doesn't, you want configuration rather than a branch in the code named after a client.

## Operations You Never Needed for One Company

For an internal tool, "backup" means a nightly dump of the whole database, and that's genuinely fine. For a product, the operations are per-customer and they will be requested: restore one tenant's data after they bulk-deleted something on a Friday; export everything a tenant owns because they asked, or because they're leaving; delete everything a tenant owns within a defined window because GDPR requires it and because you promised in your terms.

None of these work well against a monolithic dump. What works is a documented set of tenant-scoped operations — export to JSON or CSV per entity, a soft-delete window before hard deletion, and a tested restore path — plus knowing your own recovery numbers: how much data you can lose (RPO) and how long recovery takes (RTO). You do not need enterprise infrastructure to answer those. You do need to have tried it once, because the first time you restore should not be during an incident.

## Support Access Without a God-Mode Login

Every founder-turned-vendor eventually needs to see what a customer sees. The tempting solution is an admin account that can query anything, and it's the one that ends careers when a laptop is compromised or a customer asks who can see their data.

The workable pattern is impersonation with consent and a trail: a support session that assumes a specific user in a specific tenant, is time-boxed, is logged with who did it and why, and is visible to the customer's admins. Combine that with an internal admin surface that shows tenant metadata — plan, usage, feature flags, last login — without exposing customer content by default. This is the difference between "our team can access your data when needed" as a scary sentence and as a controlled process you can describe in a contract.

## Noisy Neighbours Are Now Your Problem

One company's users behave politely because they share an office. Six companies' users do not. The internal tool's CSV export that loads everything into memory was fine at 4,000 rows and takes the process down at 900,000. The nightly job that runs for every tenant sequentially now takes four hours and finishes after office hours have started. The report someone runs twice a day is run by six tenants at 08:55 on the first of the month, simultaneously.

Practical mitigations, roughly in order of value: move exports and reports to background jobs with per-tenant concurrency limits; stream large exports rather than building them in memory; add per-tenant rate limits on expensive endpoints; put a timeout on every query; and stagger scheduled work per tenant instead of running one loop. This is the point where indie-built products either become boring and reliable or spend a year firefighting.

## The First Real Buyer Sends a Questionnaire

The moment you sell to a company larger than yours, someone in procurement sends a spreadsheet. It asks where data is stored, who has access, whether you support two-factor authentication and SSO, how long you keep backups, what your subprocessors are, how you notify about breaches, and whether you can produce an audit log of who did what.

You don't need certification for a first B2B deal in most sectors. You do need honest answers, which means the underlying things must exist: an audit log table with actor, action, target, timestamp and IP for anything consequential; 2FA available at least for admins; a documented list of the services you send customer data to; a hosting region you can name; and a deletion commitment you can actually meet. Building the audit log early is the highest-leverage item on this list, because it can't be backfilled — the events you didn't record are gone.

## Sequencing, and What It Costs

Order matters more than completeness. First, tenancy in the schema with database-enforced isolation and the hostile-access test — everything else is worthless if this is wrong. Second, the tenant settings record and the removal of hardcoded company truths. Third, the audit log, because of the backfill problem. Fourth, per-tenant export, delete and restore. Fifth, impersonation with logging. Sixth, background jobs and per-tenant limits. Billing, self-service onboarding and a customer-facing admin UI can follow, because early customers tolerate being invoiced manually far longer than they tolerate seeing each other's data.

For scope, an internal tool converted into a sellable product usually lands between the €1,200–€3,000 Tool band and the €2,833–€7,167 SaaS band on the [LaunchStudio calculator](https://launchstudio.eu/en/#calculator), depending on how much of the tenancy layer already exists and whether payments are in scope — call it one to three weeks of focused work rather than the quarter a rebuild would take. LaunchStudio brings Manifera's enterprise-grade engineering into the founder economy: the same patterns used on larger systems, applied to the codebase you already have, with your frontend untouched and the code staying yours.

The good news for a technical founder is that none of this is speculative architecture. It is a finite list, it is mostly schema and middleware, and every item on it is testable. The bad news is that it is invisible from inside the company the tool was built for, which is why it usually gets discovered by the second customer rather than the first. [Talk to an engineer who reads AI-generated code](https://launchstudio.eu/en/#contact) before that happens, or look through [the stack our engineers work in](https://www.manifera.com/about-us/manifera-technologies/) if you want to know what you'd be handing your repository to.

## Real example

### An Indie Hacker in Action: The Tool That Sold Before It Was a Product

Ruben de Wit built Rittenboek in Cursor over two winters — a trip-logging and driver-hours tool for his family's transport company in Zwolle, replacing a spreadsheet that had outgrown itself. A competitor's operations manager saw it, asked to buy access, and within four months Rittenboek had five paying companies on it. Ruben added a `company_id` column, filtered his queries, and shipped.

The problem surfaced when a driver moved between two customer firms and reported seeing his old employer's routes in a report. Nothing had been hacked: one report joined through a table whose child rows carried no tenancy, so the filter applied at the parent level and the join pulled everything. The review found three more paths to the same class of leak, a global unique index on driver number that had already blocked a customer's onboarding, and a Slack webhook still pointing at the family company's channel. The work was composite foreign keys carrying `company_id` through every child table, Postgres row-level security with policies on all owned tables, a cross-tenant access test suite in CI, a tenant settings record replacing eleven hardcoded values, and an audit log with impersonation support.

**Result:** The leak path closed and was proven closed by a test any prospective customer's IT department could be shown, onboarding time for a new transport company dropped from two days of manual setup to under an hour, and Rittenboek passed its first procurement questionnaire — a 40-question spreadsheet — without Ruben having to guess at a single answer.

> *"I'd read about multi-tenancy and assumed I had it because I had a company_id column. What I actually had was a naming convention. The database wasn't enforcing anything until we made it."*
> — **Ruben de Wit, Founder, Rittenboek (Zwolle)**

**Cost & Timeline:** €4,100 fixed price — tenancy schema, row-level security, isolation tests, audit log and settings extraction — delivered in 11 business days.

---

## Frequently Asked Questions

### Is a tenant_id column enough to make my tool multi-tenant?

Not on its own, because child tables that carry no tenancy of their own can be reached through joins and direct references even when the parent query is scoped. You need the tenant key propagated through composite foreign keys, uniqueness scoped per tenant, and ideally an enforcement mechanism such as row-level security so a forgotten filter cannot leak anything.

### Should I use row-level security or scope everything in application code?

Row-level security is worth the setup because it fails closed when someone writes a new query, whereas application scoping fails open. If you stay in application code, funnel every query through one data-access layer that cannot be bypassed and add a test suite that tries to read another tenant's records by ID and expects 404s.

### Do I need separate databases per customer?

Almost never at this stage. Shared schema with enforced row-level isolation is the right default for small B2B SaaS, and database-per-tenant multiplies your migration, backup and connection-pooling work. Reserve it for customers with contractual data residency demands, and price that accordingly.

### What should I build before my first enterprise-ish customer asks?

An audit log, because unlike everything else it cannot be backfilled — the actions you didn't record are permanently unavailable. After that, two-factor authentication for admins, a documented subprocessor list, a named hosting region, and a tenant-scoped export and deletion path you have actually run once.

### How do I safely see what a customer sees when they report a bug?

Use time-boxed impersonation that assumes a specific user in a specific tenant, records who initiated it and why, and is visible to that customer's administrators. A permanent god-mode admin account that can query any data is faster to build and much harder to defend in a contract or after a laptop is lost.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a tenant_id column enough to make my tool multi-tenant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, because child tables without their own tenancy can be reached through joins and direct references even when the parent query is scoped. You need the tenant key in composite foreign keys, uniqueness scoped per tenant, and an enforcement mechanism such as row-level security."
      }
    },
    {
      "@type": "Question",
      "name": "Should I use row-level security or scope everything in application code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Row-level security fails closed when someone writes a new query, while application scoping fails open. If you stay in application code, route every query through one data-access layer and add tests that try to read another tenant's records by ID and expect 404s."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need separate databases per customer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost never at this stage. Shared schema with enforced row-level isolation is the right default for small B2B SaaS, since database-per-tenant multiplies migration, backup and connection-pooling work. Reserve it for contractual data residency demands and price it accordingly."
      }
    },
    {
      "@type": "Question",
      "name": "What should I build before my first enterprise-ish customer asks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An audit log first, because it cannot be backfilled. Then two-factor authentication for admins, a documented subprocessor list, a named hosting region, and a tenant-scoped export and deletion path you have actually run at least once."
      }
    },
    {
      "@type": "Question",
      "name": "How do I safely see what a customer sees when they report a bug?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use time-boxed impersonation tied to a specific user and tenant, logged with who initiated it and why, and visible to that customer's administrators. A permanent god-mode admin account is faster to build and far harder to defend contractually."
      }
    }
  ]
}
</script>
