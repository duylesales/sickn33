🔍 CASE FILE: The Policies That Were Never Consulted

THE CLIENT
Ahmed Benali, Den Haag. Built Factuurportaal with v0, Next.js and Supabase: freelancers and small agencies send invoices to clients, who view and pay them online.

THE ALIBI
Ahmed had done his homework. After reading about Supabase security, he carefully wrote Row Level Security policies.

THE INCIDENT
A client changed the invoice number in a URL, by accident, and saw another freelancer's invoice meant for a different client.

THE INVESTIGATION
While adding reporting features, Cursor had installed Prisma and moved most data access into server actions. Prisma connected with the postgres role from the default connection string. That role bypasses every RLS policy. The policies were there. Nobody was asking them.

FURTHER EVIDENCE
• 14 of 23 Prisma server actions and routes loaded or updated records by ID with no ownership check
• Some screens used the Supabase client in the browser as well
• Schema changes made both in the dashboard and through Prisma migrations
• Direct connections from serverless functions, failing at month-end invoice peaks

THE RESOLUTION (LaunchStudio, €3,500)
• Exposure closed within a day
• Every data access path documented, and one clear pattern chosen: Prisma server-side with authorisation in scoped helper functions, the browser client only for RLS-protected reads
• All 23 server actions rewritten to require the user's organisation scope, each with negative authorisation tests
• One migration history, with RLS kept in SQL as a second layer
• Prisma through the Supabase pooler, and project instructions telling Cursor which pattern to follow
Full cleanup: 9 business days.

CASE CLOSED
Month-end connection errors disappeared. The new tests have since caught two AI-generated changes that would have brought unscoped queries back.

"I had written all the right policies. I just didn't know that the code doing most of the work wasn't using them." - Ahmed Benali

https://launchstudio.eu/en/blog/prisma-or-drizzle-in-an-ai-written-nextjs-app

#Prisma #Drizzle #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
