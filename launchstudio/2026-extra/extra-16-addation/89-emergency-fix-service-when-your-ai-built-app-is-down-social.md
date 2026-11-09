🚨 Dennis Vos runs a SaaS for car repair garages from Zoetermeer, built with Lovable and Supabase and used by around 70 garages for appointments and invoices. On Sunday evening he asked his AI tool to "add a column for the mechanic's name" and accepted several follow-up suggestions. On Monday morning, garages saw empty schedules. Four more prompts made it worse. At 08:40 he called LaunchStudio. ☎️

The diagnosis showed: 🧠

❌ A Sunday suggestion had replaced the appointments policy with one referencing the new column incorrectly, so every query returned nothing
❌ A later prompt renamed a column the invoice function depended on
❌ No staging, so every change went straight to garages
❌ No tests to catch the broken policy before release

How it was stabilised: ✅

✅ A fixed price of €950 agreed before any change
✅ Policy restored from migration history and the column rename reverted
✅ Deployment rolled back to Saturday's version, with schedules and invoices confirmed by two garages by 10:15
✅ The mechanic column re-added properly that afternoon through a migration on new staging, plus an incident report with recommendations

At **LaunchStudio**, backed by Manifera's 11+ years of operating production systems for clients such as Vodafone and TNO, we stabilise first, explain clearly and help prevent the next incident. 🛠️

His result: about ninety minutes of downtime, an honest apology and no garage cancelled. A follow-up Launch Ready project added tests that have since caught a similar prompt mistake. 🚀

👉 Emergency fix service when your AI-built app is down: https://launchstudio.eu/en/blog/emergency-fix-service-when-your-ai-built-app-is-down

#AppDown #IncidentResponse #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
