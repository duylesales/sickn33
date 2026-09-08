🚨 "Is it ready?" "It works. I've used it daily for three weeks." "That's not what I asked." Ruben had passed five of seven gates before that forced the other two. 😳

A Cursor codebase is real code you shaped yourself — why generic "AI code has holes" advice is useless here: 🧠

❌ Twenty-three routes, written across forty sessions, in three authorization idioms
❌ Three routes checked a user's organisation but never their role — anyone could delete a booking
❌ A CSV export added late for a demo took an orgId and checked nothing
❌ The Prisma diff against production came back with eleven undocumented statements

✅ Name the single layer deciding "may this user touch this record" — everything routes through it
✅ Inventory every route and where its authorization decision happens; the list is the finding
✅ An empty schema diff between repo and production is the pass condition
✅ Rotate any secret that ever touched git history, private repo or not

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we run the seven-gate review built for exactly this failure pattern. 🚦

His result: authorization consolidated into one layer across all twenty-three routes, six days, plus a findings document for his customers' IT contacts. 🚀

👉 Book a 15-minute call and bring your worst gate: https://launchstudio.eu/en/blog/your-cursor-codebase-works-production-readiness-review

#IndieHacker #AICoding #LaunchStudio #Manifera #ProductionReady #SaaS
