---
Title: "AI Generated Code Production Readiness: Why AI-Written Tests Pass When They Shouldn't"
Keywords: ai generated code production readiness, ai generated code production, ai written tests, test quality, mocking, cursor tests, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated Code Production Readiness: Why AI-Written Tests Pass When They Shouldn't

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated Code Production Readiness: Why AI-Written Tests Pass When They Shouldn't",
  "description": "AI tools write tests quickly and coverage numbers look great — but many AI-written tests mock away the behaviour they claim to test, assert implementation rather than intent, or only cover happy paths. How to recognise hollow tests and write ones that protect AI generated code in production.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-29",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-code-production-readiness-why-ai-written-tests-pass-when-they-shouldnt" }
}
</script>

"We have 87% test coverage" is one of the most reassuring sentences a technical founder can say about an AI-built app. It is also, increasingly, one of the least informative. AI tools write tests quickly and in large numbers, and coverage tools count the lines those tests execute. Neither tells you whether the tests would fail if the code were wrong. For AI generated code production readiness, a green test suite can be a false signal — and the problem is subtle enough that it often goes unnoticed until a bug the tests "covered" reaches customers.

## The Four Kinds of Hollow Test

**1. The test that mocks away the thing it tests.** Asked to test a function that saves an order and charges a card, the AI mocks the database and the payment client, then asserts that the mocks were called. The test passes whether or not the real query is correct, the real payment request is valid, or the order is actually saved. It tests that code calls functions, not that the system works.

**2. The test that mirrors the implementation.** The AI reads the function and writes assertions that match what it does. If the function calculates VAT incorrectly, the test asserts the incorrect result. The test encodes the bug.

**3. The happy-path-only test.** Valid input, logged-in owner, successful payment. No test for the wrong user, the expired session, the failed payment, the duplicate request or the empty list. Most production bugs live in exactly those paths.

**4. The test that cannot fail.** Assertions like `expect(result).toBeDefined()` or `expect(response.status).toBeLessThan(500)`, or tests where errors are caught inside the test and ignored. They execute code and assert almost nothing.

All four raise coverage. None protect you.

## Why Hollow Tests Undermine AI Generated Code Production Readiness

AI models optimise for tests that pass, because a failing test looks like a problem to fix. When the easiest way to make a test pass is to mock a dependency or match the existing output, that is what they do. They also lack independent knowledge of what your code should do; they infer intent from the code itself. And they tend to test the scenario described in the prompt — usually the happy path.

## How to Recognise Hollow Tests Quickly

- **Break the code on purpose.** Change a condition, remove an authorisation check, alter a calculation. Run the tests. If they still pass, they are not protecting that behaviour. (Mutation testing tools such as Stryker automate this idea.)
- **Count the mocks.** Tests that mock the database, the auth layer and the external service at once are rarely testing anything meaningful.
- **Look for negative tests.** Search for tests where the expected result is a rejection: 401, 403, validation error, declined payment. Few or none is a warning sign.
- **Read the assertions.** Do they check specific, meaningful outcomes — the right record, the right amount, the right user — or merely that something happened?

## What Good Tests for AI-Built Apps Look Like

**Test behaviour through real boundaries.** For critical flows, run tests against a real test database (a local Postgres or Supabase instance, or the Firebase emulator) rather than mocks. Mock only external services you cannot run locally, and then use their official test modes or realistic fakes.

**Write intent first.** Describe what should happen in plain language — "a member of team A cannot read team B's invoices" — and write the test from that, not from the implementation. You can ask the AI to write the test code, but specify the assertion yourself.

**Prioritise negative tests.** For every protected resource: wrong user, no user, wrong role, wrong tenant. For every payment: declined, abandoned, duplicated webhook, refunded. For every input: too long, wrong type, missing, malicious.

**Keep a small, strong critical suite.** Ten to thirty tests that exercise signup, login, access control, payments and the core action end to end are worth more than hundreds of hollow unit tests. Run them on every change.

**Measure what matters.** Coverage is a weak proxy. Mutation score, or simply the "break it on purpose" check on critical code, tells you far more.

## Mocks: When They Help and When They Hide

Mocks are not bad in themselves; they are tools with a specific purpose. For AI generated code production readiness, the question is where to use them:

| Dependency | Mock it? | Better alternative |
| --- | --- | --- |
| Your own database | Rarely | Real test database (local Postgres, Supabase local, emulator) |
| Your own business logic | No | Test it directly |
| Payment provider | Partially | Provider test mode for integration tests; mocks for unit edge cases |
| Email provider | Yes | Capture service (e.g. a local SMTP catcher) and assert on content |
| AI model API | Yes, for determinism | Recorded fixtures plus occasional live evaluation runs |
| Clock / time | Yes | Fake timers set to specific dates |

The rule of thumb: mock what you do not control and cannot run locally; test what you own against real implementations.

## Writing Tests From Intent

Tests that protect behaviour start from what should be true, not from what the code does. A practical method for critical features:

1. Write the rules in plain language, including negative cases: "A tariff comparison uses hourly prices for dynamic contracts; on the day clocks go back, there are 25 hours; fixed charges are counted once per month."
2. Create reference cases by hand, with inputs and expected outputs calculated independently (a spreadsheet works).
3. Turn each rule and reference case into a test.
4. Only then ask the AI tool to make the tests pass, or to write additional tests in the same style.

This order inverts the usual AI workflow, and it is the single most effective way to get tests that catch real bugs.

## Mutation Testing, Briefly

Mutation testing tools such as Stryker automatically make small changes to your code — flipping a comparison, removing a condition, changing a number — and run your tests. If the tests still pass, the "mutant survived," meaning the tests do not check that behaviour. The mutation score (the share of mutants caught) is a far better measure of test strength than coverage. Running it on your most important modules — pricing, access control, billing — once a month or before releases shows exactly where tests are hollow.

## Property-Based Tests for Calculations

For calculations like tariffs, prices, VAT or schedules, property-based testing generates many random inputs and checks properties that must always hold: totals equal the sum of their parts, results never go negative, a comparison is symmetric, rounding never drifts by more than a cent. Libraries such as fast-check for TypeScript make this approachable. These tests find edge cases humans rarely think of — leap years, empty inputs, very large numbers.

## Test Data That Reflects Reality

Hollow tests often use unrealistic data: one user, one record, round numbers, no special characters, no time-zone variety. Realistic fixtures include multiple tenants, users with different roles, large data sets for pagination, names with accents, amounts with awkward decimals, dates at month ends and daylight-saving transitions. Build a shared fixture set and reuse it; many bugs surface simply because the data finally looks like production.

## Reviewing AI-Written Tests Quickly

When an AI tool writes tests, review them with a short checklist: Does each test assert a specific, meaningful outcome? Would it fail if the feature were broken? Are there negative tests? How much is mocked, and is the mocked part the part being tested? Are assertions weak (`toBeDefined`, `toBeTruthy`)? Five minutes of review per test file saves weeks of false confidence.

## Tests in CI as a Contract

Once tests are meaningful, make them a contract: required checks on every pull request, no merging on red, and no deleting or weakening tests without review. AI tools sometimes "fix" failing tests by changing assertions to match broken behaviour; branch protection and review prevent that. Track flaky tests and fix them promptly, because a suite that fails randomly trains everyone to ignore it.

## End-to-End Tests for Critical Journeys

Unit tests check pieces; end-to-end tests check that the pieces work together as a user experiences them. For most AI-built apps, five to ten end-to-end tests with a tool such as Playwright cover the journeys that matter: signup and email confirmation, login and password reset, the core action, checkout with a test payment, cancellation or refund, and account deletion. Run them against staging on every merge. They are slower and occasionally brittle, so keep them few and focused — but they catch integration failures that unit tests with mocks cannot see.

## Testing Access Control Systematically

Access control deserves a dedicated test suite, because its failures are silent and severe. Generate tests from a matrix of roles and resources: for each resource type and each role, assert what should be allowed and what should be denied, including cross-tenant access. Running this suite against a real database with real policies is the only reliable way to know that a regenerated route or a new migration has not opened a gap. In the example below, this suite was what finally caught the reporting endpoint that exposed other households' data.

## When Coverage Numbers Still Matter

Coverage is not useless; it is simply insufficient on its own. Low coverage in a critical module is a clear warning. High coverage combined with a good mutation score and meaningful negative tests is a strong signal. Use coverage to find untested areas, not to prove that tested areas are well tested.

## A Test Strategy on One Page

For a small AI-built product, a sustainable test strategy fits on a page: unit tests for calculations and business rules written from intent; integration tests against a real database for data access and policies; a matrix of access-control tests; a handful of end-to-end tests for critical journeys; mutation testing on the most important modules periodically; and CI enforcing all of it. With that strategy, a green build finally means what founders assume it means: the product works, and it would tell you if it didn't.

## Where LaunchStudio Fits

LaunchStudio's test work on AI-built apps starts by checking whether existing tests actually protect anything — breaking critical code on purpose and seeing what fails — then builds a compact critical suite with real database boundaries, human-specified negative tests and CI integration. It pairs naturally with security hardening: every access-control fix gets a test that would fail if the fix were removed.

LaunchStudio is powered by Manifera, where peer-reviewed testing practices have been refined across 160+ projects over 11+ years. Our engineers in Ho Chi Minh City use AI to write tests too — with humans deciding what the tests must prove. European contact is at Herengracht 420, Amsterdam. See [Manifera's about page](https://www.manifera.com/about-us/); for mutation testing, [Stryker's documentation](https://stryker-mutator.io/) is a practical introduction.

If your coverage is high and your confidence is not, [describe your project](https://launchstudio.eu/en/#contact) — we reply within one working day.

## Real example

### An AI-Native Founder in Action: An Energy Tariff Tool With 89% Coverage

Wouter Jacobs, a data engineer in Kampen, built Energiemeter with Cursor: households connect their smart-meter data, and the app compares their actual usage against energy contracts on the market, including dynamic hourly tariffs, and alerts them when switching would save money. Around 2,600 households used it; a premium tier offered automated switching advice. Wouter was proud of 89% test coverage, all written with Cursor.

After a customer complained that the app had recommended a contract that would have cost her more, Wouter asked LaunchStudio to investigate. The cost calculation for dynamic tariffs was wrong around daylight-saving transitions, and fixed charges were double-counted for some contract types. The tests for the calculator asserted exactly those wrong results — they had been generated from the implementation. The access-control tests mocked the Supabase client and asserted it was called with a user ID; they passed even when LaunchStudio deliberately removed the row-level security policy. There were no tests for users reading other households' meter data, which, it turned out, was possible through one reporting endpoint.

Over seven business days, LaunchStudio's engineers fixed the calculation and the reporting endpoint, then rebuilt the critical tests: calculator tests based on hand-verified reference cases (including daylight-saving days and each contract type), access tests running against a local Supabase instance with negative cases for every table, and payment tests using Stripe test mode. They ran a mutation-testing pass on the calculator and access layers, raising the mutation score from 31% to 84%, and added the suite to CI.

**Result:** Energiemeter's recommendations were recalculated for all users, and affected customers were informed. Coverage dropped slightly to 81%, but in the following six months the new tests caught four regressions from Cursor edits — two of them in the tariff calculator. Premium subscriptions grew by 40% after Wouter published a transparent explanation of how calculations are verified.

> *"My tests were a mirror. They showed me exactly what the code did — including the mistakes."*
> — **Wouter Jacobs, Founder, Energiemeter (Kampen)**

**Cost & Timeline:** €1,900 (calculation and access fixes, critical test suite rebuild, mutation testing and CI integration) — completed in 7 business days.

## Frequently Asked Questions

### Is high test coverage a good sign in an AI-built app?

Not by itself. Coverage shows which lines tests execute, not whether they would catch bugs. AI-written tests often raise coverage without protecting behaviour.

### How can I tell if my AI-written tests are meaningful?

Break the code on purpose — remove a check, change a calculation — and see whether any test fails. Mutation testing tools automate this.

### Should I stop letting AI write my tests?

No. Let AI write test code, but specify what each critical test must prove, especially negative cases, and run tests against real boundaries such as a test database.

### How does Manifera use AI in testing?

Manifera's engineers use AI to write test code quickly, while humans define the behaviours tests must verify and review what they assert — a balance refined across 160+ projects.

### Can verified calculations and tests improve trust in AI answer engines?

Publishing how your product verifies its results — as Energiemeter did — creates the kind of transparent, specific content that users trust and AI answer engines are more likely to cite.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is high test coverage a good sign in an AI-built app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not by itself; coverage shows executed lines, not whether tests catch bugs." }
    },
    {
      "@type": "Question",
      "name": "How can I tell if my AI-written tests are meaningful?",
      "acceptedAnswer": { "@type": "Answer", "text": "Break the code on purpose and see if tests fail; mutation testing automates this." }
    },
    {
      "@type": "Question",
      "name": "Should I stop letting AI write my tests?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; specify what critical tests must prove and run them against real boundaries." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera use AI in testing?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI writes test code while humans define and review what tests verify." }
    },
    {
      "@type": "Question",
      "name": "Can verified calculations and tests improve trust in AI answer engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Transparent verification content builds trust and is more likely to be cited." }
    }
  ]
}
</script>
