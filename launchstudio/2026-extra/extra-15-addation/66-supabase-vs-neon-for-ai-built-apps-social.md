Q&A: "Should I move my whole app to Supabase for better security?" 🗄️

Q: Who's asking?
A: Kevin Mulder. He built Projectboekhouding with v0, Next.js and Neon: project cost tracking for architecture and engineering firms, recording hours, expenses and budgets per project and client. Drizzle in server actions, a separate auth provider, files in an S3-compatible bucket. A friend suggested moving everything to Supabase "for better security."

Q: Was Neon the wrong choice?
A: No. It suited the app well: server-side data access, preview branches for each pull request, and low costs in quiet periods.

Q: So where was the security problem?
A: In the code. Eleven server actions loaded records by ID without checking the firm, so one firm's user could read another firm's project budgets. The Neon connection string had been committed early on. Uploaded files were public. And serverless functions connected directly, not through Neon's pooled connection string, causing errors at month-end.

Q: Would moving to Supabase have fixed that?
A: Not by itself. The same code would have had the same problems on any database.

Q: What did LaunchStudio change instead?
A: In 9 business days, for €3,600, while keeping Neon:
• All data access moved into a scoped module that requires a firm context from the authenticated session
• Negative authorisation tests for every server action
• The connection string rotated, and secrets moved to the hosting platform
• Functions on the pooled connection endpoint
• Files in a private bucket with signed URLs
• Neon branching tied to preview deployments, so migrations run against realistic data first
• Database and object storage confirmed in EU regions, and documented for customers

Q: And the outcome?
A: Three weeks later, Projectboekhouding passed a security review by a large engineering firm. No migration, no rebuild, and the team kept the workflow it liked.

"I nearly migrated my whole app because I thought the database was the security problem. The problem was how my code used it." - Kevin Mulder

https://launchstudio.eu/en/blog/supabase-vs-neon-for-ai-built-apps

#Supabase #Neon #Postgres #NextJS #AIFounder #LaunchStudio #Manifera
