---
Title: "NEN 7510 and Healthcare Apps in the Netherlands"
Keywords: nen 7510 app, healthcare app netherlands, zorgapp beveiliging, nen 7510 saas startup, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# NEN 7510 and Healthcare Apps in the Netherlands

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "NEN 7510 and Healthcare Apps in the Netherlands",
  "description": "Dutch healthcare organisations expect suppliers handling health data to meet NEN 7510, alongside GDPR rules for special category data and related standards such as NEN 7512 and NEN 7513. This guide explains what NEN 7510 is, when it applies to an AI-built healthcare app, what it means technically and how founders can prepare for certification or supplier assessments.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-08",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/nen-7510-and-healthcare-apps-in-the-netherlands" },
  "citation": [
    { "@type": "CreativeWork", "name": "NEN: NEN 7510 Information security in healthcare", "url": "https://www.nen.nl/en/nen-7510-1-2017-a1-2020-nl-267179" },
    { "@type": "CreativeWork", "name": "GDPR Article 9: Processing of special categories of personal data", "url": "https://gdpr-info.eu/art-9-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Health data", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/health" },
    { "@type": "CreativeWork", "name": "Besluit elektronische gegevensverwerking door zorgaanbieders", "url": "https://wetten.overheid.nl/BWBR0040089/" }
  ]
}
</script>

Healthcare is one of the most rewarding markets for AI-built software. Practices, clinics, home care organisations and mental health providers are under constant pressure, and tools that save time on scheduling, intake, reporting or communication are genuinely welcome. A founder with domain knowledge, perhaps a former nurse, physiotherapist or practice manager, can build a useful prototype in weeks with Lovable, Bolt or Cursor.

Then the first serious customer asks a question that stops many founders: "Are you NEN 7510 certified?" Or, more often: "Can you show us how you comply with NEN 7510?" Health data is among the most sensitive data there is, and Dutch healthcare has its own information security standard that builds on international norms. Understanding what it asks, and when it applies to you, is essential before selling to healthcare providers.

This guide explains NEN 7510 for founders. It is general information, not legal advice; for specific obligations, consult a privacy lawyer or healthcare compliance specialist.

## Key Takeaways

- **NEN 7510 is the Dutch standard for information security in healthcare,** based on ISO 27001 and ISO 27002 with healthcare-specific additions.
- **Healthcare providers are legally required to meet NEN 7510** for electronic processing of health data, and they expect suppliers who process that data to support it.
- **Health data is special category data under GDPR,** which brings stricter processing conditions, a data protection impact assessment in many cases and strong security expectations.
- **Related standards matter too:** NEN 7512 for trust in data exchange and NEN 7513 for logging access to patient records.
- **Technical foundations come first:** strong authentication, strict access control, complete access logging, encryption, EU hosting and tested recovery.

## What NEN 7510 Is

NEN 7510 is published by NEN, the Dutch standardisation institute, and is titled "Medical informatics - Information security in healthcare". Its current version consists of two parts: NEN 7510-1, which describes requirements for an information security management system, and NEN 7510-2, which describes controls. It follows the structure of ISO/IEC 27001 and 27002 and adds requirements specific to healthcare, for example around patient data, continuity of care and the roles involved in treatment.

Organisations can be certified against NEN 7510 by accredited certification bodies, in a process similar to ISO 27001 certification. Many healthcare software suppliers hold NEN 7510 certification, often combined with ISO 27001.

## Why Healthcare Customers Ask About It

Dutch regulation requires healthcare providers that process health data electronically to meet specific security standards. The Besluit elektronische gegevensverwerking door zorgaanbieders refers to NEN 7510, NEN 7512 and NEN 7513 as the applicable standards for healthcare providers. A clinic or care organisation therefore needs to demonstrate that its information security, including the systems supplied by others, meets these norms.

The practical result for a SaaS supplier: if your app processes health data on behalf of healthcare providers, they will want evidence that your service meets NEN 7510 requirements. That may be a certificate, or it may be a supplier assessment where you show how you meet the relevant controls. Larger organisations and hospitals increasingly require certification; smaller practices may accept documented compliance in the early stages.

## When Does NEN 7510 Apply to Your App?

| Your app | Likely expectation |
| --- | --- |
| Patient records, treatment notes or diagnoses for care providers | NEN 7510 compliance expected; certification often required by larger customers |
| Scheduling for care providers including patient names and appointment types | Health data involved, NEN 7510 expectations apply |
| Intake forms or questionnaires collecting symptoms or health history | Health data involved, NEN 7510 expectations apply |
| Staff rostering for care organisations without patient data | Lower expectations, but customers may still apply their supplier policies |
| Consumer wellness app not used by care providers | NEN 7510 not directly applicable, but GDPR special category rules may apply |
| Healthcare marketing website | Not applicable |

Note that even appointment types can be health data. An appointment with a "psychologist" or "fertility clinic" reveals health information about the patient. When in doubt, assume health data is involved.

## GDPR and Health Data

Independently of NEN 7510, GDPR treats data concerning health as a special category under Article 9. Processing is prohibited unless a specific exception applies, such as necessity for the provision of health care under the responsibility of a professional bound by confidentiality. As a supplier, you usually act as a processor for the healthcare provider, which means:

- A processing agreement under Article 28 is required, often based on templates used in Dutch healthcare
- Your security measures must be appropriate to the high risk of health data
- A data protection impact assessment is often required for the processing, typically carried out by the healthcare provider with your input
- You must support the provider in meeting patients' rights, such as access and deletion where applicable
- Sub-processors, including hosting and AI providers, need careful selection and agreements

The Autoriteit Persoonsgegevens, the Dutch data protection authority, has repeatedly made health data a focus area. Our guide on [DPIAs for AI features](https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one) covers the assessment side.

## NEN 7512 and NEN 7513

Two related standards often appear in healthcare procurement:

**NEN 7512** covers trust in electronic data exchange between healthcare parties: how you authenticate parties, protect data in transit and ensure the integrity of exchanged information. It matters when your app sends data to or receives data from other healthcare systems.

**NEN 7513** covers logging of actions on electronic patient records: who accessed which record, when and what they did. For any app containing patient records, healthcare customers will expect access logging that meets NEN 7513 principles, because patients have the right to know who has accessed their data.

## What NEN 7510 Means Technically for an AI-Built App

AI-generated healthcare prototypes typically lack exactly the controls healthcare buyers check first. The technical baseline looks like this:

| Area | Requirement | Common gap in AI-built apps |
| --- | --- | --- |
| Authentication | Strong authentication, MFA for professionals, secure session handling | Email and password only, long sessions |
| Access control | Access only for professionals involved in treatment, roles per organisation | All staff see all patients, or isolation only in the frontend |
| Access logging | Every view and change of patient data logged, per NEN 7513 principles | No logging, or only error logs |
| Encryption | TLS in transit, encryption at rest, careful key management | Usually provided by hosting, but file storage public or unsigned |
| Hosting | EU hosting with suppliers that support healthcare requirements | Default region outside the EU |
| Backups and continuity | Tested backups, defined recovery objectives | Backups never restored |
| Data minimisation | Collect only what is necessary | Extensive optional fields, free text everywhere |
| AI features | No health data to providers without agreements, no training use | Patient notes sent to AI APIs without agreements |
| Development | Change management, testing, separation of environments | Real patient data in test environments |

A particularly important rule: **never use real patient data in development or staging**. AI builders encourage testing with realistic data, and founders sometimes import a pilot customer's export to see how the app behaves. That creates an uncontrolled copy of health data in a less protected environment.

## AI Features in Healthcare Apps

AI features such as summarising consultation notes, drafting referral letters or classifying intake questionnaires can save healthcare professionals significant time. They also raise specific questions:

- **Which provider processes the data, and where?** EU processing and a processing agreement are expected.
- **Is data used for training?** Contracts should exclude it.
- **Is output reviewed?** Professionals should review AI-generated content before it becomes part of a record.
- **Is this a medical device?** Software that supports diagnosis or treatment decisions may fall under the EU Medical Device Regulation. Administrative support usually does not, but clinical decision support may. Get advice early if your feature influences clinical decisions.
- **What does the EU AI Act say?** Some AI uses in healthcare may be classified as high-risk, particularly where linked to medical devices.

## Documents Healthcare Buyers Typically Request

Whether or not you are certified, healthcare procurement teams usually ask for a recognisable set of documents. Having them ready shortens assessments considerably:

- **Supplier security overview** mapped to NEN 7510 themes: organisation, access control, cryptography, operations, communications, development, supplier management, incident management and continuity
- **Processing agreement** suitable for healthcare, often based on a sector template, with clear descriptions of data categories, purposes, retention and sub-processors
- **Sub-processor list** with locations and the safeguards for each
- **Logging description** explaining which access events are recorded, how long logs are kept and how a provider can retrieve them to answer patient questions
- **Incident procedure** with notification timelines that allow the provider to meet its own 72-hour GDPR deadline
- **Continuity summary** with backup frequency, recovery objectives and the date of the last restore test
- **Input for the DPIA** describing data flows, risks and mitigations, so the provider can complete its assessment

Keep these documents short, specific and current. A five-page overview that matches what reviewers find in the product builds more trust than a fifty-page policy pack that does not.

## Certification or Documented Compliance?

For an early-stage healthcare SaaS, full NEN 7510 certification may not be the first step. A realistic path:

1. **Build the technical baseline** described above.
2. **Document how you meet relevant controls,** in a supplier security overview mapped to NEN 7510 themes.
3. **Prepare healthcare-specific documents:** processing agreement, sub-processor list, logging description, incident procedure and continuity summary.
4. **Pilot with smaller providers** who accept documented compliance.
5. **Start certification** when larger customers make it a requirement, typically following an ISO 27001-style project with NEN 7510 additions.

Our article on [ISO 27001 for early-stage SaaS](https://launchstudio.eu/en/blog/iso-27001-for-early-stage-saas-when-to-start) explains the certification process, which NEN 7510 closely follows.

## How LaunchStudio Helps

LaunchStudio builds the technical foundations that healthcare customers and NEN 7510 assessments look for: MFA and strong session handling, role-based access per organisation and care relationship enforced in the database, access logging aligned with NEN 7513 principles, EU hosting, private file storage, tested backups, safe AI integrations and separated environments with synthetic test data. We also help prepare the technical sections of your supplier documentation.

The **Launch Ready** package (€800-€3,500) covers security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, backups, monitoring and priority support, which most healthcare apps need. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink co-founded the cybersecurity company now known as CFLW Cyber Strategies. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Speech Therapy App With Patient Notes in a Test Database

Annemiek Dekker, a speech therapist in Enschede, built Logopedieplan with Lovable and Supabase: an app where speech therapists plan treatment, record session notes, share home exercises with patients and their parents, and produce progress reports for referring doctors. Her own practice and two others used it, and a regional chain of twelve practices wanted to adopt it, subject to a supplier assessment referencing NEN 7510.

The assessment questionnaire exposed serious gaps. Every therapist in a practice could see every patient, including children treated by colleagues. There was no MFA and sessions lasted thirty days. Nothing recorded who viewed a patient's notes. Exercise videos for children were in a public storage bucket. An AI feature summarising session notes called a US endpoint without a processing agreement, and the staging project contained a copy of real patient data imported to test reports.

LaunchStudio deleted the patient data from staging and replaced it with synthetic records, then rebuilt access control so therapists only saw patients in their caseload, with practice managers holding defined additional rights. MFA became mandatory for therapists with shorter sessions, and an append-only access log recorded every view and change of patient data, with a screen for practices to answer patient access requests. Exercise videos moved to private storage with signed links, the AI summary moved to an EU endpoint under a processing agreement with no training use and therapist review before saving, and hosting moved to Frankfurt with tested point-in-time recovery. Engineers mapped the controls to NEN 7510 themes in a supplier security document.

**Result:** The practice chain accepted the documented compliance for a one-year pilot, with NEN 7510 certification planned for the second year. Logopedieplan now supports around 70 therapists, and the access log has been used twice to answer parents' questions about who viewed their child's file.

> *"I knew how to treat patients and protect their privacy in a practice. I didn't know what that meant in a database until LaunchStudio showed me."*
> - **Annemiek Dekker, Founder, Logopedieplan (Enschede)**

**Cost & Timeline:** €6,600 (Launch & Grow package: caseload-based access control, MFA, access logging, private storage, EU AI integration, EU hosting and NEN 7510 control mapping) - completed in 17 business days.

## Frequently Asked Questions

### Do I need NEN 7510 certification to sell to Dutch healthcare providers?

Not always at the start. Healthcare providers must meet NEN 7510 and will assess suppliers who process health data. Smaller providers may accept documented compliance and a solid technical baseline, while hospitals and larger organisations often require certification. Plan for certification as you grow.

### Is appointment data health data?

Often, yes. An appointment with a specific type of care provider, or an appointment type such as "diabetes check", can reveal health information about a person. Treat scheduling data for healthcare providers as health data unless you are certain it reveals nothing about health.

### Can I use AI features with patient data?

Possibly, with care. You need an appropriate legal basis through your customer, a processing agreement with the AI provider, EU processing where possible, no training use and review by professionals. If the feature supports clinical decisions, check whether medical device rules apply.

### How does Manifera's experience help with healthcare security?

Manifera has built systems under strict security requirements for 11+ years, and its CEO comes from cybersecurity. LaunchStudio uses that experience to implement the controls healthcare buyers check first, such as access per care relationship and complete access logging, without slowing product development.

### Does a strong security posture help healthcare apps get found?

Yes. Healthcare buyers research suppliers carefully, and a clear public page describing your security, hosting and compliance approach helps them shortlist you. Search engines and AI answer engines also surface such pages when buyers ask which tools meet healthcare requirements.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need NEN 7510 certification to sell to Dutch healthcare providers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always at first. Smaller providers may accept documented compliance and a solid baseline; hospitals and larger organisations often require certification." }
    },
    {
      "@type": "Question",
      "name": "Is appointment data health data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often yes, because the type of provider or appointment can reveal health information. Treat healthcare scheduling data as health data unless certain otherwise." }
    },
    {
      "@type": "Question",
      "name": "Can I use AI features with patient data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Possibly, with a legal basis via the customer, a processing agreement, EU processing, no training use and professional review; check medical device rules for clinical support." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with healthcare security?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built systems under strict security requirements for 11+ years, and LaunchStudio implements access per care relationship and access logging that buyers check first." }
    },
    {
      "@type": "Question",
      "name": "Does a strong security posture help healthcare apps get found?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A clear public security and compliance page helps buyers shortlist suppliers and is surfaced by search and AI engines." }
    }
  ]
}
</script>
