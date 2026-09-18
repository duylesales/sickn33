---
Title: "Lovable Payments: Refunds, Cancellations and Proration Without Drama"
Keywords: lovable payments, refunds, cancellation flow, proration, plan changes, chargebacks, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Payments: Refunds, Cancellations and Proration Without Drama

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Refunds, Cancellations and Proration Without Drama",
  "description": "The unglamorous half of billing in an AI-built app: cancelling at period end, prorating upgrades, issuing refunds that reach the accounting, and handling the chargeback that arrives anyway.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-refunds-cancellations-and-proration" }
}
</script>

Everyone builds the part where money comes in. Almost nobody builds the part where some of it goes back out — and that is the part your reputation is made of, because a customer who leaves cleanly tells people you were fair, and a customer who cannot find the cancel button tells rather more people rather more loudly.

There is also a regulatory edge to it in Europe, and a practical one: an app that cannot cancel properly generates support work forever.

## Cancellation Is a Product Decision Before It Is Code

Answer four questions and the implementation follows.

**When does access end?** At the end of the paid period, almost always. The customer paid through the 30th; take away access on the 30th, not the moment they click. Immediate termination on cancellation feels punitive and generates refund requests you would otherwise never see.

**Is there a refund?** For a monthly subscription, usually not — they keep the month they paid for. For an annual plan cancelled in month two, a pro-rata refund is the reasonable default and worth stating in your terms, because the alternative is arguing about it individually forever.

**What happens to their data?** Say it explicitly: retained for a defined period, exportable during that window, then deleted. This is both good practice and the answer to a question your privacy policy has to make anyway.

**Can they come back?** Reactivation should work. A returning customer with their history intact is the cheapest revenue you will ever get, and losing their data at cancellation makes returning feel like starting over.

Then make the cancel button findable. Burying it is a tactic that survives only until someone writes about it, and in the EU a subscription that is hard to exit is increasingly a legal exposure rather than a clever retention lever.

## Do Not Delete on Cancellation

The mistake appears in AI-generated code with some regularity: cancellation removes the user row, or cascades a delete across their records.

This destroys your accounting history — you still need the invoices for those payments, for years. It destroys your ability to reactivate. And it makes every "can you check whether I was charged in April?" unanswerable.

Cancellation is a state change, not a deletion. The account exists, marked cancelled, with access restricted and a retention clock running. Deletion is a separate action with its own rules, which the customer can request and which you then carry out deliberately.

## Proration: Small Feature, Large Arguments

A customer on €29 upgrades to €79 on day ten of a thirty-day cycle. What do they pay today?

The conventional answer is the difference for the unused time: roughly two thirds of €50. Both major providers calculate this for you. The trouble is that founders frequently override the behaviour without understanding it, and then cannot explain a customer's statement.

Two rules keep it sane. Upgrades take effect immediately and charge the prorated difference — the customer asked for more product now. Downgrades take effect at the end of the current period and charge the lower price from the next one — otherwise you are issuing refunds on plan changes and the arithmetic gets strange when someone changes twice in a month.

Whatever you choose, show it before they confirm: *You will be charged €33.50 today, then €79 monthly from 1 November.* One sentence, and your plan-change support load approaches zero.

## Refunds Must Land in Three Places

A refund is not complete when the provider dashboard says refunded.

It must reach **the provider**, which returns the money. It must reach **your database**, updating the payment record and any access it granted — otherwise a customer refunded in full continues using the product, and your revenue figures stay wrong. And it must reach **your accounting** as a credit note, sequentially numbered and referencing the original invoice, or your quarter will not reconcile.

Refunds issued by hand in a dashboard reliably complete only the first of the three. That is why refunding from inside your own application — a small admin action that performs all three steps together — is worth the afternoon it takes to build, long before you think you need an admin panel.

Partial refunds deserve one extra thought: decide whether they change entitlement. Refunding half of an annual plan usually should not halve their remaining access; it should either end the subscription at a date or leave it alone. Pick, write it down, implement it once.

## Chargebacks Are a Different Animal

A chargeback is not a refund. The customer went to their bank instead of to you, and the money is taken back with a fee attached, whether or not you agree.

The defence is evidence, and the evidence has to already exist: what was bought, when, by whom, from which IP and device, that terms were accepted, that the product was used, and any support correspondence. Applications that log none of this cannot contest anything.

Most chargebacks against small subscription products are not fraud. They are people who did not recognise the line on their statement. Two cheap fixes address the majority: make sure the descriptor that appears on the bank statement is your product name rather than an abbreviation nobody recognises, and email a receipt on every single charge, including renewals. A renewal that arrives silently after eleven quiet months is the classic chargeback.

## The Admin Actions Worth Having on Day One

Most billing support requests are the same handful of operations, and each one performed by hand in a provider dashboard is a chance to leave your own database out of step. A small internal page — visible only to you, with no design to speak of — pays for itself within weeks.

The set worth building first: **issue a refund** (full or partial, which updates the provider, the payment record, the entitlement and the credit note together); **cancel a subscription** on the customer's behalf, since some people will always email rather than click; **extend or credit**, for the goodwill gesture that keeps an unhappy customer; **change a plan** manually, for the deals you negotiate that your pricing page does not model; and **look up a customer's billing history**, so that answering "was I charged in April?" takes seconds.

Add one thing to each: a note field, recording who did it and why. Six months later, the question about an unusual credit on an account is answerable by reading rather than by remembering.

What does not belong here is direct editing of amounts on issued invoices, or a delete button. Every change should be an action with a recorded reason, not a field you can type over. An admin panel that can silently rewrite financial history is worse than no admin panel, because its edits leave no trace and its convenience guarantees they will happen.

Access matters too. This page performs irreversible financial operations, so it belongs behind a separate permission check rather than an `is_admin` flag that any account row can carry — and it should log every use, including the ones you make yourself.

## Write the Rules Down Before You Need Them

Every refund and cancellation decision made in the moment, under pressure, from an email that has made you feel guilty, becomes an informal policy you cannot remember and cannot apply consistently.

Write a page — internal, half a side — covering the cases that actually occur. Annual plan cancelled early: pro-rata refund of complete unused months. Monthly plan cancelled: no refund, access to period end. Customer who forgot to cancel and was charged yesterday: full refund, no argument, it costs less than the complaint. Customer who forgot for four months: one month refunded as a gesture. Downgrade mid-cycle: at period end. Service failure on your side: refund the affected period without being asked.

Two benefits, and the second is the one founders underestimate. Consistency, obviously — the same situation gets the same answer regardless of how the email was written. But also speed: a decision already made is a decision you do not spend an evening turning over, and billing correspondence is uniquely good at consuming attention that belongs to the product.

Publish the parts that affect customers in your terms, keep the rest internal, and revise it when a case arrives that the page does not cover.

## Setting This Up

For a product already billing customers this is two to three days: a self-service cancellation that ends access at period end with a stated retention and export window, reactivation that works, proration configured with upgrade-now and downgrade-later semantics and the amount shown before confirmation, refunds issued from inside your own admin so provider, database and credit note move together, partial refund semantics decided and implemented, receipts on every charge including renewals, a recognisable statement descriptor, and enough evidence logged to contest a chargeback.

LaunchStudio builds the full billing lifecycle rather than the checkout alone, under the Launch & Grow package with managed hosting at €49 per month. The engineers are Manifera's — eleven years, 160+ projects, client contact from Herengracht 420 in Amsterdam and delivery from Ho Chi Minh City.

[Tell us what happens in your app when someone cancels](https://launchstudio.eu/en/#contact).

## Real example

### The Annual Plan Nobody Could Leave

Sander Kroese built Clubkas in Lovable: subscription and dues administration for amateur sports clubs, sold on annual plans of €240 to 95 clubs across Brabant and Limburg.

Cancellation in his app was an email to Sander. He then cancelled in the Stripe dashboard, refunded when he felt it was fair, and updated a flag by hand. With 95 customers this was survivable; with the growth he wanted it was not, and it was already going wrong in ways he could see.

Two clubs had been refunded in the dashboard and kept full access for months, because nothing had changed in the database. One club was refunded twice for the same unused period, once in June and again in August when a different email reached him, and neither refund had produced a credit note. And an April chargeback had cost him €240 plus a fee with no evidence to contest it, because his app logged nothing beyond the payment itself.

Four business days: self-service cancellation ending access at period end, with a 90-day retention window, an export of the club's data available during it and reactivation that restores everything; a pro-rata refund rule for annual plans written into the terms and implemented as a single admin action that refunds through the provider, updates the payment and entitlement records, and issues a numbered credit note in one step; proration for mid-year plan changes with the amount shown before confirmation; receipts emailed on every charge including renewals; the statement descriptor changed from an abbreviation to "CLUBKAS"; and per-account logging of terms acceptance, sign-in history and usage sufficient to contest a dispute.

**Result:** cancellation emails to Sander stopped entirely, the accounting reconciled at year end without adjustment for the first time, and of the three chargebacks in the following year two were successfully contested with the logged evidence.

> *"The double refund was the moment I understood the problem. Nothing in my app knew a refund had happened, so nothing could stop me doing it twice."*
> — **Sander Kroese, Founder, Clubkas (Tilburg)**

**Cost & Timeline:** €2,600 (self-service cancellation with retention and reactivation, unified refund action with credit notes, proration, receipts, descriptor change, dispute evidence logging) — completed in 4 business days.

## Frequently Asked Questions

### Should cancellation take effect immediately or at the end of the period?

At the end of the paid period. The customer paid for it, immediate cutoff reads as punitive, and it generates refund requests you would not otherwise receive.

### Do I have to refund an annual plan cancelled early?

Not automatically, but a pro-rata refund is the reasonable default and worth stating in your terms. A written rule applied consistently prevents the case-by-case negotiation that otherwise consumes your time.

### How should upgrades and downgrades be prorated?

Upgrade immediately and charge the prorated difference; downgrade at the end of the current period at the lower price from the next one. Show the exact amount before the customer confirms.

### Why can I not just refund from the provider dashboard?

Because that updates only the provider. Your database still grants access, your revenue figures stay wrong and no credit note exists. Refund from inside your own app so all three move together.

### How do I reduce chargebacks?

Use a statement descriptor customers recognise and email a receipt on every charge, including renewals. Most chargebacks against small products are unrecognised line items rather than fraud.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should cancellation take effect immediately or at period end?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "At the end of the paid period. Immediate cutoff reads as punitive and generates refund requests you would otherwise never see."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to refund an annual plan cancelled early?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not automatically, but a stated pro-rata rule applied consistently is the reasonable default and avoids negotiating every case individually."
      }
    },
    {
      "@type": "Question",
      "name": "How should upgrades and downgrades be prorated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Upgrades immediately with the prorated difference charged; downgrades at period end. Always show the exact amount before confirmation."
      }
    },
    {
      "@type": "Question",
      "name": "Why not refund from the payment provider dashboard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It updates only the provider. Your database still grants access and no credit note exists. Refund from your own admin so provider, database and accounting move together."
      }
    },
    {
      "@type": "Question",
      "name": "How do I reduce chargebacks on a subscription product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A recognisable statement descriptor and a receipt on every charge including renewals. Most disputes are unrecognised statement lines, not fraud."
      }
    }
  ]
}
</script>
