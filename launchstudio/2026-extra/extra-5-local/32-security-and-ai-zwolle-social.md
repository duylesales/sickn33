If I wanted to steal from Handelspunt before launch, I wouldn't have needed to hack anything. 🕵️

Here's the marketplace through an attacker's eyes.

Handelspunt is a B2B marketplace connecting Zwolle-region wholesalers with independent retailers. Thijs Kooiman built it in Bolt in three weeks. Sellers list inventory, buyers place orders, and payments run through a Stripe integration that Bolt scaffolded automatically. In testing, it worked beautifully.

The checkout itself was fine. Sessions were created server-side, correctly.

The weak spot was the message that comes back afterwards. When Stripe confirms a payment, it sends a webhook. Handelspunt never verified those webhooks against Stripe's signing secret. So anyone could forge a "payment succeeded" event and mark an order as paid without paying.

No exploit kit. No stolen password. Just a message the server believed.

LaunchStudio caught it in the pre-launch review and closed it (5 business days, €950):
🔐 Webhook verification rebuilt
🔐 Idempotency handling, so one order can't be processed twice
🔐 Admin inventory routes locked behind role-based access control

Then the real test: the first 200 real transactions. Fraudulent orders: zero. Twelve wholesalers from Zwolle's business district onboarded in the first month.

"I had no idea anyone could fake a payment confirmation until LaunchStudio showed me. That single fix probably saved us from our first real fraud case." - Thijs Kooiman

Think like an attacker before one does: https://launchstudio.eu/en/blog/security-and-ai-zwolle

#AINativeFounder #LaunchStudio #Manifera #Zwolle #PaymentSecurity
