🏋️ HOME EXERCISE PROGRAMME: getting a physio app ready for 14 practices

Wouter Smit, a physiotherapist running two practices near Utrecht, built Oefenmaatje in Lovable and Supabase. Therapists put together home exercise programmes from a video library, patients follow them on their phones and log pain scores, and therapists see progress before the next appointment. After a year, a chain of fourteen practices wanted it. Its quality officer's requirements showed what the app couldn't do yet:
• Every therapist in both practices could see every patient
• Exercise videos and patients' photos of swelling sat in a public bucket
• No access logs, no MFA, no processing agreement
• A patient deleting their account also deleted treatment progress that was part of the patient record
• Staging held a copy of real patient data

The programme (LaunchStudio, 17 business days, €6,700):

EXERCISE 1: Separation
Data split per practice, therapists limited to their own patients, a logged "stand-in" for colleagues, and defined rights for practice managers.

EXERCISE 2: Strength
Mandatory MFA for staff, and an append-only log of every view and change of patient data.

EXERCISE 3: Privacy
Videos and photos moved to private storage with signed links.

EXERCISE 4: Balance
Patients can stop app access, while clinical data is kept according to the practice's retention obligations, with an export for practices.

EXERCISE 5: Cool-down
Real data out of staging, synthetic data in. Hosting in Frankfurt with tested point-in-time recovery, plus a security overview and data flow description for the processing agreement.

PROGRESS CHECK
The chain approved Oefenmaatje and rolled it out across all fourteen practices: around 4,000 active patients within six months. Next up: an integration with the chain's practice management system.

"I built the app as a physiotherapist. Making it ready for other practices meant thinking like a guardian of other people's patient records." - Wouter Smit

https://launchstudio.eu/en/blog/ai-built-app-for-physiotherapy-practices

#HealthTech #Physiotherapy #GDPR #Supabase #AIFounder #LaunchStudio #Manifera
