🚨 Thijmen de Lange, a gliding instructor near Lelystad, built Zweefvliegclub in FlutterFlow: members book flight slots and instructors, log flights, check aircraft availability and pay flight fees. Three clubs, about 520 members — and Thijmen wanted it in both app stores before the new season. 😳

Firestore rules let any logged-in member read and write every collection — including others' medical certificate dates and payments — and mark their own flights as paid. A Mollie API key was baked into the app binary. The instructor-only "approve solo flight" screen was hidden, but the write behind it was open to all. AI-pasted custom code added an outdated package, there was no account deletion or crash reporting, and edits in FlutterFlow and exported code overwrote each other. Here's what exported FlutterFlow code still needs before production: 🧠

❌ Firestore rules that allow everything to everyone
❌ A payment key inside the app
❌ Role restrictions only in the interface
❌ Two sources of truth for the code

✅ Firestore rules scoped to clubs, members and roles, with emulator tests
✅ Payment creation and confirmation in Cloud Functions with Mollie webhooks, and instructor approvals enforced server-side
✅ The problematic package replaced, in-app account deletion with backend clean-up, Crashlytics enabled
✅ FlutterFlow as the single source of truth with exports committed to Git — and both store submissions prepared with staged rollout

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and a decade of Flutter delivery, we make sure the rules behind a finished-looking app are finished too. ⚙️

His result: €3,300, eleven business days. Both apps were approved at first submission, a fourth club joined mid-season, and crash-free sessions stayed above 99.5%. 🚀

👉 AI prototype to production with FlutterFlow: what exported code still needs: https://launchstudio.eu/en/blog/ai-prototype-to-production-with-flutterflow-what-exported-code-still-needs

#FlutterFlow #Firebase #MobileApps #Flutter #LaunchStudio #Manifera
