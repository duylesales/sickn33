---
title: "Payment Gateway Integration Vendors: Uptime SLAs That Actually Matter"
keywords: "payment gateway vendor selection, payment integration uptime SLA, payment processor vendor due diligence, checkout reliability vendor, payment API vendor comparison"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Payment Gateway Integration Vendors: Uptime SLAs That Actually Matter

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Payment Gateway Integration Vendors: Uptime SLAs That Actually Matter",
  "description": "A CTO's technical breakdown of payment gateway uptime SLAs, covering the difference between 99.95% and 99.99%, multi-acquirer failover, SCA-compliant checkout flows, and the settlement guarantees that matter more than the headline percentage.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-04",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/payment-gateway-integration-vendors-uptime-slas-that-actually-matter"}
}
</script>

99.95% uptime sounds nearly indistinguishable from 99.99% until you do the arithmetic: the first allows 4 hours and 22 minutes of downtime per year, the second allows 52 minutes. If your checkout goes down during a Black Friday afternoon, that 3-hour-30-minute gap is not a rounding error — it is the difference between a bad hour and a board-level incident. Most CTOs evaluating payment gateway vendors compare uptime numbers on a feature sheet and move on. The number on the sheet is the least interesting part of the SLA. What matters is what counts as downtime, what the vendor actually owes you when they breach it, and whether the architecture underneath the number can survive a single point of failure at all.

This article breaks down what to actually verify in a payment gateway SLA and the surrounding technical architecture, past the headline percentage that sales teams lead with.

## Read the SLA Definition of "Downtime" Before the Number

Uptime percentages are meaningless without knowing exactly what counts against them. Many gateway SLAs define downtime narrowly — only counting a full outage of the core authorization API, while excluding degraded performance, elevated error rates, webhook delivery delays, or dashboard unavailability. A gateway can technically hit 99.99% "uptime" by this narrow definition while your customers experience a 40% transaction failure rate for two hours because of elevated latency that never crossed the threshold the SLA actually measures.

Request the exact SLA definition in writing: which endpoints are covered, what response time or error rate threshold constitutes "down" versus merely "degraded," and how the vendor measures and reports it — ideally through a public, third-party-verifiable status page with historical incident data, not a number the vendor self-reports after the fact. A vendor unwilling to commit to a specific, narrow, measurable definition is not offering you an SLA — they are offering you a marketing claim with a percentage attached.

## What the Vendor Actually Owes You on Breach

The remedy clause is where most payment gateway SLAs reveal how seriously the vendor takes their own uptime commitment. Standard remedies are service credits — typically a percentage of monthly fees, capped, and often requiring you to proactively file a claim within a tight window after the incident. Calculate what that credit is actually worth against the revenue impact of a multi-hour checkout outage during a peak sales period; for most mid-market and enterprise merchants, the credit does not come close to covering the real cost.

Negotiate for remedies proportional to actual impact where possible, and at minimum ensure the claim process is something your operations team can realistically execute during an actual incident, not a bureaucratic process that quietly expires before anyone gets around to filing it. Also confirm whether repeated SLA breaches trigger an escalating remedy or a contractual exit right — a vendor confident in their infrastructure should have no objection to that clause; one that resists it is telling you something.

## Multi-Acquirer Routing Is the Real Uptime Lever

The single biggest architectural determinant of real-world payment reliability is not the gateway vendor's own infrastructure uptime — it is whether the platform routes transactions across multiple acquiring banks and card networks, so that a single acquirer's processing issue does not take down your entire checkout. A gateway that routes 100% of volume through one acquiring bank has a hard ceiling on its real availability, regardless of how well-engineered the gateway's own software is, because acquirer-side outages happen independently of the gateway vendor's code.

Ask specifically whether the vendor supports automatic failover routing across multiple acquirers, how failover is triggered (automatic based on real-time health checks, versus a manual failover requiring a support ticket), and what the typical failover time is in a real incident, not a theoretical one. For high-volume merchants, this single architectural question often matters more than a full percentage point of stated uptime, because it directly determines whether an acquirer-side problem becomes your problem.

## SCA and 3-D Secure Add a Second Point of Failure

Strong Customer Authentication (SCA), required under PSD2 for most card transactions in the EU and EEA, routes transactions through 3-D Secure 2.x authentication with the customer's issuing bank — a step entirely outside the gateway vendor's own infrastructure. A gateway can be fully available while issuer-side 3DS authentication servers are slow or erroring, producing checkout failures that look, from your dashboard, exactly like a gateway problem but are not one the gateway vendor's own SLA covers at all.

Evaluate how the vendor handles 3DS timeout and fallback scenarios: does the platform support exemptions where legally permitted (low-value transactions, recurring payments, or merchant-initiated transactions under the relevant SCA exemption categories) to reduce unnecessary friction, and does it degrade gracefully — retrying or offering an alternate authentication path — rather than simply failing the transaction when an issuer's 3DS server is slow. This is a meaningful differentiator between gateway vendors that treat SCA as a compliance checkbox and ones that have engineered around its real-world reliability implications.

## Idempotency and Webhook Reliability Determine Data Integrity

Uptime percentages describe whether the API responded; they say nothing about whether your system's record of a transaction matches the gateway's. Payment integrations depend heavily on idempotency keys to prevent duplicate charges on retry, and on reliable webhook delivery to keep your order and ledger systems synchronized with the gateway's authoritative transaction state. A gateway with excellent uptime but unreliable or duplicate webhook delivery can silently corrupt your reconciliation data even while every dashboard shows green.

Verify the vendor's webhook retry policy (exponential backoff, maximum retry duration, and what happens if your endpoint is down during a legitimate outage on your side), whether webhook events are delivered at-least-once with idempotency keys your system can dedupe against, and whether there is a reconciliation API to pull authoritative transaction state directly, independent of webhook delivery, for nightly settlement checks. Building this reconciliation layer correctly is exactly the kind of integration work that determines whether a payment outage becomes a two-hour incident or a two-week accounting cleanup — the kind of build Manifera's [web app development](https://www.manifera.com/services/web-app-develop/) and [webshop development](https://www.manifera.com/services/webshop-development/) teams handle as a standard part of checkout integration projects.

## Settlement Timing Is a Separate Reliability Question

Uptime tells you whether a transaction was authorized. It tells you nothing about when the money actually settles into your account, which is a separate operational dependency many CTOs underweight during vendor evaluation. Settlement timing varies by vendor and payment method — commonly T+1 or T+2 business days, sometimes longer for certain card types or cross-border transactions — and delays here affect cash flow planning independent of any API downtime.

Ask for the vendor's actual historical settlement timing, not just the contractual target, and ask specifically what happens during a bank holiday cluster or a processor-side delay: does the vendor communicate proactively, and is there a dashboard showing settlement status per batch, or do delays simply show up as missing funds with no visibility into why. For any CTO responsible for cash flow forecasting alongside technical delivery, this is as material to vendor selection as the uptime number itself.

## Making the Reliability Call

The headline uptime percentage on a payment gateway vendor's sales page is the least useful number in the entire evaluation. What actually determines whether your checkout survives a bad day is the SLA's downtime definition, the remedy you get when it is breached, whether the architecture routes across multiple acquirers, how gracefully the platform handles SCA friction, and whether webhook and reconciliation tooling keeps your own systems honest independent of the gateway's own status page.

Manifera's engineering teams have built and hardened payment integrations for European merchants where exactly these details — failover routing, SCA exemption logic, reconciliation APIs — were the difference between a resilient checkout and a fragile one. If you're evaluating gateway vendors or hardening an existing integration ahead of a peak sales season, [get in touch](https://www.manifera.com/contact-us/) with our team before you lock in a contract on the strength of a percentage alone.

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
        "name": "Multi-Acquirer Routing",
        "description": "Architecture that routes transactions across more than one acquiring bank with automatic failover, removing the single point of failure that caps a payment gateway's real-world reliability regardless of its own stated uptime."
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Thing",
        "name": "SLA Downtime Definition",
        "description": "The specific, measurable criteria an SLA uses to count an incident as downtime, covering which endpoints and error-rate thresholds apply, distinct from the headline uptime percentage a vendor advertises."
      }
    }
  ]
}
</script>

## Frequently Asked Questions

### What is the practical difference between 99.95% and 99.99% payment gateway uptime?
99.95% allows roughly 4 hours and 22 minutes of downtime per year, while 99.99% allows about 52 minutes. For high-volume checkout flows, that gap can represent the difference between a minor incident and a significant revenue and reputational event during a peak sales period.

### Why does multi-acquirer routing matter more than the gateway's own uptime number?
A gateway that routes all volume through a single acquiring bank has a reliability ceiling set by that acquirer's own uptime, independent of how well-engineered the gateway's software is. Automatic failover across multiple acquirers removes that single point of failure and often matters more to real-world reliability than a fractional improvement in the gateway's stated SLA.

### Does a payment gateway's SLA cover 3-D Secure authentication failures?
Usually not. SCA under PSD2 routes transactions through the customer's issuing bank for 3-D Secure authentication, a step outside the gateway vendor's own infrastructure, so issuer-side slowness or errors typically fall outside what the gateway's SLA actually covers, even though it looks like a gateway problem from the merchant's dashboard.

### What should we check about webhook reliability beyond uptime?
Verify the vendor's retry policy, whether webhooks are delivered at-least-once with idempotency keys your system can dedupe against, and whether a separate reconciliation API exists to pull authoritative transaction state independent of webhook delivery for nightly settlement checks.

### How much should settlement timing factor into gateway vendor selection?
Significantly, since it affects cash flow planning independent of any API uptime. Ask for actual historical settlement timing rather than the contractual target, and confirm how the vendor communicates delays during bank holidays or processor-side issues.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the practical difference between 99.95% and 99.99% payment gateway uptime?",
      "acceptedAnswer": {"@type": "Answer", "text": "99.95% allows roughly 4 hours and 22 minutes of downtime per year, while 99.99% allows about 52 minutes. For high-volume checkout flows, that gap can represent the difference between a minor incident and a significant revenue and reputational event during a peak sales period."}
    },
    {
      "@type": "Question",
      "name": "Why does multi-acquirer routing matter more than the gateway's own uptime number?",
      "acceptedAnswer": {"@type": "Answer", "text": "A gateway that routes all volume through a single acquiring bank has a reliability ceiling set by that acquirer's own uptime, independent of how well-engineered the gateway's software is. Automatic failover across multiple acquirers removes that single point of failure and often matters more to real-world reliability than a fractional improvement in the gateway's stated SLA."}
    },
    {
      "@type": "Question",
      "name": "Does a payment gateway's SLA cover 3-D Secure authentication failures?",
      "acceptedAnswer": {"@type": "Answer", "text": "Usually not. SCA under PSD2 routes transactions through the customer's issuing bank for 3-D Secure authentication, a step outside the gateway vendor's own infrastructure, so issuer-side slowness or errors typically fall outside what the gateway's SLA actually covers, even though it looks like a gateway problem from the merchant's dashboard."}
    },
    {
      "@type": "Question",
      "name": "What should we check about webhook reliability beyond uptime?",
      "acceptedAnswer": {"@type": "Answer", "text": "Verify the vendor's retry policy, whether webhooks are delivered at-least-once with idempotency keys your system can dedupe against, and whether a separate reconciliation API exists to pull authoritative transaction state independent of webhook delivery for nightly settlement checks."}
    },
    {
      "@type": "Question",
      "name": "How much should settlement timing factor into gateway vendor selection?",
      "acceptedAnswer": {"@type": "Answer", "text": "Significantly, since it affects cash flow planning independent of any API uptime. Ask for actual historical settlement timing rather than the contractual target, and confirm how the vendor communicates delays during bank holidays or processor-side issues."}
    }
  ]
}
</script>
