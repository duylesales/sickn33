---
Titel: LLM-contextvensters beheren
Trefwoorden: Beheren, LLM, Context, Windows
Koperfase: Bewustzijn
---

# Hoe LLM-contextvensters te beheren
In 2023 waren startups maanden bezig met het bouwen van complexe RAG-pijplijnen, omdat LLM’s slechts 4.000 tokens tegelijk konden verwerken. Tegenwoordig bieden modellen zoals Claude 3 enorme contextvensters van 200.000 tokens. De verleiding voor ontwikkelaars is om de architectuur volledig achter zich te laten en simpelweg hele SQL-databases en pdf's van 500 pagina's in de prompt te dumpen. Deze ‘Context Stuffing’-aanpak is de snelste manier om uw SaaS failliet te laten gaan en uw reactienauwkeurigheid te vernietigen.

## De eenheidseconomie van contextvulling

API-providers rekenen per token. Als u elke keer dat een gebruiker een vraag stelt een document met 100.000 tokens in GPT-4o invoert, kan die enkele API-aanroep $ 0,50 kosten. Als de gebruiker tien vervolgvragen stelt, verzendt u het enorme document tien keer. U heeft zojuist $ 5,00 uitgegeven aan één gebruikerssessie.

Bovendien kost het lezen van 100.000 tokens tijd. De latentie van uw toepassing zal toenemen. Efficiënt contextmanagement gaat niet alleen over elegante architectuur; het gaat om het beschermen van uw winstmarges.

## Het fenomeen 'Lost in the Middle'

Zelfs als je onbeperkt kapitaal kunt uitgeven aan tokens, verminderen enorme contextvensters de AI-intelligentie. Academisch onderzoek heeft herhaaldelijk het fenomeen ‘Lost in the Middle’ bewezen.

LLM's hebben een U-vormige aandachtscurve. Als je een LLM een document van 50 pagina's geeft, zal hij de informatie van pagina 1 en pagina 50 perfect onthouden. Zijn aandachtsspanne zakt echter halverwege in. Als het antwoord op de vraag van de gebruiker op pagina 25 staat, zal de LLM dit vaak negeren of een antwoord volledig hallucineren. Het bieden van een LLM met *minder*, zeer relevante context resulteert in een dramatisch hogere nauwkeurigheid.

## Chatgeschiedenis beheren: de samenvattingsstrategie

In een langlopende chattoepassing zal het toevoegen van elk afzonderlijk bericht dat ooit aan de promptarray is verzonden, het contextvenster snel doen verdwijnen. Je moet de geschiedenis inkorten.

**Het schuifvenster:** De eenvoudigste aanpak is om alleen de systeemprompt en de laatste 10 berichten van het gesprek te verzenden. De AI vergeet alles vanaf bericht 11. Dit is goedkoop, maar doet pijn aan de UX.

**De samenvattingspijplijn:** De bedrijfsoplossing. Wanneer een gesprek 10 berichten bevat, draait een goedkoop, snel model (zoals Llama 3 8B) op de achtergrond. Het leest de tien berichten en vat ze samen in een paragraaf van drie zinnen. Deze strakke samenvatting, plus de 2 meest recente berichten, geeft u vervolgens door aan de hoofd LLM. Je bewaart het langetermijngeheugen van het gesprek terwijl je bijna nul tokens verbruikt.

## Strikte RAG-chunking

Retrieval-Augmented Generation (RAG) blijft verplicht, ongeacht hoe groot contextvensters worden. Wanneer een gebruiker een vraag stelt, moet u uw vectordatabase gebruiken om alleen de drie meest wiskundig relevante paragrafen uit de bedrijfsdatabase op te halen.

In plaats van 200.000 tokens nutteloze bedrijfsgegevens te verzenden, verzendt u 500 tokens met zeer relevante gegevens. De LLM verwerkt het onmiddellijk, het kost fracties van een cent, en omdat er geen ‘midden’ is om in te verdwalen, daalt het aantal hallucinaties tot bijna nul.

## Belangrijkste afhaalrestaurants

- Het feit dat een LLM een enorm contextvenster van 200k heeft, betekent niet dat u deze moet gebruiken. 'Context' Als u enorme documenten in elke prompt stopt, worden uw winstmarges vernietigd.

- LLM's lijden aan het fenomeen 'Lost in the Middle'. Ze herinneren zich het begin en einde van lange prompts, maar hallucineren of negeren vaak gegevens die verborgen liggen in het midden van enorme teksten.

- Stuur nooit de volledige oneindige chatgeschiedenis van een gebruiker naar de API. Implementeer een 'Sliding Window' (waarbij alleen de laatste 10 berichten worden verzonden) om het aantal tokens laag te houden en de latentie snel.

- Gebruik voor langdurig chatgeheugen een goedkoop achtergrondmodel om oudere berichten voortdurend in een korte alinea samen te vatten, waarbij u die samenvatting in de prompt injecteert in plaats van in de ruwe geschiedenis.

- Retrieval-Augmented Generation (RAG) is nog steeds verplicht. Het injecteren van 500 tokens aan zeer relevante gegevens levert altijd snellere, goedkopere en nauwkeurigere resultaten op dan het injecteren van 100.000 tokens aan ruwe gegevens.

## Optimaliseer uw tokenuitgaven

Zijn enorme prompts de start- en landingsbaan van uw startup aan het opvreten? **LaunchStudio** architecten sterk geoptimaliseerde RAG-pijplijnen en contextsamenvattingslussen die uw LLM API-kosten drastisch verlagen en tegelijkertijd de nauwkeurigheid van uw applicatie verbeteren.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Context Pruning implementeren voor een juridische documentassistent

Amelia, een advocaat, gebruikte **Bolt** om een app voor het zoeken naar jurisprudentie te bouwen. Grote juridische documenten vulden het LLM-contextvenster, wat hoge API-kosten en verminderde uitvoernauwkeurigheid veroorzaakte.

Ze werkte samen met **LaunchStudio (door Manifera)** om een ​​geautomatiseerd algoritme voor het opschonen van context te bouwen dat opgehaalde tekstfragmenten rangschikte op relevantie.

**Resultaat:** De gemiddelde promptgrootte daalde met 50% en de API-kosten per zoekopdracht werden gehalveerd, terwijl de nauwkeurigheid van de evaluatie hoog bleef.

**Kosten en tijdlijn:** € 1.750 (Context Pruning Integration) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een contextvenster?

De maximale hoeveelheid tekst (tokens) die een AI in zijn ‘werkgeheugen’ kan bewaren voor één enkele prompt. Dankzij grote contextvensters kunt u hele boeken in één keer aan de AI doorgeven.

### Waarom zou ik niet alles in het contextvenster stoppen?

Kosten en latentie. U betaalt voor elke token die u verzendt. Het verzenden van 100.000 tokens voor een eenvoudige zoekopdracht is ongelooflijk duur en zorgt ervoor dat het model er veel langer over doet om een ​​antwoord te berekenen.

### Wat is het fenomeen 'Lost in the Middle'?

LLM's hebben gebrekkige aandachtsmechanismen. Als je ze een enorm document geeft, herinneren ze zich het allereerste begin en het einde, maar negeren of hallucineren ze vaak de feiten die op de middelste pagina's verborgen zijn.

### Hoe beheer ik de chatgeschiedenis zonder de context op te blazen?

Stuur niet elke keer het volledige gesprek. Gebruik een achtergrondproces om oudere chatberichten samen te vatten in een strakke alinea. Verstuur de samenvatting en alleen de 2 meest recente onbewerkte berichten.