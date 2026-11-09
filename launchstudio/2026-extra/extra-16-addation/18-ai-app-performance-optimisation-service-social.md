🐢 Thijs Kuipers runs a facility services company in Amersfoort and built Roosterpunt with Bolt and Supabase to plan cleaning shifts across 140 locations. At first the planning dashboard loaded instantly. A year and tens of thousands of shifts later, it took around eleven seconds, and supervisors had started printing schedules instead. 🖨️

He was ready to pay for a bigger server. The measurements told a different story: 🧠

❌ Every shift ever created fetched, then filtered to this week in the browser
❌ Each location card making its own request: 100+ requests per page load
❌ A Row Level Security policy running a subquery for every row
❌ PDF exports inside the request, freezing the screen for half a minute

✅ Filtering moved to the database with indexes on location and date
✅ One joined query instead of a hundred small ones
✅ The policy rewritten to use an indexed lookup table
✅ Background PDF exports, lighter images, two unused libraries removed and slow-query alerts

At **LaunchStudio**, backed by Manifera's 11+ years of building systems for clients such as Vodafone and TNO, we measure first, fix the biggest causes and prove the result with before-and-after numbers. 🛠️

His result: €2,300, six business days. The dashboard loads in under a second with the full history, supervisors came back within a week and the database upgrade wasn't needed. 🚀

👉 Performance optimisation for AI-built apps: https://launchstudio.eu/en/blog/ai-app-performance-optimisation-service

#Performance #Supabase #Bolt #CoreWebVitals #AIFounder #LaunchStudio #Manifera
