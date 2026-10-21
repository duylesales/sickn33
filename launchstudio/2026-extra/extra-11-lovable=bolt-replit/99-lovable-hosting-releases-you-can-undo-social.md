🚨 Mark Oudshoorn's Kassakoppeling syncs sales from 34 shops around Gorinchem and Leerdam into their stock and accounting systems. He deployed straight to production, with no staging. One Thursday an agent session "tidied up" the sales table — and its migration dropped the column recording which till each sale came from. 😳

Reverting the code took thirty seconds and changed nothing, because the data was gone. Restoring the morning backup would have wiped a day of trading for all 34 shops. Here's why undo and rollback aren't the same thing: 🧠

❌ Deploying directly from a working environment, with no staging
❌ A rollback that had never been tested
❌ Agent-generated migrations that touch data, run unread
❌ An application database account allowed to drop columns

✅ Staging with anonymised data, reproducible builds and every deploy tied to a commit
✅ Rollback tested and timed at 40 seconds
✅ Expand-and-contract schema changes: any migration touching data is read first and preceded by a snapshot
✅ Feature flags, separated database credentials and a five-line release routine

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make every release something you can undo. ↩️

His result: six business days and €3,400 later — the lost column reconstructed from till receipts (two shops' gaps written off with their agreement) and eleven months without an incident. The read-before-run rule has since caught two more destructive suggestions. 🚀

👉 Releases you can undo: https://launchstudio.eu/en/blog/lovable-hosting-releases-you-can-undo

#DevOps #Lovable #Migrations #Retail #LaunchStudio #Manifera
