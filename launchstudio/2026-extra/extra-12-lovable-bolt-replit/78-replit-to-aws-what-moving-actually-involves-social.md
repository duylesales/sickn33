🚨 Maarten Kolff's Dossierbeheer manages around 2,800 case files for nine youth care organisations, running on Replit. A regional care partnership offered a contract covering four more organisations - on condition that personal data was stored in the Netherlands, under a specific agreement, with a named certification. His board and two advisers agreed: migrate everything to AWS. 😳

Estimated: seven weeks of work and about €900 a month to run. But the contract's condition was about where personal data is stored - not where the application executes. Here's what moving from Replit to AWS actually involves, and when you don't need to: 🧠

❌ Treating "data must be in the Netherlands" as "everything must move to AWS"
❌ Budgeting for the migration but not for the permanent operational work after it
❌ Not checking whether a smaller change satisfies the same requirement
❌ Forgetting everything the platform did implicitly: networking, certificates, logging, alerting, backups, secrets

✅ The database moved to a managed Postgres instance in a Dutch region under a qualifying agreement - rehearsed, then a 35-minute Sunday cutover
✅ Case documents moved to object storage in the same region, with URLs generated at read time
✅ The application left on Replit, simply pointed at the new database and storage
✅ A published data location statement and subprocessor page, plus in-region backups with a tested restore

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we do full migrations - and more often find the smallest move that satisfies the same requirement. ⚙️

His result: €8,900, nine business days instead of a quarter. The contract was signed, and infrastructure went from €95 to €340 a month - not €900. 🚀

👉 Replit to AWS: what moving actually involves: https://launchstudio.eu/en/blog/replit-to-aws-what-moving-actually-involves

#Replit #AWS #CloudMigration #DataResidency #LaunchStudio #Manifera
