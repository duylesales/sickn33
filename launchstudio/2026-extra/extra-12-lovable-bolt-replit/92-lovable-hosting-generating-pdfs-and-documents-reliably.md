---
Title: "Lovable Hosting: Generating PDFs and Documents Reliably"
Keywords: lovable pdf generation, invoices PDF, quotes, headless Chromium, document generation, PDF/A, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Generating PDFs and Documents Reliably

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Generating PDFs and Documents Reliably",
  "description": "Invoices, quotes, reports and certificates are what customers forward, print and file. Why browser-generated PDFs fail, the server-side approaches that work, why a sent document must never change, and the security risk hidden in rendering HTML.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-generating-pdfs-and-documents-reliably" }
}
</script>

Most B2B products eventually produce documents. Invoices and credit notes, quotes and order confirmations, inspection reports, certificates, timesheets, contracts. These are the parts of your product that leave it: forwarded to a customer's customer, printed, archived by an accountant, attached to a dispute.

They are also among the least reliable parts of AI-built products. The first PDF feature is usually generated in the browser by taking a screenshot of an HTML page and placing it in a PDF. It looks acceptable on the founder's laptop for a one-page invoice. On a phone, for a twelve-page report, in another browser, or a year later when someone needs to know exactly what was sent, it falls apart.

This article covers why browser-generated PDFs fail, the server-side approaches that work, the property that matters most — a document that was sent must never change — and the details that separate a professional document from one that looks generated.

## Why Browser-Generated PDFs Fail

The common AI-generated pattern renders the document as a hidden HTML element, captures it with `html2canvas`, and inserts the image into a PDF with `jsPDF`. It has five predictable problems.

**The text is an image.** It cannot be selected, searched or copied, accounting software cannot read it, screen readers cannot read it, and it is blurry when zoomed or printed.

**Pagination is a guess.** The screenshot is sliced into A4-sized pieces, cutting through table rows, lines of text and signatures.

**It depends on the device.** Fonts, screen width, pixel density and memory differ. Large documents exhaust memory on phones and fail silently, which is exactly where field staff generate them.

**It is regenerated from current data.** Each download renders the document again from whatever is in the database now — which is the problem described below.

**It cannot run without a person.** A document generated in the browser cannot be created by a scheduled job, attached to an automatic email, or produced in bulk at month end.

Each of these is tolerable for a prototype. Together they mean documents should be generated on the server.

## Three Server-Side Approaches

| Approach | How it works | Strengths | Weaknesses |
|---|---|---|---|
| HTML to PDF with headless Chromium | Render an HTML template in a real browser engine and print it to PDF | Use HTML and CSS you already know; excellent typography; tables and layouts are easy | Chromium is heavy — it does not run in a Supabase edge function; needs a container or a service |
| Programmatic PDF libraries | Build the document in code with a library such as PDFKit, pdf-lib or React-PDF | Lightweight, runs almost anywhere, precise control | Layout is laborious; complex tables and flowing text take real effort |
| A document service | Send data and a template to a hosted API that returns the PDF | Nothing to operate; often handles PDF/A, fonts and scale | A per-document cost; customer data leaves your infrastructure, so it is a subprocessor |

For most products the right choice is HTML to PDF with headless Chromium, run either as a small container on a platform that supports long-running processes — a self-hosted Gotenberg instance is a common choice — or through a hosted rendering service in the EU. Templates are HTML and CSS, which a developer and an AI assistant can both work with, and the output has real, selectable text.

Programmatic libraries suit simple, highly regular documents — a certificate, a label, a one-page receipt — where layout is fixed and you want to avoid running a browser.

Whichever you choose, the rendering does not belong in the request that the user is waiting on. That is the next section.

## Generate Documents as Jobs

Rendering a twenty-page report takes seconds, sometimes tens of seconds, and occasionally fails. Run it in the request and you meet timeouts, double clicks that generate two documents, and failures the user sees as an error page.

The pattern from the background work article in this series applies directly:

1. The action — "send invoice", "finalise report" — creates a `documents` record with status `pending`.
2. A worker picks it up, renders the PDF, stores it, and sets the status to `ready` along with the storage path, size and checksum.
3. The interface shows progress and the result; an email with a link is sent once the document is ready.
4. Failed renders are retried with backoff; after the final failure the record shows an error that someone is alerted to.

```sql
create table documents (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid not null references organisations(id),
  kind text not null,                 -- 'invoice' | 'quote' | 'report'
  source_id uuid not null,            -- the invoice, quote or report
  version int not null default 1,
  template_version text not null,
  status text not null default 'pending',
  storage_path text,
  sha256 text,
  created_at timestamptz not null default now(),
  unique (kind, source_id, version)
);
```

The unique constraint makes generation idempotent: a retry or a double click cannot create a second version 1.

## A Sent Document Must Never Change

This is the property that matters most, and the one browser generation gets wrong by design.

If a quote PDF is rendered from the database every time someone downloads it, then the quote changes whenever the data changes. A price list updated in March alters every quote sent in February. A customer's address corrected today alters last year's invoices. When there is a disagreement about what was offered, nobody can show what was actually sent.

For invoices this is also a legal matter. Dutch bookkeeping obligations require businesses to retain their administration, including issued invoices, for seven years, and an invoice that can be regenerated with different content is not a reliable record. The VAT and invoices article in this series covers the required content; this article covers keeping it fixed.

The rules:

- **Generate once, at the moment the document is issued** — when the invoice is sent, the quote is shared, the report is finalised — and store the file.
- **Serve the stored file** from then on. Never re-render an issued document.
- **Snapshot the data** the document was built from — line items, prices, addresses, VAT rates — in the record itself or in a JSON column, so the document and its data agree forever.
- **Record a checksum.** A SHA-256 hash of the file proves later that it has not been altered.
- **Correct with a new document.** A wrong invoice is followed by a credit note and a new invoice; a revised quote is version 2, with version 1 still available. Nothing is overwritten.

Drafts are the exception: a draft can be rendered on demand as often as needed, clearly marked as a draft, and is never sent.

## Templates That Look Professional

The difference between a document that looks generated and one that looks professional is mostly print CSS.

**A4, not Letter.** Set `@page { size: A4; margin: 20mm 18mm; }`. Defaults from American examples produce documents that print with odd margins on every European printer.

**Control page breaks.** `break-inside: avoid` on table rows, signature blocks and address blocks; `thead { display: table-header-group; }` so column headers repeat on every page of a long table.

**Headers, footers and page numbers.** "Pagina 3 van 7" in the footer, with the company details and the document number on every page. Headless Chromium supports header and footer templates for exactly this.

**Embed fonts.** Bundle the font files with the template rather than relying on what the rendering machine has installed. A missing font silently falls back, and a missing euro sign — "€" rendered as an empty box — is surprisingly common.

**Use the locale.** Amounts as € 1.250,50 and dates as 13 maart 2028 for Dutch documents, as the internationalisation article in this series describes; the document language follows the customer's settings rather than the user's interface language.

**Version the template.** Store the template version on each document. When the design changes, old documents keep their old appearance because they are stored files — and you can still tell which template produced them.

## Archiving and Accessibility

Two standards are worth knowing.

**PDF/A** is the archival profile of PDF: fonts embedded, no external dependencies, no features that may not render in twenty years. Accountants, government bodies and some sectors expect it for records that must be kept. Most rendering services and Chromium-based tools can produce PDF/A-2b with the right settings, or the output can be converted. If you issue invoices or certificates, produce PDF/A.

**Tagged PDF** carries the document structure — headings, tables, reading order — so screen readers can interpret it. The European Accessibility Act article in this series explains when this becomes an obligation; producing documents from semantic HTML through Chromium gets most of the way there, while image-based PDFs never can.

## The Security Risk in Rendering HTML

Rendering HTML on a server introduces a risk that is easy to miss: the template contains data that users typed.

A customer name, an address line or a note containing HTML — `<img src="http://169.254.169.254/latest/meta-data/">` or `<iframe src="file:///etc/passwd">` — is interpreted by the headless browser when the document is rendered. Depending on the setup, the browser on your server fetches internal URLs, reads local files or makes requests to arbitrary sites, and the result may even appear in the PDF. This is server-side request forgery through the document generator, and it has been found in many products.

Four measures close it:

- **Escape all user data** in templates. Use a templating engine that escapes by default, and never insert user content as raw HTML.
- **Disable network access** for the rendering process except to the specific hosts it needs — usually none, if fonts and images are bundled.
- **Disable JavaScript** in templates unless it is required.
- **Run the renderer isolated** — its own container, no credentials, no access to your database or internal network.

Treat the renderer as you would treat any component that processes untrusted input, as the file upload articles in this series describe.

## Storage, Access and Delivery

Generated documents are files, and the storage articles in this series apply in full.

Store them in a private bucket under an organisation-first path — `org/{id}/invoices/{invoice}/v1.pdf` — and serve them through short-lived signed URLs after checking that the user may see that document. Email a link to the document in the product rather than attaching it, except where the recipient genuinely needs the attachment — invoices sent to a customer's accounts payable address are the common exception, and then only the invoice itself.

Remember that documents are personal data when they contain names and addresses. They belong in your retention register, they must be included in full account exports, as the data exports article describes, and they must be deleted when the retention period ends — except where bookkeeping law requires you to keep them, which is a reason to write the retention rule per document type.

## When a PDF Is Not Enough: E-Invoicing

For invoices specifically, a PDF is increasingly only half the answer.

Dutch public bodies — ministries, municipalities, provinces and many semi-public organisations — require suppliers to send e-invoices: structured files in the European standard format, typically UBL following the Dutch NLCIUS profile, delivered through the Peppol network rather than by email. A PDF attached to an email is not accepted by their processing systems. Larger private companies increasingly ask for the same, because a structured invoice goes straight into their accounts payable process without anyone typing it in, and the European move towards mandatory e-invoicing for business-to-business transactions makes this a direction rather than an option.

Three consequences for document generation:

- **Generate the structured file from the same snapshot as the PDF.** The UBL invoice and the PDF must agree to the cent, which they will if both are produced from the stored invoice data rather than from separate queries.
- **Embed or attach the PDF as the human-readable version.** UBL allows the PDF to be included, so the recipient has both.
- **Use an access point for Peppol.** Sending through Peppol requires a certified access point; for a small product this is a service you connect to, often the same one your customers' accounting software already uses, rather than something you build.

If your customers sell to public bodies — care providers, installers, consultancies, training providers frequently do — e-invoicing will be one of the first enterprise requirements they bring to you, and it is far simpler when invoices are already immutable, snapshotted records.

## Bulk and Scheduled Generation

Month end brings the volume problem: four hundred invoices to generate and send at once, or a report per location every Monday.

Queue them as individual document jobs rather than one large job, so a single failure affects one document. Limit concurrency to what the renderer can handle — Chromium uses significant memory per page — and monitor the queue length. A month-end run that takes three hours because it was rendered serially in one process is a common discovery the first time it happens.

Record a batch for bulk runs, with counts of rendered, failed and sent documents, so the person who started it can see that all four hundred actually went out.

## Testing Documents

Documents are easy to break without noticing: a template change shifts a column, a long product name pushes the total onto a new page, a font fails to load.

Three kinds of test help:

- **Text assertions.** Extract the text from a generated PDF and assert that the invoice number, totals, VAT amounts and dates are present and correct.
- **Visual snapshots.** Render a set of representative documents — one line, forty lines, a long customer name, a zero-rated line — to images and compare them with approved snapshots, failing on significant differences.
- **Edge cases.** A document that spans exactly a page boundary, characters such as ë, ß and €, and a user value containing HTML that must appear as literal text.

## Setting This Up

For a Lovable product that issues documents, this is typically three to five days: server-side rendering with headless Chromium in an isolated container or an EU rendering service, generation as background jobs with idempotent document records, retries and alerting, issued documents generated once and stored with a data snapshot, template version and checksum, corrections as new versions or credit notes, print CSS for A4 with controlled page breaks, repeated table headers, page numbers and embedded fonts, locale-aware formatting, PDF/A for records that must be archived, escaped templates with network and JavaScript disabled in the renderer, private storage with signed URLs and links instead of attachments, retention rules per document type, queued bulk generation with batch reporting, and text and visual snapshot tests.

LaunchStudio builds this when documents are the part of the product customers forward to their own customers. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Send us a PDF your product generated](https://launchstudio.eu/en/#contact) and we will tell you how it was made.

## Real example

### A Quote That Changed After It Was Signed

Hidde Brouwer built Offertetool in Lovable: quotes and order confirmations for kitchen and bathroom installers, used by 38 companies whose sales staff work largely on site with customers.

Quotes were generated in the browser with `html2canvas` and `jsPDF`. Multi-page quotes cut table rows in half at page breaks, the text could not be selected, and on phones — where most quotes were produced, in customers' kitchens — quotes longer than three pages failed without an error. Every download rendered the quote again from the current database.

The problem became expensive when an installer updated their price list. A homeowner who had signed a quote in January downloaded it again in April to compare with the invoice and found different prices: the April download had been rendered from the new price list. The difference was €2,300, the homeowner had the April PDF, and the installer had nothing to show what had been sent in January. They honoured the lower price.

Four business days: rendering moved to a headless Chromium container behind a job queue, with document records, retries and alerting; quotes and order confirmations generated once when sent and stored with a snapshot of the line items and prices, the template version and a SHA-256 checksum; revisions issued as new versions with earlier versions retained and visible; print CSS for A4 with repeated table headers, rows that never split, page numbers and the installer's details on every page, and embedded fonts; quotes produced as PDF/A-2b; user content escaped, with network access and JavaScript disabled in the renderer; private storage with signed links; and text and visual snapshot tests covering one-page and forty-page quotes and long product descriptions.

**Result:** forty-page quotes render in around six seconds and work from any phone, because the phone no longer does the work. Every quote sent since can be shown exactly as it was sent, with its checksum. Two installers have since used the stored versions to settle disagreements in their favour within a day.

> *"The customer had a PDF of our quote with prices we never offered. We had generated it ourselves, three months later, from the new price list."*
> — **Hidde Brouwer, Founder, Offertetool (Veenendaal)**

**Cost & Timeline:** €3,900 (server-side rendering with job queue, immutable versioned documents with data snapshots and checksums, A4 print templates with pagination and embedded fonts, PDF/A output, renderer isolation and escaping, signed storage, snapshot test suite) — completed in 4 business days.

## Frequently Asked Questions

### Why are PDFs generated in the browser a problem?

They are usually screenshots: text cannot be selected or read by software, pages split through content, large documents fail on phones, and they cannot be generated by background jobs.

### What is the best way to generate PDFs for a Lovable app?

For most products, HTML templates rendered to PDF by headless Chromium in a container or an EU rendering service, run as a background job. Programmatic libraries suit simple fixed-layout documents.

### Why should an issued document never be regenerated?

Because it would change whenever the underlying data changes, so nobody could prove what was sent. Generate once, store the file with a data snapshot and checksum, and issue corrections as new versions or credit notes.

### Do invoices need to be PDF/A?

Not always by law, but PDF/A is the archival format that guarantees the document still renders years later, and it is what accountants and public bodies expect for records you must keep.

### What is the security risk in HTML-to-PDF rendering?

User data rendered as HTML can make the server-side browser fetch internal URLs or local files. Escape all user content, disable network access and JavaScript in the renderer, and run it isolated.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why are browser-generated PDFs a problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They are usually images: unselectable text, broken pagination, failures on phones for large documents, and no way to generate them in background jobs."
      }
    },
    {
      "@type": "Question",
      "name": "How should a Lovable app generate PDFs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Render HTML templates with headless Chromium in a container or EU service as a background job; use programmatic libraries for simple fixed layouts."
      }
    },
    {
      "@type": "Question",
      "name": "Why must issued invoices and quotes never be regenerated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Regenerated documents change with the data, so nobody can prove what was sent; store the file once with a snapshot and checksum."
      }
    },
    {
      "@type": "Question",
      "name": "Should invoices be stored as PDF/A?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "PDF/A guarantees long-term rendering and is what accountants and public bodies expect for records that must be retained."
      }
    },
    {
      "@type": "Question",
      "name": "What is the security risk of HTML-to-PDF rendering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unescaped user data can make the renderer fetch internal URLs or files; escape content, disable network and JavaScript, and isolate the renderer."
      }
    }
  ]
}
</script>
