---
title: "DevOps Development in Sneek: Finishing a Stalled Containerization"
keywords: "devops development, containerization migration, Docker Kubernetes, two environments, Sneek"
buyer_stage: "Consideration"
target_persona: "CTO"
---

# DevOps Development in Sneek: Finishing a Stalled Containerization

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DevOps Development in Sneek: Finishing a Stalled Containerization",
  "description": "A Sneek-based platform started migrating to containers eight months ago and never finished, leaving two incompatible environments running side by side. Here is the devops development plan to close the gap.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/devops-development-sneek" }
}
</script>

Picture two ships built from the same blueprint, except one was finished in steel and the other is still half wood — and your engineers are expected to sail both, simultaneously, forever.

**The Pain:** A CTO at a Sneek-based marine and watersports-technology platform — a natural fit for a town built around Sneekweek and the Frisian lakes' boating industry — kicked off a Docker and Kubernetes migration eight months ago. It got roughly halfway: about 60% of services now run in containers, orchestrated cleanly, while the remaining 40% still run on the original hand-configured VMs they were meant to replace. The migration stalled when the engineer driving it moved to a different priority project, and nobody has since owned finishing it.

**The Agitation:** The company is now paying the full operational cost of running two incompatible infrastructure paradigms at once, with none of the benefit of having finished either. Deployment tooling, monitoring, and scaling all work differently depending on which half of the system you're touching, which means every engineer needs to hold two mental models simultaneously and onboarding new hires takes noticeably longer. The VM-based half has already caused two scaling incidents during the summer boating season traffic spike — the exact kind of load event Kubernetes' autoscaling was originally meant to solve — costing an estimated 14 hours of combined downtime and manual firefighting during the platform's highest-revenue weeks of the year.

## The Architectural Mandate

A half-finished containerization migration is worse than not starting one, because it combines the operational complexity of running two systems with the benefit of neither. The fix is not "start over" — most of the architectural thinking from the first 60% is usually sound — it's a disciplined, prioritized completion plan rather than an open-ended background task nobody owns.

The first step is an honest inventory: which services remain on VMs, why they stalled (often it's a specific piece of legacy tooling, a stateful component nobody wanted to touch, or missing test coverage that made engineers nervous about the cutover), and what dependencies exist between the containerized and non-containerized halves. Services with hidden statefulness — file storage, session handling, background job queues — are almost always the ones left behind in a stalled migration, precisely because they're the hardest part.

From there, each remaining service gets containerized with Docker, deployed into the existing Kubernetes cluster behind a defined cutover plan: run in parallel with the VM version, validate behavior under real traffic via canary routing, then decommission the VM once confidence is established. This is meaningfully different from the "big bang" approach that stalled the first attempt — completing a migration in small, individually-verified increments is what actually gets it over the finish line, because each increment delivers value on its own rather than requiring the whole project to be done before anything is usable.

Critically, the CI/CD pipeline needs to be unified across both halves during the transition, so engineers aren't maintaining two separate deployment processes on top of two separate runtime environments. A single GitHub Actions or GitLab CI pipeline that can deploy to either target, with the eventual goal of deploying to only one, keeps the team's cognitive load bounded while the migration completes.

For a Sneek-based platform whose traffic is sharply seasonal — quiet in winter, intense during summer boating season — finishing the Kubernetes migration isn't optional polish. Autoscaling is precisely the capability the VM-based half of the system lacks, and the summer traffic spike is exactly when that gap costs the most.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Manifera's Dutch architects assess the stalled migration, define a prioritized, risk-ranked completion plan, and own the cutover strategy for the highest-risk remaining services.
- **Vietnam (Execution/Velocity):** Autonomous Pods in Ho Chi Minh City do the containerization work service by service, validate each cutover under real traffic, and decommission legacy VMs once confidence is established.

This reflects a bridge between European business standards and APAC development velocity — Amsterdam ensures nothing is rushed into production unsafely, Ho Chi Minh City ensures the backlog actually gets finished. Explore our approach on the [cloud migration services page](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/).

## Case Study & Testimonial

### The Mobility Platform Stuck Between Two Worlds

Kilkenny Mobility, a transport-tech company based in Dublin, Ireland, had a Kubernetes migration that stalled at roughly half complete for over a year after the original migration lead left the company. The unfinished state meant their ride-scheduling service — the most business-critical, and also the most stateful — remained on legacy VMs, while newer services ran cleanly in containers, leaving engineers maintaining two deployment playbooks for every release.

Manifera's Autonomous Pod completed a full audit of the remaining services, prioritized the stateful scheduling service first given its business criticality, and executed a phased cutover with canary validation over twelve weeks. The legacy VM environment was fully decommissioned, and the team consolidated onto a single CI/CD pipeline for the first time in over a year.

> *"We'd been living with one foot in each world for so long it felt normal. Finishing the migration removed a tax on every single release we didn't realize we were still paying."*
> — **CTO, Kilkenny Mobility, Dublin**

## Half-Migrated Containers vs. Manifera Completion

| Criteria | Stalled Migration (Bad Practice) | Manifera Completion |
|---|---|---|
| Infrastructure state | Two incompatible environments running in parallel indefinitely | Single, unified Kubernetes-based environment |
| Deployment tooling | Two separate playbooks depending on the service | One unified CI/CD pipeline |
| Scaling under load | VM half cannot autoscale; manual firefighting during spikes | Kubernetes autoscaling across all services |
| Onboarding new engineers | Must learn two operational models | One consistent model to learn |
| Ownership | Nobody owns finishing it | Prioritized, risk-ranked completion plan with clear ownership |

## The Economics

A stalled migration is a uniquely wasteful state, because the company is paying full price for infrastructure complexity while collecting none of the operational benefit that was the point of migrating in the first place. Maintaining two deployment paradigms typically adds 15-25% overhead to every release and every onboarding process indefinitely, for as long as the migration stays unfinished — a permanent tax with no offsetting return. Add seasonal-load incidents like the ones a Sneek-based summer-traffic platform experiences on its un-migrated half, and the cost of staying stuck often exceeds the cost of finishing the job outright within a single peak season.

Most stalled containerization migrations can be completed in eight to twelve weeks once someone actually owns the finish line. If your infrastructure has been half-migrated for longer than a quarter, the fastest way to stop paying for two systems is to finish building one. Talk to Manifera about completing the migration: [www.manifera.com/contact-us/](https://www.manifera.com/contact-us/).

## Frequently Asked Questions

### (Scenario: CTO who inherited a stalled migration from a previous engineer) How do we figure out why the migration stalled in the first place before restarting it?

We start with a service-by-service audit that identifies exactly which components remain on legacy infrastructure and why — usually revealing a specific technical blocker like statefulness or missing test coverage rather than a lack of effort, which tells us exactly where to focus first.

### (Scenario: Engineering leader worried about a second failed attempt) What makes this completion effort more likely to succeed than the first attempt that stalled?

Unlike an open-ended background migration with no dedicated owner, Manifera treats the remaining work as a scoped, prioritized project with a dedicated pod and a defined finish line, which is usually the missing ingredient in migrations that stall.

### (Scenario: Sneek-based platform with sharply seasonal traffic) Should we prioritize finishing the migration before or after our peak season?

If a stateful or high-traffic service is still on legacy infrastructure, we generally recommend completing that specific cutover before peak season, since that's exactly when the autoscaling gap causes the most damage — and finishing outside peak season is lower-risk for less time-sensitive services.

### (Scenario: Team nervous about touching the hardest, most stateful remaining services) Are stateful services like file storage or job queues harder to containerize safely?

Yes, which is exactly why they're usually the ones left unfinished. Manifera prioritizes these with parallel-run validation and canary cutover specifically because they carry more risk, rather than leaving them for "later" indefinitely.

### (Scenario: Leadership wants to know the real timeline) How long does it typically take to complete a stalled migration that's roughly half done?

Most half-finished migrations of this scale complete in eight to twelve weeks, depending on how many stateful or complex services remain and how much test coverage already exists to validate each cutover safely.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO who inherited a stalled migration from a previous engineer) How do we figure out why the migration stalled in the first place before restarting it?", "acceptedAnswer": { "@type": "Answer", "text": "We start with a service-by-service audit that identifies exactly which components remain on legacy infrastructure and why — usually revealing a specific technical blocker like statefulness or missing test coverage rather than a lack of effort, which tells us exactly where to focus first." } },
    { "@type": "Question", "name": "(Scenario: Engineering leader worried about a second failed attempt) What makes this completion effort more likely to succeed than the first attempt that stalled?", "acceptedAnswer": { "@type": "Answer", "text": "Unlike an open-ended background migration with no dedicated owner, Manifera treats the remaining work as a scoped, prioritized project with a dedicated pod and a defined finish line, which is usually the missing ingredient in migrations that stall." } },
    { "@type": "Question", "name": "(Scenario: Sneek-based platform with sharply seasonal traffic) Should we prioritize finishing the migration before or after our peak season?", "acceptedAnswer": { "@type": "Answer", "text": "If a stateful or high-traffic service is still on legacy infrastructure, we generally recommend completing that specific cutover before peak season, since that's exactly when the autoscaling gap causes the most damage — and finishing outside peak season is lower-risk for less time-sensitive services." } },
    { "@type": "Question", "name": "(Scenario: Team nervous about touching the hardest, most stateful remaining services) Are stateful services like file storage or job queues harder to containerize safely?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, which is exactly why they're usually the ones left unfinished. Manifera prioritizes these with parallel-run validation and canary cutover specifically because they carry more risk, rather than leaving them for 'later' indefinitely." } },
    { "@type": "Question", "name": "(Scenario: Leadership wants to know the real timeline) How long does it typically take to complete a stalled migration that's roughly half done?", "acceptedAnswer": { "@type": "Answer", "text": "Most half-finished migrations of this scale complete in eight to twelve weeks, depending on how many stateful or complex services remain and how much test coverage already exists to validate each cutover safely." } }
  ]
}
</script>
