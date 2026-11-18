MYTH: "NIS2 doesn't apply to my startup, so I can ignore it."
FACT: It may not apply to you. It can still decide whether your biggest prospect signs. 🛡️

Bas Hendriks, a former maintenance engineer, built Onderhoudsplan in Cursor: a planning tool that helps technical teams schedule inspections and maintenance for pumps, valves and installations. Three people, well under €1 million in revenue. Not in scope for NIS2.

His first large prospect, a regional water company in Gelderland, was.

MYTH: "A supplier questionnaire is a formality."
FACT: The water company sent 74 questions referencing NIS2, plus a request for a 24-hour incident notification commitment. Bas could answer about a third.

MYTH: "If the app works, the security is fine."
FACT: Staff accounts had no MFA. The admin panel was protected only by an email check in the frontend. No audit logs. Backups had never been restored. Nobody had written down which services processed customer data.

What LaunchStudio fixed (9 business days, €3,400):
• MFA for all staff and admin users
• Admin authorisation moved into the database, with Row Level Security and role checks
• Audit logs for logins and admin actions
• Point-in-time recovery, with a documented restore test
• Secrets moved out of the repo and rotated, dependency alerts and staging added
• Help writing a security overview, a sub-processor list and a one-page incident plan with a realistic 24-hour commitment

The questionnaire went back in nine business days. The water company accepted it with two follow-up questions and rolled Onderhoudsplan out the next quarter. The same documents cut two later procurement processes to under a week.

"I wasn't covered by NIS2, but my customer was. Being able to answer their questions properly was the difference between a pilot and a contract." - Bas Hendriks

https://launchstudio.eu/en/blog/nis2-for-saas-startups-does-it-apply-to-you

#NIS2 #Cybersecurity #B2BSaaS #Procurement #AIFounder #LaunchStudio #Manifera
