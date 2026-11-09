💳 Iris Bos built Thuisfit with Bolt and Supabase: home workout programmes, billed monthly by SEPA direct debit through Mollie and yearly by card for some users. At around 3,000 subscribers, she noticed something odd: revenue in Mollie didn't match active subscribers in her app. 🤔

Some users whose banks had reversed their payments still had full access, for months. Here's what the investigation found: 🧠

❌ Direct debit reversals never processed by the app
❌ Refunds done by hand in Mollie, without touching access or invoices
❌ Card disputes lost for lack of evidence, plus an old company name on statements
❌ No way to cancel in the app, so some users disputed instead

✅ Webhooks for refunds, reversals and chargebacks that update access automatically
✅ Friendly emails with an iDEAL payment link and a grace period after reversals
✅ Refunds via the Mollie API with idempotency and proper credit notes
✅ Automatic dispute evidence, a fixed descriptor, renewal reminders and two-click cancellation

At **LaunchStudio**, backed by Manifera's 11+ years of building payment and billing systems, we make refunds, reversals and disputes flow through your app instead of your inbox. 🛠️

Her result: €4,200, ten business days. Within two months revenue and subscriptions reconciled, recovered payments covered the project several times over and disputes dropped sharply. 🚀

👉 How to handle refunds and chargebacks in your SaaS: https://launchstudio.eu/en/blog/how-do-i-handle-refunds-and-chargebacks-in-my-saas

#SaaS #Payments #Mollie #Bolt #AIFounder #LaunchStudio #Manifera
