🚨 Noor El Amrani built Marktkraam with Lovable and Supabase: a PWA that about 180 market traders use on their phones to record sales, track stock and see daily takings. A bug calculated VAT wrongly on some items. Noor fixed it and deployed within the hour. Five days later, traders still reported wrong totals. 😳

Some traders ran the new version, others the old one - and the old one kept writing incorrect VAT into the database. Here's why users still see the old version after a deploy: 🧠

❌ A service worker caching index.html cache-first and never checking for updates
❌ A Cloudflare "cache everything" rule caching HTML for four hours
❌ The same one-week cache header on every file
❌ VAT calculated on the client, so outdated apps wrote wrong totals

✅ Workbox with update checks on launch and a "New version available" reload button
✅ HTML revalidated on every request, hashed assets cached for a year, HTML excluded in Cloudflare
✅ A version check when the app regains focus, and the version shown in settings
✅ VAT calculated on the server, with affected records recalculated

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure your fixes actually reach your users. 🛠️

The result: €1,800, 5 business days. The next release reached over 95% of active traders within a day, without anyone clearing a cache. 🚀

👉 Deployed a fix nobody can see? Here's how caching works: https://launchstudio.eu/en/blog/why-do-users-still-see-the-old-version-after-a-deploy

#PWA #Caching #ServiceWorker #Cloudflare #AIFounder #LaunchStudio #Manifera
