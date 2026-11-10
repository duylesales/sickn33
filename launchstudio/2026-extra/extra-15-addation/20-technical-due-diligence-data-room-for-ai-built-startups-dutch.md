---
Titel: "Technische Due Diligence Dataroom voor AI-Gebouwde Startups"
Trefwoorden: technische due diligence startup, tech dd data room, ai gebouwde startup due diligence, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Technische Due Diligence Dataroom voor AI-Gebouwde Startups

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Technische Due Diligence Dataroom voor AI-Gebouwde Startups",
  "description": "Investeerders en kopers beoordelen door AI gebouwde producten met specifieke vragen over code-eigendom, architectuur, beveiliging, schaalbaarheid, AI-afhankelijkheden en teamkennis. Deze gids beschrijft wat er in een technische due-diligence-dataroom hoort, op welke rode vlaggen reviewers letten in door AI gegenereerde codebases en hoe u zich in twee tot vier weken voorbereidt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-07",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/technical-due-diligence-data-room-for-ai-built-startups" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021", "url": "https://owasp.org/Top10/" },
    { "@type": "CreativeWork", "name": "OpenSSF Scorecard", "url": "https://securityscorecards.dev/" },
    { "@type": "CreativeWork", "name": "SPDX License List", "url": "https://spdx.org/licenses/" },
    { "@type": "CreativeWork", "name": "AVG Artikel 30: Register van verwerkingsactiviteiten", "url": "https://gdpr-info.eu/art-30-gdpr/" }
  ]
}
</script>

Technische due diligence was vroeger iets wat alleen gebeurde bij bedrijven in latere fasen: een team van engineers van de investeerder of koper bracht een week door met het doorlezen van code, het interviewen van de CTO en het opstellen van een risicorapport. Tegenwoordig vindt dit onderzoek veel vroeger plaats. Angel-investeerders nemen een technische bekende mee om de repository te controleren. Seed-fondsen laten een korte code review uitvoeren. Kopers van kleine SaaS-bedrijven stellen gedetailleerde vragen nog vóórdat ze een intentieverklaring (LOI) ondertekenen.

Voor door AI gebouwde startups zijn de vragen scherper geworden. Reviewers weten dat een product dat is gebouwd met Lovable, Bolt, Cursor of Claude Code er volwassen uit kan zien, terwijl het problemen verbergt die een menselijk team zelden zou introduceren: te soepele databasepolicies, geheimen in de git-geschiedenis, tests die niets wezenlijks verifiëren en niemand die het volledige systeem écht doorgrondt. Ze stellen ook nieuwe vragen over AI-afhankelijkheden, licenties en wie juridisch gezien de code bezit.

Een goed voorbereide technische dataroom beantwoordt die vragen al vóórdat ze worden gesteld. Deze gids legt uit wat erin hoort en hoe u zich voorbereidt.

## Belangrijkste Punten

- **Technische due diligence beoordeelt risico, geen esthetiek.** Reviewers willen weten of het product werkt, veilig is, kan schalen, eigendom is van het bedrijf en kan worden onderhouden door anderen dan de oprichter.
- **Door AI gebouwde codebases worden specifiek gecontroleerd** op toegangscontrole, secrets, testkwaliteit, dependency-hygiëne, licenties en documentatie.
- **Een dataroom moet acht secties bevatten:** overzicht, architectuur, code en eigendom, beveiliging, data en privacy, operaties, AI-afhankelijkheden en roadmap.
- **Los kritieke problemen op vóór de review,** omdat dezelfde bevindingen tijdens onderhandelingen meer kosten aan waarderingsverlies dan aan reparatiekosten.
- **Twee tot vier weken voorbereiding** is meestal voldoende voor een product in een vroeg stadium.

## Wat Reviewers Echt Vragen

Achter tientallen gedetailleerde vragen draait technische due diligence om vijf kernzorgen:

1. **Werkt het?** Is het product stabiel, in gebruik bij echte klanten en doet het wat de pitch belooft?
2. **Is het veilig?** Kan een beveiligingsincident, datalek of regelgevingsprobleem het bedrijf schaden na de investering?
3. **Kan het groeien?** Ondersteunt de architectuur tien keer zoveel gebruikers, of moet alles opnieuw worden opgebouwd?
4. **Is het uw eigendom?** Bezit het bedrijf de code, data en accounts, vrij van licentieclaims of claims van derden?
5. **Kan het doorgaan zonder de oprichter?** Kan een nieuw engineeringteam het systeem begrijpen en uitbreiden?

AI-tools hebben de eerste vraag makkelijker gemaakt om te beantwoorden en de laatste moeilijker. Een oprichter die een product via prompts tot stand heeft gebracht, kan mogelijk niet uitleggen waarom het onder de motorkap werkt - en dat is precies wat reviewers onderzoeken.

## Rode Vlaggen in Door AI Gebouwde Codebases

| Rode vlag | Waarom reviewers hierop letten | Hoe het meestal wordt ontdekt |
| --- | --- | --- |
| Te soepele databasepolicies | Elke gebruiker kan gegevens van andere klanten inzien | API bevragen met de publieke sleutel en twee testaccounts |
| Secrets in de git-geschiedenis | Sleutels kunnen zijn gecompromitteerd, rotatiediscipline ontbreekt | Secret scanning over alle eerdere commits |
| Tests die alles mocken | Testsuite geeft schijnzekerheid | Tests inspecteren op daadwerkelijke asserts |
| Geen staging-omgeving | Elke release is een experiment in productie | Beoordeling van het deploymentproces |
| Grote ongebruikte of verouderde dependencies | Beveiligings- en licentierisico | Dependency- en licentiescans |
| Dubbele logica over meerdere bestanden | Hoge onderhoudskosten, inconsistent gedrag | Code review van de programmastructuur |
| Geen migraties, schema handmatig aangepast | Databasestatus kan niet worden gereproduceerd | Vergelijking tussen database en repository |
| Accounts op persoonlijke naam | Risico voor eigendom en bedrijfscontinuïteit | Inventarisatie van accounts en abonnementen |
| Geen documentatie | Kennis bevindt zich alleen bij de oprichter of de AI-tool | Interviews en inspectie van de repository |

Geen van deze punten is ongebruikelijk. De meeste codebases in een vroeg stadium, al dan niet met AI gebouwd, vertonen enkele van deze kenmerken. Wat telt is of de oprichter hiervan op de hoogte is, een plan heeft en aantoonbare vooruitgang laat zien.

## De Acht Secties van een Technische Dataroom

**1. Product- en technisch overzicht.** Een samenvatting van twee pagina's: wat het product doet, wie het gebruikt, belangrijke statistieken zoals actieve gebruikers en uptime, de technologiestack, hostinglocaties en het team. Dit is het eerste document dat reviewers lezen en het zet direct de toon.

**2. Architectuur.** Een diagram van componenten en datastromen: frontend, backend, database, opslag, externe diensten, AI-providers en hoe deze met elkaar verbonden zijn. Neem op waar authenticatie plaatsvindt en waar autorisatie wordt afgedwongen. Een diagram van één pagina plus een korte toelichting is in vroege fasen ruim voldoende.

**3. Code en eigendom.**

- Repositorytoegang voor reviewers, op basis van alleen-lezen
- Licentie-inventaris van dependencies, met eventuele copyleft-licenties gemarkeerd
- Bevestiging dat code geschreven door externe partijen of bureaus schriftelijk is overgedragen aan het bedrijf
- Notities over gebruikte AI-tools en hun voorwaarden met betrekking tot eigendom van gegenereerde output
- Lijst van accounts, zoals domeinregistrar, hosting, database, betaalprovider, e-mail, analytics en appstores, allemaal geregistreerd op naam van het bedrijf

**4. Beveiliging.**

- Beveiligingsoverzicht: model voor toegangscontrole, authenticatie, MFA, geheimenbeheer, encryptie, logging
- Resultaten van de meest recente security review of pentest, inclusief de status van de bevindingen
- Incidentgeschiedenis en hoe incidenten zijn afgehandeld
- Proces voor het beheren van kwetsbaarheden

**5. Data en privacy.**

- Register van verwerkingsactiviteiten onder AVG Artikel 30, ten minste in vereenvoudigde vorm
- Lijst van verwerkers en subverwerkers met locaties en verwerkersovereenkomsten
- Beleid voor dataretentie en dataverwijdering
- Template voor verwerkersovereenkomsten voor klanten

**6. Operaties.**

- Deploymentproces en verschillende omgevingen
- Monitoring, alarmering en uptime-geschiedenis
- Back-upbeleid en de datum van de meest recente hersteltest
- Infrastructuurkosten per maand en hoe deze meegroeien met het gebruik

**7. AI-afhankelijkheden.**

- Welke AI-modellen en providers het product gebruikt, uitgesplitst per functionaliteit
- Contracten, voorwaarden voor datagebruik en of klantdata wordt gebruikt voor modeltraining
- Fallback-gedrag wanneer een provider onbeschikbaar is
- Kosten per gebruiker van AI-functionaliteiten en hoe deze schalen
- Evaluatie of kwaliteitsbewaking van door AI gegenereerde resultaten

**8. Roadmap en bekende problemen.**

- Register van technische schuld met prioriteiten
- Geplande architectuurwijzigingen
- Wervingsplan voor engineering

Een heldere lijst met bekende problemen is een teken van volwassenheid. Reviewers vertrouwen oprichters die openhartig zijn over knelpunten met een bijbehorend plan veel meer dan oprichters die beweren dat er geen enkel probleem is.

## Hoe U Zich in Twee tot Vier Weken Voorbereidt

**Week 1: Inventarisatie en snelle scans.** Maak een overzicht van alle accounts en zet accounts die privé worden gehouden over naar bedrijfseigendom. Voer een secret scan uit over de volledige git-geschiedenis, een kwetsbaarhedenscan op dependencies en een licentiescan. Teken het architectuurdiagram.

**Week 2: Los de kritieke problemen op.** Pak bevindingen aan die reviewers als kritiek zouden bestempelen: datatoegang tussen klanten onderling, blootgestelde secrets, ontbrekende back-ups, beheerderstoegang zonder MFA. Dit is doorgaans een paar dagen geconcentreerd werk en neemt de ernstigste waarderingsrisico's direct weg.

**Week 3: Documenteer.** Schrijf het productoverzicht, het beveiligingsoverzicht, de data- en privacydocumenten en de lijst met bekende problemen. Voeg een README toe aan de repository waarin wordt uitgelegd hoe het project lokaal kan worden gedraaid, hoe deployments werken en waar belangrijke logica zich bevindt.

**Week 4: Oefen de review.** Laat een technisch persoon die onafhankelijk is van de oorspronkelijke bouw de repository en documenten doornemen zoals een reviewer dat zou doen. Bereid u voor op interviewvragen, met name: "leg me stap voor stap uit wat er gebeurt wanneer een gebruiker zich registreert en betaalt".

## Vragen om te Oefenen

Oprichters van door AI gebouwde producten krijgen regelmatig de volgende vragen:

- "Welke delen van de code heeft u zelf geschreven, welke zijn door AI-tools gegenereerd en wie heeft deze gereviewd?"
- "Hoe voorkomt u dat de ene klant gegevens van een andere klant kan inzien?"
- "Wat gebeurt er als uw AI-provider zijn prijzen vertienvoudigt of stopt?"
- "Hoe lang zou het duren voordat een nieuwe developer een betekenisvolle wijziging kan doorvoeren?"
- "Wat zou als eerste bezwijken als het gebruik met een factor tien toeneemt?"
- "Wanneer heeft u voor het laatst een back-up succesvol hersteld?"

Eerlijke, specifieke antwoorden zijn veel overtuigender dan indrukwekkende verhalen. "We gebruiken Row Level Security op elke tabel en testen dit met twee accounts per rol in onze CI-pijplijn" is een sterk antwoord. "Supabase regelt onze beveiliging" is dat niet.

## Hoe Bevindingen Zich Vertalen Naar Dealvoorwaarden

Oprichters onderschatten vaak hoe direct technische bevindingen de dealvoorwaarden beïnvloeden. Reviewers classificeren problemen doorgaans op ernst, en elk niveau heeft een voorspelbare consequentie:

| Ernst | Voorbeeld | Typische consequentie |
| --- | --- | --- |
| Kritiek | Klantdata leesbaar over verschillende accounts, productiesleutels blootgesteld | Deal gepauzeerd tot oplossing, of prijsverlaging en specifieke garanties |
| Hoog | Geen back-ups getest, beheerderstoegang zonder MFA, accounts op persoonlijke naam | Opschortende voorwaarden vóór closing, of een deel van de koopprijs in depot (escrow) |
| Gemiddeld | Zwakke tests, verouderde dependencies, ontbrekende documentatie | Verbeterplan na closing, soms een bescheiden prijscorrectie |
| Laag | Codestijl, minimale duplicatie | Opgenomen als opmerking in het rapport, beïnvloedt de voorwaarden zelden |

Het patroon is duidelijk: kritieke en hoge bevindingen zijn kostbaar tijdens onderhandelingen en meestal goedkoop om vooraf op te lossen. Blootgestelde sleutels kunnen in een middag worden geroteerd; datatoegang tussen accounts vergt doorgaans een paar dagen beleidswerk en gerichte tests. Gemiddelde bevindingen worden verwacht bij elk product in een vroege fase en worden meestal afgehandeld met een geloofwaardig plan. Oprichters die aan tafel verschijnen met opgeloste kritieke punten en een gedocumenteerd plan voor de rest, behouden de controle over het gesprek.

## Veelgemaakte Fouten

**Pas beginnen met voorbereiden na de term sheet.** Tegen die tijd beïnvloeden bevindingen direct de prijs en de voorwaarden. Begin zodra de eerste serieuze fondsenwervings- of verkoopgesprekken starten.

**AI-gebruik verbergen.** Reviewers merken het toch aan de codestijl en de commitgeschiedenis. Eerlijk zijn over hoe AI-tools zijn ingezet en hoe de output is gecontroleerd, wekt juist vertrouwen.

**Schaalbaarheid overschatten.** "Het schaalt oneindig omdat het op Supabase draait" nodigt uit tot diepgaande vragen die u wellicht niet kunt beantwoorden. Beschrijf geteste limieten en uw plan voor wanneer die worden bereikt.

**De afhankelijkheid van de oprichter negeren.** Als u de enige persoon bent die het systeem begrijpt, geef dat dan eerlijk toe en toon de documentatie en het wervingsplan die dit oplossen.

## Wat Het Kost

LaunchStudio bereidt door AI gebouwde producten voor op technische due diligence: inventarisatie en scans, oplossingen voor kritieke bevindingen, architectuur- en beveiligingsdocumentatie, een README en overdrachtsnotities, plus een proefreview. Het **Launch Ready**-pakket (€800 - €3.500) dekt de security review, kritieke reparaties en documentatie voor kleinere producten; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, back-ups, monitoring en prioriteitsondersteuning toe voor producten met meer componenten. U ontvangt een vaste offerte na een gesprek van 15 minuten. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een schatting.

## Wie Het Werk Uitvoert

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring, 160+ opgeleverde projecten en 120+ engineers. De engineers van Manifera hebben bestaande codebases beoordeeld en overgenomen voor enterprise-klanten zoals Vodafone en TNO - werk dat sterk overeenkomt met wat een due-diligence-reviewer doet. De cybersecurity-achtergrond van CEO Herre Roelevink, als medeoprichter van wat nu CFLW Cyber Strategies is, bepaalt de focus op beveiliging bij elke review. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; engineers werken vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

Voor een breder overzicht van investeerdersverwachtingen, lees ons artikel over [of u geld kunt ophalen met een door AI gebouwde app](https://launchstudio.eu/nl/blog/can-i-raise-money-with-an-ai-built-app).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De HR-Analysetool Waarvan de Koper 140 Vragen Stuurde

Sophie de Wit bouwde in achttien maanden Verzuimradar in Lovable en Supabase: verzuimanalyse voor Nederlandse werkgevers die ziekteverzuimdata combineert met teamstructuren om patronen te signaleren voor HR en arbodiensten. Met zo'n 60 klanten en stabiele terugkerende inkomsten kreeg ze een overnamebod van een groter HR-softwarebedrijf, onder voorwaarde van technische due diligence.

Het technische team van de koper stuurde een lijst met 140 vragen en wilde binnen twee weken toegang tot de repository. Sophies eigen snelle check was alarmerend. Gevoelige gezondheidsgerelateerde data was beschermd met Row Level Security op de meeste tabellen, maar niet op alle. Drie API-sleutels stonden in oude commits, de hosting- en database-accounts stonden geregistreerd op haar persoonlijke e-mailadres, tests dekten alleen de UI, er was geen architectuurdocumentatie en ze kon niet aangeven welke open-source licenties haar dependencies gebruikten.

LaunchStudio voerde scans uit op secrets, dependencies en licenties, roteerde de blootgestelde sleutels en schoonde de geschiedenis op, en rondde Row Level Security af op de resterende tabellen met tests voor elke rol. Alle accounts werden overgezet naar bedrijfseigendom en het herstellen van back-ups werd getest en gedocumenteerd. Engineers leverden een architectuurdiagram, een beveiligingsoverzicht, een verwerkingsregister, een lijst met bekende problemen met prioriteiten en een repository-README op, en voerden vervolgens een proefreview uit met vragen die vergelijkbaar waren met die van de koper.

**Resultaat:** Sophie beantwoordde alle 140 vragen binnen de deadline, met documenten bijgevoegd. Het rapport van de koper beoordeelde het technische risico als gemiddeld met een duidelijk verbeterplan in plaats van hoog, en de overname werd afgerond zonder prijsverlaging voor technische bevindingen, op basis van de oorspronkelijke voorwaarden.

> *"De engineers van de koper wisten precies waar ze naar moesten zoeken in een door AI gebouwde codebase. Het repareren vóórdat ze keken was veel goedkoper dan achteraf onderhandelen."*
> - **Sophie de Wit, Oprichter, Verzuimradar (Utrecht)**

**Kosten & Doorlooptijd:** €5.400 (Launch & Grow-pakket: scans en secret-rotatie, afronding van RLS, accountoverdrachten, testen van back-ups, documentatieset en proefreview) - afgerond in 12 werkdagen.

## Veelgestelde Vragen

### Wanneer moet ik beginnen met de voorbereiding op technische due diligence?

Begin zodra serieuze gesprekken over fondsenwerving of een overname starten, idealiter nog vóór een term sheet of intentieverklaring (LOI). Bevindingen die aan het licht komen nadat afspraken zijn gemaakt, worden vaak onderhandelingspunten om de waardering te verlagen of voorwaarden te stellen, terwijl dezelfde kwesties vooraf oplossen doorgaans veel minder kost.

### Vinden investeerders het erg dat mijn product met AI-tools is gebouwd?

De meeste investeerders vinden de tools op zichzelf geen probleem. Ze hechten er vooral waarde aan dat het product werkt, veilig is en gemakkelijk kan worden onderhouden. Openheid over het gebruik van AI en laten zien hoe de code is beoordeeld, getest en gedocumenteerd, verandert een mogelijke zorg in het bewijs van een efficiënt bouwproces.

### Wie bezit de code die door AI-tools is gegenereerd?

Het eigendom hangt af van de voorwaarden van elke specifieke tool en van toepasselijke wetgeving, die nog volop in ontwikkeling is. Veel AI-codingtools vermelden in hun voorwaarden dat gebruikers eigenaar zijn van de output, maar controleer altijd de voorwaarden van de gebruikte tools en win juridisch advies in bij omvangrijke transacties. Reviewers zullen hiernaar vragen, dus leg uw standpunt schriftelijk vast.

### Hoe helpt de ervaring van Manifera bij de voorbereiding op due diligence?

Manifera beoordeelt en neemt al meer dan 11 jaar bestaande codebases over voor enterprise-klanten, wat nauw aansluit bij wat due-diligence-reviewers doen. LaunchStudio past dat perspectief toe om precies die punten te vinden en te herstellen die reviewers zouden aanmerken, en documenteert het systeem zodat externe partijen er direct op kunnen vertrouwen.

### Heeft de voorbereiding op due diligence invloed op de zichtbaarheid van mijn bedrijf?

Indirect wel. Dezelfde documentatie die investeerders geruststelt, zoals een publieke beveiligingspagina, een architectuuroverzicht en heldere productinformatie, helpt ook klanten, zoekmachines en AI-antwoordmachines om uw bedrijf beter te begrijpen en te vertrouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer moet ik beginnen met de voorbereiding op technische due diligence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Begin zodra serieuze gesprekken over fondsenwerving of overname starten, idealiter vóór een term sheet of intentieverklaring, omdat bevindingen na afstemming vaak de waardering drukken." }
    },
    {
      "@type": "Question",
      "name": "Vinden investeerders het erg dat mijn product met AI-tools is gebouwd?",
      "acceptedAnswer": { "@type": "Answer", "text": "De meesten geven erom dat het product werkt, veilig en onderhoudbaar is. Openheid over AI-gebruik plus reviews, tests en documentatie maakt er juist een kracht van." }
    },
    {
      "@type": "Question",
      "name": "Wie bezit de code die door AI-tools is gegenereerd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dit hangt af van toolvoorwaarden en wetgeving. Veel tools stellen dat gebruikers eigenaar zijn van output, maar controleer de voorwaarden en vraag juridisch advies bij transacties." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij de voorbereiding op due diligence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera beoordeelt en neemt al 11+ jaar enterprise-codebases over, vergelijkbaar met reviewers, waardoor LaunchStudio tijdig herstelt wat zij zouden signaleren." }
    },
    {
      "@type": "Question",
      "name": "Heeft de voorbereiding op due diligence invloed op de zichtbaarheid van mijn bedrijf?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect wel. Publieke beveiligings- en productdocumentatie die investeerders overtuigt, helpt ook klanten en AI-zoekmachines om het bedrijf te vertrouwen." }
    }
  ]
}
</script>
