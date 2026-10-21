🚨 Ruben Hooghiemstra's Leerlingvervoer plans transport for around 600 pupils in special education, for seven transport contractors. The project started as a public Replit template he was learning from. During those four public months he pasted a database connection string into a config file — and forgot. Eighteen months later, a routine review found it still there. The project had been forked eleven times. 😳

The database held pupils' names, addresses, schools and transport needs. Here's how credentials spread on a shared Replit project — and how to rotate them without breaking anything: 🧠

❌ A project left public without anyone deciding it should be
❌ A connection string pasted into a file instead of the secrets mechanism — files travel with every fork
❌ Four former collaborators who still had access
❌ One shared administrative key used for everything

✅ Database credentials rotated first; project history searched by value, which found an email key too
✅ The eleven forks identified and the platform contacted about the two public ones
✅ Scoped credentials per integration, dev and production genuinely separated, a seven-item credential inventory
✅ A documented breach assessment — and notification to the contractors and the Dutch DPA

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, credential hygiene is consistently our first finding when taking a Replit project to production. ⚙️

His result: €2,900, two business days. Logs showed no evidence of access — and because the contractors heard it directly from Ruben first, all seven stayed. 🚀

👉 Replit secrets: rotating keys on a shared project: https://launchstudio.eu/en/blog/replit-secrets-rotating-keys-on-a-shared-project

#Replit #AppSecurity #GDPR #SecretsManagement #LaunchStudio #Manifera
