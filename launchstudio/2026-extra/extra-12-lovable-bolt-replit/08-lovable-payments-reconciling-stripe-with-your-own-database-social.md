🚨 Joost Berkhout's Inschrijfpunt handles registration and payment for 22 running and cycling event organisers. One Saturday morning in May his webhook handler was down for eleven minutes during a deploy - exactly when registration opened for his biggest event of the year. 😳

Seventeen people paid. The money arrived. His app never knew. The organiser found out on race day, when seventeen runners showed up with payment confirmations and no bib numbers. Here's why your database drifts away from Stripe: 🧠

❌ Webhooks treated as guaranteed - they're retried, then abandoned
❌ No provider reference stored on payment rows
❌ Handlers that process before recording the event, with no transaction around the writes
❌ Nobody ever comparing provider, database and bank

✅ A monthly reconciliation query (and after every deploy) producing three difference lists
✅ Payout records linked to their transactions, so every bank deposit explains itself
✅ Events recorded before processing, wrapped in a transaction, idempotent on the event ID
✅ An unhandled-events list and a documented replay procedure - no hand-edited rows

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your revenue figures, entitlements and bank statements in step. 🔄

His result: two business days and €1,850 later, the seventeen runners were reinstated through the normal code path instead of typed in by hand. Over the next year reconciliation caught four more small gaps within a month each - and the organiser renewed. 🚀

👉 Reconciling Stripe with your own database: https://launchstudio.eu/en/blog/lovable-payments-reconciling-stripe-with-your-own-database

#Stripe #Webhooks #Reconciliation #Lovable #LaunchStudio #Manifera
