🗓️ A dietitian platform's payment calendar

BEFORE
Jan: iDEAL link by email ➜ chase
Feb: iDEAL link by email ➜ chase
Mar: iDEAL link by email ➜ chase
...every month, around a third paying late or not at all

AFTER
Jan: one iDEAL payment ➜ mandate created
Feb to Dec: collected automatically

Marloes Heijnen, a dietitian in Maastricht, built Dieetbox with Lovable: dietitians share meal plans, shopping lists and progress check-ins with clients for a monthly fee. Her own practice and four colleagues used it with about 150 clients. Lovable had generated a monthly payment link by email, so Marloes spent hours every month chasing payments. Access was never revoked, because the app had no idea what an unpaid month was. And when she asked for "automatic monthly iDEAL," Lovable built a scheduled function that emailed new links more often.

The mandate flow LaunchStudio built under her existing screens (12 business days, €3,600, plus €49/month managed hosting):
✓ A Mollie customer for each client
✓ A first iDEAL payment with sequenceType "first"
✓ Subscriptions on the resulting mandate
✓ A webhook keeping a subscription status per client
✓ For failed debits, a friendly email with a one-click iDEAL catch-up payment, and a seven-day grace period
✓ Payment status shown next to each client for dietitians

Within two billing cycles, on-time collection rose from about 65% to 97%. Marloes stopped chasing entirely, and two more dietitians joined because the payment side "just worked."

"My clients still say they pay with iDEAL. They just only do it once." - Marloes Heijnen

https://launchstudio.eu/en/blog/ideal-recurring-payments-for-saas-sepa-direct-debit-with-mollie

#iDEAL #SEPA #Mollie #SaaS #LaunchStudio #Manifera
