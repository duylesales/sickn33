🚨 Esther Bakker built Cateringbestel with Lovable, Supabase and Mollie: companies order lunches and catering from local caterers, with monthly invoices. Finance departments started rejecting invoices because VAT totals didn't match the lines - and one caterer was charged a fraction of a large order's value. 😳

A caterer's admin had typed "1.250,00" - and parseFloat read it as 1.25. Here are the money rounding and currency bugs that break SaaS invoices: 🧠

❌ Prices as floating point numbers, totals calculated in the browser
❌ VAT rounded per line on screen but per total in the PDF
❌ Mixed VAT rates combined incorrectly
❌ Dutch number input misread, and three-decimal refunds rejected by Mollie

✅ All amounts migrated to integer cents with explicit currencies
✅ One server-side calculation for checkout, invoices and exports
✅ VAT per rate group with one rounding step, agreed with the accountant
✅ Locale-aware input, Mollie-formatted amounts, idempotent refunds with credit notes, and tests

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make every cent add up - so finance teams keep trusting your invoices. 🛠️

Her result: €3,200, 9 business days. Invoice rejections stopped within the first billing cycle, and the accountant now gets exports that reconcile exactly with Mollie payouts. 🚀

👉 Do your invoices always add up? Here are the money bugs to fix: https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas

#Invoicing #VAT #Mollie #FoodTech #AIFounder #LaunchStudio #Manifera
