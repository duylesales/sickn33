🩺 Pieter Brink runs an occupational health SaaS from Enschede, built with Cursor and Supabase: employers and company doctors coordinate sick leave cases. A large employer required an independent penetration test before signing. Pieter booked a security consultancy straight away. The report: 32 findings, seven rated high. 😬

He had no developer, and his AI tool fixed some findings while breaking document uploads for doctors. The high-risk findings included: 🧠

❌ Missing ownership checks on API routes
❌ Case documents in a public bucket
❌ An exposed service key
❌ No rate limiting on login, plus outdated dependencies

✅ Ownership checks on every route through a shared helper, backed by Row Level Security with tests
✅ Documents in private storage with signed links, and the key rotated
✅ Rate limits, security headers and updated dependencies
✅ A short note per fix for the testers, ready for the retest

At **LaunchStudio**, backed by Manifera's 11+ years of delivering software for clients such as Vodafone and TNO, we fix findings in your code and prepare you for independent testing, ideally before the test, not after. 🛠️

His result: €3,300, eight business days. The retest found only three low-severity issues, fixed within a day, and the employer signed. 🚀

👉 LaunchStudio vs a security consultancy: https://launchstudio.eu/en/blog/launchstudio-vs-a-security-consultancy

#Pentest #Security #Cursor #Supabase #AIFounder #LaunchStudio #Manifera
