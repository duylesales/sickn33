🚨 Noor Bakker, a physiotherapist in Amersfoort, built FysioSlot with Lovable and Supabase: online booking for small practices, with patient intake forms and treatment notes. Three practices, eleven therapists. Then a patient who works in IT mentioned, kindly, that he could fetch other patients' intake forms from his browser's developer tools. 😳

Supabase is secure when it's configured. The AI never said which parts it skipped. Here's what Noor found: 🧠

❌ RLS disabled on two tables Lovable created later: intake_forms and treatment_notes
❌ Policies on the other tables that let any logged-in user read everything
❌ The service role key in a frontend environment file
❌ Intake form uploads in a public storage bucket

✅ Exposed key rotated, RLS enabled on every table
✅ A membership model: patients see their own records, therapists only their own practice
✅ Intake files in a private bucket with signed URLs
✅ Migrations in git, a staging project and daily backups with a tested restore

At **LaunchStudio**, backed by Manifera's 11+ years of enterprise PostgreSQL work, a Supabase developer finishes the layer AI builders leave open - on your own account, in your own repository. 🛠️

💡 Her result: €2,900, six business days. FysioSlot has since grown to seven practices with no further access issues. 🚀

👉 Looking for a Supabase developer? Here's the production setup step by step: https://launchstudio.eu/en/blog/supabase-developer-for-hire-production-setup-and-rls

#Supabase #RowLevelSecurity #Lovable #HealthTech #LaunchStudio #Manifera
