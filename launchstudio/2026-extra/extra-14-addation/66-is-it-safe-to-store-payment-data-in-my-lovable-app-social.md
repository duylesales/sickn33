🚨 Dennis Groot organises regional board game conventions and built Spelbeurs in Bolt for tickets and tournament tables. He asked Bolt for "faster checkout for returning visitors". Bolt built a form that saved card numbers, expiry dates and CVC codes in a saved_cards table. A developer friend found it while fixing an unrelated bug: 312 cards. 😳

He asked for faster checkout. He got a database full of card numbers that should never have existed. Here's how bad it was: 🧠

❌ Full card numbers and CVC codes stored in his own database
❌ Card details sent from his app to the payment API on every purchase
❌ The service key in the frontend, so anyone could have read the table despite RLS
❌ Payment fields showing up in logs

✅ The custom form and table removed, and stored card data securely deleted
✅ All keys rotated
✅ The provider's hosted checkout, with saved payment methods held by the provider itself
✅ Verified webhooks connected and payment fields scrubbed from logs

At **LaunchStudio**, backed by Manifera's 11+ years of Stripe, Mollie and PayPal integrations, "never touch card data" is a fixed rule - references only, never card numbers. 🛠️

💡 His result: €1,700, four business days. Returning visitors still get one-click checkout through the provider's saved payment methods, and the app no longer stores any card data at all. 🚀

👉 Is your AI-built app storing payment data it shouldn't? Here's what you may and may not keep: https://launchstudio.eu/en/blog/is-it-safe-to-store-payment-data-in-my-lovable-app

#PCIDSS #Payments #Stripe #AppSecurity #LaunchStudio #Manifera
