---
Title: "Selling SaaS to Dutch Municipalities: BIO and Security Requirements"
Keywords: saas gemeente, bio baseline informatiebeveiliging overheid, selling software to municipalities netherlands, gibit voorwaarden, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Selling SaaS to Dutch Municipalities: BIO and Security Requirements

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Selling SaaS to Dutch Municipalities: BIO and Security Requirements",
  "description": "Dutch municipalities buy software under the Baseline Informatiebeveiliging Overheid (BIO), standard IT purchasing conditions and procurement rules. This guide explains what BIO means for a SaaS supplier, the documents and controls municipalities expect, how procurement works for smaller contracts, and how to prepare an AI-built product for a first municipal customer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-11",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/selling-saas-to-dutch-municipalities-bio-and-security-requirements" },
  "citation": [
    { "@type": "CreativeWork", "name": "Baseline Informatiebeveiliging Overheid (BIO)", "url": "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/" },
    { "@type": "CreativeWork", "name": "VNG Informatiebeveiligingsdienst (IBD)", "url": "https://www.informatiebeveiligingsdienst.nl/" },
    { "@type": "CreativeWork", "name": "VNG: GIBIT inkoopvoorwaarden", "url": "https://vng.nl/artikelen/gibit" },
    { "@type": "CreativeWork", "name": "PIANOo: Dutch public procurement expertise centre", "url": "https://www.pianoo.nl/en" }
  ]
}
</script>

Municipalities are an attractive market for software founders. There are more than three hundred of them in the Netherlands, they share similar responsibilities, they face constant pressure to work more efficiently and they talk to each other. A tool that works for one municipality, whether for permits, social services, public space reports, volunteer coordination or internal workflows, often spreads to neighbouring ones.

They are also demanding customers. Municipalities handle personal data about residents, sometimes sensitive data about income, health or family situations, and they are accountable to councils, auditors and the public. Their information security is governed by a shared baseline, the BIO, and their purchasing follows standard conditions and procurement law. A founder who arrives with an AI-built prototype and no answers to security questions will rarely get past the first conversation.

This guide explains what municipalities expect from SaaS suppliers and how to prepare. It is general information, not legal or procurement advice.

## Key Takeaways

- **The BIO is the information security baseline for Dutch government,** including municipalities, based on ISO 27001 and ISO 27002. Municipalities apply it to their suppliers through contracts and assessments.
- **Standard IT purchasing conditions, such as the GIBIT,** are widely used by municipalities and contain clauses on security, data, continuity and exit.
- **Municipalities account for their security annually,** which is why they ask suppliers for evidence such as policies, certificates or assurance reports.
- **Procurement rules depend on contract value.** Smaller contracts can often be awarded through simpler procedures, which makes pilots realistic for startups.
- **The technical baseline matters most:** EU hosting, strong authentication, role-based access, logging, backups, vulnerability management and a processing agreement.

## What the BIO Is

The Baseline Informatiebeveiliging Overheid is the common framework for information security across Dutch government layers: central government, provinces, municipalities and water boards. It builds on ISO/IEC 27001 and 27002 and adds government-specific measures. It has been updated to align with the 2022 versions of the ISO standards and with the direction set by NIS2, so check which version your prospective customer applies.

The BIO is risk-based. Organisations assess their information and systems, determine the required level of protection and apply the corresponding measures. For a supplier, the important point is that a municipality is responsible for the security of its information even when it is processed in your SaaS. The municipality therefore needs to assess whether your service meets the measures relevant to the data and processes involved.

The VNG's Informatiebeveiligingsdienst (IBD) supports municipalities with guidance, templates and tools on information security, including advice on supplier management. Many municipalities use IBD materials when assessing suppliers.

## How Municipalities Account for Security

Municipalities report on their information security through ENSIA, a framework for annual accountability that covers the BIO and specific systems such as DigiD and the national base registers. That annual cycle is why municipal information security officers ask suppliers for evidence they can rely on: certificates such as ISO 27001, assurance reports, completed security questionnaires and contractual commitments.

For a startup, this means security conversations are not a formality. The person asking has to justify their decision to auditors, and your answers become part of that justification.

## Purchasing Conditions: The GIBIT

Many municipalities use the Gemeentelijke Inkoopvoorwaarden bij IT, known as GIBIT, as standard terms for buying IT products and services. The GIBIT includes clauses on, among other things:

- Information security and compliance with relevant standards
- Personal data processing and processing agreements
- Confidentiality
- Continuity and escrow arrangements
- Exit, data return and migration support
- Intellectual property and licences
- Liability

Read the current version before your first municipal sale. Some clauses, such as continuity and exit, may require arrangements you have not considered, for example a documented way to return all data in a usable format at the end of the contract.

## Procurement: How Startups Get a First Contract

Public procurement in the Netherlands is governed by the Aanbestedingswet and, for municipalities, their own procurement policies. The required procedure depends mainly on the estimated contract value:

- **Above European thresholds:** a European tender procedure is required, with formal publication and strict rules.
- **Below European thresholds:** municipalities follow their own procurement policy, which often allows a national procedure, a multiple-quote procedure or, for small amounts, a direct award.

PIANOo, the Dutch public procurement expertise centre, publishes guidance on procedures and current thresholds. For startups, the practical takeaway is that a pilot or small first contract can often be awarded through a simpler procedure, as long as the municipality follows its own policy. Many software startups enter the market this way, then compete in larger procedures once they have references.

Innovation-oriented procurement instruments, such as innovation partnerships and Small Business Innovation Research (SBIR) calls, are also used by some public bodies to work with startups on specific challenges.

## What Municipalities Will Ask You

Expect a security and privacy assessment covering:

| Area | Typical questions | What a good answer looks like |
| --- | --- | --- |
| Hosting | Where is data stored and processed? | EU hosting, named providers and regions |
| Certification | Do you have ISO 27001 or comparable evidence? | Certificate, or a documented plan and security overview |
| Authentication | How do employees log in? | SSO with the municipality's identity provider, MFA |
| Access control | Who can see which data? | Role-based access per organisation and team, enforced in the database |
| Logging | Are actions logged and retained? | Access and admin actions logged, retention defined, export possible |
| Vulnerabilities | How do you handle security updates and testing? | Dependency monitoring, patch timelines, periodic penetration tests |
| Incidents | How and when do you report incidents? | Written procedure, notification within agreed hours |
| Continuity | What if your company stops? | Backups, exit plan, data export, possibly escrow |
| Privacy | Do you sign a processing agreement? | Yes, aligned with municipal templates, with sub-processor list |
| Residents | Do residents log in, and how? | Secure resident authentication appropriate to the data |

If residents log in to your service to access personal government matters, municipalities may require DigiD or another recognised login method, which comes with its own security requirements and assessment. Clarify this early, because it affects architecture and timelines.

## The Technical Baseline for an AI-Built Product

AI-built prototypes usually need work in the same areas before they meet municipal expectations:

- **SSO for municipal employees,** typically through SAML or OpenID Connect with the municipality's identity provider, so accounts are managed centrally and removed when people leave
- **MFA** for all administrative access
- **Row Level Security or equivalent** isolating each municipality's data, with roles inside each organisation
- **Audit logging** of logins, data access, changes and exports, available to the municipality
- **EU hosting** with providers that offer appropriate agreements
- **Private file storage** with signed, expiring links
- **Backups** with tested restores and defined recovery objectives
- **Vulnerability management:** dependency alerts, patch process, periodic penetration testing
- **Separated environments** with no real resident data in development or staging
- **Data export** for exit and for answering residents' access requests

## Documents to Prepare

A municipal sales process goes much faster with a ready set of documents:

1. Security overview mapped to BIO and ISO 27002 themes
2. Processing agreement draft and sub-processor list
3. Completed standard questionnaire answers
4. Incident procedure with notification timelines
5. Continuity and exit description, including data export format
6. Penetration test summary, if available
7. Accessibility statement, since government websites and apps must meet accessibility standards
8. Product and support description with service levels

Accessibility deserves a special mention. Government bodies in the Netherlands are required to make their websites and apps accessible, and resident-facing tools you supply will be expected to meet WCAG. Our guide on [WCAG accessibility fixes for AI-built apps](https://launchstudio.eu/en/blog/wcag-accessibility-fixes-for-ai-built-apps) covers the technical work.

## Who You Will Meet Inside a Municipality

A municipal purchase usually involves several people with different concerns. Knowing them helps you prepare the right material for each:

- **The business owner,** often a team lead or policy officer, who wants the tool and champions it internally. They need a clear description of benefits and a realistic implementation plan.
- **The CISO or information security officer,** who assesses your security against the BIO. They need your security overview, questionnaire answers and evidence.
- **The privacy officer or data protection officer,** who reviews the processing agreement, the data flows and whether a DPIA is needed. They need precise descriptions of what personal data you process and why.
- **The purchasing adviser,** who determines the procedure and applies the purchasing conditions. They need clear pricing, contract terms and your acceptance of standard conditions or proposed deviations.
- **The IT or functional management team,** who will connect SSO, manage accounts and handle support. They need technical documentation and a contact person.

Founders who address each role directly, rather than sending one large document to everyone, typically move through the process faster. A short call with the security officer early in the process, before formal assessment, often prevents weeks of written back-and-forth.

## Common Mistakes

**Leading with features, not assurance.** Municipal buyers often need security and privacy answers before they can discuss features internally.

**Ignoring the exit clause.** Being able to return all data in a usable format, and to support a transition, is a standard expectation.

**Using real resident data in tests.** A pilot municipality's export imported into a staging environment creates a serious compliance issue.

**Assuming one municipality's approval works everywhere.** Each municipality makes its own decisions, though references and shared templates help considerably.

**Underestimating timelines.** Even small contracts can take months between first conversation and signature. Plan cash flow accordingly.

## How LaunchStudio Helps

LaunchStudio takes AI-built products to the technical level municipalities expect: SSO and MFA, tenant isolation with Row Level Security, audit logging, EU hosting, private storage, tested backups, vulnerability management, data export and separated environments. We also help prepare the technical content of your security overview and questionnaire answers.

The **Launch Ready** package (€800-€3,500) covers security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, backups, monitoring and priority support, which suits most government-facing products. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with experience delivering systems under formal security requirements for organisations such as TNO. CEO Herre Roelevink co-founded the cybersecurity company now known as CFLW Cyber Strategies. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Public Space Reporting Tool That Had No Exit Plan

Martijn Koster, a former municipal civil servant, built Buitenmelder with Bolt and Supabase: a tool where residents report problems in public space, such as broken streetlights, litter or damaged pavements, and municipal teams plan and track repairs. A municipality in Noord-Holland liked the pilot and wanted a contract, subject to an assessment by its information security officer and its standard IT purchasing conditions.

The assessment surfaced issues across the board. Municipal employees used separate passwords without MFA, while the municipality required SSO with its own identity provider. All teams could see all reports, including those containing residents' names, addresses and photos. Photos were stored in a public bucket. There were no audit logs, hosting was in a US region, there was no processing agreement, and the purchasing conditions required an exit arrangement with full data return, which Buitenmelder could not provide.

LaunchStudio implemented SAML SSO for municipal staff with MFA enforced by the municipality's identity provider, and Row Level Security that isolated each municipality's data and restricted residents' personal details to the teams handling their reports. Photos moved to private storage with signed links and automatic removal of location metadata from resident uploads, and an audit log recorded logins, report views, changes and exports. The application was moved to EU hosting with tested backups, a full data export in documented formats was added for exit, and engineers prepared the technical sections of a BIO-mapped security overview, which Martijn completed with a processing agreement drafted with a lawyer.

**Result:** The municipality approved Buitenmelder after the security officer's second review, and the contract was signed under its purchasing conditions with the exit arrangement included. Within the following year, two neighbouring municipalities adopted it, reusing most of the assessment documentation.

> *"I used to work inside a municipality, so I knew they were careful. I hadn't realised how much of that care would need to be visible in my own product."*
> - **Martijn Koster, Founder, Buitenmelder (Alkmaar)**

**Cost & Timeline:** €6,900 (Launch & Grow package: SAML SSO, tenant isolation, private storage, audit logging, EU hosting, data export and security documentation support) - completed in 18 business days.

## Frequently Asked Questions

### Do I need ISO 27001 to sell to a Dutch municipality?

Not always. Municipalities must apply the BIO and assess suppliers, and some require ISO 27001 or comparable certification, especially for sensitive data or larger contracts. For pilots and smaller contracts, a documented security overview, completed questionnaires and strong technical controls are often accepted, with certification expected as you grow.

### Can a startup win a municipal contract without a European tender?

Often, yes, for smaller contracts. Below European thresholds, municipalities follow their own procurement policies, which frequently allow simpler procedures or direct awards for small amounts. Larger contracts require formal tenders, where references from earlier municipal customers help.

### What is the GIBIT?

The GIBIT is a set of standard IT purchasing conditions used by many Dutch municipalities. It covers topics such as information security, data processing, continuity, exit and liability. Review it before your first municipal contract, because it may require arrangements such as full data return at the end of the contract.

### How does Manifera's experience help with government customers?

Manifera has delivered systems under formal security requirements for 11+ years, and its CEO has a cybersecurity background. LaunchStudio applies that experience to implement SSO, tenant isolation, logging and exit capabilities that municipal security officers look for first.

### Does government readiness help my visibility with other municipalities?

Yes. Municipalities share experiences and references, and a clear public page describing your BIO approach, hosting and accessibility helps procurement teams find you. Search engines and AI answer engines also surface such information when officials research suppliers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need ISO 27001 to sell to a Dutch municipality?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always. Some municipalities require it for sensitive data or larger contracts; for pilots, a documented security overview and strong controls are often accepted." }
    },
    {
      "@type": "Question",
      "name": "Can a startup win a municipal contract without a European tender?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often yes for smaller contracts below European thresholds, under the municipality's own procurement policy. Larger contracts require formal tenders." }
    },
    {
      "@type": "Question",
      "name": "What is the GIBIT?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standard IT purchasing conditions used by many Dutch municipalities, covering security, data processing, continuity, exit and liability." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with government customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has delivered systems under formal security requirements for 11+ years, and LaunchStudio implements SSO, tenant isolation, logging and exit capabilities security officers check." }
    },
    {
      "@type": "Question",
      "name": "Does government readiness help my visibility with other municipalities?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. References and a clear public page on BIO approach, hosting and accessibility help procurement teams and AI engines find you." }
    }
  ]
}
</script>
