---
Titel: "AVG-Checklist voor SaaS-Oprichters in Nederland"
Trefwoorden: avg checklist saas, gdpr checklist saas, saas privacy nederland, b2b saas avg, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: SaaS-Oprichter Scale-Up
---

# AVG-Checklist voor SaaS-Oprichters in Nederland

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AVG-Checklist voor SaaS-Oprichters in Nederland",
  "description": "Een AVG-checklist voor B2B SaaS-oprichters in Nederland, met de verdeling tussen verwerkingsverantwoordelijke en verwerker, de documenten waar klanten om vragen, technische maatregelen, subverwerkers en de vragen in een gangbare Nederlandse beveiligingsvragenlijst.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-23",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/gdpr-checklist-for-saas-founders-in-the-netherlands" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 33: Breach notification", "url": "https://gdpr-info.eu/art-33-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

B2B SaaS verandert uw positie onder de AVG op een manier die veel oprichters missen. Wanneer een Nederlands bedrijf uw software gebruikt om zijn klanten, medewerkers of patiënten te beheren, is dat bedrijf de verwerkingsverantwoordelijke voor die gegevens, en bent u de verwerker. Dat ene feit bepaalt welke documenten u nodig heeft, welke vragen u krijgt en wat uw app moet kunnen. Deze AVG-checklist voor SaaS is rond die werkelijkheid opgebouwd.

## Belangrijkste Punten

- **In B2B SaaS bent u meestal zowel verwerkingsverantwoordelijke als verwerker:** verantwoordelijke voor de accountgegevens van uw eigen klanten, verwerker voor de persoonsgegevens die zij in uw product opslaan.
- **Artikel 28 van de AVG vereist een verwerkersovereenkomst** zodra u namens een klant persoonsgegevens verwerkt.
- **Nederlandse zakelijke klanten vragen om een voorspelbaar documentenpakket:** verwerkersovereenkomst, lijst van subverwerkers, beveiligingssamenvatting, privacyverklaring, verwerkingsregister en datalekprocedure.
- **Elk document moet worden ondersteund door een technische maatregel,** vooral scheiding tussen klanten, EU-hosting, auditlogging en verwijdering op organisatieniveau.
- **LaunchStudio implementeert de technische kant** voor doorgaans €2.000-€6.000, zodat uw jurist vanuit juiste feiten kan schrijven.

## Deel 1: Ken Uw Rol

- [ ] **U bent verwerkingsverantwoordelijke** voor de accountgegevens van uw eigen klanten: namen, factuurgegevens, login-e-mails van de mensen die zich aanmelden.
- [ ] **U bent verwerker** voor de data die uw klanten in uw product zetten: hun klanten, medewerkers, patiënten of leden.
- [ ] **Uw providers zijn subverwerkers** wanneer ze de data van uw klanten verwerken: hosting, database, e-mail, foutregistratie, AI-API's.

Schrijf dit één keer op. Elk volgend punt hangt ervan af.

## Deel 2: Documenten Waar Klanten om Vragen

| Document | Waarom klanten erom vragen |
| --- | --- |
| Verwerkersovereenkomst | Wettelijk verplicht wanneer u hun data verwerkt |
| Lijst van subverwerkers | Ze moeten weten wie hun data nog meer raakt |
| Beschrijving van beveiligingsmaatregelen | Artikel 32 vereist passende maatregelen |
| Privacyverklaring | Voor uw eigen rol als verwerkingsverantwoordelijke |
| Verwerkingsregister | In de meeste gevallen verplicht; laat zien dat u uw data kent |
| Datalekprocedure | Zij hebben 72 uur om te melden; u moet hen snel informeren |

- [ ] Een standaard verwerkersovereenkomst die u elke zakelijke klant aanbiedt, idealiter één keer door een jurist bekeken
- [ ] Een openbare of op verzoek beschikbare lijst van subverwerkers met locaties
- [ ] Een samenvatting van beveiligingsmaatregelen van één pagina die u bij vragenlijsten kunt voegen
- [ ] Een privacyverklaring die klopt met wat uw app daadwerkelijk doet
- [ ] Een verwerkingsregister, ook al is het een eenvoudige spreadsheet
- [ ] Een schriftelijke datalekprocedure met wie wat doet in de eerste 24 uur

## Deel 3: Technische Maatregelen

- [ ] **Scheiding tussen klanten.** De ene klant kan nooit de data van een andere klant zien. In Supabase betekent dit volledige Row Level Security gekoppeld aan het lidmaatschap van een organisatie.
- [ ] **Datalocatie in de EU** voor de database, bestandsopslag en back-ups.
- [ ] **Versleuteling** tijdens transport (overal TLS) en in opslag (standaard bij grote beheerde databases).
- [ ] **Toegangscontrole binnen de organisaties van klanten.** Rollen zoals eigenaar, beheerder en lid, zodat een klant kan beperken wie wat ziet.
- [ ] **Auditlogging** van gevoelige acties: exports, verwijderingen, rolwijzigingen.
- [ ] **Back-ups met een geteste terugzetting**, en een bekende hersteltijd.
- [ ] **Tweestapsverificatie** beschikbaar voor gebruikers en verplicht voor uw eigen beheertoegang.
- [ ] **Geheimen op de server**, geen servicesleutels in de frontend.
- [ ] **Verwijdering en export** op zowel gebruikers- als organisatieniveau, ook aan het einde van het contract.

## Deel 4: Subverwerkers

- [ ] Maak een lijst van elke dienst die klantdata ontvangt
- [ ] Noteer per dienst de locatie en het doorgiftemechanisme (EU, adequaatheidsbesluit, Data Privacy Framework, standaardcontractbepalingen)
- [ ] Teken hun verwerkersovereenkomsten
- [ ] Bepaal hoe u klanten informeert wanneer u een nieuwe subverwerker toevoegt
- [ ] Controleer vooral AI-providers op instellingen voor bewaren en trainen

## Deel 5: De Vragenlijsttest

Nederlandse klanten, vooral in de zorg, het onderwijs, de overheid en grotere bedrijven, sturen vaak een beveiligingsvragenlijst voordat ze kopen. U bent er klaar voor wanneer u deze vragen schriftelijk kunt beantwoorden:

1. Waar wordt onze data opgeslagen, en in welke landen zitten uw subverwerkers?
2. Hoe wordt onze data gescheiden van die van andere klanten?
3. Wie in uw bedrijf heeft toegang tot onze data, en hoe wordt dat gelogd?
4. Hoe snel informeert u ons over een datalek?
5. Wat gebeurt er met onze data als we het contract beëindigen?
6. Is uw applicatie op beveiliging beoordeeld, en wanneer?
7. Gebruikt u onze data om AI-modellen te trainen?

Als een antwoord begint met "ik denk", is dat uw volgende taak.

## Deel 6: Doorlopende Gewoonten

- [ ] Bekijk de subverwerkers telkens wanneer u een tool toevoegt
- [ ] Controleer de toegangscontrole opnieuw na grote AI-gegenereerde wijzigingen
- [ ] Voer elk kwartaal een hersteltest uit
- [ ] Werk de beveiligingssamenvatting bij wanneer er iets wezenlijks verandert
- [ ] Houd een eenvoudig logboek bij van privacygerelateerde beslissingen

## Wat Artikel 28 Werkelijk Vereist

Artikel 28 van de AVG beschrijft wat een verwerkersovereenkomst moet bevatten. Wie de lijst kent, kan sjablonen beoordelen en reageren op aanpassingen die klanten voorstellen:

- Het onderwerp, de duur, de aard en het doel van de verwerking
- De soorten persoonsgegevens en de categorieën betrokkenen
- Dat u alleen verwerkt op basis van gedocumenteerde instructies van de klant
- Geheimhoudingsverplichtingen voor mensen met toegang
- Passende beveiligingsmaatregelen, met verwijzing naar artikel 32
- Voorwaarden voor het inschakelen van subverwerkers, inclusief melding van wijzigingen
- Hulp bij verzoeken van betrokkenen en bij de eigen verplichtingen van de klant
- Verwijdering of teruggave van data aan het einde van het contract
- Informatie beschikbaar stellen en audits toestaan

Elk punt heeft een technische tegenhanger in uw app. "Verwijdering aan het einde van het contract" betekent een verwijderfunctie op organisatieniveau. "Hulp bij verzoeken van betrokkenen" betekent dat u de data van één persoon snel kunt vinden en exporteren. "Passende beveiligingsmaatregelen" betekent scheiding tussen klanten, versleuteling, toegangscontrole en logging die echt werken.

## Subverwerkers Beheren in de Praktijk

Uw lijst van subverwerkers is een levend document. Een praktische opzet:

- Een tabel met per dienst het doel, de categorieën data, de locatie en het doorgiftemechanisme
- Een openbare pagina of een document dat op verzoek beschikbaar is
- Een proces om klanten te informeren voordat u een nieuwe subverwerker toevoegt, zoals de meeste overeenkomsten vereisen
- Een controle telkens wanneer u een tool toevoegt, inclusief analytics, foutregistratie en AI-API's

AI-API's verdienen bijzondere aandacht. Als u klantinhoud naar een aanbieder van taalmodellen stuurt, is die aanbieder een subverwerker. Controleer de instellingen voor bewaren en trainen, de datalocatie en de voorwaarden, en maak het bekend.

## Een Beveiligingsvragenlijst Efficiënt Beantwoorden

Nederlandse vragenlijsten verschillen in lengte, maar de meeste vragen vallen in terugkerende thema's. Bereid standaardantwoorden één keer voor:

| Thema | Het voorbereide antwoord omvat |
| --- | --- |
| Hosting en locatie | Providers, regio's, locatie van back-ups |
| Toegangscontrole | Methode van scheiding tussen klanten, rollen, MFA, beheertoegang |
| Versleuteling | Tijdens transport en in opslag |
| Logging en monitoring | Wat wordt gelogd, bewaartermijn, meldingen |
| Incidentbeheer | Detectie, stappen bij een incident, termijnen voor melding |
| Bedrijfscontinuïteit | Back-ups, hersteltests, hersteltijd |
| Ontwikkelpraktijken | Code review, staging, beheer van dependencies |
| Personeel | Wie toegang heeft, geheimhoudingsverklaringen |

Bewaar de antwoorden in één document en werk ze bij als uw opzet verandert. Uw tweede vragenlijst kost dan een uur in plaats van een week.

## Wanneer Klanten Hun Eigen Overeenkomst Sturen

Grotere Nederlandse organisaties sturen vaak hun eigen verwerkersovereenkomst in plaats van de uwe te tekenen. Lees die zorgvuldig op verplichtingen die u niet kunt nakomen, zoals auditrechten met een korte aankondigingstermijn, zeer korte termijnen voor het melden van datalekken of eisen om uitsluitend in Nederland te hosten. Onderhandel over wat onrealistisch is in plaats van beloften te tekenen die u niet kunt waarmaken; de meeste klanten verkiezen een eerlijk gesprek boven een gebroken toezegging later.

## Privacy Inbouwen in Uw Roadmap

Elke nieuwe functie kan nieuwe verwerkingen opleveren. Een lichte gewoonte houdt de documentatie juist: noteer voor elke functie die persoonsgegevens raakt welke data ze gebruikt, waarom, waar die naartoe gaat en hoe lang die blijft. Werk het verwerkingsregister en de lijst van subverwerkers bij in dezelfde pull request die de functie uitrolt. Het kost minuten en voorkomt de verschuiving die vragenlijsten pijnlijk maakt.

## Verzoeken van Betrokkenen in een B2B-Context

Wanneer een persoon vraagt zijn gegevens in te zien, te corrigeren of te verwijderen, kan het verzoek bij u of bij uw klant terechtkomen. Onder een verwerkersovereenkomst helpt u meestal de klant in plaats van zelf te beslissen. Bouw de tools die die hulp snel maken: een beheerzoekfunctie die binnen een organisatie alle records vindt die aan een e-mailadres zijn gekoppeld, een export van de gegevens van die persoon in een leesbaar formaat, en een functie voor verwijderen of anonimiseren die rekening houdt met records die uw klant moet bewaren. Log elk verzoek en de genomen actie. Wanneer een klant vraagt "hoe zou u ons helpen bij een inzageverzoek?", overtuigt een korte demonstratie veel meer dan een alinea in een contract.

## Een Realistische Planning

Voor een gangbare AI-gebouwde B2B SaaS duurt het twee tot vier weken om van "geen documentatie" naar "klaar voor vragenlijsten" te gaan: één tot twee weken voor technische maatregelen zoals scheiding tussen klanten, EU-hosting, logging en verwijdering, en parallel één tot twee weken voor uw jurist om de verwerkersovereenkomst en privacyverklaring op basis van juiste feiten af te ronden. Beginnen voordat uw eerste grote prospect erom vraagt, spaart het geduld van die prospect.

## Waar LaunchStudio Past

LaunchStudio dekt deel 3 en de technische input voor deel 2 en 4: scheiding tussen klanten, EU-hosting, auditlogs, verwijdering en export, en een gedocumenteerd overzicht van waar data naartoe gaat. Dat geeft uw jurist of privacyadviseur juiste feiten om mee te werken, en geeft u duidelijke antwoorden voor vragenlijsten. Gangbare opdrachten liggen tussen €2.000 en €6.000 tegen een vaste prijs. Voor oprichters die nog vroeg in het proces zitten, is onze bredere gids over een [AVG-proof app](https://launchstudio.eu/nl/blog/gdpr-proof-app-netherlands-avg-for-ai-built-products) een goed beginpunt.

LaunchStudio wordt aangedreven door Manifera, waarvan het engineeringteam van 120+ mensen werkt vanuit Ho Chi Minh City met klantkantoren in Amsterdam en Singapore, en tot de klanten behoren Nederlandse organisaties zoals TNO en Statler BI. De [aanpak voor offshore-ontwikkeling van Manifera](https://www.manifera.com/services/offshore-software-development/) is gebouwd rond Nederlandse contracten en gegevensverwerking in de EU. Voor officiële sjablonen en richtlijnen is de [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) de gezaghebbende bron.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Recruitment-SaaS Die Vastliep bij Inkoop

Hanna Vos, voormalig recruiter in Amsterdam, bouwde Vacaturely met Cursor: een applicant tracking-tool voor kleine en middelgrote Nederlandse werkgevers, met vacaturepagina's, kandidatenpijplijnen en het plannen van gesprekken. Vijf kleine bedrijven gebruikten het tevreden. Toen wilde een zorggroep met 1.200 medewerkers tekenen, en de privacyfunctionaris stuurde een vragenlijst van 60 vragen en een verzoek om een verwerkersovereenkomst.

Hanna had geen van beide. Bij het doorlopen van de checklist ontdekte ze dat haar app klanten scheidde via applicatiecode, niet via databasepolicies, en dat één export-endpoint de controle oversloeg. Cv's van kandidaten stonden in een bucket met langdurig geldige openbare links. Haar e-mailprovider, foutregistratie en een AI-functie voor cv-samenvattingen waren allemaal subverwerkers die ze nooit had vermeld. Een klantorganisatie verwijderen liet de gegevens van kandidaten achter.

LaunchStudio verplaatste de scheiding tussen klanten naar Row Level Security met organisatielidmaatschap, repareerde het export-endpoint, maakte de opslag van cv's privé met kortlevende ondertekende URL's, voegde auditlogging toe voor exports en verwijderingen, bouwde verwijdering op organisatieniveau aan het einde van het contract en richtte de AI-provider in onder een verwerkersovereenkomst met training uitgeschakeld. Engineers maakten een lijst van subverwerkers met locaties en een samenvatting van de beveiligingsmaatregelen. De jurist van Hanna stelde de verwerkersovereenkomst op aan de hand van die feiten.

**Resultaat:** De privacyfunctionaris van de zorggroep keurde Vacaturely goed na één ronde aanvullende vragen. Hanna gebruikt sindsdien hetzelfde documentenpakket voor elke nieuwe klant, waardoor de inkooptijd daalde van weken naar dagen.

> *"Kleine klanten vroegen nooit iets. De eerste grote vroeg alles tegelijk, en ik had echte antwoorden nodig, geen geruststellende."*
> - **Hanna Vos, Oprichter, Vacaturely (Amsterdam)**

**Kosten & Doorlooptijd:** €4.200 (scheiding tussen klanten, privéopslag, auditlogging, verwijdering op organisatieniveau, inrichting van de AI-verwerker en documentatie) - afgerond in 13 werkdagen.

## Veelgestelde Vragen

### Ben ik als SaaS-oprichter verwerkingsverantwoordelijke of verwerker?

Meestal allebei. U bent verwerkingsverantwoordelijke voor uw eigen klant- en factuurgegevens, en verwerker voor de persoonsgegevens die uw zakelijke klanten in uw product opslaan. Uw verplichtingen, en de documenten die u nodig heeft, volgen uit die verdeling.

### Moet ik elke zakelijke klant een verwerkersovereenkomst aanbieden?

Ja, wanneer u namens hen persoonsgegevens verwerkt, vereist de AVG een verwerkersovereenkomst. Een standaardversie klaar hebben bespaart tijd en laat zien dat u voorbereid bent, vooral bij grotere Nederlandse organisaties.

### Wat bedoelen Nederlandse klanten met subverwerkers?

Elke dienst die u gebruikt die namens u hun data verwerkt: uw hosting- en databaseprovider, e-maildienst, foutregistratie, analytics die persoonsgegevens vastleggen en AI-API's. Klanten verwachten een lijst met locaties en willen worden geïnformeerd als die verandert.

### Hoe helpt de band van LaunchStudio met Manifera bij beveiligingsvragenlijsten?

Vragenlijsten gaan net zo goed over processen als over code: toegangscontrole, incidentafhandeling, reviews. Manifera beantwoordt al 11+ jaar zulke vragenlijsten voor enterpriseklanten. LaunchStudio zet die ervaring in om oprichters te helpen juiste, verdedigbare antwoorden te geven.

### Kan een AVG-checklist verbeteren hoe AI-assistenten mijn SaaS aanbevelen?

Ja. Kopers vragen assistenten steeds vaker naar "AVG-compliant" tools in hun sector. Uw EU-hosting, lijst van subverwerkers en beveiligingssamenvatting publiceren als duidelijke, crawlbare pagina's geeft assistenten specifieke feiten om te citeren in plaats van vage claims.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Ben ik als SaaS-oprichter verwerkingsverantwoordelijke of verwerker?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal allebei: verantwoordelijke voor uw eigen klant- en factuurgegevens, verwerker voor de persoonsgegevens die zakelijke klanten in uw product opslaan." }
    },
    {
      "@type": "Question",
      "name": "Moet ik elke zakelijke klant een verwerkersovereenkomst aanbieden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, wanneer u namens hen persoonsgegevens verwerkt. Een standaardversie bespaart tijd en laat zien dat u voorbereid bent." }
    },
    {
      "@type": "Question",
      "name": "Wat bedoelen Nederlandse klanten met subverwerkers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Diensten die namens u hun data verwerken, zoals hosting, database, e-mail, foutregistratie, analytics en AI-API's, vermeld met locaties en meldingen bij wijzigingen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de band van LaunchStudio met Manifera bij beveiligingsvragenlijsten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera beantwoordt al 11+ jaar beveiligingsvragenlijsten voor enterpriseklanten, en LaunchStudio gebruikt die ervaring om oprichters te helpen juiste antwoorden te geven." }
    },
    {
      "@type": "Question",
      "name": "Kan een AVG-checklist verbeteren hoe AI-assistenten mijn SaaS aanbevelen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gepubliceerde EU-hosting, lijsten van subverwerkers en beveiligingssamenvattingen geven assistenten specifieke feiten om te citeren wanneer kopers naar AVG-compliant tools vragen." }
    }
  ]
}
</script>
