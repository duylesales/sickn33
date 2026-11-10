---
Titel: "DPIA voor een AI-Functionaliteit: Wanneer Is Deze Verplicht?"
Trefwoorden: dpia ai feature, data protection impact assessment saas, dpia avg ai, gdpr article 35 ai, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# DPIA voor een AI-Functionaliteit: Wanneer Is Deze Verplicht?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DPIA voor een AI-Functionaliteit: Wanneer Is Deze Verplicht?",
  "description": "Het toevoegen van een AI-functionaliteit aan een SaaS-product kan de wettelijke AVG-verplichting voor een gegevensbeschermingseffectbeoordeling (DPIA) activeren. Deze gids legt uit wanneer een DPIA verplicht is, welke criteria toezichthouders hanteren, wie verantwoordelijk is wanneer u als verwerker optreedt, wat een DPIA inhoudt, typische risico's van AI-functies en de technische beheersmaatregelen die deze risico's mitigeren.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-13",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/dpia-for-an-ai-feature-when-you-need-one" },
  "citation": [
    { "@type": "CreativeWork", "name": "AVG Artikel 35: Gegevensbeschermingseffectbeoordeling", "url": "https://gdpr-info.eu/art-35-gdpr/" },
    { "@type": "CreativeWork", "name": "Artikel 29-Werkgroep Richtlijnen inzake DPIA (WP248 rev.01)", "url": "https://ec.europa.eu/newsroom/article29/items/611236" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: DPIA", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/privacy-en-persoonsgegevens/data-protection-impact-assessment-dpia" },
    { "@type": "CreativeWork", "name": "EDPB Advies 28/2024 over AI-modellen", "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en" }
  ]
}
</script>

AI-functionaliteiten zijn momenteel de meest gevraagde uitbreiding in vrijwel elk softwaresegment. Klanten vragen om automatische samenvattingen van lange rapporten, concepten voor e-mails, categorisering van inkomende verzoeken, voorspellende suggesties op basis van historische trends en interactieve chatbots over hun eigen bedrijfsdocumenten. Dankzij moderne AI-API's kan een oprichter een dergelijke functionaliteit binnen één middag integreren in een met Lovable of Cursor gebouwde applicatie.

Wat veel langer duurt, is het beantwoorden van de onvermijdelijke vraag tijdens zakelijke inkooptrajecten: "Is er voor deze AI-functie al een DPIA uitgevoerd?" Een Data Protection Impact Assessment (in het Nederlands een gegevensbeschermingseffectbeoordeling) is het instrument onder de AVG om vooraf gestructureerd na te denken over de risico's van een gegevensverwerking. Veel AI-toepassingen voldoen aan de criteria die een DPIA wettelijk verplicht stellen, met name wanneer ze gevoelige gegevens verwerken, menselijke prestaties beoordelen of op grote schaal worden ingezet. En zelfs als uw zakelijke klant juridisch de eindverantwoordelijkheid draagt voor de DPIA, kan deze het onderzoek alleen afronden met gedetailleerde technische input van u als leverancier.

Deze gids legt uit wanneer een DPIA nodig is voor een AI-functie en hoe u zich hierop voorbereidt. Dit is algemene informatie, geen juridisch advies.

## Belangrijkste Punten

- **Een DPIA is wettelijk verplicht wanneer een verwerking waarschijnlijk een hoog risico oplevert** voor de rechten en vrijheden van betrokkenen, conform AVG Artikel 35.
- **Europese toezichthouders hanteren negen risicocriteria,** waaronder evaluatie of scoring, gevoelige gegevens, kwetsbare personen, grootschaligheid en innovatieve technologie. Voldoet een toepassing aan twee of meer criteria, dan is een DPIA in de regel verplicht. AI-functies voldoen al snel aan meerdere criteria tegelijk.
- **De verwerkingsverantwoordelijke is verantwoordelijk voor de uitvoering.** Treedt u op als verwerker voor zakelijke klanten, dan voeren zij de DPIA uit, maar moet u een kant-en-klaar technisch inputpakket aanleveren.
- **Een DPIA beschrijft de verwerking, toetst de noodzaak en evenredigheid, identificeert risico's en definieert maatregelen,** en moet worden afgerond vóórdat de verwerking daadwerkelijk van start gaat.
- **Technische keuzes bepalen het resultaat:** dataminimalisatie in prompts, verwerking binnen de EU, uitsluiting van modeltraining, menselijke controle vóór publicatie en autorisatieafhandeling in de database.

## Wat een DPIA Precies Is

Artikel 35 van de AVG verplicht een verwerkingsverantwoordelijke om vóór de start van een verwerking een effectbeoordeling uit te voeren indien de verwerking, met name bij gebruik van nieuwe technologieën, waarschijnlijk een hoog risico inhoudt. Het onderzoek moet minimaal de volgende onderdelen omvatten:

1. Een systematische beschrijving van de beoogde verwerkingen en de verwerkingsdoeleinden
2. Een beoordeling van de noodzaak en de evenredigheid (proportionaliteit) van de verwerkingen met betrekking tot de doeleinden
3. Een beoordeling van de risico's voor de rechten en vrijheden van de betrokkenen
4. De beoogde maatregelen om de risico's aan te pakken, waaronder waarborgen, veiligheidsmaatregelen en mechanismen om de bescherming van persoonsgegevens te waarborgen

Indien uit de DPIA blijkt dat de voorgenomen verwerking een hoog risico oplevert dat de verantwoordelijke niet met redelijke maatregelen kan mitigeren, is de organisatie verplicht om vooraf advies in te winnen bij de toezichthouder (voorafgaande raadpleging onder Artikel 36). In Nederland is dat de Autoriteit Persoonsgegevens.

## Wanneer Is een DPIA Verplicht?

Artikel 35 noemt drie situaties waarin een DPIA altijd verplicht is: stelselmatige en uitgebreide evaluatie van persoonlijke aspecten op basis van geautomatiseerde verwerking (inclusief profilering) met rechtsgevolgen; grootschalige verwerking van bijzondere categorieën van gegevens of strafrechtelijke gegevens; en stelselmatige en grootschalige monitoring van openbaar toegankelijke ruimten.

Daarnaast hebben de Europese privacytoezichthouders (de Artikel 29-Werkgroep, overgenomen door de EDPB) negen specifieke criteria vastgesteld om te beoordelen of er sprake is van een waarschijnlijk hoog risico:

| Criterium | Voorbeeld in een AI-functionaliteit |
| --- | --- |
| Evaluatie of scoring | Rangschikken van sollicitanten, voorspellen van klantverloop per persoon, beoordelen van werknemers |
| Geautomatiseerde besluitvorming met wezenlijk effect | Automatisch afwijzen van leningaanvragen of dynamische prijsbepaling per individu |
| Stelselmatige monitoring | Analyseren van interne communicatie of werkplekactiviteit met taalmodellen |
| Gevoelige of zeer persoonlijke data | Medische dossiers, financiële draagkracht, gegevens van minderjarigen |
| Grootschalige verwerking | Tienduizenden gebruikers, landelijke dekking, grote datavolumes |
| Koppelen of combineren van datasets | CRM-data samenvoegen met externe registers om AI-profielen te verrijken |
| Kwetsbare betrokkenen | Werknemers ten opzichte van werkgever, patiënten, kinderen, burgers in schuldsanering |
| Innovatieve technologie | Geavanceerde inzet van generatieve AI en LLM's waarvan de effecten nog niet volledig vaststaan |
| Uitsluiting van rechten of diensten | AI-screening die de toegang tot een platform of uitkering blokkeert |

Als vuistregel geldt: voldoet een functionaliteit aan **twee of meer van deze criteria**, dan is een DPIA verplicht. AI-toepassingen scoren vrijwel altijd op "innovatieve technologie", gecombineerd met gevoelige data, evaluatie of kwetsbare doelgroepen.

De Autoriteit Persoonsgegevens publiceert bovendien een officiële lijst van verwerkingen waarvoor in Nederland altijd een DPIA moet worden verricht. Raadpleeg deze lijst altijd voor sectorspecifieke verplichtingen.

## Wie Is Verantwoordelijk: Klant of Leverancier?

In de meeste B2B SaaS-relaties treedt uw zakelijke klant op als verwerkingsverantwoordelijke voor de data die zij in uw software uploaden, en bent u hun verwerker. Dit houdt in:

- **Uw klant moet de DPIA formeel uitvoeren** voor het gebruik van uw AI-functie binnen hun organisatie.
- **U bent wettelijk verplicht om hen te ondersteunen** (conform AVG Artikel 28 lid 3 sub f) door alle benodigde technische specificaties, datastromen en beveiligingswaarborgen aan te leveren.
- **Indien u data voor eigen doelen inzet** - bijvoorbeeld het trainen van uw eigen AI-modellen op basis van klantdata - wordt u zélf verwerkingsverantwoordelijke en bent u zelfstandig verplicht tot een DPIA en een geldige rechtsgrondslag.

In de praktijk verwachten zakelijke klanten en inkopers een kant-en-klaar "DPIA-inputpakket" voor elke AI-functionaliteit. Door dit document proactief te verstrekken, bespaart u weken vertraging in het inkooptraject.

## Typische Privacyrisico's van AI-Functies

Tijdens een DPIA richten privacyfunctionarissen zich steevast op de volgende risico's:

**Gegevensdoorgifte aan derden:** prompts met persoonsgegevens worden verstuurd naar een externe AI-provider (zoals OpenAI of Anthropic). Waar staan de servers? Wordt de invoer opgeslagen? Wordt klantdata gebruikt voor modeltraining?

**Onnauwkeurige output en hallucinaties:** AI-modellen kunnen onjuiste of verzonnen informatie genereren. Als een hallucinatie belandt in een formeel patiëntendossier, een kredietbeoordeling of een personeelsdossier, kan dit directe schade berokkenen aan de betrokkene.

**Vooringenomenheid en discriminatie:** taalmodellen reflecteren vooroordelen uit hun trainingsdata. Dit is riskant bij functies die mensen rangschikken of selecteren.

**Buitensporige datatoegang (privilege leakage):** een AI-zoekassistent met ongefilterde toegang tot de volledige bedrijfsdatabase kan vertrouwelijke informatie tonen aan medewerkers die daartoe niet bevoegd zijn, indien de autorisatiestructuur niet op databaseniveau is afgedwongen.

**Prompt injection:** kwaadaardige instructies verborgen in externe bestanden of e-mails kunnen het AI-model manipuleren om vertrouwelijke data te lekken of ongeautoriseerde acties uit te voeren.

**Gebrek aan transparantie:** betrokkenen weten vaak niet dát er AI wordt gebruikt, noch op welke criteria de uitkomsten zijn gebaseerd.

**Buitensporige bewaartermijnen:** prompts en AI-antwoorden die voor onbepaalde tijd in serverlogs blijven staan.

## Technische Maatregelen Die het Risico Drastisch Verlagen

Oprichters kunnen deze risico's effectief beheersen door gerichte architectuurkeuzes te maken vóórdat de code in productie gaat:

| Risico | Technische oplossing |
| --- | --- |
| Gegevens naar derden | Europese API-endpoints, zakelijke verwerkersovereenkomst, contractuele uitsluiting van modeltraining, anonimisering van prompts |
| Onnauwkeurige output | Verplichte menselijke controle (human-in-the-loop) vóór definitieve opslag, duidelijke AI-markering, eenvoudige correctiemogelijkheid |
| Vooringenomenheid | Geen volautomatische besluitvorming over personen; prestaties testen over diverse groepen en beperkingen documenteren |
| Buitensporige datatoegang | Retrieval-Augmented Generation (RAG) waarbij contextfiltering strikt via Row Level Security (RLS) in de database wordt afgedwongen |
| Prompt injection | Invoer van gebruikers strikt scheiden van systeeminstructies, tool-permissies inperken en verdachte interacties loggen |
| Transparantie | Duidelijke melding in de interface dat een tekst door AI is gegenereerd, inclusief toelichting in de privacyverklaring |
| Dataretentie | Korte bewaartermijnen voor prompts (maximaal 30 dagen), automatische data-scrubbing in debug- en crashlogs |

Onze handleidingen over [het kiezen van een LLM-API voor een EU-SaaS](https://launchstudio.eu/nl/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral) en [AI-fallbacks bij API-uitval](https://launchstudio.eu/nl/blog/ai-feature-fallbacks-when-the-model-api-is-down) belichten deze keuzes in technisch detail.

## Het DPIA-Inputpakket voor Zakelijke Klanten

Als SaaS-verwerker stelt u voor elke AI-functionaliteit een beknopt document op met de volgende gegevens:

1. **Beschrijving van de functionaliteit:** wat de AI doet, welke gebruikers er toegang toe hebben en welke gegevens worden verwerkt
2. **Datastromen:** welke velden worden meegestuurd in de prompt, welke serverlocatie deze verwerkt en wat de output is
3. **Subverwerkers:** de exacte AI-leverancier en hostingpartijen, inclusief contractuele voorwaarden
4. **Trainingsclausule:** expliciete schriftelijke bevestiging dat invoer- en uitvoerdata niet wordt gebruikt voor modeltraining
5. **Autorisatiemodel:** hoe het systeem waarborgt dat de AI uitsluitend data raadpleegt waar de actieve gebruiker kijkrechten voor heeft
6. **Menselijk toezicht:** hoe professionals de gegenereerde teksten controleren en bewerken vóór gebruik
7. **Beveiligingsmaatregelen:** encryptie in rust en transport, mitigatie van prompt injections, auditlogging
8. **Bewaartermijnen:** maximale retentie van prompts, embeddings en tijdelijke caches
9. **Uitschakeloptie:** de mogelijkheid voor de klant om de AI-functionaliteit organisatiebreed of per rol uit te schakelen
10. **Bekende beperkingen:** foutmarges, ondersteunde talen en randgevallen

Met dit document kan de Functionaris Gegevensbescherming van uw klant de DPIA binnen enkele uren afronden.

## De Europese AI Act Naast de AVG

De Europese AI-verordening (AI Act) stelt aanvullende eisen aan bepaalde toepassingen. Systemen die als hoog-risico worden geclassificeerd - zoals AI gebruikt bij werving en selectie, toegang tot onderwijs, essentiële publieke diensten of medische hulpmiddelen - brengen zware verplichtingen met zich mee voor zowel leveranciers als gebruikers, waaronder een grondrechteneffectbeoordeling (FRIA). Reguliere ondersteunende SaaS-functies, zoals het samenvatten van documenten of het formuleren van conceptbrieven voor professionals, vallen doorgaans buiten de hoog-risicocategorie van de AI Act. Een DPIA en een AI Act-analyse kunnen waar nodig integraal worden gecombineerd.

## Wanneer Voert U de Beoordeling Uit?

Een DPIA moet wettelijk worden uitgevoerd vóórdat de gegevensverwerking start:

- **Tijdens de ontwerpfase van de functionaliteit,** wanneer keuzes over model, datastromen en interface nog flexibel zijn
- **Vóór aanvang van een proefproject met echte klantdata,** niet pas achteraf
- **Bij wezenlijke wijzigingen in de functionaliteit,** zoals een switch van API-provider, uitbreiding met nieuwe datatypes of het toekennen van autonome actiebevoegdheden aan de AI

Tijdig handelen bespaart aanzienlijk veel geld: het toevoegen van waarborgen in de ontwerpfase is eenvoudig, terwijl het achteraf verbouwen van een actieve architectuur na bezwaren van een toezichthouder complex en kostbaar is.

## Hoe LaunchStudio Helpt

LaunchStudio ontwerpt en bouwt AI-functionaliteiten met de exacte waarborgen die toezichthouders en DPIA-beoordelaars verlangen: Europese API-koppelingen zonder modeltraining, minimale prompts, geautoriseerde RAG-architecturen via Row Level Security in de database, verplichte human-in-the-loop interfaces, bescherming tegen prompt injection en strikte bewaartermijnen in logging. Tevens stellen onze engineers het complete technische DPIA-inputpakket voor uw zakelijke klanten op.

Het **Launch Ready**-pakket (€800 - €3.500) omvat security reviews en het verstevigen van een bestaande AI-functie; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, 24/7 monitoring en SLA-ondersteuning toe voor applicaties met meerdere AI-componenten. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte raming.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring, 160+ succesvolle projecten en 120+ software-engineers. De cybersecurity-achtergrond van CEO Herre Roelevink waarborgt dat datastromen en autorisatiestructuren in AI-systemen voldoen aan de hoogste veiligheidsnormen. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Schuldhulp-Assistent Die Ieder Cliëntdossier Kon Inzien

Fatima Ouali, voormalig schuldhulpverlener in Zaandam, bouwde Schuldwijzer met Cursor en Supabase: een casemanagementtool voor gemeentelijke en particuliere schuldhulpverleners, waarin hulpverleners schuldenoverzichten, schuldeisers, betalingsregelingen en documenten bijhouden. Ze voegde een slimme AI-assistent toe die vragen van hulpverleners over complexe dossiers beantwoordde en direct conceptbrieven naar schuldeisers genereerde. Een grote gemeentelijke kredietbank wilde met Schuldwijzer starten - onder voorwaarde van een goedgekeurde DPIA door haar privacyfunctionaris.

De initiële beoordeling bracht direct grote privacybezwaren aan het licht. Cliënten in de schuldsanering zijn kwetsbare personen, de dossiers bevatten gevoelige inkomensgegevens, gezondheidsinformatie die van invloed was op de afloscapaciteit en gezinssituaties, en de inzet van generatieve AI vormde een innovatieve technologie - waarmee direct aan meerdere hoogrisicocriteria werd voldaan. Technisch bleek de assistent bovendien documenten uit de gehele organisatie op te halen in plaats van uitsluitend de eigen caseload van de consulent, werden prompts verstuurd naar een Amerikaans endpoint zonder zakelijke verwerkersovereenkomst, bleven volledige dossiers in serverlogs bewaard en konden door AI opgestelde brieven zonder verplichte tussencontrole direct worden verzonden.

LaunchStudio herstructureerde de retrieval-pijplijn zodat de AI uitsluitend documenten kon raadplegen waartoe de specifieke hulpverlener strikt bevoegd was, afgedwongen via Row Level Security op de databasequeries. De AI-provider werd omgezet naar een Europees endpoint onder een formele verwerkersovereenkomst zonder modeltraining, prompts werden ontdaan van niet-noodzakelijke identificatoren (zoals BSN en exacte geboortedata) en de logging werd gelimiteerd tot geanonimiseerde metadata met een bewaartermijn van 30 dagen. Het verzenden van brieven werd voorzien van een verplichte beoordelings- en bewerkingsstap door de consulent inclusief een duidelijke AI-markering, en geüploade documenten van derden werden strikt als passieve tekstdata behandeld om prompt injection uit te sluiten. Tot slot stelden engineers een gedetailleerd DPIA-inputpakket op, waarmee de gemeentelijke privacy-officer het onderzoek succesvol kon afronden.

**Resultaat:** De gemeentelijke DPIA concludeerde dat alle restrisico's met de doorgevoerde technische maatregelen acceptabel waren, waarna Schuldwijzer officieel werd uitgerold naar 25 consulenten. Zij besparen gemiddeld een uur per dag op het opstellen van brieven, zonder dat er ooit een brief ongecontroleerd de deur uitgaat.

> *"Mijn cliënten bevinden zich vaak in de meest stressvolle periode van hun leven. De AI moest hen ontlasten, zonder ooit lichtzinnig om te springen met hun meest persoonlijke gegevens."*
> - **Fatima Ouali, Oprichter, Schuldwijzer (Zaandam)**

**Kosten & Doorlooptijd:** €4.400 (Launch & Grow-pakket: geautoriseerde retrieval via RLS, Europese AI-provider, prompt-minimalisatie, review-workflow, logbeveiliging en oplevering van het DPIA-inputpakket) - afgerond in 12 werkdagen.

## Veelgestelde Vragen

### Heeft elke AI-functionaliteit verplicht een DPIA nodig?

Nee. Een DPIA is uitsluitend vereist wanneer de verwerking waarschijnlijk een hoog risico oplevert voor betrokkenen. Een AI-functie die uitsluitend algemene marketingteksten genereert zonder persoonsgegevens vereist geen DPIA. Toepassingen die persoonsgegevens verwerken, mensen evalueren, kwetsbare groepen betreffen of gevoelige data analyseren, voldoen doorgaans aan twee of meer criteria en zijn daardoor vrijwel altijd DPIA-plichtig.

### Wie voert de DPIA uit: mijn SaaS-bedrijf of mijn klant?

De verwerkingsverantwoordelijke. In de meeste B2B SaaS-situaties is uw klant de verantwoordelijke voor de data die zij in uw software verwerken en moeten zij de DPIA uitvoeren. Als SaaS-leverancier en verwerker bent u echter wettelijk verplicht om hen te voorzien van de benodigde technische documentatie. Gebruikt u klantdata voor eigen doeleinden (zoals modeltraining), dan bent u zélf verantwoordelijk en moet u zelfstandig een DPIA uitvoeren.

### Wat gebeurt er als een DPIA een hoog restrisico aantoont?

De verantwoordelijke moet aanvullende technische of organisatorische maatregelen nemen om het risico te verlagen. Indien er na alle mitigerende maatregelen nog steeds een hoog restrisico overblijft, mag de verwerking niet starten zonder voorafgaande raadpleging van de Autoriteit Persoonsgegevens. Een doordachte technische architectuur voorkomt dit scenario door risico's al tijdens de bouw te elimineren.

### Hoe helpt de ervaring van Manifera bij AI-functionaliteiten en DPIA's?

Manifera ontwikkelt al ruim 11 jaar software conform strenge Europese privacy- en beveiligingsstandaarden. LaunchStudio benut die kennis om AI-functies zo in te richten dat datastromen, autorisaties via Row Level Security en menselijk toezicht direct voldoen aan de strenge eisen van een DPIA, in plaats van achteraf noodgrepen te moeten toepassen.

### Draagt een privacybewuste AI-architectuur bij aan de marktpositie van een product?

Jazeker. Zakelijke inkopers en overheidsinstanties zoeken nadrukkelijk naar AI-oplossingen die voldoen aan de AVG en binnen de EU worden gehost. Een transparant DPIA-inputpakket neemt direct zorgen weg bij security- en privacy-officers, versnelt het inkoopproces en vormt een sterk betrouwbaarheidssignaal dat door zoekmachines en AI-zoeksystemen prominent wordt opgepikt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heeft elke AI-functionaliteit verplicht een DPIA nodig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, alleen bij een waarschijnlijk hoog risico. AI die gevoelige gegevens verwerkt, mensen evalueert of kwetsbare groepen betreft vereist vrijwel altijd een DPIA." }
    },
    {
      "@type": "Question",
      "name": "Wie voert de DPIA uit: mijn SaaS-bedrijf of mijn klant?",
      "acceptedAnswer": { "@type": "Answer", "text": "De verwerkingsverantwoordelijke (in B2B SaaS meestal de klant), waarbij de SaaS-leverancier als verwerker de technische informatie en waarborgen aanlevert." }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een DPIA een hoog restrisico aantoont?",
      "acceptedAnswer": { "@type": "Answer", "text": "De verantwoordelijke moet extra maatregelen nemen; blijft het restrisico hoog, dan is voorafgaande raadpleging van de toezichthouder verplicht vóór de start." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij AI-functionaliteiten en DPIA's?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar systemen onder Europese privacyregels. LaunchStudio ontwerpt AI met dataseparatie en toezicht die een DPIA direct doorstaan." }
    },
    {
      "@type": "Question",
      "name": "Draagt een privacybewuste AI-architectuur bij aan de marktpositie van een product?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Een helder DPIA-inputpakket neemt zorgen weg bij zakelijke inkopers, versnelt de verkoopcyclus en versterkt het vertrouwen bij zoek- en AI-engines." }
    }
  ]
}
</script>
