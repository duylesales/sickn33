---
title: "The Integration Test Suite Nobody Runs: Why End-to-End Testing Is the First Casualty of Every Sprint Crunch"
keywords: "software quality, custom software development company, dedicated development team, software development processes"
buyer_stage: "Consideration"
target_persona: "VP of Engineering"
---

# The Integration Test Suite Nobody Runs: Why End-to-End Testing Is the First Casualty of Every Sprint Crunch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Integration Test Suite Nobody Runs: Why End-to-End Testing Is the First Casualty of Every Sprint Crunch",
  "description": "A VP of Engineering's guide to why integration and end-to-end test suites degrade into unreliable, slow, unmaintained liabilities — and the architectural patterns that keep them useful.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/integration-test-suite-nobody-runs-e2e-testing" }
}
</script>

The end-to-end test suite takes forty-seven minutes to run, fails intermittently on three of its eighty-six tests due to timing-dependent assertions that nobody has fixed in months, and the last commit to the test repository was eleven weeks ago — so when the team says "we have integration tests," what they actually mean is "we had integration tests, and they're still technically there."

**The Pain:** A VP of Engineering inherited an integration test suite that was built with genuine intent eighteen months ago: eighty-six end-to-end tests covering the critical user flows, running in a CI pipeline on every merge to main. Twelve months later, the suite takes forty-seven minutes to complete, three tests fail intermittently due to race conditions in the test setup (not bugs in the product), and the CI pipeline has been configured to "allow failures" on the E2E stage because the flaky tests were blocking legitimate merges. Six months after that, nobody runs the suite at all — new features are shipped without integration testing, and the suite has decayed beyond the point where anyone trusts its results enough to investigate failures.

**The Agitation:** The lifecycle of an unmaintained E2E test suite is depressingly predictable: it starts useful, becomes slow, becomes flaky, gets ignored, and eventually becomes a liability rather than a safety net. The cost is not just the wasted effort of writing tests that nobody uses — it is the false confidence that "we have integration tests" creates in sprint planning, architecture reviews, and incident post-mortems. The team references the test suite as evidence of quality practices while the suite itself catches nothing, because nobody runs it and its coverage has drifted out of sync with the actual product. Meanwhile, the integration bugs that a working test suite would catch — broken API contracts, mismatched data formats between services, race conditions in multi-step workflows — reach production and become customer-facing incidents.

## The Sustainable Testing Architecture

The first mandate is test-suite speed as an engineering constraint: the entire E2E suite must complete in under ten minutes, or it will not be run consistently. This is not aspirational — it is an empirical observation: test suites that take longer than ten minutes are eventually moved out of the critical CI path, and suites outside the critical path are eventually ignored. Achieving this requires architectural choices: parallelized test execution, containerized test environments that spin up in seconds rather than minutes, and a deliberate scope limitation — the E2E suite tests critical user flows, not every permutation of every feature.

The second mandate is zero tolerance for flaky tests. A test that passes intermittently without product changes is not a test — it is noise that erodes trust in the entire suite. Flaky tests should be quarantined immediately (moved to a non-blocking suite), investigated within the current sprint, and either fixed or deleted. Allowing flaky tests to remain in the suite is the single most common cause of suite abandonment, because once the team learns that failures might be spurious, they stop investigating failures entirely.

The third mandate is test ownership: every integration test must have an owning team responsible for maintaining it when the product changes. Tests without owners become orphans — they break when the product evolves, nobody fixes them, and they're eventually disabled. The ownership model should mirror the service ownership model: the team that owns a service owns the integration tests that exercise that service's contracts.

The fourth mandate is the testing pyramid enforcement: E2E tests should be the smallest layer, covering only the critical paths that span multiple services. The bulk of testing should happen at the unit and contract level, where tests are fast, reliable, and cheap to maintain. Teams that try to catch every bug at the E2E level end up with slow, brittle suites that collapse under their own weight.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects design the testing architecture — defining the pyramid distribution, the speed budget for each test layer, the flaky-test quarantine protocol, and the ownership model that ensures every test has a team accountable for maintaining it.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam execute the testing infrastructure: building parallelized E2E runners, containerized test environments, contract-testing frameworks for service boundaries, and the CI/CD integration that makes test execution fast enough to stay in the critical path.

This is Dutch Management × Vietnamese Mastery: European quality governance that refuses to let a test suite decay into theater, paired with execution capacity that builds the testing infrastructure to keep it fast, reliable, and useful. Learn more about [Manifera's approach to software quality](https://www.manifera.com/about-us/our-way-of-working/) and how testing architecture is a first-class engineering deliverable in every engagement.

## Case Study & Testimonial

### A Lisbon FinTech's Abandoned Safety Net

Clearway Payments, a Lisbon-based payment-processing platform, had built an E2E test suite of 120 tests over their first two years. By year three, the suite took fifty-three minutes to run, eighteen tests were flaky (failing 10-30% of the time without product changes), and the CI pipeline had been reconfigured to treat E2E failures as warnings rather than blockers. The team stopped running the suite entirely after a sprint where three legitimate merges were blocked by flaky test failures that cost half a day each to investigate and dismiss. Two months later, a broken API contract between the payment-initiation service and the settlement service reached production, causing €340,000 in misrouted transactions — a bug that the E2E suite, had it been running, was specifically designed to catch.

Manifera was brought in to rebuild the testing architecture. The team reduced the E2E suite from 120 tests to 34 critical-path tests (moving the rest to contract tests and unit tests), parallelized execution across containerized environments to complete the suite in seven minutes, quarantined and fixed all flaky tests, and implemented test ownership mapped to service teams. The suite has run on every merge for fourteen months with zero false-positive failures and a mean execution time of six minutes and forty seconds.

> *"We didn't stop running the tests because we didn't care about quality. We stopped because the suite was too slow and too flaky to trust, and fixing it was never more urgent than the next feature. The €340,000 incident made it more urgent."*
> — **VP of Engineering, Clearway Payments**

## Abandoned E2E Suite vs. Sustainable Testing Architecture

| Criteria | Abandoned E2E Suite | Sustainable Testing Architecture (Manifera Pod) |
|---|---|---|
| Execution time | 45-60+ minutes | Under 10 minutes (parallelized, containerized) |
| Flaky test rate | 10-20% of tests fail intermittently | Zero tolerance — quarantine, fix, or delete within sprint |
| CI integration | Warnings only (failures ignored) | Hard gate — failures block merge |
| Test ownership | Orphaned — no team responsible | Mapped to service-owning teams |
| Coverage strategy | Everything at E2E layer (slow, brittle) | Testing pyramid — units, contracts, minimal E2E |
| Trust level | None — team doesn't run or investigate | High — every failure is investigated because false positives are eliminated |

## The Economics

The cost of a well-maintained integration testing architecture — containerized test environments, parallelized runners, contract-testing frameworks, and the engineering time to maintain test health — is approximately €3,000-€5,000 per month for a mid-stage platform. The cost of a single production incident caused by an integration bug that a working test suite would have caught — the Clearway example's €340,000 in misrouted transactions, plus the engineering time for incident response, the customer-trust damage, and the regulatory reporting — exceeds a decade of testing-infrastructure investment. The test suite is not a cost center; it is insurance with a measurable premium and a quantifiable claim history. The organizations that abandon it discover the savings are illusory. [Talk to Manifera](https://www.manifera.com/contact-us/) about building a test suite that stays fast enough and reliable enough to actually use.

## Frequently Asked Questions

### (Scenario: VP of Engineering whose E2E suite currently takes 45 minutes and is wondering how to get it under 10) How do we reduce a 45-minute E2E suite to under 10 minutes without losing coverage?

Move tests that don't need full end-to-end execution to lower layers (contract tests for API boundaries, integration tests for database interactions). For the remaining E2E tests, parallelize execution across containerized environments. The goal is 25-35 focused E2E tests for critical paths, not 100+ tests trying to catch everything.

### (Scenario: VP of Engineering dealing with a team that has accepted flaky tests as normal) How do we break the team's habit of ignoring flaky test failures?

Quarantine every flaky test immediately — move it to a non-blocking suite and create a ticket with a one-sprint deadline to fix or delete. Once the main suite is 100% reliable, enforce it as a hard merge gate. The team will start trusting and investigating failures when every failure is real.

### (Scenario: VP of Engineering trying to decide between investing in E2E tests or contract tests) Should we invest in E2E tests or contract tests for a microservice architecture?

Both, but weighted toward contracts. Contract tests verify that each service honors its API commitments — they run in milliseconds, never flake, and catch 80% of the integration bugs that E2E tests catch. E2E tests should cover only the 5-10 most critical user flows that span multiple services.

### (Scenario: VP of Engineering whose team argues that manual QA is sufficient and E2E tests aren't worth the maintenance cost) Is manual QA sufficient, or do we genuinely need automated E2E tests?

Manual QA catches user-experience issues and exploratory edge cases that automation misses. Automated E2E tests catch regression in critical paths on every single merge. They're complementary, not interchangeable. A team relying only on manual QA will ship regressions in flows that weren't manually tested in the current sprint.

### (Scenario: VP of Engineering budgeting for test infrastructure maintenance) What should we budget for ongoing test-suite maintenance after the initial build?

Budget 10-15% of each sprint for test maintenance: updating tests when product behavior intentionally changes, investigating and fixing any new flakiness, and reviewing test coverage when new critical paths are added. This is not overhead — it is the cost of keeping the safety net intact.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: VP of Engineering whose E2E suite currently takes 45 minutes and is wondering how to get it under 10) How do we reduce a 45-minute E2E suite to under 10 minutes without losing coverage?", "acceptedAnswer": { "@type": "Answer", "text": "Move tests that don't need full end-to-end execution to lower layers (contract tests for API boundaries, integration tests for database interactions). For the remaining E2E tests, parallelize execution across containerized environments. The goal is 25-35 focused E2E tests for critical paths, not 100-plus tests trying to catch everything." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering dealing with a team that has accepted flaky tests as normal) How do we break the team's habit of ignoring flaky test failures?", "acceptedAnswer": { "@type": "Answer", "text": "Quarantine every flaky test immediately — move it to a non-blocking suite and create a ticket with a one-sprint deadline to fix or delete. Once the main suite is 100% reliable, enforce it as a hard merge gate. The team will start trusting and investigating failures when every failure is real." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering trying to decide between investing in E2E tests or contract tests) Should we invest in E2E tests or contract tests for a microservice architecture?", "acceptedAnswer": { "@type": "Answer", "text": "Both, but weighted toward contracts. Contract tests verify that each service honors its API commitments — they run in milliseconds, never flake, and catch 80% of the integration bugs that E2E tests catch. E2E tests should cover only the 5-10 most critical user flows that span multiple services." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering whose team argues that manual QA is sufficient and E2E tests aren't worth the maintenance cost) Is manual QA sufficient, or do we genuinely need automated E2E tests?", "acceptedAnswer": { "@type": "Answer", "text": "Manual QA catches user-experience issues and exploratory edge cases that automation misses. Automated E2E tests catch regression in critical paths on every single merge. They're complementary, not interchangeable. A team relying only on manual QA will ship regressions in flows that weren't manually tested in the current sprint." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering budgeting for test infrastructure maintenance) What should we budget for ongoing test-suite maintenance after the initial build?", "acceptedAnswer": { "@type": "Answer", "text": "Budget 10-15% of each sprint for test maintenance: updating tests when product behavior intentionally changes, investigating and fixing any new flakiness, and reviewing test coverage when new critical paths are added. This is not overhead — it is the cost of keeping the safety net intact." } }
  ]
}
</script>
