🚨 Ayoub Benali, a bookkeeper in Schiedam, built Nota Nu with Cursor: invoicing for freelancers, with quotes, reminders and a quarterly VAT overview. About 260 freelancers paid €9 a month. Then an accountant working with several of them noticed the quarterly VAT totals didn't match the invoices - off by a few cents to a few euros per client. 😳

Amounts were stored as floats. VAT was rounded per line on screen but per invoice in the overview. Invoice numbers were "count plus one", producing duplicates when two devices created invoices at once - and going backwards after a deletion. Sent invoices were fully editable, EU reverse charge wasn't handled, and deleting an account wiped invoices users were legally required to keep. Here's how to productionize an AI invoicing app: 🧠

❌ Floating-point money
❌ Mixed VAT rounding between screens and reports
❌ Numbering that duplicates and goes backwards
❌ Editable issued invoices and deletion that ignores the seven-year rule

✅ Amounts migrated to integer cents with a verified conversion
✅ Per-line VAT rounding everywhere
✅ Transactional numbering per series, assigned at finalisation
✅ Locked issued invoices with stored PDFs, credit notes, reverse-charge invoices and seven-year retention - plus a report of every historic discrepancy

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix the arithmetic and the rules behind an invoice, not just its layout. ⚙️

His result: €2,700, nine business days. Quarterly VAT overviews now reconcile to the cent, Nota Nu grew to 610 subscribers the next year, and two accountancy firms began recommending it. 🚀

👉 Productionize an AI app for invoicing: VAT, rounding and numbering: https://launchstudio.eu/en/blog/productionize-an-ai-app-for-invoicing-vat-rounding-and-numbering

#Invoicing #VAT #Freelancers #Cursor #LaunchStudio #Manifera
