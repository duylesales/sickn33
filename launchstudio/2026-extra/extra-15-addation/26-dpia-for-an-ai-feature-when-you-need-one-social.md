⚠️ RISK REGISTER: an AI assistant for debt counsellors

Fatima Ouali, a former debt counsellor in Zaandam, built Schuldwijzer with Cursor and Supabase: case management for debt counselling organisations, covering clients' debts, creditors, payment plans and documents. Its AI assistant answers counsellors' questions about a client and drafts letters to creditors. A municipal debt counselling service wanted it, and its privacy officer required a DPIA.

The context: vulnerable clients, data on income, health affecting payment capacity and family circumstances, and new technology. Several high-risk criteria at once.

RISK 1: The assistant sees too much
Found: retrieval across the whole organisation, not just the counsellor's caseload
Measure: retrieval limited to documents the counsellor may see, enforced by Row Level Security on the underlying queries

RISK 2: Data leaves the EU
Found: prompts sent to a US endpoint without a processing agreement
Measure: an EU endpoint under a processing agreement, no training use

RISK 3: More data than needed
Found: full identifiers in prompts
Measure: identifiers the task doesn't need are stripped

RISK 4: Logs kept forever
Found: full prompts and answers stored indefinitely
Measure: metadata only, 30-day retention

RISK 5: Letters sent unchecked
Found: AI drafts could go out without review
Measure: counsellor review and edit required, with clear AI labelling

RISK 6: Instructions hidden in documents
Measure: text inside uploaded documents treated as data, never as commands

LaunchStudio also wrote a DPIA input pack on data flows, measures and limitations for the privacy officer (12 business days, €4,400).

The outcome: residual risks judged acceptable, and a rollout to 25 counsellors, who save around an hour a day on letters. No letter has gone out unreviewed.

"My clients are often in the most stressful period of their lives. The AI had to be helpful without ever being careless with their information." - Fatima Ouali

https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one

#DPIA #ResponsibleAI #GDPR #GovTech #AIFounder #LaunchStudio #Manifera
