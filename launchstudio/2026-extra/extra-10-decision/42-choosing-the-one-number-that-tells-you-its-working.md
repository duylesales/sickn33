---
Title: "Choosing the One Number That Tells You It's Working"
Keywords: north star metric, one metric that matters, vanity metrics SaaS, SaaS success metric, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Choosing the One Number That Tells You It's Working

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing the One Number That Tells You It's Working",
  "description": "A decision framework for picking the single metric that would actually change a SaaS founder's behaviour, and for recognising the vanity metrics on the same dashboard that never will. Helps founders cut a crowded dashboard down to the number worth acting on.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/choosing-the-one-number-that-tells-you-its-working" }
}
</script>

Most SaaS dashboards are a museum, not an instrument. Thirty metrics, four charts nobody scrolls to, a "engagement score" someone built once and never revisited, and a weekly ritual of glancing at all of it and feeling roughly the same regardless of what the numbers say. That's the uncomfortable claim worth sitting with: a dashboard full of metrics that don't change what you do on Monday morning is decoration, not decision support — and most founders have one.

This isn't an argument for measuring less broadly across the business. It's an argument for identifying, out of everything you track, the single number that would actually alter your next move if it moved, and treating every other metric as context around that one. Founders who skip this step don't lack data. They lack the discipline to admit that most of their data doesn't matter yet.

## The Test That Eliminates Almost Everything

There's one question that does the sorting: **if this number moved 20% in either direction next week, would you do something differently?** Not "would you notice." Not "would it be interesting." Would you actually change a decision — reprioritise the roadmap, pause a spend, call a customer, delay a launch.

Run your current dashboard through that test, metric by metric, and watch how much falls away. Total registered users: interesting, rarely actionable on its own, because it doesn't distinguish someone who tried your product once from someone using it daily. Page views: almost never actionable for a SaaS product, because a page view proves someone's browser loaded something, not that they got value. Social media followers, app store rating, press mentions: real, sometimes useful for other purposes, but they fail the test for "is the product working," because none of them move in response to anything you'd do differently inside the product itself.

What survives the test is usually smaller and less flattering than the dashboard suggests. That's the point.

## Why MRR Alone Fails the Test, Even Though It Matters

This one trips up founders because MRR obviously matters — it's revenue, it pays the bills, investors ask for it. But as *the one number*, it fails the actionability test for a specific reason: it's a lagging composite of several things happening upstream (new signups, activation, conversion, churn, expansion) blended into a single figure that moves for reasons you can't immediately diagnose. MRR dropped 8% this month — was it churn, a failed renewal batch, a slow sales month, or a pricing change working through the base? You can't tell from the number alone, which means it can't directly tell you what to do differently, only that something needs investigating.

Treat MRR as the scoreboard, not the instrument panel. It tells you whether you're winning. The one number you pick should tell you *why*, early enough to act before the scoreboard reflects it.

Run the arithmetic on why "early enough" matters. If your one number is an activation proxy measured in the first week, a drop shows up in your dashboard roughly thirty days before it shows up as a dent in MRR, because that's how long it typically takes new-customer weakness to work its way through trial periods, first invoices and first-month churn. Thirty days is the difference between catching a broken onboarding flow before it costs you a cohort and explaining a bad quarter after the fact.

## Other Common Candidates That Also Fail the Test

MRR isn't the only metric that feels obviously important and still fails the actionability test. Total customer count fails it for the same reason MAU does for consumer apps — it doesn't distinguish an account that's thriving from one quietly circling the drain toward cancellation. Net Promoter Score fails it operationally for most early-stage SaaS teams, not because the underlying sentiment is meaningless, but because a single quarterly survey rarely arrives fast enough, or with enough respondents, to change a specific decision this month. Support ticket volume fails it in the opposite direction: it changes constantly, but rising tickets can mean either a broken feature or growing usage, and without a second signal you can't tell which.

None of these are useless — they're worth watching as secondary context. They just can't carry the weight of being *the* number, because none of them, on their own, tells you what to do next Monday.

## Finding Your One Number: Work Backward From the Decision

The reliable method is to work backward from the action, not forward from the data you happen to have. Ask: what is the earliest reliable signal that a customer is going to stick around and eventually pay (or expand)? That signal, made countable, is usually your candidate.

For a project-management SaaS tool, that might be "teams that create three or more projects in their first week" — because internal data (yours, once you have enough of it) shows that threshold correlates strongly with month-three retention. For a scheduling tool for small clinics, it might be "clinics with a completed booking cycle within 48 hours of signup." For a usage-metered API product, it's often "accounts that make a successful call within the first session," because a signup that never calls the API has learned nothing about whether your product solves their problem.

Notice what these have in common: each is a specific, countable action tied to a specific, short timeframe, chosen because it predicts an outcome you actually care about (retention, expansion, revenue) earlier than that outcome itself would show up. This is the same idea behind defining a genuine activation moment, and the two decisions often converge on the same event — which is a good sign, not a coincidence.

If you genuinely don't know which early action predicts retention, that itself is the answer to what to work on first: instrument three or four candidate actions, wait six to eight weeks, and see which one actually correlates with the customers who are still there in month three. Guessing without checking is how founders end up optimising for an action that feels important and predicts nothing.

## Different Products, Different One Numbers

There's no universal answer, and pretending otherwise is how founders end up copying a metric from a blog post that fits nobody's actual business. A two-sided marketplace's one number is often the number of completed transactions between new supply and new demand in the first week — not signups on either side, because a marketplace with unmatched supply and demand is failing regardless of how many people registered. A subscription SaaS tool typically lands on weekly active accounts performing the core action, not weekly logins, because a login without action is browsing, not usage. A usage-based product often does best with a consumption metric — API calls, documents processed, minutes transcribed — tracked per account against a floor that predicts churn if crossed.

The wrong move is treating "monthly active users" as a safe default because it sounds standard. MAU is a fine health metric for a consumer app used casually; for a B2B SaaS tool used by a handful of people at each account, it can mask a real problem, because ten accounts logging in daily looks identical on a MAU chart to two accounts logging in heavily and eight barely opening the app at all.

## What Actually Changes Once You Have It

The practical shift is smaller than it sounds and more disruptive than founders expect. It means your weekly team check-in opens with that one number, not a tour of the dashboard. It means a feature request gets weighed partly by whether shipping it would plausibly move that number, not just whether a customer asked loudly. It means a marketing spend gets judged by whether it brought in users who eventually hit that number, not just users who signed up.

It also means saying no to metrics that used to feel important. A founder who's spent a year reporting MAU to a board can feel exposed switching to a smaller, more specific number — it looks like admitting the old metric didn't mean much. It didn't. Better to say so at €20k MRR than at €200k MRR, when the wrong number has shaped two years of roadmap decisions instead of six months.

Put the number somewhere unavoidable — the top of the shared dashboard, the first line of the weekly Slack update, the whiteboard in the room where planning happens. A metric that lives three tabs deep in an analytics tool nobody opens voluntarily doesn't function as a steering number regardless of how well-chosen it is. The founders who get real value from this exercise are the ones who make the number annoying to ignore, not just technically available.

## When the One Number Should Change

It isn't permanent. Early on, your one number is usually an activation proxy, because the biggest risk is that people try the product and get nothing from it. Once activation is reliably above the level you'd expect and stable, the constraint typically moves — to retention, then to expansion revenue, then eventually to something like net revenue retention once you have enough paying accounts for that to be statistically meaningful rather than noisy. Revisit the choice roughly every time you clear a growth stage (first ten paying customers, first product-market-fit signal, first sales hire), not on a fixed calendar — the number should track your actual bottleneck, and the bottleneck moves.

## The Common Mistake: Picking a Number You Can't Yet See Clearly

None of this works if the underlying event isn't instrumented, which is why this decision has to follow, not precede, the instrumentation work covered elsewhere in this series. A founder who picks "teams that complete onboarding" as their one number but has never defined what "complete onboarding" means as a tracked event is picking a metric on faith. Define the event first, confirm it fires correctly, watch it for a few weeks to see the baseline, and only then commit to it as the number the team steers by.

LaunchStudio is powered by Manifera, whose engineers have spent 11+ years building the measurement layer underneath products at very different scales — which is usually the difference between a founder who can name their one number in a sentence and one who points at a dashboard and shrugs. If your product's instrumentation isn't solid enough to trust the number you'd pick, [talk to an engineer who can tell you what's actually being measured](https://launchstudio.eu/en/#contact) before you build a habit around a number that's quietly wrong.

## Real example

### A Scale-Up That Was Reporting the Wrong Win

Lars Bakker ran Ordis, a small SaaS tool helping independent contractors manage quotes and invoices, sitting at roughly €14,000 MRR with steady but unspectacular growth. His investor updates led with monthly signups, which had been climbing nicely for two quarters — 340, then 410, then 480. Morale was good. Growth "looked" real.

A closer look at activation data told a different story: of those 480 signups, only 61 had sent a single invoice through the product within their first two weeks, and that ratio had actually been falling as signups rose, because a recent ad campaign was bringing in curious browsers rather than contractors with an immediate invoicing need. Signups were up. The number that predicted revenue was quietly down.

Lars switched the team's weekly number to "accounts sending their first invoice within 14 days of signup" and reallocated the ad spend that had been inflating raw signups toward a referral channel that converted at nearly triple the rate on that metric, even though it produced fewer total signups per euro.

**Result:** within two months, first-invoice conversion rose from 12.7% to 21%, and MRR growth — the scoreboard metric — accelerated for the first time in a quarter, driven by a smaller but sharper top of funnel.

> "We were celebrating a number that had stopped meaning anything. Once we switched to the one that actually predicted a paying customer, half our roadmap arguments just disappeared."
> — **Lars Bakker, Founder, Ordis**

**Cost & Timeline:** metric redefinition and instrumentation review completed in one week alongside an existing Launch & Grow engagement.

## Frequently Asked Questions

### Is it wrong to track more than one metric at all?

No — most teams track a handful for full context. The point is that only one should function as the number the whole team is steered by in a given period; the rest are supporting context, not competing headlines.

### What if my one number and my board's expected metric (like MRR) don't match?

Report both. MRR is still the scoreboard investors care about; your one number is the instrument panel that explains why the scoreboard is moving the way it is, and a good board update uses the second to explain the first.

### How long should I wait before trusting a candidate metric?

Generally six to eight weeks of data with a reasonable sample size, long enough to see a few cohorts move through it. Committing to a number after two weeks of data risks steering the whole team based on noise.

### Can a marketing-driven vanity metric like "downloads" ever be the right one number?

Only if downloads reliably predict something you care about downstream, which is rare — most download-heavy products still need a second, in-product action to confirm the download turned into real usage. Treat raw download counts as a funnel-entry stat, not the metric you steer by.

### Do B2C and B2B SaaS products pick this metric differently?

Yes, mainly in timeframe and unit. B2C metrics often look at individual user behaviour within days; B2B metrics more often look at account-level behaviour (multiple seats, a completed workflow) within a slightly longer window, because B2B adoption typically involves more than one person before it sticks.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is it wrong to track more than one metric at all?", "acceptedAnswer": { "@type": "Answer", "text": "No, most teams track a handful for context. Only one should function as the number the whole team steers by in a given period; the rest support it rather than compete with it." } },
    { "@type": "Question", "name": "What if my one number and my board's expected metric (like MRR) don't match?", "acceptedAnswer": { "@type": "Answer", "text": "Report both. MRR remains the scoreboard investors care about, while your one number is the instrument panel that explains why the scoreboard is moving." } },
    { "@type": "Question", "name": "How long should I wait before trusting a candidate metric?", "acceptedAnswer": { "@type": "Answer", "text": "Generally six to eight weeks of data, long enough to see a few cohorts move through it. Committing after two weeks risks steering the team based on noise." } },
    { "@type": "Question", "name": "Can a marketing-driven vanity metric like 'downloads' ever be the right one number?", "acceptedAnswer": { "@type": "Answer", "text": "Only if downloads reliably predict something further downstream, which is rare. Most download-heavy products still need an in-product action to confirm real usage, so treat downloads as a funnel-entry stat rather than the metric to steer by." } },
    { "@type": "Question", "name": "Do B2C and B2B SaaS products pick this metric differently?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, mainly in timeframe and unit. B2C metrics often track individual behaviour within days, while B2B metrics more often track account-level behaviour over a slightly longer window, since adoption usually involves more than one person before it sticks." } }
  ]
}
</script>
