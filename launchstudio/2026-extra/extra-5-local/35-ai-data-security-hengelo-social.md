🩺 PATIENT CHART: Zorgrooster, Hengelo

NAME: Zorgrooster
BUILT BY: Marloes ten Cate, former hospital administrator
BUILT WITH: Lovable
PURPOSE: scheduling for home care nurses, covering patient visit times, care notes and medication schedules

HISTORY
Worked well in a pilot with four nurses. Next step: a regional home care organization with more than sixty staff.

EXAMINATION (LaunchStudio data security review)
No row-level security on the Supabase backend. Any logged-in nurse could query the full patient database, including care notes and medication records for patients they were never assigned to.

DIAGNOSIS
A direct GDPR violation, given the special category health data involved.

TREATMENT (7 business days, €1,450)
💊 Granular RLS policies, so each nurse sees only their assigned patients
💊 Encryption at rest for medication and care note fields
💊 An audit log of every record access, for compliance

PROGNOSIS
Excellent. Zorgrooster passed the care organization's data protection review on the first submission. It now schedules more than sixty nurses across Hengelo and the wider Twente region.

"I had no idea every nurse could see every patient's medication history. That's the kind of mistake that ends a healthcare product before it starts - LaunchStudio caught it before our first real client ever saw it." - Marloes ten Cate

Building with health data? Book a check-up: https://launchstudio.eu/en/blog/ai-data-security-hengelo

#AINativeFounder #LaunchStudio #Manifera #Hengelo #GDPR
