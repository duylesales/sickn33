---
title: "Everything to Verify Before a Single Workload Moves to the Cloud"
keywords: "development in cloud, cloud migration, GDPR compliance, euro cloud"
buyer_stage: "Decision"
target_persona: "A"
---

# Everything to Verify Before a Single Workload Moves to the Cloud

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Cloud Migration Checklist Before Moving a Workload",
  "description": "A pre-migration checklist covering data classification, dependency mapping, compliance requirements, rollback planning, and cost modeling before moving a workload to the cloud.",
  "step": [
    { "@type": "HowToStep", "name": "Classify and map data sensitivity", "text": "Identify which data is regulated (GDPR, industry-specific) and where it's legally permitted to be hosted." },
    { "@type": "HowToStep", "name": "Map all workload dependencies", "text": "Document every system the workload connects to, including undocumented integrations that only surface under investigation." },
    { "@type": "HowToStep", "name": "Confirm compliance and data residency requirements", "text": "Verify which cloud regions satisfy GDPR or industry-specific compliance obligations before selecting infrastructure." },
    { "@type": "HowToStep", "name": "Model realistic cloud costs against current usage patterns", "text": "Build a cost projection based on actual traffic and data patterns, not vendor-provided best-case estimates." },
    { "@type": "HowToStep", "name": "Define a rollback plan before migrating", "text": "Establish a tested way to revert if the migration surfaces an unforeseen issue in production." },
    { "@type": "HowToStep", "name": "Plan a staged migration with a pilot workload", "text": "Migrate a lower-risk workload first to validate the process before moving business-critical systems." }
  ]
}
</script>

A cloud migration that goes wrong rarely goes wrong because of the cloud provider itself, whatever an under-pressure postmortem's first instinct tends to blame first. It goes wrong because of an undocumented dependency nobody mapped in advance, a compliance requirement nobody checked against the target region, or a cost model based on the vendor's best-case pricing example rather than the company's own actual usage pattern.

## 1. Classify and Map Data Sensitivity

Before migrating anything at all, identify precisely which data is subject to GDPR, industry-specific regulation, or contractual data residency commitments — and confirm the target cloud region and provider configuration actually satisfies those requirements. Migrating regulated data to a non-compliant region is a mistake that's expensive to unwind after the fact.

## 2. Map All Workload Dependencies

Every system the workload connects to — internal APIs, third-party integrations, scheduled jobs, other services quietly reading from the same database — needs to be documented before migration begins, not discovered mid-cutover. Undocumented dependencies are, empirically, the single most common cause of unexpected breakage during a cloud migration, because a workload that looks entirely self-contained from the outside rarely actually is once its real connections are traced.

## 3. Confirm Compliance and Data Residency Requirements

For European companies specifically, this means carefully verifying which cloud regions actually satisfy GDPR data residency expectations and whether the specific services being used (not just the region) are covered by adequate data processing agreements. A workload correctly and carefully migrated to an EU region can still create real compliance exposure if a specific managed service within that region quietly processes data outside it.

## 4. Model Realistic Cloud Costs Against Current Usage Patterns

Cloud provider cost calculators, by design and by incentive, tend to model best-case, steady-state usage rather than a specific customer's actual traffic and data patterns. Real workloads have traffic spikes, data transfer costs between services, and storage growth that a simplified calculator often understates significantly. Build a cost model from actual historical usage data, not a generic vendor estimate, before committing to a migration budget anyone will be held to.

## 5. Define a Rollback Plan Before Migrating

Every migration should have a genuinely tested way to revert to the previous state if something goes wrong in production — not as a theoretical fallback described in a document nobody has actually tried, but as a concretely planned and, ideally, rehearsed process the team has run at least once before it's needed for real. Migrations without a genuinely rehearsed rollback plan tend, reliably, to turn what would have been a recoverable issue into an extended, customer-visible outage.

## 6. Plan a Staged Migration With a Pilot Workload

Migrate a lower-risk, non-business-critical workload first to validate the entire process end to end, surface unexpected issues while the stakes are still low, and refine the runbook before moving anything customers depend on directly. Full "big bang" migrations of business-critical systems attempted without a pilot phase carry a disproportionate amount of risk relative to the modest amount of time actually saved by skipping it.

## Why a Checklist, Specifically, Is the Right Tool for This

Surgeon and researcher Atul Gawande's 2009 book "The Checklist Manifesto" documented something genuinely counterintuitive about complex, high-stakes work: even world-class experts — surgeons, pilots, engineers — reliably miss steps under pressure or amid unfamiliar complexity, and a simple checklist, followed without exception, measurably reduces those misses in ways that expertise and good intentions alone do not. Gawande's own research, drawing on aviation safety and a WHO-led surgical safety checklist implemented across hospitals internationally, found that checklists work specifically because they don't rely on memory or vigilance under pressure — exactly the two things that degrade most reliably when stakes are high and a deadline is looming.

Cloud migration sits squarely in the category of work this research describes: genuinely complex, involving multiple specialized domains (data governance, networking, compliance, cost modeling) that no single team member holds complete expertise in simultaneously, and frequently executed under real time pressure. This is precisely the combination — complexity plus pressure — where Gawande's research shows unaided expert judgment degrades most predictably, and where a followed-without-exception checklist earns back the most safety relative to its cost.

This also explains why the discipline of following the checklist in order matters more than it might seem to for a team confident in their technical skill. Gawande's research specifically found that experts who felt confident enough to skip checklist items under time pressure were the ones most likely to have a genuine miss — not because they lacked skill, but because confidence and time pressure are exactly the conditions under which memory-dependent processes fail silently. Ferrovia Pay's instinct to skip the dependency-mapping step under deadline pressure, described below, is a close real-world echo of the exact failure pattern Gawande's research identified and that a followed checklist is specifically designed to prevent.

## Manifera's Approach: Migration as a Structured Process, Not an Event

- **Amsterdam (Governance/Compliance):** Dutch architects lead the data classification, dependency mapping, and GDPR compliance verification before any migration begins, with direct experience navigating EU data residency requirements for clients across regulated industries.
- **Vietnam (Execution/Staged Delivery):** The engineering pod executes migrations in staged phases, starting with a pilot workload and maintaining tested rollback capability throughout, rather than attempting a single high-risk cutover.

This is Dutch Management × Vietnamese Mastery applied to cloud migration itself: European compliance rigor paired with disciplined, staged execution that manages risk deliberately. Explore Manifera's [Euro Cloud migration](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) services.

## Case Study: A Turin Fintech's Compliant Migration

Ferrovia Pay, a Turin-based fintech, urgently needed to migrate off a US-hosted infrastructure provider to satisfy a new institutional client's EU data residency requirement, on a compressed timeline that left, on paper, little room for a discovery-heavy process.

Manifera's Amsterdam team insisted on running an accelerated but genuinely complete dependency mapping and compliance verification in the first two weeks, identifying three genuinely undocumented integrations that would have broken silently and unpredictably in a rushed migration. The Vietnam pod executed a genuinely staged migration starting with a reporting workload, then moved core transaction processing only once a tested, rehearsed rollback plan was firmly in place. The full migration completed exactly on the client's original deadline with zero unplanned downtime anywhere along the way.

> *"We were under real time pressure, and the instinct was to skip the mapping step to move faster. That step is exactly what caught the three integrations that would have broken everything."*
> — **CTO, Ferrovia Pay**

Ferrovia's CTO has since introduced a version of the same checklist discipline for other high-stakes engineering work beyond migrations — production deployment sign-offs, incident response — having directly experienced how much a followed checklist recovers under exactly the deadline pressure that makes skipping steps feel most tempting.

## Why "We Know What We're Doing" Isn't a Substitute for the List

The instinct to skip a step under time pressure — "we've done this before, we know what we're doing" — is precisely the instinct Gawande's research identified as the highest-risk moment for an expert team, not the lowest. Confidence born of experience is genuinely valuable for judgment calls the checklist doesn't cover, but it's specifically unreliable for the mechanical, memory-dependent task of confirming that every relevant step has actually been completed under pressure — which is exactly the category of failure a checklist protects against regardless of how experienced the team running it is.

This is why Manifera treats the six-step checklist as followed in full for every migration, rather than as a menu a senior architect can selectively apply based on their read of a given project's risk. The entire point of a checklist, per Gawande's research, is that it doesn't depend on an individual's judgment about which steps matter this time — that judgment is exactly the thing under-pressure experts have been repeatedly found to get wrong, in aviation, in surgery, and in the technical work described throughout this article.

## Migration Risk Reduction Checklist

| Step | Risk If Skipped |
|---|---|
| Data classification | Compliance violation in wrong region |
| Dependency mapping | Silent breakage of undocumented integrations |
| Compliance verification | GDPR or contractual exposure |
| Realistic cost modeling | Budget overrun from underestimated cloud spend |
| Rollback plan | Recoverable issue becomes extended outage |
| Staged pilot migration | Full-scale failure instead of contained, early issue |

## Before You Move Anything

Treat this checklist as sequential and complete, not optional in parts under deadline pressure — each step catches a specific category of risk the others structurally can't, which is exactly why Gawande's research found partial checklist adherence to be little better than none at all. [Talk to Manifera](https://www.manifera.com/contact-us/) about scoping a migration plan for your specific workloads.

## Frequently Asked Questions

### (Scenario: CTO under time pressure to migrate quickly) Can we skip dependency mapping if we're under a tight deadline?

Skipping it under time pressure is exactly when undocumented dependencies are most likely to cause an unplanned outage — an accelerated mapping process is safer than skipping it entirely, even on a compressed timeline.

### (Scenario: CTO trying to estimate migration cost accurately) Why do cloud costs often come in higher than the provider's calculator suggested?

Provider calculators typically model steady-state, best-case usage and often underrepresent data transfer costs between services and traffic spikes — build your cost model from actual historical usage data instead.

### (Scenario: European company evaluating cloud regions) What's the biggest GDPR mistake companies make during cloud migration?

Assuming that choosing an EU cloud region alone guarantees compliance, without verifying that every specific managed service used within that region also keeps data processing within the required jurisdiction.

### (Scenario: CTO deciding whether a pilot migration is worth the extra time) Is a pilot migration worth the extra time if we're confident in our plan?

Yes — even a well-planned migration can surface unexpected issues, and finding them on a lower-risk pilot workload is far less costly than finding them during a business-critical system's cutover.

### (Scenario: CTO planning for the worst case) What should a rollback plan actually include?

A tested, documented process to revert to the previous infrastructure state, including data synchronization considerations if any writes occurred during the migration window, verified before the migration begins rather than improvised during an incident.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO under time pressure to migrate quickly) Can we skip dependency mapping if we're under a tight deadline?", "acceptedAnswer": { "@type": "Answer", "text": "Skipping it under time pressure is exactly when undocumented dependencies are most likely to cause an outage — an accelerated mapping process is safer than skipping it entirely." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to estimate migration cost accurately) Why do cloud costs often come in higher than the provider's calculator suggested?", "acceptedAnswer": { "@type": "Answer", "text": "Provider calculators typically model steady-state usage and underrepresent data transfer costs and traffic spikes — build your model from actual historical usage." } },
    { "@type": "Question", "name": "(Scenario: European company evaluating cloud regions) What's the biggest GDPR mistake companies make during cloud migration?", "acceptedAnswer": { "@type": "Answer", "text": "Assuming an EU cloud region alone guarantees compliance, without verifying every managed service used also keeps data processing within the required jurisdiction." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding whether a pilot migration is worth the extra time) Is a pilot migration worth the extra time if we're confident in our plan?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — finding unexpected issues on a lower-risk pilot workload is far less costly than finding them during a business-critical cutover." } },
    { "@type": "Question", "name": "(Scenario: CTO planning for the worst case) What should a rollback plan actually include?", "acceptedAnswer": { "@type": "Answer", "text": "A tested, documented process to revert to the previous infrastructure state, including data synchronization considerations, verified before the migration begins." } }
  ]
}
</script>
