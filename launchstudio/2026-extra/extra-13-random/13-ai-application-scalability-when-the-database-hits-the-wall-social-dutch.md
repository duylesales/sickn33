🚨 Koen Hendriks, bibliothecaris in Enschede, bouwde Leesclub op Replit: leesclubs plannen bijeenkomsten, houden de voortgang per hoofdstuk bij en bespreken boeken. Via bibliotheeknetwerken groeide het naar ~1.900 clubs en 14.000 lezers. Toen begon de zondagavond het te breken - traag, daarna fouten. Hij upgradede twee keer naar grotere machines. Er veranderde niets. 😳

De servers waren in orde. De database niet: elk verzoek opende een nieuwe Postgres-verbinding, discussiepagina's draaiden één query per reactie, een tabel met 3,2 miljoen rijen had geen index op club of gebruiker, en elke voortgangsupdate vocht om één tellerrij. Daarom loopt de schaalbaarheid van AI-apps eerst vast in de database:

❌ Verbindingen uitgeput binnen minuten na de zondagse piek
❌ N+1-query's - één per reactie om de auteur op te halen
❌ Geen indexen op de kolommen waarop elke query filterde
❌ Een teller op een "hete rij" waardoor leden van grote clubs in de rij stonden

✅ Connection pooling en één gedeelde client per functie
✅ Reacties en auteurs in één query opgehaald
✅ Vier indexen op basis van de traagste echte query's
✅ De teller vervangen door een gecachete berekende waarde, en meldingen ouder dan 90 dagen gearchiveerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, meten we de database voordat iemand een grotere server koopt. ⚙️

💡 Het resultaat: € 2.800, negen werkdagen. De fouten op zondag verdwenen volledig, de discussiepagina ging van ~3,5 s naar 180 ms, en de hostingkosten daalden met ongeveer 35% toen de onnodige upgrades waren teruggedraaid. 🚀

👉 Schaalbaarheid van AI-applicaties: wanneer je database tegen de muur loopt: https://launchstudio.eu/nl/blog/ai-application-scalability-when-the-database-hits-the-wall

#Postgres #Schaalbaarheid #Replit #Supabase #LaunchStudio #Manifera
