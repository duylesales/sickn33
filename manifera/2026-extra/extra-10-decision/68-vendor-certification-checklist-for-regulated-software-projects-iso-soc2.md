---
title: "Vendor Certification Checklist for Regulated Software Projects (ISO, SOC 2)"
keywords: "vendor certification checklist, ISO 27001 vendor, SOC 2 Type II, software vendor compliance, security certification vetting, regulated software vendor"
buyer_stage: "Decision"
target_persona: "Compliance Officer"
---

# Vendor Certification Checklist for Regulated Software Projects (ISO, SOC 2)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vendor Certification Checklist for Regulated Software Projects (ISO, SOC 2)",
  "description": "A compliance officer's checklist for verifying vendor security certifications on regulated software projects, covering what ISO 27001 and SOC 2 actually attest to, how to read a report rather than trust a logo, and the gaps certifications don't cover.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/vendor-certification-checklist-for-regulated-software-projects-iso-soc2"}
}
</script>

A vendor's website shows an ISO 27001 badge and a SOC 2 logo, and the sales deck calls it "enterprise-grade security." Neither of those facts tells you what the certification actually scopes, when it was last assessed, or whether the controls it covers are the ones your specific engagement needs. Compliance officers see this gap constantly: a vendor gets waved through diligence because the logos are present, and eighteen months later a security review discovers the SOC 2 certification covered a different product line than the one being used, or the ISO 27001 scope excluded the development environment where your code actually lives.

This is not a hypothetical problem. Certification badges are marketing assets first and evidence documents second, and the vendors who lean hardest on the badge in their pitch are sometimes the ones who have looked least closely at what it actually covers. A compliance officer's job in vendor vetting is not to confirm the badge exists — it is to read the underlying report and verify it actually attests to what your engagement needs attested to.

This checklist covers what each certification actually means, what it doesn't cover, and the specific verification steps that separate real diligence from logo-checking.

## ISO 27001: What "Certified" Actually Attests To

ISO 27001 certifies that an organization has implemented an Information Security Management System (ISMS) meeting the standard's requirements — a systematic, risk-based approach to managing information security, not a checklist of specific technical controls. Critically, ISO 27001 certification has a defined scope, stated explicitly on the certificate, and that scope can be narrower than you assume: a vendor might hold ISO 27001 certification for their corporate IT environment and HR systems while their software development environment — the part that actually touches your code and data — sits outside the certified scope. Always request the Statement of Applicability and the certificate's scope statement, not just the certificate itself, and confirm the scope covers the specific environment, team, and systems your engagement will actually use.

Also verify currency: ISO 27001 certification requires annual surveillance audits and a full recertification every three years. A certificate issued 32 months ago with no evidence of an interim surveillance audit is a yellow flag worth a direct question.

## SOC 2 Type I vs. Type II: A Distinction Vendors Sometimes Blur

SOC 2 Type I attests that a vendor's controls were suitably designed at a single point in time. SOC 2 Type II attests that those controls actually operated effectively over an observation period, typically six to twelve months. This is a meaningful difference: Type I tells you the vendor wrote a good security policy; Type II tells you they actually followed it, continuously, over an extended window, verified by an independent auditor testing the evidence. For any regulated engagement, insist on Type II — a vendor offering only Type I, especially one who has held the certification for multiple cycles without progressing to Type II, is telling you something about either their operational maturity or their willingness to be tested over time, neither encouraging.

Request the actual report, not a summary letter. The report itself includes the auditor's description of tested controls, any exceptions noted, and the vendor's response to those exceptions — this is where the real signal lives, not in the pass/fail headline.

## Reading Exceptions in a SOC 2 Report Without Overreacting or Underreacting

A SOC 2 Type II report with zero noted exceptions across a full observation period is actually somewhat rare and worth a light second look — either the vendor's control environment is genuinely excellent, or the audit scope was narrow enough to avoid surfacing anything meaningful. More commonly, a mature vendor's report will show a small number of minor exceptions (a patch applied a few days outside SLA, an access review completed slightly late) with a documented remediation response. This is normal and not disqualifying — what matters is whether the vendor's response demonstrates they caught and corrected it themselves versus the auditor catching it for them, and whether the same exception recurs across multiple reporting periods, which would indicate a control that isn't actually being fixed.

## ISO 27701 and SOC 2 Privacy Criteria: The Piece Compliance Officers Often Miss

Security certifications and privacy certifications are not the same thing, and a vendor handling personal data under GDPR needs evidence of both. ISO 27701 extends ISO 27001 with privacy information management requirements, and SOC 2 reports can optionally include the Privacy Trust Services Criteria alongside the standard Security criteria. A vendor certified only against SOC 2's Security criteria, without the Privacy criteria included in scope, has demonstrated security control maturity but not specifically privacy program maturity — a distinction that matters directly for GDPR accountability obligations. If your engagement involves personal data at any meaningful scale, ask specifically whether Privacy criteria are in scope, not just Security.

## What Certifications Don't Cover: The Gaps That Still Need Direct Verification

No certification, however current and well-scoped, substitutes for domain-specific diligence. ISO 27001 and SOC 2 both attest to process discipline around information security — they say nothing about whether the vendor's engineers understand financial reconciliation logic, insurance regulatory reporting, or your specific technical stack. They also generally don't cover subcontractor and subprocessor chains in the depth a regulated engagement needs — verify that separately, in the contract, as covered in this cluster's article on audit rights. Treat certifications as a floor that filters out clearly under-resourced vendors, then move to engagement-specific diligence for everything the certification doesn't and cannot attest to.

## Verifying the Certificate Is Real and Current

This sounds basic, but it is worth stating explicitly because it is skipped often enough to matter: verify the certifying body is accredited (for ISO 27001, check the certifying body against national accreditation bodies such as the UK's UKAS or the Dutch Raad voor Accreditatie), and for SOC 2, confirm the report was issued by a licensed CPA firm, since SOC 2 is an American Institute of CPAs (AICPA) framework and only CPA firms can issue the report. A "SOC 2 certified" claim from a vendor who cannot produce an actual report from a named CPA firm on request should be treated as unverified until it is.

## Making the Final Call

Certifications are a necessary but insufficient gate — require them as a baseline for any regulated engagement, verify scope and currency rather than trusting the badge, and then move directly to the domain-specific and contractual diligence that certifications were never designed to cover. A vendor with a pristine SOC 2 Type II report and zero relevant domain experience is not automatically a safer choice than a vendor with a slightly older certification cycle and deep, demonstrated expertise in your specific regulatory context — weigh both, and don't let the certification checkbox substitute for the harder judgment call underneath it.

Manifera maintains current security certifications and can provide full report access under NDA as part of vendor due diligence for regulated engagements. If certification verification is part of your current vendor selection process, our [about us](https://www.manifera.com/about-us/our-way-of-working/) page outlines our governance and security practices, or [contact us](https://www.manifera.com/contact-us/) directly for documentation.

## Frequently Asked Questions

### Is SOC 2 or ISO 27001 more relevant for a European regulated industry engagement?
Both are relevant and increasingly requested together — ISO 27001 is more globally recognized as an ISMS standard and often expected by European auditors and regulators, while SOC 2 is more common among US-headquartered or US-serving vendors. For a vendor operating across both markets, holding both certifications is increasingly the norm rather than the exception.

### How do we verify a certificate is legitimate rather than fabricated or expired?
For ISO 27001, check the certifying body's public registry (most accredited certification bodies maintain a searchable database of active certificates). For SOC 2, request the full report directly from the vendor and confirm the issuing CPA firm's identity independently rather than relying solely on a logo or summary letter.

### Should a vendor's SOC 2 report exceptions automatically disqualify them?
No — minor, well-documented, and promptly remediated exceptions are normal in a mature control environment and are actually a sign the audit was rigorous enough to catch something real. What should raise concern is a pattern of the same exception recurring across multiple reporting periods without resolution, which indicates a control gap the vendor isn't actually closing.

### Do we need to re-verify a vendor's certification status during an ongoing engagement, or only at vendor selection?
Ongoing verification matters, particularly for multi-year regulated engagements. Build a contractual obligation for the vendor to proactively share renewed certificates and reports as they're issued (SOC 2 Type II reports typically renew annually, ISO 27001 has annual surveillance audits), rather than relying on your team to remember to ask.

### What should we do if a vendor we want to use doesn't yet hold either certification?
Assess whether the engagement's data sensitivity genuinely requires certification, or whether other evidence (a completed security questionnaire, a willingness to undergo your own penetration test, references from comparably regulated clients) can substitute for a defined interim period. For engagements involving payment data, health data, or core financial infrastructure, treat the lack of certification as a significant gap rather than a minor one, and consider requiring the vendor to pursue certification as a contractual milestone.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is SOC 2 or ISO 27001 more relevant for a European regulated industry engagement?", "acceptedAnswer": {"@type": "Answer", "text": "Both are relevant and increasingly requested together — ISO 27001 is more globally recognized as an ISMS standard and often expected by European auditors and regulators, while SOC 2 is more common among US-headquartered or US-serving vendors. For a vendor operating across both markets, holding both certifications is increasingly the norm rather than the exception."}},
    {"@type": "Question", "name": "How do we verify a certificate is legitimate rather than fabricated or expired?", "acceptedAnswer": {"@type": "Answer", "text": "For ISO 27001, check the certifying body's public registry (most accredited certification bodies maintain a searchable database of active certificates). For SOC 2, request the full report directly from the vendor and confirm the issuing CPA firm's identity independently rather than relying solely on a logo or summary letter."}},
    {"@type": "Question", "name": "Should a vendor's SOC 2 report exceptions automatically disqualify them?", "acceptedAnswer": {"@type": "Answer", "text": "No — minor, well-documented, and promptly remediated exceptions are normal in a mature control environment and are actually a sign the audit was rigorous enough to catch something real. What should raise concern is a pattern of the same exception recurring across multiple reporting periods without resolution, which indicates a control gap the vendor isn't actually closing."}},
    {"@type": "Question", "name": "Do we need to re-verify a vendor's certification status during an ongoing engagement, or only at vendor selection?", "acceptedAnswer": {"@type": "Answer", "text": "Ongoing verification matters, particularly for multi-year regulated engagements. Build a contractual obligation for the vendor to proactively share renewed certificates and reports as they're issued (SOC 2 Type II reports typically renew annually, ISO 27001 has annual surveillance audits), rather than relying on your team to remember to ask."}},
    {"@type": "Question", "name": "What should we do if a vendor we want to use doesn't yet hold either certification?", "acceptedAnswer": {"@type": "Answer", "text": "Assess whether the engagement's data sensitivity genuinely requires certification, or whether other evidence (a completed security questionnaire, a willingness to undergo your own penetration test, references from comparably regulated clients) can substitute for a defined interim period. For engagements involving payment data, health data, or core financial infrastructure, treat the lack of certification as a significant gap rather than a minor one, and consider requiring the vendor to pursue certification as a contractual milestone."}}
  ]
}
</script>
