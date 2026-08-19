---
title: "What PSD2 and GDPR Actually Add to a Fintech Custom Software Budget"
keywords: "custom software development cost, custom software development, fintech software development, custom software solution"
buyer_stage: "Decision"
target_persona: "A"
---

# What PSD2 and GDPR Actually Add to a Fintech Custom Software Budget

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What PSD2 and GDPR Actually Add to a Fintech Custom Software Budget",
  "description": "A cost breakdown of what PSD2 and GDPR compliance genuinely add to a fintech custom software build, layer by layer, for a CTO scoping a realistic budget.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/fintech-custom-software-compliance-cost" }
}
</script>

A fintech CTO scoping a first real budget for a payments or lending product usually starts from a generic custom software estimate, then adds "compliance" as a vague percentage on top — 15%, 20%, a number pulled from a conference talk rather than any actual cost model grounded in the specific product. That number is close to meaningless without knowing exactly which specific regulatory obligations are actually driving it, because PSD2 and GDPR add real cost in genuinely different places in the architecture, not as a single flat markup applied evenly across the whole build.

## Why "Add 20% for Compliance" Is the Wrong Mental Model

Compliance cost in real fintech software isn't a flat percentage tax applied evenly across the entire codebase — it's a set of specific, identifiable architectural requirements that show up in particular layers: authentication, data storage, third-party integration, audit logging, and incident response. A team that budgets compliance as a flat percentage consistently tends to underfund the specific layers that actually carry the real regulatory weight (strong customer authentication, audit trails) while overfunding other layers that don't genuinely need much extra work at all (a standard admin dashboard, for instance, rarely has meaningful PSD2 exposure). Understanding where the cost genuinely concentrates produces a more accurate budget than any percentage rule of thumb.

## PSD2: What It Specifically Requires, and What That Costs to Build

The EU's Second Payment Services Directive mandates Strong Customer Authentication (SCA) for most electronic payment transactions — a two-factor authentication requirement combining at least two of: something the user knows (a PIN or password), something they have (a device or token), and something they are (biometrics). For a custom fintech build, this isn't a checkbox feature; it requires:

- **A dedicated authentication service** capable of orchestrating multiple factors, handling fallback flows when a factor is unavailable, and logging every authentication event with enough detail to demonstrate compliance during an audit.
- **Integration with a licensed SCA provider or building a compliant in-house flow**, both of which carry real engineering cost — the build-vs-buy decision here should be made explicitly, not defaulted into.
- **Exemption handling logic**, since PSD2 allows specific exemptions (low-value transactions, trusted beneficiaries, recurring payments) that reduce friction for users but require their own rule engine and audit trail to justify why SCA was skipped for a given transaction.
- **Open Banking API compliance** if the product touches account information or payment initiation services, requiring adherence to specific technical standards (Berlin Group NextGenPSD2, or UK Open Banking equivalents) that dictate exact API shapes, not just general REST conventions.

Realistically, SCA and Open Banking API compliance together typically add a genuinely substantial, identifiable chunk of engineering time to a payments product's initial build — concentrated almost entirely in the authentication and integration layers, not spread evenly across the whole application. A team that hasn't built a compliant SCA flow before also tends to underestimate the testing burden specifically: exemption logic has to be verified against real regulatory edge cases, not just happy-path transactions, and that verification work is itself a meaningful and easily overlooked share of the total authentication-layer cost.

## GDPR: A Different Kind of Cost, Concentrated in Data Architecture

GDPR compliance cost concentrates in a different place: data modeling, retention, and subject-rights implementation, rather than authentication flows. For a fintech product specifically, this includes:

- **Data minimization at the schema level** — designing database tables to store only what's genuinely necessary for each specific purpose, rather than a single broad customer record that mixes KYC data, transaction history, and marketing preferences without clear purpose-limitation boundaries.
- **Right-to-erasure implementation that respects financial record-keeping obligations** — a genuinely tricky intersection, since GDPR's erasure right conflicts directly with anti-money-laundering (AML) requirements to retain transaction records for five to seven years, requiring careful legal-technical design of what can actually be erased versus what must be retained and anonymized instead.
- **Consent and purpose-tracking infrastructure**, since a fintech product typically processes data under multiple legal bases (contract necessity for transactions, legitimate interest for fraud detection, consent for marketing) that each require separately trackable justification.
- **Data processing agreements and sub-processor tracking** for every third-party service touching customer data — a payment gateway, an identity verification vendor, a cloud provider — each requiring its own documented data flow.

## Why These Two Layers Compound Rather Than Simply Add

The genuinely expensive part isn't PSD2 or GDPR individually — it's where they intersect. Strong Customer Authentication generates detailed logs of exactly when and how a user authenticated, which is itself personal data subject to GDPR's minimization and retention rules. An AML-driven retention requirement to keep transaction records for years directly constrains how a GDPR erasure request can actually be honored. A build that treats these as two separate compliance checklists, handled by two different consultants who never talk to each other, routinely produces a system where one regulation's requirement quietly undermines the other's — exactly the kind of gap that surfaces expensively during a regulatory audit or a Series B technical due diligence process, not during initial development.

## What a Realistic Fintech Compliance Budget Actually Looks Like

- **Scope compliance requirements during discovery, not after architecture is set** — retrofitting SCA or proper data minimization into an already-built system costs meaningfully more than designing for it from the schema up.
- **Separate the compliance budget into named line items** (authentication infrastructure, data architecture, audit logging, DPA management) rather than a single lump percentage, so a CFO can actually see where the money goes and evaluate trade-offs.
- **Budget for ongoing compliance maintenance, not just initial build** — PSD2's Regulatory Technical Standards and GDPR guidance both evolve, and a fintech product needs standing engineering capacity to track and implement regulatory updates, not a one-time compliance sprint.
- **Get compliance requirements reviewed by someone who understands both the legal obligation and the engineering implementation** — a legal-only review misses architectural implications; an engineering-only review misses legal nuance in exemptions and retention conflicts.

## Manifera's Approach: Compliance Architecture as a First-Class Scoping Input

- **Amsterdam (Governance/EU Regulatory Fluency):** Dutch project leads scope PSD2 and GDPR requirements explicitly during discovery, translating regulatory obligations into specific architectural line items a CFO can actually budget against, rather than a vague compliance percentage.
- **Vietnam (Execution/Compliant-by-Design Engineering):** The engineering pod builds authentication, data architecture, and audit logging with compliance requirements designed in from the schema level, rather than retrofitted after the fact.

This is Dutch Management × Vietnamese Mastery applied to regulated fintech development itself: governance that understands EU payments and data protection regulation in genuine depth, paired with execution that builds compliance into the architecture rather than bolting it on afterward. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach for regulated fintech products.

## Case Study: A Utrecht Fintech's Realistic Rebudget

Domplein Payments, a Utrecht-based fintech startup, had budgeted its first lending product using a generic custom software estimate plus a flat 20% "compliance buffer" suggested by an early advisor, with no breakdown of where that buffer would actually be spent.

Manifera's Amsterdam team, engaged during the scoping phase, broke the compliance requirement into specific line items: a dedicated SCA-capable authentication service, a data model designed around purpose-limited tables from the start, and an erasure-versus-retention decision tree built in consultation with the founder's AML counsel. The resulting budget was higher in the authentication and data-architecture line items than the original flat buffer had allocated, but lower overall than the generic 20% applied everywhere — because large parts of the application, like internal reporting dashboards, genuinely didn't carry the same compliance weight.

> *"The 20% buffer felt like a number nobody could actually defend. Once we saw it broken into the four or five places it was actually going, the budget conversation with our investors got a lot easier, not harder."*
> — **CTO, Domplein Payments**

Domplein Payments now uses the same line-item compliance breakdown for every new feature that touches payments or personal data, rather than reapplying a flat percentage assumption.

## PSD2 vs. GDPR: Where Each Cost Concentrates

| Regulation | Primary Cost Layer | Typical Engineering Work |
|---|---|---|
| PSD2 | Authentication, payment initiation | SCA orchestration, exemption logic, Open Banking API compliance |
| GDPR | Data architecture, subject rights | Purpose-limited schema design, erasure-vs-retention logic, consent tracking |
| Intersection | Audit logging, retention policy | Reconciling AML retention with GDPR erasure rights |

## Scoping Your Own Fintech Compliance Budget

Before accepting a flat compliance percentage on a fintech build, ask your vendor to break PSD2 and GDPR requirements into specific architectural line items — the two regulations add cost in genuinely different, identifiable places, not as a uniform markup. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about scoping a compliant fintech build.

## Frequently Asked Questions

### (Scenario: fintech CTO scoping a first compliance budget) How much should PSD2 and GDPR compliance actually add to a fintech software budget?

There's no reliable flat percentage — the real cost depends on how much of the product touches payment authentication versus personal data processing. Ask for a line-item breakdown by architectural layer rather than accepting a generic percentage estimate.

### (Scenario: founder confused about SCA requirements) Does every transaction in a fintech product need Strong Customer Authentication under PSD2?

No — PSD2 includes specific exemptions for low-value transactions, trusted beneficiaries, and certain recurring payments, though implementing exemption logic correctly requires its own rule engine and audit trail.

### (Scenario: CTO facing a GDPR erasure request that conflicts with AML rules) Can a fintech company actually honor a GDPR erasure request given AML record-retention requirements?

Generally not fully — most fintech products need a reconciliation approach that anonymizes rather than deletes transaction data subject to AML retention rules, while genuinely erasing data that isn't subject to that separate legal obligation.

### (Scenario: CFO trying to understand ongoing versus one-time compliance cost) Is fintech compliance a one-time cost or an ongoing budget line?

Ongoing — both PSD2's technical standards and GDPR guidance evolve over time, and a fintech product needs standing engineering capacity to track and implement regulatory updates, not just a one-time compliance sprint during initial build.

### (Scenario: startup trying to decide whether to build or buy SCA infrastructure) Should a fintech startup build its own Strong Customer Authentication flow or use a third-party provider?

It depends on scale and specific requirements — a licensed third-party SCA provider often makes sense for an early-stage product avoiding upfront infrastructure cost, while a larger, more differentiated payment flow may justify an in-house build; this should be an explicit decision, not a default.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: fintech CTO scoping a first compliance budget) How much should PSD2 and GDPR compliance actually add to a fintech software budget?", "acceptedAnswer": { "@type": "Answer", "text": "There's no reliable flat percentage — ask for a line-item breakdown by architectural layer rather than a generic percentage estimate." } },
    { "@type": "Question", "name": "(Scenario: founder confused about SCA requirements) Does every transaction in a fintech product need Strong Customer Authentication under PSD2?", "acceptedAnswer": { "@type": "Answer", "text": "No — PSD2 includes specific exemptions for low-value transactions, trusted beneficiaries, and certain recurring payments." } },
    { "@type": "Question", "name": "(Scenario: CTO facing a GDPR erasure request that conflicts with AML rules) Can a fintech company actually honor a GDPR erasure request given AML record-retention requirements?", "acceptedAnswer": { "@type": "Answer", "text": "Generally not fully — most fintech products need a reconciliation approach that anonymizes rather than deletes AML-retained data." } },
    { "@type": "Question", "name": "(Scenario: CFO trying to understand ongoing versus one-time compliance cost) Is fintech compliance a one-time cost or an ongoing budget line?", "acceptedAnswer": { "@type": "Answer", "text": "Ongoing — both PSD2 technical standards and GDPR guidance evolve, requiring standing engineering capacity, not a one-time sprint." } },
    { "@type": "Question", "name": "(Scenario: startup trying to decide whether to build or buy SCA infrastructure) Should a fintech startup build its own Strong Customer Authentication flow or use a third-party provider?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on scale — a licensed third-party provider often suits an early-stage product, while a differentiated flow may justify an in-house build." } }
  ]
}
</script>
