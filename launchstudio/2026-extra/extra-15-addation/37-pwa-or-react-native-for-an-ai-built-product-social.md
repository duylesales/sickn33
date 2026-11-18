Two quotes for "a real app." 🐕

QUOTE A
Native iOS and Android apps
Price: over €40,000

QUOTE B
Fix the web app, make it installable, wrap it natively only where needed
Price: €4,600, 13 business days

Sophie Kramer runs a dog walking business in Utrecht. She built Uitlaatplanner with Lovable and Supabase: owners book walks, walkers check in with a photo at pick-up and drop-off, and owners get updates. Several customers asked for "a real app," and Quote A arrived.

Before signing, she asked LaunchStudio for a second opinion. What she actually needed:
• Check-ins with photos and location
• Push notifications for owners
• Offline resilience for walkers in parks with poor reception
• No app store discovery yet: every owner was an existing customer invited by email

What was actually broken: a cramped mobile layout, check-ins failing without signal, and uncompressed photo uploads.

What Quote B delivered:
✓ A better mobile interface, plus a PWA with manifest and icons
✓ Offline check-ins queued in IndexedDB, and compressed photo uploads
✓ Push notifications for installed PWAs, email as fallback, and an install guide for customers
✓ For walkers only: the PWA wrapped with Capacitor, with native push and camera, via TestFlight and Google Play internal testing
✓ Backend preparation: secure tokens, API versioning, push token management

The result: owners adopted the installed PWA quickly, walkers use the Capacitor app daily, and missed check-ins dropped to near zero. The full native decision waits until expansion to other cities.

"I almost spent forty thousand euros on an app my customers didn't need. What they needed was the web app working properly on their phones." - Sophie Kramer

PWA or React Native? https://launchstudio.eu/en/blog/pwa-or-react-native-for-an-ai-built-product

#PWA #ReactNative #Capacitor #MobileApps #AIFounder #LaunchStudio #Manifera
