---
Title: "Lovable Supabase: Indexes and the Queries That Get Slow First"
Keywords: lovable supabase, database indexes, slow queries, Postgres performance, query plans, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Indexes and the Queries That Get Slow First

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Indexes and the Queries That Get Slow First",
  "description": "An AI-built app is fast with 200 rows and slow with 200,000. Which queries degrade first, how to find them in Supabase, the four indexes most products actually need, and what an index costs you.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-indexes-and-the-queries-that-get-slow-first" }
}
</script>

Nothing about your app changed. You did not deploy anything. But the page that used to open instantly now takes four seconds, and the only thing that is different is that you have more customers than you did in spring.

This is the most predictable performance problem in software and it has a specific cause. Without an index, a database answers "find me the rows where this column equals that" by reading every row in the table. At 200 rows nobody notices. At 200,000 it is four seconds, and at two million it is a timeout.

AI coding tools create tables and write queries. They rarely create the indexes those queries need, because with the amount of data present during development there is nothing to notice.

## Find the Slow Ones Before Guessing

Do not add indexes by intuition. Supabase exposes query statistics — every statement your application has run, how often, and how much total time it consumed — and it is the only honest source.

Sort by total time rather than by the slowest single execution. A query taking 900 milliseconds that runs once a day matters far less than one taking 40 milliseconds that runs on every page load, and founders optimise the wrong one constantly because the slow number is more alarming.

Then take your worst offender and ask the database to explain itself. Running `EXPLAIN ANALYZE` in front of a query returns the plan it used and the time each step took. You are looking for one phrase: a sequential scan on a large table. That means the whole table was read. Combined with a filter on one column, it is an index waiting to be created.

The same applies to sorting. A plan showing an expensive sort step on a large result set, feeding into a limit, is a list page in your product that will get worse every week.

## The Four Indexes Most Products Need

For a typical Lovable and Supabase application, four cover the overwhelming majority of the problem.

**Every foreign key.** Postgres indexes primary keys automatically and does not index the columns that point at them. Any table with `user_id`, `organisation_id`, `project_id` needs an index on it, because every query in your product filters by one of those. This alone fixes most small applications.

**The tenancy column, first.** If your app is multi-tenant, nearly every query begins with "the rows belonging to this organisation". That column belongs first in a composite index, with whatever you filter or sort by next: `(organisation_id, created_at desc)` serves both the filter and the ordering in one structure.

**Anything you sort a list by.** Usually `created_at` on the tables behind your main screens, and usually alongside the tenancy column rather than alone.

**Columns used for lookup by a value users type.** Email, reference number, slug. These want unique indexes, which both speed the lookup and prevent the duplicate you would otherwise discover in production.

Add them one at a time and measure. An index that does not change a plan is an index you are paying for and not using.

## What an Index Costs

Indexes are not free and the trade is worth understanding, because the instinct after reading the above is to index everything.

Every index consumes storage, and more importantly every index must be updated on every insert, update and delete of the indexed column. A table with eleven indexes writes considerably slower than the same table with three. For a product doing far more reading than writing — which is most — the trade favours indexes heavily. For a table receiving high-volume writes, such as an event or logging table, be sparing.

Unused indexes are pure cost. Postgres tracks how often each one has been used, and reviewing that after a few months of real traffic usually reveals two or three that were added speculatively and never touched. Drop them.

## The Problem That Looks Like a Slow Database

Before adding anything, check whether your problem is actually the number of queries rather than the speed of each one.

The pattern: a page lists 50 projects, and for each project the code fetches its owner. That is 51 queries where two would do. Each is fast, the page is slow, and no index will help.

This is endemic in AI-generated code because it is the natural way to express the logic — get the list, then loop over it. The fix is to fetch related data in one query rather than in a loop, which in Supabase means selecting the related table alongside the main one rather than calling the client inside a loop.

Distinguishing the two cases takes thirty seconds: if your slow page produced dozens of fast queries, it is this. If it produced three slow ones, it is indexes.

## Count Carefully

`SELECT count(*)` on a large table is slower than people expect, because Postgres genuinely counts. On a list page with pagination, that count often costs more than fetching the page itself.

Three options, in order of preference for small products. Do not show a total at all — "showing 1-25" with a next button is sufficient for most interfaces. Show an approximate count, which the database can estimate cheaply. Or maintain a counter yourself if the number is genuinely important, updated as rows are created and deleted.

The general principle applies beyond counting: a number displayed in the corner of a page is rarely worth a query that grows with your data.

## Adding Indexes to a Live Table

On a table with real data, creating an index normally locks writes while it builds, which on a large table means a period where your application cannot insert anything.

Postgres offers a concurrent build that does not take that lock. It is slower and occasionally fails, leaving an invalid index that must be dropped and retried — but it does not stop your product working, which is the property you want at four in the afternoon.

Two habits go with it. Create indexes through migration files rather than by typing into a dashboard, so that your staging and production databases stay identical and the change is recorded. And measure the same query before and after, because an index that did not change the plan means the database decided not to use it, and knowing that immediately is better than assuming it worked.

## Partial Indexes and the Rows You Never Query

One refinement worth knowing, because it applies to almost every product and costs nothing.

Most applications query a fraction of their data over and over. Open tickets, active subscriptions, unarchived projects, unprocessed jobs. The closed, cancelled and archived rows accumulate forever and are almost never read, yet a normal index dutifully includes every one of them.

A partial index covers only the rows matching a condition — active records, say — which makes it dramatically smaller, faster to search and cheaper to maintain. On a table where 95 percent of rows are historical, the difference is not marginal.

The catch is that the database only uses a partial index when the query's condition matches the index's condition, so the filter has to appear in the query itself. That is usually already true: the screens that feel slow are the ones showing current work.

The same thinking applies to a queue table. An index over pending jobs only, rather than every job ever run, keeps the polling query fast no matter how much history accumulates behind it — and history accumulating behind a working queue is precisely what happens to every successful product.

## When Indexes Are Not the Answer

Three situations look like an indexing problem and are not, and recognising them saves a day.

**Search across text.** Filtering on a word appearing anywhere in a description cannot use an ordinary index. That needs full-text search, which Postgres supports natively, or a dedicated search service — and reaching for one before the other is a decision worth making deliberately.

**Aggregations over everything.** A dashboard summing every transaction since launch will get slower forever regardless of indexes, because the work grows with your history. Those numbers belong in a summary table updated as data arrives, or computed nightly.

**Row-level security doing more work than you think.** Supabase policies are conditions applied to every query, and a policy containing a subquery against another table executes for each row considered. A slow query with a simple plan and an expensive policy is a policy problem, and the fix is to make the policy's own lookup indexed — or to restructure it so it compares against a value already on the row.

## Setting This Up

For a running Supabase application this is typically one to two days: query statistics reviewed and ranked by total time, plans captured for the worst offenders, foreign key indexes created across the schema, composite indexes for tenancy and sort order on the tables behind your main screens, unique indexes on natural lookup columns, N+1 query patterns rewritten to fetch related data in one statement, expensive counts removed or estimated, everything applied through migrations with concurrent builds, and a note of the before-and-after timings so the next person can see what was done and why.

LaunchStudio does this as part of production readiness, and it is usually the cheapest performance work available to a growing product — hours rather than a rebuild. The engineers are Manifera's: eleven years, 160+ projects, Postgres in production long before it was fashionable.

[Send us your slowest page](https://launchstudio.eu/en/#contact) and we will tell you whether it is indexes or queries.

## Real example

### Four Seconds at Nine in the Morning

Wendy Roos runs Verzuimlijn, built in Lovable: absence registration for small employers, used by 140 companies covering around 4,000 employees.

Everything was fine for eight months. Then the dashboard — the first screen every user opens — began taking four to six seconds, always worst between nine and ten in the morning when most of her users log in at once. Two customers complained and one asked whether the product could handle their size.

The absence records table had reached 310,000 rows and had exactly one index: its primary key. The dashboard query filtered by employer and sorted by date, so the database read all 310,000 rows and sorted them, every time, for every user. The morning peak was simply many people doing that at once.

Two business days: query statistics reviewed, showing the dashboard query consuming 71 percent of total database time; `EXPLAIN ANALYZE` confirming a sequential scan and an external sort; a composite index on employer and date descending, created concurrently through a migration; indexes added on the six foreign key columns across the schema that had none; an N+1 pattern on the same dashboard fixed, where each of 25 absence rows fetched its employee record separately; the total record count replaced with a next-page control; and index usage reviewed a month later, with two speculative indexes dropped.

**Result:** the dashboard went from 4.2 seconds at the morning peak to 180 milliseconds, on the same hardware and the same plan. Wendy's database CPU during peak hours fell from routinely above 80 percent to under 15, which removed a planned upgrade she had budgeted €340 a month for.

> *"I assumed I had outgrown the plan and needed to pay for a bigger one. It turned out I had never created a single index, and nobody had told me that was a thing I was supposed to do."*
> — **Wendy Roos, Founder, Verzuimlijn (Helmond)**

**Cost & Timeline:** €1,600 (query analysis, composite and foreign key indexes via concurrent migrations, N+1 remediation, count removal, index usage review) — completed in 2 business days.

## Frequently Asked Questions

### How do I know which queries are slow?

Use Supabase's query statistics and sort by total time consumed, not by the slowest single run. A 40-millisecond query on every page load usually matters more than a one-second query that runs nightly.

### Should I just index every column?

No. Each index slows every write to that table and consumes storage. Index foreign keys, tenancy columns, sort columns and natural lookup keys, then review usage after a few months and drop what is untouched.

### Why is my page slow when every query is fast?

Because there are dozens of them — a list fetching related data in a loop. No index fixes that; fetching the related rows in one query does.

### Is it safe to add an index to a live table?

Use a concurrent build, which avoids locking writes while the index is created. Apply it through a migration rather than the dashboard so staging and production stay identical.

### Why is counting rows so slow?

Postgres counts genuinely rather than storing a total. On large tables, drop the total from list pages, show an estimate, or maintain your own counter if the number really matters.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I find slow queries in Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use query statistics sorted by total time consumed rather than slowest single execution, then run EXPLAIN ANALYZE on the worst offenders."
      }
    },
    {
      "@type": "Question",
      "name": "Should I index every column?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Every index slows writes and costs storage. Index foreign keys, tenancy and sort columns and lookup keys, then drop unused ones after real traffic."
      }
    },
    {
      "@type": "Question",
      "name": "Why is my page slow when every query is fast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You are running dozens of them — related data fetched inside a loop. Fetch it in a single query instead; no index will help."
      }
    },
    {
      "@type": "Question",
      "name": "Is it safe to add an index to a live table?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use a concurrent build so writes are not locked, and apply it through a migration so staging and production stay identical."
      }
    },
    {
      "@type": "Question",
      "name": "Why is counting rows slow in Postgres?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It counts genuinely rather than storing a total. Remove totals from list pages, use an estimate, or maintain your own counter."
      }
    }
  ]
}
</script>
