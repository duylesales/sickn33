---
Titel: "Lovable-productanalyse: Welke Events U Binnen de AVG Wilt Meten"
Trefwoorden: lovable productanalyse, eventtracking, analyse en AVG, session replay, activatiemetingen, accountgezondheid, PostHog EU, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable-productanalyse: Welke Events U Binnen de AVG Wilt Meten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable-productanalyse: Welke Events U Binnen de AVG Wilt Meten",
  "description": "De meeste AI-gebouwde producten meten niets nuttigs of veel te veel, inclusief data die ze nooit hadden mogen verzamelen. Welke vragen productanalyse moet beantwoorden, hoe u een klein trackingplan ontwerpt, wat nooit in een event hoort, en hoe u binnen de AVG en de Nederlandse cookieregels blijft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-product-analytics-events-worth-tracking-under-gdpr" }
}
</script>

Vraag de oprichter van een AI-gebouwd B2B-product welke klanten het product actief gebruiken, welke functies niemand aanraakt, en welke accounts stilletjes op weg zijn naar opzeggen, en het antwoord is meestal een gok. Ofwel wordt er niets gemeten, ofwel is er tijdens het bouwen een analysescript toegevoegd dat elke klik op elke pagina vastlegt - en dat de vraag nog steeds niet kan beantwoorden, omdat de events nooit zijn ontworpen.

De tweede situatie is vaak erger dan de eerste. Analysetools die met één regel code worden toegevoegd, leggen paginatitels, URL's, formulierinhoud en, met session replay aan, opnames van hele schermen vast. In een product met persoonsgegevens van klanten betekent dat het versturen van namen, adressen, gezondheidsinformatie of financiële gegevens naar een analyseaanbieder - vaak buiten de EU, vaak zonder verwerkersovereenkomst, en bijna altijd zonder dat de klant het weet.

Goede productanalyse is klein, bewust en privacybewust. Dit artikel behandelt de vragen die analyse voor een B2B-product moet beantwoorden, hoe u events en een trackingplan ontwerpt, wat nooit in een event mag staan, session replay, toestemming onder de Nederlandse regels, het kiezen van een tool, en het omzetten van de data in beslissingen.

## Begin met Vragen, Niet met Events

Analyse bestaat om vragen te beantwoorden. Schrijf ze eerst op; de events volgen eruit.

Voor de meeste B2B-producten zijn de belangrijke vragen beperkt:

- **Activatie.** Bereiken nieuwe accounts het moment waarop het product nuttig voor hen wordt - de eerste factuur verstuurd, het eerste rooster gepubliceerd, het eerste rapport gedeeld - en hoe lang duurt dat?
- **Betrokkenheid per account.** Welke organisaties gebruiken het product wekelijks, welke nemen af, welke zijn gestopt?
- **Gebruik van functies.** Welke functies worden gebruikt, door welk deel van de accounts, en welke zijn gebouwd en worden genegeerd?
- **Frictie.** Waar haken gebruikers af in een flow - onboarding, import, afrekenen - en waar clusteren fouten?
- **Signalen van groei.** Welke accounts naderen hun abonnementslimieten, voegen gebruikers toe of gebruiken premiumfuncties intensief?

Elke vraag wijst naar een handvol events. Een product met vijftien tot dertig goed ontworpen events kan ze allemaal beantwoorden. Een product met vierhonderd automatisch vastgelegde events kan er meestal geen enkele betrouwbaar beantwoorden.

## Ontwerp Events Bewust

Een event legt vast dat er iets betekenisvols gebeurde. Goede events delen een consistente structuur.

**Een duidelijke naam in de vorm object_actie** - `invoice_sent`, `schedule_published`, `import_completed`, `member_invited`. In de verleden tijd, en beschrijvend voor een zakelijke actie in plaats van een klik: "factuur verstuurd" heeft betekenis, "knop aangeklikt" niet.

**Het account en de gebruiker**, als identificatoren. In B2B is het account - de organisatie - de eenheid die het meest uitmaakt: het is de klant, het abonnement en het risico op opzeggen. Elk event draagt het organisatie-ID; de meeste analyse gebeurt per organisatie, niet per persoon.

**Een kleine set eigenschappen die de vragen beantwoorden** - het abonnement, het aantal regels op de factuur, of de import uit een sjabloon kwam, de bron van de actie. Eigenschappen beschrijven het event, niet de mensen of de data die erbij betrokken zijn.

**Een tijdstip van de server**, niet van het apparaat van de gebruiker.

Schrijf de events op in een trackingplan - één document of bestand met elk event, zijn eigenschappen, wanneer het wordt verstuurd en welke vraag het dient. Wanneer iemand, of een AI-assistent, een event wil toevoegen, is het trackingplan de plek waar het wordt ontworpen en gereviewd. Zonder trackingplan leveren vijf sessies `invoice_sent`, `InvoiceSent`, `sent_invoice`, `invoice-send` en `send_invoice_click` op, en kan geen rapport ze combineren.

## Geef de Voorkeur aan Serverside Events voor Wat Ertoe Doet

Events kunnen vanuit de browser of vanaf uw server worden verstuurd.

**Browserevents** leggen vast wat de gebruiker in de interface ziet en doet - een bekeken pagina, een stap in een wizard, een gebruikt filter. Ze worden in een aanzienlijk deel van de browsers geblokkeerd door adblockers en privacyinstellingen, en ze kunnen worden gemanipuleerd.

**Serverevents** worden verstuurd wanneer de actie echt plaatsvindt in uw backend - de factuur is echt verstuurd, de import is echt voltooid, het abonnement is echt gewijzigd. Ze zijn volledig, betrouwbaar en niet gevoelig voor blokkering.

Verstuur de events die zakelijke vragen beantwoorden - activatie, betrokkenheid, gebruik, groei - vanaf de server, in dezelfde functie die de actie uitvoert. Gebruik browserevents alleen voor vragen over de interface, zoals waar gebruikers afhaken in een flow met meerdere stappen.

Een praktisch patroon is events eerst naar een eigen tabel te schrijven en ze vanuit een achtergrondtaak door te sturen naar de analysetool. Uw eigen kopie is volledig, samen met uw data te bevragen, en overleeft een wissel van analyseaanbieder.

## Wat Nooit in een Event Mag Staan

Hier gaan AI-gebouwde producten het vaakst mis, en de gevolgen zijn juridisch in plaats van technisch.

**Geen persoonsgegevens van de cliënten, patiënten of medewerkers van uw klanten.** Namen, e-mailadressen, telefoonnummers, adressen, geboortedata, notities, diagnoses, salarissen. Is uw product een tool voor zorg, HR, financiën of juridische zaken, dan stuurt een event met zulke data bijzondere of gevoelige persoonsgegevens naar een derde partij.

**Geen vrije tekst.** Zoekopdrachten, formulierinhoud, notities en berichten bevatten op onvoorspelbare wijze persoonsgegevens. Leg vast dat er werd gezocht en hoeveel resultaten dat opleverde, niet waarop werd gezocht.

**Geen URL's of paginatitels met identificatoren of namen.** `/clients/jan-de-vries/medical-history` als paginaweergave is een persoonsgegeven. Stel de analysetool zo in dat paden worden ontdaan of genormaliseerd - `/clients/:id/medical-history` - voordat er iets wordt verstuurd.

**Geen e-mailadressen als gebruikersidentificator.** Gebruik uw interne gebruikers-ID, of een daarvan afgeleid gepseudonimiseerd ID.

Functies voor automatisch vastleggen - "autocapture" van elke klik, elk formulierveld en elke tekst op het scherm - zijn waar het meeste hiervan lekt. Schakel ze uit, of beperk ze tot expliciet toegestane elementen, in elk product dat persoonsgegevens toont.

## Session Replay Verdient Bijzondere Voorzichtigheid

Tools voor session replay leggen vast wat gebruikers zien en doen - muisbewegingen, klikken, scrollen en de inhoud van het scherm - en spelen het af als een video. Ze zijn echt nuttig om verwarrende interfaces te begrijpen.

In een product dat persoonsgegevens toont, zijn ze ook een opname van die gegevens. Een opname van een zorgcoördinator die een cliëntdossier gebruikt, bevat het cliëntdossier. De meeste tools maskeren formulierinvoer standaard, maar geen andere tekst op het scherm, en de maskeerinstellingen zijn makkelijk verkeerd te doen.

Gebruikt u session replay toch: maskeer standaard alle tekst en maak alleen specifieke statische elementen zichtbaar; sluit schermen met persoonlijke of gevoelige data volledig uit; neem alleen een steekproef van sessies op; bewaar opnames kort; en documenteer het in uw privacyinformatie en verwerkingsregister. Voor producten met gezondheids-, financiële of kinderdata is het veiligste antwoord session replay helemaal niet in de applicatie te gebruiken, en alleen op openbare marketingpagina's waar geen klantdata verschijnt.

## Toestemming en de Nederlandse Regels

Twee sets regels gelden voor productanalyse, en ze worden vaak verward.

**De cookieregels** in de Telecommunicatiewet - de Nederlandse invulling van de Europese ePrivacy-regels - gaan over het opslaan of uitlezen van informatie op het apparaat van een gebruiker, inclusief analytische cookies en vergelijkbare identificatoren. Analytische cookies vereisen in het algemeen toestemming, met een smalle uitzondering voor analyse met weinig of geen gevolgen voor de privacy. De Autoriteit Persoonsgegevens heeft voorwaarden voor die uitzondering beschreven: onder meer een verwerkersovereenkomst met de aanbieder, gemaskeerde of ingekorte IP-adressen, geen delen van data met de aanbieder voor eigen doeleinden, en geen volgen over sites heen. Analyse die zo is ingericht, kan zonder cookiebanner worden gebruikt; analyse die niet aan de voorwaarden voldoet, heeft eerst toestemming nodig. Het artikel over cookietoestemming in extra-11 behandelt de kant van de banner.

**De AVG** gaat over de verwerking van persoonsgegevens in de events zelf, waar ze ook worden opgeslagen. Voor analyse binnen de app van een B2B-product is de gebruikelijke grondslag het gerechtvaardigd belang bij het verbeteren en onderhouden van de dienst, mits de analyse beperkt blijft tot wat nodig is, geen gevoelige data bevat, en transparant wordt beschreven.

Serverside events, zonder cookies naar uw eigen database geschreven en doorgestuurd naar een in de EU gehoste tool onder een verwerkersovereenkomst, vermijden de cookievraag vaak volledig terwijl ze binnen de AVG blijven - nog een reden om ze te verkiezen.

Uw zakelijke klanten zullen er ook naar vragen. Analysetools zijn subverwerkers wanneer ze persoonsgegevens zoals gebruikers-ID's ontvangen; neem ze op in uw lijst, zoals het artikel over subverwerkers in deze reeks beschrijft, en bied klanten die dat eisen de mogelijkheid hun organisatie uit te sluiten van analyse.

## Een Tool Kiezen

De keuze hangt meer af van hosting en gegevensverwerking dan van functies.

**Productanalyse gehost in de EU** - PostHog in de EU-regio, of zelf gehost, en vergelijkbare tools - biedt events, funnels, retentie en feature flags, met een verwerkersovereenkomst en data in Europa.

**Privacygerichte webanalyse** - Plausible, Simple Analytics, een zelf gehoste Matomo - is uitstekend voor marketingpagina's en verkeer in totalen, en minder geschikt voor productanalyse per account.

**Uw eigen database plus een dashboardtool** - events in een Postgres-tabel, bevraagd met SQL of een BI-tool. Voor een klein product met serverside events is dat in het eerste jaar vaak genoeg en houdt het alle data onder uw beheer.

Wat u ook kiest, controleer de hostingregio, de verwerkersovereenkomst, of de aanbieder uw data voor eigen doeleinden gebruikt, en hoe verwijderen werkt wanneer een gebruiker of klant erom vraagt.

## Zet Data om in Beslissingen

Analyse betaalt zich alleen terug wanneer iemand ernaar kijkt en handelt. Drie overzichten dekken het meeste van wat een klein B2B-team nodig heeft.

**Een activatiefunnel** - aangemeld, inrichting voltooid, de kernactie voor het eerst uitgevoerd, haar in de tweede week opnieuw uitgevoerd - met de mediane tijd tussen de stappen. Verbeter de stap waar de meeste accounts stoppen.

**Accountgezondheid** - per organisatie: actieve gebruikers deze week vergeleken met de afgelopen maand, kernacties per week, datum van laatste activiteit, gebruikte functies. Afnemende accounts zijn een lijst voor een telefoontje, vaak maanden vóór een opzegmail.

**Gebruik van functies** - het aandeel actieve accounts dat elke functie de afgelopen maand gebruikte. Functies die bijna niemand gebruikt, zijn kandidaten voor verbetering, uitleg of verwijdering, wat ook vermindert wat het product moet onderhouden.

Bekijk ze in een vast ritme - wekelijks voor accountgezondheid, maandelijks voor gebruik - en leg vast wat u besloot. Een dashboard dat niemand opent, is alleen een kostenpost en een privacyrisico.

## Bewaren en Verwijderen

Analysedata wordt standaard voor altijd bewaard, omdat niemand iets anders besluit. Onder de AVG mag ze niet langer worden bewaard dan nodig, en moet ze worden meegenomen wanneer iemand zijn rechten uitoefent.

**Stel een bewaartermijn vast.** Gedetailleerde events met gebruikersidentificatoren hoeven zelden langer dan twaalf tot vijfentwintig maanden te worden bewaard - lang genoeg om een seizoen te vergelijken met hetzelfde seizoen vorig jaar. Tel ze daarna op per organisatie en week en verwijder de afzonderlijke events. Leg de beslissing vast in het bewaarregister dat het artikel over bewaartermijnen in deze reeks beschrijft.

**Neem analyse mee bij verwijderen.** Wordt het account van een gebruiker verwijderd, of vertrekt een klant en wordt zijn data gewist, dan moeten hun events ook weg - in uw eigen tabel en bij de analyseaanbieder. De meeste aanbieders bieden verwijderen per gebruikers-ID via een API; roep die aan vanuit hetzelfde verwijderproces dat het account wist, zoals het artikel over wissen onder de AVG in extra-11 beschrijft.

**Neem analyse mee bij inzageverzoeken.** Vraagt iemand welke data u over hem hebt, dan horen events die aan zijn gebruikers-ID zijn gekoppeld bij het antwoord. Gepseudonimiseerde ID's verkleinen het risico van de data, maar halen haar niet buiten de AVG, omdat u ze kunt terugkoppelen.

## Deel Gebruik met Uw Klanten

Dezelfde data die u vertelt welke accounts floreren, is waardevol voor de beheerders van uw klanten - en haar delen is een van de weinige analysefuncties die ook helpt het product te verkopen.

Een gebruikspagina per organisatie - actieve gebruikers deze maand, de uitgevoerde kernacties, de gebruikte functies, misschien de bespaarde tijd - beantwoordt de vraag die een manager van een klant bij de verlenging stelt: "Gebruiken we dit eigenlijk wel?" Het helpt de pleitbezorger bij de klant het abonnement te verantwoorden, en het laat beheerders zien welke collega's het product nog niet zijn gaan gebruiken.

Houd het op het niveau van de eigen data van de organisatie, nooit vergeleken met andere klanten bij naam, en toon nooit meer over individuele medewerkers dan hun beheerder mag zien. Geaggregeerde vergelijkingen - "organisaties van uw omvang versturen gemiddeld 40 facturen per maand" - kunnen nuttig zijn wanneer er genoeg klanten zijn om ze anoniem te maken.

## Datakwaliteit

Analysedata is maar zo goed als de events. Drie gewoonten houden haar betrouwbaar.

**Controleer events tegen het trackingplan**, bij voorkeur met een getypeerde functie per event in de code, zodat een event met een ontbrekende eigenschap of een verkeerde naam faalt tijdens de ontwikkeling in plaats van productiedata te vervuilen.

**Test events zoals functies.** Wanneer de factuurflow verandert, controleer dan dat `invoice_sent` nog één keer wordt verstuurd - niet nul keer, niet twee keer.

**Sluit intern en testverkeer uit** - uw eigen organisatie, demoaccounts, loadtests - anders is elke meting vertekend, vooral in een product met weinig klanten.

## Dit Inrichten

Voor een Lovable-product is dit doorgaans twee tot vier dagen: de zakelijke vragen opgeschreven, een trackingplan van vijftien tot dertig events benoemd als object en actie met account- en gebruikersidentificatoren en een kleine set eigenschappen, serverside events voor zakelijke acties weggeschreven naar een eigen tabel en doorgestuurd door een achtergrondtaak, browserevents alleen voor vragen over de interface, geen persoonsgegevens, vrije tekst of herleidbare URL's in events, autocapture uitgeschakeld of beperkt, session replay uitgesloten van gevoelige schermen of niet gebruikt in de applicatie, een beoordeling van cookies en toestemming tegen de Nederlandse regels, een in de EU gehoste tool onder een verwerkersovereenkomst die als subverwerker is opgenomen, een opt-out voor klanten die dat eisen, een bewaartermijn en verwijderen bij de aanbieder, overzichten van activatie, accountgezondheid en gebruik met een vast ritme, een gebruikspagina voor beheerders van klanten, getypeerde controle van events, tests voor events, en intern verkeer uitgesloten.

LaunchStudio richt dit in zodat oprichters kunnen zien welke klanten floreren zonder te verzamelen wat ze niet horen te verzamelen. Daarachter staat Manifera - elf jaar, 160+ projecten, 120+ engineers, vanaf de Herengracht 420 in Amsterdam.

[Vraag ons wat uw analysescript werkelijk verstuurt](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Opnames van Notities over Ziekteverzuim

Naomi Dekker bouwde Verzuimregistratie in Lovable: registratie van ziekteverzuim en afwezigheid voor het mkb, gebruikt door 160 bedrijven om verzuim, afspraken over re-integratie en contact met arbodiensten vast te leggen.

Tijdens het bouwen was een analysescript toegevoegd met standaardinstellingen: autocapture van elke klik en pagina, en session replay aan. Pagina-URL's bevatten namen van medewerkers. Opnames van sessies legden de verzuimschermen vast - inclusief de vrije notities waarin leidinggevenden vastlegden wat medewerkers hun over hun gezondheid hadden verteld. De data ging naar een aanbieder buiten de EU, zonder verwerkersovereenkomst en zonder vermelding in de privacyverklaring.

Het kwam aan het licht toen de functionaris gegevensbescherming van een klant met 400 medewerkers vroeg om de lijst met subverwerkers en hoe met gezondheidsgerelateerde data werd omgegaan. Tegelijk kon Naomi een eenvoudigere vraag van haar eigen bestuur niet beantwoorden: welke van de 160 bedrijven het product echt elke week gebruikten. De tool bevatte 140 verschillend benoemde events en geen betrouwbare organisatie-identificator.

Drie werkdagen: session replay volledig uit de applicatie verwijderd en autocapture uitgeschakeld; de bestaande data bij de oude aanbieder verwijderd, met schriftelijke bevestiging; een trackingplan van 22 serverside events benoemd als object en actie, elk met gepseudonimiseerde organisatie- en gebruikers-ID's en zonder namen, notities of herleidbare URL's; events weggeschreven naar een tabel in de eigen database van het product en doorgestuurd naar een in de EU gehoste analysetool onder een verwerkersovereenkomst, ingericht volgens de voorwaarden van de Autoriteit Persoonsgegevens voor analyse met weinig impact; een opt-out per klantorganisatie; een beoordeling vastgelegd in het verwerkingsregister, een bijgewerkte lijst met subverwerkers en privacyverklaring; overzichten van activatie en accountgezondheid; en getypeerde eventfuncties met tests.

**Resultaat:** het incident werd met hulp van een privacyjurist beoordeeld en gemeld bij de Autoriteit Persoonsgegevens, en getroffen klanten werden geïnformeerd; de functionaris gegevensbescherming van de klant accepteerde het herstel en de klant bleef. Het overzicht van accountgezondheid identificeerde negen bedrijven waarvan het gebruik sterk was gedaald; Naomi belde ze allemaal, en zeven waren een jaar later nog klant. Het aandeel nieuwe accounts dat binnen een week het eerste verzuim registreerde, steeg van 48% naar 71% nadat de onboardingstap waar de meesten stopten opnieuw was ontworpen.

> *"Ik voegde analyse toe om te weten welke klanten actief waren. Wat het eigenlijk deed, was de notities van leidinggevenden over de gezondheid van hun medewerkers opnemen en naar het buitenland sturen - en het kon me nog steeds niet vertellen welke klanten actief waren."*
> - **Naomi Dekker, Oprichter, Verzuimregistratie (Ede)**

**Kosten & Doorlooptijd:** €3.400 (verwijderen van session replay en autocapture, verwijdering bij de vorige aanbieder, trackingplan van 22 events met gepseudonimiseerde serverside events, analyse gehost in de EU met verwerkersovereenkomst, opt-out per klant, verwerkingsregister en privacydocumentatie, overzichten van activatie en accountgezondheid, controle en tests van events) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Welke events moet een B2B-product meten?

De events die een paar zakelijke vragen beantwoorden: activatie, betrokkenheid per account, gebruik van functies, frictie in belangrijke flows en signalen van groei. Vijftien tot dertig goed ontworpen events zijn meestal genoeg.

### Moeten events vanuit de browser of de server worden verstuurd?

Zakelijke acties vanaf de server, waar ze volledig en betrouwbaar zijn; interactie met de interface alleen vanuit de browser waar dat nodig is. Events eerst naar uw eigen tabel schrijven houdt een volledige kopie onder uw beheer.

### Wat mag nooit in analyse-events staan?

Persoonsgegevens van de cliënten of medewerkers van uw klanten, vrije tekst zoals notities en zoekopdrachten, herleidbare URL's en e-mailadressen. Gebruik in plaats daarvan interne of gepseudonimiseerde ID's.

### Is session replay toegestaan onder de AVG?

Dat kan, met strikte maskering, uitsluiting van gevoelige schermen, steekproeven, korte bewaring en transparantie. Voor producten met gezondheids-, financiële of kinderdata is het veiliger het niet in de applicatie te gebruiken.

### Heb ik toestemming nodig voor productanalyse in Nederland?

Analytische cookies vereisen in het algemeen toestemming, tenzij de analyse voldoet aan de voorwaarden van de Autoriteit Persoonsgegevens voor weinig privacy-impact. Serverside events zonder cookies, verwerkt onder de AVG met een verwerkersovereenkomst, vermijden de cookievraag vaak.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat moet een B2B-SaaS meten in productanalyse?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Events die vragen over activatie, betrokkenheid per account, gebruik van functies, frictie en groei beantwoorden - meestal vijftien tot dertig."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten analyse-events client-side of server-side zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zakelijke acties server-side voor volledigheid en betrouwbaarheid; browserevents alleen voor vragen over de interface."
      }
    },
    {
      "@type": "Question",
      "name": "Welke data moet buiten analyse-events blijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Persoonsgegevens van eindcliënten of medewerkers, vrije tekst, herleidbare URL's en e-mailadressen - gebruik gepseudonimiseerde ID's."
      }
    },
    {
      "@type": "Question",
      "name": "Voldoet session replay aan de AVG?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen met strikte maskering, uitgesloten gevoelige schermen, steekproeven, korte bewaring en transparantie; vermijd het in apps met gezondheids- of financiële data."
      }
    },
    {
      "@type": "Question",
      "name": "Is voor productanalyse in Nederland cookietoestemming nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor analytische cookies in het algemeen wel, tenzij ze voldoen aan de voorwaarden van de AP voor weinig impact; serverside events zonder cookies vermijden dit vaak."
      }
    }
  ]
}
</script>
