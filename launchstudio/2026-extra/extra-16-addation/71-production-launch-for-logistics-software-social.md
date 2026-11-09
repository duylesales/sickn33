🚛 Sander Bosman runs a regional delivery company for furniture and appliances in Lelystad and built Leverlijst with Bolt and Supabase: planners import webshop orders and build routes, drivers see stops and capture signatures. It worked in town. On rural routes in Flevoland, drivers lost signal, and signatures captured there sometimes never arrived. 📵

In the November peak, the planning screen took almost a minute to load. The assessment found: 🧠

❌ Every driver action requiring a live connection, with no local queue
❌ Retries after failed uploads creating duplicate deliveries
❌ A Shopify import that stopped silently at rate limits, and tracking links with sequential numbers
❌ Driver locations recorded every ten seconds, after working hours too, and never deleted

✅ An offline-capable PWA with local routes and an idempotent action queue, plus a clear pending indicator
✅ Compressed, private proof-of-delivery photos and signatures linked to shipments
✅ A background Shopify import with throttling, retries, alerts and stored order IDs, and unguessable tracking links
✅ Location limited to active routes and deleted after a short period, as agreed with his adviser and explained to drivers, plus indexed queries tested at triple volume

At **LaunchStudio**, backed by Manifera's 11+ years of building mobile, integration and high-volume systems for clients such as Vodafone and TNO, we make logistics software work without signal and through every peak. 🛠️

His result: €5,300, fourteen business days. In December, planning loaded in under two seconds and no proof of delivery was lost. 🚀

👉 Production launch for logistics software: https://launchstudio.eu/en/blog/production-launch-for-logistics-software

#Logistics #Offline #PWA #Bolt #AIFounder #LaunchStudio #Manifera
