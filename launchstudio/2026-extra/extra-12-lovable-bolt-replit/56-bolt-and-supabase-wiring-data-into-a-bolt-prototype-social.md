🐴 Told by a horse (dramatized; the database problems are real)

Hello. I'm a horse at an equestrian centre in Gelderland. For a while, I existed twice.

I lived in two tables. My owner's phone number lived in three, under different column names, and by then with different values. Nobody could say which one was right.

Nothing tied me to my stall, or my stall to my centre. There were no foreign keys and no row-level security. One table belonged to a feature abandoned in week one, and nobody had removed it.

Then a second centre started using the system, and their horses appeared in our stall list.

I live in Ritmeester, the stable and livery management tool Hidde Kwakernaak built with Bolt: horses, owners, stalls, feeding schedules, vet appointments and invoicing, for six centres in Gelderland and Utrecht. Every time he built a screen, he asked the tool to add a database for it. Three weeks later there were 19 tables. 🐎

How I became one horse again (LaunchStudio, 3 business days, €3,200):
✓ The business described first: centres, horses, owners, stalls and appointments, plus invoicing
✓ A schema built around those, with an organisation ID on every table, random primary keys, a readable horse reference people can quote, and consistent naming
✓ 19 tables merged into 8, with duplicate horse and owner records combined after the three copies of contact details were reconciled by hand
✓ Row-level security with policies on all eight, checked with accounts in two centres
✓ Foreign keys, which turned up 40 orphaned records
✓ Not-null, unique and check constraints
✓ Seed data: 400 horses across four centres, unevenly spread, with missing optional fields and diacritics in names
✓ Mock data fallbacks removed from four screens that had been quietly showing invented horses whenever a result came back empty
✓ Migrations committed and types regenerated

The cross-centre leak was closed by the structure itself, not patched. Hidde found the three days uncomfortable, since they produced no visible feature. But the next six centres onboarded in a day each, not the week the first two took, because nothing needed reconciling.

"Nineteen tables for a business with five things in it. Each one was a reasonable answer to a screen I was building that afternoon, and together they were a product where a horse could exist twice with different owners." - Hidde Kwakernaak

https://launchstudio.eu/en/blog/bolt-and-supabase-wiring-data-into-a-bolt-prototype

#Bolt #Supabase #DatabaseDesign #Prototyping #LaunchStudio #Manifera
