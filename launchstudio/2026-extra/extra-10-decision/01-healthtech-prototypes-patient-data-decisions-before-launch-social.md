🚨 Femke's triage app worked beautifully in demos. It also stored symptom descriptions in the same table as patient names, readable by any clinic staff account, and piped through a marketing tool with no Data Processing Agreement. 😳

AI tools build a symptom field exactly like a name field. Here's why that's a problem the moment a real patient shows up: 🧠

❌ One Supabase table, one RLS policy — every authenticated clinic account could read every patient's full symptom history
❌ A general "I agree to terms" checkbox isn't explicit consent for special category health data under Article 9
❌ Symptom text was flowing to a marketing email tool that had never seen a DPA
❌ Lovable and Bolt projects on Supabase often default to a non-EU region nobody thought to check

✅ Move symptom fields into a separate, encrypted table with staff-role access limited to a patient's own clinic
✅ Add read-access logging so any clinic manager can answer "who opened this record, and when"
✅ Replace the generic checkbox with a consent screen naming the specific purpose
✅ List every sub-processor touching patient data before a clinic's procurement team asks for it

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn "it's just a wellness log" into a build that survives a clinic's privacy review. 🩺

Her result: RouteToRecovery signed its first clinic contract four weeks later, after the clinic's privacy officer reviewed the sub-processor list and access logs directly. 🚀

👉 Find out what your patient data actually requires: https://launchstudio.eu/en/blog/healthtech-prototypes-patient-data-decisions-before-launch

#HealthTech #GDPR #StartupFounders #DataPrivacy #LaunchStudio #Manifera
