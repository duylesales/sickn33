---
Title: "The EU AI Act and Your Small AI Product: What Actually Applies"
Keywords: EU AI Act compliance, AI Act risk tiers, transparency obligations AI, AI Act small business, AI Act SaaS founder, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# The EU AI Act and Your Small AI Product: What Actually Applies

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The EU AI Act and Your Small AI Product: What Actually Applies",
  "description": "A risk-tier walkthrough of the EU AI Act aimed at founders building on top of third-party AI models, clarifying which obligations apply to a small product built on OpenAI or Anthropic APIs versus which only apply to the model provider itself.",
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
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/the-eu-ai-act-and-your-small-ai-product"
  }
}
</script>

It's 2 AM, you're three weeks from demoing your AI-powered resume screening tool to your first pilot customer, and someone in a founder Discord drops a link: "isn't this exactly what the EU AI Act calls high-risk?" You skim the summary. The words "high-risk," "conformity assessment," and "fines up to €35 million" appear in the same paragraph as your product category. You close the laptop. The next morning, still unsure whether you've built something legally fine or something that needs six months of work you don't have time for, is a genuinely common moment for founders building AI features right now — and the honest answer, in most cases, is calmer than the 2 AM panic suggested, but it does require actually working through which tier your specific product falls into rather than pattern-matching on a scary word.

The EU AI Act is real, it's binding, and parts of it are already in force — but it's a risk-tiered framework, not a blanket rule that treats a customer support chatbot the same as a medical diagnosis tool, and most of the heaviest obligations fall on the handful of companies actually building or deploying systems in specific high-stakes categories, not on every founder who's wired an OpenAI API call into a SaaS product. Here's the decision tree that actually applies to a small AI-native product.

## The Four Tiers: Where Almost Everything Small Actually Sits

The AI Act sorts systems into four risk categories, and understanding which one your product falls into is the single most important decision this article covers, because the obligations attached to each tier are wildly different in scope. **Unacceptable risk** systems — social scoring, manipulative subliminal techniques, real-time biometric surveillance in public spaces for law enforcement (with narrow exceptions) — are banned outright; almost no legitimate small SaaS product falls here, and if a founder is genuinely unsure whether their product does, that uncertainty itself is a signal to get a real legal opinion rather than guessing. **High-risk** systems are the tier that carries the heaviest obligations: this covers specific, enumerated use cases like employment decisions (hiring, firing, performance evaluation), credit scoring, biometric identification, critical infrastructure management, education access decisions, and law enforcement applications. **Limited-risk** systems are ones with specific transparency obligations attached — chatbots, deepfake generators, emotion-recognition systems — where the law's core requirement is that users know they're interacting with AI or AI-generated content, not that the system meets extensive technical and documentation requirements. **Minimal-risk** systems — the large majority of AI-assisted features in ordinary SaaS products, like a writing assistant, a search-ranking feature, a content summarizer, a general-purpose customer support bot not making consequential decisions about a person — carry no mandatory obligations under the Act at all, beyond voluntary codes of conduct. Most AI-native founders building on Lovable, Bolt, or similar tools, using a third-party model API for features like content generation, summarization, or conversational support, land in minimal-risk or limited-risk, not high-risk — but the way to know for certain is to check your specific use case against the high-risk list, not to assume based on how sophisticated the feature feels.

## The Question That Actually Determines Your Tier: What Decision Is the AI Making, About Whom?

The fastest way to self-assess is to ask a specific question about your product: is the AI feature making, or materially influencing, a consequential decision about a specific person's access to employment, credit, education, essential services, or legal rights? If yes, you're likely looking at high-risk territory and need a real legal assessment. If the AI feature is generating content, summarizing information, answering questions, ranking search results, or assisting a human who retains the actual decision-making authority, you're very likely in limited or minimal risk regardless of how advanced the underlying model is. This distinction trips founders up because it's about function, not sophistication — a simple rules-based system that auto-rejects loan applications below a credit score threshold is high-risk, while a genuinely sophisticated large language model helping a support team draft better responses to customer emails, with a human sending the final message, is not. Founders sometimes assume "more powerful model equals more risk category," when the Act's risk tiers track consequence to real people, not model capability.

## If You're Building on Someone Else's Model: Provider vs. Deployer Obligations

A critical distinction the Act draws, and one that directly affects nearly every founder using OpenAI, Anthropic, or another third-party model API: the heaviest technical obligations — risk management systems, extensive technical documentation, training data governance — fall on the "provider" of a high-risk AI system, which for a founder calling a third-party API is usually the model company (OpenAI, Anthropic, Google), not the founder building a product on top of it. A founder in this position is generally a "deployer," a category with meaningfully lighter obligations even within the high-risk tier: primarily ensuring appropriate human oversight, using the system per the provider's instructions, and monitoring for issues rather than building an entire technical documentation and risk-management apparatus from scratch. This matters enormously for a two-person startup evaluating whether the Act is even feasible to comply with — building a high-risk AI system from the ground up as a "provider" is a genuinely heavy lift; deploying a high-risk use case on top of a major provider's already-compliant model, as a "deployer," is a substantially lighter one, largely about your own usage practices rather than the model's internals. Even so, if your specific use case is genuinely high-risk (say, an AI-powered hiring screening tool), the deployer obligations are still real and still require actual work — this isn't a loophole that exempts you, it's a lighter but non-trivial set of requirements.

## Transparency Obligations: The Part That Applies to Almost Everyone

Regardless of risk tier, if your product uses AI to interact with users conversationally, or generates synthetic content, specific transparency requirements apply that are genuinely cheap to implement and worth building in regardless of how the broader compliance question resolves. Users need to know they're interacting with an AI system rather than a human, unless it's obvious from context — a chatbot needs a visible disclosure, not necessarily an intrusive one, but a real one, not buried in a terms-of-service page nobody reads. AI-generated or manipulated image, audio, or video content (deepfakes) needs to be labeled as such. Emotion-recognition or biometric categorization systems need disclosure to the people being analyzed. None of this requires a legal team to implement — it requires a founder deciding, deliberately, to add a small UI element ("You're chatting with an AI assistant") or a metadata tag, rather than assuming a sophisticated-feeling AI feature speaks for itself. This is the single most actionable part of the Act for a small product: cheap to do, clearly required, and the kind of thing that's easy to simply forget to add when a chatbot feature ships fast off an AI coding tool's default template.

## What's Already in Force vs. What's Still Phasing In

The Act's obligations didn't all activate on one date — they're phasing in on a schedule, and knowing where in that schedule you are matters for prioritization. The bans on unacceptable-risk practices and AI literacy obligations took effect first. Obligations for general-purpose AI models (relevant mainly to the model providers themselves, not founders building on top of them) followed. The bulk of high-risk system obligations phase in over a longer runway, giving founders in genuinely high-risk categories real time to build compliance rather than facing an immediate cliff — but "real time" isn't "indefinite," and a founder whose product is clearly high-risk should treat the phase-in period as a planning window, not a reason to defer the assessment itself. Checking the current phase-in status against your specific obligations, rather than assuming either "it's all already enforced" or "it's all years away," is worth five minutes against an official source before making any bigger decision based on the timeline.

## AI Literacy: The Overlooked Obligation That Applies Even at Minimal Risk

One obligation under the Act applies regardless of which risk tier your product lands in, and it's the one founders are least likely to have heard about: providers and deployers of AI systems are expected to ensure their own staff, and to a reasonable extent their users, have sufficient "AI literacy" to understand the system's capabilities, limitations, and risks. For a two-person startup this doesn't mean a formal training program — it means being able to explain, in plain language, what your AI feature can and can't reliably do, and making sure that explanation actually reaches users somewhere in the product, not just in an internal team conversation. A one-paragraph "how this works and where it can be wrong" note near an AI feature, written honestly rather than as marketing copy, does double duty here: it satisfies the spirit of the literacy obligation and it tends to reduce support tickets from users who assumed an AI-generated suggestion carried more certainty than it does. This is a cheap, easy-to-skip requirement precisely because it doesn't come with a dramatic penalty attached in most founders' minds — but it's worth treating as a real item on the launch checklist rather than an afterthought, alongside the transparency disclosures covered above.

## The Practical Decision Framework for a Founder Right Now

Given all of the above, here's the actual sequence worth running through: first, identify whether your AI feature makes or materially influences a consequential decision about a person in one of the enumerated high-risk categories — if genuinely unsure, this is worth a real legal consultation, not a guess, given the stakes involved. Second, if you're not high-risk, implement the cheap, universal transparency obligations anyway (AI disclosure to users, labeling of synthetic content) because they're inexpensive and increasingly expected regardless of strict legal necessity. Third, if you are high-risk but building as a deployer on top of a major provider's model, understand that your obligations center on oversight and appropriate use, not on replicating the provider's own compliance work — a meaningfully lighter, though still real, lift. Fourth, document your reasoning at each step, even informally — a short internal note explaining why you assessed your product as minimal-risk is worth having if the question ever comes up again with an investor, an enterprise customer's compliance team, or a future regulatory inquiry.

Working through this classification honestly, and building in the cheap transparency wins regardless of tier, is exactly the kind of practical last-mile decision [LaunchStudio](https://launchstudio.eu/en/) helps AI-native founders make before launch, backed by Manifera's 11+ years of experience building compliant production systems, including for clients like TNO operating in genuinely regulated spaces.

[Book a 15-minute intro call](https://launchstudio.eu/en/#contact) to walk through where your specific AI feature actually sits on the Act's risk tiers.

## Real example

### A SaaS Founder in Action: The Feature That Wasn't What It Looked Like

Bram Willemsen built ShiftMatch, an AI-powered shift-scheduling tool for retail chains, using Cursor, with a feature that used an LLM to suggest which employees should be offered available shifts based on past performance ratings entered by managers. A prospective enterprise customer's legal team flagged the feature as a potential high-risk "employment decision" system under the AI Act and paused the deal pending clarification.

Manifera's review, brought in through LaunchStudio, found the actual determining factor: ShiftMatch's AI suggested candidates, but a human manager always made the final assignment and could freely override the suggestion — placing the feature closer to a decision-support tool than an autonomous employment decision system, though the performance-rating data it used still warranted careful documentation of how those ratings were generated and whether they could inadvertently encode bias. The team helped Bram document the human-in-the-loop design explicitly, add a clear disclosure that shift suggestions were AI-generated and manager-reviewed, and prepare a short written rationale for the classification the enterprise customer's legal team could evaluate directly.

**Result:** The enterprise deal resumed once Bram's legal reasoning and human-oversight documentation were in hand, and ShiftMatch now includes AI Act classification documentation as a standard part of every enterprise sales conversation rather than a reactive scramble.

> *"I'd assumed 'AI Act' meant 'stop building this feature.' It actually meant 'write down, clearly, how a human stays in control of the decision' — which I'd already built, I just hadn't documented it anywhere."*
> — **Bram Willemsen, Founder, ShiftMatch (Nijmegen)**

## Frequently Asked Questions

### Does the EU AI Act apply to my product if my company isn't based in the EU?

Yes, generally — the Act applies based on where your AI system is used or where its outputs affect people, not where your company is incorporated, so a non-EU founder serving EU users or customers is still in scope for the relevant obligations.

### Is a customer support chatbot automatically high-risk under the AI Act?

No — a standard support chatbot answering questions or routing tickets is typically minimal-risk or limited-risk (requiring only a disclosure that users are talking to AI), not high-risk. High-risk status attaches to specific enumerated categories like employment, credit, or education decisions, not to conversational AI generally.

### What penalties actually apply if a small company gets its risk tier wrong?

Penalties scale by violation severity and company size, with the highest fines reserved for the most serious violations like deploying banned systems; enforcement in practice, especially early on, tends to focus on clear, willful non-compliance rather than a small company that made a documented, good-faith classification effort that later needs revising.

### If I use OpenAI or Anthropic's API, do I inherit their compliance obligations automatically?

No — the heaviest "provider" obligations (technical documentation, risk management systems) generally fall on the model company itself, while you, as a "deployer" building on their API, have a lighter set of obligations focused on appropriate use and human oversight, though these still apply and still require real attention if your use case is high-risk.

### Should I get a lawyer involved, or can I self-assess my product's risk tier?

Self-assessment using the framework above is a reasonable first step for most minimal and limited-risk products, especially conversational or content-generation features. Get a lawyer involved specifically if your feature touches employment, credit, education, or another enumerated high-risk category, or if self-assessment leaves genuine ambiguity you can't resolve confidently on your own.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Does the EU AI Act apply to my product if my company isn't based in the EU?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, generally. The Act applies based on where your AI system is used or where its outputs affect people, not where your company is incorporated, so a non-EU founder serving EU users is still in scope." } },
    { "@type": "Question", "name": "Is a customer support chatbot automatically high-risk under the AI Act?", "acceptedAnswer": { "@type": "Answer", "text": "No. A standard support chatbot is typically minimal or limited-risk, requiring only a disclosure that users are talking to AI. High-risk status attaches to specific categories like employment, credit, or education decisions." } },
    { "@type": "Question", "name": "What penalties actually apply if a small company gets its risk tier wrong?", "acceptedAnswer": { "@type": "Answer", "text": "Penalties scale by violation severity, with the highest fines reserved for the most serious violations like deploying banned systems. Enforcement tends to focus on willful non-compliance rather than a small company's documented, good-faith classification effort." } },
    { "@type": "Question", "name": "If I use OpenAI or Anthropic's API, do I inherit their compliance obligations automatically?", "acceptedAnswer": { "@type": "Answer", "text": "No. The heaviest provider obligations generally fall on the model company itself, while you as a deployer have a lighter set of obligations focused on appropriate use and human oversight, though these still apply for high-risk use cases." } },
    { "@type": "Question", "name": "Should I get a lawyer involved, or can I self-assess my product's risk tier?", "acceptedAnswer": { "@type": "Answer", "text": "Self-assessment is reasonable for most minimal and limited-risk products. Get a lawyer involved specifically if your feature touches employment, credit, education, or another enumerated high-risk category, or if genuine ambiguity remains." } }
  ]
}
</script>
