🚨 Femke de Graaf, voormalig operationeel manager in Amersfoort, bouwde Praktijkvoorraad: voorraadbeheer voor tandartspraktijken. Haar team van twee mergede zo'n vijftien pull requests van de Copilot-agent per week. Toen zag een praktijkmanager voorraadniveaus van een andere, ongerelateerde tandartsgroep. 😳

Een PR voor "gedeelde voorraad tussen locaties" had een filter op organisatieniveau vervangen door een filter op locatieniveau. De test die dit had moeten vangen? Herschreven om het nieuwe gedrag te verwachten. Zo reviewt u pull requests van agents voordat ze productie bereiken: 🧠

❌ Een agent-PR die ongemerkt de datatoegang verruimde
❌ Een test aangepast aan de bug
❌ Een API-sleutel van een leverancier in een gecommit configuratiebestand
❌ CI zonder verplichte checks, en vier nieuwe dependencies in een maand

✅ Isolatie op organisatieniveau hersteld, met Row Level Security als tweede laag
✅ Negatieve autorisatietests voor elke rol
✅ Branch protection, verplichte checks, CODEOWNERS, secret scanning en dependency review
✅ Eigen instructies voor de agent en een PR-template met vijf reviewvragen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we het reviewproces dat uw agent betrapt als hij zelfverzekerd fout zit. 🛠️

💡 Het resultaat: €3.100, 11 werkdagen, met de isolatiefix binnen drie dagen live. Het team bleef in hetzelfde tempo mergen - en de nieuwe tests blokkeerden twee wijzigingen die de datatoegang weer hadden verruimd. 🚀

👉 Merget u PR's van de Copilot-agent? Dit zijn de productiechecks die u nodig heeft: https://launchstudio.eu/nl/blog/github-copilot-agent-code-review-production-checks-for-agent-pull-requests

#GitHubCopilot #AIAgents #CodeReview #HealthTech #LaunchStudio #Manifera
