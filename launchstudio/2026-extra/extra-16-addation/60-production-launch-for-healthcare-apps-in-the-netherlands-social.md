🩺 THE INFORMATION SECURITY OFFICER'S LIST

☐ EU hosting
☐ Separation between practices
☐ A log of who viewed patient records
☐ MFA for therapists
☐ A processing agreement
☐ Documentation for the DPIA

Charlotte Dekkers is a physiotherapist in Apeldoorn who built Herstelpad with Lovable and Supabase: physiotherapists assign exercise programmes, patients log pain scores and progress, and practices see outcomes. A group of eight practices wanted to roll it out. Their information security officer sent the list above.

The assessment found the opposite of most boxes:
• The database outside the EU
• Policies letting any therapist see every patient, across practices
• Full pain notes sent to an AI provider for weekly summaries
• No logging, and no MFA
• A BSN field, added during prompting, that the app didn't even need

Ticking the boxes (LaunchStudio, Launch & Grow, 13 business days, €4,900, plus €49/month):
☑ The project moved to an EU region
☑ Practices separated, with roles for therapists, practice managers and patients, enforced by Row Level Security and covered by tests
☑ An append-only audit log of access and changes to patient records, exportable for the practices
☑ MFA enforced for therapists
☑ The BSN field removed, and existing values deleted
☑ AI summaries sent only pseudonymised scores and dates
☑ Private storage, backups with a restore test, and monitoring
☑ Data flows documented for the DPIA
☑ The processing agreement, prepared by Charlotte's privacy lawyer

The security officer approved Herstelpad after reviewing the documentation. The eight practices onboarded around 1,100 patients, and two more practice groups later used the same documentation in their own assessments.

"I know how to treat patients. I did not know how to prove to a security officer that their data was safe. Now I have an audit trail and the paperwork to show it." - Charlotte Dekkers

https://launchstudio.eu/en/blog/production-launch-for-healthcare-apps-in-the-netherlands

#HealthTech #NEN7510 #GDPR #Lovable #AIFounder #LaunchStudio #Manifera
