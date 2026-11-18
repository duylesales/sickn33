🌙 A quiet night, inside the app (illustrative log; the behaviour is real)

01:45 Loop checks: anything due now? Yes. Reminder sent.
02:10 No traffic. The app goes to sleep. The loop stops with it.
04:00 A repeat prescription reminder falls due. Nobody is awake to send it.
06:30 Another one.
07:15 A visitor arrives, the app wakes, and the loop restarts.
07:15 Loop checks: anything due now? No.

The 04:00 and 06:30 reminders are never sent, not even late, because the loop only asked what was due at that exact moment.

Annemarie Poortvliet built Innametool on Replit: intake and medication checking for small pharmacy chains, sending patients a reminder when a repeat prescription is due, around 4,000 patients across six pharmacies. Reminders due roughly between two and seven in the morning were never sent. She found out when a pharmacy compared its own repeat prescription records against the reminders and saw a consistent gap. 💊

A night shift that doesn't fall asleep (LaunchStudio, 2 business days, €2,200):
✓ Reminders moved out of the web app into a scheduled deployment running every fifteen minutes
✓ The job now asks what's been due since the last successful run, so a missed window recovers itself
✓ The queue moved into the database, with idempotency on patient and prescription so a re-run can't send a duplicate
✓ In-memory counters replaced with database values (they'd been resetting invisibly, which made her sending statistics wrong)
✓ The web app left on autoscale, since nothing depends on it running nonstop, so she didn't need the reserved instance she'd been about to buy
✓ A run record for every execution, and an alert if the job hasn't completed within an hour
✓ An external uptime check against a page that queries the database

The gap closed. Within the first fortnight, a platform incident stopped the job for three hours. The next run processed everything that had built up, and nobody missed a reminder. Costs went down slightly, not up.

"Reminders due at four in the morning were never sent, and they were never sent later either, because the job only ever asked what was due at that exact moment." - Annemarie Poortvliet

https://launchstudio.eu/en/blog/replit-always-on-keeping-a-background-service-alive

#Replit #BackgroundJobs #DevOps #HealthTech #LaunchStudio #Manifera
