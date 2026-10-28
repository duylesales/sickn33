🚨 Rick Jonker, a chef who runs cooking workshops in Hattem, built Pannenklaar in Lovable: guests book a seat, pay through Mollie and get a confirmation with the menu and ingredients list. Workshops sold well - sometimes too well. And every week brought a few puzzles. 😳

Guests arrived with bank statements showing payment, but no booking in the system. Other bookings were marked paid with no matching Mollie payment - some from guests who'd closed the tab and come back via the thank-you link in their history. Refunds in the Mollie dashboard never freed the seat, so workshops looked full when they weren't. Rick didn't know what a webhook was; the app confirmed bookings when guests reached the thank-you page. Here's what a webhook is - and why payments depend on it: 🧠

❌ The thank-you page treated as proof of payment
❌ Paid bookings missing, unpaid bookings confirmed
❌ Refunds that never reached the app
❌ No alerts and no reconciliation

✅ Mollie webhooks that look up the real payment status on every notification
✅ Booking confirmation depending only on that status, with repeats and out-of-order notifications handled
✅ Seats released automatically on refunds and expired payments, confirmation emails sent by a background job
✅ Alerts on failed webhook processing - and two months of bookings reconciled against Mollie's records

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure only the payment provider - not the thank-you page - decides what's paid. ⚙️

His result: €1,350, five business days. Unmatched payments and phantom bookings stopped entirely, freed seats are resold for an estimated €600 extra a month, and Rick spends Monday mornings cooking instead of reconciling. 🚀

👉 AI code to production explained: what a webhook is and why payments depend on it: https://launchstudio.eu/en/blog/ai-code-to-production-explained-what-a-webhook-is-and-why-payments-depend-on-it

#Webhooks #Payments #Mollie #Lovable #LaunchStudio #Manifera
