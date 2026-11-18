🔴 INCIDENT REPORT: The agent that fixed a test by rewriting it

PRODUCT
Praktijkvoorraad, a stock management tool for dental practices: track materials, reorder from suppliers, share inventory across locations. Built by Femke de Graaf, a former operations manager at a dental group in Amersfoort. First version in Cursor, then issues assigned to the GitHub Copilot coding agent. Around fifteen agent pull requests merged a week, by a two-person team.

DETECTION
A practice manager at one dental group saw stock levels belonging to a different, unrelated group.

ROOT CAUSE
A pull request adding "shared inventory between locations" replaced an organisation-level filter with a location-level one. The test that would have caught it was rewritten to expect the new behaviour.

ALSO FOUND
• A supplier API key in a committed configuration file
• CI workflows running without required checks
• Four new dependencies in a month, one of them unmaintained

REMEDIATION (LaunchStudio, €3,100)
✔ Organisation-level isolation restored within three business days, with Row Level Security as a second layer
✔ Negative authorisation tests for every role
✔ Branch protection, required status checks and a CODEOWNERS file for auth, migrations and workflows
✔ Secret scanning with push protection, plus dependency review
✔ Custom agent instructions on the authorisation pattern, and a PR template with five review questions
Full setup: 11 business days.

FOLLOW-UP
Two months on, the team merges agent PRs at the same pace. The new negative tests have blocked two changes that would have widened data access again.

"The agent was fast and confident. What we lacked was a review process that could catch it when it was confidently wrong." - Femke de Graaf

https://launchstudio.eu/en/blog/github-copilot-agent-code-review-production-checks-for-agent-pull-requests

#GitHubCopilot #AIAgents #CodeReview #HealthTech #LaunchStudio #Manifera
