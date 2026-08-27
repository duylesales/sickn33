---
title: "GDPR Data Processing Agreements: What a Software Vendor Contract Must Include"
keywords: "GDPR data processing agreement vendor, DPA software vendor contract, GDPR compliance software vendor, data processing agreement clauses, EU data protection vendor contract"
buyer_stage: "Decision"
target_persona: "Compliance Officer"
---

# GDPR Data Processing Agreements: What a Software Vendor Contract Must Include

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "GDPR Data Processing Agreements: What a Software Vendor Contract Must Include",
  "description": "A Compliance Officer's checklist for what a GDPR Data Processing Agreement with a software development vendor must legally include, covering Article 28 requirements, subprocessor management, breach notification timelines, international transfers, and audit rights.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/gdpr-data-processing-agreements-what-a-vendor-contract-must-include"}
}
</script>

A software vendor emails over their "standard contract" and mentions, almost in passing, that a Data Processing Agreement is "included as an addendum, happy to sign whatever you need." For a Compliance Officer, that sentence should trigger more scrutiny, not less — a vendor treating the DPA as an interchangeable formality rather than a document with specific legal content is signaling that GDPR compliance sits somewhere below "sign quickly and move on" on their priority list. Under Article 28 of the GDPR, a Data Processing Agreement isn't optional boilerplate; it's a legally mandated contract between a controller and any processor handling personal data on the controller's behalf, and its content is specified in enough detail that a generic template rarely satisfies it without careful review.

Getting the DPA right at the vendor selection stage matters more than almost any other document in the contract stack, because the controller — your company, in nearly every vendor relationship covered by this cluster — retains regulatory liability for how a processor handles personal data, even when the processor is the party that actually mishandles it. A weak or generic DPA doesn't just create legal risk in the abstract; it removes your ability to demonstrate accountability to a regulator or auditor when something goes wrong. This article walks through what Article 28 actually requires and the specific clauses a Compliance Officer should verify before a vendor contract gets signed.

## What Article 28 Actually Requires — Not Just "GDPR Compliant" Language

Article 28(3) of the GDPR lists specific, mandatory content for any processing agreement: the subject matter and duration of processing, the nature and purpose of processing, the type of personal data and categories of data subjects involved, the controller's obligations and rights, and a defined set of processor obligations including processing only on documented instructions, ensuring confidentiality commitments from anyone with data access, implementing appropriate technical and organizational security measures, and assisting the controller in fulfilling data subject rights requests and regulatory obligations. A DPA that simply states the vendor "will comply with GDPR" without addressing these specific elements does not meet the legal standard, regardless of how confidently it's presented.

The practical test for a Compliance Officer reviewing a vendor's proposed DPA: read it against the Article 28(3) list item by item. If any element is missing or addressed only in vague, non-specific language, that's a negotiation point to raise before signature, not an assumption to make afterward. In a review of vendor DPAs submitted during procurement processes at mid-market European companies, a notable share — commonly cited around one in three in practitioner surveys — were found to be missing at least one Article 28(3) required element on first submission, which suggests this gap is common enough that assuming a vendor's first draft is complete is a genuine risk, not an overcautious formality.

## Subprocessor Authorization and the Notification Requirement

A processor is required under Article 28(2) to obtain the controller's prior authorization — either specific or general — before engaging a subprocessor to handle any of the controller's personal data. Under general authorization, the processor must inform the controller of any intended changes concerning the addition or replacement of subprocessors, giving the controller the opportunity to object. A DPA silent on this notification mechanism, or one that authorizes subprocessors broadly with no ongoing visibility, leaves a Compliance Officer with no practical way to track who actually has access to the organization's data over the life of the contract.

The clause worth insisting on: a current, named list of subprocessors attached to the DPA as a living exhibit, a defined notification window (commonly 14 to 30 days) before any new subprocessor is engaged, and a genuine right to object that isn't rendered meaningless by an unreasonably short response window. Ask specifically how a vendor updates this list in practice — a vendor with a real process will have an example to show you; one without will describe intentions rather than mechanics.

## Breach Notification Timelines Tighter Than the GDPR Baseline

GDPR requires a controller to notify the relevant supervisory authority of a personal data breach within 72 hours of becoming aware of it. That 72-hour clock starts when the controller becomes aware — but if a processor is the one who discovers the breach, the controller only "becomes aware" once the processor tells them, which makes the processor's own notification speed the actual constraint on your regulatory compliance timeline. A DPA that simply commits a processor to notify "without undue delay" gives you no real operational guarantee, because "undue delay" is elastic enough to consume most of your 72-hour window before you've even started your own assessment.

A well-drafted DPA specifies a concrete processor-to-controller notification deadline meaningfully shorter than 72 hours — commonly 24 to 48 hours — precisely so the controller retains enough time within the regulatory window to assess the breach, prepare notification content, and file with the supervisory authority. This is one of the clauses most frequently left at GDPR's vague default language rather than tightened to something operationally usable, and it's worth pushing for explicitly during negotiation rather than accepting the statutory minimum framing as if it were sufficient for your own compliance timeline.

## International Data Transfers and Standard Contractual Clauses

If a vendor's processing involves any transfer of personal data outside the EU/EEA — including remote access by engineers based outside the region, even without data physically relocating — the DPA needs to address the transfer mechanism explicitly: which Standard Contractual Clauses module applies, whether a transfer impact assessment has been completed for the destination jurisdiction, and what supplementary technical measures (encryption, pseudonymization, access controls) are in place given the post-Schrems II requirement to evaluate destination-country surveillance and access laws, not simply rely on SCCs as a checkbox. This is a frequent point of confusion for Compliance Officers evaluating offshore development vendors, since a well-governed offshore engagement can operate entirely within EU-hosted infrastructure — the DPA should specify this architecture explicitly rather than leaving the question to inference from where the vendor's office happens to be located. Manifera's engagements are structured around [migrating and hosting client infrastructure in GDPR-compliant EU cloud regions](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) specifically so that this section of the DPA can be answered with architecture, not just contractual promises.

## Audit Rights and End-of-Contract Data Handling

Article 28(3)(h) requires that a DPA make available to the controller all information necessary to demonstrate compliance and allow for audits, including inspections, conducted by the controller or an appointed auditor. A DPA that limits this to the vendor's own self-certifications or a third-party report the vendor selects unilaterally falls short of a genuine audit right — the clause should preserve the controller's ability to request a specific audit, with reasonable notice and scope limitations to protect the vendor's other clients' confidentiality, rather than being fully substituted by a generic compliance certificate.

Equally important is the end-of-contract data handling clause: Article 28(3)(g) requires the processor to delete or return all personal data at the end of the provision of services, at the controller's choice, and delete existing copies unless retention is required by law. A DPA should specify a concrete timeline for this deletion or return — commonly 30 to 90 days post-termination — and, ideally, a certification of deletion the vendor provides as documented proof, not just a contractual promise taken on faith.

## Making the Final Call

A generic DPA "addendum" that a vendor treats as an afterthought is a warning sign worth taking seriously, not a formality to sign quickly to keep procurement moving. The specific clauses covered here — complete Article 28(3) content, a living subprocessor list with real notification mechanics, breach notification timelines tighter than the regulatory baseline, explicit international transfer architecture, and genuine audit and deletion rights — are what separate a DPA that actually protects your organization's regulatory position from one that merely exists as a signed document in a file.

Manifera provides a complete, Article 28-compliant DPA as standard with every engagement, including a maintained subprocessor list, a 24-hour internal breach notification commitment to clients, and EU-region hosting architecture documented explicitly rather than left to inference. Across 160+ delivered projects and clients spanning the EU, Singapore, and APAC, our compliance documentation has held up under client-side regulatory and customer audits without requiring last-minute amendments.

If your organization is finalizing a vendor contract and wants its proposed DPA reviewed against the Article 28 checklist before signature, our Amsterdam team can walk through it with your legal or compliance function directly.

## Frequently Asked Questions

### Is a Data Processing Agreement legally required, or just best practice?
It's legally required under Article 28 of the GDPR whenever a processor handles personal data on a controller's behalf. It is not optional boilerplate, and its content is specified in enough detail under Article 28(3) that a generic or incomplete template can fail to meet the legal standard.

### What happens if a vendor's subprocessor causes a data breach?
The controller retains regulatory liability and must notify the supervisory authority within 72 hours of becoming aware of the breach. Because that clock starts when the processor informs the controller, the DPA should require the processor to notify the controller well within that window — commonly 24 to 48 hours — not merely "without undue delay."

### Does using an offshore development team automatically require special GDPR transfer clauses?
It depends on whether personal data or remote access crosses outside the EU/EEA, not simply where the vendor's engineers are physically located. A well-governed offshore engagement can operate entirely within EU-hosted infrastructure with controlled, logged access, and the DPA should document this architecture explicitly.

### What audit rights should a compliance officer insist on in a vendor DPA?
The DPA should preserve a genuine right for the controller to request a specific audit or inspection, with reasonable notice and scope limitations, rather than being fully substituted by the vendor's own self-certification or a generic third-party compliance report the vendor selects unilaterally.

### What should happen to data when a vendor contract ends?
Article 28(3)(g) requires the processor to delete or return all personal data at the controller's choice, deleting existing copies unless law requires retention. The DPA should specify a concrete timeline for this — commonly 30 to 90 days — and ideally require a documented certification of deletion.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is a Data Processing Agreement legally required, or just best practice?", "acceptedAnswer": {"@type": "Answer", "text": "It's legally required under Article 28 of the GDPR whenever a processor handles personal data on a controller's behalf. It is not optional boilerplate, and its content is specified in enough detail under Article 28(3) that a generic or incomplete template can fail to meet the legal standard."}},
    {"@type": "Question", "name": "What happens if a vendor's subprocessor causes a data breach?", "acceptedAnswer": {"@type": "Answer", "text": "The controller retains regulatory liability and must notify the supervisory authority within 72 hours of becoming aware of the breach. Because that clock starts when the processor informs the controller, the DPA should require the processor to notify the controller well within that window — commonly 24 to 48 hours — not merely \"without undue delay.\""}},
    {"@type": "Question", "name": "Does using an offshore development team automatically require special GDPR transfer clauses?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on whether personal data or remote access crosses outside the EU/EEA, not simply where the vendor's engineers are physically located. A well-governed offshore engagement can operate entirely within EU-hosted infrastructure with controlled, logged access, and the DPA should document this architecture explicitly."}},
    {"@type": "Question", "name": "What audit rights should a compliance officer insist on in a vendor DPA?", "acceptedAnswer": {"@type": "Answer", "text": "The DPA should preserve a genuine right for the controller to request a specific audit or inspection, with reasonable notice and scope limitations, rather than being fully substituted by the vendor's own self-certification or a generic third-party compliance report the vendor selects unilaterally."}},
    {"@type": "Question", "name": "What should happen to data when a vendor contract ends?", "acceptedAnswer": {"@type": "Answer", "text": "Article 28(3)(g) requires the processor to delete or return all personal data at the controller's choice, deleting existing copies unless law requires retention. The DPA should specify a concrete timeline for this — commonly 30 to 90 days — and ideally require a documented certification of deletion."}}
  ]
}
</script>
