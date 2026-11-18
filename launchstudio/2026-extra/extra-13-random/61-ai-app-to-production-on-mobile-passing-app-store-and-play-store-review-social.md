🐕 Apple, rejection #1: our reviewers couldn't log in.
Apple, rejection #2: there's no in-app account deletion.
Apple, rejection #3: your privacy label leaves out location data, and crash analytics collected by an SDK.
Google Play: your Data safety form has the same gap.

Three rejections in five weeks. Apple wasn't being difficult. It was reading the app more carefully than its founder had.

Joost Verbruggen, a dog walker in Tilburg, built Uitlaatmaatje in Bolt as an Expo app: dog owners book walks, walkers share live location during the walk and upload photos, and payments run through Stripe. The web version worked for his own clients. He wanted both app stores before the summer holidays.

And there was a fourth problem no reviewer mentioned: a friend unpacked the Android build and found the Stripe secret key and the Google Maps key inside it.

What LaunchStudio did before the next submission (14 business days, €3,900):
✓ Both keys rotated, with payment creation and map calls moved behind server-side functions
✓ A backend deletion flow that removes profiles, dog records, walk photos and location history, and cancels Stripe customers
✓ Versioned API routes, so older builds keep working
✓ A demo account seeded with realistic walks, for the reviewers
✓ Every SDK's data collection documented, for accurate privacy declarations
✓ Clear purpose strings for the location and camera permissions
✓ Submission notes explaining why Stripe is correct here: walks are real-world services

Apple: ✅ approved.
Google Play: ✅ approved.
Both at the next submission.

In its first three months on mobile, Uitlaatmaatje gained 640 dog owners and 38 walkers around Tilburg and Breda.

"I thought the rejections were Apple being difficult. They were Apple reading my app more carefully than I had." - Joost Verbruggen

https://launchstudio.eu/en/blog/ai-app-to-production-on-mobile-passing-app-store-and-play-store-review

#MobileApps #AppStore #ReactNative #Expo #LaunchStudio #Manifera
