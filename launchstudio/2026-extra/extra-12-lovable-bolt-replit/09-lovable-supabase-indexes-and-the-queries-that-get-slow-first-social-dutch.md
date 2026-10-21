🚨 Verzuimlijn van Wendy Roos verzorgt de verzuimregistratie voor 140 werkgevers met samen zo'n 4.000 werknemers. Acht maanden ging het goed. Toen begon het dashboard — het eerste scherm dat elke gebruiker opent — vier tot zes seconden te duren, het ergst tussen negen en tien uur 's ochtends. Eén klant vroeg of het product hun omvang wel aankon. 😳

De verzuimtabel had 310.000 rijen en precies één index: de primaire sleutel. Dit wordt als eerste traag als uw data groeit:

❌ Geen indexen op foreign keys — elk filter las de hele tabel
❌ Een dashboardquery die voor elke gebruiker 310.000 rijen scande en sorteerde
❌ Een N+1-patroon: 25 rijen, die elk afzonderlijk hun werknemer ophaalden
❌ Een totaal aantal rijen op een lijstpagina dat meegroeide met de data

✅ Querystatistieken gerangschikt op totale tijd — het dashboard gebruikte 71% van de databasetijd
✅ Een samengestelde index op werkgever en datum, gelijktijdig opgebouwd via een migratie
✅ Indexen op de zes foreign-key-kolommen die er geen hadden, en de N+1-opvraging herschreven als één query
✅ Het totaal vervangen door een knop voor de volgende pagina — en ongebruikte indexen na een maand verwijderd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zoeken we uit of uw trage pagina aan indexen of aan queries ligt — meestal in uren, zonder herbouw. ⚡

💡 Het resultaat: na twee werkdagen en € 1.600 ging het dashboard van 4,2 seconden tijdens de piek naar 180 milliseconden, op hetzelfde plan. De database-CPU tijdens de piek daalde van boven de 80% naar onder de 15% — waardoor een upgrade van € 340 per maand niet meer nodig was. 🚀

👉 Indexen en de queries die als eerste traag worden: https://launchstudio.eu/nl/blog/lovable-supabase-indexes-and-the-queries-that-get-slow-first

#Supabase #PostgreSQL #Prestaties #Lovable #LaunchStudio #Manifera
