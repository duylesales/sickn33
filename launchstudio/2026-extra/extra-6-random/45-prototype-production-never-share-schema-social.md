🗄️ Amber Schouten built VoorraadKoppel, an inventory sync tool, using Cursor — with test data and real production data living in the exact same database schema. She ran a migration script that had worked fine during testing. It updated every row matching its criteria — which now included live customer inventory counts. 😳

No structural boundary meant "the database" was really just one database, for everything. 🧠

❌ A routine migration script corrupted live customer inventory records along with the test data it was meant to touch
❌ Nothing about the script itself was unusual — it did exactly what it was written to do
❌ Several customers' stock levels were silently altered before anyone noticed
❌ No AI tool ever flagged that this separation was missing

✅ Rebuild the data layer with a genuinely separate test environment
✅ Restore affected records from available backups
✅ Add safeguards so future scripts need an explicit override to touch production

At **LaunchStudio**, our engineers in Singapore treat environment separation as a standard check on every AI-built project before it goes live — the same rigor behind Manifera's 160+ delivered projects. 🛡️

Her result: VoorraadKoppel now runs test and production on fully separated infrastructure, with a documented sign-off process before any future migration touches live data. 🚀

👉 Not sure if your test and production data are actually separated: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #DatabaseSchema #AIDevelopment
