---
Titel: "Waarom Gaat Mijn Bolt-App Kapot na Deployment? Zeven Oorzaken en Oplossingen"
Trefwoorden: bolt app kapot na deploy, bolt.new deployfout, bolt netlify 404, bolt app werkt niet in productie, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Waarom Gaat Mijn Bolt-App Kapot na Deployment? Zeven Oorzaken en Oplossingen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Gaat Mijn Bolt-App Kapot na Deployment? Zeven Oorzaken en Oplossingen",
  "description": "Een Bolt-app die in de preview werkt en na deployment kapotgaat, heeft bijna altijd een van zeven oorzaken: ontbrekende omgevingsvariabelen, SPA-routing, hoofdlettergevoelige imports, code die alleen in Node werkt, redirect-URL's voor authenticatie, CORS of verschillen in de build. Elke oorzaak wordt uitgelegd met een oplossing.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-08",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-does-my-bolt-app-break-after-deploy" },
  "citation": [
    { "@type": "CreativeWork", "name": "StackBlitz WebContainers", "url": "https://webcontainers.io/" },
    { "@type": "CreativeWork", "name": "Vite: Env Variables and Modes", "url": "https://vite.dev/guide/env-and-mode" },
    { "@type": "CreativeWork", "name": "Vite: Deploying a Static Site", "url": "https://vite.dev/guide/static-deploy" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A05 Security Misconfiguration", "url": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/" }
  ]
}
</script>

**Kort antwoord:** omdat de preview van Bolt draait in een omgeving in de browser die vergevingsgezinder is dan een echte server. De zeven meest voorkomende oorzaken zijn ontbrekende omgevingsvariabelen, routing van single-page apps op de host, verschillen in hoofdletters in bestandsnamen, code die afhankelijk is van functies die alleen in Node bestaan, redirect-URL's voor authenticatie die nog naar de preview wijzen, cross-origin-beperkingen (CORS) en verschillen tussen de ontwikkelserver en de productiebuild. Elke oorzaak heeft een snelle diagnose en een bekende oplossing.

## Belangrijkste Punten

- **De preview van Bolt draait in StackBlitz WebContainers in uw browser,** die dingen toestaan die echte servers niet toestaan.
- **Zeven oorzaken verklaren de meeste fouten na deployment:** omgevingsvariabelen, SPA-routing, hoofdlettergevoelige imports, code die alleen in Node werkt, redirect-URL's voor authenticatie, CORS en verschillen tussen ontwikkeling en build.
- **Met Vite bereiken alleen variabelen met het voorvoegsel `VITE_` de browser,** en ze worden tijdens de build ingebakken; geheimen mogen dat voorvoegsel nooit gebruiken.
- **Draai de productiebuild lokaal voordat u deployt** (`npm run build` en `npm run preview`) om de meeste problemen vroeg te vangen.
- **Deployment repareren brengt u online; productierijpheid is de volgende laag:** toegangsregels, geheimen, betalingen, staging, back-ups en monitoring.

## 1. Ontbrekende of Verkeerd Benoemde Omgevingsvariabelen

**Symptoom:** leeg scherm, "undefined" in API-URL's, fouten van Supabase of Stripe direct na het laden.
**Waarom:** variabelen die in de Bolt-sessie of een lokaal `.env`-bestand waren ingesteld, zijn nooit aan de host toegevoegd. Met Vite worden alleen variabelen die beginnen met `VITE_` beschikbaar gemaakt voor de browsercode, en ze worden tijdens de build ingevoegd.
**Oplossing:** voeg elke benodigde variabele toe in de instellingen van de host (Netlify, Vercel), met het juiste voorvoegsel voor frontendvariabelen, en bouw opnieuw. Zet nooit geheime sleutels in `VITE_`-variabelen.

## 2. Pagina Niet Gevonden bij het Verversen van een Route

**Symptoom:** de homepage werkt, maar `/dashboard` verversen of een gedeelde link openen geeft een 404.
**Waarom:** de host zoekt een bestand op dat pad. In een single-page app moeten alle routes door `index.html` worden geserveerd.
**Oplossing:** voeg een rewrite-regel toe. Op Netlify een bestand `_redirects` met `/* /index.html 200`. Op Vercel een rewrite in `vercel.json`. Frameworks met server rendering regelen dit anders.

## 3. "Module Not Found" in het Buildlog

**Symptoom:** de build faalt met een importfout voor een bestand dat duidelijk bestaat.
**Waarom:** de import zegt `./components/UserCard`, maar het bestand heet `usercard.tsx`. Sommige omgevingen vergeven verschillen in hoofdletters; Linux-buildservers niet.
**Oplossing:** hernoem bestanden of imports zodat de hoofdletters exact overeenkomen. Een lintregel kan voorkomen dat het opnieuw gebeurt.

## 4. Code die Alleen in Node Werkt

**Symptoom:** fouten zoals `process is not defined`, `fs` of `Buffer` niet beschikbaar, of servercode die tijdens het draaien faalt.
**Waarom:** code die voor een server bedoeld was, is in de frontendbundel terechtgekomen, of een backend verwacht een Node-server die altijd draait terwijl de host statische hosting of serverless functions biedt.
**Oplossing:** verplaats serverlogica naar serverless functions (Netlify Functions, Vercel Functions, Supabase Edge Functions) en houd de frontend vrij van API's die alleen in Node bestaan. Als u een server nodig heeft die altijd draait, kies dan een host die er een draait.

## 5. Inloggen Werkt in de Preview maar Niet in Productie

**Symptoom:** inloggen stuurt terug naar de preview-URL, magic links falen, OAuth toont "redirect URI mismatch".
**Waarom:** Supabase Auth, Google, GitHub of andere providers staan alleen redirects toe naar URL's die u heeft ingesteld. Het productiedomein is nooit toegevoegd.
**Oplossing:** voeg de productie-URL en eventuele preview-URL's toe aan de lijst met toegestane redirects in Supabase en bij elke OAuth-provider. Werk de site-URL in Supabase bij.

## 6. API-Aanroepen Geblokkeerd door CORS

**Symptoom:** netwerkfouten die CORS noemen, verzoeken aan uw eigen API of een API van derden die alleen in productie falen.
**Waarom:** de API staat verzoeken toe vanaf de origin van de preview maar niet vanaf uw domein, of een API van derden hoort helemaal niet vanuit de browser te worden aangeroepen.
**Oplossing:** stel toegestane origins in op uw API of edge functions. Laat aanroepen naar API's van derden met geheime sleutels via een serverfunctie lopen.

## 7. Verschillen tussen Ontwikkelserver en Productiebuild

**Symptoom:** functies gedragen zich anders, stijlen ontbreken, dynamische imports falen.
**Waarom:** de ontwikkelserver compileert op aanvraag; de productiebuild optimaliseert, verwijdert ongebruikte code en splitst code op. Sommige patronen, zoals dynamische importpaden die uit variabelen worden opgebouwd, gedragen zich anders.
**Oplossing:** draai de productiebuild lokaal (`npm run build` en daarna `npm run preview`) voordat u deployt, en los eventuele waarschuwingen op.

## Een Buildlog Lezen Zonder Paniek

Als een deployment faalt, vertelt het buildlog u waarom, maar logs zijn lang en rommelig. Drie tips maken ze leesbaar:

1. **Scrol naar de eerste fout, niet de laatste.** Latere fouten zijn vaak gevolgen van de eerste.
2. **Zoek naar bestandspaden.** "Could not resolve './components/UserCard'" noemt het precieze bestand en de import.
3. **Zoek ook naar "warning".** Waarschuwingen over ontbrekende omgevingsvariabelen of verouderde packages verklaren vaak fouten die pas tijdens het draaien verschijnen.

De eerste fout, samen met het bestand dat erin wordt genoemd, kopiëren naar Bolt, Cursor of een zoekmachine, leidt meestal snel naar de oplossing.

## Verschillen in Omgevingen Uitgelegd

De documentatie van Vite beschrijft hoe omgevingsvariabelen werken: variabelen met het voorvoegsel `VITE_` worden beschikbaar gemaakt voor clientcode en tijdens de build statisch vervangen. Dat heeft twee gevolgen. Ten eerste vraagt het wijzigen van een variabele op uw host om een nieuwe build voordat die effect heeft. Ten tweede is alles met dat voorvoegsel openbaar. Een veelvoorkomend patroon in exports uit Bolt is een geheime sleutel met een naam als `VITE_STRIPE_SECRET`, die leesbaar wordt in de browser van elke bezoeker. Geef geheimen voor de server een naam zonder het voorvoegsel en gebruik ze alleen in serverless functions.

## Routing in Single-Page Apps

Een single-page app heeft één echt HTML-bestand. De router in uw JavaScript bepaalt wat er voor `/dashboard` of `/settings` wordt getoond. Als een gebruiker ververst of een gedeelde link opent, ontvangt de host een verzoek voor `/dashboard` en zoekt hij een bestand op dat pad. Zonder een rewrite-regel die voor onbekende paden `index.html` serveert, geeft de host een 404. Het bestand `_redirects` van Netlify en de rewrites in `vercel.json` van Vercel lossen dit op. Frameworks met server rendering, zoals Next.js, regelen routing anders en hebben deze regel niet nodig.

## Fouten Zichtbaar Maken in Productie

De WebContainer toont fouten in de console van uw editor. In productie ziet niemand de console, behalve de gebruiker die tegen het probleem aanliep. Voeg foutregistratie toe aan de frontend en serverless functions, zodat fouten tijdens het draaien met context aan u worden gemeld, en een uptimecontrole, zodat u weet wanneer de site plat ligt. De SRE-richtlijnen van Google raden aan te alarmeren op symptomen die gebruikers ervaren, zoals fouten en trage reacties; voor een kleine app is een uptimemonitor met foutregistratie en meldingen bij nieuwe soorten fouten genoeg om te beginnen.

## Een Checklist voor Deployment van Bolt-Projecten

- Het project bouwt vanaf een schone kopie met `npm ci && npm run build`
- `npm run preview` serveert de gebouwde app en diepe links werken
- Alle benodigde omgevingsvariabelen staan in `.env.example` en zijn op de host ingesteld
- Geen enkel geheim gebruikt een frontendvoorvoegsel
- Redirect-URL's in Supabase en bij OAuth bevatten het productiedomein
- De rewrite-regel voor de SPA staat erin
- Foutregistratie en uptimemonitoring zijn ingericht

## Wanneer Bolt Niet de Juiste Plek Is om Dingen te Repareren

Sommige oplossingen zijn makkelijker buiten Bolt: bestanden hernoemen met hoofdletterwijzigingen, instellingen van de host aanpassen, CI-controles toevoegen, serverless functions schrijven. Met het project in GitHub kunt u of een developer deze wijzigingen in een gewone editor doen en Bolt blijven gebruiken voor interfacewerk. Houd de code wel in één repository, zodat beide gesynchroniseerd blijven.

## CORS in Gewone Taal

Browsers blokkeren webpagina's die API's op andere domeinen aanroepen, tenzij die API's dat uitdrukkelijk toestaan. Die regel, de same-origin policy, wordt versoepeld via CORS-headers. In de preview van Bolt draaien uw app en de API's mogelijk onder origins die toevallig zijn toegestaan; in productie is uw domein nieuw en staat het mogelijk niet op de lijst. Als u CORS-fouten in de console ziet, controleer dan de toegestane origins op uw eigen API of edge functions, en vraag u af of de aanroep wel vanuit de browser hoort te komen. Aanroepen naar API's van derden die geheime sleutels vereisen, horen via een serverless function te lopen, wat ook het CORS-probleem oplost.

## Wanneer de App Deployt maar Zich Vreemd Gedraagt

Soms slaagt de deployment en laadt de app, maar gedragen functies zich vreemd: data laadt traag, afbeeldingen ontbreken of een formulier wordt twee keer verzonden. Dat komt meestal door verschillen tussen de ontwikkelserver en de geoptimaliseerde productiebuild, zoals code die afhankelijk was van gedrag dat alleen tijdens ontwikkeling bestaat, assets met absolute paden die in productie anders zijn, of effecten die tijdens ontwikkeling twee keer draaien en in productie één keer. Lokaal reproduceren met `npm run build` en `npm run preview` is de snelste manier om het te onderzoeken.

## Voorkomen voor de Volgende Keer

Zodra uw Bolt-app betrouwbaar deployt, houdt u het zo met een CI-pipeline die elke wijziging bouwt en lint, een stagingsite die elke commit van Bolt als eerste ontvangt en een korte checklist voor deployment in uw README. De meeste herhaalde fouten komen van een nieuwe variabele of route die in Bolt is toegevoegd zonder de host bij te werken; de checklist vangt ze in seconden.

## Houd een Logboek van Deployments Bij

Schrijf elk deploymentprobleem dat u tegenkomt op, en hoe u het heeft opgelost, in een kort bestand in uw repository. Na een paar weken wordt dat logboek de meest praktische documentatie die uw project heeft.

## Tabel voor een Snelle Diagnose

| Wat u ziet | Waar u kijkt |
| --- | --- |
| Lege pagina, consolefouten over ongedefinieerde configuratie | Omgevingsvariabelen (1) |
| 404 bij verversen of gedeelde links | Rewrites (2) |
| Build faalt op een import | Hoofdletters in bestandsnamen (3) |
| Fouten met `process` / `fs` / `Buffer` | Code die alleen in Node werkt (4) |
| Inloggen stuurt naar de verkeerde plek | Redirect-URL's voor authenticatie (5) |
| CORS-fouten in de console | Toegestane origins, routing via de server (6) |
| Werkt in ontwikkeling, vreemd in de build | Productiebuild lokaal (7) |

## Verder dan "Het Deployt"

Met deze oplossingen staat uw Bolt-app online. Hij is daarmee nog niet productierijp: toegangsregels voor data, geheimen op de server, geverifieerde betalingen, staging, back-ups en monitoring vormen de volgende laag. Onze [dienst om een Bolt.new-app naar productie te brengen](https://launchstudio.eu/nl/blog/bolt-new-app-to-production-fixed-price-launch-service) dekt beide lagen tegen een vaste prijs, voor de meeste Bolt-apps doorgaans €800-€3.500.

Onze engineers hebben via Manifera, het softwareontwikkelbedrijf achter LaunchStudio, 160+ projecten opgeleverd voor enterpriseklanten, met 11+ jaar deploymentwerk op Netlify, Vercel, AWS en Azure. De engineering zit in Ho Chi Minh City, met klantcontact in Amsterdam en Singapore. Zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/). Voor de details van Vite is de officiële [gids van Vite over het deployen van een statische site](https://vite.dev/guide/static-deploy) een goede bron.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Museumtour Die Overal Werkte Behalve in het Museum

Emma Lambrecht, museumeducator in Brugge, bouwde Zaalgids met Bolt: een mobielvriendelijke audiotour die bezoekers openen door een QR-code naast elk kunstwerk te scannen, met tekst, audio en een kleine quiz voor kinderen. In de preview van Bolt was hij vlekkeloos. Op Netlify ging hij op de eerste testdag op drie manieren kapot.

Elke QR-code linkte rechtstreeks naar een zaalpagina, zoals `/room/flemish-primitives`, en allemaal gaven ze een 404, omdat er geen rewrite-regel was. Nadat Emma er met de hand een had toegevoegd, laadden de audiobestanden niet, omdat hun opslag-URL uit een omgevingsvariabele kwam die alleen in haar Bolt-sessie was ingesteld. En de quizscores, opgeslagen via Supabase, faalden omdat het productiedomein ontbrak in de toegestane URL's van Supabase, waardoor ook het inloggen voor medewerkers niet werkte.

LaunchStudio voegde rewrites toe op Netlify, stelde omgevingsvariabelen per omgeving in, voegde het productie- en previewdomein toe aan de instellingen van Supabase Auth, verplaatste de audiobestanden naar een bucket met CDN en caching voor de zwakke wifi in het museum, en voegde offline caching toe voor de teksten van de tour. Een controle voor elke deployment draait nu de productiebuild en test de QR-routes automatisch.

**Resultaat:** Zaalgids ging live voor de zomertentoonstelling van het museum. In twaalf weken startten bezoekers ongeveer 9.600 tours, en de audio laadde betrouwbaar, zelfs in de kelderzalen.

> *"Elke QR-code wees naar een pagina die volgens de server niet bestond. In de preview had hij altijd bestaan."*
> - **Emma Lambrecht, Oprichter, Zaalgids (Brugge)**

**Kosten & Doorlooptijd:** €1.600 (Launch Ready-pakket: rewrites, configuratie van omgevingen, URL's voor authenticatie, audio via CDN, offline caching en controles bij deployment) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Waarom toont mijn Bolt-app na deployment een lege pagina?

Meestal omdat omgevingsvariabelen op de host ontbreken, of omdat er bij het opstarten een JavaScript-fout optreedt. Open de browserconsole: fouten over ongedefinieerde configuratie wijzen op omgevingsvariabelen. Voeg ze met het juiste voorvoegsel toe in de instellingen van de host en bouw opnieuw.

### Hoe los ik 404-fouten bij het verversen van een pagina in een Bolt-app op?

Voeg een rewrite toe, zodat elke route door `index.html` wordt geserveerd. Maak op Netlify een bestand `_redirects` met `/* /index.html 200`; voeg op Vercel een rewrite toe in `vercel.json`. Dit geldt voor single-page apps die zijn gebouwd met Vite en React Router.

### Moet ik mijn Bolt-app deployen vanuit Bolt of vanuit GitHub?

Voor alles wat verder gaat dan een demo: vanuit GitHub, via een pipeline. Dat geeft u buildlogs, previews, gescheiden omgevingen en rollbacks. De ingebouwde deployment van Bolt is handig om snel te delen, maar biedt minder controle.

### Hoe helpt de deploymentervaring van Manifera bij Bolt-apps?

De zeven oorzaken hierboven zijn standaardproblemen bij deployment die de engineers van Manifera al 11+ jaar op verschillende hostingplatforms afhandelen. LaunchStudio zet die ervaring in om fouten bij het deployen van Bolt-apps snel te diagnosticeren en pipelines in te richten die ze voorkomen.

### Hebben deploymentfouten invloed op mijn posities in zoekmachines?

Ja. Zoekmachines die 404-pagina's of lege schermen crawlen, kunnen uw inhoud niet indexeren, en kapotte gedeelde links verliezen hun waarde. Problemen met routing en rendering oplossen is essentieel voordat u in inhoud of SEO investeert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom toont mijn Bolt-app na deployment een lege pagina?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal ontbrekende omgevingsvariabelen of een JavaScript-fout bij het opstarten. Controleer de console, voeg variabelen met het juiste voorvoegsel toe op de host en bouw opnieuw." }
    },
    {
      "@type": "Question",
      "name": "Hoe los ik 404-fouten bij het verversen van een pagina in een Bolt-app op?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voeg een rewrite toe die index.html voor alle routes serveert: een bestand _redirects op Netlify of een rewrite in vercel.json op Vercel." }
    },
    {
      "@type": "Question",
      "name": "Moet ik mijn Bolt-app deployen vanuit Bolt of vanuit GitHub?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vanuit GitHub via een pipeline voor alles wat verder gaat dan een demo, voor buildlogs, previews, omgevingen en rollbacks." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de deploymentervaring van Manifera bij Bolt-apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dit zijn standaardproblemen bij deployment die Manifera al 11+ jaar afhandelt, wat snelle diagnose en preventieve pipelines mogelijk maakt." }
    },
    {
      "@type": "Question",
      "name": "Hebben deploymentfouten invloed op mijn posities in zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. 404's en lege schermen kunnen niet worden geïndexeerd en kapotte links verliezen waarde, dus los routing en rendering op voordat u in SEO investeert." }
    }
  ]
}
</script>
