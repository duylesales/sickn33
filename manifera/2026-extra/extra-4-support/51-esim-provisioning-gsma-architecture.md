---
title: "Why an eSIM Provisioning Platform Needs to Be Built on the GSMA Remote SIM Provisioning Standard"
keywords: "custom software development, custom software engineering, software product, software system development"
buyer_stage: "Consideration"
target_persona: "A"
---

# Why an eSIM Provisioning Platform Needs to Be Built on the GSMA Remote SIM Provisioning Standard

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why an eSIM Provisioning Platform Needs to Be Built on the GSMA Remote SIM Provisioning Standard",
  "description": "A technical deep-dive into why a custom eSIM provisioning platform for MVNOs and IoT connectivity providers should be built around the GSMA SGP.22 Remote SIM Provisioning standard.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/esim-provisioning-gsma-architecture" }
}
</script>

A CTO at a mobile virtual network operator or IoT connectivity provider building a custom eSIM provisioning platform faces a foundational architecture decision with real interoperability consequences: whether the platform's remote SIM provisioning is built around GSMA's SGP.22 standard, the industry specification governing how eSIM profiles are securely provisioned onto consumer devices, or a more limited, vendor-specific provisioning approach.

## What SGP.22 Actually Standardizes

GSMA's SGP.22 specification defines the technical architecture and security protocols governing how an eSIM profile — the digital equivalent of a physical SIM card's identity and network credentials — is securely downloaded and provisioned onto a device's embedded universal integrated circuit card (eUICC). The standard defines the roles and interactions between the entity managing subscription data (the SM-DP+, Subscription Manager Data Preparation), the entity coordinating profile discovery for the device (the SM-DS, Subscription Manager Discovery Service), and the device's own eSIM management interface, establishing a consistent, secure provisioning flow that works across compliant devices regardless of manufacturer.

## Why Deviating From This Standard Creates a Real Device Compatibility Problem

An eSIM provisioning platform built around a simplified or non-compliant implementation of remote SIM provisioning risks a direct, practical consequence: modern consumer devices with eSIM capability, across major device manufacturers, expect to interact with an SGP.22-compliant provisioning backend specifically, and a platform that deviates from the standard's defined security and communication protocols may simply fail to provision correctly on a meaningful share of real devices, or require ongoing, fragile device-specific workarounds to achieve compatibility that a standards-compliant implementation wouldn't need. For an MVNO or connectivity provider whose actual business depends on being able to provision service onto whatever specific device a real customer brings, this isn't a minor technical nuance — it's a direct constraint on the provider's actual addressable customer base.

## Why This Matters Even More for IoT-Specific Deployments

For IoT connectivity providers specifically, GSMA maintains a related but distinct specification, SGP.32, addressing the specific remote provisioning needs of IoT devices, which often have different constraints than consumer smartphones — devices that may need remote provisioning without direct user interaction, or that need to support profile switching across different network operators as a device moves between coverage areas or business relationships change. An IoT connectivity platform built without this IoT-specific provisioning model in mind, assuming the consumer-device-oriented provisioning flow translates directly, risks building a platform poorly suited to the actual operational requirements of many real IoT deployment scenarios, where devices frequently can't rely on the same user-interactive provisioning flow a consumer smartphone naturally supports.

## What Building Standards-Compliant Provisioning Actually Requires

- **Implementing genuine SM-DP+ and, where applicable, SM-DS functionality according to the GSMA specification**, rather than a simplified approximation that handles common cases but deviates from the standard's defined security and communication protocols in edge cases.
- **Undergoing GSMA compliance testing and certification** for the platform's provisioning implementation, since formal certification is often what actually confirms genuine interoperability with the real device ecosystem, rather than a platform's own internal testing against a limited set of test devices.
- **Building profile lifecycle management (download, enable, disable, delete) as genuinely robust, standards-compliant functionality**, since real-world eSIM management involves ongoing lifecycle events beyond initial provisioning, and a platform's compliance needs to extend across the full profile lifecycle, not just the initial download step.

## Why This Gap Often Isn't Visible Until Real Launch Volume Is Reached

A specific reason simplified, non-certified provisioning implementations like Mobilnost Nova's below tend to pass internal testing convincingly: a development team's internal test device set is naturally limited, both in raw device count and in how representative it is of the actual device diversity a real, launched customer base brings. A provisioning flow that works correctly across a team's own limited test devices provides a genuinely reassuring, but ultimately incomplete, signal, since the specific edge cases in eSIM implementation that vary meaningfully between device manufacturers and even between different models from the same manufacturer are precisely the cases a small, non-representative test set is least likely to happen to include. This is a specific instance of a broader testing principle worth naming directly: a testing approach that validates the common, expected path thoroughly can still miss a meaningful share of real-world failure modes that only exist in the specific diversity a small internal test set structurally can't represent, no matter how carefully that limited set is tested against.

This is precisely the gap formal GSMA compliance certification is designed to close, since certification testing is specifically built around the standard's full range of defined behaviors and edge cases, informed by the broader industry's collective experience with where real interoperability problems tend to occur, rather than being limited to whatever specific device diversity a single development team happens to have direct access to internally.

## Why This Decision Also Shapes an MVNO's Ability to Support New Device Launches Quickly

A related, practical business consideration worth naming directly: as device manufacturers release new devices with updated eSIM implementations, an MVNO or connectivity provider whose provisioning platform is built on genuine standards compliance is considerably better positioned to support new devices quickly and reliably, since compliance with the shared standard is what new devices are themselves being built and validated against by their manufacturers. A provider running a simplified, non-compliant implementation faces a recurring risk with each significant new device launch: discovering, often only after real customers begin attempting to provision the new device, that the platform's specific deviations from the standard create a new compatibility gap requiring urgent, reactive correction, precisely the kind of ongoing operational burden a genuinely standards-compliant platform avoids by design. This makes standards compliance not just a one-time launch-readiness consideration, but an ongoing operational efficiency factor that compounds in value with every new device generation the platform needs to support over its operational lifetime.

## Manifera's Approach: Building eSIM Provisioning Platforms on Certified, Standards-Compliant Architecture

- **Amsterdam (Governance/Standards-Compliant Provisioning Scoping):** Dutch project leads scope eSIM provisioning platforms around genuine GSMA SGP.22 and, where relevant, SGP.32 compliance from the initial architecture phase, positioning the platform for broad real-world device compatibility.
- **Vietnam (Execution/Certified Provisioning Engineering):** The engineering pod builds SM-DP+ and provisioning lifecycle functionality designed to pass genuine GSMA compliance testing, avoiding the device compatibility gaps a simplified implementation risks.

This is Dutch Management × Vietnamese Mastery applied to eSIM provisioning platform development itself: governance that scopes provisioning architecture around genuine industry standards compliance, paired with execution capable of building certified, broadly compatible provisioning infrastructure. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) approach for MVNO and IoT connectivity platforms.

## Case Study: A Maribor MVNO's Provisioning Platform Correction

Mobilnost Nova, a Maribor-based MVNO, had launched its eSIM provisioning platform with a simplified implementation that handled the most common device provisioning scenarios adequately during initial testing but hadn't undergone formal GSMA compliance certification. Following launch, customer support began receiving a meaningful volume of provisioning failures specifically from certain device models whose particular implementation of the eSIM standard exposed edge cases the simplified platform hadn't correctly handled.

Manifera's Amsterdam team rebuilt the platform's SM-DP+ implementation to genuine GSMA SGP.22 compliance, guided the platform through formal GSMA compliance certification, and rebuilt profile lifecycle management to handle the full range of standard-defined lifecycle events robustly.

> *"We'd tested against the devices we had in the office and things looked fine. It turned out real customers had a much wider range of devices than our test set, and 'mostly compliant' wasn't actually good enough once we saw the real failure pattern across our actual customer base."*
> — **CTO, Mobilnost Nova**

Mobilnost Nova's provisioning failure rate dropped substantially following certification and the platform rebuild, and the company now treats formal GSMA compliance certification as a non-negotiable requirement for any provisioning platform change, rather than relying on internal testing against a limited device set.

## Simplified Provisioning Implementation vs. Certified, Standards-Compliant Architecture

| Factor | Simplified Provisioning Implementation | Certified, Standards-Compliant Architecture |
|---|---|---|
| Device compatibility | Works for common cases, fails on edge cases | Broad compatibility across compliant devices |
| Validation approach | Internal testing against limited device set | Formal GSMA compliance certification |
| IoT-specific scenarios | Often not addressed | SGP.32 considerations built in where relevant |
| Profile lifecycle handling | May be incomplete | Full standard-defined lifecycle supported |

## Scoping Your Own eSIM Provisioning Platform's Architecture

Before building or launching an eSIM provisioning platform, build genuine GSMA SGP.22 (and where relevant, SGP.32) compliance into the core architecture and pursue formal certification — a simplified implementation that works in limited internal testing risks real device compatibility failures once it meets the actual diversity of real customer devices. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about building a certified, standards-compliant eSIM provisioning platform.

## Frequently Asked Questions

### (Scenario: CTO scoping an eSIM provisioning platform) What is GSMA SGP.22, and why does it matter for a provisioning platform's architecture?

SGP.22 is the industry specification governing how eSIM profiles are securely provisioned onto devices, and compliance is often what actually confirms genuine interoperability with the real, diverse device ecosystem.

### (Scenario: engineering lead deciding on implementation rigor) Why is internal testing against a limited device set insufficient for eSIM provisioning?

Different devices can expose edge cases in their specific eSIM implementation, and internal testing against a limited device set can miss compatibility issues that only surface once the platform meets the actual diversity of real customer devices.

### (Scenario: IoT connectivity provider evaluating provisioning needs) Does the standard consumer eSIM provisioning model work well for IoT deployments?

Not always directly — GSMA's SGP.32 addresses IoT-specific provisioning needs like non-interactive provisioning, and a platform built assuming the consumer flow translates directly may be poorly suited to real IoT operational requirements.

### (Scenario: MVNO evaluating platform readiness) Why does formal GSMA compliance certification matter beyond a platform's own internal testing?

Certification validates genuine interoperability against the standard's full requirements and real device ecosystem behavior, providing a level of assurance internal testing against a necessarily limited device set can't fully replicate.

### (Scenario: CTO evaluating a development team's telecom experience) What should I ask a development team about their eSIM provisioning platform experience?

Ask specifically whether their SM-DP+ implementation has undergone formal GSMA compliance certification and how they handle full profile lifecycle management, not just initial provisioning — genuine experience produces a specific, technical answer.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO scoping an eSIM provisioning platform) What is GSMA SGP.22, and why does it matter for a provisioning platform's architecture?", "acceptedAnswer": { "@type": "Answer", "text": "SGP.22 governs secure eSIM profile provisioning, and compliance confirms genuine interoperability with the real device ecosystem." } },
    { "@type": "Question", "name": "(Scenario: engineering lead deciding on implementation rigor) Why is internal testing against a limited device set insufficient for eSIM provisioning?", "acceptedAnswer": { "@type": "Answer", "text": "Different devices can expose edge cases limited internal testing misses, surfacing only against real customer device diversity." } },
    { "@type": "Question", "name": "(Scenario: IoT connectivity provider evaluating provisioning needs) Does the standard consumer eSIM provisioning model work well for IoT deployments?", "acceptedAnswer": { "@type": "Answer", "text": "Not always — SGP.32 addresses IoT-specific needs like non-interactive provisioning that the consumer flow doesn't directly cover." } },
    { "@type": "Question", "name": "(Scenario: MVNO evaluating platform readiness) Why does formal GSMA compliance certification matter beyond a platform's own internal testing?", "acceptedAnswer": { "@type": "Answer", "text": "Certification validates interoperability against the full standard and real device behavior beyond what internal testing can replicate." } },
    { "@type": "Question", "name": "(Scenario: CTO evaluating a development team's telecom experience) What should I ask a development team about their eSIM provisioning platform experience?", "acceptedAnswer": { "@type": "Answer", "text": "Ask whether their SM-DP+ implementation has undergone GSMA certification and how they handle full profile lifecycle management." } }
  ]
}
</script>
