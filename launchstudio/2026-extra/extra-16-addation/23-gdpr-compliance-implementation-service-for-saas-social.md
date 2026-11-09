🗂️ Eline Mertens runs an HR consultancy in Den Bosch and built Verlofwijs with Claude Code and Supabase: small employers manage leave, sick days and employee documents. Her first business customer, with 80 employees, asked for a processing agreement, a subprocessor list and proof that employee data could be deleted. She couldn't answer with confidence. 😟

The data inventory found personal data in seven places: 🧠

❌ Contracts and sick notes in a public storage bucket
❌ Medical notes inside error tracking request bodies, and employee names in analytics URLs
❌ The database hosted outside the EU, and deletion removing only the login
❌ Every admin able to see every employee across all companies

✅ Database and storage moved to an EU region, storage made private with signed links
✅ Company and role-based access enforced in Row Level Security
✅ Data minimised: no request bodies in logs, IDs in URLs, only leave dates sent to the AI provider
✅ Deletion and retention features plus documentation for the processing agreement

At **LaunchStudio**, backed by Manifera's 11+ years of building software for European clients such as Vodafone and TNO, we implement the technical side of GDPR so your app does what your privacy documents promise. 🛠️

Her result: €3,200, nine business days. The customer signed within two weeks, and two more employers used the same documents without further questions. 🚀

👉 GDPR compliance implementation service for SaaS: https://launchstudio.eu/en/blog/gdpr-compliance-implementation-service-for-saas

#GDPR #Privacy #SaaS #ClaudeCode #AIFounder #LaunchStudio #Manifera
