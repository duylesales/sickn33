🚨 Ilona Peters built Circuo, an IoT monitoring dashboard for small manufacturing floors, with Lovable — polished enough that two Brainport-region manufacturers asked to pilot it. Then onboarding revealed the database had no row-level security at all: any logged-in user could pull another company's sensor data just by changing an ID in the URL. 😳

It worked flawlessly in the demo because there had only ever been one account. 🧠

❌ Row-level security was never configured — a default Supabase gap invisible until a second real tenant showed up
❌ API keys were sitting exposed in client-side code
❌ The auth flow let sessions leak across companies once more than one account existed
❌ None of it showed up anywhere in the demo

✅ Audit the schema and implement proper row-level security scoped to each company's account
✅ Rebuild the auth flow so sessions can't cross tenants
✅ Move exposed API keys out of the frontend and into a secured backend layer

At **LaunchStudio**, we treat this exact gap — the invisible layer under a polished AI-built frontend — as a checklist item, backed by Manifera's 11+ years of production engineering for clients like Vodafone and TNO. 🛡️

Circuo's result: it went live with both pilot manufacturers within the month, and Ilona signed a third client after passing their security questionnaire outright. 🚀

👉 Built an IoT or SaaS dashboard with an AI tool? Get a fixed-scope review before your next pilot: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #RowLevelSecurity #Eindhoven
