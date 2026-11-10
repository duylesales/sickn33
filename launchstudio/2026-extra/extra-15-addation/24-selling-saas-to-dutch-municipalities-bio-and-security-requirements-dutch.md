---
Titel: "SaaS Verkopen aan Nederlandse Gemeenten: BIO en Beveiligingseisen"
Trefwoorden: saas gemeente, bio baseline informatiebeveiliging overheid, software verkopen aan gemeenten, gibit voorwaarden, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# SaaS Verkopen aan Nederlandse Gemeenten: BIO en Beveiligingseisen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "SaaS Verkopen aan Nederlandse Gemeenten: BIO en Beveiligingseisen",
  "description": "Nederlandse gemeenten schaffen software aan onder de Baseline Informatiebeveiliging Overheid (BIO), standaard IT-inkoopvoorwaarden (GIBIT) en formele aanbestedingsregels. Deze gids legt uit wat de BIO betekent voor een SaaS-leverancier, welke documenten en beheersmaatregelen gemeenten verwachten, hoe inkoop werkt bij kleinere contracten en hoe u een met AI gebouwd product voorbereidt op een eerste gemeentelijke klant.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-11",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/selling-saas-to-dutch-municipalities-bio-and-security-requirements" },
  "citation": [
    { "@type": "CreativeWork", "name": "Baseline Informatiebeveiliging Overheid (BIO)", "url": "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/" },
    { "@type": "CreativeWork", "name": "VNG Informatiebeveiligingsdienst (IBD)", "url": "https://www.informatiebeveiligingsdienst.nl/" },
    { "@type": "CreativeWork", "name": "VNG: GIBIT inkoopvoorwaarden", "url": "https://vng.nl/artikelen/gibit" },
    { "@type": "CreativeWork", "name": "PIANOo: Expertisecentrum Aanbesteden", "url": "https://www.pianoo.nl/nl" }
  ]
}
</script>

Gemeenten vormen een bijzonder aantrekkelijke markt voor software-oprichters. Nederland telt meer dan driehonderd gemeenten die vergelijkbare wettelijke taken uitvoeren, onder constante druk staan om processen te digitaliseren en intensief met elkaar communiceren. Een applicatie die uitstekend functioneert voor één gemeente - of het nu gaat om vergunningen, het sociaal domein, meldingen openbare ruimte (MOR), vrijwilligerscoördinatie of interne werkstromen - verspreidt zich dikwijls snel naar omliggende buurgemeenten.

Tegelijkertijd zijn gemeenten veeleisende opdrachtgevers. Gemeenten verwerken privacygevoelige persoonsgegevens van burgers, variërend van inkomensgegevens tot gezondheid en gezinssituaties, en moeten verantwoording afleggen aan gemeenteraden, accountants en de toezichthouder. Hun informatiebeveiliging wordt gestuurd door een landelijke standaard, de Baseline Informatiebeveiliging Overheid (BIO), en hun inkoop volgt vaste kaders zoals de GIBIT en de Aanbestedingswet. Een oprichter die aanklopt met een prototype gebouwd in Lovable of Bolt zonder sluitende antwoorden op securityvragen, strandt vrijwel altijd na het eerste kennismakingsgesprek.

Deze gids legt uit wat Nederlandse gemeenten verwachten van SaaS-leveranciers en hoe u uw product hierop voorbereidt. Dit is algemene informatie, geen formeel juridisch of aanbestedingsadvies.

## Belangrijkste Punten

- **De BIO is het normenkader voor informatiebeveiliging binnen de gehele Nederlandse overheid,** inclusief gemeenten, gebaseerd op ISO 27001 en ISO 27002. Gemeenten leggen deze normen contractueel op aan hun IT-leveranciers.
- **Standaard IT-inkoopvoorwaarden, zoals de GIBIT,** worden breed gehanteerd en bevatten bindende bepalingen over beveiliging, privacy, bedrijfscontinuïteit, escrow en exitregelingen.
- **Gemeenten leggen jaarlijks verantwoording af via ENSIA,** waardoor CISO's en privacy-officers formele bewijsstukken verlangen (certificaten, assurance-rapporten en audits).
- **Aanbestedingsregels zijn afhankelijk van de contractwaarde.** Kleinere opdrachten en pilots onder de drempelwaarden kunnen via enkelvoudige of meervoudige onderhandse procedures worden gegund.
- **Het technische fundament is bepalend:** hosting binnen de EU, Single Sign-On (SSO) voor ambtenaren, strikte scheiding van data, auditlogging, geteste back-ups en een deugdelijke verwerkersovereenkomst.

## Wat de BIO Inhoudt

De Baseline Informatiebeveiliging Overheid (BIO) is het gezamenlijke normenkader voor informatiebeveiliging voor alle overheidslagen: Rijk, provincies, waterschappen en gemeenten. De BIO rust op de fundamenten van ISO/IEC 27001 en ISO/IEC 27002, aangevuld met specifieke overheidsmaatregelen. Met de actualisaties richting de vernieuwde ISO-standaarden en de Europese NIS2-richtlijn wordt het kader continu aangescherpt.

De BIO werkt risicogestuurd via Basisbeveiligingsniveaus (BBN1, BBN2 en BBN3). Gemeenten beoordelen hun informatiesystemen en wijzen een beveiligingsniveau toe. Voor u als SaaS-leverancier is de kernboodschap helder: de gemeente blijft wettelijk eindverantwoordelijk voor de veiligheid van haar data, ook wanneer deze in uw cloudapplicatie draait. Een gemeente moet daarom aantonen dat uw SaaS aan de vereiste beheersmaatregelen voldoet.

De Informatiebeveiligingsdienst (IBD) van de Vereniging van Nederlandse Gemeenten (VNG) ondersteunt gemeenten met richtlijnen, modelvragenlijsten en handreikingen voor leveranciersmanagement. Veel gemeenten hanteren IBD-templates bij leveranciersaudits.

## Verantwoording via ENSIA

Gemeenten rapporteren jaarlijks over hun informatiebeveiliging via ENSIA (Eenduidige Normatiek Single Information Audit). Dit verantwoordingssysteem toetst de naleving van de BIO en specifieke stelsels zoals DigiD en de basisregistraties. Door deze jaarlijkse auditcyclus kunnen CISO's geen genoegen nemen met mondelinge toezeggingen. Zij hebben concrete bewijsstukken nodig die standhouden bij de externe accountant: ISO 27001-certificaten, pentest-rapportages en ingevulde beveiligingsverklaringen.

Voor een startende SaaS betekent dit dat beveiligingsvragen geen formaliteit zijn; uw antwoorden belanden rechtstreeks in het gemeentelijke auditdossier.

## De Gemeentelijke Inkoopvoorwaarden: GIBIT

Veel gemeenten hanteren de Gemeentelijke Inkoopvoorwaarden bij IT (GIBIT) als standaardcontract voor de aanschaf van software en clouddiensten. De GIBIT stelt scherpe eisen aan onderwerpen die bij standaard SaaS-contracten vaak onderbelicht blijven:

- Naleving van BIO-beveiligingsnormen en actieve medewerking aan security-audits
- Verwerking van persoonsgegevens conform een vaste gemeentelijke verwerkersovereenkomst
- Strikte geheimhouding en geheimhoudingsverklaringen voor personeel
- Continuïteitsgaranties en eventuele escrow-regelingen voor broncode en data
- Exit-regeling: de verplichting om bij beëindiging van het contract alle gegevens kosteloos, tijdig en in een open, herbruikbaar formaat over te dragen aan de gemeente of een opvolgende leverancier
- Intellectueel eigendom, open source-licenties en aansprakelijkheidsbepalingen

Bestudeer de actuele GIBIT-voorwaarden vóór uw eerste verkoopgesprek. Met name de exitregeling vereist dat uw applicatie over een geautomatiseerde en gedocumenteerde data-exportfunctie beschikt.

## Aanbestedingsregels: Hoe Startups een Eerste Voet Tussen de Deur Krijgen

Overheidsopdrachten in Nederland vallen onder de Aanbestedingswet en het inkoopbeleid van de desbetreffende gemeente. Welke inkoopprocedure van toepassing is, hangt af van de geraamde contractwaarde over de totale looptijd:

- **Boven de Europese drempelwaarde:** een formele Europese openbare aanbesteding is wettelijk verplicht, met uitgebreide selectie- en gunningscriteria.
- **Onder de Europese drempelwaarde:** de gemeente volgt haar eigen inkoopbeleid. Binnen bepaalde financiële grenzen maakt dit een meervoudig onderhandse procedure (offertes opvragen bij 3 tot 5 partijen) of zelfs een enkelvoudig onderhandse gunning (één-op-één contract voor een pilot) mogelijk.

PIANOo, het expertisecentrum voor aanbesteden, publiceert de actuele drempelbedragen en handreikingen. Voor startups is dit van cruciaal belang: een proefproject, innovatiepilot of kleinschalige implementatie kan vaak onderhands worden gegund. Zodra de SaaS zich in de praktijk heeft bewezen, beschikt u over een waardevolle overheidsreferentie voor toekomstige aanbestedingen.

## Wat Gemeenten Aan U Gaan Vragen

Houd rekening met een security- en privacy-assessment op de volgende onderdelen:

| Onderwerp | Typische vraag | Wat een overtuigend antwoord inhoudt |
| --- | --- | --- |
| Hosting | Waar staat de data en wie verwerkt het? | Hosting binnen de EU/EER, gedefinieerde cloudregio's en gecertificeerde datacenters |
| Certificering | Beschikt u over ISO 27001 of vergelijkbaar? | Een certificaat, of een gedocumenteerd BIO-beveiligingsoverzicht met concrete implementatie |
| Authenticatie | Hoe loggen ambtenaren in? | SAML 2.0 / OpenID Connect SSO met de identity provider van de gemeente, inclusief MFA |
| Autorisatie | Wie kan welke gegevens inzien? | Role-Based Access Control per afdeling en rol, strikt afgedwongen in de database |
| Logging | Worden gebruikersacties gelogd? | Auditlogs voor logins, mutaties en exports; exporteerbaar voor de gemeente |
| Kwetsbaarheden | Hoe test u op gaten en updates? | Geautomatiseerde dependency-scans, patchbeleid en periodieke pentests |
| Incidenten | Wat is uw datalekkenprocedure? | Schriftelijk protocol met melding binnen de overeengekomen uren (conform AVG 72-uurseis) |
| Continuïteit | Wat gebeurt er als uw startup stopt? | Geteste back-ups, data-exit in open standaarden, eventueel broncode-escrow |
| Privacy | Tekent u onze verwerkersovereenkomst? | Ja, aansluitend op gemeentelijke standaardtemplates met actuele subverwerkerslijst |
| Burgers | Loggen inwoners in en op welke wijze? | Passende authenticatie; DigiD indien het om officiële overheidstaken gaat |

Indien burgers via uw portaal inloggen voor officiële overheidszaken of gevoelige beschikkingen, kan aansluiting op DigiD vereist zijn. DigiD brengt eigen strenge normen en jaarlijkse audits met zich mee. Verhelder deze eis direct bij aanvang van het traject.

## Het Technische Fundament voor een AI-Gebouwde Applicatie

Applicaties die zijn gebouwd met behulp van AI-assistenten moeten op een aantal cruciale technische punten worden verstevigd voordat ze aan gemeenten kunnen worden geleverd:

- **Enterprise Single Sign-On (SSO):** ondersteuning voor SAML 2.0 of OpenID Connect (Azure AD / Entra ID, ADFS), zodat ambtenaren inloggen via het gemeentenetwerk en accounts centraal worden ingetrokken bij uitdiensttreding.
- **Multi-Factor Authenticatie (MFA):** verplicht voor alle beheerderstoegang en ondersteunend personeel.
- **Tenant-isolatie via Row Level Security (RLS):** strikte scheiding van gegevens tussen verschillende gemeenten en tussen afdelingen binnen één gemeente.
- **Auditlogging:** onwijzigbare logging van wie welk dossier heeft ingezien, bewerkt of geëxporteerd.
- **Europese hosting:** hosting bij betrouwbare cloudleveranciers binnen de EER met sluitende contracten.
- **Afgeschermde bestandsopslag:** foto's en documenten opgeslagen in private buckets met tijdelijke signed URL's; automatische verwijdering van privacygevoelige EXIF-locatiemetadata bij uploads van burgers.
- **Geverifieerde back-ups:** periodiek geteste herstelprocedures met meetbare RTO- en RPO-doelen.
- **Beheer van kwetsbaarheden:** continue monitoring op kwetsbaarheden in open source dependencies.
- **Strikte bronscheiding:** nooit echte burger- of gemeentedata gebruiken in test- of stagingomgevingen.
- **Complete data-export:** een exportfunctionaliteit (CSV/JSON/SQL) om bij contractbeëindiging alle data compleet te kunnen overdragen.

## Documentatie Die Klaar Moet Liggen

Het gemeentelijke inkoopproces verloopt aanmerkelijk soepeler wanneer u direct de juiste documenten kunt overleggen:

1. Beveiligingsverklaring (Security Overview) gemapt op de BIO- en ISO 27002-normen
2. Concept-verwerkersovereenkomst en complete subverwerkerslijst met datalocaties
3. Ingevulde gemeentelijke leveranciersvragenlijst (vaak op basis van IBD-standaarden)
4. Incidenten- en datalekkenprotocol met escalatielijnen en reactietermijnen
5. Continuïteits- en exitplan, inclusief de specificatie van exportformaten
6. Samenvatting van de meest recente penetratietest (management summary)
7. Toegankelijkheidsverklaring (WCAG 2.1 niveau AA voor publieksgerichte interfaces)
8. Service Level Agreement (SLA) met duidelijke beschikbaarheidsgaranties en reactietijden

Overheidswebsites en -applicaties moeten wettelijk voldoen aan de digitale toegankelijkheidseisen van WCAG 2.1 AA. Indien burgers meldingen via uw app doen, is toegankelijkheid een keiharde inkoopeis. Onze handleiding over [WCAG-toegankelijkheidsaanpassingen voor AI-apps](https://launchstudio.eu/nl/blog/wcag-accessibility-fixes-for-ai-built-apps) behandelt de technische uitvoering hiervan.

## Wie U Ontmoet Binnen de Gemeente

Een inkooptraject bij een gemeente brengt meerdere functionarissen aan tafel, elk met een eigen invalshoek:

- **De proceseigenaar / vakambtenaar:** de afdelingsmanager die het operationele probleem ervaart en enthousiast is over uw oplossing.
- **De CISO of ISO (Information Security Officer):** toetst uw applicatie streng aan de BIO en beoordeelt uw beveiligingsarchitectuur.
- **De Functionaris Gegevensbescherming (FG) of privacy-officer:** beoordeelt de verwerkersovereenkomst, datastromen en eventuele DPIA-noodzaak.
- **De inkoopadviseur:** bewaakt de Aanbestedingswet, hanteert de GIBIT-voorwaarden en onderhandelt over contractvorm en tarieven.
- **Functioneel en technisch applicatiebeheer:** verzorgt de koppeling met SSO, autorisaties en eventuele systeemintegraties.

Door elk van deze rollen direct van de juiste, gerichte documentatie te voorzien, voorkomt u maandenlange vertraging in het inkoopproces.

## Veelgemaakte Fouten

**Uitsluitend focussen op functionaliteiten in plaats van zekerheid.** Gemeentelijke inkopers hebben eerst sluitende antwoorden nodig op beveiliging en privacy vóórdat ze de functionaliteit intern mogen bespreken.

**De exit- en datareparatiebepalingen negeren.** Het contractueel kunnen garanderen dat alle data bij contracteinde netjes en bruikbaar wordt overgedragen is een standaardvereiste onder de GIBIT.

**Echte burgerdata gebruiken tijdens pilots en tests.** Een export van een pilotgemeente importeren in een ontwikkelomgeving levert een direct datalek en compliance-overtreding op.

**Aannemen dat goedkeuring bij één gemeente overal geldt.** Elke gemeente beslist autonoom, al vormen positieve referenties van buurgemeenten de allersterkste aanbeveling.

**De doorlooptijd onderschatten.** Zelfs bij kleine onderhandse opdrachten nemen besluitvormings- en controleprocessen vaak enkele maanden in beslag.

## Wat Het Kost

LaunchStudio brengt door AI gebouwde SaaS-applicaties op het beveiligingsniveau dat Nederlandse gemeenten eisen: SAML SSO, strikte tenant-isolatie via Row Level Security, auditlogging, veilige Europese hosting, afgeschermde opslag, geteste back-up- en herstelprocedures, complete data-exportmogelijkheden en veilige testdata. Tevens ondersteunen wij bij het opstellen van de BIO-beveiligingsverklaring en vragenlijsten.

Het **Launch Ready**-pakket (€800 - €3.500) omvat security hardening, configuratie en deployment; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, geautomatiseerde back-ups, 24/7 monitoring en SLA-ondersteuning toe - onmisbaar voor overheidstoepassingen. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte offerte.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring, 160+ opgeleverde projecten en 120+ engineers met ruime ervaring in het bouwen van complexe systemen onder formele overheidsnormen (zoals voor TNO). CEO Herre Roelevink was medeoprichter van het cybersecuritybedrijf dat tegenwoordig opereert als CFLW Cyber Strategies. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Meldingen-App Voor de Buitenruimte Die Geen Exitplan Had

Martijn Koster, voormalig gemeenteambtenaar, bouwde Buitenmelder met Bolt en Supabase: een platform waarop inwoners problemen in de openbare ruimte melden (kapotte straatverlichting, zwerfafval, losliggende stoeptegels), waarna gemeentelijke buitendiensten het herstel inplannen en afhandelen. Een gemeente in Noord-Holland reageerde na een succesvolle demonstratie enthousiast en wilde overgaan tot een contract - onder voorbehoud van een audit door haar ISO en toepassing van de GIBIT-inkoopvoorwaarden.

De security review bracht fundamentele knelpunten aan het licht. Ambtenaren logden in met losse gebruikersnamen en wachtwoorden zonder MFA, terwijl de gemeente verplichtte tot SSO via haar eigen Microsoft Entra ID. Alle gemeentelijke teams konden alle meldingen inzien, inclusief namen, adressen en foto's van melders. De foto's stonden in een publieke cloud-bucket en bevatten nog alle GPS-locatiedata. Er waren geen auditlogs, de database draaide in een Amerikaanse AWS-regio, er ontbrak een deugdelijke verwerkersovereenkomst en de applicatie bood geen enkele voorziening voor een geautomatiseerde data-exit bij contractbeëindiging.

LaunchStudio implementeerde SAML SSO voor gemeentemedewerkers met MFA via de centrale identity provider van de gemeente, en richtte Row Level Security in die de data van verschillende gemeenten hermetisch scheidde en persoonsgegevens van burgers afschermde voor niet-betrokken teams. Foto's werden ondergebracht in private storage met tijdelijke signed links en automatische verwijdering van privacygevoelige EXIF-data. Er werd een onveranderbaar auditlog gerealiseerd voor alle logins, inzages en mutaties. De applicatie verhuisde naar Europese datacenters met geteste back-up- en herstelprocedures. Tevens werd een volledige data-exportfunctie in open standaarden (JSON/CSV) opgeleverd voor de vereiste exitregeling. Tot slot leverden engineers de technische onderbouwing voor een BIO-beveiligingsoverzicht, waarna een privacyjurist de verwerkersovereenkomst finaliseerde.

**Resultaat:** De gemeente keurde Buitenmelder bij de herbeoordeling volledig goed en ondertekende een tweejarig contract onder de GIBIT-voorwaarden inclusief de exitregeling. Binnen twaalf maanden namen twee buurgemeenten de software eveneens in gebruik, waarbij vrijwel het gehele auditdossier kon worden hergebruikt.

> *"Ik kende de gemeentelijke wereld van binnenuit, dus ik wist dat ze voorzichtig waren. Ik had me alleen niet gerealiseerd hoeveel van die zorgvuldigheid direct zichtbaar moest zijn in de architectuur van mijn product."*
> - **Martijn Koster, Oprichter, Buitenmelder (Alkmaar)**

**Kosten & Doorlooptijd:** €6.900 (Launch & Grow-pakket: SAML SSO, tenant-isolatie via RLS, private bestandsopslag, auditlogging, EU-hosting, complete data-exportfunctie en documentatieondersteuning voor de BIO) - afgerond in 18 werkdagen.

## Veelgestelde Vragen

### Heb ik verplicht een ISO 27001-certificaat nodig om aan een Nederlandse gemeente te verkopen?

Niet in alle gevallen. Gemeenten moeten zelf voldoen aan de BIO en hun leveranciers hierop toetsen. Sommige gemeenten eisen een ISO 27001-certificaat voor grote aanbestedingen of gevoelige gegevens. Voor pilots en opdrachten onder de aanbestedingsdrempel volstaat doorgaans een gedocumenteerd BIO-beveiligingsoverzicht, een sluitend vragenformulier en een aantoonbaar veilig technisch fundament.

### Kan een startend SaaS-bedrijf een gemeentelijke opdracht krijgen zonder Europese aanbesteding?

Ja, voor opdrachten onder de Europese aanbestedingsdrempels. Gemeenten volgen daaronder hun eigen gemeentelijk inkoopbeleid, wat ruimte biedt voor enkelvoudige gunningen bij pilots of meervoudig onderhandse trajecten met enkele uitgenodigde partijen. Grotere contracten vergen een formele aanbesteding, waarbij eerdere gemeentelijke referenties zwaar meetellen.

### Wat houden de GIBIT-voorwaarden precies in?

De GIBIT (Gemeentelijke Inkoopvoorwaarden bij IT) is de standaardset contractvoorwaarden die door het merendeel van de Nederlandse gemeenten wordt gehanteerd. Deze voorwaarden regelen informatiebeveiliging, privacy, continuïteit, geheimhouding, aansprakelijkheid en exitverplichtingen (zoals de verplichte teruggave van alle data in open standaarden bij beëindiging).

### Hoe helpt de ervaring van Manifera bij het verkopen aan overheden?

Manifera ontwikkelt al ruim 11 jaar bedrijfskritische software onder formele beveiligingskaders (onder meer voor gerenommeerde organisaties zoals TNO). LaunchStudio past die ervaring toe om Enterprise SSO, dataseparatie, auditlogging en exit-functionaliteiten in te bouwen zoals gemeentelijke CISO's dat verwachten.

### Helpt naleving van overheidseisen bij de adoptie door andere gemeenten?

Absoluut. Gemeenten werken nauw samen en wisselen ervaringen en leveranciersbeoordelingen intensief uit. Een duidelijke openbare pagina over uw BIO-naleving, hosting en WCAG-toegankelijkheid zorgt ervoor dat inkoopadviseurs en AI-zoekmachines uw oplossing sneller identificeren als betrouwbare overheidssoftware.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik verplicht een ISO 27001-certificaat nodig om aan een Nederlandse gemeente te verkopen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd. Voor pilots en kleinere opdrachten onder de drempelwaarde volstaat vaak een gedocumenteerd BIO-overzicht en een aantoonbaar veilige technische basis." }
    },
    {
      "@type": "Question",
      "name": "Kan een startend SaaS-bedrijf een gemeentelijke opdracht krijgen zonder Europese aanbesteding?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, voor opdrachten onder de Europese drempels hanteren gemeenten hun eigen inkoopbeleid, met mogelijkheden voor onderhandse gunningen en pilots." }
    },
    {
      "@type": "Question",
      "name": "Wat houden de GIBIT-voorwaarden precies in?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standaard gemeentelijke IT-inkoopvoorwaarden die informatiebeveiliging, privacy, continuïteit, geheimhouding, aansprakelijkheid en data-exit regelen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het verkopen aan overheden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar software onder strikte security-normen. LaunchStudio implementeert SSO, RLS-isolatie, logging en data-exit zoals gemeentelijke CISO's verlangen." }
    },
    {
      "@type": "Question",
      "name": "Helpt naleving van overheidseisen bij de adoptie door andere gemeenten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Gemeenten delen referenties intensief. Een publieke verantwoording over BIO en WCAG helpt inkoopteams en AI-zoeksystemen u direct te vinden." }
    }
  ]
}
</script>
