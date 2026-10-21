🚨 Thijs Groen, a sommelier in Nijmegen, built WijnWijzer: a wine subscription shop with a v0 storefront and a Supabase backend. Eager to earn, he spent his first two weeks on Stripe subscriptions — and 70 customers signed up in a soft launch. Then the order problem showed. 😳

Subscriptions were tied to a customer ID created in the browser, so returning customers on new devices got duplicate accounts and duplicate charges. Age verification — legally required for alcohol — was a frontend checkbox, Stripe secret keys sat in client code, and the database ran in the US. Here's the order of operations that avoids doing it all twice: 🧠

❌ Payments built first, on top of a weak user model
❌ Age verification enforced only in the interface
❌ Stripe secret keys in a client-side config file
❌ A US-region database

✅ Accounts consolidated, Stripe keys rotated and moved server-side
✅ A proper server-side user model with age confirmation stored and enforced
✅ Database migrated to an EU region with a tested restore
✅ Stripe rebuilt around verified webhooks — 11 duplicate records merged and 4 double charges refunded — then staging, hosting and monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we follow the same sequence every time: ownership, secrets, access, data, money, delivery, visibility. ⚙️

His result: €3,200, twelve business days. WijnWijzer grew to 410 active subscribers in five months with zero duplicate accounts or double charges, and passed the payment provider's alcohol-sales review. 🚀

👉 Make an AI-generated app production ready: the order of operations: https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-the-order-of-operations

#Stripe #Supabase #AIApp #Startups #LaunchStudio #Manifera
