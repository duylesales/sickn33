---
Titel: "Waarom Toont Mijn App Data van een Andere Gebruiker Na Uitloggen? Sessielekken Oplossen"
Trefwoorden: app toont data vorige gebruiker na uitloggen, react query cache uitloggen, supabase logout data nog zichtbaar, datalek gedeeld apparaat, LaunchStudio, Manifera
Koperfase: Probleembewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Waarom Toont Mijn App Data van een Andere Gebruiker Na Uitloggen? Sessielekken Oplossen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Toont Mijn App Data van een Andere Gebruiker Na Uitloggen? Sessielekken Oplossen",
  "description": "Wanneer de ene gebruiker uitlogt en een ander direct daarna inlogt op hetzelfde apparaat, tonen door AI gebouwde apps soms nog secondelang gegevens van de vorige bezoeker. Deze gids legt uit hoe dit gebeurt via client-side querycaches, local storage, globale state en gedeelde CDN-caches, waarom dit onder de AVG geldt als een ernstig datalek zelfs als uw database waterdicht is, en hoe u alle applicatie-state betrouwbaar wist bij uitloggen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-25",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-does-my-app-show-another-users-data-after-logout" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Session Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "MDN: Clear-Site-Data header", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data" },
    { "@type": "CreativeWork", "name": "TanStack Query: QueryClient clear", "url": "https://tanstack.com/query/latest/docs/reference/QueryClient" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Kort antwoord:** Als een nieuwe gebruiker na het inloggen op een gedeeld apparaat kortstondig of permanent gegevens ziet van de vorige ingelogde gebruiker, is die data niet afkomstig van een verse databasequery, maar uit het lokale geheugen van de webbrowser. Met AI gebouwde applicaties cachen gegevens in het werkgeheugen (met libraries zoals React Query of SWR), slaan gebruikersprofielen en selecties op in `localStorage`, houden actieve toestanden vast in globale state-managers (zoals Zustand of Redux) en cachen API-antwoorden soms zelfs in een service worker. De standaard uitlogknop roept simpelweg `supabase.auth.signOut()` aan en navigeert weg: de authenticatiesessie stopt, maar alle lokale gegevens blijven achter. In zeldzamere en nog gevaarlijkere gevallen cachet een CDN gepersonaliseerde pagina's voor andere gebruikers. De structurele oplossing: wis bij elke uitlogactie en accountwissel alle lokale caches en stores, koppel cache-keys strikt aan het unieke gebruikers-ID en zorg dat gepersonaliseerde serverdata nooit publiek gecachet kan worden.

## Belangrijkste Inzichten

- **Uitloggen uit Supabase wist de lokale caches van uw app niet.** De frontendcode moet dat expliciet zelf initiëren.
- **Gedeelde apparaten maken dit een acuut privacyprobleem:** gezamenlijke gezinstablets, kassa's in winkels, incheckzuilen bij sportclubs en flexplek-laptops op kantoor.
- **Row Level Security (RLS) biedt hier geen enkele bescherming tegen:** de getoonde data was immers eerder legitiem opgehaald door de vorige gebruiker en wordt nu simpelweg uit het lokale browsergeheugen getoond.
- **CDN-caching van gepersonaliseerde pagina's** is de gevaarlijkste variant, omdat daarmee privégegevens kunnen lekken naar gebruikers op compleet andere apparaten.
- **Eén centrale uitlogroutine** die alle geheugenlagen, lokale opslag en actieve netwerkverbindingen tegelijkertijd leegt, lost het probleem structureel op.

## Hoe Dit Datalek Ontstaat

Zodra een gebruiker inlogt, haalt de webapplicatie allerlei persoonsgegevens op: profielinformatie, bestelgeschiedenis, privéchats en administratieve instellingen. Om de applicatie razendsnel te laten aanvoelen, bewaart de frontend deze data op verschillende plekken:

- **Query-caches:** Tools zoals TanStack Query (React Query) of SWR bewaren JSON-antwoorden in het werkgeheugen onder algemene sleutels zoals `['orders']` of `['profile']`.
- **Globale state-stores:** Zustand, Redux of React Context onthouden het actieve gebruikers-ID, het geselecteerde team en openstaande formulieren.
- **Local Storage en Session Storage:** Bewaren instellingen, concept-notities en de laatst gekozen organisatie tussen browsersessies door.
- **IndexedDB:** Bewaart grotere datasets voor offline PWA-gebruik.
- **Service Workers:** Cachen soms integrale netwerkantwoorden.

Wanneer een gebruiker op "Uitloggen" klikt, voert de gegenereerde code doorgaans alleen `await supabase.auth.signOut()` uit en stuurt de browser door naar de inlogpagina. De authenticatiesessie bij Supabase is beëindigd, maar de volledige cache in het browsergeheugen blijft onaangeroerd. Logt de volgende bezoeker op datzelfde scherm in, dan putten de schermen direct uit de bewaarde cache, soms enkele seconden totdat een refetch klaar is, en soms permanent als de cache-sleutel niet verandert.

## Waarom Dit een Ernstig Probleem Is, Ondanks een Veilige Database

Veel software-oprichters denken ten onrechte dat er geen vuiltje aan de lucht is zolang de PostgreSQL-database goed is beveiligd met Row Level Security. Het datalek heeft op het scherm van de klant echter al daadwerkelijk plaatsgevonden: de volgende bezoeker ziet namen, privégegevens, facturen of medische notities van iemand anders.

Onder de Algemene Verordening Gegevensbescherming (AVG/GDPR) geldt het tonen van persoonsgegevens aan een onbevoegde derde partij direct als een **datalek**, ongeacht of de data afkomstig was van een server of uit een lokale browsercache. Raadpleeg onze gids over [AVG datalek 72 uur respons](https://launchstudio.eu/nl/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas) voor de wettelijke verplichtingen als dit zich heeft voorgedaan.

Dit risico is levensgroot bij software die wordt gebruikt op gedeelde hardware:
- Een registratietablet bij de receptie van een sportschool of praktijk.
- Een kassa-iPad in een horecagelegenheid of winkel.
- Een gedeelde werkplek-laptop in een werkplaats of kantoor.
- Een gezinssmartphone of tablet thuis.

## Oorzaak 1: De Query Cache Wordt Niet Geleegd

React Query en SWR bewaren serverantwoorden standaard onder generieke sleutels, zoals `['facturen']`. Na een nieuwe aanmelding retourneert dezelfde query-key direct de gegevens van de vorige gebruiker uit het RAM-geheugen, totdat de stale-tijd verstrijkt en de backend opnieuw wordt bevraagd.

**Oplossing:** Roep bij het uitloggen altijd direct `queryClient.clear()` aan. Voeg daarnaast altijd het unieke `userId` toe aan alle query-keys: `['facturen', user.id]`. Hierdoor kan data van gebruiker A technisch nooit worden uitgelezen door gebruiker B, zelfs als de cache per ongeluk niet volledig is gewist.

## Oorzaak 2: Gegevens in Local Storage Blijven Bewaard

AI-code slaat gebruikersinstellingen voor het gemak vaak op in `localStorage`: het volledige gebruikersprofiel, het actieve team-ID, eerdere zoekopdrachten of concept-invoer. In tegenstelling tot sessiecookies blijft `localStorage` oneindig op de schijf van het apparaat staan totdat het expliciet met code wordt gewist.

**Oplossing:** Houd een strikte lijst bij van alle opslagsleutels die uw app gebruikt en wis deze integraal bij het uitloggen (`localStorage.removeItem(...)` of `localStorage.clear()`). Sla privacygevoelige persoonsgegevens liever helemaal niet op in `localStorage`. Moeten concepten bewaard blijven? Koppel de sleutel dan altijd aan het gebruikers-ID (`draft_123_userid`).

## Oorzaak 3: Globale State Wordt Niet Gereset

Een globale store (zoals Zustand) bewaart de geselecteerde organisatie of het actieve klantnummer. Na uitloggen en hernieuwd inloggen bevat die store nog steeds de waarden van de vorige gebruiker. De eerste API-aanroepen van de nieuwe gebruiker worden vervolgens verstuurd met de organisatie-ID van de vorige gebruiker, wat resulteert in lege schermen of, bij zwakke backend-policies, toegang tot verkeerde gegevens.

**Oplossing:** Reset alle globale state-stores expliciet naar hun initiële beginwaarden zodra de uitlogknop wordt ingedrukt. Leid de actieve organisatie bij het inloggen altijd server-side af uit de daadwerkelijke lidmaatschappen van de nieuwe gebruiker.

## Oorzaak 4: De Pagina Wordt Niet Volledig Herladen

In een Single Page Application (SPA) navigeert de gebruiker via JavaScript tussen inlog- en dashboardschermen zonder dat de browser de HTML-pagina opnieuw inlaadt. Alle in-memory variabelen, actieve WebSockets en event-listeners blijven gewoon doordraaien op de achtergrond.

**Oplossing:** Sluit actieve Supabase Realtime-kanalen (`supabase.removeAllChannels()`) expliciet af bij het uitloggen en forceer een harde paginavernieuwing (`window.location.href = '/login'`). Dit is de meest betrouwbare garantie dat het JavaScript-werkgeheugen van de browser volledig wordt opgeschoond.

## Oorzaak 5: Service Workers en Offline Gegevens

Progressive Web Apps (PWA's) die netwerkverzoeken cachen via een service worker of lokale kopieën bewaren in IndexedDB, kunnen na een herstart doodleuk alsnog data van de vorige gebruiker tonen. Zie onze handleiding over [offline modus voor PWA's](https://launchstudio.eu/nl/blog/offline-mode-for-pwas-built-with-ai-tools).

**Oplossing:** Cache beveiligde API-endpoints met gebruikersgegevens nooit in de statische service worker cache, wis gebruikersspecifieke IndexedDB-tabellen bij uitloggen en stuur vanuit uw logout-endpoint optioneel de HTTP-header `Clear-Site-Data: "cache", "storage"` mee.

## Oorzaak 6: CDN- of Servercaching van Privégegevens (Het Gevaarlijkste Scenario)

Dit is het meest alarmerende scenario: een CDN (zoals Cloudflare), een reverse proxy of een caching-laag slaat een gepersonaliseerd API-antwoord of dashboardpagina op in zijn wereldwijde cache en levert deze vervolgens uit aan willekeurige andere bezoekers op **totaal andere apparaten**.

Dit ontstaat meestal wanneer een oprichter in Cloudflare een agressieve regel zoals "Cache Everything" aanzet om de app sneller te maken, of wanneer de backend API-antwoorden verstuurt met publieke cache-headers (`Cache-Control: public, max-age=3600`).

**Oplossing:** Alle endpoints die gepersonaliseerde gebruikersdata serveren moeten te allen tijde worden voorzien van de header: `Cache-Control: private, no-store, no-cache, must-revalidate`. Configureer Cloudflare zo dat alle dynamische API-routes en geauthenticeerde paden standaard worden gepasseerd (*Bypass Cache*). Lees onze instructies over [Cloudflare voor uw AI-gebouwde app](https://launchstudio.eu/nl/blog/cloudflare-in-front-of-your-ai-built-app).

## De Universele Uitlogroutine

Bundel alle opschoonacties in één centrale functie die wordt aangeroepen bij handmatig uitloggen, automatische sessietimeouts en het wisselen van account:

1. Verbreek de sessie via `supabase.auth.signOut()`.
2. Leeg de complete query-cache (`queryClient.clear()`).
3. Reset alle globale state-stores naar hun initiële status.
4. Verwijder alle gerelateerde sleutels uit `localStorage` en `sessionStorage`.
5. Ruim eventuele persoonsgegevens in IndexedDB op.
6. Sluit alle actieve Supabase Realtime-verbindingen af.
7. Forceer een volledige herlaadactie naar het inlogscherm (`window.location.replace('/login')`).

Bouw daarnaast een vangnet in bij het inloggen: zodra een gebruiker inlogt, controleert de app of eventuele achtergebleven gecachete data overeenkomt met het zojuist ingelogde `userId`. Wijkt dit af? Dan wordt de cache direct gewist voordat er ook maar één pixel gerenderd wordt.

## Diagnose-Tabel voor Caching- en Sessielekken

| Symptoom | Meest waarschijnlijke oorzaak | Eerste controlepunt |
| --- | --- | --- |
| Data van vorige gebruiker kort zichtbaar na inloggen | Query cache (React Query/SWR) niet geleegd | `queryClient.clear()` en gebruikersspecifieke query-keys |
| Oude data blijft zichtbaar tot handmatige F5 | Globale store (Zustand/Redux) behoudt state | Reset-functie van stores aanroepen bij logout |
| Oude data blijft zelfs na harde refresh aanwezig | Gegevens bewaard in `localStorage` of IndexedDB | Tabblad Application in DevTools > Storage inspecteren |
| Data van vorige gebruiker verschijnt in offline modus | Service worker cachet geauthenticeerde API-calls | Service worker cacherules controleren |
| Gebruikers op andere computers zien vreemde data | CDN cachet dynamische API-routes | `Cache-Control` headers op API-endpoints inspecteren |
| Nieuwe gebruiker opent dashboard van vorig bedrijf | Opgeslagen organisatie-ID in globale state | Bedrijfskoppeling server-side valideren bij login |

## Hoe U Dit Grondig Test

- Log in als Testgebruiker A op een computer, open verschillende pagina's, formulieren en zoekschermen, en klik op uitloggen.
- Log direct daarna in als Testgebruiker B op datzelfde apparaat **zonder de browser te vernieuwen**.
- Controleer alle dashboards, zoekgeschiedenis, concepten en instellingenpagina's op sporen van Gebruiker A.
- Herhaal de test na een herstart en met de app geïnstalleerd als PWA.
- Inspecteer in het Network-tabblad de response headers van uw API-routes en verifieer dat overal `private, no-store` staat.

Neem deze tien minuten durende controle op in uw vaste testprocedure vóór elke grote release. Zie onze gids over [uw AI-gebouwde app testen voor lancering](https://launchstudio.eu/nl/blog/how-do-i-test-my-ai-built-app-before-launch).

## Hoe LaunchStudio Helpt

LaunchStudio lost gevaarlijke sessie- en cachelekken in door AI gebouwde applicaties definitief op: we implementeren een centrale en onfeilbare uitlogprocedure, richten gebruikersspecifieke query-keys in, saneren browseropslag en globale state, sluiten lekkende WebSockets af, beveiligen HTTP-cacheheaders tegen ongewenste CDN-caching, voeren strenge shared-device audits uit en ondersteunen bij eventuele AVG-datalekdocumentatie.

Het **Launch Ready**-pakket (€800 - €3.500) omvat complete sessie- en cachebeveiliging, security hardening en deployment; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt continue hostingbegeleiding, proactieve monitoring en prioritaire ondersteuning. Bereken uw investering direct via de [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is onderdeel van Manifera, een software-ontwikkelingsbedrijf met ruim 11 jaar ervaring, meer dan 160 opgeleverde projecten en 120+ senior engineers gespecialiseerd in privacy-first architecturen en applicatiebeveiliging. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; onze engineering vindt plaats in het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City en onze vestiging aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in de Praktijk: De Incheck-Tablet die Zich de Vorige Sporter Bleef Herinneren

Daan Peters bouwde Ledenloket met Lovable en Supabase: een innovatieve incheck- en abonnementsapplicatie voor moderne boetiek-fitnessstudio's en yogascholen. Leden checken bij binnenkomst in op een centrale iPad bij de balie, bekijken hun actieve rittenkaart of abonnement en schrijven zich direct in voor groepslessen. Negen fitnessstudio's maakten actief gebruik van het platform met een vaste gedeelde tablet bij de receptie, terwijl leden de app tevens op hun eigen smartphone gebruikten.

Op een ochtend diende een verontrust lid een officiële klacht in: nadat zij op de inchecktablet had ingelogd met haar pincode, zag zij gedurende enkele seconden de volledige naam, het abonnementsbedrag en de recente blessurenotities van het vorige lid op het scherm staan. Door snel door te klikken had zij bovendien per abuis een yogales geboekt op het account van die vorige sporter. Daan ontdekte dat de uitlogknop in Lovable uitsluitend `supabase.auth.signOut()` aanriep. React Query bewaarde alle data in het geheugen onder algemene sleutels zonder gebruikers-ID, het profiel en de geselecteerde clublocatie stonden opgeslagen in `localStorage`, en een globale Zustand-store hield het lidnummer vast totdat het nieuwe profiel geladen was. Tot overmaat van ramp bleek een Cloudflare-paginaregel de API-route voor het dagelijkse lesrooster inclusief een gepersonaliseerde vlag *"al_geboekt"* publiek te cachen, waardoor sporters op hun eigen telefoon soms de boekingen van wildvreemden zagen staan.

LaunchStudio greep direct in en verwijderde de CDN-caching voor alle geauthenticeerde endpoints, met strikte `private, no-store` headers op alle gepersonaliseerde API-antwoorden. Er werd een centrale uitlogprocedure geïmplementeerd die de query-cache direct leegt, alle globale stores reset, `localStorage` opschoont, realtime-verbindingen sluit en de pagina forceert te herladen. Alle query-keys kregen een verplicht `userId`-attribuut en de boekingsactie valideert het lidnummer nu uitsluitend aan de serverzijde via de cryptografische sessie. Op de balie-tablets werd een geautomatiseerde inactiviteitstimer ingesteld die de tablet na 60 seconden zonder aanraking automatisch veilig uitlogt. Daan documenteerde het incident met ondersteuning van LaunchStudio conform de AVG als datalek en stelde de betrokken leden netjes op de hoogte.

**Resultaat:** Uitgebreide tests op de fysieke balie-iPads toonden aan dat er geen enkel residu van eerdere leden meer achterblijft. Er zijn geen nieuwe klachten binnengekomen, en de automatische kiosk-timeout wordt door studio-eigenaren nu actief geprezen als een professionele privacyfeature.

> *"Mijn database was uitstekend beveiligd. Het datalek zat in alles wat mijn app bleef onthouden nadat de gebruiker was weggelopen."*
> - **Daan Peters, Oprichter, Ledenloket (Eindhoven)**

**Kosten & Doorlooptijd:** €1.700 (Launch Ready-pakket: uitlogroutine, cache- en state-opschoning, CDN- en header-herstel, kiosk-timeout en incidentdocumentatie) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Waarom toont mijn app na het inloggen nog gegevens van de vorige gebruiker?

Omdat de applicatie gegevens toont uit lokale browsercaches (zoals React Query, `localStorage` of globale state-stores) die bij het uitloggen niet zijn gewist. De uitlogfunctie van Supabase beëindigt uitsluitend de databasesessie, maar laat de lokale opslag in de browser van de gebruiker onaangeroerd achter.

### Is het tonen van gegevens van een vorige gebruiker een AVG-datalek?

Ja. Het onbedoeld tonen van persoonsgegevens aan een onbevoegde derde partij geldt onder de Algemene Verordening Gegevensbescherming (AVG) direct als een beveiligingsincident en datalek, zelfs wanneer uw centrale database optimaal beveiligd is. U bent verplicht dit intern te registreren.

### Voorkomt Row Level Security (RLS) dit probleem niet automatisch?

Nee. Row Level Security controleert uitsluitend welke data de PostgreSQL-database naar de server terugstuurt. In dit geval is de data al eerder legitiem opgehaald door de vorige gebruiker en wordt deze getoond vanuit het lokale cachegeheugen van de browser.

### Hoe helpt de ervaring van Manifera bij het beveiligen van sessies?

Manifera ontwikkelt al meer dan 11 jaar veilige bedrijfssoftware en enterprise portalen, inclusief systemen voor gedeelde kiosken en balie-omgevingen. LaunchStudio past die strenge sessiebeveiliging en opschoonprocedures toe op door AI gebouwde applicaties.

### Kan het cachen van persoonsgegevens invloed hebben op SEO of AI-zoekmachines?

Ja, met name wanneer dynamische pagina's met gebruikersgegevens per abuis publiek worden gecachet door een CDN. Zoekmachinebots kunnen die pagina's indexeren, waardoor privégegevens van gebruikers zichtbaar worden in Google-zoekresultaten en AI-samenvattingen. Strikte `private, no-store` headers voorkomen dit risico.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom toont mijn app na het inloggen nog gegevens van de vorige gebruiker?",
      "acceptedAnswer": { "@type": "Answer", "text": "Lokale browsercaches zoals React Query, localStorage of globale state werden niet gewist bij het uitloggen." }
    },
    {
      "@type": "Question",
      "name": "Is het tonen van gegevens van een vorige gebruiker een AVG-datalek?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; het tonen van persoonsgegevens aan onbevoegden is een AVG-datalek, ongeacht waar de data lokaal vandaan komt." }
    },
    {
      "@type": "Question",
      "name": "Voorkomt Row Level Security (RLS) dit probleem niet automatisch?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee; RLS beveiligt databaseverzoeken, maar deze data wordt direct geserveerd vanuit het browsergeheugen van de vorige sessie." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het beveiligen van sessies?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar veilige bedrijfssoftware voor gedeelde apparaten conform strikte sessie- en privacyrichtlijnen." }
    },
    {
      "@type": "Question",
      "name": "Kan het cachen van persoonsgegevens invloed hebben op SEO of AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; publiek gecachete privépagina's kunnen door crawlers geïndexeerd worden; correcte headers houden data privé." }
    }
  ]
}
</script>
