🩹 Triage: three bugs in one accounting integration

BUG #1: Connections dropping
Symptom: about once a week, a customer's Exact Online link broke and needed re-authorising.
Cause: the nightly sync and a user sending an invoice sometimes refreshed the token at the same moment.
Fix: token refresh serialised per organisation with an advisory lock, tokens encrypted at rest, and disconnections reported to the customer's administrator.

BUG #2: Invoices booked twice
Symptom: duplicate sales invoices.
Cause: when Exact answered slowly, the integration retried and created the invoice again.
Fix: an outbox, the Exact ID stored on each invoice, and a lookup by invoice number before every retry.

BUG #3: VAT on the wrong code
Symptom: misbooked VAT amounts.
Cause: every booking used VAT code "2". In most administrations that's 21%. In four, set up by different accountancy firms, it meant something else.
Fix: a mapping screen loading each administration's VAT codes, revenue ledgers and sales journal via the API, validated before activation.

Iris Meijer built Schoonmaakplanner in Lovable: scheduling, time registration and invoicing for 44 commercial cleaning companies. The integration was generated in an afternoon and demoed well. At quarter end, accountants for nine customers found 312 duplicate invoices and misbooked VAT in their returns. Two customers said they'd cancel unless it was fixed. 🧽

Also in the treatment (LaunchStudio, 4 business days, €4,600):
✓ Rate-limited processing per organisation
✓ Sync status on every invoice, with errors that say what to do, and a sync overview per customer
✓ Invoices locked after booking, with corrections as credit notes
✓ A weekly reconciliation of missing, duplicated and differing bookings
✓ A scripted list of the 312 duplicates with their Exact IDs, for the accountants to remove

The duplicates and VAT were corrected inside the filing window, and both unhappy customers stayed. Six months on: no duplicates, no token disconnections. With everything behind one connector interface, a Moneybird connector followed in three days, and six new customers the next quarter named the accounting integration as a reason for choosing the product.

"It worked perfectly in the demo. Three months later nine accountants found three hundred and twelve invoices twice, and four administrations had our VAT on the wrong code." - Iris Meijer

https://launchstudio.eu/en/blog/lovable-integrations-connecting-exact-online-and-moneybird

#ExactOnline #Moneybird #Integrations #SaaS #LaunchStudio #Manifera
