🚨 A Metrivue customer briefly saw another store's revenue numbers on their own dashboard. Radek's cache key never asked whose data it was caching. 😳

Caching is conceptually trivial and practically treacherous — and the treacherous 20% is exactly where a data leak lives: 🧠

❌ The cache key was built from the route path alone — `dashboard:summary` — with no account identifier at all
❌ Whichever customer requested the dashboard first within a 60-second window populated the entry every other customer briefly saw
❌ The speed improvement was tested against one account, so nobody ever tested it as two customers back to back
❌ Caching added at a proxy or CDN layer by URL alone can't tell a personalized response from a public one

✅ Include the account or user ID in every cache key that varies by who's asking, full stop
✅ Pick an invalidation strategy deliberately per value — TTL, explicit invalidation, or cache-aside as a backstop
✅ Test every cached route with two logged-in accounts back to back before it ships
✅ Audit any caching added under `/api/` broadly for the same per-user pattern, not just the one that leaked

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit cache keys for exactly this pattern before your first real traffic spike finds it. 🗂️

His result: the leak was closed within hours with no evidence of financial or competitive harm, and the two-account test now runs automatically on every deploy touching the caching layer. 🚀

👉 Check whether your caching layer knows whose data it's serving: [Link to article]

#IndieHacker #Redis #ProductionReady #SaaS #LaunchStudio #Manifera
