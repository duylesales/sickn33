---
title: "The Board Asked for Faster Innovation. The Real Answer Was a Debt Register."
keywords: "innovation in software, software innovation, software development processes, custom software engineering"
buyer_stage: "Awareness"
target_persona: "C"
---

# The Board Asked for Faster Innovation. The Real Answer Was a Debt Register.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Board Asked for Faster Innovation. The Real Answer Was a Debt Register.",
  "description": "Why leadership requests to 'innovate faster' often surface an underlying technical debt problem, and what actually needs to change before new feature velocity improves.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/innovate-faster-technical-debt-reality" }
}
</script>

Leadership, in nearly every version of this conversation, says "we need to innovate faster." Engineering hears a request for more hours, more headcount, or more pressure. What "innovate faster" usually actually requires — though almost nobody frames it this way — is less accumulated friction in the codebase the team is already working in, which is a different problem with a different solution than simply pushing harder.

## Why "Innovate Faster" and "Ship More Features" Aren't the Same Request

Innovation velocity is bounded by how quickly a team can safely make changes to existing systems, not just by how many engineers are typing. A team with significant unaddressed technical debt can add headcount and see diminishing or even negative returns, because more people working in a fragile, poorly understood codebase increases coordination overhead and the risk of one change breaking another, unrelated feature — the opposite of the velocity leadership is asking for.

## What Slows Innovation That Has Nothing to Do With Effort

- **Fragile, undocumented code** that requires excessive caution and manual verification for even small changes, since nobody's confident what else a given change might affect.
- **Thin or absent test coverage** that makes every change a gamble on whether something unrelated silently broke, requiring extensive manual verification that a solid test suite would automate.
- **Tightly coupled architecture** where changing one feature requires touching several others, multiplying the effort and risk of what should be an isolated change.
- **Accumulated "quick fixes"** layered on top of each other over time, each one making the next change slightly harder to reason about safely.

None of these are solved by working harder or longer. They're solved by deliberately paying down the specific debt that's creating the friction — which requires reframing "innovate faster" from an effort problem into an architecture problem.

## The Uncomfortable Conversation This Requires

Translating "innovate faster" into "we need dedicated capacity to reduce technical debt" is a hard conversation to have with leadership focused on visible feature output, because debt-reduction work produces no new customer-facing functionality in the short term. The case has to be made in terms leadership already cares about: quantified velocity trends, the specific features that took disproportionately long to ship and why, and a credible projection of how much faster future features will ship once specific debt is addressed.

## The Original Metaphor, and What It Actually Meant

The phrase "technical debt" traces back to a specific origin worth revisiting, because the metaphor's original meaning is more precise than how it's often used today. Software engineer Ward Cunningham introduced the term in a 1992 experience report, describing not sloppy or careless code, but the entirely legitimate practice of shipping a first, imperfect implementation quickly to get real-world feedback, with the explicit intention of paying down the resulting shortcuts once that feedback arrived — a financing decision, made deliberately, not a mistake. Cunningham's own framing emphasized that debt, used well, is a legitimate tool: it lets a team move fast on a genuine uncertainty, the same way a business might use financing to seize a real, time-sensitive opportunity.

The part of Cunningham's original metaphor that tends to get lost is the interest payment — his point wasn't just that shortcuts exist, it's that every shortcut left unpaid continues accruing a cost on every subsequent change to that code, exactly like unpaid financial debt accruing interest. A team that takes on debt deliberately and pays it down promptly, once the uncertainty it was hedging against resolves, uses debt the way Cunningham intended. A team that takes on debt and never revisits the decision is doing something meaningfully different from what the metaphor describes — not managing debt, but accumulating a permanent, compounding tax on every future sprint, without ever having consciously decided to carry that tax indefinitely.

This distinction matters directly for the "innovate faster" conversation, because it reframes what leadership is actually asking for. A board asking for faster innovation isn't asking a team to take on more debt — teams generally already do that reflexively under any deadline pressure. They're implicitly asking whether the debt already on the books, much of it taken on without anyone consciously deciding to, has ever actually been paid down the way Cunningham's original metaphor assumed it eventually would be. Verlain Retail's checkout-module bottleneck, described below, is precisely this pattern: debt taken on at some point, for reasons that made sense at the time, that nobody had gone back to service since — exactly the failure mode Cunningham's interest-payment framing was meant to warn against.

## Manifera's Approach: Making the Debt-to-Velocity Connection Explicit

- **Amsterdam (Governance/Business Translation):** Dutch project leads help technical leaders quantify how specific technical debt is slowing feature delivery, translating an engineering problem into the business-velocity terms leadership actually asked about.
- **Vietnam (Execution/Debt Remediation):** The engineering pod executes targeted debt reduction — the specific modules and patterns actually slowing delivery — as standing capacity alongside ongoing feature work, rather than as a separate initiative competing for the same limited attention.

This is Dutch Management × Vietnamese Mastery applied to the innovation-velocity question itself: business translation that reframes the real problem accurately, paired with execution that measurably restores the velocity leadership is actually asking for. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) practice.

## Case Study: A Bordeaux Retailer's Reframed Roadmap Conversation

Verlain Retail, a Bordeaux-based e-commerce company, had a board pushing for faster feature releases after two consecutive quarters of slipping roadmap commitments — a pressure the engineering team initially absorbed as a demand to simply work harder, without addressing why velocity had actually been declining.

Manifera's Amsterdam team ran a velocity audit, quantifying that features touching the checkout module took, on average, three times longer to ship than comparable features elsewhere in the codebase, tracing the gap to a specific tightly coupled, undocumented section of legacy code. The Vietnam pod spent six weeks refactoring that module into a more modular structure with proper test coverage. Subsequent checkout-related features shipped in line with the rest of the codebase's velocity.

> *"The board wanted faster innovation. What they actually needed to hear was that one specific part of our codebase was quietly taxing every feature that touched it — and that's a fixable problem, not a motivation problem."*
> — **CTO, Verlain Retail**

Verlain's CTO now explicitly logs every deliberate shortcut against a named "interest payment" — a documented, scheduled point at which that specific piece of debt is revisited — rather than allowing shortcuts to accumulate as untracked, indefinite obligations the way the checkout module's debt had.

## Debt You Chose vs. Debt That Just Accumulated

Cunningham's original framing suggests a useful diagnostic question for any engineering team trying to understand its own velocity problems: for any given piece of technical debt currently slowing work down, was it taken on as a deliberate, tracked financing decision with an intended repayment point, or did it simply accumulate as an unexamined byproduct of many individually reasonable short-term choices? The first kind of debt, managed the way Cunningham's metaphor intends, is a legitimate and often smart trade-off. The second kind is closer to debt a household never realized it was taking on — no single purchase felt reckless, but the balance grew anyway, silently, because nobody was tracking the running total.

Most technical debt audits, including the one that found Verlain's checkout bottleneck, discover a mix of both kinds — some debt that was consciously and reasonably taken on, and a larger share that simply accumulated through inattention rather than deliberate choice. Distinguishing between the two matters for how leadership should respond: consciously taken debt with a clear original rationale is a scheduling conversation about when to pay it down. Debt nobody remembers deciding to take on is a process conversation about why the organization currently has no mechanism for noticing debt accumulate before it becomes a bottleneck significant enough to require an external audit to find.

## Reframing the Request

| Leadership Says | Engineering Often Hears | What's Actually Needed |
|---|---|---|
| "Innovate faster" | "Work harder / hire more" | Reduce specific friction in the codebase |
| "Why did that feature take so long" | A defensive explanation | A velocity audit identifying the real bottleneck |
| "Ship more this quarter" | Cut corners to hit the number | Targeted debt reduction in the slowest modules |

## Having the Conversation With Data

Before quietly absorbing an "innovate faster" request as a call to simply work harder, run a proper velocity audit to identify which specific parts of the codebase are actually creating the friction — the conversation with leadership changes entirely once the bottleneck has a name and a location. [Talk to Manifera](https://www.manifera.com/contact-us/) about quantifying your own velocity bottlenecks.

## Frequently Asked Questions

### (Scenario: CTO facing board pressure to innovate faster) How do I respond to a board asking for faster innovation without it sounding like an excuse?

Bring data — a velocity audit showing which specific modules or patterns are slowing delivery, and a credible plan and timeline for addressing them — rather than a general statement about technical debt, which can sound like deflection without specifics.

### (Scenario: engineering manager trying to identify the real bottleneck) How do I find which part of our codebase is actually slowing us down?

Track how long features take to ship by which module or area of the codebase they touch — a clear pattern of one area consistently taking disproportionately longer is a strong signal of where the debt is concentrated.

### (Scenario: CTO trying to justify debt-reduction time to leadership) How do I get leadership to approve time for technical debt reduction instead of new features?

Frame it explicitly in terms of future feature velocity — "addressing this specific debt will let us ship checkout features three times faster going forward" is a business case leadership can evaluate, unlike a general request for "cleanup time."

### (Scenario: engineering leader worried debt reduction never actually gets prioritized) Why does technical debt reduction keep losing to new feature requests in prioritization?

Because it produces no visible customer-facing output in the short term, making it easy to deprioritize against a feature with a clear, immediate business case — unless the debt's impact on future feature velocity is made equally concrete and quantified.

### (Scenario: CTO trying to prevent this cycle from recurring) How do we avoid ending up back in this position after fixing the current bottleneck?

Establish a standing capacity allocation for ongoing debt management — typically 15-20% of sprint capacity — rather than treating debt reduction as a one-time project that ends and lets the same pattern reaccumulate.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO facing board pressure to innovate faster) How do I respond to a board asking for faster innovation without it sounding like an excuse?", "acceptedAnswer": { "@type": "Answer", "text": "Bring data — a velocity audit showing which specific modules are slowing delivery, and a credible plan and timeline for addressing them." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to identify the real bottleneck) How do I find which part of our codebase is actually slowing us down?", "acceptedAnswer": { "@type": "Answer", "text": "Track how long features take to ship by which module they touch — a clear pattern of disproportionate delay signals where the debt is concentrated." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to justify debt-reduction time to leadership) How do I get leadership to approve time for technical debt reduction instead of new features?", "acceptedAnswer": { "@type": "Answer", "text": "Frame it in terms of future feature velocity — a specific, quantified business case leadership can evaluate, unlike a general request for cleanup time." } },
    { "@type": "Question", "name": "(Scenario: engineering leader worried debt reduction never actually gets prioritized) Why does technical debt reduction keep losing to new feature requests in prioritization?", "acceptedAnswer": { "@type": "Answer", "text": "Because it produces no visible customer-facing output in the short term, unless its impact on future velocity is made equally concrete." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to prevent this cycle from recurring) How do we avoid ending up back in this position after fixing the current bottleneck?", "acceptedAnswer": { "@type": "Answer", "text": "Establish a standing capacity allocation for ongoing debt management, typically 15-20% of sprint capacity, rather than a one-time project." } }
  ]
}
</script>
