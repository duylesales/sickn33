🚨 Rik Smeets bouwde Kapperplanner met Lovable en Supabase: online afspraken voor kapsalons. Om het sneller te maken, zette een vriend Cloudflare voor alles, met een "Cache Everything"-regel en Flexible SSL. Binnen enkele dagen zag een saloneigenaar de afspraken van een andere salon - met namen en telefoonnummers van klanten. 😳

Medewerkers kwamen ook in inlog-loops, Mollie-webhooks voor aanbetalingen werden geblokkeerd door botbescherming en bots maakten nepafspraken. Zo zet u Cloudflare voor uw door AI gebouwde app zonder iets te breken: 🧠

❌ Flexible SSL dat inlog-loops veroorzaakte
❌ Een cacheregel die het dashboard van de ene salon aan een andere toonde
❌ Botbescherming die Mollie-webhooks blokkeerde
❌ Nepafspraken van bots op openbare boekingspagina's

✅ SSL ingesteld op Full (strict)
✅ Caching beperkt tot statische bestanden, app-responses op private, no-store, caches geleegd
✅ Webhookpaden uitgezonderd van challenges en beschermd met handtekeningverificatie
✅ Turnstile op het boekingsformulier, rate limits op inloggen en boeken, en een incidentbeoordeling

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we Cloudflare allebei de taken doen die het moet doen: sneller en veiliger. 🛠️

💡 Het resultaat: €1.900, 5 werkdagen. Inlog-loops en het lekken tussen salons stopten direct, aanbetalingen werden weer betrouwbaar verwerkt en botboekingen daalden tot bijna nul. 🚀

👉 Gebruikt u Cloudflare bij uw app? Zo configureert u het veilig: https://launchstudio.eu/nl/blog/cloudflare-in-front-of-your-ai-built-app

#Cloudflare #WebSecurity #Lovable #Caching #AIFounder #LaunchStudio #Manifera
