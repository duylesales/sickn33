🕐 Did you know? Three facts about time that a driving school learned the hard way

DID YOU KNOW #1: The Netherlands changes its clocks in March.
Kees Bakkenes runs a driving school in Emmen with six instructors and built Rijlesrooster in Bolt: students book lessons, instructors manage availability, everyone gets SMS reminders. All winter, reminders worked. After the March clock change, every reminder arrived an hour late, and some students missed lessons. Bolt's scheduled function compared local times stored as text with UTC server time.

DID YOU KNOW #2: A slow reply is not the same as no reply.
The function ran every minute. When the SMS provider responded slowly, it sent the reminder again. Some students got the same message three times.

DID YOU KNOW #3: A job that fails quietly can stay failed for days.
After an SMS provider outage, the function stopped working. Nobody noticed for two days.

What LaunchStudio built (5 business days, €1,400):
✓ A reminders table with UTC timestamps and Europe/Amsterdam scheduling logic
✓ Scheduling moved to Supabase Cron, every five minutes
✓ Idempotent sending, with a status per reminder
✓ Retries for temporary failures
✓ Alerts for stalled jobs

ONE MORE THING YOU MIGHT NOT KNOW
Through the October clock change and the whole following year, reminders arrived on time, with no duplicates. And according to Kees's instructor reports, missed lessons fell noticeably.

"The reminders worked perfectly for five months. Then the clocks changed and so did my students' attendance." - Kees Bakkenes

https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app

#Supabase #Bolt #pgcron #SaaS #LaunchStudio #Manifera
