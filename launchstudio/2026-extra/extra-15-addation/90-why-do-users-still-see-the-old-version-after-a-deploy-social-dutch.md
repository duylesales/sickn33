🚨 Noor El Amrani bouwde Marktkraam met Lovable en Supabase: een PWA waarmee zo'n 180 marktkooplieden op hun telefoon verkopen vastleggen, voorraad bijhouden en dagomzet zien. Een bug berekende de btw op sommige artikelen verkeerd. Noor repareerde het en deployde binnen het uur. Vijf dagen later meldden kooplieden nog steeds verkeerde totalen. 😳

Sommige kooplieden draaiden de nieuwe versie, anderen de oude - en de oude bleef verkeerde btw in de database schrijven. Waarom gebruikers na een deploy nog de oude versie zien: 🧠

❌ Een service worker die index.html cache-first bewaarde en nooit op updates controleerde
❌ Een Cloudflare-regel "cache everything" die HTML vier uur cachete
❌ Dezelfde cacheheader van een week op elk bestand
❌ Btw berekend op de client, zodat verouderde apps verkeerde totalen schreven

✅ Workbox met updatecontrole bij het openen en een knop "Nieuwe versie beschikbaar"
✅ HTML bij elk request opnieuw gevalideerd, gehashte bestanden een jaar gecachet, HTML uitgezonderd in Cloudflare
✅ Een versiecontrole zodra de app weer focus krijgt, en de versie zichtbaar in de instellingen
✅ Btw berekend op de server, met getroffen records opnieuw berekend

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw fixes uw gebruikers ook echt bereiken. 🛠️

💡 Het resultaat: €1.800, 5 werkdagen. De volgende release bereikte binnen een dag meer dan 95% van de actieve kooplieden, zonder dat iemand een cache hoefde te legen. 🚀

👉 Een fix gedeployd die niemand ziet? Zo werkt caching: https://launchstudio.eu/nl/blog/why-do-users-still-see-the-old-version-after-a-deploy

#PWA #Caching #ServiceWorker #Cloudflare #AIFounder #LaunchStudio #Manifera
