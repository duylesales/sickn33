---
title: "Choosing a Vendor for Government and Public Sector Software Projects"
keywords: "government software vendor, public sector software procurement, EU public procurement, accessibility compliance software, TenderNed procurement, public sector IT vendor"
buyer_stage: "Decision"
target_persona: "Procurement Lead"
---

# Choosing a Vendor for Government and Public Sector Software Projects

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Vendor for Government and Public Sector Software Projects",
  "description": "A procurement lead's guide to vetting software vendors for government and public sector projects, covering EU procurement thresholds, accessibility mandates, security baselines, and the criteria that hold up under public tender scrutiny.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-a-vendor-for-government-and-public-sector-software-projects"}
}
</script>

A private-sector software vendor selection lives or dies on ROI and delivery risk. A government or public sector selection lives or dies on all of that plus a defensible procurement trail, because the losing bidders can and sometimes do challenge the award, and a procedural misstep can unwind a contract months into delivery. If you are the procurement lead on a public sector software project, you are not just picking the best vendor — you are building a record that has to survive scrutiny from auditors, competitors, and occasionally a court.

This is a fundamentally different discipline from commercial vendor selection, and treating it the same way is the most common mistake procurement teams make on their first few public sector projects. Commercial buyers can weight a decision however they want and change their mind mid-process. Public sector buyers in the EU operate under procurement directives that dictate how criteria must be published in advance, how they must be applied consistently, and how the process must be documented well enough to withstand a challenge. Get the process wrong, and even the objectively best vendor selection can be reversed on procedural grounds.

This article covers what actually needs to be verified and documented when selecting a software vendor for a government or public sector project, beyond the standard commercial due diligence.

## EU Procurement Thresholds and Which Regime Actually Applies

The EU Public Procurement Directive (2014/24/EU) sets thresholds above which a full formal tender procedure is mandatory — for central government bodies and most public sector entities, this threshold for services contracts sits in the range that most meaningful software development engagements will exceed, which means an open, restricted, or negotiated procedure with published criteria is required, not a discretionary vendor selection. Below threshold, member states set their own national procurement rules, which in the Netherlands are governed by the Aanbestedingswet, and which still typically require some form of competitive process and documented rationale even when the full EU directive doesn't strictly apply.

The practical implication for a procurement lead: confirm which regime applies before drafting selection criteria, because criteria that are legally sufficient for a below-threshold procurement may not survive scrutiny for an above-threshold one, and restarting a procurement process mid-stream because the wrong regime was applied costs months.

## Publishing Criteria Before You See a Single Proposal

The defining discipline of public procurement, and the one most likely to trip up teams used to commercial vendor selection, is that award criteria must be published before proposals are evaluated, and the evaluation must apply those exact published criteria — not criteria that feel right once you've seen what vendors actually proposed. A commercial buyer can informally weight "we liked their team better" after the fact; a public sector buyer generally cannot, without exposing the award to a legitimate challenge from a losing bidder. This means the criteria-setting phase deserves as much rigor as the evaluation phase itself: weight technical capability, price, delivery methodology, and relevant experience explicitly, in percentages, published in the tender documentation, before a single proposal is opened.

## Accessibility Isn't Optional: WCAG 2.1 AA and the European Accessibility Act

Any public-facing software delivered for a government body in the EU must meet accessibility standards, most commonly WCAG 2.1 Level AA as referenced by EN 301 549, the European standard for ICT accessibility. This is not a nice-to-have feature request — it is a legal requirement under the EU Web Accessibility Directive for public sector bodies, and increasingly extends to private-sector digital services under the European Accessibility Act, which entered into force for many product and service categories in June 2025. A vendor bidding on a public sector project needs to demonstrate, with specifics, how accessibility is built into their development process — automated accessibility testing in CI, screen reader testing as a standard QA step, keyboard navigation verification — rather than treated as a post-launch remediation item. Ask for an accessibility audit from a prior public sector engagement as evidence, not just a claim of WCAG familiarity.

## Security Baseline: BIO and National Government Security Standards

In the Netherlands, government bodies at national, provincial, and municipal levels operate under the Baseline Informatiebeveiliging Overheid (BIO), a mandatory information security framework aligned with ISO 27001 but with specific government-context controls layered on top. A vendor bidding on a Dutch public sector project should be able to speak to BIO specifically, not just generic ISO 27001 certification, since BIO compliance is often an explicit tender requirement with its own documentation and assessment process. Other EU member states have equivalent national frameworks — confirm which one applies to your specific procuring authority and verify the vendor's familiarity with it directly, rather than assuming general security certifications transfer automatically.

## Data Sovereignty and Sub-National Hosting Requirements

Government data often carries hosting requirements beyond standard GDPR compliance — some public sector tenders specify that data must remain within national borders, not just the EU/EEA, particularly for anything touching citizen identity data, law enforcement, or critical infrastructure. Confirm this requirement explicitly in the tender specification before evaluating vendors, since a vendor with excellent EU-wide infrastructure may still fail a national-hosting requirement if their nearest data center sits across a border. This is a case where the requirement needs to be stated with precision in your tender documents — "EU-based" and "nationally-based" are materially different bars, and vendors will (reasonably) bid to whichever standard you actually publish.

## Evaluating Delivery Track Record Without Over-Weighting Incumbency

Public sector procurement has a well-documented tendency to favor incumbent vendors, partly because incumbency reduces perceived risk and partly because evaluators default to familiar names. This is worth actively guarding against in your evaluation design: weight genuinely comparable delivery experience (similar scale, similar regulatory context, similar technical domain) rather than simply rewarding "has worked with government before" as a generic credential. A vendor with strong commercial-sector delivery experience and demonstrated ability to meet the specific accessibility, security, and documentation requirements above can be a stronger technical choice than an incumbent whose actual delivery record is mediocre but familiar.

## Making the Final Call

Public sector vendor selection is procedurally heavier than commercial selection, and that weight is not bureaucratic overhead for its own sake — it exists because public money and public accountability require a defensible process, and it protects the procuring authority from a challenge that could unwind an award months into delivery. The right approach is to treat the procedural requirements — published criteria, threshold-appropriate procedure, accessibility and security baseline verification — as fixed constraints to design around, not obstacles to minimize, while still evaluating the underlying delivery capability with the same rigor a commercial buyer would apply.

Manifera has delivered public-sector-adjacent projects with the accessibility, security documentation, and process rigor these engagements require. If you're structuring a public sector software tender, our [about us](https://www.manifera.com/about-us/our-way-of-working/) page details our delivery governance model, or [get in touch](https://www.manifera.com/contact-us/) to discuss your specific tender requirements.

## Frequently Asked Questions

### Do EU procurement rules apply to every government software purchase, regardless of size?
No — the full EU Public Procurement Directive procedures apply above specific financial thresholds, which are set and periodically updated by the European Commission. Below those thresholds, national procurement rules apply, which in the Netherlands still typically require a documented, competitive process even though the full EU directive procedures aren't mandatory.

### Can we shortlist based on informal criteria and formalize the published criteria afterward?
No, and doing so is one of the most common grounds for a successful procurement challenge. Award criteria must be published in the tender documentation before proposals are evaluated, and the evaluation must demonstrably apply those exact criteria — retrofitting criteria to match a preferred outcome exposes the award to legal challenge from losing bidders.

### Is WCAG 2.1 AA compliance required for internal government software, or only public-facing systems?
The strongest legal requirement applies to public-facing digital services under the Web Accessibility Directive, but many national frameworks and the broader European Accessibility Act extend accessibility expectations further. It's safest to build accessibility requirements into any government software tender regardless of whether the system is public-facing, since internal systems often become public-facing later or need to accommodate employees with accessibility needs.

### How should we weight price versus technical capability in a public sector tender?
This should be decided and published explicitly before evaluation begins, commonly as a percentage split (for example 40% price, 60% quality and technical capability, though the specific split varies by procuring authority and project type). The "most economically advantageous tender" standard under EU procurement law explicitly allows quality-weighted evaluation, not just lowest price — use that latitude deliberately rather than defaulting to price-only comparison.

### What's the biggest procedural mistake procurement leads make on their first public sector software tender?
Treating vendor selection like a commercial process and only formalizing the procurement paperwork afterward. The published criteria, the documented evaluation, and the audit trail need to exist before and during evaluation, not be reconstructed after an informal decision has already been made — reconstructed documentation is exactly what a procurement challenge exposes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Do EU procurement rules apply to every government software purchase, regardless of size?", "acceptedAnswer": {"@type": "Answer", "text": "No — the full EU Public Procurement Directive procedures apply above specific financial thresholds, which are set and periodically updated by the European Commission. Below those thresholds, national procurement rules apply, which in the Netherlands still typically require a documented, competitive process even though the full EU directive procedures aren't mandatory."}},
    {"@type": "Question", "name": "Can we shortlist based on informal criteria and formalize the published criteria afterward?", "acceptedAnswer": {"@type": "Answer", "text": "No, and doing so is one of the most common grounds for a successful procurement challenge. Award criteria must be published in the tender documentation before proposals are evaluated, and the evaluation must demonstrably apply those exact criteria — retrofitting criteria to match a preferred outcome exposes the award to legal challenge from losing bidders."}},
    {"@type": "Question", "name": "Is WCAG 2.1 AA compliance required for internal government software, or only public-facing systems?", "acceptedAnswer": {"@type": "Answer", "text": "The strongest legal requirement applies to public-facing digital services under the Web Accessibility Directive, but many national frameworks and the broader European Accessibility Act extend accessibility expectations further. It's safest to build accessibility requirements into any government software tender regardless of whether the system is public-facing, since internal systems often become public-facing later or need to accommodate employees with accessibility needs."}},
    {"@type": "Question", "name": "How should we weight price versus technical capability in a public sector tender?", "acceptedAnswer": {"@type": "Answer", "text": "This should be decided and published explicitly before evaluation begins, commonly as a percentage split (for example 40% price, 60% quality and technical capability, though the specific split varies by procuring authority and project type). The 'most economically advantageous tender' standard under EU procurement law explicitly allows quality-weighted evaluation, not just lowest price — use that latitude deliberately rather than defaulting to price-only comparison."}},
    {"@type": "Question", "name": "What's the biggest procedural mistake procurement leads make on their first public sector software tender?", "acceptedAnswer": {"@type": "Answer", "text": "Treating vendor selection like a commercial process and only formalizing the procurement paperwork afterward. The published criteria, the documented evaluation, and the audit trail need to exist before and during evaluation, not be reconstructed after an informal decision has already been made — reconstructed documentation is exactly what a procurement challenge exposes."}}
  ]
}
</script>
