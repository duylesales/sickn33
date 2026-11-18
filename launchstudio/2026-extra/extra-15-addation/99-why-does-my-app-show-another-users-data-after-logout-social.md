🧠 Five things an app forgot to forget

Daan Peters built Ledenloket with Lovable and Supabase: a check-in and account app for fitness studios. Members log in on a shared tablet at reception to check in, view their membership and book classes, and use the same app on their own phones. Nine studios.

Then a member complained. After she logged in on the tablet, she saw the previous member's name, membership type and upcoming bookings for several seconds. Once, after tapping quickly, she booked a class on the previous member's account.

The database was locked down properly. The problem was everything the app remembered after people left.

1. Cached query results
React Query kept every result under keys without a user ID.

2. Local storage
The profile and selected studio stayed stored.

3. A global store
It held the member ID used for bookings until the new profile loaded.

4. The CDN
A Cloudflare rule cached "today's classes," including a personalised "booked" flag, so members on their phones sometimes saw someone else's bookings marked as their own.

5. The logout itself
It only called Supabase's sign-out. Nothing else was cleared.

Teaching the app to forget (LaunchStudio, 4 business days, €1,700):
✓ No CDN caching on authenticated routes, and private, no-store headers on every personalised response
✓ One central logout that clears the query cache, resets all stores, removes local storage keys, closes realtime channels and reloads the app
✓ Query keys that include the member ID
✓ Bookings that take the member ID from the server session, not from client state
✓ Automatic logout on kiosk tablets after 60 seconds of inactivity
✓ Help assessing the incident, documenting it as a data breach under the GDPR and informing the affected members

Shared-device tests across every key screen now show no previous-member data. No further complaints, and studios now mention the automatic kiosk logout when they recommend Ledenloket.

"My database was locked down properly. The leak was in everything my app remembered after people left." - Daan Peters

https://launchstudio.eu/en/blog/why-does-my-app-show-another-users-data-after-logout

#Privacy #SessionSecurity #GDPR #FitnessTech #AIFounder #LaunchStudio #Manifera
