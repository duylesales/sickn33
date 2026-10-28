🚨 Casper IJsselstein's Afspraakherinnering sends evening-before reminders for 38 dental and orthodontic practices - about 1,900 appointments a week. In March a deploy changed a dependency and the nightly job started failing on its first line. The product looked completely healthy. 😳

Eleven days later a practice in Bergen op Zoom called: their no-show rate had roughly doubled. Around 3,000 reminders never sent, and 200+ missed appointments. Here's why scheduled work fails silently: 🧠

❌ One nightly cron run doing all the work for every practice
❌ A cron endpoint anyone could call if they knew the path
❌ A single UTC schedule - an hour late since the clocks changed
❌ Failures logged where nobody looked, and no alert when the job simply didn't run

✅ The cron task now enqueues one job per practice - a failure hits one practice, not all
✅ The endpoint protected with a shared secret, plus an advisory lock against overlap
✅ Hourly runs that check each recipient's time zone and practice opening hours
✅ A run record per job, an alert if no successful run in 26 hours, and an external heartbeat

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make the silence audible when scheduled work stops. 🔔

His result: two business days and €2,100 later, failures are detected in hours, not weeks. The absence alert fired three times in the next year - and no practice has spotted a gap before Casper did. 🚀

👉 Cron and work that runs off the request: https://launchstudio.eu/en/blog/lovable-hosting-cron-and-work-that-runs-off-the-request

#Cron #Monitoring #Reliability #Lovable #LaunchStudio #Manifera
