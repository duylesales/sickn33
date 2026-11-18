🧪 LAB NOTES: Can a festival volunteer app survive 10:00 on a Saturday?

SUBJECT
Vrijwilligersrooster, built by Tim Hoogland with Bolt and Supabase. Festival organisers publish volunteer shifts, volunteers claim them, and free tickets are the reward.

THE CHALLENGE
A large summer festival near Nijmegen would open 4,000 shifts at exactly 10:00, announced to around 9,000 registered volunteers. The most simultaneous users Tim had ever seen: about 40.

SETUP
A spike test on a staging copy, with synthetic data and 9,000 test accounts.

OBSERVATION AT ~600 CONCURRENT USERS
• The shift list took over 12 seconds to load
• Claims started failing

DIAGNOSIS
• Every user loaded all 4,000 shifts with their claims
• The RLS policy on shifts queried the volunteer's teams for every single row
• No index on the shift date and team columns
• Claims checked in the browser, so two volunteers could take the last spot
• A confirmation email sent synchronously with every claim

INTERVENTION (LaunchStudio, 10 business days, €4,300)
• Shift list paginated by day and team, with only the needed columns
• Composite indexes, and the policy rewritten around an indexed membership lookup
• Claiming moved into a database function that locks the shift row and checks capacity in a transaction, so overbooking is impossible
• Emails moved to a background queue, connection pooling configured

RETEST
1,500 concurrent users. 95th percentile under 800 milliseconds. Zero errors.

FIELD RESULT
On the day, around 5,200 volunteers opened the app in the first ten minutes. All 4,000 shifts were claimed within 47 minutes, with no overbooking and no downtime. The festival renewed and recommended the app to two other events.

"I had tested my app with friends. The festival tested it with nine thousand volunteers. Doing the load test first meant the festival never found out how close it came." - Tim Hoogland

https://launchstudio.eu/en/blog/load-testing-an-ai-built-app-before-launch

#LoadTesting #Supabase #Performance #EventTech #AIFounder #LaunchStudio #Manifera
