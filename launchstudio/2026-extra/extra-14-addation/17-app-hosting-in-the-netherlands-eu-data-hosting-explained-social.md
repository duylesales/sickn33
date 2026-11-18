🌍 Where does a vet clinic app actually live?

Database ............ 🇺🇸
File uploads ........ 🇺🇸
Error tracking ...... 🇺🇸 (and capturing owners' email addresses in error messages)
Email provider ...... 🇺🇸
Vercel functions .... 🇺🇸 (so every request crossed the Atlantic twice)

Evelien Kramer, a veterinary practice manager in Den Bosch, built Dierdossier with Bolt and Supabase: records and reminders for small veterinary clinics, with vaccination schedules, treatment histories and automatic reminders to pet owners. Four clinics used it. Then a regional chain of fourteen clinics wanted to adopt it, with one contract condition: all data stored in the EU, documented.

When Evelien mapped her own app, the flags above told the story.

The move (LaunchStudio, 12 business days, €4,100):
✓ Database, storage and auth users migrated to a new Supabase project in Frankfurt
✓ Error tracking moved to an EU data region, with personal data scrubbed from error messages
✓ The email provider switched to an EU processing setup
✓ Vercel functions set to an EU region
✓ A one-page data location overview for the chain's contract

AFTER
Database ............ 🇪🇺
File uploads ........ 🇪🇺
Error tracking ...... 🇪🇺
Email provider ...... 🇪🇺
Vercel functions .... 🇪🇺

The clinic chain signed, taking Dierdossier to eighteen clinics and around 21,000 pet owners. Bonus: with functions and database closer to Dutch users, pages load noticeably faster.

"I thought hosting was one setting. It was seven, and five of them were in America." - Evelien Kramer

https://launchstudio.eu/en/blog/app-hosting-in-the-netherlands-eu-data-hosting-explained

#EUHosting #GDPR #Supabase #Bolt #LaunchStudio #Manifera
