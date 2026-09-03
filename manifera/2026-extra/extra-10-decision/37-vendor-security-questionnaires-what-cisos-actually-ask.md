---
title: "Vendor Security Questionnaires: What CISOs Actually Ask"
keywords: "vendor security questionnaire, CAIQ SIG VSA, third-party risk assessment, security evidence request, fourth-party risk, vendor risk management"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Vendor Security Questionnaires: What CISOs Actually Ask

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vendor Security Questionnaires: What CISOs Actually Ask",
  "description": "A Security Lead's guide to what experienced CISOs actually probe for in vendor security questionnaires, beyond standard frameworks like CAIQ and SIG, and how to prepare answers that survive follow-up.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/vendor-security-questionnaires-what-cisos-actually-ask"}
}
</script>

Your vendor filled out the 300-question standardized security questionnaire in under a day. Every answer was "Yes." A questionnaire that fast, with no qualified answers and no attached evidence, is not proof of a mature security program — it's proof nobody actually checked the answers against reality before hitting submit. Experienced CISOs know this, and their real evaluation starts after the checkbox questionnaire comes back clean.

Whether you're the Security Lead sending the questionnaire or the vendor filling one out, understanding what a rigorous evaluator actually probes for — beyond the standardized form — determines whether the vendor relationship survives real scrutiny during an incident, an audit, or a customer's own third-party risk review of you. This article covers both sides: the frameworks in play, and the follow-up questions that separate a vendor with a real security program from one that's good at filling out forms.

## Why the Standard Questionnaire Rarely Reveals Real Risk

Standardized questionnaires exist to create comparability across vendors and reduce the burden of writing custom questions for every relationship, and they serve that purpose reasonably well as a first-pass filter. Their weakness is structural: most questions are binary (yes/no) or self-attested, with no built-in mechanism to catch a vendor answering aspirationally rather than accurately, and no verification unless the evaluator specifically demands evidence. A vendor that answers "yes" to "do you encrypt data at rest" without specifying the standard, the scope, or providing evidence is giving you a true statement about intent that may or may not reflect implementation. Experienced CISOs treat the standardized questionnaire as a starting point for follow-up, never as the final evaluation.

## The Frameworks Most Vendors Are Asked to Fill Out

The Consensus Assessments Initiative Questionnaire (CAIQ), maintained by the Cloud Security Alliance, is common for cloud service vendors and maps closely to the CSA's Cloud Controls Matrix. The Standardized Information Gathering (SIG) questionnaire, in both full and Lite versions, covers a broader operational risk surface beyond pure security — privacy, business continuity, and compliance. The Vendor Security Alliance (VSA) questionnaire is shorter and more security-focused, popular among tech companies specifically. Knowing which framework a request uses matters because each has different depth: a SIG Lite response tells you far less than a full SIG or a well-answered CAIQ, and a vendor's willingness to complete the longer, more detailed version is itself a weak signal about how seriously they take the relationship.

## Questions That Separate Real Answers From Marketing Answers

Rigorous evaluators reframe standard questions to force specificity. Instead of "do you have an incident response plan," they ask "walk me through your last actual security incident, what happened, how long detection took, and what changed afterward" — a vendor with a real program answers this concretely; one without either claims no incidents ever occurred (implausible at scale) or gives a generic, hypothetical answer. Instead of "are employees trained on security," they ask for the actual training completion rate and how repeat offenders on phishing simulations are handled. Instead of "do you have access controls," they ask how access is provisioned and, more tellingly, how quickly it's revoked when someone leaves — de-provisioning lag is one of the most common and least discussed real-world vulnerabilities in vendor organizations.

## Evidence Requests: What CISOs Ask to See, Not Just Hear

A mature evaluation moves past self-attestation to documentary evidence: the actual SOC 2 report with the auditor's exceptions noted (not the marketing summary), a redacted penetration test executive summary from the last twelve months, the actual sub-processor list rather than a promise that one exists, and evidence of patch management cadence such as time-to-patch metrics for critical vulnerabilities. Ask specifically for evidence tied to a recent time period — a SOC 2 report from three years ago with no bridge letter covering the gap tells you almost nothing about current controls. A vendor's willingness to share this evidence, versus resistance or delay, is itself diagnostic; genuine maturity comes with genuine confidence in showing the underlying reality.

## Fourth-Party Risk: The Question Most Questionnaires Miss

Standard questionnaires focus heavily on the vendor's own controls and rarely probe deeply into the vendor's own vendors — the fourth parties whose failures become your risk indirectly. Ask specifically which critical sub-processors and infrastructure providers the vendor depends on, whether those relationships are themselves assessed and re-assessed periodically, and what contractual flow-down protections exist requiring the vendor's own vendors to meet equivalent security standards. A vendor with excellent internal controls sitting on top of an unvetted fourth-party dependency has a real, often invisible, risk concentration that the standard questionnaire structure simply doesn't surface.

## Red Flags in How Vendors Respond

Beyond the content of answers, the pattern of response is diagnostic. A questionnaire completed suspiciously fast with uniformly positive answers and no qualifications or "partially" responses is a signal, not a reassurance — real security programs have gaps, and a vendor unwilling to disclose any is either not being candid or hasn't actually assessed their own posture rigorously enough to find them. Resistance to providing evidence beyond the questionnaire itself, generic answers that could apply to any company rather than specifics about their actual environment, and an inability to name who internally owns security (a specific role, not "the team") are all patterns experienced evaluators weight heavily, independent of the specific answers given.

## Making the Final Call

Use the standardized questionnaire (CAIQ, SIG, or VSA depending on your sector) as the efficient first filter it's designed to be, but treat a clean result as the start of the evaluation, not the end. Reserve your follow-up effort for evidence requests and specificity probes on the areas that matter most for the relationship — incident history, access de-provisioning, and fourth-party dependencies consistently reveal more real risk than the standardized form itself.

Manifera maintains documented security practices and can provide evidence-backed answers to vendor security questionnaires as a standard part of client onboarding, not as a scramble triggered by the first request. If your organization needs a development partner ready to withstand real due diligence rather than just complete a form, our [about us](https://www.manifera.com/about-us/our-way-of-working/) page details how governance is built into daily delivery practice.

## Frequently Asked Questions

### What's the difference between CAIQ, SIG, and VSA vendor questionnaires?

CAIQ, maintained by the Cloud Security Alliance, focuses on cloud service controls and maps to the CSA's Cloud Controls Matrix. SIG, available in full and Lite versions, covers broader operational risk including privacy and business continuity. VSA is shorter and more security-focused, popular among tech companies specifically. Depth varies significantly between them, so knowing which one a vendor completed changes how much weight to give a clean result.

### Why is a questionnaire completed entirely with "Yes" answers a warning sign?

Real security programs have gaps, and a vendor unwilling to disclose any, or to qualify answers with "partially" or specific scope limitations, is either not being candid or hasn't rigorously assessed their own posture enough to find the gaps. A questionnaire completed suspiciously fast with uniform positive answers deserves more scrutiny, not less.

### What evidence should a CISO request beyond the standardized questionnaire itself?

The actual SOC 2 report with auditor exceptions noted, a redacted penetration test executive summary from the last twelve months, the current sub-processor list, and patch management metrics such as time-to-patch for critical vulnerabilities. Evidence should be tied to a recent time period — an old report with no bridge letter covering the gap tells you little about current controls.

### What is fourth-party risk and why do standard questionnaires miss it?

It's the risk introduced by a vendor's own vendors — sub-processors and infrastructure providers whose failures become your risk indirectly. Standard questionnaires focus on the vendor's own controls and rarely probe how those third parties are assessed, leaving a real, often invisible risk concentration unaddressed.

### What follow-up question reveals more than "do you have an incident response plan"?

Asking a vendor to walk through their last actual security incident — what happened, how long detection took, and what changed afterward — forces a concrete answer that a generic, hypothetical response can't fake. A vendor claiming zero incidents ever occurred, at any meaningful scale, is itself worth probing further.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What's the difference between CAIQ, SIG, and VSA vendor questionnaires?", "acceptedAnswer": {"@type": "Answer", "text": "CAIQ, maintained by the Cloud Security Alliance, focuses on cloud service controls and maps to the CSA's Cloud Controls Matrix. SIG, available in full and Lite versions, covers broader operational risk including privacy and business continuity. VSA is shorter and more security-focused, popular among tech companies specifically. Depth varies significantly between them, so knowing which one a vendor completed changes how much weight to give a clean result."}},
    {"@type": "Question", "name": "Why is a questionnaire completed entirely with \"Yes\" answers a warning sign?", "acceptedAnswer": {"@type": "Answer", "text": "Real security programs have gaps, and a vendor unwilling to disclose any, or to qualify answers with 'partially' or specific scope limitations, is either not being candid or hasn't rigorously assessed their own posture enough to find the gaps. A questionnaire completed suspiciously fast with uniform positive answers deserves more scrutiny, not less."}},
    {"@type": "Question", "name": "What evidence should a CISO request beyond the standardized questionnaire itself?", "acceptedAnswer": {"@type": "Answer", "text": "The actual SOC 2 report with auditor exceptions noted, a redacted penetration test executive summary from the last twelve months, the current sub-processor list, and patch management metrics such as time-to-patch for critical vulnerabilities. Evidence should be tied to a recent time period — an old report with no bridge letter covering the gap tells you little about current controls."}},
    {"@type": "Question", "name": "What is fourth-party risk and why do standard questionnaires miss it?", "acceptedAnswer": {"@type": "Answer", "text": "It's the risk introduced by a vendor's own vendors — sub-processors and infrastructure providers whose failures become your risk indirectly. Standard questionnaires focus on the vendor's own controls and rarely probe how those third parties are assessed, leaving a real, often invisible risk concentration unaddressed."}},
    {"@type": "Question", "name": "What follow-up question reveals more than \"do you have an incident response plan\"?", "acceptedAnswer": {"@type": "Answer", "text": "Asking a vendor to walk through their last actual security incident — what happened, how long detection took, and what changed afterward — forces a concrete answer that a generic, hypothetical response can't fake. A vendor claiming zero incidents ever occurred, at any meaningful scale, is itself worth probing further."}}
  ]
}
</script>
