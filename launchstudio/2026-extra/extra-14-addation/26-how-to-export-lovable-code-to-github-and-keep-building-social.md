🚨 Jeroen Vink sells and installs kitchens in Ede. He built Keukenofferte in Lovable: customers configure a kitchen and get an indicative quote. He connected it to GitHub and hired a freelancer to fix a VAT rounding error. The fix lasted three days. 😳

Then Jeroen asked Lovable for a new worktop material, Lovable regenerated the quote component - and the rounding error was back. It happened twice more. Here's what was going wrong: 🧠

❌ Critical price logic living in a component Lovable kept regenerating
❌ The repository under Jeroen's personal GitHub account
❌ A committed .env file with the email provider's secret key
❌ No workflow separating Lovable's changes from the freelancer's

✅ Repository moved to a company GitHub organisation, exposed key rotated and history cleaned
✅ Price calculation moved into a Postgres function in Supabase, out of Lovable's reach
✅ A staging deployment from main and a protected-files list in Lovable's knowledge settings
✅ A feature-branch workflow for the freelancer

At **LaunchStudio**, backed by Manifera's 160+ projects with branches, reviews and staging as standard, we make your Lovable repository safe for more than one builder. 🛠️

💡 His result: €1,450, six business days. Jeroen kept adding options in Lovable without breaking prices again, Keukenofferte produced about 540 quotes in four months, and fixes stopped disappearing. 🚀

👉 Exporting Lovable code to GitHub? Here's the workflow that keeps fixes from vanishing: https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building

#Lovable #GitHub #Supabase #AIFounder #LaunchStudio #Manifera
