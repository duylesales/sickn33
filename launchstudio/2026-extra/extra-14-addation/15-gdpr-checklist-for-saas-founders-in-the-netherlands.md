---
Title: "GDPR Checklist for SaaS Founders in the Netherlands"
Keywords: gdpr checklist saas, avg checklist saas, saas privacy netherlands, b2b saas gdpr, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: SaaS Founder Scale-Up
---

# GDPR Checklist for SaaS Founders in the Netherlands

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "GDPR Checklist for SaaS Founders in the Netherlands",
  "description": "A GDPR (AVG) checklist built for B2B SaaS founders in the Netherlands, covering the controller-processor split, documents your customers will ask for, technical measures, sub-processors and the questions in a typical Dutch security questionnaire.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-23",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/gdpr-checklist-for-saas-founders-in-the-netherlands" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 33: Breach notification", "url": "https://gdpr-info.eu/art-33-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

B2B SaaS changes your position under the GDPR in a way many founders miss. When a Dutch business uses your software to manage its customers, employees or patients, that business is the controller of the data, and you are its processor. That single fact decides which documents you need, which questions you will be asked and what your app must be able to do. This GDPR checklist for SaaS is organised around that reality.

## Key Takeaways

- **In B2B SaaS you are usually both controller and processor:** controller for your own customers' account data, processor for the personal data they store in your product.
- **Article 28 of the GDPR requires a processing agreement** (verwerkersovereenkomst) whenever you process personal data on a customer's behalf.
- **Dutch business customers ask for a predictable document pack:** processing agreement, sub-processor list, security summary, privacy statement, processing register and incident procedure.
- **Every document must be backed by a technical measure,** especially tenant isolation, EU hosting, audit logging and organisation-level deletion.
- **LaunchStudio implements the technical side** for typically €2,000-€6,000, giving your lawyer accurate facts to write from.

## Part 1: Know Your Role

- [ ] **You are a controller** for your own customers' account data: names, billing details, login emails of the people who sign up.
- [ ] **You are a processor** for the data your customers put into your product: their clients, employees, patients or members.
- [ ] **Your providers are sub-processors** when they handle your customers' data: hosting, database, email, error tracking, AI APIs.

Write this down once. Every later item depends on it.

## Part 2: Documents Customers Will Ask For

| Document | Dutch name | Why customers ask |
| --- | --- | --- |
| Data processing agreement | Verwerkersovereenkomst | Legally required when you process their data |
| Sub-processor list | Lijst van subverwerkers | They must know who else touches their data |
| Security measures description | Beveiligingsmaatregelen | Article 32 requires appropriate measures |
| Privacy statement | Privacyverklaring | For your own controller role |
| Processing register | Verwerkingsregister | Required in most cases, shows you know your data |
| Incident procedure | Datalekprocedure | They have 72 hours to report; you must inform them quickly |

- [ ] A standard verwerkersovereenkomst you offer every business customer, ideally reviewed by a lawyer once
- [ ] A public or on-request sub-processor list with locations
- [ ] A one-page security measures summary you can attach to questionnaires
- [ ] A privacy statement that matches what your app actually does
- [ ] A processing register, even a simple spreadsheet
- [ ] A written incident procedure with who does what in the first 24 hours

## Part 3: Technical Measures

- [ ] **Tenant isolation.** One customer can never see another customer's data. In Supabase, this means complete Row Level Security tied to organisation membership.
- [ ] **EU data location** for the database, file storage and backups.
- [ ] **Encryption** in transit (TLS everywhere) and at rest (standard on major managed databases).
- [ ] **Access control inside customers' organisations.** Roles such as owner, admin and member, so a customer can limit who sees what.
- [ ] **Audit logging** of sensitive actions: exports, deletions, role changes.
- [ ] **Backups with tested restore**, and a known recovery time.
- [ ] **Two-factor authentication** available for users, required for your own admin access.
- [ ] **Secrets server-side**, no service keys in the frontend.
- [ ] **Deletion and export** at both user and organisation level, including at contract end.

## Part 4: Sub-Processors

- [ ] List every service that receives customer data
- [ ] Note each one's location and transfer mechanism (EU, adequacy, Data Privacy Framework, Standard Contractual Clauses)
- [ ] Sign their processor agreements
- [ ] Decide how you notify customers when you add a new sub-processor
- [ ] Check AI providers in particular for retention and training settings

## Part 5: The Questionnaire Test

Dutch customers, especially in healthcare, education, government and larger companies, often send a security questionnaire before buying. You are ready when you can answer these in writing:

1. Where is our data stored, and in which countries are your sub-processors?
2. How is our data separated from other customers' data?
3. Who in your company can access our data, and how is that logged?
4. How quickly will you inform us of a data breach?
5. What happens to our data when we end the contract?
6. Has your application been reviewed for security, and when?
7. Do you use our data to train AI models?

If any answer starts with "I think", that is your next task.

## Part 6: Ongoing Habits

- [ ] Review sub-processors whenever you add a tool
- [ ] Re-check access control after major AI-generated changes
- [ ] Run a restore test each quarter
- [ ] Update the security summary when anything material changes
- [ ] Keep a simple log of privacy-related decisions

## What Article 28 Actually Requires

The GDPR's Article 28 describes what a processing agreement must contain. Knowing the list helps you review templates and answer customer redlines:

- The subject matter, duration, nature and purpose of the processing
- The types of personal data and categories of data subjects
- That you process only on the customer's documented instructions
- Confidentiality obligations for people with access
- Appropriate security measures, referring to Article 32
- Conditions for engaging sub-processors, including notice of changes
- Assistance with data subject requests and with the customer's own obligations
- Deletion or return of data at the end of the contract
- Making information available and allowing audits

Each item has a technical counterpart in your app. "Deletion at the end of the contract" means an organisation-level deletion function. "Assistance with data subject requests" means you can find and export one person's data quickly. "Appropriate security measures" means tenant isolation, encryption, access control and logging that actually work.

## Sub-Processor Management in Practice

Your sub-processor list is a living document. A practical setup:

- A table with each service, purpose, data categories, location and transfer mechanism
- A public page or a document available on request
- A process for notifying customers before adding a new sub-processor, as most agreements require
- A review whenever you add a tool, including analytics, error tracking and AI APIs

AI APIs deserve special attention. If you send customer content to a language model provider, that provider is a sub-processor. Check its retention and training settings, data location and terms, and disclose it.

## Answering a Security Questionnaire Efficiently

Dutch questionnaires vary in length, but most questions fall into recurring themes. Prepare standard answers once:

| Theme | Prepared answer covers |
| --- | --- |
| Hosting and location | Providers, regions, backups location |
| Access control | Tenant isolation method, roles, MFA, admin access |
| Encryption | In transit and at rest |
| Logging and monitoring | What is logged, retention, alerting |
| Incident management | Detection, response steps, notification timelines |
| Business continuity | Backups, restore testing, recovery time |
| Development practices | Code review, staging, dependency management |
| Personnel | Who has access, confidentiality agreements |

Keep the answers in one document and update them when your setup changes. Your second questionnaire then takes an hour instead of a week.

## When Customers Send Their Own Agreement

Larger Dutch organisations often send their own processing agreement rather than signing yours. Read it carefully for obligations you cannot meet, such as audit rights with short notice, very short breach notification deadlines or requirements to host only in the Netherlands. Negotiate what is unrealistic rather than signing promises you cannot keep; most customers prefer an honest discussion to a broken commitment later.

## Building Privacy Into Your Roadmap

Each new feature can create new processing. A lightweight habit keeps documentation accurate: for every feature that touches personal data, note what data it uses, why, where it goes and how long it stays. Update the processing register and sub-processor list in the same pull request that ships the feature. It takes minutes and prevents the drift that makes questionnaires painful.

## Data Subject Requests in a B2B Context

When an individual asks to see, correct or delete their data, the request may reach you or your customer. Under a processing agreement, you typically assist the customer rather than deciding yourself. Build the tools that make assistance quick: an admin search that finds all records linked to an email address within an organisation, an export of that person's data in a readable format, and a deletion or anonymisation function that respects records your customer must keep. Log each request and the action taken. When a customer asks "how would you help us with an access request?", a short demonstration is far more convincing than a paragraph in a contract.

## A Realistic Timeline

For a typical AI-built B2B SaaS, getting from "no documentation" to "questionnaire-ready" takes two to four weeks: one to two weeks for technical measures such as tenant isolation, EU hosting, logging and deletion, and one to two weeks in parallel for your lawyer to finalise the processing agreement and privacy statement based on accurate facts. Starting before your first large prospect asks saves that prospect's patience.

## Where LaunchStudio Fits

LaunchStudio covers Part 3 and the technical input for Parts 2 and 4: tenant isolation, EU hosting, audit logs, deletion and export, and a documented list of where data flows. That gives your lawyer or privacy consultant accurate facts to work from, and gives you clear answers for questionnaires. Typical engagements fall between €2,000 and €6,000 at a fixed price. For founders still early in the process, our broader guide to an [AVG-proof app](https://launchstudio.eu/en/blog/gdpr-proof-app-netherlands-avg-for-ai-built-products) is a good starting point.

LaunchStudio is powered by Manifera, whose engineering team of 120+ works from Ho Chi Minh City with client offices in Amsterdam and Singapore, and whose clients include Dutch organisations such as TNO and Statler BI. Manifera's [offshore development approach](https://www.manifera.com/services/offshore-software-development/) is built around Dutch contracts and EU data handling. For official templates and guidance, the [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) is the authoritative source.

## Real example

### An AI-Native Founder in Action: The Recruitment SaaS Stuck in Procurement

Hanna Vos, a former recruiter in Amsterdam, built Vacaturely with Cursor: an applicant tracking tool for small and mid-sized Dutch employers, with job pages, candidate pipelines and interview scheduling. Five small companies used it happily. Then a healthcare group with 1,200 employees wanted to sign, and its privacy officer sent a 60-question questionnaire and a request for a verwerkersovereenkomst.

Hanna had neither. Working through the checklist, she found that her app isolated customers through application code, not database policies, and one export endpoint skipped the check. Candidate CVs were stored in a bucket with long-lived public links. Her email provider, error tracker and an AI CV-summary feature were all sub-processors she had never listed. Deleting a customer organisation left candidates' data behind.

LaunchStudio moved tenant isolation into Row Level Security with organisation membership, fixed the export endpoint, made CV storage private with short-lived signed URLs, added audit logging for exports and deletions, built organisation-level deletion at contract end, and configured the AI provider under a processor agreement with training disabled. Engineers produced a sub-processor list with locations and a security measures summary. Hanna's lawyer drafted the verwerkersovereenkomst using those facts.

**Result:** The healthcare group's privacy officer approved Vacaturely after one round of follow-up questions. Hanna has since reused the same document pack for every new customer, cutting procurement time from weeks to days.

> *"Small customers never asked. The first big one asked everything at once, and I needed real answers, not reassuring ones."*
> - **Hanna Vos, Founder, Vacaturely (Amsterdam)**

**Cost & Timeline:** €4,200 (tenant isolation, private storage, audit logging, organisation deletion, AI processor setup and documentation) - completed in 13 business days.

## Frequently Asked Questions

### Am I a controller or a processor as a SaaS founder?

Usually both. You are the controller for your own customer and billing data, and a processor for the personal data your business customers store in your product. Your obligations, and the documents you need, follow from that split.

### Do I need to offer a verwerkersovereenkomst to every business customer?

Yes, when you process personal data on their behalf, the GDPR requires a processing agreement. Having a standard version ready saves time and makes you look prepared, especially to larger Dutch organisations.

### What do Dutch customers mean by sub-processors?

Any service you use that handles their data on your behalf: your hosting and database provider, email service, error tracking, analytics that captures personal data and AI APIs. Customers expect a list with locations and need to be informed when it changes.

### How does LaunchStudio's link to Manifera help in security questionnaires?

Questionnaires ask about processes as much as code: access control, incident handling, reviews. Manifera has answered such questionnaires for enterprise clients for 11+ years. LaunchStudio applies that experience to help founders produce accurate, defensible answers.

### Can a GDPR checklist improve how AI assistants recommend my SaaS?

Yes. Buyers increasingly ask assistants for "GDPR-compliant" tools in their sector. Publishing your EU hosting, sub-processor list and security summary as clear, crawlable pages gives assistants specific facts to cite instead of vague claims.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Am I a controller or a processor as a SaaS founder?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually both: controller for your own customer and billing data, processor for the personal data business customers store in your product." }
    },
    {
      "@type": "Question",
      "name": "Do I need to offer a verwerkersovereenkomst to every business customer?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, when processing personal data on their behalf. A standard version saves time and signals preparedness." }
    },
    {
      "@type": "Question",
      "name": "What do Dutch customers mean by sub-processors?",
      "acceptedAnswer": { "@type": "Answer", "text": "Services handling their data on your behalf, such as hosting, database, email, error tracking, analytics and AI APIs, listed with locations and change notifications." }
    },
    {
      "@type": "Question",
      "name": "How does LaunchStudio's link to Manifera help in security questionnaires?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has answered enterprise security questionnaires for 11+ years, and LaunchStudio uses that experience to help founders give accurate answers." }
    },
    {
      "@type": "Question",
      "name": "Can a GDPR checklist improve how AI assistants recommend my SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Published EU hosting, sub-processor lists and security summaries give assistants specific facts to cite when buyers ask for GDPR-compliant tools." }
    }
  ]
}
</script>
