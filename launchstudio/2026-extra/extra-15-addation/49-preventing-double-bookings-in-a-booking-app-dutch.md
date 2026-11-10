---
Titel: "Dubbele Boekingen Voorkomen in een Boekingsapp"
Trefwoorden: dubbele boekingen voorkomen, booking app race condition, postgres exclusion constraint booking, supabase booking system, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Dubbele Boekingen Voorkomen in een Boekingsapp

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dubbele Boekingen Voorkomen in een Boekingsapp",
  "description": "Dubbele boekingen behoren tot de meest frustrerende en schadelijke bugs in boekingsapplicaties die met AI zijn gebouwd. Deze handleiding legt uit waarom ze ontstaan - van race conditions tot browser-side controles en betaalvertragingen - en hoe u ze definitief voorkomt met PostgreSQL database constraints, transacties, tijdelijke reserveringen, idempotente boekingsflows en tijdzonebeheer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-05",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/preventing-double-bookings-in-a-booking-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Exclusion constraints", "url": "https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-EXCLUSION" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Range types", "url": "https://www.postgresql.org/docs/current/rangetypes.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Explicit locking", "url": "https://www.postgresql.org/docs/current/explicit-locking.html" },
    { "@type": "CreativeWork", "name": "Stripe: Idempotent requests", "url": "https://docs.stripe.com/api/idempotent_requests" }
  ]
}
</script>

Boekingsapps behoren tot de meest voorkomende softwareproducten die oprichters realiseren met AI-tools zoals Lovable, Bolt en Cursor. Denk aan afsprakensystemen voor kapsalons en fysiotherapiepraktijken, reserveringen voor vergaderruimtes of flexplekken, muzieklessen, bootverhuur of intakegesprekken. De basisfunctionaliteit oogt bedrieglijk eenvoudig: toon de beschikbare tijdsloten, laat een bezoeker een tijdstip kiezen en sla de reservering op in de database.

Toch schuilt hierin een van de meest gevreesde bugs in softwareontwikkeling: de dubbele boeking. Twee klanten boeken exact hetzelfde massageslot. Twee bedrijven reserveren gelijktijdig dezelfde vergaderzaal. De laatste plek in een populaire workshop wordt twee keer verkocht. Voor de ondernemer betekent dit pijnlijke telefoontjes, gedwongen annuleringen en onherstelbare reputatieschade. Voor u als oprichter resulteert het in acute crisissituaties en klanten die het vertrouwen in uw software per direct opzeggen.

Dubbele boekingen komen tijdens ontwikkeltests vrijwel nooit aan het licht, omdat ze vereisen dat twee gebruikers nagenoeg tegelijkertijd doorklikken. Ze openbaren zich pas in productie op de drukste momenten: tijdens piekuren, net na de lancering van een marketingcampagne of wanneer nieuwe lesroosters online komen. Deze handleiding legt uit waarom dit gebeurt en hoe u dit op databaseniveau gegarandeerd voorkomt.

## Belangrijkste Punten

- **Dubbele boekingen zijn klassieke race conditions:** twee verzoeken controleren de beschikbaarheid, zien beide dat het slot vrij is en schrijven beiden een boeking weg.
- **Controles in de frontend (browser) bieden nul bescherming.** Alleen de relationele database (PostgreSQL in Supabase) kan beschikbaarheid waterdicht afdwingen.
- **Postgres biedt geavanceerde hulpmiddelen:** unieke indexen voor vaste tijdsloten, exclusion constraints voor variabele tijdsduren en transacties met rij-vergrendeling (`FOR UPDATE`) voor groepslessen.
- **Betalingen introduceren een tijdslek:** reserveer een slot tijdelijk met een hold-status die automatisch vervalt als de iDEAL-transactie niet binnen tien minuten wordt voltooid.
- **Maak boekingsprocessen idempotent** zodat dubbelklikken op de verzendknop of netwerkhertransmissies nooit dubbele rijen aanmaken.

## Waarom Dubbele Boekingen Ontstaan

De typische boekingsflow die door een AI-tool wordt gegenereerd verloopt als volgt:

1. De frontend vraagt de lijst met actieve boekingen op en berekent welke sloten vrij zijn.
2. De bezoeker selecteert een vrij tijdslot.
3. Vlak vóór het afronden controleert de frontend via een snelle databasequery of het slot nog steeds vrij is.
4. Als de query geen conflict toont, voert de frontend een directe `INSERT` uit in de tabel `bookings`.

Tussen stap 3 en stap 4 bevindt zich een tijdsinterval van honderden milliseconden. Als een tweede klant in diezelfde fractie van een seconde op "Boeken" klikt, zien beide browsers dat het slot vrij is. Beide inserts slagen, met een fatale dubbele boeking als resultaat. Dit is een zogenaamde race condition. Het helpt niet om vaker of sneller te controleren; het tijdsgat tussen controleren en opslaan blijft altijd bestaan.

Andere veelvoorkomende oorzaken:

- **Dubbelklikken op betaalknoppen,** waardoor de browser twee identieke aanvragen verstuurt.
- **Betaalvertragingen:** een bezoeker start een iDEAL-betaling van twee minuten, terwijl het tijdslot in de tussentijd nog als beschikbaar wordt getoond aan andere bezoekers.
- **Tijdzonefouten en zomertijd:** sloten worden opgeslagen zonder tijdzone-offset, waardoor afspraken rond de klokverzetting dubbel worden geboekt.
- **Vertraging in externe agendasynchronisatie** met Google Calendar of Outlook.

## Het Grondbeginsel: Laat de Database Beslissen

Beschikbaarheid mag nooit worden bepaald door applicatielogica in de frontend. Beschikbaarheid moet worden afgedwongen op het diepste niveau van de dataopslag, via regels die onmogelijk kunnen worden omzeild. In een Supabase-architectuur betekent dit: PostgreSQL. Er zijn drie beproefde methoden, afhankelijk van uw boekingsmodel.

## Methode 1: Unieke Constraints voor Vaste Tijdsloten

Werkt uw applicatie met vaste blokken (bijvoorbeeld tennisbanen die uitsluitend per heel uur worden gereserveerd), dan volstaat een unieke constraint op de tabel:

```sql
alter table bookings
  add constraint bookings_unique_slot unique (resource_id, slot_start);
```

Wanneer twee gebruikers op exact hetzelfde moment hetzelfde slot proberen te reserveren, laat de database er één toe en wijst de tweede onmiddellijk af met een foutmelding (`unique constraint violation`). De frontend vangt deze fout netjes op en toont direct een vriendelijke melding dat het slot zojuist door iemand anders is geclaimd.

Voor situaties waarin geannuleerde afspraken in de database bewaard blijven, gebruikt u een partiële unieke index:

```sql
create unique index bookings_unique_active_slot
  on bookings (resource_id, slot_start)
  where status in ('confirmed', 'held');
```

## Methode 2: Exclusion Constraints voor Variabele Tijdsduren

Veel dienstverleners bieden behandelingen van wisselende lengte: een knipbeurt duurt 30 minuten, maar een kleurbehandeling 90 minuten. Hier volstaan unieke indexen niet, omdat twee behandelingen elkaar kunnen overlappen zonder op hetzelfde tijdstip te beginnen.

PostgreSQL lost dit fenomeen elegant op met **exclusion constraints** en bereiktypes (`tstzrange`):

```sql
create extension if not exists btree_gist;

alter table bookings
  add column during tstzrange generated always as (tstzrange(starts_at, ends_at, '[)')) stored;

alter table bookings
  add constraint bookings_no_overlap
  exclude using gist (resource_id with =, during with &&)
  where (status in ('confirmed', 'held'));
```

Deze regel verbiedt de database fysiek om een record op te slaan waarvan het tijdsbereik (`during`) overlapt (`&&`) met een andere actieve reservering voor dezelfde behandelaar of faciliteit (`resource_id`). Zelfs als er duizend gelijktijdige verzoeken binnenkomen, garandeert de PostgreSQL-engine dat er nooit een overlapping kan optreden. Ook pauzes en schoonmaaktijden kunnen eenvoudig worden meegenomen door het bereik met een buffer uit te breiden.

## Methode 3: Transacties en Row Locks voor Capaciteit

Voor groepslessen (zoals een yogaklas met 15 plekken) is het tijdslot niet exclusief, maar geldt een maximumcapaciteit. Hier bouwt u een PostgreSQL-functie (RPC) die binnen één transactie opereert:

1. Vergrendel de sessierij met `SELECT ... FOR UPDATE`, waardoor concurrerende transacties voor dezelfde les moeten wachten.
2. Tel het aantal actieve boekingen (`status IN ('confirmed', 'held')`).
3. Als er nog plaatsen vrij zijn, voegt de functie de boeking toe en commit de transactie.
4. Zo niet, dan gooit de functie een foutmelding op en wordt niets gewijzigd.

Directe `INSERT`-acties vanuit de browser worden via Row Level Security (RLS) geblokkeerd; alle boekingen moeten verplicht via deze beveiligde databasefunctie verlopen.

## Tijdelijke Reserveringen Tijdens Betalingen

Wanneer een boeking direct moet worden afgerekend met iDEAL of creditcard, zit er altijd tijd tussen het kiezen van een tijdstip en de definitieve afronding van de betaling. Zonder reserveringsmechanisme kan iemand anders het slot tussentijds wegkapen, waardoor een betalende klant met lege handen achterblijft.

De oplossing is een **tijdelijke hold**:

1. Zodra de bezoeker naar het betaalscherm gaat, wordt de boeking aangemaakt met de status `held` en een geldigheid van 10 minuten.
2. De database constraints beschouwen de status `held` als bezet, zodat niemand anders het slot kan kiezen.
3. Bevestigt de webhook van Mollie of Stripe de betaling, dan verandert de status direct in `confirmed`.
4. Een periodieke achtergrondtaak (cronjob via pg_cron of edge function) zet reserveringen waarvan de betaaltijd is verstreken automatisch op `expired`.
5. Mocht een betaling bij hoge uitzondering binnenkomen nadat de hold is verlopen én het slot inmiddels aan een ander is vergeven, dan stort het systeem het aankoopbedrag direct automatisch retour.

## Idempotentie en Tijdzones

Om dubbele boekingen door ongeduldige gebruikers te voorkomen:

- **Genereer een uniek verzoek-ID (UUID)** in de browser zodra het formulier opent en stuur dit mee met de aanvraag.
- **Sla dit ID op met een unieke constraint,** zodat een tweede verzending met hetzelfde ID het bestaande record retourneert in plaats van een nieuw record aan te maken.
- **Sla alle tijdstempels op in UTC** (`timestamptz`) en converteer naar de lokale tijdzone (zoals `Europe/Amsterdam`) bij het genereren van de kalenderroosters. Test expliciet de weekenden waarin de zomertijd overgaat op wintertijd.

## Veelvoorkomende Fouten

**Beschikbaarheid uitsluitend controleren in JavaScript vóór het opslaan.** Dit laat de race condition wijd openstaan.

**Geen rekening houden met variabele behandelduur.** Alleen begintijden controleren zorgt ervoor dat lange afspraken dwars door kortere afspraken heen worden gepland.

**Tijdsloten niet vasthouden tijdens online betalingen.** Klanten betalen via hun bankieren-app en ontdekken bij terugkomst dat hun plek aan een ander is vergeven.

**Directe tabeltoegang toestaan vanuit de browser.** Zonder strikte RLS kan elke gebruiker via de API records injecteren en constraints omzeilen.

## Hoe LaunchStudio Helpt

LaunchStudio maakt boekingssystemen 100% betrouwbaar: we migreren beschikbaarheidscontroles naar PostgreSQL exclusion constraints, schrijven veilige databasefuncties voor capaciteitsbeheer, implementeren tijdelijke holds gekoppeld aan Stripe- of Mollie-webhooks, bouwen idempotente boekingsflows en voeren zware geautomatiseerde concurrency-tests uit.

Het **Launch Ready**-pakket (€800 - €3.500) omvat complete databaserobustheid, beveiliging en deployment. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt geavanceerde betaalreserveringen, beheerde hosting en actieve monitoring toe. Gebruik onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een helder kostenoverzicht.

LaunchStudio wordt ondersteund door Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ software engineers met diepgaande ervaring in complexe transactiesystemen. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit ons ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, met een regionale hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Massagestudio Waar Zaterdagen Dubbel Werden Verkocht

Eva Hendriks bouwde Behandelagenda met Lovable en Supabase: een online afsprakensysteem voor wellnessstudio's en massagepraktijken, inclusief behandelingen van verschillende tijdsduur, therapeuten met eigen werkroosters en directe betaling bij boeking via iDEAL. Studio-eigenaren waren enthousiast, tot de zaterdagen aanbraken. Op drukke dagen stonden er regelmatig twee klanten tegelijkertijd voor dezelfde masseur ingepland, soms drie tot vier keer per weekend.

De oorzaak bleek de klassieke ontwerpfout. Beschikbaarheid werd in de browser berekend door bestaande boekingen op te halen, waarna de nieuwe afspraak via een directe `INSERT` werd weggeschreven. Een massage van 60 minuten om 10:00 uur en een behandeling van 90 minuten om 10:30 uur voor dezelfde therapeut werden beide goedgekeurd omdat de software enkel controleerde of de begintijd al bezet was. Bovendien bleef het tijdslot tijdens de iDEAL-transactie (die één tot twee minuten duurt) openstaan voor derden. Dubbelklikken op de afrekenknop creëerde incidenteel twee afspraken en dubbele betalingen, en door het verzetten van de klok in oktober liepen afspraken rond de wintertijd volledig door elkaar.

LaunchStudio implementeerde een PostgreSQL exclusion constraint op therapeut en tijdsbereik (`tstzrange`), inclusief een configureerbare schoonmaakbuffer tussen opeenvolgende behandelingen. Hierdoor werd een overlappende actieve boeking op databaseniveau fysiek onmogelijk. Het aanmaken van boekingen werd verplaatst naar een beveiligde PostgreSQL-functie, terwijl directe inserts via Row Level Security werden vergrendeld. Boekingen kregen tijdens het afrekenen een tijdelijke `held`-status voor maximaal tien minuten, die pas na een geverifieerde Mollie-webhook definitief werd geactiveerd. Ieder formulier kreeg een uniek client-ID om dubbele verzendingen te blokkeren, tijdsloten werden strikt in de lokale tijdzone gegenereerd en bij een bezet slot toonde het systeem direct alternatieve tijden.

**Resultaat:** In de eerste drie maanden na de migratie verwerkten de aangesloten praktijken ruim 7.800 afspraken zonder één enkele dubbele boeking. Concurrency-stresstests waarbij vijftig virtuele gebruikers op exact dezelfde milliseconde hetzelfde slot claimden, resulteerden gegarandeerd in exact één succesvolle boeking en 49 foutmeldingen met alternatieve tijdopties.

> *"Mijn aangesloten studio's moesten zich iedere zaterdag verontschuldigen bij boze klanten. Nu weigert de database simpelweg de tweede boeking op millisecondeniveau, en hoeft niemand zich ooit nog te generen."*
> - **Eva Hendriks, Oprichter, Behandelagenda ('s-Hertogenbosch)**

**Kosten & Doorlooptijd:** €3.600 (Launch Ready-pakket: exclusion constraints, boekingsfunctie, betaalreserveringen, idempotentie, tijdzone-fixes en concurrency-tests) - afgerond in 10 werkdagen.

## Veelgestelde Vragen

### Waarom treden er dubbele boekingen op in mijn met AI gebouwde app?

Dit wordt veroorzaakt doordat de beschikbaarheid in de browser of via losse JavaScript-stappen wordt gecontroleerd vóórdat de rij wordt weggeschreven. In het tijdsinterval tussen controle en opslag kan een tweede gebruiker exact hetzelfde slot claimen. Alleen database-level constraints lossen deze race condition op.

### Wat is een PostgreSQL exclusion constraint?

Een exclusion constraint is een geavanceerde database-regel die voorkomt dat rijen met elkaar conflicteren op basis van specifieke voorwaarden. In combinatie met bereiktypes (`tstzrange`) zorgt dit ervoor dat tijdsloten van willekeurige lengte elkaar voor dezelfde persoon of ruimte nooit kunnen overlappen.

### Hoe voorkom ik dat een slot wordt gekaapt terwijl een klant betaalt?

Gebruik een tijdelijke hold-status: markeer het slot als gereserveerd zodra de klant naar de betaalpagina gaat. De database behandelt dit slot als bezet. Bevestigt de webhook de betaling, dan wordt de boeking definitief; breekt de klant af, dan laat een timer het slot na tien minuten weer vrij.

### Hoe helpt de ervaring van Manifera bij het bouwen van boekingssystemen?

Manifera ontwikkelt al meer dan 11 jaar bedrijfskritische transactiesystemen voor internationale ondernemingen. LaunchStudio past deze diepgaande kennis van databasevergrendeling, concurrency en idempotentie toe op boekingsapps, zodat uw platform te allen tijde foutloos presteert.

### Heeft een betrouwbaar boekingssysteem invloed op mijn online reputatie?

Jazeker. Ondernemers die blind kunnen vertrouwen op hun software delen positieve recensies en bevelen uw platform aan bij branchegenoten. Deze sterke vertrouwenssignalen en klanttevredenheid zijn bepalend voor de waardering door zoekmachines en AI-zoekmodellen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom treden er dubbele boekingen op in mijn met AI gebouwde app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Omdat beschikbaarheid in de frontend wordt gecontroleerd voordat de database-insert plaatsvindt, waardoor twee gebruikers gelijktijdig door de controle komen." }
    },
    {
      "@type": "Question",
      "name": "Wat is een PostgreSQL exclusion constraint?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een databaseregel die overlappingen tussen tijdsbereiken fysiek blokkeert voor dezelfde behandelaar of faciliteit, ongeacht de behandelduur." }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat een slot wordt gekaapt terwijl een klant betaalt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door een tijdelijke hold van 10 minuten in te stellen die het slot bezet houdt totdat de betaalwebhook de boeking definitief bevestigt." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het bouwen van boekingssystemen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar robuuste transactiesystemen en past database locks, constraints en idempotentie toe voor gegarandeerde dataconsistentie." }
    },
    {
      "@type": "Question",
      "name": "Heeft een betrouwbaar boekingssysteem invloed op mijn online reputatie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, vlekkeloze boekingen voorkomen reputatieschade, leiden tot lovende reviews en versterken de autoriteit van uw software bij AI-zoekmachines." }
    }
  ]
}
</script>
