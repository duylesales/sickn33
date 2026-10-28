🚨 Suzanne Grotenhuis's Inspectierapport produces about 2,000 inspection reports a month for 39 surveying and inspection firms. She made her repository public for four days to share a code sample. Eleven months earlier, an environment file had been committed - with the Supabase service role key, email credentials, a usage-billed mapping key and her webhook signing secret. 😳

Within a day, automated scanners found it. She heard from the mapping provider: 140,000 requests in eleven hours from unknown addresses. Here's what to do in the first hour after a leak: 🧠

❌ Deleting the file or commit first - the key still works, and clones and scanners already have it
❌ Rotating only the key you noticed, not everything in the same file
❌ Never checking provider logs for whether it was used
❌ Leaving the route open: no secret scanning, weak ignore rules, shared logins

✅ The abused mapping key rotated first, then the database key, then email and the webhook secret (accepting old and new during the switch)
✅ Every credential in the file treated as compromised, rotated in order of consequence
✅ Database and email logs reviewed, a documented breach assessment and a precautionary report to the Dutch DPA
✅ Build-time secret scanning, fixed ignore rules, per-person access in a password manager, and an inventory of nine secrets

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we help you rotate first and tidy afterwards - the order that actually reduces risk. 🔑

Her result: two business days and €3,100 later, the mapping provider waived €2,840 of usage, and no evidence of database or email access was found. The real incident, she concluded, was the key sitting in that file for eleven months. 🚀

👉 Rotating every secret after a leak: https://launchstudio.eu/en/blog/ai-app-security-rotating-every-secret-after-a-leak

#IncidentResponse #Secrets #AppSecurity #Lovable #LaunchStudio #Manifera
