🚨 Ricardo Fernandes built Rijlesplanner with Lovable and Supabase: driving schools publish availability, students book lessons and get reminders. On the Monday after summer time started, dozens of students turned up an hour late - or found instructors waiting an hour early. 😳

Everyone using the app was in the Netherlands. But the Netherlands has two time zones a year. Here are the timezone and date bugs AI-built apps get wrong: 🧠

❌ Weekly availability stored as fixed UTC times
❌ timestamp without time zone, read as local in the browser and UTC in reminders
❌ A fixed-UTC cron sending reminders at 06:00 or 07:00 instead of 08:00
❌ toISOString() dating invoices on the wrong month, and reports on UTC days

✅ Lesson times migrated to timestamptz, with each school's time zone stored
✅ Recurring availability as local rules in Europe/Amsterdam
✅ Reminders computed as UTC instants at booking, sent by a five-minute job
✅ Local invoice dates and month boundaries, explicit time zones in emails, and DST tests

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure your schedule survives the clock change. 🛠️

His result: €2,900, 8 business days. October and the following March passed without a single displaced lesson, and time-related tickets dropped from a few dozen a month to almost zero. 🚀

👉 Does your app handle time zones correctly? Here are the bugs to check: https://launchstudio.eu/en/blog/timezone-and-date-bugs-in-ai-built-apps

#Timezones #Scheduling #Supabase #EdTech #AIFounder #LaunchStudio #Manifera
