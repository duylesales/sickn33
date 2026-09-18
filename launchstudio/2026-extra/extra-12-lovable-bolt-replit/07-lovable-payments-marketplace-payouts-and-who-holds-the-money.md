---
Title: "Lovable Payments: Marketplace Payouts and Who Holds the Money"
Keywords: lovable payments, marketplace payouts, split payments, connected accounts, escrow, platform liability, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Payments: Marketplace Payouts and Who Holds the Money

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Marketplace Payouts and Who Holds the Money",
  "description": "Two-sided products collect money for somebody else, which changes what your app must do and what you are legally responsible for. Connected accounts, payout timing, refunds across two parties, and the model to avoid.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-marketplace-payouts-and-who-holds-the-money" }
}
</script>

There is a version of this product that a weekend with Lovable will build for you, and it works. Customers pay into your business bank account. At the end of the month you open a spreadsheet, work out what each supplier earned, subtract your commission and send the transfers yourself.

It works at eleven suppliers. At forty it is a day a month. At a hundred it is a part-time job with a compliance problem attached, because taking custody of other people's money and passing it on later is a regulated activity in the European Union, and "I built a small marketplace" is not an exemption anyone has heard of.

The alternative is not more complicated to build. It is just different, and choosing it before you have suppliers is much cheaper than converting afterwards.

## The Model to Avoid

Money in, money out, from your own account, is called being a payment intermediary and it is the arrangement that creates the problem.

Three things come with it. The regulatory exposure of holding funds belonging to others, which in the Netherlands and the wider EU has a licensing regime attached. An accounting picture where gross transaction volume flows through your revenue, making your business look far larger than it is and your tax position considerably more interesting than you want. And operational risk that is entirely yours: if a supplier disputes what they were paid, the evidence is your spreadsheet.

There is one narrow case where it is fine — you are genuinely the seller, the supplier is your subcontractor, and you take commercial responsibility for delivery. That is not a marketplace. That is a business with suppliers, and it should be structured and described as one.

## Connected Accounts, and What They Change

The standard structure is that each supplier has their own account with the payment provider, connected to your platform. The customer pays; the provider splits the payment at the moment of capture; your commission lands with you and the remainder with the supplier. The money never sits in your bank account at all.

This changes your build in four specific ways.

**Onboarding becomes a real feature.** Each supplier goes through identity verification with the provider — name, address, bank details, and for companies the ownership structure. Your app has to move them through it, tell them what is still missing, and refuse to let them list anything until they are cleared. This takes suppliers days, not minutes, and every marketplace underestimates it.

**Payouts have timing.** Funds are typically held for a period before they reach the supplier, and each provider does this differently. Suppliers care about this far more than you expect — cash flow is the reason small businesses join marketplaces and the reason they leave them. Show the schedule in their dashboard rather than answering the question by email forty times.

**Refunds become a three-party problem.** If a customer is refunded after the supplier has been paid, the money has to come from somewhere. Decide in advance: from the supplier's next payout, from their balance, or from you. Then implement it, because the alternative is negotiating each case while a customer waits.

**Your commission is your revenue, not the transaction.** Model this correctly from the first sale. Your accounts should show commission as revenue and the rest as flow-through, which is both accurate and much easier to explain to an accountant or an investor later.

## What Your Database Has to Hold

Whatever the provider does, your application needs its own ledger, and this is the part AI-generated marketplace code omits entirely.

For every transaction: the gross amount, the commission, the supplier's share, any VAT on either side, the provider's reference, the status, and the payout it eventually belongs to. For every supplier: verification status, what has been paid out, what is pending, and what is being held back.

This ledger is what lets you answer a supplier's question about a payment from March, produce the annual statement they need for their own accounts, and detect the case where the provider's records and yours disagree — which happens, usually because a refund or a dispute was processed somewhere your code was not watching.

Reconcile it monthly against the provider's own report. Automatically if you can, by eye if you must, but do it: a marketplace whose ledger has quietly diverged from reality is very hard to fix retrospectively.

## VAT in a Three-Party Transaction

Get advice on this one, because the answer depends on what you are actually selling and to whom.

Broadly: your commission is a service you supply to the supplier, and it has its own VAT treatment based on where they are and whether they are a business. The underlying goods or service is supplied by the supplier to the customer, with its own treatment that is generally not yours to determine.

Two practical consequences for your build. You will be issuing invoices in two directions — your commission invoice to the supplier, and often the supplier's invoice to the customer on their behalf, which is a legitimate arrangement called self-billing and requires their agreement. And your app needs to know each supplier's VAT status, because a marketplace of private individuals and one of registered businesses do not work the same way.

## Trust and Safety Arrives Sooner Than You Think

Every marketplace eventually meets a version of the same afternoon: a supplier who did not deliver, a customer who says they did not receive what they paid for, and a platform in the middle with no process.

You need three things before it happens rather than during. A way to hold a payout — the ability to pause a supplier's settlement while something is investigated, which is nearly impossible to add retrospectively because the money has already moved. A written statement of what the platform is and is not responsible for, in your terms, so the conversation starts from a shared position. And a record of what was agreed: the booking, the message thread, the cancellation, the timestamps. Marketplaces that keep communication off-platform lose the ability to adjudicate anything.

Suspension deserves a designed flow, not an improvised one. A suspended supplier should stop receiving new bookings, keep access to their existing obligations and their own records, and have a stated route to resolution. A blanket account deletion in the middle of a dispute turns a bad week into a legal letter.

None of this needs to be elaborate at 30 suppliers. It needs to exist.

## The Reporting Suppliers Will Ask For

The questions arrive in a predictable order, and answering them well is a retention feature rather than an administrative burden.

In the first month: what have I earned, and when will it arrive? In the first quarter: which of my listings actually make money? At the end of the year: what do I give my accountant?

The last of those is the one small marketplaces neglect, and it is the one that most affects whether suppliers stay. An annual statement — gross earnings, commission deducted, net paid, by month, with VAT treatment stated — costs you an afternoon and saves each supplier an evening. For a platform whose suppliers are one-person businesses, that is a genuine reason to prefer you over the alternative.

## One Provider Decision Worth Making Early

Not every payment provider supports connected accounts in every country, and marketplaces discover this at the worst possible moment — when a supplier in Belgium or Germany cannot be onboarded.

Check three things before you commit. Which countries can your suppliers be resident in, which legal forms are supported (sole traders and one-person companies are the majority of most Dutch marketplaces and are handled differently from limited companies), and whether the payment methods your customers expect — iDEAL above all — work with split payments rather than only with direct charges.

The answers differ by provider and change over time, so verify them against current documentation rather than against a comparison article. Ten minutes of checking against your actual supplier base prevents the migration that would otherwise be forced on you in month eight.

## Setting This Up

For a marketplace this is typically two to three weeks rather than days: provider selected for connected-account support in your markets, supplier onboarding with verification tracked through to completion, listings gated on verified status, split payments at capture with commission taken automatically, a transaction ledger in your own database, payout schedules visible to suppliers, refund policy across three parties decided and implemented, dispute handling, self-billing or commission invoicing with correct VAT treatment, supplier statements, and monthly reconciliation against the provider.

LaunchStudio has built this shape of product repeatedly and the failure modes are consistent. Behind the work is Manifera — eleven years, 120+ engineers, and platform work for clients including Vodafone, TNO and CFLW, with European client contact from Herengracht 420 in Amsterdam.

[Describe your marketplace](https://launchstudio.eu/en/#contact) before you take the first payment — this is the part that is genuinely expensive to change later.

## Real example

### The Spreadsheet That Became a Liability

Pleun Maasland built Atelierplek in Lovable: a platform where independent ceramicists and printmakers rent studio time and kiln slots from workshops across the Randstad. Customers pay per session; workshops receive the fee minus a 12 percent commission.

Her first version did the obvious thing. Payments went to Atelierplek's account, and on the fifth of each month she calculated what each of 34 workshops was owed and paid them by hand. It took her most of a day and had been wrong twice.

Two things arrived in the same month. A workshop asked why a January session had never appeared in a payout, and reconstructing the answer from bank statements and her booking table took an evening. And her accountant told her that €287,000 of gross bookings was sitting in her turnover, which changed her VAT position, made her look like a company several times her actual size, and raised the question of whether she was permitted to hold that money at all.

Eleven business days: migration to connected accounts, with all 34 existing workshops onboarded through identity verification and listings blocked until cleared; payments split at capture so the commission arrives with Atelierplek and the session fee goes directly to the workshop; a transaction ledger recording gross, commission, workshop share, VAT and payout reference for every booking; payout schedules shown in each workshop's dashboard; a refund policy for cancellations after payout, taken from the workshop's next settlement with their agreement in the terms; self-billing invoices issued to customers on behalf of workshops, with a separate monthly commission invoice to each workshop; annual statements for their own bookkeeping; and a monthly reconciliation job comparing the ledger to the provider's report.

**Result:** the manual payout day disappeared, turnover in the accounts fell to the commission Pleun actually earns, and the licensing question closed because the platform no longer holds anyone's money. In fourteen months the reconciliation job has flagged three discrepancies, all refunds processed outside the application, each resolved the same week rather than at year end.

> *"A day a month I could live with. Finding out that €287,000 of other people's money had been through my business account was the part I could not."*
> — **Pleun Maasland, Founder, Atelierplek (Haarlem)**

**Cost & Timeline:** €7,400 (connected account migration, supplier onboarding and verification gating, split payments, transaction ledger, payout visibility, three-party refunds, self-billing and commission invoicing, statements, monthly reconciliation) — completed in 11 business days.

## Frequently Asked Questions

### Can I not just collect payments and pay suppliers myself?

You can technically, and it creates regulatory exposure around holding other people's funds, inflates your turnover with money that is not yours, and leaves supplier disputes resting on your spreadsheet. Connected accounts avoid all three.

### How long does supplier onboarding take?

Days rather than minutes, because identity and bank verification involve the provider and sometimes documents. Build it as a tracked process with clear status, and do not let a supplier list anything before it completes.

### Who pays for a refund after the supplier has been paid out?

Whoever your terms say, decided before it happens. Common approaches are deducting from the supplier's next payout or holding a rolling balance. Leaving it undefined means negotiating with a supplier while a customer waits.

### Is my revenue the transaction or the commission?

The commission. Modelling it that way from the first sale keeps your accounts accurate and avoids an unpleasant conversation with your accountant about gross transaction volume in your turnover.

### Do I need my own transaction ledger if the provider has one?

Yes. You need to answer supplier questions, produce statements, and detect when your records and the provider's disagree — which happens, usually through refunds or disputes processed outside your application.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I collect marketplace payments and pay suppliers myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Technically yes, but it creates regulatory exposure around holding others' funds, inflates turnover with money that is not yours, and leaves disputes resting on a spreadsheet."
      }
    },
    {
      "@type": "Question",
      "name": "How long does marketplace supplier onboarding take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Days, because identity and bank verification involve the provider and often documents. Track it as a process and gate listings on completion."
      }
    },
    {
      "@type": "Question",
      "name": "Who pays for a refund after the supplier has been paid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Whoever your terms specify — usually deducted from the supplier's next payout or a rolling balance. Decide before it happens, not during."
      }
    },
    {
      "@type": "Question",
      "name": "Is marketplace revenue the transaction or the commission?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The commission. Model it that way from the first sale so your accounts reflect what the business actually earns."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need my own ledger if the payment provider has one?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — for supplier questions, annual statements, and detecting divergence between your records and the provider's after refunds or disputes."
      }
    }
  ]
}
</script>
