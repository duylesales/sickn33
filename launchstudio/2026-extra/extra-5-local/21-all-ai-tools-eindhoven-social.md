🔍 CASE FILE: The Demo That Was Too Perfect

THE CLIENT
Ilona Peters, Eindhoven. Built Circuo, an IoT monitoring dashboard for small manufacturing floors, in Lovable over about two weeks of evenings.

THE SITUATION
The frontend was polished enough that two Brainport-region manufacturers asked to pilot it. In the demo, everything worked flawlessly.

THE CLUE
In the demo, there had only ever been one account.

THE DISCOVERY
During onboarding, it surfaced: the database had no row-level security. Any logged-in user could read any other company's sensor data just by changing an ID in the URL. API keys were exposed in client-side code as well.

THE SOLUTION (LaunchStudio, 6 business days, €1,450)
• Audit of the Supabase schema
• Row-level security policies scoped to each company's account
• A rebuilt auth flow, so sessions can't leak across tenants
• Secrets moved into a secured backend layer
• Ilona's Lovable frontend left untouched

CASE CLOSED
Circuo went live with both pilot manufacturers that same month. Ilona then signed a third client after passing its security questionnaire, which the original build would have failed outright.

"I thought I'd built a finished product. I'd actually built a very convincing demo. LaunchStudio didn't touch my design - they fixed the part I didn't know was broken." - Ilona Peters

Only ever tested with one account? Open your own case file: https://launchstudio.eu/en/blog/21-all-ai-tools-eindhoven

#AINativeFounder #LaunchStudio #Manifera #RowLevelSecurity #Eindhoven
