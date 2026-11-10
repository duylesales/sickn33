🚨 Rik Smeets built Kapperplanner with Lovable and Supabase: online booking for hair salons. To speed things up, a friend put Cloudflare in front of everything with a "Cache Everything" rule and Flexible SSL. Within days, one salon owner saw another salon's appointments - with clients' names and phone numbers. 😳

Staff also hit login loops, Mollie deposit webhooks were blocked by bot protection, and bots made fake bookings. Here's how to put Cloudflare in front of your AI-built app without breaking it: 🧠

❌ Flexible SSL causing login loops
❌ A cache rule serving one salon's dashboard to another
❌ Bot protection challenging Mollie webhooks
❌ Fake bookings from bots on public booking pages

✅ SSL set to Full (strict)
✅ Caching limited to static assets, app responses set to private, no-store, caches purged
✅ Webhook paths excluded from challenges and protected by signature verification
✅ Turnstile on the booking form, rate limits on login and booking, and an incident assessment

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make Cloudflare do both jobs it should: faster and safer. 🛠️

His result: €1,900, 5 business days. Login loops and cross-salon exposure stopped immediately, deposits processed reliably again and bot bookings fell to nearly zero. 🚀

👉 Using Cloudflare with your app? Here's how to configure it safely: https://launchstudio.eu/en/blog/cloudflare-in-front-of-your-ai-built-app

#Cloudflare #WebSecurity #Lovable #Caching #AIFounder #LaunchStudio #Manifera
