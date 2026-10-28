🚨 Prijsopgave van Willemijn Stoffels maakt zo'n 1.100 offertes per maand voor 52 hoveniers- en bestratingsbedrijven. Een hovenier in Alphen aan den Rijn meldde dat een offerte van € 14.000 verdween nadat hij die had opgeslagen. Hij maakte haar opnieuw, verloor de klus aan een concurrent - en zei dat hij overwoog te vertrekken. 😳

Ze kon het niet onderzoeken. De logs waren ongestructureerde tekst, 24 uur bewaard, en de melding kwam vier dagen later. Daarom kunnen de meeste logs de vraag die ertoe doet niet beantwoorden:

❌ Printstatements in plaats van gestructureerde logregels
❌ Geen request-ID - geen manier om de middag van één klant te vinden
❌ Een bewaartermijn van 24 uur, korter dan de tijd die een klant nodig heeft om iets te melden
❌ Volledige formulierinhoud gelogd, inclusief adressen van klanten

✅ Gestructureerde logs met gebeurtenis, ernst, request-ID, gebruiker en account op elke regel
✅ Request-ID's meegenomen in databaseaanroepen, pdf-generatie en achtergrondtaken
✅ Gevoelige velden op naam opgeschoond, 30 dagen bewaartermijn, en een audittabel van twee jaar voor inlogs, statuswijzigingen en exports
✅ Error tracking met release-, gebruikers- en verzoekcontext - en een korte referentiecode in elke foutmelding voor gebruikers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat u kunt onderzoeken wat er vorige week gebeurde. 🔎

💡 Het resultaat: na twee werkdagen en € 2.000 werd drie weken later een identieke mislukking volledig vastgelegd - een pdf-time-out die "geslaagd" teruggaf terwijl het opslaan werd teruggedraaid - en in een middag opgelost. De hovenier bleef, omdat hij een specifieke uitleg en een referentienummer kreeg. 🚀

👉 Logs die u kunt doorzoeken wanneer het ertoe doet: https://launchstudio.eu/nl/blog/lovable-hosting-logs-you-can-search-when-it-matters

#Logging #Observability #SaaS #Lovable #LaunchStudio #Manifera
