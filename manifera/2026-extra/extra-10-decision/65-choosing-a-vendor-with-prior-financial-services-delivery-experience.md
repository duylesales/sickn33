---
title: "Choosing a Vendor With Prior Financial Services Delivery Experience"
keywords: "financial services software vendor, fintech development experience, banking software vendor, PSD2 development, financial software compliance, vendor selection fintech"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Choosing a Vendor With Prior Financial Services Delivery Experience

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Vendor With Prior Financial Services Delivery Experience",
  "description": "A CTO's framework for verifying whether a vendor's claimed financial services experience is real operational depth or surface-level familiarity, covering reconciliation logic, regulatory reporting, and the diligence questions that separate the two.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-a-vendor-with-prior-financial-services-delivery-experience"}
}
</script>

Every vendor on your shortlist will claim financial services experience. Half of them mean "we built a website for a bank once." The other half mean they have shipped reconciliation logic that survives a month-end close, understand why a ledger entry can never be edited only reversed, and can explain PSD2's Strong Customer Authentication requirements without opening a browser tab. As a CTO deciding who builds your next payments feature, lending platform, or core banking integration, telling these two groups apart before you sign is the single highest-leverage thing you can do in the vendor selection process.

This distinction matters because financial software has a failure mode that most software doesn't: bugs that look fine in every test environment and only surface at scale, under real transaction volume, against real regulatory scrutiny. A double-entry bookkeeping error that nets to zero in a demo can silently misstate a balance sheet after ten thousand transactions. An idempotency gap that never triggers in staging can cause duplicate payment execution the first time a network blip causes a client to retry a request. Generic engineering talent, however skilled, has not internalized these failure modes because they have not been burned by them before — and the first time they get burned, it is on your production system with your customers' money.

This article gives you the specific technical and operational questions to ask that separate a vendor with genuine financial services delivery depth from one that has adjacent experience and is hoping it transfers.

## Ledger Discipline: The Tell That Separates Real Experience From Adjacent Experience

Ask any vendor how they would model an account balance, and a vendor without real financial services depth will describe a mutable balance field updated on each transaction — fast to build, and fundamentally wrong for anything handling money at scale. A vendor with real experience will describe an append-only ledger of debits and credits, where balance is a derived value computed from the transaction history, never stored as ground truth and directly edited. This is not a stylistic preference; it is the difference between a system that can reconstruct exactly what happened at any point in time for an audit, and one that cannot.

The follow-up question that further separates real experience: how do you handle a transaction that needs to be corrected after the fact? A vendor with genuine domain depth will answer "reversal entry, never a delete or edit" without hesitation, because financial ledgers are immutable by design — every correction is itself a new, auditable entry. If a vendor's answer involves editing or deleting a prior record, that is disqualifying for anything touching real money movement.

## Idempotency and Retry Logic: Where Naive Systems Lose Money

Payment and transaction systems operate over unreliable networks, which means clients will sometimes retry a request after a timeout, not knowing whether the original request actually succeeded server-side. A system without idempotency keys will, under exactly this condition, execute the same payment twice. This is not a hypothetical edge case — it is one of the most common production incidents in fintech engineering, and a vendor who has actually built payment systems will bring up idempotency unprompted when discussing architecture, because they have been burned by its absence before.

Ask specifically: how does your proposed architecture guarantee exactly-once processing for a payment instruction under network failure and client retry? A vendor with real experience will describe idempotency keys, request deduplication windows, and explicit state machines for transaction status. A vendor without it will describe generic "retry with backoff" logic that solves network reliability but not the money-duplication problem underneath it.

## Regulatory Reporting Isn't a Feature, It's an Architecture Constraint

PSD2's Strong Customer Authentication (SCA) requirements, open banking API standards, and national regulator reporting obligations — DNB reporting requirements in the Netherlands, for instance — are not features bolted onto a finished system. They shape core architecture decisions: how authentication flows are sequenced, what data must be retained and for how long, and what audit trail granularity a transaction record needs to carry from the start. A vendor who treats regulatory reporting as a checklist added near launch will typically need to retrofit data capture that should have existed from the first transaction, which for a system already in production means a painful and sometimes incomplete backfill.

Ask a shortlisted vendor to describe, specifically, how SCA exemption logic (low-value transactions, trusted beneficiaries, recurring payments) would be architected into a checkout flow. This is specific enough that a vendor without direct experience cannot convincingly fake an answer.

## The Reference Check That Actually Reveals Something

Standard reference checks ask "were they good to work with," which every reference will answer positively — nobody offers a hostile reference. The reference check that actually reveals financial services depth asks a narrower, harder question: "describe a production incident on the financial system this vendor built, and how they responded." A vendor with real experience will have an incident to describe, because financial systems at any meaningful scale experience incidents, and the interesting information is in the response — how fast it was detected, how it was communicated, whether root cause analysis prevented recurrence. A vendor who claims a spotless record on a live financial system is either exaggerating scale, exaggerating experience, or has not been running the system long enough to have hit a real edge case yet.

## Compliance Certifications Are a Floor, Not a Substitute for Domain Fluency

ISO 27001 and SOC 2 certifications demonstrate security process maturity, and they matter — but they are not evidence of financial domain fluency. A vendor can hold both certifications while still modeling account balances incorrectly, because certifications audit information security controls, not business logic correctness. Treat certifications as a prerequisite gate, not a decision criterion: verify them, then move past them to the domain-specific questions above, which is where the real differentiation between vendors actually lives.

## What "Prior Experience" Should Actually Mean in a Proposal

When a vendor's proposal cites financial services experience, push for specifics: which systems, what regulatory frameworks governed them, what scale (transaction volume, not just user count, since financial systems live or die on throughput and consistency under load), and what went wrong along the way. A proposal that lists client logos without any of this detail is marketing, not evidence. A proposal that names the specific reconciliation problem solved on a prior engagement, unprompted, is evidence.

## Making the Final Call

Prior financial services experience is not always the deciding factor — a well-bounded, low-stakes feature like an internal reporting dashboard pulling from an already-reconciled data warehouse does not require the same domain depth as a payments engine or lending decision system. But for anything that moves money, holds a balance, or feeds regulatory reporting, domain experience should outweigh a lower day rate every time, because the cost of a naive implementation surfaces later, at scale, and is materially more expensive to fix than to build correctly the first time.

Manifera's engineering teams have delivered ledger systems, payment integrations, and regulatory reporting pipelines for European financial services clients, with the domain fluency to ask the right architecture questions before code gets written. If you're evaluating vendors for a financial services build, our [custom software development](https://www.manifera.com/services/custom-software-development/) team can walk through your specific transaction and compliance requirements.

## Frequently Asked Questions

### Is it ever acceptable to use a generalist vendor for a financial services project?
Yes, for components genuinely outside the money-movement and regulatory-reporting core — a marketing site, an internal admin tool reading from an already-correct data source, or a reporting dashboard with no write access to financial data. The moment the vendor touches ledger logic, payment execution, or regulatory data capture, domain experience becomes non-negotiable.

### How do we verify a vendor's claimed transaction volume experience isn't exaggerated?
Ask for order-of-magnitude specifics — transactions per day or peak transactions per second — and a description of what broke at that scale. A vendor who can describe a specific scaling bottleneck they hit and resolved is more credible than one who states a large number without operational detail.

### What's a reasonable timeline expectation difference between an experienced and inexperienced vendor?
An experienced vendor typically front-loads more time into architecture and data modeling discovery, which can look slower in week one, but avoids the mid-project rework that inexperienced vendors commonly hit once reconciliation or regulatory gaps surface — often adding 30-50% to the original timeline.

### Should we require SOC 2 or ISO 27001 certification even for a smaller financial services engagement?
Generally yes if the vendor will have any access to production financial data, since certification reflects baseline security process discipline regardless of engagement size. For a small, tightly-scoped engagement with no production data access, it's reasonable to weight it less heavily.

### How many reference calls should we make before deciding, and what should we ask?
Two to three is typically sufficient if each call goes deep rather than wide. Prioritize the incident-response question over generic satisfaction questions — a reference who can describe a real production issue and the vendor's response gives you far more signal than five references who all say "they were great to work with."

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is it ever acceptable to use a generalist vendor for a financial services project?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, for components genuinely outside the money-movement and regulatory-reporting core — a marketing site, an internal admin tool reading from an already-correct data source, or a reporting dashboard with no write access to financial data. The moment the vendor touches ledger logic, payment execution, or regulatory data capture, domain experience becomes non-negotiable."}},
    {"@type": "Question", "name": "How do we verify a vendor's claimed transaction volume experience isn't exaggerated?", "acceptedAnswer": {"@type": "Answer", "text": "Ask for order-of-magnitude specifics — transactions per day or peak transactions per second — and a description of what broke at that scale. A vendor who can describe a specific scaling bottleneck they hit and resolved is more credible than one who states a large number without operational detail."}},
    {"@type": "Question", "name": "What's a reasonable timeline expectation difference between an experienced and inexperienced vendor?", "acceptedAnswer": {"@type": "Answer", "text": "An experienced vendor typically front-loads more time into architecture and data modeling discovery, which can look slower in week one, but avoids the mid-project rework that inexperienced vendors commonly hit once reconciliation or regulatory gaps surface — often adding 30-50% to the original timeline."}},
    {"@type": "Question", "name": "Should we require SOC 2 or ISO 27001 certification even for a smaller financial services engagement?", "acceptedAnswer": {"@type": "Answer", "text": "Generally yes if the vendor will have any access to production financial data, since certification reflects baseline security process discipline regardless of engagement size. For a small, tightly-scoped engagement with no production data access, it's reasonable to weight it less heavily."}},
    {"@type": "Question", "name": "How many reference calls should we make before deciding, and what should we ask?", "acceptedAnswer": {"@type": "Answer", "text": "Two to three is typically sufficient if each call goes deep rather than wide. Prioritize the incident-response question over generic satisfaction questions — a reference who can describe a real production issue and the vendor's response gives you far more signal than five references who all say 'they were great to work with.'"}}
  ]
}
</script>
