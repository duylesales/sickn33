🚨 Rosa Jacobs built Klantdossier with Lovable and Supabase: a CRM for insurance and mortgage advisers, used daily by about 120 advisers. On a Monday morning, she asked Lovable to rename client_name to full_name and split addresses into separate columns. The builder applied it straight to production. 😳

For about forty minutes, advisers saw errors on every client page. Here's how to run zero-downtime database migrations in Supabase: 🧠

❌ A rename that broke every query in open browser tabs
❌ An address split rewriting a large table while holding a lock
❌ An index blocking writes
❌ A migration history out of sync, with policies only in the dashboard

✅ Service restored with a compatibility view and a frontend redeploy
✅ A clean migration baseline including all policies and functions
✅ Production separated from the Lovable-connected staging, with reviewed migrations via GitHub
✅ Expand and contract with batched backfills, concurrent indexes and lock timeouts

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we teach your database to change tyres while the car keeps driving. 🛠️

Her result: €3,400, 9 business days. Rosa has since shipped over forty schema changes without downtime - and review caught an AI migration that tried to drop and recreate a table. 🚀

👉 Changing your database schema? Here's how to do it without downtime: https://launchstudio.eu/en/blog/zero-downtime-database-migrations-in-supabase

#Supabase #Postgres #DatabaseMigrations #Lovable #AIFounder #LaunchStudio #Manifera
