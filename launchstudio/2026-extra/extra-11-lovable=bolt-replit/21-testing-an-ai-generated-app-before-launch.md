---
Title: "Testing an AI-Built App When There Are No Tests"
Keywords: Lovable, testing ai generated app, critical path tests, seed realistic data, pre-launch QA founder, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Testing an AI-Built App When There Are No Tests

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Testing an AI-Built App When There Are No Tests",
  "description": "A pragmatic testing plan for a product built with AI tools and no test suite: the five paths that must never break, how to seed realistic data, what to automate first, and what to leave manual.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/testing-an-ai-generated-app-before-launch" }
}
</script>

Ask an AI tool to add tests to your project and it will happily produce forty of them. They will pass. They will also, in most cases, test that a function returns what it was written to return — which is a tautology dressed as assurance, and it is why founders who add tests this way feel no safer afterwards.

Useful testing for a small product is not about coverage. It is about a short list of things that must never break, tested in a way that reflects how they actually break. For an AI-built app with no test suite at all, that list is five items long and takes a day to implement.

## Why Generated Tests Feel Hollow

A test is only meaningful if it could fail for a reason you care about. Generated tests tend to be written from the implementation rather than from the requirement, so they assert that the code does what the code does. Change the behaviour incorrectly and the test changes with it.

They also concentrate on pure functions — formatting a date, calculating a total — because those are easy to test in isolation. Almost nothing in your product breaks there. Your product breaks at the seams: the database, the payment provider, the session, the concurrent request.

So the first decision is to ignore coverage entirely and start from a different question: what would end this business if it silently stopped working?

## The Five Paths Worth Protecting

For nearly every small product, the answer is these.

**Signup and login.** If people cannot get in, nothing else matters. This includes the password reset flow, which is the part that breaks most often and is noticed least.

**The core action.** The one thing your product exists to do: create a booking, publish a listing, generate a report, send an invoice. One test that performs it end to end.

**Payment.** From clicking pay to the customer actually having what they paid for — which, as anyone who has read about webhooks knows, is not the same as the checkout succeeding.

**Data isolation.** A test that logs in as user A and asserts that user B's records are unreachable. This is the single highest-value test in a multi-tenant product and almost nobody writes it.

**Permissions.** A normal user attempting a privileged action and being refused, at the API level rather than through the interface.

Five tests. They will not catch every bug. They will catch every bug that would make you lose customers, which is the point.

## Test at the Right Level

There is a hierarchy, and for a small product the middle is where the value sits.

**Unit tests** check one function in isolation. Cheap, fast, and mostly irrelevant to the five paths above because those span multiple systems.

**Integration tests** check that your code works against a real database and real dependencies. This is where the five paths belong, and where AI-built apps are weakest, because the seams are exactly what generation gets wrong.

**End-to-end tests** drive a real browser through the interface. Valuable for the signup and payment paths, slower to write and more brittle. Two or three is plenty; twenty becomes a maintenance burden that a solo founder abandons within a month.

A reasonable target for a small product: five integration tests covering the paths above, two end-to-end tests for signup and payment, and no unit tests at all unless you have a genuinely tricky calculation.

## Seed Data That Resembles Reality

Most testing failures in AI-built apps come from testing with data that is too polite.

Your test database should contain at least two organisations, several users with different roles, records that belong to each, a user with no records at all, and at least one of each awkward case your production data will contain: a very long name, an apostrophe, an emoji, a zero quantity, a date from years ago, a deleted-but-referenced record.

Write a seed script that creates this state from scratch. It takes an hour and it turns testing from something you dread into something you run. Without it, every test run starts with manually clicking through your app to create the situation you want to test, which is why people stop.

## What to Automate and What to Keep Manual

**Automate** the five paths, because they must be checked on every change and humans forget.

**Keep manual** anything visual, anything involving a real payment provider in live mode, and anything you do once before launch. A written checklist that you actually follow beats an automated test suite you abandoned.

That checklist deserves to exist in its own right. Ten items, run before each release: the five paths by hand on a phone, a real payment refunded, a password reset from a real inbox, an upload of a large file, a page loaded as a logged-out visitor, and the error tracker checked afterwards for anything new.

## Running Tests Where It Matters

Tests that only run on your laptop get skipped exactly when you are in a hurry, which is exactly when you break things. Two arrangements fix this without ceremony.

**Run them on every push,** through your hosting platform's pipeline or a hosted service. The result is a red mark on a change that breaks a critical path, before it reaches customers.

**Run them against a staging environment** that mirrors production configuration, including a real test-mode payment provider and a database with the same schema. An app tested only against a local setup with different settings is tested against a different app.

## The Test That Pays for Itself Immediately

If you write one test today, write the data isolation one: authenticate as one user, attempt to read another user's record by its identifier, and assert that it fails.

It is perhaps fifteen lines. It protects against the single most common serious flaw in AI-generated applications. And because it runs on every change, it prevents the specific regression where someone loosens a policy to fix an unrelated bug and quietly opens the door again — which is how these flaws return after being fixed once.

## When Someone Else Should Build This

Setting up a test harness against a real database, with seeding, in a pipeline, is a few days of work for someone who has done it before and a frustrating fortnight for someone who has not. It is also the kind of foundation that pays back continuously rather than once.

LaunchStudio builds it as part of making an AI-built product production-ready: seed data that reflects reality, integration tests over the paths that matter, browser tests for signup and payment, a staging environment matching production configuration, and the whole thing running automatically on every change — alongside the access policies and monitoring that the tests are there to protect.

The interface you built in Lovable, Bolt or Cursor is untouched, and the tests are left readable so you can extend them yourself or ask your AI tool to. That is part of the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's engineers, whose eleven years of production work for clients including Vodafone, TNO and CFLW involved rather a lot of exactly this.

If you are about to launch something with no tests at all, [describe your project](https://launchstudio.eu/en/#contact) and we will tell you which five matter most for your product within one business day.

## Who Does the Testing When It Is Only You

Solo founders test their own product, which is the least reliable arrangement possible, because you use the app the way you built it. Three cheap substitutes for a second person.

**Recruit two real users as a launch group.** Not for feedback on the idea — for use. People who did not build the product find the broken path in twenty minutes, because they do things in the order that makes sense to them rather than the order you designed.

**Watch someone use it without helping.** Sit behind a friend, give them a goal, and say nothing for ten minutes. This is uncomfortable and it is the highest-information ten minutes available to a small product.

**Test on a device you do not own.** Borrow a phone. Your own device has your session, your cached assets and your autofill, all of which hide problems a new visitor will meet immediately.

Then write down what you find rather than fixing as you go. A list produced in one sitting shows patterns — three findings in the signup flow, two in payments — and patterns point at causes, while fixing one item at a time points at symptoms.

## What Not to Test

Restraint matters as much as coverage, because a suite you abandon is worth less than three tests you keep running.

**Do not test the framework.** That a form submits or a route renders is the library's responsibility, not yours.

**Do not test generated formatting helpers.** A function that turns a date into a string will not surprise you, and a test asserting it does what it does catches nothing.

**Do not write tests that mirror the implementation.** If changing the code always requires changing the test in the same shape, the test is a copy rather than a check.

**Do not chase a coverage percentage.** It rewards testing the easy half of your product and says nothing about whether the risky half works.

**Do not automate anything visual.** Layout tests are brittle, and a human glance at two screen sizes before release is faster and more reliable for a small product.

The test to keep is the one you would be alarmed to see fail. If a test failing would make you shrug, delete it — it is costing maintenance and buying nothing.

## Real example

### A Booking Platform That Broke Its Own Payments Twice

Jelle Vroomen built Sportlokaal in Lovable: a platform for booking community sports halls across Zaanstad and Purmerend. It had forty-eight venue partners and had twice shipped a change that broke the payment flow — once for six hours, once for a full weekend, both discovered by venue managers rather than by Jelle.

There were no tests. Every release was verified by clicking through the app manually, and both failures happened on evenings when that check had been abbreviated.

Four business days of work produced something deliberately small: a seed script creating two venues, four users across three roles and a set of awkward records; five integration tests covering signup, booking creation, payment completion through to entitlement, cross-venue data isolation and a permission refusal; two browser tests for signup and checkout; a staging environment mirroring production with test-mode payments; and the suite running on every push with a notification on failure.

The isolation test failed on its first run, revealing that a venue manager could read bookings from a venue they did not manage — a flaw that had existed since launch and that nobody had found by clicking.

**Result:** eleven months and roughly ninety releases later, no payment outage. The suite has failed on four occasions, each time catching a regression before it reached a venue.

> *"Two outages cost me more goodwill than the tests cost money. The one that actually scared me was the bug the tests found on day one, which had been live for eight months."*
> — **Jelle Vroomen, Founder, Sportlokaal (Zaanstad)**

**Cost & Timeline:** €2,450 (seed data, integration and browser tests, staging environment, pipeline) — completed in 4 business days.

## Frequently Asked Questions

### Can I just ask my AI tool to write tests for me?

You can, and you will usually get tests written from the implementation rather than from the requirement, concentrated on pure functions. Ask instead for specific scenarios — "log in as user A and assert user B's record is unreachable" — which produces tests that can actually fail for a reason you care about.

### How many tests does a small product need?

Five to eight meaningful ones covering signup, the core action, payment, data isolation and permissions. Coverage percentages are the wrong target at this stage; protecting the paths that would lose you customers is the right one.

### What is the difference between integration and end-to-end tests?

Integration tests exercise your code against a real database and real dependencies without a browser. End-to-end tests drive an actual browser through your interface. Integration tests give most of the value for the cost; keep end-to-end tests to signup and payment.

### Do I need a staging environment to test properly?

For anything involving payments, authentication providers or webhooks, yes. Those behave differently against real services, and an app verified only on a local setup with different configuration has been verified as a different app.

### Which single test should I write first?

The data isolation test: authenticate as one user and assert that another user's records cannot be read. It is fifteen lines, it guards the most common serious flaw in AI-built apps, and it prevents the flaw returning when someone loosens a policy later.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just ask my AI tool to write tests for me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can, but you usually get tests written from the implementation and concentrated on pure functions. Ask for specific scenarios instead, such as asserting that one user cannot read another's record."
      }
    },
    {
      "@type": "Question",
      "name": "How many tests does a small product need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Five to eight meaningful ones covering signup, the core action, payment, data isolation and permissions. Coverage percentages are the wrong target at this stage."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between integration and end-to-end tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Integration tests exercise code against a real database without a browser; end-to-end tests drive the interface. Integration gives most value for the cost; keep end-to-end to signup and payment."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a staging environment to test properly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For payments, authentication providers and webhooks, yes, because those behave differently against real services than against a local setup."
      }
    },
    {
      "@type": "Question",
      "name": "Which single test should I write first?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The data isolation test — authenticate as one user and assert another user's records cannot be read. It guards the most common serious flaw in AI-built apps."
      }
    }
  ]
}
</script>
