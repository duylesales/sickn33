---
title: "The Team Size Where Adding One More Person Quietly Starts Subtracting Output"
keywords: "team of developers, application development team, software dev team, application developers"
buyer_stage: "Consideration"
target_persona: "A"
---

# The Team Size Where Adding One More Person Quietly Starts Subtracting Output

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Team Size Where Adding One More Person Quietly Starts Subtracting Output",
  "description": "Why individual effort within a development team tends to decline as team size grows, based on a finding first documented in 1913 and confirmed repeatedly since across group settings.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/ringelmann-effect-team-size" }
}
</script>

A CTO expanding a development team from six people to twelve reasonably expects roughly double the actual output, or at least something reasonably close to it once normal onboarding friction eventually settles down. What actually tends to happen, in team after team across many decades of organizational research, is considerably and consistently less than double — and the real shortfall isn't fully explained by coordination overhead alone either. Part of it comes from something considerably quieter: individual effort per person measurably declining as the group itself gets larger, even when nobody consciously decides to work any less.

## Why Team Output Doesn't Scale the Way Headcount Does

The intuitive model treats a team's total output as the sum of each member's individual output, held roughly constant regardless of team size — twelve people should produce twice what six people produce, full stop. Real team performance data consistently falls short of this prediction, and while coordination overhead (the communication cost Brooks's Law and related research describe) explains part of the gap, it doesn't explain all of it. A meaningful additional portion of the shortfall comes from a separate, well-documented phenomenon: individuals in larger groups tend to exert measurably less individual effort than the same individuals would in a smaller group, even on tasks where coordination overhead is minimal.

## The Original 1913 Discovery Behind This Pattern

French agricultural engineer Max Ringelmann, in research conducted in the late 1880s and published in 1913, had participants pull on a rope, measuring both individual effort alone and effort when pulling as part of a group. Ringelmann found that as group size steadily increased, the average individual effort exerted per person decreased just as steadily — a group of eight people pulled together with barely half the combined force that eight separate individuals pulling entirely alone would have generated, meaning the group's actual collective output fell well short of the simple arithmetic sum of its individual members' own capabilities. This became known as the Ringelmann effect, and subsequent research throughout the twentieth century, including work by social psychologists studying what they termed "social loafing," confirmed the same basic pattern across a wide range of group tasks well beyond rope-pulling, including cognitive and collaborative work more directly relevant to a modern engineering team.

Researchers have identified two distinct mechanisms contributing to the Ringelmann effect, both relevant to software teams specifically: coordination loss, where larger groups genuinely struggle to synchronize individual efforts efficiently (closely related to the communication overhead Brooks's Law describes), and motivation loss, where individuals in larger groups feel less personally accountable for the group's overall output, since any single person's individual contribution becomes proportionally less visible and less identifiably theirs as team size grows. It's specifically this second mechanism — motivation loss, not just coordination cost — that explains why simply solving communication overhead through better tooling or process doesn't fully close the output gap a larger team predictably produces.

## Why Motivation Loss Is Easy to Miss in a Software Team Specifically

A software engineering context can make individual contribution more visible than physical group tasks — commits, pull requests, and code ownership are individually attributable in a way rope-pulling isn't. This visibility genuinely mitigates the Ringelmann effect's motivation-loss component to some degree, which is precisely why software teams don't experience the same dramatic falloff Ringelmann originally measured. But it doesn't eliminate the effect entirely, particularly for less individually attributable work — code review thoroughness, proactive bug-catching, voluntary knowledge-sharing — where a specific individual's contribution or lack of one is considerably harder to trace, and where the same underlying motivation-loss mechanism has more room to operate unchecked.

## What Managing This Effect Actually Requires

- **Preserve individual attribution and visibility even as a team grows**, since the Ringelmann effect's motivation-loss component is specifically mitigated by an individual's sense that their personal contribution is identifiable and valued, not anonymized into an undifferentiated group output.
- **Watch less individually-attributable work categories more carefully as team size increases**, since code review thoroughness and voluntary knowledge-sharing are more susceptible to motivation loss than individually-owned feature work.
- **Consider smaller, semi-autonomous sub-teams within a larger organization**, since this structure preserves more of the individual visibility and accountability that mitigates the effect, compared to one large, undifferentiated team.
- **Don't assume linear output scaling when planning capacity around headcount growth**, building realistic expectations around both coordination overhead and motivation-loss effects rather than a simple headcount multiplication.

## Why the Effect Persists Even Among Motivated, Professional Teams

A natural objection to applying century-old rope-pulling research to a modern, professional engineering team is that software developers are generally intrinsically motivated, career-invested professionals, not conscripted participants in a physical exertion experiment, and might reasonably be expected to be immune to the effect Ringelmann documented. Subsequent social loafing research addressed this objection directly, finding the effect persists, in a measurably reduced but still real form, even among motivated professionals and even on cognitively engaging tasks, not just physically effortful or tedious ones. The mechanism isn't primarily about laziness or lack of commitment — it's about diffusion of perceived responsibility, which operates to some degree regardless of how genuinely motivated an individual is, simply because the psychological sense of "my specific contribution matters and is visible" naturally weakens as the group around a person grows larger, independent of that person's underlying work ethic.

This is precisely why the mitigation strategy that actually works isn't "hire more motivated people" — Makedonia Systems' team was already skilled and professionally invested, and the shortfall still occurred — but structural: rebuilding the conditions under which individual contribution remains visible and attributable, restoring the psychological mechanism the research identifies as the actual lever, rather than assuming the problem is a motivation deficit that better hiring or more inspiring leadership alone could solve.

## Manifera's Approach: Structuring Teams to Preserve Individual Accountability at Scale

- **Amsterdam (Governance/Attribution-Preserving Team Structure):** Dutch project leads structure larger engagements around clearly attributable ownership — specific modules, specific responsibilities — rather than an undifferentiated pool, mitigating the motivation-loss component of the Ringelmann effect as team size grows.
- **Vietnam (Execution/Individually Accountable Contribution):** The engineering pod maintains clear individual code ownership and review accountability even within larger dedicated team engagements, preserving the visibility that keeps individual effort from quietly declining as the team scales.

This is Dutch Management × Vietnamese Mastery applied to team-scaling dynamics itself: governance that structures growing teams to preserve individual accountability, paired with execution that maintains attributable ownership rather than diffusing responsibility as headcount increases. Explore how Manifera structures [dedicated development teams](https://www.manifera.com/services/offshore-software-development/) to scale without losing individual accountability.

## Case Study: A Thessaloniki Company's Scaling Shortfall

Makedonia Systems, a Thessaloniki-based enterprise software company, had scaled its development team from seven to sixteen over a year, expecting roughly proportional output growth, but found feature delivery had increased by less than 40%, considerably below the expectation even after accounting for typical onboarding and coordination overhead.

Manifera's Amsterdam team, engaged to review the scaling shortfall, found that the larger team's structure had drifted toward a less individually attributable model — code review had become inconsistent and diffuse, with reviewers assuming someone else would catch issues, and feature ownership had become blurred across overlapping responsibilities. The team restructured around clearly attributable module ownership and individually accountable review responsibilities, restoring much of the missing output without any further headcount change.

> *"We'd assumed the shortfall was pure coordination overhead, the Brooks's Law problem everyone already knows about. Restructuring for individual accountability, not just better communication tools, is what actually closed most of the remaining gap."*
> — **VP of Engineering, Makedonia Systems**

Makedonia Systems now explicitly evaluates individual attribution and ownership clarity whenever team size grows, treating motivation-loss risk as a distinct planning factor alongside the more commonly discussed coordination overhead, and specifically resists the instinct to treat the gap as a hiring or motivation problem rather than a structural one.

## Coordination Loss vs. Motivation Loss in Growing Teams

| Factor | Coordination Loss | Motivation Loss |
|---|---|---|
| Underlying cause | Communication overhead scaling with team size | Reduced individual accountability as group grows |
| Well-known via | Brooks's Law | Ringelmann effect / social loafing research |
| Most visible in | Cross-team dependencies, integration work | Less individually attributable work (review, knowledge-sharing) |
| Mitigated by | Clear interfaces, reduced cross-team dependency | Preserved individual attribution and ownership |

## Planning Your Own Team Growth With Both Effects in Mind

Before scaling a development team and expecting proportional output growth, plan explicitly and deliberately for both coordination overhead and motivation-loss effects, and structure growth around preserved individual attribution to mitigate the second. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about scaling a team without losing individual accountability.

## Frequently Asked Questions

### (Scenario: CTO whose team scaled but output didn't scale proportionally) Why didn't our team's output roughly double when we roughly doubled headcount?

Beyond coordination overhead, a well-documented phenomenon called the Ringelmann effect means individual effort tends to decline in larger groups, particularly for less individually attributable work, contributing to output growth that falls short of headcount growth.

### (Scenario: engineering lead trying to distinguish two different scaling problems) Is this the same thing as the communication overhead problem described by Brooks's Law?

Related but distinct — Brooks's Law describes coordination cost from communication overhead, while the Ringelmann effect describes a separate motivation-loss mechanism where individuals feel less personally accountable as group size grows, even when coordination isn't the bottleneck.

### (Scenario: engineering manager trying to mitigate this in a software context) How can we reduce motivation loss as our development team grows?

Preserve clear individual attribution and ownership — specific modules, specific review responsibilities — since the Ringelmann effect's motivation-loss component is significantly mitigated when individual contribution remains visible and identifiable.

### (Scenario: CTO planning capacity for a growing team) Should we assume linear output scaling when planning capacity around headcount growth?

No — plan for both coordination overhead and motivation-loss effects reducing per-person output somewhat as team size grows, rather than assuming a simple headcount multiplication will predict actual output.

### (Scenario: engineering lead wondering if smaller teams are always better) Does this mean smaller teams are always more efficient than larger ones?

Not universally, but smaller or well-structured semi-autonomous sub-teams do tend to preserve more individual accountability, which is why restructuring a larger team around smaller, clearly-owned units often recovers some of the output a purely headcount-driven scaling loses.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO whose team scaled but output didn't scale proportionally) Why didn't our team's output roughly double when we roughly doubled headcount?", "acceptedAnswer": { "@type": "Answer", "text": "Beyond coordination overhead, the Ringelmann effect means individual effort tends to decline in larger groups, especially for less attributable work." } },
    { "@type": "Question", "name": "(Scenario: engineering lead trying to distinguish two different scaling problems) Is this the same thing as the communication overhead problem described by Brooks's Law?", "acceptedAnswer": { "@type": "Answer", "text": "Related but distinct — Brooks's Law is coordination cost; the Ringelmann effect is a separate motivation-loss mechanism." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to mitigate this in a software context) How can we reduce motivation loss as our development team grows?", "acceptedAnswer": { "@type": "Answer", "text": "Preserve clear individual attribution and ownership, since motivation loss is mitigated when contribution stays visible and identifiable." } },
    { "@type": "Question", "name": "(Scenario: CTO planning capacity for a growing team) Should we assume linear output scaling when planning capacity around headcount growth?", "acceptedAnswer": { "@type": "Answer", "text": "No — plan for both coordination overhead and motivation-loss effects reducing per-person output as team size grows." } },
    { "@type": "Question", "name": "(Scenario: engineering lead wondering if smaller teams are always better) Does this mean smaller teams are always more efficient than larger ones?", "acceptedAnswer": { "@type": "Answer", "text": "Not universally, but smaller or well-structured sub-teams tend to preserve more individual accountability and recover lost output." } }
  ]
}
</script>
