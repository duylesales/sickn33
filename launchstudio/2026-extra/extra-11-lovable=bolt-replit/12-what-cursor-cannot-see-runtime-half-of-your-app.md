---
Title: "Cursor Cannot See the Runtime Half of Your App"
Keywords: Cursor, ai code review limits, runtime errors production, observability small product, ai app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor Cannot See the Runtime Half of Your App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor Cannot See the Runtime Half of Your App",
  "description": "An AI editor reasons about code it can read. Production failures come from configuration, concurrency, data state and third-party behaviour it cannot. What that means practically, and the minimum observability a small product needs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-cursor-cannot-see-runtime-half-of-your-app" }
}
</script>

Your editor has read every file in your project. It can explain any function back to you, refactor across the codebase, and answer questions about how the pieces connect. So it is reasonable to assume that if something were seriously wrong, it would have said so.

It would not, and the reason is not a limitation of the model. It is that roughly half of what your application *is* does not exist in your repository. Configuration lives in a hosting dashboard. Access rules live in a database. State lives in rows created by users you have never met. Behaviour depends on a payment provider's response at 03:00 on a Sunday. None of that is text Cursor can read, and almost all production incidents come from exactly there.

## The Two Halves, Named Clearly

**The static half** is your source code: logic, structure, dependencies, types. AI editors are genuinely excellent here — spotting inconsistencies, suggesting refactors, catching a null case you missed, explaining unfamiliar code faster than you could read it.

**The runtime half** is everything that only exists when the app is running against real infrastructure and real people. Environment variables and their values. Database access policies. Network boundaries and which service can reach which. Data that has accumulated shapes nobody designed. Concurrency. Third-party services with their own moods.

An AI editor reasons about the first half with a great deal of skill and has, structurally, no visibility into the second.

## Four Failures That Only Exist at Runtime

**The correct code with the wrong configuration.** Your payment integration is implemented properly and points at a test endpoint, or your database client is perfect and connects to a project in the wrong region. The code reviews cleanly because the code is clean. The value it reads is somewhere else entirely.

**The race condition.** Two people book the last slot within the same second. Read your booking function and the logic is obviously correct: check availability, then write. At runtime, both checks happen before either write, and you have sold the same thing twice. Nothing in the file is wrong; the wrongness lives in the interleaving.

**The data-shaped bug.** Your report works for every record you created while testing. Then a user submits a name with an apostrophe, a quantity of zero, or a date from 1970, and a query returns something absurd. The code handles the data it was written against, which is the data you imagined.

**The third-party surprise.** A provider returns a status you never saw during development, times out mid-request, or changes a response shape in a minor version. Your integration is correct against the documented behaviour and wrong against the actual one.

No amount of reading the repository surfaces any of these, because in all four cases the repository is not where the problem is.

## Why Fluency Feels Like Correctness

There is a psychological dimension worth naming, because it affects experienced developers as much as newcomers.

Code produced or reviewed by a capable assistant reads well. It is idiomatic, consistently formatted, plausibly structured, and it typically runs on the first attempt. That combination produces a confidence signal your brain has spent years learning to trust — historically, code that looked this coherent had usually been thought about carefully.

That correlation no longer holds. Fluency is now cheap and correctness is not, and the gap between them is where production incidents live. The practical implication is not to distrust the tool; it is to stop treating "it looks right and it ran" as evidence about anything except that it looks right and it ran.

## What Replaces Reading the Code

Once you accept that half the system is invisible to static inspection, the question becomes how you observe the other half. For a small product, four things cover most of it.

**Error tracking.** Every unhandled exception, with a stack trace, the user context and the request that caused it, sent somewhere you will actually look. This single item turns "a customer says it broke" into a diagnosable event.

**Structured logs you can search.** Not print statements scattered through the code — a consistent record of what happened, with identifiers that let you follow one user's request end to end.

**Uptime monitoring.** An external check that your app responds, from outside your own infrastructure, alerting somewhere that reaches you.

**Basic metrics.** Response times, error rates, and database connection usage. You are not building a dashboard practice; you are answering "is this normal for us" when something feels slow.

For a product with a few hundred users this is an afternoon of configuration and a modest monthly cost, and it converts your relationship with production from hoping to knowing.

## Testing the Half Cursor Cannot Read

Static analysis and unit tests check the readable half. The runtime half needs different exercises, and they are largely manual for a small product.

**Run the flow against real infrastructure with real credentials,** including a small live payment that you then refund. Test mode does not exercise the same code paths at the provider.

**Deliberately create concurrency.** Two browsers, same record, same second. Book the last slot twice. Submit the form twice by double-clicking.

**Poison your own data.** Apostrophes, emoji, very long strings, zero, negative numbers, a date far in the past. Your app will meet all of these within a month of launch.

**Break a dependency on purpose.** Point a service at a wrong address and see what your user sees. If the answer is a blank screen or a spinning wheel forever, that is the bug to fix.

**Test as a hostile authenticated user.** Edit an identifier in a request and try to read someone else's record. This is the most common real-world failure in AI-built apps, and no editor will find it for you.

## Where the Editor Genuinely Helps With Runtime Problems

This is not an argument for working without the tool. Once you have observability, an AI editor becomes considerably more useful, because you can bring it evidence: a stack trace, a slow query, a log sequence showing what happened before the failure. Given actual runtime data, it is very good at explaining what the code was doing and proposing a fix.

The sequence matters. Observe first, then ask. Asking the editor to find a runtime problem from the source alone is asking it to guess about a system it cannot see.

## Getting the Invisible Half Under Control

The runtime layer is exactly what LaunchStudio builds underneath an existing prototype: configuration made explicit and verifiable rather than living in someone's dashboard, database access policies written and then tested by attempting to break them, concurrency handled where it matters commercially, third-party integrations given proper failure handling, and error tracking, logging, uptime monitoring and alerting wired up so you find out before your customers do.

The frontend you built in Cursor, Lovable or Bolt is untouched, the codebase stays conventional and AI-readable, and the code remains yours. That work is delivered by Manifera's engineers, whose eleven years of production systems for clients including Vodafone, TNO and CFLW is mostly eleven years of the runtime half.

If you have a product live and no way of knowing when it fails, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact) — or see what [Launch Ready](https://launchstudio.eu/en/#packages) includes before you assemble it yourself.

## Reading an Error Without Panicking

Once error tracking exists, you will start receiving things you have never had to interpret before. A short orientation saves a lot of anxiety.

**Read the bottom of the stack trace first, then the top.** The bottom tells you where the failure surfaced; the top tells you what your own code was doing when it happened. The intervening library frames are usually noise for a first diagnosis.

**Separate frequency from severity.** One error affecting one user once is a curiosity. The same error forty times in an hour is an incident. A single error affecting a payment is worse than a thousand affecting a tooltip. Error trackers group and count for exactly this reason.

**Look at what the user was doing,** not only at the code. Good tracking captures the request, the account and the sequence of actions. Three failures that share a page and a time window usually share a cause.

**Distinguish "expected failure" from "broken".** A declined card is a normal event your app should handle; if it appears as an unhandled exception, the bug is the missing handling rather than the decline.

**Resist fixing the stack trace.** The message describes the symptom at the moment everything fell over, which is frequently several steps after the actual mistake. Find the first thing that was not true, not the last thing that broke.

Founders who get comfortable with this stop treating production as something that happens to them. It is the difference between a product you operate and one you hope about.

## The First Week After Launch

Observability earns its keep in the first seven days, when your app meets behaviour it has never seen. Three habits make that week informative rather than frightening.

**Read the error tracker every morning,** even when nothing is on fire. New errors in the first week are usually small and cheap to fix, and they tell you which assumptions were wrong while the user count is still low enough that fixing them costs nothing.

**Watch the shape of your traffic, not just the volume.** Ten signups from one address in a minute is not a launch; it is a script. Knowing your normal pattern early is what lets you recognise an abnormal one later.

**Keep a written log of what you changed and when.** When something degrades on day five, the first useful question is what shipped on day four. Founders reconstruct this from memory and get it wrong.

None of this takes more than ten minutes a day, and it converts the launch week from a period you survive into the period where your product's real behaviour becomes visible for the first time.

## Real example

### A Ticketing Tool That Sold the Same Seat Twice

Wouter Bleeker built Podiumkaart in Cursor: a ticketing tool for small theatre venues in Haarlem and Leiden. The code was clean, reviewed repeatedly with AI assistance, and covered by a reasonable set of unit tests.

On the first genuinely popular show, the venue sold 214 tickets for 210 seats. The availability check and the write were two separate operations, and under a burst of simultaneous requests several pairs interleaved. Every test passed, because tests run sequentially.

Worse, nobody noticed for two days. There was no error tracking, so the duplicate bookings were discovered when a customer arrived to find someone sitting in her seat. There were no structured logs, so reconstructing what had happened meant reading raw database rows by hand.

Six business days of work: the booking operation rewritten as a single atomic transaction with a database-level constraint so the seat cannot be sold twice regardless of timing, error tracking and structured logging added, uptime monitoring wired to Wouter's phone, and a load test that simulates fifty simultaneous purchases now part of the deploy pipeline.

**Result:** the same venue ran a sold-out run of eleven performances two months later without a single duplicate, and the one incident that did occur — a payment provider timeout — appeared in Wouter's error tracker eleven minutes before the venue called.

> *"My editor had read that function dozens of times. It was correct. It just wasn't correct when two people clicked at once, and there was no way for it to know that."*
> — **Wouter Bleeker, Founder, Podiumkaart (Haarlem)**

**Cost & Timeline:** €2,800 (transaction rewrite, observability setup, load testing in pipeline) — completed in 6 business days.

## Frequently Asked Questions

### Can an AI editor find security problems in my code?

It can find some patterns in code it can read — a missing check, an unsafe query construction. It cannot evaluate your database access policies, your hosting configuration or what an authenticated stranger can reach, because none of that is in the repository.

### If my tests pass, am I covered for runtime issues?

Only partly. Unit tests run sequentially against data you chose, so they do not exercise concurrency, real third-party behaviour, production configuration or accumulated data shapes. Those need deliberate manual exercises and observability.

### What is the minimum monitoring a small product should have?

Error tracking, searchable structured logs, an external uptime check, and basic response and error-rate metrics. For a few hundred users this is an afternoon of setup and a small monthly cost.

### How do I test for race conditions without special tooling?

Manually, first: two browsers, the same record, simultaneous submissions, double-clicked buttons. Anything involving limited stock, seats, slots or balances deserves this treatment before launch, and a proper constraint in the database afterwards.

### Does this mean AI-assisted development is unsafe?

No. It means the confidence signal has changed. Code that reads fluently and runs is no longer evidence of careful thought, so the verification has to come from observing the running system rather than from how the source looks.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can an AI editor find security problems in my code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can find some patterns in readable code, such as a missing check or unsafe query. It cannot evaluate database access policies, hosting configuration or what an authenticated stranger can reach, because none of that is in the repository."
      }
    },
    {
      "@type": "Question",
      "name": "If my tests pass, am I covered for runtime issues?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only partly. Unit tests run sequentially against chosen data, so they miss concurrency, real third-party behaviour, production configuration and accumulated data shapes."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum monitoring a small product should have?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Error tracking, searchable structured logs, an external uptime check and basic response and error-rate metrics — an afternoon of setup for a small product."
      }
    },
    {
      "@type": "Question",
      "name": "How do I test for race conditions without special tooling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manually first: two browsers, the same record, simultaneous submissions and double-clicked buttons. Anything with limited stock, seats or balances also needs a database-level constraint."
      }
    },
    {
      "@type": "Question",
      "name": "Does this mean AI-assisted development is unsafe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it means the confidence signal changed. Fluent, running code is no longer evidence of careful thought, so verification must come from observing the running system."
      }
    }
  ]
}
</script>
