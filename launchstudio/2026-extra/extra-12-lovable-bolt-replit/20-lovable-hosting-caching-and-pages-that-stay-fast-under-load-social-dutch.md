🚨 Tuincentrumgids van Noor Vreugdenhil is een gids van tuincentra en kwekerijen in heel Nederland, gefinancierd door 120 uitgelichte bedrijven. Een tuinprogramma linkte naar een van haar kwekerijen. Het verkeer ging in twee uur van 400 bezoeken per dag naar 9.000 - en de site lag de hele middag plat. 😳

Elke pagina werd voor elke bezoeker opnieuw opgebouwd, met elf databasequeries en foto's van meerdere megabytes. Zo houdt caching pagina's snel onder belasting:

❌ Pagina's die al weken niet waren veranderd, bij elk verzoek opnieuw opgebouwd
❌ Foto's op volle resolutie naar elke telefoon - 4,2 MB per vermeldingspagina
❌ Een geauthenticeerd dashboard dat cachebaar was - één randverzoek verwijderd van het lekken van statistieken tussen bedrijven
❌ Een dure aggregatie die voor elke bezoeker opnieuw werd berekend

✅ Publieke pagina's 15 minuten gecachet op het CDN, met hervalidatie op de achtergrond
✅ Een levensduur van een jaar voor statische bestanden met vingerafdruk
✅ Het bedrijfsdashboard expliciet gemarkeerd als private en no-store
✅ Afbeeldingen op weergaveformaat in moderne formaten (310 KB per pagina), plus legen van de cache als eigenaren hun vermelding bewerken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw app niet negenduizend keer dezelfde pagina opbouwt. ⚡

💡 Het resultaat: na één werkdag en € 1.800 daalde het aantal verzoeken naar de applicatie met 94% bij hetzelfde verkeer. Toen een tweede programma het onderwerp in april behandelde, werd de piek volledig vanaf de rand geserveerd - en haar hostingrekening daalde met € 70 per maand. 🚀

👉 Caching en pagina's die snel blijven onder belasting: https://launchstudio.eu/nl/blog/lovable-hosting-caching-and-pages-that-stay-fast-under-load

#Caching #CDN #Webprestaties #Lovable #LaunchStudio #Manifera
