⏱️ 4.2 seconds ➜ 180 milliseconds

Same dashboard. Same hardware. Same plan.

Wendy Roos runs Verzuimlijn, built in Lovable: absence registration for small employers, used by 140 companies covering around 4,000 employees. For eight months, all was well. Then the dashboard, the first screen every user opens, started taking four to six seconds, worst between nine and ten in the morning, when most users log in. Two customers complained. One asked whether the product could handle their size.

Wendy assumed she'd outgrown her plan, and budgeted €340 a month for an upgrade.

WHERE THE SECONDS WENT
⏳ The absence records table had 310,000 rows, and one index: its primary key
⏳ The dashboard filtered by employer and sorted by date, so the database read and sorted all 310,000 rows, for every user, every time
⏳ The morning peak was simply many people doing that at once
⏳ Query statistics: that one query used 71% of all database time
⏳ Plus an N+1 pattern: each of 25 absence rows fetched its employee record separately

WHERE THEY CAME BACK (LaunchStudio, 2 business days, €1,600)
⚡ EXPLAIN ANALYZE confirming the sequential scan and external sort
⚡ A composite index on employer and date descending, created concurrently through a migration
⚡ Indexes on the six foreign key columns across the schema that had none
⚡ The N+1 pattern fixed
⚡ The total record count replaced by a next-page control
⚡ A month later, index usage reviewed, and two speculative indexes dropped

THE NEW READINGS
Dashboard at morning peak: 180 ms
Database CPU at peak: from routinely above 80% to under 15%
Planned €340-a-month upgrade: cancelled

Nobody had told Wendy indexes were a thing she was supposed to create.

"I assumed I had outgrown the plan and needed to pay for a bigger one. It turned out I had never created a single index, and nobody had told me that was a thing I was supposed to do." - Wendy Roos

https://launchstudio.eu/en/blog/lovable-supabase-indexes-and-the-queries-that-get-slow-first

#Supabase #PostgreSQL #Performance #Lovable #LaunchStudio #Manifera
