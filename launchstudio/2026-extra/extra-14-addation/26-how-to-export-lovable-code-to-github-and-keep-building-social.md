🔁 A kitchen quote tool's Groundhog Day

Day 1: A freelancer fixes the VAT rounding in the price calculation. ✅
Day 4: Jeroen asks Lovable to add a new worktop material. Lovable regenerates the quote component. The rounding error is back. ❌
Day 1 (again): Fix. ✅
Day 4 (again): New prompt. Fix gone. ❌
Day 1 (again): ...

Jeroen Vink sells and installs kitchens in Ede. He built Keukenofferte in Lovable: customers configure a kitchen layout, pick fronts and worktops and get an indicative quote, which his team turns into a final offer. He'd connected the project to GitHub and hired a freelancer to fix the rounding. It kept coming back, and so did two other fixes.

While breaking the loop, LaunchStudio found two more things:
• The repository lived under Jeroen's personal GitHub account
• The freelancer had committed a .env file with the email provider's secret key

How the loop was broken (6 business days, €1,450):
✓ The repository moved into a company GitHub organisation
✓ The exposed key rotated, and the history cleaned
✓ The price calculation moved into a Postgres function in Supabase, which the Lovable frontend now calls instead of calculating prices itself
✓ A staging deployment from main
✓ A short protected-files list in Lovable's knowledge settings
✓ A feature-branch workflow for the freelancer

Day 5, finally: Jeroen kept adding materials and options in Lovable, and prices stayed right. Over the next four months, Keukenofferte produced around 540 quotes, and the freelancer's work stopped disappearing.

"Every time I asked Lovable for something new, it quietly undid something old. Moving the important logic out of its reach fixed that." - Jeroen Vink

https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building

#Lovable #GitHub #Supabase #AIFounder #LaunchStudio #Manifera
