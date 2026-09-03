---
title: "MDR Compliance for Digital Health Software: What EU Vendors Must Prove"
keywords: "MDR compliance digital health software, EU medical device regulation vendor, digital health software vendor Europe, MDR classification software, CE marking software vendor"
buyer_stage: "Decision"
target_persona: "Compliance Officer"
---

# MDR Compliance for Digital Health Software: What EU Vendors Must Prove

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "MDR Compliance for Digital Health Software: What EU Vendors Must Prove",
  "description": "What a compliance officer needs a software vendor to demonstrate under EU MDR 2017/745 before building digital health software that qualifies as a medical device.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-06",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/mdr-compliance-for-digital-health-software-what-eu-vendors-must-prove"}
}
</script>

A digital health company building a clinical decision support tool for the German and Dutch markets assumed their software was Class I under EU MDR — the lowest-risk, self-certification tier, no Notified Body required. Their development vendor had built it that way, without ever formally running the classification logic in MDCG 2019-11 against the actual software function. Six months before launch, a regulatory consultant reviewing the file for CE marking determined the software's intended purpose — providing information used to make treatment decisions — put it squarely in Class IIa under Rule 11, which requires Notified Body involvement, and Notified Body queues for software submissions were running 9-12 months at the time. The launch delay wasn't caused by bad code. It was caused by a vendor who built first and classified later.

Choosing a vendor for EU digital health software means choosing one who treats MDR classification as the first engineering decision, not a legal afterthought discovered during CE marking prep. Under Regulation (EU) 2017/745, software can be a medical device in its own right, and the classification rules for software specifically — Rule 11 — catch far more digital health products than most first-time builders expect.

## Does Your Software Even Qualify as a Medical Device Under MDR?

MDR Article 2 defines a medical device broadly, and software qualifies when it's intended by the manufacturer for a medical purpose — diagnosis, prevention, monitoring, treatment, or providing information used for such purposes — specifically for an individual patient. MDCG 2019-11, the EU's guidance document on qualification and classification of software, is the reference every vendor should be working from. The distinction that trips up the most products: software providing general wellness information (a fitness tracker counting steps) generally isn't a medical device, but software that processes patient-specific data to inform a clinical decision usually is, even if a human clinician makes the final call. "The clinician reviews it before acting" does not automatically exempt software from MDR — this is a common and costly misunderstanding.

## Classification Under Rule 11: Why Most Digital Health Software Lands in IIa

Rule 11, introduced with MDR specifically to address standalone software, classifies based on the significance of information provided and the healthcare situation's severity. Software providing information for decisions with a serious impact on health, or used to monitor physiological processes, generally lands in Class IIa at minimum; software that could directly cause death or irreversible deterioration if it provides incorrect information can reach Class IIb or III. The practical effect: the era of digital health software defaulting to Class I self-certification largely ended with MDR's software-specific rules. A vendor who assumes Class I without running the Rule 11 analysis in writing is building against the wrong regulatory pathway, and that mistake compounds every month development continues.

## The Technical Documentation Vendors Must Produce

MDR Annex II and III specify the technical documentation required regardless of class: a general description of the device and intended purpose, design and manufacturing information, general safety and performance requirements (Annex I) with evidence of conformity, benefit-risk analysis and risk management per ISO 14971, and — for software specifically — verification and validation documentation reflecting IEC 62304 software lifecycle processes. Clinical evaluation (demonstrating clinical benefit and safety through literature review, clinical data, or clinical investigation, per MEDDEV 2.7/1 Rev 4 methodology) is required proportionate to risk class, and it's frequently underestimated for software — a well-built app with zero clinical evidence behind its claims will not clear a Notified Body review.

A capable vendor structures development so this documentation accumulates naturally: requirements traceable to design outputs, verification testing mapped to risk controls, and a clinical evaluation plan started early enough that evidence-gathering (even a modest clinical validation study) doesn't become a last-minute scramble before submission.

## The Notified Body Bottleneck

For anything above Class I, a Notified Body — an independent, EU-designated conformity assessment organization — must review the technical file and issue a CE certificate before market entry. Notified Body capacity has been a persistent bottleneck since MDR's phased implementation, with queues that have stretched well beyond a year for less-prepared submissions at various points. A vendor experienced in this process will factor Notified Body lead time into your product roadmap from the start and will know which Notified Bodies have relevant software/SaMD accreditation (not all Notified Bodies are accredited for every device category). Non-EU manufacturers additionally need an EU Authorized Representative, and your vendor should be able to explain how that role interacts with the technical file and post-market obligations, not just gesture at "you'll need one of those."

## Post-Market Surveillance Obligations

MDR doesn't end at CE marking. Manufacturers must maintain a Post-Market Surveillance (PMS) system, including a PMS plan, periodic safety update reports (for Class IIa and above), and — where relevant — Post-Market Clinical Follow-up (PMCF) to continue generating clinical evidence after launch. For software, this typically includes structured monitoring of real-world performance, user-reported issues, and any software updates that could affect the device's classification or safety profile (a "significant change" under MDR can trigger re-assessment). A vendor building the product should also be building the technical hooks — usage logging, error reporting, structured feedback capture — that make PMS operationally realistic rather than a paperwork exercise disconnected from what the software actually does.

## Vendor Questions Before You Commit

Ask a prospective EU digital health vendor to walk through their Rule 11 classification reasoning for a product like yours, in writing, before development starts. Ask which EUDAMED registration steps (the EU's device database) they've handled directly versus left entirely to you or a regulatory consultant. Confirm their approach to UDI (Unique Device Identification) assignment and labeling, and ask for a sample risk management file structure from a prior software project. A vendor fluent in this will answer in specifics — MDCG guidance numbers, Notified Body names they've worked with, actual classification outcomes from past projects — rather than general reassurance.

## Making the Call

MDR compliance for digital health software is decided in the first weeks of a project, through classification, not in the final weeks through documentation cleanup. A vendor who runs the Rule 11 analysis before writing a line of production code, structures traceability around IEC 62304 and ISO 14971 from day one, and plans for Notified Body lead time in your roadmap is the one worth hiring. Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) team builds digital health products for the European market with this classification-first discipline, and our [migration and EU cloud compliance work](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) supports the data residency requirements that often accompany MDR-regulated products. If your product also touches US markets, our companion article on [FDA 510(k) documentation requirements](https://www.manifera.com/blog/medical-device-software-vendors-fda-510k-documentation-requirements) covers the parallel American pathway.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Rule 11 Classification",
      "description": "The MDR classification rule specific to standalone software, determining device class based on the significance of information provided and the severity of the healthcare situation it addresses, which places most clinically relevant digital health software in Class IIa or above."
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Post-Market Clinical Follow-up (PMCF)",
      "description": "An ongoing obligation under MDR to continue generating clinical evidence about a device's real-world performance and safety after CE marking and market launch, feeding back into the manufacturer's post-market surveillance system."
    }
  ]
}
</script>

## Frequently Asked Questions

### Is our digital health app automatically exempt from MDR if a clinician reviews the output before acting?
No, this is a common misconception. If the software's intended purpose is to provide information used to make a clinical decision — diagnosis, treatment planning, monitoring — it typically still qualifies as a medical device under MDR regardless of downstream clinician review, and needs to go through the Rule 11 classification analysis.

### How long does Notified Body review typically take for Class IIa software?
It varies significantly by Notified Body and submission quality, but timelines of 9-12 months or longer have been common during MDR's implementation, especially for less-prepared submissions. This should be factored into product launch timelines from the earliest planning stages, not treated as a fixed final step.

### Do we need an EU Authorized Representative if our company is based outside the EU?
Yes. Non-EU manufacturers placing a device on the EU market under MDR must designate an EU Authorized Representative, who takes on specific regulatory responsibilities and serves as the contact point for EU authorities regarding the device.

### What's the difference between clinical evaluation and clinical investigation under MDR?
Clinical evaluation is the broader, ongoing process of assessing and analyzing clinical data to verify safety and performance, which can draw on literature review and equivalent device data; a clinical investigation is a specific, more resource-intensive study generating new clinical data, required when existing evidence is insufficient for the device's risk class and novelty.

### Can our software's classification change after launch if we release an update?
Yes. A "significant change" to a device's design, intended purpose, or performance characteristics can trigger a reclassification review or require updated conformity assessment, which is why the vendor's approach to change management and documentation needs to account for this ongoing obligation, not just the initial submission.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is our digital health app automatically exempt from MDR if a clinician reviews the output before acting?",
      "acceptedAnswer": {"@type": "Answer", "text": "No, this is a common misconception. If the software's intended purpose is to provide information used to make a clinical decision, including diagnosis, treatment planning, or monitoring, it typically still qualifies as a medical device under MDR regardless of downstream clinician review, and needs to go through the Rule 11 classification analysis."}
    },
    {
      "@type": "Question",
      "name": "How long does Notified Body review typically take for Class IIa software?",
      "acceptedAnswer": {"@type": "Answer", "text": "It varies significantly by Notified Body and submission quality, but timelines of nine to twelve months or longer have been common during MDR's implementation, especially for less-prepared submissions. This should be factored into product launch timelines from the earliest planning stages."}
    },
    {
      "@type": "Question",
      "name": "Do we need an EU Authorized Representative if our company is based outside the EU?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. Non-EU manufacturers placing a device on the EU market under MDR must designate an EU Authorized Representative, who takes on specific regulatory responsibilities and serves as the contact point for EU authorities regarding the device."}
    },
    {
      "@type": "Question",
      "name": "What's the difference between clinical evaluation and clinical investigation under MDR?",
      "acceptedAnswer": {"@type": "Answer", "text": "Clinical evaluation is the broader, ongoing process of assessing and analyzing clinical data to verify safety and performance, which can draw on literature review and equivalent device data. A clinical investigation is a specific, more resource-intensive study generating new clinical data, required when existing evidence is insufficient for the device's risk class and novelty."}
    },
    {
      "@type": "Question",
      "name": "Can our software's classification change after launch if we release an update?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. A significant change to a device's design, intended purpose, or performance characteristics can trigger a reclassification review or require updated conformity assessment, which is why the vendor's approach to change management and documentation needs to account for this ongoing obligation, not just the initial submission."}
    }
  ]
}
</script>
