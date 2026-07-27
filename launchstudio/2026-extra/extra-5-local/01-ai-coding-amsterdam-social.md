🚨 Sanne de Wit spent six weeks building Ledgerly — a shared expense-tracking tool for freelancers — almost entirely in Cursor. It looked finished. Then a beta tester mentioned, almost in passing, that they could see a stranger's grocery receipts. 😳

AI coding tools optimize for "does it run," not "is it safe" — and row-level security is the first thing that quietly gets skipped. 🧠

❌ Every user's expense records were reachable by any other logged-in user by just changing an ID in the URL
❌ The AI had built the database queries without scoping them to the authenticated user
❌ No one caught it in six weeks of testing — because the demo never tested for it
❌ Her Stripe secret key was also sitting in a client-exposed environment file

✅ Add row-level security so queries are scoped to the authenticated user, not just "logged in"
✅ Add rate limiting on the API before real traffic finds the gaps
✅ Rotate and relocate secret keys out of anything the browser can read

At **LaunchStudio**, we're backed by Manifera's 11+ years building production systems for clients like Vodafone and TNO — the same rigor we bring to solo-founder prototypes. 🛡️

Ledgerly relaunched with proper data isolation nine days later and passed a follow-up penetration check with no critical findings. 🚀

👉 Building on AI in Amsterdam right now? Get a free security check before launch: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AICoding #Amsterdam
