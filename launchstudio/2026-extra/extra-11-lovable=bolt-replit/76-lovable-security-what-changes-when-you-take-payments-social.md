🚨 Bas Tolhuizen's Lesgeld collects lesson fees for 31 music schools, driving instructors and sports clubs around Roermond - about €40,000 a month. The payment webhook accepted any request and never checked the provider's signature. Someone sent it a forged "payment succeeded" event. It worked. 😳

Over eleven days, 23 accounts were activated without a single payment - and used to collect real money from real parents. Here's what changes once you take payments: 🧠

❌ A webhook that trusts whatever reaches it
❌ No deduplication, so retried notifications create duplicate subscriptions
❌ Plan or amount decided in the browser instead of on the server
❌ Anyone on the team able to issue refunds, with no record of why

✅ Verify every webhook signature - and re-validate historical events against the provider
✅ Deduplicate on event ID and keep the endpoint reliably reachable
✅ Determine plans and amounts server-side; enable rate limits and the provider's fraud tools
✅ An immutable audit trail for every money operation, with restricted refund rights

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make the money path sound before your first real payment. 💳

His result: nine business days and €4,300 later, the fraudulent accounts were closed and parents refunded by the provider. The same work found four duplicate subscriptions that had been quietly overcharging customers. Reconciliation has balanced every month since. 🚀

👉 What changes when your Lovable app takes payments: https://launchstudio.eu/en/blog/lovable-security-what-changes-when-you-take-payments

#Payments #Webhooks #Lovable #FinTech #LaunchStudio #Manifera
