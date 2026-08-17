---
title: "The Metrics on Your Engineering Dashboard That Don't Actually Predict the Next Outage"
keywords: "software quality, sw quality, software engineer stages, software development processes"
buyer_stage: "Consideration"
target_persona: "A"
---

# The Metrics on Your Engineering Dashboard That Don't Actually Predict the Next Outage

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Metrics on Your Engineering Dashboard That Don't Actually Predict the Next Outage",
  "description": "Which software quality metrics genuinely correlate with production incident rate, and which commonly tracked ones don't, based on how engineering teams actually measure quality.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/software-quality-metrics-production-incidents" }
}
</script>

Test coverage percentage is the metric most engineering dashboards lead with by default, and it's also, reliably, one of the weaker actual predictors of production incident rate — a codebase can hit 90% coverage while testing the wrong things entirely, giving false confidence that's arguably worse than knowing coverage is low.

## Why Test Coverage Percentage Alone Is a Weak Signal

Coverage percentage only measures how much code executes during tests, not whether those tests actually verify meaningful, correct behavior along the way. A test suite can achieve high coverage by exercising code paths without asserting anything meaningful about correct behavior — passing tests that don't actually catch regressions. Coverage is a genuinely useful floor metric (very low coverage is always a real problem worth flagging) but a poor ceiling metric (high coverage never, on its own, guarantees genuine quality).

## Metrics That Correlate More Reliably With Production Incidents

- **Change failure rate** — the percentage of deployments that result in a rollback, hotfix, or genuine incident. This directly and honestly measures what actually matters: does shipped code work reliably in production.
- **Mean time to recovery (MTTR)** — how quickly, in practice, the team actually detects and resolves an incident once it genuinely occurs. A team with a higher incident rate but very fast MTTR may have better overall reliability than a team with fewer incidents that take days to resolve.
- **Code churn concentrated in specific modules** — files that get modified repeatedly in quick succession, sprint after sprint, are a genuinely strong predictor of underlying design problems, more reliable than a static, once-off coverage snapshot.
- **Cyclomatic complexity trends** — code with rapidly growing branching complexity is measurably more defect-prone, independent of how well it's covered by tests.
- **Deployment frequency alongside change failure rate together** — high deployment frequency paired with low change failure rate together indicate a genuinely mature, low-risk delivery process; the two metrics need to be read together, not separately.

## Why These Metrics Predict Better Than Coverage Alone

These metrics measure real outcomes — did the change actually work, how fast did the team genuinely recover, is complexity trending toward unmanageable — rather than a proxy for testing effort. Coverage measures an input (how much code has tests around it); change failure rate and MTTR measure the output that actually matters to the business (does software work reliably for users).

## The Management Fallacy Named After a Defense Secretary

Management researchers have a name for the specific error of over-relying on the easiest-to-measure number available: the McNamara fallacy, named after U.S. Secretary of Defense Robert McNamara, whose Vietnam-era reliance on quantifiable metrics like enemy body counts — chosen because they were measurable, not because they were the metrics that actually predicted the war's outcome — became a widely cited management cautionary tale. The fallacy, as later articulated by social scientist Daniel Yankelovich, unfolds in a specific, recognizable sequence: first, measure whatever can be easily measured; then treat that measurement as if it's the whole picture; then, over time, start disregarding whatever can't be easily quantified as if it doesn't matter, simply because it doesn't fit neatly into the metric already being tracked.

Test coverage percentage is a close engineering analogue to McNamara's body counts: it's genuinely easy to measure, automatically calculated by tooling with no human judgment required, and it produces a single clean number that looks authoritative on a dashboard. None of that makes it the metric that actually predicts what a team cares about — production reliability — the same way a body count, however precisely tallied, never actually measured progress toward the war's stated objectives. A team that optimizes for coverage percentage because it's measurable, the way McNamara's fallacy predicts, ends up in exactly the position Kwarcyt found itself in below: a reassuring number on a dashboard and a production incident every two weeks, with no one having noticed the gap because the easy metric was quietly standing in for the hard, more meaningful question.

Avoiding the McNamara fallacy doesn't mean abandoning measurement — it means resisting the temptation to let ease of measurement determine what gets measured, and instead doing the harder work of finding proxies, like change failure rate and MTTR, that track closer to the outcome that actually matters, even when they require more deliberate tracking infrastructure than a coverage tool that ships built into most testing frameworks by default.

## Manifera's Approach: Measuring What Predicts Reliability, Not What Looks Good on a Slide

- **Amsterdam (Governance/Metrics Strategy):** Dutch project leads track change failure rate, MTTR, and complexity trends alongside coverage, giving clients a realistic picture of production reliability risk rather than a single vanity metric.
- **Vietnam (Execution/Quality Practice):** The engineering pod treats meaningful test assertions and manageable complexity as delivery standards, not just coverage percentage targets that can be gamed without improving actual reliability.

This is Dutch Management × Vietnamese Mastery applied to quality measurement itself: metrics strategy that reflects what genuinely predicts incidents, paired with execution discipline that improves the metrics that matter rather than optimizing the ones that don't. Dashboards built for client visibility surface change failure rate and MTTR trends alongside coverage, specifically so a non-technical stakeholder reviewing engineering health sees the same outcome-based picture the engineering team is actually managing against, rather than a single number that can look reassuring while masking real risk. Learn about Manifera's [QA and testing](https://www.manifera.com/about-us/manifera-technologies/) practices.

## Case Study: A Wrocław SaaS Company's Metric Correction

Kwarcyt, a Wrocław-based SaaS company, had prided itself on 88% test coverage while still experiencing a production incident roughly every two weeks — a disconnect that puzzled the engineering team until an audit found the coverage was concentrated in simple, low-risk utility functions while the complex, frequently changed business logic modules had minimal meaningful test assertions.

Manifera's Amsterdam team introduced change failure rate and code churn tracking alongside coverage, redirecting testing effort toward the specific modules the new metrics flagged as high-risk. Within four months, change failure rate dropped by 60%, even as overall coverage percentage stayed roughly flat.

> *"Our coverage number had made us feel safe. It took a different set of metrics to show us we'd been testing the wrong things the whole time."*
> — **Engineering Manager, Kwarcyt**

Kwarcyt's engineering manager now opens every quarterly review by explicitly naming the McNamara fallacy by name to new team members, treating it as a standing reminder that whatever metric is easiest to pull from a dashboard is not automatically the metric that matters most.

## Asking What's Being Missed, Not Just What's Being Measured

The McNamara fallacy's most useful practical lesson isn't a specific alternative metric to adopt — it's a standing question to keep asking about whatever metrics a team already tracks: what does this number make it easy to stop paying attention to? Coverage percentage made it easy to stop asking whether tests actually verified meaningful behavior, because a rising number felt like sufficient reassurance on its own. Any metric, including change failure rate and MTTR, can eventually suffer the same fate if a team starts treating the number itself as the goal rather than as an imperfect proxy for the underlying reliability that's the actual objective.

This is why Manifera pairs quantitative metrics with a standing practice of qualitative incident review — reading the actual story of what happened in a production incident, not just updating the change-failure-rate counter — specifically to catch the kind of texture and nuance a pure number, however well-chosen, will eventually start to flatten out of the picture. McNamara's own body-count metric might have looked less catastrophically misleading if someone in the chain of command had kept asking, consistently and skeptically, what the number wasn't showing them — the same discipline a software team benefits from applying to its own dashboards, quarter after quarter, indefinitely.

## Metric Reliability Comparison

| Metric | What It Measures | Predictive Value for Incidents |
|---|---|---|
| Test coverage percentage | Code executed during tests | Weak alone, useful as a floor |
| Change failure rate | Deployments resulting in rollback/incident | Strong |
| Mean time to recovery | Speed of incident detection and resolution | Strong |
| Code churn by module | Files repeatedly modified in quick succession | Strong |
| Cyclomatic complexity trend | Branching complexity growth | Moderate-strong |

## Rethinking Your Engineering Dashboard

If test coverage is still the primary quality metric on your team's dashboard, add change failure rate and MTTR alongside it, and keep asking what those numbers might themselves be quietly hiding — the combination gives a far more reliable picture of production reliability than coverage alone ever could. [Talk to Manifera](https://www.manifera.com/contact-us/) about auditing your team's current quality metrics.

## Frequently Asked Questions

### (Scenario: engineering manager relying primarily on coverage percentage) Should we stop tracking test coverage entirely?

No — low coverage is still a meaningful warning sign, but high coverage alone shouldn't be treated as proof of quality. Track it alongside change failure rate and MTTR for a more complete picture.

### (Scenario: CTO trying to explain incident rate to leadership) How do I explain to non-technical stakeholders why our high coverage number hasn't reduced incidents?

Coverage measures testing effort, not testing effectiveness — explain that a test can execute a line of code without meaningfully verifying its correct behavior, which is why outcome-based metrics like change failure rate matter more.

### (Scenario: engineering manager trying to start tracking better metrics) What's the easiest quality metric to start tracking if we're not tracking anything beyond coverage today?

Change failure rate is usually the most straightforward to start with, since it just requires tagging deployments that led to a rollback or hotfix — no new tooling investment required to begin.

### (Scenario: CTO trying to identify which parts of the codebase are actually risky) How do I find which modules in our codebase are the biggest reliability risk?

Track code churn (frequency of modification) combined with defect rate per module — modules that are both frequently changed and frequently buggy are the strongest candidates for focused quality investment.

### (Scenario: engineering manager worried about gaming metrics) Can change failure rate and MTTR be gamed the way coverage sometimes is?

Less easily, since they measure real production outcomes rather than a proxy — though teams should still be alert to under-reporting incidents, which is a process and culture issue rather than a metric-design issue.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: engineering manager relying primarily on coverage percentage) Should we stop tracking test coverage entirely?", "acceptedAnswer": { "@type": "Answer", "text": "No — low coverage is still a meaningful warning sign, but high coverage alone shouldn't be treated as proof of quality." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to explain incident rate to leadership) How do I explain to non-technical stakeholders why our high coverage number hasn't reduced incidents?", "acceptedAnswer": { "@type": "Answer", "text": "Coverage measures testing effort, not effectiveness — a test can execute a line of code without meaningfully verifying its correct behavior." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to start tracking better metrics) What's the easiest quality metric to start tracking if we're not tracking anything beyond coverage today?", "acceptedAnswer": { "@type": "Answer", "text": "Change failure rate is usually the most straightforward to start with, requiring only tagging deployments that led to a rollback or hotfix." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to identify which parts of the codebase are actually risky) How do I find which modules in our codebase are the biggest reliability risk?", "acceptedAnswer": { "@type": "Answer", "text": "Track code churn combined with defect rate per module — modules that are both frequently changed and frequently buggy are the strongest candidates for focused quality investment." } },
    { "@type": "Question", "name": "(Scenario: engineering manager worried about gaming metrics) Can change failure rate and MTTR be gamed the way coverage sometimes is?", "acceptedAnswer": { "@type": "Answer", "text": "Less easily, since they measure real production outcomes, though teams should stay alert to under-reporting incidents." } }
  ]
}
</script>
