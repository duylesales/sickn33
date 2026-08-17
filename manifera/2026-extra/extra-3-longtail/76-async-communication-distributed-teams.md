---
title: "Why the Best Distributed Teams Write More and Meet Less"
keywords: "dedicated development team, software dev team, developer team, team of developers"
buyer_stage: "Consideration"
target_persona: "A"
---

# Why the Best Distributed Teams Write More and Meet Less

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why the Best Distributed Teams Write More and Meet Less",
  "description": "Why written, asynchronous communication outperforms real-time meetings for a distributed engineering team, and what a communication theory from the 1980s predicts about when each actually works.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/async-communication-distributed-teams" }
}
</script>

A CTO skeptical of distributed development teams often assumes the core risk is time zone overlap — not enough shared hours for real-time collaboration. Teams that actually work well across distance tend to have made a different, less obvious adjustment: they've deliberately shifted a large share of their communication away from real-time meetings and toward clear, written, asynchronous documentation, and that shift turns out to improve collaboration quality even when time zone overlap is available, not just when it isn't.

## Why "More Meetings" Isn't the Same as "Better Communication"

A colocated team defaults naturally to real-time conversation because it's genuinely low-friction when everyone's in the same room — a quick question gets a quick answer, and nobody has to think much about how to phrase it for someone reading it later without the original context. A distributed team that simply tries to replicate that same pattern over video calls, without adjusting for what's actually different about the medium, tends to produce meetings that run long, decisions that aren't clearly recorded, and context that lives only in the memory of whoever happened to be on the call, unavailable to anyone in a different time zone who wasn't.

## The Communication Theory That Explains When Each Medium Actually Works

Researchers Richard Daft and Robert Lengel, in influential work published through the 1980s, developed media richness theory, which ranks communication channels by how much contextual information they carry — tone, immediate feedback, nonverbal cues — and argues that a channel's effectiveness depends on matching its richness to the ambiguity of the message being communicated. A rich channel like face-to-face conversation is well suited to genuinely ambiguous, nuanced topics where immediate back-and-forth clarification adds real value. A leaner channel like written text is, counterintuitively, often better suited to unambiguous, well-defined information, precisely because it forces the sender to fully resolve the ambiguity before sending, rather than relying on real-time interaction to sort it out collaboratively as the conversation unfolds.

Daft and Lengel's framework directly explains why the best distributed teams don't just default to whichever channel feels most natural — they deliberately match channel to message. A genuinely ambiguous architectural trade-off, where real-time back-and-forth adds real value, still warrants a synchronous conversation, ideally scheduled during whatever overlap hours exist. A status update, a decision record, or a technical specification is actually better served by a rich channel's absence — the writer has to think the message through fully and unambiguously before sending it, producing a clearer, more useful, and more durable artifact than a verbal explanation in a meeting ever would, one that remains equally accessible to a teammate in a different time zone reading it six hours later as to someone who happened to be in the original conversation.

## What This Means Practically for a Distributed Engineering Team

- **Default to written documentation for anything unambiguous and reference-worthy** — decisions, specifications, status updates — since forcing full written clarity produces a better artifact than a live conversation would, independent of time zone considerations entirely.
- **Reserve real-time meetings specifically for genuinely ambiguous, high-stakes discussions**, where the rich, immediate back-and-forth a synchronous channel provides is actually adding real value, not just following the colocated-team default out of habit.
- **Treat written communication skill as a real, trainable engineering competency**, not an incidental byproduct of technical skill — a team that writes clearly asynchronously is functionally more collaborative across distance than one that communicates well only in person.
- **Measure whether a recurring meeting is actually serving an ambiguous-topic function**, or whether it's become a status-update ritual that a written async update would serve better, freeing the meeting time for genuinely ambiguous work instead.

## Why the Colocated Default Feels Right Even When It Isn't

Daft and Lengel's original research was conducted primarily on colocated organizational communication, before distributed teams and remote work were the norm they are today, which makes its application to distributed engineering teams worth explaining a bit further rather than assuming it translates automatically. The theory's insight was that richer channels aren't universally better — they're better specifically for ambiguous messages, and can actually introduce noise and inefficiency for unambiguous ones, since a live conversation invites tangents, requires everyone's simultaneous attention regardless of whether they need the full message, and produces no durable record unless someone separately takes the effort to write one up afterward.

A colocated team defaults to rich, synchronous channels for almost everything not because that's actually optimal by Daft and Lengel's framework, but because the cost of doing so feels low when everyone's already in the same building — a quick hallway conversation costs little in the moment, even for a message that would have worked fine as a two-line message. A distributed team doesn't have that same low-cost default available, and that constraint, uncomfortable as it initially feels, is precisely what forces a distributed team to actually apply Daft and Lengel's matching principle deliberately rather than defaulting to richness out of sheer convenience. This is a genuine, underappreciated case where the distributed team's structural constraint produces better communication discipline than the colocated team's comfortable default ever forces it to develop.

## Manifera's Approach: Matching Channel to Message as Standard Practice

- **Amsterdam (Governance/Communication Discipline):** Dutch project leads default to clear, written documentation for decisions, specifications, and status updates, reserving synchronous meetings for genuinely ambiguous discussions that benefit from real-time back-and-forth.
- **Vietnam (Execution/Written Communication Competency):** The engineering pod is trained specifically in clear technical writing as a core professional skill, ensuring async updates and documentation are genuinely useful reference artifacts, not a weaker substitute for a meeting that didn't happen.

This is Dutch Management × Vietnamese Mastery applied to distributed communication itself: governance that deliberately matches communication channel to message type, paired with execution built on strong written communication as a real, developed competency. Explore how Manifera structures [dedicated development teams](https://www.manifera.com/services/offshore-software-development/) for effective distributed collaboration.

## Case Study: A Trondheim Company's Meeting Reduction

Trøndersk Teknologi, a Trondheim-based logistics software company, had structured its relationship with a previous offshore team around daily status call meetings, assuming frequent real-time contact was the best way to stay aligned across the time difference — a pattern that consumed a meaningful share of each day's limited overlap window without noticeably improving project clarity.

Manifera's Amsterdam team proposed restructuring communication around Daft and Lengel's framework directly: daily status updates moved to written, asynchronous documentation, reserving the shared overlap window specifically for genuinely ambiguous discussions that actually needed real-time back-and-forth. The change freed a significant portion of the overlap window for higher-value synchronous conversation, while the written status updates proved more useful as a reference than the verbal updates they replaced had ever been.

> *"We'd assumed more live contact meant better alignment. It turned out most of what we were saying live didn't need to be live at all, and writing it down forced a clarity the calls had never actually produced."*
> — **Engineering Director, Trøndersk Teknologi**

Trøndersk Teknologi now explicitly evaluates any new recurring meeting against the question of whether its content is genuinely ambiguous enough to need real-time discussion, defaulting to written async communication whenever the answer is no — a discipline the engineering director admits their previous colocated-style habits had never actually forced them to develop before the distributed arrangement made the old default impractical.

## Matching Communication Channel to Message Type

| Message Type | Ambiguity Level | Best Channel |
|---|---|---|
| Status update | Low | Written, asynchronous |
| Technical specification | Low to moderate | Written, asynchronous |
| Architectural trade-off discussion | High | Synchronous, real-time |
| Urgent production incident | High | Synchronous, real-time |
| Routine decision record | Low | Written, asynchronous |

## The Documentation Byproduct Nobody Plans For but Everyone Values Later

A secondary benefit of shifting unambiguous communication to written channels, rarely the original motivation but consistently reported once teams make the switch, is that the resulting body of written status updates, decisions, and specifications becomes a genuinely useful institutional record over time — something a stream of verbal meeting updates almost never produces on its own. A new team member joining months later can read through past written decisions to understand how the system reached its current state, in a way that "ask someone who remembers the meeting" simply can't replicate reliably, especially once the people who were actually on that call have moved to other projects or left the company entirely.

This compounding documentation benefit is worth naming explicitly because it changes the calculus on whether the upfront effort of writing clearly is worth it relative to the lower-friction alternative of just talking it through live. The real comparison isn't "five minutes of writing versus five minutes of talking" — it's five minutes of writing that remains useful indefinitely versus five minutes of talking that provides value only to the people in the room, only for as long as they happen to remember it accurately.

## Restructuring Your Own Distributed Team's Communication

Audit your team's recurring meetings against the ambiguity of what they actually cover — anything unambiguous and reference-worthy is likely better served by written, asynchronous documentation instead. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about structuring communication for a distributed dedicated team.

## Frequently Asked Questions

### (Scenario: CTO skeptical that a distributed team can communicate well) Can a distributed team really communicate as effectively as a colocated one?

Yes, often more effectively for certain message types — written asynchronous communication, done well, produces clearer, more durable artifacts than verbal updates in a meeting, independent of time zone considerations.

### (Scenario: engineering lead trying to reduce meeting load) How do I decide which recurring meetings should become written async updates instead?

Ask whether the meeting's actual content is genuinely ambiguous enough to benefit from real-time back-and-forth — if it's mostly status reporting or decisions that don't need live discussion, it's a strong candidate for a written format.

### (Scenario: team lead worried async communication reduces connection) Does moving communication to written, async channels hurt team relationships and trust?

Not inherently — relationship-building benefits from some synchronous contact, but that's a different function from information transfer, and the two can be intentionally separated rather than assuming all communication needs to be real-time.

### (Scenario: engineering manager trying to improve async communication quality) What's the most important skill for making asynchronous communication actually work well?

Clear, unambiguous writing — treating it as a real, developed professional skill rather than an informal byproduct of technical competence significantly changes how useful async updates and documentation actually turn out to be.

### (Scenario: CTO trying to apply this with limited time zone overlap) Does this approach reduce the importance of time zone overlap for a distributed team?

It reduces reliance on overlap for routine communication, though genuinely ambiguous, high-stakes discussions still benefit from some synchronous time — the goal is using limited overlap hours for the conversations that actually need them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO skeptical that a distributed team can communicate well) Can a distributed team really communicate as effectively as a colocated one?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, often more effectively for certain message types — written async communication produces clearer, more durable artifacts than verbal meeting updates." } },
    { "@type": "Question", "name": "(Scenario: engineering lead trying to reduce meeting load) How do I decide which recurring meetings should become written async updates instead?", "acceptedAnswer": { "@type": "Answer", "text": "Ask whether the content is genuinely ambiguous enough to benefit from real-time back-and-forth — status reporting is a strong candidate for written format." } },
    { "@type": "Question", "name": "(Scenario: team lead worried async communication reduces connection) Does moving communication to written, async channels hurt team relationships and trust?", "acceptedAnswer": { "@type": "Answer", "text": "Not inherently — relationship-building and information transfer are different functions that can be intentionally separated." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to improve async communication quality) What's the most important skill for making asynchronous communication actually work well?", "acceptedAnswer": { "@type": "Answer", "text": "Clear, unambiguous writing, treated as a real, developed professional skill rather than an informal byproduct of technical competence." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to apply this with limited time zone overlap) Does this approach reduce the importance of time zone overlap for a distributed team?", "acceptedAnswer": { "@type": "Answer", "text": "It reduces reliance on overlap for routine communication, while reserving limited overlap hours for genuinely ambiguous discussions." } }
  ]
}
</script>
