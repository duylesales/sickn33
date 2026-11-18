🔍 CASE FILE: The Quotation That Arrived Twice

THE CLIENT
Marnix Oosterveld, Waalwijk. Runs Offerteroute, built with Lovable and extended over a year by AI sessions: quotation management for kitchen and bathroom installers. 61 companies, around 900 quotations a month.

THE COMPLAINT
Customers received two copies of every quotation, sometimes minutes apart, sometimes hours. Two customers replied to both, creating duplicate follow-ups, and one argument about a price that changed between versions.

THE CLUE
Some duplicates arrived at three in the morning.

THE SUSPECTS
Suspect 1: the application, which sent a quotation email when one was marked sent.
Suspect 2: a trigger on the quotations table, written eight months earlier, which fired on any update that changed the status column. Including the nightly job that updates expiry dates.

Both were guilty.

FURTHER INVESTIGATION: eleven triggers in total
• 4 maintaining timestamps and counters, correctly
• 2 duplicating application logic
• 1 calling an external webhook inside a transaction, which caused three timeouts
• 3 doing nothing, because their target tables had been replaced
• 1 security definer function fetching quotations with no authorisation check, callable by any logged-in user against any company's data

THE RESOLUTION (LaunchStudio, 3 business days, €2,700)
✓ Every function and trigger inventoried and described
✓ The email and webhook triggers removed, with the work moved into the application, where it can be retried and logged
✓ Duplicate-logic pairs resolved, and three dead triggers dropped
✓ The security definer function rewritten with an explicit membership check and a fixed search path
✓ Timestamp and counter triggers kept, documented and covered by SQL tests
✓ The whole schema dumped into a baseline migration and committed, instead of living only in the dashboard

CASE CLOSED
Duplicate emails stopped, the timeouts stopped with them, and the exposed function was closed before anyone used it. Marnix now has a two-page document describing what his database does without being asked.

"Nothing in my code sent a second email. It took an afternoon to accept that the database was doing it by itself, because I had asked it to, in a chat I do not remember." - Marnix Oosterveld

https://launchstudio.eu/en/blog/lovable-supabase-database-functions-and-triggers-worth-keeping

#Supabase #PostgreSQL #DatabaseDesign #Lovable #LaunchStudio #Manifera
