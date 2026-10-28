---
Title: "Vendor Lock-In: An Exit Plan for Every Service Your App Uses"
Keywords: vendor lock-in, exit plan, business continuity, service dependencies, Supabase export, email failover, AI provider switching, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Vendor Lock-In: An Exit Plan for Every Service Your App Uses

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vendor Lock-In: An Exit Plan for Every Service Your App Uses",
  "description": "An AI-built product typically depends on ten to twenty external services, and any of them can raise prices, suspend your account, change terms or disappear. How to inventory every dependency, understand the kind of lock-in each creates, write a short exit plan per service, and make the few switches that matter fast.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/vendor-lock-in-an-exit-plan-for-every-service-your-app-uses" }
}
</script>

Building with Lovable, Bolt or Replit means building on other people's services from the first day. The builder itself, the hosting, the database and authentication, file storage, transactional email, payments, an AI model, analytics, error tracking, the domain registrar. A typical AI-built B2B product depends on ten to twenty external services - and the founder usually chose most of them by accepting a default.

That is not a mistake. Using managed services is what makes a small team able to run a serious product. But every one of those services can change in ways you do not control: a price increase, a suspended account because of an automated abuse check, changed terms, an acquisition, a discontinued feature, a regional outage, a company that simply stops. When it happens, the question is not whether you depend on the service, but how long it would take to stop depending on it.

Avoiding all lock-in is neither possible nor desirable. What is possible is knowing, for each dependency, what you would do if you had to leave - and making the handful of preparations that turn a crisis into a few days of work. This article covers how to build the inventory, the kinds of lock-in, what an exit plan contains, the services that deserve the most preparation, and the questions customers will ask about it.

## Start With an Inventory

Most founders cannot list every service their product depends on. The list is in billing emails, in environment variables, in DNS records and in the code, and nobody has assembled it.

Build it once, as a table, with a row per service:

- **What it does** and which features depend on it.
- **Who holds the account** - the company or a person, and which login.
- **What data it holds** - customer data, your code, configuration, nothing.
- **Monthly cost** and contract terms - notice periods, price change clauses.
- **Region** where it processes data.
- **Kind of lock-in** - described below.
- **Exit plan** - a link to a short document.
- **Last reviewed.**

Sources to check: your environment variables and secrets, the dependency list in your code, DNS records, your credit card statements, your email inbox for "welcome to" messages, and the subprocessor list if you have one, as the subprocessors article in this series describes. The inventory is also the basis of that subprocessor list, the services list in the handover article, and the answer to a large part of any security questionnaire.

## The Kinds of Lock-In

Different services lock you in in different ways, and the exit effort depends on which.

**Data lock-in.** The service holds data you need, and getting it out is hard or incomplete. A database is the obvious example; less obvious are payment providers holding stored cards and direct debit mandates, and authentication services holding password hashes.

**Code lock-in.** Your code calls the service's proprietary API directly throughout the codebase, so replacing it means rewriting many files.

**Identity lock-in.** Users, customers or integrations are identified by the service's IDs - a payment provider's customer ID used as your primary key, an authentication provider's user ID referenced everywhere.

**Reputation lock-in.** The service holds something that took time to build: an email sending reputation, an app store listing, search engine rankings on a platform domain.

**Operational lock-in.** Knowledge of how the service is configured exists only in its dashboard, or in one person's head.

**Contractual lock-in.** Minimum terms, long notice periods, penalties, or prices that increase sharply after a commitment ends.

A service can create several at once. A payment provider typically creates data, identity and contractual lock-in; a builder tool creates code and operational lock-in until the code lives in your own repository.

## What an Exit Plan Contains

An exit plan is not a migration project. It is a page per significant service, written in advance, answering five questions.

1. **Triggers.** What would make us leave? A price increase above a threshold, repeated outages, a change of ownership, a policy change, a suspended account.
2. **Data.** What do we need to take with us, and how do we get it out? Which export, in what format, how complete, how long it takes.
3. **Alternatives.** Which one or two services could replace it, and what differs.
4. **Effort.** What has to change - code, configuration, DNS, customer communication - with an honest estimate in days.
5. **Preparation.** What we do now so the exit is faster later: regular exports, an abstraction layer, a second configured provider, contract terms.

For most services the plan is half a page. For the few critical ones it is longer, and the preparation is actually done rather than described.

## The Builder Itself

The first dependency of an AI-built product is the tool it was built in. If the code exists only inside Lovable, Bolt or Replit, the product is locked into that tool's availability, pricing and continued existence.

The preparation is simple and should be done immediately: the code synchronised to a Git repository in an account the company owns, as the Git and handover articles in this series describe. With the code in your own repository, the builder becomes a convenient editor rather than the only place your product exists. The Bolt-to-Next.js and Replit-to-AWS articles in this series cover what moving away actually involves if you ever need to.

## Database and Authentication

Supabase is built on Postgres, which is about as portable as databases get. A logical dump restores into any Postgres host. That portability is only real if you use it.

**Make regular exports to storage you control**, outside Supabase - a nightly or weekly `pg_dump` to an object storage bucket at another provider, encrypted, with a tested restore, as the backups article in extra-11 describes. This is both a backup and an exit route.

**Know what is Supabase-specific.** Row level security policies, database functions and triggers are standard Postgres and move with the dump. Edge functions, storage buckets, realtime subscriptions and the auto-generated REST API are Supabase features that need equivalents elsewhere.

**Authentication is portable if you plan for it.** Supabase Auth stores users in the `auth.users` table with bcrypt password hashes, which most authentication systems can import, so users can keep their passwords. Reference users by your own profile ID where practical rather than spreading the authentication provider's ID through every table, and keep the email address as a stable second identifier.

The leaving Supabase article in this series covers a full move; the preparation above makes it a planned project rather than an emergency.

## Transactional Email

Email is the service whose failure is noticed fastest - password resets, invitations, booking confirmations and invoices stop - and whose suspension is most often automatic. A burst of bounces after a customer imports an old address list can trigger a provider's abuse protection and pause sending for the whole account.

Preparation that pays for itself:

- **Sending through your own domain**, with SPF, DKIM and DMARC configured, as the transactional email article in extra-11 describes - so reputation belongs to your domain rather than to the provider.
- **A second provider configured and verified**, with DKIM records for both in DNS, and sending code behind a small interface so switching is a configuration change.
- **Automatic failover** for critical messages - password resets, invitations - when the primary provider returns errors or the account is paused.
- **Bounce handling and list hygiene** so imports of old addresses do not damage reputation in the first place.

## Payments

Payment providers create the most difficult lock-in, because much of what they hold cannot simply be exported.

**Card details** are stored by the provider for PCI compliance. Moving stored cards to another provider is possible through a provider-to-provider transfer under PCI rules, but it takes weeks, requires both providers' cooperation and is not available for every combination.

**SEPA direct debit mandates** are agreements between your customer and your business, but the mandate references and records live at the provider. Moving them requires the mandate data to be exported and accepted by the new provider; plan it rather than assume it.

**Customer, subscription and invoice history** can usually be exported, and should also exist in your own database, as the reconciliation article in this series argues.

Preparation: store payment state in your own tables with the provider's IDs as references rather than primary keys; keep your own invoice records; know the provider's process for data portability before you need it; and read the termination and data return terms. For a product where payments are central, knowing the realistic switching time - often one to three months - is the real exit plan.

## AI Models

AI providers change prices, deprecate models, alter usage policies and have outages more often than most other services. Of all dependencies, they are both the easiest to switch technically and the easiest to switch badly.

**Put model calls behind your own interface** - one module that takes a task and returns a result, with the provider and model as configuration. Calls scattered through the codebase with provider-specific parameters are what make switching slow.

**Keep prompts and structured output schemas provider-neutral** where possible, and store them in the repository.

**Evaluate an alternative before you need it.** The evaluation set described in the AI output evaluation article in this series lets you test a second provider in hours and know exactly where it is better or worse. Without it, switching providers is a gamble on quality.

**Consider a configured fallback** for critical features, used automatically when the primary provider is unavailable.

## Domains, DNS and Accounts

The least technical lock-in is often the most dangerous: access.

A domain registered in a former co-founder's personal account, a DNS provider only one person can log into, a hosting account tied to a personal email address, two-factor authentication on the phone of someone who has left. None of these appears in architecture diagrams; any of them can take the product offline or make it impossible to change.

Move every account to company ownership: registrations in the company's name, logins in a shared password manager the company controls, two-factor authentication on company devices or with recovery codes stored securely, and at least two people able to access each critical service. Renewal reminders should go to a shared address that is read. The handover article in this series describes how this goes wrong when it is left until someone leaves.

## Contracts, Prices and Notice

Technical preparation is half of an exit plan. The other half is knowing what the agreements allow.

For each significant service, record four things from its terms: how much notice it must give before changing prices or terms, how quickly you can leave and whether minimum commitments apply, what happens to your data after termination and for how long you can still export it, and under what conditions the provider may suspend your account. These answers determine how much time an exit plan actually has - a provider that can change prices with thirty days' notice gives you thirty days, whatever your technical readiness.

Two habits help. Read change notifications from critical providers rather than archiving them, and add a line to the inventory when terms change. And when a service becomes significant enough - usually when its cost or its role in the product grows - consider whether a business plan with a contract, a named account manager and defined notice periods is worth more than the price difference. For a supplier your customers depend on indirectly, predictable terms are often the most valuable feature on offer.

## Abstraction Where It Is Cheap, Not Everywhere

A common overreaction to lock-in is to wrap every service in an abstraction "in case we switch". That adds code, hides useful features of the service and is usually wasted: most services you will never leave.

Abstract where switching is likely and the cost is low - email sending, AI model calls, file storage access, payment provider calls - with a thin interface in one module. Do not abstract the database query language, the frontend framework or the authentication flow on speculation. Use the services' strengths, and keep the data you would need in a portable form.

## Concentration and Customers' Questions

Two further considerations apply as the product grows.

**Concentration risk.** If hosting, database, storage, authentication and functions all run on one platform, one platform incident or account suspension affects everything. That is often an acceptable trade for simplicity; it should be a conscious one, with backups held elsewhere.

**Customers will ask.** Procurement questionnaires increasingly include business continuity questions: what happens if a critical supplier fails, where backups are held, how long recovery would take, and sometimes whether source code escrow is available. The inventory and exit plans are the basis for honest answers - and "we export the database nightly to a second provider and have tested a restore" is a better answer than any assurance.

## Review It Once a Year

Exit plans decay as services change. Once a year - or when a service raises prices or changes terms - review the inventory and run a short exercise: pick one critical service and ask, "If this disappeared tomorrow, what would we do in the first hour, the first day and the first week?" Walk through it with whoever would do the work. The gaps that appear are the preparation for the coming year.

## Setting This Up

For a Lovable or Supabase product, this is typically three to five days: an inventory of every external service with its purpose, account owner, data, cost, terms, region and kind of lock-in, a short exit plan per significant service with triggers, data export, alternatives, effort and preparation, code synchronised to a company-owned repository, regular encrypted database exports to storage at another provider with a tested restore, user references designed for portable authentication, transactional email on your own domain with a second verified provider and failover for critical messages, payment state and invoices held in your own database with the provider's portability process documented, AI calls behind a provider-neutral interface with an evaluated alternative, every account and domain moved to company ownership with shared access, thin abstractions only where switching is likely, and an annual review with a tabletop exercise.

LaunchStudio does this as part of making a product something a company can depend on. Behind it is Manifera - eleven years, 160+ projects, 120+ engineers, with continuity planning for clients including Vodafone, TNO and CFLW.

[Ask us which of your services would hurt most to lose](https://launchstudio.eu/en/#contact).

## Real example

### Two Days Without Email

Monique van Dam built Baanreservering in Lovable: court booking, memberships and payments for padel and tennis clubs, used by 70 clubs with around 26,000 members.

One club imported a member list from an old system containing several thousand outdated email addresses. The welcome emails bounced in bulk, and the email provider's automated abuse protection paused sending for Monique's entire account. For two days no club sent anything: no booking confirmations, no password resets, no invitations for new members. There was no second provider, and adding one meant changing DNS records and code under pressure.

Reviewing what else could fail the same way, she found more. The AI provider behind the product's automatic match scheduling had announced a price increase that would roughly triple that cost. The Lovable project was linked to her personal account rather than the company's. And the product's domain was registered in the personal account of a co-founder who had left the company a year earlier.

Four business days: an inventory of 14 external services with owners, data, costs, terms and lock-in type; a one-page exit plan for each, with full preparation for the five critical ones; a second email provider verified on the product's domain with DKIM for both, sending behind a small interface, and automatic failover for confirmations, resets and invitations; bounce handling and validation of imported addresses before sending; AI calls moved behind a provider-neutral module, with an alternative provider evaluated against the scheduling evaluation set; nightly encrypted database exports to object storage at another provider, with a restore tested; the code synchronised to a company-owned Git repository and the Lovable project moved to the company account; the domain transferred to the company with the former co-founder's cooperation, and every critical login moved to a shared company password manager with two people per service; and an annual review in the calendar.

**Result:** five months later the primary email provider had a regional outage; failover switched critical messages to the second provider within minutes and clubs noticed nothing. The AI switch, tested in advance, was made in two days and reduced that cost by about 40% compared with the original price. When a club group asked about business continuity during a procurement process, the exit plans answered every question.

> *"One club's old mailing list paused our email for every club for two days. Looking further, I found that I did not even own our domain - someone who had left the company did."*
> - **Monique van Dam, Founder, Baanreservering (Eindhoven)**

**Cost & Timeline:** €3,800 (service inventory, exit plans for 14 services, secondary email provider with failover and bounce handling, provider-neutral AI module with evaluated alternative, off-platform database exports with tested restore, repository and account ownership, domain transfer, shared access, annual review) - completed in 4 business days.

## Frequently Asked Questions

### What is vendor lock-in for an AI-built product?

Depending on a service in a way that makes leaving slow or costly - through the data it holds, the code that calls it, the IDs your system uses, the reputation it holds, contract terms, or access tied to one person.

### Do I need an exit plan for every service?

A short one for every significant service, and real preparation for the few critical ones - usually the code repository, database, email, payments, AI provider and domain.

### How do I make my Supabase data portable?

Make regular encrypted Postgres exports to storage at another provider, test a restore, know which features are Supabase-specific, and reference users in a way that allows authentication to move with password hashes intact.

### Should I wrap every service in an abstraction layer?

No. Abstract only where switching is likely and cheap - email, AI calls, file storage, payment calls. Elsewhere, use the service fully and keep your data portable.

### What do customers ask about vendor dependencies?

How critical supplier failures are handled, where backups are held, how long recovery takes, and sometimes source code escrow. An inventory and tested exit plans give honest answers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is vendor lock-in for an AI-built SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dependence on a service through data, code, identifiers, reputation, contracts or access that makes leaving slow or costly."
      }
    },
    {
      "@type": "Question",
      "name": "Does every service need an exit plan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A short one for each significant service, with real preparation for critical ones such as code, database, email, payments, AI and domain."
      }
    },
    {
      "@type": "Question",
      "name": "How can Supabase data be kept portable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Regular encrypted Postgres exports to another provider with tested restores, awareness of Supabase-specific features, and portable user references."
      }
    },
    {
      "@type": "Question",
      "name": "Should every external service be abstracted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No - only where switching is likely and cheap, such as email, AI calls, storage and payment calls."
      }
    },
    {
      "@type": "Question",
      "name": "What continuity questions do B2B customers ask?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "How supplier failures are handled, where backups live, recovery times, and sometimes source code escrow."
      }
    }
  ]
}
</script>
