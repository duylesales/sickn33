🚨 Wessel Hofman built Storingsboek with Lovable and Supabase: maintenance companies log repair requests, assign technicians and track work orders. His largest customer reached around 180,000 work orders - and the main dashboard took nine seconds to load. 😳

Technicians said their mobile assignment list was barely usable. Wessel was ready to blame Supabase. Here's how to find and fix slow Supabase queries: 🧠

❌ All open work orders loaded with every column, filtered in JavaScript
❌ Separate requests per work order for technician and property
❌ An RLS policy querying team membership for every row, unindexed
❌ No indexes on key filters, and search using ilike '%term%'

✅ Composite indexes for common filters and sorts
✅ A rewritten policy with (select auth.uid()) and an indexed membership lookup
✅ A view with only needed columns, joined names and keyset pagination
✅ Status counts from a trigger-updated summary table and trigram search, tested at production scale

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we stop your app asking the database to do the same work hundreds of times. 🛠️

His result: €3,100, 8 business days. The dashboard loads in about 400 milliseconds, mobile lists in under half a second, and database CPU dropped by more than half. 🚀

👉 Is your Supabase app getting slower? Here's how to find and fix slow queries: https://launchstudio.eu/en/blog/slow-supabase-queries-how-to-find-and-fix-them

#Supabase #Postgres #Performance #PropTech #AIFounder #LaunchStudio #Manifera
