🚨 Evelien Kramer, a veterinary practice manager in Den Bosch, built Dierdossier with Bolt and Supabase: records, vaccination schedules and reminders for small vet clinics. A regional chain of fourteen clinics wanted to adopt it, with one condition in the contract: all data stored within the EU, documented. 😳

She thought hosting was one setting. When she mapped her own app, it turned out to be seven - and five of them were in America: 🧠

❌ The Supabase database and file uploads in a US region
❌ Error tracking in a US data region, capturing pet owners' emails in error messages
❌ An email provider processing data in the US
❌ Vercel functions in their default US region, crossing the Atlantic twice per request

✅ Database, storage and auth users migrated to a new Supabase project in Frankfurt
✅ Error tracking moved to an EU data region, personal data scrubbed from errors
✅ Email switched to EU processing, functions set to an EU region
✅ A one-page data location overview for the chain's contract

At **LaunchStudio**, backed by Manifera's 11+ years on AWS, Azure and Dutch infrastructure, we choose the simplest EU setup that meets your customer's contract. 🛠️

💡 Her result: €4,100, twelve business days. The chain signed, bringing Dierdossier to eighteen clinics and around 21,000 pet owners - and pages loaded noticeably faster for Dutch users. 🚀

👉 Customers asking "is it hosted in the Netherlands?" Here's what EU data hosting really requires: https://launchstudio.eu/en/blog/app-hosting-in-the-netherlands-eu-data-hosting-explained

#EUHosting #GDPR #Supabase #Bolt #LaunchStudio #Manifera
