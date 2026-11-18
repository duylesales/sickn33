⏱️ 9 seconds ➜ 400 milliseconds

That's the main dashboard of Storingsboek, before and after.

Wessel Hofman built Storingsboek with Lovable and Supabase: property maintenance companies log repair requests, assign technicians and track work orders. After a year, his biggest customer, a maintenance company serving several housing associations, had around 180,000 work orders. The dashboard took nine seconds. Technicians said their mobile assignment list was barely usable.

WHERE THE SECONDS WENT
⏳ All open work orders loaded with every column, long descriptions and history included, then filtered in JavaScript
⏳ A separate request per work order for its technician and its property: hundreds of requests per page
⏳ An RLS policy calling a function that checked team membership for every row, with no index on the membership table
⏳ No indexes on organisation_id, status or assigned_to
⏳ Search using ilike '%term%' on descriptions

WHERE THEY CAME BACK (LaunchStudio, 8 business days, €3,100)
⚡ Composite indexes for the most common filters and sorts
⚡ The policy rewritten with (select auth.uid()) and an indexed membership lookup, plus explicit organisation filters
⚡ A view returning exactly the needed columns, with technician and property names joined in
⚡ Keyset pagination for long lists
⚡ Status counts from a summary table kept up to date by triggers
⚡ Search on a trigram index over titles and addresses
⚡ Everything tested on staging with production-scale synthetic data

THE NEW TIMES
Dashboard: about 400 ms
Technicians' lists on mobile networks: under half a second
Database CPU during working hours: down by more than half
Planned compute upgrade: postponed

"I was ready to blame Supabase. It turned out my app was asking the database to do the same work hundreds of times on every page." - Wessel Hofman

https://launchstudio.eu/en/blog/slow-supabase-queries-how-to-find-and-fix-them

#Supabase #Postgres #Performance #PropTech #AIFounder #LaunchStudio #Manifera
