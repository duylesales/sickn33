🔀 SHOULD YOU SWITCH PAYMENT PROVIDERS? A decision path from one ticketing SaaS

START: "Serious companies use Adyen."
That's what an adviser told Bram Hoekstra after a strong season. Bram built Zaalkassa with Bolt and Supabase: ticketing and memberships for Dutch theatres and concert venues, running on Mollie. He started planning a migration.

STEP 1: Where does your revenue come from?
A year of payment data: mostly iDEAL, plus SEPA direct debit for memberships. Cost differences between providers there were small.
➜ No strong reason to switch yet.

STEP 2: How big is your card volume?
Growing, but still moderate.
➜ Not yet.

STEP 3: What's actually hurting?
• Webhooks not processed idempotently, causing occasional duplicate tickets
• Refunds for cancelled shows handled by hand
• Payouts that didn't reconcile automatically with accounting
• Venues wanting one view of ticket sales and box office payments
➜ None of these are fixed by changing providers.

STEP 4: What would switching cost?
Re-collecting around 2,600 membership mandates.
➜ Expensive.

THE PATH TAKEN (LaunchStudio, 11 business days, €4,400)
✓ Stay with Mollie for now
✓ Idempotent webhook processing keyed on payment IDs
✓ Automated refunds for cancelled performances
✓ Daily reconciliation between Mollie settlements and Zaalkassa's records, plus accounting exports for venues
✓ A provider abstraction around payment creation, refunds and webhooks, so a future switch stays contained
✓ Concrete thresholds, based on card volume and international sales, for when an Adyen evaluation makes financial sense

THE OUTCOME
Duplicate tickets and manual refund work disappeared, and venues got reconciled reports. When international touring productions later pushed card volumes up, Bram had the data and the abstraction ready to evaluate Adyen properly.

"Switching providers felt like growing up. Fixing how we used the provider we had turned out to be the grown-up decision." - Bram Hoekstra

https://launchstudio.eu/en/blog/mollie-vs-adyen-for-a-growing-dutch-saas

#Mollie #Adyen #Payments #EventTech #AIFounder #LaunchStudio #Manifera
