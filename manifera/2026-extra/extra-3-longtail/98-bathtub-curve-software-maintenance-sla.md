---
title: "Software Failures Follow a Predictable Curve, and Most SLAs Are Written for the Wrong Part of It"
keywords: "software quality, software services, custom software development, software development processes"
buyer_stage: "Decision"
target_persona: "C"
---

# Software Failures Follow a Predictable Curve, and Most SLAs Are Written for the Wrong Part of It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Failures Follow a Predictable Curve, and Most SLAs Are Written for the Wrong Part of It",
  "description": "Why software failure rates follow a predictable pattern borrowed from reliability engineering, and why most maintenance SLAs are structured around only one phase of that pattern.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/bathtub-curve-software-maintenance-sla" }
}
</script>

An IT manager negotiating a software maintenance SLA typically focuses the entire conversation on just one single number: guaranteed response time for a reported issue. A well-established reliability engineering model suggests that number, while genuinely important, addresses only one specific phase of a system's actual failure pattern over its life — and the phase most maintenance SLAs are structured around isn't always the phase where the most consequential risk actually lives.

## Why Failure Rate Isn't Constant Over a System's Life

An intuitive but inaccurate mental model treats a system's failure rate as roughly constant throughout its operational life — bugs happen at some steady background rate, and a maintenance SLA's job is simply to respond quickly whenever one occurs. Real systems, in both physical reliability engineering and, with some adaptation, software specifically, tend to follow a considerably more specific pattern: failure rate is elevated early in a system's life, drops and stabilizes at a lower rate during a long middle period, then rises again as the system ages — a pattern that requires meaningfully different management approaches at each phase, not a single, uniform response-time guarantee applied identically throughout.

## The Reliability Engineering Model Behind This Pattern

The "bathtub curve," a standard model in reliability engineering used across manufacturing, electronics, and mechanical systems since at least the mid-twentieth century, describes exactly this three-phase failure pattern, named for the shape of the resulting graph: a high "infant mortality" failure rate early in a product's life, driven by manufacturing defects or design flaws that surface quickly under real use; a long, low, stable "useful life" period once early defects have been found and fixed; and a rising "wear-out" phase later in the product's life as components genuinely degrade from accumulated use. The model has been adapted extensively to software reliability engineering, with some modification — software doesn't physically wear out the way mechanical components do, but an analogous pattern holds for different underlying reasons.

In software specifically, the "infant mortality" phase reflects new code's genuinely higher defect density before real-world usage has surfaced and fixed the bugs that inevitably exist in freshly written code, regardless of how careful the original development process was. The "useful life" phase reflects a mature, well-tested system with most easily-discoverable bugs already found and fixed, producing a genuinely lower steady-state failure rate. The "wear-out" phase in software reflects something different from mechanical wear: accumulated technical debt, an aging architecture increasingly mismatched to evolved requirements, and dependencies on outdated, decreasingly-supported components — a real, measurable rise in failure rate driven by accumulated maintenance debt rather than physical degradation, but a rise nonetheless, following the same basic curve shape the physical model describes.

## Why Most SLAs Are Structured for the Middle Phase Only

A standard maintenance SLA — guaranteed response time, defined severity tiers, monthly uptime targets — is implicitly designed around the assumptions of the useful-life phase: a relatively low, stable failure rate that a consistent, steady-state support process can handle predictably. This works reasonably well during that middle phase, which is precisely why it's become the default SLA template across the industry. It works considerably less well during the infant-mortality phase right after a major release, when failure rate is genuinely elevated and a steady-state response process may be under-resourced for the actual volume of issues surfacing, and it works even less well during the wear-out phase, when the SLA's standard response-time guarantee says nothing about the accumulating structural risk that's actually driving the rising failure rate, a risk a fast response time doesn't address at its root cause.

## What an SLA Structured Around the Full Curve Actually Requires

- **Elevated support capacity and tighter monitoring immediately following any major release**, explicitly acknowledging the infant-mortality phase rather than applying the same steady-state resourcing assumption used during stable periods.
- **Standard, predictable response-time SLA terms for the mature, useful-life phase**, since this is genuinely where a consistent, steady-state process is the right fit, matching the standard industry SLA template reasonably well.
- **A periodic architecture health assessment, not just incident response metrics, for aging systems**, since the wear-out phase's rising failure rate reflects structural debt a fast response time can manage symptom by symptom but can't actually resolve.
- **Explicit SLA terms distinguishing these phases**, rather than a single flat response-time guarantee applied uniformly regardless of where a system actually sits on its own failure curve.

## Why Software's Wear-Out Phase Is Actually More Manageable Than Hardware's

An important, genuinely encouraging distinction between the bathtub curve's original mechanical context and its software adaptation is worth naming directly: a physical component's wear-out phase reflects genuine, largely irreversible material degradation — a bearing wears down, a component fatigues, and no amount of maintenance short of replacement actually reverses that trajectory. Software's wear-out phase, by contrast, reflects accumulated technical debt and architectural mismatch, which, unlike physical wear, is genuinely reversible through deliberate investment — refactoring, modernization, targeted architectural rework can meaningfully lower a software system's failure curve back toward useful-life levels in a way no maintenance program can do for a mechanically worn-out physical component.

This distinction is precisely why the periodic architecture health assessment matters more than a physical-world equivalent might: it's not just a monitoring mechanism to detect an otherwise inevitable decline, it's a genuine intervention point where a wear-out trajectory can actually be corrected rather than merely managed until eventual replacement becomes unavoidable. A maintenance strategy that only monitors for rising failure rates, without using that information to trigger corrective architectural investment, is capturing half of what makes software's version of the bathtub curve genuinely more manageable than its mechanical original.

## Manifera's Approach: SLA Structures Matched to Where a System Actually Sits on the Curve

- **Amsterdam (Governance/Phase-Aware SLA Design):** Dutch project leads structure maintenance agreements with explicit provisions for elevated post-release support and periodic architecture health reviews, rather than a single flat SLA template applied regardless of a system's actual life phase.
- **Vietnam (Execution/Responsive Across All Phases):** The engineering pod scales support capacity around major releases and conducts genuine architecture health assessments for aging systems, addressing both the response-time and structural-risk dimensions the bathtub curve identifies.

This is Dutch Management × Vietnamese Mastery applied to maintenance strategy itself: governance that structures SLA terms around a system's actual failure-curve phase, paired with execution that addresses both incident response and underlying structural risk. Explore Manifera's approach to [custom software development](https://www.manifera.com/services/custom-software-development/) and ongoing maintenance.

## Case Study: A Nicosia Retailer's Restructured Maintenance Agreement

Lefkosia Retail Group, a Nicosia-based retail technology company, had operated under a standard flat-rate maintenance SLA with a previous vendor that performed reasonably well for years during its platform's stable middle life, but proved inadequate twice: once during a major release when a surge of new issues overwhelmed the steady-state support capacity the SLA had been resourced for, and again years later when the platform's aging architecture began generating a rising rate of failures the standard response-time SLA managed reactively without ever addressing the accumulating structural cause.

Manifera's Amsterdam team, engaged for a maintenance strategy reset, restructured the agreement explicitly around the bathtub curve's three phases: temporarily elevated support capacity scheduled around any major release, standard steady-state terms for normal operation, and a semi-annual architecture health assessment specifically designed to catch and address wear-out-phase structural risk before it manifested as a rising incident rate.

> *"Our old SLA treated every point in the system's life the same way. It turned out the two times we actually got hurt were exactly the two phases that template was never designed for."*
> — **IT Director, Lefkosia Retail Group**

Lefkosia Retail Group now evaluates any new maintenance agreement explicitly against all three curve phases, rather than assuming a standard flat-rate SLA template adequately covers a system's entire operational life, and specifically requires that any architecture health assessment finding be paired with a corrective investment plan, not just a monitoring report.

## SLA Structure Across the Three Failure Phases

| Phase | Failure Pattern | What a Matched SLA Requires |
|---|---|---|
| Infant mortality (post-release) | Elevated, decreasing failure rate | Temporarily elevated support capacity |
| Useful life (mature, stable) | Low, steady failure rate | Standard response-time SLA terms |
| Wear-out (aging system) | Rising failure rate from accumulated debt | Periodic architecture health assessment |

## Structuring Your Own Maintenance Agreement Around the Full Curve

Before accepting a standard, flat-rate maintenance SLA, ask directly whether it accounts for the elevated risk immediately following a major release and the rising structural risk of an aging system, not just steady-state response time alone. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about a maintenance agreement matched to your system's actual life phase.

## Frequently Asked Questions

### (Scenario: IT manager whose SLA underperformed right after a major release) Why did our standard maintenance SLA feel inadequate right after a major release?

Standard SLAs are typically resourced for a system's stable, mature failure rate, not the elevated "infant mortality" failure rate that follows a major release — a mismatch the bathtub curve model explains directly.

### (Scenario: CTO managing an aging system with rising incidents) Why do we keep seeing more incidents as our system gets older, despite a consistent maintenance SLA?

An aging system's rising failure rate, driven by accumulated technical debt and outdated dependencies, reflects the "wear-out" phase of the bathtub curve — a structural issue a response-time SLA manages reactively but doesn't actually resolve at its root.

### (Scenario: IT director trying to restructure a maintenance agreement) What should a maintenance SLA include beyond a standard response-time guarantee?

Provisions for elevated support capacity around major releases and periodic architecture health assessments for aging systems, addressing the phases where a standard steady-state response-time guarantee alone is insufficient.

### (Scenario: founder wondering if this applies to a young, newly launched product) Does the bathtub curve apply to a brand-new software product, or only older systems?

Yes, from the start — a newly launched product is squarely in the infant-mortality phase, which is exactly why elevated support capacity matters most immediately after any major release or initial launch specifically.

### (Scenario: engineering manager trying to detect the wear-out phase early) How can we tell if our system has entered the wear-out phase before incident rates rise substantially?

A periodic architecture health assessment — evaluating technical debt accumulation and dependency currency directly — can surface wear-out risk before it manifests as a rising incident rate, rather than waiting for the failure rate itself to reveal the problem.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: IT manager whose SLA underperformed right after a major release) Why did our standard maintenance SLA feel inadequate right after a major release?", "acceptedAnswer": { "@type": "Answer", "text": "Standard SLAs are resourced for stable failure rates, not the elevated 'infant mortality' rate following a major release." } },
    { "@type": "Question", "name": "(Scenario: CTO managing an aging system with rising incidents) Why do we keep seeing more incidents as our system gets older, despite a consistent maintenance SLA?", "acceptedAnswer": { "@type": "Answer", "text": "An aging system's rising failure rate reflects the 'wear-out' phase — accumulated technical debt a response-time SLA doesn't resolve." } },
    { "@type": "Question", "name": "(Scenario: IT director trying to restructure a maintenance agreement) What should a maintenance SLA include beyond a standard response-time guarantee?", "acceptedAnswer": { "@type": "Answer", "text": "Provisions for elevated support around major releases and periodic architecture health assessments for aging systems." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if this applies to a young, newly launched product) Does the bathtub curve apply to a brand-new software product, or only older systems?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, from the start — a newly launched product is squarely in the infant-mortality phase." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to detect the wear-out phase early) How can we tell if our system has entered the wear-out phase before incident rates rise substantially?", "acceptedAnswer": { "@type": "Answer", "text": "A periodic architecture health assessment can surface wear-out risk before it manifests as a rising incident rate." } }
  ]
}
</script>
