🧗 Lars Mulder runs a network of climbing gyms in Utrecht and built Klimslot with Lovable and Supabase for booking slots and courses. He improved the app every Friday afternoon. Three Fridays in a row, an update broke production: no slots in the calendar, sign-ups failing, course capacity wiped. Each time he spent the weekend fixing it while members emailed the front desk. 😩

The inventory explained why every change was a live experiment: 🧠

❌ The Supabase project in a former freelancer's account
❌ The domain registered privately by a former partner
❌ The live Stripe key used during testing
❌ One environment, production, and no record of database changes

✅ Supabase project and domain moved into Lars's business accounts
✅ Separate staging and production with their own keys and data
✅ Lovable connected to GitHub with a pipeline and tracked database migrations
✅ Email authentication records, tested backups, uptime monitoring and a practised rollback

At **LaunchStudio**, backed by Manifera's 11+ years of running production systems for clients such as Vodafone and TNO, we take AI-built apps from preview link to real production at a fixed price. 🛠️

His result: €1,950, five business days. Three months of weekly releases without a production incident, and two breaking changes caught on staging. 🚀

👉 Production deployment service for AI-built apps: https://launchstudio.eu/en/blog/production-deployment-service-for-ai-built-apps

#Deployment #Lovable #Supabase #DevOps #AIFounder #LaunchStudio #Manifera
