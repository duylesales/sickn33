🔴 INCIDENT REPORT: one prompt, every session note

PRODUCT
Behandelbord, built by Eva Kuipers with Lovable and Supabase. A practice tool for independent dietitians: client records, session notes and nutrition plans. 31 dietitians, notes on roughly 2,600 clients.

TRIGGER
One evening, the prompt: "split the notes field into separate fields for complaints, advice and follow-up."

WHAT HAPPENED
The generated migration dropped the session_notes table and recreated it with the new structure. The builder was connected to production, so it ran there immediately.

DETECTION
The next morning. Dietitians opened client files, and every historical session note was gone.

COMPLICATING FACTORS
• Daily backups on the Pro plan, but no point-in-time recovery
• About fourteen hours of new notes written since the last backup
• Health data involved

RESPONSE (LaunchStudio, data restored on day two)
1. Further changes stopped, the incident documented, GDPR obligations assessed, the incident recorded and the dietitians informed
2. The latest daily backup restored to a separate project
3. Old notes copied back into production and mapped into the new structure, with the original text in the "complaints" field and marked for review
4. Notes written after the backup kept intact
5. The few notes written between the backup and the migration recovered from API logs

PREVENTION (8 business days in total, €3,400)
• A staging project for Lovable
• Point-in-time recovery enabled
• Migration review before every production release
• Restricted production access
• Soft deletes for client records

OUTCOME
99.6% of historical notes restored within two days. Every dietitian stayed. A restore test now runs quarterly, and in the following year two risky migrations were caught in review before production.

"One prompt erased two years of my customers' work. What saved me was a backup I had never tested and people who knew how to use it carefully." - Eva Kuipers

https://launchstudio.eu/en/blog/why-did-my-data-disappear-after-an-ai-prompt

#DataRecovery #Backups #Lovable #HealthTech #AIFounder #LaunchStudio #Manifera
