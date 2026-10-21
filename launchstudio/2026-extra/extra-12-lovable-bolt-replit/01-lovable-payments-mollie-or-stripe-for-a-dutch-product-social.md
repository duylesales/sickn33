🚨 Wouter Nagelkerke built Vaarschool Online with Lovable — €79 theory courses for the Dutch boating licence. He integrated Stripe because the tutorials did, and launched with card payments only. Checkout conversion sat at 31%, which he assumed was normal. 😳

He asked one question in the abandonment email. Of 46 replies, 38 said some version of "I don't use a credit card." Here's what a Dutch checkout needs: 🧠

❌ A card-only checkout for Dutch consumers who pay with iDEAL
❌ The Stripe secret key sitting in the frontend bundle since launch
❌ Prices posted from the browser and trusted by the server
❌ Unverified webhooks — a retried event granted a second course enrolment

✅ iDEAL enabled and placed as the default payment method
✅ Checkout created server-side, with the price looked up from the database
✅ Webhook signature verification plus an idempotency key
✅ A payments table in his own database, and abandoned iDEAL flows that expire cleanly

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we pick the payment provider for your actual customers — and wire it up so it can't be abused. 💳

His result: four business days and €2,150 later, checkout conversion went from 31% to 68% in the first month on the same traffic — and the weekly duplicate-enrolment emails stopped entirely. 🚀

👉 Mollie or Stripe for a Dutch product: https://launchstudio.eu/en/blog/lovable-payments-mollie-or-stripe-for-a-dutch-product

#iDEAL #Mollie #Stripe #Lovable #LaunchStudio #Manifera
