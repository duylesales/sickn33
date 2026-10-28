🚨 Hugo Verbeek spent eleven years as a policy adviser before founding BuurtSignaal in The Hague: residents report broken streetlights, illegal dumping and unsafe crossings, and municipal teams triage and respond. Built in Windsurf, piloted with one city district - residents liked it, staff liked it more. Then procurement sent a 90-question security and privacy questionnaire. Hugo could answer about a third. 😳

Staff roles were just "user" and "admin", with case-handler limits only in the interface. No audit log. Password logins instead of the municipality's identity provider. Resident photos with location data kept forever, US hosting, and keyboard traps in the resident form. Here's what moving AI code to production for public-sector buyers really involves: 🧠

❌ Two roles, partly enforced in the interface
❌ No record of who viewed or changed resident data
❌ Passwords instead of government SSO
❌ Indefinite retention, US hosting and inaccessible forms

✅ Four staff roles enforced in the database, plus an append-only audit log
✅ SSO via the municipality's OpenID Connect provider, with MFA for administrators
✅ Location metadata stripped from photos, agreed retention rules, EU hosting with tested backups
✅ Accessibility fixes and a BIO-mapped security overview, processor list, recovery description, incident procedure and exit plan

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering - including work for TNO - we harden first, so the penetration test confirms the work instead of cataloguing basics. ⚙️

His result: €6,900, twenty-one business days. The independent pentest found two low-severity issues, fixed that week. BuurtSignaal signed a three-year contract, and two neighbouring municipalities have since piloted it with the same documentation. 🚀

👉 AI code to production in The Hague: GovTech and public-sector buyers: https://launchstudio.eu/en/blog/ai-code-to-production-in-the-hague-govtech-and-public-sector-buyers

#GovTech #TheHague #BIO #Accessibility #LaunchStudio #Manifera
