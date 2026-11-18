🚦 The pipeline that wasn't there

push ➜ install ➜ build ➜ lint ➜ type check ❌ STOP
"Variable not defined in this scope." Deployment blocked.

That's roughly the 95-second check that would have caught it. Without it, here's what happened instead.

Maud Terlouw built Rittenregistratie on Replit: journey and expense registration for 11 home care organisations, around 700 carers who travel between clients. She deployed with the platform's button, straight from the editing session, several times a day. No tests, no checks.

One Thursday she made a small change to the expense calculation, deployed at 16:25, and left to collect her children. The change referenced a variable that didn't exist in that scope, the kind of error a type checker reports instantly and a quick human read misses. The app failed to start.

Until 19:40, when a carer's message finally reached her, around 400 carers finishing their shifts couldn't register the day's journeys. Most gave up. At two organisations, staff wrote them on paper and re-entered them the following week. 🚗

Building the pipeline (LaunchStudio, 2 business days, €2,600):
✓ Code in a repository, with the platform deploying from the main branch instead of an editing session
✓ On every push: install, build, lint, type check, run tests, and scan the built output for credential patterns
✓ Deployment gated on all of it
✓ 31 tests: authorisation across 14 endpoints, the expense and distance calculations, and one end-to-end journey registration
✓ The whole run in 95 seconds
✓ A preview deployment per branch, with its own database and credentials, protected from public access
✓ An external uptime check that would have flagged the outage within two minutes

In the following year, the pipeline blocked 14 deployments. Nine were build or type failures that would have broken the product exactly as that Thursday did. And Maud deploys more often now, not less, because the decision isn't hers to make any more.

"I deployed at twenty-five past four and went to collect my children. Four hundred carers could not register their journeys for three hours, and the error was a variable name a type checker would have caught before I left the room." - Maud Terlouw

https://launchstudio.eu/en/blog/replit-and-ci-testing-before-a-deployment

#Replit #ContinuousIntegration #DevOps #Testing #LaunchStudio #Manifera
