🚨 Mila Pauwels built Urenregistratie Pro with Cursor, Next.js and Supabase: time tracking and payroll exports for small staffing agencies. Every Friday afternoon, as agencies exported hours for payroll, the app started failing with connection errors. 😳

Mila planned a bigger database. The real problem: the code kept opening new connections every time someone knocked. Here's how Supabase connection pooling and limits work: 🧠

❌ Serverless functions on the direct connection string, scaling up on Fridays
❌ A new database client created inside every server action
❌ An export worker opening a pool per job and never closing it
❌ Long transactions around external API calls, and a BI tool on production

✅ The app on Supavisor transaction mode with Drizzle configured for it, one client per instance
✅ One small session-mode pool for the worker, with connections released
✅ External API calls moved outside transactions, plus statement timeouts
✅ A read-only BI role and connection alerts at 75% of the limit

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we fix the cause before you pay for a bigger server. 🛠️

Her result: €2,600, 7 business days. The next Friday, peak connections stayed below 40% while agencies exported around 2,600 timesheets - and the planned compute upgrade wasn't needed. 🚀

👉 Seeing connection errors in Supabase? Here's how pooling and limits work: https://launchstudio.eu/en/blog/supabase-connection-pooling-and-limits-explained

#Supabase #Postgres #Serverless #Performance #AIFounder #LaunchStudio #Manifera
