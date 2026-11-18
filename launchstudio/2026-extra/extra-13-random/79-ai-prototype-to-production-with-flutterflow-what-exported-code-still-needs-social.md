🎬 A beautiful film set, at a gliding club

On screen, Zweefvliegclub looked finished. Members book flight slots and instructors, log flights, check aircraft availability and pay flight fees. Three gliding clubs, about 520 members. Thijmen de Lange, a gliding instructor at a club near Lelystad, built it in FlutterFlow, and wanted it in both app stores before the new season.

FlutterFlow made the app look finished. The rules behind it decided whether it actually was.

BEHIND THE SET
🎭 Firestore rules let any logged-in member read and write every collection, including other members' medical certificate expiry dates and payment records, and mark their own flights as paid
🎭 A Mollie API key, configured in a FlutterFlow API call, sitting in the app binary
🎭 An instructor-only "approve solo flight" screen, hidden in the interface, with the underlying write open to everyone
🎭 Custom code pasted from an AI chat, pulling in an outdated package with known issues
🎭 No account deletion, and no crash reporting
🎭 Designs edited both in FlutterFlow and in the exported code, overwriting each other

BUILDING THE REAL THING (LaunchStudio, 11 business days, €3,300)
🏗️ Firestore rules scoped to clubs, members and roles, with emulator tests
🏗️ Payment creation and confirmation in Cloud Functions, with Mollie webhooks
🏗️ Instructor approvals enforced on the server
🏗️ The problematic package replaced
🏗️ In-app account deletion, with backend clean-up
🏗️ Crashlytics enabled
🏗️ FlutterFlow as the single source of truth, with exports committed to Git
🏗️ Both store submissions prepared, with a staged rollout

Both apps were approved at first submission. The season started with all three clubs on the app, a fourth joined mid-season, and crash-free sessions stayed above 99.5%.

"FlutterFlow made the app look finished. The rules behind it decided whether it actually was." - Thijmen de Lange

https://launchstudio.eu/en/blog/ai-prototype-to-production-with-flutterflow-what-exported-code-still-needs

#FlutterFlow #Firebase #MobileApps #Flutter #LaunchStudio #Manifera
