---
Title: "How We Handle Your Code and Customer Data During a Project"
Keywords: developer access to customer data, data protection during development project, processing agreement developer, least privilege access agency, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# How We Handle Your Code and Customer Data During a Project

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How We Handle Your Code and Customer Data During a Project",
  "description": "An explanation of how LaunchStudio handles founders' code, accounts and customer data during projects on apps built with Lovable, Bolt, v0, Cursor or Claude Code: working in your accounts, least-privilege access, staging with test data, rules for accessing production data, processing agreements, engineers in Ho Chi Minh City, use of AI tools on your code, confidentiality, incident handling and access removal at the end.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-16",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-we-handle-your-code-and-customer-data-during-a-project" },
  "citation": [
    { "@type": "CreativeWork", "name": "EUR-Lex: General Data Protection Regulation (EU) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj" },
    { "@type": "CreativeWork", "name": "European Commission: Standard contractual clauses for international transfers", "url": "https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Verwerkersovereenkomst", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/avg-algemeen/verwerkersovereenkomst" },
    { "@type": "CreativeWork", "name": "OWASP: Principle of least privilege", "url": "https://owasp.org/www-community/Access_Control" }
  ]
}
</script>

When you invite a team to work on your app, you give them access to two valuable things: your code and your customers' data. Founders are right to ask how that access is handled. Who can see what? Where are the engineers? Do they copy the database? Do they paste your code into AI tools? What happens to access afterwards? And what do you tell your own customers when they ask who processes their data?

This page explains how LaunchStudio handles your code, accounts and customer data during a project. It is a description of our standard practice; the specific arrangements for your project are confirmed in the quote and, where personal data is involved, in a processing agreement.

## Key Takeaways

- **We work in your accounts,** with individual access you can see and revoke.
- **Access is limited to what the work needs,** and production data access is the exception.
- **Staging with test data is the default** for development and testing.
- **A processing agreement covers personal data,** including our engineering location outside the EU.
- **Access is removed at the end** unless you continue with ongoing care.

## Working in Your Accounts

We do not move your code to our repository or your data to our servers. Instead, you invite our team members to your accounts, such as GitHub, Supabase, Vercel or your payment provider, with individual logins and roles. That means you can see at any time who has access, change roles and revoke access with one click. When accounts were previously in someone else's name, we help move them into your company's ownership first.

## Least Privilege

Each engineer receives the access needed for their tasks and no more. For example, an engineer working on frontend performance does not need access to your payment provider. Read-only access is used where possible during the review phase. Administrator roles are limited to the people who must change configuration. All access is listed in the account inventory we deliver at handover.

## Staging and Test Data First

Most work happens on a staging environment that mirrors production but contains test data. Where realistic data is needed, for example to test performance or a migration, we prefer generated data or a copy with personal data removed or masked. Staging uses its own keys for payments and email, so tests never charge real cards or email real customers.

## When Production Data Is Accessed

Some tasks require access to production data: reconciling payments, migrating data, investigating a bug that only occurs with real records or restoring a backup. In those cases we agree with you in advance what will be accessed, why and by whom, access only the data needed, avoid downloading personal data to local devices, record the access in the project log and remove temporary copies afterwards. If a task can be done without seeing personal data, for example by working with counts or anonymised extracts, we do it that way.

## Processing Agreements

When we process personal data on your behalf, we act as a processor and sign a processing agreement with you. It describes the categories of data, the purposes, the security measures, the subprocessors involved and how we assist you with data subject requests and incidents. If you are yourself a processor for your customers, our agreement fits into that chain.

## Where Our Engineers Are

LaunchStudio's front office is at Herengracht 420 in Amsterdam. Engineering is done by Manifera's development centre on Pho Quang Street in Ho Chi Minh City, Vietnam, with a hub on Tras Street in Singapore. Your hosting and databases stay where you choose, usually in an EU region; we do not move them. However, remote access to personal data by engineers outside the EU is treated as a transfer under the GDPR and needs appropriate safeguards, typically standard contractual clauses approved by the European Commission, plus technical and organisational measures. We document this in the processing agreement so you can list it accurately in your own subprocessor overview and privacy documentation. Combined with staging-first work and limited production access, the amount of personal data actually accessed from outside the EU is usually small.

## Use of AI Tools on Your Code

Our engineers use AI coding tools in their work, as do most developers today. We use business plans of these tools with terms that do not permit training on your code, and we do not paste customer personal data into AI prompts. Secrets are never shared with AI tools. If you prefer that certain parts of your code or data are not processed with AI tools at all, tell us at the start and we will agree how to handle it.

## Confidentiality

Everyone working on your project is bound by confidentiality obligations. We do not discuss your product, customers or code outside the project team. Case studies or references are only published with your explicit permission, and examples in our public content are anonymised or written with the founder's approval.

## Devices and Accounts on Our Side

Engineers work on company-managed devices with disk encryption, screen locks and up-to-date software. Access to your systems uses individual accounts with multi-factor authentication where your services support it. Shared passwords are not used; where a service only offers a single login, we discuss alternatives with you or use a password manager with access logging.

## Secrets

Secrets such as API keys, database passwords and signing secrets are stored in your environment configuration, not in chat messages, email or documents. If a secret must be shared for setup, we use a secure method and rotate it afterwards where possible. Secrets that were exposed before the project, for example in browser code or repository history, are rotated as part of the work.

## If Something Goes Wrong

If we discover a security incident during the project, such as an exposed key, evidence of unauthorised access or a misconfiguration exposing data, we inform you immediately, help contain it and provide the information you need to assess whether a data breach must be reported to the authority or affected people. If an incident were caused by our own actions, the same applies, and the processing agreement describes our obligations.

## At the End of the Project

When the project ends, we remove our access or reduce it to what is needed for Launch & Grow ongoing care, at your choice, and confirm it in writing. Temporary data copies are deleted. The account inventory shows the final state of access. If you continue with ongoing care, access remains documented and you can review it at any time.

## What You Can Tell Your Customers

Founders often need to explain to their own customers who works on their systems. A typical description is: "Our application is maintained with the support of LaunchStudio, part of Manifera, under a processing agreement. Hosting remains in the EU. Engineers work primarily on test environments and access production data only when necessary, under documented safeguards." We can help adapt this to your subprocessor list and privacy documentation.

## What We Need From You

- Invitations to the relevant accounts with appropriate roles
- Agreement on when production data may be accessed
- Your processing agreement template, or use of ours
- Any restrictions, for example on AI tools or specific data

## Price

These practices are standard in every project:

| Package | Price |
| --- | --- |
| Launch Ready | €800-€3,500 fixed, including 48 hours of post-launch support |
| Launch & Grow | €2,500-€7,500 fixed, plus €49 per month for ongoing care |

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Questions to Ask Any Development Partner

Whether you work with us or someone else, ask: will you work in my accounts? Who will have access, and with which roles? Will you use test data? When would you access production data, and how is that recorded? Where are your engineers, and how are transfers covered? Do you use AI tools on my code, and under which terms? How is access removed at the end? Clear answers protect your customers and your reputation.

## Sensitive Sectors

For apps in healthcare, finance, education, HR or legal services, we agree additional measures at the start: stricter limits on production access, named engineers only, extra logging and sometimes working exclusively with anonymised data. These arrangements are written into the quote and processing agreement, so your customers' expectations, and any sector requirements they pass on to you, are met throughout the project.

## Transparency During the Project

You can see what we do. Changes arrive as pull requests in your repository, configuration changes are listed in updates, and the project log records when production data was accessed and why. If you want, we invite you or your technical adviser to review pull requests before they are merged. That transparency is part of how trust is built, especially for founders who cannot judge every technical detail themselves.

## Data Subject Requests and Your Obligations

As the controller, or as a processor for your own customers, you may receive requests from people who want to see, correct or delete their data. During and after a project, we help you respond: finding where a person's data is stored, exporting it or deleting it across tables, storage and connected services. Many projects include building self-service export and deletion features, which reduce the manual work for each request and make it easier to meet the deadlines that apply.

## Retention of Project Materials

Projects produce materials: notes, screenshots, test results, logs and sometimes temporary data extracts. Project notes and documentation that belong to you are handed over and stored in your systems. Temporary extracts containing personal data are deleted once the task that required them is complete, and we confirm deletion at the end of the project. Internal project records without personal data may be kept for our own administration, as described in the processing agreement.

## Your Right to Review

You can ask at any time for an overview of who has accessed which systems during the project and why. That right is part of the processing agreement and part of how we work.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working with confidential systems and data for clients such as Vodafone and TNO. Manifera's CEO, Herre Roelevink, co-founded the cybersecurity company CyberDevOps, now CFLW Cyber Strategies. We treat your customers' data as carefully as you would want your own to be treated, and we document how we do it.

## Real example

### An AI-Native Founder in Action: The Question From a Hospital

Hanna Brouwer runs a scheduling SaaS for physiotherapy departments from Groningen, built with Lovable and Supabase. A hospital considering her product asked a pointed question in its supplier assessment: who outside her company had access to patient-related data, where they were located and under what agreement? She was about to start a Launch & Grow project with LaunchStudio and wanted to answer accurately.

Before work began, Hanna and LaunchStudio signed a processing agreement that described the data categories, purposes and security measures, listed Manifera's engineering centre in Ho Chi Minh City as a location from which remote access might occur and included the European Commission's standard contractual clauses. The project plan stated that development and testing would use a staging environment with generated data, and that production access was limited to two named engineers for a planned migration step, scheduled with Hanna and logged.

During the project, production data was accessed once, for the migration, with counts and anonymised samples used for verification. At the end, LaunchStudio's access was reduced to what ongoing care required and confirmed in writing, and the account inventory listed every remaining role.

**Result:** Hanna answered the hospital's question with a clear paragraph and attached the relevant parts of the documentation. The hospital's privacy officer accepted the arrangement, and the department started using the product the following quarter.

> *"The hospital did not expect zero access. They expected me to know exactly who had it, where, and why. Now I can tell them in one paragraph."*
> - **Hanna Brouwer, Founder, Fysiorooster (Groningen)**

**Cost & Timeline:** Included in a €4,800 Launch & Grow project, plus €49 per month for ongoing care - processing agreement signed before the start, project completed in 13 business days.

## Frequently Asked Questions

### Will LaunchStudio copy my database?

Not by default. We work on staging with test or masked data. When production data must be accessed, we agree in advance what, why and by whom, access only what is needed and remove temporary copies afterwards.

### Where are LaunchStudio's engineers located?

The front office is in Amsterdam; engineering is done by Manifera's development centre in Ho Chi Minh City, with a hub in Singapore. Your hosting stays in the region you choose. Remote access to personal data from outside the EU is covered by standard contractual clauses and documented in the processing agreement.

### Do you use AI tools on my code?

Yes, our engineers use AI coding tools under business terms that do not allow training on your code. We never paste customer personal data or secrets into prompts. If you prefer restrictions, we agree them at the start.

### How does Manifera's experience support data protection?

Manifera has worked with confidential systems and data for 11+ years across 160+ projects with 120+ engineers, for clients such as Vodafone and TNO, and its CEO co-founded a cybersecurity company. LaunchStudio applies those practices to every project.

### Does careful data handling affect SEO and AI visibility?

Indirectly. A clear, accurate description of how your data is handled, including subprocessors, supports your privacy and security pages, which buyers read and which search engines and AI answer engines use when describing how trustworthy your product is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Will LaunchStudio copy my database?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not by default; staging with test data is used and production access is agreed and minimised." }
    },
    {
      "@type": "Question",
      "name": "Where are LaunchStudio's engineers located?",
      "acceptedAnswer": { "@type": "Answer", "text": "Amsterdam front office, engineering in Ho Chi Minh City, hub in Singapore; transfers covered by SCCs." }
    },
    {
      "@type": "Question",
      "name": "Do you use AI tools on my code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes under business terms without training; no personal data or secrets in prompts." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience support data protection?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years with confidential systems, and its CEO co-founded a cybersecurity company." }
    },
    {
      "@type": "Question",
      "name": "Does careful data handling affect SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, by supporting accurate privacy and security pages." }
    }
  ]
}
</script>
