⏱️ 11 seconds ➜ under 1 second

That's one planning dashboard, before and after.

Thijs Kuipers runs a facility services company in Amersfoort and built Roosterpunt with Bolt and Supabase to plan cleaning shifts across 140 locations. At first, the dashboard loaded instantly. A year and tens of thousands of shifts later, it took around eleven seconds. Supervisors started printing schedules instead.

Where the seconds went:
⏳ Every shift ever created was fetched, then filtered to the current week in the browser
⏳ Each location card made its own request for staff details: more than a hundred requests per page load
⏳ The RLS policy checked a supervisor's locations with a subquery that ran for every row
⏳ The PDF export ran inside the request, freezing the screen for half a minute

Thijs was about to upgrade his database plan.

Where the seconds came back (LaunchStudio, 6 business days, €2,300):
⚡ Filtering moved into the database, with a date range and indexes on location and date
⚡ The per-card requests replaced by a single query joining staff details
⚡ The policy rewritten around an indexed lookup table of supervisor locations
⚡ PDF exports moved to a background job that emails the file when it's ready
⚡ Location images resized and lazy-loaded, and two unused libraries removed from the bundle
⚡ Monitoring for slow queries, with alerts

The new time: under one second, with the full history in place. Supervisors were back in the app within a week. And the database plan turned out to be big enough after all.

"I was ready to pay for a bigger server. It turned out the app was asking the database the same question a hundred times." - Thijs Kuipers

https://launchstudio.eu/en/blog/ai-app-performance-optimisation-service

#Performance #Supabase #Bolt #CoreWebVitals #AIFounder #LaunchStudio #Manifera
