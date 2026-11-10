🚨 Iris Kok bouwde Akteslim met Claude Code: een dienst voor notariskantoren en juridische kantoren die kerngegevens uit gescande aktes en contracten haalt, met een Python-API voor OCR en AI-extractie. Claude Code schreef een Dockerfile, en Iris zette die op een gehuurde server volgens een tutorial. 😳

De image was meer dan 2 GB, deploys duurden twintig minuten en de API-sleutels zaten in de image ingebakken. Wanneer uw app een container nodig heeft - en hoe u Docker goed inzet: 🧠

❌ Een image van 2 GB met buildtools, testdata en de volledige repo-geschiedenis
❌ De container draaide als root, met sleutels gekopieerd uit een .env-bestand
❌ Een maanden oude latest-basisimage en een poort zonder TLS open
❌ Logs die bij elke herstart verdwenen, en stille geheugencrashes bij grote pdf's

✅ Een multi-stage build op een vastgepinde slim-image, terug naar zo'n 400 MB, als non-root
✅ Sleutels geroteerd en verplaatst naar omgevingsvariabelen bij runtime
✅ Scans op kwetsbaarheden in images in een GitHub Actions-pipeline
✅ Een managed containerplatform in de EU met TLS, health checks, geheugenlimieten, een jobwachtrij en centrale logs

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van een container die werkt een container die u kunt vertrouwen met klantdata. 🛠️

💡 Het resultaat: €3.900, 10 werkdagen. Deploys duren nu minder dan drie minuten, geheugencrashes zijn verdwenen en Akteslim doorstond de IT-beveiligingsreview van een notarisgroep. 🚀

👉 Heeft uw app Docker nodig? Dit moeten oprichters weten: https://launchstudio.eu/nl/blog/docker-for-founders-when-your-app-needs-a-container

#Docker #Containers #ClaudeCode #LegalTech #AIFounder #LaunchStudio #Manifera
