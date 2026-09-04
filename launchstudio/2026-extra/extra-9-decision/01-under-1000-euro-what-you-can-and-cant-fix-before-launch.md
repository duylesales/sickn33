---
Title: "Under €1,000: What You Can and Can't Fix Before Launch"
Keywords: launch on a small budget, cheap production readiness, AI prototype budget, what production hardening costs, minimum viable security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Under €1,000: What You Can and Can't Fix Before Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Under €1,000: What You Can and Can't Fix Before Launch",
  "description": "A realistic breakdown of what a sub-€1,000 budget actually buys when taking an AI-generated prototype to production, and which gaps genuinely cannot be closed at that number. Helps non-technical founders decide whether to spend now, save first, or shrink the launch.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/under-1000-euro-what-you-can-and-cant-fix-before-launch"
  }
}
</script>

Nine hundred euros. That is the number a lot of founders arrive with — not because it is a considered budget, but because it is what is left after a year of subscriptions, a Lovable plan, a domain, a logo, and the accountant's invoice. And the honest answer nobody gives them is that €900 is neither nothing nor enough for everything. It buys a specific, defensible subset of production work, and it flatly cannot buy the rest.

Most advice on this dodges the question. It either tells you to bootstrap everything yourself (fine, until the part where a stranger reads your customers' data) or quotes you a number with four zeros and moves on. What follows is the actual arithmetic: what a sub-€1,000 spend covers, what it doesn't, and how to tell which side of the line your prototype falls on before you commit the money.

## Where €1,000 Sits on the Real Price Ladder

LaunchStudio's entry package, Launch Ready, runs €800–€3,500 as a fixed price. So €1,000 is not below the floor — it is just above it, in the narrow band where scope has to be chosen rather than assumed. The published [price calculator](https://launchstudio.eu/en/#calculator) makes the composition visible: a simple website-shaped project starts around €800–€2,000, a small internal tool €1,200–€3,000, a dashboard €2,000–€4,500, and a full SaaS product €2,833–€7,167. Then the add-ons stack: security hardening +€500, database and backend work +€350, payments +€400, user accounts +€250, hosting and deployment +€200, email integration +€150, external API connections +€250.

Do that arithmetic against €1,000 and the picture sharpens fast. A tool-shaped prototype at €1,200 base is already over budget before a single add-on. A website-shaped project at €800 leaves you €200 — exactly one add-on, and it had better be the right one. This is why "what can I fix for under €1,000" is really the question "which single category of risk am I buying down, and am I buying down the one that will actually hurt me?"

The founders who get value at this number are the ones who walk in having already decided what shape their product is. The ones who burn it are the ones who ask for "everything, but cheaper," get a scoped-down version of everything, and end up with four categories half-addressed instead of one category genuinely closed.

## The Four Things Worth Buying First at This Budget

If €1,000 buys one or two categories, these are the ones that repay the spend, roughly in order.

**Authorization at the API layer.** Not the login screen — the layer beneath it. AI builders reliably produce a frontend that hides the admin button from non-admins, and just as reliably produce a backend that will happily serve admin data to anyone who asks for it directly. In Supabase-backed prototypes this shows up as tables with row-level security switched off, or a single blanket policy that reads `true` for authenticated users, which means every logged-in user can read every row belonging to every other user. This is the single most common serious finding in AI-generated code, and it is the one that turns into a disclosure email rather than a bug report.

**Secrets that aren't in the browser.** A prototype that calls a third-party API from client-side code ships that API key to every visitor. Anyone can open the network tab and read it. If that key belongs to Stripe, OpenAI, or a mail provider with your card attached, the failure mode is a bill, not an inconvenience. Moving those calls behind a server route and rotating the exposed keys is a small, contained job — and it is one of the few fixes that measurably reduces a real, quantifiable financial exposure for a few hundred euros.

**A deployment you can repeat.** Not "it's on Vercel." A repeatable path: source in a repository you own, environment variables set per environment, a build that runs from a clean checkout, SSL on your own domain, and a rollback you can execute without asking anyone. Founders underrate this because the prototype is already reachable at a URL. The value shows up on the first bad deploy at 21:00 on a Friday.

**Backups you have actually restored.** Managed database platforms make backups sound automatic. Many free and starter tiers keep them for a matter of days, some for none, and almost nobody tests a restore until they need one. A nightly dump written somewhere outside the same provider, plus one documented restore that someone genuinely performed, is cheap insurance against the one failure with no workaround.

## What €1,000 Cannot Cover, Stated Plainly

Being direct here saves everyone a scoping call.

**A real payments integration.** Payments is +€400 on the calculator, and that number reflects the connection — not the surrounding work. A production payment flow means webhook signature verification, idempotency so a retried webhook doesn't grant two subscriptions, a plan-state model that survives a failed renewal, refund and cancellation handling, and VAT treatment that a Dutch accountant will accept. Stripe or Mollie's checkout page is genuinely quick. The state machine behind it is where the hours go, and it is why payments almost never fits inside a €1,000 total alongside anything else.

**Multi-tenancy retrofitted after the fact.** If your product serves organisations rather than individuals — a clinic, an agency, a school — and the prototype's database has no notion of which organisation a row belongs to, that is a schema change, a migration, and a rewrite of every query. It is not a hardening pass; it is structural. This is squarely €2,500+ territory and pretending otherwise produces a half-migrated database, which is worse than either end state.

**Migrating off a no-code backend.** Moving from Bubble, Airtable, or a Firebase structure that doesn't fit your access model into PostgreSQL involves data mapping, dual-running, and a cutover. Real work, properly done, at a real number.

**Load capacity for traffic you haven't had yet.** Query optimisation, indexing, caching, rate limiting. Legitimate work — and almost always the wrong purchase before you have users, because you will optimise the wrong query.

## The Ladder: €800 vs €2,500 vs €5,000

It helps to see the three rungs side by side, because most founders are choosing between them without knowing what separates them.

**At €800–€1,200**, you are buying one thing done properly and a second thing checked. Realistically: an access-control pass over your database policies and API routes, plus a clean deployment onto your own domain with SSL and environment variables handled correctly. What you get is a product that will not leak one customer's data to another and that you can redeploy without fear. What you do not get is payments, email, or anything that touches the schema.

**At €2,500**, the shape changes. That is enough for access control *and* a working payment integration *and* transactional email, with a database review that can actually recommend and apply small structural fixes rather than just noting them. This is the number at which a subscription product becomes genuinely sellable — you can take money, the money reconciles, and the customer gets a receipt. Most solo founders with a real product land here, not at €900.

**At €5,000**, you are into Launch & Grow territory (€2,500–€7,500 plus €49/month), and what the extra buys is not more features but less of your attention: managed hosting, uptime monitoring, automatic backups, security updates, and priority fixes. The €49/month is the part founders discount and then miss most, because it converts "something is broken and I don't know who to call" into a message thread.

The uncomfortable truth is that the gap between €900 and €2,500 is usually four to eight weeks of revenue or one raised friends-and-family cheque. Founders who spend six months protecting the €900 frequently spend more than €1,600 in delay.

## Three Things You Can Safely Postpone

Not everything that sounds urgent is. At a tight budget, these can wait, and knowing that is worth as much as knowing what can't.

**Formal penetration testing.** A structured external pen test is a real product with a real price, and it is aimed at a maturity stage past your first customers. A code-level review of authorization and secrets catches the issues that actually appear in AI-generated prototypes, at a fraction of the cost. Revisit the pen test when an enterprise buyer asks for one — and they will tell you when.

**Full observability tooling.** Error tracking through a free Sentry tier and your host's built-in logs is enough to run a product with fewer than a few hundred users. Distributed tracing and a metrics dashboard solve problems you do not have yet.

**Redundancy and multi-region hosting.** A single well-configured region with tested backups is an entirely reasonable posture for a launch. Failover architecture is for products with an SLA, and you do not have one yet.

Postponing is not the same as ignoring. Write the three down with a trigger next to each — "pen test when a customer's procurement asks," "tracing at 500 daily actives" — so the decision is deferred rather than forgotten.

## How to Make €1,000 Go Further Before You Spend It

There is preparation work that costs you nothing and directly reduces what an engineer has to bill you for, because scoping time is billable time.

Write down, in plain language, who is allowed to see what. One paragraph per user type. Half of an access-control engagement is discovering the intended rules; if you supply them, the engineer implements instead of interviewing.

Delete your seed data. Prototypes accumulate test accounts, dummy customers and half-finished tables. Every one of them is something an engineer has to ask about.

Inventory your environment variables and third-party accounts — every service with a key, who owns the login, which plan it is on. Founders routinely discover during this exercise that a co-founder's personal account holds something the company depends on.

Make sure the code is in a repository you own, with the current deployed version actually committed. It is remarkably common for the live version and the repository to have diverged, and reconciling that is an hour nobody wants to pay for.

Finally, be honest about traffic. Ten users and ten thousand users need different work, and overstating it moves you into a bracket you don't need.

## The Test That Tells You Which Bracket You're In

One question sorts most prototypes. **Does your product hold data that one user would be harmed by another user seeing?**

If no — a marketing site, a calculator, a content tool where everything is public anyway — you are genuinely a €800–€1,200 project. Deploy it properly, protect the keys, launch.

If yes — anything with accounts, uploads, client records, messages, health or financial data — then access control is not one line item among several. It is the launch condition, and it needs to be done thoroughly rather than partially. That usually puts you at €1,500 and up, and the right response to a €900 budget is not to buy a cheaper version of that work. It is to shrink the launch: strip the product down to the part that doesn't hold sensitive data, ship that, and fund the rest from what it earns.

Shrinking the product to fit the budget is a legitimate strategy. Shrinking the security work to fit the budget is not, because the thing you cut is precisely the thing that has no visible symptom until it becomes the only symptom.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience — the same engineers who [build production systems for enterprise clients](https://www.manifera.com/services/custom-software-development/) are the ones who look at a €900 prototype and say plainly which half of it is fundable today.

A small budget is a scoping problem, not a disqualification. [Run your project through the price calculator](https://launchstudio.eu/en/#calculator) and you will see, in about ninety seconds, whether you are €200 short or €2,000 short — and those are very different decisions.

## Real example

### A Non-Technical Founder in Action: Buying One Thing Properly Instead of Four Things Halfway

Sanne Vermeulen, a former veterinary nurse in Deventer, built PawPortal in Lovable — a small platform where independent pet-care providers keep client records, vaccination dates and visit notes. She had €950 left, a waiting list of eleven providers, and a plan to spend it across "security, payments, email and hosting."

The scoping call reordered that plan in ten minutes. PawPortal's Supabase tables had row-level security disabled entirely; every provider account could read every other provider's client records, including addresses and medical notes. Payments could wait — the eleven providers had all agreed to pay by bank transfer for the first quarter anyway, and email confirmations could be sent by hand at that volume. Spending €400 on a Stripe integration while the client records were readable across accounts would have been buying the wrong thing beautifully.

The engagement did one category thoroughly: row-level policies scoped to the provider that owns each record, the same rules enforced server-side rather than in the frontend routing, an exposed mapping API key moved behind a server route and rotated, and a nightly database dump to storage outside the primary provider, with one restore performed and documented.

**Result:** PawPortal launched with eleven paying providers three weeks later, invoicing manually, and funded a proper €2,400 payments-and-email engagement out of the first quarter's revenue rather than out of Sanne's savings.

> *"I came in wanting four things and left with one. Six months on, it was obviously the right one — the other three were things I could do by hand, and that one wasn't."*
> — **Sanne Vermeulen, Founder, PawPortal (Deventer)**

**Cost & Timeline:** €950 (Launch Ready Package, access control and secrets hardening) — live in 7 business days.

---

## Frequently Asked Questions

### Is €800 really the floor, or can a very small project cost less?

€800 is the floor for the Launch Ready package because below that the scoping, review and handover overhead exceeds the actual fix. If your project genuinely needs less than that, it usually means it needs nothing — a static site with no accounts and no data, which you can deploy yourself.

### If I can only afford one thing, should it be security or payments?

Security, in almost every case. A product that cannot take card payments can still take a bank transfer or an invoice for its first customers; a product that leaks one customer's data to another has no manual workaround and no way to undo it after the fact.

### Can I do the cheap parts myself and pay only for the hard parts?

Yes, and it genuinely reduces the bill. Writing down your access rules, deleting seed data, inventorying your API keys and making sure the deployed version is committed to your repository are all unbillable hours you can absorb, and they typically cut a scoping session in half.

### What happens if the review finds something that doesn't fit in my budget?

You get told before any work starts, with the finding described in plain language and a fixed price for closing it. The useful outcome of a small engagement is often the map: knowing that a schema change is coming lets you plan for it rather than discover it after launch.

### Does spending €1,000 now mean paying twice when I later need the bigger package?

No, provided the first engagement is scoped as a foundation rather than a patch. Access control implemented properly at the API layer is the thing a payments integration later builds on top of, so the work carries forward instead of being redone.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is €800 really the floor, or can a very small project cost less?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "€800 is the floor for the Launch Ready package because below that the scoping, review and handover overhead exceeds the actual fix. A project genuinely needing less usually needs nothing beyond a self-deployed static site with no accounts and no data."
      }
    },
    {
      "@type": "Question",
      "name": "If I can only afford one thing, should it be security or payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Security, in almost every case. A product that cannot take card payments can still invoice its first customers manually, while a product that leaks one customer's data to another has no manual workaround and no way to undo it afterwards."
      }
    },
    {
      "@type": "Question",
      "name": "Can I do the cheap parts myself and pay only for the hard parts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Writing down your access rules, deleting seed data, inventorying API keys and committing the deployed version to your repository are unbillable hours you can absorb, and they typically cut a scoping session in half."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if the review finds something that doesn't fit in my budget?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You are told before any work starts, with the finding described in plain language and a fixed price to close it. Knowing a schema change is coming lets you plan for it rather than discover it after launch."
      }
    },
    {
      "@type": "Question",
      "name": "Does spending €1,000 now mean paying twice when I later need the bigger package?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, provided the first engagement is scoped as a foundation rather than a patch. Access control implemented properly at the API layer is what a later payments integration builds on, so the work carries forward."
      }
    }
  ]
}
</script>
