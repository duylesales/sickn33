🔐 Thijs Kooiman built Handelspunt, a B2B marketplace connecting Zwolle-region wholesalers with independent retailers, using Bolt in three weeks. Everything worked in testing — until LaunchStudio's pre-launch review found the Stripe webhook wasn't verified against Stripe's signing secret. Anyone could have forged a "payment succeeded" event and marked an order paid without ever paying. 😳

AI writes fast code, not automatically secure code — and payment flows are where that gap gets expensive. 🧠

❌ Checkout sessions were created correctly server-side, but webhook events went unverified
❌ Anyone could forge a fake payment confirmation and get free inventory
❌ Admin inventory routes had no role-based access control locking them down
❌ None of this showed up in normal testing — only an adversarial review catches it

✅ Rebuilt the webhook verification layer against Stripe's signing secret
✅ Added idempotency handling to block duplicate order processing
✅ Locked admin inventory routes behind proper role-based access control

At **LaunchStudio**, Manifera's 120+ engineers — the same team behind projects for Vodafone and cybersecurity firm CFLW — run this exact threat-modeling process on every AI-built checkout flow. 🛡️

Handelspunt processed its first 200 real transactions with zero fraudulent orders, and Thijs onboarded twelve wholesalers in his first month. 🚀

👉 Processing payments in Zwolle? Verify your webhooks before you take real money: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #Zwolle #PaymentSecurity
