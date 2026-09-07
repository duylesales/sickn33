🚨 Wietse de Groot's invoices were one cent off, and an accountant noticed. Digging deeper turned up a payment that had charged €14.50 instead of €1,450.00. 😳

A support email about a single cent is rarely about the cent — it's a sign of how your product handles money everywhere: 🧠

❌ Amounts were stored as ordinary floating-point decimals, and line sums quietly accumulated small errors on invoices with many entries
❌ VAT was applied to the summed total instead of per line, disagreeing with the accountant's own bookkeeping software by a cent or two
❌ Amounts sent to the payment provider were converted at the boundary, and two payments were transmitted as €14.50 instead of €1,450.00 — both refunded as "customer errors"
❌ Invoices displayed `1,450.00` in English convention, leaving two Dutch customers unsure whether it meant one thousand or one point four

✅ Store amounts as integers in the smallest unit — cents — so all arithmetic stays exact
✅ Calculate and round VAT per line before summing, matching Dutch accounting convention, and apply the same rule everywhere
✅ Store currency alongside every amount, and never let it cross a payment boundary as an ambiguous decimal
✅ Format numbers with locale-aware functions instead of assembling strings by hand

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we correct money handling and verify totals against real invoices before launch. 💶

His result: all amounts migrated to integer cents, per-line VAT rounding fixed, and a 14-month reconciliation that found and reissued 40 invoices with a one-cent discrepancy. 🚀

👉 Check what your money handling is actually doing: [Link to article]

#SaaS #FinTech #Invoicing #IndieHacker #LaunchStudio #Manifera
