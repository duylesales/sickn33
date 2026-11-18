👩‍🍳 THE CHEF'S PREP LIST for a recipe costing app that survives lunch service

Amira Haddad, a former sous-chef in The Hague, built Kostprijs with Replit Agent. Chefs enter ingredients and supplier prices, and the app calculates margin per dish and flags when a price increase makes a menu item unprofitable. Six restaurants started on a free trial.

Then the complaints came, at lunchtime, when traffic peaked: chefs logged out mid-edit, losing their changes.

WHAT WAS WRONG IN THE KITCHEN
🔥 An Autoscale deployment with sessions stored in memory. When Replit added an instance under load, requests landed on an instance that didn't know the user.
🔥 Test scripts running against the same database the restaurants used. One test reset a client's supplier prices to sample values.
🔥 A nightly price-alert email started from inside a web request, silently skipped whenever the instance scaled down

THE PREP LIST (LaunchStudio, 9 business days, €2,200)
☐ ➜ ☑ Sessions stored in the database
☐ ➜ ☑ Separate development and production databases
☐ ➜ ☑ Nightly alerts moved into a Scheduled deployment
☐ ➜ ☑ Server-side checks so each restaurant group sees only its own recipes
☐ ➜ ☑ Nightly backups, with a tested restore
☐ ➜ ☑ Uptime and error alerts

Kostprijs stayed on Replit, on an Autoscale deployment that now behaves correctly under load.

SERVICE REPORT
Lunchtime logouts stopped completely. Four of the six trial restaurants converted to paid plans within the month. Amira still adds features with Replit Agent, against the development database.

"Replit made it easy to build and easy to deploy. Nobody told me those were two different questions from making it reliable." - Amira Haddad

https://launchstudio.eu/en/blog/replit-app-deployment-from-agent-build-to-production

#Replit #ReplitAgent #AIFounder #SaaS #LaunchStudio #Manifera
