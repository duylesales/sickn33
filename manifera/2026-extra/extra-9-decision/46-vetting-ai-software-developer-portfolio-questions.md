---
title: "Vetting an AI Software Developer: Portfolio Questions That Matter"
keywords: "ai software developer, portfolio review questions, vetting ai talent, ai developer interview, team augmentation ai skills"
buyer_stage: "Decision"
target_persona: "IT Manager"
---

# Vetting an AI Software Developer: Portfolio Questions That Matter

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vetting an AI Software Developer: Portfolio Questions That Matter",
  "description": "A depth-focused list of portfolio review questions for IT Managers vetting an AI software developer before augmenting an existing team, designed to distinguish genuine ownership from adjacent involvement.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/vetting-ai-software-developer-portfolio-questions" }
}
</script>

A portfolio of AI projects is a lot like a restaurant's tasting-menu photos: beautifully lit, professionally arranged, and almost entirely unable to tell you whether the person in front of you can actually run the kitchen during a dinner rush. Every candidate presenting themselves as an AI software developer will have a portfolio, and nearly every portfolio will look impressive at first glance — polished GitHub repos, clean demo videos, confident project descriptions. What that portfolio can't tell you on its own is which parts the candidate actually built, what happened to the project after the screenshot was taken, and whether they can operate under the pressure of a live production issue rather than a controlled demo.

For an IT Manager augmenting an existing team with AI-specific expertise, this distinction matters more than almost any other hiring variable, because a team augmentation hire is expected to contribute meaningfully within weeks, not months, and there's little margin for discovering the gap between portfolio and reality after the person has already started. The following list walks through the specific portfolio questions worth asking, each one designed to test a different dimension of genuine capability rather than surface-level polish.

## 1. "Which part of this project did you personally build, versus contribute to as part of a team?"

This is the single most important question on this list, and it's the one candidates answer least precisely by default. Many AI portfolio projects are team efforts, academic collaborations, or open-source contributions where a candidate's actual role ranges from primary architect to minor contributor — but the portfolio description rarely makes that distinction explicit. Ask directly, and listen for specificity: a candidate with genuine ownership will describe exactly which modules, decisions, or components were theirs, often unprompted, because they remember the details of work they actually did. A candidate who answers in vague collective terms — "we built a recommendation engine" — without ever shifting to "I" for any specific component is showing you a team credit being presented as an individual accomplishment.

## 2. "What was the actual production traffic or data volume this system handled?"

A model that performs well on a curated dataset of a few thousand records behaves very differently from one operating against millions of real-world, messy production records, and the engineering challenges at each scale are genuinely different disciplines. Ask for concrete numbers — requests per second, total users, data volume processed daily — and note whether the candidate has this at their fingertips or has to estimate vaguely. A candidate who worked at meaningful production scale will remember specific numbers because scale-related problems (latency, cost, infrastructure limits) were a real part of their daily work; a candidate who only ever worked in a research or prototype context typically won't have precise figures because scale was never the constraint they were solving for.

## 3. "Walk me through a decision on this project you'd make differently today."

This question tests both technical judgment and honesty simultaneously, and it's remarkably hard to fake convincingly. A candidate with genuine hands-on experience will have a specific, often slightly uncomfortable answer — a technology choice that created technical debt, a data labeling approach that introduced bias they didn't catch until later, an architecture decision that made scaling harder than it needed to be. The specificity and self-awareness of the answer matters far more than the particular mistake itself; every real practitioner has one of these stories, and a candidate who claims their approach was correct in hindsight on every project is either inexperienced or not being fully candid with you.

## 4. "What happened to this project after you moved on — is it still running?"

Portfolios almost universally stop at the launch or handoff moment, because that's the most photogenic part of any project's lifecycle. Ask what happened afterward: did the system continue running in production, did it get replaced, did anyone maintain it. A candidate who stays in touch with a project's fate, even loosely, demonstrates the kind of ownership mentality that predicts good behavior on your team — someone who cares whether their work actually lasted, not just whether it launched successfully. A candidate who has genuinely never wondered what happened next is telling you something about how they relate to their own work once it's out of sight.

## 5. "Can you sketch the actual architecture for me, not just describe the outcome?"

Ask the candidate to describe, in their own words and ideally on a shared whiteboard or screen, how data actually flowed through their system — from ingestion through processing to output — rather than restating the polished project summary from their portfolio page. Genuine builders can do this fluidly because they lived inside the architecture daily; candidates who contributed a narrower slice, or who are describing someone else's project as their own, tend to struggle with the connective details between components even if they can describe each component individually and correctly.

## 6. "What was the most tedious or unglamorous part of this project, and how did you handle it?"

Every real AI project involves substantial unglamorous work — data cleaning, label quality review, handling edge cases in production, writing monitoring code that nobody will ever see in a demo. A candidate with genuine hands-on experience will have a specific, often mildly exasperated story about this kind of work, because it's an unavoidable part of building anything real. A candidate whose entire portfolio narrative jumps straight from problem statement to polished result, with no mention of the tedious middle, is either omitting that part because someone else did it, or hasn't actually done the full lifecycle of building an AI system themselves.

## 7. "Who can I speak with to verify your role on this project?"

This is the question that puts everything above to the test. A candidate with genuine, verifiable ownership will offer a specific former manager, teammate, or client contact readily, often before you finish asking. Hesitation, vague deflection, or an inability to provide any verifiable contact for a supposedly significant portfolio project is one of the strongest single red flags available in the entire vetting process — far stronger than any technical answer, because it tests whether the story holds up under independent scrutiny rather than just under your own questioning.

## Common Excuses and How to Respond to Them

Even strong candidates will occasionally give a weak answer to one of these questions, and how they respond to gentle follow-up pressure is often more informative than the original answer itself. A few patterns come up often enough to be worth preparing for directly.

**"It's under NDA, so I can't share specifics."** This is a legitimate constraint for some portfolio projects, but a candidate can almost always describe their architecture and decision-making in generic, non-identifying terms without revealing client names or proprietary data. If a candidate uses NDA as a reason to avoid all specificity rather than just client-identifying details, push gently for the architectural and decision-level detail that doesn't require breaking confidentiality — a genuine builder can usually find a way to answer within those constraints.

**"I don't remember the exact numbers, but it was a lot of traffic."** Reasonable people forget precise figures over time, especially for older projects, so don't treat imprecision alone as disqualifying. What matters is whether the candidate can still describe the order of magnitude and the specific engineering challenges that scale created — a genuine builder retains the texture of the problem even after forgetting the exact figure, while someone who never actually worked at that scale won't have that texture to draw on regardless of how the question is framed.

**"I was mostly focused on the research side, not the production side."** This is a fair and common specialization, and it's worth taking seriously rather than treating as a disqualifying dodge — plenty of strong AI professionals genuinely specialize in research or model development without owning production deployment. The follow-up here should shift the remaining questions to match: ask instead about experimental rigor, how they validated results, and how they collaborated with whoever did own the production side, since the underlying goal is verifying genuine expertise in whatever their actual specialization is, not forcing every candidate into a production-generalist mold that doesn't match their real career path.

## Turning This List Into a Repeatable Vetting Process

Used together, these seven questions convert a static portfolio review into something closer to a structured audit, and the pattern across all seven answers matters more than any single one in isolation. A candidate who answers most of these with specific, verifiable detail is very likely the genuine builder their portfolio implies; a candidate who answers most of them vaguely, regardless of how polished the portfolio itself looks, is showing you a gap worth taking seriously before extending an offer for a role expected to contribute independently within weeks.

It's also worth keeping a simple written record of how each candidate answered each question, rather than relying on memory after a full day of back-to-back interviews. A short note after each question — specific, vague, or evasive — turns what would otherwise be a subjective overall impression into a comparable scorecard across your entire shortlist, which matters enormously when a hiring decision involves more than one interviewer and you need to reconcile different reads on the same candidate afterward. This record also becomes useful evidence later if a hiring decision is ever questioned, since it documents the specific reasoning behind the choice rather than a vague sense that one candidate "felt stronger" than another.

For IT Managers who don't have the bandwidth to run this level of scrutiny across every candidate in a hiring pipeline, this is precisely the vetting discipline that a mature offshore partner should already be applying before a candidate ever reaches your interview stage. Manifera's [offshore software development](https://www.manifera.com/services/offshore-software-development/) engagements run every proposed AI engineer through a version of this same portfolio audit internally, verifying ownership claims and production history before a CV is presented to a client — which is a bridge between European business standards and APAC development velocity that removes much of this vetting burden from your team's plate. This track record spans 160-plus delivered projects for 120-plus global clients, a scale that has let Manifera build and refine exactly this kind of vetting discipline over more than a decade rather than treating it as a one-off exercise for each new hire.

For legacy system modernization work specifically, where AI-assisted analysis of existing codebases is increasingly common, our [custom software development](https://www.manifera.com/services/custom-software-development/) services page outlines how augmented teams are typically scoped and integrated with an existing engineering organization's existing tools and processes.

## Put This List to Work on Your Next Shortlist

The next AI software developer candidate who presents an impressive portfolio deserves these seven questions before any offer discussion begins, not after. Each one targets a different dimension of genuine capability — ownership, scale experience, judgment, follow-through, architectural fluency, tolerance for unglamorous work, and verifiability — and together they're considerably harder to fake convincingly than any single technical interview question, however difficult.

Request a shortlist of vetted AI engineers within 48 hours from Manifera's delivery team, each already screened against this same portfolio-depth standard before you ever see a resume.

## Frequently Asked Questions

### How do I tell if an AI software developer's portfolio project was a genuine individual contribution?

Ask which specific components, modules, or decisions were theirs personally versus the broader team's, and listen for whether they shift naturally into first-person specifics or stay in vague collective language throughout. Genuine individual contributors typically remember granular details unprompted; someone presenting a team credit as an individual accomplishment tends to stay general.

### What is the most important portfolio question to ask an AI developer candidate?

Asking who can verify their specific role on a portfolio project tends to be the single most revealing question, since it tests whether the story holds up under independent scrutiny rather than just your own follow-up questions. Hesitation or an inability to provide a verifiable contact is one of the strongest red flags in the entire vetting process.

### Should a candidate's portfolio projects match the exact industry of my company?

Not necessarily. The underlying skills this vetting process tests — genuine ownership, production experience, architectural fluency, and honest self-assessment — transfer across industries more readily than specific domain knowledge does. A strong AI software developer from an unrelated industry with clear evidence of these traits is often a better hire than an industry-matched candidate who can't answer these questions convincingly.

### How long should a portfolio-based vetting conversation take?

A thorough conversation covering all seven questions in this list typically takes 45 to 60 minutes when done conversationally rather than as a rigid checklist, allowing time to follow up on interesting or evasive answers. Rushing this process to fit a shorter interview slot tends to reduce its effectiveness significantly.

### Is it worth hiring an AI software developer who has strong technical skills but a thin portfolio?

Yes, in many cases, provided the technical skills are verified through a working session or technical interview rather than relying on the portfolio alone. A thin portfolio often reflects limited opportunity rather than limited ability, especially for candidates earlier in their career, and shouldn't automatically be weighted the same as a portfolio that raises the specific red flags described in this guide.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I tell if an AI software developer's portfolio project was a genuine individual contribution?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ask which specific components or decisions were theirs personally versus the broader team's, and listen for whether they shift into first-person specifics or stay in vague collective language. Genuine individual contributors typically remember granular details unprompted." }
    },
    {
      "@type": "Question",
      "name": "What is the most important portfolio question to ask an AI developer candidate?",
      "acceptedAnswer": { "@type": "Answer", "text": "Asking who can verify their specific role on a portfolio project tends to be the most revealing question, since it tests whether the story holds up under independent scrutiny. Hesitation or an inability to provide a verifiable contact is a strong red flag." }
    },
    {
      "@type": "Question",
      "name": "Should a candidate's portfolio projects match the exact industry of my company?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily. Genuine ownership, production experience, and architectural fluency transfer across industries more readily than specific domain knowledge does, so a strong candidate from an unrelated industry can be a better hire than a poorly-vetted industry match." }
    },
    {
      "@type": "Question",
      "name": "How long should a portfolio-based vetting conversation take?",
      "acceptedAnswer": { "@type": "Answer", "text": "A thorough conversation covering all seven questions typically takes 45 to 60 minutes when done conversationally, allowing time to follow up on interesting or evasive answers. Rushing this process tends to reduce its effectiveness." }
    },
    {
      "@type": "Question",
      "name": "Is it worth hiring an AI software developer who has strong technical skills but a thin portfolio?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, in many cases, provided technical skills are verified through a working session rather than relying on the portfolio alone. A thin portfolio often reflects limited opportunity rather than limited ability." }
    }
  ]
}
</script>
