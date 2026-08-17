---
title: "You Don't Have to Rewrite the Whole System to Start Replacing the Worst Part of It"
keywords: "custom software development, custom software solution, bespoke software development services, software product"
buyer_stage: "Decision"
target_persona: "C"
---

# You Don't Have to Rewrite the Whole System to Start Replacing the Worst Part of It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Modernizing a Legacy System Using the Strangler Fig Pattern",
  "description": "A step-by-step approach to replacing a legacy system incrementally, module by module, instead of committing to a risky full rewrite.",
  "step": [
    { "@type": "HowToStep", "name": "Identify the highest-risk or highest-friction module", "text": "Find the specific part of the legacy system causing the most pain, rather than planning a full rewrite." },
    { "@type": "HowToStep", "name": "Build a new version of that module in isolation", "text": "Develop the replacement independently, alongside the still-running legacy system." },
    { "@type": "HowToStep", "name": "Route traffic to the new module incrementally", "text": "Redirect specific functionality to the new module while the legacy system continues handling the rest." },
    { "@type": "HowToStep", "name": "Retire the replaced legacy portion", "text": "Once the new module is proven stable, decommission the corresponding legacy code." },
    { "@type": "HowToStep", "name": "Repeat for the next highest-priority module", "text": "Continue the cycle until the legacy system has been fully replaced, module by module." }
  ]
}
</script>

An IT manager facing a legacy system nobody wants to touch is usually presented with two options that both sound frightening: keep patching an increasingly fragile system indefinitely, or commit to a full rewrite that carries genuine, well-documented risk of running over budget, over time, or failing outright before it ever reaches feature parity with what it's replacing. There's a well-established third option that avoids both extremes, and it's been in active use in the software industry for over two decades.

## The Pattern That Avoids the All-or-Nothing Choice

Software architect Martin Fowler named this approach the "strangler fig" pattern in a 2004 article, borrowing the metaphor from a type of fig tree that grows around a host tree, gradually taking over its structure until the original host is no longer needed and can be removed, with the fig having assumed its former role and shape by that point. Applied to software, the strangler fig pattern means building a new system incrementally around the edges of an old one — routing specific pieces of functionality to new, properly built modules one at a time, while the legacy system continues handling everything not yet replaced — rather than attempting a single, all-at-once cutover from old to new.

## Why This Avoids the Specific Failure Mode of Full Rewrites

A full rewrite carries a specific, well-documented risk: the new system has to reach full feature parity with the old one before it can safely replace it, which means the organization runs both systems' full development cost simultaneously for the entire rewrite period, while gaining zero incremental value until the very end, when the cutover finally happens all at once. If the rewrite runs over budget or over time — which large rewrites do with striking regularity — the organization is stuck maintaining the old system indefinitely while also funding an increasingly expensive, unfinished replacement, a genuinely dangerous position that has ended several well-funded modernization efforts before they ever reached completion.

The strangler fig pattern avoids this specific trap because value is delivered incrementally, module by module, rather than all at once at a distant finish line. Each module that gets successfully migrated and retired from the legacy system is a real, banked improvement, independent of whether every other module ever gets migrated at all. If the effort needs to pause partway through — a change in business priorities, a budget constraint, anything — the organization is left with a partially modernized system that's still a meaningful improvement over where it started, rather than two half-finished systems and none of the value either was supposed to deliver.

## How to Actually Choose the First Module to Migrate

- **Start with the highest-friction module**, not necessarily the largest one — the part of the system generating the most support tickets, the most fragile part everyone's afraid to touch, or the part most directly blocking a genuine business priority.
- **Choose a module with a relatively clean, definable boundary**, since the pattern works best where a piece of functionality can be isolated and routed to independently, rather than a module deeply entangled with everything else in the system.
- **Avoid starting with the module carrying the highest risk if something goes wrong**, at least for the first migration — building organizational confidence in the pattern with a lower-stakes early success makes the harder migrations later considerably easier to get support for.
- **Plan the routing mechanism before starting development**, since how traffic gets directed to old versus new code is as much a part of the pattern as the new module itself, and retrofitting routing logic after the fact is considerably harder than designing it in from the start.

## Why the Routing Layer Is the Part Most Teams Underestimate

Fowler's original description of the pattern emphasized something teams new to the approach frequently underweight: the routing mechanism that decides, for any given request, whether it goes to the old system or the new module isn't a minor implementation detail — it's arguably the most architecturally important part of the entire pattern, since it's what makes incremental migration possible at all rather than forcing an all-or-nothing cutover by default. A poorly designed routing layer, bolted on as an afterthought once a team has already started building new modules, tends to reintroduce exactly the kind of entanglement the pattern is supposed to avoid, making each subsequent module migration harder rather than easier as the pattern's benefits erode.

A well-designed routing layer, by contrast, treats the decision of "old system or new module" as a clean, centralized, easily adjustable piece of infrastructure — ideally one that can redirect traffic gradually, monitor the new module's behavior against the old system's known-good output during a transition period, and roll back quickly if something in the new module doesn't behave as expected once it starts handling real production traffic. This is precisely why planning the routing mechanism before writing the first line of the first new module's code, not after, is the specific implementation detail that determines whether a team gets the pattern's full benefit or ends up with a harder, more entangled version of the same migration problem they were trying to avoid in the first place.

## Manifera's Approach: Modernizing Incrementally Without Betting the Whole System

- **Amsterdam (Governance/Incremental Modernization Planning):** Dutch project leads plan legacy modernization using the strangler fig pattern by default where a system's architecture allows it, sequencing module migrations to deliver real value early rather than requiring a client to wait for a single, distant full-rewrite finish line.
- **Vietnam (Execution/Careful Migration Discipline):** The engineering pod builds new modules alongside a still-running legacy system, with careful routing and rollback planning at each incremental step, minimizing disruption to a business's ongoing operations throughout the modernization.

This is Dutch Management × Vietnamese Mastery applied to legacy modernization itself: governance that sequences migration for early, real value delivery, paired with execution that manages the incremental cutover carefully at each step. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach to legacy modernization.

## Case Study: A Coimbra Insurer's Incremental Rebuild

Mondego Seguros, a Coimbra-based insurer, had a fifteen-year-old claims processing system considered too risky to touch directly but too central to the business to leave unmaintained indefinitely. A previous vendor had proposed a full rewrite, estimated at fourteen months, which internal leadership ultimately rejected after reviewing the risk of running both systems in parallel for over a year with no incremental value delivered until the very end.

Manifera's Amsterdam team proposed a strangler fig approach instead, starting with the claims intake module — the system's highest-friction component, generating the most support tickets and blocking a specific business priority around faster initial claims processing. The Vietnam pod built and routed the new intake module within ten weeks, delivering a real, immediate improvement while the rest of the legacy system continued operating unchanged.

> *"The full rewrite proposal asked us to bet everything on a fourteen-month finish line. This let us bank a real win in ten weeks and decide about the next module with actual evidence in hand, not just a plan."*
> — **CTO, Mondego Seguros**

Mondego Seguros has since migrated three additional modules using the same incremental pattern, each decision informed by the real, delivered results of the module before it, rather than a single upfront commitment made before any part of the new system existed. The CTO specifically credits the routing layer built during the first migration — designed deliberately before any new module code was written — with making each subsequent migration progressively easier rather than harder.

## Full Rewrite vs. Strangler Fig Pattern

| Factor | Full Rewrite | Strangler Fig Pattern |
|---|---|---|
| Value delivery | All at once, at the end | Incremental, module by module |
| Risk if paused | Two unfinished systems, no benefit | Partial modernization, real value banked |
| Parallel running cost | Full duration of the rewrite | Only during each module's migration |
| Organizational confidence | Requires upfront full commitment | Builds incrementally with each success |

## Knowing When to Stop, Not Just When to Start

An underappreciated benefit of the incremental approach is that it also gives an organization a genuine, evidence-based stopping point that a full rewrite structurally cannot offer. After several modules have been successfully migrated, a team can reasonably ask whether the remaining legacy components are actually worth modernizing at all, or whether they've reached a point of diminishing returns where the remaining legacy code is stable, low-risk, and cheap enough to maintain that further migration isn't worth the cost. A full rewrite commits an organization to finishing what it started, since a half-finished rewrite is close to worthless. A strangler fig migration lets that same organization stop rationally, informed by real evidence from each completed step, exactly when the remaining work stops being worth its cost.

## Applying the Pattern to Your Own Legacy System

Before committing to a full rewrite of a legacy system, identify its highest-friction module and evaluate whether an incremental, strangler fig approach could deliver real value sooner with meaningfully less risk. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about modernizing your legacy system incrementally.

## Frequently Asked Questions

### (Scenario: IT manager weighing a full rewrite against incremental modernization) When does the strangler fig pattern make more sense than a full system rewrite?

When the legacy system's architecture allows functionality to be isolated into distinct modules, and when the organization wants to avoid the risk of running parallel systems for an extended period with no value delivered until the very end.

### (Scenario: CTO trying to choose which module to migrate first) How do I decide which part of a legacy system to modernize first?

Start with the highest-friction module — the part generating the most support burden or most directly blocking a business priority — ideally one with a relatively clean, isolatable boundary from the rest of the system.

### (Scenario: IT director worried about running two systems at once) Doesn't running the old and new systems simultaneously create its own risk?

Some, but contained to each specific module's migration period rather than the entire system for the whole modernization effort, which is meaningfully less risk exposure than a full rewrite's much longer parallel-running period.

### (Scenario: founder wondering if this pattern always applies) Does the strangler fig pattern work for every type of legacy system?

It works best where functionality can be reasonably isolated into distinct modules with definable boundaries — a system that's deeply entangled with no clean separation points is harder to migrate incrementally and may need a different approach.

### (Scenario: CTO trying to estimate the full modernization timeline) How long does a full strangler fig modernization typically take compared to a rewrite?

It varies by system complexity, but the total calendar time can be comparable to or longer than a rewrite — the key difference isn't total time, it's that real value gets delivered incrementally throughout, rather than only at a single distant finish line.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: IT manager weighing a full rewrite against incremental modernization) When does the strangler fig pattern make more sense than a full system rewrite?", "acceptedAnswer": { "@type": "Answer", "text": "When the system's architecture allows functionality to be isolated into modules, avoiding the risk of running parallel systems with no value delivered until the end." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to choose which module to migrate first) How do I decide which part of a legacy system to modernize first?", "acceptedAnswer": { "@type": "Answer", "text": "Start with the highest-friction module with a relatively clean, isolatable boundary from the rest of the system." } },
    { "@type": "Question", "name": "(Scenario: IT director worried about running two systems at once) Doesn't running the old and new systems simultaneously create its own risk?", "acceptedAnswer": { "@type": "Answer", "text": "Some, but contained to each module's migration period rather than the entire system for the whole effort." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if this pattern always applies) Does the strangler fig pattern work for every type of legacy system?", "acceptedAnswer": { "@type": "Answer", "text": "It works best where functionality can be isolated into distinct modules with definable boundaries." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to estimate the full modernization timeline) How long does a full strangler fig modernization typically take compared to a rewrite?", "acceptedAnswer": { "@type": "Answer", "text": "Total calendar time can be comparable, but real value is delivered incrementally throughout rather than only at one distant finish line." } }
  ]
}
</script>
