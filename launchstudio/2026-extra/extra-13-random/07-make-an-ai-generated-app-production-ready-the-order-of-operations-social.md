🍷 RECIPE: production readiness, where the order of the steps matters

Thijs Groen, a sommelier in Nijmegen, built WijnWijzer: a wine subscription webshop with a v0 storefront and a Supabase backend assembled with AI prompts. Customers take a taste quiz, get a monthly box of three bottles, and can skip or pause. Eager to start earning, Thijs spent his first two weeks on Stripe subscriptions. 70 customers signed up in a soft launch.

He started with the dessert.

WHAT WENT WRONG BY COOKING IN THE WRONG ORDER
• Subscriptions linked to a customer ID created in the browser, so returning customers on a new device sometimes got a second account, and a second subscription
• Age verification, legally required for alcohol sales in the Netherlands, only as a frontend checkbox
• Stripe secret keys in a client-side configuration file
• The database in a US region

THE RECIPE, IN ORDER (LaunchStudio, Launch & Grow, 12 business days, €3,200, plus €49/month)
1. Consolidate the accounts
2. Rotate the Stripe keys and move them server-side
3. Build a proper server-side user model, with age confirmation stored and enforced
4. Migrate the database to an EU region, with a tested restore
5. Only now: rebuild the Stripe integration on verified webhooks and the corrected user IDs, merging eleven duplicate customer records and refunding four double charges
6. Finally: staging, hosting on Thijs's own domain, and monitoring

SERVES
410 active subscribers over the next five months. Duplicate accounts and double charges: none. And WijnWijzer passed a payment provider review for alcohol sales that had previously been flagged.

"I did the money part first because it felt most important. It turned out to be the part that depended on everything else." - Thijs Groen

https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-the-order-of-operations

#Stripe #Supabase #AIApp #Startups #LaunchStudio #Manifera
