---
title: "Choosing a Government Digital Services Vendor: Security Clearance Requirements"
keywords: "government digital services vendor, security clearance software vendor, govtech vendor due diligence, public sector security requirements vendor, government software vendor selection"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Choosing a Government Digital Services Vendor: Security Clearance Requirements

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Government Digital Services Vendor: Security Clearance Requirements",
  "description": "A security lead's guide to knowing when a government software project actually requires personnel or facility security clearance, when it doesn't, and how offshore and distributed delivery models fit into that picture honestly.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-05",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-a-government-digital-services-vendor-security-clearance-requirements"}
}
</script>

The most expensive mistake in a government digital services procurement isn't hiring a vendor without adequate security clearance — it's specifying clearance requirements the project doesn't actually need, and then paying a premium for a vendor pool that's smaller, slower, and more expensive than the work justifies. The reverse mistake — assuming a public-facing citizen portal needs the same personnel screening as a classified defense system — is just as common and just as costly, in the other direction. Getting this right starts with understanding what security classification tiers actually mean and mapping them honestly against what the specific project touches.

## Classification Tiers: What They Actually Gate

Most EU member states run a national security classification system loosely aligned with NATO's tiers — RESTRICTED, CONFIDENTIAL, SECRET, and TOP SECRET — with national equivalents layered underneath. In the Netherlands specifically, personnel handling anything above the lowest sensitivity tier typically require a VGB (Verklaring van Geen Bezwaar — a certificate of no objection), issued by the AIVD (the General Intelligence and Security Service) after a background screening that can take anywhere from a few weeks to several months depending on the tier and the depth of investigation required. The screening covers criminal history, financial vulnerability (susceptibility to bribery or coercion), foreign contacts and loyalties, and in higher tiers, extends to close family members.

The gating question a security lead has to answer honestly before writing clearance requirements into a tender: does the software project actually touch classified information, or does it touch sensitive-but-unclassified data — citizen PII, internal administrative systems, non-classified operational data — that requires strong security controls but not personnel clearance in the classified-information sense. These are frequently conflated, and the conflation is expensive: a project requiring only strong data protection and access controls, but specified as requiring cleared personnel, needlessly shrinks your vendor pool to firms holding facility security clearances, inflates cost, and adds months of screening lead time to a project timeline that didn't need it.

## Personnel Clearance vs. Facility Clearance vs. Data Handling Controls

These are three distinct things, and government buyers often bundle them into a single vague "security requirement" line in an RFP without specifying which actually applies. Personnel clearance screens individuals. Facility clearance certifies that a vendor's physical premises and IT infrastructure meet specific standards for storing and processing classified material — air-gapped networks, controlled physical access, accredited secure rooms. Data handling controls — encryption standards, access logging, data residency, need-to-know access restrictions — are a separate layer that applies broadly to sensitive government data whether or not classification is involved at all.

A project can require rigorous data handling controls without requiring either personnel or facility clearance. Conflating the three in a tender specification is one of the most common ways a procuring authority accidentally excludes qualified, cost-effective vendors who could deliver the actual technical requirement perfectly well under a data processing agreement and standard security controls, simply because the RFP language borrowed classified-project boilerplate for a project that isn't classified.

## Screening Timelines Are a Project-Planning Input, Not a Footnote

When personnel clearance genuinely is required, the screening timeline needs to be built into the project plan from day one, not treated as a formality that happens in parallel with kickoff. Lower-tier screening can complete in a matter of weeks; higher-tier investigations, particularly ones involving foreign contacts or financial deep-dives, can run several months and occasionally longer if a candidate's history requires additional verification. A vendor team assembled around individuals who haven't started screening yet is a team that may not be able to touch the actual work for months — and swapping in already-cleared personnel from a different engagement, while common, has its own continuity and confidentiality risk if it means less product-specific ramp-up time before deployment.

The security lead's practical responsibility here: verify at the proposal stage whether the vendor's proposed team already holds relevant clearance, is currently in process, or would need to start from zero — these are three very different risk profiles for your delivery timeline, and a vendor who glosses over which applies is a vendor you should press for specifics before contract signature.

## Where Distributed and Offshore Delivery Models Genuinely Fit

This is worth addressing directly rather than around: classified-information work requiring cleared personnel and accredited facilities is not a fit for a distributed or offshore delivery model, and any vendor claiming otherwise for genuinely classified work should be treated with suspicion. But a large share of government digital services work isn't classified at all — citizen-facing service portals, internal administrative tools, data dashboards, case management systems handling sensitive-but-unclassified data — and for that category, the relevant security bar is rigorous data protection engineering (encryption at rest and in transit, strict access controls, EU data residency, audit logging) rather than personnel clearance. A distributed delivery model, with the right data handling architecture, data processing agreements, and EU-based hosting, can meet that bar well, which is a meaningfully different question from whether it can meet a classified-facility bar, which it generally cannot.

The due diligence step for a security lead: get specific about which tier your actual project sits in before ruling vendors in or out based on delivery model alone, and make sure the RFP language reflects that tier accurately rather than defaulting to the most conservative classified-project template out of caution.

## Secure SDLC Requirements That Apply Regardless of Clearance Tier

Independent of whether personnel clearance is required, government software projects should verify a vendor's secure software development lifecycle practices directly: static and dynamic application security testing integrated into CI, dependency vulnerability scanning, a documented secure coding standard, and — increasingly required explicitly in government tenders — a software bill of materials (SBOM) for delivered systems, so the procuring authority has visibility into every component and library the delivered software depends on. These controls matter for classified and non-classified projects alike, and a vendor's maturity here is a better predictor of delivered security posture than clearance tier alone.

## Making the Security Call

The discipline that actually protects a government digital services project isn't defaulting to the highest clearance bar out of caution — it's mapping the specific classification tier the project genuinely requires, separating personnel clearance from facility clearance from data handling controls, and building realistic screening timelines into the plan when clearance truly is needed. Get that mapping wrong in either direction, and you either exclude qualified vendors who could deliver the work well under standard security controls, or you understate the requirement for a project that genuinely needed cleared personnel. Manifera delivers non-classified government and public-sector-adjacent digital services under rigorous data protection engineering and EU-compliant hosting — see our [migration to EU/NL cloud infrastructure](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) services or [get in touch](https://www.manifera.com/contact-us/) to discuss which security tier your specific project actually requires.

## Frequently Asked Questions

### How long does personnel security screening typically take in the Netherlands?
It varies by tier: lower-sensitivity VGB screening can complete in a few weeks, while higher-tier investigations involving foreign contacts or deeper financial checks can run several months. This timeline needs to be built into the project schedule from the outset rather than assumed to run in parallel with kickoff without delaying anything.

### Does citizen-facing government software always require cleared personnel?
No. Most citizen-facing digital services handle sensitive-but-unclassified data — PII, administrative records — which requires rigorous data protection controls (encryption, access management, data residency, audit logging) rather than personnel security clearance in the classified-information sense. Clearance is generally required only when the work directly touches genuinely classified material.

### What's the difference between facility clearance and personnel clearance?
Personnel clearance screens individuals for trustworthiness to handle classified information. Facility clearance certifies that a vendor's physical premises and IT infrastructure — air-gapped networks, controlled access, accredited secure rooms — meet the standard required to store and process classified material. A vendor can have cleared personnel without holding facility clearance, and a project may require one, both, or neither depending on scope.

### Can a distributed or offshore delivery team work on any government digital services project?
It depends entirely on classification. Genuinely classified work requiring cleared personnel and accredited facilities is not a fit for distributed delivery. Non-classified government work — the majority of citizen service portals, internal tools, and administrative systems — can be delivered by a distributed team under strong data protection engineering and appropriate data processing agreements, which is a different and lower security bar than classified-facility work.

### What secure development practices should we verify regardless of clearance tier?
Static and dynamic application security testing integrated into the CI pipeline, dependency vulnerability scanning, a documented secure coding standard, and increasingly a software bill of materials (SBOM) for delivered systems. These apply to classified and non-classified government projects alike and are often a better predictor of actual delivered security posture than clearance tier by itself.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How long does personnel security screening typically take in the Netherlands?", "acceptedAnswer": {"@type": "Answer", "text": "It varies by tier: lower-sensitivity VGB screening can complete in a few weeks, while higher-tier investigations involving foreign contacts or deeper financial checks can run several months. This timeline needs to be built into the project schedule from the outset rather than assumed to run in parallel with kickoff without delaying anything."}},
    {"@type": "Question", "name": "Does citizen-facing government software always require cleared personnel?", "acceptedAnswer": {"@type": "Answer", "text": "No. Most citizen-facing digital services handle sensitive-but-unclassified data — PII, administrative records — which requires rigorous data protection controls (encryption, access management, data residency, audit logging) rather than personnel security clearance in the classified-information sense. Clearance is generally required only when the work directly touches genuinely classified material."}},
    {"@type": "Question", "name": "What's the difference between facility clearance and personnel clearance?", "acceptedAnswer": {"@type": "Answer", "text": "Personnel clearance screens individuals for trustworthiness to handle classified information. Facility clearance certifies that a vendor's physical premises and IT infrastructure — air-gapped networks, controlled access, accredited secure rooms — meet the standard required to store and process classified material. A vendor can have cleared personnel without holding facility clearance, and a project may require one, both, or neither depending on scope."}},
    {"@type": "Question", "name": "Can a distributed or offshore delivery team work on any government digital services project?", "acceptedAnswer": {"@type": "Answer", "text": "It depends entirely on classification. Genuinely classified work requiring cleared personnel and accredited facilities is not a fit for distributed delivery. Non-classified government work — the majority of citizen service portals, internal tools, and administrative systems — can be delivered by a distributed team under strong data protection engineering and appropriate data processing agreements, which is a different and lower security bar than classified-facility work."}},
    {"@type": "Question", "name": "What secure development practices should we verify regardless of clearance tier?", "acceptedAnswer": {"@type": "Answer", "text": "Static and dynamic application security testing integrated into the CI pipeline, dependency vulnerability scanning, a documented secure coding standard, and increasingly a software bill of materials (SBOM) for delivered systems. These apply to classified and non-classified government projects alike and are often a better predictor of actual delivered security posture than clearance tier by itself."}}
  ]
}
</script>
