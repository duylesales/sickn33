---
Titel: "AI-functies: Modeluitvoer Beoordelen Voordat Klanten Dat Doen"
Trefwoorden: AI-evaluatie, LLM-evals, kwaliteit van modeluitvoer, controles op hallucinaties, gestructureerde uitvoer, regressietests voor prompts, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-functies: Modeluitvoer Beoordelen Voordat Klanten Dat Doen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-functies: Modeluitvoer Beoordelen Voordat Klanten Dat Doen",
  "description": "Een AI-functie die in de demo werkte, kan stilletjes slechter worden door een nieuw model, een gewijzigde prompt of andere invoer. Hoe u een evaluatieset bouwt, bepaalt wat goed betekent, elke wijziging test vóór de release, uitvoer in productie controleert, en leert van wat klanten corrigeren.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-features-evaluating-model-output-before-customers-do" }
}
</script>

De meeste AI-functies in AI-gebouwde producten zijn op dezelfde manier getest: de oprichter probeerde een paar voorbeelden, de uitvoer zag er goed uit, en de functie ging live. Een samenvatting van een overleg, een conceptantwoord aan een klant, een classificatie van binnenkomende documenten, een voorgesteld plan — elk werkte overtuigend op de voorbeelden die het te zien kreeg.

Wat niemand testte, is wat er daarna gebeurt. De modelaanbieder brengt een nieuwe versie uit en de oude wordt uitgefaseerd. Een AI-assistent "verbetert" de prompt tijdens een refactor. Klanten beginnen langere documenten in te voeren, andere formaten, een andere taal. De uitvoer verandert — meestal niet dramatisch, maar op manieren die ertoe doen: een detail weggelaten, een feit verzonnen, een toon die niet meer past. En in de meeste producten merkt niets het op, totdat een klant het doet.

Traditionele software heeft tests die falen wanneer gedrag verandert. AI-functies hebben het equivalent nodig, aangepast aan uitvoer die nooit twee keer precies hetzelfde is. Dit artikel behandelt hoe u bepaalt wat goede uitvoer betekent voor uw functie, een evaluatieset bouwt, die beoordeelt, wijzigingen ervan afhankelijk maakt, uitvoer in productie controleert, en gebruikt wat klanten corrigeren om de functie te verbeteren.

## Waarom AI-functies Afdrijven

Vier dingen veranderen het gedrag van een AI-functie zonder dat iemand de functie zelf aanraakt.

**Het model verandert.** Aanbieders brengen nieuwe versies uit, faseren oude uit, en passen soms een model aan achter dezelfde naam. Een goedkoper of sneller model dat "even goed is op benchmarks", kan slechter zijn in het ene ding dat uw functie nodig heeft.

**De prompt verandert.** Prompts staan in code, en code wordt bewerkt — steeds vaker door AI-assistenten die opruimen, inkorten en herformuleren. Een zin die werd verwijderd omdat hij overbodig leek, was vaak de instructie die een specifieke fout voorkwam.

**De invoer verandert.** Klanten gebruiken de functie op manieren die niemand testte: langere transcripten, gescande documenten, gemengd Nederlands en Engels, ongebruikelijke vaktermen. De kwaliteit van de uitvoer op echte invoer kan sterk verschillen van die op de voorbeelden uit de ontwikkeling.

**De context verandert.** Retrieval levert andere documenten op naarmate de kennisbank groeit, een sjabloon verandert, een veld dat vroeger was ingevuld, is nu leeg.

Geen van deze levert een foutmelding op. Allemaal kunnen ze slechtere uitvoer opleveren. De enige verdediging is de kwaliteit van de uitvoer systematisch en herhaaldelijk te meten.

## Bepaal Wat Goed Betekent voor Uw Functie

"Is de uitvoer goed?" kan niet worden getest. Specifieke eigenschappen wel. Schrijf, voordat u iets bouwt, op wat goede uitvoer voor deze functie betekent, in termen die u zou kunnen controleren.

Voor een samenvatting van een intakegesprek kan dat zijn:

- Elk risico of elke zorg over veiligheid die in het gesprek wordt genoemd, staat in de samenvatting.
- Er verschijnt geen persoon, datum of feit dat niet in het gesprek voorkomt.
- De samenvatting is korter dan 300 woorden en gebruikt de sectiekoppen van de organisatie.
- Ze is in het Nederlands geschreven, in de formele aanspreekvorm die de organisatie gebruikt.

Voor een classificatie van binnenkomende documenten: de juiste categorie, en een betrouwbaarheid waaronder een mens beslist. Voor een conceptantwoord aan een klant: de juiste feiten uit de order, geen toezeggingen die het bedrijf niet doet, de juiste toon.

Deze criteria zijn de specificatie van de functie. Ze zijn ook bijna altijd veeleisender dan waar de oorspronkelijke demo tegen werd gecontroleerd.

## Bouw een Evaluatieset

Een evaluatieset is een verzameling realistische invoer, elk met de informatie die nodig is om de uitvoer te beoordelen. Het is het equivalent van een testsuite.

**Begin met vijftig tot honderdvijftig voorbeelden.** Genoeg om de variatie van echt gebruik te dekken; weinig genoeg om met de hand na te lopen.

**Gebruik echte invoer, geanonimiseerd.** Synthetische voorbeelden die de oprichter schreef, testen wat de oprichter zich voorstelde. Geanonimiseerde voorbeelden uit echt gebruik — met namen, adressen en herleidbare details vervangen — testen wat klanten werkelijk doen. Spreek dit af met klanten als de data van hen is, en verwerk het onder uw verwerkersovereenkomst.

**Dek de moeilijke gevallen bewust af.** Lange invoer, korte invoer, invoer van slechte kwaliteit, randgevallen, voorbeelden waarin het juiste antwoord "dit kan ik niet bepalen" is, voorbeelden waarop een vorige versie faalde. Elke foutmelding van een klant wordt een nieuw voorbeeld.

**Leg per voorbeeld de verwachte eigenschappen vast**, niet één verwachte uitvoer. Voor een samenvatting: de feiten die erin moeten staan, de feiten die er niet in mogen staan. Voor een classificatie: het juiste label. Voor extractie: de juiste velden.

```json
{
  "id": "intake-042",
  "input": "transcripts/intake-042.txt",
  "must_include": ["zorg over alcoholgebruik vader", "schoolverzuim sinds oktober"],
  "must_not_include_names_except": ["Sanne", "moeder", "vader", "mentor"],
  "max_words": 300,
  "language": "nl"
}
```

Bewaar de set in de repository, geef haar versies, en behandel wijzigingen eraan met dezelfde zorg als wijzigingen aan tests.

## Beoordeel Uitvoer op Drie Manieren

Verschillende eigenschappen vragen verschillende controles. Gebruik voor elke eigenschap de goedkoopste controle die betrouwbaar is.

**Deterministische controles** — code die een eigenschap exact controleert. Is de uitvoer geldige JSON die aan het schema voldoet? Is ze korter dan de woordlimiet? Is ze Nederlands? Komt elke naam in de uitvoer voor in de invoer? Komt de classificatie overeen met het label? Deze zijn snel, goedkoop, en moeten zo veel mogelijk dekken.

**Beoordeling door een model** — een tweede model beoordeelt een eigenschap die code niet makkelijk kan controleren: "Noemt deze samenvatting elke zorg die hieronder staat?" of "Belooft dit antwoord iets wat niet in het beleid staat?" Beoordelende modellen zijn nuttig en onvolmaakt. Geef ze een smalle, specifieke vraag in plaats van "is dit goed?", vraag om een ja of nee met een geciteerde onderbouwing, en valideer de beoordelaar zelf op voorbeelden waarvan u het antwoord kent voordat u hem vertrouwt.

**Menselijke review** — voor een steekproef van de uitvoer, vooral bij de introductie van een nieuw model of een nieuwe prompt, en voor eigenschappen die geen geautomatiseerde controle goed vangt, zoals of een samenvatting echt nuttig zou zijn voor de persoon die haar leest. Houd het gestructureerd: elke keer dezelfde beoordelingsmaatstaf, met scores, zodat resultaten kunnen worden vergeleken.

Het resultaat van een evaluatierun is een set getallen per eigenschap — "risico-uitspraken opgenomen: 97%; verzonnen namen: 0 van 120; binnen woordlimiet: 100%" — geen indruk.

## Maak Elke Wijziging Afhankelijk van de Evaluatie

Zodra de evaluatieset bestaat, wordt ze de releasepoort voor alles wat de AI-functie raakt.

Een wijziging aan de prompt, het model, de temperatuur, de retrieval, de voorbewerking van de invoer of het verwerken van de uitvoer draait de evaluatie en vergelijkt de resultaten met de huidige versie. Gaat een kritieke eigenschap achteruit, dan gaat de wijziging niet live.

```ts
// evaluatierunner (vereenvoudigd)
const results = await Promise.all(evalSet.map(async (ex) => {
  const output = await generateSummary(await load(ex.input), { model: CANDIDATE_MODEL });
  return {
    id: ex.id,
    schemaValid: SummarySchema.safeParse(output).success,
    mustInclude: await judgeIncludes(output.text, ex.must_include),   // beoordeeld door model
    inventedNames: findNames(output.text).filter(n => !ex.must_not_include_names_except.includes(n)),
    words: wordCount(output.text),
  };
}));
assert(rate(results, r => r.mustInclude.allPresent) >= 0.95, 'risico-uitspraken achteruitgegaan');
assert(results.every(r => r.inventedNames.length === 0), 'verzonnen namen');
```

Draai haar in CI wanneer prompts of AI-code veranderen, en met de hand vóór het wisselen van model. Zet modelversies expliciet vast in de configuratie in plaats van aliassen te gebruiken die de aanbieder kan verplaatsen, zodat een modelwissel een bewuste commit is die door de poort gaat.

Dit is wat de aankondiging van een aanbieder dat een model wordt uitgefaseerd, verandert van een noodgeval in een taak: draai de evaluatie op de kandidaat-vervangers, vergelijk, kies.

## Modellen en Prompts Eerlijk Vergelijken

Het meeste evaluatiewerk gebeurt op een beslismoment: een goedkoper model, een nieuwe aanbieder, een herschreven prompt. Ze goed vergelijken voorkomt twee tegengestelde fouten — overstappen op iets slechters omdat het er op vijf voorbeelden goed uitzag, en weigeren over te stappen op iets beters omdat niemand het mat.

**Draai elke kandidaat op dezelfde evaluatieset, met dezelfde instellingen.** Zet de temperatuur, de context en de nabewerking vast, zodat de enige variabele de vergeleken variabele is.

**Draai meer dan één keer.** Modeluitvoer varieert per run. Twee of drie runs per kandidaat laten zien of een verschil van twee punten echt is of ruis. Behandel bij kleine evaluatiesets kleine verschillen als gelijkspel en beslis op kosten, latentie of andere eigenschappen.

**Vergelijk per eigenschap, niet op één score.** Een kandidaat die gemiddeld beter is maar slechter op de ene kritieke eigenschap — weggelaten risico's, verkeerde bedragen, verzonnen feiten — is slechter. Beslis vooraf welke eigenschappen kritiek zijn en behandel elke achteruitgang daarop als uitsluitend.

**Vergelijk de kosten per acceptabele uitvoer.** Een goedkoper model dat vaker faalt bij validatie, en daardoor opnieuw probeert of terugvalt op een mens, kan per bruikbaar resultaat meer kosten dan het dure model. Deel de totale kosten door het aantal uitvoeringen dat alle kritieke controles doorstaat.

**Bevestig geleidelijk in productie.** Nadat een kandidaat de evaluatie heeft doorstaan, released u hem achter een feature flag aan een klein deel van de klanten, zoals het artikel over feature flags in deze reeks beschrijft, en vergelijkt u bewerkingspercentages en validatiefouten tussen de twee groepen voordat u iedereen overzet. De evaluatieset vertelt u wat u verwachtte; productie vertelt u wat u niet verwachtte.

Leg elke vergelijking vast — kandidaten, resultaten, beslissing en reden — in het beslissingenlogboek. De volgende keer dat een aanbieder een nieuw model aankondigt, is de vorige vergelijking het vertrekpunt in plaats van een vergeten gesprek.

## Beperk de Uitvoer

Veel kwaliteitsproblemen worden goedkoper voorkomen door te beperken wat het model kan opleveren dan door het achteraf te controleren.

**Gebruik gestructureerde uitvoer.** Vraag het model JSON terug te geven die aan een schema voldoet — de meeste aanbieders ondersteunen dat direct — en valideer die met een schemabibliotheek voordat u haar gebruikt. Een samenvatting met verplichte velden zoals `concerns`, `agreements` en `follow_up` kan de sectie met zorgen niet stilletjes weglaten; ze kan haar alleen leeg laten, en dat is te controleren.

**Vraag om onderbouwing.** Vraag bij extractie en samenvatting om een kort citaat uit de invoer dat elke belangrijke uitspraak onderbouwt. Uitspraken zonder onderbouwing kunnen worden gemarkeerd of weggelaten, en verzonnen feiten worden veel zeldzamer.

**Sta "onbekend" toe.** Een model dat elk veld moet vullen, verzint waarden. Maak onzekerheid een expliciet, geldig antwoord.

**Houd de taak smal.** Eén prompt die tegelijk samenvat, classificeert, extraheert en een concept schrijft, is moeilijker te beoordelen en faalt op meer manieren dan vier kleine prompts, elk met een eigen evaluatie.

## Controleer Uitvoer in Productie

De evaluatieset beschermt tegen achteruitgang die u voorzag. Controles in productie vangen de rest.

**Valideer elke uitvoer** met de deterministische controles voordat ze wordt getoond of opgeslagen: schema, lengte, taal, namen die niet in de invoer voorkomen. Faalt een controle, probeer het dan één keer opnieuw en val daarna terug — toon een duidelijke melding, bied de handmatige route aan — in plaats van kapotte uitvoer te tonen.

**Neem steekproeven voor review.** Een klein percentage van de uitvoer, willekeurig gekozen en geanonimiseerd, wekelijks beoordeeld tegen de maatstaf. Het vangt afdrijven op echte invoer die de evaluatieset nog niet bevat, en elke interessante fout wordt aan de set toegevoegd.

**Meet wat gebruikers met de uitvoer doen.** Duim omhoog en omlaag is nuttig maar zeldzaam. Informatiever is wat er daarna gebeurt: werd de suggestie ongewijzigd geaccepteerd, flink bewerkt, of weggegooid? Het aandeel uitvoer dat wordt bewerkt, en hoeveel, is een doorlopend kwaliteitssignaal dat niets kost om te verzamelen. Een plotselinge stijging na een release is een achteruitgang.

**Behandel kosten en latentie als kwaliteitseigenschappen.** Een wijziging die de uitvoer iets beter en drie keer trager of duurder maakt, kan de verkeerde wijziging zijn. Volg tokens en reactietijd per verzoek naast de kwaliteit, zoals de artikelen over AI-kosten in deze reeks beschrijven.

## Menselijke Review Waar Veel op het Spel Staat

Voor sommige functies is het juiste antwoord geen betere evaluatie maar een mens in de lus. Uitvoer die iemands zorg, geld, juridische positie of werk raakt, moet een concept zijn dat een persoon beoordeelt en bevestigt, geen actie die het systeem uitvoert.

Ontwerp de review zo dat ze echt is in plaats van wegklikken: toon de onderbouwing bij elke uitspraak, markeer waar het model onzeker over was, en maak bewerken makkelijk. Leg vast wie de uitvoer bevestigde. Het artikel over de EU AI Act in deze reeks beschrijft wanneer dit een verplichting wordt; voor veel B2B-functies is het gewoon wat klanten verwachten.

## Loggen Zonder een Privacyprobleem te Maken

AI-functies beoordelen en debuggen vraagt om inzicht in invoer en uitvoer. De invoer bevat vaak precies de persoonsgegevens die klanten u toevertrouwen.

Log bewust. Bewaar prompts en uitvoer alleen zo lang als nodig — dertig dagen is gebruikelijk — met beperkte toegang en elke toegang vastgelegd. Verwijder waar mogelijk identificatoren vóór het loggen. Sluit de gevoeligste functies volledig uit van logging en vertrouw in plaats daarvan op de evaluatieset en de steekproefreview. Leg voor elk verzoek het model, de promptversie en de instellingen vast, zodat een klacht kan worden herleid tot de configuratie die haar veroorzaakte. Voeg de logging toe aan uw verwerkingsregister en bewaarregister, zoals de AVG-artikelen in deze reeks beschrijven — en controleer dat de gegevensverwerking van uw modelaanbieder overeenkomt met wat u uw klanten vertelde.

## Kwaliteit in het Nederlands

De meeste modellen zijn het sterkst in het Engels. Een functie die in het Engels goed werkt, kan in het Nederlands merkbaar zwakker zijn: onnatuurlijke formuleringen, anglicismen, gemengde formele en informele aanspreekvorm, onjuiste vaktermen.

Beoordeel in de taal die uw klanten gebruiken. Neem eigenschappen voor taalkwaliteit op in de maatstaf — de juiste aanspreekvorm, de terminologie van de organisatie, geen Engelse fragmenten — en laat een moedertaalspreker een steekproef beoordelen bij het evalueren van een nieuw model. Overweeg het model in het Nederlands te instrueren in plaats van in het Engels wanneer de uitvoer Nederlands moet zijn; test beide, omdat het resultaat per model verschilt.

## Dit Inrichten

Voor een product met één of meer AI-functies is dit doorgaans vier tot zes dagen: de definitie van goede uitvoer per functie opgeschreven als controleerbare eigenschappen, een evaluatieset van vijftig tot honderdvijftig geanonimiseerde echte voorbeelden met moeilijke gevallen en verwachte eigenschappen, deterministische controles voor alles wat code kan controleren, smalle en gevalideerde beoordelingen door een model voor de rest, een gestructureerde maatstaf voor menselijke review, een evaluatierunner die wijzigingen aan prompts, modellen en de pijplijn in CI tegenhoudt, vastgezette modelversies, eerlijke vergelijkingen van kandidaten per eigenschap en kosten per acceptabele uitvoer, gestructureerde uitvoer met schema's, onderbouwing en expliciete onzekerheid, validatie in productie met nieuwe poging en terugval, een wekelijkse steekproefreview, het bijhouden van acceptatie en bewerkingen, kosten en latentie gevolgd naast kwaliteit, menselijke bevestiging voor uitvoer met veel impact, privacybewuste logging met bewaartermijn en redactie, en taalkwaliteit in het Nederlands in de maatstaf.

LaunchStudio richt dit in voor AI-functies waarop klanten zijn gaan vertrouwen. Daarachter staat Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons hoe u zou weten of uw AI-functie slechter werd](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Een Goedkoper Model en de Zorgen Die Het Wegliet

Linda Smits bouwde Intakeverslag in Lovable: AI-samenvattingen van intakegesprekken voor sociale teams, gebruikt door wijkteams in 19 gemeenten. Een medewerker neemt het gesprek op of uploadt het, het product maakt een concept van een gestructureerde samenvatting, en de medewerker bewerkt en bevestigt die.

Om kosten te verlagen werd het model met één configuratieregel overgezet op een nieuwere, goedkopere versie. In dezelfde release kortte een AI-assistent die de code opruimde de prompt in, waarbij een alinea verdween die het model opdroeg altijd elke uitspraak over risico of veiligheid op te nemen.

Drie weken later merkte een teamleider op dat een samenvatting de uitspraak van een kind over geweld thuis wegliet, die duidelijk in de opname stond. Een controle van recente samenvattingen vond hetzelfde patroon in andere, en twee samenvattingen die een broer of zus noemden die niet bestond. De medewerkers hadden samenvattingen bewerkt, maar onder tijdsdruk, en met vertrouwen in het concept.

Vijf werkdagen: een evaluatieset van 120 geanonimiseerde intakegesprekken, samen met twee teamleiders opgebouwd, elk voorzien van de risico-uitspraken die erin moeten staan en de personen die bestaan; deterministische controles op schema, lengte, taal en namen die niet in het transcript voorkomen; een beoordeling door een model voor elke vereiste risico-uitspraak, vóór gebruik gevalideerd tegen de annotaties; een poort in CI die de evaluatie draait bij elke wijziging aan prompts, modellen of de samenvattingspijplijn, met vastgezette modelversies; gestructureerde uitvoer met een verplicht veld `risk_indicators`, elk item met een onderbouwend citaat uit het transcript; de weggelaten promptalinea teruggezet en gedocumenteerd met de reden dat ze bestaat; validatie in productie die samenvattingen blokkeert met namen die niet in het transcript staan; risico-indicatoren gemarkeerd zodat de medewerker ze expliciet bevestigt; het bijhouden van bewerkingen per samenvatting; en logging beperkt tot 30 dagen met redactie, gedocumenteerd voor de privacyfunctionarissen van de gemeenten.

**Resultaat:** op de evaluatieset liet het goedkopere model met de ingekorte prompt in 14% van de gesprekken minstens één risico-uitspraak weg; de teruggezette prompt met gestructureerde uitvoer bracht dit op het oorspronkelijke model onder 2%, en de poort wees later twee kandidaat-modellen af die achteruitgingen. Verzonnen namen gingen in productie naar nul. De privacyfunctionarissen van de gemeenten accepteerden de documentatie, en het aandeel samenvattingen dat door medewerkers flink werd bewerkt, daalde met ongeveer een derde.

> *"We veranderden één regel om geld te besparen en een opruimactie haalde één alinea weg. Er ging niets fout. De samenvattingen begonnen gewoon de dingen weg te laten die er het meest toe deden."*
> — **Linda Smits, Oprichter, Intakeverslag (Utrecht)**

**Kosten & Doorlooptijd:** €5.200 (geannoteerde evaluatieset van 120 gesprekken, deterministische controles en beoordelingen door een model, evaluatiepoort in CI met vastgezette modellen, gestructureerde uitvoer met onderbouwing, validatie in productie, expliciete bevestiging van risico's, bijhouden van bewerkingen, privacybewuste logging en documentatie) — afgerond in 5 werkdagen.

## Veelgestelde vragen

### Waarom wordt een AI-functie slechter zonder dat iemand haar verandert?

Omdat het model, de prompt, de invoer of de context verandert. Nieuwe modelversies, bewerkte prompts, andere klantdata en groeiende kennisbanken veranderen allemaal de uitvoer zonder foutmeldingen op te leveren.

### Wat is een evaluatieset?

Een verzameling realistische, geanonimiseerde invoer, elk met de eigenschappen die goede uitvoer moet hebben. Ze werkt als een testsuite voor AI-uitvoer en wordt gedraaid wanneer de functie verandert.

### Kan ik een model de uitvoer van een ander model laten beoordelen?

Ja, voor smalle en specifieke vragen, met een onderbouwing, nadat de beoordelaar is gevalideerd op voorbeelden met bekende antwoorden. Gebruik deterministische codecontroles overal waar een eigenschap exact te controleren is.

### Hoe weet ik dat de functie in productie nog goed is?

Valideer elke uitvoer automatisch, beoordeel wekelijks een willekeurige steekproef, en houd bij hoe vaak gebruikers de uitvoer accepteren, bewerken of weggooien. Een stijging van zware bewerkingen na een release wijst op achteruitgang.

### Moet AI-uitvoer door een persoon worden beoordeeld?

Voor alles wat iemands zorg, geld, juridische positie of werk raakt, ja — als echte review met de onderbouwing zichtbaar, niet als bevestiging met één klik.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom gaan AI-functies na verloop van tijd achteruit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Modelversies, prompts, invoer van klanten en opgehaalde context veranderen, waardoor de uitvoer verandert zonder foutmeldingen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een AI-evaluatieset?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geanonimiseerde realistische invoer, voorzien van de eigenschappen die goede uitvoer moet hebben, gedraaid als testsuite bij elke wijziging."
      }
    },
    {
      "@type": "Question",
      "name": "Is LLM-as-judge betrouwbaar voor evaluatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor smalle, specifieke vragen met onderbouwing en na validatie van de beoordelaar; geef waar mogelijk de voorkeur aan deterministische controles."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe wordt de kwaliteit van AI-uitvoer in productie bewaakt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Valideer elke uitvoer, beoordeel wekelijks een willekeurige steekproef, en houd bij hoe vaak gebruikers resultaten accepteren, bewerken of weggooien."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet een mens AI-uitvoer beoordelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanneer uitvoer zorg, geld, juridische positie of werk raakt — met zichtbare onderbouwing en echte bewerking, niet met één klik bevestigen."
      }
    }
  ]
}
</script>
