---
title: "What Actually Happens Between 'We Signed the Contract' and 'The App Is Live'"
keywords: "software developer stages, stages software development, software development processes, software development cycle"
buyer_stage: "Awareness"
target_persona: "D"
---

# What Actually Happens Between "We Signed the Contract" and "The App Is Live"

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Actually Happens Between 'We Signed the Contract' and 'The App Is Live'",
  "description": "A plain-language walkthrough of the stages of software development for non-technical founders, explaining what happens in each phase and why skipping any of them creates cost later.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/stages-of-software-development-explained" }
}
</script>

A non-technical founder signs a contract expecting a straight line from "yes" to "launched." What actually happens is five distinct stages, each with its own risks, its own timeline, and its own way of quietly going wrong — and understanding them is the difference between managing a project and being managed by one, since a founder who can't name the stages can't ask which one is currently being shortchanged.

## Stage One: Discovery and Requirements

Before any code is written — the cheapest possible point, per the cost-of-change research, to catch a misunderstanding — a real project starts with understanding what's actually being built — interviews with stakeholders, documenting user flows, and identifying technical constraints like existing systems the new software needs to connect to. This stage is invisible to a founder impatient to see progress, which is exactly why it's the stage most commonly rushed or skipped, and exactly why skipping it is the single biggest predictor of later cost overruns, since every misunderstanding it would have caught instead gets carried forward into stages where fixing it costs measurably more.

## Stage Two: Design and Architecture

Two parallel tracks happen here, both still comfortably on the cheap end of the cost-of-change curve: UX/UI design (what users see and interact with) and technical architecture (how the system is structured underneath). A founder typically only sees the first — wireframes, mockups, a clickable prototype — while the second, less visible track determines whether the product can actually scale, integrate with other systems, and stay maintainable as features get added later.

## Stage Three: Development (The Build)

This is the stage most people picture, and often the only stage they picture, when they think "building software" — engineers writing code against the design and architecture from stage two. It's typically broken into sprints, two-to-three-week cycles that each produce a working, demonstrable increment of the product, rather than one long stretch of invisible work followed by a single reveal at the end.

## Stage Four: Quality Assurance and Testing

Code that works on the developer's machine and code that works reliably for real users across different devices, network conditions, and edge cases are not the same thing, and confusing the two is one of the more common ways a project quietly climbs the cost-of-change curve without anyone noticing until later. QA is where that gap gets closed — through manual testing, automated test suites, and cross-device verification — and it's the stage most frequently compressed under deadline pressure, with consequences that surface as bugs after launch instead of before it.

## Stage Five: Deployment and Post-Launch Support

Launch isn't the finish line — it's the point where real user behavior starts revealing what testing, however thorough, structurally couldn't replicate in advance. A defined post-launch stabilization window, typically two to four weeks, is when the team monitors for issues, fixes what surfaces, and hands off into ongoing maintenance. Projects that treat launch as "done" rather than "the next stage begins" tend to accumulate the exact kind of technical debt that becomes measurably more expensive to unwind eighteen months later than it would have been to address at launch.

## Why Skipping a Stage Doesn't Save Time, It Relocates It

Every stage skipped or compressed doesn't disappear from the project — it resurfaces later, usually more expensively, tracing the same cost-of-change pattern software engineering research has documented for decades. Skipped discovery resurfaces as scope disputes during development. Skipped QA resurfaces as production bugs after launch. Skipped post-launch stabilization resurfaces as an emergency fix cycle a month in, under worse pressure than if it had been planned from the start.

## The Research Behind "Catch It Early or Pay More Later"

Software engineering research has documented the cost of catching problems late for decades, under a finding generally known as the cost-of-change curve. Barry Boehm's empirical work on software economics — the same research tradition behind the COCOMO estimation model — found that the cost of fixing a defect rises sharply the later it's discovered in a project's lifecycle: a requirements misunderstanding caught during discovery might cost an hour of conversation to correct, while the same misunderstanding discovered after launch can require rearchitecting already-shipped code, migrating live data, and managing the customer-facing fallout simultaneously. The finding has been revisited and refined many times since Boehm's original work, and the specific multiplier varies by study and context, but the directional pattern — errors get more expensive to fix the later they're caught, often by a wide and non-linear margin — has proven remarkably durable across decades of software projects.

This is the empirical backbone behind why each of the five stages exists as a distinct checkpoint rather than being collapsed into "build it and see." Discovery exists specifically to catch requirements misunderstandings at the cheapest possible point — before any code reflecting the wrong understanding has been written. QA exists to catch implementation defects before they reach production, where the same bug costs substantially more to fix once real users and real data are involved. Post-launch stabilization exists because some issues are, by their nature, only detectable once real usage patterns exist to reveal them — but even there, a defined, actively monitored window catches those issues faster and cheaper than waiting for them to surface as unprompted customer complaints months later.

Understanding this curve reframes why compressing a stage under deadline pressure so often backfires. It isn't that a compressed QA phase saves time and risks a vague, generic "more bugs" outcome — it's that every bug pushed past its cheapest catch point moves up a steep, well-documented cost curve, and a founder compressing QA to save two weeks now is very often trading that for a multiple of those two weeks in post-launch firefighting later, at a point in the project where the cost also includes real damage to user trust that a pre-launch bug never would have caused.

## Manifera's Approach: Five Stages, Visible at Every Step

- **Amsterdam (Governance/Process):** Dutch project leads structure every engagement through all five stages explicitly, with a founder-visible view into each — not just the development stage that happens to be the easiest to demo.
- **Vietnam (Execution/Velocity):** The engineering pod executes each stage without compressing QA or post-launch stabilization under deadline pressure, because those stages are scoped into the timeline from day one rather than treated as flexible.

This is Dutch Management × Vietnamese Mastery applied to process itself: European structural discipline across all five stages, paired with delivery speed that doesn't come from quietly skipping the ones a founder can't see. Learn about [Manifera's way of working](https://www.manifera.com/about-us/our-way-of-working/).

## Case Study: A Prague Marketplace's Compressed Timeline

Trhovna, a Prague-based marketplace startup, had previously worked with an agency that compressed QA from a planned two weeks to three days to hit a launch date — resulting in a payment bug that affected 8% of first-week transactions and required an emergency two-week fix cycle immediately after launch.

For their next major feature, Manifera's Amsterdam team held the full five-stage timeline, including the originally-planned QA window, even under similar deadline pressure. The feature launched on schedule with zero payment-related incidents in the first month.

> *"The agency that skipped QA to hit our date actually cost us more time in the end — the emergency fix cycle took longer than the QA window they cut would have."*
> — **Founder, Trhovna**

Trhovna's engineering team now tracks, informally, which stage any newly discovered bug would have been cheapest to catch in — a habit borrowed directly from the cost-of-change research, used less as a blame exercise and more as a way of deciding where to invest process improvement next.

## The Five Stages at a Glance

| Stage | What Happens | Most Common Mistake |
|---|---|---|
| Discovery | Requirements gathering, stakeholder interviews | Rushed or skipped entirely |
| Design & Architecture | UX/UI design + technical structure | Only UX visible, architecture underinvested |
| Development | Sprint-based code building | Treated as the only "real" stage |
| QA & Testing | Manual + automated verification | Compressed under deadline pressure |
| Deployment & Post-Launch | Launch + stabilization window | Treated as the finish line, not a stage |

## Managing a Project You Can Now See Clearly

Ask any vendor which stages are explicitly scoped into your timeline and budget, and which ones are assumed to happen "in the background." The stages you can't see are the ones most likely to be cut first, and — per the cost-of-change research — the ones whose cutting quietly costs the most once the resulting defects surface downstream. [Download our project scoping guide](https://www.manifera.com/contact-us/) to see all five stages mapped for your specific project.

## Frequently Asked Questions

### (Scenario: non-technical founder confused by a project timeline) Why does the actual build only look like half of my project timeline?

Because discovery, design, QA, and post-launch stabilization are separate stages requiring real time and expertise — the build is often the largest single stage, but rarely the entire timeline.

### (Scenario: founder under pressure to launch faster) Which stage is safest to compress if I need to launch faster?

None are truly safe to compress, but if forced to choose, reducing scope (fewer features) preserves quality better than reducing time spent on QA or post-launch stabilization for the features you do build.

### (Scenario: founder trying to understand a vendor's proposal) How can I tell if a vendor's timeline has properly scoped all five stages?

Ask for the timeline broken out by stage, not just by feature. A proposal that only shows development sprints without dedicated discovery, QA, and stabilization time has likely underscoped those stages.

### (Scenario: founder wondering why bugs appeared after launch) Why do bugs still appear after a project passes QA?

Real-world usage — different devices, network conditions, and user behavior patterns — always surfaces things a QA process, however thorough, can't fully replicate in advance. That's exactly why the post-launch stabilization stage exists.

### (Scenario: founder planning their first software project) What's the most commonly underestimated stage for first-time founders?

Discovery. It produces no visible output — no screens, no working code — which makes it the easiest stage to rush, even though skipping it is the single biggest predictor of scope disputes and cost overruns later.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: non-technical founder confused by a project timeline) Why does the actual build only look like half of my project timeline?", "acceptedAnswer": { "@type": "Answer", "text": "Because discovery, design, QA, and post-launch stabilization are separate stages requiring real time — the build is often the largest single stage, but rarely the entire timeline." } },
    { "@type": "Question", "name": "(Scenario: founder under pressure to launch faster) Which stage is safest to compress if I need to launch faster?", "acceptedAnswer": { "@type": "Answer", "text": "None are truly safe to compress, but reducing scope preserves quality better than reducing time spent on QA or post-launch stabilization." } },
    { "@type": "Question", "name": "(Scenario: founder trying to understand a vendor's proposal) How can I tell if a vendor's timeline has properly scoped all five stages?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for the timeline broken out by stage, not just by feature. A proposal showing only development sprints has likely underscoped discovery, QA, and stabilization." } },
    { "@type": "Question", "name": "(Scenario: founder wondering why bugs appeared after launch) Why do bugs still appear after a project passes QA?", "acceptedAnswer": { "@type": "Answer", "text": "Real-world usage always surfaces things a QA process can't fully replicate in advance, which is exactly why the post-launch stabilization stage exists." } },
    { "@type": "Question", "name": "(Scenario: founder planning their first software project) What's the most commonly underestimated stage for first-time founders?", "acceptedAnswer": { "@type": "Answer", "text": "Discovery. It produces no visible output, which makes it the easiest stage to rush, even though skipping it is the biggest predictor of cost overruns later." } }
  ]
}
</script>
