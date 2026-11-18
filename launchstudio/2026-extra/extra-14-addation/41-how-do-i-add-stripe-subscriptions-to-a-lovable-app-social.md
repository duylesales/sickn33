🎟️ Imagine a members-only party where the bouncer checks... whether you're standing near the door.

That's roughly how Dagritme decided who was "pro."

Femke Brouwers, a lifestyle coach in Zeist, built Dagritme in Lovable: habit tracking with coaching programmes on a monthly plan. Lovable connected Stripe Checkout and marked users as pro when they reached the success page.

Two months in, the guest list didn't add up:
Stripe's list: 58 active subscriptions
The app's list: 91 pro users

Who were the other 33?
• Members who had cancelled in Stripe and kept access
• People who opened checkout, refreshed an old tab to reach the success URL, and never paid
• And failed renewals nobody ever noticed
Plus one open door: the profiles.is_pro column was writable by users themselves.

The new door policy (LaunchStudio, 8 business days, €2,700, plus €49/month managed hosting):
✓ A subscriptions table updated only by a verified Stripe webhook
✓ Failed renewals handled with a seven-day grace period and email
✓ Plan checks for premium content moved into RLS
✓ The Stripe Customer Portal connected
✓ Existing users reconciled against Stripe

From the next billing cycle, app access matched Stripe exactly. And recovering failed renewals added roughly 9% to monthly revenue.

"I thought Stripe was working because money came in. I just didn't know how much more was leaking out." - Femke Brouwers

https://launchstudio.eu/en/blog/how-do-i-add-stripe-subscriptions-to-a-lovable-app

#Stripe #Lovable #SaaS #Subscriptions #LaunchStudio #Manifera
