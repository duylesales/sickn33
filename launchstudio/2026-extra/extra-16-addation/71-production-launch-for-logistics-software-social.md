🚚 ONE ROUTE THROUGH THE POLDER, stop by stop (before)

STOP 1, Lelystad town: 📶📶📶 Signature captured. Uploaded.
STOP 2, a rural road in Flevoland: 📶 Signature captured. Upload failed. Never arrives.
STOP 3, further out: ✗ No signal. Driver retries. The delivery is now recorded twice.
BACK AT THE OFFICE, November peak: the planning screen takes almost a minute to load.

Sander Bosman runs a regional delivery company in Lelystad for furniture and large appliances. He built Leverlijst with Bolt and Supabase: planners import webshop orders and build routes, and drivers use a web app to see their stops and capture signatures. In town, it worked well. In the polder, it didn't.

What else the assessment found:
• Every driver action needed a live connection, with no local queue
• A scheduled Shopify import that stopped silently when it hit rate limits
• Tracking links with sequential numbers, so recipients could view other shipments
• Drivers' locations recorded every ten seconds, even after working hours, and never deleted

THE NEW ROUTE (LaunchStudio, Launch & Grow, 14 business days, €5,300, plus €49/month)
✓ An offline-capable PWA for drivers: routes stored locally, an action queue that syncs idempotently when coverage returns, and a clear indicator of what's still pending
✓ Signatures and photos compressed, stored privately and linked to shipments
✓ The Shopify import as a background job, with throttling, retries, alerts and recorded order IDs against duplicates
✓ Unguessable tracking links that show only the recipient's own delivery window
✓ Location tracking only on active routes, used for arrival estimates and deleted after a short period, agreed with Sander's adviser and explained to drivers
✓ Planning queries indexed and paginated, tested at three times normal volume

THE DECEMBER PEAK
Planning screen: under two seconds. Proof of delivery lost on rural routes: none. Duplicate deliveries: gone. And drivers said the clear rules on location tracking made them more comfortable.

"The polder doesn't care about mobile coverage. Now the app doesn't either, and our drivers know exactly when we can see where they are." - Sander Bosman

https://launchstudio.eu/en/blog/production-launch-for-logistics-software

#Logistics #Offline #PWA #Bolt #AIFounder #LaunchStudio #Manifera
