🚨 Gijs Visser runs a dairy farm with a farm shop near Assen and built Boerderijkist in Lovable on Lovable Cloud: about 380 households pre-order weekly boxes of cheese, milk and vegetables. Then a cooperative of seven farms wanted the platform under their own brand - with an EU database, a processing agreement they could review and direct access for their accountant's reporting tool. 😳

Lovable Cloud got him started without thinking about databases. The cooperative needed him to think about databases. Here's what the move involved: 🧠

❌ 23 tables, 4 edge functions, about 1,600 product photos and 410 user accounts to move
❌ Two tables altered by hand that no longer matched the migration files
❌ Password hashes that couldn't be carried over
❌ A Mollie webhook still pointing at the old backend

✅ A company-owned Supabase project in Frankfurt, schema drift reconciled into proper migrations
✅ The data import rehearsed twice, edge functions deployed with new secrets, photos migrated
✅ A friendly one-click "set your password" email plus a magic link option
✅ Mollie's webhook updated and a 40-minute maintenance window on a Monday night

At **LaunchStudio**, backed by Manifera's 11+ years of enterprise data migrations, we rehearse every migration before the real switch - and plan the rollback too. 🛠️

💡 His result: €3,800, ten business days. By Wednesday 87% of active customers had logged in again, the cooperative signed, and Boerderijkist now serves seven farm shops from one platform. 🚀

👉 Outgrowing Lovable Cloud? Here's the step-by-step migration plan to your own Supabase: https://launchstudio.eu/en/blog/how-to-migrate-from-lovable-cloud-to-your-own-supabase

#Lovable #Supabase #DataMigration #AgriTech #LaunchStudio #Manifera
