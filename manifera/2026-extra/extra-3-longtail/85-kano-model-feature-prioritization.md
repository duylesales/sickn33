---
title: "Not Every Feature on Your Roadmap Deserves the Same Kind of Attention"
keywords: "software product, software services, software innovation, custom software engineering"
buyer_stage: "Consideration"
target_persona: "B"
---

# Not Every Feature on Your Roadmap Deserves the Same Kind of Attention

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Not Every Feature on Your Roadmap Deserves the Same Kind of Attention",
  "description": "A framework for distinguishing which roadmap features are baseline expectations, which drive genuine satisfaction, and which delight users, using a model developed in 1984 and still standard in product strategy.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/kano-model-feature-prioritization"}
}
</script>

A typical product roadmap treats every single listed feature as roughly the same kind of thing — an item to be built, then simply checked off the list. That flat treatment hides a real, consequential difference: some features prevent dissatisfaction if missing but generate no real enthusiasm if present, others generate satisfaction roughly proportional to how well they're built, and a rare few generate disproportionate delight precisely because users didn't expect them at all. Treating all three identically on a single roadmap routinely means over-investing in the wrong category and under-investing in the one that actually differentiates a product.

## Why "More Features" Isn't a Coherent Prioritization Strategy

A roadmap organized purely around raw feature count or stakeholder request volume treats a basic security requirement and a genuinely delightful, unexpected touch as interchangeable line items competing for the exact same development capacity. They aren't interchangeable in their effect on user satisfaction, and prioritizing them as though they were produces a specific, avoidable failure pattern: a product that's invested heavily in features users will barely notice while underinvesting in the smaller number of features that would have actually made users enthusiastic advocates rather than merely satisfied customers.

## The Framework That Categorizes Features by Actual Effect

Quality researcher Noriaki Kano introduced what's since become known as the Kano model in a 1984 paper, categorizing product features into distinct types based on the specific relationship between a feature's presence and user satisfaction. "Must-be" features are baseline expectations whose absence causes real dissatisfaction but whose presence generates no positive satisfaction at all — users simply expect them, like basic security or a working login. "Performance" features generate satisfaction roughly proportional to how well they're executed — more and better generally means more satisfied, like page load speed or search accuracy. "Attractive" features are unexpected additions that generate disproportionate delight specifically because users didn't anticipate them, but whose absence causes no dissatisfaction at all, since nobody was expecting them in the first place.

Kano's framework matters for roadmap prioritization because these three categories require fundamentally different investment logic, not the same treatment scaled by size. Must-be features need to be adequate, not exceptional — additional investment beyond "solidly working" produces essentially no additional satisfaction, since users were never going to notice or reward excellence in a feature they simply expected to exist. Performance features reward continued investment roughly proportionally, making them a reasonable target for sustained, incremental improvement. Attractive features are where disproportionate impact actually lives, but they're also the easiest category to underfund, since they don't show up as an urgent gap the way a missing must-be feature does, and their absence isn't a fire anyone's forced to notice and fix.

## Why Attractive Features Get Systematically Underfunded

A missing must-be feature generates loud, immediate complaints, making it easy to justify prioritizing. A well-executed performance feature shows up clearly in user feedback and usage metrics, making its value easy to demonstrate. An attractive feature that was never built generates no complaints at all, because nobody was expecting it — its absence is genuinely invisible, which means it has to compete for roadmap space against loud, visible, easily justified must-be and performance work, and predictably loses that competition more often than its actual potential impact would justify, precisely because the cost of not building it never shows up as a visible, urgent signal the way the other two categories' gaps do.

## How to Apply the Kano Model to an Actual Roadmap

- **Categorize each roadmap item explicitly before prioritizing**, asking specifically whether it's a baseline expectation, a proportional-satisfaction driver, or a genuine, unexpected delight — the category, not just the perceived importance, should shape the investment approach.
- **Cap investment in must-be features at "solidly adequate," not "exceptional"**, since Kano's model predicts additional polish beyond adequacy in this category produces little additional user satisfaction to justify the additional cost.
- **Protect a deliberate, explicit allocation for attractive features**, since their systematic tendency to lose the roadmap competition against louder, more visible must-be and performance items means they need active protection, not just equal footing in a general prioritization process.
- **Revisit categorization periodically**, since today's attractive feature can become tomorrow's must-be expectation once competitors adopt it and users start expecting it as standard — Kano categories shift over time as a market matures.

## Why Kano's Original Method Involved Asking Users Directly, Not Guessing

Kano's original research methodology is worth understanding beyond the three-category framework itself, because it offers a practical technique for actually determining which category a specific feature belongs to, rather than guessing internally. Kano proposed a specific paired-question survey technique: asking users how they'd feel if a feature were present, and separately how they'd feel if it were absent, then cross-referencing the two answers to determine the feature's actual category empirically rather than assuming it based on internal stakeholder intuition alone. A feature that generates "I'd expect that" for presence and "I'd be upset" for absence is a must-be feature. A feature that generates "I'd like that" for presence and genuine indifference for absence is an attractive feature — and the specific pairing of answers, not either answer in isolation, is what actually reveals the category.

This matters practically because internal teams are frequently wrong about which category a feature actually falls into, especially for the attractive category, where a team's own excitement about a clever idea doesn't reliably predict whether real users will experience it as delightful or simply not notice it at all. Running even an informal, lightweight version of Kano's paired-question technique with real users before committing significant roadmap capacity to a feature believed to be attractive is a meaningfully more reliable way to protect that investment than relying purely on internal conviction that a specific idea belongs in the delight category.

## Manifera's Approach: Building Roadmap Strategy Around Actual User Impact

- **Amsterdam (Governance/Kano-Informed Prioritization):** Dutch project leads help clients categorize roadmap items using the Kano framework during planning, protecting deliberate space for attractive features that would otherwise lose out to louder, more visible priorities.
- **Vietnam (Execution/Right-Sized Investment by Category):** The engineering pod calibrates build effort to each feature's actual category — solid and efficient for must-be features, genuinely polished for the attractive features positioned to differentiate the product.

This is Dutch Management × Vietnamese Mastery applied to roadmap strategy itself: governance that categorizes features by actual user-satisfaction effect rather than treating a roadmap as an undifferentiated list, paired with execution that calibrates investment to match. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach to product roadmap strategy.

## Case Study: A Bratislava SaaS Company's Roadmap Rebalance

Dunaj Software, a Bratislava-based SaaS company, had a roadmap organized purely by stakeholder request frequency, resulting in continued heavy investment in incremental improvements to already-solid core functionality while a specific, genuinely novel feature idea — repeatedly suggested internally but never prioritized — sat untouched for over a year because it never generated the kind of urgent, visible pressure the other roadmap items did.

Manifera's Amsterdam team introduced the Kano framework during a roadmap planning session, categorizing the existing backlog explicitly and identifying that several heavily-resourced items were must-be features already at "solidly adequate," receiving further investment with little additional satisfaction to show for it, while the neglected feature idea was a genuine attractive-category candidate with real potential to differentiate the product. The team rebalanced the roadmap, capping further must-be investment and protecting dedicated capacity for the previously neglected feature.

> *"We'd been polishing things nobody was going to notice while the one idea that could have actually excited people sat in the backlog because it never felt urgent enough to prioritize. Categorizing it properly is what finally got it built."*
> — **Head of Product, Dunaj Software**

Dunaj Software now explicitly categorizes every roadmap item by Kano type during planning, with a standing protected allocation specifically for attractive-category features that would otherwise keep losing to louder, more visible priorities, and now runs a lightweight version of Kano's original paired-question survey before committing significant capacity to any feature believed to be genuinely delightful.

## The Three Kano Categories

| Category | Effect of Absence | Effect of Presence | Investment Logic |
|---|---|---|---|
| Must-be | Real dissatisfaction | No added satisfaction | Cap at solidly adequate |
| Performance | Reduced satisfaction | Proportional satisfaction | Reward continued investment |
| Attractive | No dissatisfaction (invisible) | Disproportionate delight | Protect dedicated allocation |

## Categorizing Your Own Roadmap Before Your Next Planning Cycle

Before your very next roadmap prioritization session, categorize each item explicitly and deliberately as must-be, performance, or attractive — the category should shape investment level, not just perceived urgency or request volume. [Talk to Manifera](https://www.manifera.com/contact-us/) about applying the Kano model to your product roadmap.

## Frequently Asked Questions

### (Scenario: product lead trying to prioritize a crowded roadmap) How do I decide which roadmap items deserve more investment than others?

Categorize each item by its actual relationship to user satisfaction using the Kano model — must-be, performance, or attractive — since these categories require fundamentally different investment logic, not just a ranking by stakeholder request volume.

### (Scenario: founder wondering why a delightful feature idea keeps getting deprioritized) Why does a genuinely exciting feature idea keep losing out to more mundane roadmap items?

Attractive-category features generate no visible, urgent complaint when absent, unlike must-be features, so they systematically lose the prioritization competition against louder, more easily justified items unless deliberately protected.

### (Scenario: product manager unsure how much to invest in a baseline feature) Should we keep investing heavily in polishing a feature users already consider standard?

Usually not beyond solidly adequate — Kano's model predicts additional investment in a must-be feature produces little additional satisfaction, since users never reward excellence in something they simply expected to exist.

### (Scenario: founder wondering if feature categories are permanent) Do Kano categories stay the same over time, or can a feature change category?

They can shift — an attractive feature can become a must-be expectation once competitors adopt it and the market starts expecting it as standard, so periodic recategorization is worth building into planning cycles.

### (Scenario: product lead trying to build this into a planning process) How do I actually build Kano categorization into our roadmap planning?

Explicitly categorize each item before prioritizing, cap must-be investment at adequate, and set aside protected capacity specifically for attractive-category work so it doesn't lose out to louder, more visible priorities by default.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: product lead trying to prioritize a crowded roadmap) How do I decide which roadmap items deserve more investment than others?", "acceptedAnswer": { "@type": "Answer", "text": "Categorize each item using the Kano model — must-be, performance, or attractive — since these require fundamentally different investment logic." } },
    { "@type": "Question", "name": "(Scenario: founder wondering why a delightful feature idea keeps getting deprioritized) Why does a genuinely exciting feature idea keep losing out to more mundane roadmap items?", "acceptedAnswer": { "@type": "Answer", "text": "Attractive-category features generate no visible complaint when absent, so they systematically lose the prioritization competition unless protected." } },
    { "@type": "Question", "name": "(Scenario: product manager unsure how much to invest in a baseline feature) Should we keep investing heavily in polishing a feature users already consider standard?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not beyond solidly adequate — additional investment in a must-be feature produces little additional satisfaction." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if feature categories are permanent) Do Kano categories stay the same over time, or can a feature change category?", "acceptedAnswer": { "@type": "Answer", "text": "They can shift — an attractive feature can become a must-be expectation once competitors adopt it as standard." } },
    { "@type": "Question", "name": "(Scenario: product lead trying to build this into a planning process) How do I actually build Kano categorization into our roadmap planning?", "acceptedAnswer": { "@type": "Answer", "text": "Explicitly categorize each item, cap must-be investment at adequate, and protect capacity specifically for attractive-category work." } }
  ]
}
</script>
