📱 DEVICE TEST: Knipklok booking flow

                     Android  Laptop  iPhone
Time slots shown        ✅       ✅      ❌
Confirm button visible  ✅       ✅      ❌
Google sign-in          ✅       ✅      ❌ (Instagram in-app browser)
Deposit receipt opens   ✅       ✅      ❌

Sanne Bakker built Knipklok with Bolt and Supabase: customers of hair salons pick a stylist and time slot, then pay a deposit. Twelve salons joined after a pilot, and most bookings came from a link in each salon's Instagram profile. Then owners reported fewer bookings, and customers said the app "didn't work." Sanne tested on her Android phone and laptop. Everything was fine.

On an iPhone, the column turned red:
❌ Slots looked empty because the backend sent times like 2028-03-12 14:30:00, which Safari couldn't parse
❌ The "Confirm booking" button sat in a fixed footer, hidden behind the keyboard while customers typed their phone number
❌ Google sign-in failed outright in Instagram's in-app browser
❌ The deposit receipt, opened in a new tab after the payment call, got blocked as a pop-up

Turning the column green (LaunchStudio, 6 business days, €2,100):
✅ ISO timestamps with time zones from the API, and a date library instead of manual parsing
✅ The confirm button kept in the flow above the keyboard, with dynamic viewport units and 16px inputs to prevent zoom
✅ Guest booking with email and a one-time code, plus in-app browser detection offering "Open in Safari" for Google sign-in
✅ Receipts as server-generated download links
✅ Error monitoring, and a short real-device test checklist for every release

Completed bookings from iPhone users went from about 40% of attempts to above 90%, level with Android. Six weeks later, bookings across the twelve salons were up by roughly a third.

"Half my customers' customers use iPhones and come from Instagram. I had tested on neither." - Sanne Bakker

https://launchstudio.eu/en/blog/why-does-my-app-break-on-iphone-and-safari

#Safari #iPhone #MobileUX #Bolt #AIFounder #LaunchStudio #Manifera
