---
Title: "Peppol E-Invoicing for SaaS in Belgium and the Netherlands"
Keywords: peppol e-invoicing saas, peppol belgium 2026, e-facturatie peppol, ubl invoice integration, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Peppol E-Invoicing for SaaS in Belgium and the Netherlands

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Peppol E-Invoicing for SaaS in Belgium and the Netherlands",
  "description": "Belgium made structured B2B e-invoicing through Peppol mandatory from 1 January 2026, Dutch public bodies already receive e-invoices and EU rules are moving towards wider e-invoicing. This guide explains what Peppol is, who must comply, what a structured invoice contains, and how an AI-built SaaS can send and receive Peppol invoices through an access point.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-04",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/peppol-e-invoicing-for-saas-in-belgium-and-the-netherlands" },
  "citation": [
    { "@type": "CreativeWork", "name": "OpenPeppol", "url": "https://peppol.org/" },
    { "@type": "CreativeWork", "name": "FPS Finance Belgium: E-invoicing", "url": "https://einvoice.belgium.be/en" },
    { "@type": "CreativeWork", "name": "European Commission: eInvoicing and EN 16931", "url": "https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing" },
    { "@type": "CreativeWork", "name": "Peppol BIS Billing 3.0", "url": "https://docs.peppol.eu/poacc/billing/3.0/" }
  ]
}
</script>

Invoices used to be a solved problem for SaaS founders. Your payment provider or accounting tool generated a PDF, emailed it to the customer and that was the end of it. That model is changing across Europe. Governments want invoices as structured data that systems can read automatically, both to reduce administrative cost and to close VAT gaps. The network that carries those invoices in the Benelux, and in much of Europe, is Peppol.

For a SaaS company invoicing Belgian business customers, the change is already here: since 1 January 2026, Belgian businesses must exchange structured electronic invoices with each other, with Peppol as the default network. Dutch public-sector bodies already expect e-invoices from suppliers, and EU legislation is moving towards structured e-invoicing for cross-border business transactions later this decade.

This guide explains what Peppol is, whether it affects your SaaS and how to support it without rebuilding your billing.

## Key Takeaways

- **Peppol is a network for exchanging structured business documents,** mainly invoices, between companies through certified access points.
- **Belgium requires structured B2B e-invoicing from 1 January 2026,** for VAT-registered businesses established in Belgium, with Peppol as the standard network.
- **The Netherlands has no general B2B mandate yet,** but government bodies receive e-invoices and many large buyers request them.
- **A PDF is not an e-invoice.** A Peppol invoice is structured data, typically UBL XML following the European standard EN 16931 and the Peppol BIS Billing 3.0 specification.
- **Most SaaS companies connect through an access point provider or their accounting software,** rather than joining Peppol directly.

## What Peppol Is

Peppol, originally Pan-European Public Procurement Online, is a set of specifications and a network governed by OpenPeppol, a non-profit association. It works much like email for business documents, with stricter rules:

- Each participating business has a **Peppol ID,** often based on its company or VAT number.
- Businesses connect to the network through a certified **access point,** a service provider that sends and receives documents on their behalf.
- A **directory** lets senders look up whether a recipient is registered and which document types it accepts.
- Documents follow agreed **formats,** with Peppol BIS Billing 3.0 being the standard for invoices and credit notes.

The model is sometimes called a "four-corner model": the sender, the sender's access point, the receiver's access point and the receiver. Because every access point follows the same specifications, a business only needs one connection to reach every other Peppol participant.

## Belgium: Mandatory From 1 January 2026

Belgium adopted legislation requiring structured electronic invoicing for transactions between VAT-registered businesses established in Belgium, applying from 1 January 2026. The Belgian Federal Public Service Finance designates Peppol as the default exchange network, while allowing parties to agree on other compliant channels. PDF invoices sent by email no longer qualify as invoices for these transactions.

For a SaaS company, the practical consequences depend on your situation:

| Your situation | Implication |
| --- | --- |
| Belgian company invoicing Belgian business customers | Structured e-invoices are required for those invoices |
| Dutch company invoicing Belgian business customers | Check how the mandate applies to non-established suppliers; many Belgian customers will request Peppol regardless |
| Any company invoicing Belgian consumers | Consumer invoices are not covered by the B2B mandate |
| Any company receiving invoices from Belgian suppliers | Expect to be asked for a Peppol ID |

The rules have details on scope, exemptions and penalties that change through implementing measures. Check the official Belgian e-invoicing information and your accountant's guidance for your exact situation.

## The Netherlands: Government First

The Netherlands has not introduced a general B2B e-invoicing mandate. However:

- **Central government** has required e-invoices from suppliers for many years, and Dutch public bodies are able to receive e-invoices through Peppol under the EU directive on e-invoicing in public procurement.
- **Many large companies** prefer or require structured invoices because they process thousands of supplier invoices automatically.
- **Accounting software** used by Dutch SMEs increasingly supports sending and receiving Peppol invoices.

If you sell to municipalities, provinces, water boards, ministries or large corporates in the Netherlands, supporting Peppol is often a procurement advantage, and sometimes a contract requirement.

## The EU Direction: ViDA

The EU's VAT in the Digital Age package, known as ViDA, sets the course for structured e-invoicing across the union, including mandatory e-invoicing for many intra-EU business transactions later this decade, based on the European standard EN 16931. Member states also gain more freedom to introduce domestic mandates without special permission. The timelines are long, but the direction is clear: a SaaS company selling to businesses across the EU should expect structured e-invoicing to become normal rather than exceptional.

## What a Structured Invoice Contains

A Peppol invoice is an XML document, typically in UBL format, following Peppol BIS Billing 3.0, which implements the European standard EN 16931. Its mandatory content resembles a normal invoice, but every field has a defined place and format:

- Invoice number, issue date and due date
- Seller and buyer names, addresses, VAT numbers and, where applicable, company registration numbers
- Buyer reference or purchase order number, often required by public bodies
- Line items with description, quantity, unit price, net amount and VAT category and rate
- VAT breakdown per category and rate
- Totals, payable amount and currency
- Payment instructions, such as IBAN and payment reference

Validation rules are strict. A missing buyer reference, an inconsistent VAT total or an invalid VAT category code will cause rejection. That strictness is the point: the receiver's system can book the invoice without human intervention.

## How a SaaS Product Can Support Peppol

There are three common situations, each with a different solution.

**1. You invoice your own customers.** Your SaaS charges customers through Stripe, Mollie or another provider, and invoices are generated by that provider or your accounting software. The simplest route is usually to let your accounting software send invoices through Peppol, since many tools used in the Benelux support this. Your app's job is to make sure the data the accounting software needs, such as the customer's VAT number, company number and purchase order reference, is collected at sign-up or checkout.

**2. Your SaaS generates invoices on behalf of your users.** If your product is an invoicing, booking, marketplace or practice-management tool where your users bill their own customers, those users will need to send Peppol invoices. You integrate with a Peppol access point provider through its API: your app produces structured invoice data, the provider converts or validates it as UBL and delivers it over the network, and status updates come back through webhooks.

**3. Your SaaS receives or processes invoices.** If your product handles purchasing, expenses or bookkeeping, receiving Peppol invoices can be a strong feature. The access point delivers incoming UBL documents, and your app parses them into its own data model, removing manual entry.

## Implementation Checklist for Case 2

For SaaS products that send invoices on behalf of users, the work typically involves:

| Step | What to do |
| --- | --- |
| Choose an access point provider | Compare API quality, pricing per document, onboarding of your users and support for Belgium and the Netherlands |
| Collect identifiers | Capture each user's and each recipient's VAT number, company number and Peppol ID |
| Look up recipients | Query the Peppol directory before sending, and fall back to PDF where the recipient is not registered and rules allow it |
| Map your data model | Ensure every invoice field required by BIS Billing 3.0 exists, including buyer reference and VAT category codes |
| Validate before sending | Run validation and show users clear errors in their language |
| Handle statuses | Process delivery, acceptance and rejection messages via webhooks, idempotently |
| Store originals | Keep the sent UBL documents for the statutory retention period |
| Credit notes | Support structured credit notes, not just invoices |
| Test | Use the provider's test environment with realistic Belgian and Dutch scenarios |

## Choosing an Access Point Provider

Many providers offer Peppol access, from accounting software vendors to specialised e-invoicing companies. For a SaaS product sending invoices on behalf of users, compare them on criteria that affect your product, not only on price per document:

- **API design.** Can you send structured JSON that the provider converts to UBL, or must you build UBL yourself? Is there a sandbox with realistic validation?
- **User onboarding.** Each of your users needs to be registered as a sender. How does the provider handle registration, identity checks and Peppol ID assignment at scale?
- **Coverage.** Belgium and the Netherlands at minimum, with support for other countries you plan to enter.
- **Status messages.** Delivery confirmations, business-level acceptance or rejection, and clear error codes delivered through webhooks.
- **Receiving.** If you might want to receive invoices later, check whether the same integration supports it.
- **Data location and agreements.** Invoices contain personal and commercial data. Confirm EU processing and sign a processing agreement.
- **Pricing model.** Per document, per sender or flat subscription. Model costs at your expected volume in two years, not today.

Run a short proof of concept with two candidates before committing. Sending ten realistic invoices, including a credit note and a deliberately invalid invoice, reveals more about a provider than any feature comparison.

## Common Mistakes

**Treating Peppol as a PDF attachment problem.** Attaching a PDF to an XML file does not fix missing structured data.

**Collecting VAT numbers too late.** If your sign-up flow does not capture VAT and company numbers, every invoice needs manual correction.

**Ignoring rejections.** A rejected invoice is an unpaid invoice. Rejections must reach the user with a clear explanation.

**Rounding differences.** EN 16931 rules require totals to match line items exactly. Store money as integer cents and calculate VAT consistently. Our article on [money and rounding bugs in SaaS](https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas) explains why.

**Building your own access point.** Becoming a certified access point involves agreements, certification and operational obligations. For almost every SaaS company, using a provider is the right decision.

## What It Costs

Adding Peppol support to an AI-built SaaS, whether by preparing data for your accounting software or integrating an access point provider's API, typically fits within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which also includes payments, managed hosting, backups and priority support. Smaller changes, such as collecting identifiers and connecting accounting software, may fit within **Launch Ready** (€800-€3,500). Access point providers charge their own fees, usually per document or by subscription. You receive a fixed quote after a 15-minute call. Use the [price calculator](https://launchstudio.eu/en/#calculator) for a first range.

## Who Does the Work

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including financial integrations for European and Asian clients. Founders meet the team at Herengracht 420 in Amsterdam; engineers are based at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We work alongside your accountant, who remains the authority on your invoicing obligations.

## Real example

### An AI-Native Founder in Action: The Physiotherapy Billing Tool That Belgian Clinics Needed by January

Kevin Peeters, a Flemish-Dutch founder living in Breda, built Praktijkfactuur with Lovable and Supabase: a scheduling and billing tool for independent physiotherapists and small group practices in Flanders and the southern Netherlands. Practices used it to plan sessions, invoice clients and send invoices to companies that paid for employee treatments. By autumn 2025 it had about 140 practices, two thirds of them in Belgium.

As the Belgian mandate approached, practices began asking whether Praktijkfactuur could send Peppol invoices to the companies they billed. It could not. Invoices were PDFs generated in the browser, VAT numbers of business recipients were optional free-text fields, credit notes were not supported, and totals occasionally differed by one cent from the sum of the lines because amounts were stored as decimals.

LaunchStudio integrated an access point provider through its API, mapped Praktijkfactuur's invoice model to Peppol BIS Billing 3.0 and added validation with Dutch-language error messages before sending. Business recipient records gained required VAT and company number fields with a Peppol directory lookup that showed whether a company could receive e-invoices. Money was migrated to integer cents with consistent VAT rounding, structured credit notes were added, and delivery and rejection statuses flowed back through verified, idempotent webhooks into a status column users could see. Sent UBL files were stored for the retention period.

**Result:** Peppol sending went live in mid-December, two weeks before the Belgian mandate applied. In the first quarter of 2026, practices sent around 3,900 Peppol invoices, with a rejection rate below 1%, almost entirely caused by recipients' incomplete registrations. Several Dutch practices began using it for corporate clients as well.

> *"My users were physiotherapists, not accountants. They needed the invoices to just work on 1 January, and they did."*
> - **Kevin Peeters, Founder, Praktijkfactuur (Breda)**

**Cost & Timeline:** €5,800 (Launch & Grow package: access point integration, BIS Billing mapping and validation, money migration, credit notes and status webhooks) - completed in 15 business days.

## Frequently Asked Questions

### Is Peppol e-invoicing mandatory in the Netherlands?

There is no general B2B mandate in the Netherlands at the moment. Dutch public bodies receive e-invoices and central government has long required them from suppliers, and many large companies prefer them. EU-level changes under ViDA point towards wider structured e-invoicing in the coming years.

### Does the Belgian mandate apply to my Dutch SaaS company?

The Belgian mandate primarily concerns transactions between VAT-registered businesses established in Belgium. How it applies to foreign suppliers depends on your VAT situation in Belgium, so check with your accountant. In practice, many Belgian business customers will ask for Peppol invoices regardless.

### Is a PDF invoice with an XML attachment enough?

Only if the XML is a valid structured invoice in an accepted format, such as UBL following Peppol BIS Billing 3.0, delivered through a compliant channel. A PDF alone does not meet the Belgian requirement for B2B invoices.

### How does Manifera's experience help with e-invoicing integration?

Manifera has built financial and integration systems for 11+ years, where exact data, validation and reliable message handling are essential. LaunchStudio applies that discipline to Peppol integrations, so invoices validate the first time and status messages are never lost.

### Does supporting Peppol help my SaaS get found by buyers?

It can. Belgian and Dutch businesses increasingly search for tools that support Peppol, and stating it clearly on your website, with structured product information, helps search engines and AI answer engines include you when buyers ask which tools can send e-invoices.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Peppol e-invoicing mandatory in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "There is no general Dutch B2B mandate currently. Public bodies receive e-invoices and many large companies prefer them, and EU ViDA rules point towards wider e-invoicing." }
    },
    {
      "@type": "Question",
      "name": "Does the Belgian mandate apply to my Dutch SaaS company?",
      "acceptedAnswer": { "@type": "Answer", "text": "It primarily concerns VAT-registered businesses established in Belgium; foreign suppliers should check their VAT situation with an accountant. Many Belgian customers will request Peppol anyway." }
    },
    {
      "@type": "Question",
      "name": "Is a PDF invoice with an XML attachment enough?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only if the XML is a valid structured invoice such as UBL per Peppol BIS Billing 3.0 delivered through a compliant channel. A PDF alone does not meet the Belgian B2B requirement." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with e-invoicing integration?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built financial and integration systems for 11+ years, and LaunchStudio applies that discipline so Peppol invoices validate and status messages are handled reliably." }
    },
    {
      "@type": "Question",
      "name": "Does supporting Peppol help my SaaS get found by buyers?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can. Stating Peppol support clearly with structured product information helps search and AI engines include you when buyers look for e-invoicing tools." }
    }
  ]
}
</script>
