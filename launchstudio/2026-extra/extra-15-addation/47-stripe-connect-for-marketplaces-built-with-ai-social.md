🚨 Sander de Jong built Fotograafvinder with Lovable and Supabase: couples and companies book freelance photographers. Customers paid into Sander's own Stripe account, and every Friday he transferred photographers' shares from his business bank account, keeping 12%. 😳

At around 150 bookings a month, it cracked. His accountant questioned whether he was holding client money without the right structure. A chargeback left him out of pocket. Here's how Stripe Connect works for marketplaces built with AI: 🧠

❌ Manual Friday transfers from a bank account
❌ Refunds for cancelled shoots calculated by hand
❌ Payment confirmed by the success page redirect
❌ The Stripe secret key in a frontend file

✅ Stripe Connect Express with hosted onboarding, bookable only after verification
✅ Separate charges and transfers, released automatically after the shoot minus the platform fee
✅ Verified, idempotent webhooks, refunds that reverse transfers and a dispute evidence flow
✅ The key rotated server-side and a daily reconciliation job

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn a spreadsheet-and-bank-app marketplace into a payment system you can trust. 🛠️

His result: €6,800, 17 business days. Manual transfers ended, the accountant approved, around 1,100 bookings were processed in six months - and two disputes were won with automatically collected evidence. 🚀

👉 Building a marketplace? Here's how Stripe Connect handles payouts properly: https://launchstudio.eu/en/blog/stripe-connect-for-marketplaces-built-with-ai

#StripeConnect #Marketplace #Payments #Lovable #AIFounder #LaunchStudio #Manifera
