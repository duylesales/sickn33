---
Title: "What to Do When Your Cloud Bill Doubles"
Keywords: cloud bill spike saas, egress costs surprise, serverless function cost, database compute pricing, cost per customer unit economics, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# What to Do When Your Cloud Bill Doubles

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What to Do When Your Cloud Bill Doubles",
  "description": "Infrastructure costs rarely rise smoothly: they jump, usually because of something inefficient rather than something successful. How to find out where the money is going, the usual culprits in AI-built products, and what to know before optimising anything.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-to-do-when-your-cloud-bill-doubles" }
}
</script>

A bill that goes from €180 to €390 in a month is alarming in a specific way: it is not enough money to be a crisis, and it is enough to suggest that at ten times the customers it would be a serious problem. The instinct is to start optimising immediately. The better first move is to find out what actually changed, because in most cases the increase is not proportional to growth — it is one inefficient thing that has crossed a threshold.

That distinction matters commercially. Costs that scale with customers are a pricing question. Costs that scale with a bug are an engineering question, and treating the second as the first leads founders to raise prices or worry about unit economics when they should be fixing a query.

## Find Out Where It Went Before Changing Anything

Every provider offers a cost breakdown by service, and reading it carefully answers most of the question in twenty minutes.

Look for three things. **Which line grew**, in absolute terms rather than percentage — a service that tripled from €4 is not the story. **When it grew**, since a step change on a particular date points at a deployment or a new customer, while a gradual rise suggests genuine growth. **Whether usage or price changed**, because providers do adjust pricing and free tiers.

Then compare against a number that actually matters: cost per active customer. A bill that doubled while customers doubled is fine and possibly good. A bill that doubled while customers grew 10% is a problem with a cause. Founders who track only the total react to the wrong signal in both directions — panicking at healthy growth, and missing genuine waste hidden by it.

## The Usual Culprits

Infrastructure costs concentrate in a small number of places, and in products built quickly the same items appear repeatedly.

**Database compute, driven by inefficient queries.** The most common cause by a wide margin. A query without an index that was imperceptible at 1,000 rows becomes the dominant workload at 500,000, and managed database pricing follows compute. This is why cost spikes so often coincide with the arrival of one large customer.

**Data transfer out.** Egress is charged, often at rates that surprise people, and it is where products serving images, files, or exports accumulate cost invisibly. Serving user-uploaded images at full resolution to every page view is the classic version.

**Storage that only grows.** Uploads, generated files, exports, logs, and backups accumulate because nothing deletes them. Storage is cheap per gigabyte and unbounded growth is not, and this is where a retention policy pays for itself directly.

**Function invocations and duration.** Serverless pricing multiplies calls by time by memory. A function called on every page load, running longer than necessary, or provisioned with far more memory than it uses, produces a bill that seems disconnected from traffic.

**Background jobs running more often than needed.** A job polling every minute that could run every fifteen costs fifteen times as much for no benefit.

**Logging.** Verbose logging at scale is a genuine line item, and logs retained indefinitely compound it.

**Idle non-production environments.** Staging and preview environments left running at production sizing, doing nothing, at full cost.

## Optimise the Largest Line, Not the Easiest

With a breakdown in hand, the discipline is to work on the biggest number rather than the most tractable one. It is common to spend a day shaving 30% off a €12 line while a €200 line goes unexamined because it looks harder.

Three moves cover most situations, roughly in order of return.

**Add the missing index.** Database cost driven by a slow query is usually resolved by an index, and the improvement is often an order of magnitude. Providers expose slow query logs; the top three queries typically account for most of the load.

**Stop transferring what you do not need to.** Serve appropriately sized images rather than originals, put a CDN in front of static assets, and make sure exports are not being regenerated on every view.

**Delete what is no longer needed.** Apply retention to logs, generated files, and old exports. This is the least interesting and frequently the largest single reduction available.

Two things to avoid. Do not move providers to save money before understanding the cause — the same inefficient query costs money everywhere. And do not spend engineering time worth more than the saving: a day of work to save €15 a month is a poor trade at any stage, and the time is usually better spent on the product.

Identifying which query, transfer, or job is responsible, and fixing it properly, is ordinary production engineering with an unusually direct payback. LaunchStudio, backed by Manifera's 11+ years of production engineering, performs cost and performance reviews on AI-built products, where a small number of inefficient paths typically account for most of the bill. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Ceilings So It Cannot Happen Overnight

Some cost increases arrive over months and some arrive over a weekend. The second kind needs a hard stop rather than a review.

Any feature calling a metered third-party service — an AI model, an SMS gateway, a mapping API — needs limits enforced in your own code: per account, and globally per day. Provider budget alerts notify after money has been spent and often hours late; the control that actually protects you is your product declining to make the call.

Add spend alerts at meaningful thresholds and, more usefully, an alert on daily rate rather than monthly total, since a monthly threshold is reached after the damage. And close the obvious doors: nothing expensive should be reachable without authentication, and rate limits should apply to anything a script could call in a loop.

The single most valuable number to know is your cost per active customer. It converts every subsequent question — can I afford this feature, is this customer profitable, should I raise prices — from a guess into arithmetic.

## Real example

### One Customer, One Missing Index, €430

Marek Novotny ran Inzichtbord, a reporting dashboard for logistics companies, built in Lovable and hosted on a managed platform. Costs had run at about €210 a month for a year, then reached €640.

Customer count had grown by two. The breakdown showed database compute accounting for nearly all of the increase, with the step change beginning on a specific Monday — the day a new customer with 1.4 million shipment records began using the product.

Their dashboard was executing an unindexed aggregation across the full table on every page load, taking eleven seconds and consuming most of the database's capacity while it ran. The customer had assumed the product was simply slow. Two other customers had noticed general slowness during the same period without connecting it to anything.

Two smaller contributors surfaced too: a staging environment at production sizing running continuously for eight months, and application logs retained indefinitely at roughly 12GB a month.

**Result:** three indexes added and the dashboard aggregation precomputed on a schedule, reducing load time from eleven seconds to under one; staging resized and set to sleep outside working hours; log retention set to 30 days. The following month's bill was €185 — below the original figure, with three more customers than before.

> "I assumed my costs had started scaling with customers and that my pricing was wrong. It was one query, for one customer, that nobody had ever indexed."
> — **Marek Novotny, Founder, Inzichtbord**

**Cost & Timeline:** cost and performance review with fixes delivered in 3 business days.

## Frequently Asked Questions

### What usually causes a sudden infrastructure cost increase?

Most often an inefficient database query that crossed a threshold, frequently triggered by one large customer arriving. Data transfer, accumulated storage, and over-frequent background jobs are the other common causes.

### Should I switch providers to reduce costs?

Not before understanding the cause. An inefficient query costs money on every platform, and migrating carries its own risk and effort. Fix the cause first, then reassess whether the provider is still the right one.

### What number should I track instead of the total bill?

Cost per active customer. A bill that doubles alongside customers is healthy; one that doubles while customers grow slightly indicates waste with a specific cause.

### How do I stop a metered feature from producing a huge bill overnight?

Enforce per-account and global daily limits in your own code, alert on daily spend rate rather than monthly total, and ensure nothing expensive is reachable without authentication.

### Is it worth optimising a small cost line?

Rarely. Engineering time spent saving less than it costs is a poor trade, and the largest line is almost always where the return is. Work down from the biggest number, not the easiest one.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What usually causes a sudden infrastructure cost increase?", "acceptedAnswer": { "@type": "Answer", "text": "Most often an inefficient database query crossing a threshold, frequently when one large customer arrives. Data transfer, accumulated storage, and over-frequent background jobs follow." } },
    { "@type": "Question", "name": "Should I switch providers to reduce costs?", "acceptedAnswer": { "@type": "Answer", "text": "Not before understanding the cause. An inefficient query costs money on every platform, and migration carries its own risk. Fix the cause, then reassess." } },
    { "@type": "Question", "name": "What number should I track instead of the total bill?", "acceptedAnswer": { "@type": "Answer", "text": "Cost per active customer. A bill doubling alongside customers is healthy; one doubling while customers grow slightly indicates waste with a specific cause." } },
    { "@type": "Question", "name": "How do I stop a metered feature from producing a huge bill overnight?", "acceptedAnswer": { "@type": "Answer", "text": "Enforce per-account and global daily limits in your own code, alert on daily spend rate rather than monthly total, and keep expensive operations behind authentication." } },
    { "@type": "Question", "name": "Is it worth optimising a small cost line?", "acceptedAnswer": { "@type": "Answer", "text": "Rarely. Engineering time worth more than the saving is a poor trade, and the largest line is almost always where the return is." } }
  ]
}
</script>
