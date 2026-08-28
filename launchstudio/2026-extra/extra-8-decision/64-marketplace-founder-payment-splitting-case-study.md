---
Title: "Case Study: A Marketplace Founder Gets Payment Splitting Right the First Time"
Keywords: marketplace payment splitting, Stripe Connect marketplace, multi-party payments SaaS, platform payment processing, payment split compliance, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Case Study: A Marketplace Founder Gets Payment Splitting Right the First Time

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: A Marketplace Founder Gets Payment Splitting Right the First Time",
  "description": "A marketplace founder in Amersfoort needed payment splitting — buyers pay, sellers receive, the platform takes a cut. Stripe Connect handles this, but the implementation isn't a one-button setup. Here's how LaunchStudio got it right before a single real euro was processed.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/marketplace-founder-payment-splitting-case-study"
  }
}
</script>

Marketplace payments are a different animal from SaaS subscriptions. In a SaaS product, one party pays you and you keep the money — a straight line. In a marketplace, a buyer pays, a seller receives, and the platform takes a percentage — a triangle, with tax obligations, payout schedules, identity verification requirements, and refund policies that differ depending on which corner of the triangle you're standing in. Joris Kuipers discovered this structural complexity three weeks into building HulpMarkt, a Lovable-built platform connecting Dutch homeowners with local handymen for small repair jobs, when he realized that "add payments" didn't mean adding a payment button — it meant designing a three-party financial flow with compliance requirements he'd never encountered.

## The Founder

Joris Kuipers, a former property manager in Amersfoort, knew the small-repair market intimately. Homeowners needed someone to fix a leaky faucet, hang a heavy mirror, or replace a broken tile — jobs too small for a licensed contractor but too tricky for most people to DIY. Local handymen wanted these jobs but had no efficient way to find them. HulpMarkt was the matchmaker: homeowners posted jobs, handymen bid on them, and the platform took a 12% service fee from the handyman's payout.

## The Problem

Joris had built the marketplace frontend in Lovable — job postings, bidding, messaging, profile pages, reviews — and it worked beautifully as a demo. The payment question seemed simple: buyer pays for the job, platform takes 12%, handyman receives 88%. Stripe handles marketplace payments. Done.

Except Stripe Connect, the product designed for exactly this use case, has three distinct integration models (Standard, Express, and Custom), each with different onboarding requirements, payout timelines, and platform responsibilities. The wrong choice would either require handymen to create full Stripe accounts themselves (Standard — high friction, many would drop off), give the platform too little control over the payout experience (Express — limited customization), or saddle Joris with compliance obligations he wasn't equipped to handle (Custom — the platform becomes responsible for identity verification, tax reporting, and dispute management).

Additionally, HulpMarkt's payment flow had a timing complication: the buyer needed to pay when accepting a bid, but the handyman should only receive the payout after the job was marked complete and the homeowner confirmed satisfaction — an escrow-like hold that Stripe supports through delayed payouts but that requires specific API configuration and careful state management between the job's lifecycle and the payment's lifecycle.

## What LaunchStudio Did

The Manifera engineering team, drawing on experience with multi-party payment flows from enterprise marketplace projects, structured the engagement around three decisions and their implementations:

**Connected Account Model:** Express accounts — the right balance for HulpMarkt's use case. Handymen go through a streamlined onboarding flow (identity verification handled by Stripe, not by the platform), and the platform retains control over payout timing without taking on Custom-level compliance responsibilities. LaunchStudio implemented the Express onboarding flow as a seamless step in the handyman registration process.

**Payment Flow with Escrow Hold:** When a homeowner accepts a bid, a Payment Intent is created with an `application_fee_amount` representing HulpMarkt's 12% and a `transfer_data[destination]` pointing to the handyman's connected account. The charge is captured immediately (money leaves the homeowner's card), but the transfer to the handyman's account is delayed until the job is marked complete. If the homeowner reports an issue, the platform can hold or refund without the handyman having already received the funds.

**Payout and Refund Logic:** After job completion, the transfer to the handyman's connected account triggers automatically. Stripe's payout schedule then handles moving money from the connected account to the handyman's bank account. For disputes and refunds, the system handles three scenarios: full refund (job not completed), partial refund (job completed but with issues — the platform mediates), and refund after payout (the platform covers the refund from its own balance and debits the handyman's next payout).

## The Result

HulpMarkt launched with a payment flow that handled the full triangle — buyer charges, platform fees, seller payouts, escrow holds, and refund scenarios — from day one. The handyman onboarding flow (Stripe Express) took an average of 4 minutes to complete, with a 91% completion rate. In the first two months, the platform processed €23,400 in job payments, collected €2,808 in platform fees, and handled three refund scenarios (two full, one partial) without manual intervention.

> *"I thought 'add Stripe' would take an afternoon. The marketplace payment flow — escrow, splits, refunds, identity verification — was the single most complex part of my entire product, and I had no idea until I started trying to build it."*
> — **Joris Kuipers, Founder, HulpMarkt (Amersfoort)**

**Cost & Timeline:** €3,400 (Launch & Grow Package, Stripe Connect Express integration + escrow flow + refund handling + handyman onboarding) — live in 13 business days.

---

[LaunchStudio](https://launchstudio.eu/en/) builds marketplace payment flows that handle the full triangle — not just the charge, but the split, the hold, the payout, and the refund — backed by Manifera's experience with enterprise multi-party financial systems.

[Describe your marketplace and how money should flow between the parties](https://launchstudio.eu/en/#contact) — the payment architecture is usually the hardest part, and it's better to get it right before your first real transaction.

---

## Frequently Asked Questions

### Do I need Stripe Connect, or can I handle marketplace payments with a regular Stripe account?

For a true marketplace where buyers pay and sellers receive, Stripe Connect is the correct infrastructure. A regular Stripe account only handles payments to a single entity (you), making proper payment splitting and seller payouts either impossible or non-compliant.

### How long does it take for a seller to complete the Stripe Express onboarding process?

Typically 3–5 minutes — the seller provides basic identity information, Stripe handles verification in the background, and most accounts are active within minutes. The conversion rate is significantly higher than Standard accounts, which require sellers to create full Stripe dashboards.

### What happens if a buyer disputes a charge after the seller has already been paid out?

LaunchStudio configures the platform to cover disputes from its own balance and recover the amount from the seller's next payout — a standard marketplace practice that prevents the buyer from being stuck without recourse and gives the platform a clear escalation path.

### Can I use Mollie instead of Stripe for marketplace payment splitting?

Mollie supports multi-party payments through its Connect feature, but the implementation model differs from Stripe Connect. LaunchStudio's Manifera team can implement either, depending on whether the marketplace primarily serves Dutch customers (Mollie's iDEAL support is stronger) or international ones (Stripe's global coverage is broader).

### What percentage platform fee is typical for a two-sided marketplace?

Platform fees vary widely — from 5% for high-ticket services to 30% for low-ticket gig work — and the right percentage depends on your market, competition, and the value the platform provides. The payment infrastructure supports any percentage; the business decision is yours.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need Stripe Connect, or can I handle marketplace payments with a regular Stripe account?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a true marketplace where buyers pay and sellers receive, Stripe Connect is the correct infrastructure. A regular Stripe account only handles payments to a single entity, making proper payment splitting either impossible or non-compliant."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it take for a seller to complete the Stripe Express onboarding process?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically 3-5 minutes — the seller provides basic identity information, Stripe handles verification in the background, and most accounts are active within minutes."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if a buyer disputes a charge after the seller has already been paid out?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio configures the platform to cover disputes from its own balance and recover the amount from the seller's next payout — a standard marketplace practice that prevents the buyer from being stuck without recourse."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use Mollie instead of Stripe for marketplace payment splitting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mollie supports multi-party payments through its Connect feature. LaunchStudio can implement either, depending on whether the marketplace primarily serves Dutch customers or international ones."
      }
    },
    {
      "@type": "Question",
      "name": "What percentage platform fee is typical for a two-sided marketplace?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Platform fees vary from 5% for high-ticket services to 30% for low-ticket gig work. The payment infrastructure supports any percentage; the business decision is yours."
      }
    }
  ]
}
</script>
