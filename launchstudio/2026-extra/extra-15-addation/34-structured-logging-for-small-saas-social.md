🚨 Joris Peters built Leskaart with Bolt and Supabase: dance and yoga studios sell class cards and subscriptions through Mollie. One studio owner noticed members who had paid for ten-class cards still showed zero classes. 😳

Investigating took two days. The logs were full of names, emails and phone numbers - but said nothing about whether processing had worked. A schema change had broken card crediting eleven days earlier, affecting 63 payments across five studios. Here's why small SaaS needs structured logging: 🧠

❌ console.log dumping full requests and member data
❌ No request IDs to trace what happened
❌ A webhook returning 200 even when the database update failed
❌ Default log retention and no reconciliation

✅ A structured logger recording receipt, verification, result and duration with internal IDs only
✅ Request IDs on every request, returned in error messages
✅ Webhook errors returning a failure status so Mollie retries, with alerts
✅ 30-day retention and a daily job comparing Mollie payments with credited cards

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make your logs tell you what happened - and nothing about anyone's personal life. 🛠️

His result: €2,400, 7 business days. All 63 payments credited. Two months later, an alert fired within minutes of a provider timeout, and Joris found the full story in under five minutes. 🚀

👉 Can your logs explain what went wrong? Here's how to set up structured logging: https://launchstudio.eu/en/blog/structured-logging-for-small-saas

#Logging #Observability #Mollie #SaaS #AIFounder #LaunchStudio #Manifera
