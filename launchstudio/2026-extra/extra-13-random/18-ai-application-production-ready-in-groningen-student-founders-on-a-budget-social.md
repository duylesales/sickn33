🚨 Wessel Postma, a third-year student at the University of Groningen, built Kamerzoeker in Bolt: room-seekers post profiles with photos, budgets and move-in dates, and tenants looking for a housemate message them. He shared it in two student association group chats on a Tuesday evening. By Thursday, 1,300 students had signed up. Then a computer science friend checked the API. 😳

Every profile — phone numbers and the "private notes" where people described their situation — could be fetched without logging in. Row level security was missing, the database sat in a US region, photos were in a public bucket and accounts couldn't be deleted. Wessel had about €1,500 saved. Here's how to make an AI application production ready on a student budget: 🧠

❌ Profiles readable by anyone through the API
❌ Profile photos in a public bucket
❌ Database outside the EU, no tested backup
❌ No way to delete an account

✅ Row level security: profiles for logged-in users only, private fields for their owner only
✅ Photos in private storage with signed links
✅ Database migrated to an EU region with backups and a tested restore
✅ Full account deletion — while Wessel did the free work himself: one project email with 2FA, a privacy notice, an uptime monitor

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix exactly what can hurt people first — and tell you honestly what can wait. ⚙️

His result: €1,200, six business days. Kamerzoeker reached 4,800 users by the next academic year with no data incidents, and a local incubator accepted Wessel, citing the clear privacy setup. 🚀

👉 AI application production ready in Groningen: student founders on a budget: https://launchstudio.eu/en/blog/ai-application-production-ready-in-groningen-student-founders-on-a-budget

#StudentStartup #Groningen #Bolt #GDPR #LaunchStudio #Manifera
