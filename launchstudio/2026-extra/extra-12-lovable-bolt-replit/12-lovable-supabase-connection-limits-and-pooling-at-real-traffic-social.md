🚨 Thijs Kranenburg's Zaalplanner books 48 community centres and village halls across Friesland and Groningen. Every Monday morning — exactly when managers plan the week — the product broke completely for ten to twenty minutes. Two venues had already asked about alternatives. 😳

Nine or ten concurrent users were enough to exhaust a 60-connection database. Here's why "too many clients already" hits AI-built apps: 🧠

❌ A new database client created inside every serverless function call
❌ Application code on the direct connection instead of the pooler
❌ Transactions held open around an email call — 90 seconds per provider hiccup
❌ A realtime subscription re-created on every render

✅ The database client moved to module scope, so each instance reuses one connection
✅ All application traffic on the pooled port; the direct connection kept for migrations
✅ An explicit pool size, short transactions, and no external calls inside them
✅ An alert at 70% of the limit and a load test at 120 concurrent users

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix the connection bug before you pay for a bigger database. 🔌

His result: one business day and €1,450 later, Monday mornings stopped failing. Peak connections fell from the 60 ceiling to a steady 7, and the app handled 120 concurrent users on the plan he'd been about to upgrade for €300/month. 🚀

👉 Connection limits and pooling at real traffic: https://launchstudio.eu/en/blog/lovable-supabase-connection-limits-and-pooling-at-real-traffic

#Supabase #PostgreSQL #Serverless #Lovable #LaunchStudio #Manifera
