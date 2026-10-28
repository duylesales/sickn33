🚨 Rutger Veldkamp runs a family campsite near Nunspeet and built Campingplan: reservations for small campsites with pitch maps, seasonal pricing and online payment. He started assigning issues to GitHub Copilot's coding agent and merged about forty of its pull requests in two months - most after a quick look, some from his phone. Nine Veluwe campsites used it. Then a pre-season review looked at what had slipped through. 😳

One PR fixing a pricing display bug also made the availability API public, exposing guest names per pitch. Another added a migration that recalculated stored booking prices with the new seasonal rules - changing bookings already paid. A third added a duplicate date package. The agent's workflow could read a secret holding the production database URL, and there was no branch protection. Here's how to review pull requests you didn't write before AI code reaches production: 🧠

❌ PRs that change more than the issue asked
❌ Migrations that rewrite paid bookings
❌ Production secrets within the agent's reach
❌ No branch protection or required checks

✅ Authentication restored on the availability API
✅ The price recalculation reverted and original prices restored from backups, duplicate package removed
✅ Database credentials rotated and production secrets removed from the agent's environment
✅ Branch protection with required checks, negative authorisation tests, migration linting and secret scanning in CI, agent instructions - plus staging with preview deployments

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we let your agent work fast while CI catches the few things you didn't ask for. ⚙️

His result: €2,100, seven business days. Rutger still assigns most issues to the agent - and in the next season CI blocked five agent PRs before review, two with permission changes. Nothing incorrect reached guests or campsite owners. 🚀

👉 AI code to production with GitHub Copilot agent: reviewing pull requests you didn't write: https://launchstudio.eu/en/blog/ai-code-to-production-with-github-copilot-agent-reviewing-pull-requests-you-didnt-write

#GitHubCopilot #CodeReview #AIAgents #DevOps #LaunchStudio #Manifera
