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
  "headline": "Software Engineering voor AI: Waarom Traditioneel Agile en TDD Vastlopen",
  "description": "De introductie van niet-deterministische AI-modellen ontregelt traditionele Software Development Life Cycles (SDLC). Een diepgaande analyse van Evaluation-Driven Development (EDD).",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/software-engineering-for-ai"
  }
}
</script>

De afgelopen twee decennia werd software engineering beheerst door één centrale aanname: determinisme. Als een software-engineer een functie schrijft die twee getallen optelt, zal `add(2, 2)` altijd exact gelijk zijn aan `4`. Omdat code deterministisch was, bouwde de industrie uiterst robuuste methodieken rondom deze aanname: Test-Driven Development (TDD), twee-wekelijkse Agile-sprints, CI/CD-pipelines en binaire geslaagd/mislukt-unit tests.

De integratie van Large Language Models (LLMs) in de applicatiestack heeft deze aanname definitief doorbroken. Software engineering voor AI introduceert een chaotische, niet-deterministische variabele in het hart van uw applicatie. Als u een LLM vraagt "vat dit contract samen", zal de output elke afzonderlijke keer licht afwijken. Het model kan op dinsdag 200 woorden teruggeven en op woensdag 150 woorden. Het kan de output vandaag opmaken als opsommingstekens en morgen als een dichte alinea.

Wanneer een VP of Engineering probeert een AI-project te beheren volgens traditionele software engineering-paradigma's, loopt het project onvermijdelijk vast. Unit tests falen willekeurig (flaky tests). Agile-schattingen worden onmogelijk omdat niet kan worden voorspeld hoelang het duurt om de prompt zodanig te "tunen" dat het model stopt met hallucineren.

Om enterprise-grade AI-software te bouwen, moeten engineeringleiders een fundamenteel nieuwe Software Development Life Cycle (SDLC) omarmen die specifiek is ontworpen voor stochastische (willekeurig bepaalde) systemen.

## Het Uiteenvallen van Traditionele Paradigma's in AI

Voordat we de oplossing implementeren, moeten we nauwkeurig analyseren waarom traditionele methodologieën voor software engineering bezwijken wanneer ze worden toegepast op AI.

### 1. De Dood van Binaire Unit Testing (TDD-Mislukking)
In traditioneel TDD schrijft u een bewering: `assert(resultaat == "verwachte_string")`. In AI-engineering is dit onmogelijk. Als uw AI een marketing-e-mail genereert, kunt u geen exacte string-overeenkomst afdwingen. Engineeringteams proberen dit op te lossen met regex (controleren of specifieke trefwoorden aanwezig zijn), maar dit is uiterst kwetsbaar. Een creatieve, uitstekende AI-e-mail bevat wellicht niet exact het trefwoord waar de regex op zoekt, wat leidt tot een fout-negatieve testuitslag. Omgekeerd kan een slechte, gehallucineerde e-mail per ongeluk wel het trefwoord bevatten, wat leidt tot een fout-positieve goedkeuring. Traditionele CI/CD-pipelines storten in wanneer tests onbetrouwbaar worden.

### 2. De Onmogelijkheid van Schatten (Agile-Mislukking)
In Agile schat een engineer een ticket (bijv. "3 Story Points") op basis van eerdere ervaring met het bouwen van soortgelijke CRUD-functies (Create, Read, Update, Delete). Bij AI kost het bouwen van de initiële functie (de API-call naar OpenAI) 10 minuten. Het zorgen dat de functie *stopt met hallucineren bij randgevallen* kan echter 3 dagen duren, of 3 weken. De verdeling van de werklast verschuift zwaar naar prompt-tuning en het afvangen van randgevallen, waardoor het bijhouden van de sprint-velocity vrijwel nutteloos wordt.

### 3. De Stille Degradatie (Monitoring-Mislukking)
Traditionele software faalt luidruchtig. Het genereert een `NullReferenceException` of een `500 Server Error`, wat direct een PagerDuty-incidentmelding activeert. AI-software faalt in stilte. Als het OpenAI-model wordt bijgewerkt (bijv. van `gpt-4-0613` naar een nieuwere versie), kan het model plotseling besluiten een ander deel van uw systeem-prompt te prioriteren. De code crasht niet. De API geeft nog steeds een `200 OK` terug. De kwaliteit van de gegenereerde tekst degradeert echter langzaam, wat leidt tot ergernis bij gebruikers en toenemend verloop, zonder dat er ooit een traditionele Datadog- of New Relic-melding wordt geactiveerd.

## Het Nieuwe Paradigma: Evaluation-Driven Development (EDD)

Om deze architectonische crises op te lossen, hebben vooraanstaande AI-engineeringteams TDD losgelaten ten gunste van Evaluation-Driven Development (EDD).

In EDD test u niet op een exacte output. In plaats daarvan gebruikt u LLM's om de outputs van andere LLM's te beoordelen aan de hand van een gestructureerde rubriek, wat resulteert in een statistische kwaliteitsverdeling in plaats van een binair geslaagd/mislukt-oordeel.

### Fase 1: De Gouden Dataset (Golden Dataset)
In plaats van het schrijven van traditionele unit tests vereist AI software engineering een "Gouden Dataset". Dit is een gecureerde database van 100 tot 500 uiteenlopende invoeren (gebruikers-prompts, geüploade PDF-bestanden, complexe randgevallen) gekoppeld aan door mensen goedgekeurde ideale uitkomsten of specifieke beoordelingscriteria. Deze dataset fungeert als het verankeringspunt van de waarheid voor uw niet-deterministische systeem.

### Fase 2: De LLM-as-a-Judge Pipeline
Wanneer een ontwikkelaar een prompt aanpast of het RAG-zoekalgoritme (Retrieval-Augmented Generation) wijzigt, wordt de code niet zomaar naar de staging-omgeving gepusht. De CI/CD-pipeline voert de nieuwe codebase uit tegen de gehele Gouden Dataset.

Omdat het handmatig beoordelen van 500 langdurige uitkomsten ondoenlijk is, gebruikt de pipeline een secundair, uiterst strikt geprompt LLM (de "Judge" of Beoordelaar). De Judge beoordeelt de output van de applicatie op basis van een scoring-rubriek (bijv. "Beoordeel nauwkeurigheid op een schaal van 1-10", "Controleer op hallucinaties", "Verifieer merktoon").

### Fase 3: Statistische Uitrol-Drempels (Deployment Guardrails)
De CI/CD-pipeline voegt de scores van de Judge samen. Een uitrol naar productie wordt alleen toegestaan als de nieuwe prompt een statistisch significante verbetering aantoont (bijv. "Gemiddelde nauwkeurigheidsscore gestegen van 8,2 naar 8,7, en het hallucinatiepercentage is gedaald tot onder 2%"). Als de score daalt, wordt de pull request automatisch geblokkeerd. Dit elimineert het probleem van onbetrouwbare tests en vervangt het door robuust, statistisch vertrouwen.

## Hoe LaunchStudio AI-Software Ontwikkelt

Het bouwen van een volwaardige EDD-pipeline vereist gespecialiseerde MLOps-infrastructuur (Machine Learning Operations) waarover standaard webontwikkelaars zelden beschikken.

[LaunchStudio](https://launchstudio.eu/nl/), aangedreven door de diepe enterprise software engineering-roots van [Manifera](https://www.manifera.com/), implementeert deze geavanceerde AI-engineeringkaders voor schaalbare SaaS-bedrijven.

Onder de architectonische visie van CEO Herre Roelevink in Amsterdam, en uitgevoerd door onze gespecialiseerde platform engineering-teams aan de Phố Quang-straat 10 in Ho Chi Minhstad, transformeren wij uw team van chaotisch "prompt-tweakerschap" naar rigoureuze AI software engineering.

Onze EDD-implementatie omvat:
1. **Evaluatie-Frameworks:** Wij integreren gespecialiseerde open-source evaluatieframeworks (zoals Ragas, LangSmith of TruLens) rechtstreeks in uw GitHub Actions of GitLab CI.
2. **Deterministische Wrappers:** Wij implementeren strikte JSON Schema-handhaving (met behulp van tools zoals Zod of OpenAI Structured Outputs) om niet-deterministische LLM's te dwingen voorspelbare, type-safe datastructuren op te leveren die uw traditionele frontend kan verwerken zonder te crashen.
3. **Schaduw-Uitrol (Shadow Deployments):** Voordat een grote prompt-update live gaat, richten wij een "Schaduwmodus" in. De nieuwe prompt draait op de achtergrond parallel met de oude prompt in productie en beoordeelt de verschillen in stilte zonder de nieuwe output aan de gebruiker te tonen. Zodra het statistische vertrouwen hoog genoeg is, schakelen we de feature-flag om.

## Belangrijkste inzichten

- **Determinisme is voorbij**: LLM's zijn stochastisch; traditionele binaire unit tests (TDD) en Agile-story points functioneren niet voor prompt-engineering.
- **Implementeer Evaluation-Driven Development (EDD)**: Bouw een Gouden Dataset van 100-500 randgevallen en gebruik een secundair LLM als "Judge" in uw CI/CD-pipeline.
- **Automatiseer de kwaliteitsdrempel**: Blokkeer pull requests via GitHub Actions als de gemiddelde nauwkeurigheidsscore daalt of het hallucinatiepercentage stijgt.

## Echt voorbeeld

### Een AI-native oprichter in actie: De Fintech CTO gevangen in prompt-helling

Marcus is de CTO van een in Londen gevestigde fintech-startup die crediteurenadministratie automatiseert. De kern van hun product was een AI-engine (snel gebouwd met Bolt) die PDF-facturen in verschillende talen verwerkte, regelitems extraheerde en deze koppelde aan de interne boekhoudcodes van het bedrijf.

Gedurende de eerste twee maanden werkte het systeem fantastisch. Toen besloot Marcus' team om de centrale systeem-prompt te "verbeteren" om een specifiek randgeval met Franse btw-tarieven af te handelen.

Een junior ontwikkelaar paste de prompt aan, testte drie Franse facturen lokaal, zag dat het perfect werkte en pushte de code naar productie.

De volgende ochtend werden de Franse btw-facturen inderdaad vlekkeloos verwerkt. De prompt-wijziging had echter een catastrofaal, onbedoeld effect op Duitse facturen. De AI begon plotseling leveranciersnamen te hallucineren en factuuradressen te verwisselen. Omdat de traditionele unit tests alleen controleerden of de API een `200 OK` en een geldig JSON-object teruggaf, was de CI/CD-pipeline vlekkeloos geslaagd. Het systeem faalde in alle stilte.

Tegen de tijd dat klanten vier dagen later de gecorrumpeerde boekhoudgegevens opmerkten, moest Marcus' team duizenden onjuiste grootboekboekingen handmatig terugdraaien. De ontwikkelaars durfden de prompt vervolgens niet meer aan te raken. De ontwikkeling van nieuwe functies kwam volledig tot stilstand.

Om de ontwikkelingssnelheid te herstellen, schakelde Marcus LaunchStudio in.

Het engineeringteam van Manifera voerde een directe interventie uit. Binnen 15 werkdagen vervingen zij Marcus' traditionele CI/CD-pipeline volledig door een Evaluation-Driven Development (EDD) framework.

Ten eerste verzamelden zij 400 historische facturen (de Gouden Dataset) die elke taal, elk randgeval en elk formaat dekten dat het systeem ooit was tegengekomen.
Ten tweede implementeerden zij een LLM-as-a-Judge evaluatiescript met behulp van LangSmith.
Wanneer een ontwikkelaar nu een prompt aanpast om een Frans btw-probleem op te lossen, verwerkt de CI/CD-pipeline automatisch alle 400 facturen met de nieuwe prompt. De Judge LLM vergelijkt de nieuwe extracties met de Gouden Dataset. Als de Franse nauwkeurigheid stijgt, maar de Duitse nauwkeurigheid met zelfs maar 1% daalt, blokkeert de pipeline expliciet de merge en geeft exact aan welke Duitse facturen zijn mislukt.

**Resultaat:** De ontwikkelingssnelheid keerde direct terug. Ontwikkelaars waren niet langer verlamd door angst omdat de EDD-pipeline een wiskundig vangnet bood. Het hallucinatiepercentage in productie daalde naar 0,1%, en Marcus' team schaalde het systeem succesvol naar het verwerken van 50.000 facturen per maand voor grote Europese ondernemingen.

> *"We probeerden een neuraal netwerk te beheren met dezelfde tools die we gebruikten voor een eenvoudige database. Het was een ramp die op het punt stond te gebeuren. LaunchStudio heeft niet alleen onze code gerepareerd; ze hebben onze complete engineeringafdeling geleerd hoe je daadwerkelijk software bouwt in het AI-tijdperk. De evaluatiepipeline die ze hebben gebouwd is het meest waardevolle stuk infrastructuur dat we bezitten."*
> — **Marcus Sterling, CTO, LedgerAI (Londen)**

**Kosten & Doorlooptijd:** € 12.500 (Launch & Grow Pakket met Enterprise MLOps & EDD Add-on) — productieklaar en uitgerold in 15 werkdagen.

---

## Veelgestelde vragen

### Hoe schatten we de tijd voor AI-functies in als prompt-engineering zo onvoorspelbaar is?
U moet het "deterministische" werk scheiden van het "stochastische" werk. Schat de API-integratie, het databaseschema en de UI-componenten met behulp van standaard Agile-story points. Gebruik voor de prompt-engineering en tuning-fase Timeboxing (bijv. "We besteden exact 3 dagen aan het tunen van deze prompt tegen de Gouden Dataset. De score die we vrijdag behalen is de versie die we lanceren, en we itereren in de volgende sprint").

### Kan ik traditionele test-frameworks zoals Jest of PyTest gebruiken voor AI-applicaties?
Ja, maar uitsluitend voor de deterministische "infrastructuur". U moet absoluut Jest gebruiken om te testen of uw databaseverbinding werkt, uw API-routes authenticatie vereisen en uw frontend correct rendert. U moet Jest echter *niet* gebruiken om de daadwerkelijke tekst-output van de LLM te testen. Triggert voor de LLM-output een EDD-script dat een Judge-model gebruikt om de semantische betekenis van de reactie te scoren.

### Wat is het grootste risico van stille AI-degradatie?
Het grootste risico is dat een onderliggend AI-model (zoals GPT-4) een stilzwijgende update krijgt van de provider die de redeneerpatronen licht veranderd. Uw prompt, die zes maanden lang perfect werkte, begint plotseling randgevallen te missen. Omdat er aan uw zijde geen code is gewijzigd, merkt standaard monitoring dit niet op. LaunchStudio ondervangt dit door uw Gouden Dataset dagelijks uit te voeren tegen productie; als de gemiddelde score overnacht daalt, ontvangt u direct een waarschuwing.

### Wordt het uitvoeren van een LLM om een ander LLM te beoordelen in CI/CD niet enorm kostbaar?
Dat kan het worden als het slecht is ontworpen. U hoeft echter niet het duurste model (zoals GPT-4o of Claude 3.5 Sonnet) te gebruiken als Judge voor elke routine-test. LaunchStudio ontwerpt EDD-pipelines die snelle, voordelige modellen (zoals GPT-4o-mini of Llama 3 8B) gebruiken voor 90% van de routinematige evaluatietaken (zoals het controleren van de JSON-structuur en trefwoordaanwezigheid), en bewaart de duurdere modellen uitsluitend voor complexe semantische beoordelingen.

### Hoe voorkomen we dat ontwikkelaars de EDD-pipeline omzeilen?
De EDD-pipeline moet op repository-niveau worden afgedwongen via branch protection rules (bijvoorbeeld in GitHub). Een pull request kan fysiek niet worden gemerged naar de `main`-branch tenzij de geautomatiseerde Evaluation-action een "Pass"-status teruggeeft op basis van de door u ingestelde statistische drempelwaarde. LaunchStudio configureert deze strikte Platform Engineering guardrails zodat de governance geautomatiseerd en wiskundig wordt afgedwongen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe schatten we de tijd voor AI-functies in als prompt-engineering zo onvoorspelbaar is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Scheid deterministisch werk van stochastisch werk. Schat API's en UI met Agile points. Gebruik voor prompt-tuning strikte Timeboxing (bijv. 3 dagen tunen tegen de Gouden Dataset en de beste versie lanceren)."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik traditionele test-frameworks zoals Jest of PyTest gebruiken voor AI-applicaties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, maar alleen voor deterministische infrastructuur (DB, auth, UI). Gebruik voor LLM-tekst-output een EDD-script met een Judge-model dat de semantische betekenis scoort."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het grootste risico van stille AI-degradatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat de AI-provider het onderliggende model stilzwijgend bijwerkt. Uw prompt begint te falen zonder dat uw code verandert. LaunchStudio voert dagelijks de Gouden Dataset uit om dit op te sporen."
      }
    },
    {
      "@type": "Question",
      "name": "Wordt het uitvoeren van een LLM om een ander LLM te beoordelen in CI/CD niet enorm kostbaar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet als het goed is ontworpen. LaunchStudio gebruikt snelle, voordelige modellen (zoals GPT-4o-mini) voor 90% van de routinetaken, en reserveert dure modellen voor complexe semantische beoordelingen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomen we dat ontwikkelaars de EDD-pipeline omzeilen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dwing het af via repository branch protection rules in GitHub. Een PR kan fysiek niet worden gemerged tenzij de geautomatiseerde evaluatie een Pass-status teruggeeft."
      }
    }
  ]
}
</script>
