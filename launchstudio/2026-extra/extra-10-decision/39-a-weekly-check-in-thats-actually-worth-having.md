---
Title: "How to Run a Weekly Check-In That's Actually Worth Having"
Keywords: weekly check-in agenda founder, effective status meeting, surfacing risk early, non-technical founder meeting, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# How to Run a Weekly Check-In That's Actually Worth Having

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Run a Weekly Check-In That's Actually Worth Having",
  "description": "A specific 30-minute agenda for a founder's weekly check-in with an engineering partner, designed to surface risk early rather than produce a status recitation. Helps non-technical founders decide what to actually ask in the meeting they're already having.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/a-weekly-check-in-thats-actually-worth-having" }
}
</script>

Here's the same weekly call, run two different ways.

**Version one:** "How's it going?" "Good, making progress." "Any blockers?" "Not really, just the usual." Thirty minutes pass. Everyone hangs up feeling vaguely reassured. Twelve days later, the founder learns the payment integration has been stuck for a week on a decision nobody flagged as urgent, because "not really, just the usual" is what people say when a question hasn't been framed sharply enough to surface it.

**Version two:** same two people, same thirty minutes, same week of work behind it. But the questions are different, and by minute ten a specific risk is on the table — a webhook integration that depends on an answer from a third-party support team, sitting unanswered for four days — with a plan already forming for what happens if it isn't resolved by Thursday. Nothing about the underlying work changed between these two versions of the call. What changed is whether the meeting was built to extract a status, or built to surface a risk.

Most founder check-ins default to version one, because "how's it going" is the natural thing to ask and "good, making progress" is the natural thing to hear. Getting to version two takes a specific, repeatable structure — not more time, not more technical fluency, just a different set of questions asked in a different order.

## What to Do With What You Hear

Surfacing a risk in minute 10 is only useful if it changes what happens in minute 11. Two habits make the difference between a check-in that surfaces problems and one that surfaces them and then does nothing about it anyway. First, when a blocker or looming risk comes up, ask for a specific next step and a specific owner before moving to the next agenda item — "who's chasing the third-party support ticket, and when do we check back if it's still unanswered" — rather than letting it sit as a noted concern with no clear action attached. Second, if the same risk gets mentioned two weeks in a row without resolution, that's the moment to escalate it outside the regular cadence rather than letting it become a permanent fixture of the weekly update, quietly normalised by repetition.

## Why "How's It Going" Fails as a Question

The problem with an open-ended status question isn't that people lie in response to it — it's that it invites an averaged answer. If a week contained four smooth days and one seriously blocked one, "how's it going" naturally produces "pretty good, on track," because the respondent is summarising the whole week rather than surfacing the one thing that actually matters. A good check-in structure doesn't ask for a summary. It asks for the outliers directly, because outliers are where risk lives and summaries are where risk hides.

This isn't a trust issue or a communication failing on either side — it's simply how open questions work. Replacing them with specific, risk-shaped questions is the entire fix, and it costs nothing beyond deciding to ask differently.

## The 30-Minute Agenda

**Minutes 0–5: What shipped since we last spoke, tested against the outcome, not the task list.** Not "what did you work on" but "what can I actually use or verify now that I couldn't last week." This grounds the meeting in something real rather than a description of effort, and it's your chance to do quick outcome testing live if something is ready (see article 33 in this series on testing outcomes rather than process).

**Minutes 5–12: What's currently blocked, and by whom.** Ask this directly: "is anything stuck right now, and is it stuck on you, on me, or on something outside both of us?" This single framing does more work than any other question in the agenda, because it forces a specific answer instead of an averaged one, and it immediately tells you whether the blocker needs your decision (see article 31 on the specific decisions only founders can make), your engineer's technical judgment, or a third party like a payment provider's support team.

**Minutes 12–18: What's likely to become a problem in the next week, even if it isn't one yet.** This is the question version-one check-ins never ask, and it's the single highest-value five minutes in the whole meeting. Phrase it as "if something in the next week is going to go sideways, what's your best guess at what it'll be?" A good engineering partner will have an honest answer to this more often than founders expect — engineers usually sense a looming risk (an ambiguous third-party API, an assumption that hasn't been verified yet) well before it becomes an actual blocker, but rarely volunteer it unless asked directly, because it isn't a problem yet and raising unconfirmed problems can feel presumptuous.

**Minutes 18–23: Any decisions waiting on me, batched from the week.** Rather than trickling in throughout the week (though genuinely urgent ones still should), non-urgent business decisions can queue for this slot specifically. Run through the open-decisions list described in article 31 and clear what's on it.

**Minutes 23–27: Anything I need to tell you that changes the picture.** Your turn. A customer commitment that's shifted, a new deadline, a piece of context that affects priority. This is where you contribute the business information only you have — don't skip it because the meeting feels like it's "their" update; half the value of a founder check-in is what flows in the other direction.

**Minutes 27–30: Confirm what happens before the next check-in.** One sentence each: what's being worked on, what you're deciding or providing, when the next blocker-relevant update should happen if something can't wait a week. This closes the loop so nothing drifts on the assumption that "we'll talk about it next time."

## Why the Order Matters

Notice that blockers and looming risks come before decisions-waiting-on-you and your own updates. This is deliberate: if you ask about your own open decisions first, the conversation orients around your to-do list rather than the build's actual state, and a looming risk mentioned in passing at minute 25 gets six minutes of attention instead of the eighteen it might deserve. Front-loading the risk-surfacing questions means the most consequential information comes out while there's still time in the meeting to actually discuss it, rather than being squeezed in at the end because time ran out.

## What This Agenda Deliberately Leaves Out

**Task-by-task time accounting.** "How many hours did the migration take" doesn't belong in this meeting on a fixed-price engagement — it's an audit question, not a risk-surfacing one, and asking it shifts the meeting's whole register from partnership to oversight (see article 33 in this series on the product-owner/project-manager distinction).

**Implementation walkthroughs you can't evaluate.** If your engineer starts explaining a technical approach in detail during minute 3, it's fine to say "I trust that call, is there a business implication I should know about?" and move on. You're not obligated to sit through detail you have no way to judge and no decision attached to.

**Review of every small change since last time.** A comprehensive changelog belongs in written form you can scan asynchronously, not in a live meeting's limited thirty minutes. Use the meeting for what needs a conversation — risk, decisions, judgment calls — and let anything purely informational live in a shared doc or channel instead.

## Adjusting the Cadence and Length

Thirty minutes weekly is a solid default for a Launch Ready engagement running one to three weeks, but it isn't universal. A very short engagement (under a week) might compress this into two fifteen-minute check-ins rather than one weekly call, simply because a week doesn't fit inside the build. A longer Launch & Grow engagement with an ongoing monthly plan might run this same agenda less frequently once the initial build stabilises — biweekly, then monthly — because the risk-surfacing value drops once the product is live and stable rather than actively being built. The agenda's shape stays the same regardless of frequency; only the cadence should flex with how much is actually changing week to week.

## A Note on Who Should Be in the Room

If your engagement involves more than one engineer, resist the instinct to include everyone in your weekly check-in "to stay close to the whole team." A single point of contact — a lead engineer who has visibility into the full picture — can answer the agenda above more completely and more honestly than a group call where individual contributors are each reporting only on their own slice and reluctant to speculate about someone else's. Group calls also tend to revert to version-one behaviour, because a risk that feels comfortable to admit one-on-one often gets softened in front of peers.

If you have a co-founder or an internal team member who also needs visibility into the build, a short written summary after your check-in — three or four lines covering what shipped, what's blocked, and what's being watched — serves that need better than adding more people to the live conversation itself. Keep the risk-surfacing conversation small; distribute the outcome of it widely.

## What Changes When You Actually Run It This Way

The measurable difference isn't in how the meeting feels — though founders consistently report version two feeling less like a status theatre performance and more like an actual working session. The measurable difference is in when problems surface. A blocker raised in minute 8 of a Tuesday check-in gets a full week of runway to resolve before it threatens a deadline. The same blocker, unasked-for and unmentioned until it becomes unavoidable, often surfaces with two or three days of runway left — the exact gap between a minor scheduling adjustment and a genuine crisis.

This is the same principle LaunchStudio's own engagement structure is built around: short, fixed-scope builds succeed or fail largely on whether risk surfaces early enough to route around, and Manifera's 11+ years of client delivery has made the weekly or twice-weekly structured check-in one of the most consistent predictors of an engagement finishing on schedule, across founders with wildly different levels of technical background. The agenda above is close to what LaunchStudio's own engineers use as a default starting point with new clients, adjusted per engagement.

If your current check-ins feel more like version one than version two, that's worth raising directly with whoever you're working with. And if you're about to start a build and want this structure in place from day one, [describe your project](https://launchstudio.eu/en/#contact) and ask how check-ins are run — the answer tells you a lot about how the rest of the engagement will go.

## Real example

### The Meeting That Started Surfacing Problems on Time

Lotte Faassen, founder of a subscription meal-planning app called Weekmenu, ran her first two weekly check-ins with an open "how's it going" format and came away both times reassured that everything was on track. In week three, four days before her planned launch date, her engineer told her the email-confirmation service integration had been failing intermittently since early in week two — a problem that had been present, unmentioned, through both of the "on track" check-ins, because it hadn't yet become a full blocker and nobody had asked a question sharp enough to surface a partial one.

After that scare, Lotte and her engineer switched to the structured agenda above, starting with the very next check-in. In the first structured call, the "what's likely to become a problem" question surfaced a genuine early warning: a rate limit on the recipe-image hosting service that hadn't caused an issue yet but was projected to, based on current growth, within about six weeks of launch. Because it surfaced with six weeks of runway instead of zero, the fix — moving to a different hosting tier — was scheduled calmly into the post-launch roadmap instead of becoming an emergency.

**Result:** the original launch date held after a two-day adjustment to fix the confirmation-email issue once it was properly surfaced, and the image-hosting rate limit was resolved during a planned week-six maintenance window rather than as an unplanned outage.

> *"I thought I was staying close to the build by checking in every week. I was actually just collecting reassurance. The new questions found the actual problems — including one that hadn't happened yet."*
> — **Lotte Faassen, Founder, Weekmenu**

**Cost & Timeline:** €3,300 (Launch & Grow Package) — live 2 days behind original date after the confirmation-email fix; no unplanned downtime post-launch.

## Frequently Asked Questions

### What if my engineering partner doesn't want to answer "what's likely to go wrong next week" because it feels speculative?

Frame it explicitly as a low-stakes guess, not a commitment: "I'm not holding you to this, I just want your honest instinct." Most engineers have a reasonably accurate sense of looming risk and will share it once they understand you're asking for a hunch, not a guarantee.

### Should this check-in happen over video, phone, or is a written async update just as good?

Live, even briefly, works better specifically for the risk-surfacing minutes, because a written update tends to report the same averaged, tidied-up status that a bad live question would also produce — the value here comes from a direct, specific question and a direct, specific answer in the moment, not from the format itself.

### What if nothing is blocked and there's no looming risk — does the meeting still need all 30 minutes?

No — a genuinely smooth week can produce a genuinely short check-in, and that's a feature, not a sign the meeting isn't working. The agenda is a ceiling for what to cover, not a floor you need to fill regardless of what's actually happening.

### How do I adapt this agenda if I'm working with an internal hire rather than an outside engineering partner?

The structure works identically — the questions are about surfacing risk and decisions, not about the nature of the working relationship. The main adjustment is cadence: an internal hire embedded full-time might warrant a shorter, more frequent version rather than one longer weekly call.

### Is it a bad sign if my engineering partner always says everything is fine and never flags a risk?

It's worth a direct, non-accusatory conversation rather than an assumption either way. Sometimes it genuinely means the work is going smoothly; sometimes it means the risk-surfacing questions aren't landing as intended, or minor concerns are being filtered out before they reach you. Asking "has anything ever felt shaky that you didn't mention" as a one-off retrospective question can clarify which it is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What if my engineering partner doesn't want to answer \"what's likely to go wrong next week\" because it feels speculative?", "acceptedAnswer": { "@type": "Answer", "text": "Frame it explicitly as a low-stakes guess, not a commitment. Most engineers have a reasonably accurate sense of looming risk and will share it once they understand you're asking for a hunch, not a guarantee." } },
    { "@type": "Question", "name": "Should this check-in happen over video, phone, or is a written async update just as good?", "acceptedAnswer": { "@type": "Answer", "text": "Live works better for the risk-surfacing minutes specifically, because a written update tends to report the same averaged status a bad live question would also produce. The value comes from a direct question and direct answer in the moment." } },
    { "@type": "Question", "name": "What if nothing is blocked and there's no looming risk — does the meeting still need all 30 minutes?", "acceptedAnswer": { "@type": "Answer", "text": "No. A genuinely smooth week can produce a genuinely short check-in, which is a feature, not a problem. The agenda is a ceiling for what to cover, not a floor you need to fill regardless of what's actually happening." } },
    { "@type": "Question", "name": "How do I adapt this agenda if I'm working with an internal hire rather than an outside engineering partner?", "acceptedAnswer": { "@type": "Answer", "text": "The structure works identically since the questions target risk and decisions, not the nature of the relationship. The main adjustment is cadence: an embedded full-time hire might warrant a shorter, more frequent version instead." } },
    { "@type": "Question", "name": "Is it a bad sign if my engineering partner always says everything is fine and never flags a risk?", "acceptedAnswer": { "@type": "Answer", "text": "Worth a direct, non-accusatory conversation rather than an assumption. It might genuinely be going smoothly, or the risk-surfacing questions might not be landing. Asking a one-off retrospective question can clarify which it is." } }
  ]
}
</script>
