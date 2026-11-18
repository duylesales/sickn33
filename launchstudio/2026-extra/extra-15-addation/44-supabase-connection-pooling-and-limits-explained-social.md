MYTH: "Connection errors every Friday? I need a bigger database."
FACT: Mila Pauwels had already planned the compute upgrade. She never needed it. 🔌

Mila built Urenregistratie Pro with Cursor, Next.js and Supabase: time tracking and payroll exports for small staffing agencies. The app ran on Vercel with Drizzle in server actions, plus a Node.js worker on a separate server for weekly payroll exports. Every Friday afternoon, as agencies exported hours, the app started failing.

MYTH: "Serverless means I don't have to think about connections."
FACT: Drizzle used the direct connection string, so every function instance opened its own connections. On Friday afternoons, Vercel scaled up many instances.

MYTH: "One client per action is clean code."
FACT: A new Drizzle client was created inside each server action, multiplying connections further.

MYTH: "The worker cleans up after itself."
FACT: It opened a new pool for every export job and never closed it.

MYTH: "Long transactions are safer."
FACT: Some exports wrapped everything, including calls to an external payroll API, in one long transaction.

And a BI tool was connected straight to the production database.

What LaunchStudio changed (7 business days, €2,600):
✓ The Supavisor transaction mode connection string, with Drizzle configured for it
✓ One database client per instance
✓ One small session-mode pool for the worker, with connections released properly
✓ External API calls moved outside database transactions
✓ A separate direct connection for migrations, and statement timeouts
✓ A read-only role with limited concurrency for the BI tool
✓ Alerts at 75% of the connection limit

The next Friday: around 2,600 timesheets exported, peak connections below 40% of the limit, zero errors.

"I thought I needed a bigger database. I needed my code to stop opening a new door every time someone knocked." - Mila Pauwels

https://launchstudio.eu/en/blog/supabase-connection-pooling-and-limits-explained

#Supabase #Postgres #Serverless #Performance #AIFounder #LaunchStudio #Manifera
