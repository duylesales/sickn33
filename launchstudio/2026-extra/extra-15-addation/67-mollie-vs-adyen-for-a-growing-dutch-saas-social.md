🚨 Bram Hoekstra built Zaalkassa with Bolt and Supabase: ticketing and memberships for Dutch theatres and concert venues, running on Mollie. After a strong season, an adviser said to move to Adyen "because serious companies use it". Bram began planning a migration. 😳

A year of payment data told a more nuanced story. Most revenue came through iDEAL and SEPA, where provider costs differed little. The real issues were in the integration. Here's how to choose between Mollie and Adyen for a growing Dutch SaaS: 🧠

❌ Webhooks not processed idempotently, causing duplicate tickets
❌ Refunds for cancelled shows handled manually
❌ Payouts not reconciling with accounting
❌ A migration that would mean re-collecting around 2,600 membership mandates

✅ Staying with Mollie for now, with idempotent webhooks keyed on payment IDs
✅ Automated refunds for cancelled performances
✅ Daily reconciliation between Mollie settlements and records, plus accounting exports
✅ A provider abstraction and concrete thresholds for when Adyen makes sense

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we help you make the grown-up decision, not the impressive one. 🛠️

His result: €4,400, 11 business days. Duplicate tickets and manual refunds disappeared, venues got reconciled reports - and when card volumes grew, the data and abstraction were ready to evaluate Adyen properly. 🚀

👉 Mollie or Adyen for your SaaS? Here's how to decide: https://launchstudio.eu/en/blog/mollie-vs-adyen-for-a-growing-dutch-saas

#Mollie #Adyen #Payments #EventTech #AIFounder #LaunchStudio #Manifera
