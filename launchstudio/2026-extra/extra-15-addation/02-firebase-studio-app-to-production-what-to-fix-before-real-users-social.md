One line of code:

`if request.auth != null`

It reads like security. It means: "anyone who is signed in can read everything." 🔓

Ingrid Hoekstra coordinates volunteers for a network of food banks around Leeuwarden. Tired of spreadsheets, she used Firebase Studio to build Inzetrooster in three weekends: volunteers pick shifts, coordinators see who's coming, and each location manages its own schedule.

Two weeks into a pilot with four locations, a volunteer who worked in IT warned her. The app's Security Rules were still that prototype line. Every signed-in volunteer could read every other volunteer's phone number and address.

The same review found three more things hiding behind the clean interface:
• Firestore created in a US multi-region
• An AI feature that drafted shift reminders, callable without any limit
• All testing done on the live database

What LaunchStudio replaced that one line with (8 business days, €2,450):
🇪🇺 A new production project with Firestore in europe-west4, pilot data migrated
🔐 Rules limiting volunteers to their own profile and their location's schedule, with coordinators scoped by a custom claim
🛡️ App Check enforced, the AI feature moved behind authentication with a daily quota, and budget alerts set
🧪 The original project turned into staging, with deploys from GitHub

Today: eleven food bank locations, around 380 volunteers, monthly Firebase costs below €25. Ingrid still builds in Firebase Studio, and tests on staging first.

"Firebase Studio gave me the app. LaunchStudio gave me the confidence to put real people's addresses in it." - Ingrid Hoekstra

Check your own rules before real users arrive: https://launchstudio.eu/en/blog/firebase-studio-app-to-production-what-to-fix-before-real-users

#FirebaseStudio #Firebase #GDPR #NonProfit #AIFounder #LaunchStudio #Manifera
