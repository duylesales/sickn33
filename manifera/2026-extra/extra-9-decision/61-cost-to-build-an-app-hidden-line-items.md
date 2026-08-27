---
title: "Cost to Build an App: The Hidden Line Items in Your Fixed Quote"
keywords: "cost to build an app, app development budget, fixed-price app quote, hidden app development costs, mobile app development cost"
buyer_stage: "Decision"
target_persona: "Founder"
---

# Cost to Build an App: The Hidden Line Items in Your Fixed Quote

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cost to Build an App: The Hidden Line Items in Your Fixed Quote",
  "description": "A euro-by-euro breakdown of the cost to build an app, showing which line items are missing from most fixed-price quotes and how non-technical founders can budget for them before signing a contract.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-24",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/cost-to-build-an-app-hidden-line-items"}
}
</script>

Fewer than half of the fixed-price app quotes founders sign actually hold their original number by the time the app reaches the App Store. The rest quietly grow — through change orders, "out of scope" emails, and a final invoice that looks nothing like the one-pager you approved months earlier. If you are staring at a proposal right now trying to work out the real cost to build an app, the number printed at the bottom of that PDF is not the number you should be budgeting around. It is a starting bid, and the gap between that bid and your actual spend is made up of line items vendors rarely put on page one.

This matters most for founders without an in-house technical team, because you have no easy way to sanity-check a quote against reality. You are trusting a vendor's word on scope, and vendors have every incentive to keep the headline number attractive enough to win the deal against three competing bids. This article walks through exactly which costs get hidden, why they get hidden, and how to build a budget that survives contact with development reality rather than falling apart in month three.

## Why the Fixed-Price Number Isn't the Real Cost to Build an App

A fixed-price quote is only as accurate as the specification it was built against. Most quotes are generated from a short discovery call and a handful of reference apps you pointed to as inspiration — not a written specification detailed enough to estimate against reliably. When the vendor starts building and discovers that "user profiles" actually means five different profile types with different permissions, that gap becomes a change order, and change orders are priced at a markup because they were never part of the original estimate. By the time you notice the pattern, you have already signed off on two or three of them.

The honest cost to build an app has two components: the base build, which is what most quotes price, and the discovery and iteration overhead, which most quotes omit or radically underestimate. A rigorous discovery phase before pricing — data models, user flows, API dependencies mapped in advance — is the single biggest predictor of whether a fixed-price quote survives intact. Vendors who skip this step are not necessarily dishonest; they are often just as surprised by the eventual overrun as you are, because neither side actually knew what "done" meant when the contract was signed.

## Line Item 1: Discovery and Scoping Depth

Cheap quotes are often cheap because the vendor skipped proper discovery. A one-to-two week discovery sprint that produces wireframes, a data model, and a written feature specification typically costs €3,000-€6,000 depending on app complexity — and it is money well spent, because it is the document every later estimate gets measured against. Without it, "scope" is whatever the founder and the vendor each individually assumed, and those assumptions rarely match once real screens exist. Founders who skip this step to save a few thousand euros almost always spend more than that back in change orders within the first two development sprints.

A good discovery deliverable should be specific enough that a second, independent vendor could read it and produce roughly the same estimate. If your discovery document is three paragraphs of prose rather than a structured spec with entities, flows, and edge cases, treat the resulting quote as directional, not binding.

## Line Item 2: Third-Party Integrations and API Costs

Payment processing, push notifications, mapping, SMS verification, social login — each of these pulls in a third-party API with its own setup time, usage-based fees, and edge cases the vendor has to handle. A Stripe integration alone can add 20-40 development hours once you account for webhooks, refunds, disputed charges, and failed-payment retry logic. If your quote lists "payment integration" as a single line with no hour estimate attached, assume it is underscoped, because experienced teams price these individually rather than bundling them into a vague catch-all line.

Multiply this across three or four integrations and the gap between "app with payments" and "app with payments, notifications, and location services" can easily run an extra €8,000-€15,000 that never appeared on the original one-page quote.

## Line Item 3: Design Iteration Beyond Round Two

Most quotes include two rounds of design revision. Founders routinely need four to six, because seeing a screen in a working prototype reveals problems that were invisible in a static mockup — a navigation pattern that looked fine in Figma but confuses real users, a form that needs restructuring once actual data fields are mapped. Each additional round beyond what is contracted typically runs €800-€1,500 per major screen set. Ask upfront how many rounds are included and what an extra round costs — this single clarification prevents one of the most common budget surprises founders report after launch.

## Line Item 4: App Store Compliance and Review Cycles

Apple and Google both reject a meaningful share of first submissions over privacy disclosures, permission requests, or design guideline violations. Fixing a rejection and resubmitting is not usually free rework under a fixed-price contract unless the contract explicitly says so — and Apple's review cycle alone can add one to two weeks per rejection cycle, with no guarantee the second submission clears on the first pass either. Confirm in writing whether store submission and rejection remediation are included in your quoted cost to build an app, because many contracts stop at "code complete," not "live and approved in the store," and that gap can add real weeks to your launch timeline.

## Line Item 5: Post-Launch Bug Fixes vs. New Feature Requests

The line between a "bug" and a "new feature" becomes contested almost immediately after launch, and vendors and founders disagree about it constantly. A button that doesn't work as the founder expected might be a legitimate defect, or it might be a feature the original spec never described in enough detail to pin down. Without a clear warranty period — typically 30-90 days of free defect fixes, defined against a written acceptance criteria document agreed before build started — every post-launch fix becomes a billing negotiation instead of a straightforward support ticket.

## Line Item 6: QA Coverage Across Devices and OS Versions

Testing on one iPhone and one Android device is not QA — it is a smoke test. Real coverage means testing across multiple screen sizes, at least two OS versions back, and both online and degraded-connectivity states. Vendors who quote minimal QA hours are shifting that risk onto you in the form of one-star reviews reporting crashes on devices nobody tested. Ask specifically what device matrix is covered in your quote, because "cross-platform tested" without a device list attached is a marketing phrase, not a QA plan.

## Line Item 7: Infrastructure and Ongoing Maintenance

The build cost ends at launch. Hosting, monitoring, SSL certificates, dependency updates, and OS-version compatibility testing continue indefinitely, and Google and Apple both push OS updates that can break apps without warning. Budget €400-€1,200 per month for infrastructure and light maintenance depending on user volume, and treat any quote that omits this entirely as incomplete, not cheap — an app with zero ongoing maintenance budget is an app that will eventually stop working and no one will notice until users start complaining.

## Why the Cheapest Bid Is Rarely the Cheapest App

When founders compare three quotes side by side, the instinct is to treat the lowest number as the most competitive offer. In practice, the lowest bid in a stack of three is frequently the one that scoped the least and assumed the most. A vendor bidding €22,000 against two competitors bidding €48,000 for the same feature list has either found genuine efficiencies worth investigating, or has quietly excluded QA, integrations, and warranty coverage to win the comparison. Founders rarely find out which explanation is true until the change orders start arriving.

The safer comparison is not lowest total cost, but cost per line item covered. Lay the three quotes side by side against the seven line items above and see which vendor actually priced discovery, integrations, design iteration, store compliance, QA, warranty, and infrastructure explicitly. The vendor with the most complete breakdown is usually the one whose final invoice will look the most like the quote you signed, even if their headline number is not the smallest one on the page.

## A Realistic Sample Budget

For a mid-complexity MVP with user accounts, one payment integration, and push notifications: discovery €4,000, base development €35,000-€55,000, design iteration buffer €3,000, App Store submission and remediation buffer €1,500, QA across a defined device matrix €2,500, and a 90-day warranty period included. Add €600-€900 monthly for infrastructure post-launch. That puts a realistic total closer to €46,000-€66,000 for the first year, not the €25,000 headline number a bargain vendor might quote to win the deal against better-scoped competitors.

This is where working with a partner offering genuine [custom software development](https://www.manifera.com/services/custom-software-development/) capability rather than a template-app shop matters — a team that scopes properly upfront prices these line items honestly instead of discovering them mid-build. Manifera's engineers also handle native and cross-platform builds directly, so the [mobile app development](https://www.manifera.com/services/mobile-app-development/) estimate you receive reflects actual engineering hours, not a placeholder guess dressed up in a polished PDF. Because Manifera can scale a team up or down within two to four weeks as scope firms up, you are not locked into a rigid headcount before the specification is even final.

## How to Protect Your Budget Before You Sign

Ask every vendor for a line-item breakdown, not a single total. Ask what happens when scope changes — the process, not just the price. Ask for the warranty period in writing. And ask to see the discovery documentation that the quote was built against; if none exists, the number you were given is a guess dressed up as a quote. With 160+ delivered projects across SMEs and larger clients, Manifera's estimating process is built around avoiding exactly this gap between quoted and actual cost, because a vendor relationship that starts with a budget surprise rarely recovers the founder's trust.

Before you sign anything, run the quote through a short checklist: does it name a specific discovery deliverable rather than "requirements gathering"; does it list integrations individually rather than as one bundled line; does it state a number of design revision rounds; does it specify what happens on App Store rejection; does it define a warranty window with clear acceptance criteria; does it name a device and OS testing matrix; and does it address infrastructure costs after handover, even briefly. A quote that answers all seven questions in writing is one you can hold a vendor accountable to later. A quote that answers none of them is a placeholder, however professional the PDF looks.

Founders who get burned on app costs almost always skipped one of these questions, not because they were careless, but because no one told them which questions mattered. Now you know which ones to ask before the next proposal lands in your inbox, and which line items separate an honest quote from an optimistic one.

None of this means fixed-price contracts are a bad idea for a first app — for a non-technical founder, a fixed price with a clear scope document is usually safer than an open-ended time-and-materials arrangement with no ceiling. The goal is not to avoid fixed pricing; it is to make sure the fixed price you sign actually reflects the full app, not just the parts that were easy to estimate on a first call. A vendor willing to walk through each of these seven line items before you sign is telling you something important about how they will handle the inevitable surprises that come up mid-build — and a vendor unwilling to have that conversation is telling you something too.

Get a custom team proposal within 48 hours that breaks down every line item before you commit a single euro.

## Frequently Asked Questions

### What is the realistic cost to build an app for a first-time founder?
For a mid-complexity MVP with accounts, one payment integration, and push notifications, budget €45,000-€65,000 for the first year including discovery, development, design iteration, and post-launch infrastructure. A quote significantly below that range has usually omitted several of the line items covered above.

### Why do fixed-price app quotes often end up costing more than promised?
Most fixed-price quotes are built from a short discovery call rather than a detailed specification, so scope gaps surface once development starts. Those gaps become change orders, which are priced separately and at a markup because they were never part of the original estimate.

### Should I pay extra for a discovery phase before getting a fixed-price quote?
Yes. A one-to-two week discovery sprint costing €3,000-€6,000 produces the specification every later estimate is measured against, and it is the single strongest predictor of whether your final invoice matches your original quote.

### Does the cost to build an app include ongoing maintenance after launch?
Not usually. Base development quotes typically stop at launch, while hosting, monitoring, and OS-compatibility updates continue indefinitely. Budget an additional €400-€1,200 per month depending on user volume, and confirm this explicitly with your vendor before signing.

### How do I know if a vendor's app development quote is missing hidden costs?
Ask for a line-item breakdown rather than a single total, request the discovery documentation the quote was built against, and confirm in writing what warranty period covers post-launch defects. A vendor unable to produce any of these has likely under-scoped the project.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the realistic cost to build an app for a first-time founder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a mid-complexity MVP with accounts, one payment integration, and push notifications, budget €45,000-€65,000 for the first year including discovery, development, design iteration, and post-launch infrastructure. A quote significantly below that range has usually omitted several of the line items covered above."
      }
    },
    {
      "@type": "Question",
      "name": "Why do fixed-price app quotes often end up costing more than promised?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most fixed-price quotes are built from a short discovery call rather than a detailed specification, so scope gaps surface once development starts. Those gaps become change orders, which are priced separately and at a markup because they were never part of the original estimate."
      }
    },
    {
      "@type": "Question",
      "name": "Should I pay extra for a discovery phase before getting a fixed-price quote?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A one-to-two week discovery sprint costing €3,000-€6,000 produces the specification every later estimate is measured against, and it is the single strongest predictor of whether your final invoice matches your original quote."
      }
    },
    {
      "@type": "Question",
      "name": "Does the cost to build an app include ongoing maintenance after launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not usually. Base development quotes typically stop at launch, while hosting, monitoring, and OS-compatibility updates continue indefinitely. Budget an additional €400-€1,200 per month depending on user volume, and confirm this explicitly with your vendor before signing."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if a vendor's app development quote is missing hidden costs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask for a line-item breakdown rather than a single total, request the discovery documentation the quote was built against, and confirm in writing what warranty period covers post-launch defects. A vendor unable to produce any of these has likely under-scoped the project."
      }
    }
  ]
}
</script>

