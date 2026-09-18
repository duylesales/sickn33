---
Title: "The EU AI Act: What It Means for One Small AI Feature"
Keywords: EU AI Act, AI compliance, risk categories, transparency obligations, AI feature, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# The EU AI Act: What It Means for One Small AI Feature

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The EU AI Act: What It Means for One Small AI Feature",
  "description": "Most products with an AI feature fall into the lightest category and need transparency rather than paperwork. How to work out which category yours is in, the obligations that follow, and the uses that are prohibited outright.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-30",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-eu-ai-act-what-it-means-for-one-small-ai-feature" }
}
</script>

You added a feature that summarises text, or drafts a reply, or sorts incoming items into categories. It took an afternoon. Then somebody asked whether it complies with the AI Act, and the honest answer was that you had not thought about it at all.

The useful thing to know first is that the regulation is risk-based rather than uniform. Most AI features in most small products fall into the lightest category, where the obligation is essentially honesty: tell people they are interacting with a system rather than a person, and be clear about what it produces.

The work is in establishing which category you are in, and that depends entirely on what your feature decides.

## The Four Categories, Briefly

**Prohibited.** A small set of uses that are not permitted at all: social scoring by public authorities, exploiting vulnerabilities of specific groups, certain biometric categorisation, emotion inference in workplaces and education, and untargeted scraping of facial images. Few founders build these deliberately; the emotion inference one occasionally catches people who added sentiment analysis to a staff tool.

**High risk.** Systems used in defined sensitive contexts — employment and recruitment, education access and assessment, essential private and public services including credit scoring, law enforcement, migration, and safety components of regulated products. This category carries substantial obligations.

**Limited risk.** Systems that interact with people or generate content. The obligation is transparency.

**Minimal risk.** Everything else, with no specific obligations.

The category is determined by use rather than by technology. The same summarisation model is minimal risk in a note-taking tool and high risk when it summarises job applications to support a hiring decision.

## Are You a Provider or a Deployer?

The second question that changes your obligations.

If you build an AI system and put it on the market under your name, you are a provider. If you use somebody else's system in your own operations, you are a deployer, with lighter obligations.

For most founders reading this, the position is: you are a deployer of a model API, and a provider of the AI-enabled product you sell. Your obligations attach to what you offer customers.

One warning worth knowing: substantially modifying a high-risk system, or putting your name on one, can make you its provider with the full set of obligations. For most small products this does not arise, but it is the mechanism by which a founder using someone else's technology can acquire responsibilities they did not expect.

## The Transparency Obligations Most Products Have

If your product falls into limited risk — the common case — three things are expected and none is difficult.

**Tell people they are talking to a system.** A chat interface answering questions must not let a user believe a human is replying. A line of text is sufficient; pretending otherwise is the thing that is not permitted.

**Mark generated content.** Where your product generates text, images or audio that could be mistaken for human-produced or authentic material, it should be identifiable as generated. In a business tool this usually means a visible label rather than technical watermarking.

**Disclose emotion recognition and biometric categorisation** where used and permitted.

Beyond these, the general principle that serves you well commercially as well as legally: be clear about what the feature does, what it does not do, and that its output should be checked. A product that says "this draft was generated and should be reviewed" is both compliant and more trusted.

## If You Might Be High Risk

Check carefully rather than assuming, because several ordinary-sounding products land here.

Recruitment and employment decisions. Screening applications, ranking candidates, evaluating performance, allocating tasks, or making termination decisions — a great many HR tools built with AI tooling fall in this category.

Education. Determining access, evaluating learning outcomes, assessing students, monitoring exams.

Essential services. Creditworthiness, insurance pricing for life and health, emergency service dispatch, eligibility for public benefits.

If you are here, the obligations are substantial: a risk management system, data governance, technical documentation, logging, human oversight, accuracy and robustness measures, conformity assessment, and registration. This is a project rather than an afternoon, and it needs specialist advice.

The alternative worth considering honestly: change what the feature decides. A tool that surfaces information for a recruiter to use is a different proposition from one that ranks candidates, and the difference is frequently a design choice rather than a loss of value.

## Human Oversight Is the Practical Requirement

Across categories, the thread that matters is that a person remains responsible for consequential decisions.

That is good product design independently of any regulation, and it is what a customer's own compliance review will ask about. Can a user see why the system suggested this? Can they disagree and override it? Is there a record of what was suggested and what was decided?

Building those three things covers a large share of what any AI governance question will ask, and it makes the feature better — because the output of a model that nobody can question is a feature people quietly stop trusting.

## What Your Customers Will Ask Before the Regulator Does

In practice, the pressure arrives commercially rather than through enforcement. A business customer's procurement or compliance function asks, and you need an answer that week.

Four questions come up repeatedly, and they are worth preparing once.

**What does the feature do and what does it not do?** A plain description, free of marketing language, including its limitations.

**Which model provider, and where does the processing happen?** Named, with a region and a data processing agreement in place.

**Is our data used to train models?** The expected answer is no, supported by the provider's terms — check rather than assume, since behaviour differs between tiers and products.

**What happens when it is wrong?** How a user notices, how they override it, and whether there is a record. This is the question that separates a considered feature from a demo, and it is the one most likely to be asked by someone who has seen a model be confidently wrong.

Write the answers on one page and keep it with your subprocessor list and processing agreement. For most small products, that page plus a documented categorisation is the entirety of what an AI governance review asks for — and having it ready turns a three-week exchange into a single reply.

## Keep the Assessment Alive

The specific hazard for products like these is drift. An AI feature is categorised correctly in March and is a different feature by October, because each individual change was small and reasonable and nobody re-examined the whole.

The example above is the pattern: a score, then a sort, then a threshold. No single step looked like a change of category, and together they were.

Two habits prevent it. Write the categorisation down with its reasoning, so that the basis is explicit rather than remembered — "this is limited risk because the output is advisory and a person decides" is a sentence that can be checked against a future version. And treat any change to what an AI feature decides, hides, ranks or excludes as a trigger to reread that sentence.

The second habit is the one that matters, because it converts an annual review — which nobody does — into a check attached to the moment of change, which takes two minutes.

It also produces a better product argument. A feature whose limits are written down is a feature whose scope is deliberate, and the founders who do this tend to discover that the version which stays advisory is both easier to sell and easier to defend.

## Setting This Up

For a product with AI features this is typically one to two days: each feature described in terms of what it decides and for whom, categorised against the risk tiers with the reasoning written down, prohibited uses confirmed absent, transparency measures implemented — system disclosure, generated content labelling, clear statements of capability and limits — human oversight built in with visible reasoning, override and a decision record, model provider terms reviewed for what they permit, and a short internal document recording the assessment so it can be shown to a customer and revisited when features change.

LaunchStudio does this as part of preparing AI features for business customers, where the question now arrives in most procurement processes. Behind it is Manifera — eleven years, clients including Vodafone, TNO and CFLW, from Amsterdam, Singapore and Ho Chi Minh City.

[Describe what your AI feature decides](https://launchstudio.eu/en/#contact) and we will tell you which category it is in.

## Real example

### A Ranking Feature That Changed Category

Vincent Doeleman built Kandidaatmatch in Lovable: a tool helping recruitment agencies match candidates to vacancies, 23 agencies with around 30,000 candidate records.

The original feature searched and filtered — a recruiter typed requirements and saw matching candidates with the matching terms highlighted. Useful, and clearly minimal risk.

Over a year it grew. A model was added that scored candidates for fit, ordered the list by that score, and hid anyone below a threshold. Recruiters worked from the top of the list. The change had happened gradually, one reasonable request at a time.

An agency's client — a large employer with its own compliance function — asked how the system complied with the AI Act. Vincent's product was now filtering access to employment on the basis of an automated assessment, which put it in the high-risk category, and neither he nor the agencies had documentation of any kind.

Nine business days: every feature described by what it decides and for whom; legal advice confirming that automatic exclusion below a threshold was the determining factor; the threshold removed so every matching candidate remains visible and the score becomes one sortable column among several, with the default order returned to relevance; the reasoning for each score exposed in the interface — which requirements matched and which did not — replacing a number with no explanation; recruiter override recorded, with a log of what was suggested and what was decided, retained and exportable; a statement shown in the interface that scores are generated and must not be the sole basis for a decision; an assessment document recording the categorisation and reasoning; the model provider's terms reviewed and a data processing agreement put in place, which had been missing; and candidate data sent to the model reduced to the relevant experience text rather than the full record.

**Result:** legal advice was that the revised feature sits in the limited-risk category, with the reasoning documented. The employer accepted the assessment. Two agencies told Vincent the visible reasoning was a better product than the score had been, because they could now explain a shortlist to their own clients.

> *"I never decided to build a high-risk system. I added a score, then sorted by it, then hid the bottom of the list — and somewhere in those three steps my product started deciding who got seen."*
> — **Vincent Doeleman, Founder, Kandidaatmatch (Utrecht)**

**Cost & Timeline:** €6,200 (feature categorisation with legal input, threshold and ranking redesign, explainable scoring, override and decision logging, transparency statements, assessment documentation, provider agreement, payload reduction) — completed in 9 business days.

## Frequently Asked Questions

### Does the AI Act apply to a small summarisation feature?

Usually as limited risk, where the obligation is transparency: tell people they are interacting with a system and make generated content identifiable. Category depends on what the feature decides, not on its size.

### What makes a feature high risk?

Use in defined sensitive contexts — employment and recruitment, education access and assessment, essential services such as credit and insurance, law enforcement, migration. Many HR tools qualify without their builders realising.

### Am I a provider or a deployer?

You are typically a deployer of a model API and a provider of the AI-enabled product you sell. Your obligations attach to what you offer customers under your own name.

### Can I avoid high-risk classification by changing the feature?

Often, yes. A tool that surfaces information for a person to use differs from one that ranks or excludes automatically, and the difference is usually a design choice rather than a loss of value.

### What should I do first?

Write down what each AI feature decides and for whom. That description determines the category, and most founders have never articulated it — which is why the answer is unclear.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does the EU AI Act apply to a small AI feature?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually as limited risk, requiring transparency — disclosing that it is a system and labelling generated content. Category depends on what the feature decides."
      }
    },
    {
      "@type": "Question",
      "name": "What makes an AI feature high risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use in employment and recruitment, education access and assessment, essential services like credit and insurance, law enforcement or migration."
      }
    },
    {
      "@type": "Question",
      "name": "Am I a provider or a deployer under the AI Act?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically a deployer of a model API and a provider of the AI-enabled product you sell under your own name."
      }
    },
    {
      "@type": "Question",
      "name": "Can redesigning a feature avoid high-risk classification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often. Surfacing information for a human to act on differs from ranking or excluding automatically, and that is usually a design choice."
      }
    },
    {
      "@type": "Question",
      "name": "What is the first step in assessing an AI feature?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Write down what it decides and for whom. That description determines the category and most founders have never articulated it."
      }
    }
  ]
}
</script>
