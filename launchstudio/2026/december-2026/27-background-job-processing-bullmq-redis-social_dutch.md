# Social Media Post (Dutch): Background Job Processing for AI Workloads with BullMQ and Redis

Vercel API-routes hebben een time-outlimiet van 10-60 seconden.
Als uw AI-app een video van 2 uur analyseert, audio transcribeert, of de volledige website van een bedrijf scraapt, zal het HTTP-verzoek crashen en ziet uw gebruiker een 504 Gateway Timeout.

U kunt zware AI-workloads niet synchroon uitvoeren.

U moet een asynchrone wachtrij-architectuur bouwen:
1️⃣ De Gebruiker klikt op "Analyseer".
2️⃣ Next.js plaatst een taak in een **Upstash Redis**-wachtrij en retourneert onmiddellijk `{"status": "processing"}` naar de frontend.
3️⃣ Een langlopende Docker-container (gehost op Fly.io) met een **BullMQ** Worker haalt de taak op. Het werkt 25 minuten lang zonder time-outs.
4️⃣ Als OpenAI een `429 Too Many Requests` fout geeft, verwerkt BullMQ automatisch exponentiële nieuwe pogingen.

Stop met het laten crashen van de browsers van uw gebruikers. Lees onze volledige technische gids op de LaunchStudio blog.

#LaunchStudio #Redis #BullMQ #AISaaS #Nextjs #Vercel #Architecture
