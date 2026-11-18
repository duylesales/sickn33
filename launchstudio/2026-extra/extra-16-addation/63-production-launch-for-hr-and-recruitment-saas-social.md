🏷️ BEST BEFORE: candidate data has an expiry date

Bart Lammers runs a recruitment agency for technical staff in Hengelo and built Vakkrachtpool with Bolt and Supabase: vacancies, applications, interview notes and an AI feature that ranked candidates by fit. He started selling it to installation companies hiring their own technicians. Then an employer with 300 staff wanted it, and its HR manager and privacy officer asked three questions: how long is candidate data kept, who can see interview notes, and how does the ranking work?

The database remembered everything:
• Around 9,000 candidate records, going back three years, without consent for long-term storage
• Every user at a customer could see all candidates and interview notes, even hiring managers for unrelated vacancies
• CVs in a public bucket
• An AI ranking that sent full CVs, dates of birth and photos included, to a model provider, and automatically moved low-ranked candidates to "rejected"

The new labels (LaunchStudio, Launch & Grow, 15 business days, €5,900, plus €49/month):

🏷️ Candidates after a procedure ends
Anonymised after a configurable number of weeks, with periods advised by Bart's lawyer

🏷️ Talent pool
Opt-in only, with recorded consent that expires after a year

🏷️ The existing backlog
Cleaned up to match

And around the labels:
✓ Roles for recruiters, hiring managers and HR admins, enforced by Row Level Security, so hiring managers see only candidates for their own vacancies
✓ CVs moved to private storage
✓ The AI feature changed to suggestions only, with a recruiter making every decision
✓ Photos and dates of birth removed before anything is sent to the model
✓ Each suggestion logged, next to the recruiter's final choice
✓ MFA, audit logging and documentation for the processing agreement

The employer adopted Vakkrachtpool after its privacy officer reviewed the documentation and its works council received a description of the AI feature. Bart now uses the same documentation in every sale.

"My database remembered every candidate for three years and my AI rejected people on its own. Now candidates are forgotten when they should be, and every decision has a person behind it." - Bart Lammers

https://launchstudio.eu/en/blog/production-launch-for-hr-and-recruitment-saas

#HRTech #Recruitment #AIAct #GDPR #AIFounder #LaunchStudio #Manifera
