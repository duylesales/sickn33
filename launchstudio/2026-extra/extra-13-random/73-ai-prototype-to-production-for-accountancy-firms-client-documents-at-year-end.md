---
Title: "AI Prototype to Production for Accountancy Firms: Client Documents at Year-End"
Keywords: ai prototype to production, accountancy client portal, document upload security, year-end peak, lovable accounting app, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# AI Prototype to Production for Accountancy Firms: Client Documents at Year-End

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Prototype to Production for Accountancy Firms: Client Documents at Year-End",
  "description": "Small accountancy firms and their founders build client document portals with AI tools. This decision guide covers what moving that AI prototype to production requires: BSN and financial data, per-client access, upload handling, the tax-season peak, retention obligations and authorisations.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-12",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-prototype-to-production-for-accountancy-firms-client-documents-at-year-end" }
}
</script>

Every spring, small accountancy firms go through the same scramble: hundreds of clients sending annual statements, mortgage overviews, pension letters and receipts by email, WhatsApp and the occasional shoebox. A client portal that collects everything in one place is an obvious improvement, and accountants and their developers now build one in Lovable within weeks. Moving that AI prototype to production, though, means handling some of the most sensitive documents a household owns — during the busiest weeks of the year.

## Decision 1: What Is in These Documents?

Tax documents contain citizen service numbers (BSN), income, bank balances, mortgage and pension details, health costs for deductions and sometimes information about children and partners. The BSN may only be processed where the law allows, and financial and health-related data demand strong protection. Decide what the portal needs to store and what it can pass straight into the firm's accounting software.

## Decision 2: Who Sees Which Client?

A firm has partners, accountants, assistants and sometimes seasonal staff. Clients may be households with two partners, or entrepreneurs with several companies. Each client should see only their own requests and documents; each staff member only the clients assigned to them or their team. Enforce this in the database. AI-built portals commonly let any logged-in client fetch documents by ID, and any staff member see everything.

## Decision 3: How Are Uploads Handled?

Uploads are the heart of the portal and its biggest risk:

- **Private storage** with short-lived signed links; never public URLs.
- **Virus scanning** on upload — clients send files from all kinds of devices.
- **Size and type limits,** with support for phone photos (including HEIC) and multi-page PDFs.
- **Deduplication and naming** so staff can find documents quickly.
- **Download logging** for accountability.

## Decision 4: Can Your AI Prototype to Production Survive Tax Season?

The Dutch income tax filing period concentrates activity into March, April and May, with further peaks around deadlines. Hundreds of clients uploading large files at once stress storage, database connections and upload handling. Background processing for scanning and thumbnails, resumable uploads for mobile users and a load test before March avoid the worst surprises.

## Decision 5: How Long Must You Keep Documents?

Firms have retention obligations for records they rely on, typically seven years for tax-related administration in the Netherlands, while GDPR requires deleting personal data once it is no longer needed. Define retention per document type, automate it, and make sure clients who leave get their documents back before deletion.

## Decision 6: Authorisations and Signatures

Accountants often need authorisation to file on a client's behalf and approval of the final return. The portal can manage approval requests, but approvals must be recorded with a fixed version of the document and a server timestamp, so that "I never agreed to this" can be answered.

## Decision 7: Strong Login and Communication

For portals holding BSNs and financial data, multi-factor authentication is a sensible default. Notifications should say "a document is waiting for you in the portal", never attach the document to an email.

## A Document Workflow That Fits Tax Season

Taking an accountancy AI prototype to production means designing the workflow around how firms actually work in spring:

1. **Checklist generation:** based on last year's return and the client's situation, the portal generates a list of requested documents (annual income statements, mortgage statements, pension overviews, health cost receipts, gift receipts).
2. **Upload per item:** clients upload against specific checklist items, so staff know what each file is.
3. **Automated checks:** file type, size, readability, duplicates and whether the document seems to match the requested year.
4. **Staff review:** accountants mark items as accepted, rejected with a reason, or needing clarification.
5. **Questions and answers:** structured questions (did you move house? did you have children?) stored with the return.
6. **Draft return approval:** the client reviews a frozen PDF and approves it with a timestamped record.
7. **Filing and archive:** filed documents are archived with retention rules.

Each step has a status visible to both client and firm, which removes most "did you receive my documents?" emails.

## Handling the BSN and Other Identifiers

Tax documents contain the citizen service number (BSN) almost everywhere. Accountancy firms may process it for tax purposes, but the portal should limit exposure: avoid showing the BSN in lists and search results, never include it in email notifications or file names, restrict who can view full documents, and log access. When documents are shared with other parties — for example a mortgage adviser at the client's request — record the authorisation and the transfer.

## Upload Pipeline Engineering

A robust upload pipeline for tax documents:

| Stage | What happens | Why |
| --- | --- | --- |
| Direct-to-storage upload | Client uploads to private storage via short-lived signed URL | Fast, resumable, no server bottleneck |
| Virus scan | File scanned before becoming visible | Protects staff machines |
| Type and size validation | Real content type checked; limits enforced | Blocks disguised or oversized files |
| Conversion | HEIC photos converted; thumbnails generated | Staff can view everything consistently |
| Metadata stripping | Location and device data removed from photos | Privacy |
| Deduplication | Hash compared with existing files | Avoids double processing |
| Classification (optional) | Document type suggested, confirmed by staff | Speeds up review |

Processing happens in background jobs, so uploads stay fast even at peak times.

## Peak Capacity Planning

Tax season is predictable. In February, prepare: estimate uploads per day from last year's numbers, load-test uploads and staff review screens at three times that level, confirm storage and email quotas, ensure database connection pooling, set up monitoring dashboards for upload failures and queue backlogs and schedule no major releases during the busiest weeks. Communicate with clients about deadlines and send reminders in waves rather than all at once, to smooth the peak.

## Retention Rules per Document Type

Retention in accountancy is layered: the firm's working papers and filed returns are kept for legally required periods, while supporting documents uploaded by clients may not all need the same retention. Define rules per document type with the firm, apply them automatically after the relevant tax year is closed, and record deletions. Offer clients an export of their documents before deletion. Clear retention reduces risk: the fewer old documents stored, the smaller the impact of any incident.

## Secure Communication With Clients

Clients often reply by email with attachments, undoing the portal's security. Make the portal the easiest channel: reminders with direct links to the right checklist item, mobile-friendly upload, and clear messages that documents should not be emailed. When clients do email documents, staff can upload them into the portal and delete the email copies according to policy.

## Multi-Firm Platforms and White-Labelling

When one portal serves several accountancy firms, each firm expects its own branding, client base and staff — and absolute separation. Enforce firm-level tenancy in the database and storage paths, allow per-firm configuration (checklists, email templates, retention), and give each firm its own processing agreement. A firm's clients should never see another firm's name, and a firm's staff should never see another firm's clients.

## Preparing Documentation for Firms

Accountancy firms will ask about hosting location, sub-processors, encryption, access control, MFA, logging, backups, incident procedures and retention. Prepare a concise security and privacy overview and a standard processing agreement. Firms often have professional obligations regarding confidentiality; showing that the portal supports them strengthens the sale considerably.

## Approvals That Hold Up

The client's approval of a tax return or annual accounts is an important record. Implement it like a signature: freeze the document as a PDF, compute a hash, send a secure link to the client, require login (ideally with a second factor), record the approval with the document version, timestamp and account, and lock the document. If changes are needed after approval, create a new version and request a new approval. Store the approval record with the filed return for the retention period.

## Year-Over-Year Continuity

Accountancy relationships last years. The portal becomes more valuable when it carries context forward: last year's checklist as the starting point for this year's, recurring documents pre-listed, notes about the client's situation visible to the accountant. Design data structures around tax years and client households, so historic information remains organised and accessible — and so retention rules can be applied per year cleanly.

## Security Controls Worth Prioritising

For a portal full of financial documents and identifiers, prioritise: MFA for all staff and as a default for clients; firm and client separation enforced in the database; private storage with short-lived links; download logging; alerts on unusual access such as bulk downloads; encryption at rest; tested backups; and a written incident procedure including notification assessment. These controls protect clients and support the firm's professional duty of confidentiality.

## Common Pitfalls in AI-Built Accountancy Portals

Recurring issues include public storage buckets, sequential document IDs in URLs, uploads that fail on mobile data, staff with access to every client, approvals stored as editable checkboxes, email notifications containing personal details and no retention at all. Each is fixable in days; together they represent most of the risk in a typical AI-built portal.

## A Pre-Season Checklist

Before the next tax season: private storage with scanning and metadata stripping; resumable uploads tested on mobile; client and team access enforced; MFA active; approvals frozen and logged; retention rules configured; load test passed at three times last year's peak; monitoring for upload failures; client communications scheduled in waves. With these in place, the firm can focus on the returns rather than on the portal.

## Why Clients Stay With Digital Firms

Clients who experience a smooth portal — a clear checklist, uploads that work from the kitchen table, status updates without chasing and an easy approval — tend to stay with their accountant for years and recommend the firm to friends and family. For small firms competing with larger practices and online filing services, a secure, reliable portal is one of the most visible signs of professionalism. It turns the most stressful weeks of the year into a predictable process for both client and accountant, and it demonstrates care for the confidential information clients entrust to the firm.

## First Step

Open one uploaded document's link in a private browser window. If it loads without logging in, move documents to private storage first.

## Where LaunchStudio Fits

LaunchStudio takes accountancy portals built with AI to production: per-client and per-team access in the database, secure upload pipelines with scanning and private storage, peak-ready performance, retention automation, logged approvals, MFA and EU hosting. The interface your clients already use stays the same.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience and clients including Statler BI in business intelligence, with engineers in Ho Chi Minh City and offices in Amsterdam and Singapore. See [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/); the [Belastingdienst](https://www.belastingdienst.nl/) publishes the filing periods and record-keeping rules that shape your peaks and retention.

[Describe your project](https://launchstudio.eu/en/#contact) before the next tax season.

## Real example

### An AI-Native Founder in Action: A Document Portal in the Middle of Tax Season

Jolanda Smeets, who runs a small accountancy practice in Venray, built Aangiftebox in Lovable: clients receive a checklist of documents needed for their tax return, upload them from their phones, answer a few questions and approve the final return. She then offered it to four other small firms in North Limburg, covering about 2,100 households.

The first April was rough. Uploads failed for clients on mobile data, and many sent photos again, creating duplicates. On the busiest evening the portal became unresponsive for an hour. Worse, a client noticed she could open another household's annual income statement by changing a number in the download URL. Documents — including BSNs on nearly every page — sat in a public storage bucket. Staff at all five firms could see all clients, approvals were a checkbox that could be ticked again after edits, and nothing was ever deleted.

Over twelve business days, LaunchStudio's engineers moved documents to private storage with signed links and malware scanning, implemented resumable uploads and duplicate detection, enforced firm, team and client separation with row-level security, added MFA for staff and as a default for clients, recorded approvals against a frozen PDF with server timestamps, set up retention rules per document type, and added connection pooling and background processing ahead of a load test at three times the April peak. The exposed documents were assessed with Jolanda, who notified the affected household and the regulator on advice.

**Result:** The next tax season ran without outages, uploads from mobile phones completed reliably and no cross-client access was possible. Aangiftebox added six more firms, several of which cited the security description in their decision.

> *"My clients hand me their whole financial life once a year. The portal had to be at least as careful as the shoebox — and it wasn't."*
> — **Jolanda Smeets, Founder, Aangiftebox (Venray)**

**Cost & Timeline:** €3,400 (Launch & Grow package: document security, uploads, access control, approvals, retention and peak readiness) — completed in 12 business days, plus €49/month managed hosting.

## Frequently Asked Questions

### Can an accountancy portal store documents containing a BSN?

Accountancy firms process BSNs where the law allows for tax purposes, but such documents need strong protection: private storage, restricted access, logging and defined retention.

### How long should an accountancy portal keep client documents?

Tax-related administration is typically kept for seven years in the Netherlands, while other personal data should be deleted once no longer needed. Automate retention per document type.

### Should documents be sent to clients as email attachments?

No. Notify clients by email that a document is waiting in the portal, and deliver it through authenticated, logged access.

### How does Manifera's data experience help accountancy portals?

Manifera has built data-heavy business systems for clients such as Statler BI, which translates into careful handling of sensitive financial documents and peak processing loads.

### Can a secure client portal help an accountancy firm get found online?

Yes. Firms that explain their secure digital process attract clients searching for modern accountants, and AI assistants cite clear, specific service pages when recommending local firms.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Can an accountancy portal store documents containing a BSN?", "acceptedAnswer": { "@type": "Answer", "text": "Where the law allows for tax purposes, with private storage, restricted access, logging and defined retention." } },
    { "@type": "Question", "name": "How long should an accountancy portal keep client documents?", "acceptedAnswer": { "@type": "Answer", "text": "Tax administration typically seven years in the Netherlands; other personal data only as long as needed." } },
    { "@type": "Question", "name": "Should documents be sent to clients as email attachments?", "acceptedAnswer": { "@type": "Answer", "text": "No; notify by email and deliver through authenticated, logged portal access." } },
    { "@type": "Question", "name": "How does Manifera's data experience help accountancy portals?", "acceptedAnswer": { "@type": "Answer", "text": "Data-heavy systems for clients such as Statler BI inform careful document handling and peak processing." } },
    { "@type": "Question", "name": "Can a secure client portal help an accountancy firm get found online?", "acceptedAnswer": { "@type": "Answer", "text": "Yes; clear pages on secure digital processes attract clients and are cited by AI assistants." } }
  ]
}
</script>
