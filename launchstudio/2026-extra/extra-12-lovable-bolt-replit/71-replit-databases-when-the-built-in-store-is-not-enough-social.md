🗄️ You may have written a database by accident if...

...you keep hand-maintained lists of keys so you can find things.
...a report has to read every record ever created and do the maths in code.
...changing one customer's name means updating it in every record that copied it.
...your update script misses some of those copies.

All four were true of Materieelverhuur, the equipment rental administration Vera Slothouber built on Replit: machines, rental periods, customers and damage reports for nine construction hire companies, around 1,400 items. Everything lived as objects in the built-in key-value store.

Then two failures arrived together. The monthly utilisation report, every company's most-used feature, run on the first working day, started timing out. And a customer's name change missed 60 records, so for a month, invoices showed two different names for the same business. 🏗️

Swapping the accidental database for a real one (LaunchStudio, 3 business days, €3,800):
✓ Five entities named: companies, items, customers, rentals, damage reports
✓ A Postgres schema with an organisation ID on every table, foreign keys, and customer names referenced instead of copied
✓ A migration script run six times against a copy before it ran clean. It surfaced 140 rentals pointing at deleted customers, 31 duplicate customers created by slight spelling differences, and 12 records missing a required date, each resolved by a decision, not a default
✓ Constraints and indexes, including the composite index the utilisation report needs
✓ Four days of dual writes with daily comparison, which found two write paths the migration had missed
✓ Reads switched over area by area across two days, with the old store kept untouched for three weeks
✓ Migrations committed, backups configured, and a restore performed and timed

The utilisation report went from timing out to 400 milliseconds. A name change can no longer go wrong, because each name now exists once. And the 31 duplicates had been invisible in the old store, causing months of invoicing confusion nobody had linked to a data problem.

"I was keeping lists of keys so I could find things, and updating customer names in four hundred copies. I had written a database without noticing, and mine had no constraints." - Vera Slothouber

https://launchstudio.eu/en/blog/replit-databases-when-the-built-in-store-is-not-enough

#Replit #Postgres #Database #DataModelling #LaunchStudio #Manifera
