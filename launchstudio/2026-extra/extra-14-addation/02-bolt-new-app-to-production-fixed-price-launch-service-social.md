🚨 Maarten Oosterhuis runs a heat pump installation business in Zwolle. He built Offertewerk in Bolt.new so installers could create quotes on a tablet at the customer's kitchen table. In the Bolt preview: perfect. On Netlify: three things broke at once. 😳

Bolt runs your app inside a browser sandbox that forgives what real servers don't. Here's what broke when Offertewerk left the browser tab: 🧠

❌ Build failed on two imports that differed only in letter case
❌ Every page except the homepage returned 404 on refresh
❌ PDF generation failed silently - the API key only existed in his Bolt session
❌ Installers could see each other's quotes

✅ Import paths fixed, plus a lint rule to catch case mismatches
✅ SPA rewrites configured on Netlify
✅ PDF calls moved into a serverless function with the key as an environment variable
✅ Row Level Security per installer and a staging site for Bolt changes

At **LaunchStudio**, powered by Manifera's 11+ years of engineering, we take Bolt apps to production at a fixed price - without swapping your stack. ⚙️

His result: €1,850, live in eight business days. Four installers created ~620 quotes from the field that heating season, and nearly every quote now goes out the same day. 🚀

👉 Why Bolt apps break outside Bolt, and how to ship yours: https://launchstudio.eu/en/blog/bolt-new-app-to-production-fixed-price-launch-service

#BoltNew #Netlify #AIApp #Deployment #LaunchStudio #Manifera
