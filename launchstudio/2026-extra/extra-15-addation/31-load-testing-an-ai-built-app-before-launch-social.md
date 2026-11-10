🚨 Tim Hoogland built Vrijwilligersrooster with Bolt and Supabase: festival organisers publish volunteer shifts, volunteers claim them for free tickets. A big summer festival near Nijmegen planned to open 4,000 shifts at exactly 10:00 on a Saturday - announced to around 9,000 volunteers. Tim had never seen more than about 40 people use the app at once. 😳

A spike test on staging told the story: at around 600 concurrent users, the shift list took over 12 seconds and claims began to fail. Here's why you load-test an AI-built app before launch: 🧠

❌ Every user loading all 4,000 shifts with their claims
❌ An RLS policy querying teams for every row, with no indexes
❌ Claims checked in the browser, so two volunteers could take the last spot
❌ Confirmation emails sent synchronously on each claim

✅ The shift list paginated by day and team, with only needed columns
✅ Composite indexes and an indexed membership lookup in the policy
✅ Claims in a database function with row locking - overbooking impossible
✅ Emails in a background queue, connection pooling, and a retest at 1,500 users under 800 ms

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find the breaking point before your customers do. 🛠️

His result: €4,300, 10 business days. On the day, around 5,200 volunteers opened the app in ten minutes, and all 4,000 shifts were claimed in 47 minutes - no overbooking, no downtime. 🚀

👉 Expecting a traffic spike? Here's how to load-test your AI-built app: https://launchstudio.eu/en/blog/load-testing-an-ai-built-app-before-launch

#LoadTesting #Supabase #Performance #EventTech #AIFounder #LaunchStudio #Manifera
