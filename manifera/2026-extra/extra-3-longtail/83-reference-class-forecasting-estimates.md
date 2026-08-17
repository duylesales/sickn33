---
title: "The Only Estimating Method That Actually Predicts Software Project Overruns"
keywords: "custom software development cost, mobile app development cost, app development cost, custom software development pricing"
buyer_stage: "Decision"
target_persona: "A"
---

# The Only Estimating Method That Actually Predicts Software Project Overruns

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Estimating a Software Project Using Reference Class Forecasting",
  "description": "A method for producing more accurate software project cost and timeline estimates by grounding them in actual outcomes from similar past projects rather than bottom-up task estimation alone.",
  "step": [
    { "@type": "HowToStep", "name": "Define the reference class", "text": "Identify a category of genuinely comparable past projects, not just projects that sound similar in name." },
    { "@type": "HowToStep", "name": "Gather actual outcome data for that class", "text": "Collect real cost and timeline data from those past projects, including overruns, not just original estimates." },
    { "@type": "HowToStep", "name": "Establish the distribution", "text": "Determine the typical overrun percentage and variance across the reference class." },
    { "@type": "HowToStep", "name": "Apply the distribution to the current estimate", "text": "Adjust the current project's bottom-up estimate using the reference class's actual historical overrun pattern." }
  ]
}
</script>

A software vendor's bottom-up estimate — breaking a project into tasks, estimating each one, and summing the total — feels rigorous because it's detailed and specific. A large body of research on project forecasting suggests this exact method is also one of the most reliably wrong ways to estimate a complex project, for a structural reason that has nothing to do with any individual estimator's skill or honesty.

## Why Bottom-Up Estimates Are Structurally Biased Toward Optimism

A bottom-up estimate asks an engineer to imagine each task going roughly as planned, then sum those individually optimistic imaginings into a total. The problem isn't that any single task estimate is dishonest — it's that the method systematically excludes the kind of unplanned, unforeseeable friction that real projects reliably encounter: an integration that behaves unexpectedly, a requirement that turns out more ambiguous than it looked, a dependency that changes mid-project. No individual task estimate accounts for these, because by definition they're not part of any specific task's plan — they're the emergent friction of a complex project unfolding in reality, and a method that estimates task by task has no natural place to capture that friction at all.

## The Alternative Method Backed by Extensive Research

Economic geographer Bent Flyvbjerg, through several decades of research on megaproject cost overruns beginning in the 1990s and continuing through subsequent large-scale studies, found that bottom-up, inside-view estimates were consistently and predictably optimistic across an enormous range of project types — infrastructure, IT systems, construction — regardless of the specific estimators' expertise or honesty. Flyvbjerg's proposed alternative, reference class forecasting, deliberately ignores the specific details of the project being estimated and instead asks a different question: looking at a class of genuinely comparable past projects, what was the actual, real-world relationship between their original estimates and their final, actual outcomes?

Reference class forecasting works because it sidesteps the exact bias that makes bottom-up estimation unreliable: instead of trying to imagine every possible source of friction a specific project might encounter — an impossible task, since much of that friction is genuinely unforeseeable in advance — it uses the actual, already-realized friction that comparable past projects experienced as a statistical basis for adjustment. If a reference class of comparable software projects historically ran 40% over their original bottom-up estimate on average, that 40% adjustment is applied to the new project's bottom-up number, not because this specific project is expected to encounter exactly the same problems, but because the reference class's actual track record is a more reliable predictor of real-world overrun than any individual project's optimistic, friction-free imagining of its own execution.

## Why This Matters More for Software Than Flyvbjerg's Original Domains

Software projects arguably exhibit the pattern Flyvbjerg documented even more consistently than the physical infrastructure projects his original research focused on, because software requirements are frequently more ambiguous at the outset, dependencies on third-party systems and APIs introduce genuine unknowns that can't be fully specified in advance, and the "unknown unknowns" that reference class forecasting is specifically designed to capture are, if anything, more prevalent in software development than in comparatively more physically constrained construction or infrastructure work.

## What Building a Real Reference Class Actually Requires

- **Genuine comparability, not superficial similarity** — a reference class should be defined by real structural factors (complexity, integration count, team size, domain novelty), not just a shared label like "mobile app" that can span wildly different actual scopes.
- **Real historical outcome data, not just original estimates** — the whole method depends on knowing what actually happened to past projects, including their actual overruns, not just what they were originally quoted at.
- **A large enough reference class to be statistically meaningful**, since a reference class of two or three past projects doesn't provide the kind of reliable distribution the method depends on to be genuinely more accurate than a bottom-up guess.
- **Willingness to apply the adjustment even when it feels uncomfortably large**, since the entire value of the method comes from overriding the optimistic bottom-up number with the reference class's actual track record, not from softening the adjustment to feel more palatable.

## Why Flyvbjerg Found Skill and Honesty Weren't the Explanation

One of the more striking findings across Flyvbjerg's body of research is what didn't explain the overrun pattern: it wasn't concentrated among less experienced estimators, and it wasn't primarily explained by deliberate lowballing to win a bid, though both factors do contribute at the margins in some cases. The pattern showed up consistently even among experienced, well-intentioned professionals estimating in good faith, which is precisely what makes the finding structurally important rather than a simple call for more careful or more honest estimators. A more careful bottom-up estimate is still a bottom-up estimate, subject to the same fundamental blind spot regardless of how much additional care goes into each individual task's number.

This finding has a direct, somewhat uncomfortable implication for how a founder should read a vendor's confident, detailed estimate: the detail and apparent rigor of a bottom-up breakdown says very little about its ultimate accuracy, because the method's core weakness isn't a matter of effort or diligence — it's structural, built into what bottom-up estimation is actually capable of capturing in the first place. A founder impressed by a vendor's meticulous task breakdown is responding to a signal that, per Flyvbjerg's research, doesn't actually correlate with the estimate's real-world accuracy, which is exactly why asking for the reference-class-adjusted number alongside it matters more than scrutinizing the bottom-up breakdown's apparent thoroughness.

## Manifera's Approach: Estimating From Real Track Record, Not Just Task Breakdown

- **Amsterdam (Governance/Reference-Class-Informed Estimates):** Dutch project leads maintain and apply real historical outcome data from comparable past projects when producing estimates, adjusting bottom-up numbers against actual track record rather than presenting an optimistic, unadjusted total.
- **Vietnam (Execution/Consistent Delivery Data):** The engineering pod's consistent project execution generates the reliable historical outcome data that makes a genuine reference class forecasting approach possible in the first place.

This is Dutch Management × Vietnamese Mastery applied to estimation itself: governance that grounds estimates in real historical outcomes rather than optimistic task breakdowns alone, paired with execution consistent enough to make that historical data genuinely meaningful. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach to project estimation.

## Case Study: A Larnaca Company's Recalibrated Estimate

Larnaca Digital Freight had received a bottom-up estimate from a previous vendor for a customs documentation platform, presented with specific task-by-task detail that made the total feel rigorously calculated. The project ultimately ran 65% over that original estimate, a pattern the company later learned was close to typical for projects of that specific complexity profile across the industry, not a result of anything unusual about their specific project.

For a subsequent related project, Manifera's Amsterdam team applied reference class forecasting directly, presenting both a bottom-up estimate and a reference-class-adjusted range based on actual historical outcomes from comparable past integration-heavy projects. The adjusted range, while initially uncomfortable to see, proved close to the project's actual final cost, a meaningfully more accurate prediction than a bottom-up number alone would have provided.

> *"The detailed task-by-task estimate the first time felt more trustworthy because it was more specific. It was also completely wrong, in a completely predictable direction, and knowing that in advance the second time changed how we budgeted from the start."*
> — **Operations Director, Larnaca Digital Freight**

Larnaca Digital Freight now specifically asks any vendor for a reference-class-adjusted estimate alongside a bottom-up one, treating a vendor's willingness and ability to provide real historical outcome data as a meaningful evaluation criterion in its own right, separate entirely from how detailed or professionally formatted the accompanying task breakdown happens to look.

## Bottom-Up vs. Reference Class Forecasting

| Method | Basis | Typical Accuracy for Complex Projects |
|---|---|---|
| Bottom-up estimation | Task-by-task optimistic imagining | Systematically optimistic, unreliable |
| Reference class forecasting | Actual historical outcomes of comparable projects | More accurate, grounded in real track record |
| Ideal combined approach | Bottom-up estimate adjusted by reference class data | Most accurate available method |

## A Simple Test to Run Before Accepting Any Estimate

A practical way to apply this framework without necessarily needing a vendor to have formal reference class data on hand: ask directly what percentage, on average, the vendor's past projects of comparable complexity actually ran over their original bottom-up estimates, and ask for that number before seeing the current project's specific breakdown, not after. A vendor with a genuine, honest track record can usually answer this, at least approximately, and a vendor who can't or won't is implicitly asking a founder to trust a bottom-up number with no real-world adjustment behind it at all, which the research suggests is close to the least reliable version of an estimate available.

## Requesting a More Reliable Estimate for Your Own Project

Before accepting a detailed bottom-up estimate at face value, ask your vendor for a reference-class-adjusted range based on actual outcomes from comparable past projects — specificity in an estimate isn't the same as accuracy. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about getting a reference-class-informed estimate for your project.

## Frequently Asked Questions

### (Scenario: CTO reviewing a detailed bottom-up estimate) Why would a detailed, task-by-task estimate still be unreliable?

Because bottom-up estimation systematically excludes unforeseeable friction — ambiguous requirements, integration surprises, dependency changes — that doesn't belong to any single task's plan but reliably affects real projects anyway.

### (Scenario: founder trying to get a more accurate cost estimate) What should I ask a vendor for instead of just a bottom-up estimate?

Ask for a reference-class-adjusted estimate based on actual historical outcomes from genuinely comparable past projects, not just the vendor's optimistic task-by-task breakdown.

### (Scenario: CTO skeptical that past projects predict a new one) How can outcomes from different past projects predict a specific new project's cost?

The method doesn't claim the new project will encounter identical problems — it uses the reference class's actual overrun pattern as a statistically grounded adjustment, since unforeseeable friction reliably occurs across comparable projects even though its specific form varies.

### (Scenario: founder trying to evaluate whether a vendor's reference class is legitimate) How do I know if a vendor's reference class is genuinely comparable to my project?

Ask what specific factors define the class — complexity, integration count, domain novelty — rather than accepting a superficial label like "similar app" as sufficient grounds for comparability.

### (Scenario: engineering manager building internal estimation practice) How can we start applying reference class forecasting to our own project estimates?

Track actual outcomes, not just original estimates, across your own past projects, and build reference classes from that real data over time — the method depends on having genuine historical outcome data available to draw from.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO reviewing a detailed bottom-up estimate) Why would a detailed, task-by-task estimate still be unreliable?", "acceptedAnswer": { "@type": "Answer", "text": "Bottom-up estimation systematically excludes unforeseeable friction that doesn't belong to any single task's plan but reliably affects real projects." } },
    { "@type": "Question", "name": "(Scenario: founder trying to get a more accurate cost estimate) What should I ask a vendor for instead of just a bottom-up estimate?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for a reference-class-adjusted estimate based on actual historical outcomes from genuinely comparable past projects." } },
    { "@type": "Question", "name": "(Scenario: CTO skeptical that past projects predict a new one) How can outcomes from different past projects predict a specific new project's cost?", "acceptedAnswer": { "@type": "Answer", "text": "It uses the reference class's actual overrun pattern as a statistically grounded adjustment, since unforeseeable friction reliably occurs across comparable projects." } },
    { "@type": "Question", "name": "(Scenario: founder trying to evaluate whether a vendor's reference class is legitimate) How do I know if a vendor's reference class is genuinely comparable to my project?", "acceptedAnswer": { "@type": "Answer", "text": "Ask what specific factors define the class — complexity, integration count, domain novelty — rather than accepting a superficial label as sufficient." } },
    { "@type": "Question", "name": "(Scenario: engineering manager building internal estimation practice) How can we start applying reference class forecasting to our own project estimates?", "acceptedAnswer": { "@type": "Answer", "text": "Track actual outcomes, not just original estimates, across your own past projects, and build reference classes from that real data over time." } }
  ]
}
</script>
