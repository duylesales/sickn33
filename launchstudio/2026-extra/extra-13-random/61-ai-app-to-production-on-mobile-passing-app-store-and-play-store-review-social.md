🚨 Joost Verbruggen, a dog walker in Tilburg, built Uitlaatmaatje in Bolt as an Expo app: owners book walks, walkers share live location and photos, and payments run through Stripe. He wanted it in both app stores before the summer holidays. Apple rejected it three times in five weeks. 😳

First reviewers couldn't log in. Then there was no in-app account deletion. Then the privacy label omitted location data and crash analytics collected by an SDK Bolt had added - and Google flagged the Data safety form for the same reason. Meanwhile, a friend unpacked the Android build and found the Stripe secret key and the Google Maps key inside. Here's what passing App Store and Play Store review takes for an AI app: 🧠

❌ No demo account for reviewers
❌ "Email us to delete your account"
❌ Privacy labels that miss what SDKs collect
❌ Secret keys inside the app binary

✅ Both keys rotated, payments and map calls moved behind server-side functions
✅ A backend deletion flow removing profiles, dog records, walk photos and location history - and cancelling Stripe customers
✅ Versioned API routes so older builds keep working, plus a demo account with realistic walks
✅ Every SDK's data collection documented for accurate declarations, clear permission purpose strings - and review notes explaining why Stripe fits real-world services

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and a decade of React Native and Flutter delivery, we prepare the parts of mobile launch that AI tools skip. ⚙️

His result: €3,900, fourteen business days. Uitlaatmaatje passed review on both stores at the next submission and gained 640 dog owners and 38 walkers around Tilburg and Breda in three months. 🚀

👉 AI app to production on mobile: passing App Store and Play Store review: https://launchstudio.eu/en/blog/ai-app-to-production-on-mobile-passing-app-store-and-play-store-review

#MobileApps #AppStore #ReactNative #Expo #LaunchStudio #Manifera
