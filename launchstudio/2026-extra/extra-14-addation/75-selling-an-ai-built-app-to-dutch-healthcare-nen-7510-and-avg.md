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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/selling-an-ai-built-app-to-dutch-healthcare-nen-7510-and-avg" }
}
</script>

A physiotherapy group, a GP cooperative or a home care organisation likes your app. Then their information security officer sends questions: "Are you NEN 7510 certified? How do you log access to client data? Where is health data stored?" Health data is a special category under the GDPR (AVG), and Dutch healthcare has its own information security standards. An AI-built app can meet these expectations, but not by default.

This article is general guidance, not legal or certification advice.

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
