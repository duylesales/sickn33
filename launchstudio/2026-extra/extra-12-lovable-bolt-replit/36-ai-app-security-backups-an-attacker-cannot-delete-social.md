🚨 Youri Landman's Praktijkdossier holds client records and session notes for 64 psychologists and coaches — about 3,200 clients. A practitioner reused a breached password. The attacker signed in, used a broad export function to take data, then deleted records across the practice. 😳

His only extra backup sat in the same cloud account, with the same keys. The restore took eleven hours — and 340 session attachments had never been backed up at all. They were gone. Here's what a backup against an attack actually needs: 🧠

❌ Backups deletable with the same credentials that run the app
❌ Only the database backed up — uploaded files never were
❌ Nightly exports only, so up to 24 hours of work at risk
❌ Never once restoring a backup to see if it worked

✅ An independent backup at a separate provider, with a write-only key the app doesn't hold
✅ Object lock for 35 days, with daily, weekly and monthly retention — and attachments included
✅ Point-in-time recovery, cutting potential loss from 24 hours to five minutes
✅ A written recovery plan, a restore timed at 47 minutes, alerts for missing or shrunken backups, a narrowed export and 2FA for admins

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we ask when you last restored a backup — the answer is usually never, and that's the finding. 💾

His result: three business days and €3,300 later, an eleven-hour reconstruction became a 47-minute restore, and the backups now live where his own credentials can't reach them. The 340 lost attachments — and the conversations with affected clients — are why he says it matters. 🚀

👉 Backups an attacker cannot delete: https://launchstudio.eu/en/blog/ai-app-security-backups-an-attacker-cannot-delete

#Backups #Ransomware #DataProtection #Lovable #LaunchStudio #Manifera
