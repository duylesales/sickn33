🚨 Ferry Janssen, eigenaar van een zelfstandige garage in Helmond, bouwde Garagepost in Bolt: klanten boeken onderhoud op kenteken, krijgen offertes met foto's voor extra werk, keuren die goed in de app en betalen vóór het ophalen van hun auto. Nog drie garages in de regio Helmond–Eindhoven sloten aan. Toen kreeg een klant die een offerte van € 480 voor remschijven had goedgekeurd een factuur van € 560. 😳

De catalogusprijs van de onderdelen was tussen goedkeuring en factuur gestegen, en de offerte werd live herberekend. Goedkeuringslinks waren raadbare ordernummers. Klanten van de ene garage konden via de API voertuigen en facturen van een andere zien. Maandagochtenden waren structureel dubbel geboekt, betalingen werden als geslaagd gemarkeerd bij de redirect in de browser, en het opzoeken van kentekens kon zonder login duizenden keren per dag worden aangeroepen. Dit maakt een garage-app productierijp:

❌ Goedgekeurde offertes die achteraf van prijs veranderen
❌ Raadbare goedkeuringslinks
❌ Klanten die data van andere garages zien
❌ Geen capaciteitscontrole en betalingen bevestigd door de browser

✅ Offertes bevroren bij verzending, met onderdeelprijzen per regel en leveranciersreferenties
✅ Willekeurige verlopende goedkeuringstokens gekoppeld aan het klantaccount, goedkeuringen gelogd met tijdstempels van de server
✅ Scheiding per garage met row level security en capaciteit per brug en monteur
✅ Geverifieerde Mollie-webhooks gekoppeld aan het vrijgeven van de klus, het opzoeken van kentekens achter authenticatie met rate limits, en privéopslag van foto's

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat "ja" op een offerte dezelfde prijs op de factuur betekent. ⚙️

💡 Het resultaat: € 2.200, acht werkdagen. Betwiste offertes stopten, de overboeking op maandag verdween, en Garagepost tekende met nog vier zelfstandige garages in Noord-Brabant. 🚀

👉 AI-Applicatie Productierijp voor Autogarages: Voertuigdata, Offertes en Onderdelen: https://launchstudio.eu/nl/blog/ai-application-production-ready-for-car-garages-vehicle-data-quotes-and-parts

#Automotive #Garage #Bolt #Betalingen #LaunchStudio #Manifera
