7 functions that load projects. Only 4 check the agency.
5 ways to format money. 2 ignore VAT.
3 date libraries.
2 icon libraries.
4 similar table components.
6 files that each create a Supabase client.
3 copies of the invoice total calculation. 🔁

That was Projectkompas after ten months in Lovable.

Daan Hofstra built it as a project management tool for small marketing agencies: clients, projects, tasks, time tracking and invoicing. It worked, but every new feature broke something else. One invoice total bug was "fixed" three times and kept coming back. And one agency's user once saw another agency's project in a dashboard widget.

The duplication scan explained both. Three copies of the total calculation, each fixed separately. And seven project loaders, three of which forgot to check the agency.

The clean-up (LaunchStudio, 10 business days, €3,500):
1st: Row Level Security per agency on every table, so no frontend function can load another agency's data
Then: tests for access control and invoice calculations
3 shared data access modules, for projects, tasks and invoices
7 project loaders replaced, one by one
1 money module handling VAT and rounding
1 date library, 1 icon library
1 accessible table component
1 Supabase client, exported from one file
Plus project instructions telling Lovable which modules to use, and a duplication check in CI

The new numbers:
0 returns of the invoice bug
0 cross-agency exposure
About ⅓ smaller bundle
And a duplication check that stays flat as Daan keeps building in Lovable

"Every time I fixed something, Lovable had another copy somewhere. Consolidating the core made the app finally behave like one product." - Daan Hofstra

https://launchstudio.eu/en/blog/how-do-i-clean-up-duplicate-code-in-a-lovable-project

#Lovable #Refactoring #Supabase #TechDebt #AIFounder #LaunchStudio #Manifera
