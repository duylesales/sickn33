# Social Media Post (Dutch): Database Migration Strategies for AI SaaS

Als u een kolom hernoemt in uw Supabase-database en de code onmiddellijk pusht, crasht uw AI-app.

AI-workloads hebben een enorm schrijfvolume en lange transactietijden (het genereren van embeddings). Als u de tabel tijdens een migratie vergrendelt, verliest u data en verspilt u OpenAI-credits.

U moet het "Expand and Contract" patroon gebruiken:
1️⃣ Expand: Voeg de nieuwe kolom toe (behoud de oude). Update de code om naar beide te schrijven.
2️⃣ Migrate: Vul de oude data aan in kleine batches om vergrendeling te voorkomen. Update de code om te lezen uit de nieuwe kolom.
3️⃣ Contract: Verwijder de oude kolom een week later.

Nooit hernoemen. Nooit onmiddellijk verwijderen. Gebruik altijd `CREATE INDEX CONCURRENTLY`.

Lees onze volledige gids voor zero-downtime migraties voor AI-startups op de LaunchStudio blog.

#LaunchStudio #Supabase #Postgres #DatabaseMigrations #AISaaS #Nextjs
