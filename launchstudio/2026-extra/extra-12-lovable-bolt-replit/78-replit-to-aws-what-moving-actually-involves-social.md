🔎 A close reading of one contract condition

The condition, as the regional care partnership set it:
Personal data must be [stored] in the Netherlands, on infrastructure under a [specific agreement], with a [named certification].

The sentence everyone heard:
"You need to migrate to AWS."

What the condition covers: where personal data is stored and processed. That means the database and the case documents.
What it doesn't mention: where the application runs. The application holds no data at rest.

Maarten Kolff built Dossierbeheer on Replit: case file management for nine youth care organisations, around 2,800 cases. The partnership offered a contract covering four organisations, on that condition. His board and two advisers agreed the answer was a full move to AWS. 📁

Doing what the sentence actually says (LaunchStudio, 9 business days, €8,900):
✓ The database moved to a managed Postgres instance in a Netherlands region, under an agreement meeting the certification requirement, rehearsed on a copy first, with a 35-minute cutover on a Sunday
✓ Case documents moved to object storage in the same region, with URLs generated at read time so no stored reference needed rewriting
✓ The application left on Replit, calling the new database and storage
✓ A subprocessor page and data location statement published
✓ In-region backups, with a tested restore
✓ A documented assessment of where each category of data now lives

The comparison:

                      Targeted move      Full AWS migration (estimate)
Work                  9 business days    seven weeks
Monthly running cost  €95 ➜ €340         roughly €900
Meets the condition?  yes                yes, exactly the same one

The requirement was met and the contract signed.

"Two advisers told me I needed to be on AWS. The contract said our patients' data had to be in the Netherlands under a specific agreement. Those are not the same sentence, and it took an afternoon to establish that." - Maarten Kolff

https://launchstudio.eu/en/blog/replit-to-aws-what-moving-actually-involves

#Replit #AWS #CloudMigration #DataResidency #LaunchStudio #Manifera
