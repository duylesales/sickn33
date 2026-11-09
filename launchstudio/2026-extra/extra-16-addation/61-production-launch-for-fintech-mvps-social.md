🐷 Mehmet Yildiz runs a Rotterdam start-up that built Spaarpot with Cursor and Supabase: families and friend groups save together for trips and events. Money flows through a licensed payment institution, so Spaarpot never holds funds. But a pilot with 40 groups showed small differences between app balances and the partner's statements. A cent here, a cent there. 🪙

Before live access, the partner sent a technical questionnaire. The assessment found: 🧠

❌ Balances stored as decimals and updated directly, with rounding in the browser
❌ Retried webhooks sometimes crediting a contribution twice
❌ The partner's API key used in a client-side function
❌ Group members able to see other groups' contributions, and no audit log

✅ Amounts in integer cents with explicit currency, and an append-only ledger with derived balances
✅ Verified, idempotent webhooks keyed by the partner's event IDs, plus a daily reconciliation with alerts
✅ The key moved server-side and rotated, and groups separated with Row Level Security and tests
✅ MFA, step-up confirmation for payouts, an audit log and documentation for due diligence

At **LaunchStudio**, backed by Manifera's 11+ years of building software with payment and financial integrations for organisations such as Vodafone and TNO, we build financial MVPs that reconcile to the cent. 🛠️

His result: €5,800, fifteen business days. Live access three weeks after the documentation, and balances matching the partner's statements to the cent since launch. 🚀

👉 Production launch for fintech MVPs: https://launchstudio.eu/en/blog/production-launch-for-fintech-mvps

#Fintech #PSD2 #DORA #Supabase #AIFounder #LaunchStudio #Manifera
