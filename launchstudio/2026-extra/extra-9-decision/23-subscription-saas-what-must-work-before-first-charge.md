---
Title: "Subscription SaaS: What Has to Work Before You Charge the First Card"
Keywords: subscription SaaS billing, webhook idempotency, proration and downgrades, dunning failed payments, EU VAT invoicing SaaS, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Subscription SaaS: What Has to Work Before You Charge the First Card

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Subscription SaaS: What Has to Work Before You Charge the First Card",
  "description": "Recurring billing fails quietly: duplicated webhooks, stale entitlements, proration nobody checked and invoices that don't satisfy an accountant. This article walks the subscription lifecycle and names exactly what must be correct before the first live charge.",
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
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/subscription-saas-what-must-work-before-first-charge"
  }
}
</script>

Anouk switched her billing keys from test to live on a Thursday evening, posted the launch announcement, and watched eleven subscriptions come in overnight. On Friday morning her accountant asked for the invoices. Two of them had been issued twice with the same number, one showed €0.00 because a webhook had arrived out of order, and none carried the VAT treatment required for the four customers with German company numbers. The product worked perfectly. The billing — the part that decides whether the company has revenue or a reconciliation problem — did not.

Recurring billing is the least forgiving thing an AI-built prototype tends to contain, because it fails silently and asymmetrically. A broken feature generates support tickets. Broken billing generates a number in your dashboard that is wrong in a direction you won't notice for weeks. What follows walks the lifecycle in the order money actually moves, and marks what has to be true before your first live card.

## Moment One: The Signup That Becomes a Subscription

The first decision is whether your trial takes a card. Card-up-front trials convert better on quality and worse on volume, and they change what your code must handle: a card collected today may need Strong Customer Authentication (SCA) at the moment of the first real charge weeks later, and if that authentication challenge is never surfaced to the customer, the charge simply fails. Card-free trials avoid that but need a hard expiry, a conversion flow and a rule about what happens to data at the end of an unconverted trial.

Either way, the checkout itself should go through your payment provider's hosted flow — Stripe Checkout or a Mollie-hosted payment — rather than a custom form. That is not laziness. It moves SCA handling, card-network changes and the bulk of PCI scope onto the provider, and it removes the most common prototype pattern of all: card details touching your own server because an AI tool generated a plausible-looking form.

## Webhook Idempotency Is the Boring Thing Your Revenue Depends On

Your payment provider tells you what happened through webhooks, and those webhooks retry. A network blip, a slow response, a deploy in the middle of a delivery — any of them produce the same event twice. Providers also make no guarantee that events arrive in the order they occurred, so `invoice.paid` can land before `customer.subscription.updated`.

Production handling has four parts and takes an experienced engineer an afternoon. Verify the signature on every incoming webhook, so nobody can POST a fake "payment succeeded" to your public endpoint. Store every event ID in a table with a unique constraint and drop duplicates on arrival. Acknowledge with a 200 immediately and do the real work in a background job, so a slow email send doesn't cause the provider to retry a payment event. And make every handler idempotent — setting a state rather than incrementing a counter, so processing an event twice produces the same result as processing it once.

Prototypes typically do none of these, which is how a customer ends up with two subscription rows, or an account credited twice for one payment. It is also why "our revenue number doesn't match the payment dashboard" is one of the most common questions we get from scale-up founders.

## Entitlements: Decide Where the Truth Lives

Somewhere in your code, something answers the question "is this user allowed to use this feature right now". In most prototypes the answer is a boolean column set at signup and never revisited, which means a customer who cancels keeps access forever and a customer who upgrades doesn't get theirs until they log out and back in.

The durable pattern is a single subscription record per account holding the plan, status, current period end and quantity, updated only by webhook handlers, and read by a server-side entitlement check on every protected action. Not in the frontend — the frontend can hide the button, but the API endpoint behind it is what actually needs to refuse. That distinction is where a large share of AI-generated SaaS leaks paid features: the paywall is a conditional render, and the underlying route serves anyone with a session.

Give every plan a machine-readable definition of what it includes — seat limits, feature flags, usage caps — in one place rather than scattered through conditionals. When you add your fourth plan in six months, that decision saves you a week.

## Upgrades, Downgrades and the Proration Nobody Checks

A customer on €49/month upgrades to €99/month on day 12 of a 30-day cycle. What do they pay today? Your provider can calculate the prorated difference and charge it immediately, or roll it into the next invoice, and both are defensible — but your product needs to tell the customer which, before they click, in words. The upgrade path that silently charges an unexplained €31.40 generates a support ticket and sometimes a chargeback.

Downgrades are the mirror image and are usually best applied at period end rather than immediately, because immediate downgrades create credits that complicate every subsequent invoice and let customers cycle plans to farm credit. Seat-based products need one more rule: when an account goes from 12 seats to 8, does the customer pay for 12 until renewal, and do the four removed users lose access now or then? Write these three sentences down before implementing, and put them in the UI. Half the billing complaints in early SaaS are not about the money but about the surprise.

## Failed Payments: Dunning Is a Product Surface

Cards expire, banks decline, and 3D Secure challenges go unanswered. A meaningful share of subscription churn in every SaaS is involuntary — customers who intended to keep paying and whose payment simply failed. Your provider will retry on a schedule, but retries alone recover much less than retries plus communication.

What production looks like: a defined grace period during which the account keeps working with a visible banner, an email sequence tied to the actual retry attempts rather than a generic reminder, a one-click "update payment method" link that doesn't require logging in and hunting through settings, and a final state — suspended, not deleted — that preserves the customer's data so recovery is a card update rather than a re-onboarding. Then a rule for what happens after the last retry, and a report telling you how many accounts are in each dunning stage right now. Prototypes usually implement one behaviour: cancel on first failure, which converts a fixable card problem into permanent churn.

## Cancellation, Refunds and the End State

Cancellation needs to be as easy to find as upgrading, both because EU consumer expectations are moving that way and because a hard cancellation flow produces chargebacks, which are worse than churn. Decide whether cancelling ends access immediately or at period end — period end is standard and fairer to a customer who has paid — and make reactivation before that date a single click, because a surprising number of cancellations reverse.

Then decide your data policy, because it is a support question on day one: how long you retain a cancelled account's data, whether the customer can export it, and how deletion requests are handled. GDPR gives your customer's users rights that flow through to you. Having a documented answer — even a simple one like "data retained for 90 days, exportable at any time, deleted on request within 30 days" — is worth an hour of your time and turns an anxious enterprise procurement question into a link.

## Invoices, VAT and the Accountant Test

This is where Dutch and EU SaaS diverges from the American playbook most tutorials assume. Your invoices need a sequential, gapless numbering scheme; a credit note mechanism rather than editing an issued invoice; your company details and VAT number; and the correct VAT treatment per customer. For B2B customers in another EU member state with a valid VAT number, that means reverse charge with the customer's number on the invoice and validation against the VIES service at the time of purchase — not a text field where the customer types anything they like. For consumers, it means the VAT rate of their country and OSS reporting once you pass the threshold.

Your payment provider's tax product can handle most of this, and using it is almost always cheaper than building it. What you cannot outsource is the decision to collect and validate the VAT number at checkout, store the evidence of the customer's location, and produce a downloadable invoice per payment. Retrofitting correct VAT onto a year of invoices is an accountant's project measured in days.

## The Live-Mode Checklist Nobody Runs Until It's Too Late

Test mode and live mode are different worlds, and a working test integration proves less than founders assume. Before the first real charge: webhook endpoints registered in live mode, not just test; live signing secrets in your environment, and the test ones removed; price and product IDs mapped to live equivalents rather than hardcoded test IDs; tax settings enabled in live; email receipts pointing at your live domain with SPF and DKIM configured so they don't land in spam; and a real transaction on a real card, refunded afterwards, with the resulting invoice opened and read.

That last step catches more problems than any amount of code review. Run it before you announce, not after eleven subscriptions have already arrived. Billing work of this kind sits in the SaaS range of €2,833 to €7,167 on the [LaunchStudio calculator](https://launchstudio.eu/en/#calculator), and typically takes one to two weeks rather than the quarter an agency would scope for the same thing. Behind LaunchStudio is a team of 120+ seasoned engineers, which is the reason billing plumbing gets treated as a solved problem here rather than a research exercise.

Get the lifecycle right once and it stops being something you think about. Get it wrong and every growth metric you look at for the next year has an asterisk on it. If your prototype takes money and you're unsure which of the eight moments above it actually handles, [book a 15-minute intro call](https://launchstudio.eu/en/#contact) and we'll walk your billing flow with you — or see how [Manifera](https://www.manifera.com/services/web-app-develop/), LaunchStudio's parent software company, builds web applications where the financial record has to be defensible.

## Real example

### A SaaS Founder in Action: The Month Where Revenue and Reality Disagreed

Thomas Vroegh runs Ploegkracht, a shift-planning SaaS for Dutch hospitality groups, built in Lovable and refined in Cursor. Six months after launch, 74 paying accounts and a monthly recurring revenue figure he trusted enough to put in an investor update. His bookkeeper trusted it less: the payment dashboard, the internal MRR number and the invoice ledger disagreed by roughly 9%.

The cause was three separate defects that had been invisible individually. Webhook events were processed without deduplication, so retried events had created duplicate subscription rows for eleven accounts. Downgrades were applied immediately, generating credits that the internal MRR calculation ignored. And plan entitlements lived in a cached boolean that never updated on cancellation, so six churned accounts still had full access — one of them for four months. The fix was an event ID table with a unique constraint, background-job processing behind a 200 acknowledgement, entitlements read from a single subscription record on every server-side request, and downgrades moved to period end with a clear message in the UI.

**Result:** The three numbers reconciled to the cent, six accounts that had been using the product free were converted or closed, and Ploegkracht's investor update went out with a figure the bookkeeper signed off on rather than one Thomas had to caveat.

> *"Nobody warns you that billing bugs don't look like bugs. Everything worked. The number was just wrong, in my favour, until my accountant found it — and then it was very much not in my favour."*
> — **Thomas Vroegh, Founder, Ploegkracht (Groningen)**

**Cost & Timeline:** €3,900 fixed price — webhook idempotency, entitlement rework, proration rules and invoice numbering — live in 10 business days.

---

## Frequently Asked Questions

### Do I need webhook idempotency if my payment volume is small?

Yes, because duplication is caused by retries and network conditions rather than volume, and a single duplicated event on eleven subscriptions is enough to make your revenue number wrong. An event ID table with a unique constraint plus signature verification is roughly an afternoon of work and removes the entire class of problem.

### Should upgrades charge immediately or on the next invoice?

Either is defensible as long as the customer is told before they confirm, and the amount shown matches what the card is charged. Downgrades, by contrast, are usually best applied at period end because immediate downgrades generate credits that complicate later invoices and can be gamed.

### What happens if I only cancel subscriptions after a failed payment?

You convert a fixable card problem into permanent churn, since a large share of failed payments are expired cards or unanswered authentication rather than customers choosing to leave. A grace period with retry-aligned emails and a one-click payment update link recovers a substantial portion of those accounts.

### How much of EU VAT handling can my payment provider do for me?

Most of the calculation, rate lookup and reporting support, which is almost always cheaper than building it. What remains yours is collecting and validating the customer's VAT number at checkout, storing location evidence, applying reverse charge for valid cross-border B2B customers, and issuing sequentially numbered invoices with credit notes rather than edits.

### What is the single most common billing defect in an AI-generated SaaS?

A paywall implemented as a conditional render in the frontend while the API endpoint behind it serves anyone with a valid session. Entitlement checks have to happen server-side on every protected action, because hiding a button is a design choice and not an access control.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need webhook idempotency if my payment volume is small?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, because duplication comes from retries and network conditions rather than volume, and one duplicated event across a handful of subscriptions makes your revenue number wrong. An event ID table with a unique constraint plus signature verification is about an afternoon of work."
      }
    },
    {
      "@type": "Question",
      "name": "Should upgrades charge immediately or on the next invoice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Either works as long as the customer is told before confirming and the displayed amount matches the charge. Downgrades are usually best applied at period end, since immediate downgrades create credits that complicate later invoices and can be gamed."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if I only cancel subscriptions after a failed payment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You turn a fixable card problem into permanent churn, because many failed payments are expired cards or unanswered authentication rather than deliberate cancellations. A grace period with retry-aligned emails and a one-click payment update recovers a substantial share."
      }
    },
    {
      "@type": "Question",
      "name": "How much of EU VAT handling can my payment provider do for me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most of the calculation, rate lookup and reporting support. What stays yours is validating the customer's VAT number at checkout, storing location evidence, applying reverse charge for valid cross-border B2B customers, and issuing sequentially numbered invoices with credit notes."
      }
    },
    {
      "@type": "Question",
      "name": "What is the single most common billing defect in an AI-generated SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A paywall implemented as a conditional render in the frontend while the API endpoint behind it still serves anyone with a valid session. Entitlement checks must run server-side on every protected action."
      }
    }
  ]
}
</script>
