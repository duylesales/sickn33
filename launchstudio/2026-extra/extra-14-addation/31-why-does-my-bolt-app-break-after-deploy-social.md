🚨 Emma Lambrecht, a museum educator in Bruges, built Zaalgids with Bolt: an audio tour visitors open by scanning a QR code next to each artwork, with text, audio and a quiz for children. In Bolt's preview it was flawless. On Netlify, it broke three ways on the very first test day. 😳

Every QR code pointed to a page that didn't exist, according to the server. In the preview, it had always existed. Here's what went wrong: 🧠

❌ Every room link from a QR code returned 404 - no SPA rewrite rule on the host
❌ Audio files didn't load: their storage URL lived only in her Bolt session
❌ Quiz scores failed to save - the production domain was missing from Supabase's allowed URLs
❌ The same missing URL broke the staff login

✅ Netlify rewrites so every route is served by index.html
✅ Environment variables configured per environment
✅ Production and preview domains added to Supabase Auth settings
✅ Audio on a CDN-backed bucket with caching for weak museum wifi, offline caching for tour text, and automatic deploy checks on the QR routes

At **LaunchStudio**, backed by Manifera's 11+ years of deployment work on Netlify, Vercel, AWS and Azure, we fix the gap between "works in the preview" and "works for visitors". 🛠️

💡 Her result: €1,600, six business days. Zaalgids went live for the summer exhibition, and visitors started around 9,600 tours in twelve weeks - with audio loading even in the basement galleries. 🚀

👉 Bolt app broken after deploy? Here are the seven causes and how to fix each one: https://launchstudio.eu/en/blog/why-does-my-bolt-app-break-after-deploy

#Bolt #Netlify #Vite #Deployment #LaunchStudio #Manifera
