🚨 Thijmen de Lange, zweefvlieginstructeur bij Lelystad, bouwde Zweefvliegclub in FlutterFlow: leden boeken vliegslots en instructeurs, registreren vluchten, zien de beschikbaarheid van toestellen en betalen vliegkosten. Drie clubs, zo'n 520 leden — en Thijmen wilde vóór het nieuwe seizoen in beide app-stores staan. 😳

Firestore-regels lieten elk ingelogd lid elke collectie lezen en schrijven — inclusief vervaldata van medische verklaringen en betalingen van anderen — en eigen vluchten als betaald markeren. Een Mollie-API-sleutel zat in het binaire bestand van de app. Het scherm "solovlucht goedkeuren" voor instructeurs was verborgen, maar de schrijfactie erachter stond open voor iedereen. Door AI geplakte eigen code voegde een verouderd package toe, er was geen accountverwijdering of crashrapportage, en bewerkingen in FlutterFlow en in geëxporteerde code overschreven elkaar. Dit heeft geëxporteerde FlutterFlow-code nog nodig vóór productie:

❌ Firestore-regels die iedereen alles toestaan
❌ Een betaalsleutel in de app
❌ Rolbeperkingen alleen in de interface
❌ Twee bronnen van waarheid voor de code

✅ Firestore-regels afgebakend op clubs, leden en rollen, met emulatortests
✅ Aanmaken en bevestigen van betalingen in Cloud Functions met Mollie-webhooks, en goedkeuringen door instructeurs afgedwongen op de server
✅ Het problematische package vervangen, accountverwijdering in de app met opschoning in de backend, Crashlytics aangezet
✅ FlutterFlow als enige bron van waarheid met exports gecommit in Git — en beide store-indieningen voorbereid met gefaseerde uitrol

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en tien jaar Flutter-levering, zorgen we dat de regels achter een app die af lijkt ook echt af zijn. ⚙️

💡 Het resultaat: € 3.300, elf werkdagen. Beide apps werden bij de eerste indiening goedgekeurd, halverwege het seizoen sloot een vierde club aan, en het percentage sessies zonder crash bleef boven de 99,5%. 🚀

👉 AI-Prototype naar Productie met FlutterFlow: Wat Geëxporteerde Code Nog Nodig Heeft: https://launchstudio.eu/nl/blog/ai-prototype-to-production-with-flutterflow-what-exported-code-still-needs

#FlutterFlow #Firebase #MobieleApps #Flutter #LaunchStudio #Manifera
