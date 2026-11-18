📒 END OF MONTH RECONCILIATION

The app says: 212 fees paid
Mollie says: 174 fees paid
Difference: 38 members who hadn't paid, marked as paid

Sjoerd Wiersma, treasurer of a korfball club in Leeuwarden, built Contributieman with Bolt so members could pay annual fees and match day contributions online instead of by bank transfer. The club already had a Mollie account, so Bolt generated a flow that sent members to Mollie and back.

Why the two columns disagreed:
• The return page marked anyone who reached it as paid, including members who cancelled in their banking app or let the payment expire
• There was no webhook at all
• The Mollie live key sat in a frontend environment file
• Amounts were sent from the browser

What LaunchStudio changed (7 business days, €1,700):
✓ Payment creation moved into a Supabase edge function, with amounts set on the server
✓ A Mollie webhook that fetches the real payment status from the API and updates memberships idempotently
✓ Every status mapped to a clear message for members
✓ The exposed key rotated
✓ A monthly reconciliation report comparing app and Mollie totals

NEXT MONTH'S RECONCILIATION
The app says: matches Mollie
Mollie says: matches the app
Difference: €0.00

That season, the club collected 96% of annual fees online. The 38 members wrongly marked as paid were contacted and settled within two weeks.

"The app said everyone had paid. The bank said otherwise. I didn't know a webhook was the thing standing between those two numbers." - Sjoerd Wiersma

https://launchstudio.eu/en/blog/mollie-integration-for-ai-built-apps-step-by-step

#Mollie #iDEAL #Supabase #Bolt #LaunchStudio #Manifera
