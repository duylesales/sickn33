---
Title: "Selling an AI-Built App to Dutch Healthcare: NEN 7510 and AVG"
Keywords: nen 7510 app, healthcare app netherlands, zorg app avg, nen 7513 logging, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# Selling an AI-Built App to Dutch Healthcare: NEN 7510 and AVG

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Selling an AI-Built App to Dutch Healthcare: NEN 7510 and AVG",
  "description": "Dutch healthcare providers ask suppliers about NEN 7510, access logging and health data protection. This guide explains what these requirements mean for an AI-built app, which technical measures buyers expect and how to prepare without overbuilding.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-23",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/selling-an-ai-built-app-to-dutch-healthcare-nen-7510-and-avg" },
  "citation": [
    { "@type": "CreativeWork", "name": "NEN", "url": "https://www.nen.nl/" },
    { "@type": "CreativeWork", "name": "GDPR Article 9: Special categories", "url": "https://gdpr-info.eu/art-9-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 35: Data protection impact assessment", "url": "https://gdpr-info.eu/art-35-gdpr/" },
    { "@type": "CreativeWork", "name": "EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

A physiotherapy group, a GP cooperative or a home care organisation likes your app. Then their information security officer sends questions: "Are you NEN 7510 certified? How do you log access to client data? Where is health data stored?" Health data is a special category under the GDPR (AVG), and Dutch healthcare has its own information security standards. An AI-built app can meet these expectations, but not by default.

This article is general guidance, not legal or certification advice.

## Key Takeaways

- **Dutch healthcare buyers expect suppliers to support NEN 7510 information security,** NEN 7513 access logging and the stricter GDPR rules for health data.
- **Health data is a special category under Article 9 of the GDPR,** requiring an additional legal condition and appropriate safeguards.
- **Certification is not always required at first;** many buyers accept documented measures and a credible roadmap, but ask early.
- **Technical essentials:** strict need-to-know access, tamper-resistant access logs, EU hosting, encryption, MFA and careful AI processing.
- **This is general guidance;** consult specialists for certification and legal questions.

## The Standards You Will Hear About

| Standard | What it covers |
| --- | --- |
| NEN 7510 | Information security management in healthcare, based on ISO 27001 with healthcare-specific controls |
| NEN 7512 | Trust basis for exchanging health data electronically |
| NEN 7513 | Logging of actions on electronic health records: who accessed what, when |
| AVG (GDPR) | Health data as a special category: stricter conditions and safeguards |

Healthcare providers are responsible for complying with these standards in their own organisation. They therefore expect suppliers to support them, sometimes with certification, often with demonstrable measures.

## Certification vs Demonstrable Measures

Full NEN 7510 or ISO 27001 certification is a management system for the whole organisation, with audits and ongoing effort. For a young company, it may be a goal rather than a starting point. Many healthcare buyers accept a credible path: documented measures, a security policy, processor agreements and evidence of technical controls, sometimes combined with a timeline towards certification. Ask your buyer what they require.

## Technical Measures Buyers Expect

- **Strict access control:** care professionals see only clients they are involved with; administrators are limited and logged
- **Access logging in the spirit of NEN 7513:** who viewed or changed which client record, when, from where, retained and reviewable
- **EU hosting** of all health data, including backups and files
- **Encryption** in transit and at rest
- **Strong authentication:** two-factor authentication for professionals
- **Data minimisation:** collect only what the care process needs; be careful with BSN numbers, which have specific legal rules in healthcare
- **Incident procedure** with fast notification to the healthcare provider
- **Processor agreement** that matches healthcare expectations
- **AI features handled carefully:** if health data goes to an AI model, the provider, location, retention and legal basis need extra scrutiny

## AI-Built Apps: The Usual Gaps

Typical Lovable or Bolt apps in healthcare pilots lack access logging, use broad access policies, store files in public buckets, run in non-EU regions and send data to AI APIs without agreements. Each of these is fixable; together they make a questionnaire impossible to pass.

## Preparing Without Overbuilding

1. Ask the buyer which standards and evidence they require
2. Fix technical measures first: access, logging, MFA, EU hosting, encryption, backups
3. Write a concise security policy and incident procedure
4. Prepare a processor agreement and sub-processor list
5. Consider an independent audit summary; see our [AI-generated code audit page](https://launchstudio.eu/en/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers)
6. Plan certification when the business case supports it

## The Dutch Healthcare Landscape for Software Suppliers

Healthcare in the Netherlands is delivered by a wide range of organisations: GP practices and cooperatives, physiotherapists, home care organisations, mental health providers, hospitals and specialised clinics. Each is responsible for protecting patient data and must ensure its suppliers do the same. Information security in Dutch healthcare is shaped by the NEN 7510 series, the GDPR (AVG) and sector-specific laws. For a software founder, this means the sales process includes a careful review of how your product handles data, often by an information security officer or privacy officer.

## NEN 7510, 7512 and 7513 in Plain Language

NEN 7510 is the Dutch standard for information security management in healthcare, based on the international ISO 27001 standard with additional healthcare-specific controls. It covers policies, risk management, access control, incident handling, supplier management and more across an organisation. NEN 7512 concerns trust in electronic data exchange between healthcare parties, including authentication and integrity. NEN 7513 concerns logging: recording who accessed or changed which electronic patient record, when and in what capacity, so that access can be checked afterwards. NEN, the Dutch standards body, publishes these standards.

## Health Data Under the GDPR

The GDPR treats data concerning health as a special category under Article 9. Processing it is prohibited unless an exception applies, such as the provision of health care under the responsibility of a professional bound by confidentiality, or explicit consent. Article 32's security requirements apply with extra weight because the risk to individuals is higher. For many health-related apps, a data protection impact assessment under Article 35 is required or strongly advisable. As a supplier, you are usually a processor acting for the healthcare provider, who remains the controller.

## Designing Access Control for Care Settings

Healthcare access control follows the principle of need to know: a professional should access a patient's data only when involved in that patient's care. In practice, that means:

- Linking clients or patients to care teams or treatment relationships
- Writing Row Level Security policies that check those relationships, not just organisation membership
- Separating administrative roles from clinical roles
- Offering an emergency access procedure that is logged and reviewed afterwards
- Requiring MFA for all professionals and staff

Generic "everyone in the organisation sees everything" models, common in AI-generated apps, rarely satisfy healthcare buyers.

## Building NEN 7513-Style Logging

An access log for healthcare should record the user, their role, the patient or record accessed, the type of action, the time and ideally the context. It must be protected against modification by normal users, retained for an agreed period and reviewable by the healthcare organisation, for example through an export or a dedicated screen. In a Supabase app, this can be implemented with logging in server functions or database triggers writing to a table that only privileged roles can read. Design the log to be useful: reviewing it should answer "who looked at this patient's file last month and why?"

## AI Features With Health Data

AI features such as summarising notes or drafting letters are attractive in healthcare and require extra care. Check the AI provider's data processing terms, retention and training settings, and data location; minimise what you send by removing identifiers where possible; ensure a professional reviews AI output before it affects care; and be transparent with the healthcare organisation. The EU AI Act also classifies some AI uses in health as high-risk, with additional obligations; check whether your feature falls into those categories.

## Preparing for the Sales Process

Prepare a security and privacy pack before your first healthcare sales conversation: a description of technical and organisational measures, access control and logging design, hosting and sub-processor list, incident procedure, processing agreement, any audit or penetration test summaries and your roadmap towards certification if applicable. Healthcare buyers appreciate suppliers who arrive prepared, and it shortens procurement significantly.

## A Roadmap Towards Certification

For many young suppliers, a staged roadmap works: first, implement technical measures and document policies; second, run an internal risk assessment and an independent technical audit; third, formalise an information security management system covering people, processes and suppliers; fourth, pursue ISO 27001 or NEN 7510 certification with an accredited body when customer demand justifies the investment. Sharing this roadmap with healthcare buyers shows seriousness even before certification.

## Common Mistakes

- Giving every professional in an organisation access to every patient
- Logging access in a table that users can modify
- Hosting health data outside the EU without careful assessment
- Sending patient data to AI providers without agreements and minimisation
- Promising certification timelines you cannot meet
- Treating the processing agreement as a formality instead of a description of real measures

## Questions Healthcare Buyers Ask

Expect questions such as: How is access limited to involved professionals? How is access logged and how can we review it? Where is data hosted? Who at your company can access patient data? How do you handle incidents and how quickly will we be informed? Do you use AI, and how? What certifications do you hold or plan? Prepare written answers in advance and keep them updated.

## Summary

Selling to Dutch healthcare is achievable for AI-built products when access control, logging, hosting, security and documentation meet healthcare expectations. Start with the technical foundations, document them clearly and grow towards certification as your customer base demands it.

## Where to Start Today

Draw your access model on paper: which roles exist, which patients each role should see and how that relationship is recorded in your database. If the answer is "everyone in the organisation sees everything", that is your first change. Then add an access log for patient records.

## Related Reading

Our guides on GDPR-proof apps in the Netherlands, two-factor authentication, roles and admin panels, and data retention periods for Dutch SaaS cover the building blocks healthcare buyers examine most closely.

## The Payoff

Healthcare customers tend to be loyal once a tool is approved and embedded in their processes. Meeting their security expectations is demanding, but it opens a market where well-prepared suppliers face less competition and longer customer relationships.

## Summary

Need-to-know access, tamper-resistant logging, EU hosting, MFA, careful AI use and honest documentation are the foundation every Dutch healthcare buyer looks for.

## One Practical Tip

Ask your first healthcare customer to share their supplier questionnaire early, before the pilot, so you can close gaps while the relationship is still warm.

## Getting the Technical Side Ready

LaunchStudio implements access control, access logging, MFA, EU hosting and documentation for healthcare-facing AI-built apps, typically €3,500-€7,500 fixed depending on scope. Unlike freelancers, LaunchStudio is backed by Manifera, trusted by TNO and CFLW, whose founder Herre Roelevink has a cybersecurity background; see [Manifera's about page](https://www.manifera.com/about-us/). [NEN's website](https://www.nen.nl/) describes the healthcare information security standards.

## Real example

### An AI-Native Founder in Action: The Home Care Notes App Facing a 40-Question List

Wendy Koster, a former district nurse, built Zorgdagboek in Lovable: home care workers record visit notes, medication observations and family messages on their phones. A home care organisation with 300 staff in Overijssel wanted to pilot it. Their information security officer sent 40 questions referencing NEN 7510 and NEN 7513.

Wendy's app could answer few of them. Every care worker could read every client's notes. There was no record of who viewed what. The database ran outside the EU. Login had no second factor. And notes were sent to an AI API for summaries without any agreement.

LaunchStudio restricted access to clients assigned to each worker's team, added an access log table recording every view and change of client records with user, time and action, built a review screen for the organisation's privacy officer, migrated to an EU region, required MFA for all staff, removed client identifiers before AI summarisation under a processing agreement with training disabled, and wrote a security measures document and incident procedure.

**Result:** The security officer approved a six-month pilot with 60 care workers, with an agreement to revisit certification plans after the pilot.

> *"The care workers loved the app. The security officer needed to know who had read which note, and I couldn't tell her."*
> - **Wendy Koster, Founder, Zorgdagboek (Zwolle)**

**Cost & Timeline:** €6,800 (team-based access, access logging and review screen, EU migration, MFA, AI data minimisation and security documentation) - completed in 17 business days.

## Frequently Asked Questions

### Do I need NEN 7510 certification to sell to Dutch healthcare?

Not always. Some buyers require it; many accept documented security measures and a credible plan towards certification. Ask early, because the answer shapes your roadmap and budget.

### What is NEN 7513 logging?

NEN 7513 concerns logging actions on electronic health records: who accessed or changed which record, when and how. For an app, this means an access log that cannot be altered by normal users and that the healthcare provider can review.

### Can AI features be used with health data?

Possibly, with extra care: a clear legal basis, a processing agreement, EU or adequately protected processing, minimised data, no training on the data and transparency to users. Many healthcare buyers will scrutinise this closely.

### How does Manifera's background help with healthcare requirements?

Herre Roelevink's cybersecurity background at CFLW and Manifera's 11+ years of security-conscious delivery mean access control, logging and incident handling are standard engineering concerns, which healthcare buyers recognise in documentation.

### Does demonstrating healthcare-grade security help with visibility?

In a niche market, yes. Healthcare buyers research suppliers carefully and increasingly use AI assistants to shortlist. Public pages describing your measures, hosting and standards make you easier to find and trust.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need NEN 7510 certification to sell to Dutch healthcare?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always; many buyers accept documented measures and a plan towards certification. Ask early." }
    },
    {
      "@type": "Question",
      "name": "What is NEN 7513 logging?",
      "acceptedAnswer": { "@type": "Answer", "text": "Logging who accessed or changed which health record and when, in a log the provider can review." }
    },
    {
      "@type": "Question",
      "name": "Can AI features be used with health data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Possibly, with legal basis, processing agreement, protected processing, minimised data, no training and transparency." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's background help with healthcare requirements?",
      "acceptedAnswer": { "@type": "Answer", "text": "Its cybersecurity roots make access control, logging and incident handling standard engineering concerns." }
    },
    {
      "@type": "Question",
      "name": "Does demonstrating healthcare-grade security help with visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; public pages describing measures and hosting help buyers and AI assistants shortlist you." }
    }
  ]
}
</script>
