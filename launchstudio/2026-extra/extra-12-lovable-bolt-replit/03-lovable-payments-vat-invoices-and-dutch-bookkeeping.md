---
Title: "Lovable Payments: VAT, Invoices and What Dutch Bookkeeping Needs"
Keywords: lovable payments, BTW, VAT invoices, OSS, reverse charge, Dutch bookkeeping, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Payments: VAT, Invoices and What Dutch Bookkeeping Needs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: VAT, Invoices and What Dutch Bookkeeping Needs",
  "description": "What a Lovable app must produce so a Dutch accountant can file: compliant invoice fields, the VAT rate question for EU customers, reverse charge, OSS thresholds and sequential numbering.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-vat-invoices-and-dutch-bookkeeping" }
}
</script>

The first quarter is the one that teaches this. You built a product, people paid for it, and then your bookkeeper asked for the invoices — and what your app could produce was a list of Stripe payments with email addresses attached.

No invoice numbers. No company names. No VAT treatment. No way to tell which of those payments went to a business in Germany that should not have been charged Dutch BTW at all. What followed was a weekend of spreadsheets and a bill from the accountant for cleaning up after software you own.

This is one of the few parts of a small product where the requirements are written down precisely by someone else, which makes it unusually easy to get right — if you know what they are before you launch rather than after.

## What Belongs on the Invoice

A Dutch-compliant invoice is a defined list of fields, not a design opinion. Every one your app issues needs: a sequential invoice number with no gaps, the issue date, your company's full name, address and KvK number, your BTW-identificatienummer, the customer's name and address, a description of what was supplied, the amount excluding VAT, the VAT rate and amount, and the total.

Two of those trip up AI-generated code specifically.

**Sequential with no gaps.** An invoice number derived from a database ID will develop gaps every time a payment fails or a row is rolled back, and a gap is exactly what an inspection asks about. Invoice numbers need their own counter that increments only when an invoice is actually issued.

**Unchangeable once issued.** An invoice is a record of what happened, not a view of current data. If your app renders invoices from live customer records, then a customer changing their company address next year silently rewrites last year's accounting. Store the invoice as a snapshot of the values at issue time, and correct mistakes with a credit note rather than an edit.

For business customers you also need their VAT number, because whether you charge VAT at all depends on it.

## The Rate Question, Answered Practically

Founders expect this to be complicated. For most small products it comes down to three cases.

**Dutch customers, consumer or business:** charge Dutch BTW, normally 21 percent for software and digital services.

**Business customers elsewhere in the EU with a valid VAT number:** reverse charge. You charge no VAT and the invoice must state that the VAT is reverse-charged — *btw verlegd* — along with the customer's VAT number. Validating that number is your responsibility, not theirs, and there is a European service for exactly this. An unvalidated number that turns out to be wrong leaves the VAT owed by you.

**Consumers elsewhere in the EU:** you charge the VAT rate of the customer's own country, and report it through the One Stop Shop. There is an annual EU-wide threshold below which you may instead keep charging Dutch VAT, which most first-year products stay under — but "we stayed under it" is a thing you should be able to prove from your own records, which means recording the customer's country and the amount from the first sale.

Customers outside the EU are generally out of scope for EU VAT, with their own rules if you sell at scale into particular countries.

Stripe Tax and comparable services will calculate all of this for you, and for a product selling across borders they are worth their fee. What they will not do is store the result in your database in a form your accountant can use, which remains your application's job.

## Evidence Is Part of the Requirement

For consumer sales inside the EU you are expected to be able to evidence where the customer was — typically two non-contradictory pieces, such as billing address and the country of the payment instrument or IP address.

This sounds bureaucratic until you realise it must be captured at the moment of sale, because it cannot be reconstructed later. A product that records only an email address has no way back to that evidence.

So the checkout needs to ask for a country and a company name, and your application needs to store what it observed at the time: the billing details given, the country the payment method came from, and the VAT number if one was supplied and the result of validating it.

## What Your Accountant Actually Wants

Ask, and the answer is usually modest: a monthly or quarterly export, one row per invoice, with date, invoice number, customer name and country, net amount, VAT rate, VAT amount, gross amount, VAT treatment, and a reference to the payment.

That export is a small feature and it changes the relationship entirely, because everything else — the quarterly BTW return, the OSS declaration, the annual accounts — is derived from it. Products that cannot produce it end up with a bookkeeper manually transcribing payment provider dashboards, which is billable, error-prone, and entirely avoidable.

Build the export before the first quarter closes, not during it.

## Credit Notes, Refunds and Corrections

A refund is not an invoice deleted. It is a credit note: its own sequentially numbered document, referencing the original invoice, with its own VAT treatment, dated when the refund happened.

The same applies to mistakes. If you issued an invoice with the wrong company name or the wrong rate, you do not edit it — you credit it and issue a corrected one. Applications that let a support action quietly modify an issued invoice create exactly the kind of inconsistency between the accounting and the bank that takes days to unwind.

## What Changes When You Sell Through an App Store

One case genuinely changes the picture, and founders meet it late: selling a subscription inside an iOS or Android app.

Purchases made through the store are handled by Apple or Google, who act as the merchant for the transaction in most territories. They collect, they handle the consumer VAT, and they pay you a balance with their commission removed. Your app is no longer issuing those invoices, and attempting to issue your own for the same transaction produces double-counted revenue in your accounts.

This creates a split you have to model deliberately if you sell on the web and in an app: web subscriptions are your own sale, with your own invoice and your own VAT treatment; store subscriptions are a payout you receive, reconciled monthly against the store's report. Two revenue streams, two accounting treatments, one product.

The practical consequences are worth knowing before you build. Your database still needs to know the entitlement — whether a customer has an active subscription and where it came from — so a single subscription record with a source field is far easier than two parallel systems. Refunds issued by the store happen without your involvement and you find out from a notification, so your entitlement logic has to react to that. And a customer who subscribes in the app and then asks you to cancel has to be sent to the store, because you cannot do it for them.

If you are selling on the web today and considering an app later, the thing to get right now is simply that entitlement lives in your own database as a first-class record rather than being read from Stripe — because that is the design that will still work when half your revenue arrives from somewhere else entirely.

## Setting This Up

For a product already taking money, invoicing typically takes three to four days: a dedicated invoice sequence, invoices stored as immutable snapshots with every required field, VAT determination covering Dutch, EU business reverse charge and EU consumer rates, VAT number validation against the European service with the result recorded, location evidence captured at checkout, PDF generation and delivery with copies retained, credit notes for refunds and corrections, and a bookkeeping export in the format your accountant asked for.

LaunchStudio does this as part of production readiness for products selling in the Netherlands and the EU. The engineering comes from Manifera, eleven years and 160+ projects across Amsterdam, Singapore and Ho Chi Minh City — invoicing for European businesses is long-solved ground for the team.

[Show us one of your current invoices](https://launchstudio.eu/en/#contact) and we will tell you which fields are missing, or work out the cost with the [price calculator](https://launchstudio.eu/en/).

## Real example

### A Quarter Reconstructed From a Spreadsheet

Tijmen Verhagen sells Keurmerkbeheer, a Lovable-built tool that certification bodies use to manage audits of installation companies. Customers are businesses: 140 of them, across the Netherlands, Belgium and Germany, at €65 per month.

His app took payments correctly and issued nothing. Customers who wanted an invoice emailed him and he made one in a word processor, numbering them by hand. By the end of the first quarter he had issued 61 manual invoices with three duplicate numbers, and had charged 21 percent Dutch BTW to every customer — including nineteen German and Belgian businesses that had given him their VAT numbers and should have been invoiced under reverse charge.

His accountant's estimate for cleaning up the quarter was more than the software would cost to fix.

Six business days: an invoice sequence separate from database IDs; invoices stored as immutable snapshots carrying company name, address, KvK, both VAT numbers and line detail; VAT determination by customer type and country, with reverse charge applied and stated on EU business invoices; VAT number validation against the European service, with the validation result and timestamp stored against the customer; location evidence captured at checkout; automatic PDF issue on payment with a copy in the customer's account; credit notes implemented for the nineteen incorrect invoices and their corrected replacements; and a quarterly CSV export in his accountant's format.

**Result:** the quarter was corrected with credit notes rather than reconstructed by hand, the accountant's quarterly fee dropped by roughly €400 per quarter, and nineteen business customers stopped being charged VAT they were entitled not to pay — which two of them had already noticed and asked about.

> *"I thought invoicing was admin I could do myself until it became a compliance problem I could not. The counter starting at one and never skipping a number is the most boring feature I have ever paid for and the one I would buy first again."*
> — **Tijmen Verhagen, Founder, Keurmerkbeheer (Amersfoort)**

**Cost & Timeline:** €3,100 (invoice sequence and immutable records, VAT determination with reverse charge, VAT validation, location evidence, PDF issue and delivery, credit notes, bookkeeping export) — completed in 6 business days.

## Frequently Asked Questions

### Can I just use my payment provider's invoices?

Sometimes, for simple cases. They will not carry your KvK number by default, will not always handle reverse charge the way your accountant expects, and leave you dependent on their dashboard for records you are required to keep. For anything with business customers, issue your own.

### Do I have to charge VAT to a customer in Germany?

To a business with a valid VAT number, no — it is reverse charged, and the invoice must say so and show their number. To a consumer, you charge German VAT and report it through OSS, unless you are below the EU-wide threshold and have chosen to stay on Dutch VAT.

### Who is responsible if a customer gives a fake VAT number?

You are. Validate every number against the European service at the time of sale and store the result with a timestamp, so you can show what you checked and when.

### Can I edit an invoice after sending it?

No. Issue a credit note referencing the original and then a corrected invoice. Editing issued invoices is the fastest way to make your accounting disagree with your bank statements.

### When should I build this — before or after launch?

Before you take the tenth payment. The work is the same either way, but doing it afterwards adds reconstructing everything that already happened, which is the expensive part.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just use my payment provider's invoices?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For simple consumer cases sometimes. They omit fields like your KvK number, handle reverse charge inconsistently, and leave your legal records in someone else's dashboard."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to charge VAT to a customer in Germany?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not to a business with a valid VAT number — that is reverse charged and must be stated on the invoice. Consumers are charged their own country's rate and reported through OSS unless you are under the threshold."
      }
    },
    {
      "@type": "Question",
      "name": "Who is responsible if a customer supplies a fake VAT number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You are. Validate against the European service at the time of sale and store the result with a timestamp as evidence of what you checked."
      }
    },
    {
      "@type": "Question",
      "name": "Can I edit an invoice after it has been sent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Issue a credit note referencing the original, then a corrected invoice. Editing issued invoices makes accounting and bank records disagree."
      }
    },
    {
      "@type": "Question",
      "name": "Should invoicing be built before or after launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before the tenth payment. The build is identical either way; doing it later adds reconstructing every sale that already happened."
      }
    }
  ]
}
</script>
