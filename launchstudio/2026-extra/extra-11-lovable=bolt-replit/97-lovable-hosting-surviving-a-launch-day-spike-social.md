🚨 Thijs Damen's Startbewijs handles race entries for eleven event organisers around Doetinchem and Arnhem. Entries usually trickle in over weeks. Then a popular regional half marathon opened capped entries at 20:00 on a Tuesday, with roughly 4,000 people waiting. The product lasted eleven minutes. 😳

It stayed down for fifty minutes, and the organiser had to reschedule. Here's what breaks under a launch-day spike: 🧠

❌ A new database connection per request - the limit hit at around 90 concurrent users
❌ "Places remaining" counted by scanning an unindexed table on every refresh
❌ The email provider's rate limit hit in four minutes, so people who had entered re-entered
❌ A landing page rendered by the app instead of served as a static file

✅ Connection pooling, measured at over 2,000 concurrent
✅ A trigger-maintained counter and indexes on the entry-flow columns
✅ Static landing pages, a queued email flow within the provider's limits, and a uniqueness constraint against duplicates
✅ Spending caps, a feature flag for the live counter, a status page and a load test at 5,000 concurrent users

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we load-test your launch before your customers do. 🏁

His result: seven business days and €4,400 later, the rescheduled opening took 4,100 entries in nine minutes with no downtime and a 1.2-second peak response time. The 31 duplicate entries were refunded - and the organiser has since brought three more events. 🚀

👉 Surviving a launch-day spike: https://launchstudio.eu/en/blog/lovable-hosting-surviving-a-launch-day-spike

#Scalability #Lovable #LoadTesting #Events #LaunchStudio #Manifera
