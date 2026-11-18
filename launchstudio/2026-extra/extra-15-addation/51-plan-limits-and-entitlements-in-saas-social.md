What the pricing page promised vs. what the database did 💳

Arjen Dijkstra built Enquetewerk with Lovable, Supabase and Stripe: a survey tool for schools and associations. Revenue grew more slowly than usage, and some free accounts had dozens of surveys.

PRICING PAGE: Free plan, up to three surveys.
DATABASE: Accepted unlimited inserts. The "New survey" button was only hidden after three, and duplicating a survey skipped the check entirely.

PRICING PAGE: Free plan, up to 100 responses.
DATABASE: Nothing enforced it.

PRICING PAGE: Exports, branding and AI summaries on paid plans.
DATABASE: The buttons were hidden for free users, but the edge functions never checked the plan. AI summaries ran for anyone who called them.

PRICING PAGE: Pay, and you're upgraded.
DATABASE: The plan was a text field set by the checkout success page. Close the browser after paying, and you stayed on Free. Cancel, and you might keep Pro forever.

Making the database keep the promises (LaunchStudio, 11 business days, €4,300):
✓ A model of plans, entitlements, subscriptions and usage counters, synced by verified, idempotent Stripe webhooks
✓ Survey creation and duplication in a database function that enforces limits atomically
✓ Response limits enforced by an insert check
✓ Every edge function for exports, branding and AI summaries checks entitlements first
✓ A seven-day grace period for past-due subscriptions
✓ Downgrades keep existing surveys readable, but block new ones over the limit
✓ Upgrade prompts at the exact moment a user tries a paid feature
✓ Entitlement tests on every deployment

Two months later: free-to-paid conversions roughly doubled, AI costs from free accounts close to zero, and no paying customer locked out by a closed browser.

"My pricing page said one thing and my database did another. Making the product keep the pricing page's promises was the best growth project I did that year." - Arjen Dijkstra

https://launchstudio.eu/en/blog/plan-limits-and-entitlements-in-saas

#SaaSPricing #Stripe #Entitlements #EdTech #AIFounder #LaunchStudio #Manifera
