---
Titel: De opkomst van Vertical AI Agents in AI-software engineering
Trefwoorden: AI SaaS Platform, AI Software Engineering, AI And Software Development, AI Software Developers, Build AI App, AI Development, SaaS AI, AI In SaaS
Koperfase: Bewustzijn
---

# De opkomst van Vertical AI Agents in AI-software engineering
Als u een 'AI-tool voor marketeers' bouwt, bent u al te laat. De markt voor brede, algemene AI (Horizontale AI) is veroverd door OpenAI, Google en Anthropic. De toekomst voor solo-oprichters en startups ligt in **Verticale AI**: hyperspecifieke agenten die zijn opgeleid om enkelvoudige, complexe workflows uit te voeren voor zeer specifieke industrieën. Dit is de reden waarom een nichemarkt in 2026 de enige manier is om te winnen, en dit is wat er daadwerkelijk voor nodig is om er een te bouwen die het contact met een echte industrie overleeft.

## Horizontale versus verticale AI

**Horizontale AI** (ChatGPT, Gemini, Claude rechtstreeks gebruikt) is de ultieme generalist. Het kan slagen voor het bar-examen, Python-code schrijven en een maaltijdplan genereren. Maar omdat het van alles een beetje weet, beschikt het niet over de diepe, gelokaliseerde context om zeer specifieke professionele taken perfect uit te voeren. Vraag het om een commercieel huurcontract samen te vatten, en het mist de jurisdictie-specifieke verlengingsclausule waar uw lokale markt altijd over onderhandelt. Vraag het om een verzekeringsclaim te beoordelen, en het kent de interne fraudescore-heuristiek van uw verzekeraar niet. Het is niet dom, het is simpelweg ongedifferentieerd. De context is gevuld met het hele internet, niet met twintig jaar aan stamkennis van uw branche.

**Verticale AI** is de ultieme specialist. Het negeert 99% van wat het AI-model kan doen en richt zich volledig op 1%. Het is een AI-agent die maar één ding weet, maar het beter doet dan welk mens dan ook. Dit is waarom categorieleiders zoals Harvey (contractbeoordeling voor advocatenkantoren), Abridge (klinische documentatie voor artsen) en Rilla (spraakcoaching voor verkopers in de installatiebranche en thuisverbetering) premium zakelijke contracten binnenhalen in plaats van abonnementen van € 20 per maand. Geen van hen heeft een "beter" taalmodel dan GPT-5 of Gemini 3; ze hebben simpelweg een fundamenteel model verpakt in de workflow, terminologie en bedrijfseigen gegevens van één branche, en de saaie taken feilloos uitgevoerd.

## De prijskracht van de niche

De prijs is direct gecorreleerd met de diepte van het opgeloste probleem.

- **Horizontaal voorbeeld**: een AI-tool die "u helpt betere e-mails te schrijven." Iedereen kan het gebruiken. Prijs: $ 9,99/maand. Hoge churn.

- **Verticaal voorbeeld**: een AI-agent voor *expediteurs* die automatisch ongestructureerde e-mailoffertes van rederijen leest, deze opmaakt in een standaard JSON-array en de centrale logistieke database bijwerkt. Dit bespaart een transportbedrijf 20 uur aan handmatige gegevensinvoer per week. Prijs: $ 499/maand. Geen verloop.

- **Tweede verticaal voorbeeld**: een AI-agent voor *algemene aannemers* die architectonische PDF-bouwtekeningen inleest, een geautomatiseerde materiaalopname uitvoert (het tellen van stijlen, het berekenen van het vierkante meterage van gipsplaten, het schatten van de lengte in meters aan leidingwerk), en een kostenraming oplevert. Een junior calculator doet er twee volle dagen over om dit handmatig te doen. De agent doet het in vier minuten. Een bouwbedrijf dat op 30 projecten per maand biedt, betaalt zonder aarzelen € 1.200/maand, want het alternatief is een salaris van € 65.000 per jaar.

Let op het patroon: u bepaalt de prijs niet op basis van 'hoeveel kost AI om te draaien'. U bepaalt de prijs op basis van de volledig belaste kosten van de menselijke arbeid, software of gederfde inkomsten die de agent vervangt. Dit is waardegebaseerde prijsstelling, en het is de reden waarom verticale AI-bedrijven doorgaans 20 tot 50 keer meer vragen dan een horizontale SaaS-tool voor dezelfde onderliggende model-API-aanroepen. Workflow-lock-in doodt ook churn: zodra uw agent rechtstreeks schrijft in het PMS, ERP of boekhoudsysteem van een bedrijf, betekent het verwijderen ervan het omscholen van personeel en het opnieuw in kaart brengen van integraties — overstapkosten die horizontale tools nooit verdienen.

## Hoe u een verticale AI-agent bouwt

Om een succesvolle verticale agent op te bouwen, moet u over domeinexpertise beschikken. Als u nog nooit in commercieel vastgoed hebt gewerkt, kunt u er geen AI-tool voor bouwen, omdat u niet weet waar de frictie zit.

1. **Identificeer de wrijving**: Vind de meest vervelende, repetitieve, data-intensieve taak in uw specifieke branche. De beste methode is geen enquête, maar drie uur naast een vakspecialist gaan zitten en elke handmatige stap timen die deze zet. De taak die hen doet zuchten, is uw product.

2. **Verzamel de bedrijfseigen gegevens**: het AI-model kent de nuances van het specifieke jargon of historische precedenten van uw branche niet. U moet deze gegevens verzamelen (vaak opgesloten in PDF's, faxen of oudere databases) en vectoriseren met een embedding-model (OpenAI's `text-embedding-3-large` of open-source alternatieven zoals BGE), opgeslagen in een vectorgeschikte database zoals Supabase pgvector of Pinecone.

3. **Implementeer RAG**: gebruik Retrieval-Augmented Generation om ervoor te zorgen dat de AI altijd naar uw specifieke branchegegevens verwijst voordat deze antwoordt of inhoud genereert. In productie is een naïeve vectorzoekopdracht alleen niet voldoende: serieuze verticale agenten combineren dichte vectorzoekopdrachten met trefwoordzoekopdrachten (BM25) in een hybride retrievalpijplijn, en sturen resultaten vervolgens door een herrangschikkingsmodel (Cohere Rerank of vergelijkbaar) voordat ze ooit het contextvenster van het LLM bereiken. Het overslaan van deze stap is de meest voorkomende reden waarom demo's van verticale AI er magisch uitzien, maar productieagenten hallucineren voor de ogen van betalende klanten.

4. **Bouw de specifieke gebruikersinterface**: geef de gebruiker geen lege chatbox. Geef ze een zeer gestructureerd dashboard dat precies is afgestemd op hun workflow, met beoordelingswachtrijen, betrouwbaarheidsscores en goedkeurings-/afwijzingsacties met één klik in plaats van vrije-tekstconversatie.

5. **Richt het in voor vertrouwen**: gereguleerde sectoren (gezondheidszorg, financiën, recht, verzekeringen) nemen geen agent in gebruik die ze niet kunnen controleren. Elke actie die de agent onderneemt — elk record dat wordt gelezen, elk veld dat wordt gewijzigd — heeft een onveranderlijk auditlogboek, op rollen gebaseerde toegangscontrole en, in veel gevallen, een menselijke goedkeuringspoort nodig voordat er iets een productiesysteem raakt. Dit is ook waar oprichters zich branden: AI-codeerassistenten zoals Bolt, Lovable en Cursor zijn buitengewoon goed in het genereren van de RAG-pijplijn en het dashboard in een weekend, maar uit brancheonderzoek blijkt dat ongeveer 45% van de door AI gegenereerde code wordt uitgeleverd met minstens één te misbruiken beveiligingslek — een niet-geverifieerd eindpunt, een ontbrekend rijniveaubeveiligingsbeleid, een API-sleutel die hardcoded in de frontend-bundel staat. Bij een verticale agent die patiëntendossiers of financiële transactiegegevens verwerkt, is dat geen bug, maar een datalek in wording.

## Van prototype naar productie: waar verticale agenten daadwerkelijk falen

Het bouwen van de RAG-pijplijn is het leuke gedeelte. Het daadwerkelijk en veilig bij echte gebruikers krijgen ervan is waar de meeste verticale AI-startups vastlopen: branchecijfers suggereren dat ongeveer 80% van de door AI gegenereerde projecten nooit een productieomgeving bereikt waarin de doelklant daadwerkelijk kan inloggen. De kloof zit vrijwel nooit in het model. Het zit in de onopvallende productielaag: versleutelde databaseverbindingen, tenant-isolatie zodat Kliniek A nooit de patiëntgegevens van Kliniek B kan zien, webhook-infrastructuur die uw vectordatabase 's nachts afstemt op een verouderd PMS of ERP, en logging op SOC 2-niveau waarmee het beveiligingsteam van een zakelijke koper ja kan zeggen.

Dit is precies de kloof die Manifera al meer dan een decennium dicht. Manifera is opgericht in 2014 en heeft meer dan 160 productiesoftwareprojecten opgeleverd voor zakelijke klanten waaronder Vodafone, TNO (Nederlandse Organisatie voor Toegepast Natuurwetenschappelijk Onderzoek) en CFLW Cyber Strategies, en opereert vanuit het hoofdkantoor in Amsterdam, Nederland, aan de Herengracht 420, naast ontwikkelingscentra in Singapore en Ho Chi Minh City, Vietnam. Zoals Herre Roelevink, oprichter en Managing Director van Manifera, het verwoordt: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om deze producten tot volwassenheid te brengen. We hebben elf jaar ervaring in precies dat." Voor een verticale AI-agent betekent 'volwassenheid' specifiek: de versleutelde webhooks, de RAG-vangrails en het auditspoor die van een overtuigend prototype software maken waar een compliance officer daadwerkelijk zijn handtekening onder zet.

## Het "Big Tech"-schild

Oprichters zijn vaak bang dat Google of OpenAI hen 'verpletteren'. Dit is waar als u horizontale gereedschappen bouwt. Maar Google is een miljardenbedrijf. Ze hebben markten nodig ter waarde van honderden miljarden dollars om de naald te laten bewegen. Ze zullen nooit technische middelen inzetten om een AI-agent te bouwen die specifiek bedoeld is voor *onafhankelijke optometristen die verzekeringsclaims beheren*. De Total Addressable Market (TAM) is voor hen te klein, maar voor een solo-oprichter is het een goudmijn van $ 10 miljoen per jaar.

Het eerlijke tegenargument: big tech brengt af en toe wel 'verticale' functies uit — Microsoft heeft bijvoorbeeld gezondheidszorgspecifieke copilots gebundeld in zijn zakelijke suite. Maar let op het patroon: dit zijn platformfuncties die worden vastgeschroefd aan een bestaande zakelijke relatie, geen diep geïntegreerde, workflow-native agenten gebouwd door mensen die in de kliniek hebben gezeten. Uw slotgracht was nooit 'wij hebben een model dat Microsoft niet heeft'. Uw slotgracht is de bedrijfseigen data, de workflow-integraties en het domeinvertrouwen dat geen enkel platformteam dat voor een kwartaaldoelstelling in een niche neerstrijkt, kan repliceren.

## Belangrijkste inzichten

- Horizontale AI (tools voor algemene doeleinden) wordt gedomineerd door technologiegiganten; startups kunnen daar niet concurreren.

- Verticale AI-agenten lossen hyperspecifieke, diepgaande problemen voor afzonderlijke sectoren op, waardoor oprichters premium B2B-prijzen kunnen vragen — vaak 20 tot 50 keer meer dan wat een horizontale tool vraagt voor vergelijkbare onderliggende rekenkracht.

- Het bouwen van verticale AI vereist diepgaande domeinexpertise en bedrijfseigen gegevens die via hybride RAG (vector- en trefwoordzoekopdrachten met herrangschikking) in het model worden geïnjecteerd, niet alleen naïeve vectorzoekopdrachten.

- Gereguleerde sectoren vereisen auditlogboeken, rolgebaseerde toegang en menselijke goedkeuring; het overslaan hiervan is de reden waarom veel door AI gebouwde prototypes nooit productie bereiken.

- Door u op hyperspecifieke niches te richten, voorkomt u dat uw startup wordt verpletterd door grote technologiebedrijven die enorme schaalgrootte nodig hebben om technische investeringen te rechtvaardigen.

- Hoe saaier en nicher de sector (bijvoorbeeld vrachtvervoer, tandartsverzekeringen, bouwcalculatie), hoe winstgevender de AI-toepassing.

## Bouw uw verticale slotgracht

Heeft u de domeinexpertise, maar heeft u de infrastructuur nodig? LaunchStudio zet de complexe vectordatabases en beveiligde RAG-architectuur op die nodig zijn om een krachtige Vertical AI Agent te bouwen — bekijk het volledige aanbod aan pakketten op [launchstudio.eu/en/#packages](https://launchstudio.eu/en/#packages).

LaunchStudio wordt beheerd door **Manifera** ([manifera.com](https://www.manifera.com/about-us/)), een internationaal software-engineeringbedrijf dat in 2014 is opgericht en wordt geleid door oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP, voor ongeveer 20% van de kosten van een traditioneel ontwikkelbureau. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: tandartspraktijkautomatisering

Hazel, de oprichter van een startup, gebruikte **Bolt** om een prototype van een tandartspraktijkautomatisering te bouwen. Hoewel de applicatie functioneel was, moest deze patiëntmanagementsystemen (PMS) integreren met een AI-planningsagent, maar het ontbrak aan webhook-afhandeling — elke planningswijziging vanuit het PMS moest handmatig opnieuw worden ingevoerd voordat de AI-agent ernaar kon handelen.

Hazel werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team bouwde veilige, gecodeerde B2B-webhook-eindpunten om PMS-schemawijzigingen te ontvangen en de AI-engine in realtime te synchroniseren, voegde rijniveau-tenantisolatie toe zodat de patiëntgegevens van elke tandartspraktijk volledig gescheiden bleven, en bouwde retry-logica en auditlogging in zodat elke geautomatiseerde planningsbeslissing traceerbaar was.

**Resultaat:** Hazel automatiseerde de planning voor 8 tandheelkundige klinieken, waardoor receptiemedewerkers werden vrijgemaakt voor ander werk.

**Kosten en tijdlijn:** € 4.800 (verticaal integratiepakket) — klaar voor productie en geïmplementeerd binnen 14 werkdagen.

---
## Veelgestelde vragen

### Wat is een horizontale AI?

Tools zoals ChatGPT die zijn ontworpen om alles voor iedereen te doen. Ze zijn breed, maar missen de diepgaande, genuanceerde expertise die nodig is voor zeer gespecialiseerde professionele taken.

### Wat is een verticale AI-agent?

Een AI die is ontworpen om één hyperspecifiek ding te doen voor één hyperspecifieke sector (bijvoorbeeld het lezen van commerciële vastgoedleases). Het maakt gebruik van fundamentele modellen, maar is beperkt tot een enkelvoudig domein, doorgaans via retrieval-augmented generation over bedrijfseigen branchegegevens.

### Waarom zijn verticale AI-agenten winstgevender?

Omdat ze diepgaande, dure bedrijfsproblemen oplossen. In plaats van € 10/maand in rekening te brengen voor een generieke schrijftool, kunt u € 500/maand vragen voor een tool die complexe gegevensinvoer in de sector automatiseert, geprijsd op basis van de arbeidskosten die het vervangt in plaats van de API-kosten om het te draaien.

### Gaan de grote technologiebedrijven geen verticale AI bouwen?

Zelden, en zelden goed. Grote technologiebedrijven hebben enorme schaalgrootte nodig. Ze zullen geen middelen besteden aan het bouwen van een tool specifiek voor een beperkte niche, en wanneer ze wel verticale functies toevoegen, ontbreekt het hen aan de workflow-integratie en het domeinvertrouwen die een oprichter die in de sector heeft geleefd, kan opbouwen. Deze winstgevende micromarkten behoren overwegend toe aan agile startups.

### Waar past LaunchStudio in het bouwen van een Vertical AI Agent?

U brengt de domeinexpertise, de bedrijfseigen gegevens en de wrijving die u wilt automatiseren. LaunchStudio (beheerd door Manifera) brengt de productie-engineering: het verharden van uw RAG-pijplijn, het beveiligen van de vectordatabase, het bouwen van versleutelde webhookintegraties met legacy-branchesoftware, en het toevoegen van de auditsporen en toegangscontroles waarmee een compliance officer de agent goedkeurt voor echte klanten — doorgaans binnen 1 tot 3 weken.
