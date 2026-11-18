🎭 Two systems, one ticket (dramatized)

REDIRECT PAGE: The buyer's back from iDEAL. I'll create their tickets.
WEBHOOK: Mollie just called me. I'll create their tickets too.
REDIRECT PAGE: Did you check whether I already made them?
WEBHOOK: No. Did you check whether they actually paid?
REDIRECT PAGE: No.
THE VENUE MANAGER, at the premiere: Why do two people have seat 14?

Ruben Hoekstra runs a small theatre company in Leeuwarden and built Zaalkaart with Lovable and Supabase, selling performance tickets with iDEAL through Mollie. Sales went well, until the premiere of a popular show. Several seats were assigned to two buyers. And a handful of buyers had paid but had no ticket at all.

What the review found:
• Tickets created on the redirect page, so buyers who closed their phone browser early got nothing
• A webhook added later "to make sure," also creating tickets, without checking for existing ones
• A handler that trusted incoming requests without fetching the payment status from Mollie
• Confirmation emails sent before responding, causing timeouts and retries during busy sales

The fix (LaunchStudio, 5 business days, €2,100):
✓ One handler that fetches each payment from Mollie, records the webhook by payment ID, and creates tickets in a single transaction that also locks the seats
✓ A redirect page that only shows status, waiting for the webhook to finish
✓ Emails in a background job, with an immediate response, and an error on failed processing so Mollie retries
✓ The premiere reconciled: duplicates refunded, missing tickets issued, double-booked seats resolved with the venue
✓ A daily reconciliation job, with alerts

The next sales opening, for a sold-out comedy show: around 900 tickets in the first hour, not one duplicate or missing ticket.

"I had two systems creating tickets and neither of them trusted the other. Now there is one, and it only trusts Mollie." - Ruben Hoekstra

https://launchstudio.eu/en/blog/payment-webhook-fix-service-for-ai-built-apps

#Webhooks #Mollie #Stripe #Lovable #AIFounder #LaunchStudio #Manifera
