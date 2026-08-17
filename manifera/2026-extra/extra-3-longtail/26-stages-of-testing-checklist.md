---
title: "The Testing Layers Most Teams Skip Right Before the Launch They Regret"
keywords: "software engineer stages, software developer stages, software testing, software development processes"
buyer_stage: "Awareness"
target_persona: "A"
---

# The Testing Layers Most Teams Skip Right Before the Launch They Regret

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Testing Layers Most Teams Skip Right Before the Launch They Regret",
  "description": "A checklist of the distinct testing stages a software project needs, and which ones get quietly compressed under deadline pressure most often.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/stages-of-testing-checklist" }
}
</script>

"We tested it" can mean five very different things, depending on which of the testing stages actually happened and which one quietly got skipped when the deadline got tight. Each stage catches a different class of problem, and skipping any one of them doesn't eliminate that class of problem — it just defers it to production.

## 1. Unit Testing

Verifying individual functions or components in isolation, checking that each piece of logic does exactly what it's supposed to given specific inputs. Fast to run, cheap to maintain, and the first line of defense — but unit tests passing tells you nothing about whether the pieces work correctly together.

## 2. Integration Testing

Verifying that different components or services work correctly when connected — an API call that actually reaches the database correctly, a payment flow that actually talks to the payment processor as expected. This is where many bugs live that unit tests, by design, can't catch, since unit tests deliberately isolate components from their real dependencies.

## 3. End-to-End (E2E) Testing

Simulating a real user's full journey through the application — signing up, completing a purchase, using a core feature start to finish — to catch issues that only appear when the entire system works together under realistic conditions. E2E tests are slower and more brittle than unit tests, which is exactly why they're the ones most frequently cut when a test suite needs to run faster under time pressure.

## 4. Manual Exploratory Testing

A human deliberately trying to break the application in ways automated tests weren't specifically written to check — unusual input combinations, unexpected navigation paths, edge cases a test author didn't anticipate. Automated tests only catch what someone thought to write a test for; exploratory testing catches what nobody thought of yet.

## 5. Cross-Device and Cross-Browser Testing

Verifying the application actually works across the range of devices, screen sizes, operating system versions, and browsers real users will actually use — not just the developer's own recent-model device. This is where many demo-perfect features reveal device-specific bugs that never surfaced in development.

## 6. Performance and Load Testing

Verifying the application performs acceptably under realistic and peak traffic conditions, not just with a single test user. Skipping this stage means discovering scaling problems during an actual traffic spike, which is the worst possible time to discover them.

## 7. Security Testing

Checking for common vulnerability classes — injection attacks, authentication weaknesses, exposed sensitive data — before real users and real attackers find them instead. This stage is frequently treated as optional for internal or early-stage products, a decision that gets significantly more expensive to reverse once real user data is involved.

## Why Skipping Any One Stage Just Relocates the Problem

Each of these seven stages catches a distinct category of defect that the others don't reliably catch. Skipping unit testing means logic errors surface later, more expensively. Skipping E2E testing means integration issues surface in production instead of in a test environment. Skipping security testing means vulnerabilities surface as an incident instead of a code review comment. None of these problems disappear when a testing stage is cut — they just move downstream, to a more expensive and more visible point in the project's life.

## The Safety Research Model Behind Layered Testing

Psychologist James Reason's Swiss cheese model, introduced in his 1990 book "Human Error" and now foundational across aviation safety, medicine, and industrial risk management, offers a precise way to understand why seven distinct testing stages catch more than any single stage, however thorough, ever could on its own. Reason's model pictures each layer of defense in a complex system — in his original context, each safety procedure in aviation or surgery — as a slice of Swiss cheese: solid in most places, but with holes representing that layer's specific blind spots. A single slice, no matter how well designed, always has holes somewhere. Catastrophic failure requires the holes in multiple layers to align, letting a problem pass through every defense simultaneously.

This maps almost exactly onto the seven testing stages. Unit tests have holes where integration behavior lives — they're not designed to catch cross-component issues by construction, not because anyone did unit testing badly. Integration tests have holes where a real user's full, meandering journey through the product lives. E2E tests have holes where unanticipated edge cases live, because they only test the specific paths someone thought to write a test for. Each stage's holes are different, specific, and largely predictable from what that stage is actually designed to check — which is precisely why stacking multiple stages, each covering the others' blind spots, catches dramatically more than any single stage run twice as thoroughly ever would.

Reason's model also explains, with unusual precision, why Cordovena Pay's authentication vulnerability made it all the way to a security researcher's inbox: the case study describes a process that was effectively a single slice of cheese — unit tests plus a brief manual pass — with no security-testing layer to catch what that combination structurally couldn't. It wasn't that the existing testing was performed badly; it's that a single layer, however carefully executed, has holes by its very nature, and only additional, differently-shaped layers close the gaps a lone layer leaves open by design.

## Manifera's Approach: All Seven Stages, Scoped Into the Timeline From Day One

- **Amsterdam (Governance/QA Standards):** Dutch project leads scope all seven testing stages explicitly into project timelines and budgets, rather than treating QA as flexible time that absorbs whatever schedule pressure emerges elsewhere.
- **Vietnam (Execution/Testing Discipline):** The engineering pod runs unit, integration, and E2E testing continuously throughout development, with dedicated manual exploratory, cross-device, and security testing phases before any production release.

This is Dutch Management × Vietnamese Mastery applied to quality assurance itself: European process discipline that protects testing time, paired with execution rigor across all seven distinct stages. Explore Manifera's [QA and testing practices](https://www.manifera.com/about-us/manifera-technologies/).

## Case Study: A Seville Fintech's Post-Incident Process Overhaul

Cordovena Pay, a Seville-based fintech, had a previous vendor whose testing process consisted almost entirely of unit tests and a brief manual pass before launch — no dedicated security testing stage, which resulted in an authentication vulnerability discovered by a security researcher two months after launch, requiring an emergency remediation and disclosure process.

Manifera's Amsterdam team rebuilt the testing process to include all seven stages, with dedicated security testing before every release involving authentication or payment logic. In the fourteen months since, zero security vulnerabilities have been reported by external researchers or discovered in production.

> *"We'd assumed 'we test everything' meant something specific. It turned out it meant one specific kind of testing, done reasonably well, and nothing else."*
> — **CTO, Cordovena Pay**

Cordovena's engineering team now explicitly maps each release against the seven stages using language borrowed directly from the Swiss cheese model, asking not "did we test this" but "which specific layers of coverage does this release actually pass through, and where do their holes happen to line up."

## Why Adding More of the Same Layer Doesn't Substitute for a Different One

A common but ultimately ineffective response to a testing gap is to do more of whichever stage is already being run — more unit tests, more manual clicking through the same happy path — rather than adding a genuinely different layer. Reason's model explains directly why this doesn't work: doubling the thickness of one slice of cheese doesn't close the specific holes that slice inherently has, because those holes exist by the nature of what that layer checks, not from insufficient effort. A team that already writes thorough unit tests but has no security-testing layer will not catch an authentication vulnerability no matter how many additional unit tests get added, because unit tests and security testing are checking fundamentally different things by design.

This is the most useful practical takeaway from applying Reason's model to a testing strategy: when an incident occurs, the diagnostic question isn't "did we test enough," it's "which specific layer's hole did this pass through, and do we have a layer that's actually designed to catch that particular class of problem at all." Cordovena's authentication vulnerability didn't reveal that their unit testing was too thin — it revealed that no layer existed whose job was to catch that particular class of problem in the first place, which is a different and more specific diagnosis than "test more."

## Seven Testing Stages at a Glance

| Stage | What It Catches | Most Commonly Skipped Under Pressure |
|---|---|---|
| Unit testing | Individual logic errors | Rarely |
| Integration testing | Component interaction bugs | Sometimes |
| E2E testing | Full user journey issues | Often |
| Manual exploratory | Unanticipated edge cases | Often |
| Cross-device/browser | Device-specific bugs | Often |
| Performance/load | Scaling issues under real traffic | Very often |
| Security testing | Vulnerabilities before exploitation | Very often, especially early-stage |

## Auditing Your Own Testing Process

Ask your engineering team or vendor which of these seven stages are actually part of the standard process, and which are treated as optional under deadline pressure — the gap between the two is usually where the next production incident is quietly waiting. [Schedule a free consultation with our Amsterdam team](https://www.manifera.com/contact-us/) about a QA process audit.

## Frequently Asked Questions

### (Scenario: CTO trying to prioritize limited QA time) If we can't do all seven stages thoroughly, which matters most?

It depends on your product's risk profile, but security testing and integration testing tend to catch the most consequential and expensive-to-fix-later issues if you have to prioritize under real time constraints.

### (Scenario: founder confused by "we tested it" claims from a vendor) What should I ask a vendor to clarify what "we tested it" actually means?

Ask specifically which of these seven stages were performed, and whether security and performance testing were included or treated as separate, optional scope.

### (Scenario: engineering manager trying to protect QA time) Why does E2E and security testing get cut most often under deadline pressure?

They're typically the last stages before release, making them the easiest to compress when a deadline is fixed and earlier stages have already run long — which is exactly why they need protected time scoped in from the start.

### (Scenario: CTO trying to justify security testing investment to leadership) Is security testing necessary for an early-stage product with few users?

Yes, especially if any real user data or authentication is involved — vulnerabilities discovered by external researchers or attackers are significantly more costly and damaging than ones caught in a scheduled test.

### (Scenario: founder wondering if automated testing alone is enough) Can automated testing fully replace manual exploratory testing?

No — automated tests only catch what someone specifically thought to write a test for. Manual exploratory testing catches the unanticipated edge cases that no automated suite was designed to check.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO trying to prioritize limited QA time) If we can't do all seven stages thoroughly, which matters most?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on risk profile, but security testing and integration testing tend to catch the most consequential issues if prioritization is necessary." } },
    { "@type": "Question", "name": "(Scenario: founder confused by 'we tested it' claims from a vendor) What should I ask a vendor to clarify what 'we tested it' actually means?", "acceptedAnswer": { "@type": "Answer", "text": "Ask specifically which of the seven testing stages were performed, and whether security and performance testing were included or treated as separate scope." } },
    { "@type": "Question", "name": "(Scenario: engineering manager trying to protect QA time) Why does E2E and security testing get cut most often under deadline pressure?", "acceptedAnswer": { "@type": "Answer", "text": "They're typically the last stages before release, making them easiest to compress when earlier stages have already run long." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to justify security testing investment to leadership) Is security testing necessary for an early-stage product with few users?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, especially if real user data or authentication is involved — vulnerabilities found by external researchers are far more costly than ones caught in testing." } },
    { "@type": "Question", "name": "(Scenario: founder wondering if automated testing alone is enough) Can automated testing fully replace manual exploratory testing?", "acceptedAnswer": { "@type": "Answer", "text": "No — automated tests only catch what someone specifically wrote a test for. Manual exploratory testing catches unanticipated edge cases." } }
  ]
}
</script>
