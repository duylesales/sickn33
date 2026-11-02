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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app" }
}
</script>

**Short answer:** generate official documents such as invoices on the server, not in the browser; store each issued PDF once in a private storage bucket together with an immutable record of its data; serve it to the right users through signed links; and never regenerate an issued invoice from current data. For quotes and other non-official documents, browser generation can be acceptable, but server generation is still more consistent.

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
