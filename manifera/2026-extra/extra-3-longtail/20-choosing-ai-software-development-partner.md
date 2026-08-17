---
title: "How to Tell a Real AI Engineering Capability From a Slide With 'AI-Powered' on It"
keywords: "ai software development companies, ai app development company, ai development services, ai solution development"
buyer_stage: "Decision"
target_persona: "A"
---

# How to Tell a Real AI Engineering Capability From a Slide With "AI-Powered" on It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Choose an AI Software Development Partner Without Buying the Hype",
  "description": "A five-step approach to vetting whether a vendor's AI software development capability is genuine or primarily marketing positioning.",
  "step": [
    { "@type": "HowToStep", "name": "Ask for a specific, technical example of AI in a past project", "text": "Request the actual model, integration architecture, and evaluation approach used, not a general description." },
    { "@type": "HowToStep", "name": "Ask how they evaluate AI output quality", "text": "A real capability includes a defined process for testing accuracy, catching hallucination, and measuring output against ground truth." },
    { "@type": "HowToStep", "name": "Ask about cost and latency management", "text": "Production AI features need a real strategy for managing API costs and response times at scale, not just a working demo." },
    { "@type": "HowToStep", "name": "Ask how they handle AI failure modes", "text": "Fallback behavior, error handling, and human review processes for when the AI component is wrong or unavailable." },
    { "@type": "HowToStep", "name": "Request a reference for a shipped AI feature, not a pilot", "text": "A genuine production reference reveals whether the vendor's AI work survives sustained real usage, not just a controlled demo environment." }
  ]
}
</script>

Every vendor pitch deck in 2026, without exception, has "AI-powered" somewhere prominently on it. Fewer than half of those vendors have shipped an AI feature that survived contact with real production traffic, real cost constraints, and the specific ways language models fail in practice — and there's genuinely no reliable way to tell the difference from the deck alone, which is precisely the market condition Akerlof's classic economics research describes.

## Step 1: Ask for a Specific, Technical Example of AI in a Past Project

Not the vague "we've used AI in several projects" — the actual model used, how it was integrated (API call, fine-tuned, RAG pipeline), and what specific problem it solved for a real client. Vendors with genuine real experience tend to answer this specifically and quickly, without hesitation. Vendors positioning AI mainly as a marketing checkbox tend to answer vaguely or pivot smoothly to a different, safer topic.

## Step 2: Ask How They Evaluate AI Output Quality

Real AI engineering includes a defined evaluation process — a test set of expected inputs and outputs, a method for catching hallucination or incorrect responses, and a genuine way of measuring accuracy that isn't just "it looked right in the demo." A vendor with no answer to this question hasn't shipped AI features that needed to be reliable at scale.

## Step 3: Ask About Cost and Latency Management

LLM API costs and response times can vary wildly, order-of-magnitude wildly, based on prompt design, caching strategy, and model selection — a naive implementation can cost 10x more than a well-architected one for the same feature. Ask specifically how they've managed this in production, since a demo that works fine at low volume can become financially unworkable at real usage scale without deliberate cost engineering.

## Step 4: Ask How They Handle AI Failure Modes

What actually happens when the AI component returns a wrong answer, times out, or the underlying API provider has an outage? A real production AI feature has fallback behavior, error handling, and often a human-review escalation path for high-stakes outputs — not just a happy-path demo that assumes the AI always responds correctly and quickly.

## Step 5: Request a Reference for a Shipped AI Feature, Not a Pilot

A pilot or proof-of-concept that never reached production tells you, at best, that the vendor can build an impressive demo. A reference for a feature that's been running in production for months, handling real user traffic and real edge cases, tells you whether their AI work actually survives contact with reality.

## The Classic Economics of a Market Full of Confident Claims

George Akerlof's 1970 paper "The Market for Lemons," part of the body of work on information asymmetry that later earned him a share of the 2001 Nobel Memorial Prize in Economic Sciences alongside Michael Spence and Joseph Stiglitz, used the used-car market as its illustration: when buyers can't reliably distinguish good cars ("peaches") from bad ones ("lemons") before purchase, and sellers know which is which, buyers rationally discount every price to protect against the risk of a lemon — which pushes honest sellers of good cars out of the market, since they can't get a fair price for genuine quality that looks, from the outside, identical to a lemon's confident sales pitch. Left unaddressed, this dynamic can cause an entire market's average quality to decline, driven purely by the buyer's inability to verify claims before committing.

The AI vendor market in 2026 has more than a little in common with Akerlof's used-car lot. Every vendor's pitch deck claims "AI-powered" capability, and a founder evaluating them from the outside has no reliable way to distinguish a genuine production track record from a confident claim resting on a single unfinished pilot — exactly the information asymmetry Akerlof's model describes. And exactly as his model predicts, this creates a real cost for vendors who've done the genuine work: without some mechanism to signal real capability, they get lumped in with confident-sounding competitors who haven't, and the market's evaluation process degrades toward rewarding polished claims over verified substance.

Akerlof's own paper, and the broader signaling and screening literature that followed it (including Spence's work discussed elsewhere on this subject), points to the same structural fix this article's five-step process is built around: mechanisms that let genuine quality signal itself in ways a lemon can't cheaply fake. A vendor reference check functions as exactly this kind of screening mechanism — a "peach" vendor with real production AI experience can pass it readily, while a "lemon" vendor whose experience is a single unfinished pilot cannot manufacture a production reference on demand, regardless of how confidently their pitch deck describes their capability.

## Manifera's Approach: AI Capability Grounded in Production Discipline

- **Amsterdam (Governance/Evaluation):** Dutch architects apply the same rigor to AI feature evaluation as any other production system — defined accuracy testing, cost modeling, and failure-mode handling, treating AI components as engineering work requiring the same discipline, not a separate category exempt from it.
- **Vietnam (Execution/Production Experience):** The engineering pod has shipped AI-powered features into real production environments, with the cost, latency, and reliability engineering that separates a working demo from a working product.

This is Dutch Management × Vietnamese Mastery applied to AI capability itself: evaluation rigor paired with genuine production shipping experience. Explore Manifera's approach to [software development](https://www.manifera.com/about-us/manifera-technologies/) incorporating AI capabilities responsibly.

## Case Study: A Zagreb Insurer's Vendor Re-Selection

Drava Assurance, a Zagreb-based insurer, had shortlisted a vendor whose pitch heavily featured "AI-powered claims processing" — until a technical Q&A revealed the vendor's only AI experience was an unfinished pilot that had never handled real claims data, with no answer for accuracy evaluation or failure-mode handling.

Manifera was engaged instead, having previously shipped a document-classification AI feature into production for a comparable client. The Amsterdam team built an evaluation framework specific to Drava's claims categories before development began, and the Vietnam pod implemented cost controls that kept the feature's API spend within Drava's budget at full claims volume — details the previous shortlisted vendor had never been asked to demonstrate.

> *"The pitch decks all looked the same. The technical Q&A is where the real difference showed up, and it showed up fast."*
> — **Head of Claims Technology, Drava Assurance**

Drava's technology team now runs the same technical Q&A structure for every vendor evaluation involving an "AI-powered" claim, regardless of category, having found that the screening mechanism generalizes well beyond claims-processing software specifically.

## Why Screening Mechanisms Work Even When Vendors Aren't Lying

It's worth being precise about what this screening process is actually detecting, because it isn't primarily about catching dishonest vendors — most vendors describing themselves as "AI-powered" genuinely believe their own pitch. The Akerlof dynamic doesn't require bad faith to produce a market full of unreliable signals; it only requires that buyers can't distinguish confident belief from verified capability from the outside, which is true regardless of how sincere any individual vendor is. A vendor with one promising but unfinished pilot can honestly believe they're close to production-ready without having actually solved the cost, latency, and failure-mode problems that separate a demo from a shipped feature — their confidence is genuine, it's just not yet backed by the evidence a buyer needs.

This is precisely why the five-step process focuses on artifacts a vendor either has or doesn't have — a specific model and integration example, a defined evaluation methodology, a cost model, a failure-mode plan, a production reference — rather than trying to assess a vendor's sincerity or trustworthiness directly. Sincerity is not what a founder needs to evaluate; verified capability is, and Akerlof's framework points at exactly the kind of hard-to-fake evidence that reliably separates the two, regardless of how genuinely any individual vendor believes in their own pitch.

## Real AI Capability vs. Marketing Positioning

| Signal | Marketing Positioning | Real Capability |
|---|---|---|
| Description of past AI work | Vague, general | Specific model, integration, and outcome |
| Output quality evaluation | Not mentioned | Defined test set and accuracy process |
| Cost/latency management | Not mentioned | Concrete production cost engineering |
| Failure mode handling | Assumes AI always works | Fallback, error handling, escalation path |
| References | Pilots or demos | Production features with real usage history |

## Getting Past the Deck

Ask these five questions in a technical Q&A, not a sales call, before signing with any vendor positioning "AI-powered" as a differentiator — the format itself is a screening mechanism a confident-but-unverified claim can't easily pass. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about what a genuine AI engineering capability actually looks like under the hood.

## Frequently Asked Questions

### (Scenario: CTO evaluating a vendor's AI claims) How can I quickly tell if a vendor's AI capability is real or marketing positioning?

Ask for a specific technical example — the model used, the integration approach, and how output quality was evaluated. Vague or evasive answers to specific technical questions are the clearest signal.

### (Scenario: CTO worried about AI feature costs spiraling) Why do AI feature costs sometimes explode in production compared to the demo?

Naive implementations without caching, prompt optimization, or model selection discipline can cost dramatically more at real usage volume than a well-architected feature — this is a common gap between a working demo and a production-ready feature.

### (Scenario: CTO trying to assess AI reliability before committing) What should I ask about how a vendor handles AI errors in production?

Ask specifically what happens when the AI component returns a wrong or low-confidence answer — whether there's a fallback, an escalation to human review, or whether the system simply assumes the AI response is always correct.

### (Scenario: founder trying to distinguish a pilot from real capability) Is a successful AI pilot enough evidence that a vendor can deliver a production feature?

Not on its own — ask specifically whether the pilot's approach included production concerns like cost management, failure handling, and accuracy evaluation, or whether it was a best-case demo that hasn't been tested against real-world volume and edge cases.

### (Scenario: CTO preparing questions for an upcoming vendor call) What's the single best question to ask in a vendor's technical Q&A about AI capability?

Ask for a reference to a specific AI feature that has been running in production for at least several months, handling real user traffic — and then actually call that reference.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO evaluating a vendor's AI claims) How can I quickly tell if a vendor's AI capability is real or marketing positioning?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for a specific technical example — the model used, the integration approach, and how output quality was evaluated. Vague answers are the clearest signal." } },
    { "@type": "Question", "name": "(Scenario: CTO worried about AI feature costs spiraling) Why do AI feature costs sometimes explode in production compared to the demo?", "acceptedAnswer": { "@type": "Answer", "text": "Naive implementations without caching, prompt optimization, or model selection discipline can cost dramatically more at real usage volume." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to assess AI reliability before committing) What should I ask about how a vendor handles AI errors in production?", "acceptedAnswer": { "@type": "Answer", "text": "Ask specifically what happens when the AI component returns a wrong or low-confidence answer, and whether there's a fallback or human-review escalation." } },
    { "@type": "Question", "name": "(Scenario: founder trying to distinguish a pilot from real capability) Is a successful AI pilot enough evidence that a vendor can deliver a production feature?", "acceptedAnswer": { "@type": "Answer", "text": "Not on its own — ask whether the pilot included production concerns like cost management, failure handling, and accuracy evaluation." } },
    { "@type": "Question", "name": "(Scenario: CTO preparing questions for an upcoming vendor call) What's the single best question to ask in a vendor's technical Q&A about AI capability?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for a reference to a specific AI feature running in production for several months, handling real user traffic, and then call that reference." } }
  ]
}
</script>
