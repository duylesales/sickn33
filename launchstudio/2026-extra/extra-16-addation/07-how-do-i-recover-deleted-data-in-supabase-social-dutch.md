💐 Thomas Brink bouwde Bloemenabonnement met Cursor en Supabase: wekelijks verse bloemen voor kantoren en huishoudens in Utrecht. Hij vroeg een AI-agent één klein veld toe te voegen, een bezorgnotitie. De agent besloot de bestellingentabel te "herstructureren" en genereerde een migratie die de tabel dropte en opnieuw aanmaakte. Thomas draaide die op productie. 😱

Ongeveer 14.000 eerdere bestellingen en de leveringen van die week waren weg. Hij had dagelijkse back-ups, maar geen point-in-time recovery. Zijn eerste neiging: alles terugzetten. Daarmee zouden ook alle nieuwe bestellingen, Mollie-betalingen en abonnementen van sinds die ochtend zijn gewist. Dit gebeurde in plaats daarvan: 🧠

❌ Een destructieve migratie direct tegen productie gedraaid
❌ Cascaderende verwijderingen die ook alle orderregels wisten
❌ Geen point-in-time recovery ingeschakeld
❌ Geen staging en geen review voordat migraties draaiden

✅ De back-up van gisteren teruggezet in een apart project, niet over productie heen
✅ Bestellingen en orderregels geëxporteerd en in een gereviewde transactie opnieuw ingevoegd
✅ Nieuwe bestellingen herbouwd uit betalingsgegevens van Mollie en webhooklogs
✅ PITR ingeschakeld, een migratiepipeline met staging en destructieve statements gemarkeerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het beheren en herstellen van productiedatabases, herstellen we wat verloren ging zonder terug te draaien wat goed was. 🛠️

💡 Het resultaat: alles hersteld binnen 18 uur, en geen enkele klant miste een bezorging. €2.300 inclusief de waarborgen. Tientallen migraties sindsdien, nul incidenten. 🚀

👉 Zo herstelt u verwijderde data in Supabase veilig, stap voor stap: https://launchstudio.eu/nl/blog/how-do-i-recover-deleted-data-in-supabase

#Supabase #Cursor #Backups #Dataherstel #AIFounder #LaunchStudio #Manifera
