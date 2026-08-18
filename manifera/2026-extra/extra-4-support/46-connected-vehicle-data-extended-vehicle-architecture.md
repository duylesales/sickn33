---
title: "Why a Connected Vehicle Platform's Data Architecture Should Follow the Extended Vehicle Model"
keywords: "custom software development, custom software engineering, software product, software system development"
buyer_stage: "Consideration"
target_persona: "A"
---

# Why a Connected Vehicle Platform's Data Architecture Should Follow the Extended Vehicle Model

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why a Connected Vehicle Platform's Data Architecture Should Follow the Extended Vehicle Model",
  "description": "A technical deep-dive into why a custom connected vehicle or fleet telematics platform should be architected around the ISO 20078 Extended Vehicle data access model.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/connected-vehicle-data-extended-vehicle-architecture" }
}
</script>

A CTO at a mobility or fleet technology company building a connected vehicle data platform — one aggregating telematics, diagnostics, and usage data from vehicles across a fleet or a broader vehicle population — faces a foundational architecture decision that shapes the platform's real-world data access reliability: whether the platform's vehicle data integration follows the Extended Vehicle model formalized in ISO 20078, or a more ad hoc, vehicle-manufacturer-specific integration approach.

## What the Extended Vehicle Model Actually Standardizes

Getting this decision right early matters considerably more than it might initially appear, precisely because the cost of correcting it later compounds with every additional manufacturer relationship built on top of the wrong foundation.

ISO 20078, the Extended Vehicle (ExVe) standard, defines a structured architectural model for how vehicle data flows from a vehicle to external services: the vehicle manufacturer operates an "Extended Vehicle" backend system that securely aggregates data from the vehicle itself, and external applications and services access this data through the manufacturer's ExVe interface using standardized data categories and access patterns, rather than attempting direct vehicle-level data access (which raises real security and safety concerns manufacturers are, reasonably, unwilling to expose broadly). The standard doesn't eliminate manufacturer-specific implementation differences entirely, but it establishes a shared conceptual and architectural framework that meaningfully reduces the integration complexity a platform faces when connecting to data from vehicles across different manufacturers.

## Why Ad Hoc, Manufacturer-Specific Integration Creates a Real Scaling Problem

A connected vehicle platform built around direct, manufacturer-specific integrations — without an architecture designed around the shared conceptual model ExVe provides — tends to treat each new vehicle manufacturer relationship as an entirely bespoke integration project, since without a shared architectural framework to build against, there's no consistent internal structure the platform's data model can be organized around across different manufacturer integrations. This becomes a genuine scaling constraint for any platform intending to support vehicles across a realistic multi-manufacturer fleet or vehicle population, since the platform's actual vehicle coverage becomes gated by how many bespoke manufacturer integrations the engineering team has had capacity to individually build, rather than being gated primarily by manufacturer participation and API availability.

## What Building on the Extended Vehicle Model Actually Requires

- **Structuring the platform's internal vehicle data model around ExVe's standardized data categories**, so data from different manufacturers' ExVe-compliant interfaces can be normalized into a genuinely consistent internal representation, rather than each manufacturer integration producing its own bespoke internal data structure requiring separate downstream handling.
- **Building the platform's authentication and consent management around the access control patterns ExVe assumes**, since vehicle data access typically requires vehicle owner or fleet operator consent flows that need to work consistently across different manufacturer ExVe implementations rather than requiring a separately designed consent flow per manufacturer.
- **Designing the data ingestion layer to accommodate genuine differences in update frequency and data completeness across manufacturers**, since even within a shared standard, different manufacturers' ExVe implementations vary in exactly which data categories they expose and how frequently — a platform's data model needs to represent this variability explicitly rather than assuming uniform data availability across all connected vehicles.

## Why This Decision Directly Shapes a Platform's Realistic Market Coverage

A specific, concrete business consequence of this architectural choice: a fleet or mobility platform's actual value proposition to a customer depends directly on how comprehensively it can cover that customer's real, often multi-manufacturer vehicle fleet. A platform architected around the Extended Vehicle model's shared conceptual framework can extend coverage to a new manufacturer with meaningfully less incremental engineering effort than a platform where each new manufacturer requires a fully bespoke integration built without a shared underlying architecture to build from — directly affecting how quickly and cost-effectively a platform can grow its actual vehicle coverage to match real customer fleet composition.

## Why Consent and Data Protection Requirements Compound This Architecture Decision

A specific, additional consideration that reinforces the case for standards-aligned architecture: vehicle telematics data frequently includes information that qualifies as personal data under GDPR and similar frameworks, particularly location history and driving behavior data tied to an identifiable vehicle owner or driver, meaning a connected vehicle platform's consent management isn't purely a technical convenience, it's a genuine legal requirement with real compliance stakes. The Extended Vehicle model's standardized access control patterns were developed with exactly this consideration in mind, providing a more consistent, auditable foundation for demonstrating that vehicle data access genuinely respects owner consent across manufacturers, compared to a collection of ad hoc, per-manufacturer consent flows each implemented separately with potentially inconsistent rigor.

A platform built around fragmented, manufacturer-specific consent handling faces a harder compliance verification challenge than a platform built on a consistent, standards-aligned consent architecture, simply because demonstrating consistent, correct consent handling across several genuinely different bespoke implementations is inherently more error-prone and harder to audit than verifying a single, consistently-applied consent pattern across manufacturers. This is a specific, practical reason the architecture decision described in this article carries real compliance weight beyond its more visible engineering efficiency benefits.

## Why This Gap Is Easy to Underweight During Early Platform Development

A specific reason this architectural mismatch shows up repeatedly among mobility technology startups specifically: an early-stage platform's first manufacturer partnership is often the direct result of a specific business relationship or opportunity, and building that first integration to work well and quickly, without a broader multi-manufacturer architecture yet in view, is a genuinely reasonable early-stage priority. The cost of this sequencing only becomes visible once a second and third manufacturer relationship becomes commercially necessary, typically driven by real customer demand for broader fleet coverage, at which point the team discovers the first integration's bespoke design didn't establish any reusable architectural foundation for the integrations that follow. A team that anticipates this pattern from the start, building even a first single-manufacturer integration with the Extended Vehicle model's shared conceptual structure in mind, avoids this specific, costly rediscovery later, and enters its second manufacturer negotiation already positioned to move quickly rather than starting a new architectural conversation from zero.

## Manifera's Approach: Building Connected Vehicle Platforms on Standards-Aligned Data Architecture

- **Amsterdam (Governance/Standards-Aligned Vehicle Data Scoping):** Dutch project leads scope connected vehicle platform architecture around the Extended Vehicle model's shared conceptual framework from the initial design phase, positioning the platform for efficient multi-manufacturer coverage growth.
- **Vietnam (Execution/Normalized, Multi-Manufacturer Data Engineering):** The engineering pod builds vehicle data normalization, consent management, and ingestion infrastructure designed around ExVe's shared architectural patterns, reducing incremental integration cost per new manufacturer.

This is Dutch Management × Vietnamese Mastery applied to connected vehicle platform development itself: governance that scopes vehicle data architecture around genuine multi-manufacturer scalability, paired with execution capable of building normalized, standards-aligned data infrastructure. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach for connected vehicle and fleet telematics platforms.

## Case Study: A Miskolc Fleet Platform's Architecture Correction

Flotta Digitális, a Miskolc-based fleet telematics startup, had built an initial connected vehicle data platform with direct, bespoke integrations to its first two manufacturer partnerships, each built as an entirely custom project without a shared internal data model to normalize against. As fleet customers increasingly requested support for additional vehicle manufacturers already common in their actual fleets, each new manufacturer relationship required a multi-month, largely from-scratch integration effort, directly constraining the platform's realistic growth pace.

Manifera's Amsterdam team rebuilt the platform's core vehicle data architecture around the Extended Vehicle model's shared conceptual framework, normalizing incoming data from each manufacturer's ExVe-compliant interface into a genuinely consistent internal representation, and building a consent and authentication layer designed to work consistently across manufacturer implementations.

> *"Every new manufacturer used to mean starting mostly from scratch. Once we rebuilt around the shared architecture the industry standard actually provides, adding a new manufacturer became a meaningfully smaller, more predictable piece of work instead of its own multi-month project every time."*
> — **CTO, Flotta Digitális**

Flotta Digitális has since added coverage for several additional vehicle manufacturers at a meaningfully faster pace than its original bespoke-integration approach supported, directly expanding its addressable fleet customer base.

## Ad Hoc Manufacturer Integration vs. Extended Vehicle-Aligned Architecture

| Factor | Ad Hoc Manufacturer Integration | Extended Vehicle-Aligned Architecture |
|---|---|---|
| New manufacturer integration effort | Largely bespoke each time | Reduced by shared architectural framework |
| Internal data consistency | Fragmented per-manufacturer structures | Normalized, consistent internal representation |
| Consent and authentication | Separately designed per manufacturer | Consistent pattern across implementations |
| Realistic growth pace | Gated by bespoke integration capacity | Gated primarily by manufacturer participation |

## Scoping Your Own Connected Vehicle Platform's Data Architecture

Before building a connected vehicle or fleet telematics platform, structure the core data architecture around the Extended Vehicle model's shared conceptual framework — an ad hoc, manufacturer-by-manufacturer integration approach constrains realistic multi-manufacturer fleet coverage growth. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about building an Extended-Vehicle-aligned connected vehicle platform.

## Frequently Asked Questions

### (Scenario: CTO scoping a connected vehicle platform) What is the Extended Vehicle model, and why does it matter for platform architecture?

ISO 20078's Extended Vehicle model establishes a shared architectural framework for how vehicle data flows from manufacturers to external platforms, meaningfully reducing integration complexity compared to ad hoc, manufacturer-specific approaches.

### (Scenario: engineering lead planning multi-manufacturer support) Why does ad hoc manufacturer integration become a scaling problem?

Without a shared architectural framework, each new manufacturer relationship becomes a largely bespoke integration project, gating the platform's realistic vehicle coverage growth by available engineering capacity rather than manufacturer participation.

### (Scenario: founder trying to understand business impact) How does Extended-Vehicle-aligned architecture affect a platform's addressable market?

It reduces incremental integration effort per new manufacturer, letting a platform extend real fleet coverage to match customer vehicle composition more quickly and cost-effectively than a fully bespoke integration approach.

### (Scenario: product lead wondering about data consistency) Why does normalizing data across manufacturers into a consistent internal model matter?

Fragmented, per-manufacturer internal data structures require separate downstream handling for each manufacturer's data, while a normalized model lets the platform's analytics and features work consistently regardless of which manufacturer a specific vehicle's data originated from.

### (Scenario: CTO evaluating a mobility technology development team) What should I ask a development team about their connected vehicle platform experience?

Ask specifically how they structure vehicle data internally and whether their architecture aligns with the Extended Vehicle model's shared framework — genuine experience produces a specific, technical answer about data normalization and consent handling.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO scoping a connected vehicle platform) What is the Extended Vehicle model, and why does it matter for platform architecture?", "acceptedAnswer": { "@type": "Answer", "text": "ISO 20078's model establishes a shared framework for vehicle data flow, reducing integration complexity versus ad hoc approaches." } },
    { "@type": "Question", "name": "(Scenario: engineering lead planning multi-manufacturer support) Why does ad hoc manufacturer integration become a scaling problem?", "acceptedAnswer": { "@type": "Answer", "text": "Without a shared framework, each manufacturer becomes a bespoke project, gating growth by engineering capacity, not participation." } },
    { "@type": "Question", "name": "(Scenario: founder trying to understand business impact) How does Extended-Vehicle-aligned architecture affect a platform's addressable market?", "acceptedAnswer": { "@type": "Answer", "text": "It reduces incremental integration effort per manufacturer, letting coverage match customer fleets more quickly and cost-effectively." } },
    { "@type": "Question", "name": "(Scenario: product lead wondering about data consistency) Why does normalizing data across manufacturers into a consistent internal model matter?", "acceptedAnswer": { "@type": "Answer", "text": "A normalized model lets analytics and features work consistently regardless of which manufacturer a vehicle's data came from." } },
    { "@type": "Question", "name": "(Scenario: CTO evaluating a mobility technology development team) What should I ask a development team about their connected vehicle platform experience?", "acceptedAnswer": { "@type": "Answer", "text": "Ask how they structure vehicle data internally and whether their architecture aligns with the Extended Vehicle model's framework." } }
  ]
}
</script>
