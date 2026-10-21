🚨 Anouk Smit, a primary-school teacher in Haarlem, built Oppasklok in Bolt to coordinate babysitters between five families. It grew to 60 families — each profile with children's names, ages, allergies and home address. Before opening it to a parents' association of several hundred members, she ran a simple test herself: the two-account test. 😳

It failed immediately. By changing a number in the URL, any logged-in parent could open any family's profile. "View source" also turned up a mapping API key. Here's how to productionize an AI app when you can't read the code: 🧠

❌ Family data separated only by the interface, not the database
❌ An API key visible in the page source
❌ No tested backups, no alerts
❌ A founder who couldn't judge the fix — until she could run the test herself

✅ Database-level access rules: each family's data visible only to that family and invited babysitters
✅ The mapping key moved to a server-side function with usage limits
✅ EU-region backups with a tested restore, plus uptime alerts on Anouk's phone
✅ The two-account test re-run together on a call, so she could see it fail safely

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we explain every finding in plain words — and show you the evidence. ⚙️

Her result: €1,450, five business days. Oppasklok opened to the parents' association two weeks later and grew to 240 families with no data-access incidents. Anouk still runs the two-account test after every big change. 🚀

👉 How to productionize an AI app when you can't read the code: https://launchstudio.eu/en/blog/how-to-productionize-an-ai-app-when-you-cant-read-the-code

#Bolt #NoCode #AppSecurity #Startups #LaunchStudio #Manifera
