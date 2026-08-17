---
title: "The Software Development Stages No One Explains Until You're Already Behind on One"
keywords: "software developer stages, stages software development, software development processes, software development cycle"
buyer_stage: "Awareness"
target_persona: "D"
---

# The Software Development Stages No One Explains Until You're Already Behind on One

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Understanding the Real Stages of Software Development",
  "description": "A plain-language walkthrough of what actually happens at each stage of software development, for a non-technical founder who's never managed a build before.",
  "step": [
    { "@type": "HowToStep", "name": "Discovery and requirements", "text": "Defining what's actually being built and why, before any code is written." },
    { "@type": "HowToStep", "name": "Design and architecture", "text": "Deciding how the system will be structured, before implementation begins." },
    { "@type": "HowToStep", "name": "Development", "text": "Actually writing and building the software against the agreed design." },
    { "@type": "HowToStep", "name": "Testing and QA", "text": "Verifying the software works as intended before it reaches real users." },
    { "@type": "HowToStep", "name": "Deployment and maintenance", "text": "Launching the software and supporting it through its ongoing life." }
  ]
}
</script>

Most first-time founders learn the actual stages of software development the hard way — by watching a project timeline slip at a specific stage they never even knew existed. Knowing the five stages in advance, and specifically what tends to go wrong at each one, changes a founder from a passive recipient of status updates into someone who can ask the right question before a delay becomes a surprise.

## Stage 1: Discovery and Requirements

This is where a vendor should be asking far more questions than they're answering, working to understand the actual business problem before proposing any solution. A rushed or skipped discovery stage is the single most common root cause of later scope disputes, because requirements that felt "obvious" to a founder often carry unstated assumptions a technical team can't read without being told explicitly. A discovery stage that produces a written, specific requirements document — not just a verbal understanding — is the stage most worth insisting on doing properly, since every later stage builds directly on what gets decided here.

## Stage 2: Design and Architecture

Before any code gets written, decisions get made about how the system will be structured: what the data model looks like, how different parts of the system will communicate, what happens under load, what happens when something fails. This stage is largely invisible to a non-technical founder, which is exactly why it's the stage most often rushed or skipped entirely by a lower-quality vendor eager to start showing visible progress. A founder can't evaluate architecture directly, but can ask whether it happened at all, and for how long, before development started.

## Stage 3: Development

The stage most founders picture when they think of "building the app" — and, counterintuitively, often the most predictable of the five once discovery and design have been done properly. Development delays are frequently blamed on this stage when the actual root cause was an inadequate discovery or design phase upstream, surfacing only once developers hit an ambiguity nobody resolved earlier. A founder watching visible development progress without also asking about the quality of the stages that preceded it is watching the wrong signal.

## Stage 4: Testing and QA

The stage most commonly compressed under deadline pressure, and the one whose compression is least visible until after launch. Testing verifies not just that features work in ideal conditions, but that they handle real-world messiness — unexpected input, concurrent users, edge cases nobody anticipated during discovery. A founder should specifically ask what testing looks like as a distinct, budgeted stage, not an informal activity developers do "along the way" with no dedicated time or resource attached to it.

## Stage 5: Deployment and Maintenance

Launch isn't the finish line — it's the stage where real users start generating information no earlier stage could have produced. A vendor relationship structured only around "delivery" and silent on what happens after is setting a founder up for an unpleasant surprise the first time something breaks in production or a bug surfaces that testing didn't catch. This stage should have its own explicit terms, not be treated as an afterthought once the "real" project is considered finished.

## The Research Behind Formalizing Stages at All

Management scholar Robert Cooper introduced the Stage-Gate process in the 1980s as a formal framework for new product development, structuring innovation work into distinct stages separated by "gates" — decision points where a project is evaluated against specific criteria before being allowed to proceed to the next stage. Cooper's research, based on studying hundreds of product development efforts across industries, found that projects without clear stage boundaries and gate criteria failed at a measurably higher rate, largely because problems that should have been caught early instead surfaced downstream, where they were far more expensive to fix.

The five software development stages in this article are a direct descendant of Cooper's framework applied to software specifically, and the "gate" logic explains precisely why skipping or rushing an early stage causes disproportionate damage later: a requirements ambiguity that should have been caught and resolved at the discovery gate, if the gate is skipped, doesn't disappear — it simply resurfaces later, usually during development or testing, where resolving it costs meaningfully more time and money than it would have cost at the stage where it actually belonged. A founder who understands the gate logic can ask a genuinely useful question at each stage transition: what specifically was verified before we moved forward, not just how much visible work has been produced.

## Manifera's Approach: Making Every Stage and Gate Visible to a Non-Technical Founder

- **Amsterdam (Governance/Stage Transparency):** Dutch project leads walk non-technical founders through each stage explicitly, including what's being verified at each gate before the project proceeds, translating technical milestones into terms a founder can genuinely track.
- **Vietnam (Execution/Disciplined Stage Completion):** The engineering pod treats each stage as a real gate with defined completion criteria, rather than blending stages together in a way that hides which specific stage a delay actually originated in.

This is Dutch Management × Vietnamese Mastery applied to process visibility itself: governance that explains the stages in plain language, paired with execution discipline that respects the gates between them. Learn about Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) process from discovery through launch.

## Case Study: An Antwerp Founder's First Build

A first-time founder at Antwerp-based startup Scheldewaar had no prior experience managing a software build and, with a previous freelancer, had no visibility into which of the five stages a recurring delay was actually coming from — only a vague sense that "development was taking longer than expected."

Manifera's Amsterdam team walked her through the stage framework explicitly during onboarding, including what would be verified at each gate. When a delay did occur mid-project, she could ask a specific question — "was this a design-stage gap or a development-stage issue?" — rather than a general one, and received a specific, useful answer: an ambiguity in the original requirements had surfaced during development because a particular edge case hadn't been discussed during discovery.

> *"I didn't even know there were distinct stages before this project. Once I did, I could ask questions that actually got me real answers instead of reassurance."*
> — **Founder, Scheldewaar**

Scheldewaar's founder now asks every vendor, at the start of any new engagement, to explain which of the five stages a given deliverable belongs to before evaluating whether it's on track.

## The Five Stages and Their Most Common Failure Point

| Stage | What It Verifies | Most Common Failure |
|---|---|---|
| Discovery | What's actually being built and why | Rushed, leaves requirements ambiguous |
| Design/Architecture | How the system will be structured | Skipped to start visible development sooner |
| Development | Building against the agreed design | Blamed for delays actually caused upstream |
| Testing/QA | The software works under real conditions | Compressed under deadline pressure |
| Deployment/Maintenance | Ongoing support after launch | Treated as an afterthought, no explicit terms |

## Why Gate Criteria Matter More Than Stage Names Alone

Knowing the five stage names is a useful starting point, but Cooper's actual research emphasis was on the gate criteria between stages, not the stages themselves — a project can nominally pass through all five stages and still fail if nothing specific was actually verified at each transition. A useful habit for a non-technical founder: before a project moves from one stage to the next, ask what specifically would have to be true for that transition to be premature. If discovery ends without a written requirements document a third party could review, the gate wasn't real, regardless of how much time was nominally spent on the stage. If testing ends without a specific pass/fail result against defined criteria, the same is true.

This distinction matters because a vendor eager to show momentum can move through stage names quickly while skipping the substance of each gate — presenting a fast-looking timeline that's actually skipping the verification work that makes each stage meaningful in the first place. A founder asking "what stage are we in" gets a name. A founder asking "what was verified before we moved to this stage" gets the information that actually predicts whether problems are being caught early or quietly deferred to a more expensive point downstream.

## Using the Stage Framework on Your Own Project

Ask your vendor to name which of these five stages any current work belongs to, and what specifically was verified before moving to the next one — this single habit turns vague status updates into genuinely useful information. [Schedule a free consultation with our Amsterdam team](https://www.manifera.com/contact-us/) to see how we structure each stage.

## Frequently Asked Questions

### (Scenario: first-time founder trying to understand a vendor's process) What are the actual stages of software development, in plain language?

Discovery and requirements, design and architecture, development, testing and QA, and deployment and maintenance — five distinct stages, each with its own purpose and its own common failure point.

### (Scenario: founder noticing a delay but unsure why) How do I figure out which stage a project delay is actually coming from?

Ask your vendor directly which stage the current work belongs to and what was verified before moving to it — a delay blamed on "development" often actually originates in a rushed discovery or design stage upstream.

### (Scenario: founder unsure how much time discovery should take) How long should the discovery stage realistically take before development starts?

It varies by project complexity, but a discovery stage that produces only a verbal understanding rather than a written, specific requirements document is a sign it was rushed, regardless of how many days were spent on it.

### (Scenario: founder pressured to skip testing to save time) Is it ever reasonable to skip or heavily compress the testing stage to hit a deadline?

Rarely for anything beyond the smallest project — testing catches problems that are dramatically cheaper to fix before launch than after, and compressing it usually shifts cost forward rather than actually eliminating it.

### (Scenario: founder assuming the project ends at launch) Does the software development process actually end once the product launches?

No — deployment and maintenance is its own stage with its own ongoing needs, and a vendor relationship with no explicit terms for this stage often leaves a founder unsupported the first time a real issue surfaces in production.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: first-time founder trying to understand a vendor's process) What are the actual stages of software development, in plain language?", "acceptedAnswer": { "@type": "Answer", "text": "Discovery and requirements, design and architecture, development, testing and QA, and deployment and maintenance." } },
    { "@type": "Question", "name": "(Scenario: founder noticing a delay but unsure why) How do I figure out which stage a project delay is actually coming from?", "acceptedAnswer": { "@type": "Answer", "text": "Ask your vendor directly which stage the current work belongs to — delays blamed on development often originate in a rushed discovery or design stage." } },
    { "@type": "Question", "name": "(Scenario: founder unsure how much time discovery should take) How long should the discovery stage realistically take before development starts?", "acceptedAnswer": { "@type": "Answer", "text": "It varies, but a discovery stage producing only a verbal understanding rather than a written requirements document is a sign it was rushed." } },
    { "@type": "Question", "name": "(Scenario: founder pressured to skip testing to save time) Is it ever reasonable to skip or heavily compress the testing stage to hit a deadline?", "acceptedAnswer": { "@type": "Answer", "text": "Rarely — testing catches problems dramatically cheaper to fix before launch than after, and compressing it usually shifts cost forward." } },
    { "@type": "Question", "name": "(Scenario: founder assuming the project ends at launch) Does the software development process actually end once the product launches?", "acceptedAnswer": { "@type": "Answer", "text": "No — deployment and maintenance is its own stage, and a vendor relationship with no explicit terms for it leaves a founder unsupported later." } }
  ]
}
</script>
