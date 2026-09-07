🚨 Elin merged two duplicate client records in Ferndesk. Fourteen appointments vanished from the calendar view with zero warning. 😳

A missing foreign key doesn't slow anything down — it just lets your data quietly stop being true: 🧠

❌ Cursor wired `appointments.client_id` correctly in every happy-path flow, but never added the actual foreign key constraint
❌ Nullable columns look harmless until a `SUM()` silently skips the NULL rows in your revenue dashboard
❌ Renaming a column in production isn't a rename — it's four to five staged deploys, not one `ALTER TABLE`
❌ Missing indexes never show up on seed data — they show up as a 4ms query turning into 4 seconds at 500,000 rows

✅ Add the foreign key with `ON DELETE RESTRICT` — it turns a silent data loss into a blocked action you can see
✅ Walk every column and ask "can this legitimately be unknown" before deciding it stays nullable
✅ Track `created_at` and `updated_at` on every table now — you can't backfill history you never captured
✅ A schema and migration audit is one to two focused days, well within LaunchStudio's €800–€3,500 Launch Ready band

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit the schema decisions your AI tool made by omission before real rows make them expensive to fix. 🗄️

Her result: the fourteen missing appointments were recovered and reassigned within a day, and the same constraint has since silently blocked three further attempted deletes-with-dependents. 🚀

👉 Get your schema reviewed before it has real data to protect: [Link to article]

#IndieHacker #Postgres #ProductionReady #SaaS #LaunchStudio #Manifera
