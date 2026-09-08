🚨 Nienke Bakker's product said "Connected" on every one of eleven physiotherapy practices' calendars. It had been silently broken since March. 😳

A failed token refresh usually just gets logged — and logged is the same as invisible to the customer relying on it: 🧠

❌ One practice manager changed her Google password in March, the refresh failed, and nothing told anyone — no flag, no email, just "Connected" still showing
❌ Eleven practices were affected, three of them for over two months, before a customer reported double-bookings
❌ Refresh tokens were stored unencrypted — a database copy would have handed over calendar access to 40 practices
❌ The integration requested full read-write access to every calendar, when a narrower "events this app created" scope would have covered it — and also triggered stricter platform verification

✅ Encrypt tokens at rest with a key held outside the database, and never let them appear in logs
✅ Handle refresh centrally with protection against concurrent refresh, which is where tokens quietly get invalidated
✅ Mark broken connections visibly in the product and email the account owner with a one-click reconnect
✅ Request the narrowest scope the feature actually needs, and ask for it incrementally rather than all at signup

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build integrations that survive revocation, expiry, and the provider's review process. 🔐

Her result: connection health now shown in-product with failure alerts, tokens encrypted, and narrowed scopes that also lifted the stricter verification requirement. 🚀

👉 See what your OAuth connections are quietly holding: https://launchstudio.eu/en/blog/connecting-to-a-customers-other-tools-the-oauth-decisions

#OAuth #SaaS #API #IndieHacker #LaunchStudio #Manifera
