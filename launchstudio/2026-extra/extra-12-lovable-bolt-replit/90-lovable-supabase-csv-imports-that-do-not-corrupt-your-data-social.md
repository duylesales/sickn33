🔤 What the file said vs. what the import heard

FILE: 1.250,00 (Dutch for one thousand two hundred and fifty)
HEARD: 1.25

FILE: 0612345678 (illustrative number)
HEARD: 612345678, with the leading zero gone

FILE: the same tenants, uploaded three times
HEARD: 380 new tenants

IMPORT STATUS: "Success."

Annelies Vos built Huurbeheer in Lovable: rental administration for small housing corporations and property managers, 31 organisations, around 9,500 rental units. New customers imported tenants from Excel. The import read each row and inserted it straight away. It had been tested with a comma-separated file she'd made herself. 🏘️

A new property manager uploaded a semicolon-separated export with Dutch amounts. The monthly direct debit run then collected €1.25 from 214 tenants. The property manager found out from their bank statement.

Teaching the import to listen (LaunchStudio, 3 business days, €3,600):
✓ An XLSX and CSV parser that detects delimiter and encoding
✓ Explicit Dutch number and date formats per import, rejecting values that don't match
✓ Phone numbers, postcodes and house number additions kept as text, with length checks
✓ A staged pipeline with a preview of how amounts and dates were read, plus a downloadable error file
✓ Upserts on the source system's tenant number, with empty cells leaving existing values alone
✓ A batch ID on every row, and undo for seven days
✓ Background processing with progress for files over five hundred rows
✓ Organisation scoping from the batch, not the file
✓ Formula neutralisation on export
✓ A CI suite of fourteen difficult fixtures, the original file included

The 214 tenants were collected correctly the next week, and the 380 duplicates merged using the tenant number. Next quarter, eleven new organisations imported their data. The preview caught amount or date problems in four of those files before anything was written.

"The import said it had worked. Our customer found out from their bank that two hundred and fourteen tenants had paid one euro twenty-five in rent." - Annelies Vos

https://launchstudio.eu/en/blog/lovable-supabase-csv-imports-that-do-not-corrupt-your-data

#Supabase #DataQuality #SaaS #Onboarding #LaunchStudio #Manifera
