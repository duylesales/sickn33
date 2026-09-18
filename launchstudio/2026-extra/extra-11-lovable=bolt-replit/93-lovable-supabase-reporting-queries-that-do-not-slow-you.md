---
Title: "Lovable Supabase Reporting: Queries That Do Not Slow You"
Keywords: lovable supabase, reporting, database performance, indexes, materialized views, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# Lovable Supabase Reporting: Queries That Do Not Slow You

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase Reporting: Queries That Do Not Slow You",
  "description": "Dashboards and exports are the queries that take a product down, because they read everything while everyone else is working. Indexes, pre-computation, pagination and keeping reporting away from the live path.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-reporting-queries-that-do-not-slow-you" }
}
</script>

Reporting is where products fall over, and it is always a surprise, because reporting is the part nobody worries about. The booking flow was tested. The payment path was reviewed. The dashboard was a nice-to-have somebody added on a Friday.

Then a customer with three years of history opens it on the first of the month, at the same time as every other customer doing their monthly review, and the entire product becomes unusable for everybody — including the people who were only trying to make a booking.

The reason is structural. Ordinary application queries touch a handful of rows. Reporting queries touch everything, and they do it while everyone else is working.

## Why Reporting Behaves Differently

Three properties.

**It reads a lot.** A total for the year reads a year. An export reads everything. The work is proportional to your customer's history, which grows without anybody deciding it should.

**It is bursty and synchronised.** Month-end, quarter-end, Monday morning. Your customers' calendars align, so the heaviest queries arrive simultaneously.

**It is tolerant of delay and nobody exploits that.** A figure that is an hour old is almost always acceptable in a business dashboard, and almost every implementation computes it live on every page load anyway.

That third point is the opening. Most reporting performance problems are solved not by faster queries but by not running them at the moment somebody looks.

## The Failures That Show Up First

**No indexes on the columns you filter by.** The database reads every row to find the ones matching a date range or a tenant. Fine at a thousand rows, ruinous at a million, and the transition is sudden rather than gradual.

**One query per row.** The dashboard fetches a list, then fetches a detail for each item — a hundred rows becoming a hundred and one round trips. This is the most common generated pattern and the easiest to fix.

**Aggregates computed on every page view.** Six totals, each scanning the same table, recalculated for every visitor refreshing the page.

**Unbounded exports.** "Download all" loads everything into memory, times out at a size nobody tested, and occupies a database connection while it fails.

**Reporting running against the same connections as the application.** One heavy query consumes what the booking flow needed, and a reporting problem becomes an outage.

## Indexes, and Where They Actually Belong

The first thing to check, and the cheapest fix available.

Index the columns you filter and sort by: the tenant column on every table, dates used in ranges, foreign keys used in joins, and any status field you filter on constantly. For queries filtering on two columns together, a single index covering both in the right order usually beats two separate ones.

Two cautions. Indexes cost something on every write, so indexing everything is not the answer — index what your actual queries use. And your access policies filter rows too, which means the columns those policies reference need indexes as much as the ones in your visible query; a product that became slower after row level security was added almost always has this specific gap.

Use your database's query plan to check rather than guessing. Supabase exposes this, and the difference between a query reading an index and one reading the whole table is visible in the first line of the output.

## Pre-Compute Instead of Recomputing

The structural fix, and the one that usually matters more than any individual query.

**Summary tables.** A row per customer per day holding the counts and totals that feed your dashboard, updated as data arrives or rebuilt on a schedule. The dashboard then reads a handful of small rows instead of scanning a year.

**Materialized views** for the same purpose when the aggregation is complex, refreshed on a schedule rather than computed per request.

**Counters maintained by triggers** for the numbers displayed constantly — open items, active members, unread messages. A trigger keeping a count current is cheaper than counting on every page view, and it cannot drift the way application-maintained counters do.

The trade is freshness for speed, and the conversation worth having with customers is what freshness they actually need. In our experience the answer is almost always "this morning is fine" for anything except the record they are currently editing — and the few figures that genuinely must be live can be computed live while the rest are not.

## Exports Belong in the Background

Any export that could exceed a few seconds should be a job rather than a request.

The shape: the customer asks for an export, you accept the request and respond immediately, a background job produces the file, it lands in object storage, and the customer receives a link — signed, expiring, and access-checked. This removes the timeout, removes the held connection, and lets you stream large result sets rather than assembling them in memory.

It also gives you something to log, which matters: a bulk export of personal data is exactly the operation you want an audit record of.

## Keep Reporting Off the Critical Path

Three separations, in increasing order of effort.

**Separate connections.** Give reporting its own pool with a small limit, so a heavy query cannot exhaust what the application needs.

**Separate timing.** Schedule heavy work for quiet hours, and pre-compute before the month-end rush rather than during it.

**Separate infrastructure.** At sufficient scale, a read replica for analytics. This is a real answer and it is further along than most products need; the first two solve the problem for the large majority.

## Watching It Before Customers Do

Log slow queries and look at the list weekly. Record how long your dashboard takes for your largest customer, not your average one, and watch that number over months. Alert when a query exceeds a threshold. And test with realistic volume — a product tested with 50 rows tells you nothing about its behaviour at 50,000, and generating a large sample dataset takes an afternoon.

The pattern to watch for is a number that is fine, fine, fine and then not: database performance degrades suddenly rather than smoothly, because the query planner switches strategy when a table crosses a threshold.

## Let Customers Get Their Own Numbers

A strategic point that resolves part of the performance problem by removing the demand.

A large share of reporting load in small products is not customers using a dashboard. It is customers asking you for figures, and you running a query by hand — which is slow for them, an interruption for you, and frequently done against production with an ad-hoc query nobody reviewed.

**Build the three reports people actually ask for.** After six months you know what they are: a period summary, a per-item breakdown, and an export for their own accountant. Building them properly, pre-computed and paginated, costs less than a year of answering the same request.

**Offer scheduled delivery.** A monthly summary emailed on the first, generated overnight when nothing else is happening, removes the month-end spike entirely — because the report was produced at three in the morning rather than by forty customers at nine.

**Give heavy users a read-only API or a scheduled export** into their own systems. A customer pulling their data on a schedule you control is far cheaper than the same customer refreshing a dashboard, and for business buyers it is a genuine feature rather than a concession.

**Publish what each figure means.** A surprising amount of reporting load is customers re-running a report because they do not trust the number. A one-line definition beside each figure — which dates are included, whether cancelled items count, which time zone the day boundary uses — reduces both the queries and the support emails.

There is a security dimension too. Customers who can serve themselves stop asking you to extract data manually, which is how ad-hoc queries against production and unlogged exports of personal data stop happening.

## Making Reporting Survivable

For a product whose dashboards have started to slow, this is bounded work: the slow queries identified from actual measurements rather than suspicion, indexes added where the query plans show scans including the columns your access policies filter on, per-row query patterns collapsed into single queries, dashboard aggregates moved to summary tables or scheduled views with a freshness your customers have agreed, exports moved to background jobs delivering signed links with an audit record, reporting given its own connection pool, and monitoring added so the next threshold is crossed with warning.

LaunchStudio does this as defined work with a measured before and after. The engineers are Manifera's: eleven years of production database performance work for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us which page is slow and for which customer](https://launchstudio.eu/en/#contact) for a specific diagnosis, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### The First of the Month, Every Month

Maartje Klaassen built Verbruik with Lovable: energy consumption monitoring for housing portfolios, used by six housing associations and two property managers around Almelo and Hengelo, covering about 11,000 homes with meter readings arriving daily.

The product was fine for eighteen months. Then, on the first working day of each month, it became unusable for roughly forty minutes — not slow, unusable, with the booking of inspection appointments timing out entirely.

The cause was the portfolio dashboard, which every association opened on the first to prepare their monthly report. It computed nine figures live, each scanning the full readings table — by then 7.4 million rows — with no index on the date column or the association column. Row level security policies filtered by association on every row, and those columns were unindexed too, so the policy evaluation was scanning as well. Underneath the dashboard, a list of buildings fetched a consumption summary per building, one query each, 340 round trips for the largest association. And the annual export, offered as a button, loaded everything into memory and had been quietly failing for the two largest customers for months — they had assumed the feature did not work and were compiling reports by hand.

Nine business days of work: query plans captured for every dashboard element, which located the scans precisely; indexes added on association, date and meter identifier, including the columns the access policies filter on, which alone cut the dashboard from 47 seconds to 4; a daily summary table introduced holding per-building and per-association aggregates, rebuilt each night and updated as readings arrive, taking the dashboard to under a second; the per-building queries collapsed into one; the export moved to a background job producing a file in object storage delivered by a signed link, with an audit record, which made the annual export work for the two largest associations for the first time; reporting given a separate connection pool; and slow-query logging with alerts added.

**Result:** no month-end incident in the eleven months since. The two associations that had been compiling reports by hand stopped doing so, and one of them mentioned the export in a contract extension.

> *"Every first of the month my product stopped working for forty minutes, and I had assumed it was a hosting problem. It was nine numbers on a dashboard, each reading seven million rows."*
> — **Maartje Klaassen, Founder, Verbruik (Almelo)**

**Cost & Timeline:** €4,600 (query plan analysis, indexing including policy columns, daily summary tables, query consolidation, background export with signed delivery, connection separation, monitoring) — completed in 9 business days.

## Frequently Asked Questions

### Why does my dashboard slow the whole product down?

Because reporting queries read everything while ordinary queries read a few rows, and they arrive in synchronised bursts at month-end. One heavy query can also exhaust the database connections the rest of the application needs.

### What is the first thing to check?

Indexes on the columns you filter and sort by — tenant, dates, foreign keys, status. Check the query plan rather than guessing, and remember that the columns your access policies filter on need indexes too.

### Do dashboard figures have to be live?

Almost never. Ask customers what freshness they need; "as of this morning" is usually fine. Pre-computing into summary tables or scheduled views turns a full scan per page view into reading a handful of small rows.

### How should exports be handled?

As a background job, not a request. Accept the request, produce the file in the background, store it in object storage and deliver a signed, expiring link — with an audit record, since bulk export of personal data is worth logging.

### How do I see this coming?

Log slow queries and review them weekly, track how long the dashboard takes for your largest customer rather than the average, and test with realistic volume. Database performance degrades suddenly rather than gradually, so an average tells you nothing.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my dashboard slow the whole product down?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reporting queries read everything in synchronised month-end bursts, and a heavy one can exhaust the connections the rest of the application needs."
      }
    },
    {
      "@type": "Question",
      "name": "What is the first thing to check?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Indexes on filtered and sorted columns — including the columns your row level security policies filter on — verified with the query plan."
      }
    },
    {
      "@type": "Question",
      "name": "Do dashboard figures have to be live?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely. Pre-compute into summary tables or scheduled views at a freshness customers have agreed, and compute live only the few figures that must be."
      }
    },
    {
      "@type": "Question",
      "name": "How should exports be handled?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "As background jobs producing a file in object storage, delivered by a signed expiring link, with an audit record."
      }
    },
    {
      "@type": "Question",
      "name": "How do I see this coming?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Log slow queries, track timings for your largest customer rather than the average, and test with realistic volume — performance degrades suddenly."
      }
    }
  ]
}
</script>
