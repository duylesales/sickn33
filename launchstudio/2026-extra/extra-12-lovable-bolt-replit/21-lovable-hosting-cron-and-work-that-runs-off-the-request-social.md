🌙 THE NIGHTLY REMINDER JOB, March

Night 1: ❌ failed on its first line. Logged where nobody was watching.
Night 2: ❌
Night 3: ❌
...
Night 11: ❌

The product, every one of those days: ✅ looked completely healthy.

Casper IJsselstein built Afspraakherinnering with Lovable: appointment reminders for dental and orthodontic practices, sent the evening before by email and SMS. 38 practices, roughly 1,900 appointments a week. A deploy changed a dependency, and the nightly cron job started failing. Nothing broke on any screen. The missing thing was something nobody sees.

Day 11: a practice manager in Bergen op Zoom called. Were reminders switched off? Their no-show rate had roughly doubled. Across 38 practices: around 3,000 reminders never sent, and by the practices' own estimates, more than 200 missed appointments. 🦷

What LaunchStudio changed (2 business days, €2,100):
✓ The reminder task now queues one job per practice, so a failure hits one practice, not all, and a timeout can't cut the run in half
✓ The cron endpoint protected with a shared secret (anyone who knew the path could call it before)
✓ Hourly scheduling, with recipient time zone and practice opening hours checked inside the job, replacing a single UTC run that had been an hour late since the clocks changed
✓ An advisory lock against overlapping runs
✓ A run record written by every job
✓ An absence alert if the reminder run hasn't completed within 26 hours
✓ External heartbeat monitoring, so the alert works even when the platform doesn't
✓ All six scheduled jobs documented, which revealed two that had done nothing useful for months

A failure like that is now caught in hours, not weeks. In the following year, the absence alert fired three times: twice for real failures caught the same morning, once for a platform incident. No practice has spotted a gap before Casper did.

"It failed every night for eleven days and my product looked completely healthy the whole time. Nothing was broken on any screen. The thing that was missing was something nobody sees." - Casper IJsselstein

https://launchstudio.eu/en/blog/lovable-hosting-cron-and-work-that-runs-off-the-request

#Cron #Monitoring #Reliability #Lovable #LaunchStudio #Manifera
