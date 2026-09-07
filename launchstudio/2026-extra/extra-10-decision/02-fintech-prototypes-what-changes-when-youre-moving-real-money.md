---
Title: "Fintech Prototypes: What Changes When You're Moving Real Money"
Keywords: fintech prototype compliance, safeguarding client money, PSD2 SCA requirements, e-money license decision, fintech MVP production ready, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Fintech Prototypes: What Changes When You're Moving Real Money

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Fintech Prototypes: What Changes When You're Moving Real Money",
  "description": "A breakdown of why a fintech product that holds customer balances is a fundamentally different build than one that simply takes a Stripe payment, covering safeguarding, Strong Customer Authentication, and the licensing line most AI-built prototypes cross without noticing. Helps scale-up founders decide what has to change before real money touches their product.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/fintech-prototypes-what-changes-when-youre-moving-real-money" }
}
</script>

Every founder building a fintech product believes, at first, that the hard part is the Stripe integration. It isn't. Wiring up a checkout page is a well-documented afternoon of work, even for a prototype built mostly by an AI tool. The hard part — the part almost nobody budgets for, technically or financially — is the moment your product stops *processing a payment* and starts *holding a balance*. That single distinction moves you out of "add a payments provider" territory and into a regulatory category most AI-native founders have never heard of until a payment partner's onboarding team asks about it.

This matters because the two products look almost identical in a demo. Both show a balance on screen. Both let a user send money to another user. Only one of them requires you to think about safeguarding, e-money licensing, and Strong Customer Authentication before you can legally take a second customer. Knowing which one you built is the first decision, and it's cheaper to make now than after your seed round closes.

## Processing a Payment vs. Holding a Balance: The Line That Changes Everything

If your product's money flow is "customer pays you, you deliver a service, the money is yours" — a SaaS subscription, an e-commerce checkout, a one-time purchase — you are a merchant using a payment processor. Stripe or Mollie handles the regulated part; you handle the product. This is the overwhelming majority of what AI-native founders build, and it's genuinely straightforward to get production-ready.

If your product's money flow involves holding funds on behalf of a user before they choose what to do with them — a wallet, a marketplace that pays out sellers later, a savings or budgeting tool that moves money between accounts, a peer-to-peer transfer app — you are, functionally, providing a payment service. In the EU, that activity is regulated under frameworks tied to the Payment Services Directive (PSD2) and e-money rules, and depending on scale and structure, you may need to operate under your own license, become an agent of a licensed institution, or partner with a Banking-as-a-Service provider that already holds one. This is not a technical detail to configure later. It determines your entire architecture, your compliance calendar, and often your choice of payment partner.

## Why "Just Holding Balances for a Bit" Is a Different Product

Founders routinely underestimate this because the balance-holding version of a product often starts as a convenience feature. "Let's let sellers accumulate earnings before they cash out" sounds like a UX nicety. It is, legally, the difference between a checkout page and a payment institution's core function.

Once you hold client funds, even briefly, safeguarding obligations typically apply: customer money has to be kept separate from your operating funds, usually in a segregated account, so that if your company fails, customer balances aren't swept up in your creditors' claims. An AI-generated prototype has no concept of a segregated account — it has one Stripe balance and one database table tracking who's owed what, which is an accounting fiction, not a safeguarded fund. Building this properly means either partnering with a Banking-as-a-Service or e-money provider that handles safeguarding on your behalf (the common route for early-stage fintech founders) or pursuing your own license (rarely sensible before meaningful scale, given the capital and compliance overhead involved).

## Strong Customer Authentication: The Login Flow Your Prototype Doesn't Have

PSD2 requires Strong Customer Authentication (SCA) for most electronic payments within its scope — authentication using at least two independent factors from something the user knows, has, or is. In practice, this is why your bank sends a push notification or asks for a fingerprint before confirming a transfer. Most AI-built fintech prototypes authenticate with an email-and-password login and stop there, because that's what "add authentication" produces by default in Lovable, Bolt or a template.

If your product moves money and falls within SCA's scope, single-factor login is not a nice-to-have gap — it's a compliance gap. Implementing SCA properly means a second factor (an authenticator app, an SMS or push challenge, or a biometric check on device) specifically at the moment of payment authorization, not just at login, plus documented exemption logic for the low-risk transaction categories PSD2 actually allows to skip the second factor. Most payment processors and BaaS providers offer SCA-compliant flows out of the box — the founder's job is knowing to ask for it and configuring it correctly, not building it from scratch.

## The Payment Partner Decision: Processor, BaaS, or Your Own License

For a SaaS founder scaling past MVP, this is usually a three-way decision, and it's worth being deliberate about it rather than drifting into whichever provider a tutorial mentioned.

**A standard processor (Stripe, Mollie)** is right if you're taking payment for your own product or service and never holding funds on behalf of a third party. It's the cheapest, fastest, least regulatory-exposed option, and it's what the majority of SaaS and e-commerce founders should stay on for as long as the product allows it.

**A Banking-as-a-Service or e-money-as-a-service provider** (several operate specifically to serve fintech startups across the EU) is right the moment you need wallets, held balances, or multi-party payouts, but don't yet have the scale or capital to justify your own license. They hold the license; you build on their rails via API, and safeguarding, much of the compliance reporting, and often SCA infrastructure come with the partnership. This is where most funded fintech scale-ups sit for their first several years.

**Your own e-money or payment institution license** becomes worth evaluating once transaction volume and margin justify the cost of authorization, ongoing regulatory capital requirements, and a compliance function — typically a later-stage decision, not a launch decision, and one that needs specialist regulatory counsel, not a development partner.

Founders sometimes ask why they wouldn't just start with their own license to avoid a BaaS partner's revenue share. The answer is almost always capital and time: obtaining an e-money license in most EU member states involves demonstrating minimum initial capital, a fit-and-proper assessment of management, documented safeguarding and AML procedures, and typically a process measured in many months rather than weeks. For a pre-scale product still validating demand, that timeline and cost usually exceed the entire remaining runway. The BaaS route trades a percentage of transaction revenue for skipping that process entirely, which is why almost every fintech scale-up in this market takes it first and only revisits the licensing question once volume makes the economics clearly favour owning the license outright.

## What an AI-Built Fintech Prototype Almost Always Gets Wrong

Beyond the licensing question, four specific technical gaps show up repeatedly in fintech prototypes built through AI tools.

**Idempotency on financial transactions.** A retried API call or a flaky network connection should never result in a payment being processed twice. AI-generated payment code rarely implements idempotency keys correctly, which means the same "pay now" click, retried by a slow connection, can double-charge a customer or double-credit a balance.

**Reconciliation between your database and your payment provider's ledger.** Your app's database says a user has €340. Does your payment partner's ledger agree? Most prototypes have no reconciliation job at all — the two numbers simply drift apart silently until a support ticket reveals the gap, at which point nobody can say which number was ever correct.

**Audit trails on every balance-changing event.** Financial regulators and payment partners both expect an immutable log of every transaction, its timestamp, and its cause — not just a `balance` column that gets overwritten. Rebuilding this after the fact means reconstructing history you may not actually have.

**Webhook signature verification.** Payment providers notify your app of events via webhooks. An unverified webhook endpoint accepts a forged "payment succeeded" event from anyone who finds the URL — a real, exploitable gap, not a theoretical one, and one that's absent from a large share of AI-generated payment integrations by default.

## Sizing the Decision Against Your Actual Product

Not every fintech-adjacent idea needs the full weight of this article. A budgeting app that only *displays* a user's existing bank data via an open banking API (with the user's consent, through a licensed aggregator) and never moves money itself sits in a much lighter regulatory position than one that executes transfers. A marketplace that pays sellers out weekly via Stripe Connect is using a pre-built, compliant payout rail rather than becoming a payment institution itself.

The decision that actually determines your build cost and compliance load isn't "are we fintech" — it's "do we, at any point, hold or move funds we don't yet owe someone, or authenticate a payment on someone's behalf." Answer that specifically for your product before pricing an engineering engagement, because the gap between "add Stripe" and "become a payment service provider by conduct" is a gap most first-time fintech founders fall into without deciding to.

It's worth running this test against every feature on your near-term roadmap, not just your current build, because scope creep here happens one small feature at a time. "Let users tip each other," "let a team share a pooled budget," "let a customer pre-load credit for later use" — each of these, individually, looks like a minor addition to a product that started as a straightforward SaaS or marketplace. Each of them, technically, reintroduces the balance-holding question you thought you'd settled. Revisit the test whenever a feature involves money sitting anywhere other than directly in transit from payer to final recipient.

## Getting the Foundation Right Before You Talk to a Payment Partner

LaunchStudio's engineers, backed by Manifera's 11+ years of production engineering experience, can implement idempotent transaction handling, build reconciliation jobs, wire in SCA-compliant authentication flows through your chosen payment or BaaS partner, and construct the audit-logging layer regulators and partners both expect — all without rebuilding the frontend you already validated with users. What we won't do is tell you whether your specific product needs its own license; that's a conversation for a payments lawyer or a compliance consultant who can assess your actual transaction flows, and it's a conversation worth having before, not after, you sign with a BaaS provider.

Get the technical foundation solid first, and that licensing conversation goes from a six-month unknown to a scoped, answerable question. [Run your project through the price calculator](https://launchstudio.eu/en/#calculator) to see where a payments-hardening engagement lands, or [talk to an engineer who reads AI-generated code](https://launchstudio.eu/en/#contact) about what your specific money flow actually requires.

## Real example

### A Freelancer Marketplace Discovers It Was Never Just Taking a Cut

Bram Hoekstra built Vakwerk, a marketplace connecting independent tradespeople with homeowners, using Bolt for the frontend and a Supabase backend for the marketplace logic. Clients paid upfront through Stripe; Vakwerk held the funds until the job was marked complete, then paid the tradesperson their share, minus a platform fee, sometimes days or weeks later. Bram had assumed this was "just Stripe with extra steps." It wasn't — the moment Vakwerk held client funds before releasing them, it was functionally providing a payment service, not merely charging a card.

The review found the classic pattern: one pooled Stripe balance representing every client's held payment with no segregation, a database `balance` field that got overwritten on every transaction with no audit trail, no reconciliation between what Supabase said tradespeople were owed and what Stripe's actual balance held, and a webhook endpoint accepting Stripe events without signature verification. The fix routed held funds through a BaaS partner offering compliant escrow-style holding with safeguarding built in, replaced the balance field with an append-only ledger table, added a nightly reconciliation job, and closed the webhook gap.

**Result:** Vakwerk relaunched with a payment partner that handled safeguarding and reporting, letting Bram focus on marketplace growth instead of an accidental payment-institution compliance burden he'd never planned to carry.

> *"I thought I was building a marketplace with a payment feature. I was actually building a small payment institution and didn't know it until someone explained what 'holding funds' meant legally."*
> — **Bram Hoekstra, Founder, Vakwerk**

**Cost & Timeline:** €6,200 (Launch & Grow Package, ledger rebuild, BaaS integration and reconciliation) plus €49/month managed monitoring — live in 3 weeks.

## Frequently Asked Questions

### If I only use Stripe Connect for payouts, do I still need to worry about e-money rules?

Usually not to the same degree, because Stripe Connect is built specifically to let platforms pay third parties without the platform itself becoming a payment institution — Stripe holds the relevant licenses and handles much of the regulatory load. You still need to configure it correctly and understand what Stripe's terms require of you, but it's a materially lighter position than building your own balance-holding system.

### How do I know if my product needs Strong Customer Authentication?

If you're within PSD2's scope — broadly, initiating electronic payments or accessing payment accounts within the EEA — SCA generally applies unless a specific exemption fits your transaction type. Most payment processors and BaaS providers will tell you directly whether a given flow requires it, and it's worth asking explicitly rather than assuming your login screen already covers it.

### Can I launch with a processor now and move to a BaaS provider later if I need to hold balances?

Yes, and it's often the sensible order — validate the product on a simple processor while your money flow is still "customer pays for a service," and only move to a BaaS partnership once you actually need to hold or move funds on others' behalf. The migration is real work, but it's far less costly than building balance-holding infrastructure you don't yet need.

### Does being a small startup exempt me from safeguarding requirements?

No. Safeguarding obligations attach to the activity of holding client funds, not to company size. Some jurisdictions offer lighter registration regimes for smaller payment or e-money firms below certain volume thresholds, but "small" doesn't mean "exempt," and the right route (light regime, BaaS partnership, or full license) depends on specifics a compliance specialist should assess.

### What's the single most common technical mistake in AI-built fintech prototypes?

Missing idempotency on payment actions, closely followed by unverified webhooks. Both are invisible in a demo because demos don't retry failed requests or simulate forged events — they only surface once real users with unreliable connections and, occasionally, bad actors start using the product.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "If I only use Stripe Connect for payouts, do I still need to worry about e-money rules?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not to the same degree, because Stripe Connect is built to let platforms pay third parties without the platform itself becoming a payment institution. You still need to configure it correctly, but it's a materially lighter position than building your own balance-holding system."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my product needs Strong Customer Authentication?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you're within PSD2's scope, SCA generally applies unless a specific exemption fits your transaction type. Most payment processors and BaaS providers will tell you directly whether a given flow requires it."
      }
    },
    {
      "@type": "Question",
      "name": "Can I launch with a processor now and move to a BaaS provider later if I need to hold balances?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it's often sensible — validate the product on a simple processor while money simply passes through for a service, and move to a BaaS partnership once you actually need to hold or move funds on others' behalf."
      }
    },
    {
      "@type": "Question",
      "name": "Does being a small startup exempt me from safeguarding requirements?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Safeguarding obligations attach to the activity of holding client funds, not company size. Some jurisdictions offer lighter registration regimes below certain volume thresholds, but the right route depends on specifics a compliance specialist should assess."
      }
    },
    {
      "@type": "Question",
      "name": "What's the single most common technical mistake in AI-built fintech prototypes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Missing idempotency on payment actions, closely followed by unverified webhooks. Both are invisible in a demo because demos don't retry failed requests or simulate forged events."
      }
    }
  ]
}
</script>
