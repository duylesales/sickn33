---
Titel: "ISO 27001 voor Beginnende SaaS: Wanneer Moet U Beginnen?"
Trefwoorden: iso 27001 voor startups, iso 27001 saas, wanneer iso 27001 behalen, iso 27001 kosten startup, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# ISO 27001 voor Beginnende SaaS: Wanneer Moet U Beginnen?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ISO 27001 voor Beginnende SaaS: Wanneer Moet U Beginnen?",
  "description": "Een ISO 27001-certificering kan deuren openen naar grote enterprise-klanten en de publieke sector, maar voor een vroege SaaS-startup vergt het aanzienlijke tijd en financiële middelen. Deze handleiding legt uit wat ISO 27001 daadwerkelijk inhoudt, hoe het auditproces verloopt, wat realistische kosten en doorlooptijden zijn, wanneer het juiste instapmoment is en welk technisch fundament een met AI gebouwde SaaS eerst moet leggen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-30",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/iso-27001-for-early-stage-saas-when-to-start" },
  "citation": [
    { "@type": "CreativeWork", "name": "ISO/IEC 27001:2022 Information security management systems", "url": "https://www.iso.org/standard/27001" },
    { "@type": "CreativeWork", "name": "ISO/IEC 27002:2022 Information security controls", "url": "https://www.iso.org/standard/75652.html" },
    { "@type": "CreativeWork", "name": "Raad voor Accreditatie (Dutch Accreditation Council)", "url": "https://www.rva.nl/en/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

Vroeg of laat strandt een veelbelovend B2B-verkooptraject op één specifieke vraag in het inkoopformulier: "Is uw organisatie ISO 27001 gecertificeerd?" Voor een oprichter met een compact team en een met behulp van AI gebouwde SaaS-applicatie voelt die vraag vaak als een gesloten deur. Certificering klinkt immers als een extreem kostbaar en traag traject, uitsluitend weggelegd voor corporaties met dedicated compliance-afdelingen.

Hoewel het behalen van een certificaat een serieuze inspanning vergt, is het beslist niet voorbehouden aan multinationals. Talloze compacte SaaS-bedrijven beschikken over een officieel ISO 27001-certificaat en winnen daarmee juist cruciale aanbestedingen. De kernvraag is niet óf u zich kunt certificeren, maar wannéér het zakelijk gezien rendeert om te starten, en welke technische maatregelen u vooraf moet treffen zodat het uiteindelijke certificeringstraject veel sneller, goedkoper en gebaseerd op échte beveiliging verloopt.

Deze handleiding legt uit wat ISO 27001 daadwerkelijk voorschrijft, wat het auditproces inhoudt en hoe u het optimale instapmoment bepaalt.

## Belangrijkste Punten

- **ISO 27001 certificeert een managementsysteem (ISMS), niet direct een los softwareproduct.** Het levert het formele bewijs dat u informatiebeveiligingsrisico's binnen uw organisatie gestructureerd identificeert en beheerst via passende maatregelen.
- **Het certificeringstraject duurt voor de meeste SaaS-startups 6 tot 12 maanden** vanaf de formele start tot de uitreiking van het certificaat, gevolgd door jaarlijkse controle-audits.
- **Start pas wanneer klanten het als harde contracteis stellen,** doorgaans bij verkopen aan enterprise-bedrijven, overheden, zorginstellingen of de financiële sector, en niet puur "omdat het professioneel oogt".
- **Het technisch fundament moet eerst op orde zijn:** strikte databasetoegangscontrole, MFA, gestructureerde logging, geteste back-ups, veilige CI/CD-ontwikkeling en leveranciersbeheer. Deze basis vereist de AVG / GDPR sowieso en vormt de kern van wat auditors inspecteren.
- **Een professioneel Beveiligingsoverzicht (Security Whitepaper) volstaat vaak al** in de vroege fase van een startup, waarmee u waardevolle tijd wint tot de business case voor een formele audit onomstotelijk vaststaat.

## Wat ISO 27001 Daadwerkelijk Inhoudt

ISO/IEC 27001 is de wereldwijde standaard voor Information Security Management Systems (ISMS). De actuele normversie, ISO/IEC 27001:2022, bestaat uit twee essentiële onderdelen die direct relevant zijn voor softwarebedrijven:

**De managementsysteem-clausules (hoofdstuk 4 tot en met 10):** Deze beschrijven hoe informatiebeveiliging organisatorisch wordt bestuurd: contextanalyse van stakeholders, directiebetrokkenheid, het informatiebeveiligingsbeleid, risicoanalyse en risicobehandeling, rolverdelingen, documentbeheer, interne audits, directiebeoordeling en continue verbetering.

**Annex A (Bijlage A):** Deze bevat 93 concrete beheersmaatregelen (controls), ingedeeld in vier overzichtelijke thema's: organisatorisch, mensgericht, fysiek en technologisch. Denk aan toegangsbeheer, encryptie, veilige softwareontwikkeling, audit-logging, relaties met toeleveranciers, incidentbeheer en bedrijfscontinuïteit. U hoeft niet blindelings alle 93 maatregelen te implementeren. U analyseert uw specifieke bedrijfsrisico's, selecteert de van toepassing zijnde controls en legt dit formeel vast in een Verklaring van Toepasselijkheid (Statement of Applicability, SoA).

De norm ISO/IEC 27002 biedt gedetailleerde praktische richtsnoeren voor het inrichten van deze maatregelen. Samen vormen ze een modulair raamwerk: een SaaS-bedrijf van vijf medewerkers en een multinational kunnen beide gecertificeerd zijn, met een implementatie die exact is afgestemd op hun eigen risicoprofiel.

## Hoe het Certificeringstraject Verloopt

De formele audit wordt uitgevoerd door een onafhankelijke certificerende instelling (Certification Body). Kies in Nederland bij voorkeur voor een instelling die geaccrediteerd is door de Raad voor Accreditatie (RvA), of een gelijkwaardige Europese accreditatie-instantie; geaccrediteerde certificaten genieten internationaal het hoogste aanzien bij zakelijke inkopers.

De gebruikelijke route bestaat uit de volgende stappen:

1. **Afbakening van de scope (Scope definition):** Vaststellen welke onderdelen onder het ISMS vallen, normaliter het SaaS-product, de cloudinfrastructuur en het team dat de software bouwt en onderhoudt.
2. **Nulmeting (Gap analysis):** De bestaande werkwijze en systemen systematisch vergelijken met de normvereisten.
3. **Implementatie:** Beleidsdocumenten opstellen, de formele risicoanalyse uitvoeren, ontbrekende technische maatregelen inrichten, medewerkers trainen en het ISMS operationeel maken.
4. **Bewijsperiode (Evidence period):** Het managementsysteem enkele maanden actief draaien om bewijslast op te bouwen: periodieke toegangsrevisies, incidentregistraties, leveranciersbeoordelingen, een interne audit en een formele directiebeoordeling.
5. **Fase 1-audit (Documentenbeoordeling):** De externe auditor toetst of uw beleid, scope en risicoanalyse voldoen aan de formele normeisen.
6. **Fase 2-audit (Implementatietoets):** De auditor controleert via steekproeven, interviews en technische inspecties of het ISMS in de dagelijkse praktijk daadwerkelijk functioneert.
7. **Certificering:** Bij een positief oordeel ontvangt u het ISO 27001-certificaat met een geldigheid van drie jaar, onder voorwaarde van jaarlijkse controle-audits.

## Realistische Kosten en Doorlooptijden

De totale kosten zijn sterk afhankelijk van de gekozen scope, de technische volwassenheid van uw product en de hoeveelheid externe ondersteuning die u inhuurt. Als indicatie voor een compacte SaaS-onderneming tot circa twintig medewerkers:

| Kostenpost | Realistische bandbreedte | Toelichting |
| --- | --- | --- |
| Externe auditor (Certificerende instelling) | Enkele duizenden euro's voor de initiële audit | Afhankelijk van scope, complexiteit en personeelsaantallen |
| Compliance-platform of ISO-adviseur | Van enkele duizenden tot tienduizenden euro's | Platforms automatiseren bewijsverzameling; consultants begeleiden risico's |
| Interne tijdsinvestering | Honderden uren in het eerste implementatiejaar | Veruit de grootste verborgen kostenpost voor het team |
| Technische verbeteringen | Variabel | Kosten voor MFA, centrale logging, back-upinrichting en CI/CD-beveiliging |
| Penetratietest (Pentest) | Vaak verlangd als ondersteunend bewijs | Formeel niet verplicht door de norm, wel standaard gevraagd door auditors |

Voor een klein team bedraagt de doorlooptijd doorgaans zes tot twaalf maanden. Trajecten verlopen het soepelst wanneer de technische controls al operationeel zijn en het werk zich beperkt tot beleidsvorming en bewijsvoering. Trajecten lopen ernstige vertraging op wanneer het technische fundament van de applicatie zwak blijkt en tijdens het ISO-traject halhaast moet worden herbouwd.

## Signalen Dat het Tijd Is om te Starten

Start uitsluitend met een formeel ISO 27001-traject wanneer er een sluitende business case ligt. Duidelijke signalen:

- **Herhaalde contracteisen in salestrajecten:** Meerdere serieuze enterprise-prospects maken certificering een absolute voorwaarde voor gunning.
- **Verkoop aan sterk gereguleerde sectoren:** U richt zich primair op de overheid, zorg, banken of enterprise-corporates binnen Europa, waar ISO 27001 de gevestigde standaard is.
- **Europese aanbestedingen (tenders):** Officiële tenders sluiten leveranciers zonder erkend certificaat direct uit van deelname.
- **Integratiepartnerships:** Grote platformen of distributiepartners eisen ISO 27001 alvorens API-toegang tot klantdata wordt verleend.
- **Investerings- of overnametrajecten:** Investeerders of strategische overnamekandidaten stellen ISO-conformiteit als vereiste tijdens de technische due diligence.

Zwakke signalen die een traject doorgaans nog niet rechtvaardigen:

- Eén enkele prospect noemt het terloops in een oriënterend gesprek.
- Concurrenten voeren een ISO-badge op hun landingspagina.
- Het voelt intuïtief "professioneel" om te hebben.

Zijn de signalen nog pril? Investeer dan doelgericht in de technische baseline en een helder Beveiligingsoverzicht. Zodra de harde vraag ontstaat, heeft u al een enorme voorsprong.

## Alternatieven en Tussenstappen

**Een professioneel Beveiligingsoverzicht en audit-antwoorden.** Veel enterprise-inkopers gaan akkoord met een uitstekend gedocumenteerd security-whitepaper, een subverwerkerslijst, een samenvatting van een recente pentest en een ingevulde security-vragenlijst, zeker tijdens pilots of initiële contractjaren.

**SOC 2 Type II.** Zeer populair bij Amerikaanse opdrachtgevers. Het is een assurance-rapport van een registeraccountant in plaats van een certificaat, met overlappende technische controls. Binnen Europa blijft ISO 27001 echter de absolute voorkeursnorm.

**Branchespecifieke normen (NEN 7510).** Levert u software aan de Nederlandse zorgsector? Dan eisen ziekenhuizen en zorginstellingen nagenoeg altijd NEN 7510, een norm die direct voortbouwt op ISO 27001 maar specifieke eisen toevoegt voor medische persoonsgegevens. Onze gids over [NEN 7510 en zorgapplicaties in Nederland](https://launchstudio.eu/nl/blog/nen-7510-and-healthcare-apps-in-the-netherlands) legt de exacte samenhang uit.

**Certificeringen van uw cloudproviders.** Uw hosting- en databaseleveranciers (zoals AWS of Supabase) zijn ISO 27001 gecertificeerd. Dat certificeert uw eigen onderneming niet, maar dekt wel een belangrijk deel van de fysieke en infrastructurele controls af, wat auditors meewegen bij de leveranciersbeoordeling.

## Het Technisch Fundament Dat U Eerst Moet Leggen

Ongeacht wanneer u formeel certificeert, zijn de volgende technische fundamenten direct noodzakelijk. Ze vloeien voort uit de AVG / GDPR, worden standaard getoetst in inkoopvragenlijsten en sluiten naadloos aan op Annex A van ISO 27001:

| Domein | Vereiste Maatregel | Annex A Thema |
| --- | --- | --- |
| Toegangscontrole | Row Level Security (RLS) in de database, rolgebaseerde rechten (RBAC), periodieke toegangsrevisie | Technologisch, organisatorisch |
| Authenticatie | Verplichte MFA voor alle personeels- en admin-accounts, SSO voor interne tools | Technologisch |
| Geheimenbeheer | Geen hardcoded tokens in broncode, gecentraliseerde secrets manager met rotatieprocedures | Technologisch |
| Logging & Monitoring | Centrale logging van logins, rechtenmutaties en data-exports met een vaste bewaartermijn | Technologisch |
| Back-ups | Automatische dagelijkse back-ups met point-in-time recovery en periodiek gedocumenteerde hersteltests | Technologisch |
| Veilige Ontwikkeling | Verplichte code-reviews, aparte staging-omgeving, dependency-scans en geautomatiseerde tests | Technologisch |
| Wijzigingsbeheer | Productie-deployments uitsluitend via gecontroleerde en gelogde CI/CD-pijplijnen | Organisatorisch |
| Leveranciersbeheer | Actueel register van subverwerkers met getekende verwerkersovereenkomsten en vestigingslanden | Organisatorisch |
| Incidentenbeheer | Een geschreven incidentenprotocol, intern incidentenlogboek en contractuele meldtermijnen | Organisatorisch |
| Werkplekbeveiliging | Volledige schijfversleuteling (FileVault/BitLocker), schermvergrendeling en onboarding-checklists | Mensgericht, fysiek |

Met AI gebouwde softwareapplicaties vereisen specifieke aandacht rondom veilige ontwikkeling. Auditors toetsen steeds vaker hoe gegenereerde code wordt beoordeeld, hoe prompts worden beheerd en hoe wordt voorkomen dat bedrijfs- of klantdata weglekt naar externe AI-modellen. Sluitende code-reviews en geautomatiseerde checks leveren hierop het juiste antwoord.

## Een Realistische Roadmap van Twaalf Maanden

Wanneer de business case solide is, biedt het volgende stappenplan een beproefd tijdspad voor teams van 5 tot 15 medewerkers:

| Maanden | Focusgebied | Concreet Resultaat |
| --- | --- | --- |
| 1 - 2 | Technisch fundament | MFA, persoonlijke accounts, logging, geteste back-ups, CI/CD-pijplijn en secrets-beheer |
| 2 - 3 | Scope en risico's | ISMS-scopeomschrijving, asset-inventarisatie, risicoanalyse en risicobehandelplan |
| 3 - 4 | Beleid en SoA | Informatiebeveiligingsbeleid afgestemd op de werkelijkheid, opstellen Verklaring van Toepasselijkheid |
| 4 - 5 | Training en operatie | Security awareness training voor medewerkers, in- en uitdiensttredingsprocedures, leveranciersreviews |
| 5 - 8 | Bewijsperiode | Uitvoeren van toegangsrevisies, bijhouden incidentlog, registreren wijzigingen, interne audit |
| 8 - 9 | Directiebeoordeling & Fase 1 | Formele review door de directie, documenten-audit door de certificerende instelling |
| 9 - 11 | Afhandeling bevindingen & Fase 2 | Oplossen eventuele opmerkingen uit Fase 1, uitvoering van de praktijkaudit (Fase 2) |
| 11 - 12 | Certificaatuitreiking | Definitieve toekenning van het ISO 27001-certificaat en planning van de eerste controle-audit |

Twee uitgangspunten zijn hierbij essentieel. Ten eerste: begin altijd bij het technische fundament, want alle latere procesbeschrijvingen leunen daarop. Ten tweede: de bewijsperiode kan niet worden overgeslagen. Auditors willen zien dat procedures gedurende meerdere maanden consistent zijn uitgevoerd. Wijs bovendien direct vanaf dag één één interne eigenaar aan voor het ISMS; zonder duidelijke projectverantwoordelijke verliezen implementatietrajecten snel hun vaart.

## Veelgemaakte Fouten

**Een standaard beleidspakket downloaden en direct indienen.** Generieke templates die niet overeenkomen met hoe uw ontwikkelaars daadwerkelijk werken vallen tijdens de Fase 2-audit direct door de mand zodra auditors medewerkers interviewen.

**De audit-scope onnodig breed maken.** Wie in de eerste audit direct alle denkbare nevenactiviteiten opneemt, maakt het project onnodig zwaar. Beperk de initiële scope strikt tot het primaire SaaS-product en de bijbehorende cloudoperatie.

**Technische tekortkomingen uitstellen.** Een ISMS dat formeel beschrijft dat controles gebrekkig zijn, leidt niet tot een certificaat. Zorg dat de techniek staat voordat de auditor arriveert.

**Het certificaat zien als een eenmalig project.** ISO 27001 vereist doorlopend onderhoud: regelmatige toegangscontroles, jaarlijkse interne audits, directiebeoordelingen en toezichtaudits.

## Hoe LaunchStudio Helpt

LaunchStudio treedt niet op als uw certificerende instelling of beleidsadviseur. Wij bouwen het daadwerkelijke technische fundament dat certificering haalbaar maakt en zakelijke inkopers direct geruststelt: strenge databasetoegangscontrole, MFA, centraal geheimenbeheer, audit-logging, redundante back-ups met herstelvalidatie, beveiligde CI/CD-pijplijnen en monitoring. Daarnaast leveren we de technische systeembeschrijving op van uw architectuur. Oprichters die aansluitend een ISO-traject starten, ontdekken dat het leeuwendeel van het technologische bewijs al operationeel en gedocumenteerd is.

Ons **Launch Ready**-pakket (€800 - €3.500) omvat de complete beveiligingshardening en deployment; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) breidt dit uit met beheerde cloudhosting, automatische back-ups en prioriteitsondersteuning. Raadpleeg onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte prijsindicatie.

LaunchStudio wordt ondersteund door Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ gerealiseerde softwareprojecten en ruim 120 senior engineers. We bouwden bedrijfskritische software onder de stringente security-eisen van enterprise-opdrachtgevers zoals Vodafone en TNO. Manifera's CEO Herre Roelevink was medeoprichter van cybersecurity-organisatie CyberDevOps (nu CFLW Cyber Strategies). Oprichters ontmoeten onze adviseurs aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit ons softwarecentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Contracttool Die Nog Niet Audit-Klaar Was

Wouter Jansen en zijn medeoprichter ontwikkelden met behulp van Lovable en Supabase de applicatie Contractkompas: een softwareoplossing voor middelgrote organisaties waarmee contracten, opzegtermijnen, wederzijdse verplichtingen en goedkeuringsflows overzichtelijk worden beheerd. Na een jaar had de startup 35 betalende klanten. Vervolgens dienden zich twee grote prospects aan, een woningcorporatie en een regionale ziekenhuisgroep, die beiden contractueel eisten dat Contractkompas binnen twaalf maanden na ondertekening ISO 27001 gecertificeerd zou zijn.

Wouter schakelde een ISO-consultant in, wiens nulmeting direct een heldere conclusie opleverde: vóórdat er ook maar één beleidsdocument geschreven kon worden, moest de technische basis grondig worden gerenoveerd. Beheertoegang werd gedeeld via één generiek admin-account zonder MFA, logbestanden werden niet bewaard, back-ups draaiden wel maar waren nog nooit teruggezet, updates werden vanuit Lovable rechtstreeks naar de productieomgeving gepubliceerd en er was geen overzicht van welke externe sub-services klantdata verwerkten. Beleid schrijven bovenop deze situatie zou neerkomen op het documenteren van maatregelen die in de praktijk niet bestonden.

LaunchStudio voorzag alle medewerkers van individuele accounts met verplichte MFA en verplaatste beheerautorisaties naar specifieke database-rollen via PostgreSQL Row Level Security. Er werd gestructureerde audit-logging ingericht voor logins, rechtenmutaties en contract-exports met een vastgestelde bewaartermijn. Point-in-time recovery werd geconfigureerd inclusief een gedocumenteerde hersteltest, en een staging-omgeving met GitHub-gebaseerde deployments en collegiale code-reviews verving de directe productiemutaties. API-sleutels werden overgebracht naar een managed secrets manager, en onze engineers stelden een complete technische systeembeschrijving en een subverwerkersregister op voor het ISMS-dossier.

**Resultaat:** De technische hardening werd binnen 12 werkdagen voltooid. Contractkompas startte de formele bewijsperiode de maand daarop, doorstond de Fase 2-audit negen maanden later en behaalde het ISO 27001-certificaat ruim binnen de termijn die beide grote prospects hadden gesteld. De externe auditor constateerde geen enkele significante afwijking op de technologische beheersmaatregelen.

> *"Onze consultant had volkomen gelijk: je kunt geen beveiliging certificeren die je simpelweg niet hebt. Door eerst het technische fundament te herstellen, werd het gehele ISO-traject maanden korter en inhoudelijk ijzersterk."*
> - **Wouter Jansen, Medeoprichter, Contractkompas (Den Bosch)**

**Kosten & Doorlooptijd:** €3.600 (Launch Ready-pakket: persoonlijke accounts en MFA, rolgebaseerde autorisatie via RLS, audit-logging, back-up-herstelvalidatie, CI/CD-deploymentpijplijn en technische systeembeschrijving) - afgerond in 12 werkdagen.

## Veelgestelde Vragen

### Is ISO 27001 de investering waard voor een vroege SaaS-startup?

Het is de investering waard zodra grote potentiële klanten certificering stellen als harde eis voor contractondertekening, met name binnen de enterprise-markt, zorg, financiële sector of overheid. Vóór dat moment rendeert dezelfde investering aanzienlijk beter door te focussen op de technische beveiligingsbaseline en een overtuigend Beveiligingsoverzicht, waarmee u veel inkopers direct overtuigt en latere certificering aanzienlijk versnelt.

### Hoe lang duurt een ISO 27001-certificeringstraject voor een startup?

Voor de meeste compacte SaaS-bedrijven duurt het traject 6 tot 12 maanden vanaf de formele start tot aan het behalen van het certificaat. De doorlooptijd hangt primair af van de volwassenheid van de bestaande technische beveiliging. Bedrijven die hun technische controls vooraf op orde brengen, doorlopen de beleidsfase en audits veruit het snelst.

### Schrijft ISO 27001 specifieke verplichte beveiligingstools voor?

Nee. ISO 27001 eist een risicogebaseerde selectie van maatregelen uit Annex A, die u verantwoordt in een Verklaring van Toepasselijkheid (SoA). In de praktijk verwachten auditors bij SaaS-bedrijven echter altijd sterke database-autorisatie, MFA voor personeel, logging, geteste back-ups, veilige softwareontwikkeling, leveranciersbeoordelingen en een incidentenplan.

### Waarom is Manifera's ervaring waardevol bij de voorbereiding op ISO 27001?

Manifera ontwikkelt al ruim 11 jaar software conform de strenge beveiligingseisen van grote enterprise-organisaties, en onze directie heeft een bewezen achtergrond in de cybersecurity. LaunchStudio past die ervaring toe om exact die technische controles te bouwen die auditors verlangen, zodat u daadwerkelijke beveiliging documenteert in plaats van loze intenties.

### Versterkt een ISO 27001-certificering de vindbaarheid van mijn software?

Jazeker. Het behalen van een ISO 27001-certificering vormt een uitzonderlijk sterk vertrouwenssignaal. Een openbare compliance- en trust-pagina met de scope en details van uw certificering levert exact het type verifieerbare, gestructureerde informatie op dat zoekmachines en AI-antwoordmachines (zoals ChatGPT Search en Perplexity) presenteren wanneer zakelijke beslissers leveranciers vergelijken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is ISO 27001 de investering waard voor een vroege SaaS-startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het loont zodra enterprise-klanten of overheden het contractueel vereisen. Vóór die fase levert een technisch fundament en een sterk security-overzicht meer op en verkort het latere audits." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een ISO 27001-certificeringstraject voor een startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal 6 tot 12 maanden van voorbereiding tot certificaat. De duur wordt bepaald door de reeds aanwezige technische controls en de verplichte bewijsperiode van het ISMS." }
    },
    {
      "@type": "Question",
      "name": "Schrijft ISO 27001 specifieke verplichte beveiligingstools voor?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, de norm vereist een risicogebaseerde selectie uit Annex A verantwoord in een Verklaring van Toepasselijkheid. Wel verwachten auditors standaard MFA, RLS, logging en geteste back-ups." }
    },
    {
      "@type": "Question",
      "name": "Waarom is Manifera's ervaring waardevol bij de voorbereiding op ISO 27001?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar software onder enterprise security-eisen en LaunchStudio levert de concrete technische maatregelen en bewijzen op die externe auditors toetsen." }
    },
    {
      "@type": "Question",
      "name": "Versterkt een ISO 27001-certificering de vindbaarheid van mijn software?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een openbare trust-pagina met geverifieerde certificeringsdata vormt hoogwaardige gestructureerde data die zoekmachines en AI-systemen citeren bij leveranciersselecties." }
    }
  ]
}
</script>
