🚨 Arjen Wolters, a developer and horse owner in Assen, built Stallenlog with Windsurf over one long weekend: livery stables manage horses, feeding, farrier and vet appointments and monthly invoices. Within two months, 26 stables and about 700 owners used it. Then real owners received invoices for horses named "Test Horse 3". 😳

The agent's seed script had run against production - twice - because there was one Supabase project for everything. The Postmark key was in a committed config file. Routes checked for a session but not stable membership, so owners saw other stables' horses and vet notes. The schema had drifted from migrations, there were 214 direct dependencies (four vulnerable), and no error tracking. Here's what the agent leaves out when Windsurf code goes to production: 🧠

❌ One environment for dev, test and real customers
❌ A secret committed to the repository
❌ "Logged in" treated as "authorised"
❌ Schema drift, dependency sprawl and silent errors

✅ Separate dev, staging and production projects with separate keys - Postmark key rotated
✅ Row level security scoped to stables and owners, with negative tests
✅ A clean migration baseline and 61 unused or duplicate dependencies removed
✅ Sentry, uptime checks, and CI that blocks merges on tests, secret scanning and dependency alerts - plus a Windsurf rules file

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we add the guardrails an agent doesn't know it needs. ⚙️

His result: €2,500, nine business days. Arjen still builds almost entirely with Windsurf, now through CI-guarded pull requests - and Stallenlog grew to 58 stables with no further test-data leaks. 🚀

👉 AI code to production with Windsurf: what the agent leaves out: https://launchstudio.eu/en/blog/ai-code-to-production-with-windsurf-what-the-agent-leaves-out

#Windsurf #AgenticCoding #Supabase #DevOps #LaunchStudio #Manifera
