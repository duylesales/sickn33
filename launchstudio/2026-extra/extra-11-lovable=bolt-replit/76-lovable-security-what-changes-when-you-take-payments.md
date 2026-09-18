---
Title: "Lovable Security: What Changes When You Take Payments"
Keywords: lovable security, ai app security, payment security, pci scope, webhook verification, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (non-technical)
---

# Lovable Security: What Changes When You Take Payments

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Security: What Changes When You Take Payments",
  "description": "Accepting money changes your obligations, your attackers and your blast radius. Card data and why it must never touch you, webhook forgery, refund abuse, and the audit trail money requires.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-security-what-changes-when-you-take-payments" }
}
</script>

There is a clear before and after in the life of a product, and it is not launch. It is the first real payment.

Before it, a mistake costs you an apology. After it, a mistake costs money — sometimes your customers', sometimes yours, occasionally a provider's, and it arrives with obligations attached. Your product also becomes interesting to a category of person who was not previously paying attention, because anything that moves money is worth probing.

None of this requires a security team. It requires knowing which four things change.

## Card Data Must Never Reach You

The first rule, and the one that makes everything else manageable.

Modern payment providers are built so card details go from the customer's browser to the provider, never passing through your application. You receive a token and a result. That architecture is the reason a two-person company can take payments at all — handling card data yourself pulls you into a compliance regime that is entirely out of proportion to a small product.

So the rule is absolute: never build your own card form, never log card details, never store a card number "temporarily", and never accept card details by email or over the phone into a text field in your product. Use the provider's hosted or embedded components, which is also what a generation tool will do by default if you ask for payments — the risk arrives later, when somebody asks for a "nicer" checkout and the obvious implementation collects the numbers first.

What you may store: the token, the last four digits, the card type, and your own records. That is enough for every legitimate purpose.

## The Webhook Is the Weak Point

Your provider tells you about payments by calling an address on your server. That notification is what grants access, marks an invoice paid, or ships an order — which makes it the most valuable endpoint in your product.

Three things must be true about it.

**The signature must be verified.** Every provider signs its notifications. Without verification, anyone who discovers the address can forge a successful payment and receive whatever a payment unlocks. This is a real attack and a trivially cheap one, and it is missing from generated implementations more often than it is present.

**Events must be processed once.** Providers retry, and retries are normal rather than exceptional. Record each event's identifier and ignore repeats, or a single payment becomes two subscriptions, two orders, or two shipments.

**It must be reachable.** An endpoint on a deployment that sleeps may miss notifications quietly, producing customers who paid and got nothing — the failure that generates the angriest support emails you will ever receive.

Beyond correctness, never trust an amount or a plan sent by the browser. The client can change any value it submits; the authoritative amount is the one your server told the provider, verified against what the provider reports back.

## Refunds, Credits and the Insider Case

Once money moves, some of your risk is internal.

Anyone who can issue a refund can move money out. Anyone who can change a plan can give away your product. Anyone who can edit an invoice can alter a financial record. In a company of two this feels theoretical; it stops feeling theoretical the first time you use a contractor, a support freelancer or a bookkeeper.

Four controls, none heavy. Restrict who can perform money operations. Log every one with actor, amount, reason and timestamp, in a record that cannot be edited. Require a reason field, which changes behaviour more than people expect. And consider a threshold above which a second person approves.

This is also the record that answers a bookkeeper's question at year end, so the effort pays twice.

## Fraud, Abuse and the Costs You Absorb

Two patterns worth knowing about.

**Card testing.** Automated attempts using stolen card numbers against any checkout that accepts them, to discover which still work. Your product is a convenient tool for this. The cost to you is transaction fees on hundreds of failed attempts, and potentially a conversation with your provider about your account's health. Rate limiting the checkout, requiring an account before paying, and enabling your provider's fraud tooling handle most of it.

**Chargebacks.** A customer disputes a charge and the money is reversed, often with a fee. Defending one requires evidence: what was purchased, when, by whom, from which address, and whether it was delivered or used. If your product records that, disputes are winnable; if not, they are not. This is one more argument for the audit trail.

For subscriptions there is a related discipline: when a payment fails, what should happen and when. A defined sequence — retry, notify, restrict, cancel — with each step recorded, prevents both the customer who lost access with no warning and the one who used your product free for four months.

## Invoices, VAT and Records You Must Keep

Money brings record-keeping obligations that security work should not ignore.

Invoices must be accurate, sequential and retained. In the Netherlands, business records generally must be kept for seven years, and invoices to consumers in other EU countries bring VAT rules that depend on what you sell and where the customer is. Getting this wrong is not a security incident but it is an expensive administrative one, so verify current requirements with an accountant rather than relying on a generated implementation's assumptions.

The security-relevant part: financial records must be immutable and attributable. An invoice that can be silently edited is not a record.

## What to Verify Before Your First Real Payment

Six checks, an hour.

Card details never touch your server — confirm by looking at what your checkout submits. The webhook verifies signatures — confirm by sending an unsigned request and checking it is rejected. Events are deduplicated — confirm by replaying one from the provider's dashboard. Amounts come from your server, not the browser. Money operations are restricted and logged. And a failed payment produces the behaviour you intended, tested by abandoning a real payment halfway.

That last test is the one people skip and the one that most often reveals a customer who can pay and receive nothing.

## Subscriptions Are a State Machine, Whether You Built One or Not

Most payment problems in AI-built products are not cryptographic. They are the consequence of access being granted by scattered conditions rather than by one clear rule.

**Write down the states.** Trialling, active, past due, restricted, cancelled, expired. Then write the transitions: what moves an account from one to the next, triggered by what event. Most products have five or six states and have never named any of them, so access is decided by an assortment of checks in different places that disagree with each other.

**One rule decides access.** A single function answering "may this account use the product right now?", consulted everywhere. When that logic is duplicated across the interface, the API and the scheduled jobs, the three copies drift and you end up with customers who can use the web app but not the mobile view, or who lost access on a Saturday because one copy rounded a date differently.

**Trials need an end and a limit.** An unbounded trial with no card is an invitation to repeat sign-ups, which matters enormously if your trial includes anything expensive per use. Limit the costly features during trials, cap the allowance, and check for repeated sign-ups from the same organisation rather than the same email address.

**Cancellation must be honest and immediate to request.** A customer who cannot find how to cancel disputes the charge instead, which costs you the money plus a fee plus a mark against your account. Make cancellation available in the product, confirm it by email, and state clearly when access actually ends.

**Decide what happens to the data.** On cancellation: how long is it retained, can it be exported, when is it deleted. On reactivation three months later: is it still there. These are questions customers ask before buying, and a clear answer removes a real objection.

**Test the unhappy paths deliberately.** A card that expires mid-subscription, a payment that fails on the third renewal, a customer who cancels and returns, a plan downgraded mid-period. Each one is a state transition, and each is where products quietly grant free access or cut off paying customers — both of which you discover from an angry email rather than from your own records.

## Making the Money Path Sound

For a product already taking payments, this is bounded work: the checkout verified so card data never reaches you, webhook signature verification and event deduplication implemented and tested with replayed events, amounts made authoritative on the server, the failed-payment sequence defined and recorded, money operations restricted to named roles with an immutable audit trail, rate limiting and fraud tooling enabled on the checkout, and invoicing made sequential and retained.

LaunchStudio does this alongside the rest of production readiness, because the payment path touches access control, webhooks, logging and deployment shape all at once. The engineers are Manifera's: eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us how your product takes money](https://launchstudio.eu/en/#contact) and you will get a specific list, usually within one business day, or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers.

## Real example

### Twenty-Three Subscriptions Nobody Paid For

Bas Tolhuizen built Lesgeld with Lovable: tuition and lesson-fee collection used by music schools, driving instructors and sports clubs around Roermond, handling roughly €40,000 a month across 31 organisations.

The payment integration had been generated in a single session and worked correctly for paying customers. The webhook endpoint accepted any request that reached it. It did not verify the provider's signature.

Someone found the address — it followed an obvious pattern — and sent it a forged payment-succeeded event. It worked. Over eleven days, 23 organisation accounts were activated without a single payment, several of which were then used to collect real money from real parents, with Bas's platform as the intermediary.

He discovered it during a monthly reconciliation that did not balance.

Nine business days of work: signature verification implemented on the webhook and every historical event re-validated against the provider's records, which established exactly which 23 accounts were fraudulent; event deduplication added after replay testing revealed a second issue where retried notifications had created four duplicate subscriptions over the previous months; plan and amount determination moved entirely server-side; the endpoint moved to a reliably reachable deployment after two legitimate notifications were found to have been missed during a quiet period; rate limiting and the provider's fraud tooling enabled on the checkout after evidence of card testing appeared in the logs; an immutable audit trail added for every money operation with actor and reason; refund and plan-change rights restricted to Bas and his bookkeeper; and the failed-payment sequence defined as retry, notify, restrict, cancel, with each step recorded.

The fraudulent accounts were closed and the affected parents were refunded by the payment provider. Bas covered roughly €2,100 in fees and reversals himself.

**Result:** reconciliation has balanced every month since, and the four duplicate subscriptions — which had been quietly overcharging four organisations — were found and refunded as part of the same work.

> *"Anyone who knew the address of one endpoint could tell my product that they had paid. Twenty-three of them did, and then collected money from parents through my platform."*
> — **Bas Tolhuizen, Founder, Lesgeld (Roermond)**

**Cost & Timeline:** €4,300 (webhook signature verification and historical revalidation, deduplication, server-side amounts, deployment change, fraud controls, money audit trail, dunning sequence) — completed in 9 business days.

## Frequently Asked Questions

### Can I build my own checkout form?

No. Card details must go from the customer's browser to the provider without passing through your application, using their hosted or embedded components. Handling card data yourself pulls you into a compliance regime out of all proportion to a small product.

### What is the most common payment security mistake in AI-built apps?

An unverified webhook. Every provider signs its notifications; without verifying the signature, anyone who finds the address can forge a successful payment and receive whatever payment unlocks.

### Why do duplicate subscriptions happen?

Because providers retry notifications and the endpoint processes each one. Record every event identifier and ignore repeats, then test by replaying a stored event from the provider's dashboard.

### Can I trust the amount my frontend sends?

Never. Anything the browser submits can be changed. The authoritative amount is the one your server sent to the provider, verified against what the provider reports back.

### What internal controls does taking money require?

Restrict who can refund, credit or change plans; log every money operation with actor, amount and reason in a record that cannot be edited; and consider a second approval above a threshold. This record also answers your bookkeeper and wins chargeback disputes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I build my own checkout form?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Card details must pass from the browser to the provider via their hosted or embedded components, never through your application."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most common payment security mistake in AI-built apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An unverified webhook — without signature verification, anyone who finds the address can forge a successful payment."
      }
    },
    {
      "@type": "Question",
      "name": "Why do duplicate subscriptions happen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Providers retry notifications. Record each event identifier, ignore repeats, and test by replaying a stored event."
      }
    },
    {
      "@type": "Question",
      "name": "Can I trust the amount my frontend sends?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The authoritative amount is the one your server sent to the provider, verified against what the provider reports back."
      }
    },
    {
      "@type": "Question",
      "name": "What internal controls does taking money require?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Restricted refund and plan-change rights, an immutable log of every money operation with actor and reason, and second approval above a threshold."
      }
    }
  ]
}
</script>
