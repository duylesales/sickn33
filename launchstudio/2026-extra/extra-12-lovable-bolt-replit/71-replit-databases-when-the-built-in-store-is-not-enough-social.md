🚨 Vera Slothouber's Materieelverhuur runs equipment rental for nine construction hire companies - around 1,400 machines. Everything lived in Replit's built-in key-value store. Then two things broke at once: the monthly utilisation report - every customer's most-used feature - started timing out, and a customer name change missed 60 records, so invoices showed two names for the same business. 😳

She had been hand-maintaining lists of keys and updating names in hundreds of copies. Without noticing, she'd written a database - one with no constraints. Here's how to tell you've outgrown the built-in store: 🧠

❌ Maintaining your own key lists just to find records
❌ Reports that read every record ever created and count in code
❌ Customer names copied into every rental instead of referenced
❌ Nothing preventing orphaned references or duplicates

✅ Five entities modelled from the business; a Postgres schema with foreign keys and an organisation ID on every table
✅ A migration script run six times against a copy - surfacing 140 orphaned rentals and 31 duplicate customers, each resolved by decision
✅ Four days of dual-writing with daily comparison, which caught two write paths the migration had missed
✅ Reads switched area by area, the old store kept for three weeks, backups set up with a tested restore

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we take Replit products to production - including the database migration, with zero downtime. ⚙️

Her result: €3,800, three business days. The utilisation report went from timing out to 400 milliseconds, and the name-change problem became structurally impossible. 🚀

👉 Replit databases: when the built-in store is not enough: https://launchstudio.eu/en/blog/replit-databases-when-the-built-in-store-is-not-enough

#Replit #Postgres #Database #DataModelling #LaunchStudio #Manifera
