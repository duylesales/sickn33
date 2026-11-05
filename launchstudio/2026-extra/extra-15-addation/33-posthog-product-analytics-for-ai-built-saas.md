---
Title: "PostHog Product Analytics for AI-Built SaaS"
Keywords: posthog lovable app, product analytics saas startup, posthog eu cloud gdpr, activation retention analytics, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# PostHog Product Analytics for AI-Built SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "PostHog Product Analytics for AI-Built SaaS",
  "description": "Product analytics shows what users actually do after signing up: where they activate, which features they use and why they leave. This guide explains how to set up PostHog for an AI-built SaaS, design an event plan, use group analytics for B2B accounts, configure EU hosting and privacy settings, and turn funnels and retention charts into product decisions.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/posthog-product-analytics-for-ai-built-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostHog documentation", "url": "https://posthog.com/docs" },
    { "@type": "CreativeWork", "name": "PostHog: EU hosting", "url": "https://posthog.com/eu" },
    { "@type": "CreativeWork", "name": "PostHog: Group analytics", "url": "https://posthog.com/docs/product-analytics/group-analytics" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Cookies", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/internet-and-smart-devices/cookies" }
  ]
}
</script>

Website analytics tells you how many people visit and sign up. It does not tell you what happens next. Did new users create their first project? Did they invite a colleague? Which feature did the customers who stayed for six months use in their first week? Where do trial users give up?

Those questions are what product analytics answers, and for an AI-built SaaS they matter more than usual. When you can build features in hours with Lovable, Bolt or Cursor, the bottleneck is no longer building; it is knowing what to build. Product analytics replaces guesses with evidence.

PostHog has become a popular choice for startups because it combines product analytics, session replay, feature flags, experiments and surveys in one tool, offers an EU cloud and has a generous free tier. This guide explains how to set it up well in an AI-built product, with attention to event design, B2B accounts and privacy.

## Key Takeaways

- **Product analytics tracks behaviour inside your app,** such as activation, feature usage and retention, rather than just page views.
- **An event plan comes first.** Define a small set of meaningful events tied to your funnel before instrumenting anything.
- **B2B products need group analytics,** so you can analyse companies and workspaces, not only individual users.
- **Use the EU cloud and privacy settings,** and decide deliberately whether you use cookies or cookieless persistence, because that affects consent requirements.
- **Analytics is only useful if it drives decisions.** Review a few key charts weekly and tie product changes to them.

## What Product Analytics Gives You

| Question | Analytics feature |
| --- | --- |
| Where do new users drop out of onboarding? | Funnels |
| Do users come back after their first week? | Retention charts |
| Which features do retained customers use? | Event trends and cohorts |
| What were users doing before they gave up? | Session replay, with privacy masking |
| Does a new onboarding flow work better? | Experiments with feature flags |
| Why did users cancel? | In-app surveys |
| Which companies are most active? | Group analytics |

PostHog provides all of these in one product. Other tools, such as Mixpanel and Amplitude, offer similar analytics, and the principles below apply to them too.

## Start With an Event Plan

The biggest mistake in product analytics is tracking everything and understanding nothing. AI builders make this worse: ask for "analytics" and you may get hundreds of autocaptured clicks with names nobody understands.

Start instead with your funnel and your definition of value:

1. **Acquisition:** the user signs up.
2. **Activation:** the user reaches the first moment of value. For a project tool, perhaps "created a project and added three tasks". For an invoicing tool, "sent the first invoice".
3. **Engagement:** the user performs the core action regularly.
4. **Expansion:** the user invites teammates or upgrades.
5. **Retention:** the user or account is still active after 30, 60 and 90 days.

Then define a handful of events:

| Event | Properties | Why |
| --- | --- | --- |
| `signed_up` | plan, source | Start of the funnel |
| `onboarding_step_completed` | step | Find onboarding drop-off |
| `project_created` | template_used | Core object creation |
| `activation_reached` | days_since_signup | Your activation definition |
| `teammate_invited` | role | Expansion within accounts |
| `plan_upgraded` | from_plan, to_plan | Revenue events |
| `subscription_cancelled` | reason | Churn analysis |

Name events consistently, in past tense, with lowercase and underscores. Document them in a short tracking plan in your repository so AI-assisted changes keep using the same names.

## Defining Activation Properly

Activation is the most important metric for an early SaaS, and the one most often defined badly. "Logged in twice" or "visited the dashboard" are easy to measure but say little about value. A good activation definition has three properties:

- **It reflects real value.** The user has done the thing your product exists for, such as sending an invoice, publishing a schedule or receiving a first booking.
- **It predicts retention.** Users who reach it are much more likely to still be active weeks later than those who do not.
- **It happens early.** Ideally within the first session or first few days, so you can influence it through onboarding.

You rarely get the definition right on the first try. Start with a hypothesis, measure how well it predicts retention after a month or two, and refine it. Comparing the early behaviour of companies that stayed with those that left is usually the fastest way to find the moment that matters.

## Instrumenting an AI-Built App

PostHog offers SDKs for JavaScript and React, plus server-side libraries. A minimal React setup:

```typescript
import posthog from "posthog-js";

posthog.init(import.meta.env.VITE_POSTHOG_KEY, {
  api_host: "https://eu.i.posthog.com",
  person_profiles: "identified_only",
  autocapture: false,
  capture_pageview: true,
  persistence: "memory",
});
```

A few decisions in this configuration matter:

- **EU host.** Sending data to PostHog's EU cloud keeps analytics data in the EU.
- **Autocapture off.** Explicit events are clearer and reduce accidental capture of sensitive content. You can enable autocapture selectively later.
- **Person profiles only for identified users.** Reduces unnecessary profiles for anonymous visitors.
- **Persistence.** Memory persistence avoids cookies and local storage, at the cost of not recognising returning anonymous visitors. Cookie persistence gives better continuity but typically requires consent. Choose deliberately, with advice.

After sign-in, identify the user with an internal ID, not an email address, and associate them with their company:

```typescript
posthog.identify(user.id);
posthog.group("company", account.id, { plan: account.plan });
```

## Track Important Events on the Server

Some events should be sent from your backend rather than the browser:

- **Payments and plan changes,** from your payment webhook handler, so they are recorded even if the user closes the browser
- **Actions completed by background jobs,** such as imports finishing or reports generated
- **Events that must be accurate,** because ad blockers can prevent browser events from being sent

Server-side events are also harder to manipulate and easier to keep consistent with your database.

## Group Analytics for B2B

In B2B SaaS, the customer is usually a company, not an individual. A user may be inactive while their company is very active, or vice versa. Group analytics lets you:

- Count active companies, not just active users
- Build funnels and retention charts per company
- See which companies are at risk of churning
- Compare behaviour between plans or customer segments

Define groups early, usually one per company or workspace, and attach properties such as plan, size and sign-up date.

## Session Replay With Privacy in Mind

Session replay shows a reconstruction of what users saw and did. It is extremely useful for understanding confusing interfaces, and it is also the feature most likely to capture personal data.

- **Mask all text inputs and sensitive content by default,** and unmask only safe elements.
- **Exclude pages with sensitive data** entirely, such as payment, health or document pages.
- **Sample sessions** rather than recording all of them.
- **Set retention** to the minimum useful period.
- **Inform users** in your privacy policy.

## Privacy and Consent

Product analytics processes personal data when it links events to identified users. Consider:

- **Legal basis and transparency:** explain product analytics in your privacy policy.
- **Consent for cookies or local storage:** if you use persistent identifiers on users' devices for analytics, consent rules may apply under the Dutch Telecommunicatiewet. Cookieless configurations reduce this, but get advice for your setup.
- **Data minimisation:** do not send names, emails or content as event properties.
- **Processor agreement:** sign PostHog's data processing agreement and list it in your records of processing.
- **B2B customers' data:** if your analytics captures data about your customers' end users, consider your role and what your processing agreements say.

Our guide on [cookieless analytics for EU SaaS](https://launchstudio.eu/en/blog/cookieless-analytics-for-eu-saas-plausible-vs-ga4) covers website analytics and consent in more detail.

## Feature Flags and Experiments

PostHog's feature flags let you release features to a subset of users or companies, roll them back instantly and run experiments. For AI-built products where new features appear quickly, flags are a safety net:

- Release a new feature to your own team first, then 10% of companies, then everyone.
- Run an experiment comparing two onboarding flows and measure activation.
- Disable a misbehaving feature without a redeploy.

Evaluate flags on the server for anything security-relevant. A flag that hides a button in the frontend does not prevent access to the underlying API.

## Turning Data Into Decisions

A weekly review of a few charts beats an elaborate dashboard nobody opens:

1. **Activation funnel:** from sign-up to activation, by week of sign-up.
2. **Retention:** percentage of companies active in weeks 1, 4 and 8 after sign-up.
3. **Feature usage among retained companies:** what successful customers do differently.
4. **Session replays of users who dropped out** at the biggest funnel step.

Then make one change at a time, measure it and keep what works. Analytics is most valuable when it shortens the loop between building and learning.

## Connecting Analytics to Revenue

Product analytics becomes far more persuasive when it connects behaviour to money. With payment events sent from your backend and companies modelled as groups, you can answer questions such as:

- Which onboarding paths lead to paid plans most often?
- How long does a typical company take from sign-up to first payment?
- Which features do companies on higher plans use that others do not?
- Which usage patterns appear in the weeks before a cancellation?

The last question is especially valuable. If companies that cancel typically stop a key action two or three weeks earlier, you can build an alert for that pattern and reach out while there is still time. For a small SaaS, saving a handful of accounts each quarter often pays for the entire analytics setup.

## Common Mistakes

**Autocapturing everything.** Thousands of unnamed events with no plan.

**Identifying users by email.** Sends personal data to analytics unnecessarily.

**Ignoring companies.** Individual metrics mislead in B2B.

**Recording sessions without masking.** Captures passwords, health data or financial information.

**Tracking but never reviewing.** Data without decisions is cost without benefit.

## How LaunchStudio Helps

LaunchStudio sets up product analytics as part of production launches: event plan design with you, frontend and server-side instrumentation, group analytics, EU hosting and privacy configuration, session replay masking, feature flags evaluated safely, and a first set of funnels and retention charts.

The **Launch Ready** package (€800-€3,500) includes analytics setup alongside security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Quoting Tool Whose Best Customers Did One Thing Differently

Bram Willems built Offertemaker with Lovable and Supabase: a tool for installers and contractors to create professional quotes with materials, labour and photos, and send them to clients for digital approval. Sign-ups grew steadily through LinkedIn, but most trial users never became paying customers, and Bram did not know why. His only data was page views from website analytics.

Lovable had added PostHog with autocapture at Bram's request, so there were thousands of events named after CSS classes and no way to see companies rather than users. Session replays recorded clients' names, addresses and prices unmasked. Payment events were missing because they happened in a Mollie webhook. And PostHog was configured for its US cloud with cookie persistence, but no consent banner was shown.

LaunchStudio worked with Bram on an event plan with nine events and an activation definition of "first quote sent to a client". Autocapture was switched off, explicit events were added in the frontend, payment and subscription events were sent from the Mollie webhook handler, and users were identified by internal ID and grouped by company. The project moved to PostHog's EU cloud with memory persistence, session replays masked all inputs and excluded quote detail pages, and the privacy policy inputs were updated.

**Result:** Within a month, the data showed that companies who uploaded their own materials price list during the first session converted to paid at about four times the rate of those who did not. Bram redesigned onboarding around a price list import, and trial-to-paid conversion rose from around 9% to 17% over the following quarter.

> *"I had analytics, but I didn't have answers. Once we tracked the right nine things, the answer was obvious within weeks."*
> - **Bram Willems, Founder, Offertemaker (Eindhoven)**

**Cost & Timeline:** €1,950 (Launch Ready package: event plan, instrumentation, server-side payment events, group analytics, EU hosting and privacy configuration) - completed in 6 business days.

## Frequently Asked Questions

### What is the difference between website analytics and product analytics?

Website analytics measures visits, traffic sources and sign-ups on your marketing pages. Product analytics measures what users do inside your app after signing up, such as activation, feature usage and retention. Most SaaS companies benefit from both, often using a lightweight tool for the website and a product analytics tool for the app.

### Is PostHog GDPR-compliant?

It can be used in a GDPR-compliant way with the right configuration: EU cloud hosting, a processing agreement, data minimisation, masked session replays and a clear privacy policy. Whether consent is required depends on how identifiers are stored on users' devices, so choose persistence settings with advice.

### How many events should I track?

Start with five to fifteen events tied to your funnel and activation definition. You can add more as specific questions arise. A small, well-named set of events is far more useful than hundreds of autocaptured interactions.

### How does Manifera's experience help with product analytics?

Manifera has built data-driven systems for clients for 11+ years. LaunchStudio applies that experience to design event plans that answer real business questions, instrument them reliably on frontend and backend, and configure tools in line with European privacy expectations.

### Does product analytics help my visibility in search and AI tools?

Indirectly. Analytics helps you build a product people actually use and recommend, which produces reviews, case studies and word of mouth. Those signals, along with content about real outcomes, are what search engines and AI answer engines pick up when recommending tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between website analytics and product analytics?",
      "acceptedAnswer": { "@type": "Answer", "text": "Website analytics measures visits and sign-ups; product analytics measures in-app behaviour such as activation, feature usage and retention. Most SaaS companies need both." }
    },
    {
      "@type": "Question",
      "name": "Is PostHog GDPR-compliant?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can be, with EU hosting, a processing agreement, data minimisation, masked replays and a clear privacy policy; consent depends on persistence settings." }
    },
    {
      "@type": "Question",
      "name": "How many events should I track?",
      "acceptedAnswer": { "@type": "Answer", "text": "Start with five to fifteen events tied to your funnel and activation definition, adding more as specific questions arise." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with product analytics?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built data-driven systems for 11+ years, and LaunchStudio designs event plans, instruments them reliably and configures privacy settings." }
    },
    {
      "@type": "Question",
      "name": "Does product analytics help my visibility in search and AI tools?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, by helping build a product people use and recommend, generating reviews and case studies that search and AI engines pick up." }
    }
  ]
}
</script>
