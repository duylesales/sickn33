🚨 Ahmed Benali built Factuurportaal with v0, Next.js and Supabase: freelancers send invoices, clients view and pay them online. He'd carefully written Row Level Security policies. Then, while adding reporting with Cursor, the agent installed Prisma. 😳

A client changed the invoice number in a URL and saw another freelancer's invoice. Prisma connected with the postgres role - bypassing every policy Ahmed had written. Here's what to know about Prisma or Drizzle in an AI-written Next.js app: 🧠

❌ An ORM connection silently bypassing RLS
❌ 14 of 23 server actions loading records by ID without ownership checks
❌ Schema changes made both in the dashboard and through Prisma migrations
❌ Direct connections failing under month-end invoice peaks

✅ One clear pattern: Prisma server-side with scoped helpers, Supabase client for RLS-protected reads
✅ All 23 server actions rewritten to require organisation scope, with negative tests
✅ A single migration history with RLS kept as a second layer
✅ Prisma through the Supabase pooler, and project instructions for Cursor

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure the code doing most of the work actually respects your security rules. 🛠️

His result: €3,500, 9 business days, with the exposure closed within a day. Month-end connection errors disappeared, and the new tests caught two later AI changes that would have reintroduced unscoped queries. 🚀

👉 Using Prisma or Drizzle with Supabase? Here's what to watch out for: https://launchstudio.eu/en/blog/prisma-or-drizzle-in-an-ai-written-nextjs-app

#Prisma #Drizzle #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
