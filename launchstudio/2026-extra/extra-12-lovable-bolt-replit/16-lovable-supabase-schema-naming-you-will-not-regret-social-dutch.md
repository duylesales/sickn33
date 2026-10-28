🚨 Serviceplan van Barend Kloosterman beheert onderhoudscontracten voor 44 installatiebedrijven - zo'n 9.000 serviceadressen. Een installateur paste het adres van een klant aan in het portaal. De factuur van die avond had het oude adres. De monteur werd naar een derde adres gestuurd. 😳

Klanten stonden in drie tabellen - clients, customers en contacts - omdat elk verzoek om een functie een nieuwe tabel had opgeleverd. Dit kost inconsistente schemanaamgeving echt:

❌ Drie tabellen voor dezelfde klant, elk met een ander antwoord
❌ Een kommagescheiden tekstkolom in plaats van een echte tabel
❌ Negen ontbrekende foreign keys die 340 verweesde records verborgen
❌ Geld opgeslagen als kommagetal - en een factuurverschil van één cent dat niemand kon verklaren

✅ Een volledige schema-inventarisatie en een conventiebestand in de repository, inclusief de woordenschat van het product
✅ Drie klanttabellen samengevoegd tot één, gemigreerd zonder downtime (toevoegen, naar beide schrijven, lezen omzetten, verwijderen)
✅ Foreign keys gedeclareerd, wezen opgelost, tijdstempels tijdzonebewust gemaakt
✅ Geldkolommen hernoemd en opgeslagen als gehele centen, met gegenereerde types opnieuw gegenereerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, ruimen we door AI gebouwde schema's op zodat elke wijziging daarna sneller gaat. 🗂️

💡 Het resultaat: na vier werkdagen en € 3.400 werd de fout met de drie adressen structureel onmogelijk. Een opdrachtnemer die de maand erna begon, was op dag één productief - en zijn AI-sessies stopten met het verzinnen van nieuwe kolomnamen. 🚀

👉 Schemanaamgeving waar u geen spijt van krijgt: https://launchstudio.eu/nl/blog/lovable-supabase-schema-naming-you-will-not-regret

#Supabase #Databaseontwerp #TechnischeSchuld #Lovable #LaunchStudio #Manifera
