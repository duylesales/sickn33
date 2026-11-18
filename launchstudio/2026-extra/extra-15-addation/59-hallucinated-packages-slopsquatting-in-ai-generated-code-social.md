🚨 THE LINEUP: three packages in an AI-built codebase

Bart Scholten built Inkoopscan with Claude Code and Supabase: it reads supplier invoices from email, extracts lines and prices, and matches them with purchase orders for small wholesalers. Months of agent sessions left 214 direct and indirect dependencies. Before launch, a customer's IT department asked for a review, and LaunchStudio examined every package added in the last quarter.

Most were well known. Three stepped forward.

SUSPECT #1: "the Dutch invoice parser"
A name that sounded exactly right. Published only weeks before it was added. One anonymous maintainer. No source repository. An install script that made a network request.

SUSPECT #2: the abandoned one
Last updated years ago, with known vulnerabilities.

SUSPECT #3: the duplicate
Did what an established library already in the project did.

ACCOMPLICES
• No committed lockfile, so every production build resolved versions fresh
• The production Supabase service role key available in the CI environment where the agent ran

THE VERDICT (LaunchStudio, 7 business days, €2,800)
✓ Suspicious and abandoned packages removed, and the parsing helper rewritten on the established library
✓ 37 unused dependencies removed
✓ Lockfile committed, reproducible builds
✓ Because suspect #1's install script had run in CI, every secret there rotated, and logs checked for unusual access: none found
✓ Dependency files made a protected path that needs human review
✓ Supply chain scanning on pull requests, separate limited credentials for CI
✓ Approved libraries for common tasks listed in Claude Code's project instructions

SINCE THEN
Inkoopscan passed the IT review with a documented dependency policy and a software bill of materials. The scanner has flagged two more unfamiliar packages suggested by the agent, both rejected before installation.

"I trusted every line the agent wrote because the app worked. I never thought about who had written the packages it was quietly installing." - Bart Scholten

https://launchstudio.eu/en/blog/hallucinated-packages-slopsquatting-in-ai-generated-code

#SupplyChainSecurity #ClaudeCode #AppSecurity #AIAgents #LaunchStudio #Manifera
