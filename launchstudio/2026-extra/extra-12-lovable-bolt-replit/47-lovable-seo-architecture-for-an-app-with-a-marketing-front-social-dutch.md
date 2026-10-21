🚨 Voorraadslim van Jasmijn Kolthof regelt voorraadbeheer voor 130 zelfstandige winkeliers en webshops, bijna allemaal gevonden via een Facebookgroep. Ze had in een jaar elf artikelen geschreven. Geen ervan verscheen in de zoekresultaten. Haar homepage rankte niet eens op haar eigen productnaam. 😳

De server stuurde elke bezoeker dezelfde lege container en een script; browsers vulden de woorden in. Ondertussen waren vier pagina's van de ingelogde app geïndexeerd — een ervan met de titel "Loading...". Zo richt u de architectuur in van een app met een marketingvoorkant:

❌ Publieke pagina's die alleen in de browser werden opgebouwd
❌ Interne links als JavaScript-klikhandlers, onzichtbaar voor crawlers
❌ 40 app-routes indexeerbaar, plus drie preview-deployments geïndexeerd als volledige duplicaten
❌ Dezelfde inhoud op vier URL-variaties — en helemaal geen prijspagina

✅ Publieke pagina's statisch gegenereerd, zodat de server volledige HTML teruggeeft
✅ Echte ankerlinks, de app onder /app met een noindex-instructie, en beschermde previews
✅ Eén canonieke URL met permanente doorverwijzingen, een sitemap uit echte routes, en gestructureerde data voor artikelen
✅ De index opgeschoond via de zoekconsole, plus een prijspagina met echte prijzen en een over-pagina

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we wat een zoekmachine echt op uw homepage ziet — soms is dat niets. 🔎

💡 Het resultaat: na vier werkdagen en € 3.500 waren binnen acht weken negen van de elf artikelen geïndexeerd en gingen de organische bezoeken van 40 naar 610 per maand. Twee artikelen leveren nu meer proefaanmeldingen op dan de Facebookgroep. 🚀

👉 SEO-architectuur voor een app met een marketingvoorkant: https://launchstudio.eu/nl/blog/lovable-seo-architecture-for-an-app-with-a-marketing-front

#SEO #Lovable #TechnischeSEO #SaaS #LaunchStudio #Manifera
