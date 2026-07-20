---
Titel: De Rol van Productmanagers in de Best Of AI
Trefwoorden: Het beste van AI, Rol, AI, Product, Manager
Koperfase: Bewustzijn
---

# De Rol van Productmanagers in de Best Of AI
Decennia lang was software-engineering **deterministisch**. Als een gebruiker X invoert, voert de database Y uit. Productmanagers bouwden rigoureuze wireframes, schreven exacte acceptatiecriteria en ontwikkelaars bouwden precies wat was gespecificeerd. Generatieve AI heeft dit paradigma doorbroken. LLM's zijn **probabilistisch**. Als een gebruiker X invoert, kan de AI Y, Z uitvoeren of vol vertrouwen een volledig verzonnen antwoord verzinnen. Om een ​​B2B AI SaaS te bouwen, moet de rol van de Product Manager fundamenteel evolueren van het beheren van functies naar het beheren van chaos.

## De foutmarge beheren

In traditionele software is een bug een mislukking. Bij generatieve AI is een hallucinatie een inherent kenmerk van het statistische model. Je kunt geen 100% nauwkeurigheid bereiken.

De kerntaak van de AI PM is het definiëren van de **Aanvaardbare foutmarge** op basis van de use case. Als je een AI-tool bouwt die marketingtweets genereert, is een nauwkeurigheidspercentage van 80% prima; een hallucinerende tweet is enigszins gênant, maar kan gemakkelijk door de gebruiker worden verwijderd. Als je een AI-tool bouwt om medische patiëntendossiers samen te vatten, is een nauwkeurigheidspercentage van 99% onaanvaardbaar; een hallucinatiepercentage van 1% zal iemand doden. De PM moet beslissen of de technologie daadwerkelijk haalbaar is voor het specifieke bedrijfsrisicoprofiel.

## Het ontwerpen van de terugval (Human-in-the-Loop)

Omdat de AI onvermijdelijk zal falen, moet de AI PM de sierlijke faalstatus ontwerpen. Dit staat bekend als de ‘Fallback’- of ‘Human-in-the-Loop’-workflow (HITL).

Als de AI een juridische opdracht genereert, mag de gebruikersinterface deze niet als voltooide pdf presenteren. De premier moet de gebruikersinterface zo ontwerpen dat de generatie als een 'concept' wordt gepresenteerd. De interface moet de beweringen benadrukken waar de AI het minst vertrouwen in heeft, klikbare citaten bieden die teruglinken naar de brondocumenten (RAG) en de menselijke advocaat dwingen om het document te beoordelen en op "Goedkeuren" te klikken voordat het document kan worden geëxporteerd. De PM ontwerpt voor vertrouwen, niet alleen voor automatisering.

## Evaluatiegestuurde ontwikkeling (Evals)

Traditionele PM’s schrijven User Stories. AI PM's bouwen **Eval Datasets**. Je kunt niet weten of een AI-functie ‘goed’ is door deze een keer te testen.

De AI PM moet een enorme spreadsheet samenstellen van 500 gebruikersvragen uit de echte wereld en hun ‘ideale antwoorden’. Wanneer het technische team wil overstappen van OpenAI's GPT-4 naar Anthropic's Claude 3 om geld te besparen, pushen ze niet alleen de code. Ze voeren het nieuwe model uit tegen de 500 Evals. De premier beoordeelt de resultaten om er zeker van te zijn dat het ‘generatiesuccespercentage’ niet achteruitgaat. De Eval-dataset is het belangrijkste bezit dat het productteam bezit.

## Navigeren door de afweging tussen latentie en kwaliteit

AI introduceert strikte fysieke beperkingen die traditionele SaaS niet heeft. De slimste modellen hebben de langste tijd nodig om tekst te genereren en kosten het meeste geld.

De AI PM moet voortdurend door deze driehoek navigeren: **Snelheid versus kosten versus kwaliteit**. Als een functie onmiddellijke feedback vereist (zoals automatisch aanvullen in een code-editor), moet de premier de ingenieurs opdracht geven een snel, dom en goedkoop model te gebruiken (zoals Llama 3 8B). Als een functie 's nachts op de achtergrond draait (zoals het samenvatten van 100 lange contracten), geeft de premier het team opdracht om het langzaamste, duurste en kwalitatief beste model te gebruiken dat beschikbaar is. De PM dicteert de architecturale routeringsstrategie op basis van de beperkingen van de gebruikerservaring.

## Belangrijkste afhaalrestaurants

- Traditionele software is deterministisch (voorspelbaar). AI is probabilistisch (onvoorspelbaar). Productmanagers moeten overstappen van het schrijven van exacte functiespecificaties naar het beheren van aanvaardbare foutmarges.

- Omdat geen enkele LLM 100% accuraat is, moet de AI PM robuuste 'Fallback' en 'Human-in-the-Loop' UI-workflows ontwerpen, waarbij de AI-uitvoer wordt gepresenteerd als een concept dat menselijke beoordeling vereist.

- AI PM's moeten 'Eval Datasets' beheren: enorme databases met testquery's en ideale antwoorden die worden gebruikt om voortdurend de kwaliteit van het model te benchmarken wanneer de onderliggende prompt of architectuur verandert.

- De AI PM is verantwoordelijk voor de afweging tussen latentie en kwaliteit, waarbij hij beslist wanneer snelle/goedkope modellen moeten worden gebruikt voor directe UI-interacties versus langzame/dure modellen voor complexe achtergrondtaken.

- Het uiteindelijke doel van een AI Product Manager is het opbouwen van gebruikersvertrouwen. De gebruikersinterface moet duidelijk aangeven wanneer de AI onzeker is en verifieerbare citaten voor de resultaten ervan verstrekken.

## Verzend betere AI-producten

Zijn uw technici bezig met het bouwen van AI-functies die gebruikers niet vertrouwen? **LaunchStudio** helpt oprichters bij het opzetten van rigoureuze 'Evaluation-Driven Development'-pijplijnen en het ontwerpen van intuïtieve, Human-in-the-Loop-interfaces die het vertrouwen van de onderneming vergroten.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: componenttokens ontwerpen voor een verkoop-CRM

Sadie, een retailcoördinator, gebruikte **Lovable** om een CRM te bouwen. Ze had moeite om de lay-outspecificaties aan AI-ontwikkelaars door te geven.

Ze werkte samen met **LaunchStudio (door Manifera)** om gestructureerde ontwerptokens en componenten te creëren.

**Resultaat:** Verfijnde workflow verminderde de iteratiecycli van prototypes met 60%.

**Kosten en tijdlijn:** € 1.100 (Design Token Setup) — productieklaar en binnen 3 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom falen traditionele productmanagementframeworks met AI?

Traditionele PM vertrouwt op voorspelbare software. AI is probabilistisch; het kan hallucineren of antwoorden verzinnen. Je kunt geen traditionele 'User Stories' schrijven voor een systeem dat onvoorspelbaar handelt.

### Wat is de primaire taak van een AI-productmanager?

Het definiëren van de 'aanvaardbare foutenmarge'. Ze moeten bepalen hoe vaak de AI mag falen, en de UX-fallbacks (zoals Human-in-the-Loop-workflows) ontwerpen voor wanneer dit onvermijdelijk gebeurt.

### Wat is 'evaluatiegestuurde ontwikkeling'?

In plaats van traditioneel testen beheert de AI PM een database met honderden testprompts. Elke keer dat de technici de code aanpassen of de LLM wijzigen, wordt deze getest aan de hand van deze evaluaties om er zeker van te zijn dat de kwaliteit niet is gedaald.

### Moet een AI PM weten hoe hij moet coderen?

Ze hoeven geen productiecode te schrijven, maar ze moeten de architectuur diepgaand begrijpen. Ze moeten het verschil kennen tussen RAG en fijnafstemming, en de latentie- en tokenbeperkingen begrijpen.