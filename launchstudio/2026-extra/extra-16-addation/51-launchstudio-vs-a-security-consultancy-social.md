📊 SCOREBOARD: one occupational health SaaS, two penetration tests

FIRST TEST
Findings: 32
Rated high: 7

RETEST
Findings: 3
Rated high: 0
All low severity, fixed within a day

Pieter Brink runs Verzuimregie from Enschede, built with Cursor and Supabase: employers and company doctors coordinate sick leave cases. A large employer required an independent penetration test before signing, so Pieter booked a security consultancy straight away.

The report was clear about what was wrong. The high-rated findings included:
• Missing ownership checks on API routes
• Case documents in a public bucket
• An exposed service key
• No rate limiting on login
• Outdated dependencies

The problem: Pieter had no developer. Fixing things with his AI tool resolved some findings, and broke document uploads for doctors.

What happened between the two tests (LaunchStudio, 8 business days, €3,300):
✓ Ownership checks on every route through one shared helper, backed by Row Level Security policies with tests for employers, employees and doctors
✓ Documents moved to private storage with signed links
✓ The service key rotated
✓ Rate limits and security headers added
✓ Dependencies updated
✓ Extra hardening in areas the test hadn't covered
✓ A short note for the testers explaining every fix

The employer signed after receiving the final report. Pieter now schedules an independent test every year, with LaunchStudio's ongoing care in between.

"The consultancy told me exactly what was wrong. I just had nobody who could fix it properly. Next time, I will do it the other way round." - Pieter Brink

https://launchstudio.eu/en/blog/launchstudio-vs-a-security-consultancy

#Pentest #Security #Cursor #Supabase #AIFounder #LaunchStudio #Manifera
