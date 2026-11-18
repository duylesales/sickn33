📒 OCTOBER, preparing figures for the accountant

Provider dashboard: 180 active subscriptions
Bank statements: consistently fewer payments
Difference: 11 practices, with failed cards or lapsed SEPA mandates, the oldest since March

Fleur Alkemade runs Praktijkvoorraad, built in Lovable: stock and ordering software for independent physiotherapy and podiatry practices, €39 a month, 180 subscribers across the eastern Netherlands. Her integration handled the happy path well. A subscription created a row and set is_active to true. That was the entire model. The webhook endpoint ignored every event except the one confirming a first charge.

So eleven practices had been using the product for free for up to seven months. None of them knew. Two thought the charges were just on a different statement. And Fleur wasn't chasing anyone, because she didn't know there was anyone to chase.

What LaunchStudio built (5 business days, €2,900):
✓ A subscription model with active, past due, paused and cancelled states, in her own database, checked by one access function
✓ Failure, recovery and mandate-revoked webhooks, handled idempotently
✓ The provider's retry schedule set to four attempts over 21 days
✓ A fourteen-day grace period with working access
✓ A payment-update page reachable from a signed email link, no login needed
✓ A three-message recovery sequence, from a domain with SPF, DKIM and DMARC
✓ Direct debit access based on settlement, not initiation
✓ An internal past-due list Fleur checks on Mondays

📒 AFTERWARDS
Lapsed practices reinstated within two weeks of being told: 9 of 11
Recovered annual revenue: €4,212
Failed charges recovered automatically over the next six months: 71%
Reconciliation time: from an afternoon to a glance

"I was not chasing anyone, because I did not know there was anyone to chase. Nine of the eleven paid the day I emailed them - they just thought it was going out." - Fleur Alkemade

https://launchstudio.eu/en/blog/lovable-payments-subscriptions-that-survive-failed-cards

#SaaS #Subscriptions #Churn #Lovable #LaunchStudio #Manifera
