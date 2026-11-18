📁 Open your project folder. Now look for any of these:

• A .csv you exported from production "just for debugging"
• A database dump
• An environment file that isn't ignored
• Key material

If something's there, your editor has probably indexed it. And anything you've pasted into an AI conversation has left your machine.

Marnix Bouwhuis found a production export in his. He built Debiteurenbeheer in Cursor: receivables and payment reminder administration for accountancy offices, 29 offices managing around 18,000 debtors on behalf of their clients. Chasing a reconciliation problem, he exported a production table to CSV and left it in the project directory. It stayed four months. The project index included it, and he twice pasted rows into a conversation to ask why amounts didn't match. 🧾

The rows held names, addresses, outstanding amounts and payment histories of his customers' customers. He processed that data as a processor, under agreements that named his subprocessors and didn't include any AI tooling. He found it himself, while preparing answers for an accountancy group's audit.

Cleaning the folder, and the reason it got dirty (LaunchStudio, 2 business days, €2,400):
✓ The export deleted, with a rule that production data never enters the project directory
✓ An ignore file covering environment files, key material, exports and dumps
✓ Editor privacy settings confirmed, retention disabled, and a business tier taken for its contractual terms
✓ A seeded development dataset with a realistic shape, so ordinary work doesn't need production data
✓ A procedure for when a customer's data really must be reproduced: minimum extract, anonymised, deleted afterwards, recorded
✓ A redaction habit, and an absolute rule against pasting credentials
✓ A written assessment concluding the four months counted as processing by an undeclared subprocessor, disclosed to the affected offices with the remediation
✓ The provider's data handling terms filed with the subprocessor documentation

The accountancy group accepted the disclosure and went ahead. Marnix credits finding it himself and explaining it fully. The seeded dataset removed the reason he'd been exporting production data in the first place.

"The file sat in my project for four months and I pasted rows from it twice. Nothing was hacked. I had simply sent my customers' customers' data to a company nobody had agreed to." - Marnix Bouwhuis

https://launchstudio.eu/en/blog/cursor-security-context-secrets-and-what-leaves-your-machine

#Cursor #DataPrivacy #GDPR #AppSecurity #LaunchStudio #Manifera
