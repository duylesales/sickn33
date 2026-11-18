🌿 WHO WAS IN CHARGE OF THE APP? A responsibility chart, day three after launch

Checking the backups ........ nobody
Watching the logs ........... nobody (there were no logs)
Owning the Supabase project . a former collaborator's email
Protecting the calendar key . nobody (it was in the page source)
Testing changes before release . nobody (Lovable edits went live instantly)

Femke de Wit, a landscape designer in Leiden, built Groenschets in Lovable over three weekends: homeowners sketch their garden, pick plants suited to their soil and sun, and book a consultation with her small team. Twenty neighbours loved it, and Femke announced it in a regional gardening newsletter with about 4,000 subscribers.

Groenschets didn't crash. Something quieter happened. On day three, a customer wrote that her saved garden design had vanished. Femke couldn't tell whether it was one design or many. And one of her own Lovable changes that morning turned out to reset unsaved designs.

LaunchStudio treated it as a handover, not a repair (9 business days, €1,900):

Checking the backups ➜ daily backups, with a tested restore
Watching the app ➜ uptime and error alerts to Femke's phone
Owning the accounts ➜ everything under a company email, with two-factor authentication
Protecting the calendar key ➜ moved into a server-side function
Testing changes ➜ a staging environment, so Lovable edits are tested before release
The Lovable frontend ➜ not touched

The lost design came back from a point-in-time backup the team found still enabled on the database. Over the following spring season, Groenschets handled roughly 1,100 saved designs with no data loss, and alerts caught two minor bugs before any customer noticed.

"I thought launching meant the app was finished. It turned out launching meant somebody had to be in charge of it - and until then, nobody was." - Femke de Wit

https://launchstudio.eu/en/blog/ai-prototype-to-production-the-handover-nobody-plans-for

#Lovable #AIPrototype #NoCode #Startups #LaunchStudio #Manifera
