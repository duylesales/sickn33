🦵 Charlotte Dekkers is a physiotherapist in Apeldoorn who built Herstelpad with Lovable and Supabase: therapists assign exercise programmes, patients log pain scores and progress, practices see outcomes. A group of eight practices wanted to roll it out. Then their information security officer sent a list of requirements. 📋

EU hosting, separation between practices, logging of who viewed records, MFA, a processing agreement and DPIA documentation. The assessment found: 🧠

❌ The database hosted outside the EU
❌ Any therapist able to see every patient across all practices
❌ Full pain notes sent to an AI provider for weekly summaries
❌ No access logging, no MFA, and a BSN field added during prompting that the app didn't need

✅ An EU region, with practices separated and roles enforced by Row Level Security and tests
✅ An append-only audit log of access and changes to patient records, with export
✅ MFA for therapists, the BSN field removed and existing values deleted
✅ AI summaries using only pseudonymised scores and dates, plus storage, tested backups and DPIA documentation

At **LaunchStudio**, backed by Manifera's 11+ years of building software for organisations with strict data requirements, such as Vodafone and TNO, we make health apps production ready alongside your legal and privacy advisers. 🛠️

Her result: €4,900, thirteen business days. The security officer approved, and the eight practices onboarded about 1,100 patients. 🚀

👉 Production launch for healthcare apps in the Netherlands: https://launchstudio.eu/en/blog/production-launch-for-healthcare-apps-in-the-netherlands

#HealthTech #NEN7510 #GDPR #Lovable #AIFounder #LaunchStudio #Manifera
