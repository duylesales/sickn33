🏷️ LABEL: "Just an MVP. Just a test."

What the label protected: nobody.

Kim Verheul rents out small electric boats in Vlaardingen and built Bootje in Lovable as "just an MVP": customers pick a boat and a time slot, pay a deposit, and get a digital key code for the boat lock. The plan was to test it for one summer before investing more. Within three weeks, around 400 bookings had come in.

"Just a test" had very real consequences:
• Every booking, with the customer's name, phone number and the boat's lock code, was readable by any logged-in user through the API
• Deposits were confirmed by the browser redirect, so some customers got lock codes without paying
• The Mollie key was in the frontend
• There were no backups, and the database sat in a US region

Then a boat was taken out by someone who hadn't booked it, using a lock code from another customer's booking. That's when Kim realised the MVP label hadn't protected anyone.

The minimum safe standard (LaunchStudio, 8 business days, €2,200):
✓ Booking and lock-code access limited to the booker, and codes valid only during the booked slot
✓ Deposits confirmed by Mollie webhooks before any code is issued
✓ The key rotated
✓ EU migration, with backups and a tested restore
✓ Accounts consolidated, and alerts set up
✓ The feature set? Exactly as small as before

Bootje finished the summer with about 1,900 bookings, and no more unauthorised boat use. The next spring, Kim expanded to a second marina, with the same minimal features.

The new label: "Small MVP. Safe for real customers."

"I kept the MVP small, which was right. I also kept the safety small, which wasn't." - Kim Verheul

https://launchstudio.eu/en/blog/ai-app-production-problems-hidden-behind-its-just-an-mvp

#MVP #StartupLaunch #Lovable #Rentals #LaunchStudio #Manifera
