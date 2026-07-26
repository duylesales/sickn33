---
title: "What the Board Actually Wants to Know About Engineering Velocity"
keywords: "director of software development, software at scale, governance software development, custom software development company"
buyer_stage: "Awareness"
target_persona: "VP of Engineering"
---

# What the Board Actually Wants to Know About Engineering Velocity

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What the Board Actually Wants to Know About Engineering Velocity",
  "description": "An awareness-stage article for a VP of Engineering and director of software development on why most engineering KPI reports fail to answer what the board actually wants to know.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/engineering-kpi-board-reporting" }
}
</script>

A board slide showing "347 story points shipped this quarter" tells a director exactly nothing about whether the money spent on engineering is being spent well — and most VPs of Engineering only discover that the hard way, mid-meeting, when a board member asks the follow-up question the slide can't answer.

**The Pain:** A director of software development at a Series B company has spent two days building a velocity report for the quarterly board meeting — burndown charts, sprint completion rates, story points per engineer. A board member asks a simple question: "Is engineering spend proportional to what we're shipping toward revenue?" Nobody on the slide has an answer, because the metrics were built to describe engineering activity, not business outcomes.

**The Agitation:** A board that can't get a straight answer on engineering ROI starts asking a more dangerous question: should we be spending this much on engineering at all? Vague or activity-based reporting has led boards at comparable Series B and C companies to mandate 15-20% engineering budget cuts based on incomplete information, cuts that a director with outcome-based metrics could often have avoided by demonstrating the actual return being generated — money and headcount lost not because the work wasn't valuable, but because nobody could prove it.

## The Architectural Mandate

Boards don't care about story points, sprint velocity, or lines of code, and reporting built around those metrics fails structurally, not cosmetically. A director of software development or VP of Engineering needs a reporting architecture built around four board-legible categories: throughput toward business outcomes, cost efficiency, risk exposure, and predictability. Everything else is internal engineering telemetry that belongs in a team dashboard, not a board deck.

The first category is outcome-linked throughput: what percentage of engineering capacity went toward roadmap items directly tied to revenue, retention, or a stated strategic bet, versus maintenance, incident response, and unplanned work. A board wants to know if the org is building toward the strategy it approved, and "we shipped a lot" doesn't answer that — "62% of capacity went to the three initiatives you approved, 38% went to keeping the lights on, here's the trend" does.

The second category is cost efficiency expressed in business terms: cost per shipped outcome, not cost per engineer or cost per story point. This requires connecting engineering spend — including any software at scale infrastructure costs and outsourcing spend — to specific delivered initiatives, which most engineering orgs can't do because their time-tracking and their roadmap live in different systems that were never designed to talk to each other.

The third category is risk exposure: technical debt trend, security posture, and single-points-of-failure (bus factor, vendor concentration, compliance gaps), reported as a trend line, not a point-in-time reassurance. A board that hears "everything's fine" every quarter until a major incident has no ability to price the risk it's been implicitly carrying — the mandate is a quarterly risk trend that a non-technical director can read without translation.

The fourth category is predictability: how accurate were last quarter's delivery estimates, and what's driving the variance. This is the category most reports omit entirely because it's the most uncomfortable one, but it's also the single number a board uses to calibrate how much to trust every other number in the deck. A director who proactively reports estimate accuracy — even when it's bad — builds more board trust than one who only reports good news and gets caught flat when a "surprise" slip happens anyway.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch delivery architects design the board-reporting framework — translating engineering activity into outcome, cost, risk, and predictability metrics a non-technical director can act on.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam instrument delivery telemetry at the source, tagging work against roadmap initiatives so the reporting layer reflects reality rather than retrofitted estimates.

This is Dutch Management × Vietnamese Mastery: governance that speaks the board's language, backed by a delivery team producing the underlying data with enough discipline to trust it. See how [Manifera's offshore software development teams](https://www.manifera.com/services/offshore-software-development/) instrument delivery for governance-grade reporting.

## Case Study & Testimonial

### A Brussels SaaS Platform's Board Confidence Turnaround

Novantia Cloud, a Brussels-based vertical SaaS platform, had a director of software development whose quarterly board updates consisted entirely of sprint velocity charts. After two quarters of unexplained slowdown, the board proposed a 20% engineering budget cut on the assumption that spend had simply outpaced output, with no data to argue otherwise.

Manifera rebuilt the reporting framework around the four board-legible categories, retagging six months of historical delivery data against roadmap initiatives to show that 70% of the "slowdown" was capacity absorbed by an unplanned security remediation the board had never been informed carried engineering cost. Armed with outcome-linked throughput and a risk trend line, the director presented a revised case at the next board meeting; the proposed cut was withdrawn, and a smaller, targeted reallocation was approved instead.

> *"For the first time, the board and I were looking at the same numbers and drawing the same conclusion."*
> — **Director of Software Development, Novantia Cloud**

## Legacy Agency vs. Manifera Pod

| Criteria | Legacy Agency / Bad Practice | Manifera Pod |
|---|---|---|
| Reported metric | Story points, velocity charts | Outcome-linked throughput and cost efficiency |
| Risk visibility | Point-in-time reassurance | Quarterly risk trend line |
| Predictability | Omitted or only reported when good | Estimate accuracy reported consistently |
| Cost attribution | Cost per engineer | Cost per shipped business outcome |
| Board trust trajectory | Erodes after first "surprise" | Builds through consistent, honest trend data |

## The Economics

A board reporting failure is rarely about the numbers being wrong — it's about the numbers being unanswerable, and an unanswerable question at the board level gets resolved with a blunt instrument: a budget cut applied uniformly rather than a targeted fix informed by data. A Series B or C company that takes an unnecessary 15-20% engineering budget cut based on incomplete reporting doesn't just lose the headcount, it loses the roadmap capacity that headcount represented, often €500,000-€1.5M in annual engineering spend redirected or eliminated based on a story that better reporting would have corrected. Building a governance-grade reporting layer costs a small fraction of a single mismanaged budget cycle. [Talk to Manifera](https://www.manifera.com/contact-us/) about building board-ready engineering reporting before your next quarterly update.

## Frequently Asked Questions

### (Scenario: VP of Engineering preparing a board update) What metrics should actually be on a board slide about engineering?

Outcome-linked throughput, cost per shipped initiative, a risk trend line, and delivery predictability — not sprint velocity or story points, which describe engineering activity but don't answer whether spend is proportional to business results.

### (Scenario: director of software development facing a proposed budget cut) How do we push back on a board-mandated engineering cut with data?

Show outcome-linked throughput broken down by initiative, including unplanned work like security remediation or incident response that consumed capacity without appearing on any roadmap slide. Most proposed cuts are based on an incomplete picture that better attribution corrects.

### (Scenario: VP of Engineering wanting to report risk without alarming the board) How do we report technical risk without sounding like an excuse machine?

Report it as a consistent quarterly trend line rather than a one-off warning — a board that sees risk tracked over time can calibrate its response, while a sudden disclosure after months of silence reads as either negligence or panic.

### (Scenario: VP of Engineering deciding what to omit from a board deck) Should sprint-level metrics ever go in front of the board?

Generally no — sprint velocity and story points belong in team-level dashboards. The board needs the four business-legible categories; anything more granular should be available on request, not presented as the headline.

### (Scenario: VP of Engineering building this reporting for the first time) Can Manifera help us build this reporting framework without taking over our delivery process?

Yes, Manifera can design and instrument a board-reporting framework as a standalone engagement, connecting existing delivery data to outcome, cost, risk, and predictability metrics independent of any broader outsourcing decision.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: VP of Engineering preparing a board update) What metrics should actually be on a board slide about engineering?", "acceptedAnswer": { "@type": "Answer", "text": "Outcome-linked throughput, cost per shipped initiative, a risk trend line, and delivery predictability, not sprint velocity or story points, which describe engineering activity but don't answer whether spend is proportional to business results." } },
    { "@type": "Question", "name": "(Scenario: director of software development facing a proposed budget cut) How do we push back on a board-mandated engineering cut with data?", "acceptedAnswer": { "@type": "Answer", "text": "Show outcome-linked throughput broken down by initiative, including unplanned work like security remediation or incident response that consumed capacity without appearing on any roadmap slide." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering wanting to report risk without alarming the board) How do we report technical risk without sounding like an excuse machine?", "acceptedAnswer": { "@type": "Answer", "text": "Report it as a consistent quarterly trend line rather than a one-off warning, a board that sees risk tracked over time can calibrate its response, while a sudden disclosure after months of silence reads as either negligence or panic." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering deciding what to omit from a board deck) Should sprint-level metrics ever go in front of the board?", "acceptedAnswer": { "@type": "Answer", "text": "Generally no, sprint velocity and story points belong in team-level dashboards. The board needs the four business-legible categories; anything more granular should be available on request, not presented as the headline." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering building this reporting for the first time) Can Manifera help us build this reporting framework without taking over our delivery process?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Manifera can design and instrument a board-reporting framework as a standalone engagement, connecting existing delivery data to outcome, cost, risk, and predictability metrics independent of any broader outsourcing decision." } }
  ]
}
</script>
