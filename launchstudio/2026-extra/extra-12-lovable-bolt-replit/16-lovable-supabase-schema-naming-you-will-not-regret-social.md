❓ "Where does this customer live?"

ANSWER 1, from the clients table: one address.
ANSWER 2, from the customers table: another address.
ANSWER 3, from the contacts table: a third address.

Which one is right? Nobody could say. 🔧

Barend Kloosterman built Serviceplan in Lovable: maintenance contract administration for installation companies, 44 companies managing around 9,000 service addresses. Over fourteen months, the schema grew to 31 tables. Customers lived in three of them: clients from the original build, customers added when invoicing arrived, contacts added for the portal. Each one a reasonable answer to the question Barend had asked that day.

Then an installer updated a customer's address in the portal. That evening's invoice carried the old address. And the service engineer was sent to a third address, held somewhere else entirely.

One answer, from now on (LaunchStudio, 4 business days, €3,400):
✓ A full schema inventory, naming every duplicate and synonym
✓ A convention file in the repository, covering table and column names, timestamps, booleans, money and the product's vocabulary
✓ The three customer tables merged into one customers table, with a contacts table beneath it, migrated through add, write-both, migrate and drop, with no downtime
✓ Eleven columns renamed for consistency
✓ A comma-separated services text column normalised into a proper table with a join
✓ Nine missing foreign keys declared, surfacing 340 orphaned service records, each reviewed and reattached or archived
✓ Four timestamp columns made time-zone aware
✓ Two amount columns converted from floating point to integer minor units, which fixed a long-standing one-cent difference in invoice totals
✓ Generated types regenerated across the app

The three-address bug became structurally impossible. And a contractor Barend hired the next month was productive on day one, instead of spending two days asking which table was the real one. His AI sessions stopped inventing new column names too, because the convention file is now part of the project's instructions.

"I had three tables of customers because each time I asked for a feature I got a new table, and each one was a reasonable answer to the question I had asked that day." - Barend Kloosterman

https://launchstudio.eu/en/blog/lovable-supabase-schema-naming-you-will-not-regret

#Supabase #DatabaseDesign #TechDebt #Lovable #LaunchStudio #Manifera
