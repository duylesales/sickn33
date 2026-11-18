🕯️ IN MEMORIAM: Oppaskompas, for about four hours one Monday morning

Oppaskompas, built by Roos van Dam with Bolt and Supabase, helps parents in and around Breda find and book babysitters, with in-app messaging, Mollie payments and AI-assisted profile checks. About 2,800 families and 600 babysitters. One Monday morning, it stopped working: a certificate warning, no emails, and, once the warning was bypassed in testing, failing AI profile checks and SMS reminders.

Roos hadn't changed anything in weeks.

CAUSES OF DEATH
1. A personal credit card that had expired at the end of the previous month. The SMS provider suspended the account after failed payments, and the AI provider's prepaid credit ran out when auto-recharge failed.
2. An SSL certificate that didn't renew, because a Cloudflare setting changed two months earlier blocked the validation request. The renewal reminders went to the email of a freelancer who had set up DNS.
3. An SMTP credential revoked by the email service after a password reset, which Roos hadn't connected to the app.

None of it was in the code.

THE RESURRECTION (LaunchStudio, service restored on day one)
✓ Certificate validation fixed and the certificate renewed
✓ Billing on every service moved to a company card
✓ The SMS account reactivated, and AI credit topped up with alerts
✓ The SMTP connection replaced with an API key in server secrets
The app was fully available again within four hours.

THE AFTERLIFE (4 business days in total, €1,500)
✓ Every account moved to company email addresses, with two-factor authentication and a second admin
✓ DNS ownership transferred from the freelancer
✓ An expiry register with calendar reminders
✓ Monitoring for uptime, certificate expiry, failed emails and SMS, AI errors and low credit balances

In the following year, the register and alerts flagged eleven renewals and two quota warnings ahead of time. No unplanned outage since.

"Nothing in my code broke. My app died of a dead credit card, an old email address and a certificate nobody was watching." - Roos van Dam

https://launchstudio.eu/en/blog/why-did-my-app-stop-working-overnight

#Uptime #SSL #Monitoring #SaaSOps #AIFounder #LaunchStudio #Manifera
