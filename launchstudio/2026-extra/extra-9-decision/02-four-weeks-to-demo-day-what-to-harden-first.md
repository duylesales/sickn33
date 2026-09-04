---
Title: "Four Weeks to Demo Day: What to Harden First and What to Postpone"
Keywords: demo day preparation, four week hardening sprint, production readiness sprint, accelerator demo day, MVP triage before launch, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Four Weeks to Demo Day: What to Harden First and What to Postpone

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Four Weeks to Demo Day: What to Harden First and What to Postpone",
  "description": "A week-by-week triage plan for scale-up founders with a fixed demo date and a prototype that is not production-hardened. Covers what must be closed before strangers touch the product, and the seven categories that can safely wait until after the pitch.",
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
  "datePublished": "2027-01-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/four-weeks-to-demo-day-what-to-harden-first"
  }
}
</script>

Twenty-eight days. Not "a month or so" — twenty-eight days, of which roughly nineteen are working days, of which maybe fourteen survive contact with investor prep, deck rewrites and the three meetings your programme manager has already booked. That is the actual budget you are triaging against, and the first mistake most founders make is planning against the calendar month instead of the fourteen days.

The second mistake is bigger: treating demo day as a deadline for *features*. It isn't. Demo day is the first moment your product is touched, simultaneously, by people who did not build it, are not being careful, and in a few cases are actively curious about what happens if they poke it. That is a hardening deadline wearing a product deadline's clothes, and the triage looks completely different once you see it that way.

## What Demo Day Actually Tests

Your demo itself is rehearsed and safe. The risk sits in the ninety seconds after the QR code goes on screen and the hour after the pitch, when between forty and three hundred people open your product at once on a hotel guest network, sign up with disposable emails, and click things in an order you have never clicked them in.

Three things break in that window with boring regularity. First, concurrency: a prototype that has never had more than four simultaneous sessions meets two hundred, and the connection pool on a starter Postgres tier — often capped around 15 to 60 direct connections — saturates, so the product doesn't slow down, it errors. Second, the signup path: every flow your users normally reach *after* signing up gets exercised by someone who has just signed up, in a state your seeded test accounts never occupied. Third, the boundary: with hundreds of accounts created in ten minutes, the odds that two of them see each other's data stop being theoretical.

Notice what is not on that list. Nobody at demo day cares that your onboarding has three steps instead of two, or that the empty state is ugly. The gap between a demo that lands and a demo that becomes a story you have to explain to your lead investor is almost entirely infrastructural.

## The Triage Rule: Fix What a Stranger Can Reach

Here is the filter that makes the next four weeks decidable. **Rank every open item by whether an unknown person, acting normally or slightly abnormally, can reach it within their first ten minutes in your product.**

Anything in that zone is week-one work. Anything outside it — the admin tooling only you use, the reporting screen behind a paid plan nobody at demo day will have, the second integration — is postponable, no matter how loudly it is nagging at you.

This rule cuts against instinct, because the items nagging at a founder are usually the visible, half-finished ones. The ones that end demo days badly are invisible and feel finished. Apply the rule mechanically and it reorders your list within an hour.

## Week 1 — Audit, and the Two Decisions It Forces

Spend the first three days finding out what you actually have, not fixing anything. A code-level review of an AI-generated codebase — Lovable, Bolt, Cursor, or a mix — reliably surfaces the same categories: authorization enforced in frontend routing but not at the API, database policies missing or written as blanket `true` conditions, service keys shipped to the browser, payment webhooks accepted without signature verification, no rate limiting on anything, and a schema with no tenant column on tables that will eventually need one.

The audit's real output is not the list. It is two forced decisions.

**Decision one: is there a structural finding?** If the review says your data model has no concept of which organisation owns a row, you are not doing a four-week hardening sprint; you are doing a schema migration, and it will not fit alongside everything else. The correct response is to restrict demo day to a single-tenant demo environment and schedule the migration for after. Trying to migrate a schema in week three of a four-week sprint is how founders arrive at demo day with a half-migrated database and no rollback.

**Decision two: what are you demoing on?** Live production with real signups, or a controlled environment with pre-seeded accounts? Both are respectable. What is not respectable is discovering on the day that you meant one and built the other. Decide in week one, because it determines whether weeks two through four are about hardening a public surface or about making a controlled environment reliable.

## Week 2 — The Boundary Between Users

If you do one thing in four weeks, do this one. Week two is access control, and it has three layers that founders routinely conflate.

**Authentication** — proving who someone is — is usually the layer AI tools handle acceptably, because Supabase Auth, Auth0, Clerk and NextAuth do the hard parts. Verify the basics anyway: sessions expire, tokens are not stored somewhere a script can read them, password reset does not leak whether an address exists.

**Authorization** — deciding what that person may do — is where prototypes fail. The test is not clicking through the UI. It is taking an authenticated request for a resource you own, changing the ID in it to a resource belonging to another account, and sending it again. If the response contains data, you have found the finding. Do this for every resource type: records, uploads, exports, invoices, webhooks.

**Isolation** — making the boundary structural rather than conditional — is the durable version. Row-level security policies in Postgres, scoped to the authenticated user or their organisation, enforce the rule at the database rather than in application code you might forget to write next time. It is more work in week two and dramatically less work every week after.

Budget the whole week. Access control done in an afternoon is access control done for the paths you remembered.

## Week 3 — Money, Mail, and the Failure Paths

Week three is for the paths that only run when something goes right or badly wrong — and which therefore get tested least.

If you take payments at demo day, or expect to within days of it, the integration needs four properties, not one. Webhook signatures verified against your endpoint secret, so nobody can post a fake `checkout.session.completed` and provision themselves a plan. Idempotency, so Stripe or Mollie retrying a webhook — which they will — does not create a duplicate subscription. A plan state that lives in your database rather than being inferred from the last event you happened to receive. And a defined behaviour for a failed renewal that is not "user silently keeps full access forever."

Transactional email is the other week-three item, and it is the one that quietly ruins signup conversion. Sending from a domain with no SPF and DKIM records puts your verification emails in spam for a meaningful share of recipients — and at demo day, an email that arrives twenty minutes late is an email that arrives after the person has closed the tab. Configure the DNS records, send from a provider built for it (Postmark, Resend, SendGrid), and test delivery to Gmail, Outlook and one corporate domain, because those three behave differently.

Then spend a half-day on failure paths. What the user sees when a third-party call times out. Whether a failed upload leaves an orphaned row. Whether your error page reveals a stack trace with your database host in it. None of this is glamorous, and all of it is what a stranger meets first.

## Week 4 — Freeze, Rehearse, Instrument

Week four contains no new work. That is not a suggestion; it is the whole point of week four.

**Freeze features on day one of the week.** Every demo-day disaster story with a technical cause traces back to a change shipped inside seventy-two hours of the pitch, usually a small one, usually one that "couldn't break anything."

**Rehearse under load.** Not a formal load test — a coordinated one. Get twenty people, ideally on their phones on mobile data, to sign up and use the product inside the same three minutes. You will learn more from that than from any tool, and you will learn it in time to raise your connection pool limit, add a connection pooler, or move a synchronous email send onto a queue.

**Instrument what you cannot watch.** Error tracking with alerts to a phone, an uptime check on the signup endpoint specifically rather than the homepage, and a log you can actually read during the event. The failure you want is one you notice at 14:02 and fix at 14:20, not one an investor mentions on a call three days later.

**Write the rollback down.** One page: how to revert the deployment, who has the credentials, what the database restore procedure is. Under adrenaline, nobody remembers.

## The Postpone List

Seven things that feel urgent and are not, in a four-week window: a formal penetration test; SOC 2 or ISO 27001 preparation; multi-region redundancy; a full analytics and attribution stack; performance optimisation for traffic you haven't had; the second and third payment methods; and the admin dashboard you keep meaning to build for yourself.

Every one of these has a right moment. None of those moments is now. The way to postpone honestly is to write each with a trigger beside it — "pen test when the first enterprise procurement asks," "SOC 2 when a deal over €25k depends on it" — so that postponing is a scheduled decision rather than an unspoken hope.

## If You Only Have Two Weeks

Because plenty of founders read this with fourteen days left, here is the compressed version. Days one to three: audit, and accept its structural verdict. Days four to nine: access control at the API layer, nothing else. Days ten to eleven: email deliverability and the top three failure paths. Day twelve: freeze. Days thirteen and fourteen: rehearse with twenty real humans, and instrument.

At two weeks you are explicitly choosing to postpone payments. Take a waiting list, an invoice, or a manual Stripe payment link at demo day instead. Nobody in the audience will notice; a duplicate-subscription bug in front of them, they would.

Behind LaunchStudio is Manifera's team of 120+ seasoned engineers, whose [portfolio of delivered production systems](https://www.manifera.com/portfolio/) is precisely why a four-week window is a scoping conversation rather than a gamble — 1–3 week fixed-price delivery exists for exactly this shape of deadline.

Four weeks is enough for the boundary, the money path and a rehearsal — it is not enough for everything, and the founders who land demo day are the ones who chose. [Book a 15-minute intro call](https://launchstudio.eu/en/#contact) and you will leave it with a dated list of what fits in your remaining fourteen working days.

## Real example

### A Scale-Up Founder in Action: The Week-Three Freeze That Saved the Pitch

Joris Bakhuizen, founder of Stagelijn, a shift-planning SaaS for hospitality groups, went into an Amsterdam accelerator's demo day with a Bolt-built product, four paying pilot venues and twenty-six days on the clock. His plan was to spend all four weeks adding a payroll-export feature an investor had mentioned liking.

The week-one audit reordered the plan against his instincts. Stagelijn's API returned any shift record by ID without checking which venue the requesting account belonged to — invisible in the UI, trivially reachable by anyone who changed a number in a URL. With four venues that was a latent problem; with two hundred demo-day signups it was a live one. The payroll export, meanwhile, was a feature nobody in the room would click.

Weeks two and three went to venue-scoped authorization enforced with row-level policies in Postgres, SPF and DKIM records so verification emails stopped landing in Outlook's junk folder, and a queue for the synchronous email send that had been holding a database connection open for eight seconds per signup. Week four was a hard freeze and a rehearsal with twenty-two people from the accelerator's other cohorts hitting signup at once — which surfaced a connection-pool ceiling at around forty concurrent sessions, fixed with a pooler two days before the pitch.

**Result:** 214 signups in the ninety minutes after Stagelijn's pitch, no errors, no cross-venue data exposure, and two term-sheet conversations. The payroll export shipped five weeks later, once an actual customer asked for it.

> *"I was going to spend my last month building a feature for one person in the audience. I spent it on the part two hundred people were about to touch instead."*
> — **Joris Bakhuizen, Founder, Stagelijn (Amsterdam)**

**Cost & Timeline:** €4,200 (Launch & Grow Package, authorization, email deliverability and load readiness) — delivered in 15 business days.

---

## Frequently Asked Questions

### Should I demo on live production or a controlled environment?

Either is defensible, but decide in week one, because it changes everything downstream. A controlled environment with pre-seeded accounts removes the concurrency and signup-path risk entirely, at the cost of not capturing real signups in the room — which for many pitches is a reasonable trade.

### Can a four-week sprint include a database schema migration?

Almost never safely. A migration that touches ownership or tenancy needs its own window with a tested rollback, and squeezing it in beside hardening work is the most common way founders arrive at demo day in a half-migrated state with no clean way back.

### How do I know whether my product will survive two hundred simultaneous signups?

Rehearse it rather than reason about it. Twenty real people on mobile data signing up inside three minutes will expose connection-pool limits, synchronous email blocking and rate-limit issues far more reliably than any estimate, and it leaves you time to fix what it finds.

### Is it acceptable to demo without working payments?

Yes, and it is often the better call at four weeks or less. A payment link, an invoice or a waiting list is invisible to an audience, whereas a webhook bug that double-charges someone during your pitch is not.

### What should I do with the audit findings I don't have time to fix?

Write each one down with the trigger that will force it — a user count, a deal size, a compliance request — and share that list with your investors rather than hiding it. A founder who can name their remaining technical debt precisely reads as more competent than one who claims there is none.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I demo on live production or a controlled environment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Either is defensible, but decide in week one because it changes everything downstream. A controlled environment with pre-seeded accounts removes concurrency and signup-path risk at the cost of not capturing live signups in the room."
      }
    },
    {
      "@type": "Question",
      "name": "Can a four-week sprint include a database schema migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost never safely. A migration touching ownership or tenancy needs its own window with a tested rollback, and squeezing it beside hardening work is how founders reach demo day half-migrated with no clean way back."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know whether my product will survive two hundred simultaneous signups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rehearse rather than reason. Twenty real people on mobile data signing up within three minutes will expose connection-pool limits, blocking email sends and rate-limit issues in time to fix them."
      }
    },
    {
      "@type": "Question",
      "name": "Is it acceptable to demo without working payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and often the better call at four weeks or less. A payment link, invoice or waiting list is invisible to an audience, while a webhook bug that double-charges someone during the pitch is not."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do with the audit findings I don't have time to fix?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Write each one down with the trigger that will force it — a user count, a deal size, a compliance request — and share the list with investors. Naming your technical debt precisely reads as more competent than claiming there is none."
      }
    }
  ]
}
</script>
