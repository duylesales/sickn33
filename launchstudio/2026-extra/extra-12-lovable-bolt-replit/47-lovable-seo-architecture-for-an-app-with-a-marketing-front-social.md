🚨 Jasmijn Kolthof's Voorraadslim manages stock for 130 independent retailers and webshops, found almost entirely through a Facebook group. She'd written eleven articles in a year. None appeared in search. Her home page didn't even rank for her own product name. 😳

The server sent every visitor the same empty container and a script; browsers filled in the words. Meanwhile, four logged-in app pages were indexed - one titled "Loading...". Here's how to architect an app with a marketing front: 🧠

❌ Public pages rendered only in the browser
❌ Internal links as JavaScript click handlers, invisible to crawlers
❌ 40 app routes indexable, plus three preview deployments indexed as full duplicates
❌ The same content at four URL variations - and no pricing page at all

✅ Public pages statically generated, so the server returns complete HTML
✅ Real anchor links, the app moved under /app with a noindex directive, and protected previews
✅ One canonical URL with permanent redirects, a sitemap from real routes, and article structured data
✅ Index cleanup in search console, plus a pricing page with real prices and an about page

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we check what a search engine actually sees on your home page - sometimes it's nothing. 🔎

Her result: four business days and €3,500 later, nine of the eleven articles were indexed within eight weeks and organic visits went from 40 to 610 a month. Two articles now bring more trial signups than the Facebook group. 🚀

👉 SEO architecture for an app with a marketing front: https://launchstudio.eu/en/blog/lovable-seo-architecture-for-an-app-with-a-marketing-front

#SEO #Lovable #TechnicalSEO #SaaS #LaunchStudio #Manifera
