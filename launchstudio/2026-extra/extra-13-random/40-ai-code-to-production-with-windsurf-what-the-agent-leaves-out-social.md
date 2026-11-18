🧾 INVOICE (illustrative, but real owners got ones like it)

To: a real horse owner in Drenthe
For: monthly livery
Horse: Test Horse 3

How? The agent's seed script, which created test horses and owners, had been run against production. Twice. 🐴

Arjen Wolters, a software developer and horse owner in Assen, built Stallenlog with Windsurf over one long weekend: livery stables manage boarding horses, feeding schedules, farrier and vet appointments, and monthly invoices to owners. It spread fast among stables in Drenthe: 26 stables and about 700 horse owners within two months.

The agent built the app faster than Arjen could have. And nothing told it what not to do. A LaunchStudio review found the pattern:
• One Supabase project for everything, so the seed script hit production
• The Postmark API key in a committed config file
• API routes that checked for a session, but not stable or owner membership, so owners could see other stables' horses and vet notes
• A schema that had drifted away from the migration files after direct changes
• 214 direct dependencies, four with known vulnerabilities
• No error tracking

What LaunchStudio added, so something now tells the agent "no" (9 business days, €2,500):
✓ Separate development, staging and production projects, each with its own keys
✓ The Postmark key rotated and moved
✓ Row Level Security scoped to stables and owners, with negative tests
✓ The schema reconciled into a clean migration baseline
✓ 61 unused or duplicate dependencies removed, and vulnerable ones updated
✓ Silent catches replaced with reported errors, plus Sentry and uptime checks
✓ CI that blocks merges on tests, secret scanning and dependency alerts
✓ A Windsurf rules file documenting the environments and the access model

Stallenlog is still built almost entirely with Windsurf, now through pull requests guarded by CI. It grew to 58 stables in six months, with no more test-data leaks or cross-stable exposure.

"The agent built the app faster than I could have. It also ran my seed script on production, because nothing told it not to. Now something does." - Arjen Wolters

https://launchstudio.eu/en/blog/ai-code-to-production-with-windsurf-what-the-agent-leaves-out

#Windsurf #AgenticCoding #Supabase #DevOps #LaunchStudio #Manifera
