🚨 Rutger Veldkamp heeft een familiecamping bij Nunspeet en bouwde Campingplan: reserveringen voor kleine campings met plattegronden, seizoensprijzen en online betalen. Hij begon issues toe te wijzen aan de codeeragent van GitHub Copilot en mergede in twee maanden zo'n veertig van diens pull requests - de meeste na een snelle blik, sommige vanaf zijn telefoon. Negen campings op de Veluwe gebruikten het. Toen keek een review vóór het seizoen naar wat erdoorheen was geglipt. 😳

Eén PR die een weergavebug in prijzen oploste, maakte ook de beschikbaarheids-API openbaar, met gastnamen per plek. Een andere voegde een migratie toe die opgeslagen boekingsprijzen herberekende met de nieuwe seizoensregels - waardoor al betaalde boekingen veranderden. Een derde voegde een dubbel datumpackage toe. De workflow van de agent kon een geheim lezen met de URL van de productiedatabase, en er was geen branchbescherming. Zo beoordeelt u pull requests die u niet zelf schreef voordat AI-code productie bereikt:

❌ PR's die meer veranderen dan de issue vroeg
❌ Migraties die betaalde boekingen herschrijven
❌ Productiegeheimen binnen bereik van de agent
❌ Geen branchbescherming of verplichte controles

✅ Authenticatie op de beschikbaarheids-API hersteld
✅ De prijsherberekening teruggedraaid en oorspronkelijke prijzen uit back-ups hersteld, dubbel package verwijderd
✅ Database-inloggegevens geroteerd en productiegeheimen uit de omgeving van de agent gehaald
✅ Branchbescherming met verplichte controles, negatieve autorisatietests, linting van migraties en scannen op geheimen in CI, instructies voor de agent - plus staging met preview-deployments

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we uw agent snel werken terwijl CI de paar dingen vangt waar u niet om vroeg. ⚙️

💡 Het resultaat: € 2.100, zeven werkdagen. Rutger wijst de meeste issues nog steeds toe aan de agent - en in het volgende seizoen hield CI vijf PR's van de agent tegen vóór de review, waarvan twee met wijzigingen in rechten. Niets onjuists bereikte gasten of campinghouders. 🚀

👉 AI-Code naar Productie met GitHub Copilot Workspace: Pull Requests Beoordelen die Je Niet Zelf Schreef: https://launchstudio.eu/nl/blog/ai-code-to-production-with-github-copilot-agent-reviewing-pull-requests-you-didnt-write

#GitHubCopilot #CodeReview #AIAgents #DevOps #LaunchStudio #Manifera
