---
Title: "Lovable Payments: What Breaks After the Customer Clicks Pay"
Keywords: lovable payments integration, Stripe Mollie webhook reconciliation, AI app payment security, failed payment handling, subscription state, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Payments: What Breaks After the Customer Clicks Pay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: What Breaks After the Customer Clicks Pay",
  "description": "Test-mode checkout is the easy half. What decides whether your app can actually charge people is webhook handling, reconciliation, failed payments and refunds — the parts AI builders leave out.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-what-breaks-after-checkout" }
}
</script>

There is a moment of genuine triumph when a test payment succeeds. The checkout opens, the card number goes in, the page says paid, and your prototype has just become a business.

Then someone pays with a real card, closes the tab before the confirmation loads, and disappears. Your app has no record of their payment. Your payment provider has their money. Your customer has an email receipt from a provider they have never heard of and no access to the thing they bought. That situation — not the checkout — is what payment integration actually is, and it is the part AI builders almost never produce.

## The Half That Gets Built

Ask Lovable, Bolt or Cursor to add payments and you will reliably get: a button, a call to the payment provider, a redirect to a hosted checkout page, and a success page the customer returns to.

That is a correct and useful piece of work. It is also the half of the flow where nothing important is decided, because the customer's browser is an unreliable narrator. It can close, crash, lose signal, or be closed deliberately the moment the money leaves. Anything your app learns only from the returning browser is something your app will sometimes not learn.

## The Half That Decides Whether You Have a Business

**Webhooks.** Your payment provider sends your server a message when something happens: payment succeeded, payment failed, subscription renewed, chargeback opened. This is the authoritative channel, because it does not depend on the customer's browser. An integration without webhook handling is an integration that knows only what customers stay online long enough to tell it.

**Verification.** Those incoming messages must be checked against a signing secret to confirm they came from the provider. Without verification, anyone who learns your endpoint address can tell your app that a payment succeeded.

**Idempotency.** Providers retry messages, sometimes several times, by design. If your handler grants access on every message, a retry becomes a duplicate order, a double-credited balance or two subscriptions.

**Reconciliation.** A weekly comparison between what the provider says it collected and what your database says was paid. This is how you find the gaps you did not know about, and almost no small product does it.

**Failure states.** Cards expire. Direct debits fail days later. Banks decline for reasons nobody shares. Your app needs behaviour for each: retry, notify, restrict access, and — crucially — restore access cleanly when the customer fixes it.

**Refunds and cancellations.** Issued in the provider's dashboard, which your app may never hear about unless it is listening. A customer who was refunded and still has access is a small loss; a customer who cancelled and still gets charged is a complaint and a chargeback.

## The Dutch Specifics Worth Knowing

If you are selling in the Netherlands, iDEAL is not optional in practice. A significant share of Dutch consumers expect it, and a checkout offering only cards will lose conversions in a way your analytics will attribute to pricing.

That usually means Mollie or Stripe, both of which support it, with different strengths: Mollie's local payment method coverage and Dutch-language support are strong, while Stripe's subscription tooling and developer ecosystem are more extensive. Either is a reasonable choice, and switching later is a real project, so it is worth an hour of thought before the first integration.

Two other local realities. Direct debit — incasso — is common for recurring business payments and settles slowly, which means "paid" arrives days after the customer agreed. And VAT handling for digital products sold across EU borders has rules that your accountant should see before your first hundred invoices, not after.

## Test Mode Is Not a Rehearsal

Every provider offers test credentials, and they are essential. They are also a simplified world: test payments succeed instantly, test webhooks arrive immediately, and no bank is involved.

Before launch, run at least one small real transaction end to end. Pay with your own card. Close the tab immediately after confirming, before the redirect completes, and check whether your app granted access anyway. Refund it in the provider dashboard and check whether access was revoked. Then let a subscription renew once, if you sell subscriptions.

Founders resist this because it feels like ceremony over a few euros. Those few euros buy you the only evidence that matters.

## The Access Question Underneath

Payments are not really about money moving; they are about entitlement. Your app has to answer one question reliably at any moment: is this person currently allowed to use this?

In AI-built apps that answer is frequently stored as a single field set once at checkout — a boolean that says paid. It cannot express "paid but refunded", "subscription expired", "payment failed and we are retrying", "cancelled but valid until the end of the period", or "on a plan they downgraded last week".

The result is either customers who lose access they paid for or customers who keep access they stopped paying for, and both erode trust in a business that is otherwise working. Entitlement needs to be derived from the payment state, not set once and forgotten.

## A Pre-Launch Payment Checklist

- One real transaction completed, with the tab closed before the redirect.
- Webhook endpoint live, signature-verified, and handling retries without duplicating anything.
- A refund issued and access correctly revoked.
- A failed payment simulated, with the customer notified and access handled.
- Subscription cancellation tested, including access lasting to the end of the paid period.
- Provider totals compared against your database for the test period.
- VAT treatment confirmed with whoever does your books.

Seven items, most of them an hour each. Skipping them does not produce an error — it produces a slow accumulation of customers whose situation your app cannot describe.

## Getting Payments Actually Finished

This is one of the most common reasons an AI-built product cannot launch, and it is bounded work. LaunchStudio builds the half that generation leaves out: verified webhook handling with idempotency, entitlement derived from payment state rather than a single flag, failure and dunning behaviour, refund and cancellation handling, reconciliation, and a live-mode test pass before anything goes public. Payment integration is explicitly part of the [Launch & Grow package](https://launchstudio.eu/en/#packages), alongside hosting and monitoring.

The frontend you built stays as it is, and the code stays documented and AI-readable so you can keep iterating. The engineers are Manifera's — eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

If your checkout works and you are not certain what happens after it, [describe your project](https://launchstudio.eu/en/#contact) and you will get a specific answer within one business day.

## Invoices, VAT and What Your Accountant Will Ask For

Taking payments is a commercial act before it is a technical one, and the administrative half is where AI-built products are most consistently incomplete. None of this is difficult; all of it is painful to reconstruct a year later.

**Invoices need to be real invoices.** A payment confirmation email is not one. For business customers in particular, an invoice needs your company details, a Chamber of Commerce registration number, a VAT identification number where applicable, the customer's details, a date, a unique sequential number, the amount excluding VAT, the VAT rate and amount, and the total. Generated apps typically send a friendly receipt containing none of this, and business customers cannot file it.

**Numbering must be sequential and gapless.** Invoice numbers that restart, duplicate or skip create exactly the kind of question you do not want in an audit. If your app issues invoices, the numbering belongs in the database with a constraint, not in application logic that runs twice under load.

**VAT treatment depends on who is buying and where.** Selling digital services to consumers in another EU country, to businesses with a valid VAT number, and to customers outside the EU are three different treatments. Reverse charge rules, validation of a customer's VAT number and the thresholds that apply to cross-border digital sales are all real considerations, and they are your accountant's territory rather than your developer's.

**Records have to be retained.** Dutch administrative obligations require keeping your business records for a number of years, which means invoices generated by your app must be stored durably rather than regenerated on demand from data that may change.

**Refunds and credit notes are separate documents,** not a deleted invoice. Once an invoice is issued, correcting it means issuing a credit note, and an app that simply deletes rows makes that impossible.

The practical sequence: decide with your accountant what your invoices must contain and how VAT is treated before your first hundred customers, then have that implemented once. Retrofitting compliant invoicing across a year of transactions is significantly more expensive than building it correctly at the start, and it always happens under time pressure.

## Testing Payments Without Irritating Your Bank

Founders hesitate to run live-mode tests because it feels wasteful or, worse, like something that might flag their account. Neither is true, and a small amount of care makes the exercise painless.

**Use the smallest amount your provider allows** for the live test, then refund it. Refunds within minutes are entirely ordinary and no provider treats them as suspicious.

**Test with a card and with iDEAL separately,** because they behave differently: bank redirect flows introduce a return step where the tab can be closed, which is exactly the failure you are trying to provoke.

**Do the abandonment test deliberately.** Start the payment, complete it at the bank, then close the tab before the redirect finishes. Your app should still grant access, via the webhook, within seconds.

**Trigger a failure on purpose.** Most providers document test scenarios that produce declines and errors even in live mode for specific amounts or methods — check their documentation rather than improvising with a real declined card.

**Then check three places:** your app's database, the provider dashboard, and the customer's email. All three should agree. If they do not, you have found the gap before a customer did.

## Real example

### A Subscription Box With Nineteen Customers Nobody Was Charging

Lieke Verbeek's app, Kruidenbox, sold monthly herb-growing subscriptions to home gardeners, built in Lovable with Mollie for payments. The first month went perfectly: 140 subscribers, money arriving, boxes shipped.

The problem appeared in month three, when her accountant asked why revenue had not grown despite subscriber numbers rising. Reconciliation had never been done, and it revealed three separate faults. Nineteen subscriptions had failed to renew — expired cards and a changed bank account — and because there was no webhook handling for failed renewals, those customers had kept full access and kept receiving boxes for two months without paying. Four customers who had cancelled were still being charged, because cancellation updated her database but never told Mollie. And two payments had been recorded twice because the webhook endpoint had no idempotency check and Mollie had retried.

Seven business days of work: webhook handling rebuilt with signature verification and idempotency, entitlement derived from live payment state rather than a one-time flag, a dunning flow that emails customers on failed renewal and suspends after two attempts, cancellation wired through to the provider, and a weekly reconciliation report delivered to her inbox.

**Result:** the nineteen lapsed subscribers were contacted, eleven reinstated, the four over-charged customers were refunded before any chargeback was filed, and monthly revenue matched provider settlements exactly from the following cycle onwards.

> *"I thought the payment integration was the part I had finished. It turned out to be the part I had started."*
> — **Lieke Verbeek, Founder, Kruidenbox (Utrecht)**

**Cost & Timeline:** €3,300 (Launch & Grow scope: webhooks, entitlement model, dunning and reconciliation) — completed in 7 business days.

## Frequently Asked Questions

### My checkout works. Why is that not enough?

Because the checkout only tells you what the customer's browser reported. Payments that complete after the tab closes, renewals, failures, refunds and chargebacks all arrive through webhooks, which is the channel most AI-built apps never implement.

### Do I need webhooks for one-off payments too?

Yes. A customer closing the tab after paying is the most common single failure, and without webhook handling your app simply never learns the payment succeeded while the provider has taken the money.

### Should I use Stripe or Mollie in the Netherlands?

Both work and both support iDEAL, which Dutch customers expect. Mollie has strong local payment coverage and Dutch support; Stripe has broader subscription tooling. Choose before the first integration, because switching later is a real project.

### How do I know whether my payment records are correct?

Reconcile: compare your provider's settlement totals against your own database for the same period, every week at first. Discrepancies are normal to find and much cheaper to fix in the first month than in the first year.

### What happens if a customer disputes a charge?

Your provider notifies you through a webhook, often with a deadline for responding with evidence. An app that does not handle chargeback events leaves you finding out from a balance adjustment, usually after the window to contest it has closed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "My checkout works. Why is that not enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The checkout only reports what the customer's browser saw. Payments completing after the tab closes, renewals, failures, refunds and chargebacks arrive through webhooks, which AI-built apps rarely implement."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need webhooks for one-off payments too?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A customer closing the tab after paying is the most common failure, and without webhooks your app never learns the payment succeeded while the provider has the money."
      }
    },
    {
      "@type": "Question",
      "name": "Should I use Stripe or Mollie in the Netherlands?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both work and both support iDEAL, which Dutch customers expect. Mollie has strong local coverage and Dutch support; Stripe has broader subscription tooling. Choose before the first integration."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know whether my payment records are correct?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reconcile weekly: compare provider settlement totals against your database for the same period. Discrepancies are normal to find and far cheaper to fix early."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if a customer disputes a charge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The provider notifies you via webhook, often with a response deadline. An app that ignores chargeback events leaves you finding out from a balance adjustment after the contest window closed."
      }
    }
  ]
}
</script>
