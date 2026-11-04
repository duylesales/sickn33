🚨 Kees Bakkenes runs a driving school in Emmen with six instructors and built Rijlesrooster in Bolt, with SMS lesson reminders for every student. All winter, the reminders worked perfectly. Then the clocks changed in March - and every reminder started arriving an hour late. Some students missed their lessons. 😳

The reminders worked for five months. Then the clocks changed, and so did his students' attendance. Here's what was hiding in the generated code: 🧠

❌ Local times stored as text, compared with UTC server time
❌ A function running every minute that resent reminders when the SMS provider was slow - some students got the same message three times
❌ No record of what had already been sent
❌ No alert when the function failed after a provider outage - nobody noticed for two days

✅ A reminders outbox table with UTC timestamps and Europe/Amsterdam scheduling logic
✅ Scheduling moved to Supabase Cron, every five minutes
✅ Idempotent sending with status tracking, so each reminder goes out exactly once
✅ Retries for temporary failures and alerts for stalled jobs

At **LaunchStudio**, backed by Manifera's 11+ years of scheduling systems for enterprise and logistics clients, we treat scheduled jobs as monitored infrastructure, not a timer that hopes for the best. 🛠️

💡 His result: €1,400, five business days. Through the October clock change and the year after, reminders arrived on time with no duplicates, and missed lessons fell noticeably. 🚀

👉 Building reminders into a Supabase app? Here are the six building blocks that make them reliable: https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app

#Supabase #Bolt #pgcron #SaaS #LaunchStudio #Manifera
