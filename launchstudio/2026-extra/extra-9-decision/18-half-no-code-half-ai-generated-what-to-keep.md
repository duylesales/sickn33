---
Title: "Half No-Code, Half AI-Generated: Deciding What to Keep When You Go Live"
Keywords: no-code to production, Airtable backend limits, Make Zapier production, hybrid no-code AI app, what to keep when launching, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Half No-Code, Half AI-Generated: Deciding What to Keep When You Go Live

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Half No-Code, Half AI-Generated: Deciding What to Keep When You Go Live",
  "description": "Most real products built in 2026 are stitched together from an AI-generated front end plus three or four no-code tools, and going live means deciding which pieces survive. A keep, wrap or replace framework with the thresholds that decide each case.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-20",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/half-no-code-half-ai-generated-what-to-keep"
  }
}
</script>

LaunchStudio's CEO, Herre Roelevink, describes the shift like this: the challenge is no longer turning good ideas into software — it's the architecture and the security needed to let those products grow up. Nowhere is that more visible than in the hybrid products founders are actually building right now, which are almost never one thing. They're a Lovable or Bolt front end, an Airtable base holding the real data, a Make or Zapier scenario gluing them together, a Tally form for onboarding, a Stripe payment link taped to the side, and one Google Sheet that turns out to be load-bearing.

Nothing about that is embarrassing. It's how a solo founder gets to a working product in six weeks without a budget, and the alternative — waiting until you can afford to build it "properly" — is how products don't get built at all. But going live changes the question. A stack that's brilliant for finding out whether people want the thing is not automatically the stack to run it on once people are paying and their data is in it. So: which pieces stay, which get wrapped, and which have to go?

## The three verdicts

Every component in your stack gets one of three labels, and the whole article is about how to assign them.

**Keep.** It works, it will keep working as you grow, and moving it would be effort spent for no gain. Most of your stack should land here, and founders systematically under-use this verdict because someone told them no-code isn't "real."

**Wrap.** The tool stays, but something is built in front of it — usually a small piece of custom code that holds the credentials, enforces the rules, and talks to the tool on your behalf, so your users never touch it directly. This is the cheapest verdict and the most under-used.

**Replace.** The tool is doing a job it structurally can't do safely at production scale, and it needs to be a real database or a real server. This is the expensive verdict, and the point of the framework is to make sure you only spend it where it's genuinely required.

## The one question that decides most of it

Before the detailed rules, there's a single question that resolves maybe 70% of cases: **can a customer, or someone pretending to be one, reach this tool directly?**

If a tool sits behind you — you open it, your team opens it, it never appears in a browser request from a customer's computer — it is almost always a Keep. Your internal ops board, your content calendar, your CRM, your reporting spreadsheet. These are business tools. Nobody needs to rebuild a business tool.

If a customer's browser talks to it, everything changes, because a browser is a hostile environment by definition. Anything your front end sends to Airtable, Google Sheets, or a webhook URL can be seen, copied and modified by the person sitting in front of it. That's not a hypothetical about hackers — it's a menu built into Chrome. So the second a no-code tool is being contacted from your app's front end, it's a Wrap or a Replace, never a Keep.

## When Airtable or Sheets has to stop being your database

This is the biggest decision in most hybrid stacks, so it's worth being concrete about where the line sits.

**Replace if it holds customer data that customers themselves can read or write through your app.** The mechanism matters: to let your front end read from Airtable, you need an Airtable API key in your front end, and anything in your front end is public. That key doesn't grant access to one row — it grants access to the entire base. Every customer record, every email, every note. This is the single most common serious flaw we find in hybrid stacks, and founders are usually shocked, because the app itself looks completely normal.

**Replace if you'd be in trouble when two things happen at once.** Airtable and Sheets have no transactions — no way to say "either both of these changes happen or neither does." Take money and grant a subscription as two separate steps and you will eventually have customers who paid without access, or access without payment. At low volume you fix these by hand. At two hundred customers you don't.

**Replace if you're approaching the ceilings.** Airtable's per-base record limits depend on your plan, and its API is rate-limited to a handful of requests per second per base. Sheets slows noticeably as it grows. If each of your users generates several records a day, do the arithmetic on where you'll be in a year — and note that migrating a database with a thousand paying users in it is dramatically harder than migrating one with twenty.

**Keep if it's yours.** Your pipeline, your content plan, your internal tracker, your invoice log. Real database, wrong problem.

**Wrap if the data is genuinely customer-facing but the volumes are small and the structure suits it.** A small backend service holds the Airtable key, checks who's asking and what they're allowed to see, and returns only their rows. Your front end talks to that service instead of to Airtable. This is often a two-to-three-day job and it buys you a year.

## When your automations are a reliability problem

Make and Zapier are excellent and they are not the same as code, in one specific way: they're built for tasks that can be a bit late and can occasionally be retried by a human.

**Keep for anything internal or non-urgent.** New signup posts to Slack. Weekly digest email. Row added to your reporting sheet. If a scenario fails at 3am and you fix it at 9am, nobody was harmed.

**Replace for anything a customer is waiting on, or anything that must happen exactly once.** The obvious case is payment. If your flow is "Stripe → Zapier → Airtable → grant access," then a customer who pays is waiting on a queue you don't control, with a failure mode that is silent by default. And automations retry — meaning the same payment can be processed twice, and a customer can be charged or credited twice, unless something explicitly prevents it. Payments and access rights belong in code that can be tested and reasoned about.

**Also worth knowing:** your automation platform holds credentials to everything it touches, and a scenario's execution history often contains real customer data in plain view. Whoever has access to that account effectively has access to your product. That's worth checking before it's worth rebuilding.

## When forms and payment links have quietly become your product

Tally, Typeform and Stripe payment links are the pieces founders forget to evaluate, because they feel like small conveniences rather than architecture.

A form is fine for collecting an enquiry. It becomes a problem when it's how people sign up — because a form submission isn't an account. There's no password, no session, no way for someone to log back in and see their own data, and no way for you to know that the person editing a record is the same person who created it. If your product has anything a user should come back to, you need real accounts, and that's a Replace regardless of how well the form works.

Payment links have a similar shape. A Stripe payment link takes money beautifully. What it doesn't do is tell your product that a specific user is now on a specific plan, handle a cancellation, or downgrade someone whose card failed in month four. If you're currently matching payments to users by email address, by hand, in a spreadsheet — that works up to roughly thirty customers and becomes your whole week at a hundred.

## The seams are where things actually break

One more category, because it's the one nobody looks at: the joints between tools.

Every hybrid stack has a customer record that exists in four places — Airtable, Stripe, your email tool, and your app — and no single place that's authoritative. Someone changes their email address in one, and now they're two people. Someone cancels in Stripe and stays active in Airtable. Someone asks you to delete their data under GDPR, and answering honestly means knowing every system it's in, including the automation logs.

Before you go live, do one unglamorous exercise: write down every tool in your stack, what customer data is in each, who has access, and which one is the source of truth for each fact. It takes an hour and it usually surfaces two things you'd forgotten entirely. It's also, incidentally, most of what a GDPR processing record requires — so you're doing it eventually anyway.

## A worked example of the framework

Say you have: a Lovable front end, Airtable holding user projects, Make connecting Stripe to Airtable, a Tally onboarding form, and a Google Sheet you use for reporting.

The reporting sheet: **Keep**, immediately, it's internal. The Tally form: **Replace** with real accounts, because people need to log back in. Airtable: **Replace** for the customer projects — customers read and write those through the app, which means the key would be public — but **Keep** as your internal ops view, syncing from the new database. Make: **Keep** for the Slack notifications and digest emails; **Replace** for the payment-to-access path, which becomes a proper webhook handler. Stripe: **Keep** — always keep Stripe — but wire it up properly rather than through a link and a spreadsheet.

That's one Keep, two split verdicts, and two Replaces. Scoped that way, this is typically a one-to-two-week piece of work in the €800–€3,500 range rather than the rebuild an agency would quote — precisely because four of your six components survived. That's the approach [LaunchStudio](https://launchstudio.eu/en/) takes: keep the front end you built and every tool that's genuinely fine, move only the pieces that can't safely face customers, with engineers from [Manifera's](https://www.manifera.com/about-us/) team, who've spent eleven-plus years being the people who decide where a system's boundaries belong.

Draw up your own list — every tool, what's in it, who can reach it. Then send it over, and we'll come back with the three verdicts and what each one costs. Most founders find that fewer pieces need replacing than they feared, and one piece needs it more urgently than they realised.

## Real example

### Five Tools, Two Verdicts That Mattered

Bram Oosterhuis ran Zaadgoed, a subscription service for heirloom seed collections, from Deventer. The front end was built in Lovable, the catalogue and customer orders lived in Airtable, Make connected a Stripe payment link to the Airtable base, and a Tally form handled the preferences quiz new subscribers filled in. Around 180 subscribers, growing steadily, and he wanted to hit a thousand before spring.

Two findings changed the plan. The Lovable front end read the catalogue and each customer's order history directly from Airtable, using a key embedded in the page — which meant the full base, including 180 people's names, addresses and order histories, was retrievable by anyone who opened the browser's developer tools. Separately, the Make scenario connecting payment to fulfilment had failed silently eleven times over four months. Bram knew about four of them, because those customers had emailed him. He didn't know about the other seven.

**Result:** Customer orders and accounts moved to a proper database with per-customer isolation and real logins replacing the Tally quiz; the payment path became a signed Stripe webhook handler that processes each event exactly once and can't fail quietly. Airtable stayed — as Bram's internal catalogue and packing view, synced from the database — and the Make scenarios for Slack alerts and the weekly digest stayed untouched.

> *"I'd braced myself for 'throw it all away and start again.' What I got was 'these two things have to move, the other three are fine, here's the price.' I still open Airtable every morning to pack orders."*
> — **Bram Oosterhuis, Founder, Zaadgoed (Deventer)**

**Cost & Timeline:** €2,650 (Launch & Grow) — nine business days.

---

## Frequently Asked Questions

### Is it really unsafe to have my app read from Airtable directly?

Yes, because of how the access works. An Airtable API key grants access to an entire base rather than to one person's rows, and any key your front end uses is visible to anyone who opens their browser's developer tools. The tool isn't at fault — it was never designed to be queried by strangers' browsers.

### Can I keep using Airtable at all once I have a real database?

Absolutely, and many founders do. Airtable is excellent as an internal working surface — a view your team edits, packs orders from, or plans content in — synced from the database that customers actually touch. What changes is which one is authoritative and who can reach it.

### How do I know if my Make or Zapier scenarios have been failing silently?

Open the execution history and filter for errors rather than trusting the notification emails, which are easy to miss and sometimes not enabled. Count failures over the last three months and check how many produced a customer complaint. The gap between those two numbers is the size of the problem.

### At what point does matching payments to customers by hand stop working?

Around thirty to fifty customers for most founders, though it depends more on churn than on total count — cancellations, upgrades and failed cards are what generate the manual work, not signups. If you're spending more than an hour a week reconciling, the automation has already paid for itself.

### Will replacing part of my stack break the front end I built?

It shouldn't. What changes is the address your app calls and what it gets back, not your screens, layout or copy. A well-scoped migration keeps the same components rendering the same shapes of data, and the pages your users see stay identical throughout.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is it really unsafe to have my app read from Airtable directly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. An Airtable API key grants access to an entire base rather than one person's rows, and any key used by your front end is visible in the browser's developer tools. The tool was never designed to be queried directly by strangers' browsers."
      }
    },
    {
      "@type": "Question",
      "name": "Can I keep using Airtable at all once I have a real database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and many founders do. Airtable works well as an internal surface your team edits or packs orders from, synced from the database customers actually touch. What changes is which system is authoritative and who can reach it."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my Make or Zapier scenarios have been failing silently?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open the execution history and filter for errors rather than relying on notification emails. Count failures over three months and compare that with how many produced a customer complaint; the gap is the size of the problem."
      }
    },
    {
      "@type": "Question",
      "name": "At what point does matching payments to customers by hand stop working?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually around thirty to fifty customers, though churn matters more than headcount since cancellations, upgrades and failed cards create the manual work. More than an hour a week spent reconciling means automation has already paid for itself."
      }
    },
    {
      "@type": "Question",
      "name": "Will replacing part of my stack break the front end I built?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It shouldn't. What changes is the address your app calls and the shape of the response, not your screens, layout or copy. A well-scoped migration keeps the same components rendering the same data and the user-facing pages identical."
      }
    }
  ]
}
</script>
