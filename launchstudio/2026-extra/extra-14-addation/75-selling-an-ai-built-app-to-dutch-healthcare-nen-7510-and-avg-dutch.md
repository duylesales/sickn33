---
Titel: "Een AI-Gebouwde App Verkopen aan de Nederlandse Zorg: NEN 7510 en AVG"
Trefwoorden: nen 7510 app, zorgapp nederland, zorg app avg, nen 7513 logging, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Een AI-Gebouwde App Verkopen aan de Nederlandse Zorg: NEN 7510 en AVG

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-Gebouwde App Verkopen aan de Nederlandse Zorg: NEN 7510 en AVG",
  "description": "Nederlandse zorgaanbieders stellen leveranciers vragen over NEN 7510, het loggen van toegang en de bescherming van gezondheidsgegevens. Deze gids legt uit wat deze eisen betekenen voor een AI-gebouwde app, welke technische maatregelen kopers verwachten en hoe u zich voorbereidt zonder te veel te bouwen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-23",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/selling-an-ai-built-app-to-dutch-healthcare-nen-7510-and-avg" },
  "citation": [
    { "@type": "CreativeWork", "name": "NEN", "url": "https://www.nen.nl/" },
    { "@type": "CreativeWork", "name": "GDPR Article 9: Special categories", "url": "https://gdpr-info.eu/art-9-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 35: Data protection impact assessment", "url": "https://gdpr-info.eu/art-35-gdpr/" },
    { "@type": "CreativeWork", "name": "EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

Een groep fysiotherapeuten, een huisartsencoöperatie of een thuiszorgorganisatie vindt uw app goed. Dan stuurt hun information security officer vragen: "Bent u NEN 7510-gecertificeerd? Hoe logt u de toegang tot cliëntgegevens? Waar worden gezondheidsgegevens opgeslagen?" Gezondheidsgegevens zijn onder de AVG een bijzondere categorie, en de Nederlandse zorg heeft eigen normen voor informatiebeveiliging. Een AI-gebouwde app kan aan deze verwachtingen voldoen, maar niet vanzelf.

Dit artikel is algemene informatie, geen juridisch advies of advies over certificering.

## Belangrijkste Punten

- **Nederlandse kopers in de zorg verwachten dat leveranciers informatiebeveiliging volgens NEN 7510,** het loggen van toegang volgens NEN 7513 en de strengere AVG-regels voor gezondheidsgegevens ondersteunen.
- **Gezondheidsgegevens zijn een bijzondere categorie onder artikel 9 van de AVG,** waarvoor een aanvullende wettelijke grondslag en passende waarborgen nodig zijn.
- **Certificering is in het begin niet altijd vereist;** veel kopers accepteren gedocumenteerde maatregelen en een geloofwaardige roadmap, maar vraag het vroeg na.
- **Technische essentie:** strikte toegang op basis van need-to-know, logs van toegang die niet te manipuleren zijn, hosting in de EU, versleuteling, MFA en zorgvuldige verwerking met AI.
- **Dit is algemene informatie;** raadpleeg specialisten voor vragen over certificering en juridische vragen.

## De Normen waar U over Hoort

| Norm | Wat die dekt |
| --- | --- |
| NEN 7510 | Beheer van informatiebeveiliging in de zorg, gebaseerd op ISO 27001 met maatregelen specifiek voor de zorg |
| NEN 7512 | Vertrouwensbasis voor de elektronische uitwisseling van gezondheidsgegevens |
| NEN 7513 | Het loggen van handelingen in elektronische patiëntdossiers: wie heeft wat ingezien, en wanneer |
| AVG | Gezondheidsgegevens als bijzondere categorie: strengere voorwaarden en waarborgen |

Zorgaanbieders zijn verantwoordelijk voor de naleving van deze normen in hun eigen organisatie. Daarom verwachten ze dat leveranciers hen daarbij ondersteunen, soms met een certificering, vaak met aantoonbare maatregelen.

## Certificering Versus Aantoonbare Maatregelen

Volledige certificering voor NEN 7510 of ISO 27001 is een managementsysteem voor de hele organisatie, met audits en doorlopende inspanning. Voor een jong bedrijf kan dat een doel zijn in plaats van een startpunt. Veel kopers in de zorg accepteren een geloofwaardig traject: gedocumenteerde maatregelen, een beveiligingsbeleid, verwerkersovereenkomsten en bewijs van technische maatregelen, soms gecombineerd met een tijdlijn richting certificering. Vraag uw koper wat die vereist.

## Technische Maatregelen die Kopers Verwachten

- **Strikte toegangscontrole:** zorgprofessionals zien alleen cliënten bij wie ze betrokken zijn; beheerders zijn beperkt en worden gelogd
- **Het loggen van toegang in de geest van NEN 7513:** wie welk cliëntdossier heeft ingezien of gewijzigd, wanneer en vanaf waar, bewaard en controleerbaar
- **Hosting in de EU** van alle gezondheidsgegevens, inclusief back-ups en bestanden
- **Versleuteling** tijdens transport en in opslag
- **Sterke authenticatie:** tweestapsverificatie voor professionals
- **Dataminimalisatie:** verzamel alleen wat het zorgproces nodig heeft; wees voorzichtig met BSN's, waarvoor in de zorg specifieke wettelijke regels gelden
- **Een incidentprocedure** met snelle melding aan de zorgaanbieder
- **Een verwerkersovereenkomst** die aansluit bij de verwachtingen in de zorg
- **AI-functies zorgvuldig afgehandeld:** als gezondheidsgegevens naar een AI-model gaan, vragen de provider, de locatie, de bewaartermijn en de wettelijke grondslag extra aandacht

## AI-Gebouwde Apps: De Gebruikelijke Gaten

Gangbare Lovable- of Bolt-apps in zorgpilots missen het loggen van toegang, gebruiken ruime toegangspolicies, bewaren bestanden in openbare buckets, draaien in regio's buiten de EU en sturen gegevens zonder afspraken naar AI-API's. Elk van deze punten is op te lossen; samen maken ze het onmogelijk om een vragenlijst te doorstaan.

## Voorbereiden Zonder te Veel te Bouwen

1. Vraag de koper welke normen en welk bewijs die vereist
2. Regel eerst de technische maatregelen: toegang, logging, MFA, hosting in de EU, versleuteling, back-ups
3. Schrijf een beknopt beveiligingsbeleid en een incidentprocedure
4. Bereid een verwerkersovereenkomst en een lijst van subverwerkers voor
5. Overweeg een onafhankelijke auditsamenvatting; zie onze [pagina over de audit van AI-gegenereerde code](https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers)
6. Plan certificering wanneer de businesscase die ondersteunt

## Het Nederlandse Zorglandschap voor Softwareleveranciers

Zorg in Nederland wordt geleverd door een breed scala aan organisaties: huisartsenpraktijken en -coöperaties, fysiotherapeuten, thuiszorgorganisaties, aanbieders van ggz, ziekenhuizen en gespecialiseerde klinieken. Elk van hen is verantwoordelijk voor de bescherming van patiëntgegevens en moet ervoor zorgen dat leveranciers hetzelfde doen. Informatiebeveiliging in de Nederlandse zorg wordt bepaald door de NEN 7510-reeks, de AVG en sectorspecifieke wetten. Voor een softwareoprichter betekent dit dat het verkoopproces een zorgvuldige beoordeling bevat van hoe uw product met gegevens omgaat, vaak door een information security officer of privacy officer.

## NEN 7510, 7512 en 7513 in Gewone Taal

NEN 7510 is de Nederlandse norm voor het beheer van informatiebeveiliging in de zorg, gebaseerd op de internationale norm ISO 27001 met aanvullende maatregelen specifiek voor de zorg. Die omvat beleid, risicobeheer, toegangscontrole, de afhandeling van incidenten, het beheer van leveranciers en meer, verspreid over een organisatie. NEN 7512 gaat over vertrouwen bij elektronische gegevensuitwisseling tussen partijen in de zorg, waaronder authenticatie en integriteit. NEN 7513 gaat over logging: vastleggen wie welk elektronisch patiëntdossier heeft ingezien of gewijzigd, wanneer en in welke hoedanigheid, zodat toegang achteraf kan worden gecontroleerd. NEN, het Nederlandse normalisatie-instituut, publiceert deze normen.

## Gezondheidsgegevens onder de AVG

De AVG behandelt gegevens over gezondheid als een bijzondere categorie onder artikel 9. Verwerking ervan is verboden, tenzij een uitzondering geldt, zoals het verlenen van zorg onder de verantwoordelijkheid van een professional met een geheimhoudingsplicht, of uitdrukkelijke toestemming. De beveiligingseisen van artikel 32 wegen extra zwaar, omdat het risico voor personen groter is. Voor veel apps rond gezondheid is een gegevensbeschermingseffectbeoordeling (DPIA) onder artikel 35 verplicht of sterk aan te raden. Als leverancier bent u meestal verwerker namens de zorgaanbieder, die verwerkingsverantwoordelijke blijft.

## Toegangscontrole Ontwerpen voor de Zorg

Toegangscontrole in de zorg volgt het principe van need-to-know: een professional mag alleen bij de gegevens van een patiënt wanneer die bij de zorg voor die patiënt betrokken is. In de praktijk betekent dat:

- Cliënten of patiënten koppelen aan zorgteams of behandelrelaties
- Row Level Security-policies schrijven die die relaties controleren, niet alleen het lidmaatschap van de organisatie
- Administratieve rollen scheiden van zorginhoudelijke rollen
- Een procedure voor noodtoegang bieden die wordt gelogd en achteraf wordt beoordeeld
- MFA vereisen voor alle professionals en medewerkers

Algemene modellen waarin "iedereen in de organisatie alles ziet", die in AI-gegenereerde apps vaak voorkomen, stellen kopers in de zorg zelden tevreden.

## Logging in de Stijl van NEN 7513 Bouwen

Een log van toegang in de zorg hoort de gebruiker, diens rol, de patiënt of het ingeziene dossier, het type handeling, het tijdstip en bij voorkeur de context vast te leggen. Het moet beschermd zijn tegen wijziging door gewone gebruikers, voor een afgesproken periode worden bewaard en controleerbaar zijn voor de zorgorganisatie, bijvoorbeeld via een export of een speciaal scherm. In een Supabase-app kan dit worden geïmplementeerd met logging in serverfuncties of databasetriggers die schrijven naar een tabel die alleen bevoorrechte rollen kunnen lezen. Ontwerp het log zo dat het bruikbaar is: bij het bekijken ervan moet de vraag "wie heeft vorige maand het dossier van deze patiënt ingezien, en waarom?" te beantwoorden zijn.

## AI-Functies met Gezondheidsgegevens

AI-functies zoals het samenvatten van notities of het opstellen van brieven zijn aantrekkelijk in de zorg en vragen extra zorgvuldigheid. Controleer de verwerkersvoorwaarden, de bewaartermijn, de instellingen voor training en de locatie van gegevens van de AI-provider; minimaliseer wat u verstuurt door waar mogelijk identificerende gegevens te verwijderen; zorg dat een professional de uitvoer van de AI beoordeelt voordat die invloed heeft op de zorg; en wees transparant tegenover de zorgorganisatie. De Europese AI-verordening classificeert bovendien sommige toepassingen van AI in de zorg als hoog risico, met aanvullende verplichtingen; controleer of uw functie in die categorieën valt.

## Voorbereiden op het Verkoopproces

Bereid vóór uw eerste verkoopgesprek in de zorg een pakket over beveiliging en privacy voor: een beschrijving van technische en organisatorische maatregelen, het ontwerp van toegangscontrole en logging, hosting en de lijst van subverwerkers, de incidentprocedure, de verwerkersovereenkomst, eventuele samenvattingen van audits of penetratietests en uw roadmap richting certificering als dat van toepassing is. Kopers in de zorg waarderen leveranciers die voorbereid binnenkomen, en het verkort de inkoop aanzienlijk.

## Een Roadmap Richting Certificering

Voor veel jonge leveranciers werkt een gefaseerde roadmap: implementeer eerst de technische maatregelen en documenteer het beleid; voer daarna een interne risicoanalyse en een onafhankelijke technische audit uit; formaliseer vervolgens een managementsysteem voor informatiebeveiliging dat mensen, processen en leveranciers omvat; en ga ten slotte voor certificering voor ISO 27001 of NEN 7510 bij een geaccrediteerde instelling wanneer de vraag van klanten de investering rechtvaardigt. Door deze roadmap met kopers in de zorg te delen, laat u ook vóór certificering zien dat u het serieus neemt.

## Veelgemaakte Fouten

- Elke professional in een organisatie toegang geven tot elke patiënt
- Toegang loggen in een tabel die gebruikers kunnen wijzigen
- Gezondheidsgegevens buiten de EU hosten zonder zorgvuldige beoordeling
- Patiëntgegevens naar AI-providers sturen zonder afspraken en minimalisatie
- Tijdlijnen voor certificering beloven die u niet kunt waarmaken
- De verwerkersovereenkomst als formaliteit behandelen in plaats van als beschrijving van echte maatregelen

## Vragen die Kopers in de Zorg Stellen

Reken op vragen zoals: hoe is de toegang beperkt tot betrokken professionals? Hoe wordt toegang gelogd en hoe kunnen wij dat controleren? Waar worden gegevens gehost? Wie in uw bedrijf heeft toegang tot patiëntgegevens? Hoe handelt u incidenten af en hoe snel worden wij geïnformeerd? Gebruikt u AI, en hoe? Welke certificeringen heeft of plant u? Bereid vooraf schriftelijke antwoorden voor en houd die actueel.

## Samenvatting

Verkopen aan de Nederlandse zorg is haalbaar voor AI-gebouwde producten wanneer toegangscontrole, logging, hosting, beveiliging en documentatie aan de verwachtingen in de zorg voldoen. Begin met de technische basis, documenteer die duidelijk en groei richting certificering naarmate uw klanten daarom vragen.

## Waar U Vandaag Begint

Teken uw toegangsmodel op papier: welke rollen er zijn, welke patiënten elke rol mag zien en hoe die relatie in uw database wordt vastgelegd. Is het antwoord "iedereen in de organisatie ziet alles", dan is dat uw eerste wijziging. Voeg daarna een log van toegang toe voor patiëntdossiers.

## Gerelateerde Onderwerpen

Onze gidsen over AVG-proof apps in Nederland, tweestapsverificatie, rollen en beheerpanelen, en bewaartermijnen voor Nederlandse SaaS behandelen de bouwstenen die kopers in de zorg het nauwkeurigst bekijken.

## De Opbrengst

Klanten in de zorg blijven meestal trouw zodra een tool is goedgekeurd en in hun processen is ingebed. Aan hun beveiligingsverwachtingen voldoen is veeleisend, maar het opent een markt waarin goed voorbereide leveranciers minder concurrentie en langere klantrelaties hebben.

## In het Kort

Toegang op basis van need-to-know, logging die niet te manipuleren is, hosting in de EU, MFA, zorgvuldig gebruik van AI en eerlijke documentatie vormen de basis waar elke Nederlandse koper in de zorg naar zoekt.

## Een Praktische Tip

Vraag uw eerste klant in de zorg om de leveranciersvragenlijst vroeg te delen, vóór de pilot, zodat u gaten kunt dichten terwijl de relatie nog warm is.

## De Technische Kant Laten Voorbereiden

LaunchStudio implementeert toegangscontrole, het loggen van toegang, MFA, hosting in de EU en documentatie voor AI-gebouwde apps in de zorg, meestal €3.500-€7.500 tegen vaste prijs, afhankelijk van de omvang. Anders dan freelancers wordt LaunchStudio ondersteund door Manifera, vertrouwd door TNO en CFLW, waarvan oprichter Herre Roelevink een achtergrond in cybersecurity heeft; zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). [De website van NEN](https://www.nen.nl/) beschrijft de normen voor informatiebeveiliging in de zorg.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Thuiszorg-App met een Lijst van 40 Vragen

Wendy Koster, voormalig wijkverpleegkundige, bouwde Zorgdagboek in Lovable: thuiszorgmedewerkers leggen op hun telefoon bezoeknotities, observaties over medicatie en berichten aan familie vast. Een thuiszorgorganisatie met 300 medewerkers in Overijssel wilde een pilot. Hun information security officer stuurde 40 vragen met verwijzingen naar NEN 7510 en NEN 7513.

De app van Wendy kon er maar weinig beantwoorden. Elke zorgmedewerker kon de notities van elke cliënt lezen. Er werd niet vastgelegd wie wat had ingezien. De database draaide buiten de EU. Inloggen had geen tweede factor. En notities werden zonder enige overeenkomst naar een AI-API gestuurd voor samenvattingen.

LaunchStudio beperkte de toegang tot cliënten die aan het team van elke medewerker zijn toegewezen, voegde een tabel voor het loggen van toegang toe die elke inzage en wijziging van cliëntdossiers vastlegt met gebruiker, tijdstip en handeling, bouwde een controlescherm voor de privacy officer van de organisatie, migreerde naar een EU-regio, verplichtte MFA voor alle medewerkers, verwijderde identificerende gegevens van cliënten vóór het samenvatten met AI onder een verwerkersovereenkomst met training uitgeschakeld, en schreef een document met beveiligingsmaatregelen en een incidentprocedure.

**Resultaat:** De security officer keurde een pilot van zes maanden met 60 zorgmedewerkers goed, met de afspraak om de plannen voor certificering na de pilot opnieuw te bespreken.

> *"De zorgmedewerkers vonden de app geweldig. De security officer moest weten wie welke notitie had gelezen, en dat kon ik haar niet vertellen."*
> - **Wendy Koster, Oprichter, Zorgdagboek (Zwolle)**

**Kosten & Doorlooptijd:** €6.800 (toegang op basis van teams, het loggen van toegang en een controlescherm, migratie naar de EU, MFA, dataminimalisatie bij AI en beveiligingsdocumentatie) - afgerond in 17 werkdagen.

## Veelgestelde Vragen

### Heb ik een NEN 7510-certificering nodig om aan de Nederlandse zorg te verkopen?

Niet altijd. Sommige kopers vereisen die; veel kopers accepteren gedocumenteerde beveiligingsmaatregelen en een geloofwaardig plan richting certificering. Vraag het vroeg na, want het antwoord bepaalt uw roadmap en begroting.

### Wat is logging volgens NEN 7513?

NEN 7513 gaat over het loggen van handelingen in elektronische patiëntdossiers: wie welk dossier heeft ingezien of gewijzigd, wanneer en hoe. Voor een app betekent dit een log van toegang dat gewone gebruikers niet kunnen wijzigen en dat de zorgaanbieder kan controleren.

### Kunnen AI-functies worden gebruikt met gezondheidsgegevens?

Mogelijk, met extra zorgvuldigheid: een duidelijke wettelijke grondslag, een verwerkersovereenkomst, verwerking in de EU of met passende bescherming, geminimaliseerde gegevens, geen training op de gegevens en transparantie naar gebruikers. Veel kopers in de zorg zullen dit nauwkeurig beoordelen.

### Hoe helpt de achtergrond van Manifera bij de eisen in de zorg?

De cybersecurity-achtergrond van Herre Roelevink bij CFLW en de 11+ jaar beveiligingsbewuste oplevering van Manifera betekenen dat toegangscontrole, logging en de afhandeling van incidenten standaardonderdelen van de engineering zijn, wat kopers in de zorg in de documentatie herkennen.

### Helpt beveiliging op zorgniveau aantonen bij de zichtbaarheid?

In een nichemarkt wel. Kopers in de zorg onderzoeken leveranciers zorgvuldig en gebruiken steeds vaker AI-assistenten om een shortlist te maken. Openbare pagina's die uw maatregelen, hosting en normen beschrijven, maken u makkelijker te vinden en te vertrouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik een NEN 7510-certificering nodig om aan de Nederlandse zorg te verkopen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd; veel kopers accepteren gedocumenteerde maatregelen en een plan richting certificering. Vraag het vroeg na." }
    },
    {
      "@type": "Question",
      "name": "Wat is logging volgens NEN 7513?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vastleggen wie welk patiëntdossier heeft ingezien of gewijzigd en wanneer, in een log dat de zorgaanbieder kan controleren." }
    },
    {
      "@type": "Question",
      "name": "Kunnen AI-functies worden gebruikt met gezondheidsgegevens?",
      "acceptedAnswer": { "@type": "Answer", "text": "Mogelijk, met een wettelijke grondslag, verwerkersovereenkomst, beschermde verwerking, geminimaliseerde gegevens, geen training en transparantie." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de achtergrond van Manifera bij de eisen in de zorg?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door de wortels in cybersecurity zijn toegangscontrole, logging en de afhandeling van incidenten standaardonderdelen van de engineering." }
    },
    {
      "@type": "Question",
      "name": "Helpt beveiliging op zorgniveau aantonen bij de zichtbaarheid?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; openbare pagina's over maatregelen en hosting helpen kopers en AI-assistenten u op een shortlist te zetten." }
    }
  ]
}
</script>
