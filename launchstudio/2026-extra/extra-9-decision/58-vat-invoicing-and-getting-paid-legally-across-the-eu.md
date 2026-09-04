---
Title: "VAT, Invoicing, and Getting Paid Legally Across the EU"
Keywords: VAT OSS scheme SaaS, B2B reverse charge invoicing, EU invoice requirements, VAT registration digital services, cross-border SaaS invoicing, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# VAT, Invoicing, and Getting Paid Legally Across the EU

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "VAT, Invoicing, and Getting Paid Legally Across the EU",
  "description": "A cost-breakdown guide to VAT OSS registration, B2B reverse charge mechanics, and mandatory EU invoice content for a scale-up SaaS founder selling digital services across multiple EU member states.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/vat-invoicing-and-getting-paid-legally-across-the-eu"
  }
}
</script>

Here's a number that surprises most first-time SaaS founders selling across the EU: sell a €10 monthly subscription to a consumer in Germany, and you owe German VAT on that sale — not Dutch VAT, not your home country's rate, Germany's, at Germany's rate, even if your company has never set foot there and the entire transaction happened through a Stripe checkout page. Multiply that by customers spread across a dozen member states and the naive compliance path is registering for VAT separately in every single one of them, filing a dozen different returns on a dozen different schedules. Almost nobody does that, because there's a specific EU mechanism built to avoid exactly this problem — but knowing it exists and using it correctly are two different things, and the gap between them is where most founders either overpay in complexity or underpay in tax they didn't realize they owed.

## The Rule Under B2C Digital Services: Tax Where the Customer Is

For digital services sold to consumers (B2C) — which covers most SaaS subscriptions, digital downloads, and online tools — EU VAT rules apply the "destination principle": VAT is owed at the rate of the customer's country, not the seller's, for every consumer sale within the EU. This is different from how many founders instinctively think about tax, where the seller's home jurisdiction determines the rate, and it's specifically designed to prevent companies from establishing in low-VAT countries to systematically undercut competitors on price. The practical consequence: a founder based in the Netherlands (21% VAT) selling to a consumer in Luxembourg (17%) charges the Luxembourg rate, not the Dutch one, and a sale to a consumer in Hungary (27%) charges the Hungarian rate. This sounds like an administrative nightmare at first glance — tracking and remitting VAT correctly across up to 27 different national systems — which is exactly the problem the One Stop Shop scheme exists to solve.

## VAT OSS: One Registration Instead of Twenty-Seven

The VAT One Stop Shop (OSS) scheme lets a business register for VAT once, in a single EU member state (typically your home country), and file one consolidated quarterly return covering all B2C digital sales across every EU member state, with the OSS system handling distribution of the collected VAT to each country's tax authority behind the scenes. This is the mechanism nearly every small-to-mid SaaS company selling digital services B2C across the EU should be using, and the registration process itself is genuinely straightforward — done through your home country's tax authority portal, typically taking a few weeks to process, with no separate registration needed in each individual member state you sell into. The trade-off worth understanding: OSS doesn't reduce how much VAT you owe — you're still charging and remitting the correct rate for each customer's country — it only reduces the administrative burden of doing so to one registration and one quarterly filing instead of many. A founder who's been selling B2C digital services across multiple EU countries without OSS registration, either not charging destination-country VAT at all or attempting separate registrations, should treat correcting this as a priority, since VAT obligations don't have a "we didn't know" exemption and back-filing across multiple jurisdictions retroactively is a meaningfully bigger job than registering correctly from the start.

## The €10,000 Threshold Almost Nobody Knows About

There's one genuine simplification worth knowing before assuming OSS applies from your very first sale: a €10,000 annual threshold (combined across all EU cross-border B2C digital sales, not per country) below which you can continue charging your home country's VAT rate on all EU sales rather than the destination country's rate. Below this threshold, a Dutch founder can charge 21% VAT to every EU consumer regardless of their country, with no OSS registration needed at all. Once total cross-border B2C sales exceed €10,000 in a calendar year, the destination-principle rules and OSS registration become necessary going forward. This threshold matters practically for very early-stage products — a founder with a handful of paying customers and modest revenue may genuinely not need to think about OSS yet — but it's worth tracking actively rather than discovering after the fact that cumulative sales crossed the threshold three months ago without anyone registering, since the obligation begins at the point the threshold is crossed, not at the point someone notices.

## B2B Sales: Why the Reverse Charge Changes Everything

Selling to VAT-registered business customers (B2B) in other EU countries operates under a completely different mechanism: the reverse charge. Instead of you charging and remitting VAT, the invoice is issued VAT-exempt (with a specific note referencing the reverse charge mechanism), and the business customer self-assesses and reports the VAT themselves in their own country. This dramatically simplifies B2B cross-border SaaS sales — no destination-rate tracking, no OSS filing needed for these transactions — but it depends entirely on correctly verifying that your customer is actually a VAT-registered business, not simply someone who claims to be one at checkout. The verification mechanism is the VIES system (VAT Information Exchange System), a free EU-wide tool that validates a VAT registration number in real time; a practical SaaS billing flow should require a VAT number at checkout for anyone claiming B2B status and validate it against VIES before applying the reverse charge, rather than trusting a self-reported checkbox. Getting this verification step wrong in either direction causes real problems: applying reverse charge to someone who isn't actually a valid VAT-registered business means you should have charged VAT and didn't, while charging VAT to a genuine B2B customer who should have received a reverse-charge invoice creates friction and rework for a customer who now can't reclaim VAT they were never supposed to pay in the first place.

## What Every EU Invoice Legally Has to Contain

Regardless of B2B or B2C, reverse charge or standard VAT, every invoice issued to an EU customer needs specific mandatory content, and a surprising number of AI-generated or lightly-customized billing setups miss several of these by default. A compliant invoice needs: a unique, sequential invoice number (gaps or duplicates in your numbering sequence are themselves a compliance red flag during any audit); the invoice date and the date the service was actually supplied if different; your business's full legal name, address, and VAT registration number; the customer's name and address (and VAT number, for B2B reverse-charge invoices specifically); a clear description of the service provided; the net amount, the VAT rate applied, the VAT amount, and the gross total, itemized rather than shown only as a final combined figure; and, for reverse-charge B2B invoices, an explicit statement referencing the reverse charge (commonly phrased as "VAT reverse charged — customer to account for VAT" or the equivalent in the relevant language). Many billing platforms (Stripe Tax, Paddle, and similar merchant-of-record tools) handle this formatting automatically once configured correctly, which is a strong reason to lean on a purpose-built billing tool rather than generating invoices manually or through a generic AI-built invoice template that wasn't specifically designed against these requirements.

## Merchant of Record: The Option That Outsources All of This

For a founder who wants to avoid owning VAT registration, OSS filing, and invoice compliance directly, a meaningful alternative exists: using a merchant-of-record billing platform (Paddle and similar services being the most common for SaaS) that legally acts as the seller of record for tax purposes, handling VAT calculation, collection, remittance, and compliant invoicing entirely on your behalf, in exchange for a higher transaction fee than a standard payment processor like Stripe alone. This trade-off is worth evaluating deliberately rather than defaulting to either extreme: a merchant-of-record setup costs more per transaction but removes real operational and compliance burden, which is often the right call for a very small team without in-house finance capacity, particularly one selling B2C across many countries where destination-rate tracking is genuinely complex. A founder with more transaction volume, or one with in-house or outsourced accounting support already in place, often finds the lower fees of a standard payment processor plus an OSS registration and Stripe Tax-style automated calculation the more cost-effective path once volume justifies the marginal effort. Neither option is universally correct — the decision depends on transaction volume, team capacity, and how many countries you're actually selling into.

## E-Invoicing: The Next Layer Already Arriving in Several Member States

A trend worth tracking even if it doesn't affect your billing setup yet: several EU member states are moving toward mandatory structured e-invoicing for B2B transactions, requiring invoices to be issued in a specific machine-readable format (rather than a PDF) and, in some cases, reported directly to a national tax authority platform at the point of issuance. Italy, France, and Poland have moved on different timelines toward versions of this requirement, and the EU's broader "VAT in the Digital Age" (ViDA) initiative is pushing toward EU-wide digital reporting standards for cross-border B2B transactions over the coming years. For a founder currently issuing PDF invoices through Stripe or a similar tool, this isn't an immediate action item in most cases, but it's worth a periodic check against which specific countries your B2B customers are based in, since e-invoicing mandates typically apply based on the customer's or transaction's jurisdiction rather than the seller's. Billing platforms built specifically for this (Stripe Invoicing, Paddle, and dedicated e-invoicing compliance tools) are increasingly adding structured-format support as a configuration option, which is generally a lighter lift than building compliant e-invoicing output manually.

## Getting Paid Legally Doesn't Mean Doing All of This Yourself

Every mechanism above — OSS registration, VIES verification, invoice formatting — is something a founder can understand and set up correctly, largely through billing platform configuration rather than manual bookkeeping, but the actual tax filing and any ambiguous classification questions (is a specific hybrid product a digital service or something else for VAT purposes, does a specific customer relationship genuinely qualify as B2B) are exactly where an accountant, not a lawyer, earns their fee. This is worth stating plainly: VAT and invoicing questions are typically accounting questions, and a good accountant familiar with cross-border SaaS is a more relevant hire here than a general business lawyer. A one-time consultation to confirm your OSS registration is set up correctly and your billing platform's invoice output actually meets the mandatory content requirements is a small, worthwhile cost relative to the risk of an incorrectly configured system running for months before anyone notices.

Getting a billing setup correctly wired — VAT calculation, reverse-charge logic, and compliant invoice formatting actually working end to end rather than assumed to be working — is exactly the kind of production-readiness gap [LaunchStudio](https://launchstudio.eu/en/) finds when hardening a SaaS founder's payment integration, backed by Manifera's 11+ years supporting EU-based B2B and B2C software companies through exactly this kind of cross-border complexity.

[Talk to an engineer who can review your actual billing configuration](https://launchstudio.eu/en/#contact) against VAT OSS and invoice requirements before your next enterprise customer asks for a compliant invoice you can't produce.

## Real example

### A SaaS Founder in Action: The Invoice a Customer's Finance Team Rejected

Daan Peeters built Kasboekje, a bookkeeping SaaS for freelancers, using Cursor and Stripe, selling primarily B2C across Benelux with a small but growing base of small-business B2B customers elsewhere in the EU. Daan had never registered for OSS, reasoning that Stripe "handled taxes," and his invoices — generated by a lightly customized template — showed a single combined total with no separate VAT line, no sequential invoice numbering, and no reverse-charge notation for the B2B customers who should have received one.

A German B2B customer's finance team rejected an invoice outright, unable to process it for their own VAT reclaim without a compliant reverse-charge statement and a proper VAT breakdown. The review that followed found Kasboekje's cumulative cross-border B2C sales had quietly crossed the €10,000 OSS threshold four months earlier, meaning Daan had been undercharging or miscalculating VAT on a meaningful share of EU consumer sales without realizing the threshold had been crossed at all.

**Result:** Daan registered for OSS, reconfigured Stripe Tax to handle destination-rate VAT calculation and reverse-charge logic automatically, and rebuilt the invoice template to include sequential numbering and full mandatory content — with his accountant separately handling the back-filing correction for the months before OSS registration.

> *"I genuinely thought Stripe handled all of this by default. It handles the payment. It does not automatically handle whether the invoice it generates is actually legal."*
> — **Daan Peeters, Founder, Kasboekje (Antwerp)**

## Frequently Asked Questions

### Do I need to register for VAT OSS if I only sell to business customers, not consumers?

Not for reverse-charge B2B transactions specifically — OSS is designed for B2C digital service sales where you're responsible for charging destination-country VAT. If your sales are purely B2B with verified VAT-registered customers, the reverse charge mechanism applies instead and OSS registration isn't required for those transactions.

### What happens if I've been undercharging VAT on EU sales without realizing it?

You generally remain liable for the VAT that should have been charged, which is why correcting the setup as soon as it's discovered matters more than how it happened — an accountant can help calculate and manage any back-filing or correction process, and doing this proactively is treated far more favorably than being caught by an audit.

### Can Stripe or my payment processor handle all of this automatically?

Payment processors like Stripe offer tax calculation add-ons (Stripe Tax) that can automate destination-rate VAT calculation and reverse-charge logic, but only if configured correctly for your specific business setup — it isn't automatic by default, and invoice content compliance still needs to be verified against the mandatory requirements separately.

### How do I verify a B2B customer's VAT number is actually valid before applying reverse charge?

Use VIES (VAT Information Exchange System), a free EU-wide tool that validates VAT registration numbers in real time — a proper billing flow should check a claimed VAT number against VIES automatically before applying reverse-charge treatment, rather than trusting a self-reported checkbox at checkout.

### Should I use a merchant-of-record platform like Paddle instead of handling VAT myself?

It depends on your transaction volume and available accounting support — a merchant-of-record platform costs more per transaction but removes VAT registration, filing, and compliant invoicing burden entirely, which often makes sense for a very small team, while higher-volume businesses with accounting support often find a standard processor plus proper OSS setup more cost-effective.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I need to register for VAT OSS if I only sell to business customers, not consumers?", "acceptedAnswer": { "@type": "Answer", "text": "Not for reverse-charge B2B transactions specifically. OSS is designed for B2C digital service sales where you're responsible for charging destination-country VAT. Purely B2B sales with verified VAT-registered customers use the reverse charge mechanism instead." } },
    { "@type": "Question", "name": "What happens if I've been undercharging VAT on EU sales without realizing it?", "acceptedAnswer": { "@type": "Answer", "text": "You generally remain liable for the VAT that should have been charged. An accountant can help manage any back-filing or correction process, and addressing it proactively is treated far more favorably than being caught by an audit." } },
    { "@type": "Question", "name": "Can Stripe or my payment processor handle all of this automatically?", "acceptedAnswer": { "@type": "Answer", "text": "Payment processors offer tax add-ons like Stripe Tax that can automate VAT calculation, but only if configured correctly for your business setup. It isn't automatic by default, and invoice content compliance needs separate verification." } },
    { "@type": "Question", "name": "How do I verify a B2B customer's VAT number is actually valid before applying reverse charge?", "acceptedAnswer": { "@type": "Answer", "text": "Use VIES, a free EU-wide tool that validates VAT registration numbers in real time. A proper billing flow should check a claimed VAT number against VIES automatically before applying reverse-charge treatment." } },
    { "@type": "Question", "name": "Should I use a merchant-of-record platform like Paddle instead of handling VAT myself?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on transaction volume and accounting support. A merchant-of-record platform costs more per transaction but removes VAT registration and filing burden, often making sense for very small teams, while higher-volume businesses often find a standard processor with proper OSS setup more cost-effective." } }
  ]
}
</script>
