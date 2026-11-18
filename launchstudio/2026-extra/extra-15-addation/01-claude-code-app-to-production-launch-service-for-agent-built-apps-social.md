💬 A founder, an agent and a bug (dramatized, but the facts are real)

JOOST: A carrier says he can see competing bids by changing a number in the URL. Fix it.
AGENT: Done. I've added a check to the bid detail page.
JOOST: Great.

What nobody checked: the API endpoint behind that page, and two others, still returned any bid to any logged-in user.

Joost Vermeulen spent fifteen years in freight forwarding in Venlo. He'd never written production code, but he was comfortable in a terminal, and over two months of evenings Claude Code built him Vrachtbod: a Next.js platform where shippers post loads and small transport companies submit price quotes. Six shippers and twenty carriers joined the pilot.

When LaunchStudio reviewed the project, the list grew:
• Bids exposed through three endpoints, not one
• A Mollie API key in a committed seed script
• Tests that mocked the database entirely
• Production deploys run by hand from Joost's laptop

The real fix (9 business days, €3,200):
✅ Ownership checks on all eleven endpoints that return business data, plus Postgres Row Level Security as a second layer
✅ The leaked key rotated and the git history cleaned
✅ Negative authorisation tests for every role
✅ An automated pipeline with staging, and a CLAUDE.md with security conventions for future agent sessions

Next quarter: around 2,300 quotes, no access incidents. Twice, the new tests blocked a deploy that would have reopened bid visibility. Joost still ships features with Claude Code.

"Claude Code built more than I could have imagined. What I needed was someone to tell me which of its decisions I could trust." - Joost Vermeulen

Built your app with Claude Code? https://launchstudio.eu/en/blog/claude-code-app-to-production-launch-service-for-agent-built-apps

#ClaudeCode #AIAgents #Logistics #AIFounder #LaunchStudio #Manifera
