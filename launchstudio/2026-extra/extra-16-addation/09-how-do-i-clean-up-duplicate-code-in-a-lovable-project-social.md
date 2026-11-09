🧹 Daan Hofstra spent ten months building Projectkompas in Lovable: project management for small marketing agencies, with clients, tasks, time tracking and invoicing. It worked, but every new feature broke something else. One invoice bug was fixed three times and kept coming back. 🔁

Then a user at one agency saw another agency's project on a dashboard widget. 😳 A duplication scan explained everything: 🧠

❌ Seven different functions loading projects, only four checking the agency
❌ Money formatted five ways, two of them ignoring VAT
❌ Three copies of the invoice total, each fixed at a different time
❌ Three date libraries, two icon libraries, four table components, six Supabase clients

✅ Row Level Security per agency, so no function can load another agency's data
✅ Tests for access control and invoice calculations before refactoring
✅ Shared data modules, one money module, one date and one icon library
✅ Project instructions for Lovable and a duplication check in CI

At **LaunchStudio**, backed by Manifera's 11+ years of maintaining and refactoring codebases, we consolidate the risky parts of AI-generated code without rebuilding what already works. 🛠️

His result: €3,500, ten business days. The invoice bug never returned, the cross-agency leak was closed and the bundle shrank by about a third. Daan still builds in Lovable. 🚀

👉 How to clean up duplicate code in a Lovable project safely: https://launchstudio.eu/en/blog/how-do-i-clean-up-duplicate-code-in-a-lovable-project

#Lovable #Refactoring #Supabase #TechDebt #AIFounder #LaunchStudio #Manifera
