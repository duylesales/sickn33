💶 PAYSLIP (for the cheapest employee a salon SaaS ever had)

Employee: managed hosting
Monthly cost: €49
Shift: every night, every weekend
Duties: monitoring, SSL certificates, backups, updates
Overtime: an eleven-minute provider incident on a Tuesday, handled before most salons opened

Linda Peters, a hairdresser and salon owner in Hengelo, built Salonagenda in Lovable: online booking and client cards for hair and beauty salons, with SMS reminders and deposits. It grew to 64 salons across Twente and the Achterhoek, around 18,000 bookings a month.

And Linda was, by default, also its entire operations team.

THE PREVIOUS "EMPLOYEE": Linda herself, unpaid
• Hosting on a DigitalOcean droplet, set up with a friend who'd since moved on
• Two overnight outages in one quarter: once an SSL certificate that failed to renew, once a disk full of logs
• Found out both times from salon owners at 07:30
• Backups that had never been restored
• A booking calendar that slowed badly on Saturday mornings, when half the salons were busy at once

ONBOARDING THE NEW EMPLOYEE (LaunchStudio, Launch & Grow, 10 business days, €2,700)
✓ Managed serverless hosting, with pooled Postgres
✓ Indexes for the calendar queries
✓ Cached salon availability pages
✓ SMS reminders moved to a background queue
✓ Log rotation and retention
✓ Uptime monitoring, and backups with a documented restore test
Then managed hosting took over monitoring, certificates, backups and updates, at €49 a month.

PERFORMANCE REVIEW, after twelve months
Overnight outages: none. Saturday calendar load times: from around five seconds to under one. Salons: 110. And Linda is back to cutting hair four days a week.

"I was paying nothing for hosting and everything in sleep. Forty-nine euros a month turned out to be the cheapest employee I've ever had." - Linda Peters

https://launchstudio.eu/en/blog/ai-application-scalability-on-a-49-euro-budget-what-managed-hosting-covers

#ManagedHosting #Scalability #SaaS #Lovable #LaunchStudio #Manifera
