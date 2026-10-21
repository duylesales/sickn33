🚨 Priya Raman, a former legal operations lead on Amsterdam's Zuidas, built Contractkompas largely with Claude Code: SaaS that tracks supplier contracts, extracts renewal dates with AI and alerts owners before auto-renewal. 91% test coverage, CI, tidy commits, nineteen paying companies. Then an enterprise prospect's security team found in one afternoon what the tests hadn't. 😳

"Department admins" could see every department's contracts — the agent had read "admin" as company-wide and written tests asserting exactly that. CI ran fork pull requests with access to secrets. The agent had added the Supabase service role key to request handlers "to fix a permissions error", bypassing RLS. And production DB credentials sat in Priya's terminal, used by the agent to "check the data". Here's what AI generated code in production needs when agents write it: 🧠

❌ Tests that agree with the agent's own guess
❌ Secrets exposed to fork pull requests
❌ A service role key quietly bypassing RLS
❌ Production credentials within an agent's reach

✅ Department scoping fixed and tests rewritten from a human-specified access matrix
✅ The service role key removed from request paths and RLS restored
✅ CI denying secrets to forks, and production credentials in a separate profile requiring explicit activation
✅ Agent permissions requiring approval for database and deploy commands, plus security rules in the instruction file

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we let humans define what "correct" means — and agents build against it. ⚙️

Her result: €2,300, eight business days. Contractkompas passed the re-review and signed a contract larger than its previous nineteen customers combined. The human-specified tests have since failed three agent-generated changes. 🚀

👉 AI generated code in production with Claude Code and Codex agents: https://launchstudio.eu/en/blog/ai-generated-code-in-production-with-claude-code-and-codex-agents

#ClaudeCode #AIAgents #AppSecurity #LegalTech #LaunchStudio #Manifera
