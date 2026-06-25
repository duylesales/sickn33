---
Titel: De wiskunde van inbedding en zoeken naar overeenkomsten
Trefwoorden: Wiskunde, Inbedding, Gelijkenis, Zoeken
Koperfase: Bewustzijn
---

# De wiskunde van inbedding en zoeken naar overeenkomsten
Om een Retrieval-Augmented Generation (RAG)-pijplijn op te bouwen, moet u duizenden bedrijfsdocumenten onmiddellijk kunnen doorzoeken. Traditionele SQL-databases gebruiken 'Zoeken op trefwoord'. Als u zoekt naar 'auto', worden documenten waarin alleen het woord 'auto' wordt gebruikt volledig genegeerd. Zoeken op trefwoord is te rigide voor AI. De basis van moderne zakelijke AI is **Semantisch zoeken**, mogelijk gemaakt door de complexe wiskunde van **Vectorinsluitingen**.

## Concepten vertalen naar cijfers

Computers spreken geen Engels; ze spreken wiskunde. Een **insluiting** is het proces waarbij een stuk tekst (een woord, een zin of een hele pdf) door een neuraal netwerk wordt geleid dat de *betekenis* ervan vertaalt in een reeks getallen.

Het woord 'Apple' kan bijvoorbeeld een vector worden zoals: `[0,84, -0,12, 0,99, ...]`. In moderne insluitingsmodellen (zoals `text-embedding-3` van OpenAI) bevat deze array meer dan 1.500 getallen. Deze enorme reeks cijfers geeft perfect het abstracte concept van een Apple weer: de kleur, de vorm, de relatie met technologiebedrijven en de relatie met fruit.

## De geometrie van betekenis (vectorruimte)

Zodra u woorden in cijfers heeft omgezet, kunt u ze in een grafiek uitzetten. Stel je een enorme, 1500-dimensionale grafiek voor die een **vectorruimte** wordt genoemd.

Als u de vector voor 'Hond' en de vector voor 'Puppy' plot, worden ze fysiek heel dicht bij elkaar in de grafiek geplaatst omdat hun betekenissen vergelijkbaar zijn. De vector voor 'Carburateur' wordt miljoenen kilometers verwijderd van 'Hond'. Door menselijke taal in geometrie te vertalen, kan de AI wiskundig berekenen hoe vergelijkbaar twee concepten zijn, simpelweg door de fysieke afstand tussen hun coördinaten te meten.

## Het zoeken naar overeenkomsten uitvoeren

Wanneer een zakelijke gebruiker een vraag stelt als: *"Hoe vraag ik verlof aan?"*, voert de RAG-pijplijn een reeks wiskundige bewerkingen uit.

Ten eerste wordt de vraag van de gebruiker door het inbeddingsmodel geleid, waardoor deze in een vector (een punt op de grafiek) wordt omgezet. Vervolgens wordt uw vectordatabase doorzocht met de vraag: *"Vind mij de 5 documentvectoren die fysiek het dichtst bij mijn vraagvector liggen."*

De database gebruikt algoritmen (meestal **Cosinus Gelijkenis**) om direct de hoeken tussen de vectoren te meten. Het haalt de HR-handleiding op over 'Vakantiedagen'. Hoewel de gebruiker 'vrije tijd' heeft getypt en er in het document 'vakantie' staat, heeft de database dit gevonden omdat de concepten wiskundig gezien exact hetzelfde gebied in de vectorruimte in beslag nemen.

## De technische realiteit

Het begrijpen van de wiskunde is cruciaal voor architectonisch ontwerp, maar de technische realiteit is veel eenvoudiger. U hoeft Cosinus Gelijkenis-algoritmen niet helemaal opnieuw te schrijven in Python.

Enterprise SaaS-platforms maken gebruik van speciale **Vector Databases** (zoals Pinecone, Weaviate of pgvector). Deze databases zijn sterk geoptimaliseerde motoren die speciaal zijn ontworpen om geometrische afstandsberekeningen uit te voeren over miljarden vectoren in milliseconden. Je enige taak als ingenieur is om de Embedding API aan te roepen om de cijfers op te halen en die nummers in de database op te slaan.

## Belangrijkste afhaalrestaurants

- Traditioneel 'Zoeken op trefwoord' is nutteloos voor AI, omdat er alleen wordt gezocht naar exacte letterovereenkomsten. 'Semantic Search' begrijpt de werkelijke betekenis van de woorden, waardoor relevante documenten kunnen worden gevonden, zelfs als er een andere woordenschat wordt gebruikt.

- Een 'Embedding' is een vertaling. Een gespecialiseerd AI-model leest een tekstblok en vertaalt de abstracte betekenis ervan in een enorme reeks getallen (een vector).

- Wanneer je deze getallen in een multidimensionale grafiek (Vectorruimte) plot, worden concepten die hetzelfde betekenen (zoals 'hond' en 'puppy') fysiek heel dicht bij elkaar geplaatst.

- 'Similarity Search' is slechts geometrie. Wanneer een gebruiker een vraag stelt, zet het systeem de vraag om in cijfers en berekent het welke documenten in de database wiskundig gezien het dichtst bij de vraag liggen.

- Je hebt geen wiskundediploma nodig om dit te bouwen. Moderne vectordatabases (zoals Pinecone) verwerken alle brutale geometrie achter de schermen. U geeft ze eenvoudigweg de cijfers door en zij sturen u onmiddellijk de meest relevante documenten terug.

## Beheers semantisch zoeken

Geven uw zoekprogramma's voor ondernemingen irrelevante resultaten omdat ze nog steeds afhankelijk zijn van verouderde zoekwoorden? **LaunchStudio** ontwerpt geavanceerde Vector Embedding-pijplijnen en semantische zoeksystemen, waarbij gebruik wordt gemaakt van de complexe wiskunde van AI om direct de perfecte bedrijfseigen gegevens voor uw RAG-workflows op te halen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: normalisatie inbedden voor een muziekdatabase

Isaac, oprichter van een muziekportaal, gebruikte **Bolt** om een bot voor afspeellijstaanbevelingen te bouwen. Cosinus-gelijkenisquery's leverden onnauwkeurige resultaten op vanwege niet-genormaliseerde vectorstatistieken.

Hij werkte samen met **LaunchStudio (door Manifera)** om vectorinbedding te normaliseren en dynamische hybride zoekfilters te implementeren.

**Resultaat:** De nauwkeurigheid van het matchen van afspeellijsten is met 40% toegenomen, waardoor de gemiddelde duur van gebruikerssessies toeneemt.

**Kosten en tijdlijn:** € 1.700 (Vector Normalisatiepakket) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een inbedding?

Een vertaling van taal naar wiskunde. Er is een menselijk concept als 'Apple' voor nodig en het wordt omgezet in een gigantische lijst met getallen die perfect representeert alles wat een Apple is (een fruit, rood, zoet, een technologiebedrijf).

### Waarom zijn cijfers beter dan woorden voor zoeken?

Omdat mensen verschillende woorden gebruiken voor hetzelfde. Als u in een oude database zoekt naar 'Verlof', wordt het beleid 'Vakantie' niet gevonden. Wiskunde lost dit op, omdat de numerieke 'betekenis' van beide termen vrijwel identiek is.

### Wat is een vectorruimte?

Stel je een enorme 3D-kaart van het universum voor, maar in plaats van planeten bevat deze concepten. Verwante concepten (katten, honden, muizen) klonteren samen in één sterrenstelsel, terwijl niet-verwante concepten (auto's, motoren, banden) samenklonteren in een ander sterrenstelsel.

### Wat is cosinusovereenkomst?

De standaard wiskundige formule die door databases wordt gebruikt om de afstand tussen twee concepten op de kaart te meten. Hoe kleiner de afstand, hoe relevanter het document is voor de vraag van de gebruiker.