🚨 Bram Terlouw's Wagenparkbeheer manages maintenance, inspections and fuel for 34 companies and 1,900 vehicles. Eighteen months in, changes had become painfully slow - so he set aside a week and asked Cursor to restructure the whole project. By Wednesday, nothing worked. 😳

Four giant commits, no tests, and three days of changes he couldn't separate. He shipped the following Tuesday with three defects - one assigning maintenance records to the wrong vehicle. Here's how to clean up an AI-built codebase without breaking it: 🧠

❌ "Refactor the whole project" as a single request
❌ No test safety net to say what had broken
❌ Structure and behaviour changed in the same commits
❌ Reverting meant losing two genuine fixes along with the damage

✅ Production restored, then a safety net first: authorisation across 26 endpoints, core calculations, one end-to-end flow
✅ Deletion as its own pass: 19 unused components, 7 dead endpoints (two unauthenticated), 4 abandoned tables
✅ Duplication fixed only where it mattered - an inspection due-date calculation living in five places, in two variants
✅ A standing rule: tidy the area you're working in, in its own commit - never a cleanup week

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we do the first cleanup pass when taking over an AI-built product - and it makes everything after it cheaper. ⚙️

His result: €3,600, four business days of recovery. The same cleanup was then finished over three months alongside normal feature work - without a single customer-visible incident. 🚀

👉 Cursor refactoring: cleaning an AI-built codebase safely: https://launchstudio.eu/en/blog/cursor-refactoring-cleaning-an-ai-built-codebase-safely

#Refactoring #Cursor #TechnicalDebt #AICoding #LaunchStudio #Manifera
