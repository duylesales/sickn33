Imagine you're an annual subscriber to a home workout app. 🏋️

A charge appears on your card statement under a company name you don't recognise. There's no reminder that your renewal was coming. You look for a cancel button in the app. There isn't one; you'd have to email. So you do what feels easiest: you dispute the charge with your bank.

Now switch seats. You're Iris Bos.

Iris built Thuisfit with Bolt and Supabase: home workout programmes, billed monthly by SEPA direct debit through Mollie after a first iDEAL payment, and annually by card for some users. At around 3,000 subscribers, revenue in Mollie didn't match the active subscribers in her app. Here's why:
• Direct debit reversals were never processed, so users whose banks reversed payments kept full access, some for months
• Refunds were done by hand in the Mollie dashboard, without updating access or invoices
• Card disputes were usually lost, because there was no evidence to send
• Many disputes came from customers who didn't recognise the charge, since the descriptor showed an old company name
• There was no in-app cancellation

What LaunchStudio built (10 business days, €4,200):
✓ Webhooks for refunds, reversals and chargebacks that update subscription status and access automatically
✓ After a reversal: a friendly email with an iDEAL payment link, and a grace period before access pauses
✓ Refunds as an admin action through the Mollie API, idempotent, with credit notes and access adjusted
✓ Automatic evidence for disputes: terms acceptance, login and workout history, receipts
✓ An updated billing descriptor, and renewal reminders two weeks before annual renewals
✓ Cancellation in the app, in two clicks

Within two months, revenue and active subscriptions reconciled. Recovered reversed payments paid for the project several times over. Card disputes dropped sharply, and Iris won most of the remaining ones with the automated evidence.

"I was paying the price of being easy to dispute and hard to cancel. Fixing both turned out to be good for customers and for revenue." - Iris Bos

https://launchstudio.eu/en/blog/how-do-i-handle-refunds-and-chargebacks-in-my-saas

#SaaS #Payments #Mollie #Bolt #AIFounder #LaunchStudio #Manifera
