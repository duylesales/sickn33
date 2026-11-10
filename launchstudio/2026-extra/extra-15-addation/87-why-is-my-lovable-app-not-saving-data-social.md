🚨 Ruben Smeets built Urenbriefje with Lovable and Supabase: technicians at small installation companies log hours per job on their phones, and the office turns them into invoices. Six companies and around 70 technicians used it daily. Then one customer's month-end invoices came out 140 hours short. 😳

Technicians insisted they had logged everything - and the app had shown "Saved" every time. Here's why a Lovable app can say "saved" when nothing is saved: 🧠

❌ An insert policy checking team membership that newly invited technicians didn't have
❌ A "travel time" field in the form that didn't exist in the production database
❌ Phone sessions expiring overnight, so early-morning entries ran as anonymous users
❌ Code that ignored every error and showed a success message anyway

✅ Missing membership rows added, and invitations now create them automatically
✅ The missing migration applied and staging synced with production
✅ Ownership and team columns set by database defaults, not the frontend
✅ Every save checks the server response, keeps the form on failure and reports to monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure your app never tells customers everything is fine when it isn't. 🛠️

The result: €2,200, 6 business days. Most missing entries were reconstructed from API logs, the next month's invoices matched, and monitoring flagged two problems the following quarter before any customer noticed. 🚀

👉 Is your app silently failing to save data? Here's how to find out: https://launchstudio.eu/en/blog/why-is-my-lovable-app-not-saving-data

#Lovable #Supabase #RowLevelSecurity #FieldService #AIFounder #LaunchStudio #Manifera
