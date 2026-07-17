---
Titel: Aangepaste AI-agenten vanaf nul bouwen
Trefwoorden: Day AI, Gebouw, Aangepast, AI, Agenten, Scratch
Koperfase: Bewustzijn
---

# Vanaf nul aangepaste AI-agenten bouwen
De technologie-industrie gooit het woord ‘agent’ losjes rond. Een chatbot die een e-mail genereert, is geen agent. Een Agent is een autonoom systeem dat een complex doel kan doordenken, meerdere opeenvolgende acties kan uitvoeren via API's en koers kan corrigeren als een stap mislukt. Hoewel veel oprichters vertrouwen op zware raamwerken zoals LangChain om agenten te bouwen, is de onderliggende architectuur verrassend eenvoudig. Hier leest u hoe u helemaal opnieuw een aangepaste, zeer betrouwbare AI-agent in Node.js kunt bouwen.

## De kernvereiste: gereedschapsoproep

Een LLM is een brein in een pot. Het kan niets anders doen dan tekst genereren. Om er een agent van te maken, moet je hem de hand geven. Dit wordt bereikt via **Tool Calling** (voorheen Function Calling).

Wanneer u een prompt naar OpenAI verzendt, verzendt u ook een reeks JSON-schema's die de tools definiëren die uw Node.js-server bezit. 

Als de gebruiker vraagt: *"Hoeveel heeft Acme Corp ons betaald?"*, beseft de LLM dat hij het niet weet. In plaats van te hallucineren, pauzeert het en voert een JSON-commando uit: `{"call": "get_customer_revenue", "args": {"id": "acme"}}`. Uw Node-server voert de databasequery uit en stuurt de cijfers terug naar de LLM.

## De ReAct-lus (reden + handelen)

De architectuur van een aangepaste agent is eenvoudigweg een 'while'-lus die op uw server draait en het ReAct-framework uitvoert.

1. **Redenering:** De LLM kijkt naar het doel van de gebruiker. Het formuleert een plan. ("Ik heb de inkomsten van Acme nodig, daarna moet ik de CEO een e-mail sturen."*)

2. **Actie:** De LLM voert een Tool Call uit om de inkomsten te ontvangen.

3. **Observatie:** Uw Node-server voert de tool uit, haalt de gegevens op ($50.000) en voegt deze toe aan de gespreksgeschiedenis.

De 'while'-lus wordt opnieuw geactiveerd. De LLM ziet de nieuwe waarneming, realiseert zich dat stap 1 is voltooid en start stap 2 (het aanroepen van de e-mailtool). De lus gaat door totdat de LLM besluit dat het overkoepelende doel is voltooid. Op dat moment wordt de lus verbroken en een laatste sms-bericht teruggestuurd naar de gebruiker.

## Foutloos omgaan met fouten

Agenten falen voortdurend. De LLM geeft mogelijk het verkeerde argumenttype (een tekenreeks in plaats van een geheel getal) door aan uw databasetool. Als je een zwaar raamwerk gebruikt, crasht de hele keten.

Wanneer u helemaal opnieuw bouwt, verpakt u de uitvoering van de tool in een `try/catch`-blok op uw Node-server. Als de tool crasht, vang je de fout op en stuur je deze *terug* naar de LLM: `"Observatie: Fout, ID moet een geheel getal zijn."` De LLM is slim genoeg om de fout te lezen, zijn eigen fout te corrigeren en de tool opnieuw aan te roepen met de juiste gegevens. Zelfcorrectie is het kenmerk van een echte agent.

## De oneindige lusvangrail

Omdat de Agent autonoom is, kan hij soms in een psychotische toestand terechtkomen. Het roept een tool aan, faalt, probeert het opnieuw, faalt en herhaalt zich oneindig. Voor $ 0,01 per API-aanroep kan een oneindige lus u $ 100 per uur kosten.

Uw aangepaste Node.js-architectuur moet een harde 'Max Iteraties'-limiet bevatten. Als de 'while'-lus 5 iteraties bereikt, beëindigt uw code de lus met kracht en antwoordt aan de gebruiker: *"Ik heb een fout aangetroffen bij het voltooien van deze taak."* Deze vangrail van 5 regels beschermt uw startup tegen financiële ondergang.

## Belangrijkste afhaalrestaurants

- Een 'Agent' is niet zomaar een chatbot. Het is een LLM die in een softwarelus is geplaatst en waarmee deze autonoom functies (Tools) kan oproepen, de resultaten kan analyseren en beslissingen kan nemen om een ​​doel te bereiken.

- 'Tool Calling' geeft de LLM de mogelijkheid om met uw backend te communiceren. De LLM pauzeert het genereren van tekst om een ​​JSON-payload uit te voeren, waarbij uw Node-server wordt geïnstrueerd om een ​​specifieke API- of databasequery uit te voeren.

- De kernarchitectuur van een agent is de 'ReAct'-lus (Reason, Act, Observe). Het voert een 'while'-lus uit op uw backend, waarbij voortdurend de LLM wordt bevraagd en tools worden uitgevoerd totdat het uiteindelijke doel is bereikt.

- Als bij het bouwen van aangepaste agenten de uitvoering van een tool mislukt, stuurt u de tekst van de fout terug naar de LLM. De AI is vaak slim genoeg om de fout te begrijpen en de volgende tool call zelf te corrigeren.

- U moet een 'Max Iterations'-variabele in uw backend-lus implementeren. Als een agent hallucineert en vast komt te zitten in een oneindige herhalingslus, voorkomt deze vangrail enorme API-kosten.

## Bouw autonome workflows

Vertrouwt u op broze, opgeblazen raamwerken die tijdens de productie vastlopen? **LaunchStudio** ontwerpt zeer betrouwbare, op maat gemaakte AI-agents in pure Node.js, waarbij gebruik wordt gemaakt van native Tool Calling en robuuste foutafhandelingsloops die zijn afgestemd op bedrijfskritische B2B-omgevingen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-Native oprichter in actie: een aangepaste State Machine Agent bouwen voor een reisplanner

Elijah, een reisagent, gebruikte **Lovable** om een AI-reisplanner te bouwen. De algemene chatbot ging vaak off-topic en slaagde er niet in om de vereiste boekingsinformatie op volgorde te verzamelen.

Hij werkte samen met **LaunchStudio (door Manifera)** om de planner opnieuw op te bouwen met behulp van een deterministische, door de staatsmachine aangestuurde agentstroom.

**Resultaat:** Het succespercentage van het verzamelen van boekingen steeg van 40% naar 95%, waarbij de AI gebruikers opeenvolgend vroeg om ontbrekende details.

**Kosten en tijdlijn:** € 2.400 (ontwikkeling van aangepaste agenten) — productieklaar en binnen 6 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is het verschil tussen een LLM en een agent?

Een LLM is een staatloze tekstgenerator. Een agent is een LLM die is verpakt in een 'while'-lus die hem toegang geeft tot externe tools (zoals API's), waardoor hij autonome acties kan ondernemen om problemen in meerdere stappen op te lossen.

### Wat is 'Tool Calling'?

Het is hoe de AI handelt. U voorziet de AI van definities van uw backend-functies. Als het gegevens nodig heeft, voert het een JSON-verzoek uit. Uw server voert de code uit en stuurt de gegevens terug naar de AI.

### Wat is de ReAct-architectuur?

Reden + Handeling. De AI redeneert over het doel, roept een tool aan (Act), observeert het resultaat van uw server en redeneert vervolgens over wat er vervolgens moet gebeuren. Het blijft herhalen totdat de taak is voltooid.

### Hoe voorkom je dat een agent vast komt te zitten in een oneindige lus?

Omdat een AI een toolaanroep kan mislukken en het eindeloos opnieuw kan proberen, moet u een 'Max Iteraties'-limiet hardcoderen in uw Node.js while-lus (bijvoorbeeld een pauze forceren na vijf toolaanroepen) om uw API-factuur te beschermen.