---
title: "The Small Ugly Function Nobody Fixed Is Why Your Codebase Looks Like This Now"
keywords: "software quality, sw quality, software engineer stages, software development processes"
buyer_stage: "Awareness"
target_persona: "A"
---

# The Small Ugly Function Nobody Fixed Is Why Your Codebase Looks Like This Now

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Small Ugly Function Nobody Fixed Is Why Your Codebase Looks Like This Now",
  "description": "Why a codebase's overall quality tends to track the smallest, most visible signs of neglect left unaddressed, and what that means for maintaining software quality over time.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/broken-windows-codebase-decay" }
}
</script>

Every experienced engineering lead has watched a codebase slide gradually from disciplined to genuinely messy over roughly eighteen months, without any single dramatic event ever really explaining the decline. No one on the team formally decided to stop caring about code quality. What actually happened instead was smaller and considerably more specific: one ugly, hacky function got merged under real deadline pressure, nobody ever went back to fix it afterward, and its continued visible presence quietly changed what "acceptable" looked like to everyone who touched the codebase from that point on.

## Why One Unfixed Problem Changes Behavior Around It

A pristine codebase creates a strong, largely unconscious social norm: new code should meet the existing standard, because the existing standard is visibly, consistently high. The moment a genuinely sloppy piece of code sits unaddressed in that same codebase, it changes the visible baseline for everyone who encounters it afterward — not through any explicit policy change, but through a simple, human tendency to calibrate effort and care against the surrounding environment rather than against an abstract standard nobody's actively enforcing in the moment.

## The Criminology Theory Behind Why This Pattern Is So Consistent

Social scientists James Q. Wilson and George Kelling introduced the broken windows theory in a 1982 article, arguing that visible signs of disorder and neglect in an environment — a broken window left unrepaired, graffiti left unremoved — signal that nobody is monitoring or maintaining a space, which measurably increases the likelihood of further disorder, even among people who wouldn't have caused the initial damage themselves. The theory's core mechanism wasn't about the broken window's direct cost; it was about what the window's continued, visible presence communicated to everyone who saw it: this space isn't being watched, and the normal standard of care doesn't obviously apply here anymore.

The theory has been contested and refined considerably in criminology since its original publication, particularly regarding its application to policing policy, but the underlying psychological mechanism — visible neglect lowering the perceived standard and increasing further neglect — has held up well as a general description of how humans calibrate behavior to environmental signals, and it translates unusually cleanly to software engineering. A codebase with one unaddressed, obviously hacky function is signaling, to every engineer who encounters it, that the space isn't being consistently watched or maintained to a high standard — an implicit signal considerably more powerful, and more corrosive over time, than any written code quality policy the team might have on file but isn't visibly enforcing in practice.

## Why This Matters More Than a Single Function's Direct Cost

The direct cost of one poorly written function is usually small — it's a contained, low-risk piece of technical debt in isolation. The broken windows mechanism explains why treating it as low-risk in isolation misses the actual danger: the function's continued, visible presence in the codebase is doing ongoing communicative work, quietly signaling a lowered standard to every engineer who touches nearby code afterward, each of whom then has slightly less reason to hold their own contribution to a higher bar than the visible baseline around them already displays.

## What This Implies for How a Team Should Actually Respond

- **Fix small, visible quality problems quickly, not just large ones**, since the broken windows mechanism is specifically about visible signals, not about the underlying severity of any single issue in isolation.
- **Treat code review consistency as a signal-maintenance function**, not just a bug-catching one — a review process that lets an occasional sloppy piece of code through is doing more damage to the surrounding standard than the specific code's direct risk would suggest.
- **Prioritize addressing the first instance of a new kind of shortcut**, since the first unaddressed exception establishes a precedent that subsequent, similar shortcuts can point back to as justification.
- **Recognize that restoring a decayed standard takes disproportionately more effort than maintaining one**, since a team has to overcome an already-lowered baseline expectation, not just fix the accumulated backlog of specific issues.

## Why New Hires and New Team Members Are the Most Affected

The broken windows mechanism has a specific, practical implication for onboarding that's easy to overlook: a new engineer joining a team has no prior baseline of their own to compare the current codebase against — their entire sense of "what's normal here" gets calibrated directly from whatever they encounter during their first weeks, unaddressed shortcuts included. An experienced team member who remembers when the codebase was cleaner might mentally discount an old, known issue as an exception rather than the norm. A new hire has no such context, and is far more likely to read an unaddressed sloppy function as simply representative of the team's actual standard, then calibrate their own contributions accordingly from day one.

This means the cost of a lingering, unaddressed quality issue compounds specifically at exactly the moments a team is growing fastest — every new engineer who onboards against an already-lowered visible baseline reinforces that baseline further, rather than pulling it back toward the team's stated, but not visibly enforced, standard. A team scaling its engineering headcount without first cleaning up its most visible existing quality lapses is, in effect, actively recruiting new reinforcement for a standard lower than the one it believes it's actually maintaining, which is precisely why a quality reset before a hiring push tends to pay for itself well beyond the reset's own direct scope.

## Manifera's Approach: Treating Every Visible Quality Signal as Worth Maintaining

- **Amsterdam (Governance/Standard Maintenance):** Dutch project leads treat consistent code review and quality standards as an ongoing signal-maintenance discipline, addressing small quality lapses quickly rather than letting them accumulate as implicit permission for further lapses.
- **Vietnam (Execution/Consistent Craft):** The engineering pod maintains consistent code quality across a codebase as standard practice, recognizing that the visible standard of existing code shapes the quality of what gets added next, whether or not anyone states that expectation explicitly.

This is Dutch Management × Vietnamese Mastery applied to code quality culture itself: governance that treats small visible lapses as worth addressing promptly, paired with execution that maintains a consistently high baseline as the norm new code is measured against. Learn about Manifera's approach to [software quality and engineering discipline](https://www.manifera.com/services/custom-software-development/).

## Case Study: A Turku Platform's Quality Reset

Saaristo Digital, a Turku-based logistics platform, had watched its codebase's overall quality decline steadily over roughly two years despite no single dramatic incident explaining it, and no formal change to its stated code quality standards during that period. A review commissioned with Manifera's Amsterdam team traced the decline's origin to a handful of specific, unaddressed shortcuts from an early deadline-driven sprint — hacky workarounds that had never been cleaned up, and had visibly signaled, to every engineer who encountered them afterward, that the team's actual enforced standard was lower than its documented one.

The Vietnam pod prioritized cleaning up those specific original instances first, rather than starting with the largest or most recently added quality problems, on the reasoning that the earliest unaddressed signals were doing the most ongoing damage to the team's calibrated sense of acceptable quality.

> *"We kept trying to fix the newest messy code, assuming that's where the problem was concentrated. It turned out the actual source was a few small things from two years ago that had just been sitting there the whole time, quietly setting the tone for everything after."*
> — **Engineering Director, Saaristo Digital**

Saaristo Digital now runs a standing quarterly review specifically looking for new, small, unaddressed quality lapses, treating early intervention on visible issues as a higher priority than the size of any individual problem alone would otherwise suggest — timed deliberately to run before each hiring push, precisely because new engineers calibrate fastest against whatever standard they actually encounter first.

## Where Broken Windows Theory Applies in a Codebase

| Signal | What It Communicates | Recommended Response |
|---|---|---|
| One hacky, unaddressed function | Standard isn't being enforced | Fix quickly, regardless of size |
| Inconsistent code review | Quality gate isn't reliable | Restore consistency as a priority |
| First unaddressed shortcut of a new kind | Sets a precedent for similar shortcuts | Address before it's repeated elsewhere |
| Long-neglected legacy section | Team doesn't maintain older code | Periodic review, not just new-code focus |

## Watching for Your Own Codebase's First Broken Window

Review your own codebase specifically for small, early, unaddressed quality lapses, not just the largest and most obvious current problems — the earliest signals often do the most ongoing damage to a team's calibrated standard. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about a code quality review.

## Frequently Asked Questions

### (Scenario: engineering lead noticing gradual codebase decline) Why does our codebase's quality seem to decline gradually even though we haven't changed our stated standards?

Unaddressed small quality lapses signal a lower enforced standard to every engineer who encounters them, gradually shifting what feels acceptable in practice, even if the written policy hasn't changed at all.

### (Scenario: team lead deciding where to focus cleanup effort) Should we prioritize fixing the newest messy code or the oldest unaddressed issues?

Often the oldest, earliest unaddressed issues, since they've had the longest time to signal a lowered standard to the most people — addressing the origin point can have more impact than fixing more recent, less established problems.

### (Scenario: engineering manager trying to justify a cleanup effort to leadership) How do I explain to non-technical leadership why a small, low-risk piece of technical debt is worth fixing?

Frame it around what it signals to the team, not just its direct risk — a small unaddressed issue communicates a lowered standard that shapes the quality of everything built near it afterward, which compounds well beyond the issue's own contained cost.

### (Scenario: engineering lead wondering if this justifies obsessive perfectionism) Does this mean every minor code quality issue needs to be fixed immediately?

Not necessarily immediately, but visibly and consistently — the key is not letting a quality lapse sit unaddressed long enough to become a normalized part of the codebase's perceived standard.

### (Scenario: team lead trying to restore a codebase that's already declined) Is it harder to restore a decayed code quality standard than to maintain a good one from the start?

Yes, meaningfully harder — restoring a standard requires overcoming an already-lowered baseline expectation across the team, not just fixing the accumulated backlog of specific issues, which is exactly why early intervention is disproportionately valuable.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: engineering lead noticing gradual codebase decline) Why does our codebase's quality seem to decline gradually even though we haven't changed our stated standards?", "acceptedAnswer": { "@type": "Answer", "text": "Unaddressed small quality lapses signal a lower enforced standard to every engineer who encounters them, gradually shifting what feels acceptable." } },
    { "@type": "Question", "name": "(Scenario: team lead deciding where to focus cleanup effort) Should we prioritize fixing the newest messy code or the oldest unaddressed issues?", "acceptedAnswer": { "@type": "Answer", "text": "Often the oldest issues, since they've had the longest time to signal a lowered standard to the most people." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to justify a cleanup effort to leadership) How do I explain to non-technical leadership why a small, low-risk piece of technical debt is worth fixing?", "acceptedAnswer": { "@type": "Answer", "text": "Frame it around what it signals to the team, not just its direct risk — it shapes the quality of everything built near it afterward." } },
    { "@type": "Question", "name": "(Scenario: engineering lead wondering if this justifies obsessive perfectionism) Does this mean every minor code quality issue needs to be fixed immediately?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily immediately, but visibly and consistently — the key is not letting a lapse become a normalized part of the codebase's standard." } },
    { "@type": "Question", "name": "(Scenario: team lead trying to restore a codebase that's already declined) Is it harder to restore a decayed code quality standard than to maintain a good one from the start?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, meaningfully harder — restoring a standard requires overcoming an already-lowered baseline expectation across the whole team." } }
  ]
}
</script>
