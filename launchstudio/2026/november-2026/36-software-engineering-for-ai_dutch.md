---
Titel: "Software Engineering for AI: Gids voor Evaluation-Driven Development"
Trefwoorden: software engineering voor AI, AI software engineering, LaunchStudio, Manifera
Koperfase: Beslissing
Doelpersona: VP of Engineering / CTO
---

# Software Engineering for AI: Gids voor Evaluation-Driven Development

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Engineering voor AI: Waarom Traditioneel Agile en TDD Falen",
  "description": "De introductie van niet-deterministische AI-modellen breekt traditionele ontwikkelcycli (SDLC). Een diepgaande gids over Evaluation-Driven Development (EDD) en AI software engineering.",
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
  "datePublished": "2026-12-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/software-engineering-for-ai"
  }
}
</script>

De afgelopen twintig jaar werd software-engineering beheerst door één fundamenteel uitgangspunt: determinisme. Schreef een software-ontwikkelaar een functie die twee getallen optelt, dan was `add(2, 2)` altijd exact gelijk aan `4`. Omdat software voorspelbaar was, bouwde de industrie daar ijzersterke methodieken omheen: Test-Driven Development (TDD), Agile tweewekelijkse sprints, CI/CD-pipelines en binaire pass/fail unit tests.

De integratie van Large Language Models (LLM's) in applicaties heeft dit fundament volledig verbrijzeld. Software engineering voor AI introduceert een chaotische, niet-deterministische variabele in het hart van uw applicatie. Vraagt u een LLM om *"dit contract samen te vatten"*, dan is de uitkomst elke keer net iets anders. Op dinsdag levert het 200 woorden, op woensdag 150. Vandaag formatteert het de tekst in opsommingstekens, morgen in een doorlopende alinea.

Probeert een VP of Engineering een AI-project te managen via klassieke softwaremethoden, dan loopt het team onvermijdelijk vast: unit tests falen willekeurig ("flaky tests") en Agile story points worden onbruikbaar omdat niemand kan voorspellen hoelang het duurt om een prompt "af te stellen" tegen hallucinaties.

Om robuuste enterprise AI-software te bouwen moeten leiders overstappen op een nieuwe ontwikkelcyclus (SDLC), specifiek ontworpen voor niet-deterministische systemen.

## Waarom Traditionele Paradigma's Falen bij AI

### 1. Het Einde van Binaire Unit Tests (TDD-Falen)
Bij klassieke TDD schrijft u een harde controle: `assert(result == "verwachte_tekst")`. Bij AI-engineering is dit onmogelijk. Als uw AI een e-mail genereert, kunt u niet controleren op een exacte letterlijke tekst. Teams proberen dit op te lossen met regex (trefwoorden zoeken), maar dat is kwetsbaar: een uitstekende creatieve mail die toevallig een synoniem gebruikt faalt onterecht, terwijl een gehallucineerde slechte mail per ongeluk slaagt. De CI/CD-pipeline loopt vast op onbetrouwbare tests.

### 2. De Onvoorspelbaarheid van Schattingen (Agile-Falen)
Bij Agile schat een ontwikkelaar een ticket op basis van eerdere CRUD-functies. Bij AI kost het bouwen van de functie (de API-call naar OpenAI) 10 minuten, maar het oplossen van zeldzame randgevallen (edge cases) en hallucinaties kan 3 dagen of 3 weken duren. De sprint-planning raakt volledig ontwricht.

### 3. De Stille Kwaliteitsdegradatie (Monitoring-Falen)
Klassieke software faalt luidruchtig met een `500 Server Error` en een PagerDuty-alarm. AI-software faalt stil. Als OpenAI een model op de achtergrond update, kan het model plotseling een ander deel van uw prompt anders interpreteren. De server geeft gewoon een `200 OK` terug, maar de kwaliteit van de antwoorden daalt langzaam, waardoor gebruikers weglopen zonder dat traditionele monitoring aanslaat.

## Het Nieuwe Paradigma: Evaluation-Driven Development (EDD)

Om deze crises op te lossen hebben toonaangevende AI-teams TDD vervangen door **Evaluation-Driven Development (EDD)**.

Bij EDD test men niet op een binaire waar/niet-waar uitkomst, maar gebruikt men secundaire taalmodellen als "Rechter" (LLM-as-a-Judge) om de gegenereerde tekst statistisch te beoordelen aan de hand van een rubric.

### Fase 1: De Gouden Dataset
In plaats van statische tests bouwt men een "Gouden Dataset": een database met 100 tot 500 representatieve invoergevallen (prompts, uploads, complexe uitzonderingen) gekoppeld aan door experts goedgekeurde criteria.

### Fase 2: De LLM-as-a-Judge Pijplijn
Wijzigt een ontwikkelaar een prompt of zoektabel, dan test de CI/CD-pipeline de nieuwe code automatisch tegen de volledige Gouden Dataset. Een secundair, strikt geprompt model beoordeelt de antwoorden op accuratesse (1-10), afwezigheid van hallucinaties en merkidentiteit.

### Fase 3: Statistische Deployment-Vangrails
Een update mag uitsluitend naar productie als de Rechter-scores statistisch significant verbeteren (bijv. *"accuratesse gestegen van 8.2 naar 8.7 en hallucinaties onder 1%"*). Daalt de score op een ander domein, dan wordt de merge automatisch geblokkeerd.

## Hoe LaunchStudio AI-Software Engineering Inricht

Het bouwen van een EDD-pijplijn vereist gespecialiseerde MLOps-infrastructuur.

[LaunchStudio](https://launchstudio.eu/en/), gedragen door de enterprise-engineers van [Manifera](https://www.manifera.com/) onder leiding van Herre Roelevink in Amsterdam en Ho Chi Minhstad, vervangt subjectief prompt-knutselen door wiskundig onderbouwde AI-engineering:
1. **Evaluatie-Frameworks:** Integratie van tools zoals LangSmith, Ragas of TruLens rechtstreeks in GitHub Actions.
2. **Deterministische Parsers:** Afdwingen van strikte schema-validatie (Zod, OpenAI Structured Outputs) zodat niet-deterministische AI altijd voorspelbare JSON levert.
3. **Shadow Deployments:** Nieuwe prompts draaien eerst onzichtbaar mee in productie om statistische zekerheid op te bouwen vóór de definitieve overschakeling.

## Echt voorbeeld

### Een AI-Native Oprichter in de Praktijk: De Fintech-CTO Die Gevangen Zat in Prompt-Problemen

Marcus is CTO van een fintech-startup in Londen die factuurverwerking automatiseert. Met Bolt bouwden ze een AI-engine die factuur-PDF's inlas en posten koppelde aan interne grootboekrekeningen.

De eerste twee maanden liep alles uitstekend. Toen besloot het team de prompt aan te passen om een specifiek Frans btw-probleem op te lossen.

Een junior developer paste de prompt aan, testte drie Franse facturen lokaal en pushte de code naar productie.

De volgende ochtend werkten de Franse facturen perfect, maar bleek de promptwijziging desastreuze gevolgen te hebben voor Duitse facturen: de AI begon leveranciersnamen te hallucineren en adressen te verwisselen. Omdat de oude unit tests enkel controleerden op een `200 OK` respons, had de CI/CD-pipeline de update goedgekeurd.

Pas vier dagen later ontdekten klanten duizenden foutieve boekingen. Marcus' ontwikkelaars durfden de prompt niet meer aan te raken; de verdere productontwikkeling viel stil.

Marcus schakelde LaunchStudio in. In 15 werkdagen verving het Manifera-team de traditionele tests door een Evaluation-Driven Development (EDD) raamwerk:
- Er werd een Gouden Dataset van 400 historische facturen uit alle landen en formaten samengesteld.
- Een LLM-as-a-Judge evaluatiescript via LangSmith werd ingericht.
- Paste een developer een prompt aan voor Franse btw, dan testte het systeem direct alle 400 facturen. Steeg de Franse score maar daalde de Duitse score met 1%, dan blokkeerde de pipeline direct de merge en toonde exact welke facturen faalden.

**Resultaat:** De ontwikkelsnelheid herstelde direct. De hallucinaties in productie daalden naar 0,1% en het platform verwerkt inmiddels moeiteloos 50.000 facturen per maand voor grote Europese ondernemingen.

> *"We probeerden een neuraal netwerk te beheren met dezelfde tools als een simpele database. Dat was een recept voor een ramp. LaunchStudio heeft niet alleen onze code gerepareerd, maar ons hele engineeringteam getraind in hoe je software bouwt in het AI-tijdperk. Hun evaluatiepijplijn is ons meest waardevolle bezit geworden."*
> — **Marcus Sterling, CTO, LedgerAI (Londen)**

**Kosten & Doorlooptijd:** €12.500 (Launch & Grow Pakket met Enterprise MLOps & EDD Add-on) — productie-klaar en live binnen 15 werkdagen.

---

## Veelgestelde vragen

### Hoe schatten we planningen in als prompt engineering zo onvoorspelbaar is?
Ontkoppel deterministisch werk van niet-deterministisch werk. Schat de API-koppelingen, database-inrichting en UI via standaard Agile story points. Hanteer voor prompt-tuning Timeboxing (bijv. *"we besteden exact 3 dagen aan het tunen tegen de Gouden Dataset; de beste versie op vrijdag lanceren we"*).

### Kunnen we traditionele testframeworks zoals Jest of PyTest gebruiken voor AI?
Ja, maar uitsluitend voor de deterministische infrastructuur (databasekoppelingen, authenticatie, API-routes). Gebruik Jest nooit om de tekstuele inhoud van het AI-antwoord te beoordelen; gebruik daarvoor een EDD-script met een Rechter-model.

### Wat is het grootste gevaar van stille kwaliteitsdegradatie bij AI?
Dat de externe modelleverancier (zoals OpenAI) een update doorvoert waardoor het redeneerpatroon subtiel verandert. Zonder code-wijzigingen aan uw kant begint de prompt plotseling randgevallen te missen. LaunchStudio voorkomt dit door dagelijks geautomatiseerd uw Gouden Dataset te testen en u direct te alarmeren bij score-dalingen.

### Wordt het draaien van een Rechter-AI in CI/CD niet ontzettend duur?
Niet als het slim wordt ingericht. LaunchStudio gebruikt snelle en goedkope modellen (zoals GPT-4o-mini) voor 90% van de routinetests (JSON-controle, trefwoordchecks) en reserveert zware modellen uitsluitend voor complexe semantische beoordelingen, waardoor testkosten minimaal blijven.

### Hoe zorgen we dat ontwikkelaars de EDD-pipeline niet kunnen omzeilen?
Door branch protection rules in GitHub af te dwingen. Een pull request kan fysiek niet worden gemerged tenzij de geautomatiseerde evaluatie-actie een voldoende score oplevert conform uw vooraf ingestelde statistische drempelwaarde.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe schatten we planningen in als prompt engineering zo onvoorspelbaar is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ontkoppel deterministisch werk (UI, DB) van stochastisch werk. Gebruik Timeboxing voor prompt-tuning: stel een vaste tijd in en deploy de best scorende variant."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen we traditionele testframeworks zoals Jest of PyTest gebruiken voor AI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, voor infrastructuur en auth, maar niet voor tekstoutput van LLM's. Gebruik voor semantische beoordeling een EDD-pijplijn met een Rechter-model."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het grootste gevaar van stille kwaliteitsdegradatie bij AI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stille updates bij de AI-provider die redeneerpatronen veranderen zonder serverfout. LaunchStudio test dagelijks een Gouden Dataset om score-dalingen direct te signaleren."
      }
    },
    {
      "@type": "Question",
      "name": "Wordt het draaien van een Rechter-AI in CI/CD niet ontzettend duur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, door goedkope modellen (GPT-4o-mini) in te zetten voor routinematige checks en zware modellen alleen voor complexe semantiek te reserveren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe zorgen we dat ontwikkelaars de EDD-pipeline niet kunnen omzeilen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via repository branch protection in GitHub die merges fysiek blokkeert zolang de geautomatiseerde evaluatietest niet aan de kwaliteitsdrempel voldoet."
      }
    }
  ]
}
</script>
