---
Title: "Production Launch for Healthcare Apps in the Netherlands"
Keywords: healthcare app production launch netherlands, nen 7510 app, zorg app avg, health data app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Production Launch for Healthcare Apps in the Netherlands

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Production Launch for Healthcare Apps in the Netherlands",
  "description": "A guide to launching a healthcare app built with Lovable, Bolt, v0, Cursor or Claude Code in the Netherlands, covering health data as a special category under the GDPR, NEN 7510 and related standards, logging of access, the restrictions on using the BSN, when software may be a medical device, data protection impact assessments, EU hosting and what LaunchStudio does to make such apps production ready.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-24",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/production-launch-for-healthcare-apps-in-the-netherlands" },
  "citation": [
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Gezondheidsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/gezondheid" },
    { "@type": "CreativeWork", "name": "NEN: NEN 7510 Informatiebeveiliging in de zorg", "url": "https://www.nen.nl/zorg-welzijn/ict-in-de-zorg/informatiebeveiliging-in-de-zorg" },
    { "@type": "CreativeWork", "name": "European Commission: Medical Device Regulation", "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations_en" },
    { "@type": "CreativeWork", "name": "EUR-Lex: General Data Protection Regulation (EU) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj" }
  ]
}
</script>

Healthcare is one of the most rewarding areas to build software in, and one of the most demanding. Physiotherapists, GPs, care agencies, mental health practitioners, dentists and home care organisations all need better tools, and founders with sector experience are increasingly building them with AI tools. But health data is treated as a special category of personal data under the GDPR, Dutch healthcare organisations work with sector-specific security standards, and some software qualifies as a medical device. Launching without addressing these points can stop a promising product at the first procurement conversation, or worse, lead to a serious incident involving patients.

This page explains what a production launch for a healthcare app in the Netherlands typically involves, what LaunchStudio does and where you need other specialists. We are not lawyers or regulatory consultants; we work alongside them and make sure the app does what their advice requires.

## Key Takeaways

- **Health data is a special category** under the GDPR, with stricter conditions for processing.
- **NEN 7510** is the Dutch standard for information security in healthcare; customers often expect suppliers to align with it.
- **Logging of who accessed patient data** is a common expectation, linked to NEN 7513.
- **Some apps are medical devices** under the EU MDR, which brings separate obligations.
- **Typical price: €2,500-€7,500 within Launch & Grow,** depending on data, roles and integrations.

## What Makes Healthcare Different

| Aspect | Why it matters |
| --- | --- |
| Special category data | Processing health data is prohibited unless a specific exception applies; additional safeguards are expected |
| Sector standards | Care providers work with NEN 7510 and related standards and expect suppliers to support them |
| Access logging | Care providers must be able to show who accessed which patient records |
| BSN restrictions | Use of the citizen service number in care is regulated; not every app may process it |
| Medical device rules | Software that diagnoses, monitors or advises on treatment may be a medical device |
| Data protection impact assessment | Large-scale processing of health data usually requires one |
| Procurement | Care organisations ask detailed questions about hosting, subprocessors and security |
| Duty of confidentiality | Professionals have strict confidentiality obligations that the software must support |

## Health Data Under the GDPR

The GDPR treats data concerning health as a special category. Processing it is only allowed under specific conditions, such as explicit consent or when necessary for the provision of care by professionals bound by confidentiality, with Dutch law adding detail. Whether your app is a processor acting for a care provider or a controller in its own right affects which rules apply and which agreements you need. The Dutch Data Protection Authority publishes guidance on health data. This is a question for a privacy lawyer; our role is to make sure the app supports the chosen basis, for example through consent flows, access restrictions and data minimisation.

## NEN 7510 and Related Standards

NEN 7510 is the Dutch standard for information security in healthcare, based on the international ISO 27001 and 27002 standards with healthcare-specific additions. Care organisations are expected to work in line with it, and they often ask software suppliers how they support it. Related standards include NEN 7512 on trust in data exchange and NEN 7513 on logging access to electronic patient records.

Certification against NEN 7510 is an organisational process involving management systems, policies, risk assessments and audits; it is not something a single technical project delivers. What we can do is make sure your app has the technical measures the standard expects, such as strong access control, logging, encryption, backups, secure development practices and incident procedures, and document them so your certification or your customers' assessments go smoothly.

## Logging Access to Patient Data

Care providers must be able to answer who viewed or changed a patient's record, and when. NEN 7513 describes requirements for such logging. For an AI-built app, this usually means an append-only audit log of access and changes to patient data, recording the user, time, patient, action and context, with protection against tampering, retention settings and a way for authorised staff to review and export logs. We implement logging designed around these expectations and agree the details with you and, where relevant, your customers.

## The BSN

The citizen service number, or BSN, is widely used in Dutch healthcare, but its use is regulated. Not every app is allowed to process it, and those that are must handle it with care. Many AI-built health apps do not need the BSN at all. If yours does, for example because it exchanges data with care providers' systems, confirm the legal basis with an adviser, minimise where it appears and restrict access. If it does not, make sure it is not collected by accident in free-text fields or imports.

## When an App Is a Medical Device

Under the EU Medical Device Regulation, software intended for medical purposes, such as diagnosis, prevention, monitoring, prediction or treatment of disease, may qualify as a medical device. Apps that only handle scheduling, administration or general wellness usually do not, while apps that calculate dosages, interpret symptoms or monitor patients to inform treatment might. Classification determines the obligations, which can include a quality management system, clinical evaluation and involvement of a notified body. This is a specialist question; consult a regulatory adviser early, because it affects how you build, document and market the product. We can support the technical documentation and development practices such a process requires.

## What LaunchStudio Does for Healthcare Apps

| Area | Typical work |
| --- | --- |
| Hosting | Database, storage and backups in an EU region, with documented subprocessors |
| Access control | Roles for practitioners, staff, patients and administrators, enforced in the database with tests |
| Organisation separation | Practices or care organisations fully separated |
| Audit logging | Logging of access and changes to patient data, with review and export |
| Authentication | Strong login, MFA for professionals, session limits, optional SSO for organisations |
| Encryption and storage | Encrypted transport, private storage, signed links for documents |
| Data minimisation | Removing unnecessary fields, filtering data sent to analytics or AI providers |
| Patient rights | Export and deletion or restriction features, in line with retention obligations |
| AI features | Careful handling of data sent to model providers, with documentation |
| Backups and recovery | Tested restores and documented procedures |
| Monitoring and incidents | Alerts and a short incident procedure supporting breach notification |
| Documentation | Security overview, data flows and input for DPIAs and customer assessments |

## Data Protection Impact Assessment

Processing health data at scale usually requires a data protection impact assessment, which describes the processing, assesses risks to people and records the measures taken. The DPIA is the responsibility of the controller, often your customer or you, and is typically prepared with a privacy specialist. We provide the technical input: data flows, storage locations, access control, logging, encryption, retention and subprocessors.

## AI Features in Healthcare Apps

Many health apps now include AI features, such as summarising notes, drafting letters or answering questions. These deserve extra care. Check what data is sent to the model provider, under which terms, in which region and whether it is retained. Minimise or pseudonymise data where possible. Make clear to professionals that AI output requires their judgement. Be aware that AI features that influence diagnosis or treatment may affect medical device classification. We implement AI features in line with these considerations and document them for your DPIA.

## What We Need From You

- A 15-minute intro call about your app, users, customers and data
- Access to your repository, database, hosting and related services
- Information about any legal, privacy or regulatory advice you have received
- Decisions on roles, retention periods and logging requirements
- Contact with your privacy adviser or customers' information security officers if useful

## Price and Timeline

| Scope | Typical app | Indicative price | Duration |
| --- | --- | --- | --- |
| Small practice tool | One organisation type, limited patient data, no integrations | €2,500-€3,500 | 1-2 weeks |
| Care SaaS for multiple organisations | Roles, organisation separation, audit logging, documents | €3,500-€5,500 | 2-3 weeks |
| Complex health platform | Integrations, AI features, SSO, extensive documentation | €5,500-€7,500 | 3-4 weeks |

Healthcare projects are usually delivered within Launch & Grow, with ongoing care at €49 per month. Simpler tools without patient records may fit within Launch Ready (€800-€3,500). The quote is fixed after an assessment. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Not Included

We do not provide legal advice, act as a data protection officer, certify against NEN 7510 or ISO 27001, determine medical device classification or prepare regulatory submissions. We work with your advisers and provide the technical measures and documentation their work requires. Integrations with specific care information systems are scoped separately because they depend on the system and its access requirements.

## Patient-Facing Versus Professional-Facing Apps

Health apps used only by professionals, such as planning or documentation tools for practices, differ from apps used directly by patients. Professional tools typically process data on behalf of a care provider, with the provider as controller. Patient-facing apps, such as symptom diaries or exercise apps, may collect data directly from individuals, sometimes making the founder a controller with direct obligations towards patients, including clear consent, information and rights handling. Many products combine both. Knowing which role applies to which data shapes the consent flows, privacy texts and agreements, so clarify it with your privacy adviser before launch.

## Selling to Care Organisations

Care organisations buy carefully. Expect questions about hosting, subprocessors, NEN 7510 alignment, logging, access control, incident handling and processing agreements. A clear security overview, a subprocessor list and documentation of logging and access control shorten that process considerably. Some organisations will ask for a penetration test or certification; preparing the app properly first makes those steps easier.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building software for organisations with strict data requirements, such as Vodafone and TNO. Manifera's CEO, Herre Roelevink, co-founded the cybersecurity company CyberDevOps, now CFLW Cyber Strategies. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. Our engineers work on staging with test data wherever possible, any access to production patient data is minimised and documented, and hosting remains in the EU regions you choose.

## Real example

### An AI-Native Founder in Action: The Physio App That Needed an Audit Trail

Charlotte Dekkers is a physiotherapist in Apeldoorn who built Herstelpad with Lovable and Supabase, an app where physiotherapists assign exercise programmes, patients log pain scores and progress, and practices see outcomes. A group of eight practices wanted to roll it out, but their information security officer sent a list of requirements: EU hosting, separation between practices, logging of who viewed patient records, MFA for therapists, a processing agreement and documentation for their DPIA.

The assessment found the database outside the EU, policies allowing any therapist to see all patients across practices, pain notes sent in full to an AI provider for weekly summaries, no logging and no MFA. A field for the BSN had been added during prompting, although the app did not need it.

LaunchStudio quoted €4,900 within Launch & Grow. The project moved to an EU region, practices were separated with roles for therapists, practice managers and patients enforced through Row Level Security with tests, and an append-only audit log recorded access and changes to patient records, with export for the practices. MFA was enforced for therapists, the BSN field was removed and existing values deleted, and AI summaries were changed to send only pseudonymised scores and dates. Private storage, backups with a restore test, monitoring and documentation of data flows for the DPIA completed the work. Charlotte's privacy lawyer prepared the processing agreement.

**Result:** The information security officer approved Herstelpad after reviewing the documentation, and the eight practices onboarded around 1,100 patients. Two other practice groups later used the same documentation in their own assessments.

> *"I know how to treat patients. I did not know how to prove to a security officer that their data was safe. Now I have an audit trail and the paperwork to show it."*
> - **Charlotte Dekkers, Founder, Herstelpad (Apeldoorn)**

**Cost & Timeline:** €4,900 (Launch & Grow package: EU migration, practice separation, audit logging, MFA, BSN removal, AI data minimisation, storage, backups and documentation, plus €49 per month) - completed in 13 business days.

## Frequently Asked Questions

### What does it cost to launch a healthcare app in the Netherlands?

Technical production work typically costs €2,500 to €7,500 within Launch & Grow, depending on roles, organisations, audit logging, integrations and AI features. Legal, privacy and regulatory advice are separate. You receive a fixed quote after an assessment.

### Does my health app need NEN 7510 certification?

Not necessarily the app itself, but care organisations are expected to work in line with NEN 7510 and often ask suppliers how they support it. Some customers require certification of the supplier. We implement and document the technical measures; certification is an organisational process with an auditor.

### Is my app a medical device?

It depends on its intended purpose. Scheduling and administrative tools usually are not; software that supports diagnosis, monitoring or treatment decisions may be. Consult a regulatory adviser early, because classification affects how you build and document the product.

### How does Manifera's experience help with healthcare apps?

Manifera has built software for organisations with strict data requirements for 11+ years across 160+ projects with 120+ engineers, and its CEO co-founded a cybersecurity company. LaunchStudio applies that experience to access control, logging and documentation for health apps.

### Does compliance help SEO and AI visibility for health apps?

Yes, indirectly. Clear public pages about security, hosting and data handling answer the questions care organisations search for. Accurate information helps search engines and AI answer engines describe your app correctly when professionals ask about secure tools in their field.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does it cost to launch a healthcare app in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically €2,500-€7,500 within Launch & Grow for technical work; legal and regulatory advice are separate." }
    },
    {
      "@type": "Question",
      "name": "Does my health app need NEN 7510 certification?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily; customers often expect alignment, and certification is an organisational process." }
    },
    {
      "@type": "Question",
      "name": "Is my app a medical device?",
      "acceptedAnswer": { "@type": "Answer", "text": "It depends on intended purpose; consult a regulatory adviser early." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with healthcare apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years with strict data requirements, and its CEO co-founded a cybersecurity company." }
    },
    {
      "@type": "Question",
      "name": "Does compliance help SEO and AI visibility for health apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes indirectly, through clear public information on security and data handling." }
    }
  ]
}
</script>
