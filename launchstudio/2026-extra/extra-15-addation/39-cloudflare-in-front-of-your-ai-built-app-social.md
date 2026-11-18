⚙️ Two Cloudflare settings that made an app leak

Cache rule: Cache Everything
SSL mode: Flexible

Rik Smeets built Kapperplanner with Lovable and Supabase: online booking for hair salons, with a public booking page per salon and a dashboard for staff. To speed up the public pages, a friend put Cloudflare in front of everything, with those two settings.

Within days:
• Staff members got stuck in a login loop on the dashboard
• One salon owner briefly saw another salon's appointments, with clients' names and phone numbers
• Mollie deposit webhooks failed, because bot protection challenged them
• Bots made fake bookings on several public booking pages

The corrected configuration (LaunchStudio, 5 business days, €1,900):

SSL mode: Flexible ➜ Full (strict)
That ended the login loops.

Cache rule: Cache Everything ➜ removed
Caching limited to static assets and shared assets of public booking pages. App responses sent with private, no-store headers and excluded. Edge caches purged, and the incident assessed for data exposure.

Webhook paths: challenged ➜ excluded from bot challenges, protected by signature verification

Booking form: open ➜ Turnstile, verified server-side

Login and booking endpoints: unlimited ➜ rate limited

App hostname on Vercel: proxied ➜ DNS-only, with email records checked and preserved

The result: login loops and cross-salon exposure stopped immediately, deposits processed reliably again, and bot bookings fell to nearly zero. Public pages stayed fast thanks to asset caching, and Rik documented the setup so it won't happen again.

"Cloudflare was meant to make my app faster. Configured wrongly, it made it leak. Configured properly, it does both jobs it should." - Rik Smeets

https://launchstudio.eu/en/blog/cloudflare-in-front-of-your-ai-built-app

#Cloudflare #WebSecurity #Lovable #Caching #AIFounder #LaunchStudio #Manifera
