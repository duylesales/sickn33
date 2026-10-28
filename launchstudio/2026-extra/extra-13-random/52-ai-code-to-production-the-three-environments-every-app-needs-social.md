🚨 Jeroen Smits, a keen angler and IT support specialist in Roosendaal, built Visvergunning on Replit: anglers buy day and season permits for private waters in West Brabant and show a QR permit to wardens. About 2,800 anglers used it. Then, while testing a new feature, he generated test permits using real anglers' emails - and 340 of them received permits they hadn't paid for. 😳

Everything ran in one Replit project. A test payment had already hit a real card in live Mollie mode. Owners' sales dashboards were full of test sales. And a migration run during development locked the permits table on a Saturday morning, so wardens couldn't verify QR codes. Here's why AI code needs three environments before production: 🧠

❌ One place for building, testing and real customers
❌ Test emails reaching real people
❌ Live payment keys used during testing
❌ Migrations "just to try it" on live data

✅ Separate development, staging and production databases
✅ Mollie test mode in dev and staging; email captured in dev and restricted in staging
✅ Per-environment secrets in Replit Deployments, plus startup validation of environment variables
✅ Seed data for staging and a deployment process with migrations run outside peak fishing hours - test sales removed, mistaken permits cancelled with an apology

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure nothing you try in development can reach a real customer. ⚙️

His result: €1,800, seven business days. The next season sold around 4,500 permits with no test data reaching anglers or owners and no weekend outages - and Jeroen now experiments freely. 🚀

👉 AI code to production: the three environments every app needs: https://launchstudio.eu/en/blog/ai-code-to-production-the-three-environments-every-app-needs

#Replit #Staging #DevOps #Environments #LaunchStudio #Manifera
