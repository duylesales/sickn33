---
title: "Adding More Developers Doesn't Speed Up Every Phase of a Project Equally"
keywords: "team of developers, application development team, software dev team, application developers"
buyer_stage: "Consideration"
target_persona: "A"
---

# Adding More Developers Doesn't Speed Up Every Phase of a Project Equally

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Adding More Developers Doesn't Speed Up Every Phase of a Project Equally",
  "description": "How team size requirements actually change across a software project's phases, and why adding developers to a stalled project often makes things worse, not better.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/how-many-developers-project-needs-by-phase" }
}
</script>

"We're behind schedule, let's add more developers" is one of the most intuitive-sounding and consistently least reliable fixes in software delivery. The famous, well-documented observation that adding people to an already-late software project frequently makes it later still isn't a quirky, isolated exception — it reflects a real, genuinely predictable dynamic about how team size requirements actually shift and evolve across a project's distinct phases.

## Why Team Size Needs Aren't Constant Across a Project

Discovery and architecture phases specifically benefit from a small, tightly focused team — too many people directly involved in defining requirements and architecture creates real coordination overhead that measurably slows decision-making down rather than speeding it up. Development phases can genuinely benefit from more parallel hands, provided the work has been broken into independent enough pieces. QA and stabilization phases have their own optimal team size, often smaller and more specialized than the development phase that preceded them.

## Why Adding Developers Mid-Project Often Backfires

New developers joining a project need onboarding time to understand existing architecture and decisions, temporarily reducing the productivity of the existing team members who have to provide that onboarding. If the work hasn't been architected with clean enough separation between components, adding people doesn't parallelize the remaining work — it just adds coordination overhead on top of a bottleneck that more people can't actually resolve, because the constraint isn't hands, it's the sequential nature of some remaining work or a specific technical unknown that more people don't help solve faster.

## What Actually Determines the Right Team Size at Each Phase

- **Discovery/architecture**: typically 1-2 senior people, since the work is primarily judgment and synthesis, which doesn't parallelize well across more people.
- **Core development**: scales with how independently the remaining work can be divided — a team of 3-5 is common for a standard-complexity project, more if the architecture genuinely supports parallel workstreams.
- **QA/stabilization**: often 1-2 dedicated testers plus the ability to pull in the original developers for specific fixes, rather than a large team, since this phase requires focus and consistency more than raw capacity.
- **Ongoing maintenance**: frequently much smaller than the peak development team, sized to the actual rate of new issues and feature requests rather than the original build capacity.

## Why This Matters for Budget and Timeline Conversations

A founder assuming a constant team size across a project's entire full duration either meaningfully overestimates budget for phases that genuinely need fewer people, or seriously underestimates the real coordination cost of adding people to an already-struggling project expecting it to simply go proportionally faster. Understanding clearly that the right team size genuinely changes by phase leads to both more accurate, realistic budgeting and a more grounded response when a project eventually falls behind its original schedule.

## The Research Behind the Intuition

Computer scientist Fred Brooks documented this dynamic formally in his 1975 book *The Mythical Man-Month*, drawn from his own experience managing IBM's OS/360 project, in what's since become known as Brooks's Law: adding manpower to a late software project makes it later. Brooks's underlying reasoning was twofold. First, work has to be divisible for more people to help at all — software tasks with genuine sequential dependencies, where one step's output is required before the next can begin, don't speed up no matter how many additional people are assigned, because there's no way to divide a strictly sequential chain of work among more hands. Second, and just as important, adding people to an existing project increases communication overhead combinatorially, not linearly — a team of n people has roughly n(n-1)/2 potential communication pathways, so each additional person adds a disproportionately growing coordination burden on everyone already working, on top of the direct time cost of onboarding the new arrival.

Brooks's Law isn't a blanket claim that more people never help — it's a claim about a specific, common situation: a project already behind schedule, where the remaining work has real sequential dependencies, and where new people need meaningful ramp-up time before contributing productively. This is precisely the situation many founders find themselves in when a project slips and the instinctive response is to add headcount, and it's exactly why diagnosing the actual bottleneck first, as this article recommends, matters more than defaulting to Brooks's era-defining but frequently half-remembered conclusion as though it settles every staffing question on its own.

## Manifera's Approach: Right-Sizing the Team by Phase, Not Defaulting to a Fixed Headcount

- **Amsterdam (Governance/Phase Planning):** Dutch project leads plan team composition explicitly by project phase during scoping, rather than assuming a fixed team size throughout, and diagnose the actual cause of a delay before recommending more headcount as a fix.
- **Vietnam (Execution/Flexible Team Composition):** The engineering pod scales team composition by phase, with architecture built specifically to support genuine parallelization during development where team size increases are actually productive.

This is Dutch Management × Vietnamese Mastery applied to team sizing itself: phase-aware planning paired with execution flexibility that scales team composition appropriately rather than defaulting to a constant headcount. Explore Manifera's [dedicated team](https://www.manifera.com/services/offshore-software-development/) structuring approach.

## Case Study: A Basel Company's Diagnosed Delay

Rheinformatik, a Basel-based logistics tech company, was six weeks behind schedule on an internal platform and requested doubling the development team to catch up, assuming more hands would proportionally increase speed.

Manifera's Amsterdam team diagnosed the actual bottleneck first: a specific undocumented legacy integration that required sequential investigation by one or two people, not something more developers could parallelize. Rather than doubling headcount, the team added one senior integration specialist to that specific bottleneck while keeping the rest of the team stable, avoiding the onboarding drag a full team doubling would have introduced.

> *"Our instinct was 'behind schedule means we need more people.' The actual fix was one specific person solving one specific problem, not a bigger team solving the wrong problem faster."*
> — **CTO, Rheinformatik**

The CTO now explicitly asks, before any headcount request, whether the remaining work is genuinely divisible among more people or fundamentally sequential — a direct, deliberate application of Brooks's original reasoning rather than a purely instinctive response to schedule pressure.

## Recognizing When More People Actually Would Help

Brooks's Law is frequently invoked as a blanket argument against ever adding people to a project, which overstates what Brooks himself claimed. The genuinely useful diagnostic question is whether the remaining work can be divided into pieces with minimal interdependency — if a development phase has several genuinely independent features left to build, each ownable by a different person without constant coordination, additional developers can meaningfully increase throughput. The Rheinformatik case was different specifically because the bottleneck was one undocumented, sequential integration, not a divisible backlog of independent features, which is exactly why a specialist addressing that specific constraint outperformed a broader headcount increase that Brooks's framework would have predicted wouldn't help.

## Optimal Team Composition by Phase

| Phase | Typical Team Size | Why |
|---|---|---|
| Discovery/architecture | 1-2 senior people | Judgment-heavy work, doesn't parallelize |
| Core development | 3-5, scales with parallelizable work | Benefits from genuine independent workstreams |
| QA/stabilization | 1-2 dedicated, plus developer support | Requires focus and consistency, not raw capacity |
| Ongoing maintenance | Smaller than peak build team | Sized to actual issue/request rate |

## Applying the Divisibility Test to Your Own Delay

A practical version of Brooks's diagnostic that a founder or CTO can run without deep technical background: ask the team to describe the remaining work as a list of discrete pieces, then ask specifically how many of those pieces could genuinely be worked on in parallel by different people right now, versus how many depend on another piece finishing first. A remaining-work list dominated by parallel-capable pieces is a genuine candidate for added headcount to help. A remaining-work list dominated by sequential dependencies is exactly the situation Brooks's Law describes, and additional people are more likely to slow the effort down through onboarding drag and coordination overhead than to speed it up.

This same divisibility question is worth asking proactively during initial project planning, not only once a project has already slipped — architecting work with genuine parallelizability in mind from the outset is what makes "add more developers" a viable lever later, if a schedule pressure genuinely calls for it, rather than a reflexive response that backfires because the underlying work was never structured to support it.

## Diagnosing Before Adding Headcount

Before adding developers to a delayed project, diagnose the actual bottleneck first — the fix is sometimes a specific specialist addressing a specific constraint, not a proportional headcount increase across the board. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about right-sizing your team by phase.

## Frequently Asked Questions

### (Scenario: CTO whose project has fallen behind schedule) Should we add more developers if our project is running behind schedule?

Not automatically — first diagnose the actual bottleneck. If it's a specific technical unknown or a sequential dependency, more developers may not help and could add onboarding overhead that makes things temporarily worse.

### (Scenario: founder scoping a new project's budget) How should I think about team size when budgeting a new software project?

Plan for team composition to change by phase — a smaller team for discovery and architecture, a larger one for development if the work genuinely parallelizes, and a smaller, focused team for QA and stabilization — rather than assuming one constant headcount throughout.

### (Scenario: CTO trying to understand why doubling a team didn't double speed) Why didn't doubling our development team roughly double our delivery speed?

Because new team members need onboarding time that temporarily reduces existing team productivity, and if the remaining work isn't cleanly parallelizable, more people add coordination overhead without proportionally increasing throughput.

### (Scenario: engineering manager trying to plan for QA capacity) Does QA and stabilization typically need fewer people than development?

Often yes, though it depends on project complexity — QA benefits more from focus and consistency in a smaller dedicated team than from a large team, unlike development work that can sometimes genuinely parallelize with more people.

### (Scenario: CTO trying to identify the right time to add a specialist) How do I know if a delay needs a specialist added versus a broader headcount increase?

If the delay traces to a specific technical unknown or bottleneck, a targeted specialist addressing that specific issue is usually more effective than a broad headcount increase across the whole team.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO whose project has fallen behind schedule) Should we add more developers if our project is running behind schedule?", "acceptedAnswer": { "@type": "Answer", "text": "Not automatically — first diagnose the actual bottleneck. More developers may not help and could add onboarding overhead." } },
    { "@type": "Question", "name": "(Scenario: founder scoping a new project's budget) How should I think about team size when budgeting a new software project?", "acceptedAnswer": { "@type": "Answer", "text": "Plan for team composition to change by phase, rather than assuming one constant headcount throughout." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to understand why doubling a team didn't double speed) Why didn't doubling our development team roughly double our delivery speed?", "acceptedAnswer": { "@type": "Answer", "text": "New team members need onboarding time, and if remaining work isn't cleanly parallelizable, more people add coordination overhead instead of throughput." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to plan for QA capacity) Does QA and stabilization typically need fewer people than development?", "acceptedAnswer": { "@type": "Answer", "text": "Often yes — QA benefits more from focus and consistency in a smaller dedicated team than from a large team." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to identify the right time to add a specialist) How do I know if a delay needs a specialist added versus a broader headcount increase?", "acceptedAnswer": { "@type": "Answer", "text": "If the delay traces to a specific technical unknown, a targeted specialist is usually more effective than a broad headcount increase." } }
  ]
}
</script>
