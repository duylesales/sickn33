---
Titel: "De Europese AI Act Compliance Sprint: Interne Juristen vs. LaunchStudio's Technische Oplossing"
Trefwoorden: EU AI Act compliance sprint, technische naleving AI, model documentatie, bias logging, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Compliance Officers / CTO's / Founders
---

# De Europese AI Act Compliance Sprint: Interne Juristen vs. LaunchStudio's Technische Oplossing

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De Europese AI Act Compliance Sprint: Interne Juristen vs. LaunchStudio's Technische Oplossing",
  "description": "Waarom juridisch advies alleen beleid schrijft, terwijl LaunchStudio de daadwerkelijke logging en technische safeguards bouwt.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-08-84",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/eu-ai-act-compliance-sprint-legal-vs-launchstudio"
  }
}
</script>

De EU AI Act vraagt oprichters niet om een beleidsdocument te schrijven en het daarbij te laten — de wet vraagt om specifieke, verifieerbare technische mogelijkheden: audit-logs die vastleggen hoe een AI-systeem tot een beslissing kwam, mechanismen voor menselijk toezicht die daadwerkelijk kunnen ingrijpen, transparantiemeldingen die op het juiste moment verschijnen, en documentatie die overeenkomt met het systeem zoals het daadwerkelijk in productie draait. Voor AI SaaS-oprichters wier product iets raakt dat lijkt op een "hoogrisico"-toepassing — werving, krediet, onderwijs, biometrische verwerking — is dit geen optioneel papierwerk; het is een harde vereiste met echte handhavingstanden. Dit artikel vergelijkt wat een intern juridisch team realistisch gezien kan leveren met wat een technische compliance-sprint van LaunchStudio levert, en waarom oprichters steeds vaker beide nodig hebben, in de juiste volgorde.

## Wat Interne Juristen Wel (en Niet) Kunnen Bouwen

Een intern juridisch team, of een op compliance gerichte aanwerving, brengt echte en noodzakelijke waarde voor EU AI Act-gereedheid: het interpreteren van welke risicocategorie een product in valt, het opstellen van de vereiste beleidsdocumenten en impactbeoordelingen, het beheren van de regelgevende relatie, en het maken van beoordelingen over ambigue bepalingen naarmate richtlijnen evolueren. Die expertise is niet vervangbaar door engineers, en geen enkele oprichter zou deze moeten overslaan.

Wat interne juridische teams consequent niet kunnen doen — omdat het geen juridische vaardigheid is, maar een engineeringvaardigheid — is het implementeren van de technische vereisten die de wet daadwerkelijk stelt. Een beleidsdocument dat stelt "het systeem registreert alle beslissingen ten behoeve van audits" is niet hetzelfde als een werkende audit-logging-pijplijn die de daadwerkelijke invoer, modelversie en uitvoer van elke AI-beslissing vastlegt in een doorzoekbaar, manipulatiebestendig formaat. Een geschreven beleid voor menselijk toezicht is niet hetzelfde als een functionerende interface waarmee een menselijke beoordelaar daadwerkelijk de uitvoer van een AI-systeem kan zien, begrijpen en overschrijven voordat deze effect heeft. Juridische teams schrijven de vereiste; engineers moeten het ding bouwen dat eraan voldoet. Wanneer deze twee inspanningen niet op elkaar zijn afgestemd, eindigen oprichters met een compliance-map die een systeem beschrijft dat niet daadwerkelijk in de codebase bestaat.

## Waar Deze Kloof een Echt Probleem Wordt

De kloof komt het hardst naar voren bij door AI-builders gegenereerde producten, omdat tools zoals Lovable, Bolt en Cursor optimaliseren voor een werkende featuredemo, niet voor de specifieke logging-, transparantie- en toezichtinfrastructuur die de AI Act vereist. Een wervingsscreeningtool die in een paar weken met een AI-builder is gebouwd, kan foutloos werken voor de eindgebruiker, terwijl er nul auditspoor is van waarom een bepaalde kandidaat zo werd beoordeeld, geen mechanisme voor een menselijke recruiter om een lage score te beoordelen of te overschrijven voordat deze iemand uitfiltert, en geen gebruikersgerichte openbaarmaking dat er überhaupt AI betrokken is bij de beslissing. Niets daarvan is een probleem van juridisch opstellen — het is een ontbrekende engineeringlaag die een beleidsdocument, hoe goed geschreven ook, niet kan vervangen.

Oprichters die volledig leunen op interne juristen voor AI Act-gereedheid ontdekken dit doorgaans op de harde manier: de compliancedocumentatie is grondig en goed onderbouwd, maar een daadwerkelijke technische audit — of die nu zelf geïnitieerd is, door een toezichthouder wordt getriggerd, of voortkomt uit het due-diligenceonderzoek van een enterprise-klant — onthult dat het systeem zelf niet de helft doet van wat de documentatie beweert.

## Wat een Technische Compliance-sprint Daadwerkelijk Bouwt

De engineers van LaunchStudio benaderen EU AI Act-gereedheid als een implementatieprobleem dat moet overeenkomen met wat het juridisch team al heeft vastgesteld als toepasselijke vereisten. Een typische technische compliance-sprint omvat:

1. **Audit-logging-infrastructuur** — het vastleggen van de specifieke invoer, model of modelversie en uitvoer van elke AI-gedreven beslissing, opgeslagen in een formaat dat doorzoekbaar en bestand is tegen stille manipulatie, zodat "we registreren alle beslissingen" een verifieerbaar feit wordt in plaats van een documentatiebewering.

2. **Menselijke toezichtscontroles** — een werkende interface waarmee een geautoriseerde menselijke beoordelaar de aanbeveling van een AI-systeem kan zien voordat deze onomkeerbaar effect heeft, met de mogelijkheid deze te overschrijven, en een registratie van wanneer die overschrijving plaatsvond en door wie.

3. **Gebruikersgerichte transparantiemeldingen** — duidelijke, correct getimede openbaarmakingen dat een persoon interactie heeft met of wordt beoordeeld door een AI-systeem, geïmplementeerd op het daadwerkelijke moment van interactie in plaats van verstopt in een gebruiksvoorwaardendocument dat niemand leest.

4. **Technische documentatie die overeenkomt met het live systeem** — architectuurdiagrammen, dataflow-documentatie en risicobeperkingsbeschrijvingen die zijn gegenereerd vanuit of geverifieerd tegen de daadwerkelijke productiecodebase, niet geïsoleerd daarvan geschreven.

5. **Datagovernance-controles** — ervoor zorgen dat de data die wordt gebruikt om enig modelonderdeel te trainen of fine-tunen voldoet aan de kwaliteits-, herkomst- en biasbeperkingsverwachtingen die de wet stelt voor hoger-risicosystemen.

Dit werk vindt plaats als backend- en infrastructuur-engineering, toegevoegd aan een bestaande AI-builder-frontend — het product dat een oprichter al bij gebruikers heeft gevalideerd, hoeft niet te worden herbouwd om er onderliggend compliant te worden.

## Waarom Deze Twee Inspanningen Samen Moeten Lopen

Geen van beide paden alleen is voldoende. Juridisch werk zonder engineering levert documentatie op die een systeem beschrijft dat niet bestaat. Engineering zonder juridische input loopt het risico de verkeerde controles te bouwen — de verkeerde gebeurtenissen loggen, toezicht op de verkeerde plek implementeren, of missen dat een bepaalde feature daadwerkelijk in een hogere risicocategorie valt dan aangenomen. De oprichters die het snelst en veiligst vooruitgaan, laten beide parallel lopen: juristen bepalen precies wat het technische systeem moet aantonen, en engineers bouwen de specifieke mechanismen die dat aantonen, getoetst aan elkaar in plaats van geïsoleerd ontwikkeld.

## De Praktische Vergelijking

- **Alleen interne juristen**: Levert accurate risicoclassificatie, beleidsdocumenten en impactbeoordelingen op, maar geen werkende audit-logs, toezichtinterfaces of transparantiemechanismen — waardoor een compliancekloof onzichtbaar blijft totdat er daadwerkelijk een technische audit plaatsvindt.
- **Technische sprint van LaunchStudio, afgestemd op de vereisten van de juristen**: Levert de daadwerkelijke audit-logging, toezichtcontroles en transparantiemeldingen als werkende, verifieerbare functies — doorgaans binnen 1-3 weken afhankelijk van de scope — zodat de documentatie en het live systeem eindelijk hetzelfde beschrijven.

## Wat er Daadwerkelijk op het Spel Staat als de Technische Kloof Niet Wordt Gedicht

De gevolgen van een kloof tussen documentatie en systeem zijn niet hypothetisch. Het handhavingskader van de EU AI Act omvat gelaagde boetes die meeschalen met de ernst van de overtreding, waarbij de meest ernstige inbreuken — inclusief het inzetten van een verboden AI-systeem of het niet voldoen aan de verplichtingen voor hoogrisicosystemen — boetes met zich meebrengen die kunnen oplopen tot tientallen miljoenen euro's of een aanzienlijk percentage van de wereldwijde jaaromzet, welke van de twee hoger is. Voor de meeste AI SaaS-oprichters is het meer directe en waarschijnlijke risico niet een boete van een toezichthouder; het is het verliezen van de enterprise-deal zelf. Grote enterprise-klanten, vooral in gereguleerde sectoren zoals financiën, gezondheidszorg en HR-technologie, eisen steeds vaker bewijs van technische AI Act-compliance als voorwaarde voor het contract, niet als een leuke extra — en hun inkoop- en beveiligingsteams zijn specifiek getraind om onderscheid te maken tussen een compliancebeleid en een compliancesysteem. Een oprichter die met alleen het eerste bij dat gesprek verschijnt, in de veronderstelling dat het gelijk stond aan het tweede, verliest niet alleen die ene deal; ze geven een signaal af aan de markt dat hun compliancehouding in bredere zin niet te vertrouwen is, wat een veel moeilijker te herstellen reputatie is dan een gemiste functie of een vertraagde lancering.

De keerzijde werkt net zo sterk in de andere richting. Oprichters die werkende audit-logs, functionerende toezichtcontroles en documentatie die overeenkomt met hun live systeem kunnen aantonen, veranderen wat een compliancerisico had kunnen zijn in een echt concurrentievoordeel — vooral tegenover concurrenten die de wet nog steeds behandelen als een juridische opsteloefening in plaats van een engineeringvereiste.

## Hoe U Prioriteert Wanneer Alles Urgent Aanvoelt

Oprichters die dit voor het eerst meemaken, nemen vaak aan dat elke technische vereiste tegelijkertijd moet worden gebouwd, wat een beheersbare sprint verandert in een overweldigende. Een praktischer aanpak is prioriteren op basis van blootstelling: begin met welke AI-gedreven beslissing dan ook de meest directe, individuele impact heeft op een persoon (een wervingsbeslissing, een kredietgoedkeuring), aangezien dat typisch is waar audit-logging en menselijk toezicht het meest belangrijk zijn en waar het due-diligenceonderzoek van een enterprise-klant het eerst zal kijken. Prioriteer vandaaruit de systemen die al het dichtst bij een live enterprise-deal of -verlenging staan, aangezien dat is waar de technische kloof waarschijnlijk het snelst naar voren komt en de meeste onmiddellijke schade aanricht als deze onaangepakt blijft. Interne tooling met lagere inzet of systemen die zich nog in vroege validatie bevinden, kunnen redelijkerwijs een cyclus wachten, mits juristen deze als lager risico hebben gemarkeerd. Dit soort triage is precies het gesprek dat gezamenlijk tussen juristen en engineering moet plaatsvinden voordat er code wordt geschreven — elk systeem als even urgent behandelen betekent meestal dat het systeem met de hoogste blootstelling niet als eerste de aandacht krijgt die het daadwerkelijk nodig heeft.

## Belangrijkste inzichten

- De EU AI Act vereist werkende technische mogelijkheden — audit-logs, menselijk toezicht, transparantiemeldingen — niet alleen beleidsdocumenten die beoogd gedrag beschrijven.

- Interne juridische teams zijn essentieel voor risicoclassificatie en beleidsopstelling, maar het implementeren van de technische controles die de wet vereist, is een engineeringtaak, geen juridische.

- AI-builder-tools zoals Lovable, Bolt en Cursor bouwen zelden standaard audit-logging, toezichtinterfaces of transparantiemeldingen op, omdat dat geen functies zijn die een demo nodig heeft.

- Een compliancekloof tussen documentatie en het live systeem is vaak onzichtbaar totdat een echte technische audit — zelf geïnitieerd, regulerend, of vanuit het due-diligenceonderzoek van een enterprise-klant — deze blootlegt.

- Juridisch en technisch compliancewerk moet parallel lopen, waarbij elk het andere definieert en verifieert, in plaats van dat juristen documentatie produceren waar engineers nooit tegen implementeren.

## Sluit de Kloof Tussen uw Compliancedocumentatie en uw Daadwerkelijke Systeem

Een goed geschreven AI Act-beleidsdocument is slechts de helft van de vereiste — de andere helft moet daadwerkelijk in uw codebase bestaan.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Met meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO heeft Manifera de audit-logging-, toezicht- en datagovernance-discipline opgebouwd die technische AI Act-gereedheid daadwerkelijk vereist. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Een Wervingsscreeningtool onder Enterprise-audit

Sofia Lindqvist bouwde HireScope AI, een AI-gedreven kandidaat-screeningtool voor recruiters, met **Bolt**. Toen een enterprise HR-klant richting een getekend contract bewoog, vroeg het inkoopteam om bewijs van technische EU AI Act-compliance voor wat duidelijk een hoogrisico-wervingstoepassing was. Sofia's interne juridisch adviseur had al een grondige risicobeoordeling en beleidskader opgesteld — maar toen de technische auditors van de enterprise-klant vroegen om de daadwerkelijke audit-logs en de interface voor menselijk toezicht te zien, bestonden die niet in het product.

Sofia schakelde LaunchStudio in om de kloof te dichten. Het engineeringteam bouwde een audit-logging-pijplijn die de invoer, modelversie en uitvoer van elke screeningsbeslissing vastlegde; implementeerde een dashboard voor menselijk toezicht waarmee recruiters elke AI-gegenereerde kandidaatscore konden beoordelen en overschrijven voordat deze een wervingsbeslissing beïnvloedde; en voegde een duidelijke, correct getimede melding toe die kandidaten informeerde dat AI betrokken was bij hun eerste screening.

**Resultaat:** HireScope AI slaagde bij de eerste herindiening voor de technische compliance-audit van de enterprise-klant, met werkende audit-logs en toezichtcontroles die precies overeenkwamen met wat Sofia's juridisch team al had gedocumenteerd.

**Kosten & Doorlooptijd:** € 5.800 (Enterprise Hardening Pakket) — 12 werkdagen.

---

---

---

## Veelgestelde Vragen

### Hebben we nog steeds interne of externe juridische bijstand nodig als we LaunchStudio inhuren voor technische compliance?

Ja. Juridische bijstand bepaalt uw risicoclassificatie, stelt de vereiste beleidsdocumenten en impactbeoordelingen op, en interpreteert ambigue bepalingen naarmate richtlijnen evolueren — niets daarvan is engineeringwerk. LaunchStudio implementeert de technische systemen die deze juridische vereisten daadwerkelijk waar maken in uw live product.

### Wat telt specifiek als een "hoogrisico"-AI-systeem onder de wet?

Risicoclassificatie hangt af van de specifieke toepassing van uw product en is een juridische bepaling, maar veelvoorkomende hoogrisicocategorieën zijn onder meer AI gebruikt bij werving en arbeidsbeslissingen, krediet- en financiële toegang, onderwijs en examenbeoordeling, en biometrische identificatie. Als uw product een van deze gebieden raakt, is het de moeite waard om technische compliance-gereedheid te onderzoeken, ongeacht uw huidige bedrijfsgrootte.

### Hoe verschilt een technische compliance-sprint van wat onze AI-builder al biedt?

AI-builders zoals Bolt, Lovable en Cursor zijn geoptimaliseerd om een werkende featuredemo op te leveren, niet de specifieke audit-logging-, toezicht- en transparantie-infrastructuur die de wet vereist. Niets van die opzet wordt standaard gegenereerd, omdat een demo het niet nodig heeft — het wordt pas zichtbaar als een kloof zodra compliance daadwerkelijk wordt getest.

### Wat gebeurt er als onze documentatie zegt dat we compliant zijn, maar het systeem komt daar niet mee overeen?

Dit is precies de kloof die naar voren komt bij een echte audit — of die nu zelf geïnitieerd is, regulerend, of afkomstig van het due-diligenceonderzoek van een enterprise-klant. Documentatie die controles beschrijft die niet daadwerkelijk in de codebase bestaan, is een ernstigere bevinding dan helemaal geen documentatie hebben, omdat het suggereert dat de kloof intern niet werd opgemerkt.

### Kan dit werk worden gedaan zonder onze bestaande productfrontend aan te raken?

Ja. Audit-logging, toezichtinterfaces en transparantiemeldingen worden geïmplementeerd als backend-infrastructuur en gerichte UI-toevoegingen bovenop het bestaande product — de kernfrontend die een oprichter al heeft gebouwd en bij gebruikers heeft gevalideerd, hoeft niet te worden herbouwd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hebben we nog steeds interne of externe juridische bijstand nodig als we LaunchStudio inhuren voor technische compliance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Juridische bijstand bepaalt uw risicoclassificatie, stelt de vereiste beleidsdocumenten en impactbeoordelingen op, en interpreteert ambigue bepalingen naarmate richtlijnen evolueren — niets daarvan is engineeringwerk. LaunchStudio implementeert de technische systemen die deze juridische vereisten daadwerkelijk waar maken in uw live product."
      }
    },
    {
      "@type": "Question",
      "name": "Wat telt specifiek als een \"hoogrisico\"-AI-systeem onder de wet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Risicoclassificatie hangt af van de specifieke toepassing van uw product en is een juridische bepaling, maar veelvoorkomende hoogrisicocategorieën zijn onder meer AI gebruikt bij werving en arbeidsbeslissingen, krediet- en financiële toegang, onderwijs en examenbeoordeling, en biometrische identificatie. Als uw product een van deze gebieden raakt, is het de moeite waard om technische compliance-gereedheid te onderzoeken, ongeacht uw huidige bedrijfsgrootte."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verschilt een technische compliance-sprint van wat onze AI-builder al biedt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI-builders zoals Bolt, Lovable en Cursor zijn geoptimaliseerd om een werkende featuredemo op te leveren, niet de specifieke audit-logging-, toezicht- en transparantie-infrastructuur die de wet vereist. Niets van die opzet wordt standaard gegenereerd, omdat een demo het niet nodig heeft — het wordt pas zichtbaar als een kloof zodra compliance daadwerkelijk wordt getest."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als onze documentatie zegt dat we compliant zijn, maar het systeem komt daar niet mee overeen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit is precies de kloof die naar voren komt bij een echte audit — of die nu zelf geïnitieerd is, regulerend, of afkomstig van het due-diligenceonderzoek van een enterprise-klant. Documentatie die controles beschrijft die niet daadwerkelijk in de codebase bestaan, is een ernstigere bevinding dan helemaal geen documentatie hebben, omdat het suggereert dat de kloof intern niet werd opgemerkt."
      }
    },
    {
      "@type": "Question",
      "name": "Kan dit werk worden gedaan zonder onze bestaande productfrontend aan te raken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Audit-logging, toezichtinterfaces en transparantiemeldingen worden geïmplementeerd als backend-infrastructuur en gerichte UI-toevoegingen bovenop het bestaande product — de kernfrontend die een oprichter al heeft gebouwd en bij gebruikers heeft gevalideerd, hoeft niet te worden herbouwd."
      }
    }
  ]
}
</script>
