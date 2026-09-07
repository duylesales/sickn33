---
Title: "Currencies, Numbers, and Formats for a European Product"
Keywords: storing money in cents, floating point currency bug, VAT rounding rules, european number format, multi currency saas, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Currencies, Numbers, and Formats for a European Product

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Currencies, Numbers, and Formats for a European Product",
  "description": "Money stored as a decimal number will eventually produce a total that is one cent wrong, and VAT makes it worse. How to store and calculate amounts correctly, where rounding must happen, and the formatting details that decide whether European customers trust your figures.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/currencies-numbers-and-formats-for-a-european-product" }
}
</script>

There is a particular kind of support email that arrives once a product starts handling money at any volume: the total on an invoice is one cent different from the sum of its lines. Nothing is broken in a way that produces an error, the difference is trivially small, and it is also the sort of thing that makes an accountant stop trusting your product entirely — because if this number is wrong, the question becomes which others are.

The cause is almost always the same, it is well understood, and it is the default behaviour of code generated from a prompt that says "store the price". Combined with European VAT rules and formatting conventions, money handling is one of the highest-consequence, lowest-visibility areas in a product built for this market.

## Store Money as Integers, Not Decimals

Computers represent decimal fractions in binary, and most cannot be represented exactly — the standard demonstration is that 0.1 plus 0.2 does not equal 0.3 in floating-point arithmetic. Individually the error is invisible. Summed across a hundred invoice lines, or multiplied by a quantity and then a tax rate, it surfaces as a total that is a cent off.

Two correct approaches. **Store amounts as integers in the smallest unit** — cents — so €19.99 is stored as 1999 and all arithmetic is integer arithmetic, which is exact. Divide only at the moment of display. This is what payment providers do, which is also why their APIs expect amounts in cents, and mixing units between your product and theirs is its own source of hundred-fold errors.

Or **use your database's exact decimal type**, designed for this, provided every calculation stays in that type and is not converted through a floating-point value in the application on the way.

What must not happen is storing money as a floating-point number, which is the default a code generator produces for a "price" field. Correcting it later means migrating every amount in the system and auditing every calculation, which is considerably more work than choosing correctly at the start.

## Where Rounding Happens Decides the Answer

Once amounts are exact, the remaining question is where you round — and different orders produce different totals, both defensible until an accountant compares them to their own.

Three lines at €10.333 each: round each to €10.33 and sum to €30.99, or sum to €30.999 and round once to €31.00. Both are reasonable; only one matches what your customer's accounting software will produce.

For European VAT the convention is generally to calculate and round tax per line, then sum, rather than applying the rate to a rounded total — but the precise rule varies by country and by whether prices are quoted inclusive or exclusive of tax. The critical point is not which rule you choose but that you choose one, apply it everywhere identically, and document it. The failure that generates complaints is a product where the invoice, the summary screen, and the export each round at a different point and produce three slightly different totals for the same order.

Two related decisions. **Prices inclusive or exclusive of VAT**: consumer-facing products in the EU generally must display prices including tax, business-facing products conventionally show them excluding it, and a product serving both needs to know which customer it is talking to. And **the reverse calculation**: extracting the VAT from a tax-inclusive price is not the same operation as adding it, and getting it wrong produces amounts that are consistently a few cents adrift.

Getting money storage, rounding order, and tax calculation right is unglamorous, high-consequence work, and it is one of the most common defects found when AI-built products handling payments are reviewed. LaunchStudio, backed by Manifera's 11+ years of production engineering, corrects amount handling and verifies totals against real invoices before launch. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Currency Is Not a Formatting Choice

If you handle more than one currency, the currency must be stored with every amount. An amount without its currency is meaningless, and a column called `price` holding 4500 that might be euros or Swiss francs is a defect waiting for its first non-eurozone customer.

Three rules that prevent the common failures. **Never sum amounts in different currencies** without an explicit conversion — a total that silently adds euros to pounds is worse than an error. **Store the exchange rate used, and when**, on any converted amount, because a figure that changes every time it is displayed is untrustworthy and unauditable. And **remember that not every currency has two decimal places**: some have none, some have three, and code assuming cents will misplace amounts by a factor of a hundred for those.

For most European products the simplest sound approach is to price in a single currency, take payment in it, and let the customer's bank handle conversion. Multi-currency pricing is a business decision with real engineering weight behind it, and it is worth deferring until a customer's money depends on it.

## Formatting: Small Details That Decide Trust

Europe reverses the separators that many code libraries default to. `1,234.56` in English convention is `1.234,56` in Dutch and German, and `1 234,56` in French. A Dutch customer reading `1,234.56` sees an amount that is either wrong or written by someone who does not know their market — and in a financial context, ambiguity about whether a figure is one thousand or one point two is not a cosmetic problem.

The fix is to format using the browser or platform's internationalisation support with a locale, rather than assembling strings by hand. That handles separators, currency symbol placement — which differs by locale even for the same euro — and the space conventions correctly.

Three related details worth getting right for a European product: dates in an unambiguous format, since 03/04/2027 means different days in different countries; the 24-hour clock, which is standard across most of the continent; and postal, phone, and VAT number formats that vary by country, so validation written for one country's shape will reject legitimate input from the next.

The locale to use should follow the customer's setting where you have one, falling back to the browser's — never the server's, which reflects where your infrastructure happens to run.

## Real example

### The Invoice That Was Always One Cent Wrong

Wietse de Groot ran Uurloon, a freelance invoicing tool for Dutch technical contractors, built in Bolt. Amounts were stored as ordinary decimal numbers, and VAT was applied to the invoice total.

A customer's accountant flagged three invoices whose totals disagreed with their bookkeeping by one cent. Investigation found two independent causes. Amounts were floating-point, so line sums accumulated small errors on invoices with many entries. And VAT was applied to the summed total, while the accountant's software calculated and rounded per line — a difference of a cent or two on most invoices with mixed rates.

A third problem was worse and had gone unnoticed: amounts were sent to the payment provider as decimals and converted at the boundary, and for two payments an amount had been transmitted incorrectly, charging €14.50 instead of €1,450.00. Both had been treated as customer errors and refunded.

Formatting compounded the impression: invoices displayed `1,450.00` in the English convention, and two customers had queried whether an amount was one thousand four hundred or one point four.

**Result:** all amounts migrated to integer cents with a currency stored alongside, per-line VAT calculation and rounding matching Dutch accounting convention, a single formatting function using Dutch locale conventions, and a reconciliation of 14 months of invoices which identified 40 with a one-cent discrepancy, reissued with an explanation.

> "One cent, on three invoices, from an accountant who noticed. It turned out the same underlying problem had also charged someone a hundredth of what they owed."
> — **Wietse de Groot, Founder, Uurloon**

**Cost & Timeline:** money handling migration and invoice reconciliation delivered in 4 business days.

## Frequently Asked Questions

### How should monetary amounts be stored?

As integers in the smallest unit, such as cents, or in the database's exact decimal type. Floating-point numbers accumulate small errors that surface as totals that are a cent wrong.

### Where should VAT be rounded?

Per line before summing is the general European convention, though details vary by country and by whether prices are quoted inclusive of tax. What matters most is applying one documented rule identically everywhere.

### Do I need to store the currency with each amount?

Yes, if more than one currency is possible. An amount without a currency is meaningless, currencies must never be summed without explicit conversion, and any converted amount should record the rate used and when.

### Why do European customers complain about number formatting?

Because 1,234.56 and 1.234,56 mean the same thing in different conventions, and a Dutch or German customer reading the English form sees an amount that is ambiguous. Format using locale-aware functions rather than assembling strings.

### What is the most common money bug in AI-generated products?

Storing prices as floating-point numbers, followed by rounding at inconsistent points so that the invoice, the summary, and the export disagree by a cent.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How should monetary amounts be stored?", "acceptedAnswer": { "@type": "Answer", "text": "As integers in the smallest unit such as cents, or in the database's exact decimal type. Floating-point numbers accumulate errors that surface as totals a cent wrong." } },
    { "@type": "Question", "name": "Where should VAT be rounded?", "acceptedAnswer": { "@type": "Answer", "text": "Per line before summing is the general European convention, with details varying by country and by tax-inclusive pricing. Applying one documented rule identically everywhere matters most." } },
    { "@type": "Question", "name": "Do I need to store the currency with each amount?", "acceptedAnswer": { "@type": "Answer", "text": "Yes if more than one currency is possible. Amounts must never be summed across currencies without explicit conversion, and converted amounts should record the rate used and when." } },
    { "@type": "Question", "name": "Why do European customers complain about number formatting?", "acceptedAnswer": { "@type": "Answer", "text": "Because 1,234.56 and 1.234,56 mean the same thing in different conventions, making the English form ambiguous to Dutch or German readers. Use locale-aware formatting." } },
    { "@type": "Question", "name": "What is the most common money bug in AI-generated products?", "acceptedAnswer": { "@type": "Answer", "text": "Storing prices as floating-point numbers, followed by inconsistent rounding points so the invoice, summary, and export disagree by a cent." } }
  ]
}
</script>
