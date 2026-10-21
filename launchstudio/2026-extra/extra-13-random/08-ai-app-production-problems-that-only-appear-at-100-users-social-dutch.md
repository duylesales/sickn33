🚨 Sven Mulder, penningmeester van een hockeyclub in Deventer, bouwde Teamkas in Lovable om contributie te innen. Het werkte zo goed dat hij er een SaaS van maakte: binnen zes maanden 23 clubs, zo'n 110 beheerders en een paar duizend betalende leden. Toen raakte het nieuwe seizoen ze allemaal tegelijk. 😳

Het betalingsoverzicht duurde voor grotere clubs meer dan tien seconden. Herinneringsmails liepen tegen de ingebouwde limieten van Supabase aan en honderden gingen nooit de deur uit. Twee penningmeesters die dezelfde contributie aanpasten, overschreven elkaar — en toen een lid twee keer werd afgeschreven, kon Sven niet zien waarom. Dit zijn de problemen die pas bij zo'n 100 gebruikers verschijnen:

❌ Elke transactie opgehaald en gefilterd in de browser
❌ Transactionele e-mail via een verzender voor ontwikkelvolumes
❌ De laatste opslag wint — conflicterende bewerkingen stil verloren
❌ Geen beheerweergave, geen audittrail voor supportvragen

✅ Zware query's herschreven met paginering, filters op de server en indexen
✅ Alle e-mail naar een transactionele aanbieder met een geauthenticeerd verzenddomein
✅ Optimistische vergrendeling, zodat conflicterende bewerkingen een waarschuwing geven in plaats van te overschrijven
✅ Een eenvoudige beheerweergave met een auditlog per lid, plus monitoring van laadtijden en e-mailaflevering

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, versterken we SaaS-producten op het moment dat de eerste honderd gebruikers ze blootleggen — en blijft uw interface intact. ⚙️

💡 Het resultaat: € 3.800, dertien werkdagen. Het overzicht ging van ruim 10 seconden naar minder dan één, de aflevering van herinneringen steeg van ~60% naar 99%+, openstaande contributie daalde met ongeveer een derde — en Teamkas groeide tegen het einde van het seizoen naar 41 clubs. 🚀

👉 Productieproblemen van AI-apps die pas zichtbaar worden bij 100 gebruikers: https://launchstudio.eu/nl/blog/ai-app-production-problems-that-only-appear-at-100-users

#SaaS #Lovable #Schaalbaarheid #Startups #LaunchStudio #Manifera
