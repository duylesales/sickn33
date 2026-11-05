---
Title: "Records of Processing for Small SaaS: GDPR Article 30"
Keywords: gdpr article 30 saas, records of processing activities template, verwerkingsregister avg, processing register small business, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Records of Processing for Small SaaS: GDPR Article 30

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Records of Processing for Small SaaS: GDPR Article 30",
  "description": "GDPR Article 30 requires most SaaS companies to keep records of processing activities, both as controller for their own customers and staff and as processor for their customers' data. This guide explains the small-business exemption and why it rarely applies to SaaS, what the records must contain, how to build them from an AI-built app's actual data flows and how to keep them current.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-12",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/records-of-processing-for-small-saas-gdpr-article-30" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 30: Records of processing activities", "url": "https://gdpr-info.eu/art-30-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Register of processing activities", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/basic-gdpr/gdpr-basics/register-of-processing-activities" },
    { "@type": "CreativeWork", "name": "Article 29 Working Party position paper on Article 30(5) derogations", "url": "https://ec.europa.eu/newsroom/article29/items/624045" }
  ]
}
</script>

Most founders encounter the GDPR through visible tasks: a privacy policy, a cookie banner, a processing agreement for a business customer. Fewer know about the document that sits underneath all of them: the records of processing activities, often called a processing register or, in Dutch, a verwerkingsregister. GDPR Article 30 requires most organisations to keep one, and supervisory authorities such as the Autoriteit Persoonsgegevens can ask to see it.

For a SaaS company, the register is more than a compliance artefact. It is a map of where personal data enters your product, where it goes, who processes it and how long it stays. That map answers questions from customers, auditors and investors, and it often reveals data flows nobody knew existed, especially in apps built quickly with Lovable, Bolt or Cursor and connected to a dozen services along the way.

This guide explains what Article 30 requires and how a small SaaS company can produce a useful register in a day or two. It is general information, not legal advice.

## Key Takeaways

- **Article 30 requires records of processing activities** from controllers and from processors, with defined content for each.
- **The exemption for organisations with fewer than 250 employees rarely applies to SaaS,** because it does not cover processing that is not occasional, processing likely to create risks or special category data.
- **A SaaS company usually needs two registers:** one as controller for its own customers, users, prospects and staff, and one as processor for the personal data its customers put into the product.
- **Build the register from real data flows,** by inventorying your app's database, integrations and third-party services, not from a template alone.
- **Keep it current,** because every new integration, AI feature or analytics tool changes it.

## What Article 30 Requires

Article 30 distinguishes between the two roles an organisation can have.

**As a controller,** you decide why and how personal data is processed, for example your customer accounts, billing data, marketing contacts and employee records. Your records must include:

- Your name and contact details, and those of your data protection officer if you have one
- The purposes of the processing
- The categories of data subjects and of personal data
- The categories of recipients, including those outside the EU
- Transfers to third countries and the safeguards used
- Where possible, retention periods for each category of data
- Where possible, a general description of technical and organisational security measures

**As a processor,** you process personal data on behalf of your customers, for example the employee records an HR SaaS stores for its clients. Your records must include:

- Your name and contact details, and those of each controller you act for
- The categories of processing carried out on behalf of each controller
- Transfers to third countries and the safeguards used
- Where possible, a general description of security measures

Records must be in writing, which includes electronic form, and made available to the supervisory authority on request.

## Why the Small-Business Exemption Rarely Helps

Article 30(5) says the obligation does not apply to organisations with fewer than 250 employees, unless the processing is likely to result in a risk to rights and freedoms, is not occasional, or includes special categories of data or data on criminal convictions.

For a SaaS company, the processing is the product. It happens continuously, not occasionally. European data protection authorities have explained that the exemption should be read narrowly: if any of the conditions applies, at least the processing concerned must be recorded. In practice, almost every SaaS company processing customer data needs records, regardless of size. Dutch guidance from the Autoriteit Persoonsgegevens reflects the same reading.

Treat the register as required. It is also the easiest GDPR document to produce once you know what to put in it.

## Controller and Processor: Which Applies When

| Data | Your role | Example |
| --- | --- | --- |
| Account details of your customers' users | Usually controller for account management, processor for content | Name and email of each user, used for login and billing |
| Data your customers store in the product | Usually processor | Patient notes in a practice tool, candidate CVs in a recruitment tool |
| Billing and invoicing data | Controller | Company details, payment status, invoices |
| Marketing contacts and newsletter subscribers | Controller | Leads from your website, webinar sign-ups |
| Website and product analytics | Controller | Page views, events, campaign data |
| Support tickets | Controller, sometimes also processing customer data within tickets | Emails to your support address |
| Your own staff and contractors | Controller | Payroll, contracts, access accounts |

The split matters because your obligations differ. As a controller you need a legal basis and must handle data subject requests. As a processor you act on your customer's instructions, under a processing agreement, and support them in meeting their obligations.

## How to Build the Register From Your Actual App

Templates help with format, but the content must come from your system. For an AI-built SaaS, follow these steps.

**1. Inventory your database.** List every table and the personal data fields in it. AI builders often add fields "just in case", such as phone numbers, birthdates or free-text notes, so this step frequently reveals data you do not need.

**2. Inventory your services.** List every third-party service your app and company use: hosting, database, authentication, email delivery, payments, analytics, error tracking, support desk, CRM, AI providers, automation tools and file storage. For each, note what personal data it receives, why and where it is processed.

**3. Trace the data flows.** For each type of data, follow its path: where it enters (a form, an import, an API), where it is stored, which services receive it and where it leaves (exports, emails, integrations).

**4. Define purposes and retention.** For each processing activity, write the purpose in one sentence and decide how long the data is kept. "Until the account is deleted, plus 30 days for backups" is a valid retention description; "forever" is not.

**5. Describe security measures.** Summarise access control, encryption, logging, backups and organisational measures. A paragraph per register is usually enough, with reference to your security overview.

**6. Record transfers.** If any service processes data outside the EU, note the country and the transfer mechanism, such as an adequacy decision or standard contractual clauses.

## A Simple Format That Works

A spreadsheet or a structured document is enough. Each row is a processing activity:

| Activity | Purpose | Data subjects | Data categories | Recipients | Location and transfers | Retention | Security |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Customer accounts | Provide access to the service | Customer users | Name, email, role, login history | Hosting and auth provider | EU | Account lifetime plus 30 days | See security overview |
| Billing | Invoicing and payment | Customer contacts | Company details, invoice data, payment status | Payment provider, accounting tool | EU | 7 years for tax records | See security overview |
| Product analytics | Improve the product | Customer users | Pseudonymous usage events | Analytics provider | EU | 24 months | Aggregated, no direct identifiers |
| Transactional email | Account and service messages | Customer users | Email address, message content | Email delivery provider | EU or with safeguards | Provider logs per its policy | Authenticated sending |
| Support | Answer questions | Customer users | Name, email, ticket content | Support desk tool | EU | 2 years after closure | Access limited to support staff |

The processor register is shorter: one entry per customer type or per customer, describing the processing you perform on their behalf, sub-processors and security measures.

## Common Findings When Founders Build Their First Register

**AI features sending data outside the EU.** A summary or chat feature calling an AI API in the United States, without anyone recording it or checking the provider's terms on data use.

**Forgotten tools.** An error tracking service capturing request bodies with personal data, a form builder storing submissions, or an automation platform copying customer records.

**Unbounded retention.** No deletion of inactive accounts, old leads or support tickets.

**Unnecessary data.** Fields collected by default in AI-generated forms that serve no purpose.

**Inconsistency with the privacy policy.** Services in use that the privacy policy does not mention, or services mentioned that are no longer used.

Each finding is an opportunity: removing unnecessary data and services reduces risk, cost and the length of every future security questionnaire.

## Linking the Register to Other Documents

The register connects to most other privacy documents:

- **Privacy policy:** should be consistent with the controller register's purposes, recipients and retention.
- **Processing agreements:** the processor register and sub-processor list should match what you commit to customers.
- **DPIAs:** high-risk processing identified in the register may require a data protection impact assessment. Our guide on [DPIAs for AI features](https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one) explains when.
- **Security questionnaires:** customers ask about sub-processors, locations and retention, all of which the register already contains.
- **Breach response:** in an incident, the register tells you quickly which data and which people may be affected. See our article on [the 72 hours after a data breach](https://launchstudio.eu/en/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas).

## Keeping It Current

A register written once and forgotten loses its value. Make updates part of normal work:

- **Every new integration** or third-party service triggers a register update.
- **Every new data field** containing personal data is checked against an existing purpose.
- **A quarterly review** of services and retention takes thirty minutes.
- **Version history** shows when changes were made, which helps in audits.

For AI-built apps, add a rule to your project instructions: any prompt that adds a new external service or data field must be flagged for a register update. It is easier to keep the register current than to reconstruct it later.

## How LaunchStudio Helps

LaunchStudio does not provide legal advice, but we do the technical work that a good register depends on: inventorying the database and services, tracing data flows, removing unnecessary fields and integrations, moving processing to EU regions, implementing retention and deletion, and documenting security measures. Founders receive a technical data map that they or their privacy adviser can turn into the formal register.

The **Launch Ready** package (€800-€3,500) covers this as part of a production launch, along with security hardening and deployment. **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working under European privacy requirements for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Recruitment Tool With Eleven Undocumented Processors

Jesse van Dam built Vacatureflow with Lovable and Supabase: an applicant tracking tool for small recruitment agencies in the Randstad, where recruiters store candidate profiles, CVs and interview notes and share shortlists with clients. When a larger agency asked for his processing register and sub-processor list as part of its supplier review, Jesse realised he had neither.

Building the register exposed far more than he expected. Vacatureflow used eleven external services, from email delivery and error tracking to an AI service that parsed CVs, several of which were not mentioned in the privacy policy. The CV parsing service processed data in the United States without a processing agreement, the error tracker captured full request bodies including candidate details, and candidate profiles were never deleted, even years after a vacancy closed. Several AI-generated form fields, including date of birth and nationality, were collected without any purpose.

LaunchStudio produced a technical data map of every table, field and service, then removed the unused fields and three services that were no longer needed. The CV parsing moved to an EU-based provider under a processing agreement with no training use, and error tracking was configured to strip request bodies and personal data. Retention rules automatically anonymised candidate profiles 12 months after their last activity unless the candidate consented to stay in the pool, and backups followed the same cycle. Engineers documented security measures and sub-processors, which Jesse and his privacy adviser turned into controller and processor registers and an updated privacy policy.

**Result:** Jesse delivered both registers and a sub-processor list to the larger agency within two weeks, and the supplier review was approved. The data reduction also cut storage and service costs, and the same documents have since been reused in four other customer reviews.

> *"I thought a processing register was paperwork. Building it showed me data I didn't need, services I'd forgotten and risks I hadn't seen."*
> - **Jesse van Dam, Founder, Vacatureflow (Haarlem)**

**Cost & Timeline:** €2,800 (Launch Ready package: data mapping, field and service reduction, EU AI provider, retention automation and security documentation) - completed in 9 business days.

## Frequently Asked Questions

### Does my small SaaS company need a processing register?

Almost certainly. The exemption for organisations with fewer than 250 employees does not apply when processing is not occasional, creates risks or involves special category data. A SaaS product processes personal data continuously, so records are required at least for that processing, regardless of company size.

### What is the difference between the controller and processor registers?

The controller register covers processing you decide on yourself, such as customer accounts, billing, marketing and staff data. The processor register covers processing you carry out on behalf of customers, such as data they store in your product, and lists the controllers you work for and your sub-processors.

### Can I use a template for my processing register?

Yes, for the format. The content must come from your actual system: database fields, services, data flows, purposes and retention periods. A template filled in without inventorying your app usually misses services and data that customers and auditors will find.

### How does Manifera's experience help with GDPR documentation?

Manifera has built and documented systems under European privacy requirements for 11+ years. LaunchStudio uses that experience to map data flows accurately and to reduce unnecessary data and services, so the register reflects a system that is genuinely privacy-conscious.

### Does good GDPR documentation help my visibility with customers?

Yes. A clear public privacy and sub-processor page answers buyers' questions quickly and signals maturity, and well-structured information of this kind is often surfaced by search engines and AI answer engines when buyers compare suppliers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does my small SaaS company need a processing register?",
      "acceptedAnswer": { "@type": "Answer", "text": "Almost certainly. The under-250 exemption does not apply to processing that is not occasional, risky or involves special category data, which covers SaaS processing." }
    },
    {
      "@type": "Question",
      "name": "What is the difference between the controller and processor registers?",
      "acceptedAnswer": { "@type": "Answer", "text": "The controller register covers your own decisions such as accounts, billing and marketing; the processor register covers processing on customers' behalf and lists sub-processors." }
    },
    {
      "@type": "Question",
      "name": "Can I use a template for my processing register?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes for the format, but content must come from your actual database, services, data flows, purposes and retention periods." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with GDPR documentation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has documented systems under European privacy rules for 11+ years, and LaunchStudio maps data flows accurately and reduces unnecessary data." }
    },
    {
      "@type": "Question",
      "name": "Does good GDPR documentation help my visibility with customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A clear public privacy and sub-processor page answers buyer questions and is surfaced by search and AI engines when comparing suppliers." }
    }
  ]
}
</script>
