---
Titel: "NIS2 voor SaaS-startups: Is het van toepassing op uw bedrijf?"
Trefwoorden: nis2 saas startup, nis2 toepasselijkheid, cyberbeveiligingswet saas, nis2 leveranciersketen vereisten, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# NIS2 voor SaaS-startups: Is het van toepassing op uw bedrijf?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "NIS2 voor SaaS-startups: Is het van toepassing op uw bedrijf?",
  "description": "De NIS2-richtlijn breidt de Europese cybersecurity-verplichtingen fors uit naar talloze organisaties, maar de meeste kleine SaaS-startups worden vooral indirect via hun zakelijke klanten geraakt. Deze handleiding legt uit wie er direct onder de wet valt, de omvangscriteria, de Nederlandse Cyberbeveiligingswet, wat enterprise-klanten van toeleveranciers eisen en welke praktische maatregelen een met AI gebouwde SaaS moet nemen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-28",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/nis2-for-saas-startups-does-it-apply-to-you" },
  "citation": [
    { "@type": "CreativeWork", "name": "Directive (EU) 2022/2555 (NIS2)", "url": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj" },
    { "@type": "CreativeWork", "name": "European Commission: NIS2 Directive", "url": "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive" },
    { "@type": "CreativeWork", "name": "Commission Recommendation 2003/361/EC on SME definition", "url": "https://eur-lex.europa.eu/eli/reco/2003/361/oj" },
    { "@type": "CreativeWork", "name": "NCSC Netherlands", "url": "https://www.ncsc.nl/" }
  ]
}
</script>

Sinds de inwerkingtreding van de Europese NIS2-richtlijn worden oprichters overspoeld met e-mails, webinars en commerciële verhalen die suggereren dat elk bedrijf met een server nu onder zware nieuwe cyberveiligheidswetgeving valt. Voor een SaaS-startup van twee of drie personen, gebouwd met tools zoals Lovable of Cursor, roept dit een begrijpelijke zorg op: geldt NIS2 direct voor mij, en wat moet ik concreet regelen?

Het eerlijke antwoord voor vrijwel elke vroegtijdige SaaS-onderneming luidt: direct waarschijnlijk niet, maar indirect vrijwel zeker wel. NIS2 legt verplichtingen op aan middelgrote en grote organisaties in aangewezen sectoren, en een cruciale wettelijke plicht is het beheersen van de beveiliging in hun toeleveringsketen. Zodra uw zakelijke klanten onder NIS2 vallen, zullen hun inkoopvoorwaarden en beveiligingsvragenlijsten de NIS2-standaarden direct bij u neerleggen - ongeacht of de wet uw kleine startup expliciet noemt.

Deze gids brengt helderheid in waar u staat en welke maatregelen verstandig zijn. Dit is een praktisch en technisch overzicht, geen formeel juridisch advies; raadpleeg voor een bindende beoordeling een gespecialiseerd jurist of het Nationaal Cyber Security Centrum (NCSC).

## Belangrijkste Punten

- **NIS2 is direct van toepassing op middelgrote en grote entiteiten in aangewezen sectoren,** plus enkele uitzonderingscategorieën ongeacht hun omvang. Vrijwel alle vroege SaaS-startups vallen ruim onder de personeels- en omzetdrempels.
- **Verschillende digitale diensten vallen als sector onder de richtlijn,** zoals cloud computing, datacenters en managed service providers (MSP's), maar ook daar gelden in de basis de omvangscriteria.
- **Het indirecte effect via de toeleveringsketen is de werkelijke realiteit voor startups.** Gereguleerde klanten moeten hun leveranciersketen beveiligen en eisen harde bewijzen van gedegen informatiebeveiliging.
- **In Nederland wordt NIS2 geïmplementeerd via de Cyberbeveiligingswet (Cbw);** raadpleeg officiële overheidsbronnen voor de actuele status van de wetgeving.
- **De maatregelen die NIS2 voorschrijft zijn sowieso best practices voor software-engineering:** risicobeheer, incidentafhandeling, tweefactorauthenticatie (MFA), veilige softwareontwikkeling, geteste back-ups en subverwerkersbeheer.

## Wat NIS2 Precies Inhoudt

NIS2, officieel Richtlijn (EU) 2022/2555, vervangt de oorspronkelijke NIS-richtlijn uit 2016. Het doel is het niveau van cyberbeveiliging in de hele Europese Unie structureel te verhogen door het aantal sectoren drastisch uit te breiden, minimale beveiligingseisen op te leggen, strikte meldplichten voor incidenten in te voeren en bestuurders persoonlijk aansprakelijk te stellen voor verwaarlozing. Lidstaten moesten de richtlijn uiterlijk op 17 oktober 2024 omzetten in nationaal recht; diverse landen, waaronder Nederland, hadden meer voorbereidingstijd nodig.

De richtlijn maakt onderscheid tussen twee categorieën organisaties:

- **Essentiële entiteiten:** overwegend grote ondernemingen in sectoren uit Bijlage I, zoals energie, transport, bankwezen, gezondheidszorg, drinkwater, digitale infrastructuur en ICT-dienstbeheer.
- **Belangrijke entiteiten:** middelgrote bedrijven in Bijlage I-sectoren en middelgrote tot grote ondernemingen in Bijlage II-sectoren, zoals post- en koeriersdiensten, afvalbeheer, chemie, voedselproductie, maakindustrie en digitale aanbieders.

Beide categorieën moeten passende risicomaatregelen treffen en ernstige cyberincidenten verplicht melden. Het onderscheid zit vooral in het toezicht: essentiële entiteiten staan onder proactief toezicht, terwijl belangrijke entiteiten hoofdzakelijk reactief worden gecontroleerd na een incident of gefundeerde klacht.

## De Omvangscriteria: Waarom Startups Direct Buiten Schot Blijven

NIS2 hanteert als algemeen uitgangspunt de Europese mkb-definitie: een entiteit moet minimaal middelgroot zijn. In de praktijk betekent dit dat een onderneming minimaal 50 medewerkers in dienst heeft, of een jaaromzet én balanstotaal van meer dan €10 miljoen behaalt. Blijft een onderneming daaronder, dan wordt zij geclassificeerd als klein- of microbedrijf en valt zij in beginsel buiten het directe toepassingsbereik van NIS2.

Er zijn enkele zeldzame uitzonderingen waarbij omvang er niet toe doet. Dit betreft onder meer aanbieders van openbare elektronische communicatienetwerken, verleners van gekwalificeerde vertrouwensdiensten, topleveldomein-registers (zoals SIDN) en DNS-dienstverleners, of bedrijven die door een lidstaat specifiek als kritiek zijn aangewezen. Een doorsnee SaaS-bedrijf valt hier vrijwel nooit onder.

| Uw Bedrijfssituatie | Direct NIS2-plichtig? |
| --- | --- |
| Minder dan 50 medewerkers en omzet onder €10 miljoen, reguliere SaaS | In principe nee |
| Middelgroot of groot, levert zakelijke cloud computing-diensten | Zeer waarschijnlijk ja, als aanbieder van digitale infrastructuur |
| Middelgrote of grote Managed Service Provider (MSP) die klant-IT beheert | Zeer waarschijnlijk ja, onder ICT-dienstbeheer |
| Middelgrote of grote online marktplaats of zoekmachine | Zeer waarschijnlijk ja, als digitale aanbieder |
| Elke omvang, actieve DNS-dienstverlener of vertrouwensdienst | Vrijwel zeker ja |
| Kleine SaaS die software levert aan ziekenhuizen, waterbedrijven of netbeheerders | Direct nee, maar zeer zwaar geraakt via de leveranciersketen |

Let op: concernstructuren tellen mee. Als uw startup eigendom is van een grotere holding of investeringsgroep, kan het totale personeelsaantal van de groep bepalend zijn.

## Het Indirecte Effect: Beveiliging van de Toeleveringsketen

Dit is het mechanisme waarmee NIS2 impact heeft op nagenoeg elke B2B SaaS-onderneming. Artikel 21 van de richtlijn verplicht gereguleerde entiteiten om risicobeheermaatregelen te treffen die expliciet de **beveiliging van de toeleveringsketen** (supply chain security) omvatten. Zij moeten toezien op de informatiebeveiliging van hun directe toeleveranciers en dienstverleners. In de praktijk dwingt dit enterprise-klanten om de veiligheid van alle ingekochte software grondig te toetsen, harde contractvoorwaarden op te leggen en doorlopend toezicht te houden.

Indien u uw software verkoopt aan een ziekenhuis, netbeheerder, logistiek concern, financiële instelling of overheidsinstantie, krijgt u onvermijdelijk te maken met:

- **Uitgebreide vendor assessment vragenlijsten** over toegangsbeheer, MFA, versleuteling, logging, kwetsbaarhedenbeheer, back-upintegriteit en incidentrespons.
- **Contractuele clausules** die u verplichten om beveiligingsincidenten extreem snel te melden, dikwijls binnen 24 uur na ontdekking.
- **Verzoeken om auditbewijs,** zoals formele beveiligingsverklaringen, pentest-samenvattingen of externe certificeringen.
- **Vragen over uw eigen subverwerkers,** inclusief hostingproviders, database-leveranciers en externe AI-API's (zoals OpenAI of Anthropic).

Een SaaS-startup die deze documentatie direct en professioneel overhandigt, wint deals die concurrenten verliezen. Een startup die geen antwoord heeft, ziet offertes geruisloos stranden bij de inkoopafdeling.

## Welke Maatregelen NIS2 Concreet Voorschrijft

Zelfs als u formeel niet direct onder de wet valt, biedt de lijst van maatregelen in Artikel 21 de perfecte blauwdruk van wat zakelijke inkopers van u verwachten. De richtlijn vereist een integrale aanpak die minimaal de volgende onderdelen dekt:

1. Beleid inzake risicoanalyse en beveiliging van informatiesystemen
2. Incidentbehandeling en respons
3. Bedrijfscontinuïteit, inclusief back-upbeheer en noodherstelplannen (disaster recovery)
4. Beveiliging van de toeleveringsketen
5. Beveiliging bij de verwerving, ontwikkeling en het onderhoud van netwerk- en informatiesystemen, inclusief het afhandelen van kwetsbaarheden
6. Beleid en procedures om de doeltreffendheid van beveiligingsmaatregelen te beoordelen
7. Basisbeginselen van cyberhygiëne en gerichte security-trainingen
8. Beleid inzake het gebruik van cryptografie en versleuteling
9. Beveiligingsaspecten van personeel, toegangscontrole en activabeheer (asset management)
10. Het gebruik van meervoudige verificatie (MFA) en beveiligde communicatiemiddelen

NIS2 introduceert bovendien strikte meldtermijnen voor significante incidenten: een vroegtijdige waarschuwing binnen 24 uur na ontdekking, een officiële incidentmelding binnen 72 uur en een eindrapportage binnen één maand. Uw gereguleerde klanten moeten aan deze deadlines voldoen, en leggen daarom identieke meldplichten contractueel bij u neer.

De wettelijke boetes voor niet-naleving door gereguleerde bedrijven kunnen oplopen tot €10 miljoen of 2% van de wereldwijde jaaromzet voor essentiële entiteiten, en €7 miljoen of 1,4% voor belangrijke entiteiten. Bovendien kan het bestuur persoonlijk aansprakelijk worden gesteld. Dat verklaart waarom enterprise-inkopers geen enkel compromis sluiten op leveranciersveiligheid.

## De Situatie in Nederland: De Cyberbeveiligingswet

In Nederland wordt de Europese NIS2-richtlijn omgezet in nationale wetgeving via de Cyberbeveiligingswet (Cbw), die de eerdere Wet beveiliging netwerk- en informatiesystemen (Wbni) vervangt. Het Nederlandse wetgevingstraject vergde meer tijd dan de Europese richtsnoerdatum. Het Nationaal Cyber Security Centrum (NCSC) en de Rijksinspectie Digitale Infrastructuur (RDI) vormen de officiële gezaghebbende bronnen voor sectorale toewijzingen en registratieverplichtingen.

Voor een ambitieuze SaaS-startup is de formele ingangsdatum minder relevant dan de marktrichting. Grote Nederlandse organisaties in de zorg, energiesector, transport, waterbedrijven en het openbaar bestuur bereiden zich nu al volop voor. Hun inkoopteams stellen vandaag al concrete vragen aan softwareleveranciers op basis van de komende Cbw-normen.

## De Praktische Beveiligingsbaseline voor een Jonge SaaS

Als niet-gereguleerde startup hoeft u geen zwaar enterprise compliance-programma op te tuigen. U heeft echter wel een solide technische basis nodig waarmee u de inkoopvragen van klanten naar waarheid en met overtuiging kunt beantwoorden:

| Beveiligingsdomein | Minimale standaard voor een gezonde SaaS |
| --- | --- |
| Toegangscontrole | Row Level Security (RLS) afgedwongen op alle klantdata, getest met afzonderlijke accounts |
| Authenticatie | Verplichte MFA voor alle interne medewerkers en beheerders, optionele MFA voor eindgebruikers |
| Geheimenbeheer | Geen API-keys in git-repositories, beheer via secrets managers met gedocumenteerde rotatie |
| Versleuteling | Volledige HTTPS/TLS-encryptie voor data in transit, AES-256 voor data at rest bij cloudhosts |
| Logging & Auditing | Relevante logins, fouten en beheerdershandelingen gestructureerd gelogd en bewaard |
| Back-ups | Automatische dagelijkse back-ups met point-in-time recovery en periodieke hersteltests |
| Kwetsbaarhedenbeheer | Geautomatiseerde dependency-alerts (bijv. Dependabot) en een strak patchbeleid voor CVE's |
| Incidentrespons | Een actieplan van één pagina: wie beslist, wie informeert klanten en binnen welke termijn |
| Subverwerkers | Een gedocumenteerde lijst van externe platforms en cloudregio's met afgesloten verwerkersovereenkomsten |
| Ontwikkeling | Collegiale code-reviews, aparte staging-omgeving en geen directe wijzigingen in productie |

Het merendeel van deze eisen vloeit tevens direct voort uit Artikel 32 van de AVG / GDPR voor de bescherming van persoonsgegevens. NIS2 en de AVG wijzen in dezelfde richting.

## Documenten Die Inkooptrajecten Versnellen

Stel de volgende documenten één keer professioneel op en hergebruik ze bij elk verkooptraject:

- **Een Beveiligingsoverzicht (Security Whitepaper)** van 2 tot 4 pagina's: cloudarchitectuur, hostinglocaties binnen de EU, encryptie, toegangsbeheer, logging en incidentbehandeling.
- **Een actuele lijst van subverwerkers** met vermelding van de verwerkte datapunten en de juridische vestigingsplaats.
- **Een samenvatting van het incidentresponsplan** waarin u realistische en haalbare meldtermijnen contractueel toezegt.
- **Een vooraf ingevulde standaardvragenlijst,** zodat u binnen 24 uur antwoord kunt geven op inkoopvragen.
- **Een heldere verwerkersovereenkomst (DPA)** conform de AVG voor klanten die persoonsgegevens bij u onderbrengen.

Zodra een enterprise-klant vraagt naar uw NIS2-volwassenheid, wekt het overleggen van dit professionele dossier binnen één werkdag meer vertrouwen dan een certificaat dat u nog niet bezit.

## Veelvoorkomende Misvattingen

**"NIS2 verplicht ons om ISO 27001 te behalen."** Niet waar. NIS2 schrijft geen specifiek auditcertificaat voor. ISO 27001 is een erkende manier om volwassenheid aan te tonen, maar het behalen ervan is een commerciële kosten-batenafweging. Onze gids over [ISO 27001 voor vroege SaaS-bedrijven](https://launchstudio.eu/nl/blog/iso-27001-for-early-stage-saas-when-to-start) belicht het juiste instapmoment.

**"Wij hosten op AWS of Supabase, dus zij regelen onze security."** Uw cloudprovider beveiligt de fysieke datacenters en de hypervisor. Uw datamodel, applicatiecode, gebruikersrollen, beheerderswachtwoorden en incidentenafhandeling blijven te allen tijde uw eigen verantwoordelijkheid.

**"Onze startup is te klein om aangevallen te worden."** Kleinere leveranciers vormen voor kwaadwillenden juist de aantrekkelijkste route om binnen te dringen bij grote enterprise-organisaties. Dat is exact de reden waarom supply chain security een hoeksteen vormt van NIS2.

## Hoe LaunchStudio Helpt

LaunchStudio helpt oprichters om de technische beveiligingsbaseline direct robuust in te richten: sterke database-autorisatie, MFA, veilige geheimenopslag, audit-logging, back-ups en een gestroomlijnde deployment-pijplijn. Daarnaast stellen we samen met u het beveiligingsoverzicht en de subverwerkersdocumentatie op die zakelijke inkopers verlangen. Ons **Launch Ready**-pakket (€800 - €3.500) omvat de beveiligingshardening en productie-deployment; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) vult dit aan met beheerde hosting, redundante back-ups en prioriteitsondersteuning. Raadpleeg onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte indicatie.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde maatwerkprojecten en ruim 120 senior engineers. Manifera's CEO Herre Roelevink was medeoprichter van het cybersecuritybedrijf CyberDevOps (thans CFLW Cyber Strategies), dat in nauwe samenwerking met TNO een toonaangevende Dark Web Monitor ontwikkelde. Oprichters ontmoeten onze adviseurs aan de Herengracht 420 in Amsterdam; onze engineeringteams werken vanuit ons ontwikkelingscentrum aan Pho Quang Street in Ho Chi Minh City, met een regionale hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Onderhoudsplanner Die een Waterbedrijf Overtuigde

Bas Hendriks, voormalig onderhoudsmonteur, bouwde met behulp van Cursor de applicatie Onderhoudsplan: een gespecialiseerde planningstool waarmee technische diensten inspecties en revisies van pompen, leidingen en industriële afsluiters beheren. Zijn bedrijf telde drie medewerkers en behaalde een bescheiden omzet; NIS2 was direct dus geenszins op hem van toepassing. Zijn eerste grote potentiële klant, een regionaal waterbedrijf in Gelderland, viel echter onomstotelijk onder de essentiële NIS2-entiteiten.

Het inkoopteam van het waterbedrijf stuurde Bas een leveranciersbeveiligingsvragenlijst met 74 gedetailleerde vragen die expliciet verwezen naar NIS2, inclusief de eis om incidenten binnen 24 uur formeel te melden. Bas kon op dat moment slechts een derde van de vragen positief beantwoorden. Interne accounts hadden geen MFA, het beheerpaneel was uitsluitend beveiligd via een oppervlakkige e-mailcheck in de frontend, er waren geen auditlogs, back-ups waren nog nooit succesvol hersteld en nergens stond vastgelegd welke cloudtools precies klantdata verwerkten.

LaunchStudio implementeerde verplichte MFA voor alle medewerkers en beheerders, verplaatste de autorisatie naar de PostgreSQL-database via Row Level Security en rolgebaseerde controles, en voegde gestructureerde audit-logging toe voor alle logins en beheeractiviteiten. Er werd point-in-time recovery ingericht met een gedocumenteerde hersteltest, API-sleutels werden overgebracht naar een veilige secrets manager, en de code werd voorzien van dependency-scanning. Tot slot hielpen onze engineers Bas bij het opstellen van een overzichtelijk security whitepaper, een overzicht van subverwerkers en een praktisch incidentenprotocol met een haalbare meldtermijn van 24 uur.

**Resultaat:** Bas leverde de ingevulde vragenlijst binnen 9 werkdagen in, compleet met alle gevraagde bijlagen. Het waterbedrijf accepteerde het dossier na slechts twee inhoudelijke verduidelijkingsvragen en rolde Onderhoudsplan het kwartaal daarop uit over al haar onderhoudsteams. Dezelfde documentenset verkortte twee opvolgende inkooptrajecten bij andere nutsbedrijven tot minder dan een week.

> *"Mijn bedrijf viel zelf niet onder NIS2, maar mijn grootste klant wel. Het vakkundig kunnen beantwoorden van hun beveiligingsvragen was letterlijk het verschil tussen een vrijblijvende pilot en een getekend meerjarencontract."*
> - **Bas Hendriks, Oprichter, Onderhoudsplan (Arnhem)**

**Kosten & Doorlooptijd:** €3.400 (Launch Ready-pakket: implementatie MFA, database-autorisatie, audit-logging, back-upvalidatie, secrets-migratie en opstellen beveiligingsdossier) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Is NIS2 direct van toepassing op een kleine SaaS-startup?

In de regel niet direct. NIS2 richt zich hoofdzakelijk op middelgrote en grote organisaties (vanaf 50 medewerkers of €10 miljoen omzet) in vitale sectoren, afgezien van enkele omvangsonafhankelijke uitzonderingen zoals DNS-aanbieders. Indien uw zakelijke klanten echter wél gereguleerd zijn, moeten zij hun toeleveringsketen beveiligen, waardoor NIS2-eisen via inkoopvragenlijsten en contracten direct bij u terechtkomen.

### Welke concrete vragen stellen NIS2-gereguleerde klanten aan mijn SaaS?

U kunt gedetailleerde vragen verwachten over uw toegangsbeheer, verplichte MFA voor medewerkers, versleuteling van data in rust en transport, logging van beheerdersacties, patchbeleid voor kwetsbaarheden, back-upintegriteit en een lijst van uw subverwerkers. Daarnaast vragen zij om contractuele garanties voor het direct melden van beveiligingsincidenten.

### Moet mijn SaaS-bedrijf verplicht een ISO 27001-certificaat hebben voor NIS2?

Nee. NIS2 eist nergens een specifiek formele certificering zoals ISO 27001 of SOC 2. Sommige grote enterprise-klanten vragen hier commercieel wel om, maar een gedegen technisch beveiligingsdossier en een transparante verantwoording van uw maatregelen volstaan voor de meeste inkopers ruimschoots.

### Waarom is Manifera's achtergrond waardevol voor NIS2-voorbereiding?

Manifera's CEO was medeoprichter van een gespecialiseerd cybersecuritybedrijf dat samen met TNO geavanceerde monitors bouwde. Bovendien ontwikkelt Manifera al meer dan 11 jaar enterprise-systemen die voldoen aan strenge corporate beveiligingseisen. LaunchStudio past die diepgaande kennis toe om startups een pragmatisch en verdedigbaar beveiligingsniveau te bieden.

### Helpt openbare beveiligingsdocumentatie bij de vindbaarheid van mijn product?

Jazeker. Een heldere, openbare beveiligingspagina met informatie over datacenters binnen de EU, encryptiestandaarden en subverwerkers helpt inkoopteams bij hun initiële screening. Deze gestructureerde technische data wordt bovendien uitstekend opgepikt door zoekmachines en AI-zoeksystemen (zoals ChatGPT Search en Perplexity) wanneer zakelijke beslissers leveranciers vergelijken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is NIS2 direct van toepassing op een kleine SaaS-startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "In de regel niet direct, omdat NIS2 primair geldt voor middelgrote en grote bedrijven. Wel bereiken de eisen startups indirect via gereguleerde klanten die hun toeleveringsketen moeten beveiligen." }
    },
    {
      "@type": "Question",
      "name": "Welke concrete vragen stellen NIS2-gereguleerde klanten aan mijn SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vragen over toegangsbeheer, MFA, encryptie, logging, kwetsbaarheden, back-upintegriteit, subverwerkers en een contractuele verplichting voor snelle incidentmelding." }
    },
    {
      "@type": "Question",
      "name": "Moet mijn SaaS-bedrijf verplicht een ISO 27001-certificaat hebben voor NIS2?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. NIS2 verplicht geen specifieke certificering. Een helder beveiligingsoverzicht en bewezen maatregelen voldoen voor de meeste inkopers in een vroege fase." }
    },
    {
      "@type": "Question",
      "name": "Waarom is Manifera's achtergrond waardevol voor NIS2-voorbereiding?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's CEO richtte eerder een cybersecuritybedrijf op en het team bouwt al 11+ jaar software volgens strenge securitynormen. LaunchStudio vertaalt dit naar praktische maatregelen voor startups." }
    },
    {
      "@type": "Question",
      "name": "Helpt openbare beveiligingsdocumentatie bij de vindbaarheid van mijn product?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een openbare securitypagina helpt inkoopteams en biedt gestructureerde data die zoekmachines en AI-antwoordmachines direct citeren bij leveranciersvergelijkingen." }
    }
  ]
}
</script>
