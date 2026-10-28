🚨 Merel Duijvestein's Bouwdossier exchanges drawings, permits and contracts for twelve building firms and four architects around Almere - about 300 active projects. Each customer got an API key: stored in plain text, full access including deletion, no rate limit, never rotated. One firm's key had sat in a public repository for months. 😳

Their own IT manager found it and reported it. Here's what goes wrong with the keys you hand out: 🧠

❌ Keys stored in plain text so you can show them again
❌ Every key with full access, including deletion and user management
❌ No rate limit, no rotation, no record of which key did what
❌ No quick way to revoke everything for one customer

✅ Scoped keys - read, write and admin as separate grants
✅ Hash keys, show them once, name them per integration, display last-used time
✅ Let customers revoke their own keys, and sign webhooks in both directions
✅ An integration audit trail, plus one operation to revoke all of a customer's keys

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we design integration access assuming every key will eventually leak. 🔑

Her result: ten business days and €4,700 later, all 16 keys were reissued with the narrowest scope - nine needed only read-and-upload. The review found no unauthorised use, which was only provable because logging existed. The firm stayed and expanded its contract. 🚀

👉 The keys you hand out to integrations: https://launchstudio.eu/en/blog/ai-app-security-the-keys-you-hand-out-to-integrations

#APISecurity #Integrations #Lovable #ConTech #LaunchStudio #Manifera
