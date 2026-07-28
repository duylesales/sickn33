---
Title: "Navigeren door de EU AI Act: Wat AI SaaS-oprichters moeten weten"
Keywords: AI In SaaS, EU AI Act, AI Compliance, High-Risk AI, GPAI, AI Regulering, SaaS Founders, AI Governance
Buyer Stage: Awareness
---

# Navigeren door de EU AI Act: Wat AI SaaS-oprichters moeten weten

Tijdens de eerste jaren van de AI-hausse opereerden startups in een soort 'Wilde Westen'. Je kon in een weekend zonder seconde twijfel een AI-cv-screener, een voorspellend kredietmodel of een geautomatiseerd platform voor huurdersbeoordeling lanceren. Dat tijdperk is definitief voorbij.

De **Artificial Intelligence Act van de Europese Unie** (Verordening (EU) 2024/1689) — beter bekend als de **EU AI Act** — is op 1 augustus 2024 in werking getreden. Het is 's werelds eerste alomvattende, horizontaal toepasbare wettelijke kader voor kunstmatige intelligentie. Zoals de AVG/GDPR de manier waarop elk technologiebedrijf met persoonsgegevens omgaat fundamenteel heeft veranderd, herschrijft de AI Act de regels voor het ontwerpen, ontwikkelen, uitrollen en monitoren van AI-systemen — niet alleen in Europa, maar wereldwijd voor elk bedrijf waarvan de AI in aanraking komt met inwoners van de EU.

Dit is geen vage "toekomstige regelgeving". Sleutelbepalingen zijn nu al handhaafbaar, en andere worden op vaste datums tot 2027 verplicht. Dit is wat elke AI SaaS-oprichter moet begrijpen — in concreet, actiegericht detail — om boetes te voorkomen die kunnen oplopen tot tientallen miljoenen euro's.

---

## De handhavingslijn: Wat is al wet en wat komt er aan?

De AI Act maakt gebruik van een **gefaseerd handhavingsmodel**. Verschillende verplichtingen worden op verschillende datums van kracht, zodat bedrijven de tijd krijgen om zich voor te bereiden — maar de voorbereidingstijd dringt snel.

| **Datum** | **Wat wordt handhaafbaar** |
|---|---|
| **2 februari 2025** | Verbod op AI-praktijken met een "Onaanvaardbaar Risico" treedt volledig in werking. Verplichtingen inzake AI-geletterdheid voor aanbieders en toepassers beginnen. |
| **2 augustus 2025** | Regels voor AI-modellen voor algemene doeleinden (GPAI) zijn van toepassing. Bestuursstructuren (nationale bevoegde autoriteiten, het EU AI Office) worden operationeel. Het bootekader is volledig actief. |
| **2 augustus 2026** | De meeste overige bepalingen worden van toepassing, inclusief alle verplichtingen voor **AI-systemen met een Hoog Risico** vermeld in Bijlage III (HR, financiën, onderwijs, rechtshandhaving, enz.). Transparantieverplichtingen voor systemen met een Beperkt Risico zijn volledig handhaafbaar. |
| **2 augustus 2027** | Verplichtingen voor AI-systemen met een Hoog Risico die **veiligheidscomponenten zijn van producten** die al gereguleerd zijn onder bestaande EU-productveiligheidswetgeving (bijv. medische hulpmiddelen, machines, luchtvaart). |

**De praktische implicatie voor SaaS-oprichters:** Als uw product AI gebruikt in HR, werving, kredietwaardigheidsbeoordeling, onderwijs of verzekeringen, heeft u tot **2 augustus 2026** om volledige compliance te bereiken. Als u bouwt op basis van fundamentmodellen (GPT-4, Claude, Gemini, Llama, Mistral), zijn de GPAI-regels die uw modelaanbieder moet volgen al actief sinds **2 augustus 2025**. En als uw product onder de categorie "Onaanvaardbaar Risico" valt, is het sinds februari 2025 **al illegaal**.

---

## Het extraterritoriale bereik: Waarom de locatie van uw bedrijf irrelevant is

Een veelvoorkomende misvatting onder oprichters is: *"Mijn bedrijf is gevestigd in Delaware en mijn servers staan in AWS us-east-1, dus Europese wetten zijn niet op mij van toepassing."* Dit is onjuist en potentieel zeer kostbaar.

Net als de AVG heeft de AI Act een **breed extraterritoriaal toepassingsgebied** (Artikel 2). Het is van toepassing op:

1. **Aanbieders** (bedrijven die een AI-systeem ontwikkelen of laten ontwikkelen) die hun product op de EU-markt brengen of in de EU in gebruik nemen — ongeacht of de aanbieder binnen of buiten de EU is gevestigd.
2. **Toepassers (deployers)** (bedrijven die onder hun gezag een AI-systeem gebruiken) die in de EU zijn gevestigd of op een plaats waar het EU-recht van toepassing is.
3. **Elke aanbieder of toepasser buiten de EU** waarvan de **output van het AI-systeem in de EU wordt gebruikt**.

Dat derde punt is de vangnetbepaling. Als een hiring manager in München uw SaaS-platform gebruikt om een kandidaat te beoordelen — zelfs als uw bedrijf geen EU-kantoor, geen EU-entiteit en geen EU-servers heeft — valt u onder de AI Act. Als een kredietbeoordelaar in Amsterdam een kredietwaardigheidscheck uitvoert via uw API, valt u binnen het toepassingsgebied. Als een student in Lissabon een door AI gegenereerd cijfer ontvangt van uw EdTech-platform, bent u aan de beurt.

**De enige betrouwbare manier om de AI Act te vermijden is door alle 27 EU-lidstaten plus de EER actief te geoblokkeren** — een zakelijke beslissing die de meeste SaaS-bedrijven in de groeifase zich niet kunnen veroorloven.

Als u onder de AI Act valt maar niet in de EU gevestigd bent, bent u verplicht een **gemachtigde vertegenwoordiger** in de EU aan te wijzen (Artikel 22) voordat u uw systeem op de markt brengt. Dit is vergelijkbaar met de AVG-vereiste voor een Vertegenwoordiger voor Gegevensbescherming.

---

## Het op risico gebaseerde classificatiesysteem: Vier niveaus, radicaal verschillende verplichtingen

De AI Act reguleert niet de technologie zelf — het reguleert de **toepassing (use case)**. Hetzelfde onderliggende AI-model (bijvoorbeeld een gefinetuned LLM) kan in de ene toepassing een Minimaal Risico zijn, in de andere een Hoog Risico, en in een derde een Onaanvaardbaar Risico. Classificatie hangt volledig af van *waarvoor* het systeem wordt gebruikt en *hoe* het mensen beïnvloedt.

### Niveau 1: Onaanvaardbaar Risico — Volledig Verboden (Al handhaafbaar sinds 2 februari 2025)

Deze AI-praktijken zijn binnen de EU **volledig verboden** (Artikel 5). Er is geen compliance-traject — u mag deze onder geen enkele voorwaarde bouwen, inzetten of beschikbaar stellen aan EU-gebruikers.

De specifieke verboden omvatten:

- **Sociale kredietscoresystemen**: AI die natuurlijke personen beoordeelt of classificeert op basis van hun sociaal gedrag of persoonlijke kenmerken, wat leidt tot nadelige behandeling die niet in verhouding staat tot de context. Dit geldt voor zowel overheids- als particuliere toepassingen.

- **Subliminale, manipulatieve of misleidende AI-technieken**: Systemen die technieken inzetten buiten het bewustzijn van een persoon om, of kwetsbaarheden uitbuiten met betrekking tot leeftijd, handicap of sociaal-economische situatie, op een manier die gedrag wezenlijk vervormt en aanzienlijke schade veroorzaakt.

- **Biometrische categorisering op basis van gevoelige kenmerken**: AI-systemen die individuen categoriseren op basis van biometrische gegevens om ras, politieke opvattingen, lidmaatschap van een vakbond, religieuze overtuigingen, seksueel leven of seksuele geaardheid af te leiden. (Uitzondering: rechtmatig labelen van biometrische datasets bij rechtshandhaving.)

- **Emotieherkenning op de werkplek en in onderwijsinstellingen**: AI die emoties van werknemers of studenten afleidt op basis van biometrische gegevens, behalve om medische of veiligheidsredenen.

- **Gericht of ongericht scrapen voor gezichtsherkenningsdatabanken**: Het maken of uitbreiden van gezichtsherkenningsdatabanken via het gericht of ongericht scrapen van afbeeldingen van het internet of CCTV-beelden.

- **Voorspellende politiezorg uitsluitend gebaseerd op profiling**: AI die de kans beoordeelt dat een persoon een misdrijf pleegt uitsluitend op basis van profiling of persoonlijkheidskenmerken, zonder objectieve feiten die verband houden met criminele activiteiten.

- **Real-time biometrische identificatie op afstand in openbare ruimten voor rechtshandhaving**: Onderworpen aan zeer strenge uitzonderingen met voorafgaande rechterlijke toestemming.

**Praktische SaaS-implicaties:** Als uw product enige vorm van emotiedetectie bevat die wordt toegepast op werkplekken (monitoren van het humeur van werknemers tijdens videogesprekken, sentimentanalyse in teamvergaderingen) of onderwijsomgevingen (monitoren van de aandacht van studenten via webcam-analyse), is dit sinds februari 2025 **al illegaal in de EU**. Verschillende EdTech- en HR-tech-tools die in 2023-2024 zijn gelanceerd, hebben hun EU-activiteiten moeten staken of hun functies fundamenteel moeten herontwerpen.

---

### Niveau 2: Hoog Risico — Streng Gereguleerd (Handhaafbaar vanaf 2 augustus 2026)

Dit is het niveau waar de meeste B2B SaaS-oprichters mee te maken krijgen. Een AI-systeem wordt geclassificeerd als "Hoog Risico" als het valt onder een van de toepassingen genoemd in **Bijlage III** van de wet, of als het een veiligheidscomponent is van een product dat onder bestaande EU-productveiligheidswetgeving valt (Bijlage I).

#### Bijlage III Use Cases voor Hoog Risico die het meest relevant zijn voor SaaS-oprichters

| **Domein** | **Specifieke Use Cases** | **Veelvoorkomende SaaS-voorbeelden** |
|---|---|---|
| **Werkgelegenheid, personeelsbeheer, toegang tot ondernemerschap** | AI voor werving, cv-screening, beoordeling van kandidaten, besluitvorming over promotie/ontslag, toewijzen van taken, monitoren van prestaties | ATS-platformen met AI-ranking, tools voor het voorspellen van werknemersprestaties, AI-interviewanalysers |
| **Toegang tot essentiële particuliere/overheidsdiensten** | AI voor het beoordelen van kredietwaardigheid, vaststellen van verzekeringspremies, beoordelen van geschiktheid voor uitkeringen, credit scoring | Fintech-leenplatformen, verzekeringsacceptatiesystemen, credit scoring API's |
| **Onderwijs en beroepsopleiding** | AI voor het bepalen van toegang tot onderwijsinstellingen, beoordelen van leerresultaten, beoordelen van het juiste onderwijsniveau, monitoren van verboden gedrag tijdens examens | AI-nakijktools, adaptieve leerplatformen met hoogwaardige toetsing, online proctoring-software |
| **Rechtspleging en democratische processen** | AI die rechterlijke instanties helpt bij het onderzoeken/interpreteren van feiten en recht, AI gebruikt om verkiezingsuitslagen te beïnvloeden | Juridische AI-researchtools gebruikt door rechtbanken, politieke campagne-AI-tools |
| **Migratie, asiel en grenscontrole** | AI voor het verwerken van visum-/verblijfsaanvragen, beoordelen van veiligheidsrisico's van migranten | SaaS voor migratieverwerking |
| **Biometrische identificatie (niet-verboden)** | Biometrische identificatiesystemen op afstand niet gedekt door het verbod, biometrische categorisering voor niet-verboden doeleinden | Identiteitsverificatieplatformen voor leeftijds-/identiteitschecks |

#### Wat "Hoog Risico" daadwerkelijk vereist: De technische compliance-last

Als uw AI-systeem geclassificeerd is als Hoog Risico, moet u de volgende **verplichte vereisten** implementeren — en continu onderhouden — voordat u het op de EU-markt brengt (Artikelen 8-15):

**1. Risicobeheersysteem (Artikel 9)**
Een gedocumenteerd, iteratief proces dat gedurende de gehele levenscyclus van het AI-systeem loopt. Dit is geen eenmalig risicobeoordelingsdocument — het moet:
- Bekende en redelijkerwijs te voorziene risico's identificeren en analyseren.
- Risico's inschatten en evalueren die voortvloeien uit beoogd gebruik *en* redelijkerwijs te voorzien misbruik.
- Risicobeperkende maatregelen nemen en de effectiviteit ervan testen.
- Worden herzien en bijgewerkt wanneer er wijzigingen worden aangebracht of belangrijke nieuwe informatie aan het licht komt.

**2. Data Governance (Artikel 10)**
Trainings-, validatie- en testdatasets moeten aan strenge kwaliteitscriteria voldoen:
- Rerelevant, voldoende representatief en zo veel mogelijk vrij van fouten zijn.
- Passende statistische eigenschappen bezitten, inclusief voor de specifieke geografische, contextuele of functionele setting waarin het systeem zal werken.
- Mogelijke vooringenomenheid (bias) aanpakken, met name bias die leidt tot discriminatie van beschermde groepen.
- Als persoonsgegevens worden gebruikt voor het monitoren/corrigeren van bias, gelden specifieke waarborgen waaronder dataminimalisatie en toegangscriteria.

**3. Technische Documentatie (Artikel 11)**
Voordat u het systeem op de markt brengt, moet u uitgebreide technische documentatie opstellen waaruit blijkt dat aan alle vereisten is voldaan. Deze documentatie moet gedurende de gehele levenscyclus actueel worden gehouden. De vereiste inhoud is omvangrijk — het omvat een algemene beschrijving, gedetailleerde informatie over het ontwikkelingsproces, ontwerpspecificaties, controleprocedures en een beschrijving van het risicobeheersysteem.

**4. Automatische Logging / Record-Keeping (Artikel 12)**
AI-systemen met een Hoog Risico moeten zo worden ontworpen dat gebeurtenissen ("logs") gedurende hun levensduur automatisch worden geregistreerd. Logs moeten het volgende mogelijk maken:
- Traceerbaarheid van het functioneren van het systeem.
- Identificatie van situaties die kunnen resulteren in een risico.
- Monitoring na het op de markt brengen (post-market monitoring).
- Monitoring van de werking van het systeem door toepassers.

Logs moeten worden bewaard gedurende een periode die passend is voor het beoogde doel — ten minste de duur gespecificeerd in het toepasselijke recht, en niet minder dan zes maanden.

**5. Transparantie en informatie aan toepassers (Artikel 13)**
AI-systemen met een Hoog Risico moeten voldoende transparant zijn ontworpen om toepassers in staat te stellen de output van het systeem te interpreteren en passend te gebruiken. U moet het volgende bieden:
- Duidelijke gebruiksinstructies met beknopte, volledige, correcte en begrijpelijke informatie.
- De mogelijkheden en beperkingen van het systeem, inclusief het nauwkeurigheidsniveau, de robuustheid en de cybersecurity.
- Bekende of voorzienbare omstandigheden die tot risico's kunnen leiden.
- Technische maatregelen om de interpretatie van outputs te vergemakkelijken.

**6. Menselijk Toezicht (Human-in-the-Loop) (Artikel 14)**
AI-systemen met een Hoog Risico moeten zo worden ontworpen dat ze tijdens het gebruik doeltreffend kunnen worden gecontroleerd door natuurlijke personen:
- De menselijke toezichthouder moet de capaciteiten en beperkingen van het systeem volledig begrijpen.
- Moet outputs correct kunnen interpreteren.
- Moet kunnen besluiten het systeem niet te gebruiken, de output te negeren, te overschrijven of terug te draaien.
- Moet het systeem kunnen onderbreken via een "stop-knop" of een vergelijkbare procedure.

**7. Nauwkeurigheid, Robuustheid en Cybersecurity (Artikel 15)**
- Het systeem moet gedurende zijn gehele levenscyclus een passend niveau van nauwkeurigheid, robuustheid en cybersecurity bereiken.
- Niveaus moeten worden verklaard in de bijbehorende gebruiksinstructies.
- Moet bestand zijn tegen fouten, storingen en pogingen van onbevoegden om het gebruik of de prestaties te wijzigen (inclusief adversarial attacks zoals data poisoning of modelmanipulatie).

#### Conformiteitsbeoordeling: De toegangsprocedure tot de markt

Voordat u een AI-systeem met een Hoog Risico legaal op de EU-markt kunt brengen, moet u een **conformiteitsbeoordeling** ondergaan (Artikel 43). Voor de meeste Bijlage III-systemen kan dit een interne conformiteitsbeoordeling zijn (Bijlage VI) — wat betekent dat u zelf compliance certificeert, maar alle documentatie moet bijhouden en voorbereid moet zijn op audits door markttoezichtautoriteiten.

Na de conformiteitsbeoordeling moet u:
- Een **CE-markering** op het systeem aanbrengen.
- Het systeem registreren in de **EU AI-databank** (een openbare databank).
- Een **EU-conformiteitsverklaring** opstellen.

---

### Niveau 3: Beperkt Risico — Transparantieverplichtingen (Handhaafbaar vanaf 2 augustus 2026)

Dit niveau omvat de meeste generatieve AI-tools, chatbots en contentgeneratiesystemen. De primaire verplichting is **transparantie** (Artikel 50):

- **AI-gegenereerde content**: Als uw systeem synthetische audio-, beeld-, video- of tekstcontent genereert, moet u ervoor zorgen dat de output machinaal leesbaar is gemarkeerd als kunstmatig gegenereerd of gemanipuleerd (bijv. deepfakes).

- **Chatbots en conversationele AI**: U moet gebruikers er duidelijk van op de hoogte stellen dat ze communiceren met een AI-systeem en niet met een mens — tenzij dit uit de omstandigheden overduidelijk is.

- **Emotieherkenning of biometrische categorisering**: Als uw systeem emotieherkenning of biometrische categorisering uitvoert (in contexten waarin dit legaal is), moet u de blootgestelde personen informeren over de werking van het systeem.

**Praktische SaaS-implicaties:** Als u een klantenservice-chatbot, een AI-schrijfassistent of een AI-afbeeldingengenerator bouwt, moet u duidelijke disclosure-mechanismen implementeren (UI-labels zoals "Dit antwoord is gegenereerd door AI", metadata-tags op gegeneerde media via C2PA-standaarden, en watermerken).

---

### Niveau 4: Minimaal Risico — Geen specifieke verplichtingen

AI-toepassingen zoals spamfilters, AI-gebaseerde videogames, voorraadoptimalisatietools of aanbevelingsmotoren voor niet-kritieke beslissingen vallen hieronder. De overgrote meerderheid van de AI-systemen behoort tot deze categorie en heeft geen aanvullende regelgevingsverplichtingen onder de wet buiten de bestaande algemene wetgeving (AVG, consumentenrecht, productveiligheid).

---

## AI-modellen voor algemene doeleinden (GPAI): Verplichtingen voor aanbieder vs. toepasser

De AI Act introduceert specifieke regels voor **General-Purpose AI (GPAI)-modellen** (Artikelen 51-56) — fundamentmodellen zoals GPT-4, Claude, Gemini, Llama en Mistral.

### Als u een GPAI-modelaanbieder bent (u heeft het fundamentmodel getraind)

U moet technische documentatie bijhouden, informatie verstrekken aan downstream-ontwikkelaars, voldoen aan het EU-auteursrecht en een gedetailleerde samenvatting van de trainingsdata publiceren. Voor GPAI-modellen met **systemisch risico** (getraind met meer dan 10²⁵ FLOPs aan rekenkracht) gelden aanvullende verplichtingen zoals adversarial testing en incidentenrapportage.

### Als u een SaaS-toepasser bent die bouwt op basis van een GPAI-model

**U bent niet vrijgesteld van de AI Act omdat u het model van iemand anders gebruikt.** De aanbieder van het onderliggende model (OpenAI, Anthropic, Google) is verantwoordelijk voor de verplichtingen op modelniveau. Maar u, als toepasser of downstream-aanbieder van de *applicatie*, bent verantwoordelijk voor:

- **Het correct classificeren van het risiconiveau van uw applicatie** op basis van het beoogde doel.
- **Het voldoen aan alle verplichtingen** die horen bij dat risiconiveau (Hoog Risico, Beperkt Risico, enz.).
- **Het uitvoeren van uw eigen risicobeheer** voor de specifieke use case die u heeft gebouwd.
- **Het waarborgen dat de outputs** van het model zoals toegepast in uw systeem niet discriminerend zijn en goed onder toezicht staan.
- **Het bieden van transparantie** aan eindgebruikers over de rol van AI in uw product.

In praktische termen: als u een AI-gebaseerde cv-screener bouwt met de OpenAI API, moet OpenAI voldoen aan de GPAI-regels voor hun model — maar *u* moet voldoen aan de volledige vereisten voor AI-systemen met een Hoog Risico voor uw screeningapplicatie. U kunt dit niet delegeeren aan uw modelaanbieder.

---

## De boetes: De EU blaast niet hoog van de toren

Het bootekader (Artikel 99) is bewust ontworpen om op elke schaal van bedrijf voelbaar te zijn:

| **Overtreding** | **Maximale Boete** |
|---|---|
| Inzetten van een **verboden AI-praktijk** (Onaanvaardbaar Risico) | **€35 miljoen** of **7% van de wereldwijde jaaromzet** (het hoogste bedrag telt) |
| Niet voldoen aan **vereisten voor systemen met een Hoog Risico** of GPAI-regels | **€15 miljoen** of **3% van de wereldwijde jaaromzet** |
| Verstrekken van **onjuiste, onvolledige of misleidende informatie** aan toezichthouders | **€7,5 miljoen** of **1% van de wereldwijde jaaromzet** |

Voor kmo's en startups worden de boetes aangepast aan het laagste van de twee cijfers — maar zelfs de "gereduceerde" boetes kunnen fataal zijn voor een startup.

---

## Een praktisch compliance-stappenplan voor SaaS-oprichters

1. **Classificeer uw systeem eerlijk**: Breng elke AI-functie in uw product in kaart volgens Bijlage III. Bij twijfel: behandel het als Hoog Risico.
2. **Implementeer logging-infrastructuur vanaf dag één**: Ontwerp uw database en API-middleware zo dat elke input, output, modelversie, timestamp en menselijke override automatisch en onveranderbaar wordt vastgelegd.
3. **Bouw het Human-in-the-Loop-mechanisme**: Zorg voor een echte interface waar een gekwalificeerd persoon AI-beslissingen kan beoordelen, overschrijven of stoppen.
4. **Documenteer uw datapijplijn**: Stel technische documentatie op over databronnen, biastesten, nauwkeurigheidsbenchmarks en beperkingen.
5. **Bereid u voor op conformiteitsbeoordeling**: Stel een kwaliteitsborgingssysteem in, stel de EU-conformiteitsverklaring op en meld u aan bij de EU-databank.
6. **Wijs verantwoordelijke personen aan**: Wijs een interne AI-compliance-officer aan en wijs als niet-EU-bedrijf een gemachtigde vertegenwoordiger in de EU aan.

---

## Bouw een compliant infrastructuur

Riskering geen boete van €15 miljoen. LaunchStudio bouwt veilige, auditeerbare database-infrastructuur die uw startup helpt te voldoen aan de strenge vereisten op het gebied van logging, data governance, menselijk toezicht en risicobeheer van de EU AI Act.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf geleid door Oprichter & Directeur **Herre Roelevink**. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingshubs in **Singapore** en **Ho Chi Minh-stad, Vietnam**. Via LaunchStudio nemen onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, geautomatiseerde logging-pijplijnen, interfaces voor menselijk toezicht, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype in 1 tot 3 weken verandert in een veilige, aan de EU AI Act voldoende MVP. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact).

---

## Praktijkvoorbeeld

### Een AI-Native Oprichter in actie: AI HR-beoordelingstool

Stella, een startup-oprichter, gebruikte **Cursor** om een prototype voor een AI HR-beoordelingstool te bouwen dat sollicitanten rangschikte met behulp van een gefinetuned LLM. De tool analyseerde cv's, voorspelde culturele fit-scores en beveelde kandidaten aan. Hoewel de applicatie functioneel indrukwekkend was, kon deze niet in Europa worden gelanceerd vanwege meerdere hiaten in de naleving van de EU AI Act:

- **Geen automatische logging** van AI-beslissingen — geen audit trail van waarom specifieke kandidaten hoger of lager werden gerangschikt.
- **Geen biastesten** op de trainingsdataset — geen bewijs dat het systeem niet discrimineerde op basis van geslacht, etniciteit of leeftijd.
- **Geen human-in-the-loop-mechanisme** — hiring managers ontvingen definitieve ranglijsten zonder de mogelijkheid om de redenering van de AI te inspecteren of individuele beslissingen te overschrijven.
- **Geen technische documentatie** waarin de nauwkeurigheid, bekende beperkingen of beoogde gebruiks-omstandigheden van het systeem werden beschreven.

Stella werkte samen met **LaunchStudio (door Manifera)** om het product lanceerplatform-klaar te maken. Het engineeringteam:

1. Bouwde een **onveranderlijk model-activiteitsloggingsysteem** dat elke input, output, modelversie en timestamp in een audit trail vastlegde.
2. Ontwierp een **interface voor menselijke beoordeling** waar HR-managers AI-redeneringen konden inspecteren, rangschikkingen konden overschrijven en hun beslissingen konden documenteren.
3. Configureerde **geautomatiseerde biastestpijplijnen** die draaiden op representatieve demografische datasets.
4. Stel **uitgebreide technische documentatie** op over datatherkomst, nauwkeurigheidsbenchmarks, bekende beperkingen en richtlijnen voor uitrol.
5. Zorgde voor **veilige EU-datahosting** (Frankfurt, Duitsland) met AVG-compliant gegevensverwerking en een passend bewaarbeleid.

**Resultaat:** Stella lanceerde in volledige overeenstemming met de vereisten voor AI-systemen met een Hoog Risico van de EU AI Act, en haalde contracten binnen met Franse en Duitse bedrijven die aantoonbare naleving van regelgeving eisten van hun HR-technologieleveranciers.

**Kosten & Doorlooptijd:** €5.200 (EU Compliance Pakket) — productieclaar en uitgerold in 16 werkdagen.

---

---

---
## Veelgestelde Vragen

### Wat is de EU AI Act en wanneer treedt deze in werking?

De EU AI Act (Verordening (EU) 2024/1689) is 's werelds eerste alomvattende wettelijke kader dat kunstmatige intelligentie reguleert op basis van het potentieel om schade te berokkenen. Het verdeelt AI-systemen in vier risiconiveaus — Minimaal, Beperkt, Hoog en Onaanvaardbaar — met toenemend strenge verplichtingen. De wet is in werking getreden op 1 augustus 2024. Verboden op praktijken met een Onaanvaardbaar Risico zijn van kracht sinds 2 februari 2025, GPAI-modelregels gelden vanaf 2 augustus 2025, en de meeste verplichtingen voor systemen met een Hoog Risico worden van kracht op 2 augustus 2026.

### Is de EU AI Act van toepassing op mijn startup als ik buiten de EU gevestigd ben?

Ja. De EU AI Act heeft een breed extraterritoriaal bereik, vergelijkbaar met de AVG/GDPR. Als uw AI-systeem op de EU-markt wordt gebracht, in de EU in gebruik wordt genomen, of als de output ervan binnen de EU wordt gebruikt — ongeacht waar uw bedrijf is gevestigd of waar uw servers staan — moet u voldoen. Een in de VS gevestigde startup waarvan de SaaS door één enkele hiring manager in Duitsland wordt gebruikt, valt onder de wet. Niet-EU-aanbieders moeten bovendien een gemachtigde vertegenwoordiger in de EU aanwijzen voordat ze hun product op de markt brengen.

### Hoe bepaal ik of mijn SaaS-product is geclassificeerd als 'Hoog Risico'?

Uw AI-systeem heeft een Hoog Risico als het valt onder een van de use cases vermeld in Bijlage III van de wet. De meest voorkomende SaaS-relevante categorieën zijn: werkgelegenheid en personeelsbeheer (AI voor werving, cv-screening, prestatiebeoordeling), toegang tot essentiële diensten (credit scoring, verzekeringsacceptatie, leningbesluiten) en onderwijs (beoordeling van examens, toelatingsbesluiten, proctoring). Als uw AI invloed heeft op beslissingen over de toegang van mensen tot werk, krediet, verzekeringen of onderwijs, is het vrijwel zeker Hoog Risico.

### Welke technische maatregelen moet ik implementeren voor een AI-systeem met een Hoog Risico?

AI-systemen met een Hoog Risico vereisen zes categorieën van technische compliance: (1) een continu bijgewerkt risicobeheersysteem, (2) data governance die de kwaliteit van trainingsdata en bias-mitigatie waarborgt, (3) uitgebreide technische documentatie, (4) automatische logging van alle systeemgebeurtenissen met een passend bewaarbeleid, (5) transparantiebepalingen inclusief duidelijke instructies voor toepassers, en (6) mechanismen voor menselijk toezicht (Human-in-the-Loop) waarmee gekwalificeerde mensen AI-outputs kunnen begrijpen, interpreteren en overschrijven. Bovendien moet u passende niveaus van nauwkeurigheid, robuustheid en cybersecurity aantonen, een conformiteitsbeoordeling voltooien, het systeem registreren in de EU AI-databank en een CE-markering aanbrengen.

### Wat zijn de boetes voor het overtreden van de EU AI Act?

Boetes zijn gestructureerd in drie niveaus op basis van de ernst van de overtreding. Het inzetten van een verboden AI-praktijk (Onaanvaardbaar Risico) kan leiden tot boetes tot €35 miljoen of 7% van de wereldwijde jaaromzet, afhankelijk van welk bedrag het hoogst is. Niet voldoen aan vereisten voor systemen met een Hoog Risico of GPAI-verplichtingen kan leiden tot boetes tot €15 miljoen of 3% van de wereldwijde jaaromzet. Het verstrekken van onjuiste of misleidende informatie aan toezichthouders kan leiden tot boetes tot €7,5 miljoen of 1% van de wereldwijde jaaromzet. Voor kmo's en startups geldt het laagste van de twee bedragen — maar zelfs gereduceerde boetes kunnen fataal zijn voor beginnende bedrijven.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de EU AI Act en wanneer treedt deze in werking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De EU AI Act (Verordening (EU) 2024/1689) is 's werelds eerste alomvattende wettelijke kader dat kunstmatige intelligentie reguleert op basis van het potentieel om schade te berokkenen. Het verdeelt AI-systemen in vier risiconiveaus — Minimaal, Beperkt, Hoog en Onaanvaardbaar — met toenemend strenge verplichtingen. De wet is in werking getreden op 1 augustus 2024. Verboden op praktijken met een Onaanvaardbaar Risico zijn van kracht sinds 2 februari 2025, GPAI-modelregels gelden vanaf 2 augustus 2025, en de meeste verplichtingen voor systemen met een Hoog Risico worden van kracht op 2 augustus 2026."
      }
    },
    {
      "@type": "Question",
      "name": "Is de EU AI Act van toepassing op mijn startup als ik buiten de EU gevestigd ben?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. De EU AI Act heeft een breed extraterritoriaal bereik, vergelijkbaar met de AVG/GDPR. Als uw AI-systeem op de EU-markt wordt gebracht, in de EU in gebruik wordt genomen, of als de output ervan binnen de EU wordt gebruikt — ongeacht waar uw bedrijf is gevestigd of waar uw servers staan — moet u voldoen. Een in de VS gevestigde startup waarvan de SaaS door één enkele hiring manager in Duitsland wordt gebruikt, valt onder de wet. Niet-EU-aanbieders moeten bovendien een gemachtigde vertegenwoordiger in de EU aanwijzen voordat ze hun product op de markt brengen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe bepaal ik of mijn SaaS-product is geclassificeerd als 'Hoog Risico'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uw AI-systeem heeft een Hoog Risico als het valt onder een van de use cases vermeld in Bijlage III van de wet. De meest voorkomende SaaS-relevante categorieën zijn: werkgelegenheid en personeelsbeheer (AI voor werving, cv-screening, prestatiebeoordeling), toegang tot essentiële diensten (credit scoring, verzekeringsacceptatie, leningbesluiten) en onderwijs (beoordeling van examens, toelatingsbesluiten, proctoring). Als uw AI invloed heeft op beslissingen over de toegang van mensen tot werk, krediet, verzekeringen of onderwijs, is het vrijwel zeker Hoog Risico."
      }
    },
    {
      "@type": "Question",
      "name": "Welke technische maatregelen moet ik implementeren voor een AI-systeem met een Hoog Risico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI-systemen met een Hoog Risico vereisen zes categorieën van technische compliance: (1) een continu bijgewerkt risicobeheersysteem, (2) data governance die de kwaliteit van trainingsdata en bias-mitigatie waarborgt, (3) uitgebreide technische documentatie, (4) automatische logging van alle systeemgebeurtenissen met een passend bewaarbeleid, (5) transparantiebepalingen inclusief duidelijke instructies voor toepassers, en (6) mechanismen voor menselijk toezicht (Human-in-the-Loop) waarmee gekwalificeerde mensen AI-outputs kunnen begrijpen, interpreteren en overschrijven. Bovendien moet u passende niveaus van nauwkeurigheid, robuustheid en cybersecurity aantonen, een conformiteitsbeoordeling voltooien, het systeem registreren in de EU AI-databank en een CE-markering aanbrengen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zijn de boetes voor het overtreden van de EU AI Act?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Boetes zijn gestructureerd in drie niveaus op basis van de ernst van de overtreding. Het inzetten van een verboden AI-praktijk (Onaanvaardbaar Risico) kan leiden tot boetes tot €35 miljoen of 7% van de wereldwijde jaaromzet, afhankelijk van welk bedrag het hoogst is. Niet voldoen aan vereisten voor systemen met een Hoog Risico of GPAI-verplichtingen kan leiden tot boetes tot €15 miljoen of 3% van de wereldwijde jaaromzet. Het verstrekken van onjuiste of misleidende informatie aan toezichthouders kan leiden tot boetes tot €7,5 miljoen of 1% van de wereldwijde jaaromzet. Voor kmo's en startups geldt het laagste van de twee bedragen — maar zelfs gereduceerde boetes kunnen fataal zijn voor beginnende bedrijven."
      }
    }
  ]
}
</script>
