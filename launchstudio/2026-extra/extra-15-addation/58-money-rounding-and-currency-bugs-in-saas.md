---
Title: "Money, Rounding and Currency Bugs in SaaS"
Keywords: money rounding bugs, store money as integer cents, vat rounding invoice, javascript floating point currency, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Money, Rounding and Currency Bugs in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Money, Rounding and Currency Bugs in SaaS",
  "description": "Invoices that are one cent off, VAT totals that do not match, refunds that fail and Dutch users whose amounts are read as a thousand times too high: money bugs are common in AI-built apps. This guide explains why floating point numbers are dangerous for money, how to store and calculate amounts, VAT rounding, payment provider formats, Dutch number input, splitting amounts and multi-currency handling.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-14",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Numeric types", "url": "https://www.postgresql.org/docs/current/datatype-numeric.html" },
    { "@type": "CreativeWork", "name": "Stripe: Currencies and zero-decimal amounts", "url": "https://docs.stripe.com/currencies" },
    { "@type": "CreativeWork", "name": "Mollie API: Amount object", "url": "https://docs.mollie.com/reference/common-data-types" },
    { "@type": "CreativeWork", "name": "Belastingdienst: Invoice requirements", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/vat_in_the_netherlands/invoicing/invoice_requirements" }
  ]
}
</script>

Customers forgive many kinds of bugs. A slow page, a misaligned button or a confusing message are annoying but tolerable. Money bugs are different. An invoice total that is one cent off from the sum of its lines makes an accountant distrust everything else. A VAT amount that does not match the rate gets an invoice rejected. A refund that fails because of a formatting error leaves a customer waiting. A Dutch user who types "1.250,00" and gets charged €1.25, or €125,000, will not stay a customer.

These bugs are remarkably common in apps built with AI tools. Generated code often stores amounts as floating point numbers, calculates VAT inconsistently, formats amounts with string concatenation and passes values to payment providers in the wrong units. Each of these works in a demo with round numbers and fails with real prices, discounts and currencies.

This guide explains how to handle money correctly.

## Key Takeaways

- **Never use floating point numbers for money.** Store amounts as integer minor units, such as cents, or as exact decimals with `numeric` in Postgres.
- **Calculate on the server,** never trust amounts sent from the browser.
- **Choose and document a rounding rule,** and apply VAT rounding consistently, so invoice lines and totals always match.
- **Respect each payment provider's amount format:** for example, Stripe uses integer minor units, while Mollie uses decimal strings with a currency.
- **Parse and display amounts with locale awareness,** especially for Dutch users who write "1.234,56".

## Why Floating Point Fails

Most programming languages, including JavaScript, represent decimal numbers as binary floating point. Many decimal fractions cannot be represented exactly in binary. The classic example: `0.1 + 0.2` in JavaScript is `0.30000000000000004`, not `0.3`.

For money, those tiny errors accumulate. Multiply a price by a quantity, add VAT, apply a discount, sum many lines, and results drift by a cent here and there. Rounding at the end sometimes fixes it and sometimes rounds the wrong way.

The rules:

- **In the database,** store amounts as integers in minor units, for example `price_cents integer` or `bigint`, or as `numeric` with explicit precision. Avoid `real` and `double precision` for money.
- **In application code,** work in integer cents, or use a decimal library designed for exact arithmetic.
- **Always store the currency** alongside amounts, as an ISO 4217 code such as `EUR`.

## Calculate on the Server

AI-generated checkouts sometimes calculate the total in the browser and send it to the backend, which creates the payment for that amount. A user who edits the request can pay one euro for anything.

Prices, discounts, VAT and totals must be calculated on the server from your database, every time. The browser may display a preview, but the server decides the amount charged.

## Rounding Rules

Rounding happens whenever you calculate a percentage, divide an amount or convert currency. Decide:

- **Which rounding method:** round half up, where 0.5 rounds away from zero, is common for invoices; round half to even, sometimes called banker's rounding, reduces bias in large datasets. Use one consistently.
- **When to round:** per line, per VAT rate group or on the total. Each gives slightly different results.
- **To how many decimals:** for euros, two decimals at the point of invoicing, though intermediate calculations, such as unit prices with more decimals, may need more precision.

Document the choices, implement them in one place in your code and test them.

## VAT Rounding on Invoices

Dutch invoices must show, among other things, the VAT amount per rate. VAT rounding causes two common problems:

**Line versus total rounding.** If you calculate VAT per line and round each, then sum, the result can differ by a cent from calculating VAT on the total of lines with the same rate. Both approaches can be acceptable, but your invoice must be internally consistent: the VAT shown must equal the VAT used in the total, and the total must equal the sum of net amounts plus VAT.

**Prices including VAT.** Consumer prices are often shown including VAT, for example €49.00. Calculating the net amount and VAT from a gross price requires dividing, which produces fractions of cents. Choose whether gross or net amounts are leading for each product type and calculate the other consistently.

A robust approach:

1. Store net unit prices, or gross for consumer products, in cents, with the VAT rate.
2. Calculate line amounts in cents.
3. Group lines by VAT rate.
4. Calculate VAT per rate group from the group's net total, rounding once.
5. Total equals sum of net totals plus sum of VAT amounts.

Consult your accountant on the approach that fits your business, and test invoices with many lines and mixed rates. Our guide on [VAT and invoices for SaaS in the Netherlands](https://launchstudio.eu/en/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs) covers the invoice requirements.

## Payment Provider Formats

Payment providers have their own conventions, and mixing them up is a frequent bug:

| Provider | Amount format | Example for €49.95 |
| --- | --- | --- |
| Stripe | Integer in the currency's smallest unit | `4995` with currency `eur` |
| Mollie | String with exactly two decimals, plus currency | `{"currency": "EUR", "value": "49.95"}` |

Common errors:

- Sending `49.95` to Stripe, which interprets a non-integer as invalid, or sending `4995` thinking it is euros in another system.
- Sending a number instead of a string, or a string with one decimal, such as `"49.9"`, to Mollie, which rejects it.
- Forgetting that some currencies have no decimal places, such as the Japanese yen in Stripe.

Convert at a single boundary in your code, with a function that turns your internal cents into the provider's format, and test it.

## Dutch Number Input and Display

Dutch notation uses a comma for decimals and a period for thousands: "1.234,56". English notation is the reverse: "1,234.56". AI-generated forms usually parse input with JavaScript's `parseFloat`, which reads "1.234,56" as `1.234`, and "12,50" as `12`.

Rules:

- **Parse input according to the user's locale,** or accept both separators carefully, rejecting ambiguous input such as "1.234" when it could mean either.
- **Use `inputmode="decimal"`** on mobile so users get the right keyboard.
- **Format for display with `Intl.NumberFormat`,** such as `new Intl.NumberFormat("nl-NL", { style: "currency", currency: "EUR" })`, which produces "€ 1.234,56".
- **Never build amount strings by concatenation,** such as `"€" + amount.toFixed(2)`, which ignores locale.

## Splitting Amounts

Dividing an amount, for example splitting €100 into three instalments or allocating a discount across lines, produces remainders. €100 divided by three is €33.33 three times, totalling €99.99, a cent short.

The solution is allocation: calculate the base share, then distribute the remaining cents one by one across parts, so the parts always sum to the original. Apply the same principle to marketplace splits, discounts across lines and pro-rated refunds.

## Discounts, Coupons and Pro-Rating

- **Apply discounts in a defined order,** such as line discounts before order discounts, and before VAT unless rules say otherwise.
- **Store the discount applied,** not only the final amount, so invoices and refunds can be explained.
- **Pro-rate subscription changes** using the payment provider's logic where possible, rather than reimplementing it.
- **Prevent negative totals** and validate coupon conditions on the server.

## Refunds

- **Refund in the same currency and provider format** as the original payment.
- **Track refunded amounts** per payment and prevent refunding more than was paid.
- **Handle partial refunds** with exact amounts, and recalculate VAT for credit notes consistently with the original invoice.
- **Make refund requests idempotent,** so retries do not refund twice.

## Multiple Currencies

If you sell in more than one currency:

- **Store each amount with its currency;** never mix currencies in calculations.
- **Record exchange rates with timestamps and sources** if you convert, and store both original and converted amounts.
- **Present prices in the customer's currency consistently** across pricing pages, checkout and invoices.
- **Check provider support** for each currency and payment method.

## Reconciliation: Proving the Numbers Agree

Even with correct calculations, money can drift between systems: your database, your payment provider, your accounting software and your bank. A regular reconciliation catches problems before an accountant or customer does:

- **Daily:** compare payments recorded in your database with payments reported by Stripe or Mollie for the same period, by ID, amount and status.
- **Per payout:** match each payout from your provider with the payments, refunds and fees it contains.
- **Monthly:** compare invoice totals and VAT per rate with your accounting software and with what the provider settled.
- **On differences:** flag them for review rather than adjusting automatically, and record the resolution.

Automated reconciliation reports are inexpensive to build and give founders, accountants and investors confidence that the numbers are right. They also reveal subtle bugs, such as a webhook that occasionally fails, long before they become large.

## Testing Money Logic

Money logic deserves dedicated tests:

- Prices with awkward values, such as €0.10, €9.99 and €1,234.56
- Many lines with mixed VAT rates, verifying line, group and total consistency
- Gross-to-net calculations for VAT-inclusive prices
- Splits that do not divide evenly
- Dutch and English input formats
- Partial refunds and credit notes
- Provider format conversion for Stripe and Mollie

## Common Mistakes in AI-Built Apps

**Floats in the database and in calculations.**

**Totals calculated in the browser** and trusted by the server.

**VAT calculated differently** on screen, in invoices and in exports.

**`parseFloat` on Dutch input.**

**Wrong units sent to payment providers.**

**Lost cents when splitting amounts.**

## How LaunchStudio Helps

LaunchStudio reviews and fixes money handling in AI-built SaaS: migrating amounts to integer cents or exact decimals, moving calculations to the server, implementing consistent VAT and rounding rules agreed with your accountant, provider format conversion for Stripe and Mollie, locale-aware input and display, allocation for splits and discounts, idempotent refunds and dedicated tests.

The **Launch Ready** package (€800-€3,500) covers money handling fixes along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including billing and financial systems for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Catering Platform Whose Invoices Never Added Up

Esther Bakker built Cateringbestel with Lovable, Supabase and Mollie: an ordering platform where companies order lunches and catering for meetings from local caterers, with monthly invoices. Several customers' finance departments started rejecting invoices because the VAT total did not match the lines, and one caterer complained that a large order had been charged at a fraction of its value.

The review found a chain of issues. Prices were stored as floating point numbers, and totals were calculated in the browser and sent to the backend, which passed them to Mollie. VAT was calculated per line with rounding on screen, but per total in the invoice PDF, producing one- or two-cent differences. Mixed VAT rates, since some items such as drinks had different rates, were combined incorrectly in the totals. A caterer's admin had typed a price as "1.250,00", which `parseFloat` read as 1.25. Partial refunds for cancelled items sent amounts with three decimals to Mollie, which rejected them.

LaunchStudio migrated all amounts to integer cents with explicit currencies, moved price, discount, VAT and total calculations to a server-side function used by the checkout, invoices and exports alike, and implemented VAT per rate group with one rounding step, as agreed with Esther's accountant. Amount input used locale-aware parsing that accepted Dutch notation and rejected ambiguous values, display used `Intl.NumberFormat`, and a single conversion function produced Mollie's decimal string format. Refunds were limited to the remaining refundable amount, made idempotent and reflected in credit notes with consistent VAT. A test suite covered mixed rates, awkward prices, Dutch input and partial refunds.

**Result:** Invoice rejections stopped within the first billing cycle, and the caterer was correctly charged for the affected order after a corrected invoice. Esther's accountant now receives exports that reconcile exactly with Mollie payouts.

> *"A one-cent difference sounds trivial until a customer's finance team stops trusting every invoice you send."*
> - **Esther Bakker, Founder, Cateringbestel (Rotterdam)**

**Cost & Timeline:** €3,200 (Launch Ready package: money migration, server-side calculation, VAT rounding, locale-aware input, Mollie formatting, refunds and tests) - completed in 9 business days.

## Frequently Asked Questions

### How should I store money in Supabase?

Store amounts as integers in minor units, such as cents, in `integer` or `bigint` columns, or as `numeric` with explicit precision, always with a currency code. Avoid floating point types such as `real` and `double precision`, which cannot represent many decimal values exactly.

### Why is my invoice total one cent different from the lines?

Usually because rounding happens in different places, for example VAT rounded per line in one calculation and on the total in another, or because floating point arithmetic introduces tiny errors. Use one calculation function with a defined rounding rule for screens, invoices and exports.

### How do I handle Dutch number formats like 1.234,56?

Parse input according to the user's locale instead of using `parseFloat`, which misreads Dutch notation. Display amounts with `Intl.NumberFormat` using the `nl-NL` locale. Reject ambiguous input and give clear examples in the field.

### How does Manifera's experience help with financial calculations?

Manifera has built billing and financial systems for enterprise clients for 11+ years, where every cent must reconcile. LaunchStudio applies that discipline to AI-built SaaS, so invoices, payments, refunds and exports agree with each other and with your accountant.

### Do money bugs affect my product's reputation?

Yes, strongly. Finance teams and accountants notice inconsistencies immediately and share their experiences. Accurate invoicing builds the trust that leads to renewals, referrals and positive reviews, which in turn shape how buyers, search engines and AI answer engines perceive your product.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How should I store money in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "As integer minor units such as cents, or numeric with explicit precision, always with a currency code; avoid floating point types." }
    },
    {
      "@type": "Question",
      "name": "Why is my invoice total one cent different from the lines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Rounding in different places or floating point errors; use one calculation function with a defined rounding rule everywhere." }
    },
    {
      "@type": "Question",
      "name": "How do I handle Dutch number formats like 1.234,56?",
      "acceptedAnswer": { "@type": "Answer", "text": "Parse by locale instead of parseFloat, display with Intl.NumberFormat nl-NL and reject ambiguous input." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with financial calculations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise billing systems for 11+ years, and LaunchStudio makes invoices, payments and exports reconcile." }
    },
    {
      "@type": "Question",
      "name": "Do money bugs affect my product's reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Strongly; accurate invoicing builds trust, renewals and positive reviews that buyers and AI engines notice." }
    }
  ]
}
</script>
