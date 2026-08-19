---
title: "How Transit Agencies Use a Dedicated Software Development Team to Handle Regional Fare-Capping Rules: A Case Study"
keywords: "custom software development, software outsourcing, dedicated software development team, offshore software development company"
buyer_stage: "Consideration"
target_persona: "C"
---

# How Transit Agencies Use a Dedicated Software Development Team to Handle Regional Fare-Capping Rules: A Case Study

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Transit Agencies Use a Dedicated Software Development Team to Handle Regional Fare-Capping Rules: A Case Study",
  "description": "A case study examining why a mobility-as-a-service platform spanning multiple transit agencies needs agency-configurable architecture to correctly apply divergent fare-capping and concession rules across operators.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/transit-fare-capping-case-study" }
}
</script>

A Product Lead or IT Manager at a mobility-as-a-service (MaaS) platform spanning multiple transit agencies faces a specific fare-logic reality that's easy to underweight during architecture planning: fare-capping rules — the daily and weekly spending caps that ensure a rider is never charged more than the equivalent of a period pass, and the concession structures applying discounts for seniors, students, and other eligible rider categories — genuinely differ from one agency to the next, with each operator setting its own cap thresholds, eligibility rules, and discount percentages independently. A platform architected around a single, uniform fare-logic implementation across all agencies risks either overcharging riders under one agency's actual rules or failing to apply a legally or contractually required concession under another's.

## Why a Single Hardcoded Fare Logic Creates Real Rider-Trust Risk

A MaaS platform built around one fare-capping and concession implementation applied uniformly across every agency it serves, regardless of each agency's actual published rules, faces a direct choice with real downside either way: applying one agency's cap and concession structure to a different agency's routes risks overcharging riders relative to what that specific agency's actual fare policy requires, while under-applying caps or concessions risks the platform failing to honor legally or contractually required discounts a specific agency's rules actually guarantee. Several MaaS platforms operating across multiple agencies have specifically faced rider complaints and agency contract disputes after a hardcoded fare implementation was found overcharging riders relative to a specific agency's actual published cap, a genuine, reputationally damaging example of how significant this divergence can be for a platform's actual multi-agency operation.

## Why Agency-Configurable Fare Architecture Is the More Sustainable Approach

A fare engine architected from the start around agency-configurable rules — able to apply each specific agency's own cap thresholds, concession eligibility criteria, and discount percentages based on which agency's service a rider is actually using — lets a MaaS platform correctly honor every agency's actual fare policy without forcing a one-size-fits-all implementation onto operators with genuinely different rules. This isn't simply a matter of a per-agency price multiplier, since fare-capping logic is genuinely more structurally complex than a flat rate adjustment — caps typically accumulate across multiple trips within a rolling period, and concession eligibility often depends on rider-category verification distinct from the fare calculation itself, meaning the underlying system needs to support genuinely configurable fare-calculation logic per agency, not just a configurable price, to accommodate the actual range of fare structures across a platform's served operators.

## What Building Agency-Configurable Fare Architecture Actually Requires

- **Structuring the fare engine's core logic around a configurable ruleset per agency**, rather than a single hardcoded fare calculation, so each operator's specific cap thresholds, concession rules, and accumulation periods can be applied without a separate, parallel fare system per agency.
- **Building reliable trip-to-agency attribution**, since correctly applying agency-specific fare rules depends on accurately identifying which agency's service a specific trip actually used, a determination that carries real technical nuance for riders making multi-agency, multi-leg journeys within a single trip.
- **Designing the system to accommodate each agency's own fare-policy changes independently**, since agencies periodically revise their own cap thresholds and concession structures, and a system that can only be updated for one agency's policy change through a platform-wide rework creates real ongoing operational risk as agencies continue to adjust their own fare policies over time.

## Why This Decision Also Shapes Revenue Reconciliation With Each Agency

A related, practical consideration worth naming directly: beyond fare correctness from the rider's perspective, most multi-agency MaaS platforms separately need to reconcile and remit collected fare revenue back to each individual agency according to that agency's own actual fare structure, an obligation entirely distinct from what the rider is charged. A platform's fare engine needs to accommodate both the genuinely divergent rider-facing fare landscape this article focuses on and the separate, agency-specific revenue reconciliation this creates, which depends on the same underlying per-agency fare data being tracked accurately. An agency-configurable architecture built with genuine flexibility in mind tends to accommodate revenue reconciliation more naturally than a system built around a narrower assumption that only rider-facing fare correctness needs to be considered, since the same underlying configurability that supports per-agency fare rules typically extends readily to per-agency revenue reporting as well.

## Why Platforms Often Underestimate How Frequently Agency Fare Policies Actually Change

A specific reason this architecture decision deserves more proactive investment than a platform might initially assume necessary: individual transit agencies periodically revise their own fare-capping thresholds and concession structures, often on their own independent schedule tied to municipal budget cycles or service changes, meaning the fare landscape a MaaS platform needs to track is genuinely active rather than a fixed set defined once at integration time. A platform that built its fare architecture assuming each agency's rules at initial integration would remain essentially static risks discovering, as individual agencies adjust their own policies, that its system's fare accuracy needs updating considerably more frequently than an architecture built around a single, fixed per-agency configuration would comfortably support.

This is a specific, practical reason the agency-configurability principle in this article deserves to be treated as an ongoing architectural capability a platform invests in maintaining, not a one-time integration project completed once and considered finished. A platform genuinely serious about sustained multi-agency operation benefits from treating fare-policy monitoring and configuration updates as a standing operational responsibility, with the underlying system architecture specifically designed to make these updates straightforward configuration changes rather than recurring engineering projects each time an agency adjusts its fare policy.

## Why Smaller MaaS Platforms Face This Risk With Less Margin Than Larger Operators

It's worth naming directly that this fare architecture decision carries disproportionate stakes for a smaller, regional MaaS platform compared to a large, well-resourced operator with dedicated fare-policy and compliance staff. A large operator facing a specific agency's fare-policy dispute can typically absorb the cost of a targeted, reactive fix without existential business impact. A smaller platform depending on integration agreements with several agencies has considerably less margin to absorb either a costly reactive rework or the reputational and contractual damage from a public fare-accuracy failure, making the proactive, agency-configurable architecture this article describes a disproportionately valuable investment for exactly the platforms least equipped to absorb a reactive fare crisis after the fact.

## Manifera's Approach: Building Fare Engines With Genuine Agency Configurability

- **Amsterdam (Governance/Fare-Policy-Informed Platform Scoping):** Dutch project leads scope MaaS fare engines around genuine multi-agency fare-policy divergence from the initial design phase, rather than assuming a single uniform fare structure.
- **Vietnam (Execution/Agency-Configurable Fare Engineering):** The dedicated development team builds fare engines with genuinely configurable, agency-specific rulesets, avoiding both rider overcharging and unhonored concession requirements.

This is Dutch Management × Vietnamese Mastery applied to transit fare engine development itself: governance with direct, practical familiarity with fare-policy divergence across transit operators, paired with a dedicated engineering team capable of building genuinely flexible, agency-ready fare infrastructure. Explore Manifera's [software outsourcing](https://www.manifera.com/services/offshore-software-development/) approach for MaaS platforms and transit technology operators.

## Case Study: A Maribor Platform's Fare Engine Correction

Mestni Prevoz Maribor, a Maribor-based transit and mobility platform, had built an initial fare-capping engine around a single, uniform daily-cap and concession implementation, launched successfully covering its home city bus network before integrating several neighboring regional operators with their own distinct cap thresholds and student-discount structures.

Manifera's Vietnam-based dedicated development team rebuilt the fare engine's core architecture around a configurable, agency-specific ruleset, supporting each operator's actual cap accumulation period and concession eligibility rules, alongside reliable trip-to-agency attribution for multi-leg journeys and agency-specific revenue reconciliation, all without requiring separate, parallel fare systems per agency.

> *"We'd built one fare logic and assumed the neighboring operators' rules were close enough to just reuse it. It turned out their actual cap and discount structures were different enough that riders using those routes were being charged incorrectly, and building real per-agency configurability was what let us integrate properly across every operator's actual fare rules instead of approximating them."*
> — **Product Lead, Mestni Prevoz Maribor**

Mestni Prevoz Maribor successfully integrated its additional regional operators with agency-correct fare handling, and now treats fare-policy configurability as a standard architectural requirement for any new agency integration, rather than a single fare logic assumed to generalize across operators.

## Single Hardcoded Fare Logic vs. Agency-Configurable Architecture

| Factor | Single Hardcoded Fare Logic | Agency-Configurable Architecture |
|---|---|---|
| Fare accuracy across agencies | Requires approximating a shared fare structure | Applied per each agency's actual published rules |
| Concession handling | Risk of unhonored agency-specific discounts | Configured per agency's actual eligibility criteria |
| Response to an agency's policy change | Requires platform-wide rework | Configuration update within existing architecture |
| Revenue reconciliation | Difficult to attribute accurately per agency | Tracked accurately per agency's actual fare data |

## Scoping Your Own MaaS Platform's Fare Engine for Multi-Agency Accuracy

Before integrating a MaaS platform across multiple transit agencies, architect the fare engine around genuinely configurable, agency-specific rulesets — a single hardcoded fare logic forces an unnecessary trade-off between rider overcharging and unhonored concessions. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about building a fare engine ready for genuine multi-agency accuracy.

## Frequently Asked Questions

### (Scenario: product lead scoping a multi-agency fare engine) Why does fare-capping and concession policy vary meaningfully across transit agencies?

Each agency independently sets its own cap thresholds, accumulation periods, and concession eligibility rules, creating genuine divergence a multi-agency MaaS platform's fare engine needs to accommodate.

### (Scenario: platform worried about rider trust) What's the risk of building a fare engine around a single, uniform fare-logic implementation?

It forces a choice between overcharging riders relative to a specific agency's actual cap or failing to honor a specific agency's required concessions, a real risk that has led to rider complaints and agency contract disputes.

### (Scenario: engineering lead scoping agency configurability) Is a simple per-agency price multiplier sufficient to handle fare-capping differences across operators?

Not usually — fare-capping logic accumulates across trips within a rolling period and concession eligibility depends on rider verification, meaning the system needs genuinely configurable fare-calculation logic, not just a configurable price.

### (Scenario: finance lead reviewing technical architecture) Why does reliable trip-to-agency attribution matter for fare accuracy?

Correctly applying agency-specific fare rules depends on accurately identifying which agency's service a specific trip used, a determination that carries real technical nuance for multi-agency, multi-leg journeys.

### (Scenario: platform planning for future agency policy changes) Why should a fare engine be designed to accommodate each agency's fare-policy changes independently?

Agencies periodically revise their own fare thresholds and concession structures on independent schedules, and a system requiring platform-wide rework for each change creates real ongoing operational risk.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: product lead scoping a multi-agency fare engine) Why does fare-capping and concession policy vary meaningfully across transit agencies?", "acceptedAnswer": { "@type": "Answer", "text": "Each agency independently sets its own cap thresholds, accumulation periods, and concession eligibility rules." } },
    { "@type": "Question", "name": "(Scenario: platform worried about rider trust) What's the risk of building a fare engine around a single, uniform fare-logic implementation?", "acceptedAnswer": { "@type": "Answer", "text": "It forces a choice between overcharging riders under one agency's rules or failing to honor another agency's required concessions." } },
    { "@type": "Question", "name": "(Scenario: engineering lead scoping agency configurability) Is a simple per-agency price multiplier sufficient to handle fare-capping differences across operators?", "acceptedAnswer": { "@type": "Answer", "text": "Not usually — fare-capping accumulates across trips and concessions depend on verification, requiring genuinely configurable fare logic." } },
    { "@type": "Question", "name": "(Scenario: finance lead reviewing technical architecture) Why does reliable trip-to-agency attribution matter for fare accuracy?", "acceptedAnswer": { "@type": "Answer", "text": "Applying agency-specific rules correctly depends on identifying which agency's service a trip used, a nuance for multi-leg journeys." } },
    { "@type": "Question", "name": "(Scenario: platform planning for future agency policy changes) Why should a fare engine be designed to accommodate each agency's fare-policy changes independently?", "acceptedAnswer": { "@type": "Answer", "text": "Agencies revise fare thresholds on independent schedules, and platform-wide rework for each change creates ongoing operational risk." } }
  ]
}
</script>
