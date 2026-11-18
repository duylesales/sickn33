🔔 Afhaalklaar
"Your order is ready to collect!"

Delivered to: Android users who'd used that device last.
Not delivered to: most iPhone users. Or anyone after the keys changed. Or anyone after the push handler disappeared.

Lars Visser built Afhaalklaar with Lovable and Supabase: a PWA where customers of bakeries and delis order ahead and get a notification when their order is ready. Eleven shops used it, and the shop owners' pitch was simple: no more queues.

But customers kept waiting at the counter, or arriving far too late, saying they never got the message. On Lars's Android phone, everything worked. What the investigation found:
• iPhone users, about 60% of customers, mostly ordered from Safari without adding the app to their home screen, so web push could never reach them
• The subscription was one field on the user profile, so people with a laptop and a phone only got notifications on whichever device they'd used last
• A prompt had regenerated the VAPID keys, silently breaking every older subscription, and the sending function ignored the errors
• A later prompt had replaced the service worker with a caching-only version that had no push handler

The fix (LaunchStudio, 6 business days, €2,000):
✓ Stable VAPID keys in server secrets, and a push handler in a Workbox-based service worker
✓ Subscriptions in a table with one row per device, refreshed on every app open and removed on 404 or 410 responses
✓ Every send logged with its result
✓ A choice at checkout between push and SMS, with iPhone users who haven't installed the app getting a short guide and SMS by default, through a Dutch SMS provider
✓ A simple dashboard showing delivery rates per channel

More than 95% of "order ready" messages now arrive, by push or SMS. Queues shortened within weeks, and orders collected within 15 minutes of being ready rose from about half to over 80%.

"My notification feature worked perfectly, on my phone. For most of my customers' customers, it didn't exist." - Lars Visser

https://launchstudio.eu/en/blog/why-are-my-push-notifications-not-arriving

#PushNotifications #PWA #iOS #FoodTech #AIFounder #LaunchStudio #Manifera
