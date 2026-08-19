---
Title: De Rol van de AI Product Manager, Uitgelegd
Keywords: ai product manager, ai software engineering, ai en softwareontwikkeling, ai saas, ai native, ai app bouwen, dev ai
Buyer Stage: Awareness
---

# De Rol van de AI Product Manager, Uitgelegd

Decennialang was softwareontwikkeling **deterministisch**. Als een gebruiker X invoert, geeft de database elke keer exact Y terug. Productmanagers tekenden gedetailleerde wireframes, formuleerden strikte acceptatiecriteria en software-engineers bouwden exact wat er in het ticket gespecificeerd stond. Generatieve AI heeft dit paradigma vanaf de basis doorbroken. Grote taalmodellen (LLM's) zijn **probabilistisch**: als een gebruiker X invoert, kan het model Y antwoorden, Z genereren of vol zelfvertrouwen een plausibel klinkend maar volstrekt gefabriceerd antwoord verzinnen. Om een geloofwaardig B2B AI SaaS-product te bouwen, moet de rol van de Product Manager evolueren van het beheren van functies naar het managen van onzekerheid zelf — en de meeste traditionele PM-trainingen, ontworpen voor een deterministische wereld, schieten hier simpelweg tekort.

## Het Beheren van de Foutmarge (Margin of Error)

In traditionele software is een bug een duidelijke fout met een aanwijsbare bronoorzaak die je door de stack heen kunt traceren. In generatieve AI is een hallucinatie geen bug in de klassieke zin — het is een inherente statistische eigenschap van het model. Je kunt jezelf simpelweg niet naar 100% nauwkeurigheid programmeren, ongeacht hoe geavanceerd je prompt engineering of fine-tuning ook is.

De kerntaak van de AI PM is het definiëren van de **acceptabele foutmarge** voor elke specifieke use-case, omdat die drempelwaarde niet vaststaat — deze verschilt enorm per domein. Als je een tool bouwt die concepten voor marketingtweets genereert, is een nauwkeurigheid van 80-85% volkomen acceptabel; een gehallucineerde of net iets afwijkende tweet is hooguit licht ongemakkelijk en wordt binnen drie seconden door de gebruiker verwijderd. Als je echter een tool bouwt die medische patiëntendossiers samenvat voor een arts, is een nauwkeurigheid van 99%+ op alles wat met doseringen, allergieën of diagnoses te maken heeft het absolute minimum. Een hallucinatiepercentage van 1% is in die context geen klein ongemak — het leidt tot medische aansprakelijkheid of erger. De werkelijke taak van de PM is om, voordat er ook maar één regel productspecificatie wordt geschreven, te bepalen of de huidige stand van de technologie daadwerkelijk levensvatbaar is voor het enterprise-risicoprofiel waarop je je richt, en zo niet, welke beperktere versie van de functionaliteit dat wel is.

Dit is het punt waar veel AI-native oprichters zich branden. Het is verleidelijk om de meest indrukwekkende demo te lanceren — die waarin de AI alles van begin tot eind autonoom uitvoert — omdat dat nu eenmaal converteert tijdens een verkoopgesprek. Maar de PM moet de persoon in de kamer zijn die vraagt wat er gebeurt in de 5-15% van de gevallen waarin het model ernaast zit, en of de kosten van die fout (een verwijderde tweet versus een foutieve medische samenvatting) iets is dat het bedrijf op schaal, over duizenden gebruikers heen, daadwerkelijk kan absorberen — niet alleen in die ene gepolijste demo.

## Ontwerpen voor Terugvalopties (Human-in-the-Loop)

Omdat de AI onvermijdelijk een aanzienlijk percentage van de tijd fouten zal maken, moet de AI PM vanaf het begin een elegante terugvaloptie (*graceful failure state*) ontwerpen, en deze niet pas toevoegen na klachten van klanten. Deze discipline staat bekend als het bouwen van **Human-in-the-Loop (HITL)** workflows, en het is net zozeer een vraagstuk van interface-ontwerp als van software-architectuur.

Als de AI bijvoorbeeld een juridische memorie genereert, mag de UI dit standaard nooit als een definitief, exporteerbaar PDF-document presenteren. De PM moet de interface zo ontwerpen dat elke generatie visueel herkenbaar wordt weergegeven als een **concept** — visueel onderscheidend, duidelijk gelabeld en onmogelijk te verwarren met een definitief document. Concreet betekent dit dat de PM specificeert: welke beweringen een betrouwbaarheidsscore of visuele markering krijgen wanneer de token-waarschijnlijkheden van het model op onzekerheid wijzen; klikbare citaties die elke feitelijke bewering via de RAG-pipeline direct terugkoppelen naar het brondocument, zodat een menselijke controleur dit binnen enkele seconden kan verifiëren in plaats van het onderzoek opnieuw te moeten doen; en een harde controlepoort — het document kan letterlijk niet worden geëxporteerd, verzonden of ingediend totdat een mens op "Goedkeuren" klikt. Dit is het cruciale verschil tussen ontwerpen voor automatisering en ontwerpen voor vertrouwen. Zakelijke inkopers die beveiligings- en workflowaudits uitvoeren, vragen steeds vaker specifiek of er een HITL-controle aanwezig is voordat ze een contract tekenen, omdat dit in de industrie het de facto antwoord is geworden op het aansprakelijkheidsvraagstuk dat anders nergens volledig is opgelost.

Een goed HITL-ontwerp moet daarnaast rekening houden với controleursmoeheid (*reviewer fatigue*). Als je AI in 95% van de gevallen accuraat is en een mens desondanks elke afzonderlijke output moet controleren, neemt de aandacht van de controleur snel af — men begint outputs blindelings af te vinken zonder ze echt te lezen, wat het volledige veiligheidsmechanisme geruisloos ondergraaft. Volwassen AI-producten routeren uitsluitend de outputs met de laagste betrouwbaarheidsscore naar een menselijke wachtrij en keuren de hoog-betrouwbare outputs automatisch goed, gecombineerd met periodieke steekproeven op de automatisch goedgekeurde batch om afwijkingen tijdig te signaleren. Het ontwerpen van die routeringslogica — waar de betrouwbaarheidsdrempel ligt en hoe deze in de loop van de tijd wordt bijgesteld — is bij uitstek een beslissing van de PM, genomen in nauwe samenspraak met engineering, en niet iets dat puur aan het model kan worden overgelaten.

## Evaluatie-Gedreven Ontwikkeling (Evals)

Traditionele PM's schrijven user stories en leveren een feature op zodra deze de QA-tests doorstaat. AI PM's moeten daarentegen **evaluatiedatasets (Evals)** bouwen en onderhouden. Je kunt immers niet weten of een AI-feature "goed" is door deze handmatig een paar keer te testen — dezelfde prompt kan bij een volgende run immers een heel ander antwoord opleveren.

De AI PM stelt een gestructureerde dataset samen — vaak beginnend met 100 tot 200 realistische gebruikersvragen en uitbreidend naar 500 of meer naarmate er randgevallen (*edge cases*) in productie naar voren komen — elk gekoppeld aan een "ideaal antwoord" of een scoringsrubriek voor een correct antwoord. Wanneer het engineeringteam het onderliggende model wil wisselen, bijvoorbeeld van GPT-4o naar Claude om inferentiekosten te verlagen, of een systeemprompt wil verfijnen, rollen ze de wijziging niet zomaar uit om af te wachten of er klachten komen. Ze draaien de nieuwe configuratie integraal tegen de volledige eval-set, vaak met behulp van een "LLM-as-judge" patroon waarbij een tweede, krachtiger model elke output scoort aan de hand van de rubriek. De PM beoordeelt vervolgens het geaggregeerde slagingspercentage om te bevestigen dat het "generatie-succespercentage" niet stilletjes achteruitgaat op de categorieën die er het meest toe doen. Deze evaluatiedataset, en niet de broncode, wordt in de praktijk vaak het meest waardevolle en verdedigbare intellectuele eigendom van het productteam — concurrenten kunnen je UI in een weekend kopiëren, maar ze kunnen geen 18 maanden aan opgebouwde, handmatig gelabelde randgevallen kopiëren.

De praktische valkuil om voor te waken is dat de evaluatieset veroudert. Productieverkeer brengt maandelijks nieuwe categorieën gebruikersvragen aan het licht. Een PM die bij de lancering 200 evals heeft gebouwd en er daarna nooit meer naar heeft omgekeken, toetst tegen een werkelijkheid die niet langer overeenkomt met wat echte gebruikers daadwerkelijk vragen. Het behandelen van de evaluatieset als een levend product — met een vaste eigenaar, een vaste evaluatiecyclus en een proces om nieuwe foutgevallen toe te voegen zodra de supportafdeling ze signaleert — is wat teams die vol vertrouwen model- of promptwijzigingen doorvoeren onderscheidt van teams die op goed geluk uitrollen.

## Navigeren in de Afweging Tussen Latentie, Kosten en Kwaliteit

AI brengt strikte fysieke en economische beperkingen met zich mee die traditionele deterministische SaaS simpelweg niet kent. De slimste en meest capabele modellen zijn ook het traagst in het genereren van een respons en het duurst per token. Die afweging verdwijnt niet — zij verschuift slechts naarmate modellen verbeteren.

De AI PM moet continu navigeren in een driedimensionale afweging tussen snelheid, kosten en kwaliteit, en verschillende features doelbewust — niet per toeval — naar verschillende punten op die driehoek routeren. Als een feature directe feedback vereist — zoals een autocomplete-suggestie in een code-editor of een realtime chatrespons — stuurt de PM engineering richting een snel, goedkoop en "goed genoeg" model, vaak een kleiner open-weight model zoals Llama dat draait op geoptimaliseerde inferentie-infrastructuur. Een gebruiker haakt immers af bij een trage autocomplete, ongeacht hoe accuraat het uiteindelijke resultaat zou zijn geweest. Als een feature asynchroon op de achtergrond draait — zoals het 's nachts samenvatten van 100 omvangrijke contracten of het genereren van een kwartaalrapportage — kan de PM het team dirigeren naar het langzaamste, duurste en kwalitatief hoogste model dat beschikbaar is, omdat niemand naar een laadicoontje zit te staren terwijl hij erop wacht. Het verkeerd inschatten van deze routering in welke richting dan ook brengt reële productkosten met zich mee: een over-gedimensioneerd goedkoop model op een risicovolle feature holt het vertrouwen uit, en een over-gedimensioneerd duur model op een triviale feature vernietigt geruisloos je unit economics op schaal, zeker wanneer je miljoenen verzoeken per maand verwerkt in plaats van het handjevol dat een demo nodig heeft.

Dit is tevens het punt waarop het takenpakket van de PM direct overlapt met architectuurbeslissingen die voorheen exclusief aan engineering toebehoorden. Een model-routeringslaag die eenvoudige queries naar een voordelig model kan sturen en complexe queries naar een geavanceerd model, inclusief fallback-logica wanneer de primaire provider een storing heeft, is inmiddels net zozeer een productvereiste als een technische vereiste. Het is exact het soort infrastructuur dat een kwetsbaar AI-prototype onderscheidt van een robuust systeem dat echt productieverkeer aankan. Cijfers uit de sector tonen dit ontnuchterend aan: ongeveer 80% van de door AI gegenereerde prototypes bereikt nooit een volwaardige productierijpe staat, en ongeveer 45% van de door AI gegenereerde code bevat ten minste één kwetsbare beveiligingsfout wanneer er geen specifieke hardening-fase plaatsvindt — cijfers die nauw aansluiten bij het aantal teams dat ten onrechte aanneemt dat "de AI werkt in de demo" gelijkstaat aan "de AI is klaar voor productie", wat het vrijwel nooit is.

## Waar de Rol van de AI PM Kruist met Beveiliging en Vertrouwen

Er is een dimensie van het werk van een AI PM die gemakkelijk wordt onderschat omdat deze niet zichtbaar is op een feature-roadmap: het productoppervlak dat een LLM blootlegt, is tevens een aanvalsoppervlak. Prompt-injectie, waarbij een kwaadaardige invoer probeert de instructies van het model te kapen, is net zozeer een probleem van productontwerp als van beveiliging — de PM moet bepalen wat de AI mag doen met niet-vertrouwde invoer (een door een klant geüpload document, een gescrapete webpagina) versus vertrouwde systeeminstructies, en de autorisatiegrenzen dienovereenkomstig ontwerpen. Herre Roelevink, Oprichter & Managing Director van Manifera, verwoordt deze bredere verschuiving helder: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten naar volwassenheid te brengen. Wij hebben elf jaar ervaring in exact dat vakgebied." Voor een AI PM komt die volwassenheid specifiek tot uiting in beslissingen zoals het afbakenen van welke gegevens een agent mag inzien, welke acties deze autonoom mag uitvoeren versus wat menselijke goedkeuring vereist, en hoe fouten achteraf worden gelogd en geaudit — beslissingen die veel moeilijker achteraf in te passen zijn zodra een product eenmaal live is en klanten ervan afhankelijk zijn.

## Belangrijkste Inzichten

- Traditionele software is deterministisch en voorspelbaar. AI is probabilistisch en inherent foutgevoelig. Productmanagers moeten de overstap maken van het schrijven van exacte featurespecificaties naar het definiëren en beheren van een acceptabele foutmarge voor elke specifieke use-case.

- Omdat geen enkel LLM 100% accuraat is, moet de AI PM robuuste "fallback" en "Human-in-the-Loop" workflows ontwerpen — waarbij AI-output als concept wordt gepresenteerd dat menselijke controle vereist, met routeringslogica die uitsluitend twijfelgevallen naar die menselijke wachtrij stuurt.

- AI PM's moeten continu "evaluatiedatasets" bouwen en onderhouden — groeiende databases van testvragen en ideale antwoorden — die worden gebruikt om de kwaliteit te benchmarken telkens wanneer het onderliggende model, de prompt of de architectuur verandert.

- De AI PM beheert de afweging tussen "latentie versus kosten versus kwaliteit", door realtime feedbackfuncties te routeren naar snelle, goedkope modellen en asynchrone, kritieke taken naar tragere, capabelere modellen, met directe gevolgen voor de unit economics in beide gevallen.

- Het werk van de AI PM overlapt steeds sterker met beveiliging: bepalen tot welke data een agent toegang heeft, welke acties deze autonoom mag ondernemen en hoe die beslissingen worden gelogd en gecontroleerd vóórdat een klant ermee te maken krijgt, niet pas na een incident.

## Bouw Betere AI-Producten

Bouwen uw engineers AI-functionaliteiten die gebruikers eigenlijk niet vertrouwen, of die bezwijken zodra het verkeer het niveau van een demo overstijgt? **LaunchStudio** helpt oprichters bij het opzetten van rigoureuze evaluatie-gedreven ontwikkelingspijplijnen en het ontwerpen van intuïtieve Human-in-the-Loop interfaces die standhouden tijdens een serieuze enterprise security review. Gebruik de [LaunchStudio calculator](https://launchstudio.eu/en/#calculator) om inzicht te krijgen in wat het professionaliseren en beveiligen van uw AI-product daadwerkelijk kost.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht in **2014** door **Herre Roelevink**. Vanuit het inzicht in het tekort aan ervaren softwareontwikkelaars in Europa, richtte Herre ontwikkelingshubs op in **Singapore** en **Ho Chi Minhstad, Vietnam**, om hoogwaardig engineeringtalent in te zetten. Geleid door de filosofie van het combineren van "Nederlands management met Vietnamees meesterschap", heeft Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland**, aan de **Herengracht 420, 1017 BZ Amsterdam**, met meer dan 120 engineers verspreid over de drie kantoren. Via LaunchStudio krijgen AI-native oprichters direct toegang tot deze enterprise-grade software-expertise om hun prototypes binnen 1 tot 3 weken veilig, schaalbaar en lanceringsklaar te maken, tegen ongeveer 20% van de kosten van een traditioneel bureau. Lees meer over [Manifera's maatwerk softwareontwikkelingsdiensten](https://www.manifera.com/services/custom-software-development/). [Vraag vandaag nog een vrijblijvende offerte aan](https://launchstudio.eu/en/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Design Tokens Inrichten voor een Sales CRM

Sadie, een retailcoördinator, gebruikte **Lovable** om een CRM te bouwen. Ze had moeite om consistente lay-out- en spatiëringsspecificaties aan de AI over te brengen, omdat de tool bij elke prompt componenten met net iets andere stijlen regenereerde, waardoor het product er van scherm tot scherm onsamenhangend en ongepolijst uitzag.

Ze ging een partnerschap aan met **LaunchStudio (door Manifera)** om een gestructureerd design-tokensysteem en een bibliotheek met herbruikbare componenten op te zetten. Hierdoor kreeg de AI een vaste set bouwstenen om vanuit te werken, in plaats van elke keer stijlen vanaf nul opnieuw te genereren.

**Resultaat:** De verfijnde workflow verkortte de iteratiecycli tijdens het prototypen met 60%.

**Kosten & Tijdlijn:** €1.100 (Design Token Setup) — productieklaar en binnen 3 werkdagen live opgeleverd.

---

## Veelgestelde Vragen

### Waarom schieten traditionele Product Management frameworks tekort bij AI-producten?

Traditioneel productmanagement vertrouwt op voorspelbaar, deterministisch softwaregedrag. AI is daarentegen probabilistisch — het kan hallucineren of plausibel klinkende maar onjuiste antwoorden verzinnen. Je kunt geen traditionele, statische "user story" schrijven voor een systeem waarvan de output van run tot run kan variëren.

### Wat is de primaire taak van een AI Product Manager?

Het definiëren van de "acceptabele foutmarge" voor elke specifieke use-case, aangezien die drempelwaarde per domein enorm verschilt, en het ontwerpen van UX-fallbacks — zoals Human-in-the-Loop controlepoorten — voor de momenten waarop de AI onvermijdelijk een fout maakt.

### Wat houdt 'Evaluation-Driven Development' (Evals) in?

In plaats van te vertrouwen op handmatige steekproeven, cureert de AI PM een groeiende database van honderden testprompts met ideale antwoorden. Telkens wanneer engineers de prompt, de architectuur of het onderliggende model wijzigen, wordt het systeem opnieuw getoetst aan deze evals om kwaliteitsregressies te detecteren voordat klanten ermee worden geconfronteerd.

### Moet een AI Product Manager kunnen programmeren?

Zij hoeven zelf geen productiecode te schrijven, maar moeten de architectuur wel door en door begrijpen — het praktische verschil tussen RAG en fine-tuning, hoe token-limieten en latentie in de praktijk werken, en waar prompt-injectierisico's zich in het productoppervlak bevinden.

### Hoe helpt LaunchStudio, als onderdeel van Manifera, AI-productteams om verantwoord te lanceren?

LaunchStudio is een initiatief van Manifera, opgericht in 2014 en met het hoofdkantoor in Amsterdam. Onze engineers helpen AI-native teams om een veelbelovend Lovable-, Bolt- of Cursor-prototype om te vormen tot een volwaardig product met de beveiligingsarchitectuur, menselijke controlepoorten en databasestructuur die een AI PM nodig heeft om met vertrouwen live te gaan — doorgaans binnen 1 tot 3 weken. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom schieten traditionele Product Management frameworks tekort bij AI-producten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Traditioneel productmanagement vertrouwt op voorspelbaar, deterministisch softwaregedrag. AI is daarentegen probabilistisch — het kan hallucineren of plausibel klinkende maar onjuiste antwoorden verzinnen. Je kunt geen traditionele, statische user story schrijven voor een systeem waarvan de output varieert."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de primaire taak van een AI Product Manager?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het definiëren van de acceptabele foutmarge voor elke specifieke use-case en het ontwerpen van UX-fallbacks, zoals Human-in-the-Loop controlepoorten, voor wanneer de AI onvermijdelijk fouten maakt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat houdt 'Evaluation-Driven Development' (Evals) in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In plaats van handmatige steekproeven cureert de AI PM een database van honderden testprompts met ideale antwoorden om model-, prompt- en architectuurwijzigingen geautomatiseerd te benchmarken op kwaliteitsregressies."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een AI Product Manager kunnen programmeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet noodzakelijk productiecode schrijven, maar wel een diepgaand begrip hebben van RAG versus fine-tuning, token-limieten, latentie en prompt-injectiebeveiliging."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt LaunchStudio, als onderdeel van Manifera, AI-productteams om verantwoord te lanceren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio (onderdeel van Manifera, opgericht in 2014 te Amsterdam) helpt AI-native teams prototypes van Lovable, Bolt of Cursor te voorzien van enterprise-grade beveiliging, databasemodellering en Human-in-the-Loop interfaces binnen 1 tot 3 weken."
      }
    }
  ]
}
</script>
