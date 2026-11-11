---
Titel: "Hoeveel Gebruikers Kan een Supabase-App Aan?"
Trefwoorden: hoeveel gebruikers kan supabase aan, schaalbaarheid supabase, gelijktijdige gebruikers supabase, lovable app schalen supabase, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoeveel Gebruikers Kan een Supabase-App Aan?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoeveel Gebruikers Kan een Supabase-App Aan?",
  "description": "Oprichters die op Supabase bouwen met Lovable, Bolt of Cursor vragen vaak hoeveel gebruikers hun app aankan voordat hij bezwijkt. Deze gids legt uit waarom het antwoord afhangt van gelijktijdigheid en efficiëntie in plaats van het totale aantal gebruikers, welke limieten tellen, hoe u uw eigen capaciteit inschat, hoe het schaalpad loopt van optimalisatie naar grotere compute en read replicas, en hoe u test voordat de groei komt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-28",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-many-users-can-a-supabase-app-handle" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Compute and disk", "url": "https://supabase.com/docs/guides/platform/compute-and-disk" },
    { "@type": "CreativeWork", "name": "Supabase: Read replicas", "url": "https://supabase.com/docs/guides/platform/read-replicas" },
    { "@type": "CreativeWork", "name": "Supabase Realtime limits", "url": "https://supabase.com/docs/guides/realtime/limits" },
    { "@type": "CreativeWork", "name": "Grafana k6 documentation", "url": "https://grafana.com/docs/k6/latest/" }
  ]
}
</script>

**Kort antwoord:** Er is geen vast getal. Een goed gebouwde Supabase-app kan vele duizenden gebruikers bedienen, en Supabase draait grote productieworkloads, maar een slecht geoptimaliseerde app kan al moeite hebben met een paar honderd mensen die hem tegelijk gebruiken. Het gaat niet om het aantal accounts, maar om hoeveel gebruikers tegelijk actief zijn, hoeveel requests elk van hen doet en hoe efficiënt die requests zijn. Meet uw eigen app onder realistische belasting, los eerst inefficiënties op en schaal compute op of voeg read replicas toe wanneer de werkelijke vraag daarom vraagt.

## Belangrijkste Punten

- **Totaal aantal gebruikers en gelijktijdige gebruikers zijn verschillend.** Tienduizend geregistreerde gebruikers kunnen betekenen dat er op het drukste moment maar een paar honderd actief zijn.
- **Efficiëntie bepaalt capaciteit:** geïndexeerde queries, efficiënte policies, gepagineerde data en weinig requests per pagina vermenigvuldigen wat dezelfde compute aankan.
- **Verschillende limieten kunnen knellen:** databasecompute, verbindingen, realtimeverbindingen, storage-egress, uitvoering van functies en rate limits van auth.
- **Het schaalpad** loopt meestal van optimalisatie naar grotere compute, caching, achtergrondverwerking en read replicas.
- **Loadtests** van uw eigen app zijn de enige betrouwbare manier om uw capaciteit te kennen.

## Totaal Aantal Gebruikers versus Gelijktijdige Gebruikers

Oprichters denken vaak in totale aantallen: "Kan Supabase 50.000 gebruikers aan?" De infrastructuur ervaart iets anders: requests per seconde op het piekmoment.

Een ruwe manier om te schatten:

1. **Dagelijks actieve gebruikers:** hoeveel van uw geregistreerde gebruikers de app op een gewone dag gebruiken.
2. **Piekaandeel:** welk deel daarvan actief is in het drukste uur.
3. **Sessiegedrag:** hoeveel requests elke actieve gebruiker per minuut doet.

Bij een B2B-tool met 10.000 geregistreerde gebruikers gebruiken er misschien 3.000 de app dagelijks, een paar honderd tegelijk tijdens de ochtendpiek, die elk een paar requests per minuut doen. Dat is heel anders dan een consumentenapp met een viraal moment, waarbij duizenden mensen binnen enkele minuten binnenkomen.

## De Limieten Die Tellen

| Limiet | Wat haar bepaalt | Symptomen als ze bereikt wordt |
| --- | --- | --- |
| Database-CPU en geheugen | Computegrootte, efficiëntie van queries | Trage queries in de hele app |
| Databaseverbindingen | Computegrootte, configuratie van pooling | Verbindingsfouten |
| Efficiëntie van queries | Indexen, policies, datavolume | Specifieke pagina's worden trager naarmate de data groeit |
| Realtime | Planlimieten op gelijktijdige verbindingen en berichten | Mislukte subscriptions, gemiste updates |
| Storage en egress | Bestandsgroottes, caching | Trage media, stijgende kosten |
| Edge functions | Uitvoertijd en gelijktijdigheid | Timeouts bij zware taken |
| Auth | Rate limits op aanmeldingen en e-mails | Mislukte aanmeldingen tijdens pieken |
| Externe diensten | Limieten van betaal-, e-mail- en AI-providers | Fouten in specifieke flows |

Supabase documenteert computegroottes, realtimelimieten en andere quota per plan. Controleer de actuele documentatie, want limieten veranderen.

## Waarom Efficiëntie Belangrijker Is Dan Grootte

Neem twee versies van hetzelfde dashboard:

| Versie | Requests per paginaweergave | Gescande rijen | Databasetijd per weergave |
| --- | --- | --- | --- |
| AI-gegenereerd origineel | 40, gerelateerde data in loops geladen | Hele tabellen, geen indexen | Hoog |
| Geoptimaliseerd | 3, met gekoppelde views en paginering | Alleen overeenkomende rijen via indexen | Laag |

De geoptimaliseerde versie kan vele malen meer gebruikers bedienen op dezelfde compute. Daarom is de eerste stap bij het schalen van een met AI gebouwde app bijna altijd optimalisatie: indexen toevoegen, Row Level Security-policies vereenvoudigen, alleen benodigde kolommen selecteren, pagineren en loops van requests vervangen. Onze gidsen over [trage Supabase-queries](https://launchstudio.eu/nl/blog/slow-supabase-queries-how-to-find-and-fix-them) en [prestaties van Row Level Security](https://launchstudio.eu/nl/blog/row-level-security-performance-in-supabase) leggen uit hoe.

## Waar Apps Meestal Als Eerste Vastlopen

In met AI gebouwde apps op Supabase zijn de eerste knelpunten meestal:

1. **Een paar trage queries** op groeiende tabellen zonder indexen
2. **Policies met opzoekingen per rij** op grote tabellen
3. **Pagina's die hele tabellen** in de browser laden
4. **Directe databaseverbindingen** vanuit serverless functies of ORM's zonder pooling
5. **Realtime-subscriptions** op hele tabellen met veel verbonden gebruikers
6. **Zwaar werk in requests,** zoals PDF-generatie of AI-calls
7. **Niet-geoptimaliseerde afbeeldingen** die vanuit storage worden geserveerd

Elk van deze punten kan een app overbelast laten aanvoelen lang voordat Supabase zelf de grens is.

## Uw Capaciteit Inschatten

Een praktische aanpak:

1. **Bepaal de belangrijkste journeys:** inloggen, dashboard, zoeken, item aanmaken, afrekenen.
2. **Schat de piekgelijktijdigheid** op basis van analytics of verwacht lanceringsverkeer.
3. **Vul een stagingproject** met realistische datavolumes.
4. **Voer een loadtest uit** die die journeys simuleert bij de verwachte en een hogere gelijktijdigheid, met tools zoals k6.
5. **Volg latency, fouten en databasemetrics** om te zien waar de prestaties afnemen.
6. **Los het knelpunt op en herhaal.**

Onze gids over [loadtesten van een met AI gebouwde app](https://launchstudio.eu/nl/blog/load-testing-an-ai-built-app-before-launch) beschrijft het proces.

## Het Schaalpad

| Fase | Actie | Wanneer |
| --- | --- | --- |
| 1 | Optimaliseer queries, indexen, policies en het laden van data in de frontend | Altijd eerst |
| 2 | Configureer connection pooling correct | Bij gebruik van ORM's, workers of directe serverless verbindingen |
| 3 | Verplaats traag werk naar achtergrondtaken en cache herhaalde reads | Wanneer requests zwaar werk doen |
| 4 | Optimaliseer de levering van media met CDN en varianten | Bij het serveren van veel bestanden |
| 5 | Vergroot de compute | Wanneer efficiënte workloads CPU of geheugen nog steeds verzadigen |
| 6 | Voeg read replicas toe voor workloads met veel reads | Wanneer reads domineren en verder moeten schalen |
| 7 | Partitioneer grote tabellen en archiveer oude data | Wanneer tabellen heel groot worden |
| 8 | Splits zware workloads af naar aparte services | Wanneer specifieke workloads, zoals analytics, concurreren met de hoofdapp |

De meeste oprichters hebben lange tijd niets nodig voorbij fase 5. Direct naar fase 5 gaan zonder fase 1 tot en met 4 is duur en vaak niet effectief.

## Aandachtspunten bij Multi-Tenancy

Bij B2B-producten kan één grote klant zich heel anders gedragen dan de rest: een klant met 500.000 records, of 2.000 medewerkers die om 08.30 uur inloggen, kan de app zwaarder belasten dan alle andere klanten samen. Houd datavolumes en gebruikspatronen per klant in de gaten, en ontwerp queries en indexen die goed presteren voor de grootste tenant, niet voor de gemiddelde.

## Pieken versus Geleidelijke Groei

Geleidelijke groei geeft tijd om te observeren en te optimaliseren. Pieken, zoals een vermelding in de pers, een productlancering of een tijdgebonden moment zoals het openen van boekingen, persen maanden groei samen in enkele minuten. Verwacht u een piek, test daar dan vooraf op, optimaliseer de specifieke journeys, overweeg wachtrijen of wachtkamers voor extreme pieken, en zorg dat monitoring en een responsplan klaarstaan. Ons artikel over [een verkeerspiek bij de lancering overleven](https://launchstudio.eu/nl/blog/how-do-i-survive-a-traffic-spike-at-launch) behandelt de voorbereiding.

## Een Uitgewerkt Voorbeeld

Stel u een planning-SaaS voor met 8.000 geregistreerde gebruikers verdeeld over 200 bedrijven. Analytics tonen ongeveer 2.500 dagelijks actieve gebruikers, met het drukste uur op maandagochtend, wanneer ongeveer 20% van hen actief is, zo'n 500 mensen. Elke actieve gebruiker laadt de planner, maakt een paar wijzigingen en ververst een paar keer, gemiddeld misschien vijf requests per minuut. Dat is ongeveer 2.500 requests per minuut, of zo'n 40 per seconde op de piek.

Of dat makkelijk of moeilijk is, hangt volledig af van wat elke request doet. Als elke request één geïndexeerde query uitvoert die een pagina met resultaten teruggeeft, kan een bescheiden computegrootte dat ruim aan. Als elke keer dat de planner laadt veertig requests worden afgevuurd, waarvan verschillende hele tabellen scannen via dure policies, genereren dezelfde 500 gebruikers duizenden trage queries per seconde, en raakt de database verzadigd.

Stel nu dat het bedrijf een enterpriseklant binnenhaalt met 3.000 medewerkers die allemaal om 08.00 uur beginnen. De piekgelijktijdigheid kan binnen enkele weken verdubbelen of verdrievoudigen. Een loadtest die dat scenario simuleert, voordat de klant live gaat, laat zien of de huidige opzet standhoudt of welke query als eerste faalt. Dit is het soort schatting dat de moeite waard is vóór elke grote uitrol bij een klant of marketingcampagne.

## Kosten en Capaciteit Gaan Samen

Opschalen van compute verhoogt de maandelijkse kosten, dus efficiëntieverbeteringen betalen zich dubbel uit: meer capaciteit en lagere rekeningen. Volg de infrastructuurkosten per actieve klant naast de capaciteitsmetrics. Stijgen de kosten sneller dan het gebruik, zoek dan naar inefficiënties voordat u meer capaciteit koopt. Onze gids over [waarom Supabase-rekeningen blijven groeien](https://launchstudio.eu/nl/blog/why-does-my-supabase-bill-keep-growing) legt de gebruikelijke oorzaken uit.

## Signalen Dat U Limieten Nadert

- Database-CPU tijdens pieken structureel hoog
- Toenemende querylatency op belangrijke pagina's
- Verbindingsfouten in de logs
- Mislukte realtime-subscriptions
- Stijgende foutpercentages in foutmonitoring
- Gebruikers die op specifieke momenten traagheid melden

Stel monitoring en alerts in voor deze punten, zodat u ingrijpt voordat klanten het merken.

## Herhaalde Reads Cachen

Veel requests vragen om dezelfde data: openbare pagina's, productcatalogi, configuratie, referentielijsten, dashboards die maar om de paar minuten veranderen. Door deze te cachen, op het CDN voor openbare content of in de applicatie voor gedeelde data, verdwijnt die belasting volledig van de database. Let er goed op dat u nooit gepersonaliseerde of tenantspecifieke responses in gedeelde caches opslaat, en stel verstandige verlooptijden in zodat gebruikers verse data zien wanneer het ertoe doet.

## Is Supabase Voldoende voor Mijn Groei?

Voor de overgrote meerderheid van met AI gebouwde SaaS-producten wel. Supabase draait op Postgres, dat wereldwijd zeer grote applicaties aandrijft, en biedt grotere computegroottes, read replicas en enterpriseplannen. De vraag is zelden of het platform kan schalen; de vraag is of de datatoegang van uw app ontworpen is om te schalen. Bereikt u ooit de limieten van Supabase voor een specifieke workload, dan houdt de overdraagbaarheid van Postgres de opties open.

## Vooruit Plannen

Schrijf uw verwachte groei voor de komende twaalf maanden op, inclusief grote uitrols bij klanten en campagnes, en plan een loadtest vóór elke grote stap. Capaciteitsplanning een paar weken vooruit is veel rustiger dan noodoptimalisatie tijdens een storing.

## Hoe LaunchStudio Helpt

LaunchStudio bereidt Supabase-apps voor op groei: loadtests met realistische scenario's, optimalisatie van queries en policies, indexering, paginering en het ontwerpen van views, connection pooling, achtergrondverwerking, optimalisatie van media, advies over computegrootte, read replicas waar dat gerechtvaardigd is en monitoring met alerts.

Het **Launch Ready**-pakket (€800-€3.500) omvat een prestatiereview en fixes voor de belangrijkste journeys; **Launch & Grow** (€2.500-€7.500 plus €49 per maand) voegt loadtests, beheerde hosting, monitoring en prioriteitssupport toe. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een schatting.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat PostgreSQL-systemen met grote gebruikersbases beheert voor enterpriseklanten zoals Vodafone. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Schoolplatform Dat Op Maandag 20.000 Leerlingen Verwachtte

Karim Bouzid bouwde Huiswerkplanner met Bolt en Supabase: een app voor huiswerkplanning op middelbare scholen, waarin leerlingen opdrachten zien, docenten taken plaatsen en ouders de voortgang volgen. Een schoolbestuur met 14 scholen besloot de app in één keer uit te rollen naar ongeveer 20.000 leerlingen, vanaf een maandag na de vakantie, en vroeg of de app dat aankon.

Karim had nooit meer dan ongeveer 300 mensen tegelijk online gehad. LaunchStudio voerde een loadtest uit die de verwachte ochtendpiek simuleerde, met ongeveer 3.000 gelijktijdige leerlingen die binnen tien minuten hun planner openden. Bij ongeveer 600 gelijktijdige gebruikers duurde het laden van de plannerpagina meer dan vijf seconden en begonnen er fouten op te treden. De oorzaken: de planner laadde alle opdrachten van de school van de leerling en filterde in de browser, elke opdrachtkaart deed aparte requests voor vak en afrondingsstatus, de policy op opdrachten controleerde klaslidmaatschap met een subquery per rij zonder indexen, en een realtime-subscription op de hele opdrachtentabel stuurde elke wijziging naar elke leerling.

Engineers voegden samengestelde indexen toe voor school, klas en inleverdatum, herschreven de policy met een geïndexeerde lidmaatschapshelper en `(select auth.uid())`, en maakten een view die de opdrachten van een leerling voor de komende twee weken met vak en afrondingsstatus in één query teruggaf. Realtime werd beperkt tot privékanalen per klas met broadcasts voor nieuwe opdrachten. Afbeeldingen in opdrachten werden verkleind en gecachet, en het project ging na de optimalisatie één computegrootte omhoog, omdat de test liet zien dat dit nu de resterende grens was. De loadtest werd herhaald met 5.000 gelijktijdige gebruikers, met een 95e percentiel onder de 700 milliseconden.

**Resultaat:** Op de maandagochtend openden in het eerste uur ongeveer 11.000 leerlingen de app, met een piekgelijktijdigheid van bijna 2.800. De pagina's bleven snel, er werden geen fouten gemeld, en het schoolbestuur breidde de uitrol het volgende semester uit naar de bovenbouw van zijn basisscholen.

> *"De vraag was niet of Supabase twintigduizend leerlingen aankon. De vraag was of mijn queries dat konden."*
> - **Karim Bouzid, Oprichter, Huiswerkplanner (Rotterdam)**

**Kosten & Doorlooptijd:** €4.600 (Launch & Grow-pakket: loadtests, optimalisatie van queries en policies, views en indexen, herontwerp van realtime, caching van media en advies over computegrootte) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Hoeveel gebruikers kan Supabase aan?

Dat hangt af van hoeveel gebruikers tegelijk actief zijn en hoe efficiënt uw app is. Goed geoptimaliseerde Supabase-apps bedienen grote gebruikersbases, terwijl apps met niet-geïndexeerde queries, dure policies en veel requests per pagina al moeite kunnen hebben met een paar honderd gelijktijdige gebruikers. Een loadtest van uw eigen app geeft het echte antwoord.

### Wat is het eerste wat ik moet doen als mijn Supabase-app trager wordt met meer gebruikers?

Optimaliseer voordat u upgradet. Zoek de traagste en meest voorkomende queries, voeg indexen toe, vereenvoudig Row Level Security-policies, pagineer en vervang loops van requests. Overweeg daarna grotere compute als efficiënte workloads de database nog steeds verzadigen.

### Wanneer heb ik read replicas nodig?

Wanneer uw workload veel reads bevat en efficiënte queries op de grootste praktische computegrootte het nog steeds niet bijhouden, of wanneer u zware rapportages wilt scheiden van de hoofdapplicatie. De meeste apps in een vroeg stadium hebben ze niet nodig.

### Hoe helpt de ervaring van Manifera bij schalen?

Manifera beheert al 11+ jaar PostgreSQL-systemen met grote gebruikersbases voor enterpriseklanten. LaunchStudio past die ervaring toe op met AI gebouwde Supabase-apps, door de knelpunten te vinden die de capaciteit beperken en ze in de juiste volgorde op te lossen.

### Heeft schaalbaarheid invloed op mijn zichtbaarheid bij klanten en zoekmachines?

Ja. Apps die snel blijven tijdens groei houden gebruikers tevreden en voorkomen negatieve reviews, en openbare pagina's die onder belasting responsief blijven, zijn betrouwbaar beschikbaar voor zoekmachines en AI-antwoordmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoeveel gebruikers kan Supabase aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat hangt af van gelijktijdigheid en efficiëntie; een loadtest van uw eigen app geeft het echte antwoord." }
    },
    {
      "@type": "Question",
      "name": "Wat is het eerste wat ik moet doen als mijn Supabase-app trager wordt met meer gebruikers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Optimaliseer queries, indexen, policies en paginering voordat u de compute upgradet." }
    },
    {
      "@type": "Question",
      "name": "Wanneer heb ik read replicas nodig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Wanneer efficiënte workloads met veel reads grote compute overstijgen, of om rapportages te scheiden; de meeste vroege apps hebben ze niet nodig." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij schalen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera beheert al 11+ jaar grote PostgreSQL-systemen en LaunchStudio lost knelpunten in de juiste volgorde op." }
    },
    {
      "@type": "Question",
      "name": "Heeft schaalbaarheid invloed op mijn zichtbaarheid bij klanten en zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; apps die snel blijven tijdens groei houden gebruikers tevreden en pagina's beschikbaar voor crawlers." }
    }
  ]
}
</script>
