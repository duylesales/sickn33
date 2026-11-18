🧾 Spot the errors on this invoice (illustrative, but every error type was real)

Lunch platter (VAT per line, rounded on screen) ........ total A
Drinks (different VAT rate, merged with food) ........ total B
VAT on the PDF (rounded on the total) ........ off by 1 or 2 cents
Large order, price typed as "1.250,00" ........ charged €1.25
Partial refund ........ sent to Mollie with three decimals, rejected

Esther Bakker built Cateringbestel with Lovable, Supabase and Mollie: companies order lunch and meeting catering from local caterers, and pay by monthly invoice. Then finance departments started rejecting invoices because the VAT total didn't match the lines. And one caterer complained that a large order had been charged at a fraction of its value.

The answers:
• Prices stored as floating point numbers
• Totals calculated in the browser, sent to the backend and passed to Mollie as-is
• VAT rounded per line on screen but per total on the PDF
• Mixed VAT rates combined incorrectly
• parseFloat reading the Dutch "1.250,00" as 1.25
• Refunds with three decimals

The corrections (LaunchStudio, 9 business days, €3,200):
✓ All amounts migrated to integer cents with explicit currencies
✓ One server-side function for price, discount, VAT and total, used by checkout, invoices and exports alike
✓ VAT per rate group with one rounding step, as agreed with Esther's accountant
✓ Locale-aware input that accepts Dutch notation and rejects ambiguous values, and Intl.NumberFormat for display
✓ One conversion function for Mollie's decimal string format
✓ Refunds capped at the remaining refundable amount, idempotent, with matching credit notes
✓ Tests for mixed rates, awkward prices, Dutch input and partial refunds

Invoice rejections stopped within the first billing cycle. The caterer was correctly charged with a corrected invoice. Exports now reconcile exactly with Mollie payouts.

"A one-cent difference sounds trivial until a customer's finance team stops trusting every invoice you send." - Esther Bakker

https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas

#Invoicing #VAT #Mollie #FoodTech #AIFounder #LaunchStudio #Manifera
