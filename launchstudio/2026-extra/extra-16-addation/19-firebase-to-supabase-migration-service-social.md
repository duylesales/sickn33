📦 MOVING DAY: a running coach network leaves Firebase

WHY MOVE?
Femke Smit runs a network of independent running coaches based in Nijmegen. She built Looplijn with Cursor and Firebase: coaches create training plans, athletes log runs, and both see progress charts. After two years and around 3,000 athletes, she wanted monthly reports per coach, an export for a sports science partner and EU-region hosting under clear terms. And the Firebase bill had tripled in six months.

WHAT WAS IN THE BOXES
📦 Plans stored as documents, with nested weeks, sessions and comments
📦 A copy of the author's name and photo URL on every comment
📦 Athlete names stored in up to twelve places
📦 A progress chart listening to an athlete's entire run history in real time, which explained most of the reads
📦 Security Rules that let any coach read any athlete's data

UNPACKING IN THE NEW HOUSE (LaunchStudio, 15 business days, €5,200, plus €49/month)
✓ A relational model: coaches, athletes, plans, sessions, runs and comments
✓ Over 400 inconsistent name and email copies resolved, with Femke's approval
✓ Row Level Security, so coaches see only their own athletes
✓ Users migrated with their password hashes, confirmed with 50 real accounts before cutover
✓ The progress chart rebuilt as a query on a summary view, with realtime kept only for new comments

THE MOVE
Sunday evening. 40 minutes.

SETTLING IN
No athlete had to reset a password. Monthly coach reports became one query. The research export took a day instead of weeks. And the monthly database cost fell to about a third of the last Firebase bill.

"I expected a painful weekend and a flood of support emails. We had three questions, all about the new report button." - Femke Smit

https://launchstudio.eu/en/blog/firebase-to-supabase-migration-service

#Firebase #Supabase #Migration #Cursor #AIFounder #LaunchStudio #Manifera
