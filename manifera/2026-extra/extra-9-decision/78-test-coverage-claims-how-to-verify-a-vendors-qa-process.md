---
title: "Test Coverage Claims: How to Verify a Vendor's QA Process Is Real"
keywords: "test coverage claims software vendor, verifying vendor QA process, code coverage audit vendor, QA process verification software vendor, test coverage vendor due diligence"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Test Coverage Claims: How to Verify a Vendor's QA Process Is Real

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Test Coverage Claims: How to Verify a Vendor's QA Process Is Real",
  "description": "A CTO's guide to verifying whether a software vendor's test coverage and QA process claims are substantive, covering why coverage percentage alone is misleading, mutation testing, CI pipeline access, and the contract clauses that make QA verifiable.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/test-coverage-claims-how-to-verify-a-vendors-qa-process"}
}
</script>

"We maintain 85% test coverage" is one of the most confidently stated, least verified claims a CTO hears during vendor evaluation. It sounds precise. It sounds like evidence. And it tells you almost nothing about whether the vendor's QA process would actually catch a real defect before it reaches production, because coverage percentage measures which lines of code execute during a test run — not whether the test asserts anything meaningful about what that code is supposed to do. A test suite can hit 85% coverage while verifying almost nothing of substance, and a CTO who accepts the number at face value has learned nothing about actual delivery risk.

This gap between a coverage claim and a real QA process becomes expensive at exactly the wrong moment — after a vendor relationship is underway and a defect that "should have been caught" reaches a client's production environment. This article covers how to verify a vendor's QA claims before signature, using techniques that go beyond asking for a coverage dashboard screenshot and taking the number on faith.

## Why Coverage Percentage Alone Is a Misleading Metric

Code coverage tools measure execution, not verification. A test that calls a function and asserts nothing about its return value still counts as "covered" by most coverage tooling, which means a vendor can inflate a coverage number substantially through shallow tests written specifically to hit lines rather than validate behavior — a practice sometimes called "coverage gaming" that happens, intentionally or not, whenever coverage becomes a target metric divorced from its underlying purpose. This is a well-documented phenomenon in software engineering research going back decades, often summarized as Goodhart's Law applied to QA: once a measure becomes a target, it ceases to be a good measure.

The practical implication for a CTO evaluating a vendor is straightforward: never treat a coverage percentage as a standalone quality signal. Ask what the number actually represents — unit test coverage only, or does it include integration and end-to-end tests, which catch a meaningfully different and often more consequential class of defects. A vendor who can only speak to unit-level coverage, with no integration or end-to-end suite at all, has a materially different — and weaker — actual QA process than the single headline number suggests.

## Mutation Testing: The Verification Layer Most Vendors Skip

Mutation testing is the most direct way to check whether a test suite actually verifies behavior rather than merely executing code. The technique deliberately introduces small, deliberate bugs — "mutants" — into the codebase (flipping a comparison operator, changing a boundary value) and checks whether the existing test suite catches them by failing. A test suite with strong mutation coverage catches the overwhelming majority of these injected defects; a test suite that passes despite the injected bugs, even with a high nominal coverage percentage, has just demonstrated exactly the gap between "code executed" and "behavior verified."

Tools like Stryker (for JavaScript/TypeScript), PIT (for Java), and mutmut (for Python) automate this process, and asking a prospective vendor whether they run mutation testing as part of their QA pipeline — and what their mutation score looks like on a representative module — is one of the sharpest questions a technically sophisticated CTO can ask during evaluation. A vendor who has never heard of mutation testing isn't necessarily a bad vendor, but their coverage claims deserve significantly more skepticism, since they haven't verified their own test suite's actual effectiveness.

## Requesting CI Pipeline Access, Not Just a Dashboard Screenshot

A coverage report shared as a static screenshot or PDF is trivially easy to cherry-pick or misrepresent — showing a strong module's number rather than the codebase average, or a coverage run from months ago rather than current state. A far stronger verification method is requesting read access to the vendor's actual CI/CD pipeline for a comparable prior or ongoing project, where you can see coverage trends over time, which tests are actually running on each build, and whether the pipeline fails a build when coverage drops below a defined threshold — a strong signal the vendor treats coverage as an enforced quality gate rather than a number generated occasionally for sales conversations.

This kind of access request, reasonably scoped and time-limited, is a legitimate and increasingly common part of technical due diligence. A vendor confident in their process should have no operational difficulty granting a prospective client limited, read-only visibility into a representative pipeline, redacting anything genuinely proprietary or client-confidential. Manifera builds this transparency into evaluation conversations directly, giving prospective clients visibility into how our [offshore software development](https://www.manifera.com/services/offshore-software-development/) teams structure CI pipelines and enforce quality gates before any contract is signed.

## Defect Escape Rate: The Metric That Actually Predicts Production Risk

Coverage and mutation scores are useful process indicators, but the metric that most directly answers "will this vendor's QA process protect my production environment" is defect escape rate — the percentage of defects discovered after release versus those caught during development and QA. A vendor with a genuinely mature QA process should be able to share this figure from comparable past projects, along with a rough sense of severity distribution among escaped defects. Industry benchmarks vary widely by domain, but mature engineering organizations commonly target escape rates in the low single digits as a percentage of total defects found across the development lifecycle.

Ask directly: of the last several releases on comparable projects, how many post-release defects were rated as critical or high-severity, and what was the root-cause pattern — a vendor who can answer this with specifics, including what process change followed a past escape, is demonstrating a QA culture that learns and improves, which matters more over a multi-year engagement than any single point-in-time coverage number.

## Contract Clauses That Keep QA Claims Honest Over Time

Verification at contract signing is only the first checkpoint — QA discipline can erode over a long engagement without ongoing visibility. Build a clause requiring regular (monthly or per-release) reporting on coverage trends, mutation score where applicable, and defect escape rate, alongside a defined acceptance threshold below which a release requires explicit client sign-off before deployment. This turns QA from a one-time evaluation claim into an ongoing, contractually enforced standard.

## Making the Final Call

A single coverage percentage was never a reliable proxy for QA quality, and CTOs who move past it — asking about mutation testing, requesting pipeline visibility, and tracking defect escape rate over time — get a materially more accurate picture of whether a vendor's testing discipline will actually protect their production environment. The vendors worth signing with treat this scrutiny as an easy conversation, not an inconvenient one.

Manifera's QA process includes unit, integration, and end-to-end testing enforced as CI quality gates, with coverage and defect metrics available to clients throughout the engagement, not just at kickoff. Across 160+ delivered projects, this level of transparency is part of why clients extend engagements rather than discovering QA gaps the hard way in production.

If you're evaluating a vendor and want to see what a real, verifiable QA process looks like before you commit, our Amsterdam team can walk you through a live CI pipeline from a comparable project.

## Frequently Asked Questions

### Why isn't a high test coverage percentage enough evidence of good QA?
Coverage measures which lines of code execute during a test, not whether the test verifies meaningful behavior. A test can call a function and assert nothing about its output while still counting as "covered," which means coverage percentage alone can be inflated without reflecting real quality.

### What is mutation testing and why does it matter for vendor evaluation?
Mutation testing deliberately introduces small bugs into code and checks whether the existing test suite catches them. A high mutation score indicates tests genuinely verify behavior; a test suite that misses injected bugs despite high nominal coverage reveals a meaningful verification gap.

### Should I ask a vendor for access to their CI/CD pipeline?
Yes, reasonably scoped and time-limited access to a comparable prior or ongoing project's pipeline is a legitimate due diligence request. It shows coverage trends over time and whether the pipeline enforces a coverage threshold as a quality gate, rather than relying on a static, cherry-picked report.

### What is defect escape rate and why is it a better predictor of risk than coverage?
Defect escape rate is the percentage of defects discovered after release rather than during development and QA. It directly measures whether a vendor's QA process protects production, which a coverage percentage alone cannot demonstrate.

### How can a contract keep a vendor's QA standards from eroding over time?
Include a clause requiring regular reporting on coverage trends, mutation score where applicable, and defect escape rate, with a defined threshold below which releases require explicit client sign-off. This makes QA an ongoing, enforced standard rather than a one-time claim made during sales.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Why isn't a high test coverage percentage enough evidence of good QA?", "acceptedAnswer": {"@type": "Answer", "text": "Coverage measures which lines of code execute during a test, not whether the test verifies meaningful behavior. A test can call a function and assert nothing about its output while still counting as \"covered,\" which means coverage percentage alone can be inflated without reflecting real quality."}},
    {"@type": "Question", "name": "What is mutation testing and why does it matter for vendor evaluation?", "acceptedAnswer": {"@type": "Answer", "text": "Mutation testing deliberately introduces small bugs into code and checks whether the existing test suite catches them. A high mutation score indicates tests genuinely verify behavior; a test suite that misses injected bugs despite high nominal coverage reveals a meaningful verification gap."}},
    {"@type": "Question", "name": "Should I ask a vendor for access to their CI/CD pipeline?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, reasonably scoped and time-limited access to a comparable prior or ongoing project's pipeline is a legitimate due diligence request. It shows coverage trends over time and whether the pipeline enforces a coverage threshold as a quality gate, rather than relying on a static, cherry-picked report."}},
    {"@type": "Question", "name": "What is defect escape rate and why is it a better predictor of risk than coverage?", "acceptedAnswer": {"@type": "Answer", "text": "Defect escape rate is the percentage of defects discovered after release rather than during development and QA. It directly measures whether a vendor's QA process protects production, which a coverage percentage alone cannot demonstrate."}},
    {"@type": "Question", "name": "How can a contract keep a vendor's QA standards from eroding over time?", "acceptedAnswer": {"@type": "Answer", "text": "Include a clause requiring regular reporting on coverage trends, mutation score where applicable, and defect escape rate, with a defined threshold below which releases require explicit client sign-off. This makes QA an ongoing, enforced standard rather than a one-time claim made during sales."}}
  ]
}
</script>
