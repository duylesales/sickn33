🎶 Imagine a choir hall where the front door has a lock, but the lock says: "Anyone who has ever been inside may enter every room."

That was Koorplanner's security, after Firebase's test mode expired.

Chiara Rossi, a music teacher and choir director in Dordrecht, built Koorplanner in Firebase Studio: amateur choirs schedule rehearsals, share sheet music and practice recordings, track attendance and collect membership fees. Through choir networks, it reached 140 choirs and around 4,000 singers in one season.

Then, in the same week:
• Her Firebase bill tripled
• A choir member who works in IT told her that, with the public config from the page, he could read every choir's member list: names, phone numbers, addresses

The API key in the page was never the problem. The rules behind it were the only lock on the door, and they said "authenticated users can read and write everything."

Behind other doors:
• Open Storage rules, so sheet music licensed by individual choirs could be downloaded by anyone
• Membership-fee status written by the client, so any member could mark themselves as paid
• An attendance screen listening in real time to the entire attendance collection, which explained the bill

New locks on every door (LaunchStudio, 6 business days, €1,500):
✓ Firestore and Storage rules rewritten deny-by-default, scoped to choir membership and roles, with 48 emulator tests in CI
✓ Queries that relied on client-side filtering fixed
✓ Fee status updated only by a Cloud Function, triggered by verified payment webhooks
✓ App Check enabled
✓ The collection-wide listener replaced by a scoped, paginated query
✓ Budget alerts, and scheduled backups with a test restore

Cross-choir access closed the day the new rules went live, and affected choirs were informed. The Firebase bill dropped about 70% from its peak, and Koorplanner grew to 230 choirs the following season.

"The API key in the page was never the problem. The rules behind it were - and I didn't know they were the only lock on the door." - Chiara Rossi

https://launchstudio.eu/en/blog/firebase-studio-ai-prototype-to-production-security-rules-that-hold

#Firebase #SecurityRules #Firestore #AppSecurity #LaunchStudio #Manifera
