---
title: "Open Banking API Vendors: PSD2 Compliance Checklist Before You Sign"
keywords: "open banking API vendor, PSD2 compliance software vendor, open banking integration due diligence, TPP vendor requirements, open banking vendor selection"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Open Banking API Vendors: PSD2 Compliance Checklist Before You Sign

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Open Banking API Vendors: PSD2 Compliance Checklist Before You Sign",
  "description": "A CTO's PSD2 compliance checklist for evaluating open banking API vendors, covering TPP registration, eIDAS certificates, dedicated interface performance monitoring, and the SCA reauthorization mechanics that break poorly built integrations.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-10",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/open-banking-api-vendors-psd2-compliance-checklist-before-you-sign"}
}
</script>

Every 90 days, a percentage of your users doing account aggregation will hit a re-authentication wall they were not expecting, because PSD2's Strong Customer Authentication rules require periodic reauthorization of data access consent — and if your open banking vendor has not engineered a smooth path through that wall, you will watch active users silently churn on a schedule as predictable as a calendar reminder. This is one of dozens of PSD2-specific mechanics that separate a genuinely production-ready open banking API vendor from one whose sandbox demo simply has not encountered the regulation's real edge cases yet. This article is a working checklist for a CTO evaluating open banking vendors, built around the specific regulatory technical standards that govern the space, not generic API-vendor due diligence.

## Confirm TPP Registration Status, Not Just "PSD2 Compliant" Language

Under PSD2, any entity accessing payment account data or initiating payments on behalf of users must be registered and authorized as a Third-Party Provider (TPP) — either an Account Information Service Provider (AISP), a Payment Initiation Service Provider (PISP), or both — with a national competent authority (such as the DNB in the Netherlands or the FCA in the UK, which maintains its own parallel open banking regime post-Brexit). "PSD2 compliant" as a marketing phrase says nothing about whether the vendor itself holds this authorization or whether they operate under an "agent of" arrangement with an already-authorized entity.

Ask directly: is the vendor itself an authorized AISP/PISP, and in which jurisdiction, or do they operate as an agent under someone else's authorization? Verify the registration independently through the relevant national register (EIOPA and the EBA maintain cross-border registers of authorized payment institutions) rather than accepting the vendor's own claim. A vendor operating without valid authorization, or whose authorization has lapsed, exposes your integration to an abrupt access shutdown with essentially no notice if a regulator intervenes.

## eIDAS Certificates Are the Technical Backbone of TPP Identity

PSD2 API access to banks is authenticated using eIDAS-compliant certificates — specifically Qualified Website Authentication Certificates (QWAC) for establishing the TLS connection and Qualified Electronic Seal Certificates (QSEAL) for signing API requests, both issued by a Qualified Trust Service Provider. A vendor's platform needs to manage these certificates correctly: renewal before expiry (certificate lapses are a surprisingly common cause of unplanned open banking integration outages), correct binding to the specific TPP role authorized (AISP-only certificates cannot be used for payment initiation calls), and proper handling across the multiple bank connections a real open banking integration requires, since each bank relationship technically depends on valid certificate presentation.

Ask the vendor how certificate renewal is managed operationally — is it automated with monitoring and alerting well ahead of expiry, or a manual process dependent on someone remembering a calendar date? A vendor who has had a certificate-related outage in the past and can describe concretely what changed afterward is often more trustworthy than one who claims it has never happened, since certificate expiry incidents are common enough across the industry that a credible vendor should have a specific story about handling one.

## Dedicated Interface vs. Modified Customer Interface, and the Fallback Question

Banks implementing PSD2 access typically offer either a dedicated interface (a purpose-built API for TPPs) or, in limited circumstances, allow TPPs to use a modified version of the bank's own customer-facing interface as a fallback. The Regulatory Technical Standards on Strong Customer Authentication and Common and Secure Communication (RTS on SCA & CSC) require banks offering a dedicated interface to build in a fallback mechanism unless they have obtained a specific exemption from their national competent authority, based on demonstrated interface performance and availability.

This matters to vendor selection because dedicated interface quality varies enormously across European banks — some are robust and well-documented, others are unreliable enough that TPPs rely heavily on fallback access to maintain service continuity. Ask your vendor which banks in your target markets have known dedicated interface reliability issues, and how the platform handles fallback scenarios when a specific bank's primary interface degrades. A vendor with genuine multi-bank operational experience will have a specific, current answer to this; a vendor newer to the space may not have encountered enough real bank connections yet to know.

## RTS Article 32 Performance Monitoring Obligations

The RTS on SCA & CSC requires banks to monitor the availability and performance of their dedicated interfaces and publish quarterly statistics, and separately requires that dedicated interfaces support the same level of availability and performance as the bank's own customer-facing interface. This creates a useful, publicly available due diligence signal: ask your vendor which banks in your target coverage have published poor Article 32 statistics, and how the vendor's platform handles or routes around those specific banks' known performance issues.

A vendor that treats all bank connections as uniformly reliable, without acknowledging that some banks' dedicated interfaces are measurably worse than others, has not built the kind of resilience layer — retry logic, connection health monitoring, user-facing messaging during a specific bank's known downtime window — that a mature open banking integration actually needs.

## The 90-Day SCA Reauthorization Flow Needs to Be Engineered, Not Assumed

For account information access, SCA rules generally require the end user to reauthenticate and reconfirm consent at least every 90 days, even for continuous, automated account aggregation use cases. This is not an edge case — it is a recurring, guaranteed event for every active user on your platform, and how gracefully your vendor's platform handles it directly determines your retention numbers. A poorly engineered reauthorization flow — one that silently fails, drops the user's aggregated account connection without clear in-app messaging, or requires the user to fully re-onboard rather than simply reconfirm consent — will produce a visible churn spike on a predictable 90-day cadence.

Ask the vendor to demonstrate the actual reauthorization user experience, not describe it abstractly, and ask what percentage of users successfully complete reauthorization versus drop off at that step across their existing client base. This single number is one of the most honest indicators of vendor platform maturity available, since it reflects real production experience across many banks' individual SCA implementations, which vary in friction despite the shared regulatory framework. Building the surrounding product experience around this flow well is exactly the kind of [mobile app development](https://www.manifera.com/services/mobile-app-development/) and [web app](https://www.manifera.com/services/web-app-develop/) work where the difference between a vendor's raw API and a genuinely retentive product experience gets decided.

## Sandbox-to-Production Parity Is Where PSD2 Integrations Actually Break

Nearly every open banking vendor offers a sandbox environment, and nearly every vendor's sandbox behaves more predictably and forgivingly than the real multi-bank production environment it is meant to represent. Real bank connections vary in response time, error message formatting, rate limiting behavior, and edge-case handling (a joint account, a business account with multiple authorized signatories, an account recently migrated between core banking systems at the bank's end) in ways a sandbox rarely fully replicates.

Before committing, request access to a broader pre-production testing pool covering a representative sample of the actual banks your target market requires, not just the vendor's cleanest sandbox demo banks, and budget real integration testing time against that broader set before assuming your sandbox-validated integration will behave identically in production. This single step catches a meaningful share of the integration issues that otherwise surface only after go-live.

## Making the Compliance Call

A genuinely PSD2-ready open banking vendor is defined by operational details that never make it into a sales deck: current, correctly managed eIDAS certificates; honest acknowledgment of which specific banks have unreliable dedicated interfaces; a demonstrated, low-friction 90-day SCA reauthorization flow; and verifiable TPP authorization status you can check independently rather than take on faith. A CTO who runs this checklist before signing avoids discovering these gaps during a live incident instead.

Manifera has built the integration and product layers around open banking data for European fintechs, focused specifically on making the SCA reauthorization experience and multi-bank reliability handling feel seamless to end users rather than exposing the regulation's underlying friction directly. If you're evaluating open banking vendors or need the product layer built around one you've already selected, [reach out to our team](https://www.manifera.com/contact-us/) to scope the work.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Thing",
        "name": "TPP Authorization",
        "description": "Registration as an Account Information Service Provider or Payment Initiation Service Provider with a national competent authority under PSD2, required before an entity can access payment account data or initiate payments on a user's behalf."
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Thing",
        "name": "SCA Reauthorization",
        "description": "The mandatory reconfirmation of user consent at least every 90 days for continuous account information access under PSD2's Strong Customer Authentication rules, a recurring flow that must be engineered carefully to avoid predictable churn."
      }
    }
  ]
}
</script>

## Frequently Asked Questions

### How do I verify an open banking vendor's TPP authorization independently?
Check the relevant national competent authority's register, such as the DNB in the Netherlands or the FCA in the UK, or the cross-border registers maintained by the EBA, rather than relying solely on the vendor's own "PSD2 compliant" marketing claim. Confirm whether the vendor holds authorization directly or operates as an agent under another entity's license.

### What are QWAC and QSEAL certificates and why do they matter for vendor selection?
They are eIDAS-compliant certificates used to authenticate a TPP's connection to bank APIs — QWAC for the TLS connection and QSEAL for signing API requests. Ask how the vendor manages certificate renewal operationally, since lapsed certificates are a common and avoidable cause of open banking integration outages.

### Why does the 90-day SCA reauthorization requirement matter so much for product retention?
It is a recurring, guaranteed event for every active user on an account aggregation platform, not an edge case. A poorly engineered reauthorization flow produces a visible, predictable churn spike, so the vendor's demonstrated reauthorization completion rate is one of the most honest maturity signals available during evaluation.

### What is the difference between a dedicated interface and a modified customer interface under PSD2?
A dedicated interface is a purpose-built API for TPPs, while a modified customer interface allows TPPs to use an adapted version of the bank's own customer-facing interface, generally only as a fallback when a dedicated interface lacks a specific regulatory exemption. Dedicated interface reliability varies significantly by bank, which affects real-world integration stability.

### Should we test an open banking vendor beyond their standard sandbox environment?
Yes. Sandbox environments typically behave more predictably than real production bank connections, which vary in response time, error formatting, and edge-case handling. Requesting access to a broader pre-production testing pool covering your actual target banks catches integration issues a clean sandbox demo will not surface.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I verify an open banking vendor's TPP authorization independently?",
      "acceptedAnswer": {"@type": "Answer", "text": "Check the relevant national competent authority's register, such as the DNB in the Netherlands or the FCA in the UK, or the cross-border registers maintained by the EBA, rather than relying solely on the vendor's own \"PSD2 compliant\" marketing claim. Confirm whether the vendor holds authorization directly or operates as an agent under another entity's license."}
    },
    {
      "@type": "Question",
      "name": "What are QWAC and QSEAL certificates and why do they matter for vendor selection?",
      "acceptedAnswer": {"@type": "Answer", "text": "They are eIDAS-compliant certificates used to authenticate a TPP's connection to bank APIs — QWAC for the TLS connection and QSEAL for signing API requests. Ask how the vendor manages certificate renewal operationally, since lapsed certificates are a common and avoidable cause of open banking integration outages."}
    },
    {
      "@type": "Question",
      "name": "Why does the 90-day SCA reauthorization requirement matter so much for product retention?",
      "acceptedAnswer": {"@type": "Answer", "text": "It is a recurring, guaranteed event for every active user on an account aggregation platform, not an edge case. A poorly engineered reauthorization flow produces a visible, predictable churn spike, so the vendor's demonstrated reauthorization completion rate is one of the most honest maturity signals available during evaluation."}
    },
    {
      "@type": "Question",
      "name": "What is the difference between a dedicated interface and a modified customer interface under PSD2?",
      "acceptedAnswer": {"@type": "Answer", "text": "A dedicated interface is a purpose-built API for TPPs, while a modified customer interface allows TPPs to use an adapted version of the bank's own customer-facing interface, generally only as a fallback when a dedicated interface lacks a specific regulatory exemption. Dedicated interface reliability varies significantly by bank, which affects real-world integration stability."}
    },
    {
      "@type": "Question",
      "name": "Should we test an open banking vendor beyond their standard sandbox environment?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. Sandbox environments typically behave more predictably than real production bank connections, which vary in response time, error formatting, and edge-case handling. Requesting access to a broader pre-production testing pool covering your actual target banks catches integration issues a clean sandbox demo will not surface."}
    }
  ]
}
</script>
