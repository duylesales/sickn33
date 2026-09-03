---
title: "Accessibility Compliance Vendor Decision: WCAG Expertise That's Real vs. Claimed"
keywords: "WCAG 2.2 compliance, European Accessibility Act, accessibility audit vendor, VPAT accessibility conformance report, assistive technology testing"
buyer_stage: "Decision"
target_persona: "Compliance Officer"
---

# Accessibility Compliance Vendor Decision: WCAG Expertise That's Real vs. Claimed

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Accessibility Compliance Vendor Decision: WCAG Expertise That's Real vs. Claimed",
  "description": "A framework for compliance officers to distinguish genuine WCAG 2.2 and European Accessibility Act expertise from marketing claims, covering audit verification, testing methodology, and legal exposure.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/accessibility-compliance-vendor-decision-wcag-expertise-thats-real-vs-claimed"}
}
</script>

Ask a vendor how they test for accessibility and watch what happens next. If the answer is "we run it through our scanner and fix what comes up red," you are looking at a company that has never sat next to a screen reader user watching a checkout flow fail. If the answer names a testing protocol, a sample of assistive-technology users, and a specific WCAG success criterion they struggled to meet last quarter, you are looking at something closer to the real thing. The gap between those two answers is where compliance risk actually lives.

Every vendor pitch deck since roughly 2023 has grown an "accessibility-friendly" bullet point, usually sitting between "SEO-optimized" and "mobile-responsive" with the same weight and the same emptiness. For a compliance officer signing off on a vendor selection, that bullet is not evidence — it is a claim that has to be tested before a contract gets signed, because the cost of discovering it was hollow arrives eighteen months later, in the form of a regulatory complaint or a demand letter, not in the form of a failed sprint demo. This decision sits differently than most vendor calls: the downside of getting it wrong is not a missed deadline, it is legal exposure with your name on the sign-off.

## WCAG 2.2 AA Is the Legal Floor — AAA Is Rarely the Real Target

WCAG 2.2, published by the W3C in October 2023, is the current baseline referenced by nearly every EU accessibility regulation, and Level AA is the conformance target written into the law — not AAA. Vendors who lead with "we build to AAA" are usually either misunderstanding the standard or signaling that they have not actually mapped their process to a real success criteria list, because AAA includes criteria (such as sign language interpretation for all prerecorded video, or a strict 3:1 contrast requirement with no exceptions) that are rarely feasible for a typical commercial product and are not what regulators check for. A competent vendor should be able to name the specific new criteria introduced in 2.2 — things like Focus Not Obscured, Dragging Movements, and Accessible Authentication — and explain how their build process addresses each one, rather than gesturing at the standard as a whole. If a vendor cannot walk through at least five specific success criteria from memory, their WCAG fluency is closer to a glossary lookup than a working practice. It's also worth asking how a vendor handles conformance level mismatches within the same product — most real applications end up with a mix, where core transactional flows hit AA cleanly but a third-party embedded widget or a legacy admin panel lags behind, and a vendor who claims uniform AAA across an entire product is either testing a narrow demo surface or not testing carefully at all.

## The European Accessibility Act Raised the Stakes in June 2025

The European Accessibility Act (EAA) became enforceable across EU member states on 28 June 2025, and it changed accessibility from a best-practice recommendation into a binding legal requirement for a wide range of digital products and services — e-commerce, banking, transport ticketing, e-books, and consumer electronics interfaces among them. Unlike the earlier Web Accessibility Directive, which applied narrowly to public sector bodies, the EAA reaches private companies selling to EU consumers, with enforcement and penalty regimes set at the national level — meaning a Dutch company faces different specific fines than a German or French one, but all face real ones. For a compliance officer, this means the vendor conversation is no longer "should we invest in accessibility" but "which vendor actually understands which of our products fall inside EAA scope and which specific obligations attach to each." A vendor unfamiliar with the EAA's scope carve-outs — microenterprises are exempt, but only under specific size and revenue thresholds — is a vendor who will either over-scope your project or, worse, under-scope it and leave you exposed.

## Automated Scanners Catch a Fraction of What Matters

Tools like axe, WAVE, and Lighthouse's accessibility audit are genuinely useful and genuinely limited: independent research from Deque and other accessibility testing firms consistently finds that automated scanning catches somewhere between 30% and 40% of WCAG success criteria violations, concentrated in the mechanical checks — missing alt text, insufficient color contrast, missing form labels, invalid ARIA attributes. What automated tools cannot catch is anything requiring judgment: whether alt text is actually descriptive rather than merely present, whether a focus order makes logical sense, whether a custom widget behaves correctly with a screen reader, whether an error message is understandable in context. A vendor whose "accessibility process" is a CI pipeline step running axe-core and nothing else is running a spell-checker, not an audit. The right question to ask a vendor is not "do you scan for accessibility" — every competent dev shop does — but "what percentage of your accessibility testing is manual, and who performs it."

## Manual Testing Closes the Gap — Real Users Close What's Left

Manual testing by a trained accessibility specialist, working through a keyboard-only navigation pass and a screen reader pass with tools like NVDA and JAWS on Windows or VoiceOver on macOS and iOS, catches most of what automated scanning misses. But even rigorous manual testing by a sighted specialist simulating screen reader use is still a simulation. The vendors worth hiring supplement specialist testing with sessions involving actual assistive-technology users — people who use a screen reader or switch access device as their daily interface, not as a testing exercise — because fluent daily users navigate differently than a specialist working through a checklist, and they surface friction points a simulation never will. This tier of testing is more expensive and slower to schedule, which is exactly why vendors skip it and why a compliance officer should ask for it by name in a proposal rather than assuming it is included.

## Verifying the Claim: VPAT, ACR, and a Live Process Walkthrough

The single most concrete artifact to request from a vendor is a Voluntary Product Accessibility Template (VPAT) or Accessibility Conformance Report (ACR) from a prior engagement — not a template they hand out to prospects, but a completed one from an actual shipped product, ideally one you can verify by contacting the client. A vendor with real experience will have several of these on hand and will not hesitate to walk through how specific criteria were tested and what remediation looked like when something failed. Beyond the document, ask for a live demonstration: have the vendor run an actual audit segment on a page from your current product in front of you, narrating their process. This single request filters out most of the vendors making inflated claims, because theater is hard to sustain in real time — a team that has only ever run a scanner will visibly struggle to explain what they are looking for beyond the tool's output.

## Specialists on Staff, Not Generalists Who Took a Course

There is a meaningful difference between a developer who completed a one-day accessibility training and someone who holds a credential like the IAAP's Certified Professional in Accessibility Core Competencies (CPACC) or Web Accessibility Specialist (WAS) and works on accessibility across multiple client engagements. Ask directly how many accessibility specialists the vendor employs relative to total headcount, and ask whether accessibility work is a dedicated role or a responsibility bolted onto general QA. A team of five where one person "also does accessibility" alongside three other responsibilities is not the same commitment as a team with a standing accessibility practice, even a small one — and the difference shows up in how quickly and correctly issues get triaged during a real project.

## Legal and Liability Exposure Is the Reason This Decision Sits With You

Non-compliance under the EAA and related national implementing legislation carries real consequences: administrative fines that vary by member state, mandated corrective action with deadlines, and in several jurisdictions, private rights of action that let individuals or advocacy organizations bring claims directly. Beyond formal enforcement, accessibility litigation and demand-letter activity — long a fixture in the US under the ADA — is rising in the EU as awareness of the EAA spreads, and the reputational cost of a public complaint often outweighs the fine itself. As the compliance officer signing off on a vendor, you are not just buying development work — you are buying the evidence trail that shows reasonable effort was made, which is exactly what a VPAT, a documented testing methodology, and named specialists give you and a scanner report alone does not. This evidence trail also matters internally: when an accessibility gap surfaces in production, the first question from legal or from leadership will be what process was in place before launch, and "the vendor said it was accessible" is a materially weaker answer than a dated conformance report showing what was tested, what passed, and what remediation was scheduled.

## Making the Final Call

No vendor is perfectly accessible on day one, and a healthy amount of skepticism toward anyone claiming otherwise is warranted — the right signal is not zero-defect claims but a credible, documented process for finding and fixing defects, backed by named specialists and real conformance reports. Weight your evaluation toward vendors who can produce evidence rather than assurances, who separate automated from manual from user testing in their own language, and who understand the EAA's scope well enough to tell you where your specific product sits inside it. A vendor who says "we're not perfect, here's our last VPAT and what we fixed" is more trustworthy than one who says "fully compliant" with no artifact to back it up.

If your current vendor evaluation process is turning up more marketing language than testing methodology, it's worth bringing in a partner who treats accessibility as a build discipline rather than a checkbox — see how Manifera structures accessibility into [custom software development](https://www.manifera.com/services/custom-software-development/) engagements from the requirements stage rather than as a post-launch audit.

## Frequently Asked Questions

### What is the difference between WCAG 2.2 AA and AAA compliance?
Level AA is the conformance target referenced by EU accessibility law, covering criteria like sufficient color contrast, keyboard navigability, and accessible form labeling. Level AAA is a stricter, largely aspirational tier that includes criteria often infeasible for typical commercial products, such as sign language interpretation for all video content, and is rarely the actual legal or practical target.

### When did the European Accessibility Act become enforceable?
The European Accessibility Act became enforceable across EU member states on 28 June 2025. It applies to a broad range of digital products and services sold to EU consumers, including e-commerce, banking, and transport ticketing, with penalty regimes set individually at the national level.

### Can automated accessibility scanners like axe or WAVE catch everything?
No. Automated scanners typically catch around 30% to 40% of WCAG success criteria violations, concentrated in mechanical checks like missing alt text and insufficient contrast. Judgment-based issues — logical focus order, descriptive alt text quality, correct custom widget behavior — require manual testing by a trained specialist and, ideally, testing with actual assistive-technology users.

### What should I ask a vendor to prove their accessibility expertise is real?
Request a completed VPAT or Accessibility Conformance Report from a prior shipped engagement, ideally one you can verify with the client directly, and ask for a live demonstration where the vendor audits a real page from your product in front of you. Also ask what proportion of their headcount holds a recognized accessibility credential, such as IAAP's CPACC or WAS.

### What is the legal exposure for non-compliance under the EAA?
Exposure includes administrative fines that vary by EU member state, mandated corrective action with set deadlines, and in several jurisdictions, private rights of action allowing individuals or advocacy groups to bring claims directly. A documented testing methodology and conformance reports serve as evidence of reasonable effort, which matters both for regulatory response and litigation defense.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is the difference between WCAG 2.2 AA and AAA compliance?", "acceptedAnswer": {"@type": "Answer", "text": "Level AA is the conformance target referenced by EU accessibility law, covering criteria like sufficient color contrast, keyboard navigability, and accessible form labeling. Level AAA is a stricter, largely aspirational tier that includes criteria often infeasible for typical commercial products, such as sign language interpretation for all video content, and is rarely the actual legal or practical target."}},
    {"@type": "Question", "name": "When did the European Accessibility Act become enforceable?", "acceptedAnswer": {"@type": "Answer", "text": "The European Accessibility Act became enforceable across EU member states on 28 June 2025. It applies to a broad range of digital products and services sold to EU consumers, including e-commerce, banking, and transport ticketing, with penalty regimes set individually at the national level."}},
    {"@type": "Question", "name": "Can automated accessibility scanners like axe or WAVE catch everything?", "acceptedAnswer": {"@type": "Answer", "text": "No. Automated scanners typically catch around 30% to 40% of WCAG success criteria violations, concentrated in mechanical checks like missing alt text and insufficient contrast. Judgment-based issues — logical focus order, descriptive alt text quality, correct custom widget behavior — require manual testing by a trained specialist and, ideally, testing with actual assistive-technology users."}},
    {"@type": "Question", "name": "What should I ask a vendor to prove their accessibility expertise is real?", "acceptedAnswer": {"@type": "Answer", "text": "Request a completed VPAT or Accessibility Conformance Report from a prior shipped engagement, ideally one you can verify with the client directly, and ask for a live demonstration where the vendor audits a real page from your product in front of you. Also ask what proportion of their headcount holds a recognized accessibility credential, such as IAAP's CPACC or WAS."}},
    {"@type": "Question", "name": "What is the legal exposure for non-compliance under the EAA?", "acceptedAnswer": {"@type": "Answer", "text": "Exposure includes administrative fines that vary by EU member state, mandated corrective action with set deadlines, and in several jurisdictions, private rights of action allowing individuals or advocacy groups to bring claims directly. A documented testing methodology and conformance reports serve as evidence of reasonable effort, which matters both for regulatory response and litigation defense."}}
  ]
}
</script>
