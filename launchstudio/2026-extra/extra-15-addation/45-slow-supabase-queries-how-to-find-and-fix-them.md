---
Title: "Slow Supabase Queries: How to Find and Fix Them"
Keywords: slow supabase queries, supabase query performance, postgres explain analyze, supabase index advisor, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Slow Supabase Queries: How to Find and Fix Them

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Slow Supabase Queries: How to Find and Fix Them",
  "description": "AI-built apps on Supabase often feel fast with test data and slow with real data. This guide explains how to find slow queries using Supabase's performance tools, pg_stat_statements and EXPLAIN ANALYZE, and how to fix the most common causes: missing indexes, expensive Row Level Security policies, unbounded selects, exact counts, offset pagination, wildcard searches and N+1 query patterns.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-01",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/slow-supabase-queries-how-to-find-and-fix-them" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Query optimization", "url": "https://supabase.com/docs/guides/database/query-optimization" },
    { "@type": "CreativeWork", "name": "Supabase: RLS performance recommendations", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security#rls-performance-recommendations" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Using EXPLAIN", "url": "https://www.postgresql.org/docs/current/using-explain.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: pg_stat_statements", "url": "https://www.postgresql.org/docs/current/pgstatstatements.html" }
  ]
}
</script>

Every AI-built app is fast at first. With twenty test records, any query returns instantly, whatever its design. Then real customers arrive, tables grow to tens of thousands of rows, and pages that loaded in a blink start taking two, five or ten seconds. Customers notice, complain or quietly leave, and the founder wonders whether Supabase "doesn't scale".

Supabase runs on Postgres, which scales very well when queries are designed for it. In the projects we review, slow pages almost always come from a handful of fixable causes: missing indexes, policies that do expensive work for every row, queries that load far more data than needed, and frontends that send dozens of queries where one would do. The good news is that finding and fixing them is usually a matter of days, not a rebuild.

This guide explains how to find slow queries and fix the most common causes.

## Key Takeaways

- **Measure before fixing.** Use Supabase's query performance reports and `pg_stat_statements` to find the queries that cost the most time in total.
- **EXPLAIN ANALYZE shows why a query is slow,** for example a sequential scan of a large table where an index would help.
- **Missing indexes are the most common cause,** especially on foreign keys, filter columns and sort columns.
- **Row Level Security policies run per row.** Write them so they can use indexes and avoid repeated function calls.
- **Load less data:** select only needed columns, paginate, avoid exact counts on large tables and fix N+1 patterns in the frontend.

## Step 1: Find the Slow Queries

Do not guess. Supabase provides tools to see which queries take the most time:

- **Query performance reports** in the Supabase dashboard show slow and frequent queries.
- **Index advisor** features can suggest indexes for specific queries.
- **`pg_stat_statements`,** a Postgres extension enabled in Supabase, records statistics for every query pattern: how often it runs, total time and average time.

Sort by **total time**, not average time. A query that takes 30 milliseconds but runs 200,000 times a day costs more than one that takes 3 seconds once a day. Both may need attention, but the frequent one usually affects more users.

Also measure from the user's side. Error and performance monitoring in the browser shows which pages are slow, which helps connect database statistics to real experience.

## Step 2: Understand Why With EXPLAIN ANALYZE

For each slow query, run `EXPLAIN ANALYZE` in the SQL editor on a staging database with realistic data. It shows how Postgres executes the query and how long each step takes. Things to look for:

| What you see | What it means |
| --- | --- |
| `Seq Scan` on a large table | Postgres reads every row; an index may help |
| High "rows removed by filter" | The query reads many rows and discards most |
| `Sort` with large memory or disk usage | Sorting without a supporting index |
| Nested loops with many iterations | A join or subquery repeated per row |
| Function calls repeated per row | Often from policies or computed columns |
| Large difference between estimated and actual rows | Statistics may be outdated |

Remember that queries from the Supabase client run as the authenticated user, with policies applied. To reproduce realistic behaviour, test with the same role and claims, or examine queries captured by `pg_stat_statements`.

## Cause 1: Missing Indexes

AI builders create tables and foreign keys, but rarely indexes beyond primary keys. Postgres does not automatically index foreign key columns. Common indexes to add:

- **Foreign keys,** such as `project_id` on tasks or `organisation_id` on almost every table in a multi-tenant app
- **Columns used in filters,** such as `status`, `user_id` or `created_at`
- **Columns used in sorts,** such as `created_at desc` for activity feeds
- **Composite indexes** for common combinations, such as `(organisation_id, created_at desc)`

Indexes speed up reads but add a small cost to writes and use storage, so add them for queries that actually run, not for every column. On busy production tables, create indexes concurrently to avoid blocking writes, as explained in our guide on [zero-downtime database migrations](https://launchstudio.eu/en/blog/zero-downtime-database-migrations-in-supabase).

## Cause 2: Expensive Row Level Security Policies

Policies are evaluated for rows that queries touch. A policy that performs a lookup, such as checking team membership, can turn a simple query into thousands of subqueries. Supabase's documentation includes performance recommendations, including:

- **Index the columns used in policies,** such as `user_id` or `organisation_id`.
- **Wrap functions like `auth.uid()` in a subselect,** for example `(select auth.uid())`, so Postgres can evaluate it once per query instead of once per row.
- **Use security definer functions carefully** for membership checks, so lookups use indexes and do not trigger further policy evaluation.
- **Add explicit filters in queries** that match the policy, such as filtering by `organisation_id`, so Postgres can use indexes before applying the policy.
- **Avoid joins inside policies** where a simpler check on an indexed column works.

Our guide on [Row Level Security performance in Supabase](https://launchstudio.eu/en/blog/row-level-security-performance-in-supabase) covers these patterns in more depth.

## Cause 3: Loading Too Much Data

AI-generated code often uses `select('*')` and loads entire tables into the browser, then filters or paginates in JavaScript. With real data, that means transferring megabytes for a page showing twenty rows.

Fixes:

- **Select only needed columns,** for example `select('id, name, status, due_date')`.
- **Filter on the server,** using query filters instead of JavaScript.
- **Paginate,** returning a limited number of rows per request.
- **Avoid large JSON or text columns in list queries;** load them only on detail pages.

## Cause 4: Exact Counts on Large Tables

Showing "1,284,519 results" requires counting every matching row, which is slow on large tables. The Supabase client lets you request an exact count, a planned estimate or none. For large tables:

- Use estimated counts where approximate numbers are acceptable.
- Show "more than 1,000" instead of exact numbers.
- Maintain counters in summary tables updated by triggers for important totals.

## Cause 5: Offset Pagination on Large Tables

Pagination with `offset` gets slower the further users page, because Postgres must skip all previous rows. For feeds and long lists, **keyset pagination** is faster: request rows after the last seen value, for example `created_at < last_seen_created_at`, with an index on that column. For short lists, offset pagination is fine.

## Cause 6: Wildcard Searches

Searches implemented as `ilike '%term%'` cannot use normal indexes and scan the whole table. Options:

- **Trigram indexes** using the `pg_trgm` extension, which support `ilike` searches efficiently
- **Postgres full-text search** with `tsvector` columns and GIN indexes, which also supports ranking and language-specific stemming, including Dutch
- **A dedicated search service** for very large or complex search needs

Our guide on [adding search to a Supabase app](https://launchstudio.eu/en/blog/how-do-i-add-search-to-my-supabase-app) explains the options.

## Cause 7: N+1 Queries From the Frontend

A common pattern in AI-generated React code: load a list of projects, then for each project, load its tasks in a separate request. Twenty projects mean twenty-one requests, each with network latency and policy evaluation.

Fixes:

- **Use embedded resources** in the Supabase client to load related data in one query, for example projects with their task counts.
- **Create views or database functions** that return exactly what a screen needs.
- **Aggregate on the server,** for example counts and sums, instead of loading all child rows to count them in JavaScript.

## Cause 8: Outdated Statistics and Bloat

Postgres relies on table statistics to choose efficient plans. After large imports or deletions, statistics may be outdated, leading to poor plans. Autovacuum normally maintains statistics and cleans up dead rows, but after big data changes, running `ANALYZE` on affected tables can help. Very frequent updates to the same rows can cause table bloat, which is worth monitoring as data grows.

## Keeping Performance From Regressing

Performance work has a habit of slowly undoing itself. Each new feature adds a query, each AI-assisted change may reintroduce `select('*')` or a per-item request, and data keeps growing. A few habits keep the gains:

- **Seed staging with realistic data** and keep it there. Developers and AI tools then see slow queries while building, not after release.
- **Add performance notes to project instructions.** For example: "select only needed columns; paginate lists; never fetch related data in a loop; add an index for new filters."
- **Review new queries in pull requests.** A quick look for unbounded selects, missing filters and loops over requests catches most regressions.
- **Watch query statistics weekly.** A new entry near the top of the total-time list usually points to a recent change.
- **Set a performance budget** for key pages, such as "dashboard under one second at the 95th percentile", and check it after major releases.
- **Revisit indexes periodically.** Remove unused ones, which slow writes, and add ones for new access patterns.

These checks take little time, and they prevent the gradual slowdown that otherwise makes a fast app feel sluggish again within a few months.

## A Typical Optimisation Session

| Step | Action |
| --- | --- |
| 1 | Seed staging with realistic data volumes |
| 2 | List the slowest and most frequent queries from statistics |
| 3 | Run EXPLAIN ANALYZE for the top ten |
| 4 | Add missing indexes and rewrite expensive policies |
| 5 | Reduce selected columns and add pagination in the frontend |
| 6 | Replace N+1 patterns with joined queries or views |
| 7 | Re-measure and compare page load times |
| 8 | Add monitoring for slow queries going forward |

In most AI-built apps, the first round produces dramatic improvements, often reducing key page load times by a large factor.

## How LaunchStudio Helps

LaunchStudio optimises Supabase performance in AI-built apps: analysing query statistics, adding indexes, rewriting policies for performance without weakening security, restructuring frontend data loading, implementing search properly, introducing pagination and summary tables where needed, and setting up monitoring for slow queries.

The **Launch Ready** package (€800-€3,500) covers performance fixes for key journeys along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with deep PostgreSQL performance experience on enterprise systems. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Maintenance Dashboard That Took Nine Seconds

Wessel Hofman built Storingsboek with Lovable and Supabase: a tool for property maintenance companies to log repair requests, assign technicians and track work orders. After a year, his largest customer, a maintenance company serving several housing associations, had around 180,000 work orders, and the main dashboard took nine seconds to load. Technicians complained that the mobile list of their assignments was barely usable.

The analysis found several causes at once. The dashboard loaded all open work orders with every column, including long description and history fields, and filtered them in JavaScript. For each work order, the frontend made a separate request for the assigned technician and the property, producing hundreds of requests per page. The Row Level Security policy on work orders called a function that queried team membership for every row, without an index on the membership table. There were no indexes on `organisation_id`, `status` or `assigned_to`, and the search box used `ilike '%term%'` on descriptions.

LaunchStudio added composite indexes for the most common filters and sorts, rewrote the policy to use `(select auth.uid())` with an indexed membership lookup and added explicit organisation filters to queries. The dashboard switched to a view returning exactly the columns it needed, with technician and property names joined in, and keyset pagination for long lists. Counts per status came from a summary table updated by triggers, and search moved to a trigram index on titles and addresses. All changes were tested on staging with a copy of production-scale synthetic data.

**Result:** The dashboard now loads in about 400 milliseconds, and technicians' assignment lists load in under half a second on mobile networks. Database CPU usage during working hours dropped by more than half, so the planned compute upgrade was postponed.

> *"I was ready to blame Supabase. It turned out my app was asking the database to do the same work hundreds of times on every page."*
> - **Wessel Hofman, Founder, Storingsboek (Hilversum)**

**Cost & Timeline:** €3,100 (Launch Ready package: query analysis, indexes, policy optimisation, views and pagination, search and monitoring) - completed in 8 business days.

## Frequently Asked Questions

### Why is my Supabase app slow with real data?

Usually because queries that were fine with small test data now scan large tables without indexes, policies do expensive lookups for each row, or the frontend loads too much data or sends many separate requests. These causes are identifiable with query statistics and EXPLAIN ANALYZE, and fixable without changing platforms.

### Do Row Level Security policies make queries slow?

They can, if they perform lookups or function calls for every row without indexes. Written well, with indexed columns, subselects for functions like `auth.uid()` and explicit filters in queries, policies add little overhead.

### Should I upgrade my Supabase compute to fix slow queries?

Only after optimising. More compute helps if the workload is efficient but large. If queries scan entire tables or repeat work, upgrading only postpones the problem. Optimisation often makes an upgrade unnecessary.

### How does Manifera's experience help with database performance?

Manifera has tuned PostgreSQL performance on enterprise systems for 11+ years. LaunchStudio applies that experience to find the few queries that matter most and fix them without weakening security or rewriting the app.

### Does query performance affect SEO and AI visibility?

Yes, for public pages. Slow server responses affect page speed, user experience and crawl efficiency. Faster queries help both users and the search engines and AI answer engines that access your public content.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is my Supabase app slow with real data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually missing indexes, expensive per-row policies, loading too much data or many separate requests, all fixable without changing platforms." }
    },
    {
      "@type": "Question",
      "name": "Do Row Level Security policies make queries slow?",
      "acceptedAnswer": { "@type": "Answer", "text": "They can if they do per-row lookups without indexes; written with indexes, subselects and explicit filters they add little overhead." }
    },
    {
      "@type": "Question",
      "name": "Should I upgrade my Supabase compute to fix slow queries?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only after optimising; otherwise upgrading only postpones the problem." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with database performance?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has tuned enterprise PostgreSQL for 11+ years, and LaunchStudio fixes the queries that matter without weakening security." }
    },
    {
      "@type": "Question",
      "name": "Does query performance affect SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes for public pages: faster responses improve speed, experience and crawl efficiency." }
    }
  ]
}
</script>
