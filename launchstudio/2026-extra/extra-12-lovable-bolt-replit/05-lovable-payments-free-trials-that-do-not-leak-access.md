---
Title: "Lovable Payments: Free Trials That Do Not Leak Access"
Keywords: lovable payments, free trial, trial abuse, entitlement checks, trial conversion, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# Lovable Payments: Free Trials That Do Not Leak Access

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Free Trials That Do Not Leak Access",
  "description": "Trials in AI-built apps usually expire in the interface and nowhere else. How to build an entitlement check that actually holds, choose card-or-no-card, and end a trial without losing the customer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-free-trials-that-do-not-leak-access" }
}
</script>

Here is a test worth running on your own product this afternoon. Start a trial, let it expire, then log in and open the browser's developer tools while you use the app.

In a large share of AI-built SaaS applications you will find that the expired trial changed what the interface shows and nothing else. The upgrade banner appears, the buttons look disabled — and the underlying requests still work. A user who clicks a hidden element, calls an endpoint directly, or simply navigates to a URL the menu no longer links to has the full product.

The interface is not a permission system. It never was. But a tool asked to build a trial produces a trial that looks correct, and looking correct is the whole of the specification it was given.

## One Function Decides Everything

The fix is architectural and small: a single server-side function that answers whether this account may do this thing right now, called by every endpoint that does anything meaningful.

It reads state from your own database — plan, status, trial end date, entitlements — and returns an answer. The interface then uses the same function to decide what to display, which means what the user sees and what the server allows can never drift apart, because they are the same decision rendered twice.

The alternative, scattering checks through the code as each feature is built, guarantees that some endpoint written on a Friday will not have one. That endpoint is your trial leak, and you will not find it by looking at the application the way a customer does.

## Card or No Card

This is a business decision with an engineering consequence, and both options are defensible.

**No card required** maximises trial starts. You get far more people in the product, your conversion rate at the end is lower, and your total paying customers frequently higher. It suits products whose value is obvious quickly and whose audience is price-sensitive or non-technical.

**Card required** produces fewer, better-qualified trials, and converts them at a much higher rate because payment is already arranged. It suits higher-priced B2B products where each trial costs you support time.

The engineering difference is about who must act at the end. With a card, the trial converts unless the customer stops it — so your obligation is to tell them clearly beforehand. Without one, the trial ends unless the customer acts — so your obligation is to make that action easy at exactly the right moment.

If you take the card, send the reminder. In several European markets some form of advance notice before a trial converts is either required or close to it, and independently of the law, a charge that arrives unannounced after a forgotten signup is the single most reliable way to generate a chargeback and a public complaint.

## Preventing the Second Trial

Someone will sign up again with a plus-addressed email. Whether that matters depends on your product.

For a consumer tool at €9 a month, it mostly does not, and the effort of preventing it exceeds the loss. For a product with real per-account cost — anything that calls an AI model, sends physical mail, or consumes storage — repeated trials are a genuine expense.

Proportionate measures, roughly in order of how much they annoy honest customers: normalise email addresses so that plus-addressing and dot-variants collapse to one identity; require a card; verify a phone number; limit by organisation domain for B2B products. Blocking disposable-email domains is a common suggestion and mostly a waste of time, since the lists are always behind.

Whatever you choose, log it. Knowing that eleven accounts share a payment fingerprint is useful; blocking them automatically on a heuristic you cannot explain is how you lose a real customer with an unusual setup.

## Ending a Trial Without Ending the Relationship

Trial expiry is the moment most products handle worst, and it is a moment of maximum leverage: the person is in your product, has done work in it, and is deciding.

Three things make it go well.

**Do not delete their work.** An expired trial should keep the data, visible and read-only, with an obvious path to unlock it. Deleting on expiry destroys both the conversion and the option of them returning in three months.

**Let them export it anyway.** Counter-intuitive and correct: a product that holds data hostage is a product people warn each other about. The export costs you almost nothing and buys goodwill you will be glad of.

**Ask why, once, plainly.** A single question in the expiry email — what were you hoping it would do? — answered by a small fraction of people, is the highest-quality product feedback a small company gets, because it comes from people who tried and decided against.

And handle the extension request gracefully. Someone who asks for another week is telling you they are still interested; an admin action that grants it in ten seconds is worth building the first time you are asked.

## Instrument the Trial, Not Just the Conversion

Most founders know their trial-to-paid percentage and nothing else, which tells them whether something is wrong but never what.

Three measurements change that, and all are within reach of a small product. **Time to first meaningful action** — the point where someone has actually used the product for its purpose, not merely signed up. Define it specifically for your tool: the first patient checked in, the first invoice sent, the first schedule published. If that median is four days into a fourteen-day trial, your onboarding is eating the trial.

**The proportion who never reach it at all.** These are the people your expiry email cannot save, because they never saw the product work. For most struggling trials this number is the whole problem, and it is fixed at signup rather than at expiry.

**Activity in the final third.** People still using the product in the last few days convert at a far higher rate than those who drifted off in week one. It tells you whether your reminder emails should be about the deadline — useful for engaged trialists — or about getting started, which is what the drifted ones need.

Measuring these takes a timestamp column and three queries, not an analytics platform. And the reason it belongs in the same work as the entitlement fix is practical: once you know who is engaged and who is not, the expiry sequence stops being one email to everybody and becomes two short ones to two groups with genuinely different problems — which is typically worth more conversion than anything else you can change in a week.

## The Quiet Cost of a Generous Trial

A trial is not free to run, and the products that discover this late are the ones where each account consumes something real: model calls, storage, email volume, a seat at a service you pay per user for.

Work out the number before you set the length. If a trialist costs you €0.40, a 30-day no-card trial at a few hundred signups a month is a rounding error. If they cost €9 because your product summarises documents with a language model, the same trial is a meaningful line on your own bill and deserves either a card requirement, a usage cap during the trial, or both.

Caps are usually the better answer than shortening the trial, because they preserve the thing that matters — time to evaluate — while bounding the cost. Twenty documents, five reports, one export: enough to see whether the product works, not enough to run a business on. Say the limit plainly in the interface rather than enforcing it silently, and make hitting it an upgrade prompt rather than an error, since a trialist who reached your cap is the most qualified lead you have that week.

## Setting This Up

For an existing product this is usually two to three days: a single server-side entitlement function called by every endpoint, trial state held in your own database with an explicit end date, the interface driven by the same function so display and permission cannot diverge, an audit of existing endpoints for the ones with no check at all, card-or-no-card implemented with the matching reminder or expiry sequence, proportionate duplicate-trial handling, read-only retention with export after expiry, and an admin extension action.

LaunchStudio does this as part of production readiness, and it is one of the most common findings in any review of an AI-built SaaS. Behind the work is Manifera: 120+ engineers and eleven years of production systems for clients including Vodafone, TNO and CFLW.

[Ask us to test your expired trial](https://launchstudio.eu/en/#contact) — we do it with the developer tools open, which is how your users will do it.

## Real example

### Forty Accounts on an Expired Trial

Lotte van Bemmel built Wachtkamer in Lovable: patient check-in and waiting room display software for general practices, €59 per month after a 21-day trial without a card.

Her trial logic lived in the frontend. When the end date passed, the app displayed an upgrade screen and disabled the navigation. It did not change what the server would do for an authenticated request.

She found out from her own hosting bill. Usage was growing faster than revenue, and when she counted active accounts against paying ones the gap was 40 practices — some of which had been running daily check-ins for five months on an expired trial. Several had assumed the product was free. Two had told colleagues so.

Three business days: a single server-side entitlement function reading plan and trial state from the database, called by every endpoint including the display-screen API that had never checked anything; the frontend rewired to ask the same function what to show; an audit of all 34 endpoints, of which 19 had no authorisation check whatsoever; email normalisation to collapse plus-addressed duplicate trials; a reminder sequence at day 14, day 20 and expiry; read-only access with data export retained for 60 days after expiry; and an admin action to extend a trial by a set number of days.

**Result:** of the 40 practices using the product without paying, 12 converted to paid plans within a month of the access actually stopping, 6 asked for and received a short extension and half of those converted too, and infrastructure costs fell by a third. Trial-to-paid conversion on new signups rose from 18 to 29 percent, which Lotte attributes mostly to the day-14 reminder rather than to the enforcement.

> *"Forty practices were using it daily and I had no idea, because on my screen the trial had ended. The interface was lying to me as much as it was to them."*
> — **Lotte van Bemmel, Founder, Wachtkamer (Alkmaar)**

**Cost & Timeline:** €2,400 (server-side entitlement function, endpoint authorisation audit and remediation, trial state model, reminder sequence, export and retention, admin extension) — completed in 3 business days.

## Frequently Asked Questions

### How do I know whether my trial actually expires?

Let one expire, then call your API endpoints directly with the expired account's session. If they return data, your trial expires in the interface only — which is the most common finding in reviews of AI-built SaaS products.

### Should I require a card to start a trial?

It depends on price and audience. No card brings more trials and lower conversion; card required brings fewer and much higher conversion. Higher-priced B2B products usually take the card; low-priced or non-technical products usually should not.

### Do I have to warn customers before a trial converts to a paid plan?

Send the reminder regardless of what is strictly required where you operate. An unannounced charge after a forgotten signup is the most reliable source of chargebacks and complaints a small product has.

### How long should a trial be?

Long enough to reach the moment your product becomes useful, which for most tools is 14 days and for anything with setup work is closer to 30. Measure when trialists first do the thing that matters and set the length from that, not from convention.

### What should happen to data when a trial ends?

Keep it, read-only, with an export available, for a stated period. Deleting it destroys both the conversion and the chance of them returning later.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I know whether my trial actually expires?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Let a trial expire and call your API endpoints directly with that session. If data comes back, the trial expires only in the interface."
      }
    },
    {
      "@type": "Question",
      "name": "Should I require a card to start a trial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No card gives more trials and lower conversion; card required gives fewer and much higher conversion. Higher-priced B2B usually takes the card."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to warn customers before a trial converts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Send the reminder regardless. An unannounced charge after a forgotten signup is the most reliable source of chargebacks a small product has."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a free trial be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Long enough to reach the moment the product becomes useful — typically 14 days, or around 30 when setup work is involved. Measure it rather than copying convention."
      }
    },
    {
      "@type": "Question",
      "name": "What should happen to data when a trial ends?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep it read-only with an export available for a stated period. Deleting it destroys both the conversion and any chance of them returning."
      }
    }
  ]
}
</script>
