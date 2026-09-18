---
Title: "Lovable Supabase: Multi-Tenancy Without Leaking Data"
Keywords: lovable supabase, multi-tenancy, supabase security, tenant isolation, ai app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable Supabase: Multi-Tenancy Without Leaking Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Multi-Tenancy Without Leaking Data",
  "description": "The moment your customers are companies rather than individuals, every table needs a tenant. How isolation is actually enforced, where it leaks, and why retrofitting it costs ten times what building it costs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-multi-tenancy-without-leaking-data" }
}
</script>

A single question separates a personal tool from a business product: is a customer one person, or a company with several people in it?

Almost every founder answers "one person" at the beginning, because that is what they built and it is what the first users were. And almost every founder selling to Dutch businesses hears the same request within six months — "can my colleague have access too?" — at which point the answer determines whether the next step is an afternoon or a fortnight.

Multi-tenancy is the architecture that makes that answer easy. It is also the architecture where a mistake does not produce a bug but a breach, because the thing that leaks is one customer's data into another customer's screen.

## What a Tenant Is, Concretely

A tenant is the boundary of who may see what. For most products it is an organisation: a company, a practice, a club, a department.

Three things follow, and all three are frequently missing from AI-built products.

**Every row of business data belongs to a tenant.** Not to a user — to the organisation. A record created by an employee who later leaves must remain with the company.

**Every person belongs to one or more tenants, with a role in each.** A bookkeeper working for three clients is one account with three memberships, not three accounts.

**Every query is scoped by tenant,** and that scoping is enforced in the database rather than remembered by whoever writes the query.

The generated default — a row belongs to the user who created it — satisfies none of these, and it is the single most expensive assumption in AI-built business software.

## The Three Ways to Separate Customers

**A database per customer.** Strong isolation, and operationally heavy: every schema change must be applied everywhere, and reporting across customers becomes a project. Justified when a customer contractually requires it, rarely otherwise.

**A schema per customer.** A middle position with most of the same migration burden.

**A shared schema with a tenant column on every table,** enforced by row level security. This is the standard approach, the one Supabase is designed around, and the right default for almost every product. Everything below assumes it.

Choose the third unless a specific customer requirement forces otherwise. Founders who choose the first for a feeling of safety usually discover the real risk was never the database boundary — it was the query that forgot a filter, and that risk exists in all three models.

## Where Tenancy Actually Leaks

Five places, in the order we find them.

**A table without a tenant column.** Usually one added later for a feature: attachments, comments, notifications, a settings table. The main tables are scoped and the newcomer is not.

**A policy that checks the user instead of the organisation.** Works perfectly until two colleagues share a company, at which point one cannot see the other's records — which gets reported as a bug and fixed by loosening the policy.

**Server-side code using the privileged key.** Policies do not apply there. Every query written with that key must filter by tenant in the code, and any one that forgets is a cross-customer leak with no database-level safety net. This is why privileged code should be small, reviewed, and rare.

**Aggregates and reports.** A count, a total, a dashboard figure computed without a tenant filter reveals other customers' data in summarised form. Less obvious and equally reportable.

**Shared resources outside the database.** Uploaded files in a bucket organised by date rather than tenant. Search indexes containing every customer's content. Caches keyed by record identifier with no tenant in the key — which can serve one customer's data to another and is maddening to reproduce.

## Invitations, Roles and the Joining Problem

Once customers are companies, the product needs the mechanics of a company.

Inviting a colleague, by email, with a role. Accepting an invitation, including when the person already has an account under a different organisation. Changing someone's role. Removing someone, and deciding what happens to the records they created — which must stay with the organisation. Transferring ownership when the person who signed up leaves the company, a situation that arrives more often than founders expect and is deeply awkward without a designed path.

None of this is difficult. All of it is invisible until the first customer with two employees, and it is far cheaper to build alongside tenancy than bolted on afterwards.

## Retrofitting: What It Actually Costs

Adding tenancy to a product that already has customers is one of the more expensive changes in software, and the cost is mostly data rather than code.

The steps: add the organisation structure; decide, for every existing row, which tenant it belongs to — which is the part that requires human judgement and customer conversations; backfill; make the column required once it is populated; rewrite every policy; audit every privileged query; move files into tenant-scoped storage; and rebuild any cache or index keyed without a tenant.

For a product with a handful of customers this is a week. For one with a few hundred it is considerably more, and it must be done while the product stays running. Which is why the useful sentence is: if there is any chance your customers will be companies, build the organisation model before you have customers, not after.

## Proving Isolation to a Buyer

Dutch business customers with a procurement process will ask how their data is separated from other customers'. A good answer has three parts: the mechanism (a tenant on every row, enforced by database policies rather than application code), the verification (a documented test attempting cross-tenant access from a second account), and the exceptions (the small set of privileged operations, what they are, and who can run them).

Founders who can say that plainly close deals that founders who cannot do not. It is a five-sentence answer built on a week of work, and it is worth more in a sales conversation than any feature.

## The Cross-Tenant Features You Will Eventually Want

Strict isolation is the right default, and within a year you will want four things that deliberately cross it. Designing them as exceptions is fine; discovering them as accidents is not.

**Benchmarks and industry figures.** "Your average response time is faster than 70% of comparable firms" is a genuinely valuable feature and it computes across tenants. The rule that makes it safe: aggregates only, a minimum number of contributing tenants before a figure is shown, no possibility of deriving an individual customer's value, and an explicit statement in your terms that anonymised aggregates are produced. A benchmark computed over three customers is not a benchmark; it is a disclosure.

**Shared templates and reference data.** Document templates, standard checklists, product catalogues, postcode tables. These belong to nobody and should live in tables marked as global, readable by all tenants and writable only by you — a deliberate third category alongside tenant data and system data.

**Consultants and partners working across customers.** A bookkeeper serving twelve clients, an accountant, a franchise head office overseeing branches. The wrong solution is a special account that bypasses tenancy. The right one is multiple memberships: one person, twelve memberships, each with a role, each revocable by the client. Build it as membership and the awkward cases stop being awkward.

**Your own support access.** Covered by impersonation rules — recorded, visible, read-only by default — and it is the one exception that customers accept readily when it is documented and refuse when it is discovered.

The common thread is that each exception should be an explicit, named mechanism with its own rules, not a gap in the enforcement. A product where cross-tenant access exists only through four documented paths can describe them to a procurement reviewer in a paragraph. A product where it exists because some queries forgot a filter cannot describe it at all, which is the answer that ends evaluations.

## Building Tenancy Properly

Whether you are designing it now or retrofitting, LaunchStudio treats it as a defined piece of work: the organisation and membership model with roles, a tenant column on every table with policies enforcing it per operation, invitations and ownership transfer built as real flows, privileged queries inventoried and each one verified to filter by tenant, files and caches scoped by tenant, aggregates checked, and the isolation tested from accounts in different organisations plus an unauthenticated client — with a written description of the model you can send to a customer's security reviewer.

The engineers are Manifera's: eleven years of building multi-tenant systems for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Tell us who your customers are](https://launchstudio.eu/en/#contact) and you will get a direct assessment of what your model costs to fix now versus later, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Dashboard Total That Included Everyone

Pieter Blom built Huurbeheer with Lovable: property management software used by nine letting agencies across Dordrecht, Zwijndrecht and Sliedrecht, covering roughly 2,300 rental units.

Records belonged to the user who created them, which had worked while each agency was one person. As agencies added colleagues, the pattern that emerged was workaround rather than architecture: several agencies shared a single login between three or four staff, because that was the only way for colleagues to see each other's properties.

The leak was not in the property list, which was correctly filtered. It was on the dashboard. The figure labelled "total units under management" had been added in a later session and counted every row in the table. One agency, seeing a number far larger than its own portfolio, worked out what it meant and asked whether their tenants' details were similarly visible.

They were not — but the arrears total and the average rent figure beside it were also unfiltered, which meant every agency could see the portfolio size and rent levels of its local competitors.

Twelve business days of work: an organisation and membership model introduced with roles for agent, manager and owner; a tenant column added to all nineteen tables, backfilled by working through ownership with each agency individually, then made required; policies rewritten per table and per operation against membership rather than creator; every dashboard figure and report rewritten with an explicit tenant filter and each one tested; eleven privileged server-side queries inventoried, three of which were missing a tenant filter; tenancy documents moved into tenant-scoped storage with signed links; invitations, role changes and ownership transfer built as proper flows so the shared logins could be split into 31 individual accounts; and cross-tenant access tested from accounts in three agencies.

**Result:** the shared logins were eliminated, which also resolved an issue the agencies had raised about not knowing who had entered a payment. Two agencies that had been evaluating an alternative stayed, and Pieter now sends a one-page isolation description as part of every proposal.

> *"Nothing leaked through the part I had been careful about. It leaked through a number on a dashboard that counted the whole table."*
> — **Pieter Blom, Founder, Huurbeheer (Dordrecht)**

**Cost & Timeline:** €6,800 (organisation model, tenant column across nineteen tables with backfill, policy rewrite, dashboard and report audit, privileged query review, invitation and ownership flows, isolation testing) — completed in 12 business days.

## Frequently Asked Questions

### When do I need multi-tenancy?

As soon as a customer might be a company rather than one person — which for Dutch business products is almost always. The request "can my colleague have access too?" arrives within months, and the answer depends on whether records belong to users or to organisations.

### Should each customer get their own database?

Usually not. A shared schema with a tenant column on every table, enforced by row level security, is the standard approach and what Supabase is designed around. Separate databases add migration and reporting burden without addressing the real risk, which is a query missing a filter.

### Where does tenant isolation usually leak?

A table added later without a tenant column, policies checking the creating user rather than the organisation, privileged server-side queries where policies do not apply, unfiltered dashboard aggregates, and shared resources outside the database such as files, caches and search indexes.

### How expensive is it to add tenancy later?

Considerably more than building it, and the cost is mostly in the data: deciding which tenant every existing row belongs to requires human judgement and customer conversations, and it must happen while the product keeps running.

### What will a business customer ask about isolation?

How their data is separated, how you verified it, and what exceptions exist. A clear answer — a tenant on every row enforced in the database, tested from a second account, with a small documented set of privileged operations — is worth more in a procurement conversation than any feature.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When do I need multi-tenancy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "As soon as a customer might be a company rather than an individual. The request for colleague access arrives within months, and the answer depends on whether records belong to users or organisations."
      }
    },
    {
      "@type": "Question",
      "name": "Should each customer get their own database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not. A shared schema with a tenant column enforced by row level security is standard; separate databases add burden without fixing the real risk of a missing filter."
      }
    },
    {
      "@type": "Question",
      "name": "Where does tenant isolation usually leak?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tables added later without a tenant column, policies checking the creator rather than the organisation, privileged server-side queries, unfiltered aggregates, and files, caches or indexes not scoped by tenant."
      }
    },
    {
      "@type": "Question",
      "name": "How expensive is it to add tenancy later?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Much more than building it up front, mostly because deciding which tenant each existing row belongs to requires judgement and customer conversations while the product stays running."
      }
    },
    {
      "@type": "Question",
      "name": "What will a business customer ask about isolation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The mechanism, how you verified it, and what exceptions exist — answerable in five sentences if tenancy is enforced in the database and tested from a second account."
      }
    }
  ]
}
</script>
