🚨 Lieke added one index to speed up slow queries. It ran instantly in staging against 900 rows. Production held 2.4 million trips — and the lock took her product offline for nine minutes during evening shifts. 😳

Founders treat schema changes like they did before launch: instant, reversible, no big deal. Here's why that instinct becomes dangerous: 🧠

❌ Prompting a schema change during building is a five-second action with no memory of what "live data" means
❌ A standard index build locks writes on the whole table for its duration — imperceptible at 900 rows, over nine minutes at 2.4 million
❌ A planned address-field migration was written as one step that would drop the original column, tested against the same 900 staging rows
❌ Two duplicate driver entries were created when a retried request landed during the outage

✅ Use expand-and-contract: add new structure alongside the old, write to both, backfill in the background, then switch reads over
✅ Build indexes concurrently instead of with a standard lock
✅ Test every migration against a restored copy of production, timed for real
✅ Keep every schema change in version control, applied through a migration tool — never typed into a console

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we plan and execute live migrations so customers never notice the change happened. 🗄️

Her result: the index rebuilt concurrently, migrations moved into version control, and the address change re-planned as expand-and-contract — the backfill caught 3,100 addresses the naive transformation would have gotten wrong. 🚀

👉 Learn the pattern that makes schema changes safe on live data: [Link to article]

#SaaS #DatabaseMigration #IndieHacker #FounderLife #LaunchStudio #Manifera
