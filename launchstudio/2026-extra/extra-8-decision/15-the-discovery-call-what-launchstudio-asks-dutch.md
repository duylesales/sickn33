---
Titel: "De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt Vóór We Offreren"
Trefwoorden: discovery call software, technisch intakegesprek, wat te verwachten intake developer, audit productiegereedheid vragen, proces backend audit, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt Vóór We Offreren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt Vóór We Offreren",
  "description": "Voordat we een vaste prijs en tijdlijn offreren, voert LaunchStudio een gestructureerd intakegesprek in plaats van een generieke salespitch. Een overzicht van wat we exact vragen, waarom elke vraag telt, en hoe een oprichter zich kan voorbereiden op een snelle, accurate offerte.",
  "inLanguage": "nl-NL",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/the-discovery-call-what-launchstudio-asks"
  }
}
</script>

"Ik verwachtte een glad verkooppraatje. Wat ik kreeg leek meer op een technisch interview — over mijn eigen product." Die reactie van een oprichtster over haar eerste gesprek met LaunchStudio is herkenbaar en volkomen bewust: een offerte met een vaste prijs en vaste tijdlijn voor het harden van een met AI gebouwd prototype is immers alleen betrouwbaar als deze is geworteld in een accuraat begrip van wat er daadwerkelijk in de codebase staat. Dat inzicht haalt u niet uit een oppervlakkig verkoopgesprek. Het vraagt om een gestructureerde 'discovery call' die specifiek is ontworpen om de concrete hiaten van een applicatie naar boven te halen vóórdat er ook maar één getal wordt genoemd. Begrijpen wat er tijdens dat gesprek aan bod komt — en waarom — helpt een oprichter om zich optimaal voor te bereiden en sneller een trefzekere offerte te ontvangen.

## Waarom het Gesprek Vóór de Offerte Komt, Niet Erna

Veel eerdere ervaringen van oprichters met bureaus of freelancers hebben hen geleerd direct vooraf prijzen te verwachten, soms zelfs vóórdat er een echt gesprek heeft plaatsgevonden — een vaste pakketprijs op een website, een uurtarieflijst, of een schatting op basis van een projectbeschrijving van één alinea. Die aanpak werkt prima voor herhaalbaar routinewerk, maar schiet tekort bij het productierijp maken van een prototype. De feitelijke scope van dat werk hangt immers volledig af van de specifieke staat van een unieke codebase, die enorm kan variëren tussen twee producten die in een korte samenvatting identiek klinken. Een discovery call dient om een gok te vervangen door een gedegen analyse. De offerte die daarop volgt is navenant betrouwbaarder: een getal dat gebaseerd is op wat een engineer daadwerkelijk in de code heeft aangetroffen, niet op een abstracte aanname.

## De Technische Vragen: In Kaart Brengen Wat Er Daadwerkelijk Staat

Het eerste deel van het gesprek richt zich op het verkrijgen van een helder technisch beeld van het bestaande prototype. Welke AI-tool is gebruikt — Lovable, Bolt, Cursor, v0 of een andere? Dit is relevant omdat elke tool karakteristieke patronen heeft in de manier waarop authenticatie, API-aanroepen en datatoegang worden opgebouwd. Weten welke tool is gebruikt, wijst direct uit waar we als eerste moeten kijken. Welke backend- of databaseservice is gekoppeld, en zijn Row-Level Security (RLS) of vergelijkbare toegangscontroles momenteel geconfigureerd? Dat is een gerichte vraag met een direct verifieerbaar antwoord dat een groot deel van de uiteindelijke scope bepaalt. Zijn er betalingen mee gemoeid? Zo ja, zijn de webhooks van Stripe of een andere provider al aangesloten en worden de cryptografische handtekeningen geverifieerd? En tot slot: heeft de oprichter het gedrag van de app ooit getest door de API rechtstreeks aan te roepen, buiten de frontend om? Die laatste vraag onthult vaak — soms voor het eerst — of authenticatie daadwerkelijk op de server wordt afgedwongen of louter cosmetisch aan de client-side bestaat.

## De Zakelijke Vragen: Bepalen Wat "Productieklaar" Hier Concreet Betekent

Technische scope alleen bepaalt de urgentie of prioriteit niet. Daarom richt het tweede deel van het gesprek zich op de zakelijke context achter het verzoek. Is er een concrete lanceerdatum, een investeerdersgesprek, een grote enterprise-deal of een inkoopdeadline die tijdsdruk veroorzaakt? Welk type gegevens verwerkt de app — persoonsgegevens, betaalinformatie, gezondheidsdata of niet-gevoelige data? Het antwoord hierop bepaalt welke kwetsbaarheden de allerhoogste prioriteit hebben om direct te dichten. Hoeveel gebruikers of welk volume wordt er bij de start verwacht? Een applicatie die begint met drie testklanten kent immers een ander risicoprofiel dan een consumentenapp die van de ene op de andere dag viraal kan gaan. Dit zijn geen beleefdheidsvragen; ze bepalen direct welke technische hiaten uit het eerste deel van het gesprek nú moeten worden opgelost voor deze specifieke lancering, en welke eventueel kunnen wachten.

## Waarom "Ik Weet Het Niet" Een Volstrekt Acceptabel, Zelfs Waardevol Antwoord Is

Oprichters maken zich soms zorgen dat het niet weten van het antwoord op een technische vraag een slechte indruk maakt of suggereert dat hun project achterloopt. Het tegendeel is waar: een oprichter die eerlijk zegt: "Ik weet niet of Row-Level Security is geconfigureerd, ik heb dat nooit gecontroleerd", geeft de engineer veel waardevollere informatie dan iemand die vol zelfvertrouwen een foutieve gok waagt. Een eerlijk "ik weet het niet" stimuleert de engineer namelijk om het direct zelf in de code te verifiëren, in plaats van een offerte te baseren op een aanname die later onjuist blijkt. Van niet-technische oprichters wordt niet verwacht dat zij backend-configuratiedetails uit hun hoofd kennen — dat is immers exact de expertise die zij inhuren. Het gesprek is zo opgezet dat een niet-technische oprichter moeiteloos kan antwoorden over het feitelijke gedrag van zijn product en de zakelijke context, terwijl de technische validatie rechtstreeks op de code plaatsvindt.

## Wat Er Gebeurt Tussen het Gesprek en de Offerte

Na de call en vóórdat er een vaste prijs en tijdlijn worden voorgelegd, inspecteert een engineer doorgaans de feitelijke codebase rechtstreeks. We vertrouwen niet uitsluitend op wat mondeling is besproken: de gerapporteerde technische staat en de werkelijke staat in de code lopen doorgaans net genoeg uiteen (zonder dat de oprichter daar iets aan kan doen) dat een betrouwbare offerte een echte blik op de code vereist. Deze stap zorgt ervoor dat de offerte die volgt standhoudt zodra het werk begint, in plaats van halverwege uit te lopen door een reeks onaangename verrassingen. Dit is een veelvoorkomend probleem bij ontwikkelaars die offreren op basis van alleen een praatje en de werkelijke omvang pas ontdekken als het project al loopt — waarna heronderhandelen voor de oprichter een uiterst nadelige positie oplevert.

## Hoe Lang het Gesprek Duurt en Wat U Moet Meenemen

Een oprichter die zich voorbereidt op een eerste gesprek overschat vaak hoeveel voorbereiding er nodig is. In de praktijk duurt het gesprek doorgaans dertig tot vijfenveertig minuten. Het meest waardevolle wat u kunt meebrengen is geen ingewikkeld technisch document, maar directe toegang: een werkende link naar de live testversie van de app en, indien mogelijk, leesrechten op de GitHub-repository of het project in de AI-tool, zodat de engineer direct kan meekijken. Sommige oprichters stellen vooraf een uitgebreide briefing op; dat is zelden nodig, omdat de vragen in het gesprek juist zijn ontworpen om op natuurlijke wijze te worden beantwoord. Eerlijk antwoorden — inclusief "ik weet het niet" — levert consistent een beter en sneller resultaat op dan gissingen die worden verpakt als feiten. De engineer is getraind om de juiste informatie via gerichte vragen boven tafel te krijgen, niet om u een cijfer te geven voor uw technische woordenschat.

[LaunchStudio](https://launchstudio.eu/nl/) hanteert dit discovery-proces voorafgaand aan elk traject, zodat de vaste prijs en tijdlijn die u ontvangt uw daadwerkelijke codebase weerspiegelen in plaats van een ruwe schatting — gebaseerd op Manifera's 11+ jaar ervaring in productie-engineering over een breed scala aan met AI gebouwde applicaties.

[Plan een intakegesprek in](https://launchstudio.eu/nl/#contact) en kom zoals u bent met wat u weet over uw stack — een onvolledig beeld is een uitstekend vertrekpunt.

## Echt voorbeeld
### Een AI-Native Oprichter in de Praktijk: Een Accurate Offerte Bij de Eerste Poging

Marieke Hendriks, oprichtster van PitchPrep (een met Bolt gebouwde tool waarmee startup-oprichters hun pitches kunnen oefenen met behulp van AI-feedback), had eerder een offerte gekregen van een freelance developer op basis van een e-mail van twee alinea's. Drie weken na de start van het project was de prijs al verdubbeld, nadat de freelancer ontdekte dat de authenticatielogica van PitchPrep veel ingewikkelder in elkaar stak dan de summiere omschrijving deed vermoeden.

Vastbesloten om die fout niet te herhalen, begon Marieke aan het intakegesprek met LaunchStudio met het vaste voornemen om gewoon "dat weet ik niet" te zeggen op technische vragen. Dat deed ze dan ook: ze wist niet of haar Supabase Row-Level Security correct was geconfigureerd, en ze had de API van PitchPrep nog nooit los van de gebruikersinterface getest.

**Resultaat:** De engineer verifieerde beide punten binnen twee dagen na de call rechtstreeks in de codebase. Hij constateerde dat RLS deels was ingericht, maar een kritiek lek bevatte op de tabel met pitch-opnames. LaunchStudio bracht een vaste offerte uit die tot en met de oplevering exact standhield, zonder enige verrassing in de scope.

> *"De vorige keer voelde 'ik weet het niet' als iets wat ik moest verbergen tijdens een verkoopgesprek. Ditmaal bleek het juist het meest nuttige antwoord te zijn dat ik kon geven."*  
> — **Marieke Hendriks, Founder, PitchPrep (Groningen)**

**Kosten & Tijdlijn:** €1.900 (Launch Ready Pakket, Row-Level Security herstel) — live in 9 werkdagen.

---

## Veelgestelde Vragen

### Moet ik mijn eigen codebase technisch doorgronden voordat ik een intakegesprek boek?

Nee — het gesprek is zo ingericht dat een niet-technische oprichter moeiteloos vragen kan beantwoorden over het functionele gedrag en de zakelijke context, terwijl de technische verificatie direct door een engineer op de code wordt uitgevoerd, precies zoals bij Marieke gebeurde.

### Waarom bekijkt LaunchStudio de codebase zelf in plaats van uitsluitend af te gaan op het gesprek?

Omdat de mondelinge beschrijving en de werkelijkheid in de code vaak van elkaar afwijken, zonder dat de oprichter dat beseft. Een offerte die puur op een gesprek is gebaseerd loopt halverwege het werk vaak uit, wat haaks staat op onze garantie van een vaste prijs.

### Wat als ik tijdens het gesprek het antwoord op een technische vraag echt niet weet?

Dat is een volkomen normaal en waardevol antwoord, geen alarmsignaal. Het vertelt de engineer precies waar hij zelf in de code op moet letten in plaats van te moeten varen op aannames, zoals bij Marieke's database-beveiliging.

### Hoeveel tijd zit er doorgaans tussen het intakegesprek en de definitieve offerte?

Meestal één tot enkele werkdagen. Dit geeft ons de tijd om het gesprek te analyseren en de codebase gericht door te lichten, afhankelijk van de omvang en complexiteit van het prototype.

### Heeft het eerlijk beantwoorden van zakelijke contextvragen invloed op de prijs?

Het beïnvloedt vooral de prioritering en de afbakening van de scope. Zaken zoals de gewenste lanceerdatum, datagevoeligheid en gebruikersaantallen bepalen welke technische hiaten absoluut vóór de lancering moeten worden opgelost en welke eventueel kunnen wachten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik mijn eigen codebase technisch doorgronden voordat ik een intakegesprek boek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het gesprek behandelt zakelijke doelen en werking van de app; de technische analyse van de code voert onze engineer zelfstandig uit."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom bekijkt LaunchStudio de codebase zelf in plaats van uitsluitend af te gaan op het gesprek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een mondelinge toelichting en echte code vaak verschillen. Een echte code-inspectie garandeert dat onze vaste prijs ook echt vast blijft."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als ik tijdens het gesprek het antwoord op een technische vraag echt niet weet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat is een waardevol antwoord; het geeft onze engineers aan waar ze tijdens de code-audit specifiek zelfstandig naar moeten kijken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel tijd zit er doorgaans tussen het intakegesprek en de definitieve offerte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gewoonlijk 1 tot enkele werkdagen, waarin we het gesprek verwerken en de codebase direct auditen om tot een scherpe vaste offerte te komen."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft het eerlijk beantwoorden van zakelijke contextvragen invloed op de prijs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het stuurt vooral de prioritering van risico's: het scheidt wat strikt noodzakelijk is voor uw specifieke lanceerdatum van wat later kan."
      }
    }
  ]
}
</script>
