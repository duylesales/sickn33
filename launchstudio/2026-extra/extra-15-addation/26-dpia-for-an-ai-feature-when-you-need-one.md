---
Title: "DPIA for an AI Feature: When You Need One"
Keywords: dpia ai feature, data protection impact assessment saas, dpia avg ai, gdpr article 35 ai, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# DPIA for an AI Feature: When You Need One

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DPIA for an AI Feature: When You Need One",
  "description": "Adding an AI feature to a SaaS product can trigger the GDPR requirement for a data protection impact assessment. This guide explains when a DPIA is required, the criteria European regulators use, who is responsible when you are a processor, what a DPIA contains, typical risks of AI features and the technical measures that reduce them.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-13",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 35: Data protection impact assessment", "url": "https://gdpr-info.eu/art-35-gdpr/" },
    { "@type": "CreativeWork", "name": "Article 29 Working Party Guidelines on DPIA (WP248 rev.01)", "url": "https://ec.europa.eu/newsroom/article29/items/611236" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: DPIA", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/basic-gdpr/privacy-and-personal-data/data-protection-impact-assessment-dpia" },
    { "@type": "CreativeWork", "name": "EDPB Opinion 28/2024 on AI models", "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en" }
  ]
}
</script>

AI features are now the most requested addition to almost every SaaS product. Customers want summaries of long documents, drafts of emails, classification of incoming requests, suggestions based on historical data and chat interfaces over their own content. With modern APIs, a founder can add such a feature to a Lovable or Cursor-built app in an afternoon.

What takes longer is the question that follows in any serious customer conversation: "Has a DPIA been done for this?" A data protection impact assessment is the GDPR's tool for thinking through high-risk processing before it starts. Many AI features meet the criteria that make a DPIA mandatory, particularly when they process sensitive data, evaluate people or operate at scale. And even when your customer is legally responsible for the DPIA, they will need detailed information from you to complete it.

This guide explains when a DPIA is needed for an AI feature and how to prepare. It is general information, not legal advice.

## Key Takeaways

- **A DPIA is required when processing is likely to result in a high risk** to people's rights and freedoms, under GDPR Article 35.
- **Regulators use criteria such as evaluation or scoring, sensitive data, large scale, vulnerable people and innovative technology.** Meeting two or more usually means a DPIA is needed, and AI features often meet several.
- **The controller is responsible for the DPIA.** If you are a processor for your customers, they carry out the DPIA, but you must provide the information they need.
- **A DPIA describes the processing, assesses necessity and proportionality, identifies risks and defines measures,** and must be done before the processing starts.
- **Technical choices largely determine the outcome:** data minimisation, EU processing, no training use, human review, logging and clear boundaries on what the AI can access.

## What a DPIA Is

Article 35 of the GDPR requires a controller to carry out an assessment of the impact of planned processing on the protection of personal data when that processing, particularly using new technologies, is likely to result in a high risk. The assessment must contain at least:

1. A systematic description of the processing and its purposes
2. An assessment of the necessity and proportionality of the processing in relation to its purposes
3. An assessment of the risks to the rights and freedoms of data subjects
4. The measures envisaged to address the risks, including safeguards and security measures

If the assessment shows a high risk that cannot be sufficiently reduced, the controller must consult the supervisory authority before starting, under Article 36. In the Netherlands, that is the Autoriteit Persoonsgegevens.

## When Is a DPIA Required?

Article 35 lists three situations where a DPIA is always required: systematic and extensive evaluation of people based on automated processing, including profiling, with legal or similarly significant effects; large-scale processing of special categories of data or criminal data; and systematic large-scale monitoring of publicly accessible areas.

Beyond those, European regulators have published criteria to judge whether processing is likely to be high risk. The guidelines adopted by the Article 29 Working Party, endorsed by the European Data Protection Board, list nine:

| Criterion | Example in an AI feature |
| --- | --- |
| Evaluation or scoring | Ranking job applicants, predicting customer churn per person, rating employee performance |
| Automated decisions with significant effect | Automatically rejecting applications or adjusting prices per person |
| Systematic monitoring | Analysing employee communications or activity |
| Sensitive or highly personal data | Health notes, financial details, data about children |
| Large scale | Many data subjects, large volumes, wide geography |
| Matching or combining datasets | Combining CRM data with external data to enrich profiles |
| Vulnerable data subjects | Employees, patients, children, people in financial difficulty |
| Innovative technology | New uses of AI models whose effects are not well understood |
| Preventing people from exercising rights or using a service | AI screening that blocks access to a service |

As a rule of thumb, processing that meets two or more criteria generally requires a DPIA. AI features frequently meet at least two: "innovative technology" plus sensitive data, evaluation or vulnerable data subjects.

The Autoriteit Persoonsgegevens has also published a list of processing types for which a DPIA is mandatory in the Netherlands, covering examples such as large-scale profiling, employee monitoring, processing of health data and certain uses of biometric data. Check that list for your sector.

## Who Is Responsible: Controller or Processor?

In most B2B SaaS products, your customer is the controller for the data they put into your product, and you are their processor. That means:

- **Your customer carries out the DPIA** for their use of your AI feature.
- **You must assist them,** under Article 28, by providing information about the processing, security measures and sub-processors.
- **If you decide the purposes and means yourself,** for example using customer data to train your own model, you may become a controller for that processing and need your own DPIA and legal basis.

In practice, customers increasingly expect suppliers to provide a "DPIA input pack" for AI features. Providing it proactively saves weeks in sales and shows that you have thought the feature through.

## Typical Risks of AI Features

When you describe an AI feature for a DPIA, expect these risks to be discussed:

**Data sent to third parties.** Prompts containing personal data are sent to an AI provider. Where is it processed? Is it stored? Is it used for training? Who at the provider can access it?

**Inaccurate output.** AI models can generate incorrect or fabricated content. If output becomes part of a record about a person, such as a summary of a patient consultation or an assessment of a candidate, errors can harm them.

**Bias and unfair outcomes.** Models may reflect biases present in their training data, which matters for any feature that ranks, scores or recommends people.

**Excessive access.** An AI assistant with access to all of a customer's data may surface information to users who should not see it, if it does not respect your permission model.

**Prompt injection.** Content from documents, emails or web pages can contain instructions that manipulate the model into leaking data or taking unintended actions.

**Lack of transparency.** Data subjects may not know that AI processes their data, or how it influences decisions about them.

**Retention.** Prompts and outputs stored in logs indefinitely, with personal data inside.

## Technical Measures That Reduce Risk

The good news for founders is that most of these risks can be reduced substantially through design choices, and those choices largely determine how a DPIA concludes.

| Risk | Measure |
| --- | --- |
| Data sent to third parties | EU-region endpoints where available, processing agreement with the AI provider, contractual exclusion of training use, minimal data in prompts |
| Inaccurate output | Human review before output is saved or acted on, clear labelling as AI-generated, easy correction |
| Bias | Avoid automated decisions about people, test outputs across groups, document limitations |
| Excessive access | Retrieval that respects the user's permissions, enforced in the database, not only in the prompt |
| Prompt injection | Treat content as untrusted, limit tool permissions, separate instructions from data, log actions |
| Transparency | Explain AI use in the interface and privacy information, offer opt-outs where appropriate |
| Retention | Short retention for prompts and outputs, no personal data in debug logs |

Our guides on [choosing an LLM API for an EU SaaS](https://launchstudio.eu/en/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral) and [AI feature fallbacks](https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down) cover provider choice and resilience in more depth.

## The DPIA Input Pack for Customers

If you are a processor, prepare a short document for each AI feature containing:

1. **Feature description:** what it does, who uses it and what data it processes
2. **Data flow:** which data is sent to which AI provider, in which region, and what comes back
3. **Sub-processors:** the AI provider and any other services involved, with agreements
4. **Data use terms:** confirmation that data is not used for training and how long the provider retains it
5. **Access control:** how the feature respects user permissions
6. **Human oversight:** where users review and correct output
7. **Security measures:** encryption, logging, prompt injection mitigations
8. **Retention:** how long prompts, outputs and logs are kept
9. **Configuration options:** whether customers can disable the feature or limit it to certain users or data
10. **Known limitations:** accuracy, languages, edge cases

This pack lets your customer complete their DPIA quickly and gives their privacy officer confidence in the feature.

## The EU AI Act Alongside the GDPR

The EU AI Act adds another layer for some AI uses. Systems classified as high-risk, such as certain AI used in employment, education, access to essential services or as safety components of medical devices, carry their own obligations for providers and deployers, including, for some deployers, a fundamental rights impact assessment. Many common SaaS AI features, such as drafting text or summarising documents for professionals, are not high-risk under the AI Act, but features that evaluate people in employment or education contexts may be. A DPIA and an AI Act assessment can be prepared together where both apply.

## When to Do It

A DPIA must be done before the processing starts. For a SaaS company, that means:

- **During feature design,** when choices about data, provider and review are still open
- **Before a pilot with real customer data,** not after
- **When the feature changes significantly,** for example a new provider, new data types or automated actions

Doing it early is also cheaper: changing the design of a feature before release is easier than retrofitting safeguards after customers depend on it.

## How LaunchStudio Helps

LaunchStudio builds AI features in AI-built products with the safeguards that DPIAs look for: EU endpoints and processing agreements, minimal prompts, permission-aware retrieval enforced in the database, human review steps, prompt injection mitigations, short retention and logging. We also prepare the technical content of a DPIA input pack for your customers.

The **Launch Ready** package (€800-€3,500) covers security review and hardening of an existing AI feature; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support for products with several AI features. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink's cybersecurity background shapes how we approach data flows and access control in AI features. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Debt Counselling Assistant That Saw Every Client File

Fatima Ouali, a former debt counsellor in Zaandam, built Schuldwijzer with Cursor and Supabase: a case management tool for debt counselling organisations, where counsellors track clients' debts, creditors, payment plans and documents. She added an AI assistant that answered counsellors' questions about a client's situation and drafted letters to creditors. A municipal debt counselling service wanted to use it, and its privacy officer required a DPIA.

The DPIA work raised immediate concerns. Clients in debt counselling are vulnerable, the data included income, health information affecting payment capacity and family circumstances, and the feature was new technology, meeting several high-risk criteria at once. Technically, the assistant retrieved documents across the whole organisation rather than only the counsellor's caseload, prompts went to a US endpoint without a processing agreement, full prompts and answers were stored in logs indefinitely, and AI-drafted letters could be sent without review.

LaunchStudio redesigned the retrieval so the assistant only accessed documents the counsellor was permitted to see, enforced through Row Level Security on the underlying queries. The AI provider was switched to an EU endpoint under a processing agreement with no training use, prompts were stripped of identifiers that were not needed for the task, and logs were limited to metadata with 30-day retention. Drafted letters required counsellor review and edit before sending, with clear AI labelling, and instructions embedded in uploaded documents were treated as data rather than commands. Engineers wrote a DPIA input pack describing data flows, measures and limitations, which the municipality's privacy officer used to complete the assessment.

**Result:** The municipality's DPIA concluded that residual risks were acceptable with the measures in place, and the service rolled out Schuldwijzer to 25 counsellors. Counsellors report saving around an hour a day on letters, and no letters have been sent without review.

> *"My clients are often in the most stressful period of their lives. The AI had to be helpful without ever being careless with their information."*
> - **Fatima Ouali, Founder, Schuldwijzer (Zaandam)**

**Cost & Timeline:** €4,400 (Launch & Grow package: permission-aware retrieval, EU AI provider, prompt minimisation, review workflow, logging changes and DPIA input pack) - completed in 12 business days.

## Frequently Asked Questions

### Does every AI feature need a DPIA?

No. A DPIA is required when processing is likely to result in a high risk. A feature that drafts marketing copy without personal data probably does not need one. Features that process sensitive data, evaluate people, involve vulnerable groups or operate at scale often meet two or more risk criteria and generally require one.

### Who carries out the DPIA, my company or my customer?

The controller. In most B2B SaaS products, your customer is the controller for their data and carries out the DPIA, while you, as processor, provide the information they need. If you use customer data for your own purposes, such as training your own models, you may be a controller for that and need your own DPIA.

### What happens if a DPIA shows high risk?

The controller must take measures to reduce the risk. If a high risk remains that cannot be sufficiently mitigated, the controller must consult the supervisory authority before starting the processing. Good technical design usually prevents this by reducing risks during development.

### How does Manifera's experience help with AI features and DPIAs?

Manifera has built systems under European privacy and security requirements for 11+ years. LaunchStudio uses that experience to design AI features whose data flows, access control and oversight hold up under a DPIA, rather than adding safeguards after a privacy officer objects.

### Does a privacy-conscious AI feature help my product's visibility?

Yes. Buyers increasingly search for AI tools that are GDPR-compliant and EU-hosted. Publishing clear information about how your AI features handle data helps procurement teams shortlist you, and that structured information is also what search engines and AI answer engines surface.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does every AI feature need a DPIA?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. It is required when processing is likely high risk. Features processing sensitive data, evaluating people, involving vulnerable groups or operating at scale often require one." }
    },
    {
      "@type": "Question",
      "name": "Who carries out the DPIA, my company or my customer?",
      "acceptedAnswer": { "@type": "Answer", "text": "The controller, usually the customer in B2B SaaS, with the supplier as processor providing information. Using customer data for your own purposes may make you a controller." }
    },
    {
      "@type": "Question",
      "name": "What happens if a DPIA shows high risk?",
      "acceptedAnswer": { "@type": "Answer", "text": "The controller must reduce the risk; if a high residual risk remains, it must consult the supervisory authority before processing starts." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with AI features and DPIAs?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built systems under European privacy and security requirements for 11+ years, and LaunchStudio designs AI features whose data flows and oversight hold up under a DPIA." }
    },
    {
      "@type": "Question",
      "name": "Does a privacy-conscious AI feature help my product's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Clear information on how AI features handle data helps buyers shortlist you and is surfaced by search and AI engines." }
    }
  ]
}
</script>
