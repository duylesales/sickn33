🏃 Femke Smit runs a network of independent running coaches in Nijmegen and built Looplijn with Cursor and Firebase. Coaches create training plans, athletes log their runs, both see progress charts. After two years and around 3,000 athletes, she needed monthly coach reports, an export for a research partner and EU-hosted data. And the Firebase bill had tripled in six months. 📈

The assessment showed why a careful migration mattered: 🧠

❌ Plans stored as nested documents, with athlete names copied in up to twelve places
❌ A progress chart listening to an athlete's entire run history in real time
❌ Security Rules letting any coach read any athlete's data
❌ No way to report across coaches without expensive reads

✅ A relational model for coaches, athletes, plans, sessions, runs and comments
✅ 400+ inconsistent name and email copies resolved with Femke's approval
✅ Row Level Security so coaches see only their own athletes
✅ Users migrated with password hashes, tested with 50 real accounts, and a 40-minute Sunday cutover

At **LaunchStudio**, backed by Manifera's 11+ years of data migrations where losing records was not an option, we move apps from Firebase to Supabase at a fixed price, with a rollback plan. 🛠️

Her result: €5,200, fifteen business days. No athlete reset a password, coach reports became one query and the monthly database cost fell to about a third. 🚀

👉 Firebase to Supabase migration service: https://launchstudio.eu/en/blog/firebase-to-supabase-migration-service

#Firebase #Supabase #Migration #Cursor #AIFounder #LaunchStudio #Manifera
