🚨 Met Rittenregistratie van Maud Terlouw registreren zo'n 700 thuiszorgmedewerkers bij 11 organisaties hun ritten en onkosten. Ze deployde rechtstreeks vanuit Replit met één klik, meerdere keren per dag - geen tests, geen controles. Op een donderdag deployde ze om 16:25 een kleine wijziging en ging haar kinderen ophalen. 😳

De app startte niet. Tot 19:40 konden zo'n 400 zorgverleners die hun dienst afsloten hun ritten niet registreren. De oorzaak: een variabelenaam die niet bestond - iets wat een typecontrole direct opvangt. Zo zet u een poort tussen uw Replit-code en uw klanten:

❌ Rechtstreeks deployen vanuit een bewerksessie
❌ Geen buildcontrole, geen linter, geen typecontrole
❌ Geen tests op de onkosten- en afstandsberekeningen
❌ Geen uptimemonitoring - de storing werd drie uur later door een zorgverlener gemeld

✅ Code in een repository, met het platform dat deployt vanaf de hoofdbranch
✅ Een CI-workflow bij elke push: installeren, bouwen, linten, types controleren, testen en scannen op geheimen - deployment geblokkeerd als iets faalt
✅ 31 tests voor autorisatie over 14 endpoints, de berekeningen en één end-to-end-rit - de hele pipeline in 95 seconden
✅ Previewdeployments per branch met geïsoleerde inloggegevens, plus een externe uptimecontrole

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, is dit meestal de verandering waardoor oprichters op vrijdag durven te deployen. ⚙️

💡 Het resultaat: € 2.600, twee werkdagen. In het jaar daarna hield de pipeline 14 deployments tegen - negen daarvan zouden het product precies zoals die donderdag hebben gebroken. En ze deployt nu vaker, niet minder. 🚀

👉 Replit en CI: testen vóór een deployment: https://launchstudio.eu/nl/blog/replit-and-ci-testing-before-a-deployment

#Replit #ContinuousIntegration #DevOps #Testen #LaunchStudio #Manifera
