🚨 Inkoopportaal van Jelmer Ottevanger verbindt 19 groothandels met zo'n 300 winkeliers. Vroeg in de bouw liep een AI-sessie tegen een rechtenfout aan bij een beheerrapport — en "loste" die op met de service role-sleutel van Supabase, met een publiek voorvoegsel zodat hij in de browser draaide. 😳

Die sleutel — die de prijzen van elke groothandel kan lezen — stond zes maanden in een bestand dat iedereen kon downloaden. Zo lekken sleutels en breken deploys door configuratie:

❌ Een geheim voor de server met een publiek VITE_-voorvoegsel, ingecompileerd in elke bundel
❌ Een sleutel van de e-mailprovider die op dezelfde manier lekte
❌ Staging die de database en e-mailgegevens van productie deelde
❌ Geen lijst van vereiste variabelen en geen controle of ze zijn ingesteld

✅ De service role-sleutel direct vervangen — vóór al het andere
✅ Het beheerrapport herschreven als functie op de server met correcte autorisatie
✅ Drie volledig gescheiden omgevingen, een voorbeeldbestand en een opstartcontrole op elf vereiste variabelen
✅ Beveiligde preview-deployments en een buildstap die op geheimen scant en de build laat falen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, doorzoeken we uw live bundel op geheimen — dat kost vijf minuten. 🔑

💡 Het resultaat: na één werkdag en € 1.700 waren beide sleutels vervangen, zonder aanwijzing van misbruik — "geluk, geen resultaat". Zes weken later blokkeerde de buildscan een nieuwe AI-sessie die precies dezelfde fout maakte. 🚀

👉 Omgevingsvariabelen in drie omgevingen: https://launchstudio.eu/nl/blog/lovable-hosting-environment-variables-across-three-environments

#Geheimen #DevOps #Supabase #Lovable #LaunchStudio #Manifera
