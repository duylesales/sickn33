🚨 Joost Vermeulen spent fifteen years in freight forwarding in Venlo. Over two months of evenings, Claude Code built him Vrachtbod: shippers post loads, small transport companies submit price quotes. Six shippers and twenty carriers joined the pilot. Then a carrier mentioned, helpfully, that he could see competing bids by changing a number in the URL. 😳

Joost asked Claude Code to fix it. The agent added a check to the bid detail page, but the API endpoint behind it, and two others, still returned any bid to any logged-in user. Here's what taking an agent-built app to production really involves: 🧠

❌ Endpoints returning any bid to any logged-in user
❌ A Mollie API key in a committed seed script
❌ Tests that mocked the database entirely
❌ Production deploys run from Joost's laptop

✅ Ownership checks on all eleven endpoints with business data, plus Row Level Security
✅ The leaked key rotated and the git history cleaned
✅ Negative authorisation tests for every role
✅ An automated pipeline with staging, and a CLAUDE.md with security conventions

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we tell you which of your agent's decisions you can trust, and fix the ones you can't. 🛠️

His result: €3,200, 9 business days. Vrachtbod relaunched and handled around 2,300 quotes the next quarter with no access incidents - and the new tests twice blocked a deploy that would have reopened bid visibility. 🚀

👉 Built your app with Claude Code? Here's how to get it production-ready: https://launchstudio.eu/en/blog/claude-code-app-to-production-launch-service-for-agent-built-apps

#ClaudeCode #AIAgents #Logistics #AIFounder #LaunchStudio #Manifera
