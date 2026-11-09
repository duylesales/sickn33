🍽️ Floor Bakker runs a hospitality recruitment SaaS from Utrecht, built over eight months with Cursor and later Claude Code on Next.js, Supabase and Stripe. About 300 businesses and 4,000 workers used it. But bugs were increasing, and Floor had become afraid to touch certain files. 😰

The review showed how eight months of sessions had drifted: 🧠

❌ Three ways to log in: Supabase Auth, a custom session system and an old magic-link route
❌ API routes checking login but not whether a shift belonged to the user's business
❌ Two Stripe keys in a committed script, and 140 dependencies with about 30 unused
❌ No tests, and deployments from Floor's laptop

✅ Authentication consolidated on Supabase Auth, the old route removed and ownership checks on every API route
✅ Keys rotated, moved to environment variables and repository history cleaned
✅ Unused dependencies removed, and tests for login, cross-business access, applications and Stripe webhooks
✅ A GitHub pipeline to Vercel with migrations, plus project rules for both Cursor and Claude Code

At **LaunchStudio**, backed by Manifera's 11+ years of maintaining large codebases for clients such as Vodafone and TNO, we consolidate AI-generated code instead of rewriting it. 🛠️

Her result: €3,400, nine business days. Fewer bug reports, builds about a third faster and tests that blocked two access-breaking changes. 🚀

👉 The cost to make a Cursor or Claude Code app production ready: https://launchstudio.eu/en/blog/cost-to-make-a-cursor-or-claude-code-app-production-ready

#Cursor #ClaudeCode #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
