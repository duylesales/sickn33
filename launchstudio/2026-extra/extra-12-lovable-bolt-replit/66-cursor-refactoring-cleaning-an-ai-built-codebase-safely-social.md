🗓️ The week Bram set aside for a cleanup

MONDAY
Eighteen months in, changes have become frustratingly slow. He asks the assistant to restructure the whole project.

WEDNESDAY
The product doesn't work. Most of the codebase has moved, several behaviours changed along the way, and it's all in four enormous commits. No tests say what broke. Reverting means losing three days, including two genuine fixes.

THURSDAY + FRIDAY
Finding problems by clicking.

THE FOLLOWING TUESDAY
Deployed, with three defects. Over the next fortnight customers find them, including one that assigned maintenance records to the wrong vehicle.

Bram Terlouw built Wagenparkbeheer in Cursor: fleet administration (maintenance, inspections, fuel and driver assignment) for 34 companies, 1,900 vehicles. 🚐

The recovery, and a different kind of week (LaunchStudio, 4 business days, €3,600):

DAY 1: The branch abandoned, the production version restored.
DAY 2: A test safety net, written first: authorisation across 26 endpoints, the maintenance and inspection calculations, and one end-to-end flow.
DAY 3: Deletion as its own pass: 19 unused components, 7 dead endpoints (two unauthenticated) and 4 abandoned tables gone. Duplication merged only where it mattered: the inspection due-date calculation, found in five places with two variants.
DAY 4: The three largest files split, with structure changes and behaviour changes in separate commits throughout.

And a standing rule: cleanup happens in the area you're working on, in its own commit, not as a project.

The same cleanup was finished over the next three months, alongside normal feature work, without a single customer-visible incident. Bram's take: the lost days came entirely from having no way to tell what he'd broken.

"I asked it to restructure the project and it did exactly that. By Wednesday nothing worked, and I had no tests, one giant commit and three days of changes I could not separate from each other." - Bram Terlouw

https://launchstudio.eu/en/blog/cursor-refactoring-cleaning-an-ai-built-codebase-safely

#Refactoring #Cursor #TechnicalDebt #AICoding #LaunchStudio #Manifera
