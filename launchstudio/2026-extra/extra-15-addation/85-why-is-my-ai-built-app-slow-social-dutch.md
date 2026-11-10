🚨 Lisanne de Groot bouwde Kookschrift met Lovable en Supabase: thuiskoks delen recepten, bewaren favorieten en plannen weekmenu's. Via Instagram groeide het naar zo'n 15.000 gebruikers. Toen noemden reviews de traagheid - en de meeste mobiele bezoekers vertrokken voordat de receptpagina geladen was, wat op 4G tot elf seconden duurde. 😳

Er stapelden zich meerdere oorzaken op. Waarom door AI gebouwde apps traag worden, en wat helpt: 🧠

❌ Telefoonfoto's van zo'n 6 MB op volle grootte, zelfs in thumbnailrasters
❌ Drie chartbibliotheken en een rich-text-editor op elke pagina geladen
❌ De receptenlijst laadde elke kolom en filterde in de browser
❌ Aparte requests per kaart voor auteur, likes en bewaard-status, en geen index op user_id

✅ Verkleinen bij upload met thumbnail-, middelgrote en grote varianten via een CDN met lazy loading
✅ Zware bibliotheken alleen waar ze nodig zijn, en één chartbibliotheek in plaats van drie
✅ Een databaseview met kaartvelden, auteursnamen, likes en bewaard-status in één gepagineerde query
✅ Indexen voor favorieten, likes en filters, plus full-text search

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vinden we de paar knelpunten die ertoe doen en lossen we ze op zonder alles te herschrijven. 🛠️

💡 Het resultaat: €2.600, 7 werkdagen. De receptpagina laadt nu in zo'n 1,5 seconde op 4G, de lijst in minder dan een seconde, en de beoordelingen in de app stores herstelden binnen twee maanden. 🚀

👉 Is uw door AI gebouwde app traag? Dit zijn de oorzaken en de oplossingen: https://launchstudio.eu/nl/blog/why-is-my-ai-built-app-slow

#Performance #WebVitals #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
