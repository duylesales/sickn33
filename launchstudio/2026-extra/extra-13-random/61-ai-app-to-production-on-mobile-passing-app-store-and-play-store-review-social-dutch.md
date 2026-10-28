🚨 Joost Verbruggen, hondenuitlater in Tilburg, bouwde Uitlaatmaatje in Bolt als Expo-app: eigenaren boeken wandelingen, uitlaters delen live locatie en foto's, en betalingen lopen via Stripe. Hij wilde vóór de zomervakantie in beide app-stores staan. Apple wees de app in vijf weken drie keer af. 😳

Eerst konden reviewers niet inloggen. Toen was er geen accountverwijdering in de app. Toen liet het privacylabel locatiedata en crashanalytics weg van een SDK die Bolt had toegevoegd - en Google markeerde het formulier Data safety om dezelfde reden. Ondertussen pakte een vriend de Android-build uit en vond de geheime Stripe-sleutel en de Google Maps-sleutel erin. Dit vraagt slagen voor de review van App Store en Play Store voor een AI-app:

❌ Geen demo-account voor reviewers
❌ "Mail ons om je account te verwijderen"
❌ Privacylabels die missen wat SDK's verzamelen
❌ Geheime sleutels in het binaire bestand van de app

✅ Beide sleutels geroteerd, betalingen en kaartaanroepen naar functies aan de serverkant
✅ Een verwijderflow in de backend die profielen, hondengegevens, wandelfoto's en locatiegeschiedenis wist - en Stripe-klanten annuleert
✅ API-routes met versies zodat oudere builds blijven werken, plus een demo-account met realistische wandelingen
✅ De dataverzameling van elke SDK gedocumenteerd voor juiste verklaringen, duidelijke doelbeschrijvingen bij rechten - en reviewnotities die uitleggen waarom Stripe past bij diensten in de echte wereld

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en tien jaar levering van React Native- en Flutter-apps, bereiden we de delen van een mobiele lancering voor die AI-tools overslaan. ⚙️

💡 Het resultaat: € 3.900, veertien werkdagen. Uitlaatmaatje kwam bij de volgende indiening door de review van beide stores en kreeg in drie maanden 640 hondenbezitters en 38 uitlaters erbij rond Tilburg en Breda. 🚀

👉 AI-App naar Productie op Mobiel: Slagen voor de App Store- en Google Play-Review: https://launchstudio.eu/nl/blog/ai-app-to-production-on-mobile-passing-app-store-and-play-store-review

#MobieleApps #AppStore #ReactNative #Expo #LaunchStudio #Manifera
