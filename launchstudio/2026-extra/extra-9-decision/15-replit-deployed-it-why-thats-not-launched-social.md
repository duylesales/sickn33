🚨 Timo asked the Replit Agent to clean up leftover test rosters. It did — against the only database it had ever known, which held eleven venues' schedules too. 😳

Ninety seconds from Deploy to a real URL feels like launching. It's the only production-grade thing about that setup: 🧠

❌ Workspace and deployment shared a database — 340 shifts vanished with nothing to restore
❌ NODE_ENV was unset, so production quietly served development stack traces
❌ No rate limit existed anywhere on password reset
❌ A shift endpoint never checked which venue owned it — costs leaked across venues

✅ Verify workspace and deployment use genuinely different DATABASE_URL values, don't assume
✅ Deployment-scoped secrets exist in Replit's Secrets pane to prevent exactly this
✅ An untested backup is a belief, not a capability — restore one and time it
✅ Three end-to-end tests beat eighty generated unit tests that never check the wrong user

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we separate the environment first, since everything else is downstream of that. 🗄️

His result: separate dev and production databases, ownership checks across all seventeen endpoints, daily backups with a tested restore — seven days. 🚀

👉 Tell us what you've built and what's worrying you — a real answer within one business day: https://launchstudio.eu/en/blog/replit-deployed-it-why-thats-not-launched

#IndieHacker #AICoding #LaunchStudio #Manifera #ProductionReady #StartupGrowth
