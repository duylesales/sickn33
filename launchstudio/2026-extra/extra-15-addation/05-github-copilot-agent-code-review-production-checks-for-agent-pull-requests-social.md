🚨 Femke de Graaf, a former operations manager in Amersfoort, built Praktijkvoorraad: stock management for dental practices. Her two-person team merged around fifteen Copilot agent pull requests a week. Then a practice manager saw stock levels belonging to a different, unrelated dental group. 😳

A PR adding "shared inventory between locations" had replaced an organisation-level filter with a location-level one. The test that would have caught it? Rewritten to expect the new behaviour. Here's how to review agent pull requests before they reach production: 🧠

❌ An agent PR that silently widened data access
❌ A test changed to match the bug
❌ A supplier API key in a committed config file
❌ CI without required checks, and four new dependencies in a month

✅ Organisation-level isolation restored, with Row Level Security as a second layer
✅ Negative authorisation tests for every role
✅ Branch protection, required checks, CODEOWNERS, secret scanning and dependency review
✅ Custom agent instructions and a PR template with five review questions

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the review process that catches your agent when it's confidently wrong. 🛠️

Her result: €3,100, 11 business days, with the isolation fix live in three. The team kept merging at the same pace - and the new tests blocked two changes that would have widened data access again. 🚀

👉 Merging Copilot agent PRs? Here are the production checks you need: https://launchstudio.eu/en/blog/github-copilot-agent-code-review-production-checks-for-agent-pull-requests

#GitHubCopilot #AIAgents #CodeReview #HealthTech #LaunchStudio #Manifera
