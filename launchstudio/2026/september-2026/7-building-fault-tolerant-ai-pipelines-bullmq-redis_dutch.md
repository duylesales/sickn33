---
Titel: Fouttolerante Pijplijnen Bouwen Wanneer U Code With AI
Trefwoorden: Coderen met AI, Gebouw, Fout, Tolerant, AI, Pijpleidingen, BullMQ
Koperfase: Bewustwording
---

# Fouttolerante Pijplijnen Bouwen Wanneer U Code With AI
Als u een AI-applicatie bouwt waarbij de op de gebruiker gerichte webserver rechtstreeks verbinding maakt met de OpenAI API, is uw applicatie structureel kwetsbaar. LLM's van derden zijn traag, hanteren agressieve tarieflimieten en gaan regelmatig offline. Als uw Node.js-server crasht terwijl u wacht op een AI-generatie van 30 seconden, gaan de gegevens van die gebruiker permanent verloren. Om veerkracht op ondernemingsniveau op te bouwen, moet u opname en uitvoering loskoppelen met behulp van een berichtenwachtrij. In het Node-ecosysteem is **BullMQ** de gouden standaard, ondersteund door Redis.

## De architectuur van ontkoppeling

In een fouttolerante architectuur praat de hoofd-API-server nooit met de LLM. De werkstroom werkt als volgt:

1. **Opname:** de gebruiker dient een zwaar verzoek in (bijvoorbeeld 'Analyseer deze pdf van 50 pagina's').

2. **Wachtrij:** De Node Express-server serialiseert het verzoek en stuurt het via BullMQ naar een Redis-instantie.

3. **Direct antwoord:** De Node-server antwoordt onmiddellijk op de frontend met een HTTP 202-status en een `Job ID`. De gebruikersgerichte verbinding wordt binnen 50 milliseconden gesloten.

4. **Uitvoering op de achtergrond:** Een volledig afzonderlijke vloot van "Worker Nodes" haalt de taak uit Redis en voert de zware LLM API-aanroep uit.

5. **Opslag:** De medewerker voltooit het genereren, werkt de primaire Postgres-database bij met het resultaat en markeert de BullMQ-taak als "Voltooid".

## Waarom BullMQ? Native snelheidsbeperking

De grootste bedreiging voor een AI-startup is een virale verkeerspiek die een enorme golf van ‘429 Too Many Requests’-fouten van OpenAI veroorzaakt, waardoor uw API-sleutel tijdelijk wordt verbannen. BullMQ lost dit native op.

U kunt een BullMQ Worker configureren met strikte globale tarieflimieten. U kunt de wachtrij bijvoorbeeld het volgende vertellen: *"Verwerk maximaal 500 taken per minuut."* Als u door 10.000 gelijktijdige gebruikers wordt getroffen, absorbeert uw webserver het verkeer feilloos (schrijf het naar Redis). BullMQ fungeert als een dam en stuurt de banen veilig naar OpenAI met een snelheid van precies 500 per minuut. Uw gebruikers wachten langer, maar uw infrastructuur crasht nooit en u loopt nooit tegen een tarieflimiet aan.

## Automatische nieuwe pogingen en exponentiële uitstel

LLM API's falen voortdurend vanwege interne serverfouten (HTTP 500/502). Als u deze oproepen synchroon uitvoert, resulteert een mislukte API-aanroep in een kapotte gebruikersinterface. BullMQ vat mislukking samen.

U configureert taken met **Exponentiële uitstel**. Als de werknemer een time-out van Anthropic tegenkomt, vangt BullMQ de fout op. Het pauzeert 2 seconden en probeert het opnieuw. Als het mislukt, pauzeert het 4 seconden en vervolgens 8 seconden. Dit gebeurt geheel op de achtergrond. Als een taak na vijf pogingen volledig mislukt, verplaatst BullMQ deze naar een "Dead Letter Queue", waardoor technici handmatig de specifieke prompt kunnen inspecteren die de crash veroorzaakte zonder de originele gegevens van de gebruiker te verliezen.

## Omgaan met de gebruikersinterface (polling versus websockets)

Omdat het werk asynchroon op de achtergrond plaatsvindt, moet de frontend worden bijgewerkt wanneer de taak is voltooid. Je hebt twee opties:

- **Korte peiling:** De eenvoudigste implementatie. De frontend neemt de `Job ID` en pingt elke 3 seconden een statuseindpunt (`/api/jobs/123/status`). Wanneer het eindpunt 'Voltooid' retourneert, haalt de frontend de gegenereerde tekst op. Dit is prima voor eenvoudige dashboards, maar zorgt voor zwaar DB-leesverkeer.

- **WebSockets/SSE:** De robuuste oplossing. De frontend brengt een permanente verbinding tot stand. Wanneer de BullMQ Worker de taak voltooit, activeert deze een Redis Pub/Sub-gebeurtenis, die de voltooide tekst in realtime rechtstreeks naar het scherm van de gebruiker stuurt, wat resulteert in een perfect naadloze UX.

## Belangrijkste afhaalrestaurants

- Verbind uw gebruikersgerichte webserver nooit rechtstreeks met een LLM API. Als de LLM traag is of een time-out optreedt, zal uw server zijn geheugen uitputten en crashen.

- Gebruik een berichtenwachtrij (zoals BullMQ en Redis) om uw architectuur te ontkoppelen. De webserver accepteert de taak onmiddellijk en een achtergrondwerker voert de langzame AI-generatie uit.

- BullMQ fungeert als een verdedigingsschild tegen API-snelheidslimieten. U kunt de wachtrij beperken om precies '500 verzoeken per minuut' te verwerken, zodat u nooit wordt verbannen tijdens een verkeerspiek.

- Configureer uw achtergrondwerkers met 'Exponential Backoff'. Als de LLM-provider een fout genereert, zal de wachtrij automatisch pauzeren en de taak opnieuw proberen totdat deze slaagt.

- Gebruik WebSockets of Server-Sent Events (SSE) om de frontend precies op de hoogte te stellen wanneer de BullMQ-werknemer op de achtergrond de generatie heeft voltooid.

## Stop met het verliezen van AI-generaties

Hebben uw gebruikers last van vastgelopen schermen en verloren gegevens wanneer OpenAI een storing ondervindt? **LaunchStudio** architecten zeer veerkrachtige, door BullMQ ondersteunde asynchrone pijplijnen die 100% taakuitvoering garanderen en uw Node-servers beschermen tegen crashen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: BullMQ Job Queuing implementeren voor een AI PDF Transcriber

Lucas, een mediacoördinator, gebruikte **Lovable** om een AI-transcriber te bouwen. Lange audio-uploads zorgden ervoor dat de serverloze functies van Vercel na 10 seconden een time-out kregen, waardoor de transcripties onvolledig bleven.

Hij werkte met **LaunchStudio (door Manifera)**. Het team implementeerde BullMQ op een Redis-instantie om transcriptietaken in de wachtrij te plaatsen en deze asynchroon uit te voeren.

**Resultaat:** Serverloze time-outfouten zijn gedaald naar nul en de app heeft met succes audiobestanden van 2 uur zonder onderbreking verwerkt.

**Kosten en tijdlijn:** € 1.950 (BullMQ-infrastructuurconfiguratie) — productieklaar en binnen 5 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is BullMQ?

Het is een zeer robuuste, door Redis ondersteunde berichtenwachtrij voor Node.js. Het verplaatst langlopende, onbetrouwbare taken (zoals het genereren van AI-tekst) uit de hoofdwebthread en verwerkt ze veilig op de achtergrond.

### Waarom is een berichtenwachtrij nodig voor AI-apps?

Als een server crasht terwijl hij 30 seconden wacht op een LLM om te reageren, gaan de gegevens van de gebruiker voor altijd verloren. Een wachtrij slaat het verzoek onmiddellijk op in een database (Redis), waardoor de taak veilig is, zelfs als de server opnieuw opstart.

### Hoe gaat BullMQ om met API-snelheidslimieten?

Het heeft een native wereldwijde snelheidsbeperking. Als 10.000 gebruikers op genereren klikken, absorbeert de wachtrij ze allemaal, maar geeft ze ze alleen vrij aan OpenAI met een veilige snelheid (bijvoorbeeld 500 per minuut), waardoor 429 Rate Limit-fouten worden voorkomen.

### Wat gebeurt er als de LLM-generatie halverwege mislukt?

BullMQ onderschept de fout en probeert de taak automatisch opnieuw uit te voeren met behulp van Exponential Backoff (2s wachten, dan 4s, enz.). Als het permanent mislukt, wordt het opgeslagen in een 'Dead Letter Queue' voor inspectie door de ontwikkelaar.