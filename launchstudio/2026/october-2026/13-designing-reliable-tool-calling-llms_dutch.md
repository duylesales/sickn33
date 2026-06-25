---
Titel: Het ontwerpen van een betrouwbaar hulpmiddel voor LLM's
Trefwoorden: Ontwerpen, Betrouwbaar, Tool, Bellen, LLM's
Koperfase: Bewustzijn
---

# Betrouwbare tool ontwerpen voor LLM's
Een autonome agent is een brein; zijn **Tools** zijn zijn handen. Als de hersenen de handen niet kunnen coördineren, is de agent nutteloos. Tool Calling (of Function Calling) is de brug tussen probabilistisch LLM-denken en deterministische backend-uitvoering. LLM's zijn echter notoir slordig. Als u uw toolschema's niet extreem nauwkeurig ontwerpt, zal de LLM variabelen hallucineren, verkeerd opgestelde JSON uitvoeren en uw Node.js-server herhaaldelijk laten crashen.

## Het gevaar van parameterhallucinatie

Wanneer u een LLM een tool als `book_flight(destination, date)` geeft, vertrouwt u erop dat de LLM deze variabelen correct invult op basis van de prompt van de gebruiker. Dit is zeer riskant.

Als de gebruiker zegt: *"Boek een vlucht naar Parijs voor aanstaande vrijdag",* kan een slecht beperkte LLM de JSON uitvoeren: `{ "destination": "Paris", "date": "next Friday" }`. Wanneer uw backend probeert de string "volgende vrijdag" in de SQL-database van de luchtvaartmaatschappij te injecteren, mislukt de zoekopdracht en loopt de applicatie vast. De LLM moet worden gedwongen strikte gegevenstypen uit te voeren.

## Strenge JSON-schema's definiëren

Om parameterhallucinatie te voorkomen, moeten uw gereedschapsdefinities onaangenaam gedetailleerd zijn. U kunt een parameter niet zomaar 'datum' noemen. U moet het definiëren met behulp van het strikte **JSON-schema**.

U moet het volgende opgeven: `"type": "string", "description": "De vertrekdatum. MOET de strikte ISO 8601 JJJJ-MM-DD-indeling hebben. Gebruik geen woorden als 'morgen'."`

Gebruik bovendien waar mogelijk **Enums**. Als uw tool een valutacode vereist, laat de LLM dan niet raden. Geef een enum-array op: `["USD", "EUR", "GBP"]`. Door de keuzes van de LLM te beperken tot een hardgecodeerde lijst, elimineert u wiskundig de mogelijkheid dat deze een nepvaluta hallucineert.

## De 'gestructureerde output'-revolutie

Historisch gezien moesten ontwikkelaars complexe herhalingslussen schrijven om de LLM te smeken de kapotte JSON te repareren. Onlangs hebben API-providers (zoals OpenAI) **Structured Outputs** geïntroduceerd.

Met gestructureerde uitvoer kunt u een JSON-schema doorgeven aan de API, en de backend van de provider verandert feitelijk de kansen voor het genereren van tokens door de LLM om te *garanderen* dat de uitvoer perfect overeenkomt met uw schema. Als uw schema vier specifieke sleutels vereist, kan de LLM fysiek geen JSON-object uitvoeren met slechts drie sleutels. Het benutten van gestructureerde output is een verplichte architecturale vereiste voor bedrijfsstabiliteit.

## Sierlijke foutafhandeling (de feedbacklus)

Zelfs met perfecte JSON kan de daadwerkelijke uitvoering van het hulpprogramma mislukken (de webschraper wordt bijvoorbeeld geblokkeerd door een CAPTCHA). Traditionele code crasht bij een 500-fout. Agentcode mag niet.

Wanneer een tool faalt in uw backend, moet u de fout opvangen, deze opmaken als een string (bijvoorbeeld *"SYSTEEMBERICHT: Uitvoering van de tool mislukt. Fout 403 verboden. De doelwebsite heeft de scraper geblokkeerd."*) en die string terugsturen naar de LLM. De LLM fungeert als foutafhandelaar. Het leest de mislukking, denkt na en besluit: *"Oké, de schraper is mislukt. Ik zal in plaats daarvan de tool 'Search_Google' gebruiken."* Dit creëert echte, veerkrachtige autonomie.

## Belangrijkste afhaalrestaurants

- Tool Calling is het mechanisme waarmee een LLM kan communiceren met uw backend-databases en API's door gestructureerde JSON-opdrachten uit te voeren in plaats van conversatietekst.

- LLM's zijn slordig. Als je ze niet beperkt, zullen ze parameters hallucineren (bijvoorbeeld door de string 'morgen' door te geven in plaats van een correct opgemaakte datum), waardoor je backend-code crasht.

- Schrijf onaangenaam gedetailleerde JSON-schema's voor uw tools. Gebruik strikte typedefinities, duidelijke beschrijvingen en maak intensief gebruik van 'Enums' (hardgecodeerde lijsten met acceptabele opties) om te voorkomen dat de LLM nepgegevens verzint.

- Gebruik 'gestructureerde uitvoer' (indien ondersteund door uw LLM-provider) om wiskundig te garanderen dat de JSON-uitvoer van de AI perfect aansluit bij de vereisten van uw backend-schema, waardoor parseerfouten worden geëlimineerd.

- Laat een mislukte API-oproep de agent nooit laten crashen. Vang de fout op in uw backend, zet deze om in tekst en stuur deze terug naar de LLM, zodat de AI de fout autonoom kan analyseren en een ander hulpmiddel kan proberen om het probleem op te lossen.

## Maak uw AI-integraties waterdicht

Crashen uw autonome agenten voortdurend uw backend omdat ze verkeerd opgestelde JSON of hallucinante parameters uitvoeren? **LaunchStudio** ontwikkelt kogelvrije Tool Calling-architecturen, waarbij gebruik wordt gemaakt van strikte JSON Schema-afdwinging en geavanceerde foutfeedbacklussen om ervoor te zorgen dat uw agenten complexe B2B API-integraties feilloos uitvoeren.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: strikte Zod-schemavalidatie voor CRM-updates

Lily, een marketingmanager, gebruikte **Bolt** om een leadscore-agent op te zetten. De agent gaf af en toe ongeldige parameterschema's door aan client-CRM's, waardoor systeemfouten ontstonden.

Ze werkte samen met **LaunchStudio (door Manifera)** om strikte Zod-validatieschema's en automatische fouthandlers voor nieuwe pogingen te bouwen.

**Resultaat:** CRM-synchronisatiefouten zijn gedaald tot 0%, waardoor betrouwbare geautomatiseerde marketinglogboeken zijn gegarandeerd.

**Kosten en tijdlijn:** € 1.900 (Tool Calling Hardening) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is gereedschapsoproep (functieoproep)?

Hiermee kan de AI acties in uw software activeren. De AI voert een JSON-blok uit met de tekst 'Voer de tool voor het verwijderen van gebruikers uit voor ID 123'. Uw server ontvangt de JSON en voert de daadwerkelijke code uit om de gebruiker te verwijderen.

### Waarom mislukt Tool Calling?

Omdat LLM's raden. Als uw backend een geheel getal vereist voor een gebruikers-ID, maar de LLM een tekstreeks ('John Doe') uitvoert, crasht de databasequery van uw server. U moet de LLM dwingen om het exact juiste formaat uit te voeren.

### Hoe dwing je de LLM om correcte gegevens uit te voeren?

Door ongelooflijk strikte instructies te geven in de Tooldefinitie. Als u de LLM vertelt: 'U MOET het JJJJ-MM-DD-formaat gebruiken voor datums', is de kans veel kleiner dat er een opmaakfout wordt gemaakt.

### Wat is 'gestructureerde output'?

Een recente, krachtige API-functie waarbij de LLM-provider wiskundig garandeert dat de AI perfecte JSON zal uitvoeren die precies overeenkomt met uw regels, waardoor de nachtmerrie van kapotte JSON-parsing volledig wordt beëindigd.