---
Title: "Customer Data and Third-Party Models: What Leaves Your System"
Keywords: sending customer data to LLM provider, GDPR AI subprocessor, data processing agreement openai, EU data residency AI, training on customer data opt out, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Customer Data and Third-Party Models: What Leaves Your System

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Customer Data and Third-Party Models: What Leaves Your System",
  "description": "Adding an AI feature means sending your customers' data to another company. What that requires under GDPR, the questions business customers will ask, and the practical measures — minimisation, redaction, regional processing — that make the answers acceptable.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/customer-data-and-third-party-models-what-leaves-your-system" }
}
</script>

An AI feature is, from a data protection standpoint, a decision to send your customers' information to another company's computers. That is not an argument against it — the same is true of your hosting provider, your email service, and your payment processor. It is an argument for treating it with the same seriousness, which founders frequently do not, because a model API feels like a library rather than a supplier.

The moment this becomes concrete is the first business customer who asks where their data goes. In regulated sectors that question arrives during procurement, and "I'm not sure" ends the conversation.

## What Adding a Model Provider Actually Means

Three obligations follow from sending personal data to a model provider, and none of them are onerous once known.

**They become a subprocessor.** Your agreement with customers almost certainly lists who processes their data on your behalf, and the list has to include the model provider. Adding one usually requires notifying customers, and in some contracts giving them a right to object.

**You need a data processing agreement with them.** The major providers offer these; it is a matter of accepting the right terms in your account rather than negotiating anything, and it is a specific step that is easy to skip.

**Your privacy documentation must reflect it.** What is sent, to whom, for what purpose, where it is processed, and how long it is retained. This is the document a customer's compliance officer reads.

Then there is the question that decides whether some customers can use your product at all: **is the data used to train their models?** For the business and enterprise tiers of the major providers, the answer is generally no by default, and it is worth verifying in writing for the specific tier you are on rather than assuming. Consumer tiers sometimes behave differently, and using a personal account's key in a product is a mistake with real consequences.

## Where the Processing Happens

For European customers this is frequently the deciding factor, and it has become more addressable than it was.

The major providers now offer regional processing options — European endpoints, or contractual commitments about where data is handled and stored. Some offer zero-retention arrangements where inputs are not stored at all after the response. Whether these are available depends on the provider and the tier, and they occasionally cost more or restrict which models can be used.

The practical approach: find out what your provider offers for European processing, choose it if your customers are European businesses, and be able to state plainly where data goes. For customers in healthcare, legal, financial services, or the public sector, this is not a preference — a data transfer outside the EU without an appropriate basis can be the reason a deal does not happen, regardless of how good the feature is.

Some customers will require processing that never leaves their jurisdiction, which points to a self-hosted or regionally-guaranteed model. That is a significant architectural decision and worth making only when a customer's money depends on it.

## Send Less

The most effective protection is not contractual. It is not sending the data in the first place.

**Send the relevant portion, not the whole record.** Summarising a support conversation does not require the customer's address, payment details, or account history. Most implementations send everything available because it is easier, which increases both cost and exposure.

**Remove identifiers where the task does not need them.** Names, email addresses, phone numbers, and account numbers can frequently be replaced with placeholders before sending and restored afterwards. The model performs the task equally well on "Customer A" and you have sent nothing identifying.

**Never send secrets or credentials**, including anything that might be embedded in a document a customer uploaded.

**Exclude special-category data by default** — health, biometric, and similar information carries stricter obligations, and sending it to a third party requires a firmer basis than convenience.

Minimisation has a second benefit worth noting: it usually improves the output. A model given a focused input produces a better answer than one given everything and asked to find the relevant part, and it costs less.

Working out what actually needs to be sent, implementing redaction, and configuring regional processing is a specific piece of production work, and it is routinely skipped in AI-built products where the entire record is passed to the model because that was the simplest prompt to write. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements data minimisation and the documentation that goes with it. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Being Able to Answer the Questionnaire

Business customers ask a consistent set of questions, and having written answers turns a multi-day exchange into a link.

Which providers process our data, and where. What specifically is sent. Is it used for training. How long is it retained by the provider. Can the AI feature be disabled for our account. What happens to generated content if we delete our data. Who at your company can see the inputs and outputs.

That last one deserves attention, because it is often overlooked. If your logging captures model inputs and outputs for debugging — which is useful and recommended — then those logs contain customer data, potentially in a third-party logging service, accessible to anyone with access to it. That needs the same retention policy, the same access control, and the same mention in your documentation as the rest.

The penultimate question matters too. When a customer exercises their right to erasure, generated content derived from their data is their data, and deletion must reach it — including anything stored at the provider if retention is enabled.

## Give Customers the Choice

For products serving businesses, the single most useful feature is an account-level switch to disable AI processing entirely.

Some customers cannot use it: their own policy forbids sending client information to a third-party model, or their sector's rules do. Without a switch, your product is unusable for them and you lose the whole account rather than one feature. With it, they buy the product and turn the feature off, which is a much better outcome for both.

The same applies at a finer grain where it is easy: allowing a customer to mark particular records or fields as excluded from AI processing lets a firm use the feature for routine work while keeping its most sensitive matters out.

This is worth building before the first enterprise conversation rather than during it, because "we can add that" is a considerably weaker answer than "here is the setting."

## Real example

### The Feature That Cost a Healthcare Deal

Ruben Aarts ran Zorgnotitie, a note-taking tool for allied health practices, built in Bolt. A feature summarised session notes, sending the full note — including patient name, date of birth, and clinical detail — to a model provider on a consumer-tier account, with no data processing agreement and no regional configuration.

A practice group of eleven clinics reached procurement, and the questionnaire asked the standard questions. He could not say where processing occurred, had no agreement in place, could not confirm the data was not used for training, and had no way to disable the feature for an account. The process ended there.

The review found more. Model inputs and outputs were being logged in full to a third-party logging service on a plan with 90-day retention, meaning patient clinical notes existed in a fourth system nobody had considered. And two customers who had previously requested deletion still had generated summaries and log entries containing their patients' information.

**Result:** the provider account moved to a business tier with a data processing agreement and European processing, notes redacted of patient identifiers before sending with restoration afterwards, model input and output logging reduced to metadata only, an account-level switch to disable AI processing, generated content brought into the deletion path, and a written data-flow document for procurement questionnaires. The practice group re-engaged the following quarter and signed.

> "The feature was the reason they were interested and the reason they said no. Everything they asked was reasonable and I had answers to none of it."
> — **Ruben Aarts, Founder, Zorgnotitie**

**Cost & Timeline:** data minimisation, provider configuration, and documentation delivered in 4 business days.

## Frequently Asked Questions

### Does using an AI provider make them a subprocessor under GDPR?

Yes, where personal data is sent. They must be listed in your subprocessor disclosures, you need a data processing agreement with them, and your privacy documentation must state what is sent, where, and for how long it is retained.

### Is customer data used to train the provider's models?

Generally not on business and enterprise tiers of the major providers, but this should be verified in writing for your specific tier. Consumer tiers can differ, and using a personal account key in a product is a real risk.

### Can AI processing be kept within the EU?

Increasingly yes. Major providers offer European processing options and sometimes zero-retention arrangements, though availability varies by tier and model. For regulated European customers this is often the deciding factor.

### What is the most effective protection for customer data in AI features?

Sending less. Provide only the relevant portion, replace identifiers with placeholders where the task does not need them, and exclude special-category data by default. It also improves output quality and reduces cost.

### Should customers be able to turn AI features off?

Yes, at account level. Some businesses are prohibited by their own policy from sending information to third-party models, and without a switch you lose the entire account rather than one feature.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Does using an AI provider make them a subprocessor under GDPR?", "acceptedAnswer": { "@type": "Answer", "text": "Yes where personal data is sent. They must appear in your subprocessor disclosures, you need a data processing agreement, and your privacy documentation must state what is sent, where, and retention." } },
    { "@type": "Question", "name": "Is customer data used to train the provider's models?", "acceptedAnswer": { "@type": "Answer", "text": "Generally not on business and enterprise tiers of major providers, but verify in writing for your tier. Consumer tiers can differ and personal account keys carry real risk." } },
    { "@type": "Question", "name": "Can AI processing be kept within the EU?", "acceptedAnswer": { "@type": "Answer", "text": "Increasingly yes, through European processing options and sometimes zero-retention arrangements, though availability varies by tier and model." } },
    { "@type": "Question", "name": "What is the most effective protection for customer data in AI features?", "acceptedAnswer": { "@type": "Answer", "text": "Sending less: only the relevant portion, identifiers replaced with placeholders, and special-category data excluded by default. It also improves output and reduces cost." } },
    { "@type": "Question", "name": "Should customers be able to turn AI features off?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, at account level. Some businesses are prohibited from sending information to third-party models, and without a switch you lose the account rather than one feature." } }
  ]
}
</script>
