---
title: "Data Residency Requirements: Vendor Vetting for EU Regulated Industries"
keywords: "data residency requirements, GDPR data transfer, EU data localization, Schrems II compliance, vendor data sovereignty, regulated industry cloud hosting"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Data Residency Requirements: Vendor Vetting for EU Regulated Industries

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Data Residency Requirements: Vendor Vetting for EU Regulated Industries",
  "description": "A security lead's guide to vetting software vendors on data residency and sovereignty, covering GDPR transfer rules, Schrems II, subprocessor visibility, and the specific questions that separate compliant vendors from exposed ones.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/data-residency-requirements-vendor-vetting-for-eu-regulated-industries"}
}
</script>

Ask a vendor where your data will physically live, and most will answer "the cloud" as if that settles the question. It doesn't. A security lead vetting vendors for an EU-regulated engagement needs a materially more precise answer: which cloud region, which subprocessors touch the data in transit and at rest, and what legal mechanism governs any transfer outside the EU/EEA — because "the cloud" can mean an eu-central-1 region in Frankfurt, or it can mean a US-based subprocessor's log aggregation service scraping request metadata through a jurisdiction your DPA never anticipated.

This is not a theoretical compliance exercise. Since the Schrems II ruling invalidated the EU-US Privacy Shield in 2020, and with the Data Privacy Framework that replaced it facing its own ongoing legal challenges, data residency has become one of the more litigated and enforcement-active areas of EU regulatory practice. A security lead who signs off on a vendor without verifying data location down to the subprocessor level is accepting risk on behalf of the organization that a regulator will not treat as a good-faith mistake if it surfaces during an investigation.

This article lays out exactly what to verify, in what order, before a vendor handling EU regulated data gets approved.

## Data Residency vs. Data Sovereignty: A Distinction Vendors Blur on Purpose

Vendors frequently use "data residency" and "data sovereignty" interchangeably in sales conversations, and the distinction matters enormously. Data residency means data is physically stored within a specified geographic boundary — an EU data center, for instance. Data sovereignty means the data is subject to the laws of the jurisdiction it resides in, and critically, not subject to extraterritorial legal reach from another jurisdiction. A US-headquartered cloud provider's EU region satisfies residency (the servers are physically in Frankfurt or Dublin) but does not fully satisfy sovereignty, because the US CLOUD Act asserts jurisdiction over data controlled by US companies regardless of where it is physically stored. For most EU regulated industries, residency within the EU/EEA combined with a properly executed transfer mechanism is the practical standard; for a narrower set of use cases — certain government, defense, and critical infrastructure engagements — true sovereignty, meaning EU-owned and EU-operated infrastructure with no US corporate parent, is the actual requirement. Know which standard your engagement needs before you evaluate vendors against the wrong one.

## GDPR Articles 44-49: The Transfer Rules That Actually Govern the Decision

GDPR Chapter V (Articles 44-49) governs any transfer of personal data outside the EU/EEA, and it does not simply prohibit such transfers — it requires a valid legal mechanism to authorize them. Standard Contractual Clauses (SCCs), updated by the European Commission in 2021, are the most common mechanism a vendor will point to, but SCCs alone are not sufficient post-Schrems II: the ruling requires a supplementary Transfer Impact Assessment (TIA) evaluating whether the destination country's legal regime, including government surveillance access, undermines the protections SCCs are meant to provide. A vendor who offers to sign SCCs but has no TIA process, and cannot describe what supplementary technical measures (encryption with EU-held keys, pseudonymization) they apply on top of the SCCs, has not actually solved the Schrems II problem — they have just signed a document.

## Subprocessor Lists: Where the Real Exposure Usually Hides

A vendor's primary data center location is the easy part to verify; the subprocessor chain is where residency commitments quietly break down. A vendor hosting primary infrastructure in an EU region may still route error logging through a US-based observability platform, use a US-based email delivery service for transactional notifications containing personal data, or rely on a support ticketing tool that stores customer data in a US region by default. Each of these is a subprocessor, and under GDPR Article 28, you are entitled to a current list of them along with advance notice of any change.

The vetting step that matters here: request the vendor's full subprocessor list, cross-reference each one's data location against your residency requirement, and specifically ask how the vendor's engineering practices prevent an engineer from inadvertently introducing a new US-based tool (a debugging SaaS product, an AI coding assistant with US-based data processing) mid-project without going through the subprocessor approval process.

## Cloud Region Selection Isn't Automatically EU-Compliant

Choosing "the EU region" on a major cloud provider's console is necessary but not sufficient. Verify specifically: is the compute and storage layer EU-based, and is the control plane and metadata layer also EU-based, since some services process metadata (not payload data, but data about the data) through a global control plane that may not respect the same regional boundary. Also verify backup and disaster recovery region — it is common for a vendor to run primary infrastructure in Frankfurt but replicate backups to a US region for cost or redundancy reasons, which reintroduces the exact transfer question the primary region was chosen to avoid. Ask explicitly, and get it in writing as part of the Data Processing Agreement, not just a verbal assurance.

## National-Level Requirements That Sit on Top of GDPR

GDPR sets an EU-wide floor, but several regulated sectors carry additional national-level data localization requirements layered on top. Financial services entities in several EU member states face sector-specific guidance from national regulators (in the Netherlands, De Nederlandsche Bank's outsourcing guidelines) that can be more prescriptive than GDPR alone about where core financial data can reside and under what oversight conditions. Healthcare data in several jurisdictions carries additional restrictions beyond GDPR's special category data provisions. A vendor vetted only against GDPR baseline requirements may still fail a sector-specific national requirement — confirm which regulator, if any, has direct oversight of your organization and whether that regulator has published its own data location guidance before finalizing vendor selection.

## The Vendor Questionnaire That Actually Surfaces Gaps

A generic security questionnaire asking "is data encrypted at rest and in transit" gets a yes from nearly every vendor and reveals almost nothing. The questions that actually differentiate: name every subprocessor with access to personal data and their data location; describe the specific transfer mechanism and supplementary measures applied for any non-EU subprocessor; describe how a data location change would be communicated and what advance notice is contractually guaranteed; and describe what happens to data location commitments if the vendor is acquired by a company headquartered outside the EU. That last question is not hypothetical — vendor acquisitions have repeatedly changed the legal exposure profile of previously-compliant data arrangements, and a vendor without a contractual answer is carrying undisclosed risk.

## Making the Final Call

Not every engagement needs the maximum standard of true data sovereignty — for most EU regulated industries, EU/EEA residency with properly executed SCCs, a documented Transfer Impact Assessment, and full subprocessor transparency is a defensible, proportionate standard that satisfies GDPR and most sector regulators. Reserve the higher bar of full EU-only sovereign infrastructure for the narrower set of engagements — government, defense, critical national infrastructure — where it is actually required. Over-specifying sovereignty requirements for a standard commercial engagement needlessly shrinks your vendor pool and adds cost without corresponding regulatory benefit.

Manifera's engineering delivery is structured to work within EU data residency requirements, with governance handled from our Amsterdam base and full transparency into infrastructure and subprocessor arrangements for regulated clients. If data residency is a gating requirement for your next vendor decision, our [about us](https://www.manifera.com/about-us/our-way-of-working/) page details our governance model, or [contact us](https://www.manifera.com/contact-us/) to review your specific residency requirements before you shortlist vendors.

## Frequently Asked Questions

### Is choosing a vendor with EU-based servers enough to satisfy GDPR data residency requirements?
It's a necessary starting point but not sufficient on its own. You also need to verify the subprocessor chain, backup and disaster recovery region, and whether the vendor's corporate structure (particularly a US parent company) creates extraterritorial legal exposure under laws like the US CLOUD Act, regardless of physical server location.

### What is a Transfer Impact Assessment and why do we need one alongside Standard Contractual Clauses?
A Transfer Impact Assessment evaluates whether the destination country's legal regime, including government surveillance access, undermines the data protection SCCs are meant to guarantee — a requirement established by the Schrems II ruling. SCCs alone, without a TIA and supplementary technical measures where needed, are not considered sufficient post-Schrems II.

### How do we handle a vendor who wants to use a US-based subcontractor for one component of the project?
Require advance disclosure and your written approval before onboarding, confirm the specific data category that subcontractor would touch, and assess whether a transfer mechanism with supplementary measures (such as EU-held encryption keys) can adequately protect that specific data flow — or scope the subcontractor out of the data path entirely if the data is too sensitive to justify the risk.

### Does data residency matter as much for a vendor providing staff augmentation as one hosting infrastructure?
Yes, arguably more directly — augmented engineers working from outside the EU may access production data through remote connections regardless of where the infrastructure itself sits, which raises separate questions about access controls, VPN architecture, and where engineer workstations cache or process data locally.

### What's the practical first step in vetting a new vendor for data residency compliance?
Request the full subprocessor list and current Data Processing Agreement before any technical evaluation begins — if the vendor cannot produce a complete, current subprocessor list on request, that alone is a strong signal their data governance maturity isn't where a regulated engagement requires it to be.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is choosing a vendor with EU-based servers enough to satisfy GDPR data residency requirements?", "acceptedAnswer": {"@type": "Answer", "text": "It's a necessary starting point but not sufficient on its own. You also need to verify the subprocessor chain, backup and disaster recovery region, and whether the vendor's corporate structure (particularly a US parent company) creates extraterritorial legal exposure under laws like the US CLOUD Act, regardless of physical server location."}},
    {"@type": "Question", "name": "What is a Transfer Impact Assessment and why do we need one alongside Standard Contractual Clauses?", "acceptedAnswer": {"@type": "Answer", "text": "A Transfer Impact Assessment evaluates whether the destination country's legal regime, including government surveillance access, undermines the data protection SCCs are meant to guarantee — a requirement established by the Schrems II ruling. SCCs alone, without a TIA and supplementary technical measures where needed, are not considered sufficient post-Schrems II."}},
    {"@type": "Question", "name": "How do we handle a vendor who wants to use a US-based subcontractor for one component of the project?", "acceptedAnswer": {"@type": "Answer", "text": "Require advance disclosure and your written approval before onboarding, confirm the specific data category that subcontractor would touch, and assess whether a transfer mechanism with supplementary measures (such as EU-held encryption keys) can adequately protect that specific data flow — or scope the subcontractor out of the data path entirely if the data is too sensitive to justify the risk."}},
    {"@type": "Question", "name": "Does data residency matter as much for a vendor providing staff augmentation as one hosting infrastructure?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, arguably more directly — augmented engineers working from outside the EU may access production data through remote connections regardless of where the infrastructure itself sits, which raises separate questions about access controls, VPN architecture, and where engineer workstations cache or process data locally."}},
    {"@type": "Question", "name": "What's the practical first step in vetting a new vendor for data residency compliance?", "acceptedAnswer": {"@type": "Answer", "text": "Request the full subprocessor list and current Data Processing Agreement before any technical evaluation begins — if the vendor cannot produce a complete, current subprocessor list on request, that alone is a strong signal their data governance maturity isn't where a regulated engagement requires it to be."}}
  ]
}
</script>
