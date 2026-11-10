---
Titel: "Waarom Zien Gebruikers Na Een Deploy Nog de Oude Versie? Caching Uitgelegd"
Trefwoorden: gebruikers zien oude versie na deploy, app update niet na livegang, browser cache legen react app, service worker oude versie pwa, LaunchStudio, Manifera
Koperfase: Probleembewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Waarom Zien Gebruikers Na Een Deploy Nog de Oude Versie? Caching Uitgelegd

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Zien Gebruikers Na Een Deploy Nog de Oude Versie? Caching Uitgelegd",
  "description": "U heeft zojuist een cruciale bugfix uitgerold, maar uw klanten zien nog steeds de oude applicatie. Deze gids legt de verschillende cachelagen uit tussen uw server en uw gebruikers - van browser- en CDN-caches tot service workers in PWA's en langdurig openstaande tabbladen -, welke cache-instellingen werken voor door AI gebouwde React-apps en hoe u updates vlekkeloos uitrolt zonder klanten te vragen hun browsergeschiedenis te wissen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-16",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-do-users-still-see-the-old-version-after-a-deploy" },
  "citation": [
    { "@type": "CreativeWork", "name": "MDN: HTTP caching", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching" },
    { "@type": "CreativeWork", "name": "web.dev: Service worker lifecycle", "url": "https://web.dev/articles/service-worker-lifecycle" },
    { "@type": "CreativeWork", "name": "Vite: Building for production", "url": "https://vite.dev/guide/build" },
    { "@type": "CreativeWork", "name": "Cloudflare: Purge cache", "url": "https://developers.cloudflare.com/cache/how-to/purge-cache/" }
  ]
}
</script>

**Kort antwoord:** Gebruikers zien na een release nog steeds een verouderde versie omdat er ergens tussen uw webserver en hun scherm een kopie van de oude bestanden bewaard blijft: in het browsergeheugen, op de schijf van de client, in het netwerk van een CDN (zoals Cloudflare), in een service worker wanneer uw app als Progressive Web App (PWA) is geïnstalleerd, of simpelweg in een browsertabblad dat al dagen openstaat. Een betrouwbare architectuur berust op één gouden regel: cache `index.html` nooit langdurig (laat de browser altijd her-valideren bij de server), cache gehashte JavaScript- en CSS-bestanden gerust een vol jaar, richt service workers in met een actieve updatecontrole en laat de applicatie zelf detecteren wanneer er een nieuwere versie beschikbaar is. Zo bereikt elke deploy al uw gebruikers binnen enkele minuten, zonder dat iemand handmatig zijn cache hoeft te legen.

## Belangrijkste Inzichten

- **Het HTML-bestand is de sleutel tot succes:** als `index.html` te lang gecachet wordt, blijft de browser de oude JavaScript-bestanden opvragen.
- **Gehashte assets mogen oneindig gecachet worden,** omdat elke nieuwe software-build resulteert in unieke bestandsnamen.
- **Service workers in PWA's** vormen de meest hardnekkige cachelaag en vereisen een expliciete, gebruikersvriendelijke updatestrategie.
- **Openstaande browsertabbladen updaten nooit uit zichzelf** in een Single Page Application; de frontend moet zelf periodiek controleren op nieuwe versies.
- **"Leeg uw browsercache" is geen professionele releasestrategie.** Los het structureel op in de HTTP-headers van uw webserver.

## De Vier Cachelagen Tussen U en Uw Gebruikers

Wanneer u een nieuwe versie deployed, landen de bijgewerkte bestanden direct op uw hostingserver. Voordat een eindgebruiker die wijzigingen op zijn scherm ziet, kan het verzoek door vier verschillende lagen worden beantwoord:

1. **Het werkgeheugen van de browser:** Een openstaand browsertabblad blijft het oorspronkelijk ingeladen JavaScript uitvoeren zolang de pagina niet herladen wordt.
2. **De HTTP-schijfcache van de browser:** Bestanden die lokaal op de computer of telefoon zijn opgeslagen op basis van de `Cache-Control`-headers die uw server heeft meegestuurd.
3. **De Service Worker:** Bij PWA's een achtergrondscript dat netwerkverzoeken onderschept en een lokaal bewaarde kopie van de complete app kan serveren, zelfs wanneer de gebruiker online is.
4. **Een CDN of caching proxy:** Cloudflare, het edge-netwerk van Vercel of een bedrijfsfirewall die kopieën van uw HTML en scripts tussentijds bewaart om de laadtijd te versnellen.

Elke laag vereist specifieke configuratieregels. Zodra één laag hardnekkig vasthoudt aan de oude `index.html`, blijft de hele keten verouderde software tonen.

## Hoe een Moderne Frontend-Build Hoort te Werken

Build-tools zoals Vite genereren bij elke compilatie unieke bestandsnamen met een inhoudshash (*content hash*), bijvoorbeeld `index-a8f3c2.js` en `style-b9e4d1.css`. Als er ook maar één letter in uw code verandert, krijgt het bestand een compleet nieuwe naam. Het kleine HTML-bestand (`index.html`) bevat de verwijzingen naar die specifieke actuele bestandsnamen.

Dit leidt tot een eenvoudig en onwrikbaar configuratiemodel:

| Bestandstype | Cacheregel | Waarom |
| --- | --- | --- |
| `index.html` | Geen lange cache (`no-cache`); altijd revalideren | Moet altijd direct verwijzen naar de allernieuwste JavaScript-bestanden |
| Gehashte JS en CSS | 1 jaar cachen (`max-age=31536000, immutable`) | Bestandsnamen veranderen gegarandeerd bij elke inhoudelijke wijziging |
| Statische afbeeldingen met vaste namen | Gematigd cachen of voorzien van versienummer | Voorkomt dat verouderde logo's of banners oneindig blijven hangen |
| Service worker script (`sw.js`) | Nooit cachen (`no-store` of `no-cache`) | Browsers moeten direct kunnen zien dat er een nieuwe worker beschikbaar is |

Als uw hostingplatform of Cloudflare `index.html` per abuis vier uur lang cachet, blijven gebruikers vier uur lang de oude JavaScript-bundels laden. Dat is de hoofdoorzaak van de uitspraak: *"Ik heb het live gezet, maar ik zie nog niets."*

## Oorzaak 1: Het HTML-Bestand Wordt Gecachet

Veel standaard webserver-configuraties (zoals een eenvoudige Nginx-server of een S3-bucket) passen één algemene cacheheader toe op alle bestanden, inclusief HTML. Als u daarnaast Cloudflare voor uw domein heeft geplaatst met een paginaregel *"Cache Everything"* om de laadsnelheid te maximaliseren, bewaart Cloudflare ook de HTML-pagina urenlang in zijn wereldwijde edge-netwerk.

**Oplossing:** Configureer voor `index.html` altijd `Cache-Control: no-cache` (wat betekent: *"controleer bij de server of er een nieuwere versie is voordat je de lokale kopie toont"*). Sluit HTML expliciet uit van agressieve CDN-regels of trigger bij elke deployment een automatische CDN cache-purge. Onze gids over [Cloudflare voor uw AI-gebouwde app](https://launchstudio.eu/nl/blog/cloudflare-in-front-of-your-ai-built-app) beschrijft de exacte configuratieregels.

## Oorzaak 2: De Service Worker Blijft de Oude App Serveren

Als uw applicatie is uitgerust met PWA-functionaliteit, vangt een service worker alle netwerkverzoeken af om de app offline beschikbaar te maken. Standaard installeert een nieuwe service worker zich weliswaar geruisloos op de achtergrond, maar activeert hij pas op het moment dat **alle** geopende tabbladen en vensters van de app volledig zijn afgesloten. Op smartphones, waar webapps dagenlang op de achtergrond gepauzeerd blijven in het multitasking-overzicht, kan het dagen duren voordat een gebruiker de app echt afsluit.

Erger nog: sommige door AI gegenereerde service workers hanteren een roekeloze "Cache First"-strategie voor `index.html`, waardoor ze nooit controleren of er op de server een update klaarstaat.

**Oplossing:** Gebruik een beproefde bibliotheek zoals Workbox in plaats van handgeschreven workerscripts. Laat de app bij het opstarten controleren op updates, toon een vriendelijke melding *"Nieuwe versie beschikbaar"* met een herlaadknop, en forceer activering (`skipWaiting()`) zodra de gebruiker akkoord geeft. Cache het service worker-bestand zelf nooit. Onze gids over [offline modus voor PWA's](https://launchstudio.eu/nl/blog/offline-mode-for-pwas-built-with-ai-tools) belicht de voor- en nadelen.

## Oorzaak 3: Tabbladen die Dagenlang Open Blijven Staan

Een Single Page Application laadt eenmalig in en handelt alle volgende schermwisselingen lokaal af via JavaScript. Een kantoormedewerker die uw SaaS-applicatie op maandagochtend opent en zijn laptop aan het einde van de dag simpelweg dichtklapt, haalt nooit de nieuwe HTML op. Hij blijft de hele week werken in de oude interface en verstuurt verzoeken naar uw backend met verouderde code.

**Oplossing:** Laat de applicatie periodiek (of zodra het tabblad weer de focus krijgt) een klein `/version.json`-bestandje opvragen bij de server. Wijkt het versienummer af van de draaiende app? Toon dan een subtiele notificatiebalk om de pagina te verversen. Zorg bovendien dat mislukte chunk-aanroepen (wanneer een gebruiker navigeert naar een scherm waarvan het oude bestand gewist is) worden opgevangen en resulteren in een automatische herlaadactie. Zie [waarom apps een wit scherm tonen](https://launchstudio.eu/nl/blog/why-does-my-app-show-a-blank-white-screen) voor meer details over chunkfouten.

## Oorzaak 4: De Deployment Is Niet Geland Waar U Dacht

Soms is er helemaal geen sprake van een cacheprobleem, maar is er iets misgegaan tijdens de uitrol:

- De deployment is gekoppeld aan een preview-URL (bijvoorbeeld een pull request branch) in plaats van het productiedomein.
- Het geautomatiseerde buildproces is mislukt op een TypeScript-fout, waardoor de hostingprovider de vorige werkende versie is blijven serveren.
- Omgevingsvariabelen zijn aangepast in het dashboard, maar de frontend is daarna niet opnieuw gecompileerd.
- De DNS-records verwijzen na een recente hostingmigratie per abuis nog naar de oude server.

**Oplossing:** Controleer altijd het deployment-logboek van uw hostingserver, verifieer welk specifiek build-ID is toegewezen aan uw hoofddomein en toon een klein versienummer in de footer of op de instellingenpagina van uw app.

## Achterwaartse Compatibiliteit van Uw Backend

Omdat u nooit kunt afdwingen dat 100% van uw gebruikers op exact dezelfde seconde overstapt naar de nieuwe frontend, moet uw backend tijdelijk overweg kunnen met zowel oude als nieuwe clients. Als u in dezelfde release een databasekolom hernoemt of API-parameters wijzigt, crashen alle actieve schermen van gebruikers die de pagina nog niet ververst hebben.

**Oplossing:** Voer databasewijzigingen altijd achterwaarts compatibel uit volgens het *expand-and-contract*-principe: voeg eerst de nieuwe kolom of endpoint toe, ondersteun tijdelijk beide versies en saneer de oude velden pas nadat alle clients zijn overgestapt. Onze gids over [zero-downtime databasemigraties in Supabase](https://launchstudio.eu/nl/blog/zero-downtime-database-migrations-in-supabase) beschrijft dit stappenplan.

## Diagnose-Tabel voor Updateproblemen

| Symptoom | Meest waarschijnlijke oorzaak | Eerste controle |
| --- | --- | --- |
| Oude versie zichtbaar tot harde refresh (Ctrl+F5) | `index.html` te lang gecachet | `Cache-Control` header op HTML inspecteren |
| Oude versie blijft zichtbaar, zelfs na hard refresh | CDN-cache of agressieve service worker | Cloudflare purge en Application tab in DevTools |
| Smartphone-app (PWA) toont dagenlang oude code | Service worker wacht op sluiten tabbladen | Update- en activeringslogica van de worker |
| Gebruikers met langdurig open tabs melden oude bugs | Geen actieve versiecontrole in app | Versiepolling op window focus implementeren |
| Niemand ziet de update, ook u niet in incognito | Deploy is mislukt of staat op verkeerd domein | Build- en deployment-logs op de server controleren |
| Foutmeldingen direct na release bij actieve gebruikers | Oude frontend praat met nieuwe API | Achterwaartse compatibiliteit van endpoints checken |

## Hoe U Controleert Wat Gebruikers Daadwerkelijk Ontvangen

- **Open DevTools (F12) > Tabblad Netwerk:** Vernieuw de pagina en controleer de kolom Headers. Bekijk de `Cache-Control` waarde van zowel `index.html` als de `.js`-bestanden.
- **Inspecteer het tabblad Applicatie (Application):** Bekijk onder Service Workers welke worker actief is en inspecteer onder Cache Storage welke bestanden lokaal zijn opgeslagen.
- **Toon het build-versienummer:** Plaats het versienummer (bijvoorbeeld `v1.4.2 (build 89)`) discreet in de instellingen en vraag een klagende klant welk nummer hij ziet staan.
- **Test in een incognitovenster:** Hiermee ziet u direct wat een kersverse bezoeker zonder browserhistorie te zien krijgt.

## Een Betrouwbare Releasestrategie

1. Deploy de update eerst naar de staging-omgeving en valideer de werking.
2. Deploy naar productie; de webserver levert de nieuwe `index.html` per direct uit aan nieuwe verzoeken.
3. Leeg geautomatiseerd de HTML-cache op het CDN (indien van toepassing).
4. Actieve browsertabbladen detecteren de nieuwe versie en tonen een vriendelijke herlaadknop.
5. PWA's tonen een duidelijke update-notificatie en activeren de nieuwe service worker na één klik.
6. Houd oude JavaScript-assets nog enkele uren beschikbaar op de server om crashes tijdens actieve sessies te voorkomen.
7. Verwijder verouderde database- en backend-routes pas nadat de overgangsperiode is verstreken.

## Hoe LaunchStudio Helpt

LaunchStudio richt professionele deployment- en cachingarchitecturen in voor met AI gebouwde webapplicaties: we configureren optimale HTTP-cacheheaders per bestandstype, stellen CDN-cachingregels en automatische purges in, bouwen betrouwbare PWA-updatestromen met Workbox, implementeren slimme versiecontroles in de frontend, vangen chunk-laadfouten geruisloos op en begeleiden achterwaarts compatibele database-upgrades.

Het **Launch Ready**-pakket (€800 - €3.500) omvat een volledige configuratie van uw deployment-pijplijn en cache-architectuur; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt continue hostingontzorging waarbij releases voor u worden uitgevoerd, inclusief 24/7 monitoring. Bereken uw investering direct met onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is een initiatief van Manifera, een software-ontwikkelingsbedrijf met ruim 11 jaar ervaring, meer dan 160 opgeleverde projecten en 120+ senior engineers gespecialiseerd in high-availability webarchitecturen. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; onze engineering vindt plaats in het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City en onze vestiging aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in de Praktijk: De Btw-Correctie die Pas na Vijf Dagen Aankwam

Noor El Amrani bouwde Marktkraam met Lovable en Supabase: een praktische Progressive Web App waarmee zo'n 180 marktkooplieden op weekmarkten hun dagelijkse verkopen registreren, voorraad live bijhouden en direct inzicht hebben in hun dagomzet. Vrijwel alle kooplieden hadden de PWA geïnstalleerd op het startscherm van hun smartphone.

Een rekenfout in de software zorgde ervoor dat het btw-tarief op specifieke versproducten verkeerd werd berekend. Noor herstelde de formule snel via een prompt, voltooide de deployment binnen het uur en stuurde een geruststellend bericht naar de gebruikersgroep. Vijf dagen later bleven marktkooplieden echter melding maken van foutieve dagtotalen. Het onderzoek door LaunchStudio legde drie overlappende cacheproblemen bloot. De service worker van de PWA, gegenereerd tijdens een eerdere AI-sessie, bewaarde `index.html` volgens een agressieve "Cache First"-strategie en controleerde nooit op updates, waardoor geïnstalleerde apps stug de oude code bleven draaien. Cloudflare paste een "Cache Everything"-regel toe waardoor HTML vier uur lang op de edge bleef hangen. Bovendien stuurde de server voor alle bestanden dezelfde generieke cacheheader van één week mee.

Doordat sommige kooplieden inmiddels op de nieuwe versie draaiden en anderen op de oude, liepen de geconsolideerde marktoverzichten volledig uiteen. Bovendien berekende de oude frontendcode de btw client-side en schreef deze foutieve bedragen rechtstreeks weg naar de centrale Supabase-database.

LaunchStudio verving de handgeschreven service worker door een gecontroleerde Workbox-implementatie die bij elke opening controleert op updates en direct een duidelijke knop *"Nieuwe versie beschikbaar"* toont. De webserver werd zo geconfigureerd dat `index.html` bij elk verzoek opnieuw wordt gevalideerd, terwijl gehashte bestanden een jaar lang gecachet worden. De Cloudflare-cacherules werden aangepast om HTML structureel uit te sluiten. Zodra de app weer focus krijgt op de telefoon, pollt deze direct naar het versienummer. Daarnaast werd de btw-berekening verplaatst naar een database-trigger op de server, zodat verouderde clients geen verkeerde totalen meer kunnen wegschrijven, en werden alle aangetaste historische transacties herberekend. Het actieve versienummer staat nu helder vermeld in het instellingenmenu.

**Resultaat:** De eerstvolgende software-update bereikte binnen 24 uur ruim 95% van alle actieve marktkooplieden, zonder dat iemand handmatig zijn browsergeschiedenis hoefde te wissen. De totalen in weekrapportages kloppen sindsdien tot op de cent, en Noor rolt nieuwe functies nu uit met de zekerheid dat ze direct aankomen.

> *"Ik bleef de marktkooplui vertellen dat de oplossing live stond. Op hun telefoons was dat niet zo. Nu kan ik precies zien welke versie iedereen gebruikt."*
> - **Noor El Amrani, Oprichter, Marktkraam (Rotterdam)**

**Kosten & Doorlooptijd:** €1.800 (Launch Ready-pakket: cache-headers, service worker update-flow, CDN-regels, versiecontrole en server-side btw-berekening) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Waarom zien mijn gebruikers na een deploy nog steeds de oude versie van de app?

Omdat een gecachete kopie van de oude bestanden wordt geserveerd door hun browser, een CDN, een service worker of een browsertabblad dat al sinds vóór de deploy openstaat. Meestal wordt de HTML-pagina (`index.html`) te lang vastgehouden, waardoor de browser blijft verwijzen naar oude JavaScript-bestanden.

### Moet ik gebruikers vragen om hun browsercache te legen?

Uitsluitend als uiterste noodmaatregel bij een incident. Een professionele en duurzame oplossing bestaat uit het instellen van correcte cache-headers (`no-cache` op HTML), een geautomatiseerde service worker update-flow en een versiecontrole in de applicatie zelf, zodat updates geruisloos en automatisch landen.

### Waarom zijn Progressive Web Apps (PWA's) lastiger te updaten?

Omdat de service worker de complete applicatie lokaal opslaat om offline functioneren mogelijk te maken. Standaard wacht een service worker totdat alle actieve tabbladen en vensters volledig zijn gesloten voordat een nieuwe versie actief wordt. Zonder een actieve update-notificatie kunnen telefoons dagenlang verouderde code blijven uitvoeren.

### Hoe helpt de ervaring van Manifera bij het inrichten van software-releases?

Manifera beheert al meer dan 11 jaar releaseprocessen voor bedrijfskritische web- en mobiele applicaties. LaunchStudio past dezelfde industriestandaarden toe op AI-applicaties: voorspelbare caching, betrouwbare versienummering en achterwaarts compatibele API-wijzigingen.

### Heeft caching invloed op SEO of vindbaarheid in AI-zoekmachines?

Ja, aanzienlijk. Een effectieve cachingstrategie voor statische bestanden maakt uw pagina's razendsnel, wat essentieel is voor hoge posities in zoekmachines (Core Web Vitals). Tegelijkertijd zorgt een continu gerevalideerde `index.html` ervoor dat zoekmachinebots en AI-crawlers altijd over de allernieuwste content en metadata beschikken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zien mijn gebruikers na een deploy nog steeds de oude versie van de app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een browser, CDN, service worker of open tabblad serveert oude gecachete bestanden, meestal doordat index.html te lang wordt vastgehouden." }
    },
    {
      "@type": "Question",
      "name": "Moet ik gebruikers vragen om hun browsercache te legen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen bij hoge uitzondering; configureer correcte cache-headers, een service worker updatestrategie en versiecontrole in de app." }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn Progressive Web Apps (PWA's) lastiger te updaten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Service workers slaan de app lokaal op en wachten standaard tot alle vensters gesloten zijn voordat een update activeert." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het inrichten van software-releases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera beheert al 11+ jaar enterprise releaseprocessen en implementeert voorspelbare caching en veilige versiewissels." }
    },
    {
      "@type": "Question",
      "name": "Heeft caching invloed op SEO of vindbaarheid in AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; snelle gecachete assets verhogen Core Web Vitals en gerevalideerde HTML garandeert dat crawlers actuele content zien." }
    }
  ]
}
</script>
