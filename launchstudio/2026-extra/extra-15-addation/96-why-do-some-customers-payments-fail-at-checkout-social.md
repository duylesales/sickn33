🚨 Bram de Vries built Ambachtsavond with Bolt and Supabase: ceramicists, woodworkers and bakers sell places in evening workshops, paid upfront with iDEAL or card through Mollie. About 45 hosts listed workshops. Then hosts complained: customers said they'd paid, but weren't on the attendee list. 😳

Roughly 20% of started checkouts never completed. The Mollie dashboard showed why. Here's why some customers' payments fail at checkout: 🧠

❌ iDEAL payments "paid" at Mollie, bookings "pending" - confirmed only on the return page
❌ A custom card form that didn't handle 3D Secure
❌ A success URL that confirmed bookings without any payment
❌ Discounted prices like €42.499 that Mollie rejected

✅ Mollie's hosted checkout handling 3D Secure and all methods
✅ Bookings confirmed only by a verified Mollie webhook, with a polling return page
✅ Amounts calculated in cents on the server, plus idempotency
✅ Alerts on failed webhooks, and 37 customers who'd paid added to their workshops

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make your app believe customers who actually paid. 🛠️

The result: €2,400, 6 business days. Checkout completion rose from about 80% to 94%, and monthly booking revenue rose by around 17% in two months - without more traffic. 🚀

👉 Losing customers at checkout? Here are the causes and fixes: https://launchstudio.eu/en/blog/why-do-some-customers-payments-fail-at-checkout

#Payments #Mollie #iDEAL #3DSecure #AIFounder #LaunchStudio #Manifera
