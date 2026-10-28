🚨 Ties Kroeze built Zwemles with Bolt - swimming lesson scheduling for four swimming schools around Purmerend and Volendam, covering roughly 1,900 children. He moved it to a full development environment over a weekend. On Monday everything appeared to work. 😳

Nineteen days later a swimming school asked why parents had started phoning about lesson times. Here's what doesn't move with your code: 🧠

❌ A nightly reminder email configured in the old platform's scheduler - it simply stopped
❌ Attendance photos stored beside the app, missing from the export
❌ A payment webhook still pointing at the old address - cancellations stopped being recorded
❌ A timezone setting that silently reverted, showing lesson times an hour out for some parents

✅ The reminder rebuilt as a scheduled task, every run logged, with an alert if none is recorded
✅ A full inventory of platform-specific settings
✅ Photos in object storage with per-school access
✅ The webhook repointed with signature verification and deduplication, missed cancellations reconciled, secrets rotated

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we move prototypes between tools without leaving the invisible parts behind. 🔄

His result: eight business days and €3,600 later, everything was documented - and three families who were still being charged for lessons they had cancelled were refunded within the week. 🚀

👉 Moving a prototype between Replit and Bolt: https://launchstudio.eu/en/blog/replit-and-bolt-moving-a-prototype-between-tools

#Replit #Bolt #Migration #Webhooks #LaunchStudio #Manifera
