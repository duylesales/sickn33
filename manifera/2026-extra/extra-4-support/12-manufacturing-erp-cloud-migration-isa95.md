---
title: "Migrating a Manufacturing ERP to the Cloud Without Breaking the Shop Floor Connection"
keywords: "cloud migration, development in cloud, GDPR compliance, euro cloud"
buyer_stage: "Decision"
target_persona: "C"
---

# Migrating a Manufacturing ERP to the Cloud Without Breaking the Shop Floor Connection

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Migrating a Manufacturing ERP to the Cloud Without Breaking the Shop Floor Connection",
  "description": "A case study in migrating a manufacturing ERP system to EU cloud infrastructure while preserving the ISA-95 integration layer connecting it to shop floor control systems.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/manufacturing-erp-cloud-migration-isa95" }
}
</script>

An IT Manager at a manufacturing company evaluating an ERP cloud migration faces a genuinely specific risk that most generic enterprise cloud migration playbooks simply don't account for at all: a manufacturing ERP doesn't just run finance and inventory modules in isolation, it typically sits at a specific, defined layer of integration with the actual shop floor control systems that run production — and a migration that quietly breaks that integration doesn't just cause a minor software problem, it can genuinely stop physical production outright.

## Why Manufacturing ERP Sits in a Structured Integration Hierarchy

The ISA-95 standard, developed by the International Society of Automation, defines a widely adopted reference model for how enterprise systems (like ERP, at what the standard calls Level 4) should integrate with manufacturing operations management systems (Level 3, covering scheduling and production tracking) and the actual control systems running equipment on the shop floor (Levels 0-2). This layered model exists precisely because enterprise and shop-floor systems have very different requirements — an ERP system optimizes for business-process correctness and can tolerate some latency, while shop-floor control systems often need real-time or near-real-time responsiveness that a general-purpose cloud migration approach isn't automatically designed to preserve.

A manufacturing ERP migration that treats the ERP as a fully isolated system to simply move to the cloud, without explicitly mapping and carefully preserving its ISA-95 Level 3/4 integration points, risks introducing real latency or reliability issues into a connection that shop floor operations directly depend on for accurate, timely production data — even though the migration itself might look completely successful from the ERP's own narrow perspective in isolation.

## What Actually Needs Explicit Attention in the Migration Plan

- **Map every existing Level 3/4 integration point before migration begins** — which specific data flows between the ERP and manufacturing execution systems, at what frequency, and with what latency tolerance, since this map rarely exists as a single, current document and usually needs to be reconstructed from a combination of system documentation and direct conversations with shop floor engineers.
- **Test integration latency under cloud conditions specifically**, not just functional correctness — a data sync that worked reliably over a local network connection can behave differently once the ERP is cloud-hosted and communicating with on-premise shop floor systems over the internet, even when the integration logic itself hasn't changed at all.
- **Plan for hybrid connectivity during and potentially after migration**, since some manufacturing operations reasonably keep Level 3 manufacturing execution systems on-premise for reliability and latency reasons even after moving the ERP itself to the cloud — this isn't a failed migration, it's often the architecturally correct outcome for a specific manufacturing environment's real requirements.
- **Validate GDPR data residency requirements for any EU-relevant data flowing through the migrated system**, since a manufacturing ERP commonly holds employee data, supplier contract information, and sometimes customer data alongside its core production and inventory functions.

## Why This Mapping Work Is Genuinely Hard to Skip Safely

A reasonable objection to the ISA-95 mapping discipline described above is that it adds real time to a migration project before any visible progress is made — mapping integration points doesn't look like migration work to a stakeholder eager to see the ERP actually running in the new environment. This objection deserves a direct answer, because it's exactly the pressure that led to Śląsk Precision Manufacturing's original, unmapped migration attempt: the mapping work is genuinely hard to skip safely because the alternative isn't "probably fine" — it's "the risk moves from being visible and manageable during planning to being invisible until it surfaces as a live production problem." A scheduling discrepancy discovered during a mapping exercise costs a conversation and a design decision. The same discrepancy discovered during week one of live production costs actual manufacturing disruption, urgent remediation under pressure, and, often, a meaningful erosion of the operations team's trust in the migration effort as a whole.

This asymmetry — cheap to catch during planning, expensive to catch in production — is the same underlying logic that shows up across most of the technical due-diligence and risk-management thinking in software delivery generally, and it applies with particular force to manufacturing specifically because the downside of a missed integration point isn't abstract. It's a stopped line, a missed shipment, or an operations team that no longer trusts the next system change proposed to them, which has its own real cost in how much scrutiny and resistance future improvement projects encounter, independent of whether those future projects are actually well-planned or not.

## Manifera's Approach: Migrating the ERP Without Losing the Shop Floor Connection

- **Amsterdam (Governance/Integration-Aware Migration Planning):** Dutch project leads map ISA-95 integration points explicitly before migration planning begins, ensuring the shop-floor connection is a first-class migration requirement, not an afterthought discovered once the ERP is already moved.
- **Vietnam (Execution/Latency-Validated Integration Engineering):** The engineering pod tests integration performance under real cloud-hosted conditions before cutover, and builds hybrid connectivity architecture where a manufacturing environment's actual latency requirements call for it.

This is Dutch Management × Vietnamese Mastery applied to manufacturing ERP migration itself: governance that treats the ISA-95 integration layer as a core migration requirement, paired with execution that validates real-world performance before committing to a full cutover. Explore Manifera's [cloud migration](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) approach for manufacturing enterprise systems.

## Case Study: A Katowice Manufacturer's Preserved Integration

Śląsk Precision Manufacturing, a Katowice-based industrial parts manufacturer, needed to migrate its genuinely aging on-premise ERP system to EU cloud infrastructure, both for real infrastructure modernization reasons and to meet a major customer's specific GDPR-driven data residency requirement for supplier information. An initial internal migration attempt, planned without explicit ISA-95 mapping, went ahead with the ERP migration and only discovered post-migration that production scheduling data sync with the shop floor's manufacturing execution system had degraded from near-real-time to several minutes of latency — enough to cause scheduling discrepancies during the first week of live operation.

Manifera's Amsterdam team, engaged for a corrective remediation, mapped the full ISA-95 integration hierarchy explicitly, identified the specific latency-sensitive data flows causing the scheduling discrepancy, and implemented a hybrid architecture keeping the most latency-sensitive scheduling synchronization on a dedicated low-latency connection between the cloud-hosted ERP and the on-premise manufacturing execution system, while less time-sensitive data flows moved fully to standard cloud-to-cloud integration.

> *"We'd migrated the ERP successfully by every measure the migration team was tracking. Nobody had mapped what 'successful' needed to mean for the shop floor specifically, until the scheduling problems made it obvious we'd missed something."*
> — **IT Director, Śląsk Precision Manufacturing**

Śląsk Precision Manufacturing now requires explicit ISA-95 integration mapping as a standard first phase for any enterprise system migration touching production systems, treating shop floor connectivity as a named migration requirement rather than an assumed byproduct of a successful ERP move — a discipline the IT Director now describes as the single change most responsible for restoring the operations team's confidence in future technology projects after the original incident.

## Why This Level of Care Matters More for Manufacturing Than Typical Enterprise Migrations

A typical retail or professional services company migrating its own ERP system faces real but comparatively contained risk — a temporary sync delay affects reporting accuracy, which is genuinely disruptive but rarely stops physical operations. A manufacturing company's own ERP migration carries a categorically different and genuinely higher risk profile specifically because of the ISA-95 integration hierarchy described above: a broken or degraded Level 3/4 connection can translate directly into incorrect production scheduling, inventory discrepancies affecting material availability on the shop floor, or delayed visibility into quality issues that would normally trigger an immediate production response. This is precisely why a manufacturing ERP migration genuinely deserves its own distinct migration methodology, separate from a generic enterprise cloud migration playbook, rather than being treated simply as a standard ERP move that happens to belong to a manufacturing company.

## Generic ERP Migration vs. Manufacturing-Aware ERP Migration

| Factor | Generic ERP Migration Approach | Manufacturing-Aware Migration |
|---|---|---|
| Integration mapping | Assumed straightforward | ISA-95 Level 3/4 points explicitly mapped first |
| Latency validation | Functional testing only | Real cloud-hosted latency tested before cutover |
| Shop floor connectivity | Treated as automatically preserved | Explicit hybrid architecture where needed |
| Risk if something breaks | Reporting/data accuracy delay | Potential direct production disruption |

## Planning Your Own Manufacturing ERP Migration Correctly

Before migrating any manufacturing ERP to the cloud, map every ISA-95 Level 3/4 integration point explicitly and test latency thoroughly under real cloud conditions before cutover — a migration that looks successful from the ERP's perspective alone can still disrupt shop floor operations. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about a manufacturing-aware ERP cloud migration.

## Frequently Asked Questions

### (Scenario: IT manager planning a manufacturing ERP migration) What's different about migrating a manufacturing ERP compared to a typical enterprise ERP migration?

A manufacturing ERP sits within a structured integration hierarchy (defined by the ISA-95 standard) connecting it to shop floor manufacturing execution and control systems — a migration that doesn't explicitly preserve this connection risks disrupting production scheduling, not just reporting accuracy.

### (Scenario: engineering lead confused about ISA-95) What does the ISA-95 standard actually define, and why does it matter for cloud migration?

ISA-95 defines a reference model for how enterprise systems (like ERP) should integrate with manufacturing operations and shop floor control systems across distinct levels — mapping these integration points explicitly before migration prevents latency or reliability issues in connections production depends on.

### (Scenario: IT director wondering if the ERP needs to move fully to the cloud) Is it acceptable to keep some manufacturing systems on-premise while moving the ERP to the cloud?

Yes — a hybrid architecture, keeping latency-sensitive Level 3 manufacturing execution systems on-premise while migrating the ERP itself, is often the architecturally correct outcome for a specific manufacturing environment's real latency requirements, not a failed or incomplete migration.

### (Scenario: compliance officer checking GDPR relevance for manufacturing ERP) Does GDPR apply to a manufacturing ERP migration if the company mainly handles industrial parts, not consumer data?

Yes — a manufacturing ERP commonly holds employee data, supplier contract information, and sometimes customer data alongside production functions, all of which require the same EU data residency and processing diligence as any other personal data migration.

### (Scenario: CTO trying to validate a migration plan before committing) How can I verify a migration plan actually accounts for shop floor integration risk?

Ask the vendor directly whether ISA-95 or equivalent integration points have been explicitly mapped and whether latency will be tested under real cloud-hosted conditions before cutover, rather than relying on functional testing of the ERP system in isolation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: IT manager planning a manufacturing ERP migration) What's different about migrating a manufacturing ERP compared to a typical enterprise ERP migration?", "acceptedAnswer": { "@type": "Answer", "text": "A manufacturing ERP integrates with shop floor systems per the ISA-95 standard, so migration risk extends beyond reporting to production scheduling." } },
    { "@type": "Question", "name": "(Scenario: engineering lead confused about ISA-95) What does the ISA-95 standard actually define, and why does it matter for cloud migration?", "acceptedAnswer": { "@type": "Answer", "text": "It defines a reference model for enterprise-to-shop-floor integration levels, and mapping these points prevents latency issues production depends on." } },
    { "@type": "Question", "name": "(Scenario: IT director wondering if the ERP needs to move fully to the cloud) Is it acceptable to keep some manufacturing systems on-premise while moving the ERP to the cloud?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — a hybrid architecture is often the architecturally correct outcome given real latency requirements, not a failed migration." } },
    { "@type": "Question", "name": "(Scenario: compliance officer checking GDPR relevance for manufacturing ERP) Does GDPR apply to a manufacturing ERP migration if the company mainly handles industrial parts, not consumer data?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — manufacturing ERPs commonly hold employee and supplier personal data requiring the same GDPR diligence as any migration." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to validate a migration plan before committing) How can I verify a migration plan actually accounts for shop floor integration risk?", "acceptedAnswer": { "@type": "Answer", "text": "Ask whether integration points have been explicitly mapped and whether latency will be tested under real cloud-hosted conditions before cutover." } }
  ]
}
</script>
