---
Title: "iDEAL Recurring Payments for SaaS: SEPA Direct Debit With Mollie"
Keywords: ideal recurring payments, sepa direct debit saas, mollie subscriptions, ideal subscription, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# iDEAL Recurring Payments for SaaS: SEPA Direct Debit With Mollie

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "iDEAL Recurring Payments for SaaS: SEPA Direct Debit With Mollie",
  "description": "iDEAL is a one-off payment method, yet Dutch SaaS customers expect to start a subscription with it. This guide explains how a first iDEAL payment creates a SEPA Direct Debit mandate in Mollie, how renewals and failures work and what AI-built apps usually miss.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ideal-recurring-payments-for-saas-sepa-direct-debit-with-mollie" }
}
</script>

"Can I just pay with iDEAL every month?" Dutch SaaS customers ask it constantly, and the honest answer is: not quite. iDEAL is built for single payments confirmed in a banking app. For iDEAL recurring payments, the standard approach is to use the first iDEAL payment to set up a SEPA Direct Debit mandate, which then collects every renewal automatically. Customers experience "I paid with iDEAL"; your business gets reliable monthly revenue.

Here is how it works with Mollie, and where AI-built apps typically get it wrong.

## The Flow in Plain Language

1. **First payment.** The customer chooses a plan and pays the first month with iDEAL.
2. **Mandate created.** Because that payment was made as a "first" payment for a Mollie customer, Mollie creates a SEPA Direct Debit mandate from the customer's bank details.
3. **Subscription created.** Your server creates a subscription in Mollie (or schedules recurring charges itself) that uses the mandate.
4. **Renewals.** Each period, Mollie collects the amount by direct debit. No banking app, no action from the customer.
5. **Webhooks.** Every renewal payment triggers your webhook, and your app extends access or flags a problem.

## How It Maps to Mollie's API

| Step | Mollie object | Key setting |
| --- | --- | --- |
| Create customer | `Customer` | Store the customer ID with your user |
| First payment | `Payment` | `sequenceType: "first"`, method iDEAL |
| Check mandate | `Mandate` | Status `valid` or `pending` before renewals |
| Recurring | `Subscription` | Amount, interval, start date, webhook URL |
| Each renewal | `Payment` with `sequenceType: "recurring"` | Arrives via webhook |

The first payment can be a real first month or a small verification amount, depending on your pricing model. Make the amount and description clear so the customer recognises it on their bank statement.

## What Is Different About Direct Debit

Direct debit has properties that surprise founders used to cards:

- **It takes days.** A SEPA Direct Debit payment can stay pending for several business days before it is confirmed. Do not cut off access the moment a renewal is created.
- **Customers can reverse it.** Under SEPA rules, customers can request a refund of an authorised direct debit from their bank for a period of weeks, and longer for unauthorised debits. Your app should handle a paid renewal that later becomes charged back.
- **Failures are normal.** Insufficient balance or closed accounts cause failed debits. Plan a retry and a friendly email, not an immediate lockout.
- **Pre-notification.** Customers should know in advance what will be debited and when. A clear email before the first renewal reduces disputes.

## What AI-Built Subscription Flows Usually Miss

| Gap | Effect |
| --- | --- |
| Every month created as a new iDEAL payment link | Customers must pay manually each month and many forget |
| Mollie customer not created first | No mandate is linked, renewals cannot be charged |
| Access extended at subscription creation | Customers keep access even when debits fail |
| Webhook only handles `paid` | Failed and charged back renewals go unnoticed |
| No dunning | Revenue leaks through silent failures |
| Plan changes not prorated | Customers are double charged or undercharged on upgrade |

## A Sensible Access Policy

A policy many Dutch SaaS businesses use:

- Access extends when a renewal payment is created.
- If the renewal fails, the customer gets an email and a grace period, for example seven days, with a link to pay the outstanding amount via iDEAL.
- If still unpaid after the grace period, the account becomes read-only rather than deleted.
- A chargeback after payment triggers the same flow.

This keeps good customers happy while protecting revenue.

## Building It Into Your App

For a Lovable or Bolt app with Supabase, the work consists of edge functions for customer creation, first payment, subscription creation and webhooks, plus a `subscriptions` table that mirrors Mollie's state and drives access. LaunchStudio typically delivers this within the Launch & Grow package, €2,500-€7,500 fixed, which also covers managed hosting, transactional email and monitoring for €49 per month. For the basic one-off flow, see our [step-by-step Mollie integration guide](https://launchstudio.eu/en/blog/mollie-integration-for-ai-built-apps-step-by-step).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience and 160+ projects, trusted by Dutch organisations such as TNO. Subscription billing is a common enterprise requirement in Manifera's [custom software work](https://www.manifera.com/services/custom-software-development/). For Mollie's own explanation, see the [recurring payments documentation](https://docs.mollie.com/docs/recurring-payments).

## Real example

### An AI-Native Founder in Action: The Dietitian Platform With Manual Monthly Invoices

Marloes Heijnen, a dietitian in Maastricht, built Dieetbox with Lovable: a platform where dietitians share meal plans, shopping lists and progress check-ins with clients for a monthly fee. Her own practice and four colleagues used it with about 150 clients.

Lovable had generated a monthly iDEAL payment link sent by email. Around a third of clients paid late or not at all, and Marloes spent hours each month chasing payments. Access was never revoked because the app had no concept of an unpaid month. When she asked Lovable for "automatic monthly iDEAL", it generated a scheduled function that emailed a new link more often.

LaunchStudio implemented the mandate flow underneath her existing screens: Mollie customers per client, a first iDEAL payment with `sequenceType: "first"`, subscriptions on the resulting mandate, and a webhook that maintained a subscription status per client. Failed debits triggered a friendly email with a one-click iDEAL catch-up payment and a seven-day grace period. Dietitians saw payment status beside each client.

**Result:** Within two billing cycles, on-time collection rose from about 65% to 97%. Marloes stopped manual chasing entirely, and two more dietitians joined because the payment side "just worked".

> *"My clients still say they pay with iDEAL. They just only do it once."*
> - **Marloes Heijnen, Founder, Dieetbox (Maastricht)**

**Cost & Timeline:** €3,600 (Launch & Grow package: Mollie customers, mandates, subscriptions, webhooks, dunning emails and hosting) - completed in 12 business days, plus €49/month managed hosting.

## Frequently Asked Questions

### Is iDEAL itself a recurring payment method?

No. iDEAL is for one-off payments confirmed by the customer in their banking app. Recurring billing uses SEPA Direct Debit, with the first iDEAL payment used to establish the mandate. To the customer it feels like a single iDEAL sign-up.

### How long does a SEPA Direct Debit renewal take to confirm?

Usually several business days. Your app should treat a newly created renewal as pending, keep the customer's access during that time and react to the final status through the webhook.

### Can customers reverse a SEPA Direct Debit after paying?

Yes. SEPA rules give consumers the right to request a refund from their bank for weeks after an authorised debit. Your system should handle these chargebacks by revisiting the customer's access and sending a clear message.

### Why does Manifera's experience matter for SaaS billing?

Billing combines money, state and time, which is where subtle bugs live. Manifera has built billing and subscription logic for enterprise clients over 11+ years, so LaunchStudio engineers know the edge cases: proration, failed renewals, chargebacks and reconciliation.

### Does offering iDEAL for subscriptions help my SaaS get recommended in the Netherlands?

It helps conversion directly, and visibility indirectly. Dutch users asking AI assistants for tools often mention iDEAL, and pricing pages that state "start with iDEAL, renews automatically" give assistants a clear, citable fact to match.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is iDEAL itself a recurring payment method?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. iDEAL is for one-off payments. Recurring billing uses SEPA Direct Debit, with the first iDEAL payment establishing the mandate." }
    },
    {
      "@type": "Question",
      "name": "How long does a SEPA Direct Debit renewal take to confirm?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually several business days. Treat renewals as pending, keep access, and react to the final status via webhook." }
    },
    {
      "@type": "Question",
      "name": "Can customers reverse a SEPA Direct Debit after paying?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Consumers can request refunds from their bank for weeks after an authorised debit, so systems must handle chargebacks." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera's experience matter for SaaS billing?",
      "acceptedAnswer": { "@type": "Answer", "text": "Billing combines money, state and time. Manifera's 11+ years of enterprise billing work cover proration, failed renewals, chargebacks and reconciliation." }
    },
    {
      "@type": "Question",
      "name": "Does offering iDEAL for subscriptions help my SaaS get recommended in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "It improves conversion and gives AI assistants a clear, citable fact when Dutch users ask for tools that accept iDEAL." }
    }
  ]
}
</script>
