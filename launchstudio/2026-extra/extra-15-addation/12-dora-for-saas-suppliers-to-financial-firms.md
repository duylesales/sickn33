---
Title: "DORA for SaaS Suppliers to Financial Firms"
Keywords: dora saas supplier, dora ict third party, dora contract requirements, selling saas to banks europe, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# DORA for SaaS Suppliers to Financial Firms

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DORA for SaaS Suppliers to Financial Firms",
  "description": "The Digital Operational Resilience Act applies to EU financial entities, but SaaS startups selling to banks, insurers, payment firms and investment companies feel it through contracts, audits and exit requirements. This guide explains what DORA asks of ICT third-party providers, the contract clauses to expect, the technical evidence buyers want and how to prepare an AI-built SaaS.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-29",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dora-for-saas-suppliers-to-financial-firms" },
  "citation": [
    { "@type": "CreativeWork", "name": "Regulation (EU) 2022/2554 (DORA)", "url": "https://eur-lex.europa.eu/eli/reg/2022/2554/oj" },
    { "@type": "CreativeWork", "name": "EIOPA: Digital Operational Resilience Act", "url": "https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en" },
    { "@type": "CreativeWork", "name": "De Nederlandsche Bank: DORA", "url": "https://www.dnb.nl/en/sector-information/open-book-supervision/laws-and-eu-regulations/dora/" },
    { "@type": "CreativeWork", "name": "AFM: DORA", "url": "https://www.afm.nl/en/sector/themas/dora" }
  ]
}
</script>

Financial firms are attractive customers for SaaS startups. They have budgets, they buy specialised tools and they stay for years once a tool is embedded in their processes. A founder who builds a compliance dashboard, an onboarding tool, a document workflow or an analytics product for banks, insurers, payment companies or investment firms can find a profitable niche quickly.

Since January 2025, those buyers operate under the Digital Operational Resilience Act, better known as DORA. DORA does not regulate your startup directly in most cases. It regulates your customer, and one of its central themes is how financial entities manage the risks of the technology suppliers they depend on. That means procurement for even a small SaaS tool now comes with contract clauses, audit rights, exit plans and security evidence that many startups have never seen before.

This guide explains what DORA means for a SaaS supplier, and how to prepare your product so the procurement process becomes an advantage rather than a wall. It is a practical overview, not legal advice.

## Key Takeaways

- **DORA applies to EU financial entities from 17 January 2025.** SaaS suppliers are affected as ICT third-party service providers through their customers' obligations.
- **Contracts must contain specific provisions** under Article 30, including service descriptions, data location, security, incident support, audit and access rights, termination rights and exit strategies.
- **Requirements are stricter when your service supports a critical or important function** of the financial entity.
- **Financial entities must keep a register of all ICT contracts,** so expect detailed questions about your service, sub-contractors and data locations.
- **The technical work is familiar:** access control, logging, backups, incident response, resilience testing and a documented exit path.

## What DORA Is

DORA, Regulation (EU) 2022/2554, is a directly applicable EU regulation for the financial sector. Unlike a directive, it does not need national transposition, although national supervisors such as De Nederlandsche Bank and the AFM in the Netherlands supervise its application. It covers a wide range of financial entities: banks, payment and e-money institutions, investment firms, crypto-asset service providers, insurers and reinsurers, pension funds above a threshold, crowdfunding platforms and others.

DORA's requirements rest on five pillars:

1. **ICT risk management:** governance, frameworks and controls for technology risk
2. **ICT-related incident management and reporting:** classifying and reporting major incidents to supervisors
3. **Digital operational resilience testing:** from basic testing to threat-led penetration testing for larger entities
4. **ICT third-party risk management:** managing the risks of technology suppliers
5. **Information sharing:** voluntary exchange of threat intelligence

For a SaaS supplier, pillar four is where DORA touches you most directly, with pillars two and three appearing in contract clauses.

## How DORA Reaches a SaaS Supplier

DORA treats any company providing digital and data services to a financial entity as an ICT third-party service provider. That includes cloud platforms, data centres and also software vendors delivering services on an ongoing basis, such as SaaS. Your customer must:

- **Assess risks before contracting,** including your security, financial stability and the concentration risk of relying on you
- **Record the contract in a register of information** that supervisors can request
- **Include mandatory contractual provisions** in the agreement with you
- **Monitor you during the contract,** including through audits
- **Have an exit strategy** so the service can be replaced without disrupting operations

The largest cloud providers may be designated as critical ICT third-party providers and supervised directly by the European Supervisory Authorities. A SaaS startup is very unlikely to be designated, but it will still be managed carefully by its financial customers.

## The Contract Clauses to Expect

Article 30 of DORA lists provisions that contracts for ICT services must contain. Expect your customer's legal team to send a contract or addendum covering:

| Provision | What it means for you |
| --- | --- |
| Clear service description | What you provide, including any sub-contracting, in writing |
| Locations | Where services are provided and where data is processed and stored |
| Data protection and security | How you protect availability, authenticity, integrity and confidentiality |
| Access and return of data | How data is returned if you become insolvent or the contract ends |
| Service levels | Measurable service levels, with updates when they change |
| Incident assistance | Support to the customer during ICT incidents, at an agreed cost |
| Cooperation with authorities | Cooperation with supervisors, including those overseeing the customer |
| Termination rights | Situations in which the customer can end the contract, with notice periods |
| Training participation | Participation in the customer's security awareness programmes where relevant |

When your service supports a **critical or important function** of the financial entity, additional provisions apply, including detailed service level descriptions with quantitative targets, notice and reporting obligations, business continuity plans that you test, participation in the customer's resilience testing where relevant, unrestricted rights of access, inspection and audit, and exit strategies with an adequate transition period.

Whether your tool supports a critical or important function is the customer's assessment. A tool that supports payments, customer onboarding or regulatory reporting is more likely to qualify than an internal knowledge base.

## The Technical Evidence Buyers Want

Behind the contract clauses sit practical questions about how your product works. An AI-built SaaS can answer them well, but only if the work has been done.

**Access control and identity.** Customer data isolated per organisation and enforced in the database, MFA for all staff and admin accounts, single sign-on support for the customer's users and documented role definitions.

**Logging and traceability.** Logs of authentication, administrative actions and data exports, retained for an agreed period and available to the customer on request.

**Resilience.** Hosting in an EU region, backups with point-in-time recovery, a tested restore procedure, defined recovery time and recovery point objectives, and monitoring that detects outages quickly.

**Incident management.** A written incident response process with classification, internal escalation and customer notification timelines that support the customer's own DORA reporting duties.

**Vulnerability management.** Dependency monitoring, a patching process with timelines by severity and periodic penetration testing, especially if you support a critical function.

**Sub-contractors.** A list of every provider involved in delivering the service, including hosting, database, email and AI providers, with locations and the services they perform.

**Exit.** A documented way to export all customer data in a usable format, and a commitment to support a transition period.

## Exit Strategies: The Clause Startups Underestimate

DORA requires financial entities to be able to leave a supplier without disrupting their business or breaching regulation. For a SaaS supplier, that becomes a concrete requirement: the customer must be able to get its data out completely and continue operating while it moves to an alternative.

Prepare three things:

1. **A full data export** in a documented, machine-readable format, covering every record and file belonging to the customer, ideally self-service for admins
2. **A transition commitment,** such as continued service for an agreed period after termination
3. **Deletion confirmation** once the customer confirms the migration is complete

A startup that can demonstrate a working export during procurement removes one of the most persistent concerns financial buyers have about small suppliers. Our guide on [customer data export for SaaS](https://launchstudio.eu/en/blog/customer-data-export-csv-and-api-for-saas) explains how to build one.

## AI Features and DORA

If your product includes AI features, financial customers will ask additional questions. Which model provider processes their data? Where? Is data used for training? What happens if the AI provider has an outage? Are outputs logged for review? These questions overlap with the EU AI Act and GDPR, but under DORA the focus is resilience and third-party dependency: your AI provider is a sub-contractor in their supply chain.

Practical measures include contractual guarantees that data is not used for training, EU-region endpoints where available, a fallback when the AI service is unavailable and logs of AI-assisted decisions. Our article on [AI feature fallbacks](https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down) covers the resilience side.

## How the Procurement Process Usually Unfolds

Knowing the sequence helps you plan time and avoid surprises. With financial customers, procurement for a SaaS tool typically runs through five stages, and each one has a DORA dimension.

**1. Business case and pre-assessment.** The team that wants your tool explains it internally. Vendor management decides whether the service is in scope and whether it supports a critical or important function. Your clear service description helps the champion inside the company make this case quickly.

**2. Due diligence questionnaire.** A long assessment covering security, resilience, financial stability, sub-contractors and data locations. Answering within a week, with supporting documents, signals maturity. Vague or delayed answers are a common reason small suppliers lose.

**3. Risk review.** Information security, legal and sometimes the second-line risk function review your answers. Follow-up questions usually concentrate on gaps: missing logs, untested backups or unclear exit arrangements.

**4. Contract negotiation.** The DORA addendum is negotiated alongside commercial terms. Pay attention to audit rights, notice periods and incident assistance costs; these can be shaped, but not removed.

**5. Onboarding and monitoring.** After signing, your service enters the customer's register of information and is reviewed periodically. Expect an annual reassessment and occasional evidence requests.

Founders who budget six to twelve weeks for this process, and prepare documents before the first meeting, generally find it predictable rather than painful.

## A Preparation Checklist

- Security overview document describing architecture, hosting location, access control, encryption, backups, monitoring and incident response
- Sub-contractor register with services and locations
- Service level description with uptime targets, support hours and response times
- Incident response plan with notification timelines
- Business continuity summary with recovery objectives and the date of your last restore test
- Data export capability and exit support statement
- Penetration test summary, if available
- Standard answers to common security questionnaires
- A contract addendum template that addresses Article 30 provisions, prepared with a lawyer

## What It Costs

LaunchStudio helps SaaS founders put the technical foundations in place: access control per organisation, MFA and SSO, audit logging, EU hosting, backups with tested restores, monitoring, data export and incident procedures, plus support in preparing the security documentation financial buyers request. The **Launch Ready** package (€800-€3,500) covers the security work and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for a first estimate.

## The Team Behind LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Manifera has delivered systems for large clients with formal supplier assessments, including Vodafone and TNO. CEO Herre Roelevink's background in cybersecurity, as co-founder of what is now CFLW Cyber Strategies, informs how we prioritise access control, logging and incident readiness. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The KYC Document Tool That Needed an Exit Plan

Priya Ramdin, a former compliance officer at a payment institution in Amsterdam, built Dossiercheck with Lovable and Supabase: a tool that helps small payment and e-money firms collect customer due diligence documents, track expiry dates and prepare files for audits. Two fintech firms used it in a pilot, and a mid-sized payment institution wanted to roll it out across its onboarding team.

The payment institution's vendor management team classified Dossiercheck as supporting an important function and sent a DORA contract addendum, a 90-question assessment and a request for an exit strategy. Priya discovered gaps she had not considered: there was no way to export a customer's full dataset including documents, admin actions were not logged, the database had never been restored from backup, the AI feature that summarised documents called a US endpoint, and there was no written incident process or service level.

LaunchStudio added organisation-level Row Level Security tests, MFA for staff and SAML single sign-on for customer users, and an audit log covering logins, document access and exports. A self-service export produced every record and document in a documented format, point-in-time recovery was enabled with a restore test, and the AI feature moved to an EU endpoint with a contractual no-training commitment and a fallback for outages. Engineers helped Priya document recovery objectives, a sub-contractor register, service levels and an incident plan with notification timelines, which her lawyer used for the contract addendum.

**Result:** The payment institution approved Dossiercheck after one round of follow-up questions, five weeks after the assessment arrived. The export and audit log, initially built for one customer, became standard features that shortened the next two procurement processes considerably.

> *"I knew DORA from the bank side. I hadn't realised how much of it would land on me as a supplier until the addendum arrived."*
> - **Priya Ramdin, Founder, Dossiercheck (Amsterdam)**

**Cost & Timeline:** €6,800 (Launch & Grow package: SSO and MFA, audit logging, data export, backup and restore testing, EU AI endpoint and documentation support) - completed in 17 business days.

## Frequently Asked Questions

### Does DORA apply to my SaaS startup?

DORA applies directly to EU financial entities, not to most SaaS suppliers. However, if you sell to banks, insurers, payment firms or investment companies, they must apply DORA's third-party risk rules to you, which brings contract clauses, assessments and audit rights into your sales process.

### What is a critical or important function under DORA?

It is a function whose disruption would materially impair a financial entity's performance, soundness or compliance. Your customer decides whether your service supports one. If it does, stricter contract provisions apply, including detailed service levels, tested continuity plans, audit rights and exit strategies.

### Do I need a penetration test to sell to financial firms?

DORA does not require every supplier to have one, but many financial customers ask for a recent penetration test summary, especially for services supporting important functions. A focused test of your application and infrastructure is often a worthwhile investment once you target this market.

### How does Manifera's experience help with DORA requirements?

Manifera has delivered systems for large organisations with formal supplier assessments for 11+ years, and its CEO has a cybersecurity background. LaunchStudio uses that experience to build the controls and evidence financial buyers expect without turning a startup into a bank.

### Will DORA readiness help my visibility with financial buyers?

Yes. A public security and compliance page describing EU hosting, access control, incident response and exit support helps buyers shortlist you, and clearly structured information of this kind is often what search engines and AI answer engines surface when buyers research suppliers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does DORA apply to my SaaS startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "DORA applies directly to EU financial entities, not most SaaS suppliers, but financial customers must apply its third-party rules, bringing contract clauses, assessments and audit rights." }
    },
    {
      "@type": "Question",
      "name": "What is a critical or important function under DORA?",
      "acceptedAnswer": { "@type": "Answer", "text": "A function whose disruption would materially impair a financial entity's performance, soundness or compliance. The customer decides; if so, stricter contract provisions apply." }
    },
    {
      "@type": "Question",
      "name": "Do I need a penetration test to sell to financial firms?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always by law, but many financial customers request a recent penetration test summary, especially for services supporting important functions." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with DORA requirements?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has delivered systems under formal supplier assessments for 11+ years and LaunchStudio uses that experience to build the controls and evidence financial buyers expect." }
    },
    {
      "@type": "Question",
      "name": "Will DORA readiness help my visibility with financial buyers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A public security and compliance page helps buyers shortlist suppliers and is the kind of structured information search and AI engines surface." }
    }
  ]
}
</script>
