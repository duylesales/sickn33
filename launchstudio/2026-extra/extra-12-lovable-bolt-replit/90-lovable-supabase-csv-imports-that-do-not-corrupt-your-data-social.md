🚨 Annelies Vos's Huurbeheer runs rental administration for 31 housing organisations — around 9,500 rental units. A new property manager imported their tenants from a Dutch Excel export. The import said it had worked. The next direct debit run collected €1.25 in rent from 214 tenants. 😳

The parser had read "1.250,00" as 1.25. The same customer had also re-imported the file twice, creating 380 duplicate tenants — and every phone number had lost its leading zero. Here's how to build CSV imports that don't corrupt your data: 🧠

❌ Rows inserted straight into production, tested only on a hand-made comma-separated file
❌ Dutch amounts and dates parsed with English assumptions
❌ No preview, so nobody saw "rent: €1.25" before it was charged
❌ No deduplication and no way to undo an import

✅ XLSX and CSV parsing with delimiter and encoding detection, plus explicit Dutch number and date formats
✅ A staged pipeline: validate into staging, preview interpreted values, download an error file, commit in one transaction
✅ Upsert on the source system's tenant number, batch IDs on every row and a seven-day undo
✅ Background processing, organisation scoping from the batch, formula-injection protection and 14 nasty test fixtures in CI

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix imports when onboarding is the thing holding a product back. ⚙️

Her result: €3,600, three business days. The 214 tenants were collected correctly the next week and the duplicates merged. Eleven organisations imported next quarter — and the preview caught problems in four of their files before anything was written. 🚀

👉 Lovable Supabase: CSV imports that do not corrupt your data: https://launchstudio.eu/en/blog/lovable-supabase-csv-imports-that-do-not-corrupt-your-data

#Supabase #DataQuality #SaaS #Onboarding #LaunchStudio #Manifera
