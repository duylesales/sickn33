---
title: "What Changed in a Sprint Once AI Started Writing Half the Code, and What Didn't"
keywords: "ai assisted development, ai software development, ai and software development, ai developers"
buyer_stage: "Awareness"
target_persona: "A"
---

# What Changed in a Sprint Once AI Started Writing Half the Code, and What Didn't

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Changed in a Sprint Once AI Started Writing Half the Code, and What Didn't",
  "description": "A clear-eyed look at what AI-assisted software development actually speeds up, and what still requires the same human judgment it always did.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/ai-assisted-software-development-limits" }
}
</script>

**Myth:** AI-assisted development means software gets built roughly twice as fast across the board, and developers can reliably feel that speedup as it happens.

**Fact ✅:** AI genuinely compresses specific, well-defined categories of work dramatically — boilerplate, test scaffolding, first-draft implementations of well-understood patterns — while leaving the categories of work that actually determine whether a project succeeds largely untouched: architecture decisions, requirements interpretation, and judgment calls about trade-offs a business genuinely cares about.

## Myth #1: AI Makes Junior Developers Obsolete ❌

**Fact ✅:** AI makes junior developers faster at producing code, but doesn't replace the judgment that comes from experience — knowing which of the AI's five suggested approaches actually fits the existing architecture, which edge cases the AI's confident-sounding code silently mishandles, and when a fast AI-generated answer is subtly wrong in a way that only shows up in production. Teams using AI assistance still need senior review, arguably more than before, because AI-generated code can look equally polished and confident whether it's actually correct or subtly wrong.

## Myth #2: AI Reduces the Need for QA ❌

**Fact ✅:** AI-generated code introduces its own failure patterns — plausible-looking logic that handles the common case correctly but mishandles edge cases the model wasn't specifically prompted to consider, or code that compiles and runs but embeds a subtly incorrect assumption from its training data. Several studies through 2025 and into 2026 have found AI-assisted codebases showing measurably higher rates of specific vulnerability classes when generated without deliberate security review — meaning QA and code review matter as much as ever, just against a different failure profile.

## Myth #3: AI Speeds Up Every Stage of a Project Equally ❌

**Fact ✅:** AI's speed gains concentrate heavily in the development stage, on well-understood, pattern-matchable work. Discovery (understanding what a business actually needs), architecture decisions (how the system should be structured to scale and stay maintainable), and stakeholder communication are barely touched by current AI capability — they require judgment about a specific business context that generic patterns can't substitute for. A project that's 90% discovery-and-architecture judgment and 10% boilerplate code sees a much smaller overall speedup than the headline "AI writes code faster" claim implies.

## What AI-Assisted Development Genuinely Delivers

- **Genuinely faster first drafts** of well-understood, pattern-matchable code — CRUD endpoints, standard UI components, common data transformations.
- **Faster test scaffolding**, generating a starting point for test suites that a human still needs to review for actual coverage adequacy.
- **Faster documentation drafts** from existing code, useful as a starting point that still needs verification against what the code actually does.
- **Faster exploration of unfamiliar libraries or APIs**, reducing the time spent reading documentation for common integration patterns.

None of these replace architectural judgment, requirements discovery, or the senior review that catches the specific ways AI-generated code goes subtly wrong.

## What Controlled Studies Have Found About the Perception Gap

Beyond the general pattern of AI accelerating pattern-matchable work while leaving judgment-heavy work largely untouched, a specific and widely reported finding from controlled research deserves attention on its own: a 2025 randomized study by the nonprofit research group METR, measuring experienced open-source developers working on real tasks in codebases they were already familiar with, found that developers using AI coding assistants were measurably slower on those tasks than developers working without them — while the same developers, surveyed afterward, believed the AI tools had made them meaningfully faster. The gap between perceived and measured productivity ran in the opposite direction from what almost everyone in the study expected going in, including the researchers themselves.

This finding doesn't generalize to every task or every developer — the study's specific conditions (experienced developers, familiar large codebases, real production tasks) matter to interpreting it correctly, and other studies and contexts have found genuine speedups, particularly for less experienced developers or more boilerplate-heavy work. But it's a useful corrective to purely anecdotal claims of AI-driven speedup, because it demonstrates a specific, measurable mechanism for exactly the overclaiming pattern the Ostrelle case study below describes: a tool can feel faster to use — less friction moment to moment, less time spent staring at a blank editor — while the actual measured time to complete a task, including review and correction of the AI's output, doesn't shrink proportionally or even shrinks at all.

The practical lesson isn't "don't use AI coding assistants" — it's "measure, don't just ask people how it felt." Perceived speed and measured output are different variables that can move in opposite directions, which is precisely why Manifera tracks sprint output and defect rates before and after AI tool adoption rather than relying on developer self-report alone, following the same methodological caution the METR findings suggest is warranted.

## Manifera's Approach: AI as a Force Multiplier, Not a Replacement for Judgment

- **Amsterdam (Governance/Judgment):** Dutch architects retain ownership of architecture decisions, requirements interpretation, and security-relevant design choices — the categories of work AI assistance doesn't meaningfully compress.
- **Vietnam (Execution/AI-Augmented Velocity):** The engineering pod uses AI assistance to accelerate well-understood, pattern-matchable development work, with senior code review applied consistently to catch the specific failure modes AI-generated code introduces.

This is Dutch Management × Vietnamese Mastery applied to AI tooling itself: architectural judgment that AI can't replace, paired with execution velocity that AI assistance genuinely accelerates within a disciplined review process. Learn about [Manifera's technology approach](https://www.manifera.com/about-us/manifera-technologies/).

## Case Study: A Nantes SaaS Company's AI-Assisted Sprint

Ostrelle, a Nantes-based SaaS company, adopted AI coding assistants across its team expecting a roughly 2x velocity increase and instead saw a 15-20% increase in overall sprint output after several sprints — faster boilerplate and test scaffolding, but no meaningful change in the time spent on architecture decisions or requirements clarification, which had always been the larger share of the work.

Manifera's Amsterdam team helped Ostrelle recalibrate expectations and specifically target AI assistance at the categories of work — standard API endpoints, UI components, test scaffolding — where it genuinely delivered the largest gains, while maintaining the same senior review discipline for architecture and security-relevant code.

> *"We'd been sold a 2x number. The real number was smaller, but it was real, and once we stopped expecting AI to do the judgment work, the tool became genuinely useful instead of a source of disappointment."*
> — **Engineering Manager, Ostrelle**

Ostrelle's team has since added a lightweight before/after measurement to any new tooling adoption going forward, not just AI assistants, having learned firsthand how easily a tool's felt experience can diverge from what a sprint retrospective's actual numbers show.

## Why Perceived Speed and Measured Speed Can Diverge So Sharply

The mechanism behind the METR finding is worth understanding on its own terms, because it explains why the perception gap is so persistent rather than something experienced developers would obviously notice and correct for. Using an AI assistant removes a specific kind of friction — the blank-page moment, the need to recall exact syntax, the interruption of looking up documentation — and that friction removal is immediately, viscerally felt in the moment of coding. What's much less immediately felt, in the moment, is the cumulative time spent reviewing AI-generated suggestions, catching subtly incorrect logic, and correcting code that looked plausible but didn't actually fit the existing codebase's conventions — costs that are real but distributed across many small moments rather than concentrated into one memorable friction point the way "staring at a blank editor" is.

This asymmetry between vivid, felt friction removal and diffuse, less-noticed review cost is a specific, plausible explanation for why developers in the METR study could genuinely believe they were faster while a stopwatch showed otherwise — not because anyone was being dishonest in their self-report, but because the two things being compared (moment-to-moment felt friction versus total elapsed task time) are genuinely different measurements that don't always move together.

## What AI Speeds Up vs. What It Doesn't

| Category | AI Impact |
|---|---|
| Boilerplate code, standard patterns | Significant speedup |
| Test scaffolding | Significant speedup |
| Architecture decisions | Minimal impact, still requires human judgment |
| Requirements discovery | Minimal impact |
| Security-relevant design | Requires human review regardless of AI involvement |
| Overall project velocity | Modest speedup (15-25% typical), not the dramatic gains often marketed |

## Setting Realistic Expectations

Evaluate AI-assisted development claims against what category of work is actually being accelerated and measured, not a blanket "faster" promise resting on how the tool felt to use. The judgment-heavy work that determines whether a project succeeds is largely unchanged by current AI capability. [Schedule a free consultation with our Amsterdam team](https://www.manifera.com/contact-us/) about where AI assistance genuinely fits in your project.

## Frequently Asked Questions

### (Scenario: CTO evaluating whether to adopt AI coding tools) Should we adopt AI coding assistants for our engineering team?

Yes, for the categories of work they genuinely accelerate — boilerplate, test scaffolding, documentation drafts — but set realistic expectations for overall project velocity, which typically improves by 15-25%, not the dramatic multiples sometimes marketed.

### (Scenario: CTO worried about AI-generated security vulnerabilities) Does AI-generated code introduce more security risk than human-written code?

Without deliberate security review, yes — studies have found measurably higher rates of specific vulnerability classes in AI-generated code, which is exactly why senior code review matters as much or more with AI assistance in the workflow, not less.

### (Scenario: CTO deciding whether AI reduces headcount needs) Does AI-assisted development mean we need fewer senior engineers?

The opposite is often true — senior judgment for reviewing AI-generated code, catching subtle errors, and making architecture decisions becomes more valuable, not less, as more code is produced faster by less experienced team members using AI tools.

### (Scenario: engineering manager trying to measure real AI impact) How should we measure whether AI assistance is actually helping our team?

Track overall sprint output and defect rates before and after adoption, not just individual developer perception of feeling faster — perceived speed and measured output don't always move together.

### (Scenario: CTO trying to identify where AI assistance fits best) What kind of work should we specifically target AI assistance at?

Pattern-matchable, well-understood work — standard CRUD endpoints, common UI components, test scaffolding, and documentation drafts — where AI's speed gains are largest and the risk of subtle errors is easiest to catch in review.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO evaluating whether to adopt AI coding tools) Should we adopt AI coding assistants for our engineering team?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, for boilerplate, test scaffolding, and documentation drafts, but set realistic expectations for overall project velocity, which typically improves 15-25%." } },
    { "@type": "Question", "name": "(Scenario: CTO worried about AI-generated security vulnerabilities) Does AI-generated code introduce more security risk than human-written code?", "acceptedAnswer": { "@type": "Answer", "text": "Without deliberate security review, yes — studies show measurably higher rates of specific vulnerability classes, which is why senior code review matters as much or more." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding whether AI reduces headcount needs) Does AI-assisted development mean we need fewer senior engineers?", "acceptedAnswer": { "@type": "Answer", "text": "The opposite is often true — senior judgment for reviewing AI-generated code and making architecture decisions becomes more valuable as more code is produced faster." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to measure real AI impact) How should we measure whether AI assistance is actually helping our team?", "acceptedAnswer": { "@type": "Answer", "text": "Track overall sprint output and defect rates before and after adoption, not just individual developer perception of feeling faster." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to identify where AI assistance fits best) What kind of work should we specifically target AI assistance at?", "acceptedAnswer": { "@type": "Answer", "text": "Pattern-matchable, well-understood work — standard CRUD endpoints, common UI components, test scaffolding, and documentation drafts." } }
  ]
}
</script>
