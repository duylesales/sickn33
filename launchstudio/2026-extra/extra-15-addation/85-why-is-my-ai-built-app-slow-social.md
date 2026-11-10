🚨 Lisanne de Groot built Kookschrift with Lovable and Supabase: home cooks share recipes, save favourites and plan weekly menus. It grew to around 15,000 users through Instagram. Then reviews mentioned slowness - and most mobile visitors left before the recipe page loaded, which took up to eleven seconds on 4G. 😳

Several causes were stacked together. Here's why AI-built apps get slow, and what fixes it: 🧠

❌ ~6 MB phone photos served at full size, even in thumbnail grids
❌ Three chart libraries and a rich text editor loaded on every page
❌ The recipe list loading every column, then filtering in the browser
❌ Separate requests per card for author, likes and saved status, and no index on user_id

✅ Resizing on upload with thumbnail, medium and large variants via a CDN with lazy loading
✅ Heavy libraries loaded only where used, and one chart library instead of three
✅ A database view returning card fields, author names, likes and saved status in one paginated query
✅ Indexes for favourites, likes and filters, plus full-text search

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find the few bottlenecks that matter and fix them without a rewrite. 🛠️

Her result: €2,600, 7 business days. The recipe page now loads in around 1.5 seconds on 4G, the list in under a second, and app store ratings recovered within two months. 🚀

👉 Is your AI-built app slow? Here are the causes and the fixes: https://launchstudio.eu/en/blog/why-is-my-ai-built-app-slow

#Performance #WebVitals #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
