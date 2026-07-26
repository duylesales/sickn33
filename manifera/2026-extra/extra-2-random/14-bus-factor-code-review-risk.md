---
title: "Bus Factor One: When Only One Engineer Understands Your Critical System"
keywords: "custom software developer, custom software development company, custom software development services, custom software engineering, governance software development"
buyer_stage: "Awareness"
target_persona: "CTO"
---

# Bus Factor One: When Only One Engineer Understands Your Critical System

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bus Factor One: When Only One Engineer Understands Your Critical System",
  "description": "A CTO's guide to the bus factor risk created by missing code review culture, where one engineer becomes the sole holder of critical system knowledge and a single resignation threatens business continuity.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/bus-factor-code-review-risk" }
}
</script>

If one two-weeks'-notice email could take down your most critical system, you don't have an engineering team, you have a single point of failure with a LinkedIn profile.

**The Pain:** A CTO's most senior backend engineer — the one who built the billing and entitlements engine three years ago and has quietly maintained it alone ever since — hands in their resignation. Nobody else on the team has ever merged a pull request into that codebase. There's no design doc, no onboarding path, and the exit interview is the first time anyone has asked this engineer to explain how the system actually works.

**The Agitation:** A "bus factor one" system isn't a hypothetical risk, it's a deferred cost with a due date nobody scheduled. Losing the sole owner of a critical system typically forces 8-16 weeks of forensic reverse-engineering before the team can safely ship a change to it again, and mid-market companies commonly spend €60,000-€120,000 in lost velocity, emergency contractor fees, and delayed roadmap items recovering from a single departure that a code review culture would have prevented for the cost of a slower merge queue.

## The Architectural Mandate

Bus factor is a measurable property of a codebase, not a vague morale concern, and it should be tracked with the same rigor as test coverage or deployment frequency. The simplest useful metric is git blame concentration: what percentage of commits to a given service, in the last twelve months, came from a single author? Any critical-path system where one engineer accounts for more than 60-70% of commits, with no substantive review from anyone else, is running at bus factor one whether or not anyone has named it that.

The architectural mandate to fix this isn't "hire more people" — it's mandatory code review with rotation discipline, structured so that knowledge distribution is a forced byproduct of the normal delivery process rather than a separate initiative that competes with sprint work for time. Every pull request into a critical-path system requires at least one reviewer who is not the primary maintainer, and review assignment should rotate deliberately across the team rather than defaulting to whichever senior engineer is fastest to approve. A review culture that always routes PRs to the same one or two people for speed is optimizing for short-term velocity while actively growing the bus factor problem it should be solving.

Pair programming and rotating ownership on high-risk modules is the second lever, and it's underused because it looks like a velocity tax in the sprint it happens, even though it's the cheapest insurance the team will ever buy. A structured rotation — every engineer spends a defined period each quarter working directly in the highest-risk, lowest-bus-factor part of the codebase, paired with the current owner — spreads tacit knowledge (the "why," not just the "what") in a way that documentation alone never fully captures, because a decade of edge-case reasoning rarely survives being written down.

Documentation matters, but it has to be positioned correctly: as a byproduct of the review and rotation process, not a substitute for it. A design doc that nobody but the original author has validated against the real system tends to drift from reality within a few months and becomes actively misleading during an incident. The more durable pattern is documentation-as-you-go, captured as part of the pull request itself — the "why" behind a non-obvious decision recorded at the moment it's made, reviewed by a second engineer who can immediately flag if it doesn't match their understanding.

Finally, this needs an owner at the architecture-governance level, because bus factor risk is invisible in every sprint retro until the day it isn't. A quarterly audit of commit concentration and review coverage across critical-path systems, reported to whoever owns technical risk for the organization, converts bus factor from a thing that gets discovered during an exit interview into a thing that gets managed proactively, the same way a custom software developer would manage any other production risk.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects own the risk audit — measuring commit concentration and review coverage across critical systems — and act as an IP and quality shield ensuring knowledge is never trapped in a single individual.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam operate under mandatory, rotated code review from day one, distributing system knowledge across the team as a built-in property of how the pod works, not an afterthought.

This is Dutch Management × Vietnamese Mastery: governance that treats knowledge concentration as a managed risk, paired with a delivery model where no single engineer is ever the sole holder of critical context. See how [Manifera's offshore software development teams](https://www.manifera.com/services/offshore-software-development/) build review discipline into every pod from kickoff.

## Case Study & Testimonial

### A Lyon Medtech Platform's Single Point of Failure

Corvelia Medtech, a Lyon-based digital health platform, discovered its bus factor problem the hard way: the engineer who had single-handedly built and maintained their patient-matching algorithm for four years left with three weeks' notice. No one else had ever reviewed a line of that code. The CTO spent the notice period trying to extract as much context as possible into hurried documentation, but the first production bug after the departure took the remaining team eleven days to diagnose — a fix that would have taken hours with a second engineer who understood the system.

Manifera was brought in to both stabilize the orphaned system and rebuild the team's review culture going forward. The Amsterdam team audited commit history across all of Corvelia's critical services, surfacing three more modules quietly running at bus factor one before they became emergencies. The Vietnam pod took ownership of the patient-matching algorithm through a structured pairing rotation, rebuilding institutional knowledge across three engineers within six weeks, and instituted mandatory rotated review across every critical-path repository going forward.

> *"We found out we had three more ticking clocks before they went off. Now every critical system has at least three people who actually understand it."*
> — **CTO, Corvelia Medtech**

## Legacy Agency vs. Manifera Pod

| Criteria | Legacy Agency / Bad Practice | Manifera Pod |
|---|---|---|
| Code review | Optional, routed to fastest approver | Mandatory, rotated across the team |
| Knowledge distribution | Concentrated in one senior engineer | Deliberately spread via pairing rotation |
| Bus factor visibility | Untracked until a departure forces the issue | Quarterly audited commit-concentration metric |
| Documentation | Written once, drifts from reality over time | Captured as part of the PR process, continuously validated |
| Departure impact | 8-16 weeks of forensic reverse-engineering | Continuity maintained by design, no single point of failure |
| Risk ownership | No one owns bus factor as a managed risk | Amsterdam governance tracks it as core architecture risk |

## The Economics

A bus factor of one is a liability sitting on the balance sheet with no line item, until the day it's realized as 8-16 weeks of lost velocity, emergency contractor fees to reverse-engineer undocumented systems, and a delayed roadmap that the board will notice even if they never learn the root cause — commonly €60,000-€120,000 in direct and opportunity cost for a single departure at a mid-market company. Mandatory rotated code review costs a fraction of a percent of sprint velocity in exchange for eliminating that liability entirely, which makes skipping it one of the more expensive false economies in software engineering management. [Talk to Manifera](https://www.manifera.com/contact-us/) about auditing your team's bus factor before a resignation letter does it for you.

## Frequently Asked Questions

### (Scenario: CTO who just realized a critical system has a single owner) How do we quickly assess whether we have a bus factor problem?

Pull commit history for your critical-path services over the last twelve months and check what percentage of commits came from a single author with no substantive review from anyone else. Anything above 60-70% concentration on a business-critical system is a bus factor risk worth addressing immediately, regardless of how stable that system currently looks.

### (Scenario: CTO worried mandatory code review will slow the team down) Won't mandatory rotated review just slow down our delivery velocity?

It costs a small, measurable amount of short-term velocity in exchange for eliminating a much larger, unscheduled cost later. Teams that adopt rotated review typically see merge times increase by a small margin while catastrophic knowledge-loss events, which cost far more, become structurally far less likely.

### (Scenario: CTO deciding how to redistribute knowledge from a sole system owner) How do we redistribute knowledge from an engineer who's about to leave?

A structured pairing rotation during the notice period is far more effective than documentation alone — have the departing engineer walk a second engineer through real changes to the live system, not just a knowledge-transfer document, since tacit reasoning rarely survives being written down in the time available.

### (Scenario: CTO trying to decide which systems to prioritize for a bus factor audit) Which systems should we audit first for bus factor risk?

Start with whatever system would cause the most immediate business damage if it broke and nobody could fix it quickly — usually billing, authentication, or core transactional logic — rather than auditing every repository with equal priority.

### (Scenario: CTO building a business case for review-culture investment) How do we justify investing in review culture when nothing has broken yet?

Frame it the same way you'd frame any insurance decision: the cost of mandatory review is small, fixed, and known, while the cost of an unplanned departure from a bus-factor-one system is large, unpredictable, and has already happened to comparable companies in your industry.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO who just realized a critical system has a single owner) How do we quickly assess whether we have a bus factor problem?", "acceptedAnswer": { "@type": "Answer", "text": "Pull commit history for your critical-path services over the last twelve months and check what percentage of commits came from a single author with no substantive review from anyone else. Anything above 60-70% concentration on a business-critical system is a bus factor risk worth addressing immediately." } },
    { "@type": "Question", "name": "(Scenario: CTO worried mandatory code review will slow the team down) Won't mandatory rotated review just slow down our delivery velocity?", "acceptedAnswer": { "@type": "Answer", "text": "It costs a small, measurable amount of short-term velocity in exchange for eliminating a much larger, unscheduled cost later. Teams that adopt rotated review typically see merge times increase slightly while catastrophic knowledge-loss events become structurally far less likely." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding how to redistribute knowledge from a sole system owner) How do we redistribute knowledge from an engineer who's about to leave?", "acceptedAnswer": { "@type": "Answer", "text": "A structured pairing rotation during the notice period is far more effective than documentation alone. Have the departing engineer walk a second engineer through real changes to the live system, since tacit reasoning rarely survives being written down in the time available." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to decide which systems to prioritize for a bus factor audit) Which systems should we audit first for bus factor risk?", "acceptedAnswer": { "@type": "Answer", "text": "Start with whatever system would cause the most immediate business damage if it broke and nobody could fix it quickly, usually billing, authentication, or core transactional logic, rather than auditing every repository with equal priority." } },
    { "@type": "Question", "name": "(Scenario: CTO building a business case for review-culture investment) How do we justify investing in review culture when nothing has broken yet?", "acceptedAnswer": { "@type": "Answer", "text": "Frame it the same way you'd frame any insurance decision: the cost of mandatory review is small, fixed, and known, while the cost of an unplanned departure from a bus-factor-one system is large, unpredictable, and has already happened to comparable companies in your industry." } }
  ]
}
</script>
