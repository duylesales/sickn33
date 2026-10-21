🚨 Chiara Rossi, a music teacher and choir director in Dordrecht, built Koorplanner in Firebase Studio: amateur choirs schedule rehearsals, share sheet music and recordings, track attendance and collect fees. Within a season, 140 choirs and about 4,000 singers. Then in one week her Firebase bill tripled — and a choir member in IT showed her he could read every choir's member list. 😳

After test mode expired, the rules had been set to "authenticated users can read and write everything". Names, phone numbers and addresses were exposed across choirs, licensed sheet music was downloadable by anyone, members could mark their own fees as paid, and the attendance screen listened in real time to the entire collection. Here's how to take a Firebase Studio prototype to production with rules that hold: 🧠

❌ "Authenticated" treated as "authorised for everything"
❌ Open storage for licensed files
❌ Payment status written by the client
❌ Collection-wide listeners running up the bill

✅ Firestore and Storage rules rewritten deny-by-default, scoped to choir membership and roles — with 48 emulator tests in CI
✅ Fee status updated only by a Cloud Function on verified payment webhooks
✅ App Check enabled and the listener replaced by a scoped, paginated query
✅ Budget alerts and scheduled backups with a test restore

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure the rules behind your public config are a real lock on the door. ⚙️

Her result: €1,500, six business days. Cross-choir access closed the day the rules deployed, the Firebase bill fell about 70% from its peak, and Koorplanner grew to 230 choirs the next season. 🚀

👉 Firebase Studio AI prototype to production: security rules that hold: https://launchstudio.eu/en/blog/firebase-studio-ai-prototype-to-production-security-rules-that-hold

#Firebase #SecurityRules #Firestore #AppSecurity #LaunchStudio #Manifera
