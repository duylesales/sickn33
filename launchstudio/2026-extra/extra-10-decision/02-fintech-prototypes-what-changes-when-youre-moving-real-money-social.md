🚨 Bram thought Vakwerk was just Stripe with extra steps. It was actually holding client funds in one pooled balance, with no segregation, no reconciliation, and a webhook nobody had verified. 😳

Founders routinely underestimate the moment a payment processor turns into a payment service. Here's the line that flips it: 🧠

❌ One pooled Stripe balance representing every client's held payment, with zero segregation
❌ A database `balance` field overwritten on every transaction — no audit trail at all
❌ Supabase and Stripe's actual balance had never been reconciled against each other
❌ The webhook endpoint accepted "payment succeeded" events with no signature verification

✅ Holding funds before releasing them makes you a payment service, not a merchant using a processor
✅ Route held funds through a BaaS partner offering compliant escrow-style holding with safeguarding built in
✅ Replace the overwritten balance field with an append-only ledger table
✅ Add a nightly reconciliation job and close the webhook signature gap

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we tell founders exactly when "add Stripe" stops being the whole answer. 💳

His result: Vakwerk relaunched on a payment partner that handled safeguarding and reporting, freeing Bram to focus on marketplace growth instead of an accidental compliance burden. 🚀

👉 Find out if your product is quietly becoming a payment institution: https://launchstudio.eu/en/blog/fintech-prototypes-what-changes-when-youre-moving-real-money

#FinTech #PSD2 #StartupFounders #Marketplace #LaunchStudio #Manifera
