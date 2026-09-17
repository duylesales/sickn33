🚨 Stefan built Bezorgroute for catering companies. One morning, his Mapbox bill hit €1,800: an automated bot scraped his routing API key straight out of his public frontend JavaScript bundle. 😳

AI generators love convenience, which is why they put API keys in frontend code. Here's how secrets get stolen: 🧠

❌ Hardcoding paid third-party API keys (OpenAI, Google Maps, Resend) into React components
❌ Prefixing private keys with `VITE_` or `NEXT_PUBLIC_`, mistakenly believing they are hidden
❌ Committing `.env` files with live production secrets into version-controlled repositories
❌ No usage quotas, rate limits, or domain restrictions configured in provider dashboards

✅ Route all third-party API calls through server-side Edge Functions that hold secrets securely
✅ Restrict API keys with strict HTTP referrers, IP whitelists, and hard billing budget alerts
✅ Use modern secret management tooling and automate secret rotation upon exposure
✅ Implement build linter checks that fail immediately if private keys appear in frontend bundles

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we extract secrets from client code and build secure server proxies that protect your wallet. 🛡️

His result: Stefan's mapping costs returned to baseline and stayed predictable for fourteen months across dozens of catering clients. 🚀

👉 Learn where API keys and secrets actually belong in an AI-built application: https://launchstudio.eu/en/blog/where-secrets-belong-in-an-ai-built-app

#Lovable #Cybersecurity #APIKeys #CloudCosts #LaunchStudio #Manifera
