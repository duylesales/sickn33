---
Title: "How Do I Generate PDF Invoices and Quotes in My AI-Built App?"
Keywords: generate pdf invoices app, pdf quotes lovable, pdf generation supabase, invoice pdf ai app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Generate PDF Invoices and Quotes in My AI-Built App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Generate PDF Invoices and Quotes in My AI-Built App?",
  "description": "PDF invoices and quotes generated in the browser look fine until they need to be legally correct, consistent and stored. This guide compares PDF generation approaches for Lovable and Bolt apps and explains how to make documents immutable, private and compliant.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-08",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/" },
    { "@type": "CreativeWork", "name": "Supabase: Storage access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "Stripe Billing", "url": "https://docs.stripe.com/billing" }
  ]
}
</script>

**Short answer:** generate official documents such as invoices on the server, not in the browser; store each issued PDF once in a private storage bucket together with an immutable record of its data; serve it to the right users through signed links; and never regenerate an issued invoice from current data. For quotes and other non-official documents, browser generation can be acceptable, but server generation is still more consistent.

## Key Takeaways

- **Official documents such as invoices belong on the server:** generated from trusted data, stored once and never regenerated from current values.
- **Issued invoices are immutable records;** corrections happen through credit notes, not edits or deletions.
- **Dutch invoices must contain specific details,** and bookkeeping records are generally kept for seven years, as the Belastingdienst explains.
- **Store PDFs in private storage and serve them through short-lived signed URLs,** never public buckets with predictable names.
- **Often the simplest compliant route** is letting your payment provider or accounting software issue invoices while your app supplies correct data.

## Browser vs Server Generation

| Approach | Pros | Cons |
| --- | --- | --- |
| Browser (e.g. html-to-PDF libraries) | Quick to build, no server needed | Inconsistent across devices, data computed client-side, easy to tamper |
| Server function with a PDF library | Consistent output, trusted data, can store result | Needs an edge function or backend |
| PDF service or headless browser | Pixel-perfect from HTML templates | Extra cost and dependency, check data location |
| Payment or accounting provider's invoices | Compliant invoices handled for you | Less design control, provider-specific |

For invoices, many founders are best served by letting Stripe, Mollie with an invoicing tool, or accounting software such as Moneybird generate them. Our guide to [BTW and invoices for Dutch SaaS](https://launchstudio.eu/en/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs) explains the requirements.

## If You Generate Invoices Yourself

**1. Issue, then freeze.** When an invoice is issued, store an `invoices` record with all values: customer details, lines, VAT, totals, invoice number and date. Never recompute these later.

**2. Sequential numbers.** Assign numbers in the database inside a transaction, so concurrent invoices cannot get the same number and there are no unexplained gaps.

**3. Generate once on the server.** An edge function or backend renders the PDF from the frozen record and uploads it to private storage.

**4. Serve with signed links.** Users get a short-lived link only if Row Level Security says the invoice is theirs.

**5. Corrections via credit notes.** Never edit or delete an issued invoice. Issue a credit note referencing it.

## Quotes and Proposals

Quotes change more often, and that is fine. Still:

- Generate from server-side prices, so a quote cannot be manipulated
- Store the version the customer accepted, with timestamp
- Add validity dates and terms

## Practical Details

- **Fonts and characters.** Embed fonts that support characters like ë, ö and €.
- **File size.** Compress images and logos; large PDFs cause email delivery problems.
- **Accessibility.** Structured PDFs with real text, not images of text, are searchable and accessible.
- **Retention.** Dutch rules generally require bookkeeping records to be kept for seven years; plan storage accordingly.

## Why Documents Deserve Special Care

Invoices, quotes, contracts and certificates are not just pages; they are records with legal and financial meaning. Once sent, they may be relied on by customers, accountants and tax authorities. That changes how they should be built. A web page can be regenerated freely; an invoice must say exactly what it said when it was issued, years later. AI-generated document features often miss this distinction, regenerating PDFs from current database values every time someone clicks "download".

## Dutch Invoice Requirements in Brief

The Belastingdienst lists what an invoice must contain. Commonly required elements include your company name and address, VAT identification number, a unique sequential invoice number, the invoice date, the customer's name and address, a description of the goods or services, the date or period of supply, amounts excluding VAT, the VAT rate and amount, and the total. For reverse-charged B2B supplies within the EU, the customer's VAT number and a reverse charge statement are required. Your accountant can confirm specifics for your situation.

## Architecture for Reliable Documents

A robust design separates three things:

1. **The record:** a database row capturing every value on the document at the moment of issue, including customer details, line items, VAT and totals.
2. **The rendering:** a server-side function that turns the record into a PDF using a template.
3. **The file:** the generated PDF stored once in private storage, with its path saved on the record.

Downloads read the stored file. If a template changes later, old documents remain as issued; new documents use the new template.

## Choosing a PDF Approach

| Approach | Strengths | Considerations |
| --- | --- | --- |
| PDF library in an edge function | No extra service, full control | Layout work in code |
| HTML template rendered by a headless browser | Design in HTML and CSS | Heavier runtime; may need a separate service |
| Third-party document API | Polished templates, quick start | Another processor; check data location |
| Payment or accounting tool invoices | Compliance handled for you | Less design control |

For invoices, the last option is often best. For quotes, certificates and reports, an edge function or document API gives more flexibility.

## Numbering Without Gaps or Duplicates

Sequential numbering is easy to get wrong under concurrency. Two customers paying at the same moment can receive the same number if numbers are calculated in application code. Assign numbers inside the database, for example with a counter table updated in a transaction or a sequence per invoice series, at the moment of issue. Keep separate series if needed, such as one per year or per entity.

## Access and Privacy

Documents contain personal and financial data. Store them in private buckets with policies tied to ownership, generate signed URLs with short expiry on request and log access for sensitive documents. Include document storage in your retention policy: keep invoices for the legally required period, and delete other documents when no longer needed.

## Accessibility and Usability

Generate PDFs with real text rather than images, so they can be searched, copied and read by screen readers. Use clear structure, adequate font sizes and sufficient contrast. Name files meaningfully, such as `invoice-2028-0142.pdf`, and include the document number in email subjects so customers and accountants can find them easily.

## Quotes: A Different Lifecycle

Quotes are not invoices, and they can change until accepted. Model them with versions: each change creates a new version, the customer accepts a specific version, and the accepted version becomes immutable, with a timestamp and the accepting person recorded. When a quote converts to an order or invoice, copy values from the accepted version rather than recalculating. This prevents the classic dispute where the customer accepted one price and was invoiced another because prices changed in between.

## Sending Documents by Email

Attach PDFs or, better, send a secure link that requires login or uses a short-lived signed URL. Attachments are convenient but persist in inboxes indefinitely and may be forwarded; links let you control access and revoke it if needed. For invoices, many customers' accounting tools expect attachments, so offer both where appropriate. Send from your authenticated domain so documents do not land in spam.

## Credit Notes and Corrections

When an invoice is wrong, issue a credit note that references the original and reverses all or part of it, then issue a corrected invoice if needed. Never delete or edit an issued invoice. Credit notes use their own number series in many setups, and they must contain the same essential details as invoices. Your accounting software or payment provider usually supports credit notes; if you build your own, add them before you need them.

## Testing Document Generation

Test documents with long names, many line items, special characters such as ë and €, different VAT situations and different languages if you serve several markets. Check that totals match the database to the cent, that page breaks do not split important information awkwardly and that downloads work on mobile. Ask your accountant to review a sample before launch.

## Common Mistakes

- Regenerating issued invoices from current prices or customer details
- Calculating invoice numbers in the browser
- Storing documents in public buckets
- Missing VAT numbers or reverse charge statements for EU business customers
- Deleting invoices instead of issuing credit notes

## The Payoff

Correct, immutable, private documents protect you in disputes, satisfy your accountant and tax authority and show customers that your business is run professionally.

## A Practical Plan

1. Decide which documents your app issues and which tool should issue invoices.
2. Create immutable record tables for issued documents.
3. Assign numbers in the database at issue time.
4. Generate PDFs on the server, once, and store them privately.
5. Serve documents through signed URLs after an ownership check.
6. Add credit notes and versioned quotes.
7. Test with your accountant and real edge cases.

## Related Reading

For VAT details and invoice content, see our guide on BTW and invoices for SaaS in the Netherlands; for connecting invoices to your bookkeeping, see our Moneybird integration guide.

## Questions to Ask Your Accountant

Before building or choosing a tool, ask: Which invoice details do you need for my situation? Should I use one numbering series or several? How should credit notes be numbered? Which export format do you prefer each quarter? Do you need copies of all documents or only invoices? Ten minutes with your accountant prevents months of corrections.

## Summary

Issue documents from trusted server-side data, number them in the database, store them once privately, correct them with credit notes and let your accountant review the setup before customers receive their first invoice.

## The Payoff

Correct documents rarely get noticed. Incorrect ones always do, usually at the worst moment: in a customer dispute or a tax review.

## Getting It Built

LaunchStudio builds server-side document generation with immutable records, private storage and signed links, typically two to five days within an engagement. LaunchStudio brings Manifera's enterprise-grade engineering to the founder economy; Manifera has built document and billing systems for clients over 11+ years from Amsterdam and Ho Chi Minh City; see [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/). The [Belastingdienst](https://www.belastingdienst.nl/) publishes the official invoice requirements.

## Real example

### An AI-Native Founder in Action: The Painter's Quotes That Changed After Signing

Erik Boersma runs a painting company in Hengelo with five painters and built Verfofferte in Bolt: painters measure rooms on a tablet, the app calculates paint, hours and price, generates a PDF quote, and customers accept online. Invoices followed from accepted quotes.

Problems appeared after a price increase. Customers who reopened an accepted quote saw the new prices, because the PDF was regenerated from current price tables each time. One invoice showed a different total from the quote the customer had signed, leading to a dispute. Invoice numbers came from a client-side counter and two invoices shared a number. All PDFs were in a public bucket.

LaunchStudio froze accepted quotes and issued invoices as immutable records, moved PDF generation into an edge function that rendered each document once, assigned invoice numbers in a database sequence, moved documents to private storage with signed links, and added credit notes for corrections.

**Result:** Disputes about changing prices stopped, the duplicate invoice was corrected with a credit note, and Erik's accountant accepted the new invoice series without remarks.

> *"The customer signed one price and received another. Both came from my app, and both were 'correct' at the moment they were generated."*
> - **Erik Boersma, Founder, Verfofferte (Hengelo)**

**Cost & Timeline:** €2,150 (Launch Ready package: immutable quotes and invoices, server-side PDFs, numbering, private storage and credit notes) - completed in 7 business days.

## Frequently Asked Questions

### Should I generate PDFs in the browser or on the server?

For official documents like invoices, on the server, from trusted data, stored once. Browser generation is acceptable for informal documents but is less consistent and easier to manipulate.

### Can I regenerate an invoice PDF when needed?

Only from a frozen record of the original data, producing identical content. Never regenerate from current prices, customer details or VAT rates, because an issued invoice must not change.

### How do I store PDFs securely in Supabase?

Use a private storage bucket with policies tied to ownership, and give users short-lived signed URLs. Public buckets with predictable file names expose documents to anyone who guesses a link.

### How does Manifera approach financial documents?

As records, not views. Manifera's 11+ years of billing and document systems mean issued documents are immutable, numbered in the database and corrected only through credit notes.

### Should invoices or quotes be indexed by search engines?

Never. They contain personal and business data. Keep them in private storage, behind authentication, and make sure no public links to them exist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I generate PDFs in the browser or on the server?",
      "acceptedAnswer": { "@type": "Answer", "text": "Server-side from trusted data for official documents like invoices; browser generation only for informal ones." }
    },
    {
      "@type": "Question",
      "name": "Can I regenerate an invoice PDF when needed?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only from a frozen record producing identical content, never from current data." }
    },
    {
      "@type": "Question",
      "name": "How do I store PDFs securely in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Private buckets with ownership policies and short-lived signed URLs." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach financial documents?",
      "acceptedAnswer": { "@type": "Answer", "text": "As immutable records numbered in the database and corrected only by credit notes." }
    },
    {
      "@type": "Question",
      "name": "Should invoices or quotes be indexed by search engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Never; keep them private behind authentication." }
    }
  ]
}
</script>
