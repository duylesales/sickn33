🚨 Verbruik van Maartje Klaassen monitort het energieverbruik voor zes woningcorporaties en twee vastgoedbeheerders rond Almelo en Hengelo - zo'n 11.000 woningen. Achttien maanden ging het goed. Toen werd het op de eerste werkdag van elke maand zo'n veertig minuten onbruikbaar. 😳

Ze dacht aan een hostingprobleem. Het waren negen getallen op een dashboard, die elk 7,4 miljoen rijen lazen. Zo haalt rapportage ongemerkt een product onderuit:

❌ Negen dashboardcijfers live berekend, elk met een scan over de volledige tabel met meterstanden
❌ Geen index op datum of corporatie - ook niet op de kolommen waarop de toegangsregels filteren
❌ Eén query per gebouw: 340 round trips voor de grootste corporatie
❌ Een jaarexport die alles in het geheugen laadde en bij de twee grootste klanten stil mislukte

✅ Queryplannen vastgelegd voor elk dashboardonderdeel, om de scans precies te vinden
✅ Indexen op corporatie, datum en meter - inclusief de policy-kolommen - waardoor het dashboard van 47 naar 4 seconden ging
✅ Een dagelijkse samenvattingstabel die het onder één seconde bracht, met de queries per gebouw samengevoegd tot één
✅ Exports als achtergrondtaak, geleverd via een ondertekende link, een aparte connection pool voor rapportage, en meldingen bij trage queries

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we rapportage snel zonder de rest van uw product te vertragen. 📊

💡 Het resultaat: na negen werkdagen en € 4.600 - geen incident aan het begin van de maand in elf maanden, de twee corporaties die rapporten met de hand samenstelden zijn daarmee gestopt, en één noemde de export bij een contractverlenging. 🚀

👉 Rapportagequeries in Lovable + Supabase die u niet vertragen: https://launchstudio.eu/nl/blog/lovable-supabase-reporting-queries-that-do-not-slow-you

#Supabase #Lovable #Performance #PostgreSQL #LaunchStudio #Manifera
