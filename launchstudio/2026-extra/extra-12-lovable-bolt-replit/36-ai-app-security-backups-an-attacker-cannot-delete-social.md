⏱️ 11 hours ➜ 47 minutes

That's a full restore of one practice-records product, before and after.

Youri Landman built Praktijkdossier in Lovable: client records and session notes for psychology and coaching practices, 64 practitioners, around 3,200 clients. A practitioner reused a password from an unrelated breach. The attacker logged in, found the practice admin area, used an export function with broad database access to take a substantial amount of data, then deleted records across the practice. 🧠

THE 11-HOUR RESTORE
⏳ The only extra backup was a nightly export, in a bucket in the same cloud account as the app, with the same credentials. Not deleted this time, but reachable. A more thorough attacker would have removed it.
⏳ The export held the database and nothing else
⏳ Session note attachments, the most sensitive and least replaceable part of the product, had never been backed up at all
⏳ 340 of them were gone

Youri had backups, in the same account, with the same keys, never once restored. What he really had was a file he hoped was useful.

THE 47-MINUTE RESTORE (LaunchStudio, 3 business days, €3,300)
⚡ An independent backup in a separate provider account, with a write-only credential the app doesn't hold
⚡ Object lock with 35-day immutability: daily for a month, weekly for a quarter, monthly for a year
⚡ Session attachments included
⚡ Point-in-time recovery, cutting potential loss from 24 hours to five minutes
⚡ Configuration, DNS and webhook endpoints recorded in the repository
⚡ A recovery document with numbered steps
⚡ A restore test, performed and timed: 47 minutes for the whole product
⚡ Alerts if a backup is missing, or more than 20% smaller than the last one
⚡ The export function limited to the admin's own practice
⚡ Two-factor authentication required for admin accounts

The 340 attachments couldn't be recovered, and the affected clients were informed, which Youri calls the worst professional experience of his life. The setup since would have prevented it, and the backups now sit where his own credentials can't reach.

"I had backups. I had them in the same account, with the same keys, and I had never once restored one. What I actually had was a file I hoped was useful." - Youri Landman

https://launchstudio.eu/en/blog/ai-app-security-backups-an-attacker-cannot-delete

#Backups #Ransomware #DataProtection #Lovable #LaunchStudio #Manifera
