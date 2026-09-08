🚨 Sander de Wit's referral programme paid out roughly €2,400 in credits in eleven days — about €300 of it to real customers. 😳

A referral reward feels like a marketing widget. Here's what it actually is: 🧠

❌ €20 in credit was paid on signup, with no verification — a reward that's trivially farmed
❌ One participant generated 40 signups using plus-addressed variants of two Gmail accounts and three disposable domains
❌ Credits were stored as a single balance number, so there was no record of which credit came from which referral
❌ Reversing the fraud meant reconstructing it by hand from signup timestamps and email patterns — catching two genuine customers in the cleanup

✅ Reward on first payment, or first payment plus a 30-day retention window — never on signup
✅ Normalise email addresses before comparing them to kill plus-addressing and dot-variant self-referrals
✅ Record every credit as a separate ledger entry — what, when, how much, why — not one mutable balance
✅ Track processed webhook event IDs so a payment-provider retry never credits the same referral twice

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we treat referral programmes like the small payments systems they actually are. 💸

His result: referral logic, ledger, and abuse controls rebuilt in 4 business days — the relaunched programme produced 34 paying customers over the next four months with no material abuse. 🚀

👉 Treat your referral programme like the payments system it is: https://launchstudio.eu/en/blog/referral-flows-and-the-abuse-you-should-expect

#SaaS #GrowthEngineering #FraudPrevention #IndieHacker #LaunchStudio #Manifera
