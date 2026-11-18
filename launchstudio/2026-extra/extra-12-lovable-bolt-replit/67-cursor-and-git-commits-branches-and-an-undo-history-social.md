↩️ How to undo a bad AI session without version control: a record of attempts

ATTEMPT 1: Ask the assistant to undo it.
Result: worse.

ATTEMPT 2: Restore individual files from cloud sync history.
Result: a mix of old and new code that no longer fits together.

ATTEMPT 3: Rebuild three days of work by hand.
Result: a week gone, and months of wondering whether something from the incident was still in there.

Karin Zoetelief built Praktijkfacturatie in Cursor: invoicing for allied health practices (physiotherapy, dietetics, speech therapy), handling insurer and patient billing for 41 practices. For five months the project lived in a folder, backed up by a cloud sync that kept a few versions of individual files. Then she asked for a change to how insurer declaration codes were handled. The session changed things across the project, nothing worked, and the errors didn't obviously relate to her request. 🩻

ATTEMPT 4, with LaunchStudio (2 business days, €1,300):
✓ The project in a repository, with an initial commit pushed to a hosted remote
✓ An ignore file covering environment files, build output, and a folder of test exports containing real patient data, which had been syncing to a cloud account for five months
✓ Two credentials found in the folder, rotated
✓ A branch per change, with deletion as the answer to a bad session
✓ Commit before every session
✓ The declaration code change redone on a branch: an afternoon, not a week
✓ A short note of the workflow kept in the repository
Result: undo now takes a few seconds.

Over the following year, Karin discarded 23 sessions that went wrong, each in seconds. Before, one had cost her a week. She calls commit-before-session the rule that made the tools comfortable instead of nerve-racking.

"I rebuilt three days by hand because I had no way to go back. The fix was a repository, which took an hour, and I had spent five months not doing it because it sounded like something teams needed." - Karin Zoetelief

https://launchstudio.eu/en/blog/cursor-and-git-commits-branches-and-an-undo-history

#Git #Cursor #VersionControl #AICoding #LaunchStudio #Manifera
