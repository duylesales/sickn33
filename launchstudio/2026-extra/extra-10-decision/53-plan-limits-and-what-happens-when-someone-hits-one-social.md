🚨 Anouk Verstraeten's invoicing limit held for four months — until one customer imported 340 invoices in an afternoon on a 100-per-month plan. 😳

A pricing-page limit feels solid until real usage tests the code underneath it: 🧠

❌ The limit check read the count, compared it, then inserted — once per invoice, with dozens of requests racing at once
❌ Every check saw a stale count and passed, leaving 340 invoices on a 100-invoice plan
❌ Four other accounts sat between 104 and 190 invoices through ordinary two-tab usage
❌ The counting query scanned every invoice ever created, with no supporting index, and had begun slowing down for her three largest accounts

✅ Enforce limits with an atomic counter per billing period, not a read-then-insert check
✅ Add the index that lets you count current-period usage fast, not just at 100 rows
✅ Warn customers at 80% usage instead of letting them hit a wall with no notice
✅ Offer over-limit accounts a prorated upgrade rather than punishing them retroactively

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we test plan limits against exactly the case that breaks them: concurrent and bulk-import usage. 📊

Her result: enforcement rebuilt in 3 business days — three of the five over-limit accounts upgraded, and invoice creation got measurably faster for her largest customers. 🚀

👉 Check whether your plan limits would survive a bulk import: [Link to article]

#SaaS #Pricing #ProductEngineering #IndieHacker #LaunchStudio #Manifera
