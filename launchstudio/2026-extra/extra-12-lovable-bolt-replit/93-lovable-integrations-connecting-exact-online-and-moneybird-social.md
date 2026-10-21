🚨 Iris Meijer's Schoonmaakplanner handles scheduling and invoicing for 44 commercial cleaning companies. Its Exact Online integration was generated in an afternoon and demoed perfectly. Then, at quarter end, accountants for nine customers found 312 duplicate sales invoices — and misbooked VAT in four administrations. Two customers threatened to cancel. 😳

Three hidden problems: concurrent token refreshes broke connections weekly, timeouts made retries book invoices twice, and VAT code "2" was hard-coded even though it means different things in different administrations. Here's how to connect Exact Online and Moneybird so bookkeepers trust it: 🧠

❌ Token refresh racing between the nightly sync and user actions
❌ Retries with no idempotency, so slow responses became duplicate invoices
❌ One hard-coded VAT code for every customer's administration
❌ No sync status — nobody could see what arrived and what didn't

✅ Token refresh serialised per organisation, tokens encrypted, disconnections reported to the customer
✅ An outbox storing Exact's ID on each invoice, with a lookup by invoice number before every retry
✅ A mapping screen loading each administration's VAT codes, ledger accounts and journal, validated before activation
✅ Rate-limited sync, actionable status on every invoice, post-booking locks and a weekly reconciliation report

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build and repair accounting integrations for products whose customers live in Exact and Moneybird. ⚙️

Her result: €4,600, four business days. Duplicates removed within the filing window, both at-risk customers stayed, and six months with zero duplicates or token disconnects. A Moneybird connector followed in three days — and six new customers chose the product for its accounting integration. 🚀

👉 Lovable integrations: connecting Exact Online and Moneybird: https://launchstudio.eu/en/blog/lovable-integrations-connecting-exact-online-and-moneybird

#ExactOnline #Moneybird #Integrations #SaaS #LaunchStudio #Manifera
