🚨 2 AM, Daan's staring at a Stripe log: a customer was billed 40,000 API calls, dashboard showed 12,000. The metering code counted retries as separate events — nobody decided, it just shipped. 😳

Subscriptions, one-time, and usage-based pricing aren't flavors of one button — each needs a different backend, AI tools build the simplest: 🧠

❌ Subscriptions need proration, dunning, and renewal edge cases most AI checkouts skip
❌ One-time purchases often have no "account" concept — a problem once you sell an upgrade
❌ Usage-based billing needs a metering pipeline most prototypes lack
❌ A collapsed "is_paid" boolean breaks once dunning needs past-due versus canceled

✅ Match the model to usage: even usage fits a subscription, uneven usage justifies metering
✅ A reliable metering system counts each event once and reconciles against the customer's own dashboard
✅ Don't build usage infrastructure before real data exists — instrument first, decide in months
✅ Track customers as ongoing accounts from day one, even billing once

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we scope proration, metering, and dunning for production-ready billing. 🧾

His result: the pipeline now counts only delivered results, live in 13 days, closing the gap that had tripled one invoice. 🚀

👉 Talk to an engineer who reads AI-generated code: https://launchstudio.eu/en/blog/subscriptions-one-time-or-usage-based-choosing-before-you-build

#SaaS #BillingArchitecture #LaunchStudio #Manifera #StartupGrowth #ProductionReady
