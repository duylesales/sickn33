🚨 Isabelle Moreau built PayRail, a payroll SaaS in Lyon, with a Stripe integration coded in v0 back when she had a handful of pilot customers on one flat rate. At 200+ paying customers on tiered pricing, a customer emailed asking why they'd been charged twice for the same upgrade — Isabelle checked her dashboard and found six more identical cases she'd never noticed, each needing a manual refund. 😳

Billing bugs that are invisible at 12 customers become a weekly spreadsheet of refunds at 200. 🧠

❌ Webhook retries occasionally double-processed plan upgrades, with no idempotency check on event IDs
❌ Failed payments didn't consistently move customers into a proper past_due state
❌ No dunning logic existed to retry failed cards before access got cancelled
❌ No monitoring at all — the first signal of a problem was always a confused customer's email

✅ Implemented idempotent webhook handling keyed to Stripe event IDs
✅ Built a real subscription state machine covering trialing, past_due, and grace-period states
✅ Added dunning logic with automated retry emails, deployed onto managed, monitored hosting

At **LaunchStudio**, we harden exactly this billing-and-scale transition for growing SaaS founders — the same standard of engineering Manifera has delivered for clients like Vodafone and TNO. 🛡️

Isabelle's result: PayRail's billing now behaves like a real subscription system instead of a payment button that happened to work most of the time. 🚀

👉 Scaling past MVP with real billing on the line: check whether your Stripe setup can take it: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #SaaSBilling #StripeIntegration
