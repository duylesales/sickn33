---
Title: "The Three Questions to Ask Any Developer Before You Hire Them"
Keywords: developer hiring questions, technical due diligence, AI-generated codebase audit, freelance developer vetting, production hardening, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# The Three Questions to Ask Any Developer Before You Hire Them

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Three Questions to Ask Any Developer Before You Hire Them",
  "description": "Most founders vetting a developer to finish their AI-generated prototype ask about tech stacks and rates. The three questions that actually predict whether the work gets done safely are different, and almost nobody asks them.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/three-questions-ask-any-developer-before-hire"
  }
}
</script>

A founder with a working Lovable or Cursor prototype and a growing sense that it needs professional hardening usually does what seems reasonable: posts a job, screens a few candidates, and asks about their stack, their rate, and their availability. None of those questions predict whether the person can be trusted with a production codebase that already has real users leaning on it. There are three questions to ask any developer before you hire them that actually do, and the reason almost nobody asks them is that they don't sound like technical questions at all — they sound like questions about judgment, which is exactly what's being tested. Founders who skip them tend to discover the gap only after the engagement has already started, when scope has quietly widened and the invoice no longer matches what was actually needed.

## Why the Usual Interview Questions Don't Work for This Job

"What's your experience with React?" or "Have you worked with Supabase before?" screens for familiarity with tools, and tool familiarity is real but almost beside the point for the specific job of hardening an AI-generated prototype. The tools an AI builder produces are usually mainstream and well-documented — the risk was never that a competent developer wouldn't recognize the stack. The risk is that a developer who *does* recognize the stack treats a working prototype the way they'd treat any codebase they're unfamiliar with: as something to rewrite in their own preferred pattern, rather than something to audit and harden in place. Standard interview questions test for skill. They don't test for the specific instinct this job actually requires, which is closer to restraint than raw capability.

## Question One: "Walk Me Through the Last Time You Found a Security Gap in Someone Else's Code, Not Your Own"

This question filters for a specific, narrow experience: has this person actually done the work of reading unfamiliar code looking for what's wrong with it, as opposed to writing new code and trusting their own judgment about what's right? A developer who answers with a specific story — a hardcoded key they found in a client's repo, an authorization check that only lived in the frontend, a webhook endpoint accepting unsigned payloads — has done this work before and recognizes the pattern on sight. A developer who answers in generalities, or pivots to describing a project they built from scratch, likely hasn't spent real time in the specific posture this job demands: reading someone else's decisions charitably enough to understand them, and critically enough to find where they break.

## Question Two: "If You Found Something You'd Have Built Differently, What Would You Do About It?"

This question is designed to surface a tendency that quietly derails more hardening engagements than any technical shortfall: the urge to rebuild rather than repair. Many capable developers, faced with code they wouldn't have written themselves, default to replacing it, because rewriting from a blank page is often genuinely easier than understanding and modifying someone else's logic. The right answer to this question isn't "I'd leave it exactly as is" — sometimes a structure genuinely needs to change. The answer worth hiring for distinguishes between changes required to close a specific risk and changes that are simply a matter of personal preference, and defaults to the smallest intervention that actually closes the gap. A developer who can't articulate that distinction will, predictably, turn a two-week hardening engagement into an open-ended rebuild.

## Question Three: "What Happens If You Miss Something?"

This is the question that separates a freelance hire from an accountable engagement, and it's the one founders are most reluctant to ask directly because it sounds confrontational. It isn't — it's the single most practical question in the set, because it forces a concrete answer about what happens after the invoice is paid. A freelancer who shrugs, or describes the arrangement as strictly time-for-code with no ongoing responsibility, is telling you plainly that the relationship ends the moment the contract does, regardless of what surfaces in your codebase three weeks later. A structured provider with a defined process will have a specific answer — a warranty period, a scoped re-engagement process, a named point of contact — because accountability that only exists informally tends to evaporate exactly when it's needed most.

## Reading the Answers, Not Just Collecting Them

Asking the three questions is only half the exercise — the other half is resisting the urge to grade them like a quiz with a single correct answer. A confident, specific answer to the first question, paired with a vague or defensive answer to the second, is a meaningfully different candidate than one who's specific on all three, even though both might look equally strong on a resume. The pattern across all three answers matters more than any single one in isolation, because a developer who's genuinely strong on judgment tends to be consistent across all three — specific about past experience, measured about rebuilding, and concrete about accountability — while a developer who's strong in one area and weak in another is often compensating for a gap they haven't fully acknowledged to themselves, let alone to you.

## What the Answers Actually Reveal

None of these three questions test for coding ability, and that's deliberate — coding ability is the easiest thing to verify from a portfolio or a paid test task, and the thing founders already over-index on when vetting candidates. What these questions test for is judgment under exactly the conditions this specific job creates: unfamiliar code, ambiguous scope, and real consequences for getting it wrong. A candidate's answers to these three questions, taken together, predict far more accurately than a technical screen whether hiring them will close your production gap or quietly widen it into a rebuild you never agreed to and can't easily stop once it's underway. This matters most for exactly the founder least equipped to catch the drift after the fact — a non-technical or lightly technical founder who has no independent way to verify, three weeks into an engagement, whether the growing scope in front of them is genuinely necessary or simply where an unchecked instinct to rewrite eventually led.

[LaunchStudio](https://launchstudio.eu/en/) was built specifically around answers to all three of these questions — a defined audit process, a documented default toward hardening rather than rebuilding, and Manifera's 11+ years of production engineering accountability standing behind every engagement.

[Tell us what you've built and what you're worried about](https://launchstudio.eu/en/#contact) — the same scoping conversation these three questions are meant to shortcut.

## Real example

### A Technical Solo Founder in Action: The Interview That Almost Went Wrong

Merijn Aaldering, a former recruiter turned indie hacker in Hattem, built HireGrip, an AI-assisted candidate screening tool for small agencies, using Cursor with heavy AI-generated scaffolding around the parts he didn't have time to write by hand. Merijn could read code well enough to get by, but not well enough to trust his own judgment on security, so he posted a freelance job to find someone to finish hardening it before his first paying agency client went live.

The strongest-looking candidate, on paper, had the right stack experience and a competitive rate. But when Merijn asked the second of the three questions — what he'd do about code he wouldn't have written himself — the candidate answered that he'd "probably just rebuild the backend cleaner," estimating four weeks at an hourly rate roughly triple what Merijn had budgeted, for work Merijn hadn't actually identified as broken. When Merijn pushed for specifics on what exactly was wrong with the existing backend, the answers stayed general — architectural preferences dressed up as necessity, rather than named, specific risks.

Merijn brought HireGrip to LaunchStudio instead, and the scoping call found exactly two real gaps — an authorization check missing at the API layer and an unrate-limited login endpoint — both fixable without touching the backend structure the candidate had wanted to rebuild.

**Result:** Both gaps were closed within the original two-week timeline Merijn had planned for, at a fraction of the rebuild quote, and HireGrip's first agency client went live with an audit report Merijn could actually point to.

> *"The question that saved me wasn't about his skills. It was asking what he'd do with code he didn't write himself — and hearing 'rebuild it' when nothing was actually broken."*
> — **Merijn Aaldering, Founder, HireGrip (Hattem)**

**Cost & Timeline:** €1,450 (Launch Ready Package, authorization and rate-limiting hardening) — live in 8 business days.

---

## Frequently Asked Questions

### Why don't standard technical interview questions catch this problem?

Standard questions test tool familiarity and general coding skill, which are easy to verify and largely beside the point — the actual risk in this specific job is a developer's instinct to rewrite unfamiliar code rather than audit and harden it in place, which a stack-focused interview never surfaces.

### Should I ask these three questions even if I'm hiring a full-time employee, not a freelancer?

Yes — the judgment these questions test for, restraint around rebuilding and clarity about accountability, matters regardless of the employment structure, though the "what happens if you miss something" question naturally has a different, more built-in answer for a full-time hire than a contractor.

### What's a red flag answer to the second question, about rebuilding versus repairing?

A candidate who can't distinguish between a change required to close a specific security or reliability gap and a change that's simply their personal architectural preference is likely to expand scope well beyond what your codebase actually needs, as Merijn's near-miss illustrates.

### Is it reasonable to ask these questions before agreeing to pay for a paid test task?

Yes — these are judgment questions, not coding questions, and they're answerable in a short conversation before any paid work begins, which makes them a low-cost way to filter candidates before investing in a longer, paid evaluation.

### How does LaunchStudio's process answer these three questions differently than a typical freelance hire?

LaunchStudio's engagements start from a documented audit against known risk categories, default to the smallest fix that closes each specific gap rather than a rebuild, and carry Manifera's accountability and 11+ years of engineering track record behind the outcome, rather than ending informally when an invoice is paid.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why don't standard technical interview questions catch this problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standard questions test tool familiarity and general coding skill, which are easy to verify and beside the point, since the real risk is a developer's instinct to rewrite unfamiliar code rather than harden it in place."
      }
    },
    {
      "@type": "Question",
      "name": "Should I ask these questions even if I'm hiring a full-time employee, not a freelancer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the underlying judgment matters regardless of employment structure, though accountability naturally looks different for a full-time hire than a contractor."
      }
    },
    {
      "@type": "Question",
      "name": "What's a red flag answer to the question about rebuilding versus repairing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A candidate who can't distinguish a change required to close a specific gap from a change that's just personal preference is likely to expand scope well beyond what the codebase actually needs."
      }
    },
    {
      "@type": "Question",
      "name": "Is it reasonable to ask these questions before paying for a test task?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, these are judgment questions answerable in a short conversation, making them a low-cost filter before investing in a paid evaluation."
      }
    },
    {
      "@type": "Question",
      "name": "How does LaunchStudio's process answer these three questions differently than a typical freelance hire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio audits against known risk categories, defaults to the smallest fix that closes each gap, and carries Manifera's accountability and 11+ years of engineering experience behind every outcome."
      }
    }
  ]
}
</script>
