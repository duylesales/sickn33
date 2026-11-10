🚨 Daan Peters built Ledenloket with Lovable and Supabase: members of nine fitness studios check in on a shared tablet at reception, view their membership and book classes. Then a member complained: after logging in, she saw the previous member's name, membership and bookings for several seconds. 😳

Once, tapping quickly, she even booked a class on the previous member's account. The database was locked down. The leak was in everything the app remembered. Here's why apps show another user's data after logout: 🧠

❌ Logout that only called Supabase's sign-out
❌ React Query results cached under keys without a user ID
❌ Profile and studio in local storage, and the member ID for bookings in a global store
❌ A Cloudflare rule caching "today's classes" with a personalised "booked" flag

✅ CDN caching removed for authenticated routes, with private, no-store headers
✅ One central logout clearing caches, stores, local storage and realtime, then reloading
✅ Query keys including the member ID, and bookings using the member ID from the server session
✅ Automatic kiosk logout after 60 seconds, and the incident documented as a GDPR breach

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we clean up what your app remembers after people leave. 🛠️

The result: €1,700, 4 business days. Shared-device tests show no previous-member data, no further complaints came in, and the kiosk auto-logout became a feature studios recommend. 🚀

👉 Does your app leak data between users on shared devices? Here's how to fix it: https://launchstudio.eu/en/blog/why-does-my-app-show-another-users-data-after-logout

#Privacy #SessionSecurity #GDPR #FitnessTech #AIFounder #LaunchStudio #Manifera
