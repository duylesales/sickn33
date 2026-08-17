---
title: "The Bug Nobody Wrote on Purpose: What Happens When AI-Generated Code Goes Unreviewed"
keywords: "ai assisted development, ai software development, ai developers, ai and software development"
buyer_stage: "Consideration"
target_persona: "A"
---

# The Bug Nobody Wrote on Purpose: What Happens When AI-Generated Code Goes Unreviewed

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Bug Nobody Wrote on Purpose: What Happens When AI-Generated Code Goes Unreviewed",
  "description": "Why AI-assisted development's real risk isn't the code it writes but the review discipline teams quietly relax once code starts arriving faster than anyone expected.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/ai-generated-code-unreviewed-risk" }
}
</script>

A pull request generated with heavy AI assistance looks, on the surface, almost entirely indistinguishable from one written carefully by hand — same syntax, same consistent formatting, often cleaner comments than a genuinely rushed human developer would ever bother writing under deadline pressure. That surface-level polish is exactly what makes it dangerous to review with less scrutiny than code written the traditional way, and exactly what a growing number of engineering teams are quietly doing anyway, without ever really deciding to.

## Why Polish Isn't the Same as Correctness

AI-assisted code generation tools are, by explicit design, optimized to produce output that looks genuinely plausible and well-formed — that's substantially what these underlying models are actually trained to do well. Plausible-looking code and genuinely correct code overlap heavily in practice but aren't actually the same category at all, and the failure mode that matters most isn't obviously broken code, which typically gets caught immediately during any basic review, but rather subtly wrong code that compiles cleanly, runs without visible error, and passes a casual glance while quietly containing a logic error, an edge case gap, or a security assumption that doesn't actually hold in the specific real-world context it was inserted into.

## Why Review Discipline Quietly Erodes Even When Nobody Decides It Should

No engineering team ever formally votes to review AI-generated code less carefully than usual. What actually happens instead is considerably subtler: a reviewer sees clean, well-formatted, plausible-looking code arriving faster than usual, and unconsciously calibrates scrutiny to the code's surface polish rather than to its actual origin or risk profile. A messy, hand-written pull request visibly signals "check me carefully." AI-generated code, precisely because it looks considered and complete, signals the opposite — even when the underlying correctness guarantee is, if anything, weaker for code nobody on the team actually reasoned through line by line as they wrote it.

## The Research on Why We Trust Polished Output More Than We Should

Researcher Berkeley Dietvorst and colleagues, in a widely cited 2015 study, documented a related but distinct phenomenon called algorithm aversion — people's tendency to trust an algorithm's output less than a human's after seeing it make even a single visible mistake, even when the algorithm's overall track record was superior. A subsequent, less publicized strand of the same research area has documented the opposite failure in specific conditions: when an algorithm's output looks sufficiently polished, confident, or effortful, human reviewers can also over-trust it, applying less independent scrutiny than they would to a visibly rougher, more obviously human-authored output of equivalent actual quality.

AI-generated code sits squarely in this second failure mode. It rarely looks tentative or uncertain — a model doesn't hedge visibly the way a junior developer leaving a "not sure this is right, please check" comment would. That confident, polished presentation is precisely the surface signal research suggests triggers reduced scrutiny, independent of the code's actual correctness, which means the review discipline gap isn't a training problem or a laziness problem — it's a predictable, well-documented cognitive pattern that a team has to counteract deliberately, because it won't correct itself through good intentions alone.

## What Deliberate Counter-Calibration Actually Requires

- **Treating AI-assisted pull requests as requiring equal or greater scrutiny**, not less, explicitly stated as team policy rather than left to individual reviewer instinct.
- **Requiring the developer who used AI assistance to explain the logic in their own words** during review, not just present the output, since the act of explaining surfaces gaps the developer's own understanding might have skipped over.
- **Testing edge cases more deliberately for AI-generated sections specifically**, since a model's training data reflects common, well-represented patterns well but can still produce confidently wrong output on the specific, unusual conditions a real codebase eventually and inevitably encounters.
- **Tracking defect rates by code origin over time**, at least informally, to build an actual, real evidence base for whether a team's specific AI-assisted workflow is genuinely producing more or fewer downstream bugs than traditional development, rather than simply assuming either answer.

## Why Speed Gains and Risk Both Compound Silently

The dangerous part of this dynamic isn't any single under-reviewed pull request — it's that both the speed gains and the accumulating risk compound quietly over the same period, without either becoming visible on its own. A team adopting AI-assisted development typically sees genuine, measurable velocity improvements early, which reinforces the workflow and encourages broader adoption across the codebase. What doesn't show up on the same dashboard is the parallel accumulation of subtly under-reviewed code, because most of it doesn't fail immediately — it sits correctly most of the time, failing only under the specific edge case or unusual input that a rushed review didn't think to test for, often months after the code was merged.

This asymmetry — visible, immediate speed gains against invisible, delayed risk — is precisely why the erosion described earlier can continue for a long time before a team notices anything is wrong, and why Walutowa Sieć's near-miss took months of otherwise-successful AI-assisted development to surface. A team evaluating whether its AI-assisted workflow is actually working shouldn't rely on the absence of visible problems as evidence of safety, since the nature of the risk is specifically that it stays invisible until a low-probability edge case is finally hit in production, by which point the responsible pull request may be long forgotten and difficult to trace back to its actual cause.

## Manifera's Approach: AI as an Accelerant, Never a Substitute for Review Discipline

- **Amsterdam (Governance/Review Policy):** Dutch project leads set explicit review standards for AI-assisted code that don't relax scrutiny based on how polished the output looks, treating origin-blind review discipline as a defined process requirement, not an assumption.
- **Vietnam (Execution/Deliberate Verification):** The engineering pod applies the same testing rigor to AI-assisted and hand-written code alike, with developers required to demonstrate understanding of AI-generated logic during review rather than simply passing it through.

This is Dutch Management × Vietnamese Mastery applied to the AI-assisted development era itself: governance that names and counteracts a predictable bias rather than trusting good intentions to prevent it, paired with execution that treats speed and correctness as separate variables to manage independently. Learn about Manifera's approach to [AI-assisted software development](https://www.manifera.com/services/custom-software-development/).

## Case Study: A Kraków Fintech's Near-Miss

Walutowa Sieć, a Kraków-based fintech platform, had adopted AI-assisted development tools across its engineering team, seeing genuine velocity gains for several months before a subtly incorrect currency rounding calculation, generated by an AI tool and approved in a pull request that "looked complete," reached production and caused a batch of transactions to settle with small but real discrepancies.

A post-incident review found the reviewing engineer had approved the change in under two minutes, notably and measurably faster than the team's typical review time for hand-written changes of genuinely comparable complexity — the code's polished, well-formatted appearance had reduced scrutiny in a real, quantifiable way, exactly the pattern the underlying research on algorithmic trust would predict in advance. Manifera's Amsterdam team, engaged afterward to audit the broader codebase, introduced an explicit origin-blind review policy requiring the same minimum review time and edge-case testing regardless of how the code was produced.

> *"The code looked so clean that nobody thought to slow down and question it. That was the actual problem — not the AI, but how differently we treated code because of how it looked."*
> — **Engineering Lead, Walutowa Sieć**

Walutowa Sieć now tracks defect rates by code origin as a standing metric, and has found, six months in, that AI-assisted code under the new review discipline shows no measurable difference in downstream defect rate compared to hand-written code — a result the engineering lead attributes directly and specifically to closing the review-scrutiny gap deliberately, rather than to the AI tooling itself having somehow improved on its own during that same period.

## Review Discipline: Before and After Counter-Calibration

| Practice | Before (Instinctive) | After (Deliberate) |
|---|---|---|
| Review time for polished output | Faster, less scrutiny | Same as hand-written code |
| Explaining logic during review | Assumed from clean code | Required regardless of origin |
| Edge case testing | Lighter for "complete-looking" code | Deliberately increased for AI-assisted sections |
| Defect tracking by origin | Not tracked | Tracked as a standing metric |

## Counter-Calibrating Your Own Team's Review Habits

Set an explicit, clearly written policy that AI-assisted code requires equal or genuinely greater review scrutiny, never less — the risk isn't the tool, it's the unconscious calibration to how polished the output looks. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about building AI-assisted workflows with review discipline built in from the start.

## Frequently Asked Questions

### (Scenario: engineering lead noticing review times dropping for AI-assisted code) Why do reviewers tend to scrutinize AI-generated code less carefully than hand-written code?

Because polished, well-formatted output triggers reduced scrutiny as a cognitive pattern, independent of actual correctness — a well-documented effect in research on how humans evaluate algorithmic output that looks confident or complete.

### (Scenario: CTO deciding whether to adopt AI-assisted development tools) Does this mean AI-assisted development tools are inherently riskier than traditional development?

Not inherently — the risk comes from unconsciously relaxed review discipline, not the tools themselves. Teams that deliberately maintain equal scrutiny regardless of code origin see comparable defect rates to traditional development.

### (Scenario: engineering manager trying to build a policy) What's the most effective single policy change to counteract this risk?

Requiring the developer to explain AI-generated logic in their own words during review, rather than simply presenting the output — this surfaces gaps in understanding that visual inspection alone tends to miss.

### (Scenario: team lead trying to measure whether this is actually a problem for their team) How can a team tell if it's actually falling into this reduced-scrutiny pattern?

Track review time and defect rates by code origin, even informally — a noticeably faster review time for AI-assisted pull requests, without a corresponding drop in complexity, is a concrete signal worth investigating.

### (Scenario: founder wondering if this applies to their vendor relationship) Should I ask my software vendor how they review AI-assisted code specifically?

Yes — a vendor with an explicit, origin-blind review policy is meaningfully lower risk than one relying on individual reviewer instinct, especially as AI-assisted development becomes standard practice across the industry.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: engineering lead noticing review times dropping for AI-assisted code) Why do reviewers tend to scrutinize AI-generated code less carefully than hand-written code?", "acceptedAnswer": { "@type": "Answer", "text": "Polished, well-formatted output triggers reduced scrutiny as a cognitive pattern, independent of actual correctness." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding whether to adopt AI-assisted development tools) Does this mean AI-assisted development tools are inherently riskier than traditional development?", "acceptedAnswer": { "@type": "Answer", "text": "Not inherently — the risk comes from relaxed review discipline, not the tools. Deliberate equal scrutiny produces comparable defect rates." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to build a policy) What's the most effective single policy change to counteract this risk?", "acceptedAnswer": { "@type": "Answer", "text": "Requiring the developer to explain AI-generated logic in their own words during review, surfacing understanding gaps visual inspection misses." } },
    { "@type": "Question", "name": "(Scenario: team lead trying to measure whether this is actually a problem for their team) How can a team tell if it's actually falling into this reduced-scrutiny pattern?", "acceptedAnswer": { "@type": "Answer", "text": "Track review time and defect rates by code origin — a noticeably faster review time without lower complexity is a concrete warning signal." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if this applies to their vendor relationship) Should I ask my software vendor how they review AI-assisted code specifically?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — a vendor with an explicit, origin-blind review policy is meaningfully lower risk than one relying on individual reviewer instinct." } }
  ]
}
</script>
