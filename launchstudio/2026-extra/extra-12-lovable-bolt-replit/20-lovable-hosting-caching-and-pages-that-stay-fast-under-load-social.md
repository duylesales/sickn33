🚨 Noor Vreugdenhil's Tuincentrumgids lists garden centres and nurseries across the Netherlands, funded by 120 featured businesses. A gardening programme linked to one of her nurseries. Traffic went from 400 visits a day to 9,000 in two hours — and the site stayed down all afternoon. 😳

Every page was rebuilt from scratch for every visitor, with eleven database queries and multi-megabyte photos. Here's how caching keeps pages fast under load: 🧠

❌ Pages unchanged for weeks, rendered fresh on every request
❌ Full-resolution photos sent to every phone — 4.2 MB per listing page
❌ An authenticated dashboard that was cacheable — one edge hit away from leaking stats between businesses
❌ An expensive aggregation recomputed for every visitor

✅ Public pages cached at the CDN for 15 minutes with background revalidation
✅ Year-long lifetimes for fingerprinted static assets
✅ The business dashboard explicitly marked private and no-store
✅ Images resized to display size in modern formats (310 KB per page), plus purging when owners edit their listing

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we stop your app rebuilding the same page nine thousand times. ⚡

Her result: one business day and €1,800 later, requests reaching the application fell 94% at the same traffic. When a second programme covered the topic in April, the peak was served entirely from the edge — and her hosting bill dropped €70 a month. 🚀

👉 Caching and pages that stay fast under load: https://launchstudio.eu/en/blog/lovable-hosting-caching-and-pages-that-stay-fast-under-load

#Caching #CDN #WebPerformance #Lovable #LaunchStudio #Manifera
