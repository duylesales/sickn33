---
Titel: 10k gelijktijdige SSE-verbindingen verwerken in Node.js
Trefwoorden: AI in software-engineering, afhandeling, gelijktijdig, SSE, verbindingen, knooppunt
Koperfase: Bewustzijn
---

# Omgaan met 10k gelijktijdige SSE-verbindingen in Node.js
Om een B2B AI-product te bouwen dat magisch aanvoelt, moet u het LLM-antwoord woord voor woord naar de gebruikersinterface streamen met behulp van Server-Sent Events (SSE). Dit "typemachine-effect" bewijst dat het systeem werkt en verlaagt de waargenomen latentie tot bijna nul. Architectonisch gezien is SSE echter een tikkende tijdbom. Als u duizenden langlevende HTTP-verbindingen tegelijkertijd open houdt, raakt het geheugen en de verbindingspools van uw Node.js-server uitgeput, wat catastrofale crashes veroorzaakt tijdens verkeerspieken.

## Het probleem van de uitputting van de verbindingspool

Traditionele REST API’s zijn kortstondig. Een gebruiker vraagt ​​om een ​​dashboard, de Node-server vraagt ​​de DB op, retourneert de JSON en sluit de verbinding binnen 50 milliseconden. Eén enkele server kan duizenden van deze snelle verzoeken verwerken.

SSE-verbindingen zijn persistent. Als een LLM er 30 seconden over doet om een ​​complex contract te genereren, moet de Node-server die exacte HTTP-verbinding de hele 30 seconden open houden in het geheugen. Als 10.000 gebruikers tegelijkertijd op "Genereren" klikken, probeert de server 10.000 open TCP-verbindingen vast te houden. Node zal snel de maximale open bestandsdescriptorlimiet bereiken (meestal 1.024 op Linux) of geen heapgeheugen meer hebben, waardoor de hele instantie crasht.

## Ontkoppeling via Redis Pub/Sub

Het is niet mogelijk dat dezelfde serverthread die de zware OpenAI API-aanroep beheert, ook de SSE-stream naar de client beheert. U moet de architectuur ontkoppelen met Redis Pub/Sub (Publiceren/Abonneren).

**De schaalbare workflow:**

1. De gebruiker maakt via SSE verbinding met een lichtgewicht "Streaming Server" en abonneert zich op een unieke 'Kanaal-ID'.

2. De prompt wordt naar een "Worker Node" op de achtergrond gestuurd (via BullMQ).

3. De Worker Node maakt de langzame, zware verbinding met OpenAI. Wanneer de Werker tokens ontvangt van OpenAI, *publiceert* hij deze tokens onmiddellijk naar de Redis `Channel ID`.

4. De Streaming Server, die absoluut geen zware berekeningen uitvoert, leest eenvoudigweg de tokens van Redis en duwt ze via de open SSE-verbinding naar de client.

Met deze architectuur kunt u de zware AI-rekenknooppunten onafhankelijk van de lichtgewicht UI-streamingknooppunten schalen.

## De load balancer configureren

Het schalen van SSE mislukt vaak op de infrastructuurlaag, niet op de applicatielaag. Standaard Load Balancers (zoals Nginx of AWS Application Load Balancer) zijn ontworpen om reacties te "bufferen". Ze wachten tot de server klaar is met het verzenden van de volledige payload voordat ze deze doorgeven aan de client.

Als uw load balancer een SSE-stream buffert, wordt het "typemachine-effect" vernietigd. De gebruiker ziet gedurende 15 seconden een leeg scherm, waarna de hele paragraaf in één keer verschijnt. U moet uw load balancer expliciet configureren om buffering uit te schakelen en verbindingstime-outs te verhogen (vaak `proxy_read_timeout` instellen op 300 seconden) om persistente streams te ondersteunen.

## Sierlijke verbinding verbroken

Gebruikers zijn ongeduldig. Een gebruiker kan op 'Genereren' klikken, twee seconden wachten en vervolgens naar een andere pagina navigeren. Als de frontend de verbinding verbreekt, moet je backend dit direct beseffen.

Als uw Node-server doorgaat met het uitvoeren van de OpenAI API-aanroep en het streamen van tokens naar de leegte nadat de gebruiker zijn browsertabblad heeft gesloten, verbrandt u dure API-credits voor een geest. U moet `req.on('close')` luisteraars in Express implementeren om de upstream OpenAI-generatie API-aanroep onmiddellijk af te breken zodra de client de verbinding verbreekt.

## Belangrijkste afhaalrestaurants

- Server-Sent Events (SSE) streamen tekst woord voor woord naar de gebruikersinterface, wat verplicht is voor AI UX. Maar ze vereisen dat langlevende HTTP-verbindingen 15 tot 30 seconden open blijven.

- Als een enkele Node.js-server duizenden persistente SSE-verbindingen probeert vast te houden en tegelijkertijd langzame OpenAI API-aanroepen beheert, crasht deze als gevolg van geheugenuitputting.

- Ontkoppel de architectuur: gebruik zware achtergrondwerkers om de LLM-generatie te beheren en 'publiceer' de streamingtokens naar een Redis-wachtrij. Een lichtgewicht webserver leest de wachtrij en verzorgt de UI-streaming.

- Standaard load balancers (zoals Nginx) bufferen streaming-reacties, waardoor het typemachine-effect wordt verpest. U moet de proxy expliciet configureren om buffering uit te schakelen en permanente verbindingen toe te staan.

- Luister altijd of de client de verbinding verbreekt. Als de gebruiker het browsertabblad sluit, moet de server de upstream OpenAI-oproep onmiddellijk afbreken om te voorkomen dat dure API-credits op een dode stream worden verbrand.

## Schaal je streams

Zorgen verkeerspieken ervoor dat uw realtime AI-streams crashen? **LaunchStudio** architecten zijn sterk ontkoppelde, door Redis ondersteunde streaming-architecturen, ontworpen om tienduizenden gelijktijdige SSE-verbindingen veilig te beheren zonder ook maar één token te laten vallen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Buffervertraging door server verzonden gebeurtenissen (SSE) in een livechat SaaS oplossen

Mason, een productmanager, gebruikte **Cursor** om een klantenportaal te bouwen. De streamingtekst verscheen in grote, vertraagde brokken in plaats van vloeiende woord-voor-woord-streams vanwege Nginx-buffering.

Hij nam contact op met **LaunchStudio (door Manifera)**. Het team heeft de productie-Nginx-proxyinstellingen aangepast om buffering op SSE-reactiestromen uit te schakelen.

**Resultaat:** De tekststroom wordt soepel in realtime weergegeven, waardoor de gebruikerservaring van de chatinterface wordt verbeterd.

**Kosten en tijdlijn:** € 950 (SSE-configuratiepakket) — productieklaar en binnen 2 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat zijn door de server verzonden gebeurtenissen (SSE)?

Een protocol waarmee een server realtime gegevens naar een browser kan sturen via een enkele HTTP-verbinding. Het is de standaardmethode die wordt gebruikt om het woord-voor-woord ‘typemachine-effect’ te creëren bij het genereren van AI.

### Waarom is SSE gevaarlijk voor de servergezondheid?

Omdat een SSE-verbinding de hele AI-generatie van 30 seconden open blijft. Het vasthouden van duizenden gelijktijdige open verbindingen zal de geheugenlimieten van een enkele server snel uitputten en deze doen crashen.

### Hoe helpt Redis Pub/Sub SSE te schalen?

Het ontkoppelt het zware tillen. Een achtergrondwerker voert de langzame OpenAI-aanroep uit en 'publiceert' tokens naar Redis. Een lichtgewicht webserver leest eenvoudigweg de tokens en streamt deze naar de gebruiker.

### Hoe balanceer je SSE-verbindingen?

U moet uw load balancer (zoals Nginx) configureren om responsbuffering uit te schakelen. Als het buffert, houdt het de stream vast totdat deze is voltooid, waardoor het realtime UX-effect wordt verpest.