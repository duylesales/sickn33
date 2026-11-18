You're scrolling Instagram and find a ceramics workshop for Thursday evening. 🏺

You tap book. You pay with iDEAL. Your banking app opens, you confirm, the money leaves your account. Then a message comes in, and you never switch back to the browser.

On Thursday, you show up. You're not on the attendee list.

That happened again and again on Ambachtsavond. Bram de Vries built it with Bolt and Supabase: ceramicists, woodworkers, bakers and other craftspeople sell places in evening workshops, paid upfront with iDEAL or card through Mollie. About 45 hosts, mostly mobile visitors from social media. Hosts heard "but I paid!", and Bram's numbers showed roughly 20% of started checkouts never completing.

The Mollie dashboard explained it:
• Bookings were confirmed only when customers came back to the return page, so many paid iDEAL bookings stayed "pending"
• The custom card form generated in Bolt didn't handle 3D Secure, so some bank cards got stuck in authentication
• Anyone who reached the success URL got a confirmed booking, even without paying
• Discount codes sometimes produced amounts like €42.499, which Mollie rejected

The fix (LaunchStudio, 6 business days, €2,400):
✓ Mollie's hosted checkout, handling 3D Secure and every payment method
✓ Bookings confirmed only by a verified Mollie webhook
✓ A return page that checks with the server: "Payment received" or "We're confirming your payment"
✓ A success URL that changes nothing
✓ Amounts in cents on the server, with discounts rounded consistently, and idempotency against duplicate payments
✓ Alerts when webhooks fail or the paid-to-started ratio drops
✓ Historical bookings reconciled against Mollie: 37 customers who had paid were added to their workshops

Checkout completion rose from about 80% to 94%. Missing-booking complaints stopped. Booking revenue grew around 17% in two months, with no extra traffic.

"I thought some customers just changed their minds. Most of them had paid; my app simply didn't believe them." - Bram de Vries

https://launchstudio.eu/en/blog/why-do-some-customers-payments-fail-at-checkout

#Payments #Mollie #iDEAL #3DSecure #AIFounder #LaunchStudio #Manifera
