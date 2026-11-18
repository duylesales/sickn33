🏑 CLUB 1: everything works.
CLUB 10: still fine.
CLUB 23, START OF THE NEW SEASON: everything at once.

Sven Mulder, treasurer of a hockey club in Deventer, built Teamkas in Lovable to collect membership dues, match fees and kit payments. It worked so well for his own club that he turned it into a SaaS. Six months later: 23 clubs, roughly 110 club administrators and a few thousand paying members.

Then the new season hit all of them on the same day.

WHAT BROKE AT CLUB 23
💥 For larger clubs, the payments overview took over ten seconds, because every transaction was fetched and filtered in the browser
💥 Reminder emails ran through Supabase's built-in email service and hit its limits. Hundreds never went out, and clubs assumed members were ignoring them.
💥 Two treasurers at one club editing a member's fee at the same time silently overwrote each other
💥 When a club asked why one member had been charged twice, Sven had no way to see what had happened

WHAT LASTS TO CLUB 41 (LaunchStudio, Launch & Grow, 13 business days, €3,800, plus €49/month)
✓ Heavy queries rewritten with pagination, server-side filters and indexes
✓ All email moved to a transactional provider with an authenticated sending domain
✓ Optimistic locking, so conflicting edits show a warning instead of overwriting
✓ A simple admin view with an audit log per member
✓ Monitoring on page load times and email delivery
✓ The Lovable interface the clubs knew, left untouched

THE RESULTS
Payments overview for the largest club: from over ten seconds to under one. Reminder delivery: from an estimated 60% to above 99%. Outstanding dues across the clubs: down about a third the following month. And by the end of the season, 41 clubs.

"Every club I added made the app a little worse, and I only saw it when the new season hit all of them at once." - Sven Mulder

https://launchstudio.eu/en/blog/ai-app-production-problems-that-only-appear-at-100-users

#SaaS #Lovable #Scalability #Startups #LaunchStudio #Manifera
