🚨 Rutger Doedens's Urenstaat tracks hours for 34 engineering consultancies. For his largest customer — 90 consultants — the hours overview took eleven seconds to load, and the monthly invoicing export timed out every single month. They'd been working around it by exporting week by week. 😳

Both had the same cause: the app fetched all 240,000 rows and paginated in the browser. Here's how list pages break as data grows: 🧠

❌ One request returning every row the account owns
❌ Offset pagination that gets slower the deeper you go — and skips or repeats rows
❌ A sort order without a unique tiebreaker
❌ An export that built the whole CSV in memory

✅ Cursor pagination on timestamp plus ID, with a matching composite index
✅ The row count replaced by a "fetch one extra" next-page check
✅ Filters cut from nine arbitrary fields to four indexed ones, with name search on full-text search
✅ A streaming export, a background job with an email link for big ones — tested against 400,000 seeded rows

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your product feeling the same at 200 customers as it did at 20. ⚡

His result: one business day and €1,900 later, the overview went from 11 seconds to 240 milliseconds for the largest firm and the monthly export finished in 9 seconds. They stopped exporting week by week — and mentioned it at renewal. 🚀

👉 Pagination and lists that stay fast: https://launchstudio.eu/en/blog/lovable-supabase-pagination-and-lists-that-stay-fast

#Supabase #Performance #Pagination #Lovable #LaunchStudio #Manifera
