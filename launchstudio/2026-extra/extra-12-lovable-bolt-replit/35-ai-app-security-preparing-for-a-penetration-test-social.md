🚨 Arnoud Steenbergen's Contractbeheer manages contracts for 22 facility management companies, including three regional hospital groups. A hospital's procurement asked for a penetration test report, so he commissioned one immediately: €7,500 from the first firm that answered. 😳

31 findings, 4 critical: a service role key in the frontend, a public bucket of signed contracts, 17 endpoints without authorisation, RLS off on six tables. He'd paid a specialist to find what a one-day self-review would have — and couldn't share the report. Here's how to prepare for a pentest: 🧠

❌ Commissioning a test before fixing the obvious issues
❌ Picking the first firm that answers, without seeing a sample report
❌ Testing without documentation, accounts or a staging environment
❌ No retest included, so findings stay "open" in the report

✅ Three days of self-review across ten categories: keys, buckets, cross-account access, RLS, webhooks, sessions, uploads, enumeration, dependencies, rate limits
✅ A staging environment with anonymised production data, plus documentation and four accounts at different permission levels
✅ A second firm chosen from a redacted sample report, two-thirds manual work, with retesting included
✅ Critical and high findings fixed and retested, then a one-page summary for procurement

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we run the self-review first — so your pentest budget finds what you couldn't. 🔍

His result: the second test (€6,200) found 0 critical and 2 high — a skippable contract approval step and a rate-limit gap that no checklist would catch. Both were fixed in four days, the summary went to the hospital, and the contract was signed. 🚀

👉 Preparing for a penetration test: https://launchstudio.eu/en/blog/ai-app-security-preparing-for-a-penetration-test

#Pentest #AppSecurity #Procurement #Lovable #LaunchStudio #Manifera
