🚨 Sophie Mertens runs pottery workshops in Mechelen and built Kleiatelier in Lovable: people book a workshop, pay and get preparation emails. Lovable connected a Stripe Payment Link per workshop. Payments came in - but the app had no idea who had paid. Sophie matched payments to bookings by hand every evening, and twice a workshop was overbooked. 😳

Payment Links got her paid. They just didn't tell her app who had paid for what. Here's what was missing: 🧠

❌ Payments not linked to bookings or user accounts
❌ Unpaid reservations holding places indefinitely
❌ No webhook confirming bookings after payment
❌ Evenings spent reconciling Stripe and the booking list by hand

✅ Stripe Checkout sessions created server-side per booking, with the booking ID in metadata
✅ Bancontact and iDEAL enabled
✅ A webhook that confirms the booking only after payment
✅ Unpaid reservations released automatically after 30 minutes, plus preparation emails on confirmation

At **LaunchStudio**, backed by Manifera's 11+ years of Stripe, Mollie and PayPal integrations, we pick the simplest Stripe option that fits your stage - with webhooks that keep your app in sync. 🛠️

💡 Her result: €1,450, five business days. Manual matching stopped completely, overbooking disappeared, and a waiting list now offers released places to the next person automatically. 🚀

👉 Stripe Checkout, Payment Links or embedded payments? Here's which fits your AI-built app at each stage: https://launchstudio.eu/en/blog/stripe-checkout-vs-payment-links-vs-embedded-payments

#Stripe #Payments #Bancontact #iDEAL #LaunchStudio #Manifera
