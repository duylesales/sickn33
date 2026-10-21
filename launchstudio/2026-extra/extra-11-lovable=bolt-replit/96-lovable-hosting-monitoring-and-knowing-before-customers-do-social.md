🚨 Bram Kooistra's Sleutelkluis sends door codes for about 400 holiday rentals around Zandvoort and Haarlem. Guests get their code by email the day before arrival. For nine days, not one was delivered — and the app recorded every email as sent. 😳

Nothing was down. Nothing errored. Guests were standing outside locked houses. Here's what "the site is up" doesn't tell you: 🧠

❌ No monitoring of any kind
❌ Email authentication records that no longer met the provider's tightened rules
❌ "Sent" treated as "delivered"
❌ Property managers absorbing the problem by phone, assuming guests weren't checking their inbox

✅ Error tracking across frontend and server — which immediately surfaced two more failures
✅ Email authentication fixed and tested against four major providers, with delivery status fed back per booking
✅ Uptime checks against a page that hits the database, plus run logging and a 06:00 alert for the nightly code job
✅ A business-level check: codes sent versus arrivals expected, routed to Bram's phone

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set up monitoring so you know before your customers do. 🔔

His result: six business days and €2,900 later, the business-level check has fired twice — a provider outage and a stopped booking import — both caught within hours instead of days. Two property managers cited the change when extending their contracts. 🚀

👉 Monitoring — knowing before customers do: https://launchstudio.eu/en/blog/lovable-hosting-monitoring-and-knowing-before-customers-do

#Monitoring #Lovable #EmailDeliverability #Hospitality #LaunchStudio #Manifera
