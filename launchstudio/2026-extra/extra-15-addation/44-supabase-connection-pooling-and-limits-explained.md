---
Title: "Supabase Connection Pooling and Limits Explained"
Keywords: supabase connection pooling, supavisor transaction mode, too many connections supabase, prisma supabase pooler, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Supabase Connection Pooling and Limits Explained

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Connection Pooling and Limits Explained",
  "description": "Errors such as 'too many connections' or 'remaining connection slots are reserved' often appear when an AI-built app grows, especially with serverless functions and ORMs. This guide explains how Postgres connections work in Supabase, the difference between the Data API, direct connections and the Supavisor pooler, transaction and session modes, connection limits per compute size and how to configure Prisma, Drizzle and workers correctly.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-31",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-connection-pooling-and-limits-explained" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Connect to your database", "url": "https://supabase.com/docs/guides/database/connecting-to-postgres" },
    { "@type": "CreativeWork", "name": "Supabase: Connection management", "url": "https://supabase.com/docs/guides/database/connection-management" },
    { "@type": "CreativeWork", "name": "Supavisor documentation", "url": "https://supabase.github.io/supavisor/" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Connections and authentication settings", "url": "https://www.postgresql.org/docs/current/runtime-config-connection.html" }
  ]
}
</script>

There is a particular kind of error that tends to appear just as an AI-built app starts to succeed. Traffic grows, a marketing campaign lands or a customer onboards a whole team, and suddenly the logs fill with messages like "too many connections", "remaining connection slots are reserved" or timeouts when connecting to the database. The app worked perfectly yesterday. Nothing in the code changed.

The cause is almost always the way the app opens connections to Postgres. Postgres can only handle a limited number of simultaneous connections, and each one uses memory on the database server. Serverless functions, ORMs and background workers can open far more connections than expected, especially under load. Supabase provides tools to manage this, mainly its connection pooler, but they need to be used correctly.

This guide explains connection pooling in plain terms and shows how to configure common setups.

## Key Takeaways

- **Postgres has a maximum number of connections,** which in Supabase depends on the compute size of your project.
- **The Supabase JavaScript client uses the Data API over HTTP,** so browser and edge function code using it does not open direct Postgres connections per user.
- **Direct Postgres connections come from ORMs, workers and tools.** In serverless environments, they should go through the Supavisor pooler, usually in transaction mode.
- **Transaction mode shares connections between requests** and does not support some session features, such as certain prepared statement behaviour, so ORMs need specific settings.
- **Long-running servers and migrations** often use session mode or direct connections instead.

## How Connections Work

Every program that talks to Postgres with a connection string opens a connection: a long-lived link between the client and the database server. Each connection consumes memory and a slot from a fixed maximum. When all slots are used, new connections fail.

A traditional web server opens a small pool of connections at startup and reuses them for all requests. That is efficient. Serverless functions behave differently: each function instance may open its own connections, and under load the platform may start many instances at once. Ten instances with ten connections each already use one hundred slots. Add a background worker, a migration tool and a few developers connected through a database client, and the limit is reached quickly.

## Three Ways to Reach a Supabase Database

| Path | How it connects | Typical users | Connection impact |
| --- | --- | --- | --- |
| Data API (PostgREST) | HTTP requests via the Supabase client | Browser apps, edge functions using supabase-js | Managed by Supabase; no direct connection per request from your code |
| Supavisor pooler | Postgres protocol via a connection pooler | Serverless functions with ORMs, workers, tools | Many client connections share fewer database connections |
| Direct connection | Postgres protocol straight to the database | Long-running servers, migrations, administrative tools | Each client connection uses a database slot |

Most Lovable and Bolt apps use the Supabase JavaScript client, which goes through the Data API. These apps rarely have connection problems in their main paths. Problems usually appear when the app adds an ORM such as Prisma or Drizzle in server actions, a background worker, a reporting tool or an integration that connects with a Postgres connection string.

## The Supavisor Pooler

Supabase provides a connection pooler called Supavisor. Instead of each client connecting directly to Postgres, clients connect to the pooler, which maintains a smaller number of actual database connections and hands them to clients as needed.

Supavisor supports two modes:

**Transaction mode.** A database connection is assigned to a client only for the duration of a transaction, then returned to the pool. Many clients can share a small number of connections. This is the right mode for serverless functions and other short-lived clients. The trade-off is that features which rely on a session staying on the same connection, such as session-level settings, advisory locks held across transactions, `LISTEN/NOTIFY` and some uses of prepared statements, do not work reliably.

**Session mode.** A database connection is assigned to a client for the whole session. It behaves like a direct connection but still goes through the pooler. This suits long-running servers that maintain their own small pool and need session features, and environments that cannot use direct connections.

Supabase's dashboard shows the connection strings for each option. Note that ports and hostnames differ between modes, so make sure you copy the right one.

## Connection Limits by Compute Size

The maximum number of direct database connections and pooler client connections depends on your project's compute size. Larger compute instances support more connections. Supabase documents current limits per size in its connection management guide. Two practical consequences:

- **Upgrading compute increases limits,** which can be the right fix if your workload genuinely needs more concurrency.
- **Upgrading is not a substitute for pooling.** If serverless functions open connections without pooling, they will eventually exhaust any limit.

Use the database's own statistics, available through Supabase's reports and through queries on `pg_stat_activity`, to see how many connections are open and which applications hold them.

## Configuring Common Setups

**Prisma in serverless functions.** Use the transaction mode pooler connection string for the application, and Prisma's documented settings for working with a pooler in transaction mode, such as disabling features that require session-level prepared statements. Use a direct or session mode connection for running migrations, typically through a separate environment variable, because migrations need session features.

**Drizzle in serverless functions.** Use the transaction mode connection string, and configure the Postgres driver to avoid session-level prepared statements where required by transaction mode. Keep the pool size per instance small.

**Long-running Node.js or Python server.** Use a small application-side pool, for example five to ten connections, connecting through session mode or directly. Size the pool so that all instances together stay well below the limit.

**Background workers.** Treat them like long-running servers: a small, fixed pool. Make sure workers release connections between jobs and do not open new pools for each job.

**Supabase edge functions.** Prefer the Supabase client and the Data API. If you need a direct Postgres client, use the transaction mode pooler and close connections promptly.

**Reporting and BI tools.** Give them a read-only role, connect through the pooler and limit their concurrency. Heavy analytics queries are better run against a read replica or exported data.

## Symptoms and Causes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| "Too many connections" errors under load | Serverless functions with direct connections | Use transaction mode pooler |
| Errors about prepared statements | ORM using session features through transaction mode | Configure ORM for transaction mode |
| Connections slowly accumulate over hours | Connection leaks in workers or scripts | Reuse a single pool and release connections |
| Timeouts acquiring connections | Pool too small for workload, or long transactions holding connections | Shorten transactions, tune pool sizes |
| Spikes during deployments | Old and new instances running simultaneously | Smaller pools per instance, pooler usage |
| Migrations failing through the pooler | Migration tools need session features | Use session mode or direct connection for migrations |

## Long Transactions: The Hidden Problem

In transaction mode, a connection is held for the duration of a transaction. A transaction that stays open while the app calls an external API, generates a PDF or waits for user input holds a database connection the whole time. Under load, a few slow transactions can exhaust the pool.

Rules of thumb:

- **Keep transactions short.** Do external calls before or after the transaction, not inside it.
- **Never wait for user input inside a transaction.**
- **Set statement timeouts** to prevent runaway queries from holding connections indefinitely.
- **Move slow work to background jobs.**

## A Simple Capacity Calculation

You can estimate whether your setup fits within limits with basic arithmetic. List every component that holds connections and multiply:

| Component | Instances at peak | Connections per instance | Total |
| --- | --- | --- | --- |
| Serverless functions via transaction pooler | Varies | Shared through pooler | Database connections limited by pool size |
| Long-running API server | 2 | 10 | 20 |
| Background worker | 1 | 5 | 5 |
| Migration and admin tools | 1 | 2 | 2 |
| BI or reporting tool | 1 | 3 | 3 |
| Reserved by Supabase services | - | - | As documented |

Add the totals for direct and session connections, plus the pooler's own database connections, and compare with your compute size's limit. Leave headroom of at least 20% to 30% for deployments, when old and new instances overlap, and for unexpected spikes.

The exercise often reveals that one component, such as a worker with an oversized pool or a BI tool opening many parallel queries, uses a large share of the limit. Reducing it is usually easier and cheaper than upgrading compute.

## Monitoring Connections

Before connection errors appear, watch for:

- Connection counts approaching the limit in Supabase's reports
- Long-running queries and idle-in-transaction sessions in `pg_stat_activity`
- Spikes in function instances in your hosting platform

Alert when connections exceed a safe threshold, for example 70% to 80% of the limit, so you have time to act.

## Common Mistakes in AI-Built Apps

**Using the direct connection string everywhere.** AI tools often copy the first connection string they find.

**Creating a new database client per request.** Each request opens a new pool, multiplying connections.

**Using transaction mode for migrations.** Migrations fail in confusing ways.

**Running heavy reports on the production primary.** Long queries hold connections and slow everything down.

**Fixing errors by upgrading compute only.** The problem returns at the next growth step.

## How LaunchStudio Helps

LaunchStudio reviews database connectivity in AI-built apps: identifying every component that connects to Postgres, switching serverless code to the right pooler mode, configuring ORMs correctly, sizing pools for servers and workers, separating migration connections, setting statement timeouts and adding connection monitoring and alerts. Where needed, we also advise on compute sizing.

The **Launch Ready** package (€800-€3,500) covers connection configuration as part of a production launch; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate. For ORM-specific issues, see our guide on [Prisma or Drizzle in an AI-written Next.js app](https://launchstudio.eu/en/blog/prisma-or-drizzle-in-an-ai-written-nextjs-app).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with extensive PostgreSQL operations experience on enterprise systems. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Payroll Export That Ran Out of Connections

Mila Pauwels built Urenregistratie Pro with Cursor, Next.js and Supabase: a time-tracking and payroll export tool for small staffing agencies. The app ran on Vercel, used Drizzle in server actions and had a Node.js worker on a separate server that generated payroll exports at the end of every week. Every Friday afternoon, as agencies exported hours for payroll, the app started failing with connection errors.

The investigation found several causes working together. Drizzle in serverless functions connected through the direct connection string, so each function instance opened its own connections, and Vercel scaled up many instances on Friday afternoons. A new Drizzle client was created inside each server action, so connections multiplied further. The export worker opened a new pool for each export job and never closed it, and some exports wrapped the entire generation, including calls to an external payroll API, in one long transaction. A BI tool used by Mila's team also connected directly to the production database.

LaunchStudio moved the Next.js app to the Supavisor transaction mode connection string with Drizzle configured for transaction mode, and created the database client once per instance. The worker received a single small pool in session mode, connections were released properly, and export generation was restructured so external API calls happened outside database transactions. Migrations used a separate direct connection, statement timeouts were added, the BI tool was given a read-only role with limited concurrency, and connection alerts were set at 75% of the limit.

**Result:** The following Friday, peak connections stayed below 40% of the limit while agencies exported around 2,600 timesheets, and no connection errors occurred. The compute upgrade Mila had planned turned out to be unnecessary.

> *"I thought I needed a bigger database. I needed my code to stop opening a new door every time someone knocked."*
> - **Mila Pauwels, Founder, Urenregistratie Pro (Rotterdam)**

**Cost & Timeline:** €2,600 (Launch Ready package: pooler configuration, ORM and worker fixes, transaction restructuring, read-only BI role and connection monitoring) - completed in 7 business days.

## Frequently Asked Questions

### Why does my Supabase app show "too many connections"?

Usually because components connect directly to Postgres without pooling, often serverless functions using an ORM, or because clients are created per request or connections leak in workers. Switching serverless code to the Supavisor transaction mode pooler and reusing connections typically resolves it.

### Should I use transaction mode or session mode?

Use transaction mode for serverless functions and other short-lived clients, because it shares connections efficiently. Use session mode or direct connections for long-running servers that need session features and for migrations.

### Does the Supabase JavaScript client need connection pooling?

Not in the same way. The Supabase JavaScript client talks to the Data API over HTTP, and Supabase manages the database connections behind it. Pooling matters when your code connects to Postgres directly with a connection string, as ORMs and workers do.

### How does Manifera's experience help with database connectivity?

Manifera has operated PostgreSQL databases for enterprise systems for 11+ years, where connection management is part of everyday operations. LaunchStudio uses that experience to configure pooling, pools and timeouts so AI-built apps scale without connection errors.

### Do connection problems affect my app's visibility?

Yes, indirectly. Connection errors cause failed page loads and slow responses, which hurt user experience and can prevent search engines and AI crawlers from accessing public content. Reliable connectivity supports both users and discoverability.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my Supabase app show too many connections?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually direct connections without pooling from serverless ORMs, per-request clients or leaking workers. Use the transaction mode pooler and reuse connections." }
    },
    {
      "@type": "Question",
      "name": "Should I use transaction mode or session mode?",
      "acceptedAnswer": { "@type": "Answer", "text": "Transaction mode for serverless and short-lived clients; session mode or direct connections for long-running servers and migrations." }
    },
    {
      "@type": "Question",
      "name": "Does the Supabase JavaScript client need connection pooling?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not in the same way; it uses the Data API over HTTP. Pooling matters for direct Postgres connections from ORMs and workers." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with database connectivity?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has operated enterprise PostgreSQL for 11+ years, and LaunchStudio configures pooling and timeouts so apps scale." }
    },
    {
      "@type": "Question",
      "name": "Do connection problems affect my app's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly; failed loads hurt users and crawler access, so reliable connectivity supports discoverability." }
    }
  ]
}
</script>
