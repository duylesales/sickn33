---
Titel: "Van AI-code naar productie in Den Haag: GovTech-startups en publieke inkopers"
Trefwoorden: ai-code naar productie, govtech den haag, softwarebeveiliging publieke sector, bio baseline, windsurf, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Van AI-code naar productie in Den Haag: GovTech-startups en publieke inkopers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van AI-code naar productie in Den Haag: GovTech-startups en publieke inkopers",
  "description": "GovTech-oprichters in Den Haag krijgen te maken met overheden die formele eisen stellen aan cybersecurity, BIO-baseline, WCAG-toegankelijkheid en AVG. Dit artikel legt uit wat publieke inkopers verlangen wanneer AI-code naar productie gaat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-20",
  "inLanguage": "nl-NL",
  "contentLocation": { "@type": "Place", "name": "Den Haag, Nederland" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-code-to-production-in-the-hague-govtech-and-public-sector-buyers" }
}
</script>

Den Haag is waar de Nederlandse overheid woont, en de stad heeft een gestage stroom GovTech-oprichters voortgebracht: oud-ambtenaren, beleidsadviseurs en consultants die een probleem van binnenuit zagen en er een tool voor bouwden. Steeds meer van die tools beginnen als AI-code - een Windsurf- of Cursor-project dat snel in elkaar is gezet om een gemeente te laten zien wat mogelijk is. De pilot loopt goed. Dan stuurt inkoop een vragenlijst, en wordt het naar productie brengen van die AI-code een heel specifieke oefening.

Publieke inkopers zijn niet moeilijker tevreden te stellen dan andere klanten; ze zijn explicieter. Ze schrijven op wat ze nodig hebben. Dat is goed nieuws, want het betekent dat je je kunt voorbereiden.

## Waar Publieke Inkopers Echt om Vragen

Vragenlijsten verschillen, maar Nederlandse gemeenten, provincies, waterschappen en agentschappen vragen meestal naar dezelfde gebieden:

- **Informatiebeveiliging** - vaak gekoppeld aan de BIO (Baseline Informatiebeveiliging Overheid), de beveiligingsbasis van de overheid die gebaseerd is op ISO 27002.
- **Gegevensbescherming** - een verwerkersovereenkomst, een lijst met verwerkers, datalocatie, bewaartermijnen en een gegevensbeschermingseffectbeoordeling (DPIA) als de verwerking een hoog risico heeft.
- **Toegankelijkheid** - websites en apps van de overheid moeten voldoen aan toegankelijkheidseisen op basis van WCAG, en inkopers vragen leveranciers steeds vaker om een toegankelijkheidsverklaring.
- **Testen** - bewijs van beveiligingstesten, vaak een recente penetratietest voor alles wat met burgers in aanraking komt.
- **Continuïteit** - back-ups, hersteltijden, incidentprocessen en wat er gebeurt als je bedrijf stopt.
- **Exit** - hoe de inkoper zijn data in een bruikbaar formaat terugkrijgt als het contract afloopt.

Een AI-prototype heeft hier meestal niets van gedocumenteerd, en een deel ervan ontbreekt helemaal.

## De Gaten van AI-Code naar Productie Achter de Vragen

Achter het papierwerk zitten concrete technische eisen. Deze ontbreken het vaakst in AI-gegenereerde GovTech-prototypes:

**Rolgebaseerde toegang die past bij de organisatie.** Gemeentelijke gebruikers hebben rollen - zaakbehandelaar, teamleider, beheerder, auditor - met verschillende rechten. AI-gebouwde apps hebben vaak "gebruiker" en "beheerder", deels afgedwongen in de interface.

**Auditlogging.** Overheidsorganisaties moeten kunnen verantwoorden wie data heeft ingezien en gewijzigd. Een append-only log van toegang tot persoonsgegevens is vaak een harde eis.

**Authenticatie die past bij overheidsgebruikers.** Veel inkopers willen single sign-on met hun eigen identiteitsprovider (vaak via SAML of OpenID Connect) en meerfactorauthenticatie voor beheerders. Diensten voor burgers kunnen DigiD of eHerkenning vereisen, wat eigen eisen en beoordelingen met zich meebrengt.

**Dataminimalisatie en bewaartermijnen.** Persoonsgegevens horen alleen te worden verzameld waar dat nodig is en volgens een vastgesteld schema te worden verwijderd - iets wat AI-gegenereerde schema's nooit bevatten.

**Hosting en locatie.** Inkopers willen meestal data in de EU en soms in Nederland, met duidelijkheid over elke subverwerker.

**Toegankelijkheid in de interface.** AI-gegenereerde interfaces missen vaak labels, contrast, toetsenbordnavigatie en focusbeheer. De [richtlijnen van DigiToegankelijk](https://www.digitoegankelijk.nl/) van de Nederlandse overheid leggen uit wat er wordt verwacht.

## De Vraag naar de Penetratietest

Voor een dienst voor burgers of een dienst die gevoelige data verwerkt, vraagt een inkoper vaak om een penetratietest door een onafhankelijke partij. Er een uitvoeren op een niet-versterkt AI-prototype is geldverspilling: het rapport zal de voor de hand liggende problemen opsommen, en na het oplossen betaal je opnieuw.

De efficiënte volgorde is: eerst reviewen en versterken, de bevindingen oplossen, en dan de penetratietest laten uitvoeren op een systeem dat er klaar voor is. De test bevestigt dan je werk in plaats van de basis te catalogiseren.

## Documentatie Is Onderdeel van het Product

Bij GovTech zijn de documenten geen bijzaak; ze zijn onderdeel van wat de inkoper aanschaft. Bereid minimaal voor:

- een beveiligingsoverzicht gekoppeld aan de relevante BIO-maatregelen,
- een lijst met verwerkers en een verwerkersovereenkomst,
- een toegankelijkheidsverklaring,
- een beschrijving van back-up en herstel met realistische hersteltijden,
- een procedure voor incidentrespons,
- een exitplan dat de formaten voor data-export beschrijft.

Veel hiervan kan kort zijn. Het moet wel kloppen.

## Waarom Dit de Moeite Waard Is om Eén Keer Goed te Doen

De Nederlandse publieke sector is een grote, stabiele markt, en referentieklanten wegen enorm zwaar. Eén gemeente die voor je beveiliging en continuïteit kan instaan, opent deuren bij tientallen andere. Het productiewerk voor het eerste contract goed doen, maakt er een troef van voor elke volgende aanbesteding.

## Je App Koppelen aan de BIO

Publieke inkopers vragen vaak hoe je product zich verhoudt tot de BIO (Baseline Informatiebeveiliging Overheid). Je hoeft niet gecertificeerd te zijn om geloofwaardig te antwoorden. Een praktische aanpak is een kort koppelingsdocument dat de gebieden behandelt waar inkopers het meest op letten:

| BIO-gerelateerd thema | Waar inkopers naar kijken | Bewijs dat je kunt leveren |
| --- | --- | --- |
| Toegangsbeheer | Rollen, minimale rechten, MFA voor beheerders | Rollenmatrix, SSO-configuratie, MFA-beleid |
| Logging en monitoring | Wie wat heeft ingezien, meldingen bij afwijkingen | Beschrijving van de auditlog, voorbeeldexport, lijst met meldingen |
| Cryptografie | Versleuteling tijdens transport en in opslag | TLS-configuratie, verklaring over versleuteling van de hostingprovider |
| Leveranciersmanagement | Subverwerkers en hun locaties | Lijst met verwerkers met verwerkersovereenkomsten |
| Continuïteit | Back-ups, hersteldoelen, incidentafhandeling | Back-upschema, resultaat van een hersteltest, incidentprocedure |
| Veilige ontwikkeling | Codereview, testen, kwetsbaarheidsbeheer | CI-controles, scannen van afhankelijkheden, pentest- of reviewrapport |

Een koppeling van twee tot vier pagina's zoals deze beantwoordt een groot deel van de inkoopvragen en laat de inkoper zien dat je zijn kader begrijpt.

## Werken met DigiD, eHerkenning en SSO van de Overheid

GovTech-producten moeten vaak ambtenaren of juist burgers en bedrijven authenticeren. Ambtenaren loggen doorgaans in via de eigen identiteitsprovider van de organisatie, meestal via SAML of OpenID Connect. Authenticatie van burgers en bedrijven via DigiD of eHerkenning brengt extra eisen met zich mee: aansluiting via een erkende makelaar of leverancier, beveiligingsbeoordelingen en specifieke afspraken. Voor een vroeg GovTech-product is het vaak verstandig om te beginnen met functies voor medewerkers via SSO en authenticatie voor burgers via een gevestigde makelaar toe te voegen wanneer het contract dat vereist, in plaats van voortijdig een directe koppeling te bouwen.

## Toegankelijkheid als Contracteis

Nederlandse overheidsorganisaties zijn verplicht hun websites en apps toegankelijk te maken, en ze verwachten doorgaans hetzelfde van publieksgerichte diensten van leveranciers. In de praktijk kijken inkopers naar conformiteit met WCAG 2.1 niveau AA en een toegankelijkheidsverklaring. AI-gegenereerde interfaces hebben vaak aanpassingen nodig aan formulierlabels, foutmeldingen, contrast, zichtbaarheid van de focus en toetsenbordnavigatie. Plan vóór het eerste contract een toegankelijkheidsreview van de kritieke flows, publiceer een verklaring met bekende beperkingen en een datum waarop ze zijn opgelost, en neem toegankelijkheidscontroles op in je releaseproces zodat achteruitgang wordt opgemerkt.

## Dataminimalisatie en Bewaartermijnen voor Burgerdata

Publieke diensten verwerken data van burgers onder strenge verwachtingen. Verzamel alleen wat de dienst nodig heeft; verwijder metadata uit foto's (bijvoorbeeld de locatie van het huis van een melder); scheid identificerende data van operationele data waar mogelijk; en spreek bewaartermijnen af met de inkoper en dwing ze daarna automatisch af. Bij diensten die gevoelige situaties kunnen betreffen - klachten over buren, meldingen van onveilige situaties - denk na over hoe de identiteit van de melder wordt beschermd tegen de persoon of organisatie waarover wordt gemeld.

## Een Exitplan Dat Inkopers Kunnen Accepteren

Publieke inkopers moeten verder kunnen als een leverancier stopt. Een exitplan beschrijft hoe data wordt geëxporteerd (formaten, frequentie, volledigheid), hoe lang je de overgang ondersteunt, welke documentatie wordt overgedragen en wat er na afloop van het contract met back-ups gebeurt. Een regelmatige geautomatiseerde export naar de eigen opslag van de inkoper aanbieden is een sterk antwoord. Voor kleine GovTech-leveranciers is een geloofwaardig exitplan vaak wat een gemeente genoeg geruststelt om ondanks de omvang van het bedrijf te tekenen.

## Timing en Drempels bij Aanbestedingen

Publieke inkoop volgt regels die afhangen van de contractwaarde. Kleinere opdrachten kunnen vaak via eenvoudigere procedures worden gegund, terwijl grotere formele aanbestedingen met gepubliceerde criteria vereisen. Voor een jong GovTech-bedrijf zijn vroege contracten vaak pilots of kleine opdrachten onder de Europese drempels. Gebruik ze om referenties, documentatie en bewijs op te bouwen - een hersteltest, een toegankelijkheidsverklaring, een schone penetratietest - die je nodig hebt als grotere aanbestedingen komen. Elk geslaagd klein contract maakt het volgende inkoopdossier makkelijker in te vullen.

## Vertrouwen Opbouwen vóór het Eerste Contract

Publieke inkopers zijn voorzichtig met jonge leveranciers, om goede redenen: continuïteit, beveiliging en verantwoording. Verschillende stappen bouwen vertrouwen op voordat de inkoop begint. Betrek de informatiebeveiligingsfunctionaris (CISO) en de privacyfunctionaris van de inkoper vroeg bij de pilot, in plaats van ze bij het contract te verrassen. Deel je BIO-koppeling en lijst met verwerkers uit jezelf. Bied een vast aanspreekpunt voor incidenten. Houd een changelog van releases bij zodat de inkoper kan zien hoe het product zich ontwikkelt. En wees eerlijk over beperkingen - een gedocumenteerd gat met een plan is voor een overheidsorganisatie veel acceptabeler dan een bewering die niet blijkt te kloppen.

## Ontwerpen voor de Werkprocessen van Ambtenaren

Zaakbehandelaars en teamleiders gebruiken GovTech-tools de hele dag, vaak naast verschillende andere systemen. Productierijpheid omvat details in het werkproces die AI-prototypes zelden goed hebben: bulkacties met bevestiging en ongedaan maken, sneltoetsen voor veelvoorkomende taken, exports in formaten die de andere systemen van de organisatie accepteren, duidelijke statusgeschiedenissen per zaak, en overdracht tussen collega's zonder context te verliezen. Twee of drie ambtenaren een uur met de pilot zien werken, brengt de meeste van deze behoeften snel aan het licht - en ze oplossen maakt van een tool die mensen verdragen een tool waar ze om vragen.

## Ritme van Beveiligingstesten na de Lancering

Eén penetratietest vóór het contract is zelden genoeg voor een dienst die regelmatig verandert. Een houdbaar ritme voor een kleine GovTech-leverancier is: geautomatiseerde controles bij elke wijziging (toegangstests, scannen op afhankelijkheden en geheimen), een gerichte interne review of review door een partner vóór grote releases, en een onafhankelijke penetratietest per jaar of wanneer de inkoper dat vereist. Leg elke test, de bevindingen en de oplossing ervan vast; publieke inkopers vragen tijdens contractevaluaties of verlengingen vaak naar deze geschiedenis.

## Wie Waarvan Eigenaar Is

In GovTech-projecten voorkomt duidelijkheid over rollen de meeste wrijving. De inkoper is meestal de verwerkingsverantwoordelijke; de leverancier is een verwerker die gebonden is aan de verwerkersovereenkomst. De inkoper bepaalt bewaartermijnen, toegangsbeleid en regels voor gebruikersbeheer; de leverancier implementeert en beheert ze. Leg deze verdeling schriftelijk vast, inclusief wie nieuwe subverwerkers goedkeurt en wie tijdens een incident met burgers communiceert.

## Waar LaunchStudio Past

Het werk van LaunchStudio voor GovTech-oprichters combineert technische versterking met de documentatie die inkopers verwachten: rolgebaseerde toegang en auditlogging afgedwongen op de server, SSO-integratie, bewaarregels, hosting in de EU, toegankelijkheidsverbeteringen in de bestaande interface, en een beveiligingsoverzicht dat klaar is om bij een vragenlijst te voegen. Wanneer een penetratietest vereist is, wordt het systeem erop voorbereid en worden de bevindingen achteraf afgehandeld.

De engineering komt van Manifera, dat 11+ jaar ervaring heeft met het leveren van software aan organisaties met formele eisen - waaronder TNO, de Nederlandse Organisatie voor toegepast-natuurwetenschappelijk onderzoek. Herre Roelevink, CEO van Manifera, heeft een achtergrond in cybersecurity: hij was medeoprichter van CyberDevOps (nu CFLW Cyber Strategies). Het kantoor van Manifera aan de Herengracht 420 in Amsterdam ligt op minder dan een uur van Den Haag Centraal; de engineering wordt uitgevoerd in het ontwikkelcentrum in Ho Chi Minh-stad. Zie [maatwerksoftware van Manifera](https://www.manifera.com/services/custom-software-development/) voor zijn grootschaligere werk voor de publieke sector en grote ondernemingen.

Om te beginnen, [beschrijf je project](https://launchstudio.eu/nl/#contact) - inclusief de vragenlijst van de inkoper als je die hebt. We reageren binnen één werkdag.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Buurtmeldtool Ontmoet de Inkoop

Hugo Verbeek was elf jaar beleidsadviseur voordat hij in Den Haag BuurtSignaal oprichtte: een tool waarmee bewoners problemen kunnen melden - kapotte straatverlichting, illegale dumpingen, onveilige oversteekplaatsen - en waarmee gemeentelijke teams meldingen kunnen beoordelen en erop reageren. Hij bouwde het in Windsurf met een Next.js-frontend en Postgres, en draaide een pilot met één stadsdeel. Bewoners vonden het fijn; de medewerkers van het stadsdeel nog meer.

Toen de gemeente overstapte op een formeel contract, stuurde inkoop een vragenlijst over beveiliging en privacy met 90 vragen. Hugo kon er ongeveer een derde beantwoorden. De review die LaunchStudio uitvoerde, legde uit waarom: gemeentelijke medewerkers hadden de rollen "gebruiker" en "beheerder", met beperkingen voor zaakbehandelaars alleen in de interface; er was geen auditlog; medewerkers logden in met wachtwoorden in plaats van via de identiteitsprovider van de gemeente; meldingen van bewoners, inclusief foto's met locatiegegevens, werden voor onbepaalde tijd bewaard; de hosting stond in een Amerikaanse regio; en een toegankelijkheidsscan vond ontbrekende labels en toetsenbordvallen in het meldformulier voor bewoners.

In 21 werkdagen implementeerde het team vier medewerkersrollen afgedwongen in de database, een append-only auditlog voor toegang tot data van bewoners, SSO via de OpenID Connect-provider van de gemeente met MFA voor beheerders, automatische verwijdering van locatiemetadata uit foto's, bewaarregels afgesproken met de gemeente, hosting in de EU met geteste back-ups, en toegankelijkheidsverbeteringen in de bestaande interface. Ook stelde het een aan de BIO gekoppeld beveiligingsoverzicht op, een lijst met verwerkers, een beschrijving van herstel, een incidentprocedure en een exitplan. De gemeente liet daarna een onafhankelijke penetratietest uitvoeren, die twee bevindingen met een laag risico opleverde, die nog dezelfde week werden opgelost.

**Resultaat:** BuurtSignaal tekende een driejarig contract met de gemeente en is sindsdien door twee buurgemeenten in een pilot gebruikt, die allebei de bestaande documentatie met kleine aanvullingen accepteerden.

> *"De pilot bewees dat bewoners het wilden. Het contract hing af van bewijzen dat de gemeente het kon vertrouwen. Dat waren twee verschillende projecten, en ik had alleen het eerste gedaan."*
> - **Hugo Verbeek, Oprichter, BuurtSignaal (Den Haag)**

**Kosten & Tijdlijn:** € 6.900 (Launch & Grow-pakket: toegangsbeheer, auditlogging, SSO, bewaartermijnen, hosting, toegankelijkheidsverbeteringen en inkoopdocumentatie) - afgerond in 21 werkdagen, plus € 49/maand voor beheerde hosting.

## Veelgestelde Vragen

### Heb ik een ISO 27001-certificering nodig om aan Nederlandse gemeenten te verkopen?

Niet altijd. Veel inkopers vragen hoe je beveiliging zich verhoudt tot de BIO in plaats van certificering te eisen, vooral bij kleinere contracten. Certificering kan nodig worden voor grotere of gevoeligere contracten; een solide, gedocumenteerde basis is in beide gevallen de eerste stap.

### Moet ik een penetratietest laten uitvoeren vóór of na het versterken?

Erna. Een niet-versterkt prototype testen bevestigt vooral bekende basisproblemen. Eerst versterken betekent dat de test zich richt op het echte resterende risico, en dat je niet voor twee tests betaalt.

### Kunnen AI-gegenereerde interfaces voldoen aan de toegankelijkheidseisen van de overheid?

Ja, met gerichte aanpassingen. AI-gebouwde interfaces missen vaak labels, contrast en toetsenbordondersteuning, maar dat kan worden gecorrigeerd zonder het product opnieuw te ontwerpen.

### Hoe helpt de ervaring van Manifera met TNO GovTech-oprichters?

Werken met een organisatie als TNO betekent werken met formele eisen, documentatie en verwachtingen rond beveiliging. Die ervaring helpt de engineers van LaunchStudio te voorzien waar publieke inkopers om zullen vragen en antwoorden voor te bereiden die standhouden.

### Hoe kan een GovTech-startup online worden gevonden door publieke inkopers?

Publiceer duidelijke pagina's over het probleem dat je oplost, je aanpak van beveiliging en privacy en je toegankelijkheidsverklaring, met gestructureerde data. Inkoopteams en AI-antwoordmachines zoeken allebei naar precieze, controleerbare informatie uit betrouwbare bronnen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik een ISO 27001-certificering nodig om aan Nederlandse gemeenten te verkopen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd. Veel inkopers vragen hoe de beveiliging zich verhoudt tot de BIO; certificering kan nodig zijn voor grotere of gevoeligere contracten." }
    },
    {
      "@type": "Question",
      "name": "Moet ik een penetratietest laten uitvoeren vóór of na het versterken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Na het versterken, zodat de test zich richt op het resterende risico en je niet twee keer betaalt." }
    },
    {
      "@type": "Question",
      "name": "Kunnen AI-gegenereerde interfaces voldoen aan de toegankelijkheidseisen van de overheid?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, met gerichte aanpassingen aan labels, contrast en toetsenbordondersteuning, zonder het product opnieuw te ontwerpen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera met TNO GovTech-oprichters?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het geeft vertrouwdheid met formele eisen en documentatie, waardoor te voorzien is waar publieke inkopers om vragen." }
    },
    {
      "@type": "Question",
      "name": "Hoe kan een GovTech-startup online worden gevonden door publieke inkopers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Publiceer duidelijke pagina's over het opgeloste probleem, beveiliging, privacy en toegankelijkheid, met gestructureerde data, op een betrouwbare site." }
    }
  ]
}
</script>
