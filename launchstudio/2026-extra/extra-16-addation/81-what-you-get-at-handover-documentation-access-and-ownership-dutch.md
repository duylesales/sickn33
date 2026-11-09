---
Titel: "Wat U Ontvangt bij de Overdracht: Documentatie, Toegang en Eigendom"
Trefwoorden: overdrachtsdocumentatie project, checklist overdracht software, wat ontvangen van ontwikkelaar, eigendom code na project, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Wat U Ontvangt bij de Overdracht: Documentatie, Toegang en Eigendom

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat U Ontvangt bij de Overdracht: Documentatie, Toegang en Eigendom",
  "description": "Een uitleg van wat oprichters ontvangen aan het einde van een LaunchStudio-project voor een app gebouwd met Lovable, Bolt, v0, Cursor of Claude Code: eigendom van code en accounts, een overzicht van accounts, een schriftelijke samenvatting, documentatie van architectuur en gegevens, procedures voor releases, rollback en herstel, projectinstructies voor AI-tools, tests, monitoring, het intrekken van toegang en hoe u het overdrachtspakket gebruikt met toekomstige ontwikkelaars, klanten en investeerders.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-15",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-you-get-at-handover-documentation-access-and-ownership" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: Transferring a repository", "url": "https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository" },
    { "@type": "CreativeWork", "name": "Anthropic: Claude Code memory and project instructions", "url": "https://docs.anthropic.com/en/docs/claude-code/memory" },
    { "@type": "CreativeWork", "name": "Cursor: Rules", "url": "https://docs.cursor.com/context/rules" },
    { "@type": "CreativeWork", "name": "Diátaxis: A systematic approach to technical documentation", "url": "https://diataxis.fr/" }
  ]
}
</script>

Aan het einde van een softwareproject ontdekken veel oprichters wat ze eigenlijk hebben gekocht. Sommigen ontvangen een werkende app en een goed georganiseerde set documenten waarmee zij, of iemand anders, met vertrouwen verder kunnen. Anderen ontvangen een link, een paar wachtwoorden in een e-mail en een leverancier die als enige begrijpt hoe alles werkt. Het verschil wordt maanden later zichtbaar: wanneer er iets kapotgaat, wanneer een nieuwe ontwikkelaar begint, wanneer een investeerder om due diligence vraagt of wanneer een klant een beveiligingsvragenlijst stuurt.

Bij LaunchStudio is de overdracht een vastgesteld onderdeel van elk Launch Ready- en Launch & Grow-project. Deze pagina legt precies uit wat u ontvangt, waarom elk onderdeel telt en hoe u het gebruikt nadat wij klaar zijn.

## Belangrijkste Punten

- **Alles is van u:** code, accounts, gegevens en domein staan op naam van uw bedrijf.
- **Een overzicht van accounts** vermeldt elke dienst, wie de eigenaar is en wie toegang heeft.
- **Een schriftelijke samenvatting** legt uit wat is beoordeeld, gerepareerd en nog openstaat.
- **Procedures** voor releases, rollback en herstel laten u handelen zonder ons.
- **Projectinstructies voor uw AI-tool** houden toekomstige wijzigingen in lijn met het uitgevoerde werk.

## Eigendom: Aan het Einde Niets Over te Dragen

We werken vanaf het begin in uw accounts: uw repository, uw hosting, uw database, uw betaal- en e-mailproviders, uw domein. Als accounts op naam van iemand anders stonden, zoals een voormalige freelancer, het persoonlijke account van een medeoprichter of een bureau, brengen we ze tijdens het project onder het eigendom van uw bedrijf. Bij de overdracht valt er niets meer over te dragen, omdat alles al van u was. Dat is de belangrijkste eigenschap van een goede overdracht, en degene die oprichters het vaakst over het hoofd zien tot het te laat is.

## Het Overzicht van Accounts

Het overzicht van accounts is één document met elke dienst waarvan de app afhankelijk is:

| Kolom | Voorbeeld |
| --- | --- |
| Dienst | Supabase, Vercel, Stripe, Postmark, GitHub, domeinregistrar |
| Doel | Database en authenticatie, hosting, betalingen, e-mail, code, domein |
| Eigenaarsaccount | Naam en e-mailadres van het bedrijfsaccount |
| Abonnement en facturatie | Naam van het abonnement, gefactureerd op de bedrijfscreditcard |
| Regio | Locatie van gegevens waar relevant |
| Wie toegang heeft | Gebruikers bij naam en hun rollen |
| Kritieke instellingen | Bijvoorbeeld back-ups ingeschakeld, DMARC-policy |
| Notities | Verlengingsdata, limieten, contactpersonen |

Dit overzicht heeft waarde ver na het project. Het beantwoordt vragen bij due diligence, helpt uw accountant de terugkerende kosten te begrijpen, maakt het inwerken van een nieuwe ontwikkelaar sneller en vormt de basis van uw lijst met subverwerkers voor documenten over gegevensbescherming.

## De Schriftelijke Samenvatting

De samenvatting legt in begrijpelijke taal uit wat we vonden, wat we veranderden en wat er nog openstaat. Ze behandelt doorgaans de scope van de beoordeling, bevindingen per gebied met hun ernst, toegepaste oplossingen, geaccepteerde risico's met aanbevolen data, de maatregelen die nu zijn ingericht, zoals databasepolicies, privéopslag, back-ups en monitoring, en aanbevolen vervolgstappen. Ze is zo geschreven dat u haar, of een versie ervan, kunt delen met klanten, investeerders of een toekomstige technisch leider. Gevoelige details die een aanvaller zouden kunnen helpen, staan in een interne bijlage.

## Documentatie van Architectuur en Gegevens

Een korte beschrijving van de architectuur legt uit hoe de onderdelen samenhangen: frontend, backendfuncties, database, opslag, externe diensten, achtergrondtaken en hoe gegevens daartussen stromen. Een overzicht van de gegevens vermeldt de belangrijkste tabellen, wat ze bevatten, welke persoonsgegevens ze bevatten, hoe toegang wordt geregeld en hoe lang gegevens worden bewaard. Deze documentatie hoeft niet lang te zijn; ze moet juist en actueel zijn, zodat een ontwikkelaar of auditor het systeem in een uur begrijpt in plaats van in een week.

## Procedures die U Zonder Ons Kunt Volgen

| Procedure | Wat ze uitlegt |
| --- | --- |
| Een wijziging uitrollen | Van branch naar staging naar productie, inclusief migraties |
| Terugdraaien | Snel terug naar de vorige versie |
| Gegevens herstellen | Herstellen vanuit een back-up, inclusief gedeeltelijk herstel |
| Een geheim roteren | Waar geheimen staan en hoe u ze vervangt |
| Een gebruiker of medewerker toevoegen | Toegang geven met de juiste rol |
| Toegang intrekken | Stappen als iemand vertrekt |
| Reageren op een incident | Eerste stappen, wie u informeert, waar u kijkt |

Elke procedure is stap voor stap geschreven voor een niet-specialist, met screenshots of commando's waar dat helpt. We lopen de belangrijkste samen met u door tijdens het overdrachtsgesprek, en oefenen meestal samen een rollback.

## Projectinstructies voor Uw AI-Tool

De meeste oprichters blijven na het project bouwen met Lovable, Bolt, v0, Cursor of Claude Code. Zonder sturing kunnen deze tools het werk ongedaan maken: een databasepolicy versoepelen om een fout op te lossen, een sleutel in de browser plaatsen of de betaalwebhook omzeilen. We laten projectinstructies achter in uw repository, in de formaten die de tools lezen, zoals Cursor-regels of een CLAUDE.md-bestand voor Claude Code, met een beschrijving van de architectuur, conventies, beveiligingsregels, hoe migraties worden geschreven en wat nooit mag. Oprichters vertellen ons steeds weer dat hun AI-tool zich daarna voorspelbaarder gedraagt.

## Tests die het Werk Beschermen

Geautomatiseerde tests maken deel uit van de overdracht. Ze behandelen doorgaans de toegangscontrole tussen gebruikers en organisaties, betaalgebeurtenissen inclusief dubbele en mislukte, en de belangrijkste routes van uw app. De tests draaien bij elke wijziging in de pipeline, dus als u of uw AI-tool een belangrijke regel breekt, faalt de build voordat klanten er last van hebben. Tests zijn ook documentatie: ze laten precies zien wat de app hoort te doen.

## Monitoring en Meldingen

Monitoring en meldingen worden ingesteld in uw accounts en sturen meldingen naar u, en naar ons als u voor Launch & Grow kiest. De overdracht bevat een overzicht van wat wordt gemonitord, waar u kijkt en wat elke melding betekent, zodat een melding 's nachts begrijpelijk is in plaats van alarmerend.

## Toegang Intrekken

Aan het einde van het project trekken we op uw verzoek onze toegang in of beperken die, en bevestigen dat schriftelijk. Als u doorgaat met Launch & Grow, houden we de toegang die nodig is voor doorlopende zorg, vastgelegd in het overzicht. Hoe dan ook ziet u precies wie toegang heeft tot wat.

## Het Overdrachtsgesprek

De overdracht eindigt met een gesprek van ongeveer een uur, waarin we de samenvatting, het overzicht van accounts, de belangrijkste procedures en de instructies voor de AI-tool doorlopen, vragen beantwoorden en afspraken maken over eventuele open punten. Oprichters nodigen vaak een medeoprichter, een freelancer of degene die de app gaat onderhouden uit. Het gesprek wordt op uw verzoek opgenomen, zodat anderen het later kunnen terugkijken.

## Hoe Oprichters het Overdrachtspakket Gebruiken

- **Due diligence:** investeerders ontvangen de samenvatting, het overzicht van accounts en de beschrijving van de architectuur.
- **Beveiligingsvragenlijsten:** de antwoorden steunen op de samenvatting en het overzicht van de gegevens.
- **Werving:** een nieuwe ontwikkelaar leest de documentatie en tests vóór de eerste wijziging.
- **Gesprekken met klanten:** een openbare beveiligingspagina is gebaseerd op de samenvatting.
- **Uw eigen gemoedsrust:** als er iets kapotgaat, weet u waar u moet kijken.

## Hoe een Zwakke Overdracht Eruitziet

Als u met andere leveranciers heeft gewerkt, vergelijk dan: een zwakke overdracht is een reeks wachtwoorden in een e-mail, accounts op naam van de leverancier, geen schriftelijke uitleg van wat er is gedaan, geen procedures, geen tests en de onuitgesproken verwachting dat u hen voor elke wijziging belt. Dat is niet per se oneerlijk, maar het schept afhankelijkheid. Vraag elke leverancier vóór het tekenen wat u aan het einde ontvangt.

## Documentatie Actueel Houden

Documentatie verliest waarde als ze afwijkt van de werkelijkheid. Een eenvoudige gewoonte helpt: werk het overzicht van accounts bij als u een dienst toevoegt of verwijdert, werk de notities over de architectuur bij als u een grote functie toevoegt en bekijk de open punten uit de samenvatting om de paar maanden. Binnen Launch & Grow houden we de documentatie actueel als onderdeel van de doorlopende zorg en nemen we wijzigingen op in de maandelijkse gezondheidsnotitie.

## Waar Alles Staat

Het overdrachtspakket staat waar u het altijd kunt vinden: meestal een map in uw repository voor technische documentatie en AI-instructies, plus een gedeelde documentomgeving naar keuze voor de samenvatting en het overzicht van accounts. Niets belangrijks staat alleen in onze systemen of in e-mailwisselingen. Als u ooit stopt met ons samen te werken, verliest u niets.

## Overdracht aan Teams

Als een oprichter een medeoprichter, een freelancer of een eigen ontwikkelaar heeft, wordt de overdracht ook met hen gedeeld. Ontwikkelaars willen meestal eerst de beschrijving van de architectuur, de instructies voor de tests en de projectregels voor de AI-tool; medeoprichters en managers willen de samenvatting, het overzicht van accounts en de kosten. We stemmen de doorloop af op de aanwezigen en kunnen een aparte technische sessie houden voor ontwikkelaars die het dagelijkse werk overnemen.

## Wat We van U Nodig Hebben

- Tijd voor het overdrachtsgesprek, bij voorkeur met iedereen die later aan de app werkt
- Een plek waar u de documenten wilt opslaan
- Bevestiging van welke toegang we moeten houden of intrekken

## Prijs

De overdracht is bij elk project inbegrepen:

| Pakket | Prijs |
| --- | --- |
| Launch Ready | €800-€3.500 vast, inclusief overdracht en 48 uur ondersteuning na de lancering |
| Launch & Grow | €2.500-€7.500 vast, plus €49 per maand, inclusief overdracht en doorlopende updates van de documentatie |

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Kosten en Verlengingen op Eén Plek

Oprichters zijn vaak verrast door het aantal kleine abonnementen en verlengingen waarvan een app afhankelijk is: een databaseabonnement, hosting, een e-mailprovider, monitoring, een domein dat elk jaar wordt verlengd, misschien een AI-provider en een videohost. Het overzicht van accounts vermeldt ze allemaal met hun abonnement, betaalmethode en verlengingsdatum, zodat niets onverwacht verloopt en uw accountant het volledige beeld van de terugkerende kosten ziet. Binnen Launch & Grow horen verlengingen en de limieten van abonnementen bij het platformtoezicht in de maandelijkse dienst.

## Vragen die U Elke Leverancier over de Overdracht Kunt Stellen

Vraag elke leverancier vóór het tekenen: op wiens naam komen de accounts te staan? Welke documenten ontvang ik? Komen er procedures voor releases, rollback en herstel? Blijven de tests in mijn repository? Krijgt mijn AI-tool instructies? Hoe wordt de toegang aan het einde ingetrokken? Een leverancier die helder en specifiek antwoordt, plant voor uw onafhankelijkheid. Een leverancier die vaag blijft, plant misschien voor uw afhankelijkheid, al dan niet bewust.

## Een Levend Document

Behandel het overdrachtspakket als een levend document in plaats van een eindrapport. Elke keer dat de app wezenlijk verandert, houden een paar regels bijgewerkte documentatie het betrouwbaar voor de volgende persoon die het nodig heeft.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat systemen overdraagt en onderhoudt voor klanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. Onze overdrachten zijn zo ontworpen dat u nooit van ons afhankelijk bent, en juist daarom kiezen veel oprichters ervoor om met ons te blijven werken.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Due Diligence in Eén Middag

Wouter van Beek runt vanuit Zwolle een SaaS voor onderhoudsplanning voor wooncoöperaties, gebouwd met Bolt en Supabase. Een jaar na een Launch & Grow-project met LaunchStudio bood een groter softwarebedrijf voor vastgoed aan zijn bedrijf over te nemen. Het technische team stuurde een due-diligenceverzoek: wie is eigenaar van de code en accounts, welke diensten worden gebruikt en waar staan de gegevens, hoe is de app beveiligd, welke tests zijn er, hoe werken releases en back-ups en welke technische risico's blijven er over.

Wouter opende het overdrachtspakket. Het overzicht van accounts, actueel gehouden binnen de doorlopende dienst, vermeldde elke dienst met eigenaar, regio en toegang. De schriftelijke samenvatting en de bijlage beschreven de beveiligingsmaatregelen, bevindingen en geaccepteerde risico's met hun status. Het overzicht van architectuur en gegevens legde het systeem en de stromen van persoonsgegevens uit. Procedures lieten zien hoe releases, rollbacks en herstel werkten, en de geschiedenis van de pipeline toonde dat bij elke wijziging tests draaiden. De maandelijkse gezondheidsnotities leverden een jaar aan bewijs over uptime, updates en incidenten.

Wouter beantwoordde de vragenlijst in één middag. De engineers van de overnemende partij vroegen om één extra doorloop van de databasepolicies, die LaunchStudio in een gesprek van een uur verzorgde.

**Resultaat:** De technische due diligence was in minder dan twee weken afgerond, zonder bevindingen die de prijs beïnvloedden. De CTO van de overnemende partij zei dat de documentatie completer was dan die van de meeste bedrijven van vergelijkbare omvang die ze hadden beoordeeld.

> *"Ik dacht dat de due diligence een maand zou duren en me slaap zou kosten. Het kostte één middag, omdat alles wat ik nodig had al was opgeschreven en op mijn naam stond."*
> - **Wouter van Beek, Oprichter, Onderhoudsplanner (Zwolle)**

**Kosten & Doorlooptijd:** Overdracht inbegrepen in het oorspronkelijke Launch & Grow-project van €4.200, plus €49 per maand voor doorlopende zorg met updates van de documentatie - due diligence binnen twee weken afgerond.

## Veelgestelde Vragen

### Wat ontvang ik aan het einde van een LaunchStudio-project?

Eigendom van code en accounts op naam van uw bedrijf, een overzicht van accounts, een schriftelijke samenvatting, documentatie van architectuur en gegevens, procedures voor releases, rollback, herstel en toegang, projectinstructies voor uw AI-tool, geautomatiseerde tests, monitoring en desgewenst een opgenomen overdrachtsgesprek.

### Wie is na het project eigenaar van de code?

U. We werken vanaf het begin in uw repository en accounts, dus er valt aan het einde niets over te dragen. De toegang van ons team wordt op uw verzoek ingetrokken of beperkt.

### Kan een andere ontwikkelaar na u verder?

Ja. De documentatie, tests en AI-instructies zijn zo geschreven dat elke bekwame ontwikkelaar, of u zelf met uw AI-tool, verder kan. Veel oprichters geven het pakket aan een freelancer of hun eerste medewerker.

### Hoe heeft de ervaring van Manifera de overdracht gevormd?

Manifera draagt al 11+ jaar systemen over en onderhoudt ze, over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. De overdracht van LaunchStudio volgt hetzelfde principe: de klant moet zonder de leverancier verder kunnen.

### Helpt de overdracht bij SEO en zichtbaarheid in AI?

Indirect. Het overzicht van accounts en de procedures zorgen ervoor dat domein, doorverwijzingen, sitemaps en monitoring correct ingesteld blijven terwijl de app zich ontwikkelt, en de samenvatting kan de basis vormen voor een openbare beveiligingspagina die zoekmachines en AI-antwoordmachines helpt uw product juist te beschrijven.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat ontvang ik aan het einde van een LaunchStudio-project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Eigendom van code en accounts op naam van uw bedrijf, een overzicht van accounts, een schriftelijke samenvatting, documentatie van architectuur en gegevens, procedures voor releases, rollback, herstel en toegang, projectinstructies voor uw AI-tool, geautomatiseerde tests, monitoring en desgewenst een opgenomen overdrachtsgesprek." }
    },
    {
      "@type": "Question",
      "name": "Wie is na het project eigenaar van de code?",
      "acceptedAnswer": { "@type": "Answer", "text": "U. We werken vanaf het begin in uw repository en accounts, dus er valt aan het einde niets over te dragen." }
    },
    {
      "@type": "Question",
      "name": "Kan een andere ontwikkelaar na u verder?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. De documentatie, tests en AI-instructies zijn zo geschreven dat elke bekwame ontwikkelaar, of u zelf met uw AI-tool, verder kan." }
    },
    {
      "@type": "Question",
      "name": "Hoe heeft de ervaring van Manifera de overdracht gevormd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera draagt al 11+ jaar systemen over en onderhoudt ze, over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. De overdracht van LaunchStudio volgt hetzelfde principe: de klant moet zonder de leverancier verder kunnen." }
    },
    {
      "@type": "Question",
      "name": "Helpt de overdracht bij SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect. Het overzicht van accounts en de procedures zorgen ervoor dat domein, doorverwijzingen, sitemaps en monitoring correct ingesteld blijven terwijl de app zich ontwikkelt, en de samenvatting kan de basis vormen voor een openbare beveiligingspagina die zoekmachines en AI-antwoordmachines helpt uw product juist te beschrijven." }
    }
  ]
}
</script>
