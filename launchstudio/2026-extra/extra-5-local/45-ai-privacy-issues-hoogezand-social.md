🩺 Anouk Dijkstra built ZorgMatch — matching home care clients in Hoogezand with independent caregivers — in Lovable, moving fast on a product her community urgently needed. What she didn't know: care notes and medication schedules sat behind sequential, guessable URLs. Anyone with an account could view another client's medication schedule just by changing a number in the address bar. 😳

AI tools build what you asked for. They don't ask "what happens when this person wants their data deleted?" 🧠

❌ Care records reachable via sequential, predictable URLs — a classic IDOR vulnerability
❌ No permission check on who could view whose medication schedule
❌ Sensitive fields stored without encryption at rest
❌ No GDPR-required data export or deletion flow built in at all

✅ Rebuilt authorization so every record request is checked against the logged-in user's actual permissions
✅ Encrypted sensitive fields at rest
✅ Added a proper data export and deletion flow to meet GDPR requirements

At **LaunchStudio**, this is the exact review our engineers run for AI-built apps handling personal or sensitive data — 11+ years of experience behind every audit. 🛡️

Her result: ZorgMatch now passes a full data access audit, with every care record accessible only to the client, their caregiver, and authorized staff. 🚀

👉 Handling sensitive personal data in an AI-built app? Talk through what you might be missing: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AIPrivacy #GDPR
