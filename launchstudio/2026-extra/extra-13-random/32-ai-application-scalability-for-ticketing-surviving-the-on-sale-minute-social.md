🚨 Kevin Oosterhuis, a sound engineer and promoter in Amsterdam Noord, built Zaalkaart on Replit: ticketing for small music venues and theatres, with Mollie payments and QR tickets. Eighteen venues, events of 150–600 people. Then a well-known Dutch band announced an intimate show in a 450-seat room - and 6,000 people tried to buy at 10:00. 😳

The event page hit the database for every visitor and slowed to a crawl. Availability was checked and decremented in separate steps, so 38 seats were sold twice. Buyers who paid in their banking app but never returned got no tickets. There were no checkout holds, and a handful of accounts bought 40 tickets each. Here's what AI application scalability means for ticketing: 🧠

❌ Inventory checked in code, not enforced in the database
❌ No holds while buyers pay
❌ Payments confirmed by the browser
❌ Uncached event pages and no bot limits

✅ Every seat a row with a unique hold/order constraint
✅ 10-minute holds with automatic release and a late-payment rule
✅ Mollie webhooks through a verified, idempotent queue
✅ Cached event pages, a waiting room for high-demand events, per-account and per-card limits - and a load test with 10,000 simulated buyers

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build for the one minute when your best day and worst day are the same. ⚙️

His result: €4,800, fourteen business days. The venue's next show - 450 seats, ~7,500 buyers in the first minute - sold out in four minutes with no overselling, no missing tickets and no account buying more than four. Nine more venues have joined since. 🚀

👉 AI application scalability for ticketing: surviving the on-sale minute: https://launchstudio.eu/en/blog/ai-application-scalability-for-ticketing-surviving-the-on-sale-minute

#Ticketing #Scalability #Replit #LiveMusic #LaunchStudio #Manifera
