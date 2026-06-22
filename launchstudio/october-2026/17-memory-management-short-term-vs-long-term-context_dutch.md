---
Titel: Geheugenbeheer: context op korte termijn versus lange termijn
Trefwoorden: geheugen, management, korte termijn, lange termijn, context
Koperfase: overweging
---

# Geheugenbeheer: context op korte termijn versus lange termijn
Een autonome agent die instructies van vijf minuten geleden vergeet, is enorm frustrerend. Omdat fundamentele LLM's volledig staatloos zijn (ze onthouden eerdere API-aanroepen niet), valt de last van Geheugenbeheer volledig op de backend-architectuur van de SaaS-startup. Als je een Agent wilt bouwen die aanvoelt als een echte collega (een die de voorkeuren van een klant van zes maanden geleden onthoudt), moet je de brug slaan tussen kortetermijncontext en langetermijnvectoropslag.

## De beperking van het contextvenster (korte termijn)

Het "Contextvenster" is het kortetermijnwerkgeheugen van de LLM. Het is het maximale aantal tokens (woorden) dat het model tegelijk kan verwerken. Om een ​​gesprek te kunnen voeren, moet uw Node.js-backend bij elk nieuw bericht de volledige geschiedenis van de chat terugsturen naar de LLM.

Dit creëert twee enorme problemen. Ten eerste **Kosten**. Als u voortdurend 50.000 tokens aan chatgeschiedenis opnieuw verzendt, alleen maar om een ​​eenvoudige vervolgvraag te stellen, zal uw API-factuur astronomisch zijn. Ten tweede, **Aandachtsverval**. Zelfs als een model beschikt over een contextvenster van 200.000 tokens, zorgt het plaatsen van zoveel gegevens in de prompt ervoor dat de AI de focus verliest en vaak instructies negeert die verborgen zijn in het midden van het enorme tekstblok.

## Context snoeien en samenvatten

Om het kortetermijnvenster efficiënt te beheren, moet u **Context Snoeien** uitvoeren. U kunt niet oneindig berichten toevoegen.

Wanneer de chatgeschiedenis 8.000 tokens bereikt, moet een achtergrondwerker stilletjes een prompt 'Samenvatten' activeren. Het neemt de oudste 6.000 tokens van het gesprek en condenseert deze tot een compacte samenvatting van 500 tokens van de belangrijkste feiten. Het verwijdert de ruwe oude berichten en plaatst de nieuwe samenvatting vóór het contextvenster. Dit verlaagt de API-kosten drastisch, terwijl de AI gefocust blijft op de onmiddellijke taak.

## Het langetermijngeheugen (RAG) ontwerpen

Als een zakelijke gebruiker tegen de agent zegt: *"Maak altijd kwartaalrapporten op volgens de Britse datumstandaard",* kan dat feit niet verloren gaan als de kortetermijncontext wordt ingeperkt. Het moet naar het langetermijngeheugen worden verplaatst.

Langetermijngeheugen wordt bereikt via een vectordatabase (zoals Pinecone of Milvus). Wanneer een gebruiker een regel of voorkeur opgeeft, haalt een "Extraction Agent" dat feit op en slaat het op als inbedding in de database. Drie maanden later, wanneer de gebruiker om een ​​nieuw rapport vraagt, voert uw backend een overeenkomstzoekopdracht uit in de Vector Database, vindt de regel "UK date standard" en injecteert deze dynamisch in de onmiddellijke prompt. De Agent ‘onthoudt’ de regel perfect zonder deze drie maanden in het kortetermijngeheugen vast te houden.

## Geheugenisolatie en beveiliging

In een B2B SaaS-omgeving moet het geheugen strikt geïsoleerd zijn. Als bedrijf A uw agent een eigen strategie leert, en bedrijf B de agent een gerelateerde vraag stelt, mag de agent nooit hallucineren en het geheugen van bedrijf A naar bedrijf B lekken.

Uw vectordatabase moet strikte huurderisolatie afdwingen. Elke geheugeninsluiting moet cryptografisch worden getagd met een specifieke 'tenant_id' en 'user_id'. Uw backend-query's moeten het ophalen van geheugen tussen verschillende tenants structureel voorkomen, waardoor absolute gegevensprivacy wordt gegarandeerd.

## Belangrijkste afhaalrestaurants

- LLM's zijn inherent 'staatloos': ze herinneren zich het laatste wat u zei niet. De backend-architectuur van de startup is volledig verantwoordelijk voor het beheer van het geheugen van de agent en het bieden van context voor elk verzoek.

- Het 'Contextvenster' is het kortetermijngeheugen. Hoewel moderne vensters enorm zijn, zorgt het vullen ervan met enorme chatgeschiedenis ervoor dat de AI de focus verliest (hallucineert) en dit resulteert in astronomische API-tokenkosten.

- Implementeer 'Context Snoeien'. Schrijf backend-scripts die periodiek oudere delen van het gesprek samenvatten, waarbij duizenden woorden worden vervangen door een compacte samenvatting van 500 woorden om geld te besparen en de AI gefocust te houden.

- Bouw langetermijngeheugen op met behulp van vectordatabases. Wanneer gebruikers belangrijke feiten of voorkeuren aangeven, sla deze feiten dan op in een database. Wanneer maanden later relevante taken verschijnen, doorzoekt u automatisch de database en voegt u de feiten in de prompt in.

- Dwing strikte 'Tenant Isolatie' af in uw Vector Database. Zorg ervoor dat herinneringen cryptografisch worden vergrendeld voor specifieke gebruikers, zodat de AI nooit per ongeluk de privéregels van bedrijf A naar bedrijf B lekt.

## Geef je agenten oneindig geheugen

Lijden uw AI-agenten aan geheugenverlies, wat uw zakelijke klanten frustreert die zichzelf voortdurend moeten herhalen? **LaunchStudio** ontwikkelt geavanceerde pijplijnen voor staatsbeheer, waarbij Context Pruning en veilige Vector Database-opslag naadloos worden geïntegreerd om uw B2B SaaS een oneindig, betrouwbaar langetermijngeheugen te geven.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: semantisch langetermijngeheugen opzoeken voor een AI-docent

Ethan, een onderwijzer, gebruikte **Lovable** om een taalleraar samen te stellen. Het opslaan van volledige gespreksgeschiedenissen binnen de promptcontext veroorzaakte hoge tokengebruikskosten.

Hij werkte samen met **LaunchStudio (door Manifera)** om een ​​laag voor het genereren van samenvattingen en een semantische inbeddingsdatabase voor langetermijngeheugenquery's te bouwen.

**Resultaat:** De maandelijkse API-facturen daalden met 55%, terwijl consistente, gepersonaliseerde studentenprofielen behouden bleven.

**Kosten en tijdlijn:** € 2.200 (Agent Memory Optimization) — productieklaar en binnen 5 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom vergeten LLM's dingen?

Omdat ze bij elke API-aanroep opnieuw beginnen. Als u geen code gebruikt om de hele chatgeschiedenis handmatig terug te sturen naar de AI telkens wanneer u een nieuw bericht typt, heeft het geen context van het gesprek.

### Wat is kortetermijngeheugen (contextvenster)?

De maximale hoeveelheid tekst die u in één keer aan de AI kunt invoeren. Als uw prompt deze limiet overschrijdt, zal de AI eenvoudigweg de oudste tekst verwijderen, waardoor in feite het begin van het project wordt 'vergeten'.

### Hoe bouw je een langetermijngeheugen op?

Door de AI te verbinden met een vectordatabase. Wanneer de gebruiker iets belangrijks zegt, slaat u dit op in de database. Later schrijf je code die de database doorzoekt op relevante feiten uit het verleden en deze aan de AI doorgeeft voordat deze antwoordt.

### Wat is 'Context snoeien'?

Een kostenbesparende techniek. In plaats van een chatgeschiedenis van 50 pagina's opnieuw naar de AI te sturen (wat erg duur is), laat je de AI de eerste 40 pagina's in één alinea samenvatten, waardoor de geschiedenis kort en goedkoop blijft.