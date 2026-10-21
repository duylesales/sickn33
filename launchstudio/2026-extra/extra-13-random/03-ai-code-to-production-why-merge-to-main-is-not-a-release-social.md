🚨 Daan Visser built PlankPal with Cursor: membership and QR check-in for two bouldering gyms in Delft. Every push to main deployed automatically. One Thursday evening he asked Cursor to add a "frozen membership" status. The generated migration rewrote every existing row — and set unknown statuses to null. 😳

For two hours, members with valid passes were refused at the door. Rolling back the code didn't help: the data had already changed. Here's why "merge to main" isn't a release process: 🧠

❌ Every push deployed straight to production in forty seconds
❌ A migration that silently rewrote existing data
❌ No staging database, no tests on the check-in flow
❌ No rollback plan for data, only for code

✅ Affected rows restored from a point-in-time backup
✅ GitHub Actions running type checks and check-in tests on every branch
✅ A separate staging Supabase project with seeded data, and migrations in their own reviewed PRs
✅ A written rollback step in every PR template, plus error tracking on Daan's phone

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build release processes around the way you already work with AI tools. ⚙️

His result: €1,600, six business days. 212 releases in four months — CI blocked nine, including two migrations that would have rewritten data — and not a single check-in outage since. 🚀

👉 AI code to production: why merge to main is not a release: https://launchstudio.eu/en/blog/ai-code-to-production-why-merge-to-main-is-not-a-release

#Cursor #DevOps #CI #Supabase #LaunchStudio #Manifera
