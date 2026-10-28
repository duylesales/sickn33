🚨 Karin Zoetelief's Praktijkfacturatie handles insurer and patient billing for 41 allied health practices. For five months she built in Cursor without version control. Then one session changing how insurer declaration codes worked broke things across the whole project - and she had no way back. 😳

Prompting made it worse. Restoring files from cloud sync produced a mix of old and new code. She rebuilt three days of work by hand. Here's the minimum version control a solo founder working with AI needs: 🧠

❌ No repository - just a folder with a cloud sync of individual files
❌ Trying to undo an AI session by prompting the AI
❌ Test exports with real patient data syncing to a cloud account for five months
❌ Credentials sitting in the project folder

✅ A repository with a first commit, pushed to a hosted remote
✅ An ignore file for env files, build output and data - and the two exposed credentials rotated
✅ A branch per change, deleted rather than salvaged when a session goes wrong
✅ An absolute rule: commit before every AI session

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, version control is the first thing we set up when taking over a project - nothing else is safe without it. ⚙️

Her result: €1,300, two business days. The declaration code change took an afternoon on a branch - and over the next year she discarded 23 bad sessions, each in a few seconds. 🚀

👉 Cursor and Git: commits, branches and an undo history: https://launchstudio.eu/en/blog/cursor-and-git-commits-branches-and-an-undo-history

#Git #Cursor #VersionControl #AICoding #LaunchStudio #Manifera
