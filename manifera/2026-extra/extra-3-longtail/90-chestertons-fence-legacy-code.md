---
title: "Before You Delete That Confusing Old Function, Ask Why It's Still There"
keywords: "custom software development, custom software solution, software product, custom development company"
buyer_stage: "Decision"
target_persona: "C"
---

# Before You Delete That Confusing Old Function, Ask Why It's Still There

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Before You Delete That Confusing Old Function, Ask Why It's Still There",
  "description": "Why removing confusing, seemingly unnecessary legacy code without understanding why it was originally added is a well-documented, avoidable cause of production incidents.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/chestertons-fence-legacy-code" }
}
</script>

An engineer inheriting an unfamiliar legacy codebase frequently encounters a piece of code that looks obviously unnecessary — a strange conditional check, a redundant-seeming validation, a function that appears to duplicate something already handled elsewhere. The natural instinct is to clean it up: delete the confusing part, simplify the logic, make the code look the way a fresh implementation would look today. A specific, centuries-old piece of reasoning explains exactly why that instinct, however reasonable it feels, is one of the more reliable ways to reintroduce a bug that was deliberately fixed years earlier by someone who is no longer around to explain why.

## Why "This Looks Unnecessary" Isn't the Same as "This Is Unnecessary"

Code that looks confusing or redundant to someone unfamiliar with a system's history frequently isn't actually redundant at all — it's the visible remainder of a fix for a specific, real problem that occurred at some point in the past, often one that isn't obvious from reading the code alone, especially if the original bug report, incident postmortem, or commit message explaining the reasoning was never written clearly, was written but never read, or has simply been lost to time as the people involved moved on. The code's apparent uselessness is a fact about the current reader's limited context, not necessarily a fact about the code's actual function.

## The Principle Named After a 1929 Argument About Literal Fences

Writer G.K. Chesterton articulated a principle in his 1929 book that has since become widely known in software engineering circles as Chesterton's Fence: if you come across a fence in a field with no obvious purpose, the correct response isn't to immediately remove it because you can't see why it's there — it's to first go and find out why it was put there in the first place, since the reason may be entirely sound even though it isn't visible to you from where you're currently standing. Chesterton's original point was about reform and tradition generally, but the reasoning translates with unusual precision to legacy code: a piece of logic that looks unnecessary to a current reader may have been added specifically to handle a real problem that occurred once and never occurred again precisely because that fix has been quietly preventing it ever since.

Chesterton's Fence doesn't argue that the fence — or the confusing code — should never be removed. It argues specifically against removing it before understanding why it's there, since removal without that understanding risks reintroducing whatever problem the fence, or the code, was originally built to prevent. This is a meaningfully different and more disciplined standard than either "never touch old code" or "clean up anything that looks unnecessary" — it's specifically "investigate before you remove," a standard that costs real time upfront but avoids a specific, well-documented, and often expensive failure pattern in software maintenance.

## Why This Failure Pattern Is So Common in Practice

Legacy code accumulates exactly the conditions that make Chesterton's Fence violations likely: the original author has often left the company or moved to a different team, the original bug report or incident that prompted the fix is buried in an old ticket system nobody thinks to search, and the code itself, if not accompanied by a clear comment explaining its purpose, gives no indication of the specific history that justified it. A new engineer facing a deadline and a confusing piece of code has every incentive to simplify it and move on, and no readily available way to discover the reasoning that would tell them not to, which is precisely the combination of conditions under which this specific mistake reliably recurs across software teams.

## How to Actually Apply Chesterton's Fence to Legacy Code

- **Check version control history and commit messages before removing anything confusing**, since the original change that introduced the code may include an explanation, even an informal one, of why it was added.
- **Search issue tracking systems for related bug reports or incidents**, since a seemingly odd piece of validation or conditional logic is frequently traceable to a specific, documented production issue if the right search terms are used.
- **Ask anyone still at the company who might remember**, even informally, before assuming no one does — institutional memory often persists longer than a formal documentation trail does.
- **If the reason genuinely can't be determined, remove cautiously with strong test coverage and monitoring**, rather than either leaving confusing code untouched indefinitely out of excess caution or removing it carelessly — Chesterton's Fence argues for investigation, not permanent paralysis when investigation genuinely comes up empty.

## Manifera's Approach: Investigating Before Removing, as Standard Practice

- **Amsterdam (Governance/Legacy Code Discipline):** Dutch project leads build investigation time into any legacy cleanup or modernization scope, treating "why is this here" as a required question before removal, not an optional nicety skipped under deadline pressure.
- **Vietnam (Execution/Careful, Historically-Informed Cleanup):** The engineering pod checks version control history, issue trackers, and available institutional knowledge before removing unfamiliar legacy code, reducing the risk of reintroducing a previously fixed problem.

This is Dutch Management × Vietnamese Mastery applied to legacy code discipline itself: governance that budgets real time for investigation before cleanup, paired with execution disciplined enough to actually do the investigation rather than skip it under pressure. Explore Manifera's approach to [custom software development](https://www.manifera.com/services/custom-software-development/) and legacy code modernization.

## Case Study: A Constanța Retailer's Reintroduced Bug

Marea Neagră Retail, a Constanța-based e-commerce retailer, had a new engineer remove what appeared to be a redundant, confusing currency-rounding check during a routine code cleanup, reasoning that the platform's newer, more comprehensive currency handling logic elsewhere in the codebase had made the old check unnecessary. Within two weeks, a specific edge case involving a currency conversion during a promotional pricing event caused a rounding discrepancy in customer refunds — the exact problem the removed check had been silently preventing for the three years since it was originally added, following what a buried support ticket later confirmed was a nearly identical incident.

Manifera's Amsterdam team, engaged for the subsequent cleanup and incident review, restored the check and added a clear, explanatory comment along with a linked reference to the original incident, and established a standing practice of checking version control history and issue trackers before removing any legacy code whose purpose wasn't immediately obvious.

> *"The check looked exactly like something a less careful engineer three years ago had left in by accident. It turned out a very careful engineer three years ago had put it there on purpose, for a reason nobody had bothered to write down where the next person could find it."*
> — **Engineering Director, Marea Neagră Retail**

Marea Neagră Retail now requires a documented investigation step — checking history, searching for related incidents — before any legacy code deemed "confusing or unnecessary" can be removed, formalizing Chesterton's Fence directly into its code review checklist, alongside a new standard requiring every non-obvious fix to include a comment explaining why it exists, specifically so the next engineer never has to repeat the same investigation from scratch.

## Why Writing the Reason Down Is the Cheapest Long-Term Fix

The entire failure pattern this article describes depends on one specific condition: the original reasoning behind a piece of code wasn't captured anywhere a future reader could find it. This means the most cost-effective long-term defense against a Chesterton's Fence violation isn't only investigating before removal — it's also making sure the next confusing-looking fix a team adds today doesn't become the next unexplained fence a different engineer trips over in three years. A short, specific comment explaining why a seemingly odd piece of logic exists, or a commit message that clearly links back to the incident that prompted it, costs a few minutes now and can save the multi-day investigation, or the reintroduced production incident, that its absence predictably produces later.

## Removing Legacy Code: Reckless vs. Disciplined

| Approach | Reckless Removal | Chesterton's Fence Approach |
|---|---|---|
| Before removing | Assumes confusing means unnecessary | Investigates history and reasoning first |
| Version control check | Skipped | Standard practice |
| Issue tracker search | Skipped | Standard practice |
| If reason can't be found | Removes anyway | Removes cautiously, with strong test coverage |
| Risk | Reintroducing a previously fixed problem | Meaningfully reduced |

## Applying Chesterton's Fence to Your Own Codebase

Before removing any legacy code that looks confusing or unnecessary, invest the time to check version control history and issue trackers for the reason it was originally added — the investigation is cheaper than reintroducing a previously fixed problem. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about a disciplined approach to legacy code cleanup.

## Frequently Asked Questions

### (Scenario: engineer facing confusing legacy code during cleanup) How do I decide whether a confusing piece of legacy code is safe to remove?

Check version control history and issue tracker records for the reason it was originally added before removing it — code that looks unnecessary is often a fix for a specific past problem that isn't obvious from reading the code alone.

### (Scenario: team lead worried this means never cleaning up old code) Does this mean legacy code should never be removed or simplified?

No — Chesterton's Fence argues for investigating before removing, not against removal itself; once the original reasoning is understood, removing outdated or genuinely unnecessary code is entirely appropriate.

### (Scenario: engineering manager trying to prevent this mistake systematically) How can a team build this discipline into its standard process, rather than relying on individual engineers remembering to check?

Add a documented investigation step to the code review checklist for any removal of unfamiliar legacy code, requiring evidence that version control and issue tracker history were actually checked before approval.

### (Scenario: engineer unable to find any explanation for confusing code) What should I do if I genuinely can't find any explanation for why confusing code exists?

Remove it cautiously with strong test coverage and active monitoring afterward, rather than leaving it untouched indefinitely — Chesterton's Fence calls for investigation, not permanent paralysis when investigation genuinely turns up nothing.

### (Scenario: CTO trying to reduce this risk during a legacy system inheritance) How does this apply specifically when inheriting an entire unfamiliar legacy system from a previous team or vendor?

Budget real investigation time into the modernization scope from the start, and prioritize documenting institutional knowledge from anyone still available who worked on the original system before that knowledge is lost entirely.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: engineer facing confusing legacy code during cleanup) How do I decide whether a confusing piece of legacy code is safe to remove?", "acceptedAnswer": { "@type": "Answer", "text": "Check version control history and issue tracker records for the reason it was originally added before removing it." } },
    { "@type": "Question", "name": "(Scenario: team lead worried this means never cleaning up old code) Does this mean legacy code should never be removed or simplified?", "acceptedAnswer": { "@type": "Answer", "text": "No — Chesterton's Fence argues for investigating before removing, not against removal itself once the reasoning is understood." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to prevent this mistake systematically) How can a team build this discipline into its standard process, rather than relying on individual engineers remembering to check?", "acceptedAnswer": { "@type": "Answer", "text": "Add a documented investigation step to the code review checklist for removal of unfamiliar legacy code." } },
    { "@type": "Question", "name": "(Scenario: engineer unable to find any explanation for confusing code) What should I do if I genuinely can't find any explanation for why confusing code exists?", "acceptedAnswer": { "@type": "Answer", "text": "Remove it cautiously with strong test coverage and active monitoring afterward, rather than leaving it untouched indefinitely." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to reduce this risk during a legacy system inheritance) How does this apply specifically when inheriting an entire unfamiliar legacy system from a previous team or vendor?", "acceptedAnswer": { "@type": "Answer", "text": "Budget real investigation time into the modernization scope, and prioritize documenting institutional knowledge before it's lost." } }
  ]
}
</script>
