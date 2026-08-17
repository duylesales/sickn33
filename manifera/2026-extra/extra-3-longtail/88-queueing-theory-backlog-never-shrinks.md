---
title: "The Math That Explains Why Your Backlog Never Actually Shrinks, Even When You Ship Faster"
keywords: "dedicated software development team, dedicated development team, software dev team, team of developers"
buyer_stage: "Consideration"
target_persona: "A"
---

# The Math That Explains Why Your Backlog Never Actually Shrinks, Even When You Ship Faster

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Math That Explains Why Your Backlog Never Actually Shrinks, Even When You Ship Faster",
  "description": "Why an engineering backlog can stay stubbornly constant even as a team's shipping velocity genuinely improves, explained through a formula from queueing theory.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/queueing-theory-backlog-never-shrinks" }
}
</script>

A CTO who genuinely increases a team's shipping velocity — more features closed per sprint, faster cycle time, real measurable improvement — often finds the backlog stubbornly the same size six months later, or even larger, and reasonably wonders whether the velocity improvement was real at all. It usually was real. What changed alongside it, largely invisibly, was the rate at which new work arrived, and a formula from an entirely different field explains precisely why backlog size depends on both numbers, not the one everyone instinctively watches.

## Why Backlog Size Isn't Simply a Function of How Fast You Ship

A team's intuitive mental model treats the backlog as a fixed pile that shipping velocity should steadily reduce — if you're closing tickets faster, the pile should shrink. This model implicitly holds the arrival rate of new work constant, which is rarely actually true in a real, growing product: more users generate more feature requests and more bug reports, more stakeholders generate more requirements, and a genuinely successful product tends to generate new backlog items at a rate that itself increases over time, often roughly in proportion to the very success that improved velocity was supposed to help capture.

## The Formula That Makes This Relationship Precise

Industrial engineer John Little formalized what's known as Little's Law in a 1961 paper, a foundational result in queueing theory stating a deceptively simple relationship: the average number of items in a system equals the average arrival rate of new items multiplied by the average time each item spends in the system. Applied to a backlog, this means backlog size isn't determined by shipping velocity in isolation — it's determined by the relationship between how fast new work arrives and how long each item takes to move through the system from arrival to completion, and improving one side of that relationship without accounting for the other doesn't guarantee the outcome intuition predicts.

Little's Law explains the CTO's puzzling observation precisely: if shipping velocity improves — reducing the average time an item spends in the system — but the arrival rate of new work increases at a similar or greater proportional rate, backlog size stays flat or even grows, exactly matching Little's Law's prediction even though the velocity improvement was completely genuine. This isn't a paradox or a measurement error — it's the formula working exactly as it should, revealing that a team fixated purely on "shipping faster" is managing only one of the two variables that actually determine backlog size, while the other variable, arrival rate, keeps moving in the background, frequently unmeasured and unmanaged.

## Why Arrival Rate Gets Overlooked So Consistently

Shipping velocity is a natural, visible thing for an engineering team to measure and optimize, since it's directly within the team's own control and shows up clearly in sprint retrospectives and velocity charts. Arrival rate — how fast new work enters the backlog — is generated largely outside the engineering team's direct control, by product, sales, customer success, and the product's own growing user base, which makes it considerably less visible on an engineering dashboard and less naturally something an engineering team feels ownership over managing, even though Little's Law says it's exactly as consequential to backlog size as the velocity number everyone already watches closely.

## What Actually Managing Both Sides of the Equation Requires

- **Track arrival rate explicitly, not just shipping velocity**, since Little's Law makes clear that backlog size depends on both, and a dashboard that only shows one side is only showing half of what actually determines the outcome a team cares about.
- **Treat backlog growth as a joint product and engineering problem**, not an engineering execution failure alone, since a rising arrival rate driven by product or business decisions is just as responsible for backlog size as engineering throughput is.
- **Set explicit intake discipline for new backlog items**, since an unmanaged, unlimited arrival rate can outpace any realistic velocity improvement, making shipping speed alone an incomplete lever for actually controlling backlog size.
- **Communicate backlog trends using both numbers**, not velocity alone, since presenting only the (genuinely improving) velocity number while backlog size stays flat creates a confusing, seemingly contradictory picture that Little's Law actually explains cleanly once arrival rate is included in the conversation.

## Why This Formula Applies Far Beyond Its Original Domain

Little's Law was originally developed and proven in the context of queueing systems generally — customers waiting in a physical line, calls waiting in a phone support queue, items waiting in a manufacturing process — and its genuine mathematical power comes from how little it assumes about the specific system it's applied to. It doesn't require knowing anything about why items arrive, how they're processed, or what determines processing time; it holds as a stable, general relationship across an enormous range of systems specifically because it's a statement about long-run averages, not about the specific mechanics of any one queue. This generality is exactly what makes it applicable to a software backlog with no modification needed to the underlying formula — a backlog is, mathematically, simply another instance of the same general queueing structure Little proved his relationship for, whether the "items" are customers in a line or feature requests in a product backlog.

This generality is worth naming explicitly because it means the relationship isn't a loose metaphor borrowed from operations research for illustrative purposes — it's the same formula, applying with the same mathematical certainty, regardless of the specific domain. A team that doubles velocity while arrival rate also roughly doubles isn't experiencing a coincidental, backlog-specific quirk; it's observing Little's Law produce exactly the outcome the formula predicts for any system with that same ratio of change, which is precisely why understanding the underlying math, not just the specific software analogy, gives a team genuine predictive power over its own backlog rather than just a retrospective explanation for why last year's numbers looked confusing.

## Manifera's Approach: Managing Both Sides of the Backlog Equation Explicitly

- **Amsterdam (Governance/Full-Picture Reporting):** Dutch project leads report both shipping velocity and backlog arrival rate to clients, explaining backlog trends through the actual relationship between the two rather than velocity alone, which can otherwise tell a misleadingly incomplete story.
- **Vietnam (Execution/Consistent, Measurable Throughput):** The engineering pod delivers consistent, measurable throughput that makes the velocity side of the equation genuinely reliable, giving clients an accurate baseline to weigh against whatever arrival rate their own product and business decisions are generating.

This is Dutch Management × Vietnamese Mastery applied to backlog management itself: governance that reports and explains the full equation, not just the flattering half of it, paired with execution that delivers genuinely reliable throughput as its half of the relationship. Explore how Manifera structures [dedicated development teams](https://www.manifera.com/services/offshore-software-development/) for sustained, measurable throughput.

## Case Study: A Tartu Company's Backlog Reckoning

Emajõe Software, a Tartu-based B2B platform company, had invested significantly in engineering process improvements over a year, genuinely doubling shipping velocity by several measures — yet the backlog, which leadership had expected to shrink substantially, was actually larger at the end of the year than at the start, prompting serious internal concern that the process investment hadn't actually worked.

Manifera's Amsterdam team, engaged to review the situation, applied Little's Law directly to the company's own data and found the arrival rate of new backlog items — driven by a genuinely successful year of user growth generating proportionally more feature requests and bug reports — had grown even faster than the doubled velocity, fully explaining the flat-to-growing backlog without any failure in the velocity improvement itself.

> *"We'd been treating the flat backlog as proof that a year of process investment hadn't worked. It turned out we'd just never been measuring the other half of the equation that actually explained what was happening."*
> — **VP of Engineering, Emajõe Software**

Emajõe Software now reports backlog trends using both velocity and arrival rate explicitly in leadership updates, framing backlog management as a shared product-and-engineering responsibility rather than a pure engineering throughput metric.

## Little's Law Applied to Backlog Management

| Scenario | Velocity Change | Arrival Rate Change | Backlog Size Outcome |
|---|---|---|---|
| Velocity improves, arrivals flat | Faster | Unchanged | Backlog shrinks |
| Velocity improves, arrivals grow proportionally | Faster | Grows at similar rate | Backlog stays flat |
| Velocity improves, arrivals grow faster | Faster | Grows faster than velocity | Backlog grows |
| Velocity flat, arrivals shrink | Unchanged | Slower | Backlog shrinks |

## Applying Little's Law to Your Own Backlog

Before concluding a velocity improvement "didn't work" because the backlog didn't shrink, check your arrival rate — Little's Law explains backlog size as a function of both variables, not shipping speed alone. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about measuring and managing both sides of your backlog equation.

## Frequently Asked Questions

### (Scenario: CTO confused why backlog didn't shrink despite faster shipping) Why did our backlog stay the same size even though our team is genuinely shipping faster now?

Backlog size depends on both shipping velocity and the arrival rate of new work, per Little's Law — if new work is arriving faster too, a genuine velocity improvement can still produce a flat or growing backlog.

### (Scenario: engineering leader trying to explain this to non-technical leadership) How do I explain this counterintuitive pattern to leadership who expected the backlog to shrink?

Introduce both numbers explicitly — velocity and arrival rate — and show how Little's Law relates them, making clear that a flat backlog alongside improved velocity reflects rising demand, not a failed process investment.

### (Scenario: engineering manager trying to actually control backlog size) If arrival rate matters as much as velocity, how do we actually manage it?

Set explicit intake discipline — prioritization criteria, capacity limits on new commitments — treating arrival rate as a manageable variable rather than an uncontrollable, externally imposed given.

### (Scenario: founder wondering if this means engineering speed doesn't matter) Does this mean improving shipping velocity isn't actually valuable if the backlog doesn't shrink?

No — velocity improvement is still genuinely valuable, since it means more of the arriving work gets addressed and users wait less time for it; it just isn't the sole determinant of backlog size on its own.

### (Scenario: product leader trying to understand their own role in backlog size) Is backlog size purely an engineering execution issue, or does product play a role too?

Both matter equally per Little's Law — arrival rate is substantially shaped by product and business decisions, making backlog management a shared responsibility, not solely an engineering throughput problem.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO confused why backlog didn't shrink despite faster shipping) Why did our backlog stay the same size even though our team is genuinely shipping faster now?", "acceptedAnswer": { "@type": "Answer", "text": "Backlog size depends on both shipping velocity and arrival rate of new work, per Little's Law — rising arrivals can offset genuine velocity gains." } },
    { "@type": "Question", "name": "(Scenario: engineering leader trying to explain this to non-technical leadership) How do I explain this counterintuitive pattern to leadership who expected the backlog to shrink?", "acceptedAnswer": { "@type": "Answer", "text": "Introduce both numbers — velocity and arrival rate — and show how Little's Law relates them to explain the flat backlog." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to actually control backlog size) If arrival rate matters as much as velocity, how do we actually manage it?", "acceptedAnswer": { "@type": "Answer", "text": "Set explicit intake discipline — prioritization criteria and capacity limits — treating arrival rate as manageable, not a given." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if this means engineering speed doesn't matter) Does this mean improving shipping velocity isn't actually valuable if the backlog doesn't shrink?", "acceptedAnswer": { "@type": "Answer", "text": "No — velocity improvement is still valuable, since more arriving work gets addressed; it just isn't the sole determinant of backlog size." } },
    { "@type": "Question", "name": "(Scenario: product leader trying to understand their own role in backlog size) Is backlog size purely an engineering execution issue, or does product play a role too?", "acceptedAnswer": { "@type": "Answer", "text": "Both matter equally — arrival rate is substantially shaped by product and business decisions, making it a shared responsibility." } }
  ]
}
</script>
