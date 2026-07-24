🔓 Vincent Voskuil built "MeldStroom," an incident-reporting tool, using Cursor — and on deployment day, pushed the same config straight to production. The AI provider's API key, meant for server-only use, ended up bundled directly into the public frontend JavaScript. A curious early user found it sitting in plain view in a script file.

Nothing looked wrong at deploy time — the app worked, the feature worked. That's exactly the problem. ⏰

❌ Development mixed client-side and server-side config in one place, with no explicit split before deploy
❌ The API key lived in a file that got pulled into the client-side build, same as in local dev
❌ Nobody inspected the compiled frontend bundle for the literal key string before calling it done
❌ The key sat exposed for as long as the deployment had been public

✅ Route every AI provider call through a server-side endpoint, never directly from the browser
✅ Keep separate environment files for dev and production — never one `.env` serving both
✅ Rotate any key that touched a public build, and search the bundle for exposed strings before shipping

At **LaunchStudio**, Manifera's Singapore-based engineers bring 11+ years of production engineering experience to exactly this class of gap, reviewing deployments before launch, not after. 🛡️

His result: MeldStroom's API calls now happen entirely server-side, with the key never present in any browser-shipped code, plus rate-limit monitoring to catch future misuse. 🚀

👉 About to push your first production deploy? Talk to an engineer first: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AIDeployment #APISecurity
