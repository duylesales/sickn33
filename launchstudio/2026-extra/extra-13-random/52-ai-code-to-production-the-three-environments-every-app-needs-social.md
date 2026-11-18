🎣 ONE ENVIRONMENT FOR EVERYTHING: what happened

Testing a new feature ➜ test permits created with real anglers' email addresses ➜ 340 anglers received permits for waters they hadn't paid for
A test payment ➜ made with a real card, in live Mollie mode ➜ refunded by hand
Developing a feature ➜ test sales ➜ showing up in water owners' sales dashboards
Running a migration ➜ on a Saturday morning ➜ the permits table locked, and wardens couldn't verify QR codes

Jeroen Smits, a keen angler and IT support specialist in Roosendaal, built Visvergunning on Replit: anglers buy day and season permits for private fishing waters in West Brabant, show a QR permit to wardens, and water owners see their sales. About 2,800 anglers had bought permits. Everything ran in one Replit project. He thought he was testing. He was experimenting on his customers.

THREE ENVIRONMENTS: what happens where now (LaunchStudio, 7 business days, €1,800)

DEVELOPMENT
Its own database · Mollie in test mode · every email captured, nothing sent

STAGING
Its own database, with seed data · Mollie in test mode · email only to Jeroen's own addresses

PRODUCTION
Real anglers · real payments · migrations run deliberately, outside peak fishing hours

PLUS
✓ Per-environment secrets in Replit Deployments
✓ Startup validation of environment variables
✓ Test sales removed from production reports
✓ The mistaken permits cancelled, with an apology email

The following season: around 4,500 permits sold, no test data reaching anglers or owners, and no weekend outages. Jeroen now builds freely in development, knowing nothing he does there can reach a real angler.

"I thought I was testing. I was actually running experiments on my customers. Three environments meant I could finally experiment on myself." - Jeroen Smits

https://launchstudio.eu/en/blog/ai-code-to-production-the-three-environments-every-app-needs

#Replit #Staging #DevOps #Environments #LaunchStudio #Manifera
