🚨 Elke Brandt built ClauseCheck, an AI contract review tool for law firms, in Berlin with v0 — and left it on a Vercel preview URL for two months. A pilot lawyer opened developer tools, found an API key sitting in plain text in the page source, and emailed her: "is this supposed to be here." 😳

A working public URL is not the same thing as being deployed. 🧠

❌ The API key was embedded directly into the frontend JavaScript bundle instead of kept server-side
❌ The preview environment ran against a development database that could be wiped without warning
❌ Debug settings and verbose error messages were still switched on, quietly leaking backend details
❌ No custom domain or SSL, no rollback plan, no uptime monitoring

✅ Move exposed keys server-side where they belong
✅ Provision a proper custom domain with SSL and separate development from production databases
✅ Switch off debug logging and add basic uptime monitoring before real users find the gaps for you

At **LaunchStudio**, deployment hardening is one of the most contained pieces of production work we do — infrastructure and configuration only, backed by Manifera's 11+ years of engineering experience out of Amsterdam. 🛡️

Elke's result: ClauseCheck now runs on a hardened, properly deployed setup, with her pilot firms never noticing anything had changed except that it was finally safe. 🚀

👉 Think your "live" app is actually deployed? Check the six things that matter: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AppDeployment #SecretsManagement
