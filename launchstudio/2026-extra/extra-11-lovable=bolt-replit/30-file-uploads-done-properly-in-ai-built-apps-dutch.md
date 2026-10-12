---
Titel: "Supabase-beveiliging: Bestandsuploads zoals het hoort"
Trefwoorden: supabase beveiliging, validatie bestandsupload, gesigneerde urls vervaltijd, exif metadata strippen, beheer opslagquotum, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Supabase-beveiliging: Bestandsuploads zoals het hoort

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase-beveiliging: Bestandsuploads zoals het hoort",
  "description": "Uploadfuncties gegenereerd door AI-tools accepteren elk bestand, van iedereen, en serveren het openbaar aan de hele wereld. Een praktische gids voor validatie, opslagstructuur, gesigneerde toegang, metadata strippen, quota en geautomatiseerd opruimen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/file-uploads-done-properly-in-ai-built-apps" }
}
</script>

Een foto die met een smartphone is gemaakt, bevat vrijwel altijd de exacte GPS-coördinaten van de locatie waar hij is geschoten. De meeste mensen weten dit vaag. Maar schokkend weinig oprichters realiseren zich dat hun applicatie die coördinaten open en bloot aan de wereld toont, simpelweg omdat de door AI gegenereerde uploadfunctionaliteit het bestand exact zo opslaat als het binnenkwam en direct openbaar serveert aan iedereen met de URL.

Uploads lijken op het eerste gezicht de eenvoudigste functionaliteit van een app: een knop, een bestand selecteren en een URL terugkrijgen. In werkelijkheid vormen ze een van de dichtste concentraties van beveiligings- en financiële risico's in een applicatie. Ze combineren immers onbetrouwbare gebruikersinvoer, permanente dataopslag, openbare distributie en ongelimiteerde serverkosten in één enkele interactie. Dit is hoe een professionele uploadarchitectuur er werkelijk uitziet.

## Vier vragen die elke uploadfunctionaliteit moet beantwoorden

Nog vóór enige technische implementatie moet je vier vragen beantwoorden:
1. Welke bestandstypen worden geaccepteerd?
2. Hoe groot mogen bestanden maximaal zijn?
3. Wie mag ze naderhand inzien of downloaden?
4. Wanneer en hoe worden ze definitief verwijderd?

Een door AI gegenereerde uploadfunctie antwoordt standaard: "alles", "elke bestandsgrootte", "iedereen met de link" en "nooit".

Elk van die vier standaarden is een levensgroot probleem op zich, en samen versterken ze elkaar: een ongecontroleerd bestand, opgeslagen op een makkelijk te raden URL, zonder authenticatie opvraagbaar, tot in de eeuwigheid.

## Valideer altijd op de server, want de browser heb je niet in de hand

Controles in de browser — zoals het `accept`-attribuut op een HTML file-input of een JavaScript-check op de bestandsextensie — zijn louter interface-gemak voor goedwillende gebruikers. Iedereen met een terminal kan je upload-endpoint rechtstreeks aanroepen met elk willekeurig bestand.

Echte validatie vindt altijd plaats op de backend (of via beveiligde Edge Functions) en controleert minimaal drie zaken:
- Het werkelijke MIME-type op basis van de magic bytes in het bestand, niet de extensie (die immers eenvoudig hernoemd kan worden van `.exe` naar `.png`).
- De werkelijke bestandsgrootte tegen een harde limiet die jij hebt vastgelegd.
- Bij afbeeldingen: een controle of het bestand daadwerkelijk succesvol decodeert als een geldige afbeelding, in plaats van een kwaadaardig script dat zich voordoet als plaatje.

Het specifieke risico is helder: een kwaadaardig bestand dat geserveerd wordt vanaf jouw eigen domein erft direct het vertrouwen van jouw domein (cross-site scripting en phishing). Daarom moet "wij accepteren alleen afbeeldingen" worden afgedwongen op een plek die onmogelijk te omzeilen is.

## Opslagstructuur en bestandsnamen die niemand kan raden

Twee ontwerpkeuzes hebben hier enorme gevolgen voor je veiligheid:

**Gebruik nooit de originele bestandsnaam.** Deze kan botsen met een bestand van een andere gebruiker, vreemde tekens bevatten die paden breken, en is bovenal voorspelbaar. Genereer altijd een unieke, willekeurige UUID en bewaar de oorspronkelijke naam los in je database als metadata als je deze aan de gebruiker wilt tonen.

**Structureer mappen op basis van eigenaarschap.** Een directorystructuur die het account- of organisatie-ID bevat (bijvoorbeeld `/organisaties/{org_id}/facturen/{uuid}.pdf`), maakt het opstellen en controleren van autorisatieregels (zoals Storage RLS in Supabase) triviaal. Bestanden die willekeurig in één platte bucket worden gedumpt, maken van elke toegangsbeslissing een complex en foutgevoelig uitzonderingsgeval.

Gecombineerd zorgen deze maatregelen ervoor dat bestanden niet opsombaar (enumerable) zijn. Iemand die één bestandsadres bemachtigt, kan onmogelijk raden wat het volgende bestand is — wat direct misgaat als bestanden `factuur-1.pdf` tot en met `factuur-400.pdf` heten.

## Standaard privé, gesigneerd wanneer nodig

De allerbelangrijkste instelling in je cloudopslag: opslagbuckets die data van gebruikers bevatten moeten altijd **privé** zijn, nooit openbaar.

Toegang verloopt via gesigneerde URL's (Signed URL's) — tijdelijke, cryptografisch beveiligde adressen die jouw server on-the-fly genereert voor een specifiek bestand en een specifieke gebruiker, met een strikte vervaltijd (bijvoorbeeld 15 minuten). Die vervaltijd is cruciaal: een gesigneerde link die wordt doorgestuurd in een e-mail of ticket stopt na korte tijd met werken, terwijl een openbare URL voor altijd blijft circuleren.

Vóórdat je server zo'n tijdelijke link uitgeeft, controleert je applicatie eerst of de ingelogde gebruiker daadwerkelijk het recht heeft om dit bestand te zien. Die controle vormt je complete beveiligingsmodel — en dat is exact de stap die door AI gegenereerde code weglaat, omdat de enige gebruiker in de demo de ontwikkelaar zelf was.

## Metadata: Wat bestanden verklappen zonder dat je het doorhebt

Foto's van moderne smartphones bevatten uitgebreide EXIF-data: exacte GPS-coördinaten, tijdstempels, cameramodellen en soms zelfs gebruikersnamen. Documenten uit kantoorpakketten bevatten auteurs, revisiehistorie en soms teksten die visueel zijn gewist maar intern bewaard zijn gebleven.

Voor het overgrote deel van applicaties is de juiste standaard: **strip alle EXIF-metadata direct bij de upload** van afbeeldingen, en bewaar hooguit de oriëntatie-tag voor de juiste weergave. Verwerkt je platform documenten tussen partijen die elkaars identiteit of bewerkingsgeschiedenis niet mogen zien (zoals bij offertes of juridische stukken)? Zorg dan dat documenten geschoond worden vóór publicatie.

Dit is geen theoretisch risico. Een marktplaats die originele foto's serveert, publiceert feitelijk het thuisadres van elke verkoper aan iedereen die de foto downloadt.

## Malware-preventie, op een proportionele manier

Moet een kleine SaaS-applicatie uploads scannen op virussen? Het eerlijke antwoord hangt af van wat er met de bestanden gebeurt.

Worden geüploade bestanden uitsluitend bekeken door de gebruiker die ze zelf heeft geüpload (zoals persoonlijke administratie)? Dan ligt het risico primair bij die gebruiker zelf. Maar worden bestanden uitgewisseld tussen verschillende gebruikers — op een marktplaats, in een cliëntenportaal of in een berichtensysteem? Dan fungeert jouw platform als distributiekanaal voor malware en wordt scanning noodzakelijk.

Voor de meeste vroege applicaties volstaan proportionele maatregelen: strikte MIME-type validatie, bestanden serveren met HTTP-headers die dwingen tot downloaden in plaats van directe uitvoering in de browser (`Content-Disposition: attachment`), nooit geüploade code uitvoeren op je server, en scanning toevoegen zodra bestanden tussen accounts bewegen.

## Quota, want dataopslag en bandbreedte zijn niet gratis

Een uploadknop zonder limieten is een open uitnodiging voor torenhoge rekeningen. De kosten uiten zich op twee plekken: opslagruimte (die cumulatief toeneemt) en bandbreedte (egress, die optreedt telkens wanneer een bestand wordt opgevraagd).

Stel altijd een maximale bestandsgrootte per upload in en een maximaal totaalquotum per account. Bepaal vooraf wat er gebeurt als het quotum wordt bereikt — weiger verdere uploads netjes en bied een upgrade aan via een heldere UI-melding in plaats van een cryptische serverfout. Houd er rekening mee dat bandbreedte vaak veel duurder is dan opslag: een populair profiel met gigantische ongecomprimeerde foto's veroorzaakt een veelvoud aan dataverkeer.

Hier bewijst een automatische verwerkingspipeline direct zijn waarde: door bij upload direct geoptimaliseerde webformaten en verkleinde versies te genereren en die te serveren in plaats van het origineel, verlaag je het dataverkeer doorgaans met 80% tot 90%.

## Verwijderen en de weesbestanden die niemand ziet

Wanneer een gebruiker een advertentie, profiel of bericht verwijdert, verdwijnt het bijbehorende bestand dan ook uit de cloudopslag?

In vrijwel alle door AI gegenereerde applicaties luidt het antwoord: nee. De database-rij wordt netjes verwijderd (`DELETE FROM items`), maar het binaire bestand blijft voor altijd achter in de storage bucket. Jaar in jaar uit betaal je maandelijkse hostingkosten voor data die nergens meer aan gekoppeld is. Erger nog: gevoelige documenten die op verzoek van een klant verwijderd hadden moeten zijn (AVG-verwijderverzoek), blijven bereikbaar voor iedereen die het directe adres bewaart.

Bouw twee mechanismen in:
1. Zorg dat het verwijderen van een databaserecord automatisch een trigger activeert die het gekoppelde bestand uit de storage verwijdert (cascade).
2. Laat periodiek (bijvoorbeeld maandelijks) een opschoonscript draaien dat alle bestanden in storage opspoort die geen actieve referentie meer hebben in de database en ruim deze op. Draai dit één keer op je bestaande applicatie; het resultaat is vaak schokkend.

## Een controlelijst vóór lancering

- Type en bestandsgrootte worden server-side gevalideerd, waarbij de bestandsinhoud wordt gecontroleerd.
- Willekeurige bestandsnamen (UUID's), gestructureerd per gebruiker of organisatie.
- Storage buckets zijn strikt privé; toegang verloopt via kort geldige gesigneerde URL's na een autorisatiecheck.
- EXIF- en locatiedata van afbeeldingen worden bij de upload gestript.
- Geoptimaliseerde afbeeldingsformaten (zoals WebP) worden automatisch gegenereerd.
- Harde quota per account, met een duidelijke melding in de interface bij het bereiken van de limiet.
- Bestanden worden verwijderd zodra het databaserecord verdwijnt, aangevuld met weesbestand-opruiming.
- Een praktijktest: hernoem een `.exe` of `.html` bestand naar `.jpg`, probeer het te uploaden en verifieer dat het geweigerd wordt.

## De versie bouwen die standhoudt

Uploadfunctionaliteit is razendsnel in elkaar gezet met een prompt, maar complex om naderhand te repareren zodra er al tienduizenden bestanden in productie staan. Elke migratie moet dan immers rekening houden met historische data. LaunchStudio richt de professionele uploadarchitectuur in bovenop je bestaande frontend: server-side validatie, private buckets gestructureerd per account, gesigneerde toegang gekoppeld aan autorisatieregels, geautomatiseerd strippen van metadata, een optimalisatiepipeline voor webformaten, accountquota en grondige opruimscripts voor weesbestanden — inclusief een eenmalige opschoning van reeds opgeslagen bestanden.

De interface die je hebt gebouwd in Lovable blijft exact behouden, en de code blijft volledig gedocumenteerd en AI-leesbaar. Dit maakt deel uit van het [Launch Ready-pakket](https://launchstudio.eu/nl/#packages), gerealiseerd door de senior engineers van Manifera vanuit Amsterdam en Ho Chi Minhstad, met elf jaar productie-ervaring voor opdrachtgevers als Vodafone, TNO en CFLW.

Accepteert jouw applicatie bestanden en heb je nooit gecontroleerd wat er precies mee gebeurt? [Beschrijf je project](https://launchstudio.eu/nl/#contact) en ontvang binnen één werkdag een concrete analyse.

## Bestanden serveren: De helft die na de upload komt

Het beveiligen van de upload krijgt meestal alle aandacht; maar hoe je bestanden uitlevert (delivery) bepaalt je maandelijkse kosten en de ervaren snelheid van je app.

**Serveer afgeleide formaten, niet de originelen.** Genereer direct bij upload de exacte afmetingen die je frontend nodig heeft (thumbnails, previews) en serveer die. Dit levert de grootste besparing op dataverkeer op en versnelt de laadtijd op smartphones aanzienlijk.

**Gebruik moderne formaten.** Formaten zoals WebP en AVIF leveren drastisch kleinere bestanden op bij gelijke visuele kwaliteit.

**Cache agressief met onveranderlijke (immutable) bestandsnamen.** Omdat je bestandsnamen willekeurig zijn en nooit worden hergebruikt, verandert een bestand op een gegeven URL nooit meer. Dat betekent dat browsers en CDN's het bestand extreem lang mogen cachen. Vervangt een gebruiker zijn profielfoto? Dan krijgt hij simpelweg een nieuwe unieke URL in plaats van een verouderde gecachte versie.

**Plaats een CDN voor je opslag** zodra je gebruikers buiten je directe regio bedient. Dit verlaagt laadtijden en bespaart dure datatransfer vanaf je primaire storage bucket.

**Gebruik lazy-loading onder de vouw.** Een overzichtspagina met dertig afbeeldingen moet niet alle dertig zware bestanden binnenhalen vóórdat de bezoeker naar beneden scrolt.

**Houd rekening met de wisselwerking tussen gesigneerde URL's en caching.** Een gesigneerde link met een vervaltijd kan niet langer gecachet worden dan de geldigheid van de link zelf. Maak daarom een bewust onderscheid: publieke marketingafbeeldingen horen in een openbare, gecachete storage; vertrouwelijke documenten en privégegevens horen in een beveiligde, gesigneerde storage.

## Echt voorbeeld

### Een marktplaats die per ongeluk de woonadressen van verkopers publiceerde

Ravi Mehta bouwde Vintagehoek in Lovable: een lokale marktplaats voor tweedehands designmeubels in en rond Haarlem. Verkopers fotografeerden hun meubels thuis en plaatsten een advertentie; kopers zochten in het aanbod en maakten een afspraak om het meubel op te halen.

Tijdens een grondige technische inspectie kwamen drie pijnpunten naar voren:
1. De opslagkosten waren vier keer hoger dan logisch was voor het aantal advertenties, omdat alle foto's op maximale cameraresolutie werden opgeslagen en geserveerd, en omdat foto's van verwijderde advertenties nooit werden gewist.
2. Bestanden behielden hun oorspronkelijke uploadnaam, waardoor bestandsadressen eenvoudig te voorspellen waren.
3. De Supabase storage bucket was volledig openbaar en bevatte de originele, onbewerkte foto's inclusief embedded EXIF GPS-coördinaten. Iedere bezoeker kon de foto downloaden en tot op de meter nauwkeurig zien in welk woonhuis het dure meubelstuk stond — zelfs van advertenties die al maanden geleden waren gearchiveerd.

De alerte verkoopster die aan de bel trok, had haar eigen woonadres ontdekt via de fotodetails van haar advertentie.

In zes werkdagen werd het systeem herzien: alle EXIF-metadata wordt nu bij upload gestript; een geautomatiseerde pipeline genereert webversies (thumbnail, preview en detail) en verwijdert het zware origineel; de bucket werd strikt privé gemaakt met gesigneerde URL's die na vijftien minuten verlopen en uitsluitend na authenticatie worden verstrekt; bestandsnamen werden vervangen door willekeurige UUID's geordend per verkoper; bij het verwijderen van een advertentie worden foto's automatisch gewist; een eenmalig opschoonscript verwijderde met terugwerkende kracht circa 40% aan overbodige weesbestanden; en er werden harde quota per gebruikersaccount ingesteld.

**Resultaat:** de opslag- en bandbreedtekosten daalden met ruim 75%, pagina's laadden op smartphones binnen één seconde, en het gevaarlijke lekken van woonadressen werd voor zowel nieuwe als historische foto's definitief gedicht.

> *"Een verkoopster mailde me haar eigen adres en vroeg hoe mijn website dat wist. Zo ontdekte ik dat mijn applicatie al negen maanden lang de exacte woonadressen van verkopers aan het publiceren was."*
> — **Ravi Mehta, Oprichter, Vintagehoek (Haarlem)**

**Kosten & Doorlooptijd:** € 2.650 (server-side validatie, metadata strippen, afbeeldingspipeline, gesigneerde toegang, historische opschoning) — afgerond in 6 werkdagen.

## Veelgestelde vragen

### Is het controleren van de bestandsextensie voldoende validatie?
Nee, absoluut niet. Extensies kunnen eenvoudig worden hernoemd door een aanvaller. Valideer altijd het werkelijke MIME-type op de server aan de hand van de binaire inhoud, controleer of afbeeldingen daadwerkelijk decoderen en dwing een strikte maximale bestandsgrootte af.

### Moet mijn storage bucket openbaar of privé zijn?
Privé voor vrijwel alle door gebruikers geüploade data. Serveer bestanden via tijdelijk geldige, gesigneerde URL's die pas worden gegenereerd nadat je server heeft geverifieerd dat de opvrager het bestand mag inzien. Openbare buckets geven iedereen met de link voor altijd ongecontroleerde toegang.

### Welke metadata moet ik precies uit afbeeldingen strippen?
Bij foto's minimaal de GPS-locatiecoördinaten, tijdstempels en apparaatgegevens, waarbij je de oriëntatie-tag behoudt voor een correcte weergave. Bij documenten (zoals Word of PDF) moet je alert zijn op auteursnamen en verborgen revisiegeschiedenis.

### Heb ik automatische virus- en malwarescanning nodig?
Zelden als bestanden uitsluitend worden ingezien door de gebruiker die ze zelf heeft geüpload. Maar zodra bestanden worden gedeeld tussen verschillende gebruikers, fungeert jouw app als distributiekanaal en is scanning noodzakelijk, gecombineerd met veilige download-headers en strikte typebeperkingen.

### Waarom is mijn storage-factuur veel hoger dan mijn aantal bestanden verklaart?
Dit wordt vrijwel altijd veroorzaakt door het bewaren van gigantische originele resoluties en door weesbestanden van eerder verwijderde records die blijven rondhangen. Het genereren van webformaten en het eenmalig draaien van een opruimscript halveert de opslag vaak in één klap.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het controleren van de bestandsextensie voldoende validatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, absoluut niet. Extensies kunnen triviaal worden gewijzigd. Valideer het werkelijke MIME-type server-side aan de hand van binaire data en dwing strikte bestandsgroottelimieten af."
      }
    },
    {
      "@type": "Question",
      "name": "Moet mijn storage bucket openbaar of privé zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Privé voor alle gebruikersuploads, geserveerd via tijdelijke gesigneerde URL's na een autorisatiecontrole. Openbare buckets geven iedereen met de URL permanente en ongelimiteerde toegang."
      }
    },
    {
      "@type": "Question",
      "name": "Welke metadata moet ik precies uit afbeeldingen strippen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij foto's minimaal de GPS-locatiecoördinaten, tijdstempels en apparaatgegevens. Bij documenten moet je bedacht zijn op auteursnamen en verborgen revisiehistorie."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik automatische virus- en malwarescanning nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zelden als bestanden alleen door de uploader worden ingezien; noodzakelijk zodra bestanden tussen verschillende gebruikers worden uitgewisseld, naast strikte typebeperkingen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is mijn storage-factuur veel hoger dan mijn aantal bestanden verklaart?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel altijd door originele resoluties en weesbestanden van reeds verwijderde records; geoptimaliseerde webformaten en een opschoonscript verlagen de opslag drastisch."
      }
    }
  ]
}
</script>
