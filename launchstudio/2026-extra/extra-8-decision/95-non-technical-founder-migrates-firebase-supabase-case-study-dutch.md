---
Titel: "Praktijkvoorbeeld: Een Niet-Technische Oprichter Migreert Van Firebase Naar Supabase Zonder Downtime"
Trefwoorden: Firebase naar Supabase migratie, databasemigratie SaaS, relationele datamigratie, NoSQL naar PostgreSQL migratie, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Praktijkvoorbeeld: Een Niet-Technische Oprichter Migreert Van Firebase Naar Supabase Zonder Downtime

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Praktijkvoorbeeld: Een Niet-Technische Oprichter Migreert Van Firebase Naar Supabase Zonder Downtime",
  "description": "Hoe een niet-technische oprichter van een evenemententicketing-platform in Almere 12.000 gebruikersrecords en complexe relationele tickethiërarchieën migreerde van Firebase Firestore naar Supabase PostgreSQL, zonder één actieve transactie te laten vallen.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/non-technical-founder-migrates-firebase-supabase-case-study"
  }
}
</script>

Firebase Firestore is vaak de eerste database die niet-technische oprichters kiezen bij het prototypen. Hij verbindt makkelijk, vereist geen initiële schemadefinities, en laat u willekeurige JSON-objecten opslaan zonder wrijving. Maar zodra uw businessmodel evolueert naar complexe relationele query's — zoals het opvragen van ticketverkoop gegroepeerd naar organisator, datum, promocode en uitbetalingsstatus — wordt Firestore's NoSQL-documentmodel een prestatie- en financieel knelpunt. Voor Ruben Schipper, oprichter van FestivalPass NL, schoten de Firestore-facturen omhoog naar €450/maand terwijl eenvoudige analysequery's 12 seconden duurden. Hij wist dat hij relationele PostgreSQL op Supabase nodig had, maar de gedachte om 12.000 actieve gebruikers en tickets te migreren zonder live evenementenverkoop te breken, joeg hem angst aan.

## Het Knelpunt: Wanneer NoSQL-Documentopslag De Relationele Muur Raakt

FestivalPass NL verbond onafhankelijke Nederlandse evenementenorganisatoren met kopers van festivaltickets. Naarmate het platform groeide:
- Vereiste eenvoudige rapportage (bijv. "hoeveel VIP-tickets zijn er gisteren verkocht met promocode 'SUMMER26'?") het downloaden van duizenden individuele documenten naar clientapparaten en het aggregeren daarvan in het frontend-geheugen.
- Vermenigvuldigden Firestore-leesbewerkingen zich exponentieel, wat leidde tot onvoorspelbare maandelijkse cloudrekeningen.
- Was complexe datavalidatie onmogelijk zonder tientallen fragiele Firebase Security Rules te schrijven die regelmatig braken bij frontend-updates.

De onderliggende oorzaak was structureel, geen configuratiefout die Ruben had kunnen vermijden. Firestore is een documentdatabase: elk ticket, elke organisator en elke promocode-verzilvering leeft als zijn eigen gedenormaliseerde JSON-blob, gedupliceerd over collecties om de joins te vermijden die relationele databases van nature afhandelen. Dat werkt prima wanneer een app één document tegelijk leest. Het breekt op het moment dat een oprichter een vraag moet beantwoorden die meerdere entiteiten overspant — "welke organisatoren naderen hun maandelijkse uitbetalingsdrempel" vereist dat Firestore elk ticketdocument naar applicatiegeheugen trekt en daar aggregeert, omdat Firestore geen server-side JOIN of GROUP BY heeft. Elke dashboard-load was in feite een mini-datawarehouse-job die in Rubens browsertab draaide. Ruben wilde de kracht, voorspelbaarheid en SQL-mogelijkheden van Supabase (PostgreSQL), maar had nul ervaring met dataextractie, schemamapping of zero-downtime cutover-migraties, en elk forumdraadje dat hij las waarschuwde dat een mislukte cutover klanten dubbel kon laten betalen of tickets stilletjes kon laten vallen midden in een verkoop.

## De Strategie: Dual-Writing en Zero-Downtime Migratie

Ruben schakelde LaunchStudio in om de databasetransformatie uit te voeren. Het Manifera-engineeringteam implementeerde een beproefd 4-fasenmigratieplan, gebouwd rond één beperking: FestivalPass NL kon niet offline gaan, zelfs niet voor een onderhoudsvenster, omdat er gedurende de migratieperiode ticketverkopen voor weekendfestivals gepland stonden.

**1. Genormaliseerd PostgreSQL-Schemaontwerp:** Het team ontwierp een schoon, genormaliseerd relationeel schema in Supabase met foreign keys, indexen en geautomatiseerde Row-Level Security (RLS)-beleidsregels die de financiële data van organisatoren beschermden. Tickets, bestellingen, organisatoren en promocodes werden elk hun eigen tabel met expliciete relaties, wat de geneste documentstructuren verving waarin een enkel "bestelling"-document voorheen kopieën van ticket-, koper- en organisatordata insloot die stilletjes uit sync konden raken.

**2. Geautomatiseerde ETL-Pipeline (Extract, Transform, Load):** Een custom Node.js-script extraheerde alle historische Firestore-collecties in batches, transformeerde geneste JSON-structuren naar relationele rijen, verifieerde de integriteit van foreign keys (bijvoorbeeld door elk ticket te markeren dat verwees naar een verwijderde organisator) en backfillde de nieuwe Supabase-instance. Het script draaide eerst tegen een staging-replica, waar 340 misvormde legacy-records aan het licht kwamen — vooral testtickets uit FestivalPass NL's vroegste weken — die werden opgeschoond voordat productie werd aangeraakt.

**3. Dual-Write Middleware:** Gedurende 72 uur werd de API geconfigureerd om live transacties gelijktijdig naar zowel Firebase als Supabase te schrijven, met idempotentiesleutels die garandeerden dat een herhaald verzoek nooit een duplicaat ticket in beide systemen aanmaakte. Elke schrijfactie werd gelogd met een correlatie-ID zodat elke afwijking tussen de twee databases herleid kon worden tot de exacte API-aanroep die deze veroorzaakte, in plaats van later ontdekt te worden als een onverklaarde mismatch.

**4. Onmiddellijke DNS-Cutover en Leesverificatie:** Zodra de datapariteit was geverifieerd via geautomatiseerde hash-vergelijkingsscripts — die rijaantallen, checksums en steekproefgewijze recordinhoud tussen beide databases vergeleken — werden de frontend-API-endpoints achter een feature flag omgeschakeld om uitsluitend van Supabase te lezen, waarmee de cutover in minder dan 200 milliseconden werd voltooid, met een direct beschikbaar rollbackpad naar Firebase mocht er in het eerste uur iets vreemds opvallen.

## De Randgevallen Aanpakken: Zitplaatsreserveringen, Promocodes en Gelijktijdige Verkoop

Ticketingplatforms dragen migratierisico's die een typisch SaaS-dashboard niet kent. Firestore's eventual-consistency-model maakte het makkelijk om per ongeluk een promocode te oververkopen — twee kopers konden "SUMMER26" binnen milliseconden van elkaar verzilveren en beiden zagen het slagen, omdat niets uniciteit afdwong op databaseniveau. Een deel van het Supabase-schemawerk bestond uit het toevoegen van een unieke beperking op promocodeverzilvering per bestelling, iets wat Postgres van nature afdwingt op schrijfmoment in plaats van applicatieniveau-locking te vereisen. Tijdelijke zitplaatsreserveringen (een reserveringsvenster van 10 minuten terwijl een koper de checkout afrondt) werden op vergelijkbare wijze herbouwd met Postgres-rijlocks en een geplande opruimtaak, ter vervanging van een Firestore Cloud Function die af en toe stilletjes tickets in "gereserveerd"-limbo had achtergelaten wanneer deze zonder foutmelding faalde. Niets hiervan was zichtbaar voor Ruben als niet-technische oprichter — vanuit zijn oogpunt zag de checkoutflow er voor en na exact hetzelfde uit — maar het dichtte echte omzetlekken die in de oorspronkelijke Firestore-bouw hadden bestaan.

## Het Resultaat

FestivalPass NL migreerde **12.400 gebruikersprofielen, 38.000 tickettransacties en 450 organisatoraccounts** met **nul minuten downtime en nul verloren betalingen**.

- Analysequerytijden op het dashboard daalden van **12,4 seconden naar 85 milliseconden**.
- Maandelijkse databasehostingkosten daalden van **€450/maand op Firebase naar een vast bedrag van €25/maand op Supabase**.
- Complexe SQL-rapportage stelde Ruben in staat direct geautomatiseerde uitbetalingsrapporten voor organisatoren te lanceren, wat in Firestore voorheen technisch onmogelijk was.
- De promocode- en zitplaatsreserveringsfixes elimineerden twee categorieën supporttickets die Ruben stilletjes een paar uur per week aan handmatige reconciliatie kostten.

> *"Ik had nachtmerries over het kwijtraken van klanttickets of het crashen van onze checkout midden in een festivalticketverkoop. LaunchStudio migreerde onze hele database zonder downtime terwijl we letterlijk tickets aan het verkopen waren. Het voelde alsof we de motor van een vliegtuig verwisselden terwijl we vlogen."*
> — **Ruben Schipper, Oprichter, FestivalPass NL (Almere)**

**Kosten & Doorlooptijd:** €2.600 (Launch Ready Package, volledige ETL-migratie + dual-write-pipeline + zero-downtime cutover) — afgerond in 8 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) voert complexe databasemigraties en architecturale moderniseringen uit — mogelijk gemaakt door Manifera's 11+ jaar enterprise data-engineering.

[Plan uw naadloze databasemigratie met ons engineeringteam](https://launchstudio.eu/nl/#contact).

---

## Veelgestelde Vragen

### Waarom is PostgreSQL op Supabase meestal beter voor SaaS dan Firebase Firestore?
PostgreSQL biedt relationele integriteit, krachtige SQL-joins, ACID-transacties en voorspelbare prijzen, terwijl NoSQL-documentdatabases zoals Firestore per lees-/schrijfbewerking factureren en moeite hebben met complexe aggregaties.

### Hoe voorkomt LaunchStudio dataverlies tijdens een live databasemigratie?
We gebruiken dual-write-synchronisatiepipelines die live gebruikersacties gelijktijdig naar zowel de oude als de nieuwe database schrijven, totdat volledige datapariteit is geverifieerd.

### Dwingt het migreren van Firebase naar Supabase mij mijn frontend-UI te wijzigen?
Nee. Uw visuele frontend-componenten blijven identiek. We vervangen simpelweg de Firebase-SDK-clientaanroepen door schone Supabase-API-verzoeken eronder.

### Hoelang duurt een typische databasemigratie van begin tot eind?
Voor early-stage tot growth-stage apps (onder 100.000 records) duurt het hele proces — van schemaontwerp en ETL-testen tot live zero-downtime cutover — doorgaans 5 tot 10 werkdagen.

### Kunnen gebruikerswachtwoorden worden gemigreerd van Firebase Authentication naar Supabase zonder wachtwoordherstel te forceren?
Ja. Met behulp van cryptografische wachtwoordexporttools kunnen we bestaande wachtwoordhashes rechtstreeks naar Supabase Auth migreren, zodat gebruikers naadloos kunnen inloggen met hun bestaande gegevens.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is PostgreSQL op Supabase meestal beter voor SaaS dan Firebase Firestore?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "PostgreSQL excelleert in relationele query's, joins en aggregaties met vaste maandkosten, terwijl de prijs per leesbewerking van Firestore agressief schaalt bij complexe SaaS-rapportage."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomt LaunchStudio dataverlies tijdens een live databasemigratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We zetten dual-write-replicatiemiddleware in die garandeert dat alle live gebruikersgebeurtenissen gelijktijdig worden vastgelegd in zowel de legacy- als de doeldatabase, totdat de verificatie slaagt."
      }
    },
    {
      "@type": "Question",
      "name": "Dwingt het migreren van Firebase naar Supabase mij mijn frontend-UI te wijzigen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Uw visuele layout en frontend-design blijven ongewijzigd terwijl we datalquery's en client-hooks eronder moderniseren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoelang duurt een typische databasemigratie van begin tot eind?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meeste early-stage databasemigraties worden volledig gescoped, getest in staging en uitgevoerd met zero downtime binnen 5 tot 10 werkdagen."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen gebruikerswachtwoorden worden gemigreerd van Firebase Authentication naar Supabase zonder wachtwoordherstel te forceren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. We migreren geauthenticeerde wachtwoordhashes rechtstreeks naar Supabase Auth, zodat bestaande gebruikers zonder enige loginwrijving verder kunnen."
      }
    }
  ]
}
</script>
