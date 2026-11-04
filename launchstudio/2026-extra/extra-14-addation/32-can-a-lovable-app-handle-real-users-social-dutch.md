🚨 Stijn Koster heeft yogastudio's in Deventer en bouwde Lesrooster in Lovable: leden boeken lessen, docenten zien de aanwezigheid, leden volgen hun tegoed. Een jaar liep het soepel met ongeveer 900 leden. Toen voegde een samenwerking twee studio's en 1.400 leden toe - en werden maandagochtenden pijnlijk. 😳

Een boeking duurde acht tot twaalf seconden, sommige verzoeken liepen vast, en Stijn stond op het punt alles opnieuw te bouwen omdat "Lovable niet schaalt". Het bleken drie queries en één policy:

❌ Een roosterpagina die alle lessen, alle boekingen en het tegoed van elk lid in de browser laadde
❌ Filteren in de browser in plaats van in de database
❌ Geen indexen op de tabel met boekingen naast de primaire sleutel
❌ Een RLS-policy die voor elke rij een subquery op het studiolidmaatschap draaide

✅ Een databasefunctie die alleen de lessen van deze week en de eigen boekingen van het lid teruggeeft
✅ Indexen op lesdatum, studio en lid
✅ De RLS-policy herschreven met een geïndexeerde hulpfunctie
✅ Gepagineerde lesgeschiedenis en een belastingtest met 300 leden die binnen vijf minuten boeken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar optimaliseren van enterprisedatabases, repareren we hoe uw app data opvraagt voordat iemand een herbouw of een groter abonnement voorstelt. 🛠️

💡 Het resultaat: €1.900, zes werkdagen. De boekingstijd op maandag daalde naar minder dan een halve seconde, het Supabase-abonnement bleef hetzelfde, en Lesrooster groeide sindsdien naar zes studio's. 🚀

👉 Kan een Lovable-app echte gebruikers aan? Hier schaalt hij en hier komt hij onder druk: https://launchstudio.eu/nl/blog/can-a-lovable-app-handle-real-users

#Lovable #Supabase #Prestaties #Schalen #LaunchStudio #Manifera
