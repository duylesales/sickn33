---
Title: "Production Launch for HR and Recruitment SaaS"
Keywords: hr saas production launch, recruitment software privacy, applicant data retention netherlands, ai recruitment high risk ai act, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Production Launch for HR and Recruitment SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Production Launch for HR and Recruitment SaaS",
  "description": "A guide to launching an HR or recruitment SaaS built with Lovable, Bolt, v0, Cursor or Claude Code in the Netherlands: employee and applicant data under the GDPR, retention of applicant data, restrictions on sick leave and medical information, BSN handling, AI in recruitment under the EU AI Act, role-based access for managers and HR, integrations with payroll and HR systems, and what LaunchStudio does to make such products production ready.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-27",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/production-launch-for-hr-and-recruitment-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Werk en uitkering", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/werk-en-uitkering" },
    { "@type": "CreativeWork", "name": "EUR-Lex: Artificial Intelligence Act (Regulation (EU) 2024/1689)", "url": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj" },
    { "@type": "CreativeWork", "name": "EUR-Lex: General Data Protection Regulation (EU) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj" },
    { "@type": "CreativeWork", "name": "Business.gov.nl: Employer obligations", "url": "https://business.gov.nl/regulation/employer-obligations/" }
  ]
}
</script>

HR and recruitment software is a popular category for AI-built products. Founders with backgrounds in recruitment, HR consultancy or staffing build applicant tracking tools, onboarding portals, leave and absence planners, performance review systems, shift scheduling for hourly workers and tools that match candidates to vacancies. Small and medium employers want these tools, because many still manage people in spreadsheets and email.

HR data is also among the most sensitive data a business holds. Salaries, contracts, performance notes, sick leave, disciplinary records and application documents can all cause real harm if exposed. Dutch privacy rules contain specific guidance on employee and applicant data, and the EU AI Act classifies certain uses of AI in recruitment and employment as high-risk. Employers, works councils and HR managers ask careful questions before adopting new tools.

This page explains what a production launch for an HR or recruitment SaaS typically involves, what LaunchStudio does and where you need legal or privacy specialists. We are not lawyers; we work alongside them and make sure the app does what their advice requires.

## Key Takeaways

- **HR data is highly sensitive;** access must follow real organisational roles.
- **Applicant data has short retention expectations** unless the candidate agrees to longer storage.
- **Sick leave data is restricted:** employers generally may not record diagnoses.
- **AI used to screen or evaluate candidates** can be high-risk under the EU AI Act.
- **Typical price: €2,500-€7,500 within Launch & Grow,** depending on roles, integrations and AI features.

## Why HR Data Needs Special Care

| Aspect | Why it matters |
| --- | --- |
| Sensitive content | Salaries, performance, conflicts and health-related absence |
| Power imbalance | Employees and applicants cannot easily refuse processing |
| Many roles | Employees, managers, HR, payroll, works council, recruiters, hiring managers |
| Retention rules | Applicant and former employee data should not be kept longer than needed |
| Medical information | Strict limits on what employers may register about sickness |
| Identification numbers | BSN may only be processed where the law allows, such as payroll |
| AI regulation | Recruitment and employment AI uses are treated as high-risk |
| Employee rights | Access, correction and deletion requests from employees and candidates |

## Applicant Data and Retention

Recruitment tools collect CVs, motivation letters, assessments, interview notes and sometimes test results. Dutch privacy guidance generally expects applicant data to be deleted within a few weeks after the procedure ends, unless the candidate consents to longer storage, for example to be considered for future vacancies, often up to around a year. Check current guidance from the Dutch Data Protection Authority and your legal adviser for the exact expectations that apply to your customers.

For the app, that means retention must be built in: automatic deletion or anonymisation after a configurable period, a consent option for candidates who want to stay in the pool, clear tracking of when consent was given and a way for candidates to request deletion. AI-built recruitment tools often keep every candidate forever, which becomes a problem in the first privacy review.

## Sick Leave and Medical Information

Absence tools are common in HR SaaS. Dutch rules restrict what employers may register about sick employees. In general, employers may record practical information, such as expected duration, contact details and whether the absence relates to an accident with a liable third party, but not diagnoses, symptoms or medical details, which belong with the occupational health service. An app that offers a free-text field "reason for absence" invites employees and managers to type exactly the information that should not be stored.

We design absence features around these limits: structured fields for permitted information, no free-text medical notes for employers, separate access for occupational health professionals where the product supports them and clear guidance in the interface. Your legal adviser can confirm the exact rules for your use case.

## The BSN in HR Software

Employers need the citizen service number for payroll and tax purposes, but its use is restricted to what the law allows. Many HR tools, such as recruitment, scheduling or performance tools, do not need it at all. If your product handles payroll or integrates with payroll systems, restrict access to the BSN to the roles that need it, avoid showing it on screens where it is not required and never use it as an identifier in URLs or logs.

## AI in Recruitment and Employment

The EU AI Act lists AI systems used for recruitment or selection, such as screening applications, filtering candidates or evaluating them, and AI used for decisions about promotion, termination, task allocation or monitoring of workers, among high-risk uses. High-risk systems carry obligations, including risk management, data governance, documentation, human oversight, transparency and accuracy, which apply on a phased timeline. Providers and deployers have different responsibilities.

For founders, this matters a lot. A feature that ranks candidates or flags employees for performance concerns may make your product a high-risk AI system, with significant obligations. A feature that helps write a vacancy text or summarise an interview note for the recruiter's own use is likely in a lower-risk category, though transparency still matters. Discuss your AI features with a legal adviser early. Technically, we help by keeping humans in control of decisions, logging AI outputs, minimising personal data sent to model providers, avoiding sensitive attributes and documenting how features work.

## What LaunchStudio Does for HR and Recruitment SaaS

| Area | Typical work |
| --- | --- |
| Hosting | Database, storage and backups in an EU region, documented subprocessors |
| Organisation separation | Each employer's data fully separated |
| Roles | Employees, managers, HR, payroll, recruiters, hiring managers and admins with precise permissions |
| Manager scope | Managers see only their own teams; HR sees what its role requires |
| Sensitive fields | Salary, BSN and performance data restricted to specific roles |
| Documents | Contracts, CVs and certificates in private storage with signed links |
| Retention | Automatic deletion or anonymisation of applicants and former employees after agreed periods |
| Candidate consent | Consent for talent pools, recorded and revocable |
| Absence features | Structured permitted fields, no medical free text for employers |
| AI features | Human oversight, logged outputs, minimised data, documentation |
| Audit logging | Records of access to sensitive records and changes to roles |
| Authentication | MFA for HR and admins, SSO for larger employers |
| Integrations | Payroll, HR and accounting systems through secure, idempotent connections |
| Documentation | Security overview, data flows, input for processing agreements and DPIAs |

## Roles That Match Real Organisations

The most common problem in AI-built HR tools is that roles are too simple: "admin" and "employee", with admins seeing everything. Real organisations need more nuance. A team lead should see leave requests and schedules for their own team but not salaries. HR advisers may see personnel files for the departments they support. Payroll needs salary and BSN but not performance notes. Hiring managers see candidates for their vacancies only. Works council members may need aggregated reports but no individual data.

We model these roles with you, enforce them through Row Level Security and test them with accounts for each role. Customers notice this quickly: an HR manager trying the product will check what a team lead can see.

## Integrations With Payroll and HR Systems

HR SaaS products often integrate with payroll providers, HR information systems and accounting software. These integrations carry the most sensitive data, so they need secure connections per customer, scoped permissions, idempotent processing, error handling and logs that do not store salary details unnecessarily. We build or harden these integrations as part of the project or as a separate integration service.

## Works Councils and Employee Trust

In the Netherlands, works councils have rights of consent for certain arrangements involving the processing of employee data and systems that can monitor employees. Employers adopting your product may need to involve their works council. Clear documentation of what data your product processes, who can see it and how AI features work makes that conversation easier for your customers, and therefore makes your product easier to buy.

## What We Need From You

- A 15-minute intro call about your product, customers, roles and data
- Access to your repository, database, hosting and integrations
- Any privacy, legal or AI Act advice you have received
- Decisions on roles, retention periods and AI use
- A pilot customer willing to test roles and permissions

## Price and Timeline

| Scope | Typical product | Indicative price | Duration |
| --- | --- | --- | --- |
| Focused HR tool | Leave, scheduling or onboarding, few roles, no integrations | €2,500-€3,500 | 1-2 weeks |
| Recruitment or HR SaaS | Multiple roles, documents, retention, consent, audit logging | €3,500-€5,500 | 2-3 weeks |
| HR platform with AI and integrations | Payroll or HRIS integrations, AI features, SSO, extensive documentation | €5,500-€7,500 | 3-4 weeks |

HR projects are usually delivered within Launch & Grow, with ongoing care at €49 per month. Simple internal tools may fit within Launch Ready (€800-€3,500). The quote is fixed after an assessment. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Not Included

We do not provide legal advice on employment law, privacy law or the AI Act, prepare conformity assessments for high-risk AI systems or act as a data protection officer. We implement and document the technical measures your advisers recommend. Integrations with specific payroll or HR systems are scoped separately when they require partner approval or extensive mapping.

## Selling to Employers

Employers, especially those with HR departments, ask detailed questions: where data is hosted, who can see salaries, how long applicant data is kept, how sick leave is handled, whether AI is used in decisions and how they can respond to employee data requests. A clear security and privacy overview answering these questions, together with role descriptions, shortens the sales cycle considerably and reassures both HR managers and works councils.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building software for organisations with strict data requirements, such as Vodafone and TNO. Manifera's CEO, Herre Roelevink, co-founded the cybersecurity company CyberDevOps, now CFLW Cyber Strategies. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. Our engineers work with test data on staging wherever possible, and hosting stays in the EU regions you choose.

## Real example

### An AI-Native Founder in Action: The Talent Pool That Never Forgot

Bart Lammers runs a recruitment agency for technical staff in Hengelo and built Vakkrachtpool with Bolt and Supabase, a recruitment SaaS that he also started selling to installation companies hiring their own technicians. It handled vacancies, applications, interview notes and an AI feature that ranked candidates by fit. An employer with 300 staff wanted to adopt it, but its HR manager and privacy officer asked how long candidate data was kept, who could see interview notes and how the ranking worked.

The assessment found around 9,000 candidate records going back three years, without consent for long-term storage. Every user at a customer could see all candidates and interview notes, including hiring managers for unrelated vacancies. CVs were in a public bucket. The AI ranking sent full CVs, including dates of birth and photos, to a model provider and automatically moved low-ranked candidates to "rejected".

LaunchStudio quoted €5,900 within Launch & Grow. Roles were defined for recruiters, hiring managers and HR admins, enforced through Row Level Security, so hiring managers saw only candidates for their own vacancies. CVs moved to private storage. A retention job anonymised candidates a configurable number of weeks after their procedure ended, with an opt-in for the talent pool that recorded consent and expired after a year. Bart's lawyer advised on the periods, and the existing backlog was cleaned up accordingly. The AI feature was changed to produce suggestions only, with recruiters making every decision, sensitive attributes such as photos and dates of birth were removed before sending, and each suggestion was logged with the recruiter's final choice. MFA, audit logging and documentation for the processing agreement completed the work.

**Result:** The employer adopted Vakkrachtpool after its privacy officer reviewed the documentation and its works council received a description of the AI feature. Bart now uses the same documentation in every sale to employers.

> *"My database remembered every candidate for three years and my AI rejected people on its own. Now candidates are forgotten when they should be, and every decision has a person behind it."*
> - **Bart Lammers, Founder, Vakkrachtpool (Hengelo)**

**Cost & Timeline:** €5,900 (Launch & Grow package: roles, private storage, retention and consent, backlog clean-up, AI oversight and minimisation, MFA, audit logging and documentation, plus €49 per month) - completed in 15 business days.

## Frequently Asked Questions

### How long may an HR SaaS keep applicant data?

Dutch privacy guidance generally expects applicant data to be deleted within a few weeks after the procedure ends, unless the candidate consents to longer storage, often up to about a year. Check current guidance and your legal adviser's view, and build configurable retention into your product.

### Is AI candidate screening allowed?

It can be, but AI used to screen, filter or evaluate candidates is classified as high-risk under the EU AI Act, with significant obligations for providers and deployers. Keep humans in control of decisions, document the system and get legal advice before launching such features.

### What does it cost to make an HR SaaS production ready?

Technical production work typically costs €2,500 to €7,500 within Launch & Grow, depending on roles, documents, retention, integrations and AI features. Legal advice is separate. You receive a fixed quote after an assessment.

### How does Manifera's experience help with HR software?

Manifera has built software for organisations with strict data requirements for 11+ years across 160+ projects with 120+ engineers, and its CEO co-founded a cybersecurity company. LaunchStudio applies that experience to roles, sensitive data and documentation for HR products.

### Does privacy compliance help SEO and AI visibility for HR tools?

Yes, indirectly. HR managers and privacy officers search for information about how HR tools handle employee and candidate data. Clear public pages on privacy, retention and AI use help search engines and AI answer engines describe your product accurately when employers compare tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long may an HR SaaS keep applicant data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally a few weeks after the procedure unless the candidate consents to longer, often up to about a year; confirm with current guidance." }
    },
    {
      "@type": "Question",
      "name": "Is AI candidate screening allowed?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can be, but it is high-risk under the EU AI Act; keep humans in control and get legal advice." }
    },
    {
      "@type": "Question",
      "name": "What does it cost to make an HR SaaS production ready?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically €2,500-€7,500 within Launch & Grow for technical work." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with HR software?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years with strict data requirements, and its CEO co-founded a cybersecurity company." }
    },
    {
      "@type": "Question",
      "name": "Does privacy compliance help SEO and AI visibility for HR tools?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes indirectly, through clear public information on privacy, retention and AI." }
    }
  ]
}
</script>
