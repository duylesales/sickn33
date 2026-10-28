🚨 Hidde Kwakernaak bouwde Ritmeester met Bolt - stalbeheer voor zes manegebedrijven in Gelderland en Utrecht: paarden, eigenaren, stallen, voer, dierenartsafspraken en facturatie. Hij vroeg de tool scherm voor scherm een database toe te voegen. Na drie weken: 19 tabellen. 😳

Paarden stonden in twee tabellen, gegevens van eigenaren in drie, met verschillende waarden. Geen foreign keys, geen row-level security. Toen het tweede manegebedrijf het ging gebruiken, verschenen hun paarden in de stallenlijst van het eerste. Zo sluit u data aan op een Bolt-prototype:

❌ De tool het schema laten afleiden van welk scherm toevallig eerst kwam
❌ 19 tabellen voor een bedrijf met vijf echte dingen
❌ Geen RLS, geen foreign keys, geen constraints
❌ Terugvallen op nepdata die stilletjes paarden toonden die niet bestonden

✅ Eerst het bedrijf beschreven: vijf kernentiteiten plus facturatie, met tenantmodel, ID's en naamgeving vooraf bepaald
✅ 19 tabellen samengevoegd tot 8, met dubbele paarden en eigenaren met de hand afgestemd
✅ RLS-policies op elke tabel, getest met twee manegebedrijven, plus foreign keys (40 wezen gevonden) en constraints
✅ Een realistische seed van 400 paarden, nepdata verwijderd, migraties gecommit en types opnieuw gegenereerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, ontwerpen we uw schema voordat er iets tegen wordt gegenereerd. 🗄️

💡 Het resultaat: na drie werkdagen en € 3.200 was het lek tussen manegebedrijven structureel gedicht. Elk nieuw bedrijf daarna kostte een dag om aan te sluiten in plaats van een week, omdat er niets hoefde te worden afgestemd. 🚀

👉 Data aansluiten op een Bolt-prototype: https://launchstudio.eu/nl/blog/bolt-and-supabase-wiring-data-into-a-bolt-prototype

#Bolt #Supabase #Databaseontwerp #Prototyping #LaunchStudio #Manifera
