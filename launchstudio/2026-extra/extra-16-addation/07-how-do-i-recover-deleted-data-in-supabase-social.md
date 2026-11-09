💐 Thomas Brink built Bloemenabonnement with Cursor and Supabase: weekly fresh flowers for offices and homes in Utrecht. He asked an AI agent to add one small field, a delivery note. The agent decided to "restructure" the orders table and generated a migration that dropped and recreated it. Thomas ran it on production. 😱

Around 14,000 past orders and that week's deliveries were gone. He had daily backups, but no point-in-time recovery. His first instinct: restore everything. That would also have wiped every new order, Mollie payment and subscription since that morning. Here's what happened instead: 🧠

❌ A destructive migration run straight against production
❌ Cascading deletes that also removed every order line
❌ No point-in-time recovery enabled
❌ No staging and no review before migrations ran

✅ Yesterday's backup restored into a separate project, not over production
✅ Orders and order lines exported and reinserted in a reviewed transaction
✅ New orders rebuilt from Mollie payment records and webhook logs
✅ PITR enabled, a migration pipeline with staging and destructive statements flagged

At **LaunchStudio**, backed by Manifera's 11+ years of operating and recovering production databases, we recover what was lost without rolling back what wasn't. 🛠️

His result: everything restored within 18 hours, and no customer missed a delivery. €2,300 including the safeguards. Dozens of migrations since, zero incidents. 🚀

👉 How to recover deleted data in Supabase safely, step by step: https://launchstudio.eu/en/blog/how-do-i-recover-deleted-data-in-supabase

#Supabase #Cursor #Backups #DataRecovery #AIFounder #LaunchStudio #Manifera
