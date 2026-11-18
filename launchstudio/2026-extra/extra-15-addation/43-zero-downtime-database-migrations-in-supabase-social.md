🍳 RECIPE: How to rename a column without ruining Monday morning

First, the version that went wrong.

Rosa Jacobs built Klantdossier with Lovable and Supabase: a CRM for small insurance and mortgage advisers, used daily by about 120 of them. One Monday morning she asked Lovable to rename client_name to full_name and split addresses into separate columns. The builder applied it straight to production.

For about forty minutes, advisers saw errors on every client page:
• The rename broke every query in the app version still open in their browsers
• The address split rewrote the large clients table while holding a lock
• An index created in the same change blocked writes

Underneath: the repo's migration history no longer matched production, and several RLS policies existed only in the dashboard.

THE SAFE RECIPE (LaunchStudio, 9 business days, €3,400)

To restore service:
1. Add a compatibility view and redeploy the frontend

To prepare the kitchen:
2. Rebuild a clean migration baseline from production, including all policies and functions
3. Separate production from the Lovable-connected staging project
4. Send every migration through GitHub, with review

To split the addresses properly (expand and contract):
5. Add the new columns
6. Backfill them with a batched script
7. Write to both old and new, then switch reads
8. Create indexes concurrently
9. Set a lock timeout on migrations

To keep it that way:
10. A short guide in the repo explaining the patterns

SERVES
Forty-plus schema changes since, all without downtime. When an AI-generated migration once tried to drop and recreate a table, the review step caught it before production.

"I used to think a database change was like editing a spreadsheet column. Now I know it's more like changing a tyre while the car is driving." - Rosa Jacobs

https://launchstudio.eu/en/blog/zero-downtime-database-migrations-in-supabase

#Supabase #Postgres #DatabaseMigrations #Lovable #AIFounder #LaunchStudio #Manifera
