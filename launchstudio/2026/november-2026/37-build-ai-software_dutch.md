---
Title: "Bouw AI Software: De Transitie van Prompt Engineering naar AI Engineering"
Keywords: build ai software, build ai app, ai engineering, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: CTO / Senior Software Engineer
---

# Bouw AI Software: De Transitie van Prompt Engineering naar AI Engineering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bouw AI Software: De Transitie van Prompt Engineering naar AI Engineering",
  "description": "Om AI software te bouwen die daadwerkelijk overleeft in productie, moeten teams 'prompt engineering' loslaten en kiezen voor rigoureuze AI engineering praktijken, waaronder DSPy, prompt versioning en deterministische parsing.",
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
  "datePublished": "2026-12-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/build-ai-software"
  }
}
</script>

Tijdens de absolute pioniersdagen van de generatieve AI-boom domineerde één gloednieuwe functietitel de hele tech-industrie: De Prompt Engineer. 

Om revolutionaire AI software te bouwen, namen wanhopige bedrijven massaal "Prompt Engineers" in dienst. Dit waren mensen die zich louter specialiseerden in het typen van uiterst specifieke, bijna magische zinnen zoals: *"Jij bent een wereldklasse expert. Haal diep adem en denk stap-voor-stap na. Als je faalt, word ik ontslagen."* Deze vage bezweringen (incantations) werden domweg rechtstreeks en keihard in de backend van de applicatie geschreven (hardcoded). Soms werkten ze ronduit briljant. Maar veel vaker faalden ze compleet desastreus. 

Nu we dieper het jaar 2026 in duiken, is de industrie massaal wakker geschud door een harde realiteit: **Prompt Engineering is absoluut géén software engineering; het is pure bijgelovigheid (superstition).** 

Als jij de uiterst serieuze ambitie hebt om een enterprise AI applicatie te bouwen die probleemloos miljoenen euro's aan transacties kan verwerken, kun je onmogelijk bouwen (en vertrouwen) op een wanhopige alinea van 500 woorden vol met smeekbedes en trucjes, hardcoded in een obscuur TypeScript-bestandje. Je móét de onvermijdelijke transitie maken van de fragiele, zweverige kunst van Prompt Engineering naar de loeiharde, systematische discipline van **AI Engineering**.

## De Breekbaarheid Van De "Mega-Prompt"

Wanneer een niet-technische oprichter óf een junior developer anno nu een AI code generator (zoals Cursor of Bolt) inzet om razendsnel een AI app te bouwen, leunt de resulterende architectuur vrijwel áltijd zwaar op een zogeheten "Mega-Prompt".

Een Mega-Prompt is één gigantisch, massief blok platte tekst dat rücksichtslos vlak vóór de daadwerkelijke input van de eindgebruiker wordt geïnjecteerd. Dit wangedrocht probeert wanhopig om werkelijk álle mogelijke edge cases tegelijkertijd af te vangen in één adem: het moet de diepe intentie van de gebruiker correct bepalen, de output loeistrak formatteren als JSON, garanderen dat de tone of voice uitermate beleefd blijft, moedwillige prompt injections meedogenloos blokkeren, én tegelijkertijd ook nog even al zijn bronnen feilloos citeren. 

### Waarom de Mega-Prompt Keihard Faalt in Productie

1. **Het Aandacht-Verwateringsprobleem (Attention Dilution):** Large Language Models kampen steevast met het beruchte "Lost in the Middle" fenomeen. Als jij een LLM volstouwt met een system prompt van maar liefst 2.000 woorden, waarin je hem luidkeels vertelt dat hij zich aan 50 verschillende, keiharde regels moet houden, verwatert zijn aandachtsmechanisme (attention mechanism) gigantisch. Hij formatteert de JSON output misschien 100% vlekkeloos (Regel 42), maar is halverwege domweg finaal vergeten om die beleefde toon aan te slaan (Regel 7). 
2. **Het "Spooky Action at a Distance" Probleem:** Heb je een Mega-Prompt gebouwd? Dan zal het aanpassen van letterlijk één lullig zinnetje om een simpel bugje te fixen (bijv. de toevoeging *"Gebruik nooit meer het woord 'utilize'"*), op volstrekt onverklaarbare wijze een compleet ongerelateerd, vér weggelegen onderdeel van de output finaal slopen (ineens stopt de LLM compleet met het citeren van bronnen). De Mega-Prompt gedraagt zich als een extreem fragiel kaartenhuis; raak je één kaartje aan, dan stort de complete constructie gillend in elkaar.
3. **De Ongeversioneerde Chaos (Unversioned Chaos):** Developers hebben de levensgevaarlijke neiging om Mega-Prompts doodleuk direct in de actieve codebase aan te passen (tweaken), zonder óóit ergens te documenteren wáárom die specifieke wijziging is doorgevoerd. Zonder een robuust, gespecialiseerd versiebeheer-systeem (versioning system) louter ontworpen voor prompts, heeft je hele team fundamenteel de mogelijkheid niet om een foute prompt-wijziging direct terug te draaien (roll back) zodra de AI op productie (live) de boel bij elkaar begint te hallucineren.

## Het AI Engineering Paradigma

Om robuuste AI software te bouwen die wél daadwerkelijk schaalt, móét je afscheid nemen van de Mega-Prompt. Elitaire AI Engineering vervangt deze archaïsche, monolithische tekstblokken door strakke, modulaire pijplijnen, loeiharde programmatische optimalisatie, en militair versiebeheer.

### 1. Modulaire Ketens (Chains): De Vervanger van de Mega-Prompt
In plaats van één arme LLM-aanroep onmogelijk te dwingen om vijf volstrekt verschillende taken tegelijkertijd uit te voeren, bouwt een serieuze AI Engineer een kogelvrije "Chain" (keten). 
- **Stap 1 (Routering):** Een razendsnel, uiterst goedkoop model (zoals Claude Haiku) scant puur de user input en classificeert direct, en louter, de intentie (bijv. *"Is dit een onschuldige supportvraag of een waardevolle sales-query?"*).
- **Stap 2 (Extractie):** Een specifiek getraind, gespecialiseerd extractie-model trekt uitsluitend de belangrijkste entiteiten (namen, datums, getallen) uit de tekst en spuugt deze uit als 100% strakke, rauwe JSON.
- **Stap 3 (Generatie):** Tot slot pakt een zwaar, peperduur redeneringsmodel (reasoning model, zoals GPT-4o) deze gestructureerde JSON op, en genereert exclusief het vloeiende, definitieve eindantwoord. 

Conclusie: Heeft Stap 3 opeens een serieus toon-probleem (tone issue)? Dan fix je letterlijk en uitsluitend de geïsoleerde prompt voor Stap 3. Je hebt de variabelen strak geïsoleerd, waardoor dat dodelijke "spooky action at a distance" per direct, 100% is geëlimineerd.

### 2. Prompts als Echte Code (Prompt Versioning)
Binnen hoogwaardige AI Engineering is een prompt absoluut geen simpele string-variabele (tekst). Het is een bloedserieuze, losstaande asset die rücksichtslos geversioneerd (versioned), keihard getest, en onafhankelijk van de codebase gedeployed moet worden. Elite teams gebruiken specifieke, zware registries (zoals Langfuse of Portkey) om al hun prompts strak te managen. Een prompt wordt daarin opgeslagen als bijvoorbeeld `v1.2.4`. Als een update naar `v1.2.5` ineens heftige hallucinaties veroorzaakt, rolt de slimme backend de prompt volautomatisch direct terug (roll back) naar `v1.2.4`, zónder dat het team de hele Node.js of Python server offline moet halen voor een lastige redeployment.

### 3. Programmatische Prompt Optimalisatie (DSPy)
De meest brute, geavanceerde doorbraak binnen AI Engineering is de brede adoptie van complexe frameworks zoals DSPy (Demonstrate-Search-Predict). In plaats van dat een zwetende mens wanhopig probeert te raden (guesswork) wat de "állerbeste formulering" (phrasing) voor een prompt zou kunnen zijn, definieert de mens louter de kale, strakke *architectuur* van de pijplijn en overhandigt hij domweg een dataset vol uitstekende, goedgekeurde voorbeelden. 
Het meedogenloze DSPy-framework compileert (compiles) en optimaliseert vervolgens wiskundig de prompt. Het test volautomatisch duizenden bizarre variaties, om exact dát specifieke taalgebruik (phrasing) te ontdekken dat de allerhoogste, puur wiskundige accuratesse oplevert voor dé specifieke LLM die op dat moment gebruikt wordt. De mens stopt simpelweg met het tikken van de prompt; het geavanceerde algoritme compileert het.

## Hoe LaunchStudio AI Software Bouwt (Builds)

De loodzware transitie van een speels prototype (krakkemikkig aangedreven door een breekbare Mega-Prompt) naar een onverwoestbaar productie-systeem (loeistrak aangedreven door modulaire DSPy-pijplijnen), vereist bloedserieuze, uiterst diepe en sterk gespecialiseerde AI architectuur. 

[LaunchStudio](https://launchstudio.eu/nl/), rotsvast gesteund door de massieve enterprise engineering vuurkracht van [Manifera](https://www.manifera.com/), is exact, en specifiek, gebouwd om dít complexe architecturale transitieproces te executeren. 

Opererend onder de meedogenloze strategische leiding van CEO Herre Roelevink in Amsterdam, en perfect geëngineerd door snoeiharde AI-specialisten aan de Pho Quang Street 10 in Ho Chi Minh City, transformeert LaunchStudio jouw 'prompt-based' AI-speelgoed meedogenloos tot échte, brute, engineering-grade software.

Wanneer wij jouw haperende AI backend compleet opnieuw opbouwen (rebuild), voeren wij het loeistrakke AI Engineering draaiboek uit:
1. **Pijplijn Modularisatie:** We slopen jouw archaïsche, massieve system prompts van 2.000 woorden genadeloos tegen de vlakte (tear down). We architecteren strakke, multi-step LLM chains die complexe redenering (reasoning), extractie en formattering fysiek van elkaar scheiden (separate). Dit verplettert je hallucinatie-rates en decimeert onmiddellijk je torenhoge API-kosten.
2. **DSPy Compilatie:** We implementeren uiterst brute, programmatische prompt optimalisatie. We gaan absoluut niet blind raden (guess) wat de AI toevallig "graag wil horen"; we gebruiken kille wiskunde (math) om de aller-efficiëntste instructies volautomatisch te compileren, strak gebaseerd op de keiharde data uit jouw specifieke dataset.
3. **Prompt Registries:** We integreren zware, enterprise prompt management systemen. We ontkoppelen jouw gevoelige prompt logica rücksichtslos van je applicatiecode (decoupling). Dít stelt jou in staat om het gedrag van de AI real-time, live aan te passen zónder dat je óóit nog zenuwachtig nieuwe servers (deployments) live hoeft te pushen.
4. **Deterministische Parsing:** We verpakken werkelijk íédere AI-call strak in kogelvrije Schema Validators (zoals Zod). Hiermee garanderen we snoeihard dat de fundamenteel niet-deterministische, rommelige LLM-output meedogenloos wordt geparset in 100% perfect voorspelbare, rigide datastructuren, lang vóórdat deze output je fragiele database of frontend ook maar kán aanraken.

## Praktijkvoorbeeld

### Een AI-Native Founder in de praktijk: De Juridische Contract Parser Die Continu In Elkaar Stortte

Sarah, een briljante founder in München, bouwde vol passie "ClauseCheck": een hippe AI-applicatie waarmee lokale makelaars (real estate agents) in een handomdraai dikke, commerciële huurcontracten (lease agreements) konden uploaden. De AI zou razendsnel alle cruciale voorwaarden (zoals huurprijs, looptijd, en ontbindende voorwaarden) feilloos extraheren en deze keurig strak presenteren in een overzichtelijk, clean dashboard.

Ze had haar complete MVP (Minimum Viable Product) lokaal in Cursor in elkaar gesleuteld, zwaar leunend op een gigantische, monsterlijke Mega-Prompt. Haar prompt begon braaf met: *"Jij bent een zwaar gespecialiseerde Duitse advocaat in het vastgoed..."* en ratelde vervolgens maar liefst 1.500 wanhopige woorden lang door, met extreem gedetailleerde instructies over hóé de AI exact 20 verschillende datapunten moest extraheren en deze als één vlekkeloos JSON-object moest formatteren.

Tijdens de interne bètatest draaide de app de eerste 80% van de tijd wonderbaarlijk goed. Maar die overige 20% van de tijd? Dan crashte de hele applicatie catastrofaal (catastrophically). Soms vergat de zwoegende AI domweg één flauwe komma in de JSON syntax, wat onmiddellijk resulteerde in een dodelijke crash van de frontend parser. Op andere momenten, wanneer er toevallig een bovengemiddeld extreem lang contract werd geüpload, raakte de LLM finaal afgeleid (distracted) door de lengte. De AI stopte bruusk met zijn JSON-extractie en begon in plaats daarvan opeens vrolijk een samenvatting (summary) van het contract te schrijven als een gigantisch blok platte tekst.

Sarah besteedde frustrerende, lange weken aan het wanhopig tweaken en masseren van haar Mega-Prompt. Ze voegde in pure paniek blokken tekst toe in HOOFDLETTERS: *"JE MAG UITSLUITEND EN ALLEEN JSON OUTPUTTEN!"* Het hielp he-le-maal niets. De applicatie was fundamenteel veel te onbetrouwbaar (unreliable) om met droge ogen te kunnen verkopen aan serieuze, zware enterprise vastgoedkantoren.

Sarah greep in en schakelde direct LaunchStudio in. Het Manifera engineeringteam arriveerde en diagnosticeerde de fatale architectuurfout (issue) onmiddellijk: ClauseCheck leed loodzwaar aan Aandacht-Verwatering (Attention Dilution) én had een schokkend gebrek aan loeistrakke deterministische parsing. 

In amper 12 werkdagen re-architecteerde LaunchStudio de voltallige backend rücksichtslos en volledig. Ze rukten de levensgevaarlijke Mega-Prompt met wortel en tak uit de code. Ze vervingen het direct door een uiterst kogelvrije, modulaire pijplijn. 
Allereerst stampte een supergoedkoop model het originele document genadeloos in kleine, hanteerbare secties (chunking). 
Vervolgens werd een extreem gespecialiseerd extractiemodel (extraction model) ingezet om uitsluitend en alleen de data te grijpen, waarbij LaunchStudio OpenAI's Structured Outputs forceerde. (Dit dwingt het LLM-model puur wiskundig om louter valide JSON uit te spuwen die perfect, 100% matcht met een loeistrak Zod schema). 
Tot slot knalden ze DSPy eroverheen, om zo volautomatisch de allerbeste extractie-instructies te compileren op basis van een stevige dataset van 50 eerdere, succesvol verwerkte contracten.

**Resultaat:** De catastrofale JSON parsing errors (crashes) crashten onmiddellijk en spectaculair naar 0,0%. De pure extractie-accuratesse vloog keihard omhoog van een matige 80% naar een ongekende 99,5%. Omdat het peperdure, zware redeneerwerk (heavy reasoning) nu loeistrak geïsoleerd was tot kleine, losse chunks in plaats van het hele document in één keer door de molen te jagen, stortten de API-kosten met maar liefst 40% in elkaar. Sarah verkocht nog geen maand later razendsuccesvol de peperdure enterprise-versie van ClauseCheck aan drie gigantische Münchense vastgoedkantoren, wat haar per direct een keiharde €11.000 aan MRR opleverde.

> *"Ik behandelde die AI in het begin letterlijk als een menselijke werknemer; ik was continu in mijn prompts aan het smeken en bedelen (begging) of hij asjeblieft, asjeblieft zijn werk goed wilde doen. LaunchStudio heeft die waanzin er bij mij hardhandig uitgeslagen en me geleerd dat je een AI puur moet behandelen als een wiskundige compiler. Ze hebben die hele zweverige 'prompt engineering' onzin meedogenloos uit de app gerukt en het direct vervangen door hardcore, industriële software engineering. Exact dát was hét verschil tussen een falend, knutsel-prototype en een robuust miljoenenproduct."*
> — **Sarah Müller, Oprichter, ClauseCheck (München)**

**Kosten & Tijdlijn:** €7.200 (Launch & Grow Pakket, fors versterkt met de AI Pipeline Modularization Add-on) — productie-klaar, kogelvrij en live gedeployed in exact 12 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### (Scenario: Developer die hardnekkig prompts schrijft) Waarom zorgt het simpelweg toevoegen van *"Denk stap-voor-stap na"* (Think step by step) aan mijn prompt er soms voor dat mijn output eigenlijk drastisch sléchter wordt?

De befaamde *"Denk stap-voor-stap na"* (Chain of Thought) techniek forceert een AI-model domweg om zijn kostbare context window massief te verbruiken met het oeverloos uittypen van logische redeneringen (reasoning), vóórdat het ook maar toekomt aan het eigenlijke antwoord. Als jouw taak simpelweg louter neerkomt op strakke "data extractie" (data extraction), dan leidt al dat nutteloze geredeneer de aandacht van het model gigantisch, en fataal, af van de loeistrenge formatteringsregels die je zo zorgvuldig had opgeschreven. Serieuze AI Engineering leunt zwaar op modulaire pijplijnen, waarbij het "redeneren" (reasoning) én het "formatteren" fysiek worden opgeknipt in twee aparte, gespecialiseerde AI calls, in plaats van dat je ze wanhopig allebei in één zielige prompt propt.

### (Scenario: Oprichter die een nieuw development team samenstelt) Moet ik dan maar zo'n dure 'Prompt Engineer' inhuren om mijn stagnerende AI app beter te maken?

In 2026 is het inhuren van een 'toegewijde' Prompt Engineer — iemand wiens enige vaardigheid het intikken van leuk klinkende tekstjes is — een ronduit catastrofale en dure fout. Je hebt een pure "AI Engineer" nodig: een hardcore software developer (software developer) die exact weet hoe hij DSPy moet inzetten, vector databases droomt, JSON schema enforcement kan configureren, en complexe CI/CD evaluatie-pijplijnen bouwt. De cruciale vaardigheid (skill) anno 2026 is láng niet meer het schrijven van dat ene, perfecte zinnetje; de échte skill is het onwrikbaar en kogelvrij architecteren van het voltallige systeem rondom de LLM om, zodat je snoeihard wiskundig deterministische outputs kán garanderen.

### (Scenario: Technische oprichter die moedeloos wordt van JSON errors) Hoe garandeer ik nou écht, 100% absoluut zeker, dat de LLM te allen tijde valide JSON uitspuugt die mijn frontend niet direct doet crashen?

Dit kun je simpelweg fundamenteel en wiskundig níét (cannot guarantee) garanderen door slechts wat dreigende teksten in je prompt op te nemen (zoals *"Output uitsluitend valide JSON"*). Je móét dit rücksichtslos afdwingen en beveiligen op de API-laag. LaunchStudio implementeert loeistrikte Schema Enforcement (wij gebruiken hiervoor tools als Zod, keihard gecombineerd met de Structure Outputs van OpenAI of de Tool Use functionaliteit van Anthropic). Dit limiteert fysiek en dwingend het tokengeneratie-proces van de AI. Het maakt het wiskundig (mathematically impossible) totaal en volkomen onmogelijk voor het model om een cruciaal haakje (bracket) te vergeten of per ongeluk een foutief data type terug te sturen.

### (Scenario: CTO die de architectuur voorbereidt op grote schaal) Waarom in hemelsnaam is het zo'n ontzettend slecht idee om mijn prompts gewoon braaf in Git te versioneren?

Git is primair en louter ontworpen (designed) voor logische, deterministische code, en he-le-maal niet voor chaotische, niet-deterministische, vage tekstinstructies (zoals prompts). Als je vandaag in Git één lullig zinnetje van een prompt aanpast, heb je letterlijk nul (zero) onmiddellijk zicht op hoe exact die specifieke, ogenschijnlijk onschuldige wijziging plotseling de hallucinatie-rate (hallucination rate) of de peperdure API-kosten keihard gaat beïnvloeden bij al jouw live gebruikers. LaunchStudio integreert uitsluitend gespecialiseerde Prompt Management Registries (zoals het zware Langfuse). Deze superieure registries (registries) stellen jou in staat om live A/B testen te draaien met nieuwe prompts rechtstreeks op productie, tracken genadeloze analytics per prompt versie, én laten je binnen één seconde terugrollen (roll back) naar een oude versie zónder dat je óóit een trage server-redeployment hoeft af te wachten.

### (Scenario: Developer die voor het eerst naar DSPy kijkt) Wat doet DSPy nou écht daadwerkelijk, wat ik niet gewoon prima zelf handmatig kan typen en optimaliseren?

Het framework DSPy behandelt jouw fragiele prompts letterlijk louter als kille wiskundige parameters die geoptimaliseerd moeten worden (parameters to be optimized), exact zoals de gewichten (weights) in een klassiek neuraal netwerk. Als jij vandaag besluit om jouw gigantische foundation model om te wisselen van OpenAI GPT-4 naar een Claude 3.5 Sonnet, dan zal jouw zorgvuldig, handgeschreven prompt (die gisteren nog perfect werkte) vandaag plotseling genadeloos, onverklaarbaar falen (suddenly fail). Binnen het brute DSPy framework, wissel jij echter simpelweg één model configuratie (model configuration) instelling om, waarna het gigantische framework volautomatisch de onderliggende prompt-instructies compleet, wiskundig hercompileert en optimaliseert, strak toegespitst op de specifieke eigenaardigheden van Claude, direct gebaseerd op de waarheid in jouw dataset. Het elimineert werkelijk ál het trage, handmatige (manual) giswerk (trial-and-error guesswork) voor altijd uit het serieuze AI development proces.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom verslechtert de output soms als ik 'Denk stap-voor-stap na' aan mijn prompt toevoeg?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor simpele taken zoals data extractie verbruikt de LLM te veel context (attention) aan het genereren van irrelevante logica. AI Engineering scheidt het 'redeneren' en het 'formatteren' rücksichtslos in twee aparte, gespecialiseerde API calls, in plaats van alles in één fragiele prompt te dwingen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik anno 2026 een dure 'Prompt Engineer' inhuren om mijn AI app op te knappen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. In 2026 heb je exclusief een hardcore 'AI Engineer' nodig — een software developer die DSPy begrijpt, vector databases kan configureren en deterministische JSON schema enforcement bouwt. De skill is niet langer tekstjes schrijven, maar het architecteren van de infrastructuur."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe garandeer ik absoluut en wiskundig dat de LLM 100% valide JSON uitspuugt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Je kunt dat onmogelijk garanderen met een stukje tekst in je prompt. Je móét het afdwingen op de API-laag (bijv. via OpenAI Structured Outputs + Zod). Dit forceert en limiteert fysiek het LLM token-generatieproces, waardoor ongeldige JSON wiskundig onmogelijk wordt. LaunchStudio implementeert dit standaard."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is het vastleggen (versioneren) van mijn prompts in Git zo'n enorm slecht idee?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Git is ontworpen voor deterministische code, niet voor chaotische prompts. In Git zie je onmogelijk live hoe een prompt-wijziging direct de hallucinatie-rates (liegen) of API-kosten beïnvloedt. LaunchStudio gebruikt zware Prompt Registries (zoals Langfuse) voor live A/B tests en instant rollbacks, zónder server-redeployments."
      }
    },
    {
      "@type": "Question",
      "name": "Wat doet DSPy nou écht precies, wat ik niet zelf kan 'tweaken'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "DSPy test volautomatisch en wiskundig duizenden variaties van je prompt tegen een dataset om de absolute, optimale formulering te vinden. Stap je over van GPT-4 naar Claude? Dan hercompileert DSPy de prompt perfect voor dat nieuwe model, wat alle onzekerheid (guesswork) uit de development sloopt."
      }
    }
  ]
}
</script>
