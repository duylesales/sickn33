---
Titel: "Transformers en Vector Embeddings: De Architectuur van How AI Works"
Trefwoorden: AI works, hoe AI werkt, generatieve AI uitgelegd, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelpersona: Product Manager / Niet-Technische Oprichter
---

# Transformers en Vector Embeddings: De Architectuur van How AI Works

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Generatieve AI Werkt Onder de Motorkap: Een Gids voor Product Managers",
  "description": "Om succesvolle AI-functies te ontwerpen moeten Product Managers stoppen met AI zien als magie en de onderliggende mechanica begrijpen: transformers, attention en vector-embeddings.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-works"
  }
}
</script>

De gevaarlijkste aanname die een Product Manager in 2026 kan doen, is een AI-model behandelen als een magische zwarte doos.

Wanneer een PM in een functioneel ontwerp schrijft: *"De AI analyseert de klantdata en genereert op magische wijze een perfect analyserapport"*, stuurt hij het software-ontwikkelteam rechtstreeks af op een mislukking. AI is geen tovenarij; het is toegepaste wiskunde met harde beperkingen, specifieke eigenaardigheden en duidelijke architectonische wetten.

Om softwarefuncties te ontwerpen die daadwerkelijk waarde toevoegen zonder uw bedrijf failliet te laten gaan aan torenhoge API-facturen, moeten Product Managers begrijpen hoe generatieve AI onder de motorkap functioneert. U hoeft geen code te schrijven, maar u moet de drie kernmechanismen van Large Language Models (LLM's) doorgronden: **de Transformer**, **het Attention-Mechanisme** en **Vector Embeddings**.

Dit inzicht stelt u in staat om de vraag *"Kan de AI dit?"* te transformeren naar de eis: *"Zo moeten we de data-architectuur inrichten om dit betrouwbaar te realiseren."*

## De Motor: De Transformer-Architectuur

Vóór 2017 lazen taalmodellen tekst sequentieel — woord voor woord, zoals een mens een boek leest. Was het document lang, dan was het model aan het einde van hoofdstuk tien alweer vergeten wat er in hoofdstuk één gebeurde.

Toen introduceerde Google de **Transformer**.

Een Transformer leest tekst niet woord voor woord, maar verwerkt het gehele document gelijktijdig. Het analyseert elk woord in relatie tot álle andere woorden op hetzelfde moment. Deze massale parallelle verwerking maakt moderne modellen (zoals GPT-4o of Claude) zo razendsnel en contextueel scherp.

**Wat dit betekent voor Product Management:** Omdat Transformers enorme parallelle rekenkracht (GPU's) vereisen, rekenen leveranciers af per "Token" (ongeveer 3/4 van een woord). Elke keer dat u een functie ontwerpt die 10.000 woorden naar een LLM stuurt, tikt de meter door. Uw kerntaak als PM is bepalen hoe u het gewenste resultaat bereikt met zo *min mogelijk tokens* naar de Transformer.

## Het Stuur: Het Attention-Mechanisme

Het geheim binnen de Transformer is het **Self-Attention Mechanisme**.

Neem de zin: *"De bank van de rivier was modderig, dus ging hij naar de bank om geld te pinnen."*
Het woord "bank" komt twee keer voor, maar heeft twee totaal verschillende betekenissen. Traditionele software kan dit nauwelijks onderscheiden. Het Attention-mechanisme lost dit op door wiskundige "gewichten" toe te kennen aan omliggende woorden: bij de eerste "bank" kijkt het naar "rivier" en "modderig"; bij de tweede naar "geld" en "pinnen".

**Wat dit betekent voor Product Management (Aandachtsverwatering):** Attention is een eindige bron. Geeft u een LLM een PDF van 50 pagina's en stelt u een vraag over pagina 25, dan raakt de aandacht over 50 pagina's uitgesmeerd. Dit veroorzaakt het *Lost in the Middle* fenomeen: de AI vergeet feiten in het midden van het document of begint te hallucineren. Als PM kunt u ontwikkelaars niet opdragen "het hele document op te sturen"; u moet functies ontwerpen die data opdelen in kleine, hyper-relevante fragmenten.

## De Kaartenbak: Vector Embeddings

Hoe begrijpt een computer dat "Koning" verwant is aan "Koningin", en "Appel" aan "Banaan"?

Via **Vector Embeddings**. Dit is een wiskundig proces dat een woord of alinea omzet in een lange reeks getallen (vaak 1.536 getallen lang). Deze getallen fungeren als coördinaten op een gigantische, meerdimensionale landkaart.

Op deze kaart ligt het coördinaat voor "Appel" vlak naast "Banaan", terwijl het coördinaat voor "Vrachtwagen" heel ver weg ligt.

**Wat dit betekent voor Product Management (RAG):** Als u een functie bouwt waarmee de AI zoekt in bedrijfsspecifieke documenten (zoals eerdere supporttickets), gebruikt u geen traditionele trefwoordzoekmachine, maar Vector Embeddings. U zet alle documenten om in vectoren. Stelt een bezoeker een vraag, dan zoekt het systeem de documenten op die *fysiek het dichtst bij die vraag liggen op de kaart*. Dit heet Retrieval-Augmented Generation (RAG). Als PM ontwerpt u geen zoekbalken meer, maar semantische zoekmotoren.

## Hoe LaunchStudio AI-Theorie Vertaalt Naar Werkende Software

Product Managers worstelen regelmatig om hun ideeën technisch te vertalen naar hun engineeringteams.

[LaunchStudio](https://launchstudio.eu/en/), aangedreven door de enterprise-engineers van [Manifera](https://www.manifera.com/) onder leiding van Herre Roelevink in Amsterdam en Ho Chi Minhstad, fungeert als de technische brug tussen productvisie en backend-architectuur:
1. **Token-Optimalisatie:** Wij bouwen middleware die token-payloads minimaliseert, waardoor uw software winstgevend blijft.
2. **Contextbeheer:** Wij ontwerpen slimme chunking- en routeringsalgoritmen die Aandachtsverwatering voorkomen en hallucinaties elimineren.
3. **Vectordatabase Inrichting:** Wij configureren PostgreSQL met `pgvector` en semantische caching om van ruwe embeddings betrouwbare RAG-functies te maken.

## Echt voorbeeld

### Een AI-Native Oprichter in de Praktijk: De Juridische PM Die Stopte Met De AI de Schuld Te Geven

Julia was Product Manager bij een LegalTech-startup in Londen. Ze ontwierp een feature genaamd "Contractsamenvatting": gebruikers uploadden een huurovereenkomst van 100 pagina's en ontvingen een overzicht van de belangrijkste aansprakelijkheden in 5 opsommingstekens.

Haar functionele eis luidde: *"Stuur de PDF naar OpenAI en vraag om een samenvatting."* De junior ontwikkelaars bouwden exact dat.

In de praktijk was de functie onbruikbaar: soms was de samenvatting prima, maar vaak verzon de AI niet-bestaande clausules. Bovendien kostte elke zoekopdracht €0,45 en liep de applicatie in 30% van de gevallen tegen een time-out aan.

Julia gaf OpenAI de schuld: *"Het model is simpelweg niet slim genoeg voor juridische contracten"*, rapporteerde ze aan haar directie.

De directie schakelde LaunchStudio in voor een technische audit. Het Manifera-team stelde direct de diagnose: Julia had de AI als magie behandeld en de wetten van Aandachtsverwatering en tokengrenzen genegeerd. Het sturen van 100 pagina's naar het model veroorzaakte de hallucinaties en time-outs.

In 10 werkdagen herbouwde LaunchStudio de feature volgens de regels van AI-engineering:
- Het 100 pagina's tellende document werd omgezet in vector-embeddings.
- Moest er een samenvatting van aansprakelijkheden worden gemaakt, dan voerde het systeem een vectorzoekopdracht uit naar passages gerelateerd aan "aansprakelijkheid, risico en vrijwaring".
- Het systeem haalde uitsluitend de 5 meest relevante alinea's op (ongeveer 2 pagina's tekst) en stuurde *alleen* die 2 pagina's naar het model.

**Resultaat:** De hallucinaties verdwenen volledig omdat de aandacht van het model gefocust was op een compact stuk tekst. De API-kosten per samenvatting daalden van €0,45 naar €0,01. Time-outs behoorden tot het verleden. De feature werd het meest gewaardeerde onderdeel van het platform.

> *"Ik dacht vroeger dat mijn werk als PM ophield bij het schrijven van een goede prompt. LaunchStudio leerde me dat het ontwerpen van een AI-product begint bij het ontwerpen van de datastroom. Zij lieten me zien hoe je vectoren en aandachtsmechanismen gebruikt om software te bouwen die betrouwbaar en winstgevend is."*
> — **Julia Evans, Lead Product Manager, LexiCore (Londen)**

**Kosten & Doorlooptijd:** €6.200 (Launch & Grow Pakket met RAG Implementatie Add-on) — productie-klaar en live binnen 10 werkdagen.

---

## Veelgestelde vragen

### Hoe specifiek moet ik zijn bij het schrijven van functionele eisen voor een AI-functie?
U moet specifiek zijn over de *datapijplijn*, niet alleen over de prompt. Schrijf niet: "Gebruik AI om de mail te categoriseren". Schrijf: "Extraheer de tekst, strip HTML-tags om tokens te besparen, stuur het naar een goedkoop model (Claude Haiku) met een strikt JSON-schema en sla de output op in de database." LaunchStudio helpt PM's deze technische specificaties helder te definiëren.

### Waarom verzint een AI soms feiten bij het lezen van lange documenten?
Dit wordt veroorzaakt door "Aandachtsverwatering" (Lost in the Middle). Een Transformer-model verliest zijn focus wanneer het overspoeld wordt met tienduizenden woorden: het onthoudt het begin en eind, maar hallucineert over het midden. LaunchStudio lost dit op via RAG-pipelines die documenten opdelen en alleen relevante tekstpassages doorsturen.

### Wat is het fundamentele verschil tussen trefwoordzoeken en vectorzoeken?
Trefwoordzoeken zoekt naar letterlijke tekstovereenkomsten ("hond" vindt alleen documenten met het woord "hond"). Vectorzoeken zoekt op semantische betekenis ("hond" vindt ook "puppy", "viervoeter" of "Golden Retriever" omdat hun wiskundige coördinaten dicht bij elkaar liggen). LaunchStudio implementeert vectorzoeksystemen voor echte contextuele intelligentie.

### Waarom rekenen AI-providers af per 'Token' en niet per API-aanroep?
Omdat de benodigde GPU-rekenkracht van de Transformer lineair meeschaalt met de hoeveelheid tekst die gelezen en gegenereerd moet worden. Een vraag van 5 woorden vergt nauwelijks rekenkracht; een samenvatting van 50 pagina's vergt gigantisch veel rekenkracht. Tokens meten dit exacte verbruik. LaunchStudio bouwt middleware om dit verbruik drastisch te beperken.

### Moeten we een eigen Vectordatabase hosten om RAG te kunnen gebruiken?
Ja, voor een productiewaardige applicatie volstaan lokale bestanden niet. U heeft een dedicated vectordatabase nodig (zoals Supabase met `pgvector`) om meerdimensionale coördinaten efficiënt op te slaan en te doorzoeken. LaunchStudio richt dit zo in dat relationele data en vectoren veilig in één database worden beheerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe specifiek moet ik zijn bij het schrijven van functionele eisen voor een AI-functie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Specificeer de complete datapijplijn: tekstextractie, token-reductie, modelkeuze, JSON-validatie en databaseopslag. LaunchStudio helpt PM's met deze technische vertaalslag."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verzint een AI soms feiten bij het lezen van lange documenten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wegens Aandachtsverwatering (Lost in the Middle). Transformers verliezen focus bij te veel tekst. RAG-pijplijnen lossen dit op door documenten op te delen in selectieve fragmenten."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het fundamentele verschil tussen trefwoordzoeken en vectorzoeken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Trefwoordzoeken vereist exacte letterlijke matches; vectorzoeken begrijpt semantische betekenis en context door woorden wiskundig op een meerdimensionale kaart te plaatsen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom rekenen AI-providers af per 'Token' en niet per API-aanroep?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat GPU-rekenkracht afhangt van tekstvolume. Tokens meten de exacte verwerkingscapaciteit. LaunchStudio bouwt middleware om tokens en kosten te minimaliseren."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten we een eigen Vectordatabase hosten om RAG te kunnen gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, productiesystemen vereisen een volwaardige vectordatabase zoals PostgreSQL met pgvector. LaunchStudio combineert relationele en vector-data in één veilige database."
      }
    }
  ]
}
</script>
