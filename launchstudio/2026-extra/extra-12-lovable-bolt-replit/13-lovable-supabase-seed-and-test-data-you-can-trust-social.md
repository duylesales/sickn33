🚨 Sanne Verkerk's Deelnemerslijst handles registration and attendance for 73 training providers - about 11,000 participants a year. Her development database had 30 people, all invented, all called something like Jan Jansen. Every feature worked before release, then produced a support ticket within a fortnight. 😳

Then a Limburg provider sent 84 certificates to a corporate client. Three were blank - the ones for Müller, Peña and Van 't Hoff. Here's why AI-built apps only break in production: 🧠

❌ Test data that's too small, too clean and too new
❌ Every account with the same amount of data, hiding the largest-customer problems
❌ No apostrophes, diacritics, empty fields or extreme values
❌ No safe way to get production's real shape into staging

✅ A deterministic seed: 4,000 participants across twelve providers, one holding 2,600
✅ Awkward names, a 180-character company name, two years of history, empty fields and dangling references
✅ Four named test accounts, including a second provider for isolation checks
✅ Staging copied from production and anonymised during the copy - with email credentials removed entirely

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build test data that finds bugs before your customers do. 🧪

Her result: two business days and €2,300 later, the export bug reproduced on the first run - along with two nobody had reported. Data-shape support tickets fell from about three a week to two in the following quarter. 🚀

👉 Seed and test data you can trust: https://launchstudio.eu/en/blog/lovable-supabase-seed-and-test-data-you-can-trust

#Supabase #Testing #DataQuality #Lovable #LaunchStudio #Manifera
