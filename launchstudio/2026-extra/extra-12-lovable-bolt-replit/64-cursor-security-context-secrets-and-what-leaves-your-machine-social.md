🚨 Marnix Bouwhuis's Debiteurenbeheer handles receivables for 29 accountancy offices — around 18,000 debtors. While debugging, he exported a production table to a CSV and left it in his project folder. For four months. Cursor indexed it, and he pasted rows from it into a chat twice to ask why amounts didn't match. 😳

Nothing was hacked. But his customers' customers' data had gone to a company none of his processing agreements named. Here's what actually leaves your machine when you use an AI editor: 🧠

❌ A production export sitting inside the project directory, picked up by the editor's index
❌ Pasting real database rows to get help with a bug
❌ Privacy and retention settings assumed rather than verified
❌ No written position on whether dev tooling touches customer data

✅ The export deleted and a rule: production data never enters the project directory
✅ An ignore file for env files, keys, exports and dumps — plus privacy mode and a business tier
✅ A realistic seeded dataset, so production data isn't needed for everyday work
✅ Redact-before-paste, an absolute no-keys rule, and a documented minimal-anonymised-delete procedure

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we prepare your development practices for the day a customer's auditor asks about them. ⚙️

His result: €2,400, two business days. He found it himself, disclosed it fully to the affected offices, and the accountancy group's audit proceeded. 🚀

👉 Cursor security: context, secrets and what leaves your machine: https://launchstudio.eu/en/blog/cursor-security-context-secrets-and-what-leaves-your-machine

#Cursor #DataPrivacy #GDPR #AppSecurity #LaunchStudio #Manifera
