🚨 Ingrid Hoekstra coordinates volunteers for food banks around Leeuwarden. In three weekends, Firebase Studio built her Inzetrooster: volunteers pick shifts, coordinators see who's coming. Two weeks into a pilot with four locations, a volunteer who worked in IT warned her: the app's data was readable by anyone who knew the project ID. 😳

The rules were still the prototype's `if request.auth != null` - so every signed-in volunteer could read every other volunteer's phone number and address. Here's what to fix before real users arrive: 🧠

❌ Prototype Security Rules exposing personal data
❌ A Firestore database in a US multi-region
❌ An AI reminder feature callable without limits
❌ All testing done on the live database

✅ A new production project with Firestore in europe-west4, pilot data migrated
✅ Rules limiting volunteers to their own profile and their location's schedule
✅ App Check enforced, the AI feature behind auth with a daily quota, budget alerts
✅ The original project turned into staging, with deploys from GitHub

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we give you the confidence to put real people's data in your app. 🛠️

Her result: €2,450, 8 business days. Inzetrooster relaunched across eleven food bank locations, now used by around 380 volunteers, with monthly Firebase costs below €25. 🚀

👉 Building with Firebase Studio? Here's what to fix before real users: https://launchstudio.eu/en/blog/firebase-studio-app-to-production-what-to-fix-before-real-users

#FirebaseStudio #Firebase #GDPR #NonProfit #AIFounder #LaunchStudio #Manifera
