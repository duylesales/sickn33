---
Title: "PropTech Prototypes: Tenant Data, Deposits, and What Must Be Right"
Keywords: proptech prototype compliance, tenant screening data, rental deposit handling, rental law obligations EU, proptech production ready, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# PropTech Prototypes: Tenant Data, Deposits, and What Must Be Right

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "PropTech Prototypes: Tenant Data, Deposits, and What Must Be Right",
  "description": "A practical walkthrough of the tenant-screening data limits, deposit-handling obligations, and rental-law requirements that change what a proptech prototype needs before it can manage a real tenancy. Helps non-technical founders decide what to fix before their first landlord signs up.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/proptech-prototypes-tenant-data-deposits-and-what-must-be-right" }
}
</script>

It's 11 PM and Wouter is staring at a bank transfer confirmation for €1,400 — a tenant's deposit, sitting in his company's regular operating account, the same account that pays for his AI tool subscriptions and his lunch. His proptech platform, built in Lovable over six weeks, has just processed its first real deposit, and it occurs to him for the first time that he has no idea whether that money is legally allowed to sit where it's sitting. It isn't, in most EU jurisdictions — and this single realization, arriving after the money has already moved rather than before, is the exact moment a founder's launch decision becomes a landlord's legal problem too.

PropTech prototypes tend to look deceptively simple: a listing, a tenant application, a lease, a deposit, some maintenance requests. Each of those five things carries a distinct obligation most AI-generated builds never account for, because none of them are things a general-purpose coding assistant knows to ask about unless a human tells it to.

## Deposits Are Not Revenue, and Your Database Shouldn't Treat Them That Way

Rental deposits in most EU countries are legally the tenant's money, held in trust, not the landlord's or the platform's revenue — and many jurisdictions specifically regulate how deposits must be held, often requiring a separate, identifiable account (sometimes a government-run or government-approved deposit protection scheme, as used in several EU markets) rather than allowing the deposit to sit in a landlord's or platform's general operating funds. Where a specific protection scheme applies, failing to register the deposit correctly within a required window can carry real financial penalties for the landlord, and a proptech platform enabling that failure by design — collecting deposits into the same account as subscription revenue — is building a landlord-facing product that sets its own customers up for a compliance breach.

The technical fix isn't complicated once it's identified: deposits need to be tracked in a ledger clearly separated from platform revenue, ideally paid into an account structure that reflects their actual legal status (a client account, an escrow-style holding, or direct integration with a recognized deposit protection scheme where one applies), with a clear audit trail showing whose deposit is whose and confirming it was actually registered where the law requires. This is precisely the "holding money that isn't yours" problem that shows up across several regulated sectors — the mechanics echo what changes for a fintech product handling client funds, but the specific rules here are landlord-tenant law, not payment services law, and they vary meaningfully by country and sometimes by region within a country.

## Tenant Screening Data: Where "More Information" Becomes a Liability, Not a Feature

A tenant application typically involves gathering income verification, employment history, sometimes credit information, occasionally references from a previous landlord. It's tempting, when building fast with AI tools, to just collect everything a landlord might conceivably want to see — but tenant screening data sits under the same GDPR data-minimization principle as anywhere else, and some of what founders instinctively want to collect (nationality, family status, health information relevant to accessibility needs) can also trigger anti-discrimination law concerns entirely separate from data protection, since several EU countries and cities have specific rules against certain selection criteria in rental housing.

The safer product design collects only what's demonstrably necessary to assess a tenancy — income relative to rent, a landlord reference, basic identity verification — and treats anything beyond that as a deliberate, justified addition rather than a default. It's also worth building retention limits specifically for rejected applicants: a prospective tenant who didn't get the apartment has the same GDPR rights as one who did, and an AI-generated prototype that keeps every rejected application indefinitely, "just in case," is accumulating exactly the kind of unnecessary sensitive data that turns into liability with no corresponding benefit.

## Credit and Background Checks: A Feature That Needs a Real Legal Basis, Not Just an API Key

If your platform integrates a credit-check or background-check API — genuinely useful for landlords, and a common feature request — the legal basis for running that check needs to be explicit and the tenant needs to be informed before it happens, not discover it after the fact in a rejection email. Some EU countries impose specific consumer-protection requirements around credit checks (a right to know the check was run, sometimes a right to see or dispute the result), and a "run the check silently as part of the application flow" implementation — which is what an AI tool builds by default when asked to "add a credit check" — skips exactly the disclosure step that keeps this feature legal.

Build this as an explicit, separate consent step within the application flow, log when a check was run and on what basis, and make sure your platform (or the check provider you integrate) can produce the actual result to the tenant on request. This is a small amount of additional engineering relative to the API integration itself, and it's the difference between a useful feature and a feature that exposes your landlord customers to a consumer complaint.

## Maintenance Requests and Access Logs: Where Physical Safety Meets Software

A maintenance request feature seems purely operational — a tenant reports a broken boiler, a landlord sees it, a contractor gets scheduled. But in several EU jurisdictions, landlords carry specific statutory obligations around habitability and timely repair of certain issues (heating, water, safety hazards), and a maintenance request that gets lost in a poorly built notification system isn't just a UX bug — it can become evidence in a tenant dispute about whether the landlord met a legal repair obligation within a required timeframe.

The practical requirement: every maintenance request needs a reliable, timestamped record that survives independent of whether an email notification actually arrived (email deliverability failures are common and, unlike a support ticket for a SaaS product, a missed maintenance notification has real habitability consequences). Status changes — reported, acknowledged, scheduled, resolved — need their own timestamps too, because "the landlord says they fixed it, the tenant says they didn't" is a dispute your platform's own records should be able to help resolve, not a dispute your platform contributed to by losing the original request.

## Multi-Party Access: Landlords, Tenants, Agents, and Sometimes a Housing Authority

Proptech products frequently have more distinct user roles than founders initially design for: the landlord (who may be an individual, a small letting agency, or a larger property management company), the tenant, sometimes a co-tenant or guarantor, occasionally a housing authority or municipal inspector in jurisdictions with rental registration requirements. Each role needs genuinely different visibility — a co-tenant shouldn't see a guarantor's financial details, a letting agent managing a portfolio for an absent landlord needs delegated access without becoming the account owner, and a municipal registration requirement (increasingly common in cities managing short-term and long-term rental registries) may require your platform to produce specific reports on request.

AI-generated prototypes typically implement two roles — landlord and tenant — with a flat permission model that doesn't anticipate agents, guarantors, or regulatory reporting at all. Adding these roles after launch, once real letting agencies and multi-unit landlords are actual customers, is a genuine access-control rebuild rather than a settings change, which is why it's worth designing the role structure with these parties in mind from the start even if you launch with only two of them active.

This matters commercially as much as legally, because letting agencies and portfolio landlords are frequently the more valuable customer segment for a proptech platform — a single agency managing forty units is a larger account than forty individual landlords managing one unit each, but only if the platform can actually represent that relationship. A flat two-role model forces an agency to either share one login across staff (a security and accountability problem in its own right) or manage each property as if it belonged to a different landlord, neither of which scales past a handful of units. Deciding on a proper delegated-access model early is as much a growth decision as a compliance one.

## What to Fix Before Your First Real Deposit

If you're a non-technical founder trying to prioritize with a limited budget, sequence it this way. First, separate deposit handling from operating revenue and confirm which deposit-protection regime, if any, applies in your market — this is the one item with a genuine legal penalty attached and no manual workaround once money has already moved incorrectly. Second, tighten tenant application data collection to what's demonstrably necessary and add retention limits for rejected applicants. Third, if you run credit or background checks, make the consent and disclosure step explicit and logged. Fourth, make maintenance request records reliable and independent of email deliverability. Role structure for agents and guarantors can reasonably wait until you have a letting agency asking for it, provided your data model doesn't actively prevent adding it later.

## Getting the Deposit and Data Handling Right, Concretely

LaunchStudio's engineers can build the separated deposit ledger, wire in a recognized deposit-protection scheme's API where one applies to your market, tighten tenant data collection and retention, add the explicit consent step around credit checks, and build maintenance-request tracking that doesn't depend on email arriving — this is squarely last-mile infrastructure work, done without touching the listing and application interface your landlords and tenants already use comfortably. Backed by Manifera's 11-plus years building production systems, this is the kind of database and workflow correction that's far cheaper before your first real deposit than after a tenant dispute.

What we can't tell you is which specific deposit protection scheme applies in your market, or how local anti-discrimination rules affect your specific screening criteria — that depends on jurisdiction and needs a local property-law specialist to confirm. [Use the price calculator](https://launchstudio.eu/en/#calculator) to see what separating your deposit handling and tightening tenant data collection would realistically cost before you take on more real tenancies.

## Real example

### A Room-Rental Platform Separates Deposits From Revenue Before Its First Dispute

Wouter Jansen built Kamerbasis, a platform helping small landlords in Amsterdam list rooms and manage tenant applications, in Lovable. It had processed eleven tenancies, each with a deposit paid directly into Kamerbasis's Stripe account alongside the platform's own subscription revenue, with no separation between the two in the database beyond a label on the transaction. A landlord using the platform asked, offhand, whether the deposits were registered with the Netherlands' rent deposit protections — Wouter didn't know, and worse, didn't have a clean way to even identify which transactions were deposits versus subscription payments.

The review separated deposit transactions into their own ledger table with a clear chain of custody per tenancy, moved deposit funds into a distinctly labeled holding structure rather than the general operating account, and built a simple reporting view so a landlord could confirm exactly which deposits were held, for which tenant, and their current status. Tenant application retention was also tightened, with rejected applications now automatically purged after a defined window instead of persisting indefinitely.

**Result:** Kamerbasis's landlords could, for the first time, see their deposit obligations clearly through the platform itself, and the fix happened before any dispute forced the question — not after one.

> *"I built a rental platform. I hadn't actually thought about the fact that I was suddenly the one holding other people's deposit money, mixed in with my own subscription revenue, until a landlord asked me a question I couldn't answer."*
> — **Wouter Jansen, Founder, Kamerbasis (Amsterdam)**

**Cost & Timeline:** €2,600 (Launch Ready Package, deposit ledger separation and tenant data retention fixes) — live in 10 business days.

## Frequently Asked Questions

### Do all EU countries require deposits to go into a government-approved scheme?

No — deposit protection rules vary significantly by country, and some markets have no mandatory scheme at all while others require registration within a specific window. Confirm the specific rule for the country (and sometimes the region within it) where your platform operates before assuming a single approach covers every market.

### Can I just tell landlords to handle deposits themselves outside the platform?

You can, and for an early-stage platform it's a legitimate way to avoid the deposit-holding problem entirely — but it means being explicit in your product and terms that the platform never touches deposit funds, and building the interface so it doesn't imply otherwise (for example, no "pay deposit" button that routes through your own payment account).

### What tenant screening data is safest to collect by default?

Income relative to rent, identity verification, and a previous landlord reference cover most legitimate screening needs. Treat anything beyond that — health information, family composition, nationality — as a deliberate addition you can specifically justify, not a default field because it seemed useful.

### How is deposit handling different from the fintech "holding client money" problem?

The underlying pattern — holding funds that legally belong to someone else — is similar, but the applicable rules are different: landlord-tenant law and deposit-protection schemes rather than payment services regulation. A platform can get the fintech-style safeguarding right and still fail a deposit-protection registration requirement, because they're separate legal frameworks.

### Should maintenance requests be logged even for very small landlords with one or two properties?

Yes — habitability and repair-timeline obligations generally apply regardless of how many properties a landlord owns, and a small landlord has just as much need for a reliable, timestamped maintenance record as a larger property manager, arguably more, since they have fewer other systems tracking the same information.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do all EU countries require deposits to go into a government-approved scheme?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Deposit protection rules vary significantly by country, and some markets have no mandatory scheme while others require registration within a specific window. Confirm the specific rule for the country where your platform operates."
      }
    },
    {
      "@type": "Question",
      "name": "Can I just tell landlords to handle deposits themselves outside the platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and for an early-stage platform it's a legitimate way to avoid the deposit-holding problem entirely, provided your product and terms are explicit that the platform never touches deposit funds."
      }
    },
    {
      "@type": "Question",
      "name": "What tenant screening data is safest to collect by default?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Income relative to rent, identity verification, and a previous landlord reference cover most legitimate screening needs. Treat anything beyond that as a deliberate, justified addition rather than a default field."
      }
    },
    {
      "@type": "Question",
      "name": "How is deposit handling different from the fintech 'holding client money' problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The underlying pattern of holding funds that belong to someone else is similar, but the applicable rules differ: landlord-tenant law and deposit-protection schemes rather than payment services regulation."
      }
    },
    {
      "@type": "Question",
      "name": "Should maintenance requests be logged even for very small landlords?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Habitability and repair-timeline obligations generally apply regardless of how many properties a landlord owns, and small landlords need a reliable, timestamped maintenance record just as much as larger property managers."
      }
    }
  ]
}
</script>
