---
Title: "Building a Shopify App With AI Tools: Review, Billing and Launch"
Keywords: build shopify app with ai, shopify app review requirements, shopify billing api, shopify app developer, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Building a Shopify App With AI Tools: Review, Billing and Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Building a Shopify App With AI Tools: Review, Billing and Launch",
  "description": "AI coding tools can generate a working Shopify app quickly, but reaching the Shopify App Store requires correct OAuth and session tokens, verified webhooks, mandatory privacy webhooks, the Billing API, performance standards and a review process. This guide explains each requirement and how LaunchStudio takes AI-built Shopify apps to launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-26",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/building-a-shopify-app-with-ai-tools-review-billing-and-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "Shopify App Store requirements", "url": "https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements" },
    { "@type": "CreativeWork", "name": "Shopify privacy law compliance webhooks", "url": "https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance" },
    { "@type": "CreativeWork", "name": "Shopify Billing API", "url": "https://shopify.dev/docs/apps/launch/billing" },
    { "@type": "CreativeWork", "name": "Shopify: Verify webhooks", "url": "https://shopify.dev/docs/apps/build/webhooks/subscribe/https" }
  ]
}
</script>

Shopify merchants are some of the most willing buyers of software anywhere. They pay monthly for apps that save them time or make them money, and the Shopify App Store puts your product in front of them. For a founder with e-commerce experience and an AI coding tool, building a Shopify app is an attractive path: start from Shopify's official template, describe the features to Cursor or Claude Code, and within weeks you have something that installs on a development store and works.

The gap between "works on my development store" and "approved in the App Store and trusted by merchants" is larger than in most products. Shopify enforces specific technical and policy requirements, and its review team checks them. Merchants also trust you with their customers' personal data, which brings privacy obligations.

This guide explains what an AI-built Shopify app needs before launch.

## Key Takeaways

- **Start from Shopify's official app template.** It handles OAuth, session tokens and embedding correctly; AI tools should build features on top of it, not replace it.
- **Webhooks must be verified,** using the HMAC signature Shopify sends, and processed reliably with retries and idempotency.
- **Three privacy compliance webhooks are mandatory** for public apps: customer data requests, customer data erasure and shop data erasure.
- **Apps that charge merchants through the App Store must use Shopify's Billing API,** not an external payment provider.
- **Plan for review.** Shopify's requirements cover functionality, security, performance and listing quality; preparing for them up front avoids weeks of back-and-forth.

## Why Shopify Apps Are a Special Case

Most SaaS products control their whole environment. A Shopify app does not. It runs inside the merchant's Shopify admin, authenticates through Shopify, receives events from Shopify, often bills through Shopify and must meet Shopify's rules to stay listed. Every one of those touchpoints has a correct way to work, documented by Shopify, and a set of plausible-looking ways that AI tools sometimes produce instead.

The stakes are also higher than they look. A merchant's store contains customer names, addresses, order histories and sometimes sensitive purchase data. An app with access to that data and a security flaw is not only your problem; it is the merchant's problem with their own customers. Shopify's requirements exist largely to prevent that.

## Foundation: The Official Template and Shopify CLI

Shopify provides an official app template and the Shopify CLI to create, run and deploy apps. The template includes the authentication flow, session handling, embedding in the Shopify admin through App Bridge, and a structure for webhooks and API calls.

AI tools are good at building features on this foundation. They are less reliable when asked to build authentication from scratch or to "simplify" the template. Common problems when founders let an AI rewrite the foundation:

- OAuth implemented manually without validating the `state` parameter or the HMAC on the callback
- Access tokens stored in plain text in a table with no access controls, or logged
- Embedded app pages that rely on cookies, which browsers increasingly block inside iframes, instead of Shopify's session tokens
- Requested API scopes far broader than the app needs, which merchants and reviewers notice

A useful rule for any AI session: treat authentication, session handling and the webhook entry points as protected files. Build features around them.

## Access Scopes: Ask for Less

Every Shopify app requests access scopes, such as reading products or writing orders. Merchants see the list at install time. AI-generated apps often request broad scopes "just in case", because that avoids permission errors during development.

Before launch, review every scope against features that actually use it. Fewer scopes mean less risk if your app is compromised, faster trust at install and fewer questions in review. If the app needs access to protected customer data, such as names, emails or addresses, Shopify requires you to request that access explicitly and describe how you use and protect it.

## Webhooks: Verified, Fast and Idempotent

Shopify sends webhooks for events such as orders created, products updated or the app uninstalled. Three properties matter.

**Verified.** Each webhook includes an HMAC signature header. Your app must compute the signature over the raw request body with your app's secret and compare it before trusting the payload. AI-generated handlers sometimes parse the JSON body first, which changes the bytes and makes verification fail, after which the "fix" is to remove verification. That leaves an open endpoint anyone can call with fake orders.

**Fast.** Shopify expects a quick response. Heavy processing should be queued and handled in the background, with the webhook endpoint acknowledging receipt promptly.

**Idempotent.** Shopify may deliver the same webhook more than once. Store the webhook ID and skip duplicates, so a retried "order created" does not trigger two fulfilment actions.

The `app/uninstalled` webhook deserves special attention: when a merchant uninstalls, stop using their access token, cancel scheduled work and follow your data retention rules.

## Mandatory Privacy Compliance Webhooks

Public apps distributed through the App Store must implement three compliance webhooks, as described in Shopify's privacy documentation:

| Webhook | When it is sent | What your app must do |
| --- | --- | --- |
| `customers/data_request` | A customer asks the merchant for their data | Provide the customer data your app stores to the merchant |
| `customers/redact` | A merchant requests deletion of a customer's data | Delete or anonymise that customer's data |
| `shop/redact` | Some time after a merchant uninstalls | Delete the shop's data |

These map closely onto GDPR rights of access and erasure, which apply anyway if you serve European merchants. Founders often stub these endpoints to return success without doing anything. That passes a quick test and fails both the spirit of the requirement and the law. Implement them properly and log what was done.

## Billing: Use the Billing API

If your app charges merchants and is distributed through the Shopify App Store, Shopify's requirements state that charges must go through the Shopify Billing API. You can offer recurring subscriptions, usage-based charges and one-time purchases, and merchants approve them inside Shopify. Shopify collects the payment and pays you, minus its revenue share.

Founders coming from Stripe sometimes ask an AI to integrate Stripe for subscriptions. For a public App Store app, that is a review rejection waiting to happen. Using the Billing API also simplifies your life: no card handling, no VAT invoicing to merchants for those charges and a familiar approval flow for merchants.

Implementation points that matter:

- Check the merchant's active subscription on every relevant request, not only at install.
- Handle plan changes, cancellations and frozen stores gracefully.
- Use test charges on development stores, and make sure test mode is off in production.
- Record usage charges idempotently, so retries never bill twice.

## Performance and the Merchant Experience

Shopify's requirements and its "Built for Shopify" standards put weight on performance and user experience. Apps that inject scripts into storefronts are expected not to slow them down significantly; admin pages should load quickly and follow Shopify's design patterns, typically through Polaris components.

AI tools sometimes add heavy libraries, load data for all products on every page, or inject large storefront scripts. Before submission:

- Measure storefront impact if your app adds anything to the theme, and prefer theme app extensions over direct script injection.
- Paginate admin lists and use GraphQL queries that request only the fields you need.
- Respect Shopify's API rate limits with backoff and queuing.
- Test with a store that has thousands of products, not twenty.

## Preparing for App Review

Shopify reviews public apps before listing and checks a long list of requirements. Preparing these in advance avoids most rejections:

- **A working install flow** that redirects to the app UI immediately after authorisation
- **Accurate listing:** screenshots, description and pricing that match the app
- **A test account or instructions** so reviewers can use every feature
- **Compliance webhooks** that actually work
- **Billing through the Billing API**
- **Clean uninstall** behaviour
- **A privacy policy** describing the data you collect and why
- **Support contact** that responds

Read Shopify's current App Store requirements before submitting; they change, and the official list is the authority.

## Hosting and Operations

Shopify apps are web applications you host yourself. That means the usual production checklist applies: secrets in your host's secret manager, a production database with backups, error tracking, uptime monitoring, logs for webhook processing and a staging app connected to a development store. For European founders serving European merchants, host data in an EU region and list your processors in your privacy policy.

## Working With AI Tools on a Shopify App Safely

None of this means you should stop using Cursor, Claude Code or other AI tools on your Shopify app. They are excellent at the parts that make your app distinctive: the bundle logic, the reporting screens, the theme extension, the merchant settings. The goal is to let them work quickly where mistakes are cheap and slow them down where mistakes are expensive.

A few habits make the difference:

- **Write the rules down.** Put a short instructions file in the repository that says "never modify authentication, session handling or webhook verification; all charges go through the Billing API; request no new scopes without approval". AI tools follow written conventions well.
- **Mark protected paths.** Authentication routes, webhook handlers, compliance endpoints and billing code should require a human review for every change.
- **Test against Shopify, not mocks.** Keep a development store with realistic data and run new features against it. Mocked Shopify responses hide the API limits and payload details that cause production bugs.
- **Re-read the requirements before every major release.** Shopify updates its App Store requirements and API versions on a regular schedule. A short checklist review before each release prevents a listing problem months later.
- **Track API versions.** Shopify's APIs are versioned and older versions are retired over time. Note which version your app uses and plan upgrades, rather than discovering a deprecation through failing requests.

Used this way, AI tools keep their speed advantage, and the parts of the app that Shopify and merchants scrutinise most stay stable.

## What It Costs

A production review and launch preparation for an AI-built Shopify app typically falls within **Launch Ready** (€800-€3,500): authentication and webhook review, compliance webhooks, scope reduction, deployment and 48 hours of support. Apps that need Billing API integration, background processing, managed hosting and ongoing support typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month). You receive a fixed quote after a 15-minute call. The [price calculator](https://launchstudio.eu/en/#calculator) gives a first range.

For merchants building their own store rather than an app, our article comparing [a webshop built with an AI builder versus Shopify](https://launchstudio.eu/en/blog/webshop-with-an-ai-builder-vs-shopify) may be more relevant.

## Who Does the Work

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including e-commerce integrations for clients across Europe and Asia. Founders work with the team at Herengracht 420 in Amsterdam; engineers are based at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Bundle App That Failed Review Twice

Lisa Brouwer ran a Shopify store for sustainable baby products in Haarlem and kept wishing for a better way to sell product bundles with automatic stock deduction for each component. She built Bundelbaas with Cursor, starting from a tutorial rather than the official template, and ten merchants she knew installed it as a custom app.

Her first App Store submission was rejected because charges ran through Stripe instead of the Billing API. The second was rejected because the compliance webhooks returned success without doing anything and the install flow showed a blank page for several seconds. Meanwhile, a review of the code revealed that webhook verification had been removed after it kept failing, the app requested nine access scopes but used four, and merchants' access tokens were stored unencrypted. Stock updates sometimes ran twice when Shopify retried a webhook.

LaunchStudio moved Bundelbaas onto Shopify's official template, carrying the bundle logic across, and replaced the custom OAuth with the template's session token handling. Webhook verification was restored using the raw body, duplicate deliveries were skipped by webhook ID and heavy processing moved to a background queue. The compliance webhooks were implemented to export and delete data, scopes were reduced to four, tokens were encrypted at rest, and billing moved to the Billing API with three plans and a usage charge for large catalogues. Hosting moved to an EU region with monitoring and a staging app.

**Result:** Bundelbaas passed review on its third submission, 14 business days after the first call. Within four months it had around 230 installs, and duplicate stock deductions disappeared entirely.

> *"Cursor helped me build the features merchants wanted. LaunchStudio made it the kind of app Shopify was willing to list."*
> - **Lisa Brouwer, Founder, Bundelbaas (Haarlem)**

**Cost & Timeline:** €4,700 (Launch & Grow package: template migration, webhook and compliance fixes, Billing API, EU hosting and monitoring) - completed in 14 business days.

## Frequently Asked Questions

### Can I use Stripe to charge merchants for my Shopify app?

Not for apps distributed through the Shopify App Store; Shopify's requirements state that charges must go through its Billing API. Custom apps built for a single merchant outside the App Store follow different rules, but most founders building for many merchants need the Billing API.

### Are the privacy compliance webhooks really mandatory?

Yes, for public apps. Shopify requires apps to handle customer data requests, customer data erasure and shop data erasure. They also align with GDPR rights that apply when serving European merchants, so implement them properly rather than returning a placeholder response.

### Can an AI tool build a Shopify app that passes review?

It can build most of it, especially features on top of Shopify's official template. The common failure points are authentication rewrites, removed webhook verification, stubbed compliance webhooks, external billing and broad scopes. A focused review before submission addresses these.

### Why does Manifera's background help with Shopify apps?

Shopify apps combine e-commerce integration, privacy obligations and platform rules. Manifera has integrated commerce and enterprise systems for 11+ years, so LaunchStudio knows where integrations fail and how to meet platform requirements without slowing the founder down.

### Does a well-built app help my listing visibility?

Yes. Shopify's App Store and its "Built for Shopify" programme reward performance, quality and merchant experience, and a stable, fast app earns better reviews, which affect discovery both in the App Store and in external search and AI recommendations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I use Stripe to charge merchants for my Shopify app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not for apps distributed through the Shopify App Store, where charges must use the Shopify Billing API. Custom single-merchant apps follow different rules." }
    },
    {
      "@type": "Question",
      "name": "Are the privacy compliance webhooks really mandatory?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes for public apps: customer data requests, customer data erasure and shop data erasure. They also align with GDPR rights, so implement them properly." }
    },
    {
      "@type": "Question",
      "name": "Can an AI tool build a Shopify app that passes review?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can build most features on the official template. Common failures are auth rewrites, removed webhook verification, stubbed compliance webhooks, external billing and broad scopes." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera's background help with Shopify apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has integrated commerce and enterprise systems for 11+ years, so LaunchStudio knows where integrations fail and how to meet platform requirements." }
    },
    {
      "@type": "Question",
      "name": "Does a well-built app help my listing visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Shopify rewards performance and merchant experience, and a stable app earns better reviews that affect App Store, search and AI recommendations." }
    }
  ]
}
</script>
