---
Titel: "Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming"
Trefwoorden: ai app productieproblemen, ai recruitment tool, cv data avg, kandidaat toestemming, eu ai act werving, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming",
  "description": "Recruitmenttools die zijn gebouwd met AI verwerken cv's, contactgegevens en vaak gevoelige persoonsgegevens van kandidaten. Dit artikel behandelt de specifieke productieproblemen bij AI-werving: cv-opslag, bewaartermijnen, toestemming, recruiter-autorisaties, AI-selectieregels en kandidaatrechten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-25",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/building-an-ai-recruitment-tool-ai-app-production-problems-with-cvs-and-consent" }
}
</script>

Een oprichtster in Friesland uploadde haar eerste echte batch cv's — 180 sollicitaties voor vacatures in de installatietechniek en lasbouw — in de wervingstool die ze in Lovable had gebouwd. De AI-matching functioneerde uitstekend. Recruiters waren laaiend enthousiast. Totdat een kandidaat verbaasd opbelde met de vraag waarom een bedrijf waar hij nog nooit van had gehoord hem plotseling benaderde. Toen pas realiseerde zij zich dat elke recruiter op het platform door álle cv's kon zoeken, inclusief kandidaten die gericht op één specifieke vacature bij één specifiek bedrijf hadden gesolliciteerd. Een klassiek voorbeeld van de acute productieproblemen waar AI-recruitmenttools tegenaan lopen.

Als u een AI-recruitmenttool bouwt, bepalen deze uitdagingen of u veilig live kunt gaan: niet of de matching algoritmes werken, maar of kandidaatdata exact wordt behandeld zoals werkzoekenden, werkgevers en toezichthouders dat wettelijk eisen.

## Waarom CV's Gevoeliger Zijn Dan Ze Lijken

Een curriculum vitae staat per definitie bol van de persoonsgegevens: naam, woonadres, telefoonnummer, e-mailadres, geboortedatum, arbeidsverleden, diploma's en vaak een pasfoto. Daarnaast bevatten veel cv's indirecte gegevens die kandidaten liever niet met iedereen delen — gaten in de loopbaan door ziekte, nationaliteit, religieuze overtuiging afgeleid uit verenigingswerk of lidmaatschap van een vakbond. Een deel hiervan kwalificeert onder Artikel 9 van de AVG als bijzondere categorieën van persoonsgegevens, waarvoor een verzwaard beschermingsregime geldt.

Bovendien is er bij werving sprake van een inherente machtsongelijkheid. Een sollicitant kan gegevens nauwelijks weigeren aan een potentiële werkgever. Toezichthouders houden het gebruik en bewaren van recruitmentdata daarom scherp in de gaten.

## Probleem 1: Iedereen Kan Alles Zien

AI-gegenereerde recruitment-apps bevatten doorgaans één centrale databasetabel voor cv's met een algemene zoekfunctie. De visuele interface toont een recruiter wellicht alleen de kandidaten voor zijn eigen vacature, maar de onderliggende API levert simpelweg de volledige database terug. In een omgeving met meerdere werkgevers of wervingsbureaus leidt dit ertoe dat sollicitanten zichtbaar worden voor bedrijven waar zij nooit toestemming aan hebben gegeven.

In een productieklare architectuur is autorisatie strikt afgeschermd: de data van een kandidaat is uitsluitend zichtbaar voor de specifieke organisatie waarop is gesolliciteerd, afgedwongen op databaseniveau (Row-Level Security). Talentpools — waarin kandidaten instemmen om ook voor andere functies te worden benaderd — vereisen een afzonderlijke, expliciete toestemming.

## Probleem 2: CV's Onbeveiligd en voor Eeuwig Opgeslagen

Geüploade cv's belanden in AI-prototypes vaak in openbare cloudopslag (storage buckets) met publiek toegankelijke URL's, omdat dit de eenvoudigste manier is om een PDF in de browser te tonen. Iedereen met de directe link — of iedereen die het bestandsnaampatroon raadt — kan ze zonder authenticatie downloaden. En er wordt nooit iets verwijderd.

Een veilige inrichting vereist private cloudopslag met tijdelijk ondertekende links (signed URLs), automatische malwarescans bij het uploaden en geautomatiseerde retentieregels. De richtlijnen van de Autoriteit Persoonsgegevens stellen dat sollicitatiegegevens doorgaans binnen vier weken na afwijzing moeten worden gewist, of maximaal één jaar mogen worden bewaard mits de kandidaat hiervoor expliciet toestemming heeft gegeven. Uw software moet dit geautomatiseerd uitvoeren; recruiters doen dit in de praktijk nooit handmatig.

## Probleem 3: Toestemming Die Niet Wordt Gelogd

"Door te solliciteren gaat u akkoord met onze privacyverklaring" geldt juridisch niet als een rechtsgeldige toestemmingsregistratie. Wanneer u kandidaten opneemt in een brede talentpool, profielen deelt met andere opdrachtgevers of data gebruikt voor het hertrainen van uw matchingmodel, heeft u een aantoonbare, ondubbelzinnige keuze nodig: wat heeft de kandidaat goedgekeurd, op welk tijdstip en bij welke versie van de voorwaarden? Bovendien moet een kandidaat die toestemming net zo eenvoudig kunnen intrekken als verlenen.

## Probleem 4: AI-Selectieregels en de EU AI Act

Werving en selectie is een van de domeinen die door de Europese AI-verordening (EU AI Act) expliciet als 'hoog risico' zijn geclassificeerd wanneer AI-systemen worden ingezet om kandidaten te screenen, te filteren of te rangschikken. Indien uw applicatie sollicitanten automatisch beoordeelt of afwijst, gelden er zware verplichtingen rondom risicomanagement, menselijk toezicht, transparantie en logging. Daarnaast verbiedt Artikel 22 van de AVG geautomatiseerde besluitvorming met rechtsgevolgen of vergelijkbare wezenlijke gevolgen, zoals een automatische afwijzing zonder tussenkomst van een mens.

In de praktijk moet een productieklare wervingsapplicatie altijd een mens in de besluitvormingscyclus (human-in-the-loop) houden, recruiters uitleggen wáárom een bepaalde matchscore tot stand is gekomen, beschermde persoonskenmerken uitsluiten van het algoritme (zowel direct als via proxies zoals pasfoto's of postcodes), scoringslogica nauwkeurig loggen en kandidaten informeren dat AI wordt gebruikt ter ondersteuning.

## Probleem 5: Inzage- en Verwijderingsrechten van Sollicitanten

Kandidaten kunnen te allen tijde inzage, correctie of verwijdering van hun gegevens eisen. Ook willen afgewezen kandidaten regelmatig weten welke gegevens over hen zijn vastgelegd. Een volwassen tool heeft een functie nodig om alle data over één persoon — sollicitaties, interne notities, gespreksverslagen en bestanden — direct te lokaliseren, te exporteren en permanent te wissen, inclusief uit zoekindexen en eventuele vector-embeddings die van het cv zijn gemaakt.

## Probleem 6: Notities van Recruiters

Recruiters maken aantekeningen. Soms zijn die notities ondoordacht of bevatten ze subjectieve, gevoelige observaties. Sollicitanten hebben het wettelijk recht om deze notities op te vragen via een AVG-inzageverzoek. De software moet notities strikt binnen de werkgeversorganisatie houden, recruiters stimuleren om feitelijk te formuleren en deze notities naadloos meenemen in geautomatiseerde opschoonprocedures.

## Hoe een Productieklare AI-Recruitmenttool Eruitziet

- Toegangscontrole per organisatie, direct afgedwongen in de database
- Private opslag van cv-bestanden, beveiligd met signed URL's en virusscans
- Automatische gegevensverwijdering conform AVG-termijnen
- Gelogde, intrekbare toestemmingsregistratie voor talentpools
- Menselijke verificatie van AI-aanbevelingen, inclusief toelichting en auditlogs
- Eenvoudig zoeken, exporteren en permanent wissen van kandidaatdata
- Hosting binnen de EU, inclusief de API's voor taalmodellen
- Een complete verwerkersovereenkomst voor elke partij die cv-data aanraakt

## Het Inrichten van een Waterdichte Toestemmingsflow

Toestemming wordt in de recruitmentwereld vaak verkeerd begrepen. Voor het verwerken van een directe sollicitatie op een specifieke vacature is de rechtsgrondslag niet 'toestemming', maar 'het nemen van precontractuele maatregelen op verzoek van de betrokkene'. Toestemming is uitsluitend vereist voor zaken die daarbuiten vallen: het bewaren van het profiel in een bredere talentpool, het doorsturen naar andere werkgevers of het gebruik van gegevens voor modeltraining. Een conforme toestemmingsflow werkt daarom als volgt:

- Legt in begrijpelijke taal uit wat er met de directe sollicitatie gebeurt, zonder om toestemming te vragen.
- Biedt **afzonderlijke, niet-aangevinkte keuzevakjes** voor de talentpool, doorplaatsing en kwaliteitsverbetering.
- Slaat elke keuze op inclusief de exacte getoonde wettekst, versienummer en tijdstempel.
- Biedt kandidaten de mogelijkheid om hun keuzes met één klik te herzien via hun profiel of een link onderaan e-mails.
- Verwijdert een kandidaat bij intrekking direct automatisch uit alle overkoepelende overzichten.

## Uitlegbare AI-Matchscores

Wanneer uw applicatie kandidaten rangschikt, zullen zowel werkgevers als sollicitanten vragen naar de onderbouwing. Een transparante score toont exact welke functie-eisen matchen (certificaten, jaren relevante ervaring, talenkennis, regio) en welke onderdelen ontbreken, in plaats van één mystiek percentage. Beperk de input voor het algoritme strikt tot vacature-relevante criteria, log het versienummer van het prompt- of selectiemodel en behandel scores altijd als adviserend: de recruiter beslist, het algoritme ondersteunt. Deze opzet voldoet aan de eisen van de EU AI Act rondom transparantie en versterkt het vertrouwen van recruiters in uw platform.

## Indirecte Discriminatie (Proxy Bias) Voorkomen

Zelfs wanneer beschermde kenmerken expliciet worden weggelaten, kunnen andere datavelden fungeren als proxy: postcodes (voor afkomst of inkomensniveau), afstudeerjaren (voor leeftijd), pasfoto's (voor geslacht, etniciteit en leeftijd), en loopbaangaten (voor zwangerschapsverlof of chronische ziekte). Praktische voorzorgsmaatregelen zijn onder meer: pasfoto's en geboortedata strikt verbergen voor het AI-matchingmodel, reistijdcategorieën gebruiken in plaats van exacte postcodes, en de scoringsuitkomsten periodiek controleren op onevenredige afwijkingen. Het is aanzienlijk eenvoudiger om dit vanaf de ontwerpfase in te bouwen dan achteraf te moeten verklaren waarom een model bepaalde groepen systematisch benadeelde.

## Geautomatiseerde Retentie in de Praktijk

Bewaartermijnen werken in de praktijk alleen wanneer ze geautomatiseerd worden uitgevoerd. Een beproefde indeling:

| Gegevenscategorie | Standaard bewaartermijn | Trigger voor verwijdering |
| --- | --- | --- |
| Sollicitatie op specifieke vacature | Maximaal 4 weken na afronding procedure | Sluiting van de vacature |
| Talentpool-profiel | Maximaal 12 maanden met toestemming | Registratiedatum; notificatie vóór verloop |
| Recruiter-notities | Gelijk aan de bijbehorende sollicitatie | Gekoppeld aan de sollicitatierecord |
| CV-documenten en vectoren | Gelijk aan het kandidaatprofiel | Gelijktijdig gewist met profiel |
| Auditlogs | Langere termijn, geanonimiseerd | Vastgelegd in beveiligingsbeleid |

Een nachtelijke achtergrondtaak handhaaft deze regels en genereert een auditlog. Als een kandidaat vraagt: "hebben jullie mijn cv nog?", is het antwoord direct paraat en feitelijk juist.

## Afscheiding Tussen Werkgevers en Bureaus

Op een platform dat meerdere werkgevers bedient, moet de datascheiding waterdicht zijn: een werkgever ziet uitsluitend sollicitanten op de eigen vacatures en, uitsluitend na expliciete instemming, goedgekeurde talentpool-kandidaten; wervingsbureaus zien enkel kandidaten die zij zelf hebben aangedragen. Dwing deze regels af in de database (PostgreSQL RLS), pas ze toe op zoekindexen en vector-databases en valideer ze via geautomatiseerde beveiligingstests. Vrijwel alle datalekken in recruitmentsoftware ontstaan doordat zoekindexen niet tenant-gescheiden zijn opgezet.

## Hoe LaunchStudio Helpt

LaunchStudio implementeert deze compliance- en beveiligingsmaatregelen zonder dat de gebruiksvriendelijke interface van uw recruitmenttool verloren gaat. Wij zorgen voor de vaak over het hoofd geziene details: het verwijderen van cv-teksten uit foutregistratiesystemen, het configureren van zero-data retention op externe AI-API's, en het waarborgen dat verwijderingen daadwerkelijk doorwerken in vector-databases en back-upbestanden.

Achter LaunchStudio staat Manifera's team van meer dan 120 senior software engineers, met 11+ jaar ervaring verspreid over meer dan 160 projecten. Manifera heeft diepe wortels in complexe HR-systemen en datagedreven applicaties, en CEO Herre Roelevink's achtergrond in cybersecurity waarborgt een aanpak waarbij autorisatie, encryptie en auditability vanaf het fundament worden ingebouwd. De technische realisatie vindt plaats in ons softwarecentrum in Ho Chi Minhstad, met accountmanagement en ondersteuning via de Herengracht 420 in Amsterdam. Bekijk onze ervaring op het gebied van [softwareontwikkeling op maat bij Manifera](https://www.manifera.com/services/custom-software-development/).

Staan de eerste cv's al in uw testomgeving? [Plan vandaag nog een vrijblijvend adviesgesprek van 15 minuten](https://launchstudio.eu/nl/#contact) om onaangename verrassingen te voorkomen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Technisch Wervingsplatform in Friesland

Sophie Lambrecht, voorheen eigenares van een uitzendbureau voor technische vakmensen in Leeuwarden, bouwde Vakkracht met behulp van Lovable: een wervingsplatform waar installatie-, las- en bouwbedrijven vacatures plaatsen en een AI-model binnenkomende cv's matcht op harde eisen zoals VCA-certificaten, lasdiploma's en rijbewijzen. Twaalf installatiebedrijven en twee regionale uitzendbureaus sloten zich in het eerste kwartaal aan, en circa 1.400 vakmensen solliciteerden via het platform.

De klacht van een sollicitant die werd benaderd door een onbekend bedrijf bracht het balletje aan het rollen. Een security review door LaunchStudio bracht aan het licht dat alle aangesloten recruiters via de API door álle sollicitanten konden zoeken; de geüploade PDF-bestanden stonden in een publieke Amazon S3 bucket met voorspelbare bestandsnamen; data werd nooit gewist; het vinkje voor opname in de talentpool stond standaard aangevinkt en werd nergens in de database gelogd; het AI-matchingmodel wees kandidaten met een score onder de 40% automatisch af zonder menselijke tussenkomst; en volledige cv-teksten werden onversleuteld weggeschreven in de foutopsporingsdienst van derden zodra het parseren mislukte.

Binnen elf werkdagen voerde het engineeringteam van LaunchStudio strikte Row-Level Security in per werkgeversorganisatie, verplaatste alle documenten naar een private bucket met tijdelijk ondertekende URL's en antiviruscontrole, configureerde geautomatiseerde dataverwijdering na vier weken (of twaalf maanden met expliciete toestemming), verving de automatische afwijzing door een review-wachtrij voor recruiters inclusief toelichting op de matchscore, filterde persoonsgegevens uit foutlogs en ontwikkelde een export- en verwijderknop die persoonsgegevens direct wiste uit zowel PostgreSQL als de vector-database.

**Resultaat:** Vakkracht informeerde de betrokken kandidaten en de toezichthouder transparant en ontving geen boetes of verdere klachten. Vervolgens sloot een groot regionaal detacheringsbureau — dat eerder afhaakte wegens privacyzorgen — zich alsnog aan, waardoor het platform binnen zes maanden doorgroeide naar 31 aangesloten werkgevers.

> *"Het AI-matchingalgoritme was het slimme onderdeel, en dat was waar niemand zich druk om maakte. Iedereen maakte zich zorgen over wie de cv's kon inzien — en daar hadden ze volkomen gelijk in."*
> — **Sophie Lambrecht, Oprichter, Vakkracht (Leeuwarden)**

**Kosten & Tijdlijn:** €3.300 (Launch Ready-pakket met multi-tenant databescherming, private opslag, geautomatiseerde retentie, toestemmingslogging en AI-toezichtflow) — opgeleverd binnen 11 werkdagen.

## Veelgestelde Vragen

### Hoe lang mag een AI-recruitmenttool cv's van sollicitanten bewaren?

Volgens de richtlijnen van de Autoriteit Persoonsgegevens moeten sollicitatiegegevens doorgaans binnen vier weken na het beëindigen van de sollicitatieprocedure worden verwijderd, tenzij de kandidaat expliciet toestemming geeft om de gegevens maximaal één jaar te bewaren voor toekomstige vacatures. Automatiseer deze retentie direct in uw software.

### Is de EU AI Act van toepassing op een kleine recruitment-startup?

Zodra uw tool AI inzet voor het screenen, filteren of rangschikken van sollicitanten, valt dit onder de 'hoog-risico'-classificatie van de EU AI Act. Het borgen van menselijk toezicht, uitlegbare matchscores en auditlogs vormen nu al essentiële randvoorwaarden.

### Mogen sollicitanten inzage vragen in de interne notities van recruiters?

Ja. Op grond van het inzagerecht onder de AVG hebben kandidaten recht op inzage in alle persoonsgegevens die over hen worden verwerkt, inclusief gespreksnotities en evaluaties. De software moet deze notities per kandidaat snel kunnen verzamelen en exporteren.

### Welke meerwaarde biedt de achtergrond van Manifera voor recruitment-platforms?

Sollicitatiegegevens zijn uiterst privacygevoelig. Dankzij de cybersecurity-expertise van CEO Herre Roelevink en Manifera's ervaring met enterprise HR-systemen worden multi-tenant datascheiding, encryptie en geautomatiseerde retentie vanaf de basis ingebouwd.

### Helpt een zorgvuldige omgang met cv-data bij de online vindbaarheid van mijn platform?

Zeker. Werkgevers en kandidaten zoeken actief naar betrouwbare partijen en hechten veel waarde aan transparantie. Heldere privacyvoorwaarden en een vlekkeloze reputatie zonder datalekken dragen positief bij aan aanbevelingen door zowel zoekmachines als AI-zoeksystemen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang mag een AI-recruitmenttool cv's van sollicitanten bewaren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standaard maximaal 4 weken na afloop van de sollicitatieprocedure, of tot 1 jaar met expliciete toestemming van de kandidaat. Richt dit geautomatiseerd in." }
    },
    {
      "@type": "Question",
      "name": "Is de EU AI Act van toepassing op een kleine recruitment-startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, AI die kandidaten beoordeelt of filtert geldt als hoog risico. Menselijk toezicht, verklaarbare scores en proceslogging zijn verplicht." }
    },
    {
      "@type": "Question",
      "name": "Mogen sollicitanten inzage vragen in de interne notities van recruiters?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, op grond van het AVG-inzagerecht kunnen interne notities worden opgevraagd. Zorg dat deze per kandidaat exporteerbaar en wisbaar zijn." }
    },
    {
      "@type": "Question",
      "name": "Welke meerwaarde biedt de achtergrond van Manifera voor recruitment-platforms?",
      "acceptedAnswer": { "@type": "Answer", "text": "Cybersecurity-expertise en ervaring met HR-systemen zorgen dat autorisatie, gegevensretentie en encryptie direct solide worden neergezet." }
    },
    {
      "@type": "Question",
      "name": "Helpt een zorgvuldige omgang met cv-data bij de online vindbaarheid van mijn platform?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, betrouwbare platforms met transparante verwerking en een vlekkeloos trackrecord genieten de voorkeur van zakelijke klanten en AI-zoekmachines." }
    }
  ]
}
</script>
