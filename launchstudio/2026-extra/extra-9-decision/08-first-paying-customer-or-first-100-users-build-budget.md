---
Title: "First Paying Customer or First 100 Users: Which Should Shape Your Build Budget"
Keywords: build budget priorities, first paying customer vs users, SaaS launch budget, self-serve vs sales led, scoping a launch engagement, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# First Paying Customer or First 100 Users: Which Should Shape Your Build Budget

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "First Paying Customer or First 100 Users: Which Should Shape Your Build Budget",
  "description": "One paying customer and one hundred free users demand almost entirely different engineering, and budgeting for both at once is how scale-up founders overspend. A side-by-side breakdown of the two build budgets, where they overlap, and the sequence that costs least.",
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
  "datePublished": "2027-01-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/first-paying-customer-or-first-100-users-build-budget"
  }
}
</script>

There's a belief buried in most launch budgets that nobody says out loud: that one paying customer and a hundred users are the same destination at different distances — that you build the product, and then whichever arrives first, arrives first.

They are not the same destination. They demand different engineering, in different order, at meaningfully different prices, and the founders who overspend at this stage are almost always the ones who budgeted for both because they hadn't decided which they were chasing. Scoping for one and getting the other is recoverable in a fortnight. Scoping for both simultaneously typically adds 40–60% to an engagement and delays it by weeks, in exchange for capability that half of it will sit unused for a year.

## Two Goals, Two Completely Different Load Profiles

Strip both goals down to what they actually impose on a system.

**One paying customer** is a *depth* problem. Low volume, high consequence. One organisation, maybe five to fifty named users you can provision by hand, on a network you can identify, using the product in ways you can observe directly. Nothing about it stresses capacity. Everything about it stresses correctness: money must move accurately, their data must be provably separated from anyone else's, and a mistake is not a metric, it is a phone call with a person who has your invoice on their desk.

**One hundred users** is a *breadth* problem. Higher volume, lower per-user consequence, but an enormously wider surface. A hundred strangers means a hundred signups you didn't perform, a hundred inboxes your verification emails must reach, a hundred password resets, a hundred people clicking things in an order you never anticipated, some percentage of them bots, and a support load you cannot answer individually.

Same product. Almost no overlap in what makes it ready.

## Path A: The Budget for One Paying Customer

If your first goal is a signed contract, the money goes here:

**The boundary, done thoroughly** (typically the +€500 security work). Server-side authorization on every route, with ownership enforced at the database rather than in application handlers. For a B2B customer this isn't hygiene — it's a procurement question you will be asked directly.

**Billing depth, not billing breadth.** You need one payment method to work perfectly, not four to work adequately. Often you need none at all: an invoice on thirty-day terms is what most EU B2B buyers prefer anyway. When you do integrate, the money is in state — webhook signature verification, idempotency so a redelivered event doesn't double-provision, a plan state stored in your own database, defined behaviour for a failed renewal.

**The paperwork surface.** A processing agreement, a subprocessor list, a stated hosting region, a data export they can run. Cheap to produce, and it blocks signature if absent.

**Continuity.** Backups with a restore you have performed, and an uptime check on the two or three endpoints that matter to this one customer.

Explicitly *not* in Path A: self-serve signup, email deliverability at volume, rate limiting, abuse prevention, a support ticketing system, analytics infrastructure. You provision accounts by hand and you answer their emails yourself.

Realistic shape: €1,500–€3,000 in the Launch Ready band, delivered in one to two weeks.

## Path B: The Budget for One Hundred Users

If your first goal is a hundred people using the product, the money goes somewhere almost entirely different:

**Signup as a hardened surface.** Email verification, protection against automated registration, sensible session handling, and a password reset that doesn't leak whether an address exists. Every one of these is unnecessary when you create accounts manually and unavoidable when strangers do.

**Email deliverability, treated as infrastructure.** SPF, DKIM and DMARC records on your domain; a transactional provider like Postmark or Resend rather than SMTP from your app server; and delivery tested against Gmail, Outlook and at least one corporate domain, because they behave differently. Founders discount this constantly and it is arithmetic: if 15% of verification emails land in spam, you didn't get a hundred users, you got eighty-five and a mystery.

**Rate limiting and abuse handling.** A public signup form is a public endpoint. Without limits you will get automated registrations, and if your product sends email or calls a paid API on a user's behalf, those registrations have a euro cost attached.

**Capacity that survives a spike.** A hundred users rarely arrive evenly. They arrive because you posted somewhere, which means forty of them arrive in ten minutes. Connection pooling, a queue for anything slow in the request path, and a host tier that doesn't fall over are the difference between a launch and a screenshot of an error page.

**Observation at volume.** Per-user event logging and error tracking, because with a hundred users you cannot watch individuals — you need aggregates to know that eleven people abandoned onboarding at step three.

Explicitly *not* in Path B: subscription billing depth, dunning, refunds, processing agreements, enterprise access-control granularity.

Realistic shape: €3,000–€5,000, and often into the Launch & Grow band because the €49/month monitoring and managed hosting layer is genuinely load-bearing here in a way it isn't for one customer.

## The Forty Percent That's Shared

Both paths sit on the same floor, and it is worth knowing exactly what it is so you don't pay for it twice.

Server-side authorization on every route. Secrets out of the browser. SSL on your own domain. A deployment you can repeat and roll back. Backups with a tested restore. Error tracking.

That's roughly 40% of either budget, and it's the part that carries forward regardless of which direction you go afterwards. Which means the sequencing question isn't "which path do I buy" so much as "I buy the floor, plus one path's worth of depth" — and the second path, when you need it, costs its own increment rather than the whole thing again.

## The Cost of Choosing Wrong

**Building for a hundred users and getting one paying customer** is the more common error, and it wastes real money: a signup flow nobody self-serves through, deliverability work for emails you could have sent by hand, rate limiting against traffic that never came. Typically €1,500–€2,500 of premature capability. Recoverable — none of it is wrong, it's just early — but it was spent instead of being spent on the processing agreement and payment-state work your one customer actually asked for, and it delayed their signature by three weeks.

**Building for one paying customer and getting a hundred users** fails louder and faster. You post somewhere, forty people try to sign up in ten minutes, and there's no self-serve signup, so you're creating accounts by hand at midnight; the verification emails you cobbled together land in spam; your starter database tier saturates its connection limit and starts erroring. The financial waste is smaller. The reputational cost of a hundred people meeting a broken first impression is not, because that audience does not come back for the second launch.

Neither error is fatal. Both are avoidable by naming the target before scoping.

## What Each Goal Actually Buys You in Evidence

Worth being clear-eyed about, because founders often chase a hundred users for reasons that don't survive examination.

A hundred free users tells you about *interest and activation*: whether people understand your value proposition, where onboarding loses them, which feature they open first. It tells you almost nothing about willingness to pay, and a startling number of scale-up founders have discovered that a thousand engaged free users converted at under 1%.

One paying customer tells you about *value and price*: that this problem is worth money to someone, roughly how much, and what a buyer needs before money moves — including all the procurement and compliance requirements you will meet again with every subsequent customer.

For a fundraising conversation, one paying B2B customer at €400 a month is generally a stronger artefact than a hundred free users, because it proves something harder. For a product-led consumer or prosumer tool where the eventual model is self-serve, the hundred users genuinely are the right target — the activation data is the thing you can't get any other way.

## The Sequence That Costs Least

For the majority of B2B SaaS at this stage, one order dominates: **paying customer first, hundred users second.**

The reasons are financial rather than philosophical. The paying-customer path is cheaper (€1,500–€3,000 against €3,000–€5,000). It is faster to deliver, because there's less of it. It generates cash that can fund the second phase. And crucially, the work is additive — the boundary, the deployment, the backups all carry forward, so going on to build the self-serve surface later costs its own increment and nothing extra.

Do it the other way and the paying customer's requirements — processing agreement, payment state, access granularity — arrive as a second engagement anyway, and they arrive under time pressure, because there's a contract waiting on them.

The exception is genuine: if your product is inherently self-serve, priced at €12 a month, with no procurement process to satisfy, then the hundred-user path *is* the paying-customer path, and Path B is simply your Path A. Know which of these you are. The mistake is being a B2B company that budgets like a consumer one.

Behind the fixed price is Manifera, a software company that has spent eleven years watching which early architectural choices survive growth and which quietly don't — the [record of delivered systems](https://www.manifera.com/portfolio/) is what makes the "buy the floor, add one path" advice specific rather than theoretical.

Two goals, two budgets, one shared floor — and pricing them separately usually reveals a gap of a few thousand euros that nobody had noticed they were about to spend. [Price both paths side by side in the calculator](https://launchstudio.eu/en/#calculator) before you commit to either.

## Real example

### A Scale-Up Founder in Action: The Signup Flow That Never Got Used

Wouter Lansink ran Kaliber, a Nijmegen-built quality-inspection SaaS for metal fabrication workshops, made in Bolt and running as a free beta. He arrived with a €5,400 scope covering self-serve signup, email verification, rate limiting, a Stripe subscription integration and analytics — a hundred-user launch budget, assembled because a hundred users was the number in his head from an accelerator dashboard.

The scoping call started with a different question: who has actually said they would pay? The answer was two fabrication workshops, one of which had already sent a procurement questionnaire asking where data was hosted and whether Kaliber could sign a processing agreement. Nobody was waiting to self-serve. Kaliber's buyers were operations managers who bought by purchase order and expected an invoice.

The scope was rebuilt as Path A plus the shared floor. Workshop-scoped authorization enforced with row-level policies rather than route handlers, inspection photos moved from guessable public storage paths to signed URLs, a nightly backup with a restore Wouter performed himself, uptime checks on login and report submission, and a documented data export. No self-serve signup, no Stripe, no rate limiting. €2,650 instead of €5,400, and the accounts for both workshops' twenty-three users were created by hand in under an hour.

**Result:** Both workshops signed within five weeks, at €480 a month each, invoiced quarterly. Kaliber added self-serve signup, deliverability configuration and Stripe eleven months later, funded from revenue — and by then Wouter knew from customer conversations that the self-serve tier needed a different price point than the one he'd have built in month one.

> *"I'd budgeted for a hundred strangers and I had two buyers with purchase orders. Half of what I was about to build was for an audience I hadn't met yet."*
> — **Wouter Lansink, Founder, Kaliber (Nijmegen)**

**Cost & Timeline:** €2,650 (Launch Ready Package, workshop-scoped authorization, storage isolation and continuity) — live in 10 business days.

---

## Frequently Asked Questions

### Can I budget for both goals at once if I can afford it?

You can, but it typically adds 40–60% to the engagement and several weeks to delivery, in exchange for capability that half of it will sit unused. The stronger version of the same spend is to buy the shared floor plus one path now, and add the second path later as its own increment.

### Is one paying customer really better evidence than a hundred free users?

For B2B, generally yes, because it proves willingness to pay rather than willingness to try, and it surfaces the procurement and compliance requirements every subsequent buyer will also raise. For a genuinely self-serve product at a low price point, the activation data from a hundred users is the harder thing to obtain and the more valuable.

### What exactly is the shared floor between the two budgets?

Server-side authorization on every route, secrets kept out of the browser, SSL on your own domain, a repeatable deployment with rollback, backups with a tested restore, and error tracking. It is roughly 40% of either budget and it carries forward whichever direction you take afterwards.

### Why is email deliverability a hundred-user problem rather than a one-customer problem?

With one customer you can provision accounts and send onboarding messages by hand from your own inbox. With a hundred strangers, unverified sending domains mean a share of verification emails land in spam, and every one of those is a signup that silently fails without generating any error you can see.

### If I get a hundred users unexpectedly after scoping for one customer, how bad is it?

Uncomfortable but recoverable in one to two weeks, since the shared floor is already in place and what's missing is the self-serve surface. The real cost is reputational: a hundred people meeting a broken signup rarely return for a second attempt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I budget for both goals at once if I can afford it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can, but it typically adds 40-60% to the engagement and several weeks to delivery for capability that will sit unused. Buying the shared floor plus one path now, and adding the second later as its own increment, is the stronger version of the same spend."
      }
    },
    {
      "@type": "Question",
      "name": "Is one paying customer really better evidence than a hundred free users?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For B2B, generally yes, because it proves willingness to pay and surfaces the procurement requirements every later buyer will also raise. For genuinely self-serve products at low price points, activation data from a hundred users is more valuable."
      }
    },
    {
      "@type": "Question",
      "name": "What exactly is the shared floor between the two budgets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Server-side authorization on every route, secrets out of the browser, SSL on your own domain, a repeatable deployment with rollback, backups with a tested restore, and error tracking — roughly 40% of either budget."
      }
    },
    {
      "@type": "Question",
      "name": "Why is email deliverability a hundred-user problem rather than a one-customer problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "With one customer you provision accounts and send onboarding by hand. With a hundred strangers, unverified sending domains put a share of verification emails in spam, and each is a signup that fails without any visible error."
      }
    },
    {
      "@type": "Question",
      "name": "If I get a hundred users unexpectedly after scoping for one customer, how bad is it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uncomfortable but recoverable in one to two weeks, since the shared floor is in place and only the self-serve surface is missing. The real cost is reputational, as a hundred people meeting a broken signup rarely return."
      }
    }
  ]
}
</script>
