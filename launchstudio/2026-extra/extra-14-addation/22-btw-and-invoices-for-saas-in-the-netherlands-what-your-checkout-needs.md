---
Title: "BTW and Invoices for SaaS in the Netherlands: What Your Checkout Needs"
Keywords: btw saas netherlands, vat invoices saas, dutch vat checkout, oss vat digital services, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# BTW and Invoices for SaaS in the Netherlands: What Your Checkout Needs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "BTW and Invoices for SaaS in the Netherlands: What Your Checkout Needs",
  "description": "AI-built checkouts rarely handle Dutch BTW, reverse charge for EU businesses or OSS for EU consumers. This guide explains what a Dutch SaaS checkout and invoice must contain, and how to build it into a Lovable or Bolt app.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-30",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs" },
  "citation": [
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/" },
    { "@type": "CreativeWork", "name": "EU VAT One Stop Shop", "url": "https://vat-one-stop-shop.ec.europa.eu/index_en" },
    { "@type": "CreativeWork", "name": "VIES VAT number validation", "url": "https://ec.europa.eu/taxation_customs/vies/" },
    { "@type": "CreativeWork", "name": "KVK", "url": "https://www.kvk.nl/en/" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" }
  ]
}
</script>

Your first B2B customer pays, and the next morning their bookkeeper emails: "Could you send a proper invoice with your BTW number and ours, and is this reverse charged?" Lovable built you a checkout. It did not build you a VAT-compliant billing system. For a Dutch SaaS, getting BTW and invoices right is part of launching, not an administrative detail for later.

This article explains the rules that affect how your checkout is built. It is not tax advice; confirm your specific situation with an accountant.

## Key Takeaways

- **AI-built checkouts rarely handle Dutch BTW correctly.** VAT treatment depends on whether the customer is a consumer or business and where they are located.
- **EU business customers with a valid VAT number are generally reverse charged;** validate numbers with the EU's VIES service.
- **EU consumers abroad are charged their own country's VAT once you exceed the EU-wide threshold,** declared through the One Stop Shop (OSS).
- **Dutch invoices must contain specific details** such as your KvK and VAT numbers, sequential numbering and VAT breakdown, and records are generally kept for seven years.
- **The simplest compliant route** is usually letting your payment provider or accounting software generate invoices while your app supplies correct customer data.

## The Three Customer Types That Matter

How much BTW you charge depends on who buys and where they are:

| Customer | Where | VAT treatment (general rule) |
| --- | --- | --- |
| Business or consumer | Netherlands | Dutch BTW, standard rate 21% |
| Business with a valid VAT number | Other EU country | Usually reverse charge: no Dutch BTW, invoice states "VAT reverse charged" |
| Consumer | Other EU country | VAT of the customer's country, typically declared through the OSS scheme once above the EU-wide threshold |
| Business or consumer | Outside the EU | Usually no Dutch BTW, rules depend on the country |

For digital services such as SaaS, the customer's location and status decide the treatment. Your checkout therefore needs to know both.

## What Your Checkout Must Collect

- **Country** of the customer
- **Business or consumer** status
- **VAT number** for EU business customers, validated against the EU's VIES service
- **Company name and address** for business invoices
- **Evidence of location** for EU consumers, such as billing address and payment country

AI-generated checkouts usually collect an email and a card. Adding these fields, validating VAT numbers and calculating the right rate is where most of the work lies.

## What a Dutch Invoice Must Contain

The Belastingdienst lists the required elements. In practice, your invoices need:

- Your company name, address, KvK number and BTW identification number
- The customer's name and address, and their VAT number for reverse charge
- A unique, sequential invoice number
- Invoice date and the date or period of the service
- Description of the service
- Amount excluding VAT, VAT rate, VAT amount and total
- For reverse charge: the text "VAT reverse charged" (or "btw verlegd")

Invoices must be stored for seven years. Generating PDFs on the fly from current data is risky: if a customer changes their address, an old invoice must not change with it. Store issued invoices as immutable records.

## Build or Use Your Payment Provider's Tools?

| Option | Pros | Cons |
| --- | --- | --- |
| Stripe Tax and Stripe Invoicing | Automatic rate calculation, VAT ID collection, compliant invoices | Additional fees, Stripe-specific |
| Mollie with an invoicing tool | Dutch provider, local methods | Tax logic and invoices often need extra tooling |
| Accounting software integration (e.g. Moneybird, e-Boekhouden, Exact) | Invoices land directly in your books | Integration work, API limits |
| Custom invoice module | Full control | Most work, easy to get wrong |

For most early-stage Dutch SaaS, the simplest compliant route is to let the payment provider or accounting tool generate invoices, and have your app pass the right customer data.

## Common Mistakes in AI-Built Checkouts

1. **Prices shown including BTW to businesses and excluding it to consumers, inconsistently.** Decide and label clearly.
2. **Reverse charge applied without validating the VAT number.** If the number is invalid, Dutch BTW should have been charged.
3. **Invoice numbers generated from database IDs with gaps.** Sequences should be continuous per series.
4. **Invoices regenerated from live data.** Address or price changes rewrite history.
5. **No credit notes.** Refunds need a credit note referencing the original invoice, not a deleted invoice.

## How the EU VAT Rules for Digital Services Work

SaaS is treated as an electronically supplied service for VAT purposes, and the rules depend on the customer:

- **B2B within the EU:** the place of supply is generally where the business customer is established. With a valid VAT number, the reverse charge mechanism usually applies: you invoice without Dutch BTW and the customer accounts for VAT in their own country.
- **B2C within the EU:** the place of supply is generally where the consumer lives. Below an EU-wide threshold for cross-border distance sales and electronic services, you may charge Dutch VAT; above it, you charge the consumer's local rate and declare it through the One Stop Shop.
- **Outside the EU:** usually no Dutch BTW, but local rules in the customer's country may apply.

The European Commission's OSS portal explains the scheme, and the Belastingdienst publishes Dutch guidance. Your accountant should confirm how these rules apply to your exact situation.

## Validating VAT Numbers

Reverse charge depends on a valid VAT number. The EU's VIES service lets you check whether a number is valid at the time of the transaction. Good practice is to validate at sign-up or checkout, store the validation result and timestamp, and re-validate periodically for recurring customers. If validation fails, charge Dutch BTW until the customer provides a valid number. Payment platforms such as Stripe can perform this validation as part of their tax features.

## Evidence of Customer Location

For consumers, you need evidence of where they are located. Typical evidence includes billing address, the country of the payment method and IP-based location. Collect at least two consistent pieces where required, store them with the transaction and keep them with your records. Payment providers' tax tools often collect and store this automatically.

## Invoice Numbering and Immutability

Two invoicing principles cause the most trouble in AI-built apps:

- **Sequential numbering:** invoices need unique, sequential numbers within a series. Generating them from database IDs or timestamps can create gaps or duplicates. Assign numbers in a database transaction or let your invoicing tool do it.
- **Immutability:** an issued invoice must not change. Store invoice data at the moment of issue, including customer details and prices, rather than regenerating from current data. Corrections happen through credit notes.

## Record Keeping

Dutch businesses generally must keep their administration, including invoices, for seven years, with longer periods for some records. This interacts with the GDPR's storage limitation principle: keep what tax law requires, restrict access to it, and delete other personal data when it is no longer needed. Document both in your retention policy.

## Working With Your Accountant

Before building, spend an hour with your accountant on four questions: which customer types you serve, which countries, whether you will use OSS, and which tool will issue invoices. The answers determine the fields your checkout needs and the integration you build. A quarterly export that matches your accountant's needs then saves hours every quarter.

## Pricing Pages: Showing VAT Clearly

How you display prices shapes both conversion and compliance. Consumers in the EU must see total prices including VAT. Business-focused SaaS commonly shows prices excluding VAT with a clear "excl. BTW" or "excl. VAT" label. If you serve both, let visitors choose between business and personal pricing or show both figures. Make sure the price at checkout matches what the pricing page promised for that customer type; mismatches are a common source of abandoned checkouts and support questions.

## Refunds and Credit Notes

When you refund a customer, do not delete or edit the original invoice. Issue a credit note that references it, with the same VAT treatment, so your records and VAT returns stay consistent. Payment providers' invoicing tools usually support credit notes; if you build your own invoicing, add them before you need them, because the first refund always arrives sooner than expected.

## Testing Your Tax Setup

Before launch, run test purchases as a Dutch consumer, a Dutch business, an EU business with a valid VAT number, an EU business with an invalid number and an EU consumer in another country. Check each invoice for the correct rate, wording and details. Ten minutes of testing prevents a quarter of corrections.

## When Rules Change

VAT thresholds, rates and reporting requirements change over time, and EU-wide reforms affect digital services periodically. Rather than hard-coding rates and rules into your app, rely on your payment provider's or accounting software's tax features where possible, keep rates configurable, and ask your accountant to review your setup once a year. That way a rule change becomes a configuration update rather than a code change.

## Quick Reference

| Customer | Location | Typical VAT on invoice |
| --- | --- | --- |
| Business or consumer | Netherlands | Dutch BTW (21% standard rate) |
| Business with valid VAT number | Other EU country | No Dutch BTW, "VAT reverse charged" |
| Consumer | Other EU country | Consumer's local VAT above the EU threshold, via OSS |
| Business or consumer | Outside the EU | Usually no Dutch BTW; check local rules |

Use this as orientation only and confirm specifics with your accountant.

## How LaunchStudio Helps

Billing work like this typically sits inside a Launch & Grow engagement (€2,500-€7,500 fixed), alongside payments, email and hosting. LaunchStudio's engineers set up VAT ID collection and validation, tax calculation through your payment provider or accounting software, immutable invoice records, credit notes and the data your accountant needs. For the payment side, see our guide to [iDEAL recurring payments with Mollie](https://launchstudio.eu/en/blog/ideal-recurring-payments-for-saas-sepa-direct-debit-with-mollie).

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience and Dutch roots, with client work anchored at Herengracht 420 in Amsterdam. Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) includes financial integrations for Dutch and international clients. For the official rules on invoices and VAT, the [Belastingdienst](https://www.belastingdienst.nl/) is the authoritative source.

## Real example

### An AI-Native Founder in Action: The Photography Booking SaaS With Unusable Invoices

Kevin Bos, a wedding photographer in Dordrecht, built Fotoplan with Bolt: a booking and contract tool for photographers, sold as a monthly subscription. Within four months he had 70 subscribers, including photographers in Belgium and Germany.

His accountant's quarterly review was uncomfortable. Every customer had been charged 21% Dutch BTW, including Belgian and German businesses that should have been reverse charged. The "invoices" were payment receipts without his KvK number, customer addresses or sequential numbers. Two customers had been refunded by deleting their invoices. And a German photographer had asked three times for an invoice with her VAT number on it.

LaunchStudio added business details and VAT ID fields to sign-up with VIES validation, configured Stripe Tax to calculate Dutch BTW, reverse charge and OSS rates, switched to Stripe Invoicing with Kevin's company details and sequential numbering, created credit notes for refunds and built a quarterly export for his accountant. Existing subscribers were asked to complete their details on their next login.

**Result:** From the next quarter, Kevin's accountant filed without manual corrections. Corrections for previous invoices were handled with credit notes and new invoices, and Fotoplan's subscribers outside the Netherlands grew to about a third of the total, with no more invoice complaints.

> *"My app could take money from anywhere in Europe. It just couldn't explain to the tax office what that money was."*
> - **Kevin Bos, Founder, Fotoplan (Dordrecht)**

**Cost & Timeline:** €3,100 (Launch & Grow package: VAT data and validation, Stripe Tax and Invoicing, credit notes and accountant export) - completed in 10 business days, plus €49/month managed hosting.

## Frequently Asked Questions

### Do I need to charge Dutch BTW to EU business customers?

Generally not, if they provide a valid VAT number. For B2B digital services within the EU, the reverse charge mechanism usually applies: you invoice without Dutch BTW and state that VAT is reverse charged. Validate the VAT number through VIES and confirm with your accountant.

### What is the OSS scheme for SaaS?

The One Stop Shop lets EU businesses report VAT on cross-border sales to consumers in other EU countries through one return in their home country. Once your EU-wide cross-border consumer sales exceed the threshold, you charge the consumer's local VAT rate and declare it via OSS.

### Can my payment provider handle BTW calculations for me?

Partly. Stripe Tax calculates rates and collects VAT IDs; other providers and accounting tools offer similar features. You still need to collect the right customer data and ensure invoices contain the required details. The responsibility for correct VAT remains yours.

### Why does a team with Dutch roots matter for billing work?

BTW, KvK numbers, Dutch invoice requirements and accountants' expectations are local details. Manifera's 11+ years with Dutch clients and its Amsterdam base mean these are standard parts of how LaunchStudio sets up billing.

### Do clear pricing and VAT details help with AI search visibility?

Yes. Business buyers often ask AI assistants for tools with transparent pricing "excluding VAT" or that "support reverse charge". Pricing pages that state VAT handling clearly give assistants accurate facts to cite.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need to charge Dutch BTW to EU business customers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally not with a valid VAT number; reverse charge usually applies for B2B digital services in the EU. Validate via VIES and confirm with an accountant." }
    },
    {
      "@type": "Question",
      "name": "What is the OSS scheme for SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "The One Stop Shop lets EU businesses declare VAT on cross-border consumer sales through one home-country return, charging the consumer's local rate above the EU threshold." }
    },
    {
      "@type": "Question",
      "name": "Can my payment provider handle BTW calculations for me?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partly. Tools like Stripe Tax calculate rates and collect VAT IDs, but the founder must collect correct data, issue compliant invoices and remains responsible." }
    },
    {
      "@type": "Question",
      "name": "Why does a team with Dutch roots matter for billing work?",
      "acceptedAnswer": { "@type": "Answer", "text": "BTW, KvK numbers and Dutch invoice rules are local details that Manifera's 11+ years with Dutch clients make standard practice." }
    },
    {
      "@type": "Question",
      "name": "Do clear pricing and VAT details help with AI search visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Pricing pages that state VAT handling clearly give AI assistants accurate facts to cite to business buyers." }
    }
  ]
}
</script>
