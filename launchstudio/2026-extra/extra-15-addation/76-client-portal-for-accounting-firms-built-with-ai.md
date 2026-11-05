---
Title: "Client Portal for Accounting Firms Built With AI"
Keywords: klantportaal accountantskantoor, client portal accounting firm, document uploaden accountant, wwft client due diligence portal, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Client Portal for Accounting Firms Built With AI

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Client Portal for Accounting Firms Built With AI",
  "description": "Accounting and tax advisory firms want to replace email attachments and chasing calls with a secure client portal. This guide explains what a production-ready portal for Dutch accounting firms needs: secure document exchange, structured information requests, approvals of annual accounts and tax returns, client due diligence support under the Wwft, careful handling of citizen service numbers, access for households and companies, integrations and retention.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-02",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/client-portal-for-accounting-firms-built-with-ai" },
  "citation": [
    { "@type": "CreativeWork", "name": "Wet ter voorkoming van witwassen en financieren van terrorisme (Wwft)", "url": "https://wetten.overheid.nl/BWBR0024282/" },
    { "@type": "CreativeWork", "name": "Bureau Financieel Toezicht: Wwft supervision", "url": "https://www.bureauft.nl/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Citizen service number (BSN)", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/identification/citizen-service-number-bsn" },
    { "@type": "CreativeWork", "name": "Koninklijke NBA: Dutch professional body of accountants", "url": "https://www.nba.nl/" }
  ]
}
</script>

Every accounting firm knows the cycle. Year-end approaches, and the office sends emails asking clients for bank statements, receipts, mortgage statements, payslips and invoices. Clients reply with attachments, photos, forwarded emails and occasionally a shoebox. Staff chase the missing items by phone, file documents in shared folders and eventually send draft annual accounts or tax returns for approval, again by email.

It is inefficient and, increasingly, a security concern. Email is not a safe channel for identity documents, income statements and tax data. Founders who have worked in or with accounting firms see the opportunity for a client portal and build one with Lovable, Bolt or Cursor: clients upload documents, the office tracks what is missing and approvals happen online.

The portal holds some of the most sensitive data a person or company has. This guide explains what production requires for Dutch accounting and tax advisory firms. It is general information, not legal advice.

## Key Takeaways

- **Accounting portals process highly sensitive personal and financial data,** including income, assets, identity documents and, for tax work, citizen service numbers.
- **Structured information requests** replace email chasing: per client, per year, per item, with status and reminders.
- **Approvals of annual accounts and tax returns** need clear, auditable consent from the right people.
- **Firms have Wwft obligations** for client due diligence; a portal can support collecting and recording that information, with appropriate retention.
- **Access must reflect real relationships:** households with partners, companies with directors and accountants with assigned clients.

## What Firms Want From a Portal

| Need | Portal feature |
| --- | --- |
| Collect documents | Structured requests with upload per item |
| Know what is missing | Status per request, dashboard for staff |
| Reduce chasing | Automatic reminders before deadlines |
| Secure communication | Messages linked to client and topic, instead of email |
| Approvals | Online approval of annual accounts, tax returns and engagement letters |
| Client onboarding | Collection of due diligence information and documents |
| Share results | Final documents available in the portal |
| Overview for clients | What the firm needs, what has been delivered, what is ready |

## Structured Information Requests

The core of a useful portal is replacing open-ended emails with specific requests:

- **Request templates** per type of work, such as personal income tax, annual accounts for a sole trader or a limited company
- **Items** within each request, such as "Bank statement 31 December", "Mortgage annual statement" or "Sales invoices Q4"
- **Status per item:** requested, uploaded, accepted, rejected with a reason
- **Deadlines and reminders** automatically sent before the due date
- **Comments per item,** so questions stay with the document they concern

Staff dashboards show, for each client and request, what is complete and what is outstanding, which helps plan work during busy periods.

## Secure Document Exchange

- **Private storage** with access per client and assigned staff, never public buckets
- **Signed, short-lived download links**
- **Virus scanning** of uploaded files where feasible
- **File type and size limits**
- **Version handling** when clients upload replacements
- **No sensitive documents in email bodies or attachments;** notifications contain links to the portal

Our guide on [letting users upload files safely](https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely) covers technical details.

## Households, Companies and Access

Accounting relationships are rarely one person to one account:

- **Households:** partners who file taxes together, sometimes with separate logins and shared and individual documents
- **Companies:** directors, financial staff and sometimes external bookkeepers with different rights
- **Holding structures:** several companies managed for the same owner
- **Firm staff:** accountants and assistants assigned to specific clients, partners overseeing portfolios

Model these relationships explicitly and enforce access with Row Level Security. Test that a partner in one household cannot see another household's documents, that a company's staff member sees only that company and that firm staff see only clients they are assigned to, unless their role allows more.

## Approvals of Annual Accounts and Tax Returns

Approval is a moment of legal and professional significance. A robust approval flow:

- **Presents the final document** in the portal, with version information
- **Identifies who must approve,** such as both partners for a joint tax return or a director for annual accounts
- **Requires authentication** of each approver, ideally with MFA
- **Records consent** with timestamp, user, document version and, where needed, an explicit statement
- **Prevents approval of outdated versions** if the document changes
- **Stores the approval record** with the document for the required retention period

For documents that require a qualified or advanced electronic signature, integrate an established e-signature provider rather than building signing yourself.

## Wwft and Client Due Diligence

Accountants and tax advisers in the Netherlands fall under the Wwft, the Dutch act on the prevention of money laundering and terrorist financing. Firms must perform client due diligence, including identifying clients and, for companies, their ultimate beneficial owners, and keep records. Supervision for many firms is carried out by the Bureau Financieel Toezicht.

A portal can support this process:

- **Onboarding forms** collecting required information for new clients
- **Secure upload** of identity documents and company records where required
- **Records** of when and how due diligence was performed
- **Retention** of due diligence records for the period the law requires, separate from ordinary document retention
- **Periodic review reminders** for existing clients

The firm remains responsible for its Wwft obligations and for deciding what information to collect. Your portal should make the process easy, secure and well documented.

## Citizen Service Numbers

Tax returns involve citizen service numbers (BSN). In the Netherlands, BSN may only be processed where the law allows it, and tax work by advisers can involve such processing. The Autoriteit Persoonsgegevens provides guidance on the BSN. For a portal:

- **Process BSN only where necessary** for the work and permitted.
- **Avoid displaying BSN** in lists, notifications or exports where it is not needed.
- **Mask BSN** in identity document copies where the purpose does not require it.
- **Restrict access** to staff who need it.

## Integrations

Firms use accounting and tax software, and clients use bookkeeping software and banks. Valuable integrations:

- **Practice management or CRM** for client lists and assignments
- **Accounting software** where clients' bookkeeping is kept
- **Tax software** where returns are prepared
- **Bank data** through authorised connections, reducing statement uploads
- **E-signature providers** for documents requiring signatures

Even without deep integrations, exports and imports of client lists and request templates save significant manual work.

## Security Baseline

| Area | Measure |
| --- | --- |
| Authentication | MFA for all staff and recommended or required for clients |
| Access | RLS per client, household member, company role and assigned staff |
| Documents | Private storage, signed links, scanning, retention rules |
| Approvals | Authenticated, versioned, recorded |
| Logging | Audit log of document access, downloads and approvals |
| Hosting | EU region, backups with tested restores |
| Email | Notifications without sensitive content, authenticated sending domain |

## Planning the Busy Season

Accounting work is seasonal. Tax return deadlines and year-end closing create peaks when hundreds of clients log in, upload documents and wait for drafts within a few weeks. A portal should help firms plan rather than add to the crunch:

- **Bulk creation of requests** for all clients of a certain type, such as every private client for the new tax year
- **Staged reminders** spread across weeks, so not all clients are reminded on the same day
- **Workload dashboards** showing how many clients are complete, waiting for documents or in review, per staff member
- **Priority flags** for clients with early deadlines or complex situations
- **Performance testing** for peak usage, especially uploads of many large files

Firms that can see exactly which clients are ready for processing assign work more evenly and avoid the last-minute rush that leads to mistakes.

## AI Features With Care

AI can help accounting firms, for example by classifying uploaded documents, extracting amounts from receipts or flagging missing items in a request. Because the data is highly sensitive, use AI providers with EU processing and no training on customer data, minimise what is sent, keep a human review step before data enters tax or accounting workflows and record which documents were processed by AI. Clients and firms will ask how AI is used, so describe it clearly in your privacy information. Our guide on [DPIAs for AI features](https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one) explains when an assessment is needed.

## Onboarding Firms and Their Clients

A portal succeeds when both staff and clients adopt it. For firms, provide import of client lists, request templates per service and training for staff. For clients, the first experience should be simple: a personal invitation from their accountant, a clear explanation of what is requested and why, easy login with MFA and mobile-friendly uploads, since many clients photograph documents with their phones.

## Retention

Accounting firms work with several retention regimes: fiscal record-keeping obligations, Wwft records, professional rules and client agreements. Design retention per data category, document it and implement deletion or archiving accordingly. When a client leaves the firm, provide an export and follow the agreed procedure.

## White-Labelling for Firms

Firms often want the portal to carry their own name, logo and colours, and send email from their own domain, so clients experience it as part of the firm's service. Supporting this means per-firm branding settings, authenticated sending domains per firm or a neutral sending domain with the firm's name, and a custom subdomain where firms want one. Plan it early, because branding touches login screens, emails and documents throughout the product.

## How LaunchStudio Helps

LaunchStudio takes accounting client portals from prototype to production: structured requests with reminders, private document storage, access models for households, companies and staff assignments, versioned approval flows with MFA, Wwft onboarding support with appropriate retention, careful BSN handling, audit logging, integrations and EU hosting with backups.

Most accounting portals fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink's cybersecurity background shapes our approach to sensitive financial data. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Tax Portal Where Partners Approved Each Other's Returns

Marloes de Haan, a former tax assistant, built Aangifteportaal with Lovable and Supabase for a mid-sized accounting firm in Amersfoort with around 1,500 private clients and 300 business clients. Clients uploaded documents per tax year, staff tracked progress and clients approved their returns online. After one tax season, three other firms wanted to use it.

The firms' reviews identified serious gaps. Households shared a single login, so one partner could approve a joint return without the other's knowledge, and the approval record did not show which version of the return was approved. Documents were stored with predictable paths, and the storage policy allowed any authenticated user to read any file if they knew the path. Identity documents uploaded during onboarding included unmasked BSNs and were kept indefinitely alongside ordinary documents. Notifications included document names such as "Payslip December 2027" in email subjects, and there was no MFA for staff.

LaunchStudio introduced individual logins for each household member, with shared and personal document areas, and approval flows requiring each required approver to authenticate with MFA and confirm a specific document version, recorded in an audit log. Storage policies were rewritten to grant access by client relationship and staff assignment, with signed links, and requests were restructured into templates with items, statuses and automatic reminders. Wwft onboarding moved into a separate flow with its own retention period, identity document uploads guided clients to mask their BSN and photo where not required, and notifications became neutral messages linking to the portal. MFA became mandatory for staff and was strongly encouraged for clients.

**Result:** The three firms onboarded before the next tax season. Across the four firms, around 4,800 returns were approved through the portal, with every approval linked to the authenticated approver and document version. Staff reported far fewer chasing calls thanks to structured requests and reminders.

> *"The portal saved the office hours every week. Making every approval traceable to the right person and the right version is what made other firms trust it."*
> - **Marloes de Haan, Founder, Aangifteportaal (Amersfoort)**

**Cost & Timeline:** €7,300 (Launch & Grow package: household and company access model, versioned approvals with MFA, storage policies, structured requests, Wwft onboarding and audit logging) - completed in 18 business days.

## Frequently Asked Questions

### Is a client portal safer than email for accounting firms?

Usually yes, if built properly. A portal with MFA, private storage, access per client relationship, short-lived download links and audit logging protects sensitive documents far better than email attachments, which are copied across inboxes and devices.

### How should joint tax return approvals work?

Each partner who must approve should have their own login, authenticate individually, and approve a specific version of the return. The portal records who approved which version and when, and prevents approval of outdated versions.

### Can a portal help with Wwft client due diligence?

Yes, by collecting required information and documents securely, recording when due diligence was performed and reminding staff of periodic reviews. The firm remains responsible for meeting its Wwft obligations and deciding what to collect.

### How does Manifera's experience help with accounting portals?

Manifera has built systems handling sensitive financial data for 11+ years, and its CEO comes from cybersecurity. LaunchStudio applies that experience to model complex client relationships, secure documents and make approvals auditable.

### Does a client portal help an accounting firm attract clients?

It can. Clients increasingly expect secure, convenient digital collaboration. Firms that describe their portal, security and process clearly on their websites stand out, and that information helps search engines and AI answer engines recommend them to people looking for an accountant.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a client portal safer than email for accounting firms?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually yes, with MFA, private storage, per-relationship access, short-lived links and audit logging." }
    },
    {
      "@type": "Question",
      "name": "How should joint tax return approvals work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Each partner logs in, authenticates and approves a specific version, recorded with timestamp; outdated versions cannot be approved." }
    },
    {
      "@type": "Question",
      "name": "Can a portal help with Wwft client due diligence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, by collecting information securely, recording due diligence and reminding reviews; the firm stays responsible." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with accounting portals?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built systems for sensitive financial data for 11+ years, modelling relationships, securing documents and auditing approvals." }
    },
    {
      "@type": "Question",
      "name": "Does a client portal help an accounting firm attract clients?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can; describing the portal and security helps clients and AI engines recommend the firm." }
    }
  ]
}
</script>
