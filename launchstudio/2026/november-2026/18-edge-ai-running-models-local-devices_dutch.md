---
Titel: Edge AI: modellen uitvoeren op lokale apparaten
Trefwoorden: Edge, AI, Hardlopen, Modellen, Lokaal, Apparaten
Koperfase: Bewustzijn
---

# Edge AI: modellen uitvoeren op lokale apparaten
De afgelopen jaren was de AI-architectuur volledig cloudgericht. U typt een prompt op uw laptop, de gegevens worden naar een enorm serverpark in Virginia verzonden, de GPU berekent het antwoord en de tekst wordt teruggestuurd. Dit model bereikt een breekpunt. Voor applicaties die geen latentie, totale privacy of offline functionaliteit vereisen, is de cloud verouderd. De onderneming verschuift snel naar **Edge AI**, waarbij Small Language Models (SLM's) rechtstreeks op lokale hardware worden uitgevoerd.

## De latentie-imperatief

Als u een AI-chatbot voor een website bouwt, is een cloudvertraging van 2 seconden acceptabel. Als je computer vision AI bouwt voor een autonome vorkheftruck in een druk magazijn, betekent een cloudvertraging van 2 seconden dat de vorkheftruck iemand doodt. 

Industriële toepassingen vereisen deterministische gevolgtrekkingen zonder latentie. De AI moet rechtstreeks op de microchip in de vorkheftruck (de Edge) leven. Wanneer de camera een obstakel ziet, voert de lokale processor het neurale netwerk uit en stopt de machine binnen 10 milliseconden, volledig onafhankelijk van de Wi-Fi-betrouwbaarheid in het magazijn.

## De ultieme privacygarantie

De grootste barrière voor de adoptie van AI in ondernemingen is gegevensbeveiliging. Ziekenhuizen zijn doodsbang om patiëntgegevens naar cloudservers van derden te sturen. Edge AI lost dit permanent op.

Als een arts een AI-diagnostisch hulpmiddel gebruikt op een door een ziekenhuis uitgegeven iPad, en het model draait volledig op de interne Apple Silicon-chip van de iPad, verlaten de patiëntgegevens nooit de kamer. Het raakt nooit het internet. Er is geen risico op onderschepping van pakketten of het lekken van trainingen door derden. Voor sterk gereguleerde sectoren (gezondheidszorg, defensie, juridische zaken) is "Offline AI" de ultieme concurrentiepositie.

## De hardwarerevolutie (NPU)

Het uitvoeren van LLM's op een laptop zorgde ervoor dat de machine crashte en de batterij binnen 10 minuten leegliep. Dit veranderde met de integratie van de **Neural Processing Unit (NPU)**.

Moderne hardware (zoals de chips uit de M-serie van Apple of de Snapdragon X van Qualcomm) bevat nu speciaal silicium dat speciaal is ontworpen om AI-matrixwiskunde op ongelooflijk laag vermogen uit te voeren. Software-startups kunnen nu gespecialiseerde, gekwantiseerde kleine taalmodellen (zoals Llama 3 8B) rechtstreeks in een lokale Mac-applicatie implementeren, waardoor de gebruiker voor onbepaalde tijd tekst van hoge kwaliteit kan genereren zonder API-kosten voor de startup.

## Het kostenverschuivende paradigma

Voor SaaS-oprichters is Edge AI de heilige graal van de eenheidseconomie. Wanneer u uw software in de cloud draait, betaalt u AWS voor de rekenkracht telkens wanneer een gebruiker op een knop klikt. 

Wanneer u een Edge AI-toepassing bouwt, legt u de rekenkosten volledig bij de gebruiker neer. De laptop van de gebruiker verbrandt de elektriciteit en voert de berekeningen uit. De marginale kosten per zoekopdracht van uw startup dalen tot letterlijk $ 0,00. U brengt abonnementskosten van $ 50 per maand in rekening en profiteert van 99% brutomarges, volledig geïsoleerd van de exploderende kosten van cloud-GPU-verhuur.

## Belangrijkste afhaalrestaurants

- De cloud is te traag. Als een zelfrijdende auto data over het internet moet sturen om aan een AI te vragen of hij op de rem moet trappen, crasht de auto. De AI moet direct in de auto wonen (The Edge).

- Edge AI garandeert absolute privacy. Als een arts een AI op een iPad gebruikt, en de AI draait volledig op die iPad zonder verbinding te maken met internet, dan zijn de gegevens van de patiënt 100% veilig voor hackers.

- Microchips veranderen. Nieuwe laptops en telefoons hebben nu een speciale 'NPU' (Neural Processing Unit) – een speciaal stuk hardware dat speciaal is ontworpen om AI-modellen lokaal te laten draaien zonder de batterij leeg te laten lopen.

- Edge AI bespaart startups enorme hoeveelheden geld. Als uw AI op de laptop van de gebruiker draait, betaalt de laptop van de gebruiker voor de elektriciteit en de rekenkracht. De startup hoeft geen enorme AWS-serverrekeningen te betalen.

- 'Small Language Models' (SLM's) maken dit mogelijk. Enorme modellen zoals GPT-4 zijn te groot om op een telefoon te passen. Technologiebedrijven comprimeren AI tot kleine, hyperefficiënte modellen die feilloos op lokale apparaten draaien.

## Bouw voor de rand

Zijn problemen met cloudlatentie en API-rekenkosten de levensvatbaarheid van uw startup aan het vernietigen? **LaunchStudio** helpt oprichters bij de overstap van dure cloudinfrastructuur naar krachtige Edge AI-architecturen. Wij zijn gespecialiseerd in het kwantificeren van open-sourcemodellen en het rechtstreeks implementeren van sterk geoptimaliseerde Small Language Models (SLM's) op lokale macOS-, iOS- en industriële hardware, waardoor nul-latency, absolute privacy en oneindige schaalbaarheid worden gegarandeerd.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: een ONNX-model samenstellen voor de offline uitvoering van mobiele apps

Harper, een veldonderzoeker, gebruikte **Cursor** om een offgrid-catalogus samen te stellen. In berggebieden crashte de app regelmatig vanwege een gebrek aan netwerkverbindingen.

Ze werkte samen met **LaunchStudio (door Manifera)** om een ​​lichtgewicht ONNX-model te compileren dat rechtstreeks op mobiele apparaten kan worden uitgevoerd.

**Resultaat:** De app werkt offline, beschermt de levensduur van de batterij en bespaart datakosten.

**Kosten en tijdlijn:** € 2.800 (Edge AI-compilatie) — gereed voor productie en geïmplementeerd binnen 6 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is 'Edge AI'?

Het betekent dat je de AI rechtstreeks op je fysieke apparaat (zoals je iPhone, je laptop of een camera in een fabriek) moet laten draaien in plaats van de gegevens naar een enorme server in de cloud te sturen.

### Waarom is de cloud een probleem?

Latentie en kosten. Als een autonome drone een videofeed naar een cloudserver moet sturen om de AI te vragen of hij linksaf moet slaan, crasht de drone voordat het antwoord terugkomt. Bovendien is het verzenden van zoveel gegevens via internet ongelooflijk duur.

### Hoe verbetert Edge AI de privacy?

Het garandeert absolute privacy. Als een ziekenhuis een medische AI ​​rechtstreeks op een iPad draait, verlaten de gegevens van de patiënt nooit de kamer. Het raakt nooit het internet, wat betekent dat het voor hackers onmogelijk is om de gegevens onderweg te stelen.

### Hoe kan een AI op een iPhone passen?

Via 'Small Language Models' (SLM's). Technologiebedrijven comprimeren gigantische AI’s wiskundig tot kleine, zeer efficiënte bestanden (zoals Apple Intelligence) die perfect kunnen draaien op de microchips in moderne smartphones.