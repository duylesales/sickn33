---
Title: "Your First Dutch B2B Customer: Contracts, SLA and DPA Checklist"
Keywords: first b2b customer saas netherlands, saas sla small startup, algemene voorwaarden saas, verwerkersovereenkomst b2b, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Your First Dutch B2B Customer: Contracts, SLA and DPA Checklist

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your First Dutch B2B Customer: Contracts, SLA and DPA Checklist",
  "description": "Before signing your first Dutch business customer, you need a few documents and the technical reality to back them up: terms and conditions, a processing agreement, a realistic service level, security answers and an exit clause. A checklist for AI-built SaaS founders.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-25",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/your-first-dutch-b2b-customer-contracts-sla-and-dpa-checklist" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" },
    { "@type": "CreativeWork", "name": "KVK", "url": "https://www.kvk.nl/en/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

Consumer apps start with a sign-up button. Business customers start with a conversation, then questions: "Can we see your terms? Do you have a verwerkersovereenkomst? What uptime do you guarantee? What happens to our data if we stop?" Your first Dutch B2B customer is a milestone, and the documents you prepare for them become the foundation for every customer after. This checklist combines the contractual and technical sides. It is not legal advice; have a lawyer review your final documents.

## Key Takeaways

- **Your first Dutch B2B customer will ask for a document pack:** general terms (algemene voorwaarden), a processing agreement (verwerkersovereenkomst), a service description or SLA, a security summary and an order form.
- **Article 28 of the GDPR requires a processing agreement** when you process personal data on a customer's behalf.
- **Promise only what you can measure:** a realistic SLA backed by monitoring builds more trust than an ambitious template.
- **Every contractual claim needs a technical measure behind it:** tenant isolation, EU hosting, tested backups, monitoring, MFA and deletion.
- **Have a lawyer review your documents;** this guide describes the technical and practical side, not legal advice.

## The Documents

| Document | Dutch term | Purpose |
| --- | --- | --- |
| Terms and conditions | Algemene voorwaarden | Your general contractual rules, liability, payment terms |
| Processing agreement | Verwerkersovereenkomst | Required when you process personal data on their behalf |
| Service description and SLA | Dienstbeschrijving, SLA | What you deliver, availability, support times |
| Security summary | Beveiligingsmaatregelen | How you protect their data |
| Order form or quote | Offerte, orderformulier | Price, term, users, start date |

## Terms and Conditions: Points B2B Customers Check

- Limitation of liability, usually capped to fees paid over a period
- Payment terms and what happens on non-payment
- Contract term, renewal and notice periods
- Intellectual property: their data stays theirs; your software stays yours
- Changes to the service and to prices
- Applicable law and court (Dutch law, a Dutch court)
- How your terms relate to theirs; larger customers may send purchase conditions

## The Processing Agreement

Your customer is the controller of their data in your product; you are the processor. The agreement covers purpose, security measures, sub-processors, breach notification, assistance with rights requests and deletion at the end. Our [GDPR checklist for SaaS founders](https://launchstudio.eu/en/blog/gdpr-checklist-for-saas-founders-in-the-netherlands) lists the supporting documents.

## A Realistic SLA

Small SaaS companies often overpromise. A credible first SLA:

- **Availability target** you can actually measure and meet, excluding announced maintenance
- **Support hours** that match your capacity, for example business days, with response times by severity
- **Incident communication**: how and when you inform customers
- **Remedy**: modest service credits rather than open-ended liability

Promise only what your monitoring can prove. See our guide on [knowing when your app goes down](https://launchstudio.eu/en/blog/how-do-i-know-when-my-ai-built-app-goes-down).

## Technical Reality Behind the Words

Every promise in the documents needs a matching measure:

| Promise | Technical measure |
| --- | --- |
| "Data separated from other customers" | Tenant isolation with Row Level Security, tested |
| "Hosted in the EU" | Database, storage, backups in EU regions |
| "Daily backups" | Backups configured and a restore tested |
| "Breach notification within X hours" | Monitoring, logging and an incident procedure |
| "Data deleted at contract end" | Organisation-level deletion function |
| "Two-factor authentication available" | MFA implemented |
| "99.x% availability" | Uptime monitoring and history |

## Exit and Data Return

Business customers want to know they can leave: an export of their data in a usable format and confirmation of deletion. Build it before they ask.

## Why B2B Buyers Ask So Much

Business customers trust you with their data, their customers' data and their operations. They answer to their own customers, auditors and regulators, and increasingly face supply chain security requirements that cascade to suppliers like you. Their questions are not bureaucracy for its own sake; they are how the customer meets its own obligations. Understanding that makes the process feel less adversarial and helps you answer efficiently.

## General Terms: Practical Points

General terms set the default rules of your relationship. Points that Dutch B2B customers often review include:

| Topic | What to decide |
| --- | --- |
| Liability | A cap, often linked to fees paid over a period, with exclusions for indirect damage |
| Payment | Terms, late payment interest, suspension rights for non-payment |
| Term and termination | Duration, renewal, notice periods, termination for breach |
| Intellectual property | Your software stays yours; their data stays theirs |
| Service changes | How you may change features and prices, with notice |
| Data at the end | Export and deletion, linked to the processing agreement |
| Applicable law | Dutch law and a competent Dutch court |

Larger customers may propose their own purchase conditions. Read them carefully, especially liability, audit rights and termination clauses, and negotiate what you cannot accept.

## Writing a Realistic SLA

A service level agreement defines what customers can expect. For a small SaaS, keep it measurable and achievable:

- **Availability:** a monthly target such as 99.5%, measured by your uptime monitor, excluding announced maintenance
- **Support:** channels, hours and response times by severity, matching your actual capacity
- **Incident communication:** how and when customers are informed, for example via email or a status page
- **Service credits:** a modest remedy if targets are missed, rather than open-ended damages

Google's SRE guidance encourages setting reliability targets based on what users need and what you can sustain, rather than chasing perfection. A credible SLA built on real monitoring data is far more convincing than "99.99%" copied from a template.

## The Processing Agreement and Its Annexes

Article 28 of the GDPR lists what a processing agreement must contain, including the subject and duration of processing, types of data, your obligations on confidentiality and security, sub-processor rules, assistance with data subject requests and deletion or return at the end. Most agreements include annexes describing data categories, security measures and sub-processors. Keep these annexes accurate and versioned; they are what customers' privacy officers actually check.

## Security Questionnaires

Many Dutch organisations send a security questionnaire alongside the contract. Questions typically cover hosting and location, access control and tenant isolation, encryption, logging and monitoring, incident response, backups and recovery, secure development practices and staff access. Prepare a standard answer set once and keep it updated. Attach an independent audit summary if you have one; it often answers dozens of questions at once.

## Evidence Beats Promises

When a customer asks "do you back up our data?", the strongest answer includes evidence: backup frequency, retention, region and the date of your last successful restore test. When asked about access control, describe how isolation is enforced in the database and that it is tested automatically. Evidence-based answers shorten procurement and build trust that lasts beyond the first contract.

## Pricing and Order Forms

Your order form or quote should state the plan, price, billing interval, number of users or usage limits, start date, term and which documents apply. Clear order forms prevent disputes about what was agreed, especially when pricing includes seats or usage. Keep VAT handling explicit for business customers, including reverse charge for EU customers outside the Netherlands.

## A Two-Week Readiness Plan

| Days | Focus |
| --- | --- |
| 1-3 | Tenant isolation verified, MFA available, admin access reviewed |
| 4-6 | EU hosting confirmed, backups tested, monitoring with history |
| 7-8 | Organisation export and deletion functions |
| 9-10 | Security summary and sub-processor list written |
| 11-14 | Lawyer finalises terms, processing agreement and SLA based on the facts |

Running technical and legal work in parallel gets you from "we have nothing" to "here is our pack" in about two weeks.

## Common Mistakes

- Copying an enterprise SLA template with promises you cannot keep
- Signing a customer's processing agreement without reading audit and notification clauses
- Claiming EU hosting while a sub-processor processes data elsewhere
- No organisation-level deletion when contracts end
- Treating security questionnaires as marketing exercises

## Questions to Ask Yourself

Can I prove every claim in my documents? Who responds to an incident at night or on holiday? What happens to a customer's data the day after they leave? Which sub-processors handle their data, and where? If any answer is uncertain, fix the underlying measure before signing.

## Summary

Prepare terms, a processing agreement, a realistic SLA, a security summary and an order form, and make sure each claim is backed by a working technical measure. Your first B2B customer then becomes a template for every customer after.

## When Customers Request Changes to Your Documents

Larger customers often ask for changes: higher liability caps, shorter breach notification times, audit rights, specific hosting locations or penalties for missed SLAs. Evaluate each request against your actual capabilities and insurance, explain your position honestly and offer alternatives where possible, such as an independent audit report instead of on-site audits. Agreeing to terms you cannot meet creates more risk than losing a single deal.

## Related Reading

Our GDPR checklist for SaaS founders, monitoring guide and data retention guide cover the technical measures behind most contractual promises.

## The Payoff

A complete, honest document pack turns procurement from a hurdle into a demonstration of professionalism. Every later customer benefits from the same pack, so the effort pays back many times over.

## Where to Start Today

Write down every promise you would make to a business customer about hosting, security, availability and data handling. Next to each, write the measure that makes it true. Gaps in the second column are your to-do list.

## The Bottom Line

Business customers buy trust. Documents describe it; working measures prove it. Prepare both, and your first contract becomes the template for growth.

## One Final Tip

Keep every signed customer document in one organised folder with version numbers; you will need them at renewal, audits and due diligence.

## Getting the Technical Side in Place

LaunchStudio implements the measures behind B2B promises, such as tenant isolation, EU hosting, backups, monitoring, MFA and export and deletion, typically €2,500-€6,500 fixed, so your lawyer can write documents that match reality. LaunchStudio is powered by Manifera, which has signed and delivered on enterprise contracts for clients such as Vodafone and TNO for 11+ years; see [Manifera's portfolio](https://www.manifera.com/portfolio/). The [KVK](https://www.kvk.nl/en/) publishes guidance on general terms and conditions for Dutch businesses.

## Real example

### An AI-Native Founder in Action: The Facility SaaS That Promised 99.99%

Bram Oosting built Schoonplan in Bolt: a cleaning schedule and quality inspection tool for office buildings. His first B2B prospect, a facility management company with 40 buildings in Rotterdam, asked for terms, a processing agreement and an SLA. Bram found an SLA template online that promised 99.99% availability, 24/7 support and four-hour fixes.

Before signing, the prospect's IT contact asked how Bram measured availability and who answered calls at night. Bram had no monitoring, was a one-person company and had never restored a backup.

LaunchStudio set up monitoring with history, EU hosting and tested backups, tenant isolation, MFA and organisation export and deletion. With real data on what his setup delivered, Bram's lawyer drafted an SLA with a 99.5% monthly target, support on business days with defined response times and modest service credits, plus a processing agreement and security summary matching the implemented measures.

**Result:** The facility company signed a two-year contract. Its IT contact noted that the realistic SLA was more convincing than the original template.

> *"I almost signed a promise I couldn't keep. A smaller promise backed by real measures won the deal."*
> - **Bram Oosting, Founder, Schoonplan (Rotterdam)**

**Cost & Timeline:** €4,100 (monitoring, EU hosting, backups and restore test, tenant isolation, MFA, export and deletion, security summary input) - completed in 11 business days.

## Frequently Asked Questions

### Do I need algemene voorwaarden for B2B SaaS in the Netherlands?

It is strongly advisable. General terms set out liability, payment, term and other conditions. Make sure they are provided to customers before or at contract signing, and have a lawyer draft or review them.

### What SLA should a small SaaS offer?

A realistic one: an availability target you can measure and meet, support hours matching your capacity, clear incident communication and modest service credits. Overpromising creates legal and reputational risk.

### Is a verwerkersovereenkomst mandatory?

Yes, when you process personal data on behalf of a business customer, the GDPR requires a processing agreement. Prepare a standard version and expect larger customers to propose their own.

### How does Manifera's enterprise experience help with B2B readiness?

Manifera has delivered under enterprise contracts for 11+ years and knows which promises customers check. LaunchStudio applies that to make sure every contractual claim has a technical measure behind it.

### Do public trust pages help win B2B customers?

Yes. A public page summarising security measures, hosting location and SLA highlights answers early questions and gives AI assistants facts when buyers ask about trustworthy suppliers in your category.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need algemene voorwaarden for B2B SaaS in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "Strongly advisable, provided before or at signing and reviewed by a lawyer." }
    },
    {
      "@type": "Question",
      "name": "What SLA should a small SaaS offer?",
      "acceptedAnswer": { "@type": "Answer", "text": "A realistic, measurable availability target, support matching capacity, incident communication and modest credits." }
    },
    {
      "@type": "Question",
      "name": "Is a verwerkersovereenkomst mandatory?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes when processing personal data on a business customer's behalf." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's enterprise experience help with B2B readiness?",
      "acceptedAnswer": { "@type": "Answer", "text": "It ensures every contractual claim has a technical measure behind it." }
    },
    {
      "@type": "Question",
      "name": "Do public trust pages help win B2B customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; they answer early questions and give AI assistants facts." }
    }
  ]
}
</script>
