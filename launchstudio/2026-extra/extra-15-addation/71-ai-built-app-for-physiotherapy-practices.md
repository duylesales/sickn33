---
Title: "AI-Built App for Physiotherapy Practices: From Prototype to Production"
Keywords: app voor fysiotherapiepraktijk, physiotherapy practice software, fysio app laten bouwen, healthcare app gdpr netherlands, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI-Built App for Physiotherapy Practices: From Prototype to Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Built App for Physiotherapy Practices: From Prototype to Production",
  "description": "Physiotherapists and practice managers increasingly build their own tools with Lovable, Bolt or Cursor for scheduling, home exercise programmes and patient communication. This guide explains what a production-ready physiotherapy app needs in the Netherlands: health data protection, access by treatment relationship, logging, retention of patient records, integrations with practice systems, payments, accessibility and a realistic path to market.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-27",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-built-app-for-physiotherapy-practices" },
  "citation": [
    { "@type": "CreativeWork", "name": "KNGF: Royal Dutch Society for Physical Therapy", "url": "https://www.kngf.nl/" },
    { "@type": "CreativeWork", "name": "GDPR Article 9: Special categories of personal data", "url": "https://gdpr-info.eu/art-9-gdpr/" },
    { "@type": "CreativeWork", "name": "Wet op de geneeskundige behandelingsovereenkomst (WGBO)", "url": "https://wetten.overheid.nl/BWBR0005290/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Health", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/health" }
  ]
}
</script>

Physiotherapists are increasingly building their own software. A practice owner frustrated with exercise sheets printed on paper builds a home exercise app in Lovable. A physiotherapist with a sports background creates a rehabilitation tracker for athletes in Bolt. A practice manager builds a scheduling and waiting list tool with Cursor because the existing system does not handle group classes well. Within weeks, colleagues ask to use it, then other practices, and the founder realises they might have a product.

That is a promising path. Physiotherapy practices in the Netherlands are numerous, mostly small, and keenly aware of where their software falls short. But a tool used by one practice owner with their own patients is very different from a product used by dozens of practices with thousands of patients. Health data, treatment relationships, professional obligations and integrations with existing practice systems all come into play.

This guide explains what a production-ready physiotherapy app needs. It is general information, not legal advice; consult privacy and healthcare specialists for your specific situation.

## Key Takeaways

- **Physiotherapy apps process health data,** a special category under GDPR, which requires strong security, careful access control and documented processing.
- **Access should follow the treatment relationship:** therapists see their patients, practice managers see what they need, and nobody sees other practices' data.
- **Patient records come with retention obligations** under Dutch healthcare law, which affects deletion and backups.
- **Healthcare buyers expect NEN 7510-aligned security,** processing agreements and clear answers about hosting and AI use.
- **Integration with existing practice systems** often matters more for adoption than features.

## Typical Physiotherapy App Ideas

| App type | Main features | Data sensitivity |
| --- | --- | --- |
| Home exercise programmes | Exercise library, videos, personalised plans, progress tracking | High: linked to diagnosis and treatment |
| Scheduling and waiting lists | Appointments, group classes, reminders, waiting list management | Medium to high: appointment types can reveal health information |
| Patient intake | Questionnaires, consent, medical history | High |
| Outcome measurement | Standardised questionnaires, progress over time | High |
| Communication | Secure messages between patient and therapist | High |
| Practice operations | Rosters, room planning, internal tasks | Low to medium |

Most founders start with one of these and expand. The data sensitivity column should shape the architecture from the start.

## Health Data and GDPR

Data about a patient's complaints, diagnosis, treatment, exercises and progress is data concerning health, a special category under GDPR Article 9. In a typical B2B model, the practice is the controller and your company is the processor. That means:

- **A processing agreement** with each practice, describing data, purposes, security and sub-processors
- **Strong security measures** proportionate to the risk, including encryption, access control and logging
- **Support for patient rights,** such as access to their data, through tools practices can use
- **A data protection impact assessment** carried out by the practice in many cases, with your input
- **Careful choice of sub-processors,** including hosting, email and AI providers, preferably in the EU

If you also offer the app directly to consumers, you may become a controller for some processing, with additional obligations. Clarify your role early.

## Access by Treatment Relationship

AI-generated prototypes often give every user in a practice access to every patient. In healthcare, access should follow the treatment relationship:

- **Therapists** see patients they treat, plus colleagues' patients when standing in, through an explicit and logged mechanism.
- **Practice managers** see scheduling and administrative data, and clinical data only where their role requires it.
- **Patients** see only their own programme, messages and appointments.
- **Nobody** sees data from other practices.

Implement these rules in the database with Row Level Security, not only in the interface, and test them with accounts for each role in at least two practices.

## Logging Access

Patients have the right to know who accessed their data, and healthcare standards such as NEN 7513 describe logging of access to patient records. Record views and changes of patient data, with who, when and what, in an append-only audit log that practices can query. Our guide on [audit logs for B2B SaaS](https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas) explains the structure.

## Retention of Patient Records

Dutch healthcare law sets retention obligations for medical records. The WGBO, the Dutch act on medical treatment agreements, sets a standard retention period for patient records of twenty years from the last change, with specific exceptions. If your app holds data that forms part of the patient record, such as treatment notes or progress measurements, retention rules affect:

- **Deletion:** users cannot simply delete clinical data whenever they like, and patient requests for deletion follow specific rules.
- **Practice offboarding:** when a practice leaves your platform, its records must be exported in a usable form so it can continue meeting its obligations.
- **Backups and archives:** long retention requires durable storage and a plan for very long periods.

Clarify with practices and your adviser which data counts as part of the medical record and which, such as appointment reminders, can follow shorter retention.

## Security Baseline

Healthcare customers will ask about security, often referencing NEN 7510. A sensible baseline:

| Area | Measure |
| --- | --- |
| Authentication | MFA for therapists and staff, secure session handling, optional patient MFA |
| Access control | RLS per practice and treatment relationship |
| Logging | Access and change logging for patient data |
| Hosting | EU region with providers offering healthcare-appropriate agreements |
| Files | Exercise videos and documents in private storage with signed links |
| Backups | Point-in-time recovery, tested restores |
| Environments | No real patient data in development or staging |
| AI features | EU processing, no training use, therapist review |

Our guide on [NEN 7510 and healthcare apps in the Netherlands](https://launchstudio.eu/en/blog/nen-7510-and-healthcare-apps-in-the-netherlands) covers the standard in more depth.

## AI Features in Physiotherapy Apps

AI can help therapists, for example by suggesting exercise progressions, summarising intake questionnaires or drafting patient-friendly explanations. Keep in mind:

- **Therapists remain responsible for treatment decisions.** AI suggestions should be reviewed and approved before reaching patients.
- **Clinical decision support may fall under medical device rules.** Features that influence diagnosis or treatment choices need careful assessment under the EU Medical Device Regulation; administrative and communication support usually does not.
- **Data minimisation:** send only what is necessary to the AI provider, preferably processed in the EU with no training use.

## Integration With Practice Systems

Most Dutch physiotherapy practices already use practice management software for patient records, scheduling and insurance declarations. A new app that duplicates data entry rarely succeeds. Consider:

- **Which system holds the master patient record,** and how your app relates to it
- **Available integration options,** such as APIs, exports or partner programmes of practice software vendors
- **Whether your app complements rather than replaces,** for example adding home exercise programmes to an existing scheduling and record system

Integration is often the deciding factor in adoption. Talk to practices about their current systems before building more features.

## Payments

Many physiotherapy services are declared to health insurers through existing practice systems. Your app may handle payments for services outside insurance coverage, such as group training, sports physiotherapy packages or premium exercise programmes. For those:

- Use iDEAL and SEPA direct debit for Dutch patients, through providers such as Mollie or Stripe.
- Issue correct invoices with VAT treatment appropriate to the service; discuss with an accountant, as medical services may be VAT-exempt while some wellness services are not.
- Keep payment data with the payment provider, not in your database.

## Accessibility and Patient Experience

Patients include older adults, people recovering from injury and people with limited mobility or vision. Make the patient-facing parts accessible: large touch targets, readable contrast, captions on exercise videos, simple language and support for screen readers. Our guide on [WCAG fixes for AI-built apps](https://launchstudio.eu/en/blog/wcag-accessibility-fixes-for-ai-built-apps) covers practical steps.

## Patient Communication and Notifications

Physiotherapy apps often send reminders, exercise prompts and messages between sessions. These are valuable for adherence, but they also carry privacy risks, because notifications appear on lock screens and in email inboxes that others may see:

- **Keep notification content neutral.** "You have a new message from your practice" is safer than including complaint or exercise details.
- **Let patients choose channels and frequency,** and respect quiet hours.
- **Use secure in-app messaging** for clinical content, rather than email or SMS bodies.
- **Send email from an authenticated domain** with the practice's name, so patients recognise and trust it.
- **Log messages as part of the treatment context** where they relate to care, so therapists and practices can review communication history.

Good notification design improves adherence without exposing patients' health information to anyone who glances at their phone.

## A Realistic Path to Market

1. **Validate with a few practices** using real workflows but careful data handling.
2. **Build the production baseline:** security, access control, logging, EU hosting, backups.
3. **Prepare documentation:** processing agreement, security overview, sub-processor list.
4. **Pilot with a group of practices,** gathering feedback and references.
5. **Address integration** with common practice systems.
6. **Plan for certification** as you approach larger practice chains or healthcare groups.

## Pricing for Practices

Physiotherapy practices are cost-conscious, and pricing models influence adoption. Common approaches include a monthly fee per therapist, a fee per active patient, or tiers by practice size. Per-therapist pricing is easy for practices to budget; per-patient pricing aligns with value but varies month to month. Whatever you choose, keep it simple, offer a pilot period with clear conditions and make sure your infrastructure costs, especially for video storage and AI features, are covered at the price you set.

## How LaunchStudio Helps

LaunchStudio takes physiotherapy apps from prototype to production: access control by practice and treatment relationship, MFA, access logging, EU hosting with tested backups, private storage for exercise videos, retention-aware deletion and export, safe AI integrations, payments for uninsured services and documentation for practices' privacy officers.

Most healthcare apps fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink's cybersecurity background shapes our approach to health data. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Exercise App That Practice Chains Wanted to Adopt

Wouter Smit, a physiotherapist running two practices near Utrecht, built Oefenmaatje in Lovable and Supabase: an app where therapists assemble home exercise programmes from a video library, patients follow them on their phones and log pain scores, and therapists see progress before the next appointment. After a year in his own practices, a chain of fourteen physiotherapy practices wanted to adopt it.

The chain's quality officer sent a list of requirements that the prototype could not meet. All therapists across both of Wouter's practices could see all patients. Exercise videos and patients' uploaded photos of swelling were in a public bucket. There were no access logs, no MFA and no processing agreement. Patients deleting their account removed treatment progress that formed part of the patient record, and a staging project contained a copy of real patient data used to test new features.

LaunchStudio separated data per practice and restricted therapists to their own patients, with a logged "stand-in" mechanism for colleagues and defined rights for practice managers. MFA became mandatory for staff, every view and change of patient data was written to an append-only access log, and videos and photos moved to private storage with signed links. Account deletion by patients was redesigned to stop app access while retaining clinical data according to the practice's retention obligations, with an export for practices. Real patient data was removed from staging and replaced with synthetic data, hosting moved to Frankfurt with tested point-in-time recovery, and engineers prepared a security overview and data flow description for the chain's processing agreement.

**Result:** The chain approved Oefenmaatje after its quality officer's review and rolled it out across all fourteen practices, with around 4,000 active patients within six months. Wouter now discusses an integration with the chain's practice management system, using the documented data model as the starting point.

> *"I built the app as a physiotherapist. Making it ready for other practices meant thinking like a guardian of other people's patient records."*
> - **Wouter Smit, Founder, Oefenmaatje (Utrecht)**

**Cost & Timeline:** €6,700 (Launch & Grow package: practice and treatment-based access control, MFA, access logging, private storage, retention-aware deletion, EU hosting and documentation) - completed in 17 business days.

## Frequently Asked Questions

### Can I build a physiotherapy app with Lovable or Bolt?

Yes, AI builders are well suited to building the interface and workflows quickly. Before using the app with patients beyond a small pilot, add production foundations: access control by practice and treatment relationship, MFA, access logging, EU hosting, private file storage, backups and documentation for practices.

### Is exercise and progress data health data?

Usually yes. Exercises prescribed for a specific complaint, pain scores and progress measurements reveal information about a person's health. Treat this data as special category data under GDPR, with corresponding security and legal safeguards.

### What happens to patient data when a practice stops using my app?

The practice remains responsible for its patient records and their retention. Provide a complete export in a usable format, agree on a transition period and delete data from your systems after confirmation, in line with your processing agreement.

### How does Manifera's experience help with healthcare apps?

Manifera has built systems under strict security requirements for 11+ years, and its CEO comes from cybersecurity. LaunchStudio applies that experience to physiotherapy and other healthcare apps, focusing first on access control, logging and data protection that healthcare buyers check.

### Does a secure, well-documented app help physiotherapy practices find me?

Yes. Practices and chains research suppliers carefully, and clear information about security, hosting, accessibility and integrations helps them shortlist your app. Search engines and AI answer engines surface such information when practice owners look for tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I build a physiotherapy app with Lovable or Bolt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; before wider use add access control by practice and treatment relationship, MFA, logging, EU hosting, private storage, backups and documentation." }
    },
    {
      "@type": "Question",
      "name": "Is exercise and progress data health data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually yes; treat it as special category data under GDPR." }
    },
    {
      "@type": "Question",
      "name": "What happens to patient data when a practice stops using my app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Provide a complete export, agree a transition and delete after confirmation per the processing agreement." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with healthcare apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built systems under strict security requirements for 11+ years, focusing on access control, logging and data protection." }
    },
    {
      "@type": "Question",
      "name": "Does a secure, well-documented app help physiotherapy practices find me?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; clear security, hosting and integration information helps practices and AI engines shortlist you." }
    }
  ]
}
</script>
