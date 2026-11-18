🚚 How a shipper's IT manager tested a tracking link, in three steps

STEP 1: Open the tracking link for one delivery.
STEP 2: Change the number in the URL.
STEP 3: Read another recipient's name, full address, delivery contents and sender.

Erik Janssen works at his family's regional transport company in Venlo, around 60 trucks delivering for wholesalers and webshops. He built Leverstatus with Cursor and Supabase: shipments imported from the planning system, drivers marking deliveries in a web app, recipients receiving tracking links. Shippers loved it, and the company planned to sell it as a premium service. Then, before launch, came those three steps. And more:
• Proof of delivery photos in a public bucket
• A driver app that needed a connection, so drivers in industrial areas with weak signal marked deliveries later, from memory
• Truck positions recorded every five seconds, forever, even when drivers took vans home at night
• A location table of tens of millions of rows, slowing the dashboard

The same three steps, after LaunchStudio (17 business days, €6,900):
STEP 1: Open a tracking link with a random token. See status, an ETA window and a partial address.
STEP 2: Change the token. Nothing. Links expire two weeks after delivery, and the endpoint is rate-limited.
STEP 3: Want full details? Log in to a shipper portal, where Row Level Security shows only your own shipments.

Plus:
✓ Proof of delivery in private storage with signed links
✓ An offline-capable PWA for drivers, with signatures, photos and exception codes
✓ Location collected only on active routes during working hours, detailed tracks kept 30 days then aggregated, live positions visible to planners only
✓ The location table partitioned by day, and the approach agreed with drivers and the works council

The premium service launched with eight shippers and grew to 23 in six months. Proof of delivery completeness is near 100%, the dashboard loads in under a second, and the IT manager who found the hole now recommends the service.

"We built tracking so customers could see their deliveries. For a while, anyone could see everyone's. Fixing that turned a risk into a product we can sell." - Erik Janssen

https://launchstudio.eu/en/blog/logistics-tracking-dashboard-for-transport-companies

#Logistics #Transport #DeliveryTracking #Privacy #AIFounder #LaunchStudio #Manifera
