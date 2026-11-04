🚨 Gerda Hofstra runs a piano school in Sneek with nine teachers and built Pianoles in Lovable for bookings, lesson credits and payments. Her existing data: 17 years of spreadsheets - 640 current and former students, family links and prepaid credits. Her first attempt was pasting rows into Lovable's chat. It created 212 students, then stopped. 😳

Siblings were merged into one record, credits landed on the wrong families, and two early parents had duplicate accounts. The app took weeks; the move was what she'd underestimated. Here's what went wrong: 🧠

❌ Raw spreadsheet rows pasted into the AI chat
❌ No cleaning or deduplication before import
❌ Imported straight into production with no rehearsal
❌ No reconciliation of credit balances afterwards

✅ Spreadsheets cleaned and deduplicated, with only current students getting accounts
✅ Families, students and credits mapped to the schema, and the partial import rolled back
✅ Two test imports in staging, then accounts created via the Supabase admin API without passwords
✅ Dutch invitations sent in three batches, and credit totals reconciled with the bookkeeping

At **LaunchStudio**, backed by Manifera's 11+ years of enterprise data migrations, we treat customer imports as the small migration they are: clean, map, rehearse, import, invite, verify. 🛠️

💡 Her result: €1,800, six business days. 312 current students and parents invited, 88% activated within two weeks, and credit balances matched the bookkeeping to the euro. 🚀

👉 Moving existing customers into a Lovable app? Here's the six-step import process: https://launchstudio.eu/en/blog/how-do-i-import-my-existing-customers-into-a-lovable-app

#Lovable #Supabase #DataMigration #SaaS #LaunchStudio #Manifera
