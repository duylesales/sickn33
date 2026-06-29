# Social Media Post: Database Migration Strategies for AI SaaS

If you rename a column in your Supabase database and immediately push the code, your AI app will crash. 

AI workloads have massive write-volume and long transaction times (generating embeddings). If you lock the table during a migration, you lose data and burn OpenAI credits.

You must use the "Expand and Contract" pattern:
1️⃣ Expand: Add the new column (keep the old one). Update code to write to both.
2️⃣ Migrate: Backfill the old data in small batches to avoid locking. Update code to read from the new column.
3️⃣ Contract: Drop the old column a week later.

Never rename. Never drop immediately. Always use `CREATE INDEX CONCURRENTLY`.

Read our full guide to zero-downtime migrations for AI startups on the LaunchStudio blog.

#LaunchStudio #Supabase #Postgres #DatabaseMigrations #AISaaS #Nextjs
