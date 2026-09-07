🚨 Bas Kuipers said yes to two-way sync without asking what the customer would actually edit where. Nine days later, the two systems exchanged roughly 90,000 requests in a single weekend. 😳

"Can it sync both ways?" sounds like twice as much of something you already do — it's a different, much harder problem: 🧠

❌ One contact edited on both sides at once triggered a write loop that ran unchecked all weekend
❌ The accounting provider suspended the integration for abuse, and one contact's address had been overwritten 40 times
❌ Contacts were matched by email on every sync, merging 11 records where two employees shared a company address
❌ A deletion in the accounting package for an unrelated duplicate propagated straight into the CRM, wiping a customer's service history

✅ Ask "where do you want to make changes?" before building — most "two-way" requests are one-way in disguise
✅ Assign ownership per field: one system owns contact details, the other owns what only it should touch
✅ Prevent loops by tagging sync-originated writes and comparing content before writing anything back
✅ Never auto-propagate deletions — surface them for a human to confirm instead

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build sync that resolves conflicts predictably instead of discovering them in production. 🔄

His result: rebuilt as one-way sync for contacts with a persistent identity mapping, loop prevention, and a sync log the customer can actually see. 🚀

👉 Find out if you really need two-way sync: [Link to article]

#SaaS #Integrations #IndieHacker #DataSync #LaunchStudio #Manifera
