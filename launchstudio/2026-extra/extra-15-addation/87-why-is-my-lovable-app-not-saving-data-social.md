The app said: ✅ Saved.
The database said: ❌ No.
140 hours of work disappeared in between.

Ruben Smeets built Urenbriefje with Lovable and Supabase: technicians at small installation companies log hours per job on their phones, and the office turns them into invoices. Six companies, around 70 technicians, used it daily.

At the end of a month, one customer's invoices came out 140 hours short. The technicians insisted they had logged everything. And every time, the app had shown "Saved."

WHAT THE APP SAID vs WHAT ACTUALLY HAPPENED

Said: "Saved" for technicians invited recently.
Happened: a prompt had added team-based access. The insert policy checked team membership, but new technicians had no membership row, so every entry was refused. The code ignored the error.

Said: "Saved" for entries with travel time.
Happened: another prompt had added a "travel time" field that didn't exist in the production database. Every such entry failed, for everyone.

Said: "Saved" early in the morning.
Happened: sessions left open overnight on phones had expired, so entries ran as an anonymous user.

Making the app tell the truth (LaunchStudio, 6 business days, €2,200):
✓ Missing membership rows added, and invitations now create them automatically
✓ The missing migration applied, with staging synced to production
✓ Ownership and team columns set by database defaults, not by the frontend
✓ Every save checks the server response, keeps the form on failure and shows a clear message
✓ Failed writes reported to error monitoring
✓ Session refresh fixed, so an expired session asks to log in again without losing the entry
✓ Most missing entries reconstructed from API logs, for the customer to review

The next month's invoices matched the technicians' records. In the following quarter, monitoring warned Ruben twice about problems that were fixed before any customer noticed.

"The worst part wasn't the bug. It was that my app told people everything was fine." - Ruben Smeets

https://launchstudio.eu/en/blog/why-is-my-lovable-app-not-saving-data

#Lovable #Supabase #RowLevelSecurity #FieldService #AIFounder #LaunchStudio #Manifera
