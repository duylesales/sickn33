---
Title: "Case Study: A Fintech MVP Passes PSD2 Compliance in 12 Days"
Keywords: PSD2 compliance startup, fintech MVP launch, payment security compliance, Strong Customer Authentication SaaS, SCA implementation, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Case Study: A Fintech MVP Passes PSD2 Compliance in 12 Days

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: A Fintech MVP Passes PSD2 Compliance in 12 Days",
  "description": "A fintech founder built her expense-splitting MVP in Cursor but couldn't launch until it met PSD2 Strong Customer Authentication requirements. Here's how LaunchStudio got the compliance work done in 12 business days without touching the frontend.",
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
    "@id": "https://launchstudio.eu/en/blog/fintech-mvp-passes-psd2-compliance-case-study"
  }
}
</script>

Compliance requirements don't wait for product-market fit. Lotte van der Berg learned this four weeks into her launch timeline for SplitWise Pro — a Cursor-built expense-splitting tool for Dutch freelancer collectives — when her payment processor flagged the application for missing Strong Customer Authentication handling and paused her ability to process live transactions until the issue was resolved. The product worked. The demo was polished. Users had signed up. But without SCA-compliant payment flows, every transaction over €30 would be declined by European issuers, and her payment processor wasn't going to look the other way while she figured it out.

## The Founder

Lotte van der Berg, a freelance bookkeeper in Rotterdam, built SplitWise Pro after years of manually splitting shared workspace costs, group software subscriptions, and joint vendor invoices for clients who shared expenses across three-to-eight-person freelancer collectives. She knew the problem intimately — the spreadsheets, the Tikkie requests, the monthly reconciliation emails — and she knew exactly what the product needed to do. What she didn't know was that processing group payments in Europe in 2026 meant navigating a regulatory landscape that her AI coding tool had no awareness of.

## The Prototype

Lotte used Cursor to build a full-stack application with a React frontend, a Node.js backend, and Stripe Connect for handling the multi-party payment flows (one person pays, the platform splits the amount and distributes to the collective's shared account). The prototype handled the happy path cleanly: a user entered an expense, selected which collective members to split it with, and the payment was processed through Stripe. In testing, with Stripe's test mode, everything worked flawlessly.

## The Problem

When Lotte switched from Stripe's test mode to live mode, her Stripe account was flagged within 48 hours. The issue was specific: her payment integration didn't handle the SCA challenge flow for payments that required 3D Secure authentication. In the EU, under PSD2, most card payments above €30 (and many below, depending on the issuing bank's risk assessment) require the cardholder to complete an authentication step — typically a redirect to the bank's verification page. Lotte's integration treated every payment as a single-step charge, meaning any payment that triggered an SCA challenge simply failed silently. The customer saw a generic error; the payment never completed; the expense remained unsplit.

Additionally, Stripe's review identified two structural gaps: off-session payments (recurring splits that process without the customer being actively on the site) lacked the required `payment_method` attachment and `off_session: true` flag, meaning they couldn't legally process in Europe; and the Connect onboarding flow for collective members didn't include the identity verification steps required for payouts to connected accounts under EU anti-money-laundering requirements.

## What LaunchStudio Did

Lotte found LaunchStudio through a founder in her BNI network who'd used the service for a different compliance-adjacent problem. The Manifera engineering team — drawing on experience with enterprise payment systems including projects for clients handling regulated financial transactions — scoped the compliance work into three discrete deliverables:

**SCA-compliant payment flow:** Replaced the single-step charge with Stripe's Payment Intents API, handling the `requires_action` status that triggers when the issuing bank demands 3D Secure. Added a client-side redirect to the bank's authentication page with a proper return URL, and server-side confirmation that processes the payment only after successful authentication — or notifies the user with a specific error if authentication fails.

**Off-session payment handling:** For recurring expense splits, attached the customer's payment method with explicit future-use consent (GDPR-compliant consent language included), flagged off-session payments correctly, and implemented a re-authentication flow that emails the customer a payment link when their bank requires active verification for a recurring charge.

**Connect onboarding compliance:** Added the identity verification steps (document upload, address confirmation) to the connected account onboarding flow, using Stripe's hosted onboarding to handle the regulated verification process without Lotte needing to store sensitive identity documents on her own infrastructure.

## The Result

SplitWise Pro's Stripe account was unflagged after LaunchStudio submitted the updated integration for review. The compliance work — SCA handling, off-session payments, and Connect onboarding — was completed in 12 business days. Lotte's frontend remained completely untouched; every change was backend and API-level.

Within the first month after reactivation, SplitWise Pro processed €14,200 in collective expense splits across 43 freelancer groups, with a 97% payment success rate (the 3% that failed were genuine card issues, not compliance failures). The SCA challenge flow, which would have silently killed approximately 40% of transactions without the fix, handled 126 3D Secure authentications without a single user-facing error.

> *"I didn't know PSD2 existed until my Stripe account was frozen. I definitely didn't know I could fix it without rebuilding my entire payment system. Twelve days from 'we can't process payments' to 'we're processing payments' — with the same frontend I built in Cursor."*
> — **Lotte van der Berg, Founder, SplitWise Pro (Rotterdam)**

**Cost & Timeline:** €3,200 (Launch & Grow Package, SCA compliance + Connect onboarding + off-session payments) — live in 12 business days.

---

[LaunchStudio](https://launchstudio.eu/en/) handles payment compliance the way Manifera handles enterprise security requirements — scoped, documented, and delivered without asking you to rebuild what already works.

[Tell us what you're charging for and where your customers are](https://launchstudio.eu/en/#contact) — compliance requirements vary by jurisdiction, and the fix is usually more bounded than the regulation makes it sound.

---

## Frequently Asked Questions

### Does PSD2/SCA apply to my SaaS if I'm only charging subscriptions, not processing marketplace payments?

Yes — SCA applies to virtually all electronic payments in the EEA, including standard SaaS subscriptions. Recurring charges have exemptions for some transactions, but the initial setup and any charges the issuing bank flags still require authentication.

### Can my AI-generated payment integration be made PSD2-compliant, or does it need to be rebuilt from scratch?

In most cases, the existing integration can be upgraded rather than replaced — the core change is switching from Stripe's Charges API to the Payment Intents API and adding authentication handling, which is an additive change rather than a rewrite.

### How long does Stripe take to unflag an account after compliance issues are fixed?

Stripe typically reviews updated integrations within 2–5 business days after submission. LaunchStudio provides the documentation and test evidence Stripe needs to expedite the review.

### What percentage of European payments actually trigger an SCA challenge?

It varies by issuing bank and transaction risk profile, but current data suggests 30–60% of European card payments trigger some form of SCA challenge — enough that ignoring SCA handling effectively blocks a third to half of your potential transactions.

### Does LaunchStudio handle compliance for payment providers other than Stripe?

Yes — LaunchStudio's Manifera team has implemented payment compliance for Stripe, Mollie, Adyen, and other providers. The specific compliance requirements (PSD2/SCA, PCI-DSS scope reduction) apply regardless of provider.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does PSD2/SCA apply to my SaaS if I'm only charging subscriptions, not processing marketplace payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — SCA applies to virtually all electronic payments in the EEA, including standard SaaS subscriptions. Recurring charges have exemptions for some transactions, but the initial setup and any charges the issuing bank flags still require authentication."
      }
    },
    {
      "@type": "Question",
      "name": "Can my AI-generated payment integration be made PSD2-compliant, or does it need to be rebuilt from scratch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In most cases, the existing integration can be upgraded rather than replaced — the core change is switching from Stripe's Charges API to the Payment Intents API and adding authentication handling, which is an additive change rather than a rewrite."
      }
    },
    {
      "@type": "Question",
      "name": "How long does Stripe take to unflag an account after compliance issues are fixed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stripe typically reviews updated integrations within 2-5 business days after submission. LaunchStudio provides the documentation and test evidence Stripe needs to expedite the review."
      }
    },
    {
      "@type": "Question",
      "name": "What percentage of European payments actually trigger an SCA challenge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It varies by issuing bank and transaction risk profile, but current data suggests 30-60% of European card payments trigger some form of SCA challenge — enough that ignoring SCA handling effectively blocks a third to half of your potential transactions."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio handle compliance for payment providers other than Stripe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — LaunchStudio's Manifera team has implemented payment compliance for Stripe, Mollie, Adyen, and other providers. The specific compliance requirements apply regardless of provider."
      }
    }
  ]
}
</script>
