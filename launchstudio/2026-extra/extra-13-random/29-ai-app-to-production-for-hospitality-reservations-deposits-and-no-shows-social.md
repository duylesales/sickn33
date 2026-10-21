🚨 Evi Janssens, a restaurant manager in Maastricht, built Tafelgarant in Bolt: guests book online, pay a €10-per-person deposit via iDEAL or card, get reminders and can cancel free up to 24 hours ahead. Nine restaurants in Maastricht and Heerlen, about 2,500 covers a month. Then came carnival weekend — double-booked tables and furious guests holding payment receipts. 😳

Deposits were confirmed when the browser returned from Mollie, so guests who paid in their banking app stayed "pending" and lost their tables. The 24-hour deadline was calculated in UTC, refusing cancellations that were still in time. Refunds were manual, capacity was a fixed count per half hour, two parties grabbed the last large table at once, and allergy notes were visible to staff at all nine restaurants. Here's what a hospitality AI app needs before production: 🧠

❌ Payments confirmed by the browser redirect
❌ Cancellation deadlines in UTC instead of local time
❌ Slot counts that ignore table sizes and races
❌ Guest health data shared across venues

✅ Deposit confirmation via verified Mollie webhooks, with carnival bookings reconciled
✅ Cancellation deadlines in Europe/Amsterdam time with automatic refunds
✅ A table-based capacity model enforced in the database, with sitting duration by party size
✅ Data separated per restaurant, allergy notes limited to that venue's floor and kitchen, and reminders via an authenticated email and SMS provider

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure the table is there when your guest arrives. ⚙️

Her result: €2,950, ten business days. Zero double bookings in the next two months, no-shows under 2% of covers, and four more restaurants joined before terrace season. 🚀

👉 AI app to production for hospitality: reservations, deposits and no-shows: https://launchstudio.eu/en/blog/ai-app-to-production-for-hospitality-reservations-deposits-and-no-shows

#Hospitality #Restaurants #iDEAL #Bolt #LaunchStudio #Manifera
