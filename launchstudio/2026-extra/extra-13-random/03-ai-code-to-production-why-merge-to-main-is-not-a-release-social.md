🔴 INCIDENT REPORT: a climbing gym app that deployed its own outage

PRODUCT
PlankPal, built by Daan Visser, a former data analyst in Delft, with Cursor. A membership and check-in app for two bouldering gyms: members scan a QR code at the door, staff see live occupancy and expiring memberships. Daan pushed to main several times a day, and Vercel deployed every push automatically.

TRIGGER
A Thursday evening. Daan asked Cursor to add a "frozen membership" status.

WHAT HAPPENED
The generated migration changed the status column from text to an enum, and rewrote every existing row along the way. Statuses the enum didn't recognise became null. The deploy took forty seconds.

IMPACT
For the next two hours, members with valid passes were refused at the door. The check-in screen treated null as expired.

WHY ROLLBACK DIDN'T HELP
Rolling back the code doesn't roll back data that's already changed.

RECOVERY
The affected rows restored from a point-in-time backup.

PREVENTION (LaunchStudio, 6 business days, €1,600)
• GitHub Actions running type checks and a small suite of check-in tests on every branch
• A separate staging Supabase project with seeded data
• Migrations in their own reviewed pull requests
• A written rollback step required in every PR template
• Error tracking wired to Daan's phone

FOLLOW-UP, four months later
212 releases shipped. CI blocked nine before merge, including two migrations that would have rewritten existing data. Check-in outages since: none.

"I had a pipeline, so I thought I had a process. What I actually had was a very fast way to ship whatever Cursor gave me." - Daan Visser

https://launchstudio.eu/en/blog/ai-code-to-production-why-merge-to-main-is-not-a-release

#Cursor #DevOps #CI #Supabase #LaunchStudio #Manifera
