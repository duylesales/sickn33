---
title: "Software Quality Assurance: Why 'We Test Everything' Usually Means Almost Nothing"
keywords: "software quality assurance, software quality, qa testing"
buyer_stage: "Consideration"
target_persona: "VP of Engineering"
---

# Software Quality Assurance: Why "We Test Everything" Usually Means Almost Nothing

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Quality Assurance: Why 'We Test Everything' Usually Means Almost Nothing",
  "description": "A VP of Engineering's guide to why a vague claim of comprehensive software quality assurance is almost worthless, and what a genuinely verifiable QA practice actually looks like.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/software-quality-assurance" }
}
</script>

"We test everything" is one of the most common claims in software development and one of the least meaningful, because "everything" is doing enormous, unverified work in that sentence, and a VP of Engineering who accepts the claim at face value is trusting a word, not a process.

**The Pain:** A VP of Engineering evaluating an internal team's software quality assurance practice, or a vendor's, keeps hearing the same reassurance — comprehensive testing, high coverage, rigorous QA — without any of it being backed by a number or an artifact that could actually be checked. The claim sounds thorough. Nobody has verified whether it's true.

**The Agitation:** Vague QA claims that turn out to be inaccurate don't fail during the sales conversation or the internal status update — they fail in production, when a defect that "comprehensive testing" should have caught reaches real customers, and by then the cost of the gap is measured in incident response, customer trust, and the specific embarrassment of having assured leadership that quality was covered. Production incidents traced back to inadequate QA coverage typically cost €20,000-€60,000 per significant incident once remediation, customer communication, and engineering time are counted.

## What Verifiable Software Quality Assurance Actually Requires

Genuine software quality assurance is checkable, not just claimed, and a VP of Engineering evaluating an internal team or an external vendor should ask for the specific artifacts that separate real QA practice from a reassuring sentence.

The first checkable element is test coverage measured against the specific paths that carry real risk, not an aggregate percentage that can hide gaps behind simple code that's easy to test. Ask specifically what percentage of the payment logic, the authentication flow, or whatever the highest-stakes module is has genuine test coverage — a team with real QA discipline has this number ready; a team without it deflects to the aggregate figure, which frequently conceals exactly the gap that matters most.

The second checkable element is whether QA is structurally independent from development, or performed by the same people who wrote the code, testing their own assumptions. A developer testing their own code has an inherent blind spot — the same mental model that produced the bug is the one checking for it, and it tends not to catch its own errors. Genuine QA independence means a different person, or a genuinely separate automated process, verifies the work against requirements the developer didn't define.

The third checkable element is whether the QA process includes genuine edge-case and adversarial testing, not just verification that the intended happy path works. Ask specifically how the team tests for malformed input, unexpected user behavior, and failure conditions in dependencies — a team with real QA discipline has specific practices for this; a team without it tests the feature the way it was designed to be used and calls that comprehensive.

The fourth checkable element is defect-escape rate — the percentage of bugs that reach production versus get caught before release — tracked explicitly over time as a real metric, not estimated from memory. A team that can produce this number, and can show it improving or at least being actively managed, has genuine QA discipline. A team that's never measured it has no actual basis for the "we test everything" claim beyond confidence.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch leads require verifiable QA artifacts — critical-path coverage numbers, defect-escape rate tracking — as standard practice, not accepted claims.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam run structurally independent QA with genuine edge-case testing, producing the specific evidence that makes a quality claim checkable rather than just reassuring.

This is Dutch Management × Vietnamese Mastery: European rigor in verifying quality claims, paired with execution capacity that produces the evidence to back them. Learn more about [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) and how genuinely verifiable QA prevents the production incident a vague claim didn't actually protect against.

## Case Study & Testimonial

### A Brussels Fintech's Unverified Coverage Claim

Belgische Betaaltechnologie NV, a Brussels-based fintech, had an internal team that consistently reported "comprehensive test coverage" in status updates, and when a currency-conversion edge case caused a production incident affecting several hundred transactions, the post-incident review discovered the actual test coverage on the currency-conversion module was under 15%, buried behind a healthy-looking aggregate coverage number dominated by simple, low-risk code.

Manifera rebuilt test coverage specifically targeting the highest-risk financial logic, established structurally independent QA review, and began tracking defect-escape rate explicitly as a standing metric reported to leadership. The following twelve months produced zero comparable incidents, with the tracked defect-escape rate giving leadership an actual number to trust instead of a reassuring sentence.

> *"We'd been told 'comprehensive coverage' for two years and it turned out to mean almost nothing about the fifteen percent of the codebase that actually mattered. Now we know the real number, for the parts that matter, and it's the number that actually protects us."*
> — **VP of Engineering, Belgische Betaaldiensten NV, Belgium**

## Vague QA Claims vs. Manifera's Verifiable QA Practice

| Criteria | Vague QA Claims | Manifera's Verifiable QA Practice |
|---|---|---|
| Coverage measurement | Aggregate percentage, hides gaps | Critical-path coverage, checked directly |
| QA independence | Developers testing their own code | Structurally independent review |
| Edge-case testing | Happy-path verification only | Genuine adversarial and edge-case testing |
| Defect-escape tracking | Not measured, estimated from memory | Tracked explicitly as a standing metric |
| Production incident risk | Discovered only after a real incident | Actively managed and reduced |

## The Economics

A vague "we test everything" claim that turns out to conceal a real gap typically surfaces as a production incident costing €20,000-€60,000 in remediation, customer communication, and engineering time once it's discovered — a cost that verifiable, targeted QA coverage on genuinely high-risk modules would have prevented at a fraction of the price. [Talk to Manifera](https://www.manifera.com/contact-us/) about building QA practice that's checkable, not just claimed.

## Frequently Asked Questions

### (Scenario: VP of Engineering hearing "comprehensive testing" from a team or vendor) How do we verify a claim of comprehensive software quality assurance instead of just accepting it?

Ask for specific test coverage numbers on the highest-risk modules, not an aggregate percentage, and ask to see the defect-escape rate tracked over time.

### (Scenario: VP of Engineering whose developers test their own code) Why isn't a developer testing their own code sufficient QA?

Because the same mental model that produced a bug is the one checking for it, creating an inherent blind spot that structurally independent review avoids.

### (Scenario: VP of Engineering trying to understand why aggregate coverage numbers can be misleading) Why can a healthy-looking aggregate test coverage percentage still hide a dangerous gap?

Because simple, low-risk code is easy to achieve high coverage on, which can mathematically dominate the aggregate number while the highest-risk module remains poorly tested.

### (Scenario: VP of Engineering trying to build genuine QA discipline) What's the difference between happy-path testing and genuine QA discipline?

Genuine QA discipline explicitly tests for malformed input, unexpected user behavior, and dependency failures, not just verification that the feature works as designed under normal conditions.

### (Scenario: VP of Engineering estimating the cost of inadequate QA) What does a production incident traced back to inadequate QA coverage typically cost?

Typically €20,000-€60,000 per significant incident once remediation, customer communication, and engineering time are counted.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: VP of Engineering hearing \"comprehensive testing\" from a team or vendor) How do we verify a claim of comprehensive software quality assurance instead of just accepting it?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for specific test coverage numbers on the highest-risk modules, and ask to see the defect-escape rate tracked over time." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering whose developers test their own code) Why isn't a developer testing their own code sufficient QA?", "acceptedAnswer": { "@type": "Answer", "text": "The same mental model that produced a bug is the one checking for it, creating an inherent blind spot." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering trying to understand why aggregate coverage numbers can be misleading) Why can a healthy-looking aggregate test coverage percentage still hide a dangerous gap?", "acceptedAnswer": { "@type": "Answer", "text": "Simple, low-risk code is easy to cover, which can dominate the aggregate number while the highest-risk module stays poorly tested." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering trying to build genuine QA discipline) What's the difference between happy-path testing and genuine QA discipline?", "acceptedAnswer": { "@type": "Answer", "text": "Genuine QA discipline tests for malformed input, unexpected behavior, and dependency failures, not just the designed use case." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering estimating the cost of inadequate QA) What does a production incident traced back to inadequate QA coverage typically cost?", "acceptedAnswer": { "@type": "Answer", "text": "Typically €20,000-€60,000 per significant incident once remediation and communication are counted." } }
  ]
}
</script>
