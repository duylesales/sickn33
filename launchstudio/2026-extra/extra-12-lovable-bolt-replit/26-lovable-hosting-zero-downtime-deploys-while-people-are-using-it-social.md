🚨 Ferdi Aalbersberg's Routeplanning plans delivery routes for 24 regional bakeries and food distributors, whose drivers use the app from five in the morning. At 06:40 on a Wednesday he deployed a "trivial" change: renaming a column from adres to address. 😳

Every driver on the road was running the old version, which asked for a column that no longer existed. About 60 drivers across nine companies got errors - and the rollback failed too, because the old code needed the dropped column. Here's why correct code still breaks on deploy: 🧠

❌ Renaming a column and updating the app in a single deployment
❌ No awareness that browser tabs keep running yesterday's JavaScript
❌ A rollback that couldn't work after a destructive schema change
❌ Deploying during the customers' busiest window

✅ Expand-and-contract over three deployments: add, write both and backfill in batches of 2,000, switch reads, drop later
✅ A rule: no deployment may remove or rename a column the running version still uses
✅ Additive API changes only, with removed endpoints kept as no-ops for 30 days
✅ A "new version available" prompt drivers accept at their next stop, a four-line checklist with timed rollback, and no deploys between 05:00 and 09:00

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure your next migration is reversible before you ship it. 🔄

His result: one business day and €1,600 later - twelve months without a deployment incident, including two more schema changes of similar size. The version prompt revealed drivers had been running three-day-old builds without knowing. 🚀

👉 Zero-downtime deploys while people are using it: https://launchstudio.eu/en/blog/lovable-hosting-zero-downtime-deploys-while-people-are-using-it

#DevOps #Deployment #DatabaseMigrations #Lovable #LaunchStudio #Manifera
