📻 TRAFFIC REPORT: Tuincentrumgids

Normal conditions: 400 visits a day.
Breaking: a gardening programme mentions a featured nursery and links to its page. 9,000 visits in two hours.
Current status: complete standstill. The site has stopped responding, and stays down all afternoon.

Noor Vreugdenhil built Tuincentrumgids in Lovable: a directory of garden centres and nurseries across the Netherlands, with opening hours, stock categories and seasonal availability, funded by featured listings from 120 businesses.

CAUSES OF THE JAM
🚧 Every page rendered from scratch on every request, even directory pages unchanged for weeks
🚧 Eleven database queries per page
🚧 Nothing cached anywhere
🚧 Every photo served at full resolution, several megabytes per listing page
🚧 And one hidden hazard: the logged-in business dashboard was cacheable. Under edge traffic, it could have shown one business's statistics to another.

ROADWORKS COMPLETED (LaunchStudio, 1 business day, €1,800)
✓ Public directory and listing pages cached at the CDN for fifteen minutes, with background revalidation
✓ Static assets cached for a year, on fingerprinted filenames
✓ The business dashboard explicitly marked private and no-store
✓ Images transformed to display size in modern formats and cached at the edge: listing pages from 4.2 MB to 310 KB
✓ The seasonal availability summary on a short-lived cache, with background refresh
✓ Cache purging when a business edits its own listing, so owners see their changes right away

LATEST CONDITIONS
Requests reaching the application: down 94% at the same traffic.
April: a second programme covers the same topic. Same peak, served entirely from the edge, no change in response time.
Hosting bill: down €70 a month, as a side effect.

"I assumed I needed a bigger server. What I needed was to stop rebuilding the same page nine thousand times, and to stop sending a four-megabyte photograph to every phone." - Noor Vreugdenhil

https://launchstudio.eu/en/blog/lovable-hosting-caching-and-pages-that-stay-fast-under-load

#Caching #CDN #WebPerformance #Lovable #LaunchStudio #Manifera
