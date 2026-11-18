BEFORE ➜ AFTER: a photographer marketplace's money flow 📸

Sander de Jong built Fotograafvinder with Lovable and Supabase: couples and companies book freelance photographers for weddings, events and portraits. At around 150 bookings a month, the payment model started to crack.

BEFORE: Every payment landed in one Stripe account owned by Sander. His accountant questioned whether he was effectively holding client money without the right structure.
AFTER: Stripe Connect with Express accounts. Photographers complete Stripe's hosted onboarding, and listings become bookable only after verification.

BEFORE: Every Friday, Sander transferred photographers' shares from his business bank account by hand, keeping 12%.
AFTER: Separate charges and transfers. The platform charges deposits and final payments, and releases transfers automatically once a shoot is marked complete, minus the platform fee.

BEFORE: Refunds for cancelled shoots calculated by hand.
AFTER: Refunds that reverse transfers and fees according to the cancellation policy, in seconds.

BEFORE: A wedding chargeback left Sander out of pocket, because the photographer was already paid.
AFTER: Disputes trigger an evidence collection flow.

BEFORE: Payment confirmed by the success page redirect, so customers who closed the browser early never showed as paid.
AFTER: Verified webhooks for the platform and connected accounts, processed idempotently, plus a daily reconciliation with the database.

BEFORE: The Stripe secret key in a frontend file.
AFTER: Rotated, and server-side.

The work: 17 business days, €6,800. The next six months: around 1,100 bookings, no more Friday transfers, an accountant who approved the structure, and two disputes won with automatically collected evidence.

"I was running a marketplace with a spreadsheet and a bank app. Stripe Connect turned it into a payment system I can actually trust." - Sander de Jong

https://launchstudio.eu/en/blog/stripe-connect-for-marketplaces-built-with-ai

#StripeConnect #Marketplace #Payments #Lovable #AIFounder #LaunchStudio #Manifera
