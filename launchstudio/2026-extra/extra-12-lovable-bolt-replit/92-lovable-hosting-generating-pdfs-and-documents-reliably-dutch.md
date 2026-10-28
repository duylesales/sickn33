---
Titel: "Lovable Hosting: Pdf's en Documenten Betrouwbaar Genereren"
Trefwoorden: lovable pdf genereren, facturen als pdf, offertes, headless Chromium, documentgeneratie, PDF/A, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Pdf's en Documenten Betrouwbaar Genereren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Pdf's en Documenten Betrouwbaar Genereren",
  "description": "Facturen, offertes, rapporten en certificaten zijn wat klanten doorsturen, printen en archiveren. Waarom pdf's uit de browser falen, de aanpakken op de server die werken, waarom een verstuurd document nooit mag veranderen, en het beveiligingsrisico in het renderen van HTML.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-generating-pdfs-and-documents-reliably" }
}
</script>

De meeste B2B-producten maken uiteindelijk documenten. Facturen en creditnota's, offertes en orderbevestigingen, inspectierapporten, certificaten, urenstaten, contracten. Dit zijn de delen van uw product die het product verlaten: doorgestuurd naar de klant van een klant, geprint, gearchiveerd door een accountant, toegevoegd aan een geschil.

Ze horen ook bij de minst betrouwbare delen van AI-gebouwde producten. De eerste pdf-functie wordt meestal in de browser gemaakt door een schermafbeelding te nemen van een HTML-pagina en die in een pdf te plaatsen. Voor een factuur van één pagina ziet het er op de laptop van de oprichter acceptabel uit. Op een telefoon, voor een rapport van twaalf pagina's, in een andere browser, of een jaar later wanneer iemand precies moet weten wat er is verstuurd, valt het uit elkaar.

Dit artikel behandelt waarom pdf's uit de browser falen, de aanpakken op de server die werken, de eigenschap die het meest uitmaakt - een verstuurd document mag nooit veranderen - en de details die een professioneel document onderscheiden van een document dat er gegenereerd uitziet.

## Waarom Pdf's uit de Browser Falen

Het veelvoorkomende AI-gegenereerde patroon rendert het document als verborgen HTML-element, legt het vast met `html2canvas`, en voegt de afbeelding in een pdf in met `jsPDF`. Dat heeft vijf voorspelbare problemen.

**De tekst is een afbeelding.** Ze kan niet worden geselecteerd, doorzocht of gekopieerd, boekhoudsoftware kan haar niet lezen, schermlezers kunnen haar niet lezen, en ze is wazig bij inzoomen of printen.

**De paginering is een gok.** De schermafbeelding wordt in stukken ter grootte van A4 gesneden, dwars door tabelrijen, tekstregels en handtekeningen.

**Het hangt af van het apparaat.** Lettertypen, schermbreedte, pixeldichtheid en geheugen verschillen. Grote documenten putten het geheugen van telefoons uit en falen stil, precies waar buitendienstmedewerkers ze maken.

**Het wordt opnieuw gemaakt uit actuele data.** Elke download rendert het document opnieuw uit wat er nu in de database staat - het probleem dat hieronder wordt beschreven.

**Het kan niet draaien zonder een persoon.** Een document dat in de browser wordt gemaakt, kan niet door een geplande taak worden aangemaakt, niet aan een automatische e-mail worden toegevoegd, en niet aan het einde van de maand in bulk worden gemaakt.

Elk hiervan is te verdragen voor een prototype. Samen betekenen ze dat documenten op de server moeten worden gemaakt.

## Drie Aanpakken op de Server

| Aanpak | Hoe het werkt | Sterke punten | Zwakke punten |
|---|---|---|---|
| HTML naar pdf met headless Chromium | Een HTML-sjabloon renderen in een echte browserengine en afdrukken naar pdf | HTML en CSS gebruiken die u al kent; uitstekende typografie; tabellen en layouts zijn eenvoudig | Chromium is zwaar - het draait niet in een Supabase edge function; vraagt een container of een dienst |
| Programmatische pdf-bibliotheken | Het document in code opbouwen met een bibliotheek als PDFKit, pdf-lib of React-PDF | Licht, draait bijna overal, precieze controle | Layout is bewerkelijk; complexe tabellen en doorlopende tekst kosten echte moeite |
| Een documentdienst | Data en een sjabloon naar een gehoste API sturen die de pdf teruggeeft | Niets te beheren; regelt vaak PDF/A, lettertypen en schaal | Kosten per document; klantdata verlaat uw infrastructuur, dus het is een subverwerker |

Voor de meeste producten is de juiste keuze HTML naar pdf met headless Chromium, gedraaid als kleine container op een platform dat langlopende processen ondersteunt - een zelf gehoste Gotenberg-instantie is een gangbare keuze - of via een gehoste renderdienst in de EU. Sjablonen zijn HTML en CSS, waarmee een developer en een AI-assistent allebei kunnen werken, en de uitvoer heeft echte, selecteerbare tekst.

Programmatische bibliotheken passen bij eenvoudige, zeer regelmatige documenten - een certificaat, een label, een bon van één pagina - waar de layout vastligt en u geen browser wilt draaien.

Wat u ook kiest, het renderen hoort niet in het verzoek waarop de gebruiker wacht. Dat is de volgende sectie.

## Maak Documenten als Taken

Een rapport van twintig pagina's renderen kost seconden, soms tientallen seconden, en mislukt af en toe. Doe het in het verzoek en u krijgt time-outs, dubbele klikken die twee documenten maken, en fouten die de gebruiker als foutpagina ziet.

Het patroon uit het artikel over achtergrondwerk in deze reeks geldt direct:

1. De actie - "factuur versturen", "rapport afronden" - maakt een record in `documents` aan met status `pending`.
2. Een worker pakt het op, rendert de pdf, slaat haar op, en zet de status op `ready` samen met het opslagpad, de grootte en het controlegetal.
3. De interface toont voortgang en het resultaat; een e-mail met een link wordt verstuurd zodra het document klaar is.
4. Mislukte renders worden opnieuw geprobeerd met oplopende wachttijd; na de laatste mislukking toont het record een fout waarover iemand een waarschuwing krijgt.

```sql
create table documents (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid not null references organisations(id),
  kind text not null,                 -- 'invoice' | 'quote' | 'report'
  source_id uuid not null,            -- de factuur, offerte of het rapport
  version int not null default 1,
  template_version text not null,
  status text not null default 'pending',
  storage_path text,
  sha256 text,
  created_at timestamptz not null default now(),
  unique (kind, source_id, version)
);
```

De unieke constraint maakt het genereren idempotent: een nieuwe poging of een dubbele klik kan geen tweede versie 1 aanmaken.

## Een Verstuurd Document Mag Nooit Veranderen

Dit is de eigenschap die het meest uitmaakt, en de eigenschap die genereren in de browser per ontwerp verkeerd doet.

Wordt een offerte-pdf elke keer dat iemand haar downloadt uit de database gerenderd, dan verandert de offerte wanneer de data verandert. Een prijslijst die in maart wordt aangepast, verandert elke offerte die in februari is verstuurd. Een adres van een klant dat vandaag wordt gecorrigeerd, verandert de facturen van vorig jaar. Ontstaat er onenigheid over wat er werd aangeboden, dan kan niemand laten zien wat er werkelijk is verstuurd.

Voor facturen is dit ook een juridische kwestie. De Nederlandse bewaarplicht verplicht ondernemers hun administratie, inclusief uitgaande facturen, zeven jaar te bewaren, en een factuur die met andere inhoud opnieuw kan worden gemaakt, is geen betrouwbaar stuk. Het artikel over btw en facturen in deze reeks behandelt de verplichte inhoud; dit artikel gaat over het vastleggen ervan.

De regels:

- **Maak het document één keer, op het moment dat het wordt uitgegeven** - wanneer de factuur wordt verstuurd, de offerte wordt gedeeld, het rapport wordt afgerond - en sla het bestand op.
- **Lever vanaf dan het opgeslagen bestand.** Render een uitgegeven document nooit opnieuw.
- **Leg een momentopname vast** van de data waaruit het document is opgebouwd - regels, prijzen, adressen, btw-tarieven - in het record zelf of in een JSON-kolom, zodat document en data het voor altijd eens zijn.
- **Leg een controlegetal vast.** Een SHA-256-hash van het bestand bewijst later dat het niet is gewijzigd.
- **Corrigeer met een nieuw document.** Een onjuiste factuur wordt gevolgd door een creditnota en een nieuwe factuur; een herziene offerte is versie 2, met versie 1 nog beschikbaar. Er wordt niets overschreven.

Concepten zijn de uitzondering: een concept kan zo vaak als nodig op verzoek worden gerenderd, is duidelijk gemarkeerd als concept, en wordt nooit verstuurd.

## Sjablonen Die er Professioneel Uitzien

Het verschil tussen een document dat er gegenereerd uitziet en een document dat er professioneel uitziet, is vooral print-CSS.

**A4, niet Letter.** Stel `@page { size: A4; margin: 20mm 18mm; }` in. Standaardwaarden uit Amerikaanse voorbeelden leveren documenten op die op elke Europese printer met vreemde marges worden afgedrukt.

**Beheers paginagrenzen.** `break-inside: avoid` op tabelrijen, handtekeningblokken en adresblokken; `thead { display: table-header-group; }` zodat kolomkoppen op elke pagina van een lange tabel terugkomen.

**Kop- en voetteksten en paginanummers.** "Pagina 3 van 7" in de voettekst, met de bedrijfsgegevens en het documentnummer op elke pagina. Headless Chromium ondersteunt kop- en voettekstsjablonen precies hiervoor.

**Sluit lettertypen in.** Lever de lettertypebestanden mee met het sjabloon in plaats van te vertrouwen op wat de rendermachine heeft geïnstalleerd. Een ontbrekend lettertype valt stil terug, en een ontbrekend euroteken - "€" weergegeven als leeg vakje - komt verrassend vaak voor.

**Gebruik de locale.** Bedragen als € 1.250,50 en datums als 13 maart 2028 voor Nederlandse documenten, zoals het artikel over internationalisering in deze reeks beschrijft; de documenttaal volgt de instellingen van de klant in plaats van de interfacetaal van de gebruiker.

**Geef het sjabloon een versie.** Sla de sjabloonversie bij elk document op. Wanneer het ontwerp verandert, houden oude documenten hun oude uiterlijk omdat het opgeslagen bestanden zijn - en u kunt nog steeds zien welk sjabloon ze maakte.

## Archiveren en Toegankelijkheid

Twee standaarden zijn het kennen waard.

**PDF/A** is het archiefprofiel van pdf: lettertypen ingesloten, geen externe afhankelijkheden, geen functies die over twintig jaar misschien niet meer werken. Accountants, overheidsinstanties en sommige sectoren verwachten het voor stukken die moeten worden bewaard. De meeste renderdiensten en op Chromium gebaseerde tools kunnen met de juiste instellingen PDF/A-2b maken, of de uitvoer kan worden omgezet. Geeft u facturen of certificaten uit, maak dan PDF/A.

**Getagde pdf** bevat de documentstructuur - koppen, tabellen, leesvolgorde - zodat schermlezers haar kunnen interpreteren. Het artikel over de European Accessibility Act in deze reeks legt uit wanneer dit een verplichting wordt; documenten maken uit semantische HTML via Chromium brengt u het grootste deel van de weg, terwijl pdf's op basis van afbeeldingen dat nooit kunnen.

## Wanneer een Pdf Niet Genoeg Is: E-facturatie

Voor facturen in het bijzonder is een pdf steeds vaker maar de helft van het antwoord.

Nederlandse overheidsorganisaties - ministeries, gemeenten, provincies en veel semipublieke organisaties - eisen dat leveranciers e-facturen sturen: gestructureerde bestanden in het Europese standaardformaat, doorgaans UBL volgens het Nederlandse NLCIUS-profiel, geleverd via het Peppol-netwerk in plaats van per e-mail. Een pdf als bijlage bij een e-mail wordt door hun verwerkingssystemen niet geaccepteerd. Grotere private bedrijven vragen steeds vaker hetzelfde, omdat een gestructureerde factuur direct in hun crediteurenproces gaat zonder dat iemand haar overtypt, en de Europese beweging richting verplichte e-facturatie tussen bedrijven maakt dit een richting in plaats van een optie.

Drie gevolgen voor documentgeneratie:

- **Maak het gestructureerde bestand uit dezelfde momentopname als de pdf.** De UBL-factuur en de pdf moeten tot op de cent overeenkomen, en dat doen ze als beide uit de opgeslagen factuurdata worden gemaakt in plaats van uit aparte query's.
- **Neem de pdf op als leesbare versie.** UBL staat toe dat de pdf wordt meegestuurd, zodat de ontvanger beide heeft.
- **Gebruik een accesspoint voor Peppol.** Versturen via Peppol vereist een gecertificeerd accesspoint; voor een klein product is dat een dienst waarop u aansluit, vaak dezelfde die de boekhoudsoftware van uw klanten al gebruikt, in plaats van iets wat u bouwt.

Verkopen uw klanten aan overheidsorganisaties - zorgaanbieders, installateurs, adviesbureaus en opleiders doen dat vaak - dan wordt e-facturatie een van de eerste enterprise-eisen die ze bij u neerleggen, en het is veel eenvoudiger wanneer facturen al onveranderlijke, vastgelegde records zijn.

## Het Beveiligingsrisico in het Renderen van HTML

HTML renderen op een server brengt een risico mee dat makkelijk wordt gemist: het sjabloon bevat data die gebruikers hebben getypt.

Een klantnaam, een adresregel of een opmerking met HTML erin - `<img src="http://169.254.169.254/latest/meta-data/">` of `<iframe src="file:///etc/passwd">` - wordt door de headless browser geïnterpreteerd wanneer het document wordt gerenderd. Afhankelijk van de opzet haalt de browser op uw server interne URL's op, leest hij lokale bestanden of doet hij verzoeken naar willekeurige sites, en kan het resultaat zelfs in de pdf verschijnen. Dit is server-side request forgery via de documentgenerator, en het is in veel producten gevonden.

Vier maatregelen dichten het:

- **Escape alle gebruikersdata** in sjablonen. Gebruik een sjabloonengine die standaard escapet, en voeg gebruikersinhoud nooit in als ruwe HTML.
- **Schakel netwerktoegang uit** voor het renderproces, behalve naar de specifieke hosts die het nodig heeft - meestal geen, als lettertypen en afbeeldingen zijn meegeleverd.
- **Schakel JavaScript uit** in sjablonen, tenzij het nodig is.
- **Draai de renderer geïsoleerd** - een eigen container, geen inloggegevens, geen toegang tot uw database of intern netwerk.

Behandel de renderer zoals u elk onderdeel behandelt dat onbetrouwbare invoer verwerkt, zoals de artikelen over bestandsuploads in deze reeks beschrijven.

## Opslag, Toegang en Levering

Gemaakte documenten zijn bestanden, en de opslagartikelen in deze reeks gelden volledig.

Sla ze op in een privébucket onder een pad met de organisatie voorop - `org/{id}/invoices/{invoice}/v1.pdf` - en lever ze via kortlevende ondertekende URL's nadat is gecontroleerd dat de gebruiker dat document mag zien. Mail een link naar het document in het product in plaats van het als bijlage te sturen, behalve waar de ontvanger de bijlage echt nodig heeft - facturen die naar het crediteurenadres van een klant gaan, zijn de gangbare uitzondering, en dan alleen de factuur zelf.

Bedenk dat documenten persoonsgegevens zijn wanneer ze namen en adressen bevatten. Ze horen in uw bewaarregister, ze moeten in volledige accountexports worden opgenomen, zoals het artikel over data-exports beschrijft, en ze moeten worden verwijderd wanneer de bewaartermijn eindigt - behalve waar de bewaarplicht u verplicht ze te houden, wat een reden is om de bewaarregel per documenttype op te schrijven.

## Bulk en Gepland Genereren

Het einde van de maand brengt het volumeprobleem: vierhonderd facturen tegelijk maken en versturen, of elke maandag een rapport per locatie.

Zet ze in de wachtrij als afzonderlijke documenttaken in plaats van één grote taak, zodat één mislukking één document raakt. Beperk het aantal gelijktijdige renders tot wat de renderer aankan - Chromium gebruikt per pagina flink wat geheugen - en bewaak de lengte van de wachtrij. Een run aan het einde van de maand die drie uur duurt omdat alles achter elkaar in één proces werd gerenderd, is een gangbare ontdekking de eerste keer dat het gebeurt.

Leg voor bulkruns een batch vast, met aantallen gerenderde, mislukte en verstuurde documenten, zodat degene die de run startte kan zien dat alle vierhonderd echt zijn verstuurd.

## Documenten Testen

Documenten zijn makkelijk kapot te maken zonder dat iemand het merkt: een sjabloonwijziging verschuift een kolom, een lange productnaam duwt het totaal naar een nieuwe pagina, een lettertype laadt niet.

Drie soorten tests helpen:

- **Controles op tekst.** Haal de tekst uit een gemaakte pdf en controleer dat factuurnummer, totalen, btw-bedragen en datums aanwezig en juist zijn.
- **Visuele snapshots.** Render een set representatieve documenten - één regel, veertig regels, een lange klantnaam, een regel met nultarief - naar afbeeldingen en vergelijk ze met goedgekeurde snapshots, met een fout bij significante verschillen.
- **Randgevallen.** Een document dat precies op een paginagrens valt, tekens als ë, ß en €, en een gebruikerswaarde met HTML die als letterlijke tekst moet verschijnen.

## Dit Inrichten

Voor een Lovable-product dat documenten uitgeeft, is dit doorgaans drie tot vijf dagen: renderen op de server met headless Chromium in een geïsoleerde container of een EU-renderdienst, genereren als achtergrondtaken met idempotente documentrecords, nieuwe pogingen en waarschuwingen, uitgegeven documenten één keer gemaakt en opgeslagen met een momentopname van de data, sjabloonversie en controlegetal, correcties als nieuwe versies of creditnota's, print-CSS voor A4 met beheerste paginagrenzen, herhaalde tabelkoppen, paginanummers en ingesloten lettertypen, opmaak volgens de locale, PDF/A voor stukken die moeten worden gearchiveerd, e-facturen in UBL uit dezelfde momentopname waar klanten aan overheden leveren, ge-escapete sjablonen met netwerk en JavaScript uitgeschakeld in de renderer, privéopslag met ondertekende URL's en links in plaats van bijlagen, bewaarregels per documenttype, bulkgeneratie via de wachtrij met batchrapportage, en tests op tekst en visuele snapshots.

LaunchStudio bouwt dit wanneer documenten het deel van het product zijn dat klanten doorsturen naar hun eigen klanten. De engineers zijn van Manifera - elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Stuur ons een pdf die uw product heeft gemaakt](https://launchstudio.eu/nl/#contact) en wij vertellen u hoe hij is gemaakt.

## Echt voorbeeld

### Een Offerte Die Veranderde Nadat Ze Was Getekend

Hidde Brouwer bouwde Offertetool in Lovable: offertes en orderbevestigingen voor keuken- en badkamerinstallateurs, gebruikt door 38 bedrijven waarvan de verkopers grotendeels op locatie bij klanten werken.

Offertes werden in de browser gemaakt met `html2canvas` en `jsPDF`. Offertes van meerdere pagina's sneden tabelrijen doormidden bij paginagrenzen, de tekst kon niet worden geselecteerd, en op telefoons - waar de meeste offertes werden gemaakt, in de keukens van klanten - faalden offertes van meer dan drie pagina's zonder foutmelding. Elke download rendeerde de offerte opnieuw uit de actuele database.

Het probleem werd duur toen een installateur zijn prijslijst aanpaste. Een huiseigenaar die in januari een offerte had getekend, downloadde haar in april opnieuw om met de factuur te vergelijken en vond andere prijzen: de download van april was gerenderd uit de nieuwe prijslijst. Het verschil was €2.300, de huiseigenaar had de pdf van april, en de installateur had niets om te laten zien wat er in januari was verstuurd. Ze hielden zich aan de lagere prijs.

Vier werkdagen: het renderen verplaatst naar een headless Chromium-container achter een takenwachtrij, met documentrecords, nieuwe pogingen en waarschuwingen; offertes en orderbevestigingen één keer gemaakt bij het versturen en opgeslagen met een momentopname van de regels en prijzen, de sjabloonversie en een SHA-256-controlegetal; herzieningen uitgegeven als nieuwe versies, met eerdere versies bewaard en zichtbaar; print-CSS voor A4 met herhaalde tabelkoppen, rijen die nooit worden gesplitst, paginanummers en de gegevens van de installateur op elke pagina, en ingesloten lettertypen; offertes gemaakt als PDF/A-2b; gebruikersinhoud ge-escaped, met netwerktoegang en JavaScript uitgeschakeld in de renderer; privéopslag met ondertekende links; en tests op tekst en visuele snapshots voor offertes van één en van veertig pagina's en lange productomschrijvingen.

**Resultaat:** offertes van veertig pagina's zijn in ongeveer zes seconden klaar en werken vanaf elke telefoon, omdat de telefoon het werk niet meer doet. Elke offerte die sindsdien is verstuurd, kan precies worden getoond zoals ze is verstuurd, met haar controlegetal. Twee installateurs hebben de opgeslagen versies sindsdien gebruikt om meningsverschillen binnen een dag in hun voordeel te beslechten.

> *"De klant had een pdf van onze offerte met prijzen die we nooit hadden aangeboden. We hadden hem zelf gemaakt, drie maanden later, uit de nieuwe prijslijst."*
> - **Hidde Brouwer, Oprichter, Offertetool (Veenendaal)**

**Kosten & Doorlooptijd:** €3.900 (renderen op de server met takenwachtrij, onveranderlijke documenten met versies, momentopnamen en controlegetallen, A4-printsjablonen met paginering en ingesloten lettertypen, PDF/A-uitvoer, isolatie van de renderer en escaping, ondertekende opslag, snapshot-testsuite) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Waarom zijn pdf's die in de browser worden gemaakt een probleem?

Het zijn meestal schermafbeeldingen: tekst kan niet worden geselecteerd of door software worden gelezen, pagina's breken door inhoud heen, grote documenten falen op telefoons, en ze kunnen niet door achtergrondtaken worden gemaakt.

### Wat is de beste manier om pdf's te maken voor een Lovable-app?

Voor de meeste producten HTML-sjablonen die door headless Chromium in een container of een EU-renderdienst naar pdf worden gerenderd, als achtergrondtaak. Programmatische bibliotheken passen bij eenvoudige documenten met een vaste layout.

### Waarom mag een uitgegeven document nooit opnieuw worden gemaakt?

Omdat het dan verandert zodra de onderliggende data verandert, zodat niemand kan bewijzen wat er is verstuurd. Maak het één keer, sla het bestand op met een momentopname en controlegetal, en geef correcties uit als nieuwe versies of creditnota's.

### Moeten facturen PDF/A zijn?

Niet altijd wettelijk, maar PDF/A is het archiefformaat dat garandeert dat het document over jaren nog wordt weergegeven, en het is wat accountants en overheidsinstanties verwachten voor stukken die u moet bewaren.

### Wat is het beveiligingsrisico van HTML naar pdf renderen?

Gebruikersdata die als HTML wordt gerenderd, kan de browser op de server interne URL's of lokale bestanden laten ophalen. Escape alle gebruikersinhoud, schakel netwerktoegang en JavaScript uit in de renderer, en draai hem geïsoleerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zijn pdf's uit de browser een probleem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het zijn meestal afbeeldingen: niet-selecteerbare tekst, kapotte paginering, mislukkingen op telefoons bij grote documenten, en geen mogelijkheid om ze in achtergrondtaken te maken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moet een Lovable-app pdf's maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Render HTML-sjablonen met headless Chromium in een container of EU-dienst als achtergrondtaak; gebruik programmatische bibliotheken voor eenvoudige vaste layouts."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom mogen uitgegeven facturen en offertes nooit opnieuw worden gemaakt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Opnieuw gemaakte documenten veranderen mee met de data, zodat niemand kan bewijzen wat er is verstuurd; sla het bestand één keer op met een momentopname en controlegetal."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten facturen als PDF/A worden opgeslagen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "PDF/A garandeert weergave op lange termijn en is wat accountants en overheidsinstanties verwachten voor stukken die bewaard moeten worden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het beveiligingsrisico van HTML naar pdf renderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet-ge-escapete gebruikersdata kan de renderer interne URL's of bestanden laten ophalen; escape inhoud, schakel netwerk en JavaScript uit, en isoleer de renderer."
      }
    }
  ]
}
</script>
