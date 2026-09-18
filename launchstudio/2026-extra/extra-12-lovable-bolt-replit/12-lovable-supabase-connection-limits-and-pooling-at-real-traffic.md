---
Title: "Lovable Supabase: Connection Limits and Pooling at Real Traffic"
Keywords: lovable supabase, connection pooling, pgbouncer, serverless connections, too many clients, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Connection Limits and Pooling at Real Traffic

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Connection Limits and Pooling at Real Traffic",
  "description": "\"Too many clients already\" is what an AI-built app says when it succeeds. Why serverless functions exhaust Postgres connections, what the pooler does, and which connection string belongs where.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-connection-limits-and-pooling-at-real-traffic" }
}
</script>

The error arrives without warning and usually at the best possible moment for your business and the worst for you: *sorry, too many clients already*. Your product stops. Nothing is broken, nothing was deployed, and in ten minutes it may well work again.

What happened is that more parts of your application asked the database for a connection than the database was willing to give. Postgres does not have unlimited connections — each one costs real memory — and a small Supabase plan permits far fewer than founders assume. Sixty is a typical number. Some plans allow fifteen.

Fifteen sounds tiny until you realise it is not fifteen users. It is fifteen simultaneous conversations with the database, which a well-behaved application can serve hundreds of users with, and which a serverless application can exhaust with nine people.

## Why Serverless Makes This Worse

A traditional server starts once, opens a handful of connections, and reuses them for every request for months. That is the arrangement Postgres was designed around.

Serverless functions — Vercel functions, Supabase edge functions, Netlify functions, the default deployment target for almost every AI-built app — work the other way. Each invocation may be a fresh instance with no memory of the last. If each one opens its own connection, then a hundred concurrent requests means a hundred connections, and the database refuses somewhere around number sixteen.

Worse, an instance that finishes its work does not necessarily close the connection immediately. Connections linger, idle, holding a slot that nothing is using. It is entirely possible to exhaust your limit with almost no traffic at all, purely through accumulation.

This is not a flaw in serverless. It is a mismatch between two models, and the bridge between them is a pooler.

## What the Pooler Does

A connection pooler sits between your application and Postgres. Your functions connect to it, it maintains a small number of real connections to the database, and it hands them out for the duration of a statement or a transaction rather than for the lifetime of a client.

Because most requests use their connection for a few milliseconds and spend the rest of their life doing other things, a handful of real connections can serve a very large number of application instances.

Supabase provides this, and the practical consequence is that your application has two connection strings available and they are not interchangeable. There is a direct connection to the database, and a pooled connection on a different port with different behaviour. Using the wrong one is the most common cause of this whole class of problem.

## Which Connection String Belongs Where

The rule is short and worth writing down somewhere your future self will find it.

**Application code, especially serverless, uses the pooled connection.** Everything that serves user requests. This is the default and if you only remember one thing, remember this.

**Migrations and schema changes use the direct connection.** Pooled connections in transaction mode do not support everything — prepared statements behave differently, session-level settings do not persist, and some schema operations will fail confusingly.

**Long-running background jobs and anything holding a transaction open use the direct connection**, sparingly, because they occupy a real slot for their whole duration.

Two habits prevent the errors that remain. Never hold a database transaction open across a call to an external service — a webhook, a model API, an email provider — because that occupies a connection for the duration of somebody else's outage. And make sure your client library is configured with a sensible pool size per instance rather than the library default, which is often far too generous for an environment where dozens of instances exist at once.

## Diagnosing It When It Happens

When the error appears, three things tell you what is going on and all are available in the Supabase dashboard.

Current connection count against your plan's limit, which confirms the diagnosis. The breakdown of what those connections are doing — a large number sitting idle in transaction is a specific and fixable bug, meaning code that opened a transaction and did something slow before committing. And whether the count grows steadily over hours rather than spiking with traffic, which indicates leaked connections rather than genuine load.

A leak looks like this: connection count climbing slowly from deploy time until it hits the ceiling, regardless of how many users are active. It is nearly always a client created inside a request handler rather than once at module level, so every invocation makes another one and nothing ever tidies up.

## The Fix That Is Not Upgrading

The instinct when hitting a limit is to buy a bigger plan, and it does raise the ceiling.

It also costs money every month to work around a bug that takes an hour to fix, and it delays the diagnosis rather than removing it — a leak that took three days to fill sixty connections will take twelve days to fill two hundred and forty, and it will still happen on the busiest morning of your year.

Fix the code first: pooled connections everywhere they belong, client instances created once, transactions kept short, no external calls inside them. Then upgrade if your traffic genuinely warrants it. Most products at this stage find that the correct configuration serves several times their current load on the plan they already have.

## Realtime and Its Own Limits

If your product uses Supabase realtime for live updates, that has separate limits — concurrent connections and messages per second — and they are exhausted by a different pattern.

The usual cause is a subscription created on every render rather than once, so a user with a page open for an hour accumulates subscriptions until something gives. The symptom is one heavy user affecting everyone, and it is invisible in testing because a single developer refreshing a page never accumulates enough.

Subscribe once, unsubscribe when the component goes away, and count your active subscriptions somewhere you can see them. The same applies to any long-lived connection your product opens: the question is never whether it works, but what happens after four hours.

## Load Test Before the Campaign, Not After

Everything above is knowable in advance for the price of an afternoon.

Point a load-testing tool at your product's busiest page with realistic authentication and run it at two or three times the concurrency you expect. Watch connection count, error rate and response time together. The failure mode you are looking for is not slowness — it is the cliff, where everything is fine at thirty concurrent users and nothing works at forty.

Do this before a launch, a campaign, a press mention or a seasonal peak, because the cliff is always found by real users otherwise, and always at the moment the traffic was most valuable.

## Where the Timeouts Come From

Connection exhaustion has a quieter cousin that produces the same customer experience for a different reason: connections that are available but held too long.

Postgres has settings that govern this, and the defaults on a hosted plan are more forgiving than they should be for a small product. A statement timeout caps how long any single query may run before it is cancelled, which converts a runaway report into one failed request rather than a database everyone else is queuing behind. An idle-in-transaction timeout closes connections where something opened a transaction and then wandered off, which is exactly what a crashed function instance leaves behind.

Setting both is a five-minute change with a large effect on how your product fails. Without them, one badly written query on one customer's unusually large dataset degrades the experience of every other customer, because it is occupying a connection and the locks that come with it while it works.

Choose numbers deliberately rather than generously: a few seconds for ordinary application queries, longer for a deliberately separate role used by reports and exports. The point is not to be strict. It is that a query which has been running for thirty seconds on a screen a human is waiting for has already failed, and letting it continue only spreads the failure.

## Setting This Up

For an existing app this is usually half a day to a day: connection strings audited so application code uses the pooler and migrations use the direct connection, database clients created once per instance rather than per request, pool size configured deliberately, transactions audited for external calls and long operations, realtime subscriptions checked for accumulation, connection metrics watched with an alert before the ceiling rather than at it, and a load test at several times expected concurrency to find the cliff while it is cheap.

LaunchStudio does this as part of production readiness — it is one of the few problems that only appears once a product is working, which makes it a particularly unwelcome surprise. The engineers are Manifera's: eleven years, 160+ projects, and a great deal of Postgres under load, from Amsterdam and Ho Chi Minh City.

[Tell us your expected peak](https://launchstudio.eu/en/#contact) and we will tell you whether your current setup survives it.

## Real example

### Nine Users and a Broken Product

Thijs Kranenburg built Zaalplanner in Lovable: booking software for community centres and village halls, 48 venues across Friesland and Groningen, each with a handful of staff.

The product broke every Monday morning. Not slowly — completely, with database errors on every page, for ten to twenty minutes, then recovery without intervention. Monday morning is when venue managers do the week's bookings, so it was the worst possible window and the reason two venues had already asked about alternatives.

His Supabase plan allowed 60 connections. His application created a new database client inside each serverless function invocation, so every request opened a connection and left it to expire. Monday's nine or ten concurrent managers, each loading pages that made four or five requests, exhausted the limit within minutes.

One business day: the database client moved to module scope so each function instance reuses a single connection; every application connection string switched to the pooled port, with the direct connection reserved for migrations; pool size set explicitly rather than left at the library default; two transactions that wrapped an email call removed, since one provider outage had held connections open for ninety seconds each; a realtime subscription in the booking calendar fixed to subscribe once rather than on every render; a dashboard alert at 70 percent of the connection limit; and a load test at 120 concurrent users to confirm the fix rather than assume it.

**Result:** Monday mornings stopped failing. Peak connection use fell from the 60-connection ceiling to a steady 7, and the load test cleared 120 concurrent users — more than double Thijs's realistic peak — on the same plan he had been about to upgrade for €300 a month.

> *"I was convinced I needed a bigger database. The whole problem was one line in the wrong place, creating a connection for every request and never giving it back."*
> — **Thijs Kranenburg, Founder, Zaalplanner (Leeuwarden)**

**Cost & Timeline:** €1,450 (connection audit and pooler migration, client lifecycle fix, transaction remediation, realtime subscription fix, alerting, load test) — completed in 1 business day.

## Frequently Asked Questions

### What does "too many clients already" mean?

Your application asked Postgres for more simultaneous connections than your plan permits. It is almost always a connection lifecycle bug rather than genuine load, particularly in serverless deployments.

### When should I use the pooled connection string?

For all application code, especially serverless functions. Use the direct connection only for migrations, schema changes and long-running background work.

### Will upgrading my Supabase plan fix it?

It raises the ceiling and delays the diagnosis. A connection leak that fills 60 slots will fill 240, just more slowly, and usually on your busiest day. Fix the lifecycle first.

### Why do connections climb when nobody is using the app?

Because something creates a client per request and never closes it. Steady growth from deploy time until the ceiling, independent of traffic, is the signature of a leak.

### How do I know my limit before I hit it?

Load test at two or three times expected concurrency and watch connection count alongside errors. The failure is a cliff rather than a gradual slowdown, so it will not show up in normal use.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does the error \"too many clients already\" mean?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your app requested more simultaneous Postgres connections than the plan allows — usually a connection lifecycle bug in serverless code rather than real load."
      }
    },
    {
      "@type": "Question",
      "name": "When should I use Supabase's pooled connection string?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For all application code, especially serverless. Reserve the direct connection for migrations, schema changes and long-running jobs."
      }
    },
    {
      "@type": "Question",
      "name": "Will upgrading the plan fix connection exhaustion?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It raises the ceiling without fixing the leak, which will still fill the larger limit — usually on your busiest day."
      }
    },
    {
      "@type": "Question",
      "name": "Why do connections climb when nobody is using the app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A client is being created per request and never closed. Steady growth from deploy time regardless of traffic is the signature."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find my concurrency limit before customers do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Load test at two to three times expected peak while watching connection count and errors. The failure is a cliff, not a gradual slowdown."
      }
    }
  ]
}
</script>
