☕ A coffee subscription's delivery calendar (before)

CYCLE 1: Charge and order created. Busy day, the function times out. It starts again from the beginning. Some customers charged twice.
CYCLE 2: A customer skips this delivery. Too late: the fulfilment export already went out by hand. Coffee arrives anyway.
CYCLE 3: A SEPA debit fails. Nothing happens. Deliveries just stop, without a word to the customer.
CYCLE 4, spring: The clocks change. The schedule shifts by an hour, and one cycle runs twice.
WEEKS LATER: A reversal. Never recorded.
ANY CYCLE: Want to cancel? Email us.

Vera Hofman runs a small coffee roastery in Deventer and built Bonenpost with Bolt and Supabase: freshly roasted beans every two or four weeks, paid through Mollie. With around 900 subscribers, the complaints followed the calendar. Every bug in a subscription comes back every cycle.

What LaunchStudio changed (8 business days, €3,200):
✓ Idempotency keys per subscription and per cycle on every charge
✓ Orders generated only from confirmed payments, via verified webhooks
✓ Cycle dates stored with time zone information, tested across clock changes
✓ A clear cut-off two days before roasting, shown in the customer portal
✓ A dunning flow for failed debits: retries, emails and a payment update link
✓ Reversals updating subscription status
✓ Orders sent to the fulfilment partner through its API after the cut-off, with confirmations and tracking updates
✓ Online cancellation on the account page, with a confirmation email, as Vera's adviser recommended

THE CALENDAR NOW
Double charges: stopped entirely. Failed payments: a large share recovered within two months by the dunning flow. Support emails about unwanted deliveries: down sharply.

"Every bug in a subscription happens again every two weeks. Fixing them once fixed them for every future cycle." - Vera Hofman

https://launchstudio.eu/en/blog/production-launch-for-subscription-ecommerce

#Subscriptions #Ecommerce #Mollie #Bolt #AIFounder #LaunchStudio #Manifera
