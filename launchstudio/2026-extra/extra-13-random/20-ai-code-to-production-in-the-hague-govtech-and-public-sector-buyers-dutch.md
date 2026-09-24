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

In Den Haag klopt het hart van het Nederlandse openbaar bestuur. De stad brengt dan ook een continue stroom GovTech-oprichters voort: voormalige beleidsmedewerkers, consultants en ambtenaren die van binnenuit tegen een hardnekkig administratief knelpunt aanliepen en besloten er zelf een slimme digitale oplossing voor te bouwen. Steeds vaker start zo'n oplossing als door AI gegenereerde code — een project in Windsurf of Cursor dat in een paar weken tijd in elkaar is gezet om aan een ministerie of gemeente te laten zien wat er technisch mogelijk is. De pilot slaagt glansrijk. Maar dan stuurt de inkoopafdeling een omvangrijke vragenlijst, en verandert het productierijp maken van die AI-code in een uiterst specialistisch traject.

Publieke inkopers zijn niet per se moeilijker tevreden te stellen dan commerciële klanten; ze zijn simpelweg veel explicieter. Zij leggen hun eisen vooraf tot in detail vast in formele kaders. Dat is uitstekend nieuws, want het betekent dat je je er minutieus op kunt voorbereiden.

## Wat publieke inkopers daadwerkelijk van je verlangen

Hoewel vragenlijsten per instantie variëren, toetsen Nederlandse gemeenten, provincies, waterschappen en rijksonderdelen steevast op dezelfde vaste pijlers:

- **Informatiebeveiliging:** Vrijwel altijd gekoppeld aan de **BIO (Baseline Informatiebeveiliging Overheid)**, het overheidsbrede normenkader gebaseerd op ISO 27001/ISO 27002.
- **Gegevensbescherming (AVG/GDPR):** Een getekende verwerkersovereenkomst, een uitputtende verwerkerslijst met vestigingslanden, bewaartermijnen en een Data Protection Impact Assessment (DPIA) indien er sprake is van hoog-risico gegevensverwerking.
- **Digitale toegankelijkheid:** Overheidswebsites en -apps zijn wettelijk verplicht te voldoen aan de **WCAG 2.1 niveau AA**-richtlijnen. Inkopers eisen daarom een formele toegankelijkheidsverklaring van hun toeleveranciers.
- **Onafhankelijke beveiligingstests:** Aantoonbaar bewijs van security-onderzoek, veelal in de vorm van een recente penetratietest voor burger-interactieve systemen.
- **Bedrijfscontinuïteit:** Automatische back-ups, geteste hersteltijden (RTO/RPO), een formeel incidentenprotocol en duidelijke waarborgen voor het geval jouw onderneming failliet mocht gaan.
- **Exit-strategie:** Hoe de overheidspartner bij contractbeëindiging alle data in een open, direct herbruikbaar formaat terugontvangt zonder vendor lock-in.

Een pril AI-prototype heeft op geen van deze terreinen formele documentatie klaarliggen — en mist onder de motorkap vaak cruciale technische waarborgen.

## De technische kloof achter de inkoopvragen

Achter de stapels administratieve inkoopvragen schuilen harde software-eisen. De hiaten die AI-gegenereerde GovTech-prototypes het vaakst vertonen:

1. **Rollenstructuur sluit niet aan op gemeentelijke workflows:** Binnen een gemeente hebben medewerkers strikt afgebakende rollen — zaakbehandelaar, teamleider, privacy-officer, auditor — met elk eigen bevoegdheden. AI-apps kennen vaak slechts "gebruiker" en "admin", waarbij restricties deels alleen in de frontend worden verstopt.
2. **Ontbreken van een onwijzigbaar auditlogboek:** Overheidsinstanties moeten juridisch kunnen verantwoorden wie wanneer welk burgerdossier heeft ingezien of gemuteerd. Een sluitend *append-only* logboek is een keiharde eis.
3. **Inlogmethoden voor ambtenaren en burgers:** Inkopers verlangen Single Sign-On (SSO) via hun eigen identity provider (zoals Azure AD/Entra ID via SAML of OpenID Connect) met verplichte tweefactorauthenticatie (MFA). Publieke diensten voor burgers raken al snel aan DigiD of eHerkenning.
4. **Dataminimalisatie en bewaartermijnen:** Burgergegevens mogen uitsluitend worden verzameld voor het specifieke doel en moeten na de wettelijke bewaartermijn automatisch worden gewist. Standaard AI-schema's voorzien hier nooit in.
5. **Dataconformiteit en EU-residentie:** Inkopers eisen dataopslag binnen de EU (en bij voorkeur binnen Nederland), met harde contractuele garanties over eventuele subverwerkers.
6. **Toegankelijkheidsgebreken in de interface:** AI-interfaces missen structureel formulierlabels, toetsenbordnavigatie, focusindicatoren en voldoende kleurcontrast. De [DigiToegankelijk-richtlijnen](https://www.digitoegankelijk.nl/) van de Rijksoverheid specificeren wat vereist is.

## De penetratietest: Eerst verstevigen, dan pas testen

Voor software die burgers raakt of gevoelige data verwerkt, eist de overheidspartner vrijwel altijd een penetratietest door een gecertificeerd extern beveiligingsbureau. Het laten uitvoeren van zo'n pentest op een ongehard AI-prototype is weggegooid geld: het rapport zal slechts open deuren intrappen (zoals ontbrekende rate limits en CSRF-tokens), waarna je na het herstel opnieuw een dure hertest moet betalen.

De juiste volgorde luidt: voer eerst een gerichte code- en configuratie-inspectie uit, los alle fundamentele kwetsbaarheden op, en laat dán pas de onafhankelijke pentest los op een systeem dat er klaar voor is. Zo fungeert de test als een overtuigend keurmerk voor de inkoper, in plaats van een pijnlijke catalogus van beginnersfouten.

## Documentatie is een integraal onderdeel van het product

In de GovTech-wereld is documentatie geen bijzaak achteraf; het is een essentieel onderdeel van hetgeen de overheid inkoopt. Zorg dat je minimaal de volgende set documenten hebt klaarliggen:
- Een security-overzicht waarin jouw maatregelen puntsgewijs worden gekoppeld aan de relevante BIO-beheersmaatregelen.
- Een verwerkersovereenkomst inclusief actuele verwerkerslijst en datacenterlocaties.
- Een formele toegankelijkheidsverklaring conform WCAG 2.1 AA.
- Een continuïteits- en herstelplan met geteste doorlooptijden.
- Een incidentenprotocol met vaste meldprocedures.
- Een exit-plan met specificatie van open data-exportformaten (zoals JSON/CSV).

## Jouw applicatie koppelen aan de BIO

Publieke inkopers vragen steevast hoe jouw software zich verhoudt tot de BIO. Je hoeft niet formeel ISO 27001-gecertificeerd te zijn om een overtuigend antwoord te geven. Een praktisch BIO-mappingdocument dekt de belangrijkste inkoopthema's af:

| BIO-thema | Waar de inkoper naar zoekt | Het bewijs dat jij levert |
| --- | --- | --- |
| Toegangsbeheer | Minste privileges, rollenmatrix, verplichte MFA | Rollenmatrix, SSO-configuratie, MFA-beleid |
| Logging & Monitoring | Wie zag welke data, realtime storingsalerts | Auditlog-architectuur, export-voorbeeld, alert-routing |
| Cryptografie | Encryptie tijdens transport en in rust (at rest) | TLS 1.3-configuratie, AES-256 database-encryptie |
| Leveranciersbeheer | Subverwerkers en geografische datallocatie | Volledige verwerkerslijst met getekende DPA's |
| Bedrijfscontinuïteit | Back-ups, RTO/RPO-tijden, incidentenprocedure | Back-upschema, hersteltestrapport, escalatieladder |
| Veilige software | Code reviews, kwetsbaarheidsbeheer, tests | CI/CD security checks, dependency-scans, pentestrapport |

Een compact document van drie tot vier pagina's dat deze punten helder beantwoordt, neemt direct 80% van de zorgen bij de gemeentelijke CISO of privacy-officer weg.

## Toegankelijkheid (WCAG) als contractuele voorwaarde

De overheid moet digitaal toegankelijk zijn voor iedereen, inclusief burgers met een visuele, motorische of cognitieve beperking. Interfaces die door AI-tools worden gegenereerd hebben standaard tientallen kleine toegankelijkheidsfoutjes: ontbrekende `<label>`-elementen bij invoervelden, slechte contrastratio's en ontoegankelijke knoppen voor screenreaders.

Het herstellen van deze elementen is geen grafische herbouw, maar een kwestie van semantische HTML-precisie: zorg voor logische tabvolgordes, zichtbare focusranden, duidelijke foutmeldingen die worden voorgelezen en volledige bedienbaarheid via het toetsenbord.

## De aanpak van LaunchStudio voor GovTech

LaunchStudio combineert de diepgaande technische versteviging van AI-codebases met het opleveren van het complete inkoopdossier dat overheden verlangen: rolgebaseerde autorisatie in de database, SSO-koppelingen, dataminimalisatie, veilige EU-hosting en WCAG-toegankelijkheidsreparaties in je bestaande frontend.

De software engineering wordt geleverd door Manifera, dat al meer dan 11 jaar software ontwikkelt voor organisaties met strenge formele standaarden — waaronder TNO (Nederlandse Organisatie voor Toegepast Natuurwetenschappelijk Onderzoek). Onze CEO Herre Roelevink was eerder medeoprichter van CyberDevOps (nu CFLW Cyber Strategies) en beschikt over diepgaande cybersecurity-ervaring. Ons Europese kantoor aan de Herengracht in Amsterdam bevindt zich op minder dan 50 minuten treinen van Den Haag Centraal. Bekijk meer over onze grootschalige projecten op [Manifera's maatwerkpagina](https://www.manifera.com/services/custom-software-development/).

Heb je een inkoopvragenlijst van een gemeente ontvangen? [Deel je project vrijblijvend met ons](https://launchstudio.eu/nl/#contact) — je ontvangt binnen één werkdag een heldere reactie.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een meld-app voor de openbare ruimte ontmoet gemeentelijke inkoop

Hugo Verbeek werkte elf jaar als beleidsadviseur sociaal domein alvorens hij in Den Haag de startup BuurtSignaal oprichtte: een platform waarmee buurtbewoners eenvoudig meldingen kunnen doen van overlast, defecte straatverlichting of zwerfafval, en waarmee gemeentelijke wijkteams deze meldingen direct kunnen oppakken en afhandelen. Hij bouwde het prototype met Windsurf met een Next.js-frontend en PostgreSQL, en draaide een succesvolle pilot in één Haags stadsdeel. Bewoners waren enthousiast; de wijkbeheerders nog meer.

Toen de gemeente overging tot een formeel contract voor meerdere stadsdelen, stuurde de afdeling inkoop een beveiligingsvragenlijst van 90 pagina's. Hugo kon slechts een derde van de vragen beantwoorden. De intake door LaunchStudio legde de kwetsbaarheden bloot: de gebruikersrollen waren simpelweg "user" en "admin", waarbij behandelaars uitsluitend in de frontend werden beperkt; er was geen audittrail; ambtenaren logden in met een los wachtwoord in plaats van de centrale gemeentelijke inlogomgeving; meldingen van burgers inclusief foto's met gps-metadata werden voor eeuwig bewaard; de database draaide in de VS; en een geautomatiseerde toegankelijkheidsscan constateerde tientallen WCAG-overtredingen.

Binnen 21 werkdagen voerde LaunchStudio een complete transformatie door: vier afzonderlijke ambtenarenrollen afgedwongen in de database, een onwijzigbaar auditlogboek voor inzages in burgerdata, SSO via de gemeentelijke OpenID Connect-omgeving met verplichte MFA voor beheerders, automatische verwijdering van Exif/gps-metadata uit bewonersfoto's, een geautomatiseerd bewaartermijnenbeleid, EU-hosting met geteste back-ups, en semantische WCAG-correcties in de bestaande gebruikersinterface. Tevens leverden we het complete BIO-overzicht, het verwerkersdocument en het exit-plan op. Een daaropvolgende externe penetratietest leverde slechts twee minieme aandachtspunten op, die dezelfde week werden verholpen.

**Resultaat:** BuurtSignaal ondertekende een driejarig contract met de gemeente Den Haag en werd vervolgens uitgerold in twee buurgemeenten, die de bestaande security-documentatie zonder aanvullende vragen accepteerden.

> *"De pilot bewees dat burgers de tool graag gebruiken. Het contract hing er echter vanaf of de gemeentelijke security-officer het systeem vertrouwde. Dat waren twee totaal verschillende werelden, en ik had pas één helft gedaan."*
> — **Hugo Verbeek, Oprichter, BuurtSignaal (Den Haag)**

**Kosten & Tijdlijn:** € 6.900 (Launch & Grow-pakket: autorisatie, auditlogging, SSO, dataminimalisatie, hosting, WCAG-reparaties en BIO-inkoopdocumentatie) — afgerond in 21 werkdagen, plus € 49/maand voor beheerde hosting.

## Veelgestelde Vragen

### Is een ISO 27001-certificering verplicht om aan Nederlandse gemeenten te leveren?

Niet altijd. Veel publieke inkopers vragen hoe jouw beveiliging zich verhoudt tot de BIO-baseline in plaats van een formeel certificaat te eisen, zeker bij kleinere contracten en pilots. Een aantoonbare, gedocumenteerde BIO-mapping is in die fase ruim voldoende.

### Moet ik een penetratietest laten uitvoeren vóór of na het productietraject?

Áltijd erna. Het testen van een ongehard prototype legt louter voor de hand liggende basisgebreken bloot. Door eerst de beveiliging professioneel te harden, test de ethische hacker op daadwerkelijk rest-risico en voorkom je dat je twee keer voor een dure test moet betalen.

### Kunnen door AI gegenereerde webapplicaties voldoen aan de overheids-toegankelijkheidseisen (WCAG)?

Jazeker, mits er gerichte semantische correcties worden doorgevoerd. AI-interfaces missen vaak formulierlabels, aria-attributen en contrast, maar deze kunnen uitstekend worden hersteld zonder het visuele ontwerp van je applicatie overhoop te gooien.

### Welke meerwaarde biedt Manifera's ervaring met TNO voor GovTech-startups?

Werken voor een vooraanstaand onderzoeksinstituut als TNO betekent opereren volgens formele overheidseisen, strikte documentatiestandaarden en strenge cybersecuritynormen. Die ervaring zorgt ervoor dat LaunchStudio exact weet welke antwoorden publieke inkopers en CISO's verlangen.

### Hoe wordt een GovTech-startup online gevonden door ambtenaren en inkopers?

Publiceer feitelijke, inhoudelijke pagina's over de specifieke maatschappelijke problemen die je oplost, jouw privacy- en security-aanpak (inclusief BIO-aansluiting) en je toegankelijkheidsverklaring, ondersteund door Schema.org-metadata. Overheidsinkopers en AI-zoeksystemen zoeken gericht naar transparante leveranciers met aantoonbare naleving van wet- en regelgeving.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een ISO 27001-certificering verplicht om aan Nederlandse gemeenten te leveren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd. Voor pilots en middelgrote opdrachten volstaat meestal een deugdelijke BIO-mapping waarin de beheersmaatregelen transparant worden aangetoond." }
    },
    {
      "@type": "Question",
      "name": "Moet ik een penetratietest laten uitvoeren vóór of na het productietraject?",
      "acceptedAnswer": { "@type": "Answer", "text": "Altijd erna. Door eerst de architectuur te harden, test het pentestbureau op echt reëel restrisico en voorkom je dubbele testkosten." }
    },
    {
      "@type": "Question",
      "name": "Kunnen door AI gegenereerde webapplicaties voldoen aan de overheids-toegankelijkheidseisen (WCAG)?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Met gerichte semantische aanpassingen (labels, contrast, toetsenbordfocus) kan de bestaande interface conform WCAG 2.1 AA worden gemaakt." }
    },
    {
      "@type": "Question",
      "name": "Welke meerwaarde biedt Manifera's ervaring met TNO voor GovTech-startups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Jarenlange samenwerking met TNO waarborgt dat onze engineers de strenge publieke security- en documentatie-eisen van binnenuit begrijpen." }
    },
    {
      "@type": "Question",
      "name": "Hoe wordt een GovTech-startup online gevonden door ambtenaren en inkopers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door feitelijke pagina's te publiceren over BIO-naleving, privacy en WCAG, voorzien van gestructureerde data die AI-zoekers direct citeren." }
    }
  ]
}
</script>
