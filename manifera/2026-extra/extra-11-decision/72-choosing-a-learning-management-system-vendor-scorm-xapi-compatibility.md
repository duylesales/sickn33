---
title: "Choosing a Learning Management System Vendor: SCORM/xAPI Compatibility"
keywords: "learning management system vendor selection, SCORM xAPI compatibility, LMS vendor due diligence, LMS platform comparison, e-learning standard compliance vendor"
buyer_stage: "Decision"
target_persona: "IT Manager"
---

# Choosing a Learning Management System Vendor: SCORM/xAPI Compatibility

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Learning Management System Vendor: SCORM/xAPI Compatibility",
  "description": "An IT manager's guide to evaluating LMS vendors on real interoperability standards — SCORM, xAPI, cmi5, and LTI 1.3 — rather than a vendor's own claim of e-learning standard support.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-02",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-a-learning-management-system-vendor-scorm-xapi-compatibility"}
}
</script>

Ask an LMS vendor "do you support SCORM," and every vendor will say yes. That's not a useful test anymore — SCORM 1.2 has been the baseline floor for e-learning content interoperability since the early 2000s, and a platform that couldn't import a SCORM package would be unsellable. The question that actually separates a modern, portable LMS from one that will trap your content is more specific: which SCORM version, does it support xAPI or cmi5 as a genuine second track rather than a marketing checkbox, and what happens to your tracking data and completion records if you switch platforms in three years.

This distinction matters more than most IT managers evaluating an LMS realize going in, because content interoperability standards determine whether your organization's investment in course content and historical learner data is portable, or whether it's quietly become hostage to whichever vendor built the platform.

## SCORM 1.2 vs. SCORM 2004 vs. xAPI: Not Interchangeable

SCORM 1.2, published in 2001, is still the most widely supported packaging and tracking standard, but it's limited — it can report completion, score, and basic interaction data, and it requires content to run inside a browser frame with a persistent connection to the LMS. SCORM 2004 (through its 4th edition) added sequencing and navigation rules that let course designers branch content based on learner performance, but it's notoriously inconsistent in implementation across vendors — a SCORM 2004 package built and tested against one LMS's sequencing engine can behave differently in another's, which is one of the most common "the content plays but tracking is wrong" support tickets in the industry.

xAPI (Experience API, also called Tin Can API) is a different model entirely: instead of requiring content to run inside the LMS's frame with a live connection, it lets any application — a course, a simulation, a mobile app, even a physical device — send "statements" (actor, verb, object: "Maria completed Module 3") to a separate Learning Record Store (LRS). This means xAPI can track learning that happens outside a traditional browser-based course, which SCORM fundamentally cannot. cmi5 is a further refinement — an xAPI profile that standardizes how content launches and reports specifically within an LMS context, aiming to combine SCORM's predictable launch behavior with xAPI's flexible data model.

The vendor evaluation question: ask specifically which of these your candidate LMS supports natively versus through a third-party plugin, and ask for a live demo of a SCORM 2004 package with branching logic actually working — not just a SCORM 1.2 "quiz completes, score reports" demo, which tells you almost nothing about sequencing fidelity.

## Who Owns the LRS, and Where Does the Data Live

If xAPI matters to your use case — and it increasingly does for organizations tracking blended, informal, or on-the-job learning alongside formal courses — the critical due diligence question is whether the LRS is a first-party component you control, or a black box inside the vendor's infrastructure that you can only query through their reporting UI. A genuinely portable xAPI implementation lets you point statements at an LRS of your choosing, including a self-hosted or third-party LRS independent of the LMS vendor. A vendor that only accepts xAPI statements into its own proprietary store, with no export path in a standard xAPI statement format, has effectively built a walled garden with an open-standard label on it.

Ask explicitly: can we export the full statement history in standard xAPI JSON format, on demand, without a professional services engagement? A "yes" with a documented API endpoint is a materially different answer than a "yes" that turns out to require a support ticket and a data export fee.

## LTI 1.3 and Advantage: The Integration Layer Most Evaluations Skip

SCORM and xAPI govern how content and tracking data move. LTI (Learning Tools Interoperability), now at version 1.3 with the LTI Advantage extension, governs how external tools — a publisher's homework platform, a proctoring tool, a plagiarism checker, a video platform — plug into your LMS with single sign-on and gradebook passback. LTI 1.3 replaced the older 1.1 standard specifically to close security gaps (it uses OAuth 2.0 and OpenID Connect rather than the older, weaker signature scheme), and LTI Advantage adds standardized deep linking and Assignment and Grade Services so a third-party tool can post grades directly into your gradebook without a custom integration.

If your organization relies on third-party learning tools — and almost every mid-size-or-larger education or corporate L&D program does — verify LTI 1.3 Advantage certification specifically, not just "LTI support." A platform still running LTI 1.1 as its primary integration layer is running a standard several of the major tool providers have already begun deprecating support for.

## SIS/HRIS Integration: OneRoster and the Enrollment Data Problem

For K-12 and higher ed specifically, enrollment, roster, and gradebook sync with the Student Information System is a separate interoperability question from content standards, and it's commonly underweighted in vendor evaluations that focus entirely on SCORM/xAPI. OneRoster, maintained by the same standards body (1EdTech, formerly IMS Global) that maintains LTI, defines how roster and gradebook data move between an SIS and an LMS. A vendor with a mature OneRoster implementation can sync class rosters automatically each term; a vendor without one means your registrar's office is manually uploading CSV files every semester, and every manual upload is a data-quality incident waiting to happen. Corporate L&D buyers should ask the equivalent question about HRIS integration — is there a standard API or only manual CSV import for employee/org data.

## Content Migration: What Actually Happens When You Switch

The real test of interoperability claims is a migration scenario, and it's worth running as an actual proof-of-concept rather than taking a vendor's word for it. Request a trial migration of a representative sample of your existing SCORM packages and, if applicable, xAPI statement history, into the candidate platform, and verify: do completion records and scores import correctly, does sequencing logic in SCORM 2004 content behave the same way, and can you re-export that same content and data if you needed to move again. A vendor confident in their standards support will accommodate this test without much friction; a vendor that stalls on providing a sandbox for a migration trial is signaling how painful your actual migration — or eventual exit — will be.

This kind of interoperability-first evaluation is the same discipline we bring to [custom software development](https://www.manifera.com/services/custom-software-development/) engagements that need to integrate cleanly with existing systems rather than replace them wholesale — our [technology approach](https://www.manifera.com/about-us/manifera-technologies/) treats data portability as a design requirement, not an afterthought.

## Making the Compatibility Call

The vendors worth shortlisting are the ones that can demonstrate — not just claim — SCORM 2004 sequencing fidelity, a genuinely exportable xAPI statement store, current LTI 1.3 Advantage certification, and a real OneRoster or equivalent roster-sync integration, verified through a hands-on trial rather than a feature-matrix PDF. Standards compliance on paper and standards compliance in a working sandbox are different things, and the gap between them is exactly where LMS migrations go over budget and over schedule. If your organization is evaluating or building learning infrastructure that needs to interoperate cleanly with existing content, tools, and systems of record, [get in touch](https://www.manifera.com/contact-us/) to talk through your specific integration requirements.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "xAPI (Experience API)", "description": "An e-learning interoperability standard that lets any application send actor-verb-object statements to a Learning Record Store, enabling tracking of learning experiences outside a traditional browser-based LMS course."},
    {"@type": "ListItem", "position": 2, "name": "LTI 1.3 Advantage", "description": "The current Learning Tools Interoperability standard for plugging external tools into an LMS with secure single sign-on and standardized gradebook passback, replacing the weaker LTI 1.1 signature-based approach."}
  ]
}
</script>

## Frequently Asked Questions

### Is SCORM obsolete now that xAPI exists?
No — SCORM remains the most widely used packaging standard for self-contained e-learning courses and is unlikely to disappear soon, particularly for simple, browser-based content. xAPI extends what's trackable beyond SCORM's limits (mobile apps, simulations, blended and informal learning) but doesn't replace SCORM's role for straightforward course packaging.

### What's the practical difference between LTI 1.1 and LTI 1.3?
LTI 1.3 uses OAuth 2.0 and OpenID Connect for authentication, which is materially more secure than 1.1's older signature-based approach, and LTI Advantage adds standardized deep linking and gradebook passback (Assignment and Grade Services) that 1.1 lacks natively. Several major tool providers have begun deprecating 1.1 support, so a platform still relying on it as its primary integration layer is on a standard headed toward end-of-life.

### Do we need our own LRS, or is the LMS vendor's built-in store enough?
It depends on whether you need to track learning experiences outside the LMS itself — a simulation, a mobile app, on-the-job checklists. If you do, verify the vendor's built-in store can export full xAPI statement history in standard JSON format on demand, or plan to run a separate, vendor-independent LRS that any conformant system can send statements to.

### How do we actually test SCORM 2004 sequencing before committing to a vendor?
Request a sandbox environment and upload a SCORM 2004 package with real branching/sequencing logic — not a simple linear quiz — and verify the branching behaves as designed and that completion/score data reports correctly. This is the single most revealing test in an LMS evaluation, because sequencing engine implementations vary significantly between vendors despite all claiming SCORM 2004 support.

### What's the risk of skipping OneRoster or SIS integration during vendor evaluation?
Without a standards-based roster sync, enrollment and gradebook data typically moves through manual CSV uploads each term, which is both a recurring administrative burden and a recurring source of data-quality errors — wrong sections, missing students, stale rosters. It's worth weighting as heavily as the content-standard questions for any K-12 or higher ed deployment.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is SCORM obsolete now that xAPI exists?", "acceptedAnswer": {"@type": "Answer", "text": "No — SCORM remains the most widely used packaging standard for self-contained e-learning courses and is unlikely to disappear soon, particularly for simple, browser-based content. xAPI extends what's trackable beyond SCORM's limits (mobile apps, simulations, blended and informal learning) but doesn't replace SCORM's role for straightforward course packaging."}},
    {"@type": "Question", "name": "What's the practical difference between LTI 1.1 and LTI 1.3?", "acceptedAnswer": {"@type": "Answer", "text": "LTI 1.3 uses OAuth 2.0 and OpenID Connect for authentication, which is materially more secure than 1.1's older signature-based approach, and LTI Advantage adds standardized deep linking and gradebook passback (Assignment and Grade Services) that 1.1 lacks natively. Several major tool providers have begun deprecating 1.1 support, so a platform still relying on it as its primary integration layer is on a standard headed toward end-of-life."}},
    {"@type": "Question", "name": "Do we need our own LRS, or is the LMS vendor's built-in store enough?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on whether you need to track learning experiences outside the LMS itself — a simulation, a mobile app, on-the-job checklists. If you do, verify the vendor's built-in store can export full xAPI statement history in standard JSON format on demand, or plan to run a separate, vendor-independent LRS that any conformant system can send statements to."}},
    {"@type": "Question", "name": "How do we actually test SCORM 2004 sequencing before committing to a vendor?", "acceptedAnswer": {"@type": "Answer", "text": "Request a sandbox environment and upload a SCORM 2004 package with real branching/sequencing logic — not a simple linear quiz — and verify the branching behaves as designed and that completion/score data reports correctly. This is the single most revealing test in an LMS evaluation, because sequencing engine implementations vary significantly between vendors despite all claiming SCORM 2004 support."}},
    {"@type": "Question", "name": "What's the risk of skipping OneRoster or SIS integration during vendor evaluation?", "acceptedAnswer": {"@type": "Answer", "text": "Without a standards-based roster sync, enrollment and gradebook data typically moves through manual CSV uploads each term, which is both a recurring administrative burden and a recurring source of data-quality errors — wrong sections, missing students, stale rosters. It's worth weighting as heavily as the content-standard questions for any K-12 or higher ed deployment."}}
  ]
}
</script>
