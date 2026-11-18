🏋️ Imagine a gym where the front desk lets you in if you hand over a note saying "I've paid." No membership card. No check against the till. Just a note.

That's how Sportschoolbeheer activated memberships.

Lieke Ottenhof built it in Lovable: membership and access management for independent gyms and fitness studios, 54 locations, around 8,000 members. Subscriptions were activated by a webhook from her payment provider. The handler read the JSON, found the customer and plan, and updated the membership. It never checked the signature. The AI session that wrote it hadn't been asked to, and the provider's dashboard showed every delivery succeeding.

Then the webhook URL sat in a public repository for four days, in a config file a contractor committed and removed. Eleven weeks later, someone started posting crafted notes to it. Over a month: 23 memberships activated across nine locations, each worth €240 to €580 a year. Several were resold.

A gym owner noticed a member with active access and an empty payment history.

The front desk now checks every note (LaunchStudio, 2 business days, €2,500):
✓ Signature verification on the raw request body, with a timing-safe comparison, and failures rejected, recorded and alerted
✓ Messages older than five minutes rejected
✓ An events table of every processed event ID, so replays and retries are harmless
✓ The handler reduced to verify, record and acknowledge, with activation in a background job
✓ Every claimed payment looked up at the provider before any membership is granted
✓ Uninformative error responses
✓ The 23 fraudulent memberships found by matching activations against real payments, deactivated, and the gyms notified
✓ A monthly reconciliation of active memberships against actual payments

Roughly €9,000 of annual membership value recovered. The reconciliation has since caught two genuine discrepancies, caused by failed deliveries, not fraud. Lieke calls the signature check four lines of code guarding her whole revenue model.

"The provider's dashboard said every delivery succeeded, so I believed the integration was fine. It was fine. It just also accepted messages from everybody else." - Lieke Ottenhof

https://launchstudio.eu/en/blog/ai-app-security-webhooks-you-never-verified

#Webhooks #AppSecurity #Payments #Lovable #LaunchStudio #Manifera
