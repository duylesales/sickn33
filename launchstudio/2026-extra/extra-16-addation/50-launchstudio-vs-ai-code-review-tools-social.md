🎨 Kim Hoogendoorn runs a client portal for interior designers from Amsterdam, built with Claude Code and Supabase: designers share mood boards, quotes and invoices with clients. Kim had an AI pull request reviewer, Dependabot and secret scanning, and checked the Supabase advisor monthly. Every pull request got thoughtful comments. No critical warnings. She felt confident. ✅

Then a larger studio asked for a security review before onboarding 40 clients. Role-based testing found what no tool had flagged: 🧠

❌ An invoices policy, created months ago in the dashboard, letting any logged-in user read all rows
❌ Quote PDFs in a public bucket
❌ Password reset redirects accepting any URL
❌ Backups that had never been restored

✅ Policies rewritten per designer and client
✅ Access tests running in the pipeline on every change
✅ Files in private storage, restricted redirects and a tested restore
✅ Her existing tools kept in place, now backed by tests that encode the access rules

At **LaunchStudio**, backed by Manifera's 11+ years of combining automated tooling with human review for clients such as Vodafone and TNO, we close the gaps tools can't see and leave tests that protect your rules. 🛠️

Her result: €2,000, five business days. The studio onboarded its 40 clients, and two months later an AI-generated change that would have broadened the policy failed the access test. 🚀

👉 LaunchStudio vs AI code review tools: https://launchstudio.eu/en/blog/launchstudio-vs-ai-code-review-tools

#CodeReview #Security #ClaudeCode #Supabase #AIFounder #LaunchStudio #Manifera
