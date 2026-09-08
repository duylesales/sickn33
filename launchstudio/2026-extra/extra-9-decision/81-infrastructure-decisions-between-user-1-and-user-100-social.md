🚨 A Dutch newsletter sent Tijs's invoicing tool 1,200 signups in a day. The app didn't crash — it just went unusably slow for 20 minutes, confirmation emails arriving an hour late. 😳

Two shortcuts, invisible at 340 users, became the entire bottleneck under a burst: 🧱

❌ Welcome and invoice emails sent synchronously, inside the request cycle
❌ The invoices table had no index on the foreign key filtered every dashboard load
❌ Neither issue was visible at normal traffic — both were quietly compounding
❌ "It works" and "it scales" look identical from the outside, until they don't

✅ Sort decisions into cheap-to-defer and expensive-to-defer before you ship
✅ Schema and indexing punish procrastination hardest — fix it before real rows pile up
✅ Background jobs are invisible at 10 users, catastrophic at 200 concurrent signups
✅ File storage and session handling are safe to leave until one specific trigger

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we tell founders which shortcuts are safe to leave and which are quietly compounding toward a 2 AM incident. 🔍

His result: a Redis-backed job queue and one added index fixed both issues in a four-day engagement — the next similarly-sized traffic spike caused no slowdown at all. 🚀

👉 Get a free scope review of your prototype: https://launchstudio.eu/en/blog/infrastructure-decisions-between-user-1-and-user-100

#SaaS #ScaleUp #ProductionReady #StartupGrowth #LaunchStudio #Manifera
