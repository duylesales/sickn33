🎭 Ruben Hoekstra runs a small theatre company in Leeuwarden and built Zaalkaart with Lovable and Supabase to sell tickets, with iDEAL payments through Mollie. Sales went well until the premiere of a popular show. Then the venue manager found seats assigned to two different buyers, and buyers who had paid but had no tickets. 😳

The review found two systems creating tickets, and neither trusted the other: 🧠

❌ Tickets created on the redirect page, so closing the browser early meant no ticket
❌ A webhook added later that created tickets again without checking for duplicates
❌ No payment status fetched from Mollie, so the handler trusted any request
❌ Emails sent before responding, causing timeouts and retries during busy sales

✅ Every payment fetched from Mollie and recorded by payment ID
✅ Tickets created in one transaction that also locks the seats
✅ Emails moved to a background job and failed processing returning an error so Mollie retries
✅ A reconciliation of the premiere plus a daily reconciliation job with alerts

At **LaunchStudio**, backed by Manifera's 11+ years of building payment and integration systems, we make payment webhooks verified, idempotent and monitored, at a fixed price. 🛠️

His result: €2,100, five business days. The next sales opening processed around 900 tickets in the first hour without a single duplicate or missing ticket. 🚀

👉 Payment webhook fix service for AI-built apps: https://launchstudio.eu/en/blog/payment-webhook-fix-service-for-ai-built-apps

#Webhooks #Mollie #Stripe #Lovable #AIFounder #LaunchStudio #Manifera
