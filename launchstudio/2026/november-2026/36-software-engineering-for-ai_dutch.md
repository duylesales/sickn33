---
Title: Waarom Traditionele Agile Faalt in Software Engineering for AI
Keywords: software engineering for AI, AI software engineering, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: VP of Engineering / CTO
---

# Waarom Traditionele Agile Faalt in Software Engineering for AI

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Engineering voor AI: Waarom Traditionele Agile en TDD Falen",
  "description": "De introductie van niet-deterministische AI modellen verwoest traditionele Software Development Life Cycles (SDLC). Een deep dive in Evaluation-Driven Development (EDD) en AI software engineering.",
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

Gedurende de afgelopen twintig jaar werd software engineering gedomineerd en gedicteerd door één fundamentele aanname: determinisme. Als een software engineer een functie schrijft die domweg twee getallen optelt, dan zal de code `add(2, 2)` altijd, steevast, in 100% van de gevallen exact `4` retourneren. Puur en alleen omdát code deterministisch was, kon de industrie ongelooflijk robuuste, loeistrakke frameworks bouwen: Test-Driven Development (TDD), wendbare Agile sprints van exact twee weken, rigide CI/CD pijplijnen, en binaire pass/fail unit tests.

De pijlsnelle integratie van Large Language Models (LLM's) in de moderne applicatiestack heeft deze heilige aanname echter finaal en rücksichtslos aan gruzelementen geslagen. Software engineering voor AI introduceert een volstrekt chaotische, fundamenteel niet-deterministische (non-deterministic) variabele in de absolute kern van je applicatie. Als jij een LLM de prompt geeft: *"vat dit contract samen"*, dan is de output letterlijk elke afzonderlijke keer nét even iets anders. Op dinsdag retourneert hij vrolijk 200 woorden. Op woensdag plotseling 150. Vandaag formatteert de AI het keurig in bullet points, en morgen spuugt hij exact dezelfde info uit als een massieve, onleesbare alinea (paragraph).

Wanneer een kersverse VP of Engineering wanhopig probeert om een complex AI-project te managen met behulp van klassieke, traditionele software engineering paradigma's, loopt het project onvermijdelijk volledig vast. Zorgvuldig geschreven unit tests falen zomaar willekeurig (zogeheten flaky tests). Ouderwetse Agile inschattingen (estimations) blijken compleet onmogelijk, puur omdat je onmogelijk vooraf kunt voorspellen hoe lang het gaat duren om een prompt nét zo lang te "tunen" totdat de AI stopt met hallucineren. 

Om échte, serieuze enterprise-grade AI software te bouwen, móéten engineering leiders een fundamenteel nieuwe Software Development Life Cycle (SDLC) adopteren, die heel specifiek en uitsluitend is ontworpen voor stochastische (willekeurig bepaalde) systemen.

## De Totale Ineenstorting Van Traditionele Paradigma's In AI

Voordat we de exacte oplossing uitrollen, moeten we chirurgisch ontleden waarom onze vertrouwde, traditionele software engineering methodologieën compleet ineenstorten zodra ze in aanraking komen met AI.

### 1. De Dood Van Binaire Unit Testing (Het Falen Van TDD)
Binnen klassieke TDD schrijf je een ijskoude, wiskundige bewering (assertion): `assert(result == "verwachte_string")`. Binnen AI engineering is dít domweg en fysiek onmogelijk. Als jouw kersverse AI een wervelende marketing e-mail genereert, kun je fundamenteel niet testen op een 'exacte string match'. Wanhopige engineering teams proberen dit nog weleens op te lossen met agressieve regex (het controleren of specifieke woordjes toevallig voorkomen in de tekst), maar dit is uiterst fragiel (brittle). Een fenomenaal geschreven, super creatieve AI e-mail gebruikt misschien nét niet exact dat ene keyword waar jouw regex blind op zoekt, wat een onterechte 'test failure' triggert. Tegelijkertijd kan een volstrekt belabberde, gehallucineerde flut-e-mail toevallig wél exact dat ene woordje bevatten, wat resulteert in een valse, onterechte 'pass'. Zodra tests onvoorspelbaar en flaky worden, breekt je voltallige, traditionele CI/CD pijplijn.

### 2. De Onmogelijke Inschatting (Het Falen Van Agile)
Binnen de veilige kaders van Agile schat een engineer een ticket in (bijv. "3 Story Points") puur gebaseerd op zijn eerdere ervaring met het bouwen van vrijwel identieke, voorspelbare CRUD-features (Create, Read, Update, Delete). Binnen AI duurt het daadwerkelijk 'bouwen' van de feature (het simpele API calltje naar OpenAI) hooguit 10 minuten. Maar het vervolgens dwingen van diezelfde feature om te *stoppen met hallucineren bij complexe edge cases*? Dát duurt misschien 3 dagen. Of misschien 3 weken. Je weet het niet. De distributie van de daadwerkelijke uren (effort) is gigantisch zwaar scheefgetrokken richting 'prompt tuning' en edge-case mitigatie, waardoor het klassiek meten van sprint velocity in theorie en praktijk volstrekt nutteloos wordt.

### 3. De Stille Degradatie (Het Falen Van Monitoring)
Klassieke, traditionele software crasht met enorm veel kabaal. Het smijt agressief met een `NullReferenceException` of triggert keihard een `500 Server Error`, waarna PagerDuty de halve afdeling gillend wakker belt. AI software daarentegen faalt muisstil (fails silently). Als OpenAI toevallig hun model onzichtbaar updatet op de achtergrond (bijv. van `gpt-4-0613` naar een iets nieuwere versie), besluit dat model de volgende dag zomaar, op eigen houtje, om ineens een totaal ánder deel van jouw zwoegend geschreven system prompt prioriteit te geven. Je code crasht niet. De server staat niet in brand. De API retourneert nog steeds vrolijk een `200 OK`. Maar... de zuivere kwaliteit van de gegenereerde teksten degradeert heel langzaam en geruisloos. Je irriteert ongemerkt je gebruikers, je churn schiet door het dak, én dit alles zónder dat er ooit ook maar één enkel, traditioneel Datadog-alarm afgaat.

## Het Nieuwe Paradigma: Evaluation-Driven Development (EDD)

Om deze architecturale horror-crises te bezweren, hebben de absolute, elitaire AI engineering teams TDD resoluut bij het grofvuil gezet. Zij hebben het compleet vervangen door Evaluation-Driven Development (EDD). 

Binnen EDD test je niet langer krampachtig voor een exacte, rigide output. In plaats daarvan zet je vol in de aanval: je gebruikt letterlijk andere LLM's om de outputs van jóúw LLM te beoordelen (graden) tegen een strakke rubric, wat een statistische distributie van pure kwaliteit genereert, in plaats van een domme, binaire pass/fail.

### Fase 1: De Golden Dataset
In plaats van blind unit tests te typen, eist AI software engineering dwingend de aanleg van een zogeheten "Golden Dataset". Dit is een uiterst zorgvuldig gecureerde (curated) database vol met 100 tot 500 extreem diverse, pittige inputs (complexe user prompts, rommelige PDF's, brekende edge cases), onlosmakelijk gekoppeld aan 100% human-approved (door mensen goedgekeurde), perfecte ideale outputs, of specifieke grading criteria. Deze massieve dataset is vanaf nu het onwrikbare anker van keiharde de waarheid binnen jouw anders zo niet-deterministische systeem.

### Fase 2: De LLM-as-a-Judge Pijplijn
Als een developer vandaag de dag even een system prompt wijzigt, of het RAG (Retrieval-Augmented Generation) zoekalgoritme 'verbetert', pusht hij die code absoluut niet meer zomaar door naar de staging server. In plaats daarvan vuurt de CI/CD pijplijn de gloednieuwe codebase rücksichtslos af op de voltallige, gigantische Golden Dataset. 

Omdat het met de hand beoordelen en lezen (evaluating) van 500 lange AI-antwoorden letterlijk ondoenlijk is voor je team, vuurt de pijplijn een secundaire, extreem zwaar geprompte LLM (de "Judge" of Rechter) af op de resultaten. Deze onverbiddelijke Judge beoordeelt en scoort (evaluates) de verse output van de applicatie op basis van een snoeiharde rubric (bijv. *"Beoordeel de accuratesse van 1 tot 10"*, *"Controleer agressief op hallucinaties"*, *"Verifieer of de brand tone klopt"*). 

### Fase 3: Statistische Deploy Vangrails (Guardrails)
De CI/CD pijplijn aggregeert koud en wiskundig alle individuele scores van de Judge. Een daadwerkelijke deployment naar productie (live-gang) wordt uitsluitend en louter toegestaan als de kersverse prompt aantoonbaar een *statistisch significante* verbetering oplevert (bijv. *"De gemiddelde accuratesse score steeg van 8.2 naar 8.7, én de hallucinatie-ratio knalde omlaag tot ruim onder de 2%"*). Zodra de geaggregeerde score onverhoopt zakt, wordt het pull request fysiek en rücksichtslos geblokkeerd. Deze architectuur liquideert het dodelijke "flaky test" probleem 100%, en vervangt het door massieve, robuuste statistische zekerheid.

## Hoe LaunchStudio AI Software Engineert

Het compleet from scratch opbouwen van een waterdichte EDD-pijplijn eist bloedserieuze, gespecialiseerde MLOps (Machine Learning Operations) infrastructuur; iets waar standaard web-developers vrijwel nooit écht verstand van hebben. 

[LaunchStudio](https://launchstudio.eu/nl/), rotsvast aangedreven door de diepe, decennialange enterprise software engineering wortels van [Manifera](https://www.manifera.com/), implementeert deze uiterst geavanceerde AI engineering frameworks puur en alleen voor opschalende SaaS-bedrijven. 

Onder de loeistrakke, architecturale visie van CEO Herre Roelevink in Amsterdam, en vlekkeloos geëxecuteerd door onze dedicated platform engineering teams aan de Pho Quang Street 10 in Ho Chi Minh City, rukken we jouw development team weg van het chaotische, kansloze "prompt tweaking", en loodsen we ze direct naar volwassen, rigoureuze AI software engineering.

Onze EDD Implementatie omvat onder meer:
1. **Evaluation Frameworks:** We integreren loeizware, gespecialiseerde open-source evaluation frameworks (zoals Ragas, LangSmith, of TruLens) ram- en ramvast direct ín jouw GitHub Actions of GitLab CI.
2. **Deterministische Wrappers (Wrappers):** We implementeren kogelvrije, brute JSON Schema afdwinging (met behulp van tools zoals Zod of OpenAI Structured Outputs). Hiermee dwingen (force) we de chaotische, niet-deterministische LLM's snoeihard om 100% voorspelbare, type-safe datastructuren uit te spuwen, die jouw traditionele frontend vervolgens wél veilig kan consumeren zónder halverwege te crashen.
3. **Shadow Deployments:** Voordat we een gigantische, risicovolle prompt update live zetten op productie, architecteren we verplicht een zogeheten "Shadow Mode". De fonkelnieuwe prompt draait onzichtbaar, keurig parallel (in de schaduw) mee met de oude prompt, rechtstreeks op de echte live-productie data. Hij beoordeelt de verschillen muisstil op de achtergrond, zónder de nieuwe, ongeteste output óóit aan de nietsvermoedende gebruiker te tonen. Pas op het moment dat de wiskundige, statistische zekerheid (confidence) torenhoog is, schakelen we de feature flag definitief om.

## Praktijkvoorbeeld

### Een AI-Native Founder in de praktijk: De Fintech CTO Die Vastzat In De Hel Van Prompting

Marcus is de uiterst gedreven CTO van een hypermoderne fintech startup in Londen, gespecialiseerd in het volautomatisch verwerken van inkomende facturen (accounts payable). De absolute kern van hun paradepaardje was een superieure AI-engine (destijds in sneltreinvaart in elkaar geklikt met Bolt) die rauwe PDF-facturen in talloze talen inlas, foutloos alle line items (regels) extraheerde, en deze perfect wegschreef naar de interne boekhoudcodes van het bedrijf.

De eerste twee maanden na de live-gang was de software magisch, en een doorslaand succes. Echter, op een fatale dinsdag besloot het team van Marcus dat ze de core system prompt zélf wel eventjes konden "verbeteren", puur om een hoogst irritante, extreem zeldzame edge case op te lossen die te maken had met de specifieke berekening van de BTW (VAT) op uitsluitend Franse facturen. 

Een gemotiveerde junior developer dook de codebase in, tweakte de prompt, draaide lokaal braaf drie test-factuurtjes, zag tot zijn opluchting dat alles lokaal werkte, en pushte de gloednieuwe code doodleuk door naar productie. 

De volgende ochtend was er feest: de complexe Franse BTW-facturen werden inderdaad subliem en 100% foutloos verwerkt. Echter... deze lullige prompt-wijziging had achter de schermen een onvoorzien, ronduit catastrofaal neveneffect op de verwerking van *Duitse* facturen. De AI begon daar uit het niets, volledig op eigen houtje, agressief complete leveranciersnamen te hallucineren en draaide argeloos complete factuuradressen (billing addresses) om. Omdat hun ouderwetse, traditionele unit tests alleen maar domweg checkten óf de API braaf een `200 OK` en een 'valide' JSON object retourneerde, was de hele CI/CD pijplijn groen opgelicht. Het systeem was rücksichtslos, maar muisstil, gecrasht (failed silently). 

Vier lange dagen later ontdekten de woedende klanten pas de zwaar gecorrumpeerde boekhouddata. Marcus en zijn voltallige development team hebben vervolgens wekenlang, huilend, handmatig duizenden foute kasboek-entries (ledger entries) moeten terugdraaien. De opgelopen trauma's waren zo groot dat de developers simpelweg doodsbang werden (terrified) om ooit nog ook maar één letter in de core prompt aan te passen. Alle innovatie en de feature development kwam met een schokkende klap volledig tot stilstand.

Uit pure, bittere nood en wanhopig op zoek naar verloren engineering velocity, vloog Marcus LaunchStudio in.

Het meedogenloze engineeringteam van Manifera arriveerde in Londen en greep direct keihard in. In amper 15 werkdagen sloegen ze de voltallige, waardeloze en traditionele CI/CD pijplijn van Marcus volledig kort en klein. Ze vervingen het in recordtempo door een genadeloos, wiskundig Evaluation-Driven Development (EDD) framework. 

Allereerst trokken ze razendsnel 400 zware, historische facturen uit de archieven (de Golden Dataset), die werkelijk écht elke exotische taal, idiote edge case, en raar bestandsformaat afdekten dat het systeem in al die jaren ooit voorbij had zien komen. 
Vervolgens schreven en implementeerden ze een loeistrak LLM-as-a-Judge evaluatiescript, aangedreven door LangSmith. 
Als diezelfde junior developer vanaf nu een prompt lichtjes aanpast om snel een Frans BTW-probleempje te fixen, draait de nieuwe CI/CD pijplijn volautomatisch alle 400 loodzware facturen direct door die splinternieuwe prompt heen. De ijzeren Judge LLM vergelijkt onmiddellijk de verse output met de heilige waarheid uit de Golden Dataset. Knalt de Franse accuratesse inderdaad omhoog, maar dipt de Duitse accuratesse ook maar met een marginale 1% omlaag? Dan weigert en blokkeert (blocks) de pijplijn de code direct, snoeihard, en highlight hij vlekkeloos exact wélke Duitse test-facturen er zijn stukgelopen.

**Resultaat:** De felbegeerde engineering velocity keerde instant, op de allereerste dag, weer terug. Developers bevroren niet langer van angst achter hun toetsenbord, puur omdat de massieve EDD pijplijn ze voorzag van een onbreekbaar, wiskundig vangnet (safety net). De levensgevaarlijke hallucinatie-ratio op productie crashte spectaculair naar 0,1%, en het team van Marcus wist het fintech-systeem extreem succesvol op te schalen. Ze verwerken nu moeiteloos 50.000 facturen per maand voor de allergrootste enterprises in Europa.

> *"We deden een bizarre, waanzinnige poging om een wild en onvoorspelbaar neuraal netwerk (neural network) te managen met exact hetzelfde oude gereedschap waarmee we vroeger simpele databases doormeetden. Het was gewoon wachten tot de boel ontplofte. LaunchStudio heeft niet alleen 'even' onze code gefixt; ze hebben letterlijk onze voltallige engineering afdeling compleet opnieuw moeten opvoeden (re-educated) in hoe je in hemelsnaam échte software bouwt in dit complexe AI tijdperk. Die loeizware evaluatie-pijplijn die ze hebben gebouwd, is vandaag de dag, zónder twijfel, het meest waardevolle stukje infrastructuur dat we überhaupt bezitten."*
> — **Marcus Sterling, CTO, LedgerAI (Londen)**

**Kosten & Tijdlijn:** €12.500 (Launch & Grow Pakket, fors verzwaard met de Enterprise MLOps & EDD Add-on) — productie-klaar, kogelvrij, en live gedeployed in 15 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### (Scenario: VP Engineering die bezig is met de sprintplanning) Hoe in hemelsnaam schatten we de tijd in (estimations) voor complexe AI features, als 'prompt engineering' een dermate chaotisch en onvoorspelbaar proces is?

Je bent domweg verplicht om het "deterministische" werk rücksichtslos los te koppelen (decouple) van het onvoorspelbare "stochastische" werk. Je schat (estimate) de API integratie, de database schema's, en de UI-onderdelen nog altijd in via de standaard Agile punten. Voor de chaotische 'prompt engineering en tuning' fase, introduceer je agressieve Timeboxing (bijv. *"We spenderen exact 3 volle dagen om deze prompt te tunen tegenover de Golden Dataset. De hoogste, best scorende versie die we op vrijdagochtend hebben, deployen we. Klaar. We itereren de volgende sprint wel weer verder."*).

### (Scenario: Developer die klassieke tests moet schrijven) Kan ik nou nog wél gewoon mijn vertrouwde, traditionele test frameworks zoals Jest of PyTest gebruiken voor moderne AI applicaties?

Jazeker, absoluut, maar louter en uitsluitend voor het domme, voorspelbare "loodgieterswerk" (de deterministische plumbing). Je móét en zal absoluut Jest gebruiken om snoeihard te testen of je database connectie standhoudt, of je API routes keurig authenticatie afdwingen, en of je complexe frontend foutloos rendert. Echter, je mag werkelijk nóóit (maar dan ook nooit) Jest misbruiken om de tekstuele inhoud (de output) van de LLM zelf te testen. Om die LLM output te keuren, móét je een zwaar EDD script triggeren dat een slim Judge model inzet om de diepe, semantische betekenis (semantic meaning) van het AI-antwoord correct te scoren.

### (Scenario: CTO die de architectuur doorlicht) Wat is eigenlijk het allergrootste, dodelijkste risico van deze "stille AI degradatie" (silent AI degradation)?

Het aller-, allergrootste risico is dat het onderliggende foundation model (zoals GPT-4) op een nacht ineens een compleet onzichtbare (silent) update krijgt doorgeschoven vanuit de provider (OpenAI), die het logische redeneerpatroon van de AI net een millimetertje verlegt. Jouw peperdure prompt, die letterlijk zes maanden lang vlekkeloos heeft gedraaid, begint plotseling aan de lopende band edge cases compleet te missen. Omdat de fysieke code (de API calls) aan jóúw kant totaal niet is veranderd, zal standaard Datadog monitoring dit falen simpelweg niet detecteren (misses it). LaunchStudio roeit dit gevaar snoeihard uit door jouw zware Golden Dataset simpelweg stug elke nacht (daily) tegen de productieomgeving aan te gooien; als de gemiddelde EDD-score vannacht ineens zakt, rinkelt om 08:00 uur onmiddellijk jouw alarm.

### (Scenario: Oprichter die stress krijgt van AI kosten) Wordt het niet ronduit absurd en peperduur om voor élke simpele test een complete LLM in te zetten louter om de output van een ándere LLM te beoordelen in mijn CI/CD?

Ja, dat escaleert enorm, als je het slecht of lui engineert. Echter, je hoeft he-le-maal niet per se het allerduurste, zwaarste model (zoals GPT-4o of Claude 3.5 Sonnet) in te zetten als de allesbepalende Judge voor elk lullig testje. LaunchStudio architecteert slimme, uiterst efficiënte EDD pijplijnen die specifiek razendsnelle, spotgoedkope modellen inzetten (zoals de snelle GPT-4o-mini of een Llama 3 8B) voor ruim 90% van alle routinematige, saaie evaluatietaken (zoals het controleren op een valide JSON structuur, of het verifiëren van keywords). We reserveren en triggeren (reserving) de loodzware, extreem dure modellen exclusief en alleen voor hoogcomplexe, linguïstische semantische grading, waardoor jouw torenhoge CI/CD kosten strak, scherp en hoogst geoptimaliseerd (highly optimized) blijven.

### (Scenario: Engineering Director in een snelgroeiend team) Hoe voorkom ik in godsnaam fysiek dat luie developers die de EDD pijplijn te lastig vinden, mijn security regels negeren en hun code alsnog live forceren (overriding)?

De complete EDD pijplijn móét je meedogenloos afdwingen (enforced) op het allerhoogste repository niveau, via snoeiharde branch protection rules (bijvoorbeeld loeivast binnen GitHub). Een pull request kan simpelweg fundamenteel en fysiek níét langer (cannot be merged) naar de live `main` branch worden gepusht, tenzij de geautomatiseerde Evaluation action (de LLM Judge) officieel een snoeiharde "Pass" (goedgekeurd) status retourneert, strak gebaseerd op de keiharde statistische grens die jij vooraf hebt ingesteld. LaunchStudio configureert deze loodzware Platform Engineering vangrails, zódat die complexe governance (toezicht) 100% volautomatisch en puur wiskundig is afgedwongen (mathematically enforced). Dit roeit domweg in één klap de gevaarlijke menselijke fout en vooringenomenheid (human bias) compleet uit.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe schatten we de tijd in (estimations) voor AI features als 'prompt engineering' zo onvoorspelbaar is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Koppel deterministisch werk los van stochastisch werk. Schat API integraties en de UI in via de standaard Agile punten. Voor de chaotische 'prompt tuning', introduceer je agressieve Timeboxing (bijv. 'We spenderen exact 3 dagen aan het tunen. De beste versie op vrijdag gaat live')."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik mijn traditionele test frameworks zoals Jest of PyTest nog wel gebruiken voor moderne AI applicaties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, maar uitsluitend voor het voorspelbare, deterministische 'loodgieterswerk' (database connecties, authenticatie). Gebruik nóóit Jest om de teksten (output) van een LLM te testen. Trigger daarvoor altijd een EDD script met een Judge model om de semantische betekenis te scoren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het allergrootste risico van deze 'stille AI degradatie' (silent AI degradation)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat OpenAI onzichtbaar het foundation model updatet, waardoor jouw peperdure, werkende prompt plotseling edge cases mist, zónder dat je code verandert of crasht. Standaard monitoring ziet dit niet. LaunchStudio runt jouw Golden Dataset elke nacht om dit direct te detecteren."
      }
    },
    {
      "@type": "Question",
      "name": "Wordt het niet absurd duur om voor élke test een LLM te gebruiken louter als 'Judge' in mijn CI/CD?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. LaunchStudio bouwt slimme EDD pijplijnen die goedkope, razendsnelle modellen (zoals GPT-4o-mini) inzetten voor 90% van het saaie evaluatiewerk. De loeizware, dure modellen triggeren we exclusief voor hoogcomplexe linguïstische evaluaties."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik fysiek dat luie developers de EDD pijplijn negeren en hun code alsnog live forceren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dwing het meedogenloos af via zware branch protection rules in de repository (bijv. GitHub). Een pull request kan simpelweg níét naar de main branch, tenzij de LLM Judge volautomatisch een wiskundige 'Pass' retourneert. LaunchStudio bouwt deze onwrikbare vangrails."
      }
    }
  ]
}
</script>
