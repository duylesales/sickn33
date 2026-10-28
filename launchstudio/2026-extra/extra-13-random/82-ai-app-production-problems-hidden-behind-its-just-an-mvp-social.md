🚨 Kim Verheul rents out small electric boats in Vlaardingen and built Bootje in Lovable as "just an MVP": customers pick a boat and a slot, pay a deposit and receive a digital code for the boat lock. She planned to test it for one summer. Within three weeks, about 400 bookings came in. Then a boat was taken out by someone who hadn't booked it - using a lock code from another customer's booking. 😳

Every booking - name, phone number and lock code - was readable by any logged-in user through the API. Deposits were confirmed by the browser redirect, so some customers got codes without paying. The Mollie key sat in the frontend, there were no backups, and the database was in a US region. Here's what the "it's just an MVP" label hides: 🧠

❌ Lock codes readable by every user
❌ Codes issued before payment was confirmed
❌ A payment key in the browser
❌ No backups and data outside the EU

✅ Booking and lock-code access limited to the booker - and only valid during the booked slot
✅ Deposits confirmed by Mollie webhooks before any code is issued
✅ Key rotation, EU migration with backups and a tested restore
✅ Account consolidation and alerts - with the feature set kept exactly as small as before

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your MVP small - but never its safety. ⚙️

Her result: €2,200, eight business days. Bootje finished the summer with about 1,900 bookings and no further unauthorised boat use, and expanded to a second marina the next spring - with the same minimal features. 🚀

👉 AI app production problems hidden behind "it's just an MVP": https://launchstudio.eu/en/blog/ai-app-production-problems-hidden-behind-its-just-an-mvp

#MVP #StartupLaunch #Lovable #Rentals #LaunchStudio #Manifera
