💬 A conversation nobody in the app was listening to (dramatized)

MOLLIE: Hi, this guest just paid for Saturday's workshop.
APP: (not listening)
GUEST: (closed the tab before reaching the thank-you page)
APP: No thank-you page, no booking.
GUEST, ON SATURDAY: Here's my bank statement. Where's my seat?

ANOTHER GUEST: (reopens an old thank-you link from browser history)
APP: Thank-you page! Booking confirmed. Paid.
MOLLIE: There's no payment for that one.
APP: (not listening)

MOLLIE: This booking has been refunded.
APP: (not listening. The seat stays taken.)

Rick Jonker, a chef who runs cooking workshops in Hattem, built Pannenklaar in Lovable: guests book a workshop seat, pay through Mollie, and get a confirmation with the menu and ingredients list. The workshops sold well, sometimes too well. And every week brought the puzzles above. Rick had no idea what a webhook was. His app confirmed bookings when guests reached the thank-you page.

A webhook is Mollie calling your app to say what really happened to a payment. Mollie had been trying to tell him the truth all along.

What LaunchStudio changed (5 business days, €1,350):
✓ Mollie webhooks that look up the payment status on every notification
✓ Booking confirmation based only on that status
✓ Repeated and out-of-order notifications handled
✓ Seats released automatically on refunds and expired payments
✓ Confirmation emails sent from a background job, triggered by the webhook
✓ Alerts when webhook processing fails
✓ The past two months of bookings reconciled against Mollie's records

Unmatched payments and phantom bookings stopped completely. Seats freed by refunds now get resold, adding an estimated €600 a month. And Rick spends Monday mornings cooking, not reconciling.

"I thought the thank-you page meant someone had paid. It turned out Mollie had been trying to tell me the truth all along - I just wasn't listening." - Rick Jonker

https://launchstudio.eu/en/blog/ai-code-to-production-explained-what-a-webhook-is-and-why-payments-depend-on-it

#Webhooks #Payments #Mollie #Lovable #LaunchStudio #Manifera
