---
Title: "Cursor and Tests: Generating a Suite You Can Trust"
Keywords: cursor tests, generated tests, test coverage, assertions, regression tests, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor and Tests: Generating a Suite You Can Trust

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor and Tests: Generating a Suite You Can Trust",
  "description": "An assistant will write two hundred tests in an hour, and most of them assert nothing useful. Which tests are worth having, how to tell a real one from a decorative one, and the order to build them in.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-and-tests-generating-a-suite-you-can-trust" }
}
</script>

Ask an AI editor to write tests for your project and you will have hundreds within the hour. They will run, they will pass, and the coverage number will be impressive.

A meaningful proportion of them will assert nothing that matters: that a component renders without throwing, that a function returns a value, that a mock was called. They pass whether or not your product works, which makes them worse than no tests, because they produce confidence without providing it.

Tests are genuinely valuable in an AI-built product — more so than in a hand-written one, because the code changes fast and unpredictably. The skill is knowing which ones to keep.

## What a Real Test Looks Like

A useful test states an expectation that could fail. The question to ask of any generated test is: what would have to break for this to go red?

"Renders without crashing" fails only if the component throws, which is rarely the interesting failure.

"Calculating VAT on €100 at 21 percent returns €121" fails if the calculation is wrong, which is exactly the thing you want to know.

"A user from organisation B requesting organisation A's invoice receives a 403" fails if your authorisation breaks, which is the most valuable assertion in the entire suite.

Read the assertions, not the names. Generated tests have excellent names and sometimes empty bodies.

## The Order Worth Building In

For a small product, thirty to fifty tests covering the right things beats four hundred covering everything.

**Authorisation first.** For each endpoint, a test that a user from another organisation is refused. This is the single most valuable set in an AI-built product, because it is the failure mode this series documents most often and because it keeps working while everything around it is rewritten.

**Money second.** Every calculation involving prices, VAT, discounts, proration, totals and refunds, with the awkward numbers rather than the round ones — amounts that produce rounding differences, zero, negative, and the largest value you accept.

**The main flow third.** One end-to-end test that signs up, does the central thing your product exists for, and verifies the outcome. It catches the deploy that broke everything, which no unit test will.

**Then every bug you have fixed twice.** A test written at the moment of the second fix guarantees there is no third, and this set grows to be the most valuable part of a mature suite.

That is a suite that runs in under a minute, that you trust, and that you will keep.

## Where Generated Tests Go Wrong

Four patterns to watch for when accepting a generated suite.

**Testing the implementation rather than the behaviour.** A test asserting that a particular internal function was called breaks when you reorganise the code without changing what it does, which trains you to ignore failures.

**Mocking everything.** A test where the database, the payment provider and the email service are all replaced by mocks verifies that your code calls mocks in the right order. The bugs are usually in the interaction with the real things.

**Asserting what the code does rather than what it should do.** A model writing tests from your implementation encodes your bugs as expected behaviour. This is the most insidious failure, because the suite then actively prevents you from fixing them.

**Coverage as the goal.** A model asked to reach 90 percent will reach it, and the last 30 percent will be tests of error branches nobody encounters, written to touch lines rather than to verify anything.

## Use the Assistant Well

Tests are an excellent use of an AI editor, provided the direction comes from you.

What works: describing the case and asking for the test. "Write a test that a user in organisation B receives a 403 when requesting an invoice belonging to organisation A." Specific, checkable, and exactly the sort of boilerplate that is tedious to write by hand.

What works less well: "write tests for this file", which produces the decorative suite described above.

Two further habits. Write the test before the fix when you are correcting a bug — confirm it fails, apply the fix, confirm it passes — which is the only way to be sure the test tests what you think. And read every assertion before accepting, because the failure mode of generated tests is passing for the wrong reason.

## Make the Suite Something You Will Keep Running

A test suite that is slow, flaky or noisy stops being run, and a suite that is not run is worse than none because it rots into a source of false alarms.

Three properties keep it alive.

**Fast.** Under a minute for the suite you run constantly. If a larger set is genuinely needed — browser tests, integration against real services — separate it and run it on deployment rather than on every change.

**Deterministic.** A test that fails occasionally teaches you to ignore failures, which is the worst outcome available. The usual causes are time, randomness, network calls and ordering between tests, and all four are fixable: fix the clock, seed the randomness, avoid the network, and reset state between tests rather than depending on the order they run in.

**Honest when it fails.** A failure should say what was expected and what happened, in terms that let you find the problem. Generated tests frequently assert on a whole object, so a one-field difference produces an unreadable dump.

And wire it into deployment so that a failing suite stops the release. Tests you have to remember to run are tests you will not run on the afternoon you most needed them — which, on the evidence of every incident in this series, is a Friday.

## Tests as Instructions for the Next Session

There is a second reason tests matter more in a codebase written largely by tools, and it is not about catching regressions.

A test is an executable statement of what the code is supposed to do. An assistant working on your project reads them, and a failing test is feedback it can act on without you in the loop — which changes the quality of what comes back. Given a suite, a model asked to change a calculation will check its work; without one, it will produce something plausible and hand it to you.

This makes the authorisation and money tests doubly valuable. They are the rules you most want enforced, and they are now enforced against whatever writes the next version of that code, including sessions you have forgotten about.

Two practices amplify it. Name tests after the rule rather than the function — "a member who joins in July pays seven twelfths of the annual contribution" tells a reader and a model what is intended, where "test calculateFee case 3" tells neither. And keep the tests close to the rules they encode, so that anyone changing the behaviour meets the expectation immediately.

The broader point, which runs through this series: the artefacts that make an AI-built codebase manageable — the conventions file, the types, the tests — are all documentation the machine can read. That is a different reason for having them than the traditional one, and it is a considerably stronger one.

It also changes the economics of the thirty tests. They are not only insurance against a regression; they are the instructions that make every future session produce better work, which is a return that compounds in a way insurance does not.

That reframing usually settles the argument about whether a small product can afford tests. It can afford thirty of them, they take a day, and they are the cheapest way to make everything the tools produce afterwards more reliable.

## Setting This Up

For an existing product this is typically one to two days: an authorisation test per endpoint asserting refusal across organisations, tests for every money calculation using awkward rather than round numbers, one end-to-end test of the main flow, a test for each bug that has occurred twice, generated tests reviewed for assertions that could actually fail with the decorative ones deleted, mocking limited so that real interactions are exercised where they matter, the suite running in under a minute and wired into your deployment so a failure stops the release, and a habit of writing the failing test first when fixing a bug.

LaunchStudio builds this proportionate suite as part of production readiness, and it is usually the thing that makes deploying stop being nerve-racking. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us which of your tests would catch a real bug](https://launchstudio.eu/en/#contact). It is often fewer than the number suggests.

## Real example

### Four Hundred Tests and a Production Bug

Jeroen Wijnstra built Contributiebeheer in Cursor: membership fee administration for associations and clubs, 63 organisations collecting around €2 million a year in direct debits.

He had asked the assistant to write a test suite and accepted what it produced: 412 tests, 91 percent coverage, all passing, running in four minutes.

A direct debit run then charged 140 members twice. The cause was a calculation that applied a pro-rata discount for mid-year joiners and had been changed to fix an unrelated rounding issue; the change made the discount apply to the full annual amount rather than the remaining months, and for members who had joined recently produced a second charge.

The suite had eleven tests of that function. All eleven passed. They had been generated from the implementation, asserted the values the code produced at the time, and were updated automatically when the code changed — encoding the bug as the expected result.

Three business days: the 412 tests reviewed and 280 deleted as asserting nothing that could fail — renders without crashing, returns a value, mock was called; the remaining 132 examined for assertions derived from implementation rather than from intention, with 40 rewritten against stated business rules taken from the association agreements; an authorisation test per endpoint across 31 endpoints, of which the exercise found three with no check at all; money tests written from the rules rather than the code, covering mid-year joining, leaving, rounding, zero and the maximum contribution, using awkward amounts; an end-to-end test of the collection run; a test written for the double-charge bug before the fix, confirmed failing first; and the suite reduced to 94 tests running in 50 seconds and wired into deployment.

**Result:** the 140 duplicate charges were refunded and the associations informed. Jeroen's assessment is that the 412-test suite had been actively harmful — it had given him enough confidence to deploy a change to the contribution calculation on a Friday without checking it by hand.

> *"Four hundred and twelve tests, ninety-one percent coverage, all green, and they were green because they had been written from the code rather than from what the code was supposed to do."*
> — **Jeroen Wijnstra, Founder, Contributiebeheer (Gouda)**

**Cost & Timeline:** €3,300 (suite review and reduction, assertions rewritten from business rules, authorisation tests across 31 endpoints with three gaps found, money tests from stated rules, end-to-end collection test, regression test for the incident, deployment integration) — completed in 3 business days.

## Frequently Asked Questions

### Are generated tests worth having?

The right ones, yes. Ask of each: what would have to break for this to fail? Tests that pass regardless of whether your product works provide confidence without providing safety.

### Which tests matter most in an AI-built product?

Authorisation — a user from another organisation being refused, per endpoint. It is the failure this kind of codebase produces most, and the test keeps working while the code around it is rewritten.

### Why is high coverage misleading?

Because coverage measures lines executed, not behaviour verified. A suite can touch 90 percent of your code while asserting almost nothing about whether it is correct.

### What is wrong with tests generated from my implementation?

They encode your current behaviour as correct, including your bugs, and then prevent you from noticing when you fix them. Write assertions from the rule, not from the output.

### How many tests does a small product need?

Thirty to fifty covering authorisation, money, the main flow and every bug that has happened twice. It should run in under a minute and you should trust it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are AI-generated tests useful?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The right ones. Ask what would have to break for each to fail — tests that pass regardless of correctness give confidence without safety."
      }
    },
    {
      "@type": "Question",
      "name": "Which tests matter most in an AI-built product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authorisation tests per endpoint, asserting that a user from another organisation is refused."
      }
    },
    {
      "@type": "Question",
      "name": "Why is test coverage misleading?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It measures lines executed rather than behaviour verified — a suite can reach 90 percent while asserting almost nothing."
      }
    },
    {
      "@type": "Question",
      "name": "What is wrong with tests written from the implementation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They encode current behaviour, bugs included, as expected — and then resist the fixes."
      }
    },
    {
      "@type": "Question",
      "name": "How many tests does a small product need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thirty to fifty covering authorisation, money, the main flow and every twice-occurring bug, running in under a minute."
      }
    }
  ]
}
</script>
