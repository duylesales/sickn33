---
Titel: "DORA voor SaaS-leveranciers aan Financiële Instellingen"
Trefwoorden: dora saas leverancier, dora ict derde partij, dora contractvereisten, saas verkopen aan banken europa, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# DORA voor SaaS-leveranciers aan Financiële Instellingen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DORA voor SaaS-leveranciers aan Financiële Instellingen",
  "description": "De Digital Operational Resilience Act (DORA) geldt voor financiële entiteiten in de EU, maar SaaS-startups die leveren aan banken, verzekeraars, betaalinstellingen en beleggingsondernemingen merken dit direct via strenge contracten, audits en exit-verplichtingen. Deze handleiding legt uit wat DORA eist van ICT-derdepartijen, welke contractbepalingen u kunt verwachten, welk technisch bewijs inkopers verlangen en hoe u een met AI gebouwde SaaS hierop voorbereidt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-29",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/dora-for-saas-suppliers-to-financial-firms" },
  "citation": [
    { "@type": "CreativeWork", "name": "Regulation (EU) 2022/2554 (DORA)", "url": "https://eur-lex.europa.eu/eli/reg/2022/2554/oj" },
    { "@type": "CreativeWork", "name": "EIOPA: Digital Operational Resilience Act", "url": "https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en" },
    { "@type": "CreativeWork", "name": "De Nederlandsche Bank: DORA", "url": "https://www.dnb.nl/en/sector-information/open-book-supervision/laws-and-eu-regulations/dora/" },
    { "@type": "CreativeWork", "name": "AFM: DORA", "url": "https://www.afm.nl/en/sector/themas/dora" }
  ]
}
</script>

Financiële instellingen zijn uiterst aantrekkelijke opdrachtgevers voor SaaS-startups. Ze beschikken over aanzienlijke budgetten, schaffen graag gespecialiseerde tools aan en blijven jarenlang klant zodra een softwareoplossing eenmaal is ingebed in hun operationele processen. Een oprichter die een compliance-dashboard, een onboarding-tool, een document-workflow of een analytics-product bouwt voor banken, verzekeraars, betaalinstellingen of vermogensbeheerders kan snel een zeer winstgevende niche veroveren.

Sinds januari 2025 opereren al deze financiële partijen onder de Digital Operational Resilience Act, kortweg DORA. DORA reguleert uw startup in de meeste gevallen niet rechtstreeks. De wet reguleert uw zakelijke klant, en een van de centrale pijlers is de wijze waarop financiële entiteiten het operationele risico van hun externe technologieleveranciers beheersen. Dit betekent dat het inkooptraject voor zelfs een bescheiden SaaS-applicatie tegenwoordig gepaard gaat met gedetailleerde contractbepalingen, auditrechten, exitstrategieën en technische bewijslast die veel startups overvalt.

Deze handleiding legt uit wat DORA betekent voor een SaaS-leverancier en hoe u uw product zó inricht dat het inkoopproces verandert van een bureaucratische hindernis in een doorslaggevend verkoopargument. Dit is een praktisch en technisch overzicht, geen formeel juridisch advies.

## Belangrijkste Punten

- **DORA is van kracht voor financiële entiteiten in de EU sinds 17 januari 2025.** SaaS-leveranciers worden als 'ICT-derdepartij' geraakt via de wettelijke verplichtingen van hun opdrachtgevers.
- **Contracten moeten specifieke bepalingen bevatten** conform Artikel 30 van DORA, waaronder nauwkeurige dienstbeschrijvingen, data-locaties binnen de EU, informatiebeveiliging, incidentondersteuning, auditrechten, opzeggingsgronden en exitstrategieën.
- **De vereisten zijn aanzienlijk strenger wanneer uw dienst een kritieke of belangrijke functie ondersteunt** van de financiële instelling.
- **Financiële partijen moeten een wettelijk informatieregister bijhouden van alle ICT-contracten,** waardoor u gedetailleerde vragen kunt verwachten over uw onderaannemers, datastromen en hostingregio's.
- **De technische vereisten sluiten aan bij gedegen software-engineering:** robuuste autorisatie, gestructureerde audit-logging, geteste back-ups, incidentenprotocollen en een geautomatiseerd dataportabiliteitsmechanisme.

## Wat DORA Precies Inhoudt

DORA, formeel Verordening (EU) 2022/2554, is een rechtstreeks toepasselijke Europese verordening voor de financiële sector. In tegenstelling tot een richtlijn vereist DORA geen omzetting in nationaal recht, al zien nationale toezichthouders zoals De Nederlandsche Bank (DNB) en de Autoriteit Financiële Markten (AFM) in Nederland toe op de strikte handhaving ervan. De verordening omvat banken, betaal- en e-geldinstellingen, beleggingsondernemingen, crypto-activadienstverleners, verzekeraars, herverzekeraars, pensioenfondsen en crowdfundingplatforms.

De kern van DORA rust op vijf thematische pijlers:

1. **ICT-risicobeheer:** bestuursstructuren, kaders en preventieve controlemaatregelen voor technologierisico's
2. **Beheer en melding van ICT-gerelateerde incidenten:** classificatie en verplichte melding van ernstige incidenten aan toezichthouders
3. **Testen van digitale operationele weerbaarheid:** van basale kwetsbaarheidsscans tot geavanceerde dreigingsgestuurde penetratietests (TLPT)
4. **Beheersing van het ICT-concentratierisico bij derdepartijen:** toezicht op en risicobeheersing van externe technologieleveranciers
5. **Informatiedeling:** het vrijwillig uitwisselen van cyberdreigingsinformatie tussen instellingen

Voor een SaaS-leverancier is pijler vier de plek waar DORA u direct raakt, terwijl elementen uit pijler twee en drie terugkomen in de verplichte contractvoorwaarden.

## Hoe DORA een SaaS-Leverancier Bereikt

DORA definieert elk bedrijf dat digitale en datadiensten levert aan een financiële instelling als een ICT-derdepartij (ICT third-party service provider). Dit betreft grote cloudproviders en datacenters, maar nadrukkelijk ook SaaS-bedrijven die doorlopende softwarefunctionaliteit leveren. Uw financiële klant is wettelijk verplicht om:

- **Voorafgaand aan het contract een grondige risicoanalyse uit te voeren,** inclusief uw informatiebeveiliging, continuïteit en concentratierisico
- **Het contract op te nemen in een formeel informatieregister** dat te allen tijde opvraagbaar is door toezichthouders (zoals DNB of de ECB)
- **Verplichte contractuele clausules op te leggen** in de samenwerkingsovereenkomst
- **Gedurende de looptijd toezicht te houden,** inclusief het recht op fysieke en digitale audits
- **Een uitgewerkte exitstrategie te hanteren** zodat uw software vervangen kan worden zonder dat de financiële operatie stagneert

De allergrootste hyperscalers (zoals AWS of Microsoft Azure) kunnen door toezichthouders worden aangewezen als 'kritieke ICT-derdepartij' en onder direct Europees toezicht worden geplaatst. Voor een SaaS-startup is die directe aanwijzing uitgesloten, maar de financiële klant zal u wel als volwaardige leverancier behandelen.

## Verplichte Contractbepalingen (Artikel 30)

Artikel 30 van DORA somt de elementen op die een overeenkomst voor ICT-diensten verplicht moet bevatten. De juridische afdeling van uw klant zal u daarom een specifiek DORA-addendum voorleggen met de volgende bepalingen:

| Bepaling | Wat dit concreet voor u betekent |
| --- | --- |
| Duidelijke dienstbeschrijving | Een schriftelijke, ondubbelzinnige vastlegging van functionaliteiten en eventuele onderaannemers |
| Data- en verwerkingslocaties | Exacte specificatie van de landen en cloudregio's waar klantdata wordt verwerkt en opgeslagen |
| Informatiebeveiliging | Gegarandeerde maatregelen voor de beschikbaarheid, authenticiteit, integriteit en vertrouwelijkheid van data |
| Data-export en teruggave | Duidelijke afspraken over hoe de data volledig wordt teruggegeven bij beëindiging of insolventie |
| Serviceniveaus (SLA) | Meetbare kwantitatieve doelstellingen voor uptime en responstijden, inclusief wijzigingsprocedures |
| Incidentondersteuning | De contractuele verplichting om kosteloos of tegen vooraf afgesproken tarieven bijstand te verlenen bij incidenten |
| Medewerking aan toezichthouders | Volledige medewerking aan onderzoeken door financiële toezichthouders van de klant |
| Opzeggingsrechten | Gronden waarop de klant de overeenkomst per direct kan ontbinden bij ernstige tekortkomingen |
| Deelname aan trainingen | Deelname aan cybersecurity-trainingen van de klant waar dat passend en relevant is |

Indien uw software een **kritieke of belangrijke functie** van de financiële instelling ondersteunt, gelden aanvullende verzwaarde eisen: gedetailleerde SLA's met boeteclausules, verplichte melding van elke significante wijziging, periodiek geteste continuïteitsplannen, onbeperkte inspectie- en auditrechten, en een formeel getoetste exitstrategie met een overgangsperiode.

De kwalificatie of uw applicatie een kritieke functie ondersteunt, is een formele beoordeling van de klant. Software die betalingen initieert, klantverificatie (KYC/CDD) uitvoert of rapportages aan toezichthouders genereert, valt hier vrijwel altijd onder; een interne personeelsplanner meestal niet.

## Welk Technisch Bewijs Inkopers Verlangen

Achter de juridische contractteksten schuilen praktische technische inspecties. Een met behulp van AI gebouwde SaaS kan hier probleemloos in slagen, mits de engineering vooraf op orde is gebracht:

**Toegangscontrole en identiteit.** Volledige data-isolatie per klantorganisatie via Row Level Security (RLS) in de PostgreSQL-database, verplichte tweefactorauthenticatie (MFA) voor alle beheerders, ondersteuning voor Single Sign-On (SAML / SSO) voor medewerkers van de financiële instelling en gedocumenteerde rolgebaseerde rechten.

**Logging en traceerbaarheid.** Sluitende audit-logs voor alle logins, autorisatiemutaties, documentinzagen en data-exports. Deze logs moeten onveranderbaar worden opgeslagen en gedurende een afgesproken termijn bewaard blijven.

**Operationele weerbaarheid en back-ups.** Cloudhosting binnen de Europese Unie (bijv. Frankfurt of Amsterdam), automatische back-ups met point-in-time recovery, een geteste en gedocumenteerde herstelprocedure, en meetbare doelstellingen voor hersteltijd (RTO) en maximaal dataverlies (RPO).

**Incidentenbeheer.** Een vastgelegd incidentenprotocol met ernstclassificaties, interne escalatielijnen en contractueel vastgelegde notificatietermijnen die naadloos aansluiten op de DORA-meldplichten van de klant.

**Beheer van kwetsbaarheden.** Continue dependency-monitoring, snelle patchprocessen voor ontdekte beveiligingslekken en een recente penetratietest (pentest), zeker indien de applicatie een belangrijke functie ondersteunt.

**Overzicht van onderaannemers.** Een actueel register van alle toeleveranciers die een rol spelen bij de dienstverlening (hosting, e-mailservices, databaseproviders en externe AI-modellen), inclusief vestigingslanden en verwerkingslocaties.

**Exitmechanisme.** Een bewezen, werkende manier om alle records en bestanden van de klant in een gestandaardiseerd, machineleesbaar formaat te exporteren.

## Exitstrategieën: De Meest Onderschatte DORA-Eis

DORA verplicht financiële instellingen expliciet om een leverancier te kunnen verlaten zonder dat hun bedrijfsvoering stagneert of wettelijke plichten in het geding komen. Voor een SaaS-startup vertaalt dit zich naar een harde inkoopeis: de klant moet te allen tijde zijn volledige dataset kunnen terughalen en naadloos kunnen overstappen naar een alternatief.

Zorg dat u drie zaken direct kunt overhandigen:

1. **Een complete data-exportfunctie** in een gangbaar formaat (zoals JSON, CSV en geordende mappen voor pdf's), bij voorkeur direct toegankelijk voor beheerders via het instellingenmenu
2. **Een contractuele overgangsverplichting,** waarin u toezegt de dienstverlening gedurende een afgesproken opzegtermijn tegen gelijkblijvende condities voort te zetten
3. **Een schriftelijke vernietigingsbevestiging,** waarmee u verklaart dat alle resterende kopieën na succesvolle migratie definitief en veilig zijn gewist

Een startup die tijdens het inkoopgesprek live kan demonstreren hoe een beheerder met één klik een complete back-up van alle dossiers en documenten downloadt, neemt direct de grootste zorg van risk officers weg. Ons artikel over [data-export via CSV en API voor SaaS](https://launchstudio.eu/nl/blog/customer-data-export-csv-and-api-for-saas) toont hoe u dit bouwt.

## AI-Functionaliteiten en DORA

Bevat uw SaaS-oplossing functionaliteiten die worden aangedreven door AI (zoals automatische documentanalyse of samenvattingen via LLM's)? Dan stellen compliance teams gerichte aanvullende vragen. Welke modelleverancier verwerkt de financiële data? In welke regio? Wordt klantdata gebruikt voor het trainen van modellen? Wat gebeurt er als de API van OpenAI of Anthropic kampt met een storing? Worden AI-beslissingen gelogd?

Onder DORA draait dit om weerbaarheid en ketenafhankelijkheid: uw AI-provider is immers een onderaannemer in hun toeleveringsketen.

Praktische technische maatregelen omvatten: contractuele afspraken dat data niet voor modeltraining wordt benut, het gebruik van Europese API-endpoints, een betrouwbare fallback-functionaliteit wanneer de AI-dienst tijdelijk onbereikbaar is, en volledige audit-logging van door AI ondersteunde processen. Onze handleiding over [AI-feature fallbacks bij API-storingen](https://launchstudio.eu/nl/blog/ai-feature-fallbacks-when-the-model-api-is-down) behandelt de architectuurzijde hiervan.

## Hoe het Inkooptraject bij Financiële Partijen Verloopt

Kennis van het gebruikelijke proces voorkomt verrassingen en stelt u in staat uw planning realistisch in te richten. Een inkooptraject bij een bank of betaalinstelling doorloopt doorgaans vijf fases:

**1. Business case en pre-assessment.** De interne business sponsor motiveert waarom uw tool nodig is. Het team Vendor Risk Management beoordeelt of de dienst onder DORA valt en of er sprake is van een kritieke of belangrijke functie. Een heldere productbeschrijving helpt uw interne voorvechter enorm.

**2. Due diligence vragenlijst.** U ontvangt een omvangrijke vragenlijst (vaak 70 tot 100 vragen) over informatiebeveiliging, continuïteit, financiële gezondheid, onderaannemers en datalocaties. Binnen vijf werkdagen een compleet dossier inleveren wekt direct vertrouwen.

**3. Risicobeoordeling (Risk Review).** Security officers en risk managers beoordelen uw antwoorden. Eventuele vervolgvragen concentreren zich steevast op lacunes: ontbrekende logs, back-ups die nooit zijn getest of vage bepalingen over data-export.

**4. Contractonderhandeling.** Het DORA-addendum wordt parallel aan de commerciële overeenkomst uitonderhandeld. Let hierbij scherp op auditrechten, boetebepalingen en de kosten voor incidentbijstand.

**5. Onboarding en periodieke monitoring.** Na ondertekening wordt uw contract ingeschreven in het formele DORA-informatieregister van de klant. Verwacht een jaarlijkse herbeoordeling waarbij getoetst wordt of alle certificaten en back-uptests nog actueel zijn.

Startups die rekening houden met een doorlooptijd van zes tot twaalf weken en hun documentatie vooraf gereed hebben, ervaren dit proces als professioneel en voorspelbaar.

## De DORA-Voorbereidingschecklist

- Een beknopt Beveiligingsoverzicht (architectuur, EU-datacenters, RLS-autorisatie, versleuteling en logging)
- Een actueel register van onderaannemers inclusief locaties en diensten
- Een duidelijke Service Level Agreement (SLA) met concrete uptime-targets en responstijden
- Een formeel incidentenprotocol met getoetste meldtermijnen
- Een bedrijfscontinuïteitsplan met hersteldoelen (RTO/RPO) en een datum van de meest recente geslaagde hersteltest
- Een operationele data-exportfunctie en een uitgewerkte exitstrategie
- Een managementsamenvatting van een recente penetratietest (indien beschikbaar)
- Vooraf ingevulde antwoorden op standaard vendor risk-vragenlijsten
- Een juridisch getoetst contractaddendum dat voldoet aan Artikel 30 van DORA

## Wat Het Kost

LaunchStudio helpt software-oprichters om de vereiste technische fundamenten vakkundig in te richten: strikte tenant-isolatie via Row Level Security, MFA en enterprise SSO (SAML), onveranderbare audit-logging, hosting in de EU, automatische back-ups met herstelvalidatie, data-exportfuncties en incidentenprocedures. Daarnaast ondersteunen we bij het opstellen van het complete compliance-dossier dat financiële inkopers eisen. Ons **Launch Ready**-pakket (€800 - €3.500) omvat de beveiligingshardening en deployment; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) breidt dit uit met beheerde cloudhosting, redundante back-ups en prioriteitsondersteuning. Onze [prijscalculator](https://launchstudio.eu/nl/#calculator) geeft u direct een gerichte inschatting.

## Het Team Achter LaunchStudio

LaunchStudio wordt aangedreven door Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ gerealiseerde softwareprojecten en ruim 120 senior engineers. We bouwden en onderhielden systemen voor toonaangevende corporate organisaties met formele vendor assessments, waaronder Vodafone en TNO. Manifera's CEO Herre Roelevink was medeoprichter van cybersecurity-specialist CyberDevOps (thans CFLW Cyber Strategies). Oprichters ontmoeten ons team aan de Herengracht 420 in Amsterdam; onze engineeringteams werken vanuit ons softwarecentrum aan Pho Quang Street in Ho Chi Minh City, met een regionale hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De KYC-Dossiertool Die een Sluitend Exitplan Nodig Had

Priya Ramdin, voormalig compliance officer bij een betaalinstelling in Amsterdam, ontwikkelde met Lovable en Supabase de applicatie Dossiercheck: een intuïtieve SaaS-oplossing waarmee betaal- en e-geldinstellingen cliëntenonderzoek-documenten (KYC/CDD) verzamelen, geldigheidsdata bewaken en dossiers voorbereiden op toezichtaudits. Na een succesvolle pilot bij twee jonge fintechs wilde een middelgrote vergunninghoudende betaalinstelling Dossiercheck uitrollen over haar voltallige onboarding-afdeling.

Het vendor management-team van de betaalinstelling classificeerde Dossiercheck als ondersteunend aan een belangrijke functie en stuurde Priya een DORA-contractaddendum, een audit-vragenlijst van 90 punten en het verzoek om een formele exitstrategie. Priya ontdekte diverse kwetsbaarheden waar ze tijdens de ontwikkelfase niet bij had stilgestaan: er was geen geautomatiseerde mogelijkheid om de volledige documentenset van een klant te exporteren, beheeracties werden niet gelogd, de productiedatabase was nog nooit hersteld vanuit een back-up, de ingebouwde AI-samenvatter communiceerde met een Amerikaans cloud-endpoint, en er ontbrak een formeel incidentenprotocol.

LaunchStudio implementeerde strikte tenant-isolatie via PostgreSQL Row Level Security, activeerde verplichte MFA voor het serviceteam en integreerde SAML Single Sign-On voor de medewerkers van de betaalinstelling. Er werd een onveranderbaar audit-log ingericht voor alle logins, dossierinzagen en exports. Een self-service exportfunctie stelde beheerders in staat met één klik alle records en gekoppelde bestanden gestructureerd te downloaden. Point-in-time recovery werd geactiveerd inclusief een gedocumenteerde hersteltest, en de AI-koppeling verhuisde naar een Europees Azure-endpoint met een contractuele garantie dat data niet wordt gebruikt voor training. Engineers hielpen Priya met het documenteren van de RTO/RPO-doelen, een onderaannemersregister, SLA-normen en een incidentenplan met een 24-uurs meldtermijn, waarmee haar jurist het DORA-addendum direct kon finaliseren.

**Resultaat:** De betaalinstelling keurde Dossiercheck goed na slechts één ronde schriftelijke vragen, precies vijf weken na ontvangst van de initiële audit. De exportfunctie en de audit-logging, oorspronkelijk ontwikkeld voor deze ene klant, werden standaard productfeatures die twee opvolgende inkooptrajecten bij andere financiële instellingen aanzienlijk versnelden.

> *"Ik kende DORA goed vanuit mijn eerdere bancaire rol. Maar ik had me niet gerealiseerd hoeveel van die regelgeving direct op mijn bordje zou belanden als softwareleverancier totdat het eerste inkoopaddendum binnenkwam."*
> - **Priya Ramdin, Oprichter, Dossiercheck (Amsterdam)**

**Kosten & Doorlooptijd:** €6.800 (Launch & Grow-pakket: SAML SSO en MFA, audit-logging, complete data-exportfunctie, back-up- en herstelvalidatie, Europees AI-endpoint en compliance-documentatie) - afgerond in 17 werkdagen.

## Veelgestelde Vragen

### Is DORA direct van toepassing op mijn SaaS-startup?

DORA geldt formeel rechtstreeks voor financiële entiteiten in de EU, niet voor de meeste individuele SaaS-startups. Wanneer u echter software levert aan banken, verzekeraars, betaalinstellingen of beleggingsondernemingen, zijn zij wettelijk verplicht om DORA's derdepartij-risicoregels op u toe te passen. Hierdoor krijgt u direct te maken met specifieke contractclausules, diepgaande security-vragenlijsten en auditrechten.

### Wat verstaat DORA onder een 'kritieke of belangrijke functie'?

Dit is een bedrijfsproces waarvan een verstoring de financiële soliditeit, de continuïteit of de wettelijke vergunningseisen van de financiële instelling wezenlijk zou aantasten. Uw klant bepaalt formeel of uw SaaS-dienst hieronder valt. Is dat het geval, dan gelden strengere contracteisen rondom gegarandeerde serviceniveaus, geteste noodplannen, uitgebreide auditrechten en een gedetailleerde exitstrategie.

### Moet ik verplicht een penetratietest laten uitvoeren om aan banken te leveren?

De wet schrijft niet voor elke leverancier een verplichte pentest voor, maar in de praktijk vragen vrijwel alle financiële instellingen om een recente samenvatting van een onafhankelijke penetratietest. Zeker wanneer uw software belangrijke functies ondersteunt of persoonsgegevens verwerkt, is een professionele applicatie- en infrastructuurpentest een noodzakelijke investering.

### Hoe helpt Manifera's ervaring bij het voldoen aan DORA-eisen?

Manifera ontwikkelt al ruim 11 jaar complexe softwaresystemen voor grote corporate opdrachtgevers die onderworpen zijn aan strikte leveranciersaudits, en onze directie heeft een bewezen achtergrond in cybersecurity. LaunchStudio benut die ervaring om exact die technische controles en documentatie te realiseren die financiële inkopers verlangen, zonder uw startup te belasten met overbodige bureaucratie.

### Versterkt DORA-gereedheid de vindbaarheid en positie van mijn SaaS?

Zeker. Een transparante openbare pagina over informatiebeveiliging en compliance met vermelding van Europese datacenters, RLS-beveiliging, incidentprotocollen en exit-ondersteuning helpt risicomanagers uw product snel op de shortlist te plaatsen. Bovendien vormt deze gestructureerde informatie exact het type gezaghebbende content dat zoekmachines en AI-zoeksystemen citeren wanneer financiële instellingen leveranciers onderzoeken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is DORA direct van toepassing op mijn SaaS-startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "DORA geldt rechtstreeks voor financiële entiteiten in de EU. SaaS-startups worden geraakt doordat financiële klanten verplicht zijn de strenge derdepartij-regels contractueel door te leggen." }
    },
    {
      "@type": "Question",
      "name": "Wat verstaat DORA onder een 'kritieke of belangrijke functie'?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een functie waarvan uitval de continuïteit of solvabiliteit van de financiële instelling bedreigt. De klant beoordeelt dit; bij een positief oordeel gelden zwaardere contract- en auditregels." }
    },
    {
      "@type": "Question",
      "name": "Moet ik verplicht een penetratietest laten uitvoeren om aan banken te leveren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd wettelijk verplicht, maar financiële instellingen verlangen vrijwel unaniem een recente pentest-samenvatting, zeker voor applicaties die bedrijfskritische data verwerken." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera's ervaring bij het voldoen aan DORA-eisen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar enterprise-software onder strenge leveranciersaudits. LaunchStudio past die ervaring toe om direct de juiste maatregelen en documentatie op te leveren." }
    },
    {
      "@type": "Question",
      "name": "Versterkt DORA-gereedheid de vindbaarheid en positie van mijn SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een openbare security- en compliance-pagina helpt zakelijke inkopers direct en levert gestructureerde gegevens op die zoekmachines en AI-zoekmodellen tonen bij marktvergelijkingen." }
    }
  ]
}
</script>
