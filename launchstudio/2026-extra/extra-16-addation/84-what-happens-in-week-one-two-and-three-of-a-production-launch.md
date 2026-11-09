---
Title: "What Happens in Week One, Two and Three of a Production Launch"
Keywords: production launch timeline, what to expect app launch project, launchstudio process weeks, production readiness project plan, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What Happens in Week One, Two and Three of a Production Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Happens in Week One, Two and Three of a Production Launch",
  "description": "A week-by-week description of a LaunchStudio production launch for an app built with Lovable, Bolt, v0, Cursor or Claude Code: what happens before the start, access and review in week one, fixes and setup in week two, testing, release and handover in week three, what the founder does each week, how updates and decisions work and how shorter Launch Ready projects compress the same steps.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-18",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-happens-in-week-one-two-and-three-of-a-production-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Production checklist", "url": "https://supabase.com/docs/guides/deployment/going-into-prod" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Release Engineering", "url": "https://sre.google/sre-book/release-engineering/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" },
    { "@type": "CreativeWork", "name": "Agile Alliance: Definition of Done", "url": "https://www.agilealliance.org/glossary/definition-of-done/" }
  ]
}
</script>

Founders who have never worked with a development partner often wonder what the project will actually feel like. Will they be asked technical questions they cannot answer? Will the app be offline? How much of their time will it take? When will they see results? Uncertainty about the process is one of the reasons founders delay production work they know they need.

This page describes a typical three-week LaunchStudio project, the length of many Launch & Grow projects and the longer Launch Ready ones. Shorter Launch Ready projects of three to five business days follow the same steps in compressed form. Every project is different, but the rhythm is consistent, and knowing it in advance makes the experience calmer.

## Key Takeaways

- **Your app stays live throughout;** work happens on staging until release.
- **Week one is access and review,** ending with a prioritised list of findings.
- **Week two is fixes and setup,** with short updates and occasional decisions for you.
- **Week three is testing, release and handover,** followed by post-launch support.
- **Your time commitment is modest:** a few short calls, some decisions and a final check.

## Before the Start

Before week one, three things happen. First, an intro call of about 15 minutes, in which we learn about your app, users, plans and deadline. Second, a short look at the project with read access, so the quote is based on reality. Third, a written fixed quote listing scope, assumptions, exclusions, timeline and price, which you approve. If personal data is involved, we sign a processing agreement. We agree a start date, and you receive a short list of accounts to invite us to.

## Week One: Access and Review

**Days 1 and 2: access and ownership.** You invite our team to your accounts with individual roles. We create the account inventory and check ownership. If anything sits in someone else's name, such as a database in a freelancer's account or a domain registered by a former partner, we start moving it into your company's ownership, because some transfers take days. We also set up a staging environment if none exists, so we never experiment on your live app.

**Days 2 to 4: review.** We review the areas in scope: database policies tested with accounts in different roles, secrets, authentication, storage, payments, emails, performance, deployment, backups and monitoring, plus anything specific to your sector. Findings are recorded with severity and evidence. If we find something urgent, such as an exposed service key or customer data readable by anyone, we tell you the same day and usually fix it immediately.

**Day 5: findings review call.** In a call of about 30 to 45 minutes, we walk you through the findings in plain language, confirm priorities and ask the business questions only you can answer, such as "should a team member see invoices?" or "what should happen when a renewal fails?". If something outside the original scope appears, we explain options and costs; nothing extra is done without your approval.

**Your involvement in week one:** inviting us to accounts, a few quick questions by message and the findings call.

## Week Two: Fixes and Setup

**Fixes in priority order.** The most serious issues come first: data access, secrets, payments. Then the production setup: environments, pipeline, migrations, email authentication, backups with a restore test and monitoring. Then performance, clean-up and remaining items. All changes arrive as pull requests in your repository and are deployed to staging.

**Tests.** As we fix, we add automated tests for the rules that matter, such as "a user from company A cannot see company B's invoices" or "a payment webhook processed twice creates one order". These tests stay in your repository after the project.

**Short updates.** You receive a written update every one or two days: what was done, what is next and whether we need anything from you. Updates are short and in plain language, with links to staging if you want to look.

**Decisions.** Occasionally a fix involves a choice that affects users, such as how long applicants' data is kept, what customers see when a payment fails or whether existing users must log in again after a security change. We explain the options and recommend one; you decide.

**Your involvement in week two:** reading updates, answering occasional questions and, if you like, trying staging.

## Week Three: Testing, Release and Handover

**Days 1 and 2: verification.** We repeat the original tests against the fixed version, run the automated tests, check key journeys end to end on staging and, where relevant, run load or performance tests. We complete the launch readiness checklist with evidence for each item.

**Day 2 or 3: your check on staging.** You spend about an hour going through the main journeys of your app on staging: sign up, log in, the core actions, payment if relevant, emails. You confirm that everything works and looks as expected. Anything that does not match the scope is fixed.

**Day 3 or 4: release.** We release to production on a working day, early enough to have the rest of the day for monitoring. If a migration of data or users is involved, we agree a quiet window. After release, we run through key journeys in production with you and confirm that monitoring and alerts work. A rollback is ready if needed.

**Day 4 or 5: handover.** In a handover call of about an hour, we walk through the written summary, the account inventory, the procedures for releases, rollback and restore, and the project instructions for your AI tool. Access we no longer need is removed, or reduced to what ongoing care requires.

**Your involvement in week three:** the staging check, being available on release day and the handover call.

## After Week Three

Launch Ready projects include 48 hours of post-launch support after release, during which we watch monitoring closely and fix issues related to the work. Launch & Grow continues with ongoing care at €49 per month: monitoring, updates, backup checks, platform watch, a monthly health note and small fixes. Either way, issues caused by our work remain our responsibility after the support window.

## How Shorter Projects Compress the Same Steps

A small Launch Ready project of three to five business days follows the same sequence in less time. Access and review happen on day one, with findings shared by the end of the day or the next morning. Fixes and setup take one to three days. Testing, your staging check, release and handover happen in the final day or two. The findings call and handover call may be combined or shortened, but the steps remain.

## What Can Change the Timeline

- **Ownership transfers** that depend on third parties, such as a domain registrar or a former freelancer
- **External approvals,** such as payment partner reviews or app store submissions
- **Decisions** that take longer, for example legal input on data retention
- **Unexpected findings** that you choose to add to the scope
- **Your launch date,** if we plan backwards from a fixed deadline

We flag these early and adjust the plan with you. If a fixed deadline is at risk, we discuss which items to prioritise so the most important risks are resolved before launch.

## Your App During the Project

Your production app keeps running throughout. We work on staging and release changes in a planned moment. If you continue building with your AI tool during the project, we agree which areas are being changed, so work does not collide. Many founders simply pause larger changes for two or three weeks and focus on sales, customers or preparing their launch communication.

## Communication Channels

We agree one channel at the start, such as a shared chat or email thread, for updates and questions, with a named contact on our side. Calls are scheduled in Dutch business hours from Amsterdam; engineering in Ho Chi Minh City starts earlier in the day, which often means progress is visible when you start your morning. Urgent matters are flagged clearly so they never get lost among routine updates.

## What You Have at the End

At the end of week three, you have an app that is secure, owned by you, deployed properly, monitored and documented; a test suite that protects the most important rules; procedures you can follow without us; instructions that keep your AI tool consistent with the work; and a completed launch checklist that shows what was checked and how.

## Preparing for a Smooth Start

You can make the first week faster by preparing a few things before the start date: a list of every tool and service the app uses, login details for accounts you own so you can invite us quickly, a short description of user types and what each may see, any customer questions or requirements you have received and a note of problems you have noticed. Founders who prepare this usually see their findings call a day or two earlier, because less time is spent tracking down accounts.

## When Things Do Not Go to Plan

Occasionally a project hits an obstacle: a former supplier is slow to transfer an account, a payment partner review takes longer than expected or a decision depends on a lawyer who is on holiday. We tell you as soon as we see it, propose options, such as releasing in two phases or working around the dependency temporarily, and agree a revised plan with you. The scope and price remain as agreed; only the timeline moves, and only with your agreement.

## Price

| Package | Typical duration | Price |
| --- | --- | --- |
| Launch Ready | 3-10 business days | €800-€3,500 fixed, including 48 hours of post-launch support |
| Launch & Grow | 2-4 weeks | €2,500-€7,500 fixed, plus €49 per month for ongoing care |

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, running structured projects for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We make the process predictable, so you can focus on your customers while your app gets ready for them.

## Real example

### An AI-Native Founder in Action: Three Weeks Before the Trade Fair

Rob Jacobs runs a SaaS for event equipment rental companies from Eindhoven, built with Cursor and Supabase, and planned to present it at a national trade fair. Three weeks before the fair, he started a Launch & Grow project with LaunchStudio, quoted at €5,100.

In week one, the inventory revealed that the domain was registered by his former business partner, so the transfer started on day one. The review found loose policies between rental companies, Stripe subscriptions updated on the success page and no staging. The service key in a client-side function was rotated the same afternoon. In the findings call, Rob decided that companies' staff should see equipment and bookings but not invoices unless they had a finance role.

In week two, policies were rewritten with tests, a staging environment and pipeline were set up, Stripe moved to verified webhooks with a reconciliation of past subscriptions and email authentication was configured. Rob received updates every other day and answered two questions about failed payment rules.

In week three, Rob spent an hour checking staging, the release happened on a Tuesday morning and the handover call took place on Thursday. The domain transfer completed on Wednesday, two days before the fair.

**Result:** Rob demonstrated the live product at the fair and signed up nine rental companies during and after the event, without a technical issue during onboarding.

> *"I expected three weeks of chaos. It was three weeks of short messages, two calls and one hour clicking through staging. Then I went to the fair with an app I trusted."*
> - **Rob Jacobs, Founder, Verhuurplanner (Eindhoven)**

**Cost & Timeline:** €5,100 (Launch & Grow package: ownership transfer, policies with tests, staging and pipeline, Stripe webhooks and reconciliation, email authentication, monitoring and handover, plus €49 per month) - completed in 15 business days.

## Frequently Asked Questions

### How long does a production launch with LaunchStudio take?

Launch Ready projects usually take three to ten business days, and Launch & Grow projects two to four weeks. The exact timeline is in your fixed quote and depends on scope, ownership transfers and any external approvals.

### Will my app be offline during the project?

No. We work on a staging environment and release changes at a planned moment on a working day. Data or user migrations may need a short, agreed window, usually outside busy hours.

### How much of my time does the project take?

Typically a few hours spread over the project: inviting us to accounts, a findings call, answering occasional questions, an hour checking staging, being available on release day and a handover call.

### How does Manifera's experience make the process predictable?

Manifera has run structured software projects for 11+ years across 160+ projects with 120+ engineers, for clients such as Vodafone and TNO. LaunchStudio applies that experience in a repeatable process tailored to AI-built apps.

### Does the project include SEO and AI visibility basics?

Yes. The production setup covers custom domain, HTTPS, redirects, page metadata, exclusion of staging from indexing and fast public pages, which help search engines and AI answer engines read your site properly from launch.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a production launch with LaunchStudio take?",
      "acceptedAnswer": { "@type": "Answer", "text": "Launch Ready 3-10 business days; Launch & Grow 2-4 weeks." }
    },
    {
      "@type": "Question",
      "name": "Will my app be offline during the project?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; work happens on staging with a planned release." }
    },
    {
      "@type": "Question",
      "name": "How much of my time does the project take?",
      "acceptedAnswer": { "@type": "Answer", "text": "A few hours spread over calls, questions and a staging check." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience make the process predictable?",
      "acceptedAnswer": { "@type": "Answer", "text": "It applies a repeatable process from 11+ years and 160+ projects." }
    },
    {
      "@type": "Question",
      "name": "Does the project include SEO and AI visibility basics?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, domain, HTTPS, redirects, metadata, indexing and speed." }
    }
  ]
}
</script>
