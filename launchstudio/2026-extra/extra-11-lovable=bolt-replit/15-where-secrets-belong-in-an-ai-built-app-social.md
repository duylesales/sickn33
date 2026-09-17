🚨 Stefan Rombouts built Bezorgroute in Cursor: a delivery route optimizer for small catering firms around Tilburg. The app called a commercial mapping API for routing. Because the API key was stored in a prefixed environment variable, it was compiled directly into the client-side JavaScript bundle — where scrapers found it and racked up €1,800 in unmetered billing. 😳

If an API key is in your frontend code, it is public to the entire world. Here's how secrets get leaked: 🧠

❌ Prefixing private API secrets with `VITE_` or `NEXT_PUBLIC_`, embedding them in browser bundles
❌ Allowing frontends to make third-party API requests directly without a backend proxy
❌ Committing unencrypted `.env` files with production database credentials to GitHub
❌ Missing billing quotas and anomaly spending alerts in third-party API dashboards

✅ Move all external API calls behind authenticated server-side proxy Edge Functions
✅ Store secrets exclusively in server environment configurations or dedicated secret vaults
✅ Enforce secret rotation policies and automated CI scanners (e.g. GitGuardian)
✅ Set hard spending caps and anomaly webhook alerts across all third-party provider dashboards

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we lock down API secret boundaries to protect your credentials and your bank account. 🔑

His result: Stefan Rombouts completed the credential audit and proxy rebuild in 4 business days for €1,650 (key rotation, server-side proxy with rate limiting, pipeline checks). Mapping expenses returned to normal and have scaled predictably with subscribers for 14 months, with zero further exposures. 🚀

👉 Audit your API secret architecture before unexpected bills arrive: https://launchstudio.eu/en/blog/where-secrets-belong-in-an-ai-built-app

#Cybersecurity #APISecrets #Cursor #WebDevelopment #LaunchStudio #Manifera
