🚨 Zorgrooster van Thomas van Leeuwen regelt roosters voor 23 thuiszorgorganisaties — zo'n 1.400 zorgverleners. Toen tekende hij een regionale zorggroep met 2.600 zorgverleners, bijna een verdubbeling, met livegang op een maandag. Hun diensten beginnen om 7:00, en de meeste zorgverleners openen de app tussen 6:45 en 7:15. 😳

Een loadtest op drie keer de omvang van de zorggroep faalde zwaar: het rooster duurde 9,8 seconden op p95, verbindingen begonnen te falen bij zo'n 400 gebruikers, en de nachtelijke urenberekening duurde zes uur — klaar nadat de ochtendpiek was begonnen. Zo test u de belasting voordat een grote klant instapt:

❌ Een roosterquery die veel meer ophaalde dan de week van één zorgverlener, met ontbrekende indexen
❌ Een hulpfunctie voor row level security die per rij een subquery draaide
❌ Edge functions die rechtstreeks verbinding maakten met de database in plaats van via de pooler
❌ Pushmeldingen verstuurd binnen het verzoek, en een nachtelijke taak die niet meeschaalde

✅ De piek van de klant gemodelleerd op hun echte dienststart, met gegenereerde data op 3x hun omvang
✅ Realistische k6-load- en piektests met 900 binnenkomende zorgverleners, denktijd en grenswaarden voor slagen of falen
✅ Eén RPC per zorgverlener-week met samengestelde indexen, een stable security definer-functie voor RLS, en de transaction pooler
✅ Meldingen via een wachtrij, de nachtelijke taak in batches en parallel, en pas daarna een grotere database

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, doen we deze generale repetitie vóór de onboarding die er het meest toe doet. ⚙️

💡 Het resultaat: € 5.400, vijf werkdagen. Laatste test: rooster-p95 van 420 ms bij 3x de piek, geen fouten, nachtelijke taak in 35 minuten. 2.600 zorgverleners begonnen op een maandag zonder één klacht over snelheid — voor zo'n € 110 per maand extra. 🚀

👉 Lovable hosting: belastingtests voordat een grote klant instapt: https://launchstudio.eu/nl/blog/lovable-hosting-load-testing-before-a-large-customer-onboards

#Loadtesting #Prestaties #Supabase #SaaS #LaunchStudio #Manifera
