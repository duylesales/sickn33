---
Title: "How Do I Test My AI-Built App Before Launch?"
Keywords: test ai-built app, testing lovable app, pre-launch testing, playwright supabase testing, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Test My AI-Built App Before Launch?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Test My AI-Built App Before Launch?",
  "description": "AI-built apps are usually tested only by clicking through them. This guide gives a practical pre-launch testing plan: critical-path scenarios, permission tests with multiple users, payment tests, automated end-to-end tests and a launch rehearsal.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-05",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-test-my-ai-built-app-before-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "Perry et al., Do Users Write More Insecure Code with AI Assistants?", "url": "https://arxiv.org/abs/2211.03622" },
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "Playwright documentation", "url": "https://playwright.dev/docs/intro" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "web.dev: Web Vitals", "url": "https://web.dev/articles/vitals" }
  ]
}
</script>

**Short answer:** test the few things that would hurt most if they broke, in a staging environment, with more than one user. Write down your critical paths (sign-up, login, the core action, payment, data visibility), test each with at least two accounts and different roles, run payments in test mode through success, failure and cancellation, automate the most important paths with end-to-end tests, and do a launch rehearsal on the production setup before you announce anything.

## Key Takeaways

- **Test what would hurt most if it broke:** sign-up and login, the core action, payments, data visibility, password reset and deletion.
- **Always test with more than one user and role;** access control failures only appear when a second account exists.
- **AI-assisted code needs more testing, not less.** Stanford researchers found AI-assisted developers were more confident in less secure code, and Google's DORA research ties automated testing to stable delivery.
- **Automate the top three or four paths** with end-to-end tests such as Playwright, running on every deployment.
- **Rehearse the launch on production:** a real small payment, real emails, alerts, rollback and a backup restore.

## Why Clicking Through Is Not Enough

When you test your own app, you use one account, the happy path and a fast connection. Real users bring many accounts, wrong inputs, slow phones and bad timing. AI-generated code is especially prone to working perfectly on the path you prompted for and breaking on paths you did not.

## Step 1: List Your Critical Paths

Usually five to ten. For a booking SaaS, for example:

1. Sign up, confirm email, log in
2. Create a booking
3. Pay for a booking
4. Cancel or change a booking
5. Staff view of bookings
6. Password reset
7. Account deletion

## Step 2: Test Permissions With Real Accounts

Create users in different roles and organisations. For every critical path, check what each user can see and do. Try direct URLs and changed IDs. This is where AI-built apps fail most often; our [Lovable security self-test](https://launchstudio.eu/en/blog/is-my-lovable-app-secure) walks through the method.

## Step 3: Test Payments Thoroughly

| Scenario | Expected result |
| --- | --- |
| Successful payment | Access granted via webhook |
| Customer closes browser after paying | Access still granted |
| Payment cancelled or failed | No access, clear message, retry possible |
| Double click on pay | One charge |
| Renewal fails (subscriptions) | Grace period and email |

## Step 4: Test Bad Input and Bad Conditions

- Very long text, emojis, special characters in names
- Empty required fields, wrong formats
- Slow network (browser developer tools can simulate it)
- Mobile browsers on iOS and Android
- Two people editing the same record

## Step 5: Automate the Top Paths

End-to-end testing tools such as Playwright can log in as test users and click through critical paths automatically on every deployment. Start with three tests: sign-up and login, the core action, and a permission check that one user cannot see another's data. AI tools can help write these tests, but review what they assert.

## Step 6: Launch Rehearsal

On the production setup, before announcing:

- Real payment of a small amount, then refund
- Real email delivered to Gmail and Outlook
- Monitoring alerts tested
- Rollback tested
- Backup restore tested

## Why AI-Built Apps Need Deliberate Testing

When code is generated quickly, it is easy to assume it was checked. In practice, the AI optimised for the scenario you described, not for the ones you did not. The Stanford study by Perry and colleagues found that participants using AI assistants produced less secure code and were more likely to believe it was secure. Google's DORA research has long associated automated testing and continuous delivery with better outcomes, and its 2024 report linked higher AI adoption to lower delivery stability when such practices were missing. Testing is how you convert generated confidence into earned confidence.

## A Risk-Based Testing Plan

You cannot test everything, so test by risk. For each feature, ask two questions: how likely is it to break, and how bad would it be? Features with money, personal data or access control are always high impact. Features recently changed by prompts are always more likely to break. Combine the two to decide where to spend testing time:

| Impact / likelihood | Low likelihood | High likelihood |
| --- | --- | --- |
| High impact | Test before every major release | Test before every release, automate |
| Low impact | Spot-check occasionally | Test when changed |

## Writing Good Test Scenarios

A good scenario is concrete: who the user is, what they do, what should happen. For example: "A member of Organisation A opens an invoice URL belonging to Organisation B and sees an error, not the invoice." Write scenarios in plain language first; they are useful for manual testing, for briefing developers and for generating automated tests. Twenty well-chosen scenarios cover most of what matters for a typical founder app.

## Testing Access Control Properly

Access control deserves its own session. Create two organisations with two users each - an admin and a member - and try:

- Listing records from the other organisation through the interface and the API
- Opening another organisation's record by changing an ID in the URL
- Updating or deleting another organisation's record
- A member calling admin-only actions directly
- Downloading another organisation's files by guessing or reusing links

Every attempt should fail on the server. If any succeeds, fix it before launch; OWASP ranks broken access control as the top web application risk.

## End-to-End Tests With Playwright

Playwright drives a real browser through your app and checks results. For a founder app, start with three tests: sign-up and login, the core action for a paying customer and a cross-organisation access check. Run them against staging on every deployment through your CI pipeline. AI tools can write first drafts of these tests; review that the assertions check the correct behaviour, not simply what the app currently does.

## Testing Payments End to End

Use your payment provider's test mode to cover successful payment, cancellation, failure, double click and closing the browser before redirect. For subscriptions, use tools such as Stripe's test clocks to simulate renewals, failed renewals and cancellations without waiting weeks. Check that your database reflects each outcome correctly and that customers receive the right emails.

## Performance and Mobile Testing

Test key screens on a mid-range phone over a throttled connection. Seed staging with realistic data volumes, because a list that loads instantly with ten rows may take seconds with ten thousand. Google's Web Vitals give useful targets for loading and responsiveness on public pages.

## Accessibility Basics

Check that forms have labels, buttons are reachable by keyboard, contrast is sufficient and images have alternative text. Beyond being good practice, accessibility requirements apply to many consumer-facing digital services in the EU under the European Accessibility Act, with exemptions for microenterprises.

## A Two-Day Testing Sprint Before Launch

Day one: write your twenty scenarios, create test users and organisations in staging, run all access control and payment scenarios manually and log every issue. Day two: fix launch blockers, re-test them, write the first three Playwright tests and add them to CI, then test key flows on two phones and two browsers. Two focused days catch most issues that would otherwise appear in your first week with customers.

## Involving Early Users

Before a public launch, invite a few trusted users to a beta on staging or production with clear expectations. Real users find problems that builders never would, because they do not know which buttons are supposed to be pressed. Give them an easy way to report issues and respond quickly; early users who see their feedback acted upon often become your strongest advocates.

## Keeping Tests Alive

Tests that nobody maintains become noise. When a feature changes intentionally, update its tests in the same change. When a test fails, treat it as information: either the app broke or the test is outdated, and both deserve attention. A small set of trusted tests is worth far more than a large set nobody believes.

## What to Do With the Results

Sort every issue into three groups. Launch blockers: anything involving data access, payments, login or data loss - fix before launch. First-week fixes: broken layouts on some devices, confusing messages, slow screens - fix right after launch. Backlog: polish and nice-to-haves. Write the list down and share it with whoever helps you build; a prioritised list is far more useful than a long, unsorted one.

## Testing After Launch

Testing does not stop at launch. Add a test for every bug customers report, so it cannot return unnoticed. Re-run the access control scenarios after any feature that touches data or roles. And review your automated tests whenever a test fails for a reason other than a real bug; flaky tests erode trust in the whole suite.

## Related Reading

Testing works best with staging and CI. Our guides on setting up a staging environment and automatic deployments for Lovable or Bolt apps show how to run these tests on every change.

## Testing Checklist

- Twenty written scenarios covering critical paths
- Access control tested with two organisations and two roles each
- Payment outcomes tested in test mode, including double click and closed browser
- Key flows tested on two phones and two browsers
- Three automated end-to-end tests running on every deployment
- Launch rehearsal on production with a real small payment and refund

## The Payoff

A few days of deliberate testing protects the first impression your product makes, and first impressions are hard to repair.

## Related Reading

Our 25-point vibe code audit checklist complements this plan with the security and operations checks to run alongside functional testing.

## A Bug List That Actually Helps

For each issue: what you did, what happened, what you expected, which user and device. Fix launch blockers (data, payments, login) before launch; schedule the rest.

## Getting It Done

LaunchStudio tests every app before launch, including permission tests with multiple roles and payment scenarios, and can add automated end-to-end tests to your pipeline. LaunchStudio is powered by Manifera, whose QA practices come from 11+ years and 160+ projects for clients including Vodafone and Xpar Vision; see [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/). [Playwright's documentation](https://playwright.dev/docs/intro) is a good starting point for automated tests.

## Real example

### An AI-Native Founder in Action: The Course Platform Tested by One Person

Marloes Vink, a photography teacher in Haarlem, built Lichtlessen in Lovable: an online course platform with video lessons, assignments and teacher feedback. She tested it for weeks, always logged in as herself, the admin. Two days before launch, a friend tried it as a student.

In one hour, the friend found that students could open other students' assignment submissions by changing a number in the URL, the "mark as complete" button worked on lessons the student had not bought, iDEAL payments that were cancelled still unlocked the course, and the video player failed in Safari on iPhone.

Marloes postponed by a week. LaunchStudio fixed RLS on submissions and lesson progress, moved course access checks to the server, connected access to verified payment webhooks, fixed video playback with a compatible streaming setup, and added three Playwright tests (sign-up and purchase, student permissions, teacher feedback) running on every deployment.

**Result:** The launch went ahead a week later with 120 students in the first cohort. The automated tests caught two regressions in the following months before students saw them.

> *"I tested my app for a month. I just never tested it as anyone other than the person who built it."*
> - **Marloes Vink, Founder, Lichtlessen (Haarlem)**

**Cost & Timeline:** €2,400 (Launch Ready package: RLS fixes, server-side access, payment webhooks, Safari video fix and automated tests) - completed in 6 business days.

## Frequently Asked Questions

### What should I test first in an AI-built app?

Permissions, payments and login. Test that users cannot see or change each other's data, that payments grant access only when successful, and that sign-up, login and password reset work on real devices.

### Do I need automated tests for a small app?

A few, yes. Three to five end-to-end tests covering your critical paths catch regressions when AI tools regenerate code. You do not need full test coverage to benefit.

### Can AI write my tests?

AI tools can draft tests quickly, which is useful. Review what each test checks, because generated tests sometimes assert the current behaviour rather than the correct behaviour, including bugs.

### How does Manifera approach testing for fixed-price launches?

By focusing on risk: critical paths, permissions and payments are always tested with multiple roles before launch. Manifera's 11+ years of QA practice prioritise tests that prevent incidents over tests that only increase coverage numbers.

### Does testing affect SEO or AI visibility?

Indirectly. Testing public pages on mobile and slow connections catches rendering and performance problems that would otherwise hurt page experience and make content harder to crawl and cite.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should I test first in an AI-built app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Permissions, payments and login, on real devices and with multiple users." }
    },
    {
      "@type": "Question",
      "name": "Do I need automated tests for a small app?",
      "acceptedAnswer": { "@type": "Answer", "text": "A few end-to-end tests on critical paths catch regressions from AI-regenerated code." }
    },
    {
      "@type": "Question",
      "name": "Can AI write my tests?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can draft them; review assertions because generated tests may encode existing bugs." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach testing for fixed-price launches?",
      "acceptedAnswer": { "@type": "Answer", "text": "Risk-focused testing of critical paths, permissions and payments with multiple roles." }
    },
    {
      "@type": "Question",
      "name": "Does testing affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, by catching mobile rendering and performance issues on public pages." }
    }
  ]
}
</script>
