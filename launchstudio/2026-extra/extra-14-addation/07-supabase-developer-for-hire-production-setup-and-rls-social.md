Dear patient who works in IT, 💌

Thank you. You could have stayed quiet. Instead, you mentioned, kindly, that by changing a request in your browser's developer tools you could fetch other patients' intake forms.

That's how Noor Bakker found out.

Noor, a physiotherapist in Amersfoort, built FysioSlot with Lovable and Supabase: online booking for small physiotherapy practices, with patient intake forms and short treatment notes therapists add after each session. Three practices, eleven therapists in total.

When she checked Supabase, she found what you had found, and more:
• RLS disabled on two tables, intake_forms and treatment_notes, which Lovable had created after the initial setup
• Policies on the other tables that let any logged-in user read everything
• The service role key in a frontend environment file
• Intake form uploads in a public bucket

What happened next (LaunchStudio, 6 business days, €2,900):
✓ The exposed key rotated
✓ RLS enabled on every table, with a membership model: patients see only their own records, therapists see records for their own practice
✓ Treatment notes readable only by therapists of that practice
✓ Intake files in a private bucket with signed URLs
✓ Migrations in the repository, a staging project, daily backups with a tested restore
✓ The setup documented for the practices' data protection records

The fixes were live within six business days. Noor informed the affected practices and documented the incident as required. FysioSlot has since grown to seven practices, with no further access issues.

So, thank you. Your colleagues' records are safer because you spoke up.

"I assumed Supabase was secure by default. It is secure if you configure it - and the AI never told me which parts it skipped." - Noor Bakker

https://launchstudio.eu/en/blog/supabase-developer-for-hire-production-setup-and-rls

#Supabase #RowLevelSecurity #Lovable #HealthTech #LaunchStudio #Manifera
