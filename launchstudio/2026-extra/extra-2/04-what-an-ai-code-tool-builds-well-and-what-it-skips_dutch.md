---
Titel: "Wat een AI-codetool goed bouwt, en wat het stilletjes overslaat"
Trefwoorden: ai code tool, ai coding, build ai, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Wat een AI-codetool goed bouwt, en wat het stilletjes overslaat

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat een AI-codetool goed bouwt, en wat het stilletjes overslaat",
  "description": "Mythen ontkracht over wat een AI-codetool daadwerkelijk levert, en een specifieke blik op waar een onbeschermde beheerdersroute zich verbergt.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-an-ai-code-tool-builds-well-and-what-it-skips"
  }
}
</script>

Elke AI-codetool op de markt van vandaag – v0, Bolt, Lovable, Cursor – is oprecht goed in waar het voor gebouwd is: het omzetten van een beschreven functie in werkende, visueel correcte code, snel. De verwarring begint wanneer oprichters die bekwaamheid stilletjes uitbreiden naar gebieden waar de tool nooit voor gebouwd is, zoals toegangsbeheer, misbruikpreventie, of de specifieke vraag wat er gebeurt wanneer een route wordt opgevraagd door iemand die het nooit verondersteld was te zien in de eerste plaats.

## Mythe: Een AI-codetool bouwt een volledige applicatie

**De realiteit:** het bouwt de applicatie die u specifiek heeft beschreven, wat iets smallers is. Als een oprichter "een beheerdersdashboard voor het beheren van gebruikers" beschrijft zonder ook te specificeren "en alleen beheerders zouden het moeten kunnen bereiken," is er een redelijke kans dat de resulterende code het dashboard correct rendert voor een beheerder. Het overweegt simpelweg niet wat een niet-geauthenticeerde of lagere-machtigingsbezoeker die dezelfde URL rechtstreeks typt zou zien, omdat dat scenario in de eerste plaats nooit onderdeel van de beschrijving was.

## Mythe: Als het niet gelinkt was in de navigatie, zal niemand het vinden

**De realiteit:** het verbergen van een route in de zichtbare gebruikersinterface is niet hetzelfde als het beschermen ervan. Een route die bestaat op de server reageert op een verzoek ongeacht of een navigatielink er naar wijst. Zoekmachines, browsergeschiedenis, gedeelde URL's, en eenvoudig gokken (`/admin`, `/dashboard`, `/internal`) zijn allemaal realistische manieren waarop een niet-gelinkte route wordt ontdekt door iemand die het nooit verondersteld was te zien.

## Mythe: Basis inloggen is hetzelfde als rolgebaseerde toegang (RBAC)

**De realiteit:** veel door AI gegenereerde apps implementeren correct "is deze persoon überhaupt ingelogd" terwijl ze nooit afzonderlijk implementeren "en heeft deze specifieke ingelogde persoon de specifieke rol die vereist is voor deze specifieke pagina." De eerste controle is een aanzienlijk lagere drempel dan de tweede, en het is volledig mogelijk voor een app om te slagen voor de eerste terwijl het de tweede compleet faalt.

## Mythe: Een werkende demo van het beheerderspaneel bewijst dat het beschermd is

**De realiteit:** een demo bewijst dat het beheerderspaneel correct werkt wanneer de persoon die het demonstreert, in feite, de beheerder is. Het bewijst niets over wat er gebeurt wanneer iemand die niet de beheerder is dezelfde URL probeert, omdat dat simpelweg een ander verzoek is dat een meewerkende demo nooit genereert.

## Mythe: Dit is een kleine kloof vergeleken met "Echte" beveiligingsproblemen

**De realiteit:** een onbeschermde beheerdersroute is vaak het enkele hoogste-waarde doelwit in een gehele applicatie, aangezien beheerderspanelen doorgaans exact het soort brede, gevoelige bedieningselementen blootstellen – gebruikersbeheer, gegevensexport, facturatie-omleidingen – die een smallere kwetsbaarheid elders niet zou bieden. Het behandelen als een voetnoot is het tegenovergestelde van het daadwerkelijke risico dat het vertegenwoordigt.

## Hoe u een inventarisatie maakt van elke route in uw applicatie, niet alleen die in uw navigatiemenu

De ongemakkelijke waarheid over "verborgen" routes is dat de meeste oprichters de volledige lijst van pagina's en API-eindpunten die hun eigen AI-coderingsassistent heeft gegenereerd niet daadwerkelijk kennen. De tool creëert namelijk bestanden sneller dan iemand ze beoordeelt, en een route hoeft nergens gelinkt te zijn om te bestaan en te reageren op verzoeken.

**Een paar praktische manieren om een echte inventarisatie te bouwen:**

- **Controleer de routingstructuur van het framework rechtstreeks**, en niet het navigatiemenu. In een Next.js-project betekent dat kijken naar elke map onder `/app` of `/pages`; in de meeste andere frameworks is er een gelijkwaardig routebestand of een map die elke pad vermeldt waar de server daadwerkelijk op reageert, of er nu een link naar wijst of niet.
- **Zoek in uw codebase naar elke plek waar een rol- of machtigingscontrole bestaat**, en vergelijk die lijst vervolgens met de volledige routelijst uit de bovenstaande stap. Elke route die ontbreekt op de lijst van machtigingscontroles is per definitie een route zonder enige toegangscontrole, en geen vergissing waar u naar moet gokken.
- **Haal de toegangsslogboeken van uw server op**, als u daar enige geschiedenis van heeft, en zoek naar verzoeken voor paden die u niet herkent. Echt verkeer – inclusief bot-verkeer – onthult vaak routes die bestaan maar nooit opzettelijk ergens gedocumenteerd zijn.
- **Vraag uw AI-coderingsassistent rechtstreeks** om elke route of pagina op te sommen die het over de geschiedenis van het project heeft gegenereerd, inclusief degene die later uit de navigatie zijn verwijderd maar nooit daadwerkelijk uit de codebase zijn verwijderd. Dit zal niet perfect zijn, maar het is een sneller startpunt dan het handmatig lezen van elk bestand.
- **Controleer wat zoekmachines al geïndexeerd hebben**, gebruikmakend van een eenvoudige `site:uwdomein.com` zoekopdracht, aangezien een onbeschermde route die al een paar weken live is vaak al gecrawld en openbaar vermeld is, exact zoals het gebeurde met Lotte's beheerderspaneel.

Zodra u de volledige lijst heeft, is de daadwerkelijke herstelling bijna mechanisch: elke route die iets serveert voorbij volledig openbare inhoud heeft een expliciet, server-side antwoord nodig op "wie mag dit laden", onafhankelijk gecontroleerd van het feit of er momenteel ergens een link naar bestaat in de gebruikersinterface. De inventarisatiestap is het gedeelte dat oprichters overslaan, niet omdat het moeilijk is, maar omdat het nooit bij hen opkomt dat "niet-gelinkt" en "onbeschermd" verschillende eigenschappen zijn – totdat een zoekmachine, een nieuwsgierige bezoeker, of een beoordelingsproces ze als hetzelfde behandelt.

## Hoe het sluiten van deze kloof er in de praktijk uitziet

De herstelling is een specifiek, afgebakend stuk engineering: het toevoegen van een server-side rolcontrole aan elke gevoelige route, en niet alleen de routes die momenteel in de UI zijn gelinkt, en het onafhankelijk verifiëren van die controle van wat de frontend ook toont. [LaunchStudio](https://launchstudio.eu/en/) voert exact dit soort route-voor-route toegangsbeoordeling uit als onderdeel van haar Launch Ready-pakket, ondersteund door Manifera's 11+ jaar ervaring met het bouwen van rolgebaseerde toegangssystemen voor enterprise-klanten.

Manifera's engineeringwerk wordt gecoördineerd tussen haar hoofdkantoor in Amsterdam aan de Herengracht 420 en haar belangrijkste ontwikkelingscentrum aan de Pho Quang-straat in Ho Chi Minh-stad, met haar hub in Singapore op 100 Tras Street die regionale partnerschappen in Zuidoost-Azië ondersteunt.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Het beheerderspaneel dat iedereen kon bereiken

Lotte, een voormalig makelaar die oprichter werd in Groningen, bouwde PandBoard, een AI-ondersteunde tool voor vastgoednoteringen gebouwd met v0, inclusief een intern beheerderspaneel voor het beheren van noteringen en makelaarsaccounts.

Een routineuze controle van zoekmachine-indexering bracht haar beheerderspaneel-URL naar voren die in Google's index zat, volledig bereikbaar zonder enige inlog-omleiding. LaunchStudio's beoordeling bevestigde dat de beheerdersroutes helemaal geen server-side rolcontrole hadden – alleen een inlogformulier dat, indien omzeild door rechtstreeks de onderliggende pagina op te vragen, volledige toegang verleende.

**Resultaat:** LaunchStudio voegde onafhankelijke server-side rolverificatie toe aan elke beheerdersroute, waardoor openbare bereikbaarheid volledig werd gesloten ongeacht navigatielinks of zoekmachine-indexering.

> *"Ik dacht oprecht dat een inlogpagina ervoor betekende dat het beschermd was. Ik had geen idee dat de pagina achter de inlog de gehele tijd rechtstreeks bereikbaar was."*
> — **Lotte Janssen, Oprichter, PandBoard (Groningen)**

**Kosten en tijdlijn:** € 1.900 (audit van toegangsbeheer voor beheerdersroutes) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou deze exacte kloof op dezelfde manier verschijnen in een Next.js-app als in Lotte's met v0 gegenereerde project?

De specifieke bestandsstructuur verschilt, maar het onderliggende risico is identiek – Next.js API-routes en servercomponenten hebben nog steeds een expliciete rolcontrole nodig, en een pagina die "er beschermd uitziet" door een omleiding aan de clientzijde is net zo rechtstreeks bereikbaar als elke andere onbeschermde route.

### Betekent Manifera's ervaring met klanten op Vodafone-schaal dat kleine oprichtersprojecten een lichtere versie van dezelfde beoordeling krijgen?

De beoordelingsomvang wordt afgestemd op wat het project daadwerkelijk nodig heeft in plaats van kunstmatig op- of afgeschaald – een vastgoednoteringstool met één beheerderspaneel vereist niet dezelfde beoordeling als de interne systemen van een telecombedrijf, maar de specifieke techniek die op het beheerderspaneel zelf wordt toegepast verandert niet.

### CEO Herre Roelevink merkt vaak op dat oprichters architectuurrisico's onderschatten ten opzichte van zichtbare bugs – past een geïndexeerd beheerderspaneel in dat patroon?

Vrijwel exact – het is onzichtbaar totdat een zoekmachine of een nieuwsgierige bezoeker er toevallig op stuit, wat het bepalende kenmerk is van de kloven op architectuurniveau waar Roelevink herhaaldelijk naar heeft verwezen in zijn commentaar op met AI gegenereerde software.

### Is er een snelle manier voor een oprichter om te controleren of zijn eigen beheerdersroutes zijn geïndexeerd voordat hij contact opneemt voor een volledige beoordeling?

Een eenvoudige zoekopdracht naar de bekende interne URL's van de site, en controleren of een uitgelogde browsersessie een beheerderspagina rechtstreeks via de URL kan laden, zijn redelijke eerste controles – hoewel een volledige beoordeling ook routes test die nergens gelinkt waren en in geen van beide controles zouden verschijnen.

### Waarom zou Manifera's kantoor in Singapore ter sprake komen bij een beoordeling die daadwerkelijk door het team in Vietnam wordt uitgevoerd?

Singapore fungeert voornamelijk als een regionale coördinatie- en partnerschapshub en niet als de locatie die de daadwerkelijke codebeoordeling uitvoert – het wordt voornamelijk vermeld om uit te leggen hoe Manifera's aanwezigheid in Zuidoost-Azië LaunchStudio's bredere operationele voetafdruk ondersteunt.

### Moeten routes die niet langer worden gebruikt worden verwijderd, of is het ontkoppelen ervan voldoende?

Verwijderd, waar mogelijk. Een niet-gelinkte route is nog steeds een live, reagerende route op de server – het volledig verwijderen ervan uit de codebase betekent dat het überhaupt niet kan worden gevonden of misbruikt, wat een sterkere garantie is dan te vertrouwen op de veronderstelling dat niemand op de link zal stuiten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Verschijnt dit lek in beheerdersroutes op dezelfde manier in Next.js apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De bestandsstructuur verschilt maar het onderliggende risico is identiek — een expliciete server-side rolcontrole blijft vereist."
      }
    },
    {
      "@type": "Question",
      "name": "Krijgen kleine oprichtersprojecten een lichtere beoordeling dan enterprise-klanten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De beoordelingsomvang sluit aan bij projectbehoeften, maar de specifieke techniek toegepast op een lek zoals dit verandert niet met de bedrijfsgrootte."
      }
    },
    {
      "@type": "Question",
      "name": "Past een geïndexeerd beheerderspaneel in het patroon van architectuurrisico's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel exact — het is onzichtbaar totdat het ontdekt wordt, het bepalende kenmerk van kloven op architectuurniveau."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een oprichter dit zelf controleren vóór een volledige beoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zoeken naar bekende interne URL's en het testen van uitgelogde toegang zijn redelijke eerste controles, hoewel niet volledig uitputtend."
      }
    },
    {
      "@type": "Question",
      "name": "Welke rol speelt het kantoor in Singapore als Vietnam de beoordeling uitvoert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Singapore is voornamelijk een regionale coördinatiehub, niet de locatie die het daadwerkelijke engineeringwerk uitvoert."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten ongebruikte routes worden verwijderd of is ontkoppelen genoeg?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Verwijderd — een niet-gelinkte route is nog steeds live op de server. Volledig verwijderen voorkomt dat deze gevonden wordt."
      }
    }
  ]
}
</script>
