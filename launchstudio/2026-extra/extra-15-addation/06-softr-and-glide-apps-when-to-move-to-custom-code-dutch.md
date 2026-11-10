---
Titel: "Softr- en Glide-Apps: Wanneer Overstappen naar Maatwerkcode"
Trefwoorden: softr naar maatwerkcode, glide app migratie, softr ontgroeien, glide alternatieven voor saas, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Softr- en Glide-Apps: Wanneer Overstappen naar Maatwerkcode

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Softr- en Glide-Apps: Wanneer Overstappen naar Maatwerkcode",
  "description": "Met Softr en Glide bouwen oprichters functionele portalen en apps bovenop spreadsheets en Airtable, nhưng aanhoudende groei legt uiteindelijk grenzen bloot in datavolume, permissies, kosten per gebruiker, integraties en eigenaarschap. Deze gids licht de signalen toe dat u no-code bent ontgroeid, welke migratieroutes er zijn en hoe LaunchStudio Softr- en Glide-apps tegen een vaste prijs overzet naar maatwerkcode.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-23",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/softr-and-glide-apps-when-to-move-to-custom-code" },
  "citation": [
    { "@type": "CreativeWork", "name": "Softr documentation", "url": "https://docs.softr.io/" },
    { "@type": "CreativeWork", "name": "Glide documentation", "url": "https://www.glideapps.com/docs" },
    { "@type": "CreativeWork", "name": "Airtable API rate limits", "url": "https://airtable.com/developers/web/api/rate-limits" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" }
  ]
}
</script>

Softr en Glide behoren tot de meest praktische tools die een niet-technische ondernemer ter beschikking staan. Softr transformeert een Airtable-base (of een andere databron) in een handomdraai tot een professioneel klantenportaal, bedrijvengids of interne tool. Glide zet spreadsheets en eigen tabellen om in verzorgde, mobielvriendelijke applicaties. Geen van beide platforms vereist programmeerkennis, en beide stellen u in staat om binnen enkele dagen een waardevolle oplossing voor te leggen aan uw klanten.

Veel succesvolle bedrijven blijven hier jarenlang probleemloos op draaien. Andere ondernemingen bereiken echter een punt waarop de tool die het bedrijf ooit mogelijk maakte, verdere groei juist begint te belemmeren: softwarekosten die meestijgen met elke nieuwe gebruiker, permissiestructuren die niet kunnen uitdrukken wat zakelijke klanten eisen, harde datalimieten, trage pagina's, haperende koppelingen, of een potentiële koper die vraagt van wie het systeem juridisch eigenlijk is.

Deze gids helpt u dat kantelpunt tijdig te herkennen, de juiste vervolgstap te bepalen en de meest gemaakte migratiefouten te vermijden.

## Belangrijkste Punten

- **No-code is een volwaardige langetermijnkeuze** voor veel interne bedrijfstools en eenvoudige portalen. Overstappen is pas zinvol zodra specifieke platformgrenzen de bedrijfsvoering daadwerkelijk schaden.
- **De vijf signalen dat u Softr of Glide bent ontgroeid:** datavolume, complexe rechtenstructuren, tarieven per gebruiker, diepte van integraties en eisen rondom eigenaarschap.
- **AI-bouwers hebben de migratiekosten drastisch veranderd.** Tools als Lovable bouwen een Softr- of Glide-interface binnen enkele dagen na; het werkelijke engineeringwerk schuilt in het relationele datamodel, de autorisatieregels en de data-overdracht.
- **Een typische migratie verhuist data naar Postgres** op Supabase met Row Level Security, behoudt de vertrouwde schermen en waarborgt de dagelijkse workflow van uw gebruikers.
- **LaunchStudio migreert Softr- en Glide-apps** doorgaans binnen één tot drie weken, tegen een vaste prijs tussen €800 en €7.500.

## Waarom Oprichters Oorspronkelijk Kiezen Voor Softr en Glide

De aantrekkingskracht is volkomen begrijpelijk. Uw bedrijfsdata staat vaak al in een spreadsheet of Airtable-base, simpelweg omdat de organisatie zo functioneerde voordat er specifieke software bestond. Softr en Glide plaatsen een visuele schil bovenop die data zonder dat u deze hoeft te verplaatsen. Medewerkers kunnen records blijven bewerken in het vertrouwde raster, terwijl klanten een strak en overzichtelijk portaal te zien krijgen. Aanpassingen zijn in minuten doorgevoerd. Hosting, inlogsessies en mobiele weergaves worden automatisch verzorgd.

Voor een adviesbureau met vijftig cliënten, een ledenadministratie, een intern voorraadsysteem of een checklist-app voor servicemonteurs is dat vaak de meest efficiënte architectuur denkbaar. Het is betaalbaar, begrijpelijk en uiterst flexibel. De vraag is dan ook nooit "is no-code slecht?", maar: "is mijn onderneming veranderd op een manier die de no-codetool niet meer kan bijbenen?"

## De Vijf Signalen Dat U No-Code Bent Ontgroeid

**1. Datavolume en prestaties.** Spreadsheets en Airtable-bases kennen strikte recordlimieten per abonnementsvorm, en de laadtijden hollen vaak al ver vóór die limieten achteruit. De API van Airtable hanteert bovendien officiële rate limits, wat direct problemen geeft wanneer een portaal veel dataverzoeken per paginaweergave afvuurt. Duren laadtijden meerdere seconden, lopen filters vast of archiveert u noodgedwongen historische data om binnen uw bundel te blijven, dan is de datalaag de flessenhals geworden.

**2. Complexe permissies.** Simpele regels zijn gemakkelijk: gebruikers zien records die gekoppeld zijn aan hun e-mailadres. Echte B2B-producten vragen echter veel meer: organisaties met meerdere medewerkers, hiërarchische rollen binnen die organisaties, teamleiders die de boekingen van hun eigen afdeling mogen zien maar niet die van andere teams, externe partners met toegang tot een deelverzameling, en een onwijzigbare audittrail van wie wat heeft aangepast. Wanneer permissielogica verandert in een ondoordringbaar web van gefilterde weergaven en verborgen velden, wordt het onmogelijk om waterdicht te bewijzen dat niemand data ziet die niet voor hem bestemd is.

**3. Prijzen per gebruiker.** No-code platforms rekenen doorgaans af op basis van gebruikersaantallen, actieve apps, datavolumes of premium-features. Bij vijftig gebruikers is dat prima te overzien; bij vijfduizend gebruikers kan het de exploitatiekosten van een maatwerk-backend ruimschoots overstijgen. Rust uw verdienmodel op veel gebruikers met een lage maandelijkse marge, dan breekt de staffelprijs u al vroeg op.

**4. Diepte van integraties.** Het koppelen van betaalproviders, boekhoudpakketten, klant-API's of achtergrondprocessen via automatiseringstools (zoals Make of Zapier) volstaat voor eenvoudige situaties. Wanneer u echter tientallen losse automatiseringen onderhoudt - elk met een potentieel risico op geruisloos falen - en essentiële bedrijfslogica uitsluitend in die stappen leeft, ontstaat een systeem dat niemand meer volledig kan overzien of betrouwbaar kan debuggen.

**5. Eisen rondom eigenaarschap.** Zakelijke enterprise-klanten, investeerders en overnamepartijen vragen waar data wordt opgeslagen, wie de subverwerkers zijn, hoe back-ups zijn geregeld en wat er gebeurt als een leverancier zijn voorwaarden herziet. Wanneer meerdere SaaS-platforms aan elkaar zijn geknoopt, elk met een eigen verwerkersovereenkomst en serverregio, worden de antwoorden complex en voorwaardelijk.

Herken u één van deze signalen, dan is daar meestal nog omheen te werken. Herkent u er drie of meer, dan kosten de tijdelijke noodgrepen doorgaans meer tijd en geld dan een gerichte migratie.

## Wat Er Verandert Wanneer U Overstapt

| Aspect | Softr of Glide | Maatwerkcode (bijv. React en Supabase) |
| --- | --- | --- |
| Databron | Airtable, Google Sheets of platformtabellen | Postgres met relaties, constraints en indexen |
| Permissies | Gebruikersgroepen en filters van het platform | Row Level Security-policies per tabel en rol |
| Kostenstructuur | Oplopend per gebruiker, app of records | Vaste infrastructuurkosten, grotendeels onafhankelijk van volume |
| Prestaties | Gebonden aan API-limieten van de databron | Geïndexeerde query's, caching en server-side rendering |
| Koppelingen | Automatiseringstools en ingebouwde widgets | Directe API-aanroepen, webhooks en achtergrondtaken |
| Data bewerken | Vertrouwd spreadsheet-raster | Specifiek beheerdersportaal afgestemd op uw workflow |
| Wijzigingen | Visueel via drag-and-drop | Broncode, aanpasbaar via AI-tools of developers |
| Eigenaarschap | Verspreid over externe platforms | Uw eigen repository, database en cloud-accounts |

De laatste twee rijen vormen de werkelijke afweging. U wint volledig eigenaarschap en totale controle, en levert iets in op de flexibiliteit waarmee "iedereen in vijf minuten een knop kan toevoegen". Moderne AI-codetools hebben die kloof overigens sterk verkleind: een oprichter die overweg kan met Lovable of Cursor kan op een maatwerk-codebase nog steeds in hoog tempo schermen aanpassen.

## Hoe AI-Builders de Economie van Migraties Hebben Veranderd

Nog niet zo lang geleden betekende het verlaten van een no-code platform dat u een agency moest inhuren om elk scherm vanaf nul in code na te bouwen. Dat maakte een migratie tot een maandenlang en kostbaar project, waardoor veel bedrijven langer op no-code bleven hangen dan verstandig was.

Tegenwoordig is het bouwen van de visuele interface het voordeligste onderdeel. Een AI-builder kan de schermen van een portaal in enkele dagen reproduceren, exact afgestemd op wat uw gebruikers al gewend zijn. Wat echt technisch vakmanschap vraagt - en waar de engineering-uren in gaan zitten - is het fundament dat no-code onder de motorkap voor u verborgen hield:

- Losse spreadsheetkolommen omzetten naar een zuiver relationeel datamodel
- Elke permissieregel exact formuleren in databasepolicies en testen met verschillende rollen
- Historische records, bestandsbijlagen en accounts migreren zonder dataverlies
- Losse automatiseringen herbouwen als stabiele backendfuncties met logging en automatische retries
- Uw eigen medewerkers voorzien van een beheerdersportaal dat de vertrouwde spreadsheet vervangt

Precies daarom past een migratie tegenwoordig doorgaans binnen één tot drie weken in plaats van een halfjaar.

## De Stappen van een Geslaagde Migratie

**1. Inventarisatie.** Breng elke tabel, elk veld, alle weergaven, gebruikersgroepen, filters, automatiseringen en externe API-koppelingen in kaart. Veel oprichters ontdekken tijdens deze stap automatiseringen die ze allang waren vergeten. Elk onderdeel moet worden meegenomen.

**2. Datamodel ontwerpen.** Spreadsheetkolommen worden getypeerde velden, gekoppelde records worden relationele foreign keys, meervoudige selecties worden nette koppeltabellen, en database-constraints voorkomen dat er ooit nog inconsistente invoer ontstaat.

**3. Autorisatieregels.** Elke bestaande filterregel wordt vertaald naar een Postgres Row Level Security-policy en proefondervindelijk getest met echte gebruikersaccounts per rol. Dit is het moment waarop eerdere verborgen permissiefouten aan het licht komen.

**4. Interface aansluiten.** Schermen worden opnieuw opgebouwd om nauw aan te sluiten op de bestaande situatie, zodat gebruikers op de dag van de livegang direct hun weg vinden. Functionele vernieuwingen volgen pas nadat de overstap stabiel is afgerond.

**5. Automatiseringen overzetten.** Elke losse workflow wordt een serverloze backendfunctie of cronjob met ingebouwde foutafhandeling en logging, zodat storingen direct inzichtelijk zijn.

**6. Beheertools voor uw team.** Medewerkers die data bijhielden in Airtable of Sheets krijgen een speciaal voor hen ontworpen beheerscherm. Dit is vrijwel altijd een flinke vooruitgang, omdat invoer direct wordt gevalideerd en wijzigingen traceerbaar zijn.

**7. Definitieve overstap (Cut-over).** Data wordt definitief gesynchroniseerd, recordaantallen worden geverifieerd, gebruikers ontvangen een heldere e-mail om in te loggen, en de oude no-code app wordt op alleen-lezen gezet voordat deze definitief wordt gearchiveerd.

## Veelgemaakte Fouten Bij het Verlaten van No-Code

**De spreadsheetstructuur één-op-één kopiëren.** Een spreadsheet tolereert dubbele data en losse tekstinvoer. Een relationele database doet dat niet. Wie de historische rommel ongewijzigd overzet, behoudt alle oude problemen en creëert nieuwe.

**De ervaring van het eigen team vergeten.** Het klantenportaal krijgt alle aandacht, maar de medewerkers die dagelijks met de data werken raken hun vertrouwde spreadsheet kwijt. Betrek hun tools vanaf dag één in het ontwerp.

**De impact van automatiseringen onderschatten.** Een flow die ogenschijnlijk "alleen een bevestiging stuurt", blijkt onder water vaak drie andere tabellen bij te werken. Loop elke automatisering minutieus na.

**Overstappen in één grote klap zonder terugvaloptie.** Houd het oude systeem na de lancering nog een korte periode beschikbaar in alleen-lezen modus, zodat eventueel gemiste historische data altijd direct te raadplegen is.

## Een Eerlijke Kostenvergelijking op Drie Jaar

Oprichters vergelijken een migratieofferte geregeld met de platformfactuur van deze maand en concluderen dat blijven voordeliger is. Een zuivere vergelijking kijkt echter naar een horizon van drie jaar en neemt ook de verborgen operationele kosten mee.

| Kostenpost | Blijven op no-code | Overstappen naar maatwerk |
| --- | --- | --- |
| Platform- en licentiekosten | Stijgen mee met gebruikers, data en functionaliteiten | Grotendeels stabiele infrastructuurkosten |
| Kosten voor automatiseringstools | Lopen op met het volume aan taken en runs | Vervangen door ingebouwde backendfuncties |
| Tijd kwijt aan noodoplossingen | Wekelijks uren kwijt aan herstellen van filters, archiveren en fouten | Minimaal dankzij logging en beheertools |
| Gemiste zakelijke deals | Klanten die afhaken op ontbrekende security of AVG-eisen | Vrijwel nihil, mits gebouwd volgens standaarden |
| Eenmalige migratiekosten | Geen | Eenmalige, vaste projectinvestering |

Reken uw eigen situatie eens door. Als medewerkers wekelijks drie uur kwijt zijn aan handmatige correcties en er per kwartaal één zakelijke klant afhaakt door vragen over databeveiliging, verdient een migratie zich doorgaans al binnen het eerste jaar terug. Is dat niet het geval, dan is blijven voorlopig de meest verstandige beslissing.

## Wanneer U Beter Niét Kunt Overstappen

Blijf gerust op Softr of Glide als uw app een interne tool is met een stabiele gebruikersgroep, de permissies eenvoudig zijn, de maandelijkse kosten binnen de perken blijven en niemand lastige vragen stelt over serverlocaties. Een goed functionerende no-code app is vele malen beter dan een slecht onderhouden maatwerkapplicatie. Evalueer de situatie simpelweg jaarlijks, of zodra een van de vijf signalen de kop opsteekt.

## Wat Het Kost

De migratie van een overzichtelijke Softr- of Glide-app met enkele tabellen, basisrollen en een handvol automatiseringen valt doorgaans binnen het **Launch Ready**-pakket (€800 - €3.500), inclusief domeindeployment en 48 uur nazorg na livegang. Grotere portalen met meerdere organisatielagen, bestandsbijlagen, betalingen en integraties vallen onder **Launch & Grow** (€2.500 - €7.500 plus €49 per maand), wat tevens managed hosting, back-ups, transactionele e-mail en prioritaire ondersteuning omvat. U ontvangt een vaste prijsopgave na een gesprek van 15 minuten. Onze [prijscalculator](https://launchstudio.eu/nl/#calculator) geeft u een betrouwbare eerste schatting.

Staat uw data primair in Airtable? Onze gids over [migreren van Airtable naar Supabase](https://launchstudio.eu/nl/blog/airtable-to-supabase-migration-moving-a-no-code-backend-to-postgres) gaat dieper in op de specifieke datatechnische kant.

## Wie de Migratie Uitvoert

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, meer dan 160 opgeleverde projecten en 120+ software-engineers, met ruime ervaring in datamigraties voor enterprise-opdrachtgevers als Vodafone en TNO. Oprichters spreken met het team aan Herengracht 420 in Amsterdam; de technische migratie wordt uitgevoerd vanuit Manifera's ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door de hub aan Tras Street in Singapore.

Zoals CEO Herre Roelevink benadrukt: de uitdaging in software is niet langer om ideeën vlot zichtbaar te maken, maar om de robuuste architectuur neer te zetten waarmee die ideeën duurzaam kunnen groeien. Op het juiste moment afscheid nemen van no-code is daarvan een sprekend voorbeeld.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Tolkenportaal Dat Tegen Alle Grenzen Tegelijk Aanliep

Mehmet Yilmaz runt een tolkenbureau in Rotterdam dat tolken levert aan ziekenhuizen, gemeenten en advocatenkantoren. Hij bouwde Tolkplanner in Softr bovenop een Airtable-database: opdrachtgevers dienen tolkverzoeken in, tolken accepteren opdrachten en kantoorpersoneel bewaakt de facturatie. Het systeem functioneerde drie jaar lang uitstekend.

De aanhoudende groei legde echter alle beperkingen tegelijkertijd bloot. De base passeerde de 60.000 opdrachten, pagina's deden er zes tot acht seconden over om in te laden en het kantoor was continu bezig historische data te archiveren om binnen de bundels te blijven. Een grote ziekenhuisgroep eiste bovendien gescheiden toegang per afdeling, waarbij unithoofden alleen hun eigen afdelingen mochten inzien - een wens die met de bestaande Softr-filters niet waterdicht in te richten was. Ondertussen stegen de licentiekosten per actieve tolk fors, en haperden twee van de tweeëntwintig Make-automatiseringen al wekenlang geruisloos. Toen een gemeentelijke aanbesteding vervolgens vroeg om dataopslag binnen de EU en een sluitende verwerkersovereenkomst voor de gehele keten, was de maat vol.

LaunchStudio bracht elke tabel, weergave en automatisering in kaart, ontwierp een zuiver Postgres-schema op Supabase in Frankfurt en schreef Row Level Security-policies voor organisaties, afdelingen, managers en tolken. De interface werd met Lovable nauwkeurig nagebouwd naar het vertrouwde portaal, en het kantoorteam kreeg een snel beheerdersscherm met data-validatie en wijzigingsgeschiedenis. De automatiseringen werden omgezet naar geplande backendfuncties met actieve logging, en alle 60.000 historische dossiers (inclusief de gearchiveerde data) werden vlekkeloos overgezet.

**Resultaat:** Tolkplanner draaide binnen 15 werkdagen op zijn nieuwe fundament. Schermen laden nu in minder dan een seconde, de maandelijkse softwarekosten daalden met circa 60%, en het bureau kon de gemeentelijke aanbesteding indienen met één glasheldere privacybeschrijving. De afdelingsstructuur voor het ziekenhuis ging diezelfde maand nog live.

> *"Softr heeft mijn onderneming drie jaar lang gedragen. Toen we uit ons jasje groeiden, had ik iemand nodig die begreep wat no-code goed deed én wat er technisch opnieuw moest worden opgebouwd."*
> - **Mehmet Yilmaz, Oprichter, Tolkplanner (Rotterdam)**

**Kosten & Doorlooptijd:** €6.900 (Launch & Grow-pakket: relationeel datamodel, RLS voor vier rollen, interface-nabouw, migratie van automatiseringen, beheertools en hosting) - afgerond in 15 werkdagen.

## Veelgestelde Vragen

### Was het een vergissing om mijn app oorspronkelijk op Softr of Glide te bouwen?

Beslist niet. Bouwen op no-code stelde u in staat uw bedrijfsconcept snel en met minimale kosten te valideren. Veel gezonde bedrijven draaien er jarenlang op. Overstappen naar maatwerk is simpelweg de logische volgende fase zodra schaal, zakelijke klanten of kosten dat vereisen. Het gevalideerde productontwerp maakt de uiteindelijke migratie juist vele malen eenvoudiger.

### Zullen mijn gebruikers veel merken van de overstap naar maatwerkcode?

Idealiter vrijwel niets. We bouwen de gebruikersinterface zodanig na dat deze nauw aansluit bij wat uw klanten al gewend zijn, en alle data verhuist integraal mee. De meeste gebruikers merken uitsluitend dat pagina's merkbaar sneller laden, en ontvangen eenmalig een e-mail om hun wachtwoord opnieuw in te stellen.

### Kunnen medewerkers de data na de overstap nog steeds eenvoudig aanpassen?

Jazeker. In plaats van een kwetsbaar spreadsheet-raster ontvangen medewerkers een overzichtelijk beheerdersportaal dat specifiek is ingericht voor hun dagelijkse taken. Ingebouwde validatie voorkomt typefouten en een wijzigingsgeschiedenis houdt bij wie wat heeft aangepast, wat de meeste teams als een grote verbetering ervaren.

### Hoe helpt Manifera's ervaring bij no-code migraties?

Manifera migreert al meer dan 11 jaar bedrijfskritische data en werkprocessen voor veeleisende enterpriseklanten. Die ervaring bewijst haar waarde vooral in de onzichtbare details: het opschonen van vervuilde data, het exact dichttimmeren van permissies en het borgen dat geen enkele verborgen automatisering over het hoofd wordt gezien.

### Verbetert de overstap naar maatwerkcode de vindbaarheid in Google en AI-tools?

Zeker. Maatwerkcode biedt u volledige controle over de laadsnelheid, server-side gerenderde pagina's, gestructureerde data (schema markup) en domeinconfiguraties. Al deze elementen zorgen ervoor dat zowel traditionele zoekmachines als AI-zoeksystemen uw openbare pagina's vlotter kunnen crawlen, begrijpen en citeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Was het een vergissing om mijn app oorspronkelijk op Softr of Glide te bouwen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. No-code maakte snelle en goedkope validatie mogelijk. Verhuizen naar maatwerkcode is simpelweg de volgende stap wanneer groei, klanten of kosten dat vereisen." }
    },
    {
      "@type": "Question",
      "name": "Zullen mijn gebruikers veel merken van de overstap naar maatwerkcode?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vrijwel niets. De interface wordt identiek nagebouwd en data blijft behouden; gebruikers merken vooral snellere laadtijden en een eenmalige inlogmail." }
    },
    {
      "@type": "Question",
      "name": "Kunnen medewerkers de data na de overstap nog steeds eenvoudig aanpassen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Medewerkers krijgen een beheerdersportaal op maat met invoervalidatie en wijzigingshistorie, wat betrouwbaarder werkt dan een spreadsheet." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera's ervaring bij no-code migraties?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera migreert al 11+ jaar enterprisedata en processen, wat cruciaal is bij het opschonen van data, het inrichten van RLS-rechten en het borgen van automatiseringen." }
    },
    {
      "@type": "Question",
      "name": "Verbetert de overstap naar maatwerkcode de vindbaarheid in Google en AI-tools?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, door volledige controle over paginasnelheid, server-rendered content, gestructureerde data en domeininstellingen, wat crawlen en citeren vergemakkelijkt." }
    }
  ]
}
</script>
