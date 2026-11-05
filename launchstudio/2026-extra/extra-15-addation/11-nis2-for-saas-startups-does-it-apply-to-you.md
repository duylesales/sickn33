---
Title: "NIS2 for SaaS Startups: Does It Apply to You?"
Keywords: nis2 saas startup, nis2 applicability, cyberbeveiligingswet saas, nis2 supply chain requirements, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# NIS2 for SaaS Startups: Does It Apply to You?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "NIS2 for SaaS Startups: Does It Apply to You?",
  "description": "NIS2 expands EU cybersecurity obligations to many more organisations, but most small SaaS startups are affected through their customers rather than directly. This guide explains who is in scope, the size rules, the Dutch Cyberbeveiligingswet, what customers will ask suppliers, and the practical security measures an AI-built SaaS should put in place.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-28",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/nis2-for-saas-startups-does-it-apply-to-you" },
  "citation": [
    { "@type": "CreativeWork", "name": "Directive (EU) 2022/2555 (NIS2)", "url": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj" },
    { "@type": "CreativeWork", "name": "European Commission: NIS2 Directive", "url": "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive" },
    { "@type": "CreativeWork", "name": "Commission Recommendation 2003/361/EC on SME definition", "url": "https://eur-lex.europa.eu/eli/reco/2003/361/oj" },
    { "@type": "CreativeWork", "name": "NCSC Netherlands", "url": "https://www.ncsc.nl/" }
  ]
}
</script>

Since the NIS2 Directive entered into force, founders have received a steady stream of emails, webinars and sales pitches suggesting that every company with a server is now subject to strict new cybersecurity law. For a two-person SaaS startup built with Lovable or Cursor, this raises an anxious question: does NIS2 apply to me, and what do I need to do?

The honest answer for most early-stage SaaS companies is: probably not directly, but almost certainly indirectly. NIS2 places obligations on medium and large organisations in specific sectors, and one of those obligations is to manage the security of their suppliers. If your customers are in scope, their security questionnaires and contracts will bring NIS2 expectations to your door, whether or not the law names you.

This guide explains how to work out where you stand, and what is worth doing either way. It is a practical overview, not legal advice; for a definitive assessment of your situation, consult a lawyer or your national authority.

## Key Takeaways

- **NIS2 applies to medium and large entities in listed sectors,** plus a few categories regardless of size. Most small SaaS startups fall below the size threshold.
- **Some digital services are in scope as a sector,** including cloud computing, data centres, managed service providers and managed security service providers, but size rules still apply to most of them.
- **The indirect effect is the real one for startups.** In-scope customers must manage supply chain security, so they will ask suppliers for evidence of security practices.
- **In the Netherlands, NIS2 is implemented through the Cyberbeveiligingswet,** whose timing has shifted; check the current status with official sources.
- **The measures NIS2 describes are good practice anyway:** risk management, incident handling, MFA, secure development, backups and supplier management.

## What NIS2 Is

NIS2, formally Directive (EU) 2022/2555, replaces the original 2016 NIS Directive. It aims to raise the level of cybersecurity across the EU by expanding the number of sectors covered, setting minimum security measures, introducing strict incident reporting deadlines and making senior management accountable. Member states were required to transpose it into national law by 17 October 2024; several, including the Netherlands, took longer.

The directive distinguishes two categories of organisation:

- **Essential entities,** generally large organisations in the sectors listed in Annex I, such as energy, transport, banking, health, drinking water, digital infrastructure and ICT service management.
- **Important entities,** including medium-sized organisations in Annex I sectors and medium and large organisations in Annex II sectors, such as postal services, waste management, chemicals, food, manufacturing and digital providers.

Both categories must implement security measures and report significant incidents. The difference is mostly in supervision: essential entities face proactive supervision, important entities mainly reactive supervision after an incident or complaint.

## The Size Rule: Why Most Startups Are Out of Direct Scope

NIS2 generally applies to organisations that are at least medium-sized under the EU's SME definition. In simplified terms, that means an organisation with 50 or more employees, or an annual turnover and balance sheet total both above €10 million. Below that, a company is small or micro and is generally outside direct scope.

There are exceptions where size does not matter. These include providers of public electronic communications networks or services, trust service providers, top-level domain registries and DNS service providers, and entities designated by a member state because they are the sole provider of a critical service or because disruption would have significant impact. A small SaaS company is rarely in these categories, but if you run DNS services or issue electronic signatures, check carefully.

| Your situation | Direct NIS2 scope? |
| --- | --- |
| Fewer than 50 staff and turnover under €10 million, ordinary SaaS | Generally no |
| Medium or large, providing cloud computing services to businesses | Likely yes, as a digital infrastructure provider |
| Medium or large managed service provider operating customers' IT | Likely yes, under ICT service management |
| Medium or large online marketplace or search engine | Likely yes, as a digital provider |
| Any size, DNS service provider or trust service provider | Likely yes |
| Small SaaS selling to hospitals, energy firms or municipalities | Generally no directly, but strongly affected through customers |

Note the word "generally". Group structures, partner companies and national designations can change the outcome. If you are part of a larger group, the group's size may count.

## The Indirect Effect: Supply Chain Security

This is where NIS2 reaches almost every B2B SaaS company. Article 21 requires in-scope entities to take risk management measures that include **supply chain security**, covering the security of the relationships with their direct suppliers and service providers. In practice, that means your in-scope customers must assess the security of the software they buy, include security requirements in contracts and monitor suppliers over time.

If you sell to a hospital, a water company, a logistics firm, a bank or a municipality, expect:

- **Security questionnaires** asking about access control, MFA, encryption, logging, vulnerability management, backups and incident response
- **Contract clauses** requiring you to notify them of security incidents quickly, often within 24 hours
- **Requests for evidence,** such as policies, penetration test summaries or certifications
- **Questions about your own suppliers,** such as your hosting, database and AI providers

A startup that can answer these clearly wins deals that competitors lose. A startup that cannot answer them often never learns why the deal went quiet.

## What NIS2 Asks of In-Scope Organisations

Even if you are not directly in scope, the list of measures in Article 21 is a useful map of what your customers will look for. The directive requires an all-hazards approach that includes at least:

1. Policies on risk analysis and information system security
2. Incident handling
3. Business continuity, including backup management and disaster recovery
4. Supply chain security
5. Security in acquisition, development and maintenance of systems, including vulnerability handling
6. Policies to assess the effectiveness of security measures
7. Basic cyber hygiene and cybersecurity training
8. Policies on cryptography and encryption
9. Human resources security, access control and asset management
10. Multi-factor authentication and secured communications where appropriate

NIS2 also sets reporting deadlines for significant incidents: an early warning within 24 hours of becoming aware, an incident notification within 72 hours and a final report within one month. Your customers will want you to support those timelines, which is why incident notification clauses appear in supplier contracts.

Penalties for in-scope entities can reach €10 million or 2% of worldwide turnover for essential entities, and €7 million or 1.4% for important entities, whichever is higher. Management bodies can also be held responsible.

## The Dutch Situation: The Cyberbeveiligingswet

In the Netherlands, NIS2 is implemented through the Cyberbeveiligingswet (Cbw), which replaces the earlier Wet beveiliging netwerk- en informatiesystemen. The Dutch legislative process took longer than the EU deadline, and the expected entry into force has moved more than once. The National Cyber Security Centre (NCSC) and the government's information pages are the authoritative sources on timing, registration duties and supervisors per sector.

For a startup, the timing matters less than the direction. Dutch customers in health, energy, transport, water, digital infrastructure and government are preparing now, and their procurement teams are already asking suppliers NIS2-style questions.

## A Practical Security Baseline for a Small SaaS

If you are not directly in scope, you do not need a compliance programme. You do need a baseline that lets you answer customer questions truthfully. For an AI-built SaaS, that baseline looks like this:

| Area | Minimum for a small SaaS |
| --- | --- |
| Access control | Row Level Security or equivalent on all customer data, tested with multiple accounts |
| Authentication | MFA for all staff accounts and admin users, optional MFA for customers |
| Secrets | No keys in code or git history, secrets in the host's secret manager, rotation procedure |
| Encryption | HTTPS everywhere, encryption at rest provided by your database host |
| Logging | Authentication events and admin actions logged and retained |
| Backups | Automated backups with a tested restore |
| Vulnerability handling | Dependency alerts, a process for patching critical issues quickly |
| Incident response | A one-page plan: who decides, who informs customers, how fast |
| Suppliers | A list of your processors and sub-processors, with locations and agreements |
| Development | Code review, staging environment, no direct production changes |

Most of this is also what GDPR's security requirement, Article 32, expects for personal data. NIS2 and GDPR point in the same direction.

## Documents That Make Customer Conversations Easier

Prepare these once and reuse them:

- **A security overview** of two to four pages: architecture, hosting location, access control, encryption, backups, monitoring and incident response
- **A sub-processor list** with what each one does and where data is processed
- **An incident response summary** stating notification timelines you can commit to
- **A filled-in standard questionnaire,** so new requests can be answered quickly
- **A processing agreement template** for customers who need one under GDPR

When an in-scope customer asks about NIS2, sending these within a day signals maturity more effectively than any certificate you do not yet have.

## Common Misunderstandings

**"NIS2 means we need ISO 27001."** No. NIS2 does not require a specific certification. ISO 27001 is one way to demonstrate good practice, and some customers ask for it, but it is a business decision. Our guide to [ISO 27001 for early-stage SaaS](https://launchstudio.eu/en/blog/iso-27001-for-early-stage-saas-when-to-start) discusses timing.

**"We use AWS or Supabase, so security is their problem."** Your providers secure their infrastructure. Your access rules, your code, your admin accounts and your incident response remain yours.

**"We are too small to be a target."** Small suppliers are attractive precisely because they are a path into larger customers. That is why supply chain security is in NIS2.

## How LaunchStudio Helps

LaunchStudio helps founders put the technical baseline in place: access control, MFA, secrets handling, logging, backups, monitoring and a clean deployment process. We also help prepare the security overview and sub-processor list your customers will ask for. The **Launch Ready** package (€800-€3,500) covers the security work and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for a first range.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink co-founded the cybersecurity company CyberDevOps, now CFLW Cyber Strategies, which developed a Dark Web Monitor in cooperation with TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Maintenance Planner That Met a Water Company's Questionnaire

Bas Hendriks, a former maintenance engineer, built Onderhoudsplan in Cursor: a planning tool that helps technical teams schedule inspections and maintenance for pumps, valves and installations. His company had three people and well under €1 million in revenue, so NIS2 did not apply to it directly. His first large prospect, a regional water company in Gelderland, was firmly in scope.

The water company's procurement team sent a 74-question supplier security questionnaire referencing NIS2 and asked for an incident notification commitment of 24 hours. Bas could answer about a third of the questions. Staff accounts had no MFA, the admin panel was protected only by an email check in the frontend, there were no audit logs, backups had never been restored and nobody had written down which services processed customer data.

LaunchStudio enabled MFA for all staff and admin users, moved admin authorisation into the database with Row Level Security and role checks, added audit logs for logins and administrative actions, and set up point-in-time recovery with a documented restore test. Secrets were moved out of the repository and rotated, dependency alerts and a staging environment were added, and engineers helped Bas write a security overview, a sub-processor list and a one-page incident response plan with a realistic 24-hour notification commitment.

**Result:** Bas returned the completed questionnaire in nine business days with supporting documents. The water company accepted it with two follow-up questions, and Onderhoudsplan was rolled out to its maintenance teams the next quarter. The same documents shortened two later procurement processes to under a week.

> *"I wasn't covered by NIS2, but my customer was. Being able to answer their questions properly was the difference between a pilot and a contract."*
> - **Bas Hendriks, Founder, Onderhoudsplan (Arnhem)**

**Cost & Timeline:** €3,400 (Launch Ready package: MFA, admin authorisation, audit logging, backups, secrets cleanup and security documentation support) - completed in 9 business days.

## Frequently Asked Questions

### Does NIS2 apply to a small SaaS startup?

Generally not directly. NIS2 mainly covers medium and large organisations in listed sectors, with a few size-independent exceptions such as DNS and trust service providers. However, if your customers are in scope, they must manage supplier security, so NIS2 expectations will reach you through questionnaires and contracts.

### What will NIS2-regulated customers ask my SaaS company?

Expect questions about access control, MFA, encryption, logging, vulnerability management, backups, incident response and your own suppliers, plus contract clauses requiring prompt incident notification. Preparing a security overview and sub-processor list in advance makes these conversations much faster.

### Do I need ISO 27001 because of NIS2?

No. NIS2 does not require a specific certification. Some customers ask for ISO 27001 or similar evidence, which makes it a commercial decision. A clear security overview and good practices often satisfy customers before certification is worthwhile.

### How does Manifera's background help with NIS2 readiness?

Manifera's CEO co-founded a cybersecurity firm, and the company has built enterprise systems for 11+ years under security requirements from large clients. LaunchStudio applies that experience to give small SaaS companies the practical baseline and documentation their regulated customers expect.

### Can security documentation help my visibility with buyers and AI search?

Yes. Publishing a clear security page with your hosting location, practices and sub-processors helps procurement teams find answers quickly, and well-structured security content is the kind of information search engines and AI answer engines surface when buyers compare suppliers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does NIS2 apply to a small SaaS startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally not directly, since NIS2 mainly covers medium and large organisations in listed sectors. In-scope customers must manage supplier security, so expectations reach startups through questionnaires and contracts." }
    },
    {
      "@type": "Question",
      "name": "What will NIS2-regulated customers ask my SaaS company?",
      "acceptedAnswer": { "@type": "Answer", "text": "Questions on access control, MFA, encryption, logging, vulnerability management, backups, incident response and sub-processors, plus incident notification clauses." }
    },
    {
      "@type": "Question",
      "name": "Do I need ISO 27001 because of NIS2?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. NIS2 does not require a specific certification; ISO 27001 is a commercial decision when customers ask for it." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's background help with NIS2 readiness?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's CEO co-founded a cybersecurity firm and the company has built enterprise systems for 11+ years, so LaunchStudio delivers the practical baseline and documentation regulated customers expect." }
    },
    {
      "@type": "Question",
      "name": "Can security documentation help my visibility with buyers and AI search?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A clear public security page helps procurement teams and is the kind of structured information search and AI engines surface when buyers compare suppliers." }
    }
  ]
}
</script>
