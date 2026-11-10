🚨 Bart Scholten built Inkoopscan with Claude Code and Supabase: it reads supplier invoices from email and matches them with purchase orders. Over months of agent sessions, it gathered 214 dependencies. Before launch, a customer's IT department asked for a review. Three packages stood out. 😳

One, named as if it parsed Dutch invoices, was weeks old, had one anonymous maintainer, no source repo - and an install script making a network request. Here's what slopsquatting and hallucinated packages mean for AI-generated code: 🧠

❌ A suspicious new package with a networked install script
❌ An abandoned package with known vulnerabilities
❌ No committed lockfile, so builds resolved fresh versions every time
❌ The production service role key available in CI where the agent ran

✅ Suspicious and abandoned packages removed, plus 37 unused dependencies
✅ A committed lockfile and reproducible builds
✅ All CI secrets rotated and logs checked - no unusual access found
✅ Protected dependency files, supply chain scanning, limited CI credentials and approved libraries for Claude Code

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we check who wrote the packages your agent quietly installs. 🛠️

His result: €2,800, 7 business days. Inkoopscan passed the IT review with a dependency policy and SBOM, and the scanner later flagged two more unfamiliar agent suggestions, rejected before installation. 🚀

👉 Is your AI agent installing packages you've never heard of? Here's what to check: https://launchstudio.eu/en/blog/hallucinated-packages-slopsquatting-in-ai-generated-code

#SupplyChainSecurity #ClaudeCode #AppSecurity #AIAgents #LaunchStudio #Manifera
