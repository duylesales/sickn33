---
Titel: "Zelf Uw Product Testen Vóór de Lancering: Een Script voor Niet-Technische Oprichters"
Trefwoorden: software testen voor lancering, acceptatietest checklist oprichter, Stripe testkaarten, wachtwoordherstel testen, data isolatie multi-tenant controle, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Zelf Uw Product Testen Vóór de Lancering: Een Script voor Niet-Technische Oprichters

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Zelf Uw Product Testen Vóór de Lancering: Een Script voor Niet-Technische Oprichters",
  "description": "Een niet-technische oprichter kan in circa negentig minuten een uiterst waardevolle pre-launch testronde uitvoeren zonder ook maar één regel code te schrijven. Dit is het exacte script: registratie, betaling, weigering, terugbetaling, wachtwoordherstel en de cruciale multi-tenant controle.",
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
  "datePublished": "2027-01-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/testing-your-own-product-before-launch-a-founders-script"
  }
}
</script>

Onder niet-technische oprichters heerst vaak de geruststellende overtuiging dat testen uitsluitend de taak van de ontwikkelaar is, en dat een oprichter die zelf door het product klikt op zijn best overbodig en op zijn slechtst hinderlijk is. Dat klinkt als respect voor vakmanschap. In werkelijkheid is het een fundamenteel misverstand over het doel van testen.

Uw softwareontwikkelaar test of de code doet wat hij of zij heeft gebouwd. U test of het product doet wat een echt mens in de praktijk nodig heeft — en die twee zaken lopen voortdurend uiteen. De ontwikkelaar is immers nooit uw klant geweest en zal dat ook nooit worden. De testronde van de oprichter legt een geheel andere categorie fouten bloot: de bevestigingsmail die in het Nederlands arriveert terwijl de interface Engelstalig is, de opzeggingsprocedure die technisch slaagt maar de gebruiker achterlaat op een leeg wit scherm, of het tweede account dat via een vergeten pagina de privégegevens van het eerste account kan inzien. Geen van deze zaken komt naar voren in de geautomatiseerde unittests van een engineer, maar ze vallen direct op tijdens uw eigen testronde.

Het onderstaande protocol kost ongeveer negentig minuten, vereist geen enkele technische voorkennis en dient vóór de livegang op de staging-omgeving te worden doorlopen en direct na de lancering nogmaals op productie. Voer dit één keer grondig uit en u zult zich nooit meer een hulpeloze toeschouwer voelen bij uw eigen softwarelancering.

## Vóór U Begint: De Tien Minuten Voorbereiding

Zorg dat u eerst vijf praktische zaken klaarzet. Midden in de sessie moeten improviseren is namelijk de voornaamste reden waarom oprichters halverwege afhaken.

**Twee afzonderlijke e-mailadressen waar u daadwerkelijk toegang toe heeft.** Als u Gmail gebruikt, biedt 'plus-addressing' oneindig veel adressen: `uwbedrijf+testA@gmail.com` en `uwbedrijf+testB@gmail.com` komen beide in dezelfde inbox terecht, maar gelden binnen uw applicatie als volstrekt unieke gebruikers. U heeft er minimaal twee nodig omdat de helft van uw test draait om de vraag of gebruikersdata strikt gescheiden blijft.

**Twee browservensters die elkaars sessies niet kennen.** Eén normaal venster voor Account A en één privé-/incognitovenster voor Account B. Sessiecookies lekken niet tussen deze vensters over, waardoor u gelijktijdig twee verschillende personen kunt simuleren. Dit specifieke detail maakt het testen van datalekken tussen gebruikers mogelijk zonder dat u een tweede laptop nodig heeft.

**Uw smartphone, verbonden via 4G/5G in plaats van kantoor-wifi.** Meer dan de helft van uw eerste bezoekers gebruikt een mobiele telefoon. Mobiele data legt problemen bloot die u op een desktopverbinding nooit ziet: statische bestanden die per ongeluk alleen op uw lokale netwerk bereikbaar zijn, vertragingen bij wisselend bereik en velden waar de mobiele toetsenbord-autofill vreemd op reageert.

**Testcreditcards.** In de testmodus van Stripe slaagt `4242 4242 4242 4242` altijd met elke toekomstige verloopdatum en willekeurige CVC; `4000 0000 0000 0002` wordt gegarandeerd geweigerd; `4000 0025 0000 3155` dwingt een 3D Secure-verificatiestap af — een authenticatie die Europese kaarten onder de SCA-richtlijnen standaard moeten doorlopen. Mollie beschikt over een vergelijkbare testomgeving waarin u het gewenste resultaat handmatig selecteert. Vraag uw ontwikkelaar expliciet te bevestigen dat de applicatie in de testmodus staat voordat u start, zodat u geen reële transacties uitvoert.

**Eén notitiedocument met een kolom voor tijdstempels.** Noteer bij elke bevinding de exacte tijd. Wanneer uw engineer later de serverlogs analyseert, is "16:42 uur, op Betalen geklikt, laadicoon bleef oneindig draaien" tien keer waardevoller dan "de betaling werkte gisteren niet".

## Test Eén: Registratie, Inclusief de Drie Scenario's Die Moeten Mislukken

Maak een account aan als Account A, exact zoals een willekeurige vreemdeling dat zou doen — gebruik geen vooraf ingevulde wachtwoorden van uw browser, sla geen optionele velden over en kies niet automatisch het pad waarvan u weet dat het storingsvrij werkt.

Vervolgens breekt u het registratieproces bewust af. Het ideale scenario ('happy path') heeft iedereen namelijk al getest. Registreer u nogmaals met *exact hetzelfde* e-mailadres: u hoort een duidelijke foutmelding te krijgen, geen crash en geen geruisloze overschrijving van het bestaande account. Registreer u met een ongeldig adres zoals `test@test` en controleer of de validatie al vóór het verzenden ingrijpt. Probeer een wachtwoord van twee tekens en kijk of het systeem u tegenhoudt — talloze met AI gegenereerde prototypes valideren wachtwoordeisen uitsluitend in de frontend-interface en niet op de server, wat betekent dat er feitelijk geen enkele beveiliging is.

Controleer vervolgens de verificatiemail. Is deze binnengekomen en hoe snel? Alles wat op een rustig testsysteem langer dan twee minuten duurt, is een alarmsignaal. Belandt de mail in de inbox of in de spambox? Controleer de spambox nadrukkelijk: een lancering waarbij elke activatiemail in de spammap verdwijnt, is een lancering waarbij niemand converteert. Oogt het afzenderadres professioneel of staat er `noreply@sendgrid.net`? Werkt de activatielink daadwerkelijk, en werkt hij ook als u hem opent op uw telefoon in plaats van op de computer waarop u de aanvraag indiende? En wat gebeurt er als u tweemaal op dezelfde link klikt of dit een week later doet? Een nette melding dat de link verlopen is, is uitstekend; een ruwe foutcode of stacktrace is onacceptabel.

## Test Twee: Betaling en de Kaart Die Geweigerd Moet Worden

Reken af als Account A met de kaart die gegarandeerd slaagt. Let nauwkeurig op wat er op het scherm gebeurt en wat er daarna volgt: toont de pagina een duidelijke bevestiging, krijgt het account direct toegang tot de betaalde functies, arriveert de factuurmail netjes in de mailbox en verschijnt de betaling met het juiste bedrag en de juiste valuta in uw Stripe- of Mollie-dashboard?

Test daarna de geweigerde kaart — een scenario dat vrijwel niemand test, maar waar u in uw eerste operationele week gegarandeerd mee te maken krijgt, aangezien weigeringspercentages bij legitieme Europese kaarttransacties substantieel zijn. Gebruik `4000 0000 0000 0002` en observeer: krijgt de gebruiker een begrijpelijke melding die uitlegt dat de betaling is afgewezen en uitnodigt een andere methode te proberen? Of ziet u een blanco scherm, een oneindige laadanimatie of een ruwe JSON-foutmelding? Blijft het gebruikersaccount in een logische status achter — niet half geüpgraded, niet gefactureerd en niet geblokkeerd voor een nieuwe poging?

Test vervolgens de 3D Secure-testkaart, die de extra verificatiestap afdwingt die Europese consumenten continu tegenkomen. Voltooi de authenticatie één keer succesvol, voer de test nogmaals uit en *breek de verificatie bewust af* door het pop-upvenster te sluiten. Uw software moet dit strikt registreren als een afgebroken betaling en niet per ongeluk als een geslaagde transactie.

Voer tot slot de dubbelkliktest uit. Klik tweemaal snel achter elkaar op de definitieve betaalknop. Het resultaat moet exact één afschrijving zijn. Ziet u twee transacties verschijnen, dan heeft u zojuist een ontwerpfout ontdekt die u vanaf dag één onnodige storneringen en supportvragen zou opleveren.

## Test Drie: Terugbetaling, Opzegging en het Pad Terug

Oprichters oefenen de weg naar een betalende klant tot in den treure, maar besteden vrijwel geen aandacht aan het opzeggingsproces. Dat is een risicovolle denkfout: juist bij het verlaten van uw dienst liggen uw reputatie en uw wettelijke verplichtingen onder een vergrootglas.

Zeg het abonnement van Account A op vanuit de applicatie-interface. Drie cruciale vragen: bevestigt de interface de opzegging duidelijk, behoudt de klant toegang tot het einde van de lopende factuurperiode waarvoor is betaald, en wordt de opzegging daadwerkelijk doorgevoerd in Stripe of Mollie in plaats van alleen in uw eigen database? Een opzegging die uw applicatiedatabase wel bijwerkt maar de betalingsprovider overslaat, zorgt ervoor dat u abonnementsgelden blijft incasseren van iemand die officieel heeft opgezegd — de snelste route naar officiële chargebacks en reputatieschade.

Voer daarna een terugbetaling (refund) uit direct vanuit uw betaaldashboard en kijk hoe uw software reageert. Verliest het account netjes de betaalde status? Wordt er een notificatie verzonden? Crasht er iets in de interface? Terugbetalingen worden doorgaans verwerkt via webhooks, en precies op het snijvlak van webhooks is AI-gegenereerde code vaak uiterst kwetsbaar. Deze test legt onevenredig vaak ernstige architectuurfouten bloot.

Verwijder tot slot het account, indien uw product deze functionaliteit aanbiedt. Onder de AVG (GDPR) bent u verplicht een reëel recht op gegevenswissing te faciliteren. Deze test toont aan of "account verwijderen" de persoonsgegevens daadwerkelijk verwijdert, of enkel de inlogknop onzichtbaar maakt. Vraag uw engineer rechtstreeks wat er gebeurt met de onderliggende databaserecords en wat het bewaartermijnbeleid is. U moet dit aan klanten kunnen uitleggen zodra zij hierom vragen.

## Test Vier: Wachtwoordherstel op een Niet-Ingelogd Apparaat

Wachtwoordherstel is de meest gebruikte supportroute in elke softwareapplicatie en tegelijkertijd het onderdeel dat het vaakst half is afgewerkt — simpelweg omdat het in demo's prima lijkt te werken wanneer iedereen al standaard is ingelogd.

Meld u volledig af. Vraag een wachtwoordherstel aan voor Account A. Houd de tijd bij tot de e-mail binnenkomt. Open de herstellink op uw mobiele telefoon — een ander apparaat waarop u niet bent ingelogd — en stel een nieuw wachtwoord in. Bevestig vervolgens drie punten: het nieuwe wachtwoord functioneert, het oude wachtwoord wordt direct geweigerd, en eventuele openstaande sessies op andere apparaten worden zoals verwacht ongeldig gemaakt.

Test daarna misbruikscenario's. Vraag een reset aan voor een e-mailadres dat helemaal niet in uw database voorkomt: de schermreactie moet identiek zijn aan die van een bestaand adres ("Als dit adres bij ons bekend is, hebben we een herstellink verzonden"). Een afwijkende melding verklapt aan aanvallers exact welke e-mailadressen klant bij u zijn (user enumeration). Klik tweemaal op dezelfde herstellink — de tweede poging moet strikt geweigerd worden. En laat een herstellink eens een uur onaangeroerd liggen alvorens erop te klikken: controleer of de vervaltermijn daadwerkelijk wordt afgedwongen. Een herstellink die oneindig geldig blijft, is een permanente achterdeur naar het account die rondslingert in een mailbox.

## Test Vijf: De Multi-Tenant Controle (Waar het Écht Om Draait)

Dit vergt slechts vier minuten werk en is het allerbelangrijkste onderdeel van deze hele checklist. Het is tevens de controle die bij AI-gegenereerde producten het vaakst faalt, omdat AI-bouwtools interfaces genereren die andermans data slechts verbergen in plaats van robuuste backends die weigeren de data uit te serveren.

Log in uw normale browservenster in als Account A en maak een reëel object aan: een bestelling, een klantdossier, een boeking, een project — wat de kernactiviteit van uw product ook is. Kijk naar de adresbalk terwijl u zich op de detailpagina van dat object bevindt. Vrijwel altijd staat daar een uniek identificatienummer in, zoals een nummer of een alfanumerieke reeks (`/orders/3f8a...`). Kopieer deze volledige URL.

Schakel nu over naar uw incognitovenster, log in als Account B en plak de URL van Account A rechtstreeks in de adresbalk. U hoort een duidelijke melding te zien: "Niet gevonden" (404) of "Geen toegang" (403). Krijgt u daarentegen de vertrouwelijke data van Account A te zien, stop dan direct met testen en stuur deze URL onmiddellijk naar uw ontwikkelaar. Dit is een acuut datalek in wording en dit vergt een fundamentele correctie in de backend-autorisatie (Row Level Security).

Herhaal deze test vervolgens op twee plekken die ontwikkelaars stelselmatig vergeten: alle afdruk-, export- of PDF-overzichten (deze draaien vaak via een afzonderlijke backend-route zonder de juiste autorisatiechecks) en alle publieke deellinks. Voer nog één variant uit: verander als ingelogde Gebruiker B het getal in de adresbalk naar een aangrenzend nummer, bijvoorbeeld `/orders/104` in plaats van `/orders/105`. Het handmatig aanpassen van ID-nummers (IDOR) is precies wat nieuwsgierige gebruikers instinctief doen, en het vereist geen enkele technische kennis.

## Test Zes: De Confrontatie met de Rauwe Praktijk

Besteed tien minuten aan situaties die echte gebruikers dagelijks veroorzaken, maar die in verkoopdemo's nooit aan bod komen. Maak een gloednieuw account aan en bekijk direct de lege status: het lege dashboard of de lege lijst. Legt het scherm uit wat de volgende stap is, of staart de gebruiker naar een zielloze, lege rechthoek? De eerste indruk van uw product wordt hier gevormd.

Typ een extreem lange naam, een naam met een apostrof of trema, en een emoji in uw belangrijkste tekstvelden. Nederlandse en Belgische klanten heten regelmatig `Van der Meer-Ó Súilleabháin`. Fouten in tekstverwerking en tekencodering zijn vóór de lancering triviaal op te lossen, maar na de lancering uiterst pijnlijk.

Gebruik de 'Vorige'-knop van uw browser na elke belangrijke handeling: na een betaling, na het verzenden van een formulier en na het uitloggen. Terugnavigeren na een afrekening is een beruchte oorzaak van dubbele bestellingen en databaseconflicten. Druk midden in een registratieproces met meerdere stappen op 'Vernieuwen' (F5) en controleer of de sessie overeind blijft. Log tot slot uit en probeer via een directe URL een beveiligde pagina te bereiken; u hoort op het inlogscherm uit te komen, en na succesvol inloggen hoort u idealiter direct doorgestuurd te worden naar de pagina die u oorspronkelijk wilde bezoeken.

## Bevindingen Vastleggen Zodat Ze Direct Worden Opgelost

De wijze waarop u rapporteert bepaalt hoe snel problemen worden verholpen. Hanteer voor elke bevinding vier vaste regels: wat u deed, wat u verwachtte, wat er daadwerkelijk gebeurde en het exacte tijdstip. Voeg een screenshot of een korte schermopname toe. Probeer niet zelf de technische oorzaak te diagnosticeren — de opmerking "de knop werkt niet omdat de database niet gekoppeld is" stuurt uw ontwikkelaar op een dwaalspoor op basis van uw aanname in plaats van eigen loganalyse. Aannames van oprichters over technische oorzaken slaan de plank vaker mis dan niet.

Sorteer uw lijst vervolgens in drie categorieën en lever deze aan als drie afzonderlijke lijsten, niet als één grote berg werk: **blokkerend voor livegang** (alles uit Test Vijf, alles wat met geld te maken heeft en alles wat dataverlies veroorzaakt), **oplossen in de supportperiode** (hinderlijk maar niet fataal voor de operatie), en **na de lancering** (visuele afwerking, teksten en persoonlijke voorkeuren). Deze prioritering zelf aanbrengen is het meest waardevolle wat u kunt doen: het vertelt uw engineer wat u als een absolute showstopper beschouwt in plaats van hem te laten gissen — en dat is een zakelijk oordeel dat alleen u kunt vellen. Manifera, het software-engineeringbedrijf waar LaunchStudio uit is voortgekomen, bouwt al ruim 11 jaar bedrijfskritische software voor opdrachtgevers die op exact deze wijze testen. Een scherp getriageerde buglijst van de oprichter is steevast het meest waardevolle document in de slotweek van elk project.

Negentig minuten, zes gerichte tests, geen technische kennis vereist — en een meetbaar stabielere livegang, omdat u exact die paden heeft beproefd die uw klanten gaan bewandelen in plaats van het zorgvuldig geregisseerde demopad. Voer deze controle deze week uit op staging, en herhaal de kernonderdelen op productie binnen een uur na het live gaan. Wilt u een ervaren paar ogen dat meekijkt naar uw bevindingen? [LaunchStudio](https://launchstudio.eu/nl/) analyseert dagelijks AI-gegenereerde software, ondersteund door het [engineeringteam van Manifera](https://www.manifera.com/about-us/) in Amsterdam en Ho Chi Minhstad.

Doorloop het script en stuur ons uw lijst met bevindingen — wij geven u kosteloos direct inzicht in welke punten echte lanceerblokkades vormen en welke rustig kunnen wachten.

## Praktijkvoorbeeld

### Een Oprichter in Actie: De Lekkende PDF

Nadia el Amrani, voormalig verhuurmakelaar in Rotterdam, bouwde Huurhelder — een softwaretool voor huuradministratie en onderhoudsverzoeken voor particuliere vastgoedbeleggers — met behulp van Lovable. Vóór de lancering besloot ze het testscript voor oprichters te doorlopen op de staging-omgeving met twee testaccounts. Ze verwachtte dat het een formaliteit zou zijn, aangezien het externe beveiligingswerk al officieel was opgeleverd.

Test één tot en met vier verliepen vlekkeloos. Ook Test Vijf slaagde op elk standaardscherm: inloggen als verhuurder B en het plakken van de huurders-URL van verhuurder A resulteerde keurig in een "Geen toegang"-foutpagina. Vervolgens testte ze de maandelijkse huurafrekening in PDF-formaat — een functie die ze zelf continu gebruikte en die een downloadbaar bestand genereerde via een unieke weblink. Verhuurder B kon de volledige huurafrekening van verhuurder A downloaden, inclusief namen van huurders, woonadressen en betalingshistorie.

**Het Resultaat:** De PDF-generator werd aan de serverzijde aangeroepen via een API-eindpunt dat nooit was meegenomen in de nieuwe autorisatieregels, omdat dit endpoint ouder was en zich in een ander deel van de codebase bevond. Het probleem werd binnen een halve dag hersteld, en dezelfde inspectie bracht nog twee data-exportpunten met een identieke kwetsbaarheid aan het licht. Huurhelder lanceerde vier dagen later met alle drie de datalekken definitief gedicht.

> *"Ik had de test bijna overgeslagen omdat een professional het werk al had goedgekeurd. Hij had de webapplicatie gecontroleerd. Maar niemand had de PDF-bestanden gecontroleerd, simpelweg omdat niemand behalve ik die bestanden maandelijks daadwerkelijk downloadt."*
> — **Nadia el Amrani, Oprichter, Huurhelder (Rotterdam)**

**Kosten & Tijdlijn:** €2.650 (Launch Ready-pakket, autorisatiestructuren, Mollie-betaalkoppeling en hardening van export-eindpunten) — live binnen 11 werkdagen.

---

## Veelgestelde Vragen

### Voelt mijn softwareteam zich niet gepasseerd als ik hun werk zelf ga testen?

Een professioneel team moedigt dit juist actief aan, omdat u een heel ander type problemen ontdekt dan zij: u weet precies hoe het product voor een echte eindgebruiker moet aanvoelen, terwijl zij controleren of de code technisch functioneert. Deel uw bevindingen feitelijk met tijdstempels in plaats van als een persoonlijk oordeel; dan wordt het direct ervaren als de constructieve samenwerking die het is.

### Hoe weet ik zeker dat mijn tests geen echt geld afschrijven of echte klanten mailen?

Vraag uw ontwikkelaar expliciet te bevestigen dat u op de staging-omgeving werkt die gekoppeld is aan de testmodus van uw betaalprovider, en dat staging uitsluitend gebruikmaakt van fictieve of geanonimiseerde data in plaats van een kopie van uw echte klantenbestand. Beide horen standaard zo te zijn; deze bevestiging vragen kost dertig seconden en neemt alle onzekerheid weg.

### Wat moet ik doen als ik iets tegenkom maar twijfel of het wel echt een bug is?

Meld het altijd, en beschrijf louter feitelijk wat u waarneemt. Een ontwikkelaar kan een onduidelijke situatie in twee minuten evalueren, terwijl een betalende klant die vastloopt direct voor frictie zorgt. De notitie "dit voelde verwarrend, maar werkt mogelijk zoals bedoeld" is een volkomen professionele terugkoppeling. Te veel melden is een aanzienlijk kleiner probleem dan te weinig melden.

### Moet ik het complete script na de officiële livegang nogmaals uitvoeren?

Test de onderdelen rondom betalingen en toegangsrechten direct binnen een uur na de livegang opnieuw op de productieomgeving: registratie, één echte betaling met een eigen betaalkaart, en de controle op datalekken tussen twee accounts. Serverconfiguraties en omgevingsvariabelen wijken tussen staging en productie regelmatig af, en dat is exact waar onaangename verrassingen op de lanceerdag ontstaan. De volledige testronde kan wachten tot de volgende grote release.

### Mijn product accepteert nog geen betalingen. Welke tests zijn dan nog relevant?

Alle tests met uitzondering van de betalings- en terugbetalingsscenario's (Test Twee en Drie). Registratie, wachtwoordherstel, de autorisatiecontrole tussen verschillende accounts en de praktijktest zijn cruciaal, ongeacht of er geld in het spel is. Juist bij gratis software ontstaan door gebrekkige gegevensscheiding evenveel ernstige privacyproblemen als bij betaalde diensten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Voelt mijn softwareteam zich niet gepasseerd als ik hun werk zelf ga testen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een professioneel team moedigt dit juist aan. U ontdekt een ander type problemen: u weet hoe het product voor een echte klant moet voelen, terwijl zij weten hoe de code werkt. Deel feitelijke waarnemingen met tijdstempels in plaats van oordelen, dan geldt het direct als waardevolle samenwerking."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik zeker dat mijn tests geen echt geld afschrijven of echte klanten mailen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag uw ontwikkelaar te bevestigen dat u op de staging-omgeving werkt, gekoppeld aan de testmodus van uw betaalprovider, met fictieve of geanonimiseerde data. Beide horen standaard zo te zijn, en dit navragen kost slechts dertig seconden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als ik iets tegenkom maar twijfel of het wel echt een bug is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meld het altijd feitelijk. Voor een ontwikkelaar kost het evalueren van een twijfelgeval een minuut, terwijl een vastlopende klant direct schade oplevert. Te veel melden is een veel kleiner probleem dan een bug over het hoofd zien."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik het complete script na de officiële livegang nogmaals uitvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Doorloop de betaal- en autorisatietests binnen een uur na livegang op productie: registratie, één reële betaling en de multi-tenant controle. Omgevingsvariabelen verschillen tussen staging en productie, wat op lanceerdagen tot verrassingen kan leiden."
      }
    },
    {
      "@type": "Question",
      "name": "Mijn product accepteert nog geen betalingen. Welke tests zijn dan nog relevant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alle tests behalve de betalingen en terugbetalingen. Registratie, wachtwoordherstel, de autorisatiecontrole tussen verschillende accounts en de praktijktest zijn essentieel; gratis producten lopen bij datalekken evenveel risico als betaalde SaaS."
      }
    }
  ]
}
</script>
