🚨 Hidde Kwakernaak built Ritmeester with Bolt — stable management for six equestrian centres in Gelderland and Utrecht: horses, owners, stalls, feeding, vet appointments and invoicing. He asked the tool to add a database screen by screen. After three weeks: 19 tables. 😳

Horses lived in two tables, owner details in three with different values. No foreign keys, no row-level security. When the second centre started using it, their horses appeared in the first centre's stall list. Here's how to wire data into a Bolt prototype: 🧠

❌ Letting the tool derive the schema from whichever screen came first
❌ 19 tables for a business with five real things in it
❌ No RLS, no foreign keys, no constraints
❌ Mock-data fallbacks quietly showing horses that didn't exist

✅ The business described first: five core entities plus invoicing, with tenancy, IDs and naming decided upfront
✅ 19 tables consolidated to 8, with duplicate horses and owners reconciled by hand
✅ RLS policies on every table tested with two centres, plus foreign keys (40 orphans found) and constraints
✅ A realistic seed of 400 horses, mock fallbacks removed, migrations committed and types regenerated

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we design your schema before anything is generated against it. 🗄️

His result: three business days and €3,200 later, the cross-centre leak was closed structurally. Each new centre after that took a day to onboard instead of a week, because nothing needed reconciling. 🚀

👉 Wiring data into a Bolt prototype: https://launchstudio.eu/en/blog/bolt-and-supabase-wiring-data-into-a-bolt-prototype

#Bolt #Supabase #DatabaseDesign #Prototyping #LaunchStudio #Manifera
