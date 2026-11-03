🚨 Maarten Oosterhuis heeft een installatiebedrijf voor warmtepompen in Zwolle. Hij bouwde Offertewerk in Bolt.new zodat monteurs aan de keukentafel van de klant offertes konden maken op een tablet. In de Bolt-preview: perfect. Op Netlify: drie dingen tegelijk kapot. 😳

Bolt draait uw app in een browsersandbox die vergeeft wat echte servers niet vergeven. Dit ging er mis toen Offertewerk het browsertabblad verliet:

❌ Build faalde op twee imports die alleen in hoofdletters verschilden
❌ Elke pagina behalve de homepage gaf een 404 bij verversen
❌ Pdf's genereren faalde stil - de API-sleutel bestond alleen in zijn Bolt-sessie
❌ Monteurs konden elkaars offertes zien

✅ Importpaden hersteld, plus een lintregel tegen hoofdletterfouten
✅ SPA-rewrites ingesteld op Netlify
✅ Pdf-aanroepen naar een serverless functie met de sleutel als omgevingsvariabele
✅ Row Level Security per monteur en een stagingsite voor Bolt-wijzigingen

Bij **LaunchStudio**, aangedreven door Manifera's 11+ jaar engineering, zetten we Bolt-apps live tegen een vaste prijs - zonder uw stack te vervangen. ⚙️

💡 Het resultaat: €1.850, live in acht werkdagen. Vier monteurs maakten dat stookseizoen zo'n 620 offertes ter plaatse, en vrijwel elke offerte gaat nu dezelfde dag de deur uit. 🚀

👉 Waarom Bolt-apps buiten Bolt breken, en hoe u de uwe live zet: https://launchstudio.eu/nl/blog/bolt-new-app-to-production-fixed-price-launch-service

#BoltNew #Netlify #AIApp #Deployment #LaunchStudio #Manifera
