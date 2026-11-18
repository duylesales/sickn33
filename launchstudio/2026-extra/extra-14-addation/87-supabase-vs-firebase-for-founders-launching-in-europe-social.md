🧰 A toolbox with two tools in it

Firebase: great at live things. Chat. Match updates as they happen.
PostgreSQL: great at adding things up. Fees per team. Totals per season.

Mark Peeters had been using one tool for both jobs.

He built Clubbeheer with FlutterFlow and Firebase: a mobile app for amateur sports clubs, covering members, teams, match schedules and fee payments. Chat and live match updates worked well. Reporting didn't. Treasurers wanted fee overviews per team and season, which meant reading thousands of documents and stitching them together inside the app. Firebase costs spiked every time a treasurer ran a report. And a permissive Security Rule let any member read every other member's payment status.

How LaunchStudio sorted the toolbox (12 business days, €4,300):

FIRST, A FIX
✓ Security Rules rewritten: members see only their own payments, treasurers see their club's

TOOL 1: Firebase, kept
✓ For the mobile app's real-time features

TOOL 2: Supabase PostgreSQL in Frankfurt, added
✓ A nightly sync of financial data
✓ Treasurer reports as SQL views
✓ A small web dashboard
✓ Monitoring

THE RESULT
Firebase read costs dropped sharply. Reports that took a minute now load in seconds. And treasurers of 22 clubs use the dashboard at season end.

"Firebase was perfect for the live parts of my app. My treasurers needed a database that could add up numbers." - Mark Peeters

https://launchstudio.eu/en/blog/supabase-vs-firebase-for-founders-launching-in-europe

#Supabase #Firebase #PostgreSQL #GDPR #LaunchStudio #Manifera
