---
Titel: "Compliance met Open Source-Licenties voor AI-Gegenereerde Code"
Trefwoorden: open source licence compliance, agpl saas risk, sbom for startups, ai generated code licensing, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Compliance met Open Source-Licenties voor AI-Gegenereerde Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Compliance met Open Source-Licenties voor AI-Gegenereerde Code",
  "description": "Met AI gebouwde applicaties leunen op honderden open source-packages, en AI-tools reproduceren soms beschermde code uit publieke repositories. Deze gids legt de verschillende open source-licentietypen uit, waarom copyleft-licenties zoals de AGPL grote risico's meebrengen voor SaaS-modellen, naamsvermeldingsverplichtingen (attributie), het opstellen van een Software Bill of Materials (SBOM), geautomatiseerde licentiescans en waar investeerders tijdens technische due diligence op letten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-16",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/open-source-licence-compliance-for-ai-generated-code" },
  "citation": [
    { "@type": "CreativeWork", "name": "Open Source Initiative: Licenses", "url": "https://opensource.org/licenses" },
    { "@type": "CreativeWork", "name": "GNU Affero General Public License v3", "url": "https://www.gnu.org/licenses/agpl-3.0.html" },
    { "@type": "CreativeWork", "name": "SPDX specification", "url": "https://spdx.dev/" },
    { "@type": "CreativeWork", "name": "CycloneDX specification", "url": "https://cyclonedx.org/" }
  ]
}
</script>

Elke softwaretoepassing die is ontwikkeld met behulp van Lovable, Bolt, v0, Cursor of Claude Code rust op het fundament van open source software. React, Tailwind CSS, de Supabase JavaScript client, datum-libraries, grafiekencomponenten en PDF-engines: een applicatie bevat al snel honderden packages, elk voorzien van een specifieke licentie die het gebruik onder bepaalde voorwaarden toestaat. De overgrote meerderheid van deze licenties is permissief en stelt minimale eisen. Een kleine minderheid stelt echter strenge juridische verplichtingen die de commerciële waarde van uw intellectuele eigendom direct kunnen aantasten.

AI-programmeertools introduceren hierbij een extra complicatie. Een AI-agent installeert bibliotheken zonder de licentievoorwaarden te evalueren. Bovendien reproduceren AI-modellen incidenteel letterlijke codefragmenten uit openbare trainingsdata, waarop auteursrechtelijke verplichtingen kunnen rusten. Voor de meeste oprichters blijft deze dynamiek volkomen onzichtbaar, totdat een potentiële koper, durfinvesteerder of corporate inkoopafdeling tijdens een technische due diligence vraagt om een complete licentie-inventaris en een Software Bill of Materials (SBOM).

Deze handleiding legt de juridische en technische basisprincipes uit. Dit artikel biedt praktische zakelijke en technische richtlijnen, geen formeel juridisch advies; raadpleeg bij overnames of investeringsrondes altijd een gespecialiseerde IT-jurist.

## Belangrijkste Punten

- **Open source-licenties vallen grofweg uiteen in permissieve licenties en copyleft-licenties.** Permissieve licenties (zoals MIT en Apache 2.0) vereisen primair naamsvermelding (attributie); copyleft-licenties kunnen u dwingen uw eigen bedrijfscode openbaar te maken.
- **Voor SaaS-producten is de AGPL (Affero GPL) de gevaarlijkste licentie:** de verplichting tot het vrijgeven van broncode wordt bij de AGPL al geactiveerd wanneer gebruikers de software via een netwerkverbinding benaderen.
- **Frontend-code wordt gedistribueerd:** JavaScript-bestanden die in de browser van de eindgebruiker worden geladen tellen juridisch als distributie, waardoor licentie- en copyrightvermeldingen verplicht zijn.
- **AI-modellen kunnen beschermde code reproduceren:** configureer instellingen in uw AI-tools die voorkomen dat suggesties letterlijk overeenkomen met publieke broncode.
- **Een actuele Software Bill of Materials (SBOM) en geautomatiseerde licentiescans in CI** maken compliance direct aantoonbaar voor zakelijke klanten en investeerders.

## Overzicht van Open Source Licentiefamilies

| Familie | Bekende voorbeelden | Belangrijkste verplichtingen | Risico voor SaaS-ondernemingen |
| --- | --- | --- | --- |
| Permissief | MIT, BSD, Apache 2.0, ISC | Behoud van copyright- en licentieteksten; Apache 2.0 regelt tevens octrooien | Laag, mits naamsvermeldingen aanwezig zijn |
| Zwak copyleft | LGPL, MPL 2.0, EPL | Wijzigingen aan de bibliotheek zelf moeten openbaar worden gedeeld | Gemiddeld; vereist zorgvuldige isolatie |
| Sterk copyleft | GPL v2, GPL v3 | Bij fysieke distributie van de software moet alle gekoppelde code als GPL worden vrijgegeven | Laag voor pure server-side SaaS; hoog bij mobiele of desktop apps |
| Netwerk copyleft | AGPL v3 | Zelfde als GPL, maar wordt óók geactiveerd bij toegang over een computernetwerk | Zeer hoog; kan proprietary SaaS-code infecteren |
| Source-available | BSL, SSPL | Beperkingen op commercieel gebruik of cloudhosting | Wisselend; lees de voorwaarden zeer nauwkeurig |
| Geen licentie | Code zonder expliciete licentie | Geen enkel gebruiksrecht verleend (auteursrecht blijft 100% bij maker) | Zeer hoog; categorisch vermijden |

Let vooral op de laatste categorie: code die op GitHub staat zónder expliciet licentiebestand is auteursrechtelijk beschermd. Het overnemen van dergelijke code door een AI-tool brengt directe inbreukrisico's met zich mee.

## Waarom de AGPL Hét Aandachtspunt Is voor SaaS

De klassieke GNU General Public License (GPL) wordt geactiveerd door *distributie*: het daadwerkelijk overhandigen of leveren van binaire software aan derden. Een traditionele SaaS-backend draait echter uitsluitend op uw eigen servers in de cloud. Klanten downloaden de servercode niet, waardoor veel SaaS-bedrijven decennialang server-side GPL-componenten konden inzetten zonder hun eigen applicatiesoftware te hoeven vrijgeven.

De **GNU Affero General Public License (AGPL)** is specifiek ontworpen om dit zogenaamde "SaaS-achterdeurtje" te dichten. Artikel 13 van de AGPL stelt dat wanneer u een aangepast AGPL-programma draait en gebruikers daarmee laat interacteren over een netwerk (zoals het internet), u de volledige broncode van die aangepaste versie kosteloos ter beschikking moet stellen aan al die gebruikers. Als een AI-agent een AGPL-library rechtstreeks in uw applicatiecode compileert of importeert, kan de stelling ontstaan dat uw gehele SaaS-platform een afgeleid werk is geworden dat onder de AGPL openbaar moet worden gemaakt.

Investeringsfondsen en overnamepartijen beschouwen de aanwezigheid van AGPL-dependencies in commerciële SaaS-backends dan ook als een acuut risico (red flag) tijdens technische due diligence.

## Frontend-Code Wordt Wél Gedistribueerd

Een juridisch detail dat door veel webontwikkelaars wordt vergeten: alle JavaScript- en CSS-bestanden die u bundelt met Vite, Next.js of Webpack worden letterlijk gedownload naar de computer van elke bezoeker. Dit geldt juridisch onomstotelijk als **distributie**.

Zelfs bij uiterst permissieve licenties zoals MIT of Apache 2.0 bent u wettelijk verplicht om de originele copyright-vermeldingen en licentieteksten mee te leveren. In geminificeerde JavaScript-bundels worden comments echter standaard gewist. De oplossing is het geautomatiseerd genereren van een **Third-Party Notices**-bestand of webpagina (bijvoorbeeld op `jouwapp.nl/juridisch/open-source-licenties`), waarin alle gebruikte bibliotheken en hun licentieteksten keurig worden opgesomd.

## AI-Gegenereerde Code en Inbreukrisico's

Grote taalmodellen zijn getraind op miljarden regels openbare code, waaronder repositories met strikte copyleft-licenties. Hoewel AI-modellen meestal nieuwe syntheses produceren, tonen onderzoeken aan dat zij bij specifieke algoritmische vraagstukken soms tientallen regels code letterlijk reproduceren.

Maatregelen ter bescherming van uw intellectuele eigendom:

- **Activeer duplicatiefilters in uw AI-tools:** schakel in GitHub Copilot of vergelijkbare assistenten de optie *"Block suggestions matching public code"* in.
- **Kies voor gevestigde libraries in plaats van gegenereerde code:** laat een agent niet een complex hashing- of crypto-algoritme uitschrijven, maar instrueer hem om een officiële, permissief gelicentieerde npm-package te importeren.
- **Documenteer uw AI-beleid:** leg vast welke tools worden gebruikt en welke guardrails zijn ingesteld. Investeerders vragen hier tegenwoordig standaard naar.

## Wat Is een Software Bill of Materials (SBOM)?

Een Software Bill of Materials (SBOM) is een machineleesbare, gestructureerde inventarislijst van alle softwarecomponenten, versies en licenties die in uw product aanwezig zijn. De twee wereldwijde standaarden hiervoor zijn **SPDX** en **CycloneDX**.

Waarom een startup een SBOM nodig heeft:

- **Aanbestedingen en Enterprise Procurement:** grote zakelijke inkopers en overheden eisen een SBOM om te verifiëren dat uw software geen verboden componenten of kwetsbare bibliotheken bevat.
- **Europese Cyber Resilience Act (CRA):** nieuwe Europese regelgeving verplicht softwareleveranciers om componenten en kwetsbaarheden structureel in kaart te brengen.
- **Technische Due Diligence:** het direct kunnen overhandigen van een kloppende SBOM aan een auditcommissie toont volwassenheid en voorkomt kostbare vertragingen.

## Automatische Licentiescans in uw CI/CD Pipeline

Compliance mag geen eenmalige exercitie zijn. Een AI-agent kan morgen immers ongemerkt een nieuw AGPL-package toevoegen. Integreer licentiecontrole direct in uw deployment-pipeline (GitHub Actions of GitLab CI):

1. **Licentie-scanner draaien:** tools zoals `license-checker` of gespecialiseerde scanners inspecteren alle dependencies bij elke Pull Request.
2. **Beleid handhaven:** markeer permissieve licenties (MIT, Apache 2.0, BSD) als toegestaan. Laat de pipeline automatisch falen zodra er een package met AGPL, GPL of 'onbekende licentie' wordt gedetecteerd.
3. **Automatische SBOM-generatie:** genereer bij elke officiële release automatisch een actueel CycloneDX- of SPDX-bestand.

## Veelvoorkomende Fouten

**Denken dat 'open source' synoniem staat voor 'gratis en zonder voorwaarden'.** Ook permissieve licenties verplichten tot naamsvermelding.

**Een AGPL-package pas ontdekken tijdens een overname-audit.** Hierdoor kunnen deals op het laatste moment klappen of heronderhandeld worden.

**Code kopiëren van willekeurige GitHub-gists zonder licentie.** Zonder expliciete licentie bezit u geen enkel gebruiksrecht.

**Geen overzicht hebben van lettertypen (fonts) en iconen.** Commerciële lettertypen zonder weblicentie in geëxporteerde PDF's vormen een frequent doelwit van claims.

## Hoe LaunchStudio Helpt

LaunchStudio maakt met AI gebouwde SaaS-applicaties volledig compliant op het gebied van open source software: we voeren een diepgaande licentie-audit uit op de gehele dependency-boom, identificeren en vervangen riskante (A)GPL-componenten, richten geautomatiseerde licentiescans en SBOM-generatie (CycloneDX/SPDX) in binnen uw CI/CD-pipeline, genereren een geautomatiseerde Third-Party Notices pagina voor uw frontend en stellen een helder dependency-beleid op voor uw AI-agents. Wij werken waar nodig nauw samen met uw eigen IT-jurist.

Het **Launch Ready**-pakket (€800 - €3.500) omvat licentie-audits, vervanging van riskante componenten en security hardening. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt doorlopend dependencymonitoring, managed hosting en actieve ondersteuning toe. Bereken eenvoudig uw investering via onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is een initiatief van Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde software engineers. Wij leveren al jarenlang enterprise-oplossingen aan veeleisende multinationals zoals Vodafone en TNO, waar strenge licentie-audits en leveranciersscreenings aan de orde van de dag zijn. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de softwareontwikkeling vindt plaats in ons gespecialiseerde ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het AGPL-Component Dat Twee Weken Vóór de Investering Werd Ontdekt

Nina Postma bouwde Roosterwijzer met Cursor en Supabase: een geavanceerde personeelsplannings- en urenregistratietool voor kinderopvangorganisaties, bestaande uit een Next.js frontend en een gespecialiseerde microservice voor capaciteitsrapportages. Na twee jaar autonome groei met een gezonde omzet bereikte Nina overeenstemming met een sectorgericht investeringsfonds over een substantiële groeifinanciering, onder voorbehoud van een technische due diligence.

De externe auditor van het fonds vroeg direct om een formele licentie-inventarisatie. Nina had deze niet paraat. Een uitgebreide scan bracht meer dan 900 directe en indirecte packages aan het licht. Het merendeel was permissief, maar in de rapportageservice - grotendeels autonoom gegenereerd door een AI-agent - bleek een aangepaste AGPL-gelicentieerde charting-server te zijn ingebouwd waarmee klanten via de applicatie rechtstreeks rapportages genereerden. Twee kleinere packages bleken bovendien volstrekt licentieloos te zijn, de frontend bevatte geen enkele naamsvermelding van derden en in de PDF-export zat een commercieel lettertype verwerkt waarvoor geen weblicentie was aangeschaft. De auditor classificeerde de AGPL-vondst als een 'High Risk' en het fonds eiste een bindend herstelplan vóórdat de contracten ondertekend konden worden.

LaunchStudio saneerde de codebase binnen recordtijd: het aangepaste AGPL-component werd volledig verwijderd en vervangen door een permissieve charting-library (Apache 2.0), waarbij alle rapportage-layouts pixel-voor-pixel identiek werden herbouwd. De twee licentieloze bibliotheken werden vervangen door onderhouden open-source alternatieven, het lettertype werd vervangen door een gelijkwaardig open-source font en het build-proces werd voorzien van een script dat automatisch een Third-Party Notices pagina genereert. In de CI-pipeline werd geautomatiseerde licentie-scanning en CycloneDX SBOM-generatie ingebouwd, en de projectinstructies voor Cursor kregen een harde lijst met goedgekeurde licenties.

**Resultaat:** De auditor sloot de AGPL-bevinding binnen twee weken formeel af en de investering werd conform de oorspronkelijke condities en waardering afgerond. Roosterwijzer levert de gegenereerde SBOM nu standaard mee bij openbare aanbestedingen voor kinderopvangkoepels, wat een doorslaggevend professioneel voordeel oplevert ten opzichte van concurrenten.

> *"Ik had werkelijk nog nooit een licentiebestand van dichtbij bekeken. Eén enkel door de AI ingebouwd component had bijna de voorwaarden van onze complete investeringsronde onderuit gehaald."*
> - **Nina Postma, Oprichter, Roosterwijzer (Hengelo)**

**Kosten & Doorlooptijd:** €4.700 (Launch & Grow-pakket: licentie-audit, vervanging van AGPL-component, herbouw van rapporten, pagina met vermeldingen, scanning, SBOM en dependencybeleid) - afgerond in 12 werkdagen.

## Veelgestelde Vragen

### Mag ik open source-packages zomaar gebruiken in een commerciële SaaS?

Ja, de meeste open source-licenties (zoals MIT, BSD en Apache 2.0) staan commercieel gebruik zonder beperkingen toe. Wel bent u verplicht de auteursrecht- en licentieteksten te behouden en mee te leveren. Wees uiterst alert op copyleft-licenties zoals de AGPL, die kunnen eisen dat u uw eigen broncode openbaart.

### Waarom vormt de AGPL-licentie een specifiek gevaar voor SaaS-bedrijven?

De AGPL stelt dat wanneer u software aanpast en via een netwerkverbinding beschikbaar stelt aan gebruikers, u verplicht bent de broncode van die aangepaste versie vrij te geven. Dit kan ertoe leiden dat uw bedrijfseigen SaaS-code juridisch openbaar gemaakt moet worden.

### Wie bezit het auteursrecht op door AI gegenereerde code en kan deze licenties schenden?

De wetgeving rondom auteursrecht op AI-code is wereldwijd nog volop in ontwikkeling. AI-modellen kunnen incidenteel beschermde code reproduceren. Door duplicatiefilters in te schakelen en te kiezen voor expliciete gevestigde libraries verkleint u dit risico aanzienlijk.

### Hoe helpt de ervaring van Manifera bij licentie-compliance?

Manifera levert al meer dan 11 jaar software onder strenge compliance- en licentie-audits van internationale enterprise-klanten. LaunchStudio benut deze ervaring om AI-codebases te screenen, riskante componenten te saneren en geautomatiseerde controles in te richten die elke audit glansrijk doorstaan.

### Is licentie-compliance relevant voor de verkoopkansen van mijn software?

Zeker. Grote zakelijke inkopers, overheidsinstellingen en enterprise-auditoren controleren leveranciers streng op licentierisico's en eisen steeds vaker een SBOM. Een transparant licentiebeleid en een officiële notices-pagina stralen volwassenheid uit en versterken de betrouwbaarheid van uw software bij AI-zoekmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mag ik open source-packages zomaar gebruiken in een commerciële SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, mits u voorwaarden naleeft: behoud vermeldingen voor permissieve licenties en let scherp op copyleft zoals AGPL." }
    },
    {
      "@type": "Question",
      "name": "Waarom vormt de AGPL-licentie een specifiek gevaar voor SaaS-bedrijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Omdat netwerktoegang tot aangepaste AGPL-software verplicht tot het openbaar maken van broncode, wat investeerders direct afschrikt." }
    },
    {
      "@type": "Question",
      "name": "Wie bezit het auteursrecht op door AI gegenereerde code en kan deze licenties schenden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Rechtspraak is in ontwikkeling; AI kan bestaande code reproduceren. Gebruik duplicatiefilters en kies expliciete libraries." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij licentie-compliance?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera levert al 11+ jaar software onder enterprise licentie-audits en zorgt voor waterdichte inventarisaties en SBOM-processen." }
    },
    {
      "@type": "Question",
      "name": "Is licentie-compliance relevant voor de verkoopkansen van mijn software?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, enterprise inkopers en overheden eisen SBOM's en licentieverklaringen vóór aanschaf." }
    }
  ]
}
</script>
