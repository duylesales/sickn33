🎭 CARNIVAL WEEKEND IN MAASTRICHT: a reservation tool's diary

Evi Janssens, a restaurant manager in Maastricht, built Tafelgarant in Bolt for her own restaurant, then offered it to others: guests book online, pay a €10 per-person deposit via iDEAL or card, get reminders, and can cancel for free up to 24 hours ahead. Nine restaurants in Maastricht and Heerlen, around 2,500 covers a month.

Then came carnival weekend, and everything showed at once.

THE DEPOSITS
Guests paid in their banking app and never came back to the browser. Their bookings stayed "pending," got released to others, and tables were double-booked for guests holding payment receipts.

THE CANCELLATIONS
The 24-hour deadline was calculated in UTC. Guests cancelling at 19:30 for a 20:00 dinner the next evening, still inside the free window, were refused.

THE REFUNDS
All by hand.

THE TABLES
Capacity was a fixed count per half hour, ignoring table sizes. Two parties booked the last large table at the same time.

THE ALLERGY NOTES
Visible through the API to every staff account, at all nine restaurants.

After carnival (LaunchStudio, 10 business days, €2,950):
✓ Deposits confirmed by verified Mollie webhooks, and the carnival bookings reconciled
✓ Cancellation deadlines in Europe/Amsterdam time, with automatic refunds
✓ A table-based capacity model enforced in the database, including sitting duration by party size
✓ Data separated per restaurant
✓ Allergy notes visible only to that venue's floor staff and kitchen
✓ Reminders through a transactional email and SMS provider, with authenticated sending

The next two months: no double bookings. No-shows at participating restaurants under 2% of covers. And four more restaurants joined before the summer terrace season.

"Our guests don't care how the booking works. They care that the table is there when they arrive. Carnival showed me it wasn't, often enough to matter." - Evi Janssens

https://launchstudio.eu/en/blog/ai-app-to-production-for-hospitality-reservations-deposits-and-no-shows

#Hospitality #Restaurants #iDEAL #Bolt #LaunchStudio #Manifera
