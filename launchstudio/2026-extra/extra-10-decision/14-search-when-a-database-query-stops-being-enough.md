---
Title: "Search: When a Database Query Stops Being Enough"
Keywords: LIKE query vs full-text search, Postgres full-text search, when to add Elasticsearch, search index premature optimization, database search performance, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Search: When a Database Query Stops Being Enough

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Search: When a Database Query Stops Being Enough",
  "description": "A technical decision tree for search: when a LIKE query is genuinely fine, when Postgres full-text search covers you, and when adding a dedicated search service like Elasticsearch or Algolia is worth the operational cost instead of premature.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/search-when-a-database-query-stops-being-enough" }
}
</script>

Does your product actually need a search engine, or does it need a search *box*? Founders conflate the two constantly, because both look identical from the frontend — a text input and a list of results — and an AI page-builder will happily generate the input either way. What sits behind that box is a decision with real cost on both sides: build too little and search becomes the reason users can't find what they came for; build too much and you're operating a separate service, syncing an index, and debugging relevance scores for a feature three users a week actually touch.

This is the decision tree that actually matters, worked through with the specifics that tell you which branch you're on.

## Branch One: A `LIKE` Query Is Genuinely Fine, and Here's the Test

A query like `WHERE name ILIKE '%search term%'` is the search implementation most AI-generated prototypes ship, and it is not automatically wrong — it's wrong for the wrong dataset and the wrong query pattern, and right for a narrower set of cases than people assume.

`LIKE`/`ILIKE` with a leading wildcard cannot use a standard B-tree index, so every search scans the full table. On a table with a few hundred to a few thousand rows, that scan takes single-digit milliseconds and nobody will ever notice. On a table with a few hundred thousand rows, the same query takes hundreds of milliseconds to seconds, and it gets slower in direct proportion to the table's growth — not the search term's specificity.

The honest test for whether `LIKE` is still fine: run `EXPLAIN ANALYZE` on your actual search query against your actual (or realistically projected) row count, right now, before launch. If it returns in under roughly 50ms, ship it and move on — this is not a place to pre-optimize. If it's already climbing past a few hundred milliseconds at your current data volume, or you can see the table hitting six figures of rows within your first year, `LIKE` has an expiration date you can already see from here, and it's worth solving before launch rather than as an incident during it.

`LIKE` also fails on relevance in ways row count doesn't fix: it matches substrings literally, so it can't handle "restaurant" matching a listing tagged "restaurants," can't rank a title match above a description match, and can't tolerate a typo. If your product's core value is findability — a directory, a marketplace, a knowledge base — these relevance gaps matter even on a small dataset, independent of performance.

## Branch Two: Postgres Full-Text Search Covers More Than Founders Assume

Between `LIKE` and a dedicated search service sits a genuinely underused middle option: Postgres's built-in full-text search, using `tsvector` and `tsquery`, combined with a GIN index. It's already running inside your existing database — no new service, no new sync process, no new bill — and it solves both problems `LIKE` has.

A GIN index on a `tsvector` column turns a search that would otherwise scan the whole table into an actual indexed lookup, bringing response times back down regardless of table size. And `tsvector` handles stemming out of the box — a search for "running" matches rows containing "run" or "ran" — supports ranking multiple matches by relevance with `ts_rank`, and can weight a title match higher than a body-text match, all with SQL you write once and maintain in your existing schema.

The setup is a migration, not a new system: add a `tsvector` column (or a generated column that combines and weights the fields you want searchable), populate it, add a GIN index, and update your search query to use `@@ to_tsquery(...)` instead of `ILIKE`. For English-language content this typically takes an afternoon and handles comfortably into the millions of rows before performance becomes a concern again.

Where it stops being enough: genuine typo tolerance (fuzzy matching beyond stemming), faceted search with complex filter combinations at high query volume, search-as-you-type with sub-50ms latency at scale, and multi-language search with language auto-detection. If your product doesn't need those, Postgres full-text search is very likely the entire search subsystem you need — permanently, not as a stopgap.

## Branch Three: When a Dedicated Search Service Actually Earns Its Keep

Elasticsearch, Meilisearch, Typesense, and Algolia solve real problems Postgres full-text search doesn't: sub-second fuzzy matching that tolerates real-world typos, faceted filtering across many dimensions at once without the query planner buckling, relevance tuning with a purpose-built scoring model, and search-as-you-type responsiveness that feels instant.

The cost side is the part AI tool output — and a lot of generic advice — leaves out. Every dedicated search service is a second data store you now operate: your Postgres database remains the source of truth, and the search index is a derived copy that needs to be kept in sync every time a searchable row is created, updated, or deleted. That sync is either synchronous (added latency and a new failure mode on every write) or asynchronous (a background job, meaning search results can be briefly stale — which is usually fine, but is a decision, not an accident). It's also infrastructure you now monitor, back up or can rebuild from source, and pay for separately — Algolia's pricing scales with records and search volume in a way that can outpace a young product's revenue if it's added before it's needed.

The honest trigger conditions: you need typo tolerance or faceted search that Postgres genuinely can't do well, your search volume or table size has pushed Postgres full-text search past acceptable latency after you've actually tried it, or search is a primary, revenue-driving interaction in your product — a marketplace where discovery *is* the product — rather than a secondary convenience. Absent at least one of those, adding a dedicated search service is solving a problem you don't have yet at the cost of a problem — a second system to run — that you're creating on purpose.

## The Premature Search Service: What It Actually Costs You

The failure mode isn't hypothetical — it's the single most common overcorrection in this subsystem. A founder reads that "real" products use Elasticsearch, wires up a managed instance or an Algolia account before launch, and gets a working search box in a weekend. Then six months in, with 200 total records in the index, they're maintaining a sync job between Postgres and the search service, debugging why a newly created record doesn't show up in search for ninety seconds, paying a monthly bill for infrastructure sized for a scale they're nowhere near, and treating "the search index might be out of sync" as a standing item in their mental model of what could be wrong when a user reports something.

None of that is hypothetical complexity — it's ongoing operational surface area, for a search box that a GIN index on a `tsvector` column would have handled with zero additional moving parts. The cost of premature infrastructure isn't the setup time; it's the permanent tax of running and reasoning about a system you didn't need yet.

## Migrating Later: What It Actually Involves

The good news, and the reason "start with Postgres, upgrade later" is a genuinely sound default rather than technical debt: moving from Postgres full-text search to a dedicated service is additive, not a rewrite. Your Postgres tables stay exactly as they are — the search service reads from them, doesn't replace them. The work is: standing up the service, writing an initial bulk-index job to populate it from your existing data, adding sync logic (a database trigger, a change-data-capture stream, or application-level hooks on write) to keep it current, and swapping your search endpoint to query the new service instead of Postgres.

For a typical single-entity search feature — searching one primary table like listings, products, or documents — this is realistically a few days to a week of focused work, not a re-architecture, precisely because the schema decision underneath it (your actual data model) didn't need to change to support either approach. That's the payoff of starting with the simpler option: you're not locked out of the more capable one later, and you've avoided paying its operational cost for however many months you didn't need it.

## Worked Example: Sizing the Decision Against Real Numbers

Concrete numbers make this easier to apply than abstract advice. A directory with 3,000 listings, searched a few hundred times a day: `LIKE` is fine indefinitely at that volume; even full-text search is arguably more than necessary, though it costs almost nothing to add and improves relevance meaningfully. A support knowledge base with 15,000 articles, growing steadily, where users routinely search close variations of the same terms: Postgres full-text search with proper stemming and ranking is very likely the right permanent home, unlikely to need replacing. A marketplace with 500,000 active listings, faceted by category, price, location, and availability, searched tens of thousands of times a day, where a slow or irrelevant result directly costs a transaction: this is squarely dedicated-search territory, and building it on `LIKE` first would mean a rebuild under pressure rather than a planned upgrade.

The pattern across all three: table size alone doesn't decide it — query pattern, relevance requirements, and how central search is to the product's core value do.

## Making the Call for Your Product

Run your own search query with `EXPLAIN ANALYZE` against your real or realistically projected data before deciding anything. If it's fast, you're done — resist the urge to add infrastructure "to be safe." If it's slow or the relevance is visibly bad, Postgres full-text search resolves both for the overwhelming majority of products and costs a migration, not a new system. Reach for a dedicated search service only once you've hit one of the genuine trigger conditions above, not because a tutorial assumed you'd need it from day one.

This is exactly the kind of infrastructure decision [Manifera's engineers](https://www.manifera.com/about-us/manifera-technologies/) get asked to weigh in on mid-build — not because the code is wrong, but because nobody stopped to check which branch of this tree the product was actually on. If you're not sure which one you're on, [describe your project and you'll get a reply within one business day](https://launchstudio.eu/en/#contact) with a straight answer.

## Real example

### A Knowledge-Base Product Nearly Bought Infrastructure It Didn't Need

Dorin Ionescu was building Clarifox, an internal knowledge-base tool for small customer support teams, in Bolt. With around 8,000 articles projected within the first year and a search box that felt sluggish in testing, he'd already requested a quote for an Algolia integration, assuming that was simply what "good search" required.

A quick check told a different story: the sluggishness wasn't table size — it was an unindexed `ILIKE` query against a table with only 400 seed articles, plus an N+1 query loading each result's tags separately. `EXPLAIN ANALYZE` showed the actual query taking 340ms, almost entirely index-free scanning that would only get worse as content grew, not evidence that Postgres itself couldn't handle the job.

The fix replaced the `ILIKE` query with a `tsvector` column, a GIN index, and `ts_rank`-based relevance ordering across title and body with title weighted higher, and fixed the N+1 tag loading in the same pass. Search response time dropped to under 15ms at the target 8,000-article volume in load testing, with proper relevance ranking Algolia would have needed separate configuration to match.

**Result:** Clarifox shipped without a second infrastructure bill, and the search feature now returns typo-tolerant-enough, relevance-ranked results using nothing beyond the Postgres database it already runs.

> "I was ready to pay a monthly search bill because I assumed that's just what search costs. Turns out my search problem was an indexing problem, not a 'need a different database' problem."
> — **Dorin Ionescu, Founder, Clarifox (Bucharest)**

**Cost & Timeline:** Launch Ready engagement, search and query performance review — delivered in 3 business days.

## Frequently Asked Questions

### How do I know if my search query is actually slow, or just feels slow?

Run `EXPLAIN ANALYZE` on the exact query your search feature executes, against your real or realistically projected row count. The output shows actual execution time and whether it's doing a sequential scan (bad, at scale) or using an index. Trust that number over subjective impressions from testing on a small seed dataset.

### Can I add Postgres full-text search without any downtime?

Yes. Adding a `tsvector` column and a GIN index is a normal migration that doesn't lock the table for reads or writes in any way users would notice, especially if you use `CREATE INDEX CONCURRENTLY` for the index build itself.

### Does Postgres full-text search handle typos?

It handles word variation through stemming — matching "running" to "run" — but not true typo tolerance, like matching "recieve" to "receive." If typo tolerance is genuinely important to your product, that's one of the legitimate triggers for a dedicated search service.

### What happens to my search results while a dedicated search index is syncing?

If sync is asynchronous, which is the common and usually correct choice, there's a brief window — typically seconds — where a newly created or updated record won't yet appear in search results. Whether that's acceptable depends on your product; for most use cases it is.

### Is it a mistake to start with a dedicated search service if I can afford it?

Not a mistake exactly, but an unnecessary cost and operational burden if your data volume and relevance needs don't require it yet. The stronger argument for starting simple isn't affordability — it's that you avoid running and monitoring a second system before you have evidence you need its specific capabilities.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I know if my search query is actually slow, or just feels slow?", "acceptedAnswer": { "@type": "Answer", "text": "Run EXPLAIN ANALYZE on the exact search query against your real or realistically projected row count. It shows actual execution time and whether it's doing a sequential scan or using an index, which is more reliable than impressions from a small seed dataset." } },
    { "@type": "Question", "name": "Can I add Postgres full-text search without any downtime?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Adding a tsvector column and a GIN index is a normal migration, and using CREATE INDEX CONCURRENTLY for the index build avoids locking the table in any way users would notice." } },
    { "@type": "Question", "name": "Does Postgres full-text search handle typos?", "acceptedAnswer": { "@type": "Answer", "text": "It handles word variation through stemming, like matching running to run, but not true typo tolerance such as matching recieve to receive. Genuine typo tolerance is one of the legitimate reasons to consider a dedicated search service." } },
    { "@type": "Question", "name": "What happens to my search results while a dedicated search index is syncing?", "acceptedAnswer": { "@type": "Answer", "text": "With asynchronous sync, which is usually the right choice, there's a brief window, typically seconds, where a newly created or updated record won't yet appear in results. This is acceptable for most products." } },
    { "@type": "Question", "name": "Is it a mistake to start with a dedicated search service if I can afford it?", "acceptedAnswer": { "@type": "Answer", "text": "Not a mistake exactly, but an unnecessary cost and operational burden without a real need. The stronger case for starting simple is avoiding a second system to run and monitor before there's evidence its specific capabilities are required." } }
  ]
}
</script>
