🚨 Wendy Roos's Verzuimlijn handles absence registration for 140 employers covering about 4,000 employees. For eight months it was fine. Then the dashboard - the first screen every user opens - started taking four to six seconds, worst between nine and ten in the morning. One customer asked whether the product could handle their size. 😳

The absence table had 310,000 rows and exactly one index: its primary key. Here's what gets slow first as your data grows: 🧠

❌ No indexes on foreign keys - every filter read the whole table
❌ A dashboard query that scanned and sorted 310,000 rows for every user
❌ An N+1 pattern: 25 rows, each fetching its employee separately
❌ A total row count on a list page that grew with the data

✅ Query statistics ranked by total time - the dashboard used 71% of database time
✅ A composite index on employer and date, built concurrently via a migration
✅ Indexes on the six foreign key columns that had none, and the N+1 fetch rewritten as one query
✅ The total count replaced with a next-page control - and unused indexes dropped after a month

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find whether your slow page is indexes or queries - usually in hours, not a rebuild. ⚡

Her result: two business days and €1,600 later, the dashboard went from 4.2 seconds at peak to 180 milliseconds on the same plan. Peak database CPU fell from above 80% to under 15% - cancelling a €340/month upgrade she'd budgeted for. 🚀

👉 Indexes and the queries that get slow first: https://launchstudio.eu/en/blog/lovable-supabase-indexes-and-the-queries-that-get-slow-first

#Supabase #PostgreSQL #Performance #Lovable #LaunchStudio #Manifera
