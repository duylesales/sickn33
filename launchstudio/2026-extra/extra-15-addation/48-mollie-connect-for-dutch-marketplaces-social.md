🚨 Kees Verbruggen built Clubkas with Bolt and Supabase: amateur sports clubs in Noord-Brabant manage memberships, collect contributions and sell event tickets. All payments went through Kees's own Mollie account, and he transferred each club's money monthly. 😳

With 34 clubs, it became untenable. Transfers took a full day and occasionally went to the wrong club. His accountant raised concerns about holding others' funds. Here's how Mollie Connect works for Dutch marketplaces: 🧠

❌ All clubs' money in one founder account
❌ Manual monthly transfers, sometimes to the wrong club
❌ iDEAL redirects treated as proof of payment
❌ The Mollie API key in a frontend environment file

✅ Mollie Connect via OAuth, with encrypted tokens and visible onboarding status
✅ Payments on each club's account with an application fee for Clubkas
✅ SEPA direct debit with mandates from a first iDEAL payment
✅ Webhooks verified with the right club's credentials, platform refunds, key rotation and daily reconciliation

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we let Mollie hold the money, so you can focus on the platform. 🛠️

His result: €6,200, 15 business days. Clubs receive their money directly, payment status errors stopped, and around 4,200 contributions were collected via SEPA in the first season. 🚀

👉 Running a Dutch marketplace? Here's how Mollie Connect works: https://launchstudio.eu/en/blog/mollie-connect-for-dutch-marketplaces

#Mollie #MollieConnect #SEPA #SportsTech #AIFounder #LaunchStudio #Manifera
