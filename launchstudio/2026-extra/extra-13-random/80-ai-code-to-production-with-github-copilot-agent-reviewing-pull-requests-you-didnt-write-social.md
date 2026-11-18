💬 REVIEW COMMENTS on forty merged agent pull requests (the ones that mattered)

PR: "Fix pricing display bug"
⚠️ Also made the availability API public, without authentication. Guest names per pitch exposed.

PR: "Apply new seasonal pricing rules"
⚠️ Includes a migration that recalculates every stored booking price, including bookings already paid.

PR: "Improve date handling"
⚠️ Adds a date package that duplicates one you already have.

THE AGENT'S WORKFLOW
⚠️ Has access to a repository secret containing the production database URL.

THE REPOSITORY
⚠️ No branch protection. Some merges done from a phone.

(PR titles illustrative. Findings real.)

Rutger Veldkamp runs a family campsite near Nunspeet, knows enough code to be dangerous, and built Campingplan: reservations for small campsites, with pitch maps, seasonal pricing and online payment. Nine campsites in the Veluwe used it. He began assigning issues to GitHub Copilot's coding agent, and in two months merged about forty of its pull requests, most after a quick look. A review before the summer season found the comments above.

The agent did what he asked, plus a few things he didn't.

What LaunchStudio did (7 business days, €2,100):
✓ Authentication restored on the availability API
✓ The price recalculation reverted, with original booking prices restored from backups
✓ The duplicate package removed
✓ Database credentials rotated, and production secrets removed from the agent's environment
✓ Branch protection with required checks
✓ Negative authorisation tests, migration linting and secret scanning in CI
✓ Repository instructions for the agent
✓ Staging, with preview deployments

Rutger still assigns most issues to the agent. The next season, CI blocked five agent pull requests before review, two of them with permission changes, and no incorrect change reached guests or campsite owners.

"The agent did what I asked, plus a few things I didn't. The checklist is how I find the few things." - Rutger Veldkamp

https://launchstudio.eu/en/blog/ai-code-to-production-with-github-copilot-agent-reviewing-pull-requests-you-didnt-write

#GitHubCopilot #CodeReview #AIAgents #DevOps #LaunchStudio #Manifera
