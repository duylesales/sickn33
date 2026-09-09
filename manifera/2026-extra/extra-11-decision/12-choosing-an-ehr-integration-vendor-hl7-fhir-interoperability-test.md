---
title: "Choosing an EHR Integration Vendor: The HL7/FHIR Interoperability Test"
keywords: "EHR integration vendor selection, HL7 FHIR interoperability, electronic health record vendor due diligence, healthcare interoperability vendor, EHR API integration testing"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Choosing an EHR Integration Vendor: The HL7/FHIR Interoperability Test

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing an EHR Integration Vendor: The HL7/FHIR Interoperability Test",
  "description": "A CTO's technical framework for evaluating EHR integration vendors against real HL7 v2, FHIR R4, and Bulk Data interoperability requirements, not marketing claims.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-02",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-an-ehr-integration-vendor-hl7-fhir-interoperability-test"}
}
</script>

Most hospital systems in the US still run HL7 v2 pipe-delimited messages for the majority of their real-time clinical traffic — ADT feeds, lab results, orders — even as FHIR R4 becomes the standard for API-based data access under the ONC Cures Act Final Rule. A vendor who tells you "we do FHIR integration" without qualifying which version, which resources, and how they handle the v2-to-FHIR translation layer underneath is describing a marketing claim, not an architecture. The gap between those two statements is where EHR integration projects go three months over schedule.

Choosing an EHR integration vendor is fundamentally a test of whether they understand the standards landscape they're claiming to operate in, because "interoperability" in healthcare software is not one protocol — it's a stack of overlapping, partially-compatible standards that a competent vendor navigates deliberately and an inexperienced one stumbles through project by project.

## The Standards Landscape You're Actually Buying Into

HL7 v2.x remains the workhorse for real-time hospital messaging — ADT (admit/discharge/transfer), ORU (results), ORM (orders) — transmitted over MLLP through interface engines like Rhapsody, Cloverleaf, or Mirth Connect. It's not going away; most EHR-to-EHR and EHR-to-ancillary-system traffic inside a hospital still runs on it, and a vendor unfamiliar with segment-level v2 parsing (PID, OBX, MSH segments) will struggle with legacy interfaces that make up the bulk of real integration work.

FHIR (Fast Healthcare Interoperability Resources), currently at R4 with R5 adoption growing, is the RESTful API standard for structured data access — patient records, observations, medications — increasingly required for app-based and payer-facing integrations under ONC's information blocking rules. USCDI (United States Core Data for Interoperability) defines the minimum data classes a certified EHR must expose. SMART on FHIR defines the OAuth2-based app launch framework that lets a third-party app authenticate into an EHR session. A vendor needs fluency in all three layers — legacy messaging, RESTful FHIR, and the security framework wrapping it — because most real integration projects touch more than one.

## The FHIR Maturity Test

Before signing, run the vendor through five concrete checks rather than accepting a capabilities slide:

**1. Which FHIR version, specifically.** "FHIR support" spanning DSTU2, STU3, and R4 are not interchangeable — ask which version their integration engine targets by default and whether they've shipped R5 work yet.

**2. US Core profile conformance.** Generic FHIR resources aren't enough; ask whether their implementations conform to US Core profiles (the constrained resource definitions USCDI requires) and whether they can show a validation run against the official FHIR validator or Inferno, ONC's open-source conformance test suite.

**3. SMART on FHIR app launch experience.** If the integration involves a third-party app authenticating into Epic, Cerner (Oracle Health), or another EHR, ask for a live example of a completed SMART launch sequence they've built — the OAuth2 handshake, scope negotiation, and token refresh handling.

**4. Bulk FHIR ($export) capability.** For population-level or analytics use cases, Bulk Data Access (the FHIR $export operation) is a distinct skill from single-patient REST calls — confirm they've implemented asynchronous bulk export against a real EHR sandbox, not just single-resource GET requests.

**5. Vendor-specific API quirks.** Epic's App Orchard (now Connection Hub) and Cerner/Oracle Health's Ignite APIs both layer proprietary requirements — app registration, sandbox testing periods, production readiness reviews that can take 4-8 weeks — on top of standard FHIR. A vendor who has actually shipped through both processes will describe specific friction points; one who hasn't will describe FHIR in the abstract.

## The HL7 v2 Legacy Reality

Don't let a FHIR-forward pitch distract from legacy interface competency, because most integration budgets still go there. Ask specifically about their interface engine experience (which platforms, how many production interfaces they've built and maintained), their approach to message acknowledgment and error handling (ACK/NACK logic, retry queues), and how they handle the translation layer when a FHIR-based application needs data that only exists in a v2 ADT feed. A vendor who proposes "just migrate everything to FHIR" without acknowledging that most EHR vendors still expose v2 interfaces as the primary real-time mechanism is underestimating the project.

## Information Blocking Rule and Vendor Obligations

The ONC Cures Act Final Rule's information blocking provisions create real obligations and real leverage. Certified health IT developers (the EHR vendors themselves) are generally required to provide standardized API access without unreasonable restriction, which is useful vendor leverage — if your EHR integration vendor tells you an interface "isn't available," ask specifically whether that's a technical limitation or a business decision by the EHR vendor that could constitute information blocking. A vendor with regulatory fluency will know the difference and can help you push back through the right channel rather than accepting "the EHR won't let us" at face value.

## Vendor Evaluation Checklist

Beyond the technical test, verify: production experience with the specific EHR platforms in your environment (Epic, Oracle Health/Cerner, MEDITECH, athenahealth each have distinct integration patterns), a documented interface testing methodology (unit tests against sandbox, then a staged production cutover with parallel running), a plan for interface monitoring and alerting once live (dropped messages in a clinical feed are a patient safety issue, not just a technical bug), and references from at least one completed integration of comparable scope. If the vendor is also building custom application logic around the integration layer, [Manifera's web app development](https://www.manifera.com/services/web-app-develop/) and [custom software development](https://www.manifera.com/services/custom-software-development/) teams pair interoperability engineering with the broader product build, which avoids the handoff gap that shows up when an integration specialist and an application vendor are different companies with different incentives.

## Making the Call

The vendors worth shortlisting are the ones who can describe your specific EHR's quirks unprompted — Epic's App Orchard review cycle, Cerner's Ignite sandbox behavior, or the ADT feed format your ancillary lab system actually sends — rather than reciting FHIR as a universal solvent. Interoperability competency is demonstrated through specifics, not slide decks. Manifera's engineering teams have built both legacy HL7 v2 interfaces and FHIR-based application integrations for healthcare platforms, and our [portfolio](https://www.manifera.com/portfolio/) reflects that range. If your integration project also needs to satisfy HIPAA business associate obligations around the PHI flowing through it, see our companion piece on [the BAA clauses that actually protect you](https://www.manifera.com/blog/hipaa-compliant-software-vendors-the-baa-clauses-that-actually-protect-you) — the two decisions should happen in the same due diligence pass.

## Implementation Checklist: Scoping an EHR Integration Timeline Realistically

A production-grade HL7 v2 interface, built and tested against a single EHR endpoint with standard ADT/ORU/ORM message types, typically takes 3-6 weeks of engineering time once the interface engine and network access are in place — but that estimate roughly doubles for a non-standard ancillary system whose message segments deviate from the EHR's default implementation guide, which is common enough that "standard HL7" should never be assumed without a sample message review first. FHIR-based work follows a different curve: a single-resource, read-only FHIR integration against a well-documented sandbox can ship in 2-4 weeks, while a full SMART on FHIR app launch with OAuth2 scope negotiation and token refresh handling routinely takes 4-6 weeks on its own, before EHR vendor review even begins.

Budget the Epic App Orchard or Oracle Health Ignite review cycle as its own line item, not a buffer folded into development — 4-8 weeks is typical, and higher-risk integrations touching write-back capability or bulk data can run longer. For Bulk FHIR ($export) work specifically, confirm the vendor has handled NDJSON file output at real scale (tens of thousands of patient records, not a sandbox's few dozen test patients), since job polling and large-file handling behave very differently at production volume than in a demo. A vendor who can't give you a week-by-week breakdown across these phases, distinguishing legacy v2 work from FHIR work from vendor certification, has not actually scoped your project yet.

## Frequently Asked Questions

### Is FHIR replacing HL7 v2 entirely?
Not in the near term. FHIR is the standard for API-based, app-facing data access, but most hospitals' real-time internal messaging — ADT, orders, results — still runs on HL7 v2 through interface engines. A capable vendor needs to work fluently in both, often translating between them within the same project.

### What's the difference between FHIR DSTU2, STU3, and R4?
These are successive FHIR versions with different resource definitions and maturity levels; R4 is the current normative standard most US certified EHRs and ONC requirements target. A vendor citing "FHIR experience" without specifying the version may be working with an older, less-supported implementation.

### How do I verify a vendor's FHIR conformance claims?
Ask for evidence of testing against Inferno, ONC's open-source FHIR conformance test suite, or a validation report from the official HL7 FHIR validator. A vendor with real experience will have run these tests as a normal part of delivery and can produce results, not just describe the process.

### Why does Bulk FHIR matter separately from regular FHIR API work?
Bulk Data Access ($export) is an asynchronous, population-level data retrieval pattern distinct from single-patient REST calls, used for analytics, quality reporting, and payer data exchange. It requires different engineering — job polling, NDJSON file handling, large dataset management — that not every FHIR-competent vendor has actually implemented.

### How long does EHR vendor sandbox certification typically take?
Epic's and Oracle Health's app review and production readiness processes commonly take 4-8 weeks after development is complete, sometimes longer for higher-risk integrations. Build this into your project timeline as a distinct phase, not an afterthought tacked onto development.

### (Scenario: A CTO is comparing two integration bids where one is priced much lower for what appears to be the same HL7 v2 scope) A vendor quoted us half the time of another bidder for the same HL7 v2 interface — what should we check before trusting the lower number?
Ask both vendors whether they've actually reviewed a sample message from the specific ancillary system involved, not just assumed a standard implementation guide applies. Non-standard segment usage is common enough that a lower bid based on "standard HL7" assumptions often turns into a change order once real messages are examined.

### (Scenario: A hospital IT team is planning a bulk data export project for a quality reporting initiative) Our Bulk FHIR project only worked in the vendor's demo with a few dozen patients — is that a red flag before we scale to our full population?
Yes, treat it as unproven at production scale. Job polling behavior, NDJSON file size handling, and export completion time can all behave very differently against tens of thousands of records than against a sandbox's handful of test patients, so ask specifically for a reference project that ran Bulk FHIR at population scale before committing.

### (Scenario: A vendor's proposal doesn't distinguish between legacy interface work and FHIR work in its timeline) Should we accept a single lump-sum timeline that doesn't break out HL7 v2 work from FHIR work?
No. Legacy HL7 v2 and FHIR-based work follow genuinely different effort curves and risk profiles, and a vendor who hasn't broken out the phases likely hasn't scoped each one independently. Ask for a week-by-week breakdown that separates interface engine work, FHIR resource work, and EHR vendor certification review.

### (Scenario: A CTO is negotiating scope for an integration that includes write-back capability into the EHR) Does write-back functionality change the EHR certification review timeline compared to read-only access?
Yes, meaningfully. Write-back capability introduces additional patient safety and data integrity review at the EHR vendor level, and Epic's and Oracle Health's review cycles for write-enabled integrations commonly run longer than the standard 4-8 week window for read-only access. Confirm with the EHR vendor's own program directly rather than relying solely on your integration vendor's estimate.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is FHIR replacing HL7 v2 entirely?",
      "acceptedAnswer": {"@type": "Answer", "text": "Not in the near term. FHIR is the standard for API-based, app-facing data access, but most hospitals' real-time internal messaging, including ADT, orders, and results, still runs on HL7 v2 through interface engines. A capable vendor needs to work fluently in both, often translating between them within the same project."}
    },
    {
      "@type": "Question",
      "name": "What's the difference between FHIR DSTU2, STU3, and R4?",
      "acceptedAnswer": {"@type": "Answer", "text": "These are successive FHIR versions with different resource definitions and maturity levels; R4 is the current normative standard most US certified EHRs and ONC requirements target. A vendor citing \"FHIR experience\" without specifying the version may be working with an older, less-supported implementation."}
    },
    {
      "@type": "Question",
      "name": "How do I verify a vendor's FHIR conformance claims?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ask for evidence of testing against Inferno, ONC's open-source FHIR conformance test suite, or a validation report from the official HL7 FHIR validator. A vendor with real experience will have run these tests as a normal part of delivery and can produce results, not just describe the process."}
    },
    {
      "@type": "Question",
      "name": "Why does Bulk FHIR matter separately from regular FHIR API work?",
      "acceptedAnswer": {"@type": "Answer", "text": "Bulk Data Access, or the $export operation, is an asynchronous, population-level data retrieval pattern distinct from single-patient REST calls, used for analytics, quality reporting, and payer data exchange. It requires different engineering, including job polling, NDJSON file handling, and large dataset management, that not every FHIR-competent vendor has actually implemented."}
    },
    {
      "@type": "Question",
      "name": "How long does EHR vendor sandbox certification typically take?",
      "acceptedAnswer": {"@type": "Answer", "text": "Epic's and Oracle Health's app review and production readiness processes commonly take four to eight weeks after development is complete, sometimes longer for higher-risk integrations. This should be built into the project timeline as a distinct phase, not an afterthought tacked onto development."}
    },
    {
      "@type": "Question",
      "name": "A vendor quoted us half the time of another bidder for the same HL7 v2 interface — what should we check before trusting the lower number?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ask both vendors whether they've actually reviewed a sample message from the specific ancillary system involved, not just assumed a standard implementation guide applies. Non-standard segment usage is common enough that a lower bid based on \"standard HL7\" assumptions often turns into a change order once real messages are examined."}
    },
    {
      "@type": "Question",
      "name": "Our Bulk FHIR project only worked in the vendor's demo with a few dozen patients — is that a red flag before we scale to our full population?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, treat it as unproven at production scale. Job polling behavior, NDJSON file size handling, and export completion time can all behave very differently against tens of thousands of records than against a sandbox's handful of test patients, so ask specifically for a reference project that ran Bulk FHIR at population scale before committing."}
    },
    {
      "@type": "Question",
      "name": "Should we accept a single lump-sum timeline that doesn't break out HL7 v2 work from FHIR work?",
      "acceptedAnswer": {"@type": "Answer", "text": "No. Legacy HL7 v2 and FHIR-based work follow genuinely different effort curves and risk profiles, and a vendor who hasn't broken out the phases likely hasn't scoped each one independently. Ask for a week-by-week breakdown that separates interface engine work, FHIR resource work, and EHR vendor certification review."}
    },
    {
      "@type": "Question",
      "name": "Does write-back functionality change the EHR certification review timeline compared to read-only access?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, meaningfully. Write-back capability introduces additional patient safety and data integrity review at the EHR vendor level, and Epic's and Oracle Health's review cycles for write-enabled integrations commonly run longer than the standard 4-8 week window for read-only access. Confirm with the EHR vendor's own program directly rather than relying solely on your integration vendor's estimate."}
    }
  ]
}
</script>
