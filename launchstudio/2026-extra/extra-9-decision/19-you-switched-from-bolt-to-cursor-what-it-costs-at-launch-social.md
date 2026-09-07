🚨 Sem spent two weeks chasing an email deliverability bug in Rittenboek. His accountant-facing export was never being generated in the first place. 😳

Switching Bolt to Cursor mid-build is the right call — and it leaves seven kinds of debris neither tool cleans up: 🧠

❌ A stale Netlify deployment still built from an old branch, still connected to production
❌ Two RLS policies referenced a column a later refactor had already re-scoped
❌ The export job used an unawaited async call, so one in fifteen never ran
❌ Environment variables existed in four places, agreeing on nothing

✅ Document the origin of an imported codebase — tool, date, framework — as a paper trail
✅ Audit every hosting provider for sites still connected to your repo, delete unused ones
✅ Read every RLS policy against the current schema rather than trust it exists
✅ A short rules file stops the model from entrenching two competing conventions

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we clear a tool-switch's debris without touching the interface underneath. 🧹

His result: the stale deployment removed, policies rewritten, the export job moved onto a real queue — five days, no interface changes, 240 paying users. 🚀

👉 See how mixed-tool codebases went live, then send yours over: [Link to article]

#IndieHacker #AICoding #LaunchStudio #Manifera #ProductionReady #StartupGrowth
