🚨 Bezorgtijd van Tim Roozendaal toont bezorgmomenten bij de checkout van 34 Nederlandse webshops rond Tilburg en Breda. Endpoints controleerden de sleutel en vertrouwden daarna op de ID's in het verzoek. Een developer typte een ordernummer van een papiertje in een testaanroep - en kreeg de order van een andere retailer, met de naam van een concurrent in het adres. 😳

Dit betekent het werkelijk om een API te beveiligen die uw klanten aanroepen:

❌ De sleutel controleren, maar niet of die sleutel dit specifieke object mag zien
❌ Interne endpoints die openbaar werden op de dag dat de API live ging
❌ Update-endpoints waarmee een aanroeper kan wijzigen van welke klant een order is
❌ Geen rate limits, geen paginering, en foutmeldingen met kolomnamen erin

✅ Autorisatie per object op elk endpoint, niet alleen per sleutel
✅ Accepteer bij updates alleen een vastgestelde lijst velden
✅ Rate limits per sleutel, verplichte paginering en algemene foutmeldingen naar buiten
✅ Versiebeheer, documentatie met richtlijnen voor veilig sleutelgebruik, en testen vanuit een tweede account

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, testen we uw API zoals iemand die probeert binnen te komen. 🧪

💡 Het resultaat: in acht werkdagen en voor € 4.400 controleren alle 23 endpoints de toegang per object - inclusief zeven interne, waarvan er één elk bezorgmoment van elke retailer toonde. Twee webshops die de API vanuit browser-JavaScript aanriepen, kregen nieuwe sleutels. De werkgever van de melder breidde uit naar drie zusterbedrijven. 🚀

👉 Een API beveiligen die uw klanten aanroepen: https://launchstudio.eu/nl/blog/ai-app-security-protecting-an-api-your-customers-call

#APISecurity #Ecommerce #Lovable #B2B #LaunchStudio #Manifera
