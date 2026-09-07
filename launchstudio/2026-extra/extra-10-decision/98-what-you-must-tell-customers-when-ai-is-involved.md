---
Title: "What You Must Tell Customers When AI Is Involved"
Keywords: AI transparency obligations, EU AI Act disclosure, labelling ai generated content, chatbot disclosure requirement, automated decision making gdpr, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What You Must Tell Customers When AI Is Involved

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What You Must Tell Customers When AI Is Involved",
  "description": "Disclosure obligations for AI features are becoming specific rather than aspirational in the EU. What has to be said, where it belongs in the product, the separate GDPR rules on automated decisions, and why clear labelling protects you as much as the customer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-you-must-tell-customers-when-ai-is-involved" }
}
</script>

For most of the past decade, telling users that a feature involved AI was a marketing decision. In the EU it is becoming a compliance one, and the shift matters for small products as much as large ones, because the obligations that arrive first are the transparency obligations — and they apply to ordinary, low-risk features rather than only to dramatic ones.

The practical position for a founder is not to become an expert in the legislation. It is to know which of your features trigger a disclosure requirement, put the disclosure somewhere a person will actually see it, and keep a record of what your product does — which is, conveniently, the same information that answers a business customer's questionnaire.

## Three Sources of Obligation, Not One

It helps to separate them, because they apply differently.

**The EU AI Act's transparency rules.** These are the ones most relevant to ordinary products. Broadly: people should be told when they are interacting with an AI system rather than a person, and certain generated or manipulated content should be identifiable as such. These apply irrespective of whether the underlying system is otherwise considered high risk, and they are the obligations a typical SaaS product encounters first.

**GDPR's rules on automated decisions.** Longstanding and independent of the AI Act. Where a decision is made solely by automated means and has legal or similarly significant effects on a person — eligibility, employment, credit, access to a service — the individual has rights: to meaningful information about the logic involved, to obtain human intervention, and to contest the decision. This is the sharper obligation, and it is triggered by consequence rather than by technology.

**Sector rules and your customers' own obligations.** A clinician, an accountant, or a lawyer using your product has professional duties about what they may rely on and what they must disclose. Even where nothing binds you directly, your product must let them meet their obligations — which usually means being able to see which content was generated.

The pragmatic reading for a small product: assume you must tell people when they are talking to a machine and when content was machine-generated, and treat any feature that decides something consequential about a person as requiring a human in the loop.

## Where the Disclosure Belongs

A line in your terms of service satisfies nobody, including a regulator. Disclosure has to be where the person encounters the thing.

**Conversational features.** If a customer or their end user might reasonably think they are talking to a person, say otherwise at the start of the interaction, plainly. This is the clearest of the requirements and the easiest to meet.

**Generated content.** Label it in the interface where it appears, not in a help article. A short marker next to a summary, a draft, or a suggestion is sufficient and takes minutes to add.

**Content that goes out into the world.** Anything your product produces that will be published — text, images, audio — should be identifiable as generated. Where machine-readable marking is feasible, providers increasingly support it; where it is not, a visible statement is the practical minimum.

**In your documentation**, a plain description of which features use AI, what data they process, and where. Not for the regulator so much as for the business customer who asks, and for your own clarity.

The tone matters less than the placement. Nobody needs a paragraph of legal language; "Summary generated automatically — please check before sending" does the job better than anything longer.

## Decisions About People Need a Person

The obligation that carries the most risk is not disclosure — it is automated decision-making, and it is easy to build accidentally.

A product that scores job applicants, prioritises benefit claims, assesses creditworthiness, flags accounts for suspension, or ranks people for access to something is making decisions with significant effects. If those decisions are made solely by the system, GDPR gives affected individuals specific rights, and the AI Act's obligations for such systems are stricter still.

The straightforward way to stay on comfortable ground is to make sure a person decides. Not a person who rubber-stamps a list — someone who reviews the case, has the information needed to disagree, and sometimes does. The model proposes; a human decides and can be shown to have decided.

Three things make that defensible in practice: the recommendation is visibly a recommendation rather than a verdict; the reviewer can see what it was based on; and the decision, including who made it, is recorded. That last item is the audit trail discussed elsewhere in this cluster, applied to a context where it is not optional.

Building AI features with disclosure in the right places, human review where decisions are consequential, and the records that demonstrate both is a specific and bounded piece of work. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements it as part of preparing AI features for real customers. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Transparency Is Also Self-Protection

Set the legal framing aside for a moment, because the commercial argument points the same way.

An unlabelled AI output that turns out to be wrong is your product asserting something false. A labelled one is a draft the customer was invited to check. The difference in how a complaint unfolds is substantial, and it costs a line of text.

Labelling also sets expectations that reduce support volume. Customers who know a summary was generated treat an imperfect one as expected rather than as a defect worth reporting. And in professional settings it enables the customer to meet their own obligations, which is frequently what determines whether they can adopt your product at all.

The concern founders raise — that admitting AI involvement undermines confidence — is largely obsolete. Customers assume AI is involved, and the products that suffer are those that concealed it and were found out, not those that said so.

## What to Write Down Now

A short internal document, updated as features change, containing: which features use AI and for what; what data each sends and to which provider; where processing occurs; whether output is shown directly to a person or acted upon automatically; whether any of it constitutes a decision about a person; and what disclosure is shown and where.

This takes an hour and serves three purposes at once. It answers procurement questionnaires. It is the basis of your privacy documentation. And it is what tells you, when the obligations are clarified further — as they will be through the AI Act's phased application — whether anything you have built is affected.

None of this is legal advice, and a product making consequential decisions about people, or operating in a regulated sector, should get a qualified opinion rather than relying on an article. But the inventory is the prerequisite for that conversation, and having it makes the conversation short.

## Real example

### The Chatbot That Was Assumed to Be a Person

Eline Vos ran Huurhulp, a tenant-communication tool used by Dutch housing associations, built in Cursor. It included an assistant answering tenant queries about repairs and rent, presented in a chat window with a first name and no indication it was automated.

A tenant spent three exchanges believing they were speaking to a housing officer, received an incorrect answer about a rent adjustment deadline, acted on it, and complained to the association. The association's own review found two problems: tenants were not told they were interacting with an automated system, and the assistant's answers were shown as authoritative statements rather than as generated content requiring verification.

A broader review found a third issue. A feature prioritised repair requests into urgency bands with no human review, and the band determined response time — a decision affecting tenants, made solely by the system, with no route to contest it.

**Result:** the assistant now identifies itself as automated at the start of every conversation and offers a route to a person; generated answers are labelled and carry a note to verify anything time-sensitive; the urgency ranking became a recommendation reviewed by a coordinator before taking effect, with the decision and reviewer recorded; and an AI inventory document was produced for the associations' compliance teams.

> "Nobody set out to mislead anyone. It had a first name and a chat window, and three tenants in a row assumed it was a person because we never said it was not."
> — **Eline Vos, Founder, Huurhulp**

**Cost & Timeline:** disclosure, human review, and documentation delivered in 3 business days.

## Frequently Asked Questions

### Do I have to tell users they are talking to an AI?

Under the EU AI Act's transparency rules, people should be informed when they are interacting with an AI system rather than a person. The disclosure belongs at the start of the interaction, in plain language, not in your terms of service.

### Does AI-generated content need to be labelled?

Content that could be mistaken for human-produced, and particularly anything published outward, should be identifiable as generated. Within a product, a short visible marker next to generated output is the practical standard.

### What counts as an automated decision under GDPR?

A decision made solely by automated means with legal or similarly significant effects on a person, such as eligibility, employment, credit, or access to a service. Affected individuals have rights to meaningful information, human intervention, and to contest it.

### Is a human reviewing a list enough to avoid that?

Only if the review is genuine. The reviewer needs the information to disagree, must sometimes actually disagree, and the decision including who made it should be recorded. A rubber stamp on a ranked list is not human involvement.

### Will telling customers a feature uses AI reduce their trust in it?

Generally the opposite. Customers assume AI is involved, and labelling sets expectations that reduce complaints, while concealment is what damages trust when discovered.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I have to tell users they are talking to an AI?", "acceptedAnswer": { "@type": "Answer", "text": "Under the EU AI Act's transparency rules people should be informed when interacting with an AI system rather than a person, disclosed at the start of the interaction in plain language." } },
    { "@type": "Question", "name": "Does AI-generated content need to be labelled?", "acceptedAnswer": { "@type": "Answer", "text": "Content that could be mistaken for human-produced, particularly anything published outward, should be identifiable as generated. In-product, a short visible marker is the practical standard." } },
    { "@type": "Question", "name": "What counts as an automated decision under GDPR?", "acceptedAnswer": { "@type": "Answer", "text": "A decision made solely by automated means with legal or similarly significant effects, such as eligibility, employment, credit, or access to a service, carrying rights to information, intervention, and contest." } },
    { "@type": "Question", "name": "Is a human reviewing a list enough to avoid that?", "acceptedAnswer": { "@type": "Answer", "text": "Only if the review is genuine: the reviewer must have the information to disagree, sometimes disagree, and the decision and reviewer should be recorded." } },
    { "@type": "Question", "name": "Will telling customers a feature uses AI reduce their trust in it?", "acceptedAnswer": { "@type": "Answer", "text": "Generally the opposite. Customers assume AI is involved, labelling sets expectations that reduce complaints, and concealment is what damages trust when discovered." } }
  ]
}
</script>
