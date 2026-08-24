---
Titel: "Launch & Grow vs. Relaunch & Scale: Het Juiste LaunchStudio-pakket Kiezen"
Keywords: Launch & Grow, Relaunch & Scale, AI SaaS pakketten, LaunchStudio prijzen, Row Level Security, database schaling, Stripe webhooks, LaunchStudio, Manifera, Cursor
Buyer Stage: Decision
---

# Launch & Grow vs. Relaunch & Scale: Het Juiste LaunchStudio-pakket Kiezen

Oprichters die LaunchStudio mailen, komen meestal aan met dezelfde onderliggende vraag, maar op twee heel verschillende manieren geformuleerd. Sommigen vragen: "Hoe zorg ik ervoor dat mijn AI-gebouwde app niet instort zodra ik live ga?" Anderen vragen: "Mijn app is al live en begint te haperen — hoe repareer ik dat zonder de gebruikers die ik al heb kwijt te raken?" Dit zijn niet dezelfde problemen, en ze als identiek behandelen is precies de manier waarop oprichters uiteindelijk betalen voor de verkeerde scope aan werk. LaunchStudio heeft twee afzonderlijke pakketten rond dit onderscheid gebouwd: **Launch & Grow** voor oprichters die zich voorbereiden op hun eerste echte lancering, en **Relaunch & Scale** voor oprichters die al gebruikers hebben en nu tegen de muur aanlopen die bij echt verkeer hoort. Dit artikel legt precies uit wat elk pakket bevat, hoe u kunt bepalen welk pakket u daadwerkelijk nodig heeft, en wat er gebeurt wanneer uw situatie — zoals bij veel oprichters — niet netjes in een van beide vakjes past.

## Twee Pakketten, Twee Heel Verschillende Startpunten

Het verschil tussen Launch & Grow en Relaunch & Scale gaat niet echt over de prijs, ook al zit Relaunch & Scale iets hoger in de schaal (ongeveer € 2.500–€ 4.500 tegenover € 1.500–€ 3.500). Het echte verschil is in welke staat uw app verkeert op het moment dat het engineeringteam de codebase opent.

Launch & Grow gaat uit van een codebase die nog nooit echte, betalende, gelijktijdige gebruikers heeft gehad. Het is een verhardingsronde vóór de lancering: de AI-builder — Lovable, Bolt, Cursor of vergelijkbaar — heeft een werkend prototype opgeleverd, maar niemand buiten een kleine groep testers heeft ooit op "betalen" geklikt of de database bestookt met gelijktijdige verzoeken. Het werk is preventief. Engineers dichten gaten voordat ze incidenten worden.

Relaunch & Scale gaat uit van het tegenovergestelde: een app die al voor echte gebruikers heeft gestaan en nu de specifieke symptomen van schaal vertoont — trage query's, timeouts onder gelijktijdige belasting, een database die prima werkte bij 20 gebruikers en omvalt bij 200. Het werk hier is diagnostisch en corrigerend. Engineers sporen het exacte knelpunt op dat al pijn veroorzaakt en verwijderen dat, vaak terwijl ze tegelijk beveiligingslekken dichten die de eerste keer nooit zijn aangepakt.

Beide pakketten raken uiteindelijk vergelijkbare categorieën werk — beveiliging, betalingen, infrastructuur — maar de startcondities, het diagnostische proces en de urgentie verschillen genoeg om ze niet als inwisselbaar te behandelen; dat kost aan beide kanten tijd en geld.

## De Zelfdiagnose: Heeft u al Gelanceerd?

Beantwoord deze vragen eerlijk voordat u een pakket kiest:

**Hebben echte gebruikers uw app al gebruikt — geen testers, geen medeoprichter, maar mensen die u organisch hebben gevonden of hebben betaald om erbij te zijn?** Zo niet, dan bent u vrijwel zeker een kandidaat voor Launch & Grow. Zo ja, ga verder.

**Is uw app op dit moment traag, valt hij weg door timeouts of geeft hij foutmeldingen bij normaal gebruik — geen randgevallen, maar dagelijkse belasting?** Zo ja, dan is dat een schaalprobleem, en dat wijst richting Relaunch & Scale.

**Weet u specifiek of uw Row Level Security-beleid is ingeschakeld en gekoppeld aan `auth.uid()` — geen "de AI heeft dat waarschijnlijk geregeld", maar een bevestigd ja?** De meeste oprichters antwoorden "ik weet het niet zeker", en dat is op zichzelf het antwoord: onopgeloste beveiligingslekken komen vaak voor aan beide kanten van een eerste lancering, en die moeten worden gedicht ongeacht welk pakket u kiest.

**Kampt u met prestatieproblemen bovenop beveiligingslekken, of is dit puur een verhardingsronde vóór de lancering zonder live verkeer?** Als het beide is — u heeft al gebruikers én u bent niet zeker over de beveiliging — dan bent u een kandidaat voor Relaunch & Scale, omdat dat pakket is gebouwd om samenlopende problemen aan te pakken, niet slechts één nette categorie werk.

**Is uw facturatie al live en verwerkt deze echte transacties, of zijn betalingen nog niet gekoppeld aan echte klanten?** Live facturatie onder echte belasting verandert het risicoprofiel aanzienlijk, en het is een van de duidelijkste signalen dat u van een lanceringsprobleem naar een schaalprobleem bent verschoven.

Als de meeste van uw antwoorden wijzen op "nog niet, nog in voorbereiding" — dan is Launch & Grow de juiste scope. Als de meeste wijzen op "ja, en nu breekt het" — dan is Relaunch & Scale de juiste scope.

## Wat Launch & Grow (€1.500–€3.500) Daadwerkelijk Bevat

Launch & Grow is gebouwd voor oprichters met een werkend, door AI gegenereerd prototype en een lanceringsdatum op de kalender, maar die het nog niet hebben blootgesteld aan echt, onvoorspelbaar verkeer. De scope omvat doorgaans:

- **Implementatie en verificatie van Row Level Security.** Engineers auditen elke tabel, bevestigen dat RLS niet alleen aanwezig is in het schema maar daadwerkelijk is ingeschakeld en gekoppeld aan de geauthenticeerde gebruiker, en dichten elk gat waar het ene account theoretisch de data van een ander account zou kunnen lezen.
- **Backend-betalingsinfrastructuur.** Als Stripe uitsluitend client-side is aangesloten — een veelvoorkomende standaardinstelling van AI-builders — vervangt het team dit door een ondertekende, server-side webhook-listener met idempotentie-afhandeling, zodat een weggevallen verbinding een betalende klant nooit kan scheiden van de toegang die hij heeft gekocht.
- **Beheer van geheimen en API-sleutels.** Elke sleutel die in client-side JavaScript staat (OpenAI-sleutels, Maps-sleutels, tokens van derden) wordt verplaatst naar veilige server-side functies, waar ze niet uit de dev-tools van een browser kunnen worden gescraped.
- **Monitoring en foutopsporing.** Sentry of een gelijkwaardig alternatief wordt gekoppeld aan zowel de frontend als de backend, zodat de eerste echte bug die een echte gebruiker tegenkomt een stacktrace en een melding oplevert, geen stille crash zonder uitleg.
- **Controles vóór lancering op belasting en beveiliging.** Een laatste ronde om te bevestigen dat de app zich correct gedraagt onder een realistisch verkeerspatroon van de eerste week, niet alleen in een demo met één gebruiker.

Wat Launch & Grow doorgaans *niet* bevat, is diepgaand databaseprestatiewerk — het afstemmen van indexen voor hoge queryvolumes, read replica's, connection pooling onder aanhoudende gelijktijdige belasting — omdat er in dit stadium nog geen echt verkeerspatroon is om tegen te optimaliseren. Dat werk hoort bij Relaunch & Scale.

## Wat Relaunch & Scale (€2.500–€4.500) Daadwerkelijk Bevat

Relaunch & Scale gaat uit van de aanname dat uw app al echte gebruikers heeft ontmoet, en dat een deel van die ontmoeting niet soepel is verlopen. De scope omvat doorgaans de volledige beveiligings- en betalingsbasis van Launch & Grow — omdat het vaak voorkomt dat die gaten de eerste keer nooit zijn gedicht — plus:

- **Query- en index-optimalisatie.** Engineers profileren uw traagste, meest aangeroepen query's en voegen de indexen toe, herstructureren de joins of elimineren de N+1-patronen die AI-builders vaak genereren.
- **Connection pooling.** Databaseverbindingen worden correct gepoold, zodat gelijktijdige verzoeken niet langer strijden om dezelfde vergrendelingen — een veelvoorkomende oorzaak van timeouts zodra er echt gelijktijdig verkeer arriveert.
- **Read replica's en verdeling van belasting**, waar het verkeerspatroon dit rechtvaardigt, zodat leesintensieve bewerkingen niet langer concurreren met schrijfintensieve bewerkingen op dezelfde database-instantie.
- **Herstel van RLS en beveiliging**, waarbij eventuele gaten van vóór de herlancering worden gedicht — een stap die extra belangrijk is omdat een beveiligingsincident tijdens een herlancering, voor gebruikers die uw product al kennen, meer merkschade aanricht dan hetzelfde incident op dag één.
- **Een communicatie- en rolloutplan voor de herlancering**, inclusief hoe u bestaande gebruikers informeert over de verbeteringen zonder ze ongerust te maken over wat er eerder kapot was.

Het kernonderscheid: Launch & Grow bereidt een app voor op het eerste echte contact met gebruikers. Relaunch & Scale herstelt en verhardt een app die dat contact al heeft gehad en het volgende contact met vertrouwen moet overleven.

## Naast Elkaar Vergeleken

| | Launch & Grow | Relaunch & Scale |
|---|---|---|
| **Prijsbereik** | € 1.500–€ 3.500 | € 2.500–€ 4.500 |
| **Typisch startpunt** | Prototype vóór lancering, nog geen echte gebruikers | Al gelanceerd, echte gebruikers stuiten op echte limieten |
| **Belangrijkste focus** | Beveiliging en betalingsverharding vóór de livegang | Prestaties, schaling en herstel na de livegang |
| **RLS-werk** | Implementatie en verificatie | Audit en herstel van gaten na de lancering |
| **Betalingen** | Opbouw van backend-webhook | Opbouw van backend-webhook plus getest onder belasting |
| **Databasewerk** | Basisbeoordeling van de structuur | Query-optimalisatie, indexering, pooling, replica's |
| **Doorlooptijd** | Doorgaans 5–10 werkdagen | Doorgaans 8–14 werkdagen |
| **Best geschikt voor** | Oprichters die voor het eerst gaan lanceren | Oprichters met bestaande gebruikers en zichtbare prestatieproblemen |

## Wat als u Beide Nodig Heeft?

Veel oprichters passen niet netjes in een van beide vakjes — ze hebben technisch gezien wel gelanceerd, maar alleen naar een kleine betagroep, en ze weten niet zeker of hun echte probleem beveiliging, schaal of beide is. Dit komt vaak genoeg voor dat het daadwerkelijke proces van LaunchStudio begint met een scopinggesprek voordat een pakket wordt vastgelegd. Als een app zowel onopgeloste RLS-gaten van vóór de lancering heeft als duidelijke schaalsymptomen zodra echte gebruikers arriveren, is Relaunch & Scale meestal de juiste keuze, omdat het pakket is gebouwd om beide categorieën werk in één traject op te vangen, in plaats van een oprichter te dwingen twee afzonderlijke rondes te kopen.

Het doel van het duidelijk benoemen van deze pakketten is niet om oprichters in een rigide menu te dwingen — het is om ervoor te zorgen dat het gesprek begint met een accurate diagnose van de daadwerkelijke staat van de app, in plaats van een generiek verzoek om "mijn app te verharden" dat van alles kan betekenen, van een reparatie van twee dagen tot een rebuild van drie weken.

## Belangrijkste inzichten

- Launch & Grow is voor verharding vóór de lancering: uw app heeft nog geen echte, gelijktijdige, betalende gebruikers gehad, en het werk is preventief — beveiliging, betalingen, monitoring.

- Relaunch & Scale is voor apps die al zijn gelanceerd en nu prestatiesymptomen vertonen — trage query's, timeouts, druk op de database — vaak samen met onopgeloste beveiligingsgaten van daarvoor.

- De duidelijkste zelfdiagnosevraag is eenvoudig: hebben echte gebruikers uw app al gebruikt, en is deze momenteel traag of kapot onder normale belasting? Als het antwoord op beide ja is, heeft u Relaunch & Scale nodig.

- Relaunch & Scale neemt doorgaans de volledige beveiligings- en betalingsscope van Launch & Grow over, plus databaseprestatiewerk, omdat beveiligingsgaten en schaalproblemen vaak samen voorkomen bij apps die zonder verhardingsronde zijn gelanceerd.

- Het verkeerde pakket kiezen kost tijd aan beide kanten — een scopinggesprek vóór de opdracht zorgt ervoor dat het engineeringwerk aansluit bij de daadwerkelijke staat van de codebase, niet bij een gok.

## Nog niet Zeker Welk Pakket bij uw App Past?

Of u zich nu voorbereidt op een eerste lancering of probeert een app te stabiliseren die al live is, gokken naar de juiste scope van werk kost u tijd die u niet heeft.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), ondersteund door meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio nemen senior engineeringteams uw bestaande, door AI gebouwde frontend — of deze nu nog vóór de lancering staat of al live is en onder druk staat — en implementeren ze productieklare beveiliging, live betalingsgateways, databaseprestatiewerk en monitoring, zonder een rebuild. [Vraag vandaag nog een gratis offerte en pakketadvies aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening scoping aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: B2B-logistiek-offerteplatform

Ravi Deshmukh bouwde een B2B-logistiek-offerte-SaaS-prototype met **Cursor**, gericht op vrachtmakelaars die snel en nauwkeurig verzendoffertes nodig hadden zonder handmatig spreadsheetwerk. Hij lanceerde het zelf, wist binnen enkele weken zijn eerste 200 gebruikers te bereiken en de zaken zagen er veelbelovend uit — totdat de app tijdens piekuren voor offertes begon vast te lopen door timeouts, precies wanneer makelaars het meest van de app afhankelijk waren.

Toen Ravi contact opnam met LaunchStudio, bracht het scopinggesprek twee overlappende problemen aan het licht: het prestatieprobleem was reëel en urgent, maar een beoordeling van zijn Supabase-opzet onthulde ook Row Level Security-gaten die al onopgelost waren sinds vóór zijn oorspronkelijke lancering — sommige tabellen waren technisch nog steeds leesbaar over accounts heen. Omdat hij zowel schaalwerk als onopgeloste beveiligingsverharding nodig had, adviseerde LaunchStudio **Relaunch & Scale** boven Launch & Grow, aangezien een pure prestatieronde de beveiligingsgaten onaangeroerd zou hebben gelaten.

Engineers voegden correcte connection pooling toe, herschreven en indexeerden zijn traagste offertequery's, en dichtten de RLS-gaten zodat de vrachtdata van elk account strikt geïsoleerd was op databaseniveau. De herlancering werd gepland met een kort onderhoudsvenster en een directe e-mail naar Ravi's bestaande 200 gebruikers waarin de verbeteringen werden uitgelegd.

**Resultaat:** De gemiddelde responstijd van de offerte-engine daalde van ongeveer 6 seconden naar minder dan 400 milliseconden, en Ravi behield 95% van zijn bestaande gebruikersbestand tijdens de herlancering, waarbij makelaars meldden dat de app tijdens piekuren eindelijk betrouwbaar aanvoelde.

**Kosten & Doorlooptijd:** € 3.300 (Relaunch & Scale) — 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Hoe weet ik of ik Launch & Grow of Relaunch & Scale nodig heb?

Vraag uzelf af of echte gebruikers uw app al onder normaal verkeer hebben gebruikt. Als uw app nog geen echte, gelijktijdige gebruikers heeft gehad en u zich voorbereidt op een eerste lancering, is Launch & Grow de juiste scope. Als uw app al live is en symptomen vertoont zoals trage query's, timeouts of druk op de database, is Relaunch & Scale de juiste scope, vooral als u ook niet zeker weet of Row Level Security ooit volledig is afgedicht.

### Kan ik beginnen met Launch & Grow en later upgraden naar Relaunch & Scale?

Ja. Veel oprichters beginnen met Launch & Grow vóór hun eerste lancering, en als er later schaalproblemen optreden naarmate het echte verkeer toeneemt, pakt een vervolgtraject van Relaunch & Scale de nieuwe prestatiesymptomen aan zonder het reeds voltooide beveiligings- en betalingswerk te herhalen.

### Bevat Relaunch & Scale ook beveiligingswerk, of alleen prestatiewerk?

Het bevat beide. In de praktijk hebben apps die het punt bereiken waarop een herlancering nodig is, vaak nog onopgeloste beveiligingsgaten van vóór hun eerste lancering, dus Relaunch & Scale is opgezet om RLS-audits, betrouwbaarheid van betalingen en databaseprestatiewerk gezamenlijk te dekken, in plaats van oprichters te dwingen tot twee afzonderlijke trajecten.

### Wat als ik niet zeker weet in welke categorie mijn problemen vallen?

Dat is normaal, en daar dient het scopinggesprek vóór elk traject precies voor. De engineers van LaunchStudio beoordelen uw bestaande codebase, bepalen of de problemen preventief werk vóór de lancering zijn of herstelwerk na de lancering, en adviseren het pakket dat past bij de daadwerkelijke staat van uw app in plaats van bij een generiek verzoek.

### Moet mijn bestaande frontend voor een van beide pakketten opnieuw worden gebouwd?

Nee. Zowel Launch & Grow als Relaunch & Scale werken binnen uw bestaande, door AI-builder gegenereerde frontend — van tools zoals Lovable, Bolt of Cursor — en verharden de backend, beveiliging, betalingen en infrastructuur eronder, zonder de UI die u al heeft aan te raken of opnieuw te bouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe weet ik of ik Launch & Grow of Relaunch & Scale nodig heb?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag uzelf af of echte gebruikers uw app al onder normaal verkeer hebben gebruikt. Als uw app nog geen echte, gelijktijdige gebruikers heeft gehad en u zich voorbereidt op een eerste lancering, is Launch & Grow de juiste scope. Als uw app al live is en symptomen vertoont zoals trage query's, timeouts of druk op de database, is Relaunch & Scale de juiste scope, vooral als u ook niet zeker weet of Row Level Security ooit volledig is afgedicht."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik beginnen met Launch & Grow en later upgraden naar Relaunch & Scale?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Veel oprichters beginnen met Launch & Grow vóór hun eerste lancering, en als er later schaalproblemen optreden naarmate het echte verkeer toeneemt, pakt een vervolgtraject van Relaunch & Scale de nieuwe prestatiesymptomen aan zonder het reeds voltooide beveiligings- en betalingswerk te herhalen."
      }
    },
    {
      "@type": "Question",
      "name": "Bevat Relaunch & Scale ook beveiligingswerk, of alleen prestatiewerk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het bevat beide. In de praktijk hebben apps die het punt bereiken waarop een herlancering nodig is, vaak nog onopgeloste beveiligingsgaten van vóór hun eerste lancering, dus Relaunch & Scale is opgezet om RLS-audits, betrouwbaarheid van betalingen en databaseprestatiewerk gezamenlijk te dekken, in plaats van oprichters te dwingen tot twee afzonderlijke trajecten."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als ik niet zeker weet in welke categorie mijn problemen vallen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat is normaal, en daar dient het scopinggesprek vóór elk traject precies voor. De engineers van LaunchStudio beoordelen uw bestaande codebase, bepalen of de problemen preventief werk vóór de lancering zijn of herstelwerk na de lancering, en adviseren het pakket dat past bij de daadwerkelijke staat van uw app in plaats van bij een generiek verzoek."
      }
    },
    {
      "@type": "Question",
      "name": "Moet mijn bestaande frontend voor een van beide pakketten opnieuw worden gebouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Zowel Launch & Grow als Relaunch & Scale werken binnen uw bestaande, door AI-builder gegenereerde frontend — van tools zoals Lovable, Bolt of Cursor — en verharden de backend, beveiliging, betalingen en infrastructuur eronder, zonder de UI die u al heeft aan te raken of opnieuw te bouwen."
      }
    }
  ]
}
</script>
