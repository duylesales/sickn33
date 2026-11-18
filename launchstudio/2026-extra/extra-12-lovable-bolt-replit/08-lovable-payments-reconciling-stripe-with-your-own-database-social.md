On race day in September, seventeen runners arrived at the registration desk with payment confirmations, and no bib numbers. 🏃

The story started months earlier, on a Saturday morning in May.

Joost Berkhout built Inschrijfpunt with Lovable: registration and payment handling for running events and cycling tours, used by 22 organisers charging entry fees of €12 to €45. His webhook handler worked. But that Saturday, during a deploy, it was down for eleven minutes. And that happened to be the morning registration opened for the biggest event of his year.

Seventeen people paid in those eleven minutes. Their money reached the provider, and Joost's bank account. His application never heard about them. So they never appeared on the start list, until the organiser found out at the desk.

Afterwards, LaunchStudio made sure the app could never quietly miss a payment again (2 business days, €1,850):
✓ The provider reference stored on every payment row
✓ A reconciliation query producing three difference lists, run monthly and after every deploy
✓ Payout records stored with their transactions, so bank deposits explain themselves
✓ The webhook handler rewritten to record each event before processing, wrapped in a transaction, and idempotent on the event ID
✓ A list of unhandled events on the admin page
✓ A documented replay procedure

That replay procedure was then used to recover the seventeen registrations through the normal code path, sending the confirmations and creating the start-list entries that had never existed. No typing them in by hand.

Over the following year, reconciliation caught four more gaps, all small, all within a month. And the organiser renewed.

"Eleven minutes of downtime on a Saturday morning, and I found out about it on a Sunday in September with seventeen people standing at a registration desk." - Joost Berkhout

https://launchstudio.eu/en/blog/lovable-payments-reconciling-stripe-with-your-own-database

#Stripe #Webhooks #Reconciliation #Lovable #LaunchStudio #Manifera
