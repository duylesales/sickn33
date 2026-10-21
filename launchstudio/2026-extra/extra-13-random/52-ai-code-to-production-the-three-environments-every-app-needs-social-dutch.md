🚨 Jeroen Smits, fanatiek visser en IT-supportspecialist in Roosendaal, bouwde Visvergunning op Replit: vissers kopen dag- en seizoensvergunningen voor particuliere wateren in West-Brabant en tonen een QR-vergunning aan controleurs. Zo'n 2.800 vissers gebruikten het. Toen maakte hij bij het testen van een nieuwe functie testvergunningen aan met echte e-mailadressen van vissers — en 340 van hen kregen vergunningen waarvoor ze niet hadden betaald. 😳

Alles draaide in één Replit-project. Een testbetaling had al een echte kaart in de live modus van Mollie belast. De verkoopdashboards van eigenaren zaten vol testverkopen. En een migratie tijdens de ontwikkeling vergrendelde op een zaterdagochtend de vergunningentabel, waardoor controleurs QR-codes niet konden verifiëren. Daarom heeft AI-code drie omgevingen nodig vóór productie:

❌ Eén plek voor bouwen, testen en echte klanten
❌ Testmails die echte mensen bereiken
❌ Live betaalsleutels gebruikt tijdens het testen
❌ Migraties "om even te proberen" op live data

✅ Aparte databases voor development, staging en productie
✅ Mollie in testmodus in development en staging; e-mail opgevangen in development en beperkt in staging
✅ Geheimen per omgeving in Replit Deployments, plus validatie van omgevingsvariabelen bij het opstarten
✅ Seeddata voor staging en een deploymentproces met migraties buiten de piekuren van het vissen — testverkopen verwijderd, onterechte vergunningen ingetrokken met een excuus

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat niets wat u in development probeert een echte klant kan bereiken. ⚙️

💡 Het resultaat: € 1.800, zeven werkdagen. Het volgende seizoen werden zo'n 4.500 vergunningen verkocht zonder dat testdata vissers of eigenaren bereikte en zonder storingen in het weekend — en Jeroen experimenteert nu vrijuit. 🚀

👉 AI-Code naar Productie: De Drie Omgevingen Die Elke Applicatie Nodig Heeft: https://launchstudio.eu/nl/blog/ai-code-to-production-the-three-environments-every-app-needs

#Replit #Staging #DevOps #Omgevingen #LaunchStudio #Manifera
