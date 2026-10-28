---
Titel: "Lovable Supabase: Verbindingslimieten en Pooling bij Echt Verkeer"
Trefwoorden: lovable supabase, connection pooling, pgbouncer, serverless verbindingen, too many clients, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Verbindingslimieten en Pooling bij Echt Verkeer

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Verbindingslimieten en Pooling bij Echt Verkeer",
  "description": "\"Too many clients already\" is wat een door AI gebouwde app zegt wanneer ze succes heeft. Waarom serverless functies Postgres-verbindingen uitputten, wat de pooler doet, en welke connection string waar hoort.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-connection-limits-and-pooling-at-real-traffic" }
}
</script>

De foutmelding komt zonder waarschuwing en meestal op het best denkbare moment voor uw bedrijf en het slechtste voor u: *sorry, too many clients already*. Uw product stopt. Er is niets kapot, er is niets uitgerold, en over tien minuten werkt het misschien gewoon weer.

Wat er gebeurde, is dat meer onderdelen van uw applicatie de database om een verbinding vroegen dan de database wilde geven. Postgres heeft geen onbeperkt aantal verbindingen - elke verbinding kost echt geheugen - en een klein Supabase-plan staat er veel minder toe dan oprichters aannemen. Zestig is een gebruikelijk getal. Sommige plannen staan er vijftien toe.

Vijftien klinkt piepklein totdat u beseft dat het geen vijftien gebruikers zijn. Het zijn vijftien gelijktijdige gesprekken met de database, waarmee een goed werkende applicatie honderden gebruikers kan bedienen, en die een serverless applicatie met negen mensen kan uitputten.

## Waarom Serverless Dit Erger Maakt

Een traditionele server start één keer, opent een handvol verbindingen, en hergebruikt die maandenlang voor elk verzoek. Dat is de opzet waarvoor Postgres is ontworpen.

Serverless functies - Vercel-functies, Supabase edge functions, Netlify-functies, het standaarddoel voor de deployment van bijna elke door AI gebouwde app - werken andersom. Elke aanroep kan een nieuwe instantie zijn zonder geheugen van de vorige. Opent elke aanroep een eigen verbinding, dan betekenen honderd gelijktijdige verzoeken honderd verbindingen, en de database weigert ergens rond nummer zestien.

Erger nog: een instantie die klaar is met haar werk, sluit de verbinding niet per se direct. Verbindingen blijven hangen, inactief, en houden een plek bezet die niets gebruikt. Het is goed mogelijk uw limiet uit te putten met vrijwel geen verkeer, puur door opstapeling.

Dit is geen fout in serverless. Het is een mismatch tussen twee modellen, en de brug ertussen is een pooler.

## Wat de Pooler Doet

Een connection pooler zit tussen uw applicatie en Postgres. Uw functies verbinden ermee, hij onderhoudt een klein aantal echte verbindingen met de database, en hij deelt ze uit voor de duur van een statement of een transactie in plaats van voor de levensduur van een client.

Omdat de meeste verzoeken hun verbinding een paar milliseconden gebruiken en de rest van hun bestaan met andere dingen bezig zijn, kan een handvol echte verbindingen een heel groot aantal applicatie-instanties bedienen.

Supabase biedt dit, en het praktische gevolg is dat uw applicatie twee connection strings tot haar beschikking heeft die niet uitwisselbaar zijn. Er is een directe verbinding met de database, en een gepoolde verbinding op een andere poort met ander gedrag. De verkeerde gebruiken is de meest voorkomende oorzaak van deze hele categorie problemen.

## Welke Connection String Waar Hoort

De regel is kort en het waard om op te schrijven op een plek waar uw toekomstige zelf hem vindt.

**Applicatiecode, vooral serverless, gebruikt de gepoolde verbinding.** Alles wat verzoeken van gebruikers bedient. Dit is de standaard, en onthoudt u maar één ding, onthoud dan dit.

**Migraties en schemawijzigingen gebruiken de directe verbinding.** Gepoolde verbindingen in transactiemodus ondersteunen niet alles - prepared statements gedragen zich anders, instellingen op sessieniveau blijven niet bewaard, en sommige schemahandelingen mislukken op verwarrende wijze.

**Langlopende achtergrondtaken en alles wat een transactie openhoudt, gebruiken de directe verbinding**, spaarzaam, omdat ze gedurende hun hele looptijd een echte plek bezetten.

Twee gewoontes voorkomen de fouten die overblijven. Houd nooit een databasetransactie open tijdens een aanroep naar een externe dienst - een webhook, een model-API, een e-mailprovider - want dat bezet een verbinding zolang de storing van een ander duurt. En zorg dat uw clientbibliotheek is ingesteld met een verstandige poolgrootte per instantie in plaats van de standaard van de bibliotheek, die vaak veel te royaal is voor een omgeving waarin tientallen instanties tegelijk bestaan.

## Het Diagnosticeren Wanneer Het Gebeurt

Wanneer de foutmelding verschijnt, vertellen drie dingen u wat er aan de hand is, en ze zijn allemaal beschikbaar in het Supabase-dashboard.

Het huidige aantal verbindingen tegenover de limiet van uw plan, wat de diagnose bevestigt. De uitsplitsing van wat die verbindingen doen - een groot aantal dat "idle in transaction" staat, is een specifieke en oplosbare fout, namelijk code die een transactie opende en iets traags deed voordat ze werd vastgelegd. En of het aantal gestaag groeit over uren in plaats van te pieken met het verkeer, wat wijst op gelekte verbindingen in plaats van echte belasting.

Een lek ziet er zo uit: het aantal verbindingen loopt langzaam op vanaf het moment van deployen totdat het het plafond raakt, ongeacht hoeveel gebruikers actief zijn. Het is bijna altijd een client die binnen een request handler wordt aangemaakt in plaats van één keer op moduleniveau, zodat elke aanroep er weer een maakt en niets ooit opruimt.

## De Oplossing Die Geen Upgrade Is

De neiging bij het raken van een limiet is een groter plan te kopen, en dat verhoogt het plafond inderdaad.

Het kost ook elke maand geld om een fout te omzeilen die in een uur te verhelpen is, en het stelt de diagnose uit in plaats van haar weg te nemen - een lek dat drie dagen nodig had om zestig verbindingen te vullen, heeft twaalf dagen nodig om er tweehonderdveertig te vullen, en het gebeurt nog steeds op de drukste ochtend van uw jaar.

Repareer eerst de code: gepoolde verbindingen overal waar ze horen, clientinstanties één keer aangemaakt, transacties kort gehouden, geen externe aanroepen erbinnen. Upgrade daarna als uw verkeer dat echt rechtvaardigt. De meeste producten in dit stadium ontdekken dat de juiste configuratie meerdere keren hun huidige belasting aankan op het plan dat ze al hebben.

## Realtime en Zijn Eigen Limieten

Gebruikt uw product Supabase realtime voor live updates, dan heeft dat aparte limieten - gelijktijdige verbindingen en berichten per seconde - en die worden uitgeput door een ander patroon.

De gebruikelijke oorzaak is een abonnement dat bij elke render wordt aangemaakt in plaats van één keer, zodat een gebruiker met een pagina die een uur openstaat abonnementen opstapelt totdat er iets bezwijkt. Het symptoom is één zware gebruiker die iedereen raakt, en het is onzichtbaar tijdens het testen, omdat één developer die een pagina ververst nooit genoeg opstapelt.

Abonneer één keer, zeg het abonnement op wanneer het component verdwijnt, en tel uw actieve abonnementen op een plek waar u ze kunt zien. Hetzelfde geldt voor elke langlopende verbinding die uw product opent: de vraag is nooit of het werkt, maar wat er na vier uur gebeurt.

## Doe een Belastingtest Vóór de Campagne, Niet Erna

Alles hierboven is vooraf te weten voor de prijs van een middag.

Richt een belastingtesttool op de drukste pagina van uw product, met realistische authenticatie, en draai op twee of drie keer de gelijktijdigheid die u verwacht. Kijk tegelijk naar het aantal verbindingen, het foutpercentage en de responstijd. De faalwijze die u zoekt, is geen traagheid - het is de afgrond, waarbij alles goed gaat bij dertig gelijktijdige gebruikers en niets meer werkt bij veertig.

Doe dit vóór een lancering, een campagne, een vermelding in de pers of een seizoenspiek, want anders vinden echte gebruikers de afgrond altijd, en altijd op het moment dat het verkeer het meest waard was.

## Waar de Time-outs Vandaan Komen

Uitgeputte verbindingen hebben een stillere neef die dezelfde klantervaring oplevert om een andere reden: verbindingen die beschikbaar zijn maar te lang worden vastgehouden.

Postgres heeft instellingen die dit regelen, en de standaardwaarden op een gehost plan zijn toegeeflijker dan ze voor een klein product zouden moeten zijn. Een statement timeout begrenst hoe lang één query mag draaien voordat hij wordt geannuleerd, wat een op hol geslagen rapport verandert in één mislukt verzoek in plaats van een database waar iedereen achter in de rij staat. Een idle-in-transaction timeout sluit verbindingen waar iets een transactie opende en vervolgens wegdwaalde, wat precies is wat een gecrashte functie-instantie achterlaat.

Beide instellen is een wijziging van vijf minuten met een groot effect op hoe uw product faalt. Zonder die instellingen verslechtert één slecht geschreven query op de ongewoon grote dataset van één klant de ervaring van elke andere klant, omdat hij een verbinding en de bijbehorende locks bezet houdt terwijl hij werkt.

Kies de getallen bewust in plaats van royaal: een paar seconden voor gewone applicatiequeries, langer voor een bewust aparte rol die voor rapporten en exports wordt gebruikt. Het gaat er niet om streng te zijn. Het gaat erom dat een query die al dertig seconden draait op een scherm waar een mens op wacht, al mislukt is, en hem laten doorlopen verspreidt de mislukking alleen.

## Dit Inrichten

Voor een bestaande app kost dit meestal een halve tot een hele dag: connection strings gecontroleerd zodat applicatiecode de pooler gebruikt en migraties de directe verbinding, databaseclients één keer per instantie aangemaakt in plaats van per verzoek, de poolgrootte bewust ingesteld, transacties gecontroleerd op externe aanroepen en lange handelingen, realtime-abonnementen gecontroleerd op opstapeling, verbindingsstatistieken gevolgd met een melding vóór het plafond in plaats van erop, en een belastingtest op meerdere keren de verwachte gelijktijdigheid om de afgrond te vinden zolang dat nog goedkoop is.

LaunchStudio doet dit als onderdeel van productieklaar maken - het is een van de weinige problemen die pas opduiken wanneer een product werkt, wat het een bijzonder onwelkome verrassing maakt. De engineers zijn van Manifera: elf jaar, 160+ projecten, en heel veel Postgres onder belasting, vanuit Amsterdam en Ho Chi Minh-stad.

[Vertel ons uw verwachte piek](https://launchstudio.eu/nl/#contact) en wij vertellen u of uw huidige opzet die overleeft.

## Echt voorbeeld

### Negen Gebruikers en een Kapot Product

Thijs Kranenburg bouwde Zaalplanner in Lovable: reserveringssoftware voor buurthuizen en dorpshuizen, 48 locaties in Friesland en Groningen, elk met een handvol medewerkers.

Het product ging elke maandagochtend kapot. Niet langzaam - volledig, met databasefouten op elke pagina, tien tot twintig minuten lang, en daarna herstel zonder ingrijpen. Maandagochtend is wanneer beheerders de boekingen voor de week doen, dus het was het slechtst denkbare tijdvak en de reden dat twee locaties al naar alternatieven hadden gevraagd.

Zijn Supabase-plan stond 60 verbindingen toe. Zijn applicatie maakte een nieuwe databaseclient aan binnen elke aanroep van een serverless functie, dus elk verzoek opende een verbinding en liet die verlopen. De negen of tien gelijktijdige beheerders op maandag, die elk pagina's laadden met vier of vijf verzoeken, putten de limiet binnen minuten uit.

Eén werkdag: de databaseclient verplaatst naar moduleniveau, zodat elke functie-instantie één verbinding hergebruikt; elke connection string van de applicatie omgezet naar de gepoolde poort, met de directe verbinding gereserveerd voor migraties; de poolgrootte expliciet ingesteld in plaats van op de standaard van de bibliotheek gelaten; twee transacties die een e-mailaanroep omsloten verwijderd, aangezien één storing bij de provider verbindingen elk negentig seconden had opengehouden; een realtime-abonnement in de boekingskalender gerepareerd zodat het één keer abonneert in plaats van bij elke render; een dashboardmelding bij 70 procent van de verbindingslimiet; en een belastingtest met 120 gelijktijdige gebruikers om de oplossing te bevestigen in plaats van aan te nemen.

**Resultaat:** de maandagochtenden gingen niet meer mis. Het piekgebruik van verbindingen daalde van het plafond van 60 naar een stabiele 7, en de belastingtest haalde 120 gelijktijdige gebruikers - meer dan het dubbele van Thijs' realistische piek - op hetzelfde plan dat hij op het punt stond te upgraden voor €300 per maand.

> *"Ik was ervan overtuigd dat ik een grotere database nodig had. Het hele probleem was één regel op de verkeerde plek, die voor elk verzoek een verbinding maakte en die nooit teruggaf."*
> - **Thijs Kranenburg, Oprichter, Zaalplanner (Leeuwarden)**

**Kosten & Doorlooptijd:** €1.450 (controle van verbindingen en migratie naar de pooler, herstel van de levenscyclus van clients, herstel van transacties, herstel van realtime-abonnementen, meldingen, belastingtest) - afgerond in 1 werkdag.

## Veelgestelde vragen

### Wat betekent "too many clients already"?

Uw applicatie vroeg Postgres om meer gelijktijdige verbindingen dan uw plan toestaat. Het is bijna altijd een fout in de levenscyclus van verbindingen in plaats van echte belasting, vooral bij serverless deployments.

### Wanneer moet ik de gepoolde connection string gebruiken?

Voor alle applicatiecode, vooral serverless functies. Gebruik de directe verbinding alleen voor migraties, schemawijzigingen en langlopend achtergrondwerk.

### Lost een upgrade van mijn Supabase-plan het op?

Het verhoogt het plafond en stelt de diagnose uit. Een verbindingslek dat 60 plekken vult, vult er ook 240, alleen langzamer, en meestal op uw drukste dag. Repareer eerst de levenscyclus.

### Waarom loopt het aantal verbindingen op als niemand de app gebruikt?

Omdat iets per verzoek een client aanmaakt en die nooit sluit. Gestage groei vanaf het moment van deployen tot het plafond, onafhankelijk van verkeer, is het kenmerk van een lek.

### Hoe ken ik mijn limiet voordat ik hem raak?

Doe een belastingtest op twee of drie keer de verwachte gelijktijdigheid en kijk naar het aantal verbindingen naast de fouten. De mislukking is een afgrond in plaats van een geleidelijke vertraging, dus bij normaal gebruik ziet u haar niet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat betekent de foutmelding \"too many clients already\"?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uw app vroeg om meer gelijktijdige Postgres-verbindingen dan het plan toestaat - meestal een fout in de levenscyclus van verbindingen in serverless code in plaats van echte belasting."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet ik de gepoolde connection string van Supabase gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor alle applicatiecode, vooral serverless. Reserveer de directe verbinding voor migraties, schemawijzigingen en langlopende taken."
      }
    },
    {
      "@type": "Question",
      "name": "Lost een upgrade van het plan uitgeputte verbindingen op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het verhoogt het plafond zonder het lek te dichten, dat de grotere limiet alsnog vult - meestal op uw drukste dag."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom loopt het aantal verbindingen op als niemand de app gebruikt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Er wordt per verzoek een client aangemaakt die nooit wordt gesloten. Gestage groei vanaf het deployen, ongeacht het verkeer, is het kenmerk."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vind ik mijn gelijktijdigheidslimiet voordat klanten dat doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Doe een belastingtest op twee tot drie keer de verwachte piek en kijk naar het aantal verbindingen en de fouten. De mislukking is een afgrond, geen geleidelijke vertraging."
      }
    }
  ]
}
</script>
