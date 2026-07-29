---
Titel: "De dood van Thin Wrappers: overleven in de AI-softwareontwikkeling shakeout"
Trefwoorden: AI Software Engineering, AI And Software Development, AI Native, AI Deployment, AI Database, Build AI App, AI App Dev
Koperfase: Bewustzijn
---

# De dood van Thin Wrappers: overleven in de AI-softwareontwikkeling shakeout
In 2023 kon je een website bouwen die om het cv van een gebruiker vroeg, dit naar de OpenAI API stuurde met de prompt 'Maak dit beter', en een MRR van € 10.000 genereren. Dat tijdperk is voorbij. De "Thin Wrapper" is dood en wordt systematisch met uitsterven bedreigd doordat OpenAI en Anthropic voortdurend hun eigen consumenteninterfaces upgraden — elke grote modelrelease brengt functies met zich mee die zes maanden eerder nog iemands hele startup vormden. Om in 2026 te overleven, moet u een 'Thick Wrapper' bouwen. Hieronder leest u wat dat betekent en hoe u er stap voor stap, gracht voor gracht, een kunt bouwen.

## De existentiële dreiging: native upgrades

Sam Altman heeft de oprichters expliciet gewaarschuwd: "Bouw geen producten die slechts een functie van ChatGPT zijn."

Beschouw het kerkhof van dunne wrappers:

- **PDF-lezers**: dood. ChatGPT en Claude lezen native PDF's, afbeeldingen en tegenwoordig zelfs volledige multi-bestand-uploads.

- **Promptbibliotheken**: dood. Aangepaste GPT's en Claude Projects hebben deze vervangen door een gratis, ingebouwd equivalent.

- **Basiscopywriters**: stervende. Gebruikers zijn nu bekwaam genoeg om hun eigen aanwijzingen in de native gebruikersinterface te schrijven, en zowel ChatGPT als Claude bieden ingebouwde 'toon'- en 'stijl'-presets die vroeger de hele pitch van een wrapper vormden.

- **Eenvoudige codeerassistenten**: stervende. Wat vroeger een dedicated wrapper rond de API vereiste, is nu een native functie binnen de eigen IDE's en CLI's van de modelleveranciers.

Als uw hele waardevoorstel luidt: 'Ik zorg ervoor dat de gebruiker geen prompt hoeft te typen', heeft uw bedrijf een levensverwachting van ongeveer zes maanden — de duur van één releasecyclus van een model. Het patroon is consistent: welke dunne laag gemak uw product ook toevoegt, uiteindelijk besluit een frontier-lab dat dit in het basisproduct thuishoort, en levert het van de ene op de andere dag gratis aan honderden miljoenen gebruikers.

## Het tegengif: de 'dikke wrapper'

Een Thick Wrapper stuurt niet alleen tekst door naar een API. Het bevindt zich op het kruispunt van AI-generatie, bedrijfseigen gegevens en complexe zakelijke workflows. U bouwt een gracht door dingen te doen die de fundamentele modellen structureel niet kunnen — niet omdat ze niet slim genoeg zijn, maar omdat ze geen toestemming, context of reden hebben om dit specifiek voor u te doen.

## Moat 1: Workflow-integratie (ketenvorming)

ChatGPT bevindt zich in een browsertabblad. Uw app moet leven waar het werk daadwerkelijk gebeurt. Een dikke wrapper koppelt meerdere API's aan elkaar om menselijke stappen te verwijderen — dit wordt vaak een 'agentic workflow' genoemd, waarbij de AI-aanroep slechts één knooppunt is in een grotere, deterministische pijplijn.

**Voorbeeld (The Thin Way):** Een gebruiker kopieert een boze klant-e-mail, plakt deze in uw app, genereert een beleefd antwoord, kopieert het antwoord en plakt het terug in Zendesk.

**Voorbeeld (The Thick Way):** Uw app integreert rechtstreeks met Zendesk via de REST API en webhook-abonnementen. Wanneer er een boze e-mail binnenkomt, haalt uw server deze automatisch op, doorzoekt uw privédatabase naar de terugbetalingsgeschiedenis van de klant, stuurt beide naar OpenAI om een hyperspecifiek antwoord te genereren, en slaat het concept rechtstreeks in Zendesk op zodat de agent het kan goedkeuren. De hele keten — ophalen, doorzoeken, genereren, terugschrijven — verloopt in minder dan twee seconden zonder dat een mens ook maar één keer hoeft te kopiëren of plakken.

OpenAI kan dit niet van nature doen omdat ze geen directe toegang hebben tot de Zendesk API-sleutels of de interne database van de gebruiker, en ze hebben geen productmatige prikkel om een op maat gemaakte Zendesk-integratie te bouwen voor uw specifieke klantenbestand. Die toegang en die prikkel vormen uw gracht.

## Moat 2: Eigendomsgegevens via RAG

De modellen weten alles op het publieke internet, maar ze weten niets over de specifieke business van uw klant. Deze kloof overbrugt u met Retrieval-Augmented Generation (RAG): documenten omzetten in vector-embeddings, deze opslaan in een doorzoekbare index, en alleen de meest relevante fragmenten ophalen om het model te voeden op het moment van de zoekopdracht — in plaats van te hopen dat het model iets 'onthoudt' waar het nooit op is getraind.

Als u een AI-tool voor bedrijfsjuristen bouwt, vraagt u de AI niet alleen naar algemeen contractenrecht. U bouwt een veilige Supabase-vectordatabase (met de `pgvector`-extensie) waarin het advocatenkantoor de 10.000 succesvolle contracten uit het verleden uploadt. Elk document wordt opgesplitst in fragmenten van ongeveer 500-1.000 tokens, ge-embed (doorgaans via de `text-embedding-3`-modellen van OpenAI met 1.536 dimensies), en geïndexeerd. Wanneer de AI een nieuw contract genereert, haalt het de exacte clausules op waar het bedrijf specifiek de voorkeur aan geeft, vaak gecombineerd met traditioneel trefwoordzoeken (BM25) in een 'hybride zoek'-opstelling, zodat het systeem geen exacte termovereenkomsten mist die pure vectorgelijkenis kan vervagen. Uw app wordt een institutioneel brein — een ondoordringbare gracht: een concurrent met toegang tot hetzelfde GPT-5-klasse model kan nog steeds geen vraag beantwoorden over clausules die hij nog nooit heeft gezien.

Deze gracht brengt een reële beveiligingslast met zich mee die oprichters stelselmatig onderschatten: ongeveer 45% van de door AI gegenereerde code bevat minstens één exploiteerbare beveiligingskwetsbaarheid, en RAG-systemen zijn een veelvoorkomend doelwit, aangezien een vectordatabase met de vertrouwelijke contracten van een advocatenkantoor nu een van de gevoeligste assets in uw hele stack is. Row-level security, tenant-isolatie (zodat de embeddings van Kantoor A nooit kunnen lekken in de zoekresultaten van Kantoor B) en versleutelde opslag in rust zijn hier geen optionele extra's — het is het verschil tussen een verdedigbare gracht en een meldingsbrief over een datalek.

## Moat 3: Enterprise Team-functies

ChatGPT is een spel voor één speler. B2B-software is een multiplayerspel. U creëert een dikke wrapper door de samenwerkingsfuncties te bouwen waar bedrijven om vragen — en dit zijn opvallend genoeg precies de functies die een door AI gegenereerd prototype van Lovable, Bolt of v0 vrijwel nooit standaard bevat, omdat ze echte backend-architectuur vereisen, niet slechts een gebruikersinterface:

- **Role-Based Access Control (RBAC)**: Junior-werknemers kunnen concepten genereren, maar alleen Senioren kunnen deze goedkeuren en verzenden — afgedwongen aan de serverzijde, niet slechts verborgen in de gebruikersinterface.

- **Auditlogboeken**: de CISO kan precies zien wie wat heeft gegenereerd, en wanneer, met een onveranderlijk record dat geschikt is voor compliance-beoordeling.

- **Gedeelde werkruimten**: teams kunnen in realtime samenwerken aan de output van de AI, met echte conflictoplossing in plaats van 'laatste wijziging wint'.

- **SSO en SAML**: inkoopteams van bedrijven wijzen routinematig leveranciers af die niet kunnen integreren met hun identity provider (Okta, Azure AD), ongeacht hoe goed de AI-uitvoer is.

Deze functies komen zelden voor in een weekendprototype, en het zijn precies de functies die het verschil maken tussen een speeltje en een begrotingspost die een onderneming daadwerkelijk door inkoop laat gaan.

## De infrastructuurverschuiving

Het bouwen van een dikke wrapper vereist dat u verder gaat dan een eenvoudige React-frontend. U heeft nu een robuuste backend, vectordatabases, API-webhookbeheer, op rollen gebaseerde authenticatie en strenge beveiligingsprotocollen nodig — niets hiervan wordt standaard door een AI-paginabouwer gegenereerd, aangezien tools als Lovable, Bolt en v0 zijn geoptimaliseerd voor frontend-snelheid, niet voor backend-architectuur. Dit is waar solo-oprichters vaak tegen een muur botsen: het is precies de reden waarom ongeveer 80% van de door AI gebouwde projecten nooit een echte productiestatus bereikt. De frontend ziet er af, de backend is nooit echt begonnen.

## Belangrijkste inzichten

- Dunne wrappers (eenvoudige promptinterfaces) worden vernietigd door native updates voor ChatGPT en Claude, op een cyclus van ongeveer zes maanden.

- Om te overleven moeten oprichters 'Thick Wrappers' bouwen die diep integreren in de specifieke zakelijke workflow van een gebruiker via agentic, meerstaps pijplijnen.

- Door meerdere API's aan elkaar te koppelen (bijvoorbeeld Zendesk, interne databases, OpenAI) ontstaan workflows die fundamentele modellen niet kunnen repliceren, omdat ze de toegang en de prikkel missen.

- Het gebruik van RAG (Retrieval-Augmented Generation) om de AI te baseren op de privé-, bedrijfseigen gegevens van een bedrijf creëert een niet-kopieerbare gracht — maar ook een serieus beveiligingsrisico, aangezien 45% van de door AI gegenereerde code exploiteerbare kwetsbaarheden bevat.

- Door 'multiplayer'-functies voor ondernemingen toe te voegen, zoals op rollen gebaseerde toegangscontrole, SSO en auditlogboeken, verandert uw app van speelgoed in een B2B-noodzaak die door inkoop daadwerkelijk wordt goedgekeurd.

## Overgang van dun naar dik

Klaar om een verdedigbare gracht te bouwen? LaunchStudio implementeert complexe vectordatabases voor RAG, hybride zoekfuncties en beveiligingsfuncties op bedrijfsniveau (RBAC, auditlogboeken, SSO) om van uw prototype een Thick Wrapper te maken — zonder de frontend aan te raken die u en uw AI-tool al hebben gebouwd.

"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten volwassen te maken. Wij hebben elf jaar ervaring in precies dat," aldus Herre Roelevink, oprichter en Managing Director van Manifera.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf, opgericht in **2014** en geleid door oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420, 1017 BZ) en ontwikkelingscentra in **Singapore** (100 Tras Street #16-01) en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. Kijk voor meer informatie op [onze homepage](https://launchstudio.eu/en/) of [ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact). Voor diepere zakelijke engineeringbehoeften die verder gaan dan één MVP, zie de diensten voor [maatwerksoftwareontwikkeling](https://www.manifera.com/services/custom-software-development/) van Manifera.

## Echt voorbeeld

### Een AI-native oprichter in actie: zoekhulpmiddel voor juridische documenten

Dominic, de oprichter van een startup, gebruikte **Cursor** om een prototype van een zoekhulpmiddel voor juridische documenten te bouwen. Hoewel de applicatie functioneel was, had deze een slechte zoekrelevantie omdat de app alleen trefwoordmatching gebruikte in plaats van vectorgelijkenismatching — een advocaat die zocht op 'ontslag om dringende reden' zou een contract mislopen dat de term 'beëindiging op grond van wangedrag' gebruikte, omdat de twee zinnen vrijwel geen trefwoorden gemeen hebben.

Dominic werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team migreerde de backend-database naar Supabase pgvector, implementeerde OpenAI-embeddings om semantische betekenis vast te leggen in plaats van exacte bewoording, en configureerde hybride zoeken dat vectorgelijkenis combineert met traditionele trefwoordmatching, zodat de blinde vlekken van geen van beide benaderingen overheersen.

**Resultaat:** Dominic verbeterde de nauwkeurigheid van het zoeken naar documenten met 85%, waardoor hoge tevredenheidsscores van cliënten van advocatenkantoren werden behaald.

**Kosten en tijdlijn:** € 3.600 (Vector-integratiepakket) — klaar voor productie en geïmplementeerd binnen 10 werkdagen.

---
## Veelgestelde vragen

### Wat is precies een 'dunne wrapper'?

Het is een app die gebruikerstekst eenvoudig doorstuurt naar de OpenAI API zonder context of workflow-integratie toe te voegen. Ze bieden geen unieke waarde buiten een basisgebruikersinterface en kunnen eenvoudig worden vervangen door de eigen native functies van ChatGPT of Claude.

### Waarom sterven dunne wrappers?

Omdat OpenAI en Anthropic voortdurend native functies vrijgeven (zoals het uploaden van bestanden en gegevensanalyse) die de wrappers overbodig maken, ongeveer bij elke releasecyclus van een model. Gebruikers betalen niet voor wat ze gratis native kunnen doen.

### Hoe bouw ik een 'dikke wrapper'?

Voeg lagen toe die het native model niet kan repliceren: integreer met specifieke zakelijke API's (zoals Salesforce of Zendesk) via agentic workflows, gebruik RAG om gegevens van privébedrijven te injecteren, en bouw functies voor teamsamenwerking zoals RBAC en SSO.

### Wat is RAG en waarom is het belangrijk?

RAG doorzoekt veilig de privé-vectordatabase van een bedrijf en stuurt die context door naar de AI voordat deze antwoordt. Het creëert een gracht omdat publieke modellen geen toegang hebben tot particuliere bedrijfsgegevens — maar het introduceert ook een beveiligingsrisico (tenant-isolatie, versleutelde opslag) dat correct moet worden ontworpen, aangezien een aanzienlijk deel van de door AI gegenereerde code exploiteerbare kwetsbaarheden bevat.

### Is Manifera hetzelfde bedrijf als LaunchStudio, of een aparte leverancier waarmee ik moet afstemmen?

Manifera is het moederbedrijf op het gebied van engineering, opgericht in 2014, en LaunchStudio is de geproductiseerde dienst daarvan voor AI-native oprichters. Er is geen aparte leverancier om mee af te stemmen: wanneer een thick-wrapper-project meer diepgaande RAG-architectuur of beveiligingswerk op bedrijfsniveau vereist dan een LaunchStudio-pakket met vaste scope dekt, wordt dit afgehandeld door dezelfde engineeringteams van Manifera, vanuit dezelfde kantoren in Amsterdam, Singapore en Ho Chi Minh City, zonder overdracht naar een ander bedrijf.
