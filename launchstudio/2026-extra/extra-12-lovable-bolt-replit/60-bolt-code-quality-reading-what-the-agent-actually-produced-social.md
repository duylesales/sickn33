🔍 Scavenger hunt: find every copy of one municipality's tourist tax rate.

☑ Component #1
☑ Component #2
☑ The invoice generator
☑ The quote preview
☐ The PDF template
☐ A summary calculation
☐ A database default

Rogier Slagter found four of the seven. He updated them and deployed. Three days later, a property manager reported their invoices still showed the old amount.

Rogier built Verhuurbeheer with Bolt: rental administration for holiday home owners and small property managers, 62 users and 380 properties. The Dutch tourist tax rate in one municipality had changed. 🏖️

The bonus round, where things got worse: two of the copies had been slightly different for months. A rounding difference meant invoices disagreed with their own line items by a cent.

Ending the game (LaunchStudio, 2 business days, €2,700):
✓ All seven copies merged into one configuration with a single calculation function
✓ Date formatting, which had five implementations with three different behaviours around midnight, given the same treatment
✓ 14 dead components, 6 unused endpoints and 3 abandoned tables removed
✓ Two competing data-fetching approaches reduced to one
✓ The four largest files, each over 600 lines, split into data access, logic and presentation
✓ Loading and empty states on eleven screens that had shown blank pages
✓ Raw technical error text rewritten as sentences
✓ A formatter applied, and a conventions file committed describing the chosen patterns

The hidden prize nobody was looking for: one of those unused endpoints was an unauthenticated export of every booking, left over from an early experiment. It had been reachable for eight months. It was the most serious finding, and turned up only because dead code was being cleared out.

The tax change now takes one edit. And something Rogier didn't expect: since the conventions file went in, later AI sessions produce noticeably more consistent work.

"I changed the tax rate in four places and thought I was done. It was in seven, and two of them had been quietly disagreeing with each other since spring." - Rogier Slagter

https://launchstudio.eu/en/blog/bolt-code-quality-reading-what-the-agent-actually-produced

#CodeQuality #Bolt #TechDebt #AIDevelopment #LaunchStudio #Manifera
