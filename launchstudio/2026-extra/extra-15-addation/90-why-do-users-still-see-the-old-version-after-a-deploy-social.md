🧅 Three layers of cache between a fix and the people who needed it

Noor El Amrani built Marktkraam with Lovable and Supabase: a PWA market traders use on their phones to record sales, track stock and see daily takings. About 180 traders across several weekly markets, most with it installed on their home screen.

A bug calculated VAT wrongly on some items. Noor fixed it with a prompt, deployed within the hour and announced the fix. Five days later, traders were still reporting wrong totals.

Peel back the layers:

LAYER 1: The service worker
Generated in an earlier prompt, it cached index.html cache-first and never checked for updates. Installed apps kept running the old code.

LAYER 2: Cloudflare
A "cache everything" rule cached HTML for four hours.

LAYER 3: The server
The same one-week cache header for every file.

AND IN THE CENTRE
Some traders ran the new version, some the old one. Shared reports showed inconsistent VAT, and the old version kept writing wrong values to the database.

The fix, layer by layer (LaunchStudio, 5 business days, €1,800):
✓ A Workbox setup that checks for updates on launch and shows "New version available" with a reload button
✓ HTML revalidated on every request, hashed assets cached for a year
✓ The Cloudflare rule now excludes HTML
✓ A version check whenever the app regains focus
✓ VAT calculated on the server, so even an outdated client can't write wrong totals, and affected records recalculated
✓ The current version number shown in settings

The next release reached over 95% of active traders within a day, without anyone clearing a cache. Shared reports have been consistent since.

"I kept telling traders the fix was live. On their phones, it wasn't. Now I can see exactly which version everyone runs." - Noor El Amrani

https://launchstudio.eu/en/blog/why-do-users-still-see-the-old-version-after-a-deploy

#PWA #Caching #ServiceWorker #Cloudflare #AIFounder #LaunchStudio #Manifera
