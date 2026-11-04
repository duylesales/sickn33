🚨 Emma Lambrecht, museumeducator in Brugge, bouwde Zaalgids met Bolt: een audiotour die bezoekers openen door een QR-code naast elk kunstwerk te scannen, met tekst, audio en een quiz voor kinderen. In de preview van Bolt was hij vlekkeloos. Op Netlify ging hij op de allereerste testdag op drie manieren kapot. 😳

Elke QR-code wees naar een pagina die volgens de server niet bestond. In de preview had hij altijd bestaan. Dit ging er mis:

❌ Elke zaallink vanuit een QR-code gaf een 404 - geen rewrite-regel voor de SPA op de host
❌ Audiobestanden laadden niet: hun opslag-URL bestond alleen in haar Bolt-sessie
❌ Quizscores werden niet opgeslagen - het productiedomein ontbrak in de toegestane URL's van Supabase
❌ Dezelfde ontbrekende URL brak het inloggen voor medewerkers

✅ Rewrites op Netlify, zodat elke route door index.html wordt geserveerd
✅ Omgevingsvariabelen per omgeving ingesteld
✅ Productie- en previewdomein toegevoegd aan de instellingen van Supabase Auth
✅ Audio in een bucket met CDN en caching voor de zwakke wifi in het museum, offline caching voor de tourteksten en automatische controles van de QR-routes bij elke deployment

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar deploymentwerk op Netlify, Vercel, AWS en Azure, dichten we het gat tussen "werkt in de preview" en "werkt voor bezoekers". 🛠️

💡 Het resultaat: €1.600, zes werkdagen. Zaalgids ging live voor de zomertentoonstelling, en bezoekers startten in twaalf weken ongeveer 9.600 tours - met audio die zelfs in de kelderzalen laadde. 🚀

👉 Bolt-app kapot na deployment? Dit zijn de zeven oorzaken en hoe u elke oorzaak oplost: https://launchstudio.eu/nl/blog/why-does-my-bolt-app-break-after-deploy

#Bolt #Netlify #Vite #Deployment #LaunchStudio #Manifera
