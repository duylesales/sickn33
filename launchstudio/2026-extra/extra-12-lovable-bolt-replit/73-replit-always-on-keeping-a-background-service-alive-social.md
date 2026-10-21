🚨 Annemarie Poortvliet's Innametool reminds around 4,000 patients across six pharmacies when a repeat prescription is due. The reminder logic ran in a loop inside her Replit web app. On busy days it worked. On quiet nights the app went to sleep — and reminders due between 2 and 7 a.m. were never sent. Not then, not later. 😳

She only found out when a pharmacy compared its own prescription records with the reminders sent and saw a consistent gap. Here's how to keep background work alive on Replit: 🧠

❌ A scheduler loop inside an autoscale web app — it stops whenever the app sleeps
❌ A job that only asked "what's due right now?", so missed windows were lost forever
❌ In-memory counters silently resetting and skewing her sending statistics
❌ About to buy a reserved instance to paper over the problem

✅ Reminders moved to a scheduled deployment running every 15 minutes
✅ The job rewritten to process everything due since the last successful run — missed windows recover automatically
✅ The queue in the database, idempotent on patient and prescription, so re-runs never duplicate
✅ Run records, an alert if the job hasn't succeeded within an hour, and external uptime monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we take Replit products to production — often lowering the bill by replacing always-on instances with scheduled work. ⚙️

Her result: €2,200, two business days. Within a fortnight a platform incident stopped the job for three hours — the next run caught up on everything and no patient missed a reminder. Costs went slightly down, not up. 🚀

👉 Replit Always-On: keeping a background service alive: https://launchstudio.eu/en/blog/replit-always-on-keeping-a-background-service-alive

#Replit #BackgroundJobs #DevOps #HealthTech #LaunchStudio #Manifera
