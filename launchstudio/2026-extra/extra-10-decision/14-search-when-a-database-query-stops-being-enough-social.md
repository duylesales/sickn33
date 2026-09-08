🚨 Dorin had already requested an Algolia quote for Clarifox's "sluggish" search. The real culprit was a 340ms query against 400 rows. 😳

"Real" search doesn't automatically mean a new service — sometimes it means an index nobody added: 🧠

❌ The sluggishness wasn't table size — it was an unindexed `ILIKE` query plus an N+1 call loading tags separately
❌ `LIKE` with a leading wildcard can't use a B-tree index, so every search scans the full table regardless of relevance
❌ A dedicated search service means a second data store to sync, monitor, and pay for — before you've proven you need it
❌ Six months in at 200 records, a premature search index becomes a standing "might be out of sync" worry, not a feature

✅ Run `EXPLAIN ANALYZE` against real or realistically projected row counts before deciding anything
✅ Add a `tsvector` column and a GIN index — it's a migration, not a new system, and it's already inside Postgres
✅ Let `ts_rank` weight title matches over body matches instead of reaching for a scoring service
✅ Fix the N+1 query in the same pass — relevance and speed are often two separate bugs, not one

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we size your search problem against real numbers before anyone signs up for infrastructure you don't need yet. 🔍

His result: Clarifox shipped without a second infrastructure bill — search response time dropped to under 15ms at the target 8,000-article volume, with relevance ranking Algolia would have needed separate configuration to match. 🚀

👉 Find out which branch of the search decision tree you're actually on: https://launchstudio.eu/en/blog/search-when-a-database-query-stops-being-enough

#IndieHacker #Postgres #ProductionReady #SaaS #LaunchStudio #Manifera
