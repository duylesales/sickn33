---
Titel: "Tijdzone- en Datumbugs in met AI Gebouwde Apps"
Trefwoorden: timezone bugs javascript, timestamptz vs timestamp, daylight saving bug app, date handling supabase, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Tijdzone- en Datumbugs in met AI Gebouwde Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Tijdzone- en Datumbugs in met AI Gebouwde Apps",
  "description": "Afspraken die plotseling een uur verschuiven, facturen die gedateerd zijn op de verkeerde maand, sms-herinneringen die midden in de nacht aankomen en kwartaalrapporten die de laatste dag missen: tijdzone- en datumfouten behoren tot de meest hardnekkige bugs in met AI gebouwde SaaS-apps. Deze handleiding legt de onderliggende oorzaken uit - van PostgreSQL timestamp-typen en JavaScript Date parsing tot zomertijd en cronjobs - en biedt beproefde regels voor Supabase en React.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-13",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/timezone-and-date-bugs-in-ai-built-apps" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Date/Time types", "url": "https://www.postgresql.org/docs/current/datatype-datetime.html" },
    { "@type": "CreativeWork", "name": "MDN: Date", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date" },
    { "@type": "CreativeWork", "name": "MDN: Intl.DateTimeFormat", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat" },
    { "@type": "CreativeWork", "name": "IANA Time Zone Database", "url": "https://www.iana.org/time-zones" }
  ]
}
</script>

Weinig softwarefouten ondermijnen het professionele vertrouwen van gebruikers zo snel als datum- en tijdzonefouten. Een klant boekt een afspraak om 10:00 uur en ontvangt een bevestiging voor 09:00 uur. Een factuur die op 1 juli wordt aangemaakt vermeldt 30 juni als factuurdatum. Een herinneringsmail die 's ochtends om 08:00 uur verstuurd had moeten worden, wekt de klant om 02:00 uur 's nachts. En twee keer per jaar - rond de overgang naar de zomertijd of wintertijd - worden agenda's geteisterd door dubbele tijdsloten of verdwenen lesuren.

Deze bugs openbaren zich massaal in webapplicaties die zijn gebouwd met Lovable, Bolt, v0 en Cursor. De reden is volkomen begrijpelijk: tijdens het ontwikkelen bevinden de oprichter, de browser, de lokale testdatabase en de mockdata zich allemaal in exact dezelfde tijdzone, of alles draait op de server in UTC zonder dat iemand het merkt omdat testafspraken geen echte kloktijden hebben. Echte gebruikers brengen echter echte tijdzones mee, reizen over grenzen, hanteren wettelijke belastingtijdvakken en verwachten dat "vandaag" ook daadwerkelijk vandaag betekent.

Deze gids fileert de fundamentele oorzaken van datum- en tijdzonefouten en biedt concrete regels om ze voorgoed uit te bannen.

## Belangrijkste Punten

- **Sla specifieke tijdstippen (instants) altijd op als `timestamptz` in UTC,** en converteer ze uitsluitend naar de lokale tijdzone voor weergave en gebruikersinvoer.
- **Sla kalenderdatums zonder tijd op als het datatype `date`,** nooit als timestamp. Geboortedata, factuurdatums en betaaltermijnen hebben geen tijdzone nodig.
- **Wees u bewust van de tijdzone van elk subsysteem:** de browser van de bezoeker, de cloudserver, de database en de periodieke achtergrondtaken (cronjobs).
- **Gebruik officiële IANA-tijdzonenamen zoals `Europe/Amsterdam`,** nooit vaste offsets zoals `+01:00`, aangezien offsets in de zomer met een uur wijzigen.
- **Test expliciet op randvoorwaarden:** de weekenden van de klokwisseling (zomer-/wintertijd), middernachtelijke mutaties en maandovergangen.

## Twee Wezenlijk Verschillende Soorten Tijd

De meeste datumfouten ontstaan door het door elkaar halen van twee fundamenteel verschillende concepten:

**1. Het Absolute Moment (Instant):**
Een specifiek, universeel moment op de wereldtijdlijn. Het vindt overal ter wereld op exact hetzelfde ogenblik plaats: wanneer een online betaling voltooit, wanneer een chatbericht wordt verzonden of wanneer een internationale videocall start.
*Beste datatype:* `timestamptz` (in UTC).

**2. De Kalenderdatum en Lokale Kloktijd:**
Menselijke concepten die strikt gebonden zijn aan een fysieke locatie: een verjaardag, een factuurdatum, de openingstijd van een winkel ("elke ochtend om 08:30 uur open") of een periodieke herhaling. Een verjaardag op 14 juli blijft 14 juli, waar ter wereld u zich ook bevindt. Een afspraak om 09:00 uur in Amsterdam is in de winter een ander UTC-tijdstip (UTC+1) dan in de zomer (UTC+2).
*Beste datatype:* `date` voor datums, `time` gecombineerd met een IANA-tijdzone voor openingstijden.

| Waarde | Te gebruiken datatype | Voorbeeld |
| --- | --- | --- |
| Betaling ontvangen | `timestamptz` | 2028-06-12 08:14:03 UTC |
| Start van fysieke afspraak | `timestamptz` + IANA-tijdzone van locatie | 10:00 Europe/Amsterdam (intern UTC) |
| Factuurdatum | `date` | 2028-06-12 |
| Vervaldatum | `date` | 2028-07-12 |
| Openingstijd winkel | `time` + tijdzone | 09:00 Europe/Amsterdam |
| Wekelijkse teammeeting | Herhalingsregel + tijdzone | Elke maandag om 09:00 Europe/Amsterdam |

## PostgreSQL: `timestamp` versus `timestamptz`

PostgreSQL kent twee varianten voor tijdstempels:

- `timestamp without time zone` (`timestamp`): slaat puur de cijfers van datum en tijd op zonder enige tijdzone-informatie.
- `timestamp with time zone` (`timestamptz`): slaat een universeel tijdstip op, converteert invoer automatisch naar UTC en berekent bij opvragen de tijd conform de actieve sessietijdzone.

Gebruik voor tijdstippen altijd `timestamptz`. AI-gegenereerde databaseschema's gebruiken regelmatig per abuis `timestamp`. Hierdoor ontstaat direct ambiguïteit: is `"2028-06-12 10:00"` opgeslagen in UTC, in Nederlandse tijd of in de lokale tijd van de server? Verschillende API-functies maken hierover verschillende aannames, wat leidt tot verschuivingen van één of twee uur.

Standaardkolommen in Supabase zoals `created_at` gebruiken terecht `timestamptz DEFAULT now()`. Problemen duiken op bij tabellen die later worden toegevoegd voor agendafuncties (`start_time`, `due_at`).

## Valkuilen in JavaScript Date Handling

Het ingebouwde `Date`-object van JavaScript is berucht om zijn onvoorspelbare gedrag:

- **String parsing van datums:** `new Date("2028-06-12")` wordt door de browser geparsed als middernacht UTC (`00:00:00 UTC`). Voor een gebruiker in Nederland (UTC+2 in de zomer) resulteert dit in 02:00 uur 's nachts op 12 juni. Voor een gebruiker in Suriname of de Antillen (UTC-4) resulteert ditzelfde object echter in 20:00 uur op **11 juni** - de datum verspringt spontaan naar de vorige dag.
- **Nul-gebaseerde maanden:** `new Date(2028, 5, 12)` representeert 12 **juni**, niet 12 mei (januari is index 0).
- **`toISOString()` forceert altijd UTC:** converteert u een lokale middernachtelijke datum (00:30 uur) naar een ISO-string, dan resulteert dit in `22:30:00Z` op de vorige dag.
- **Servers en browsers verschillen:** code die draait in de browser van een gebruiker in Amsterdam geeft een ander resultaat dan exact dezelfde functie die draait in een Supabase Edge Function in Frankfurt of Ierland die op pure UTC staat ingesteld.

Vuistregels ter voorkoming:

1. Behandel kalenderdatums altijd als platte strings in het formaat `YYYY-MM-DD` en sla ze direct op in `date`-kolommen zonder ze door een JavaScript `Date`-object te halen.
2. Gebruik gespecialiseerde libraries zoals `date-fns` (met `@date-fns/tz`) of `Luxon` voor berekeningen over tijdzones.
3. Formatteer tijden voor de gebruiker altijd via `Intl.DateTimeFormat` met een expliciet meegegeven tijdzone (`timeZone: 'Europe/Amsterdam'`).

## Zomertijd en Wintertijd (DST)

Binnen de Europese Unie verzet men de klok op de laatste zondag van maart (één uur vooruit) en de laatste zondag van oktober (één uur terug). De gevolgen:

- **In het voorjaar bestaat één uur niet:** 02:30 uur 's nachts vindt op die zondag in Amsterdam simpelweg niet plaats.
- **In het najaar vindt één uur twee keer plaats:** 02:30 uur treedt twee keer op met een tussentijd van zestig minuten.
- **De offset wisselt:** Amsterdam is UTC+1 in de winter en UTC+2 in de zomer.

Dit veroorzaakt klassieke softwarefouten: tijdsloten die worden berekend door simpelweg "24 uur" op te tellen bij een UTC-tijdstempel verschuiven plotseling met een uur na het overgangsweekend. Wekelijkse afspraken die zijn opgeslagen als een vaste UTC-tijd verspringen lokaal van 10:00 naar 11:00 uur.

Sla voor terugkerende afspraken daarom nooit een vaste UTC-offset op, maar altijd de IANA-naam `Europe/Amsterdam`, en bereken het actuele tijdstip telkens dynamisch via PostgreSQL functies (`AT TIME ZONE`).

## Geautomatiseerde Taken en Herinneringen

Geplande achtergrondtaken (cronjobs in Supabase of GitHub Actions) draaien standaard in UTC. Een taak gepland om `0 7 * * *` (07:00 UTC) executeert in de Nederlandse winter om 08:00 uur, maar in de zomer om **09:00 uur**.

Voor tijdgevoelige zakelijke herinneringen:

- Laat de cronjob frequent draaien (bijvoorbeeld elke 10 of 15 minuten) en selecteer records waarvan de berekende verzendtijd in de lokale tijdzone van de ontvanger is aangebroken.
- Of bereken bij het inplannen van de afspraak direct het exacte UTC-verzendtijdstip van de herinnering en sla dit op als `timestamptz`.

## Rapportages en Boekhoudkundige Maandgrenzen

Filters zoals "omzet van deze maand" of "bestellingen van vandaag" zijn afhankelijk van tijdzones. Wordt een query uitgevoerd op basis van UTC-dagen, dan vallen transacties die in Nederland tussen 00:00 en 02:00 uur plaatsvinden onder de *vorige* dag. Voor btw-rapportages en accountantscontroles is dit onacceptabel. Bepaal daarom altijd de begin- en eindtijdstippen in de lokale tijdzone van de onderneming en converteer die grenzen naar UTC voor de SQL-query.

## Veelvoorkomende Fouten

**`timestamp` gebruiken in plaats van `timestamptz`.** Hierdoor verdwijnt alle tijdzone-context.

**Factuurdatums opslaan als timestamps.** Waardoor facturen rond middernacht een dag te vroeg worden gedateerd.

**Vaste offsets (`+01:00`) hardcoden.** Waardoor de software een half jaar lang een uur achterloopt door de zomertijd.

**`new Date("YYYY-MM-DD")` parsen in de browser.** Waardoor datums verspringen afhankelijk van de geografische locatie van de bezoeker.

**E-mailbevestigingen sturen zonder tijdzonevermelding.** Vermeld altijd expliciet "10:00 uur (Nederlandse tijd)".

## Hoe LaunchStudio Helpt

LaunchStudio lost datum- en tijdzoneproblemen structureel op in met AI gebouwde applicaties: we auditen en migreren databasekolommen naar de juiste typen (`timestamptz` versus `date`), scheiden kalenderdatums van universele tijdstippen, richten tijdzonebewuste agendaroosters in conform de IANA-database, corrigeren cronjobs en notificatieschema's, optimaliseren boekhoudkundige rapportagegrenzen en leveren geautomatiseerde tests op voor zomertijdovergangen.

Het **Launch Ready**-pakket (€800 - €3.500) omvat complete datum- en tijdzone-sanering naast security hardening en deployment. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt continue monitoring, beheerde hosting en actieve ondersteuning. Bereken eenvoudig uw investering via onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is een initiatief van Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde engineers die dagelijks samenwerken over kantoren in Amsterdam, Singapore en Ho Chi Minh City - waar tijdzonebeheer een tweede natuur is. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de softwareontwikkeling vindt plaats in ons ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Rijschool-App Die Alle Lessen een Uur Verschoof

Ricardo Fernandes bouwde Rijlesplanner met Lovable en Supabase: een plannings- en facturatiesysteem voor autorijscholen, waarmee instructeurs hun lesroosters publiceren, leerlingen rijlessen boeken, automatische herinneringen ontvangen en rijscholen maandelijks factureren. Op de maandagochtend direct na de start van de zomertijd brak er complete chaos uit: tientallen leerlingen kwamen een vol uur te laat opdagen voor hun les, terwijl instructeurs elders een uur voor een dichte deur stonden te wachten.

Een spoedinspectie bracht meerdere opeengestapelde tijdzonefouten aan het licht. Wekelijkse terugkerende beschikbaarheid was in de database opgeslagen als een statische UTC-tijd; door de verzetting van de klok van UTC+1 naar UTC+2 schoof elk gegenereerd lesuur lokaal automatisch zestig minuten op. De tabel `lessons` gebruikte bovendien `timestamp without time zone`, wat in de browser werd geïnterpreteerd als lokale tijd maar in de achtergrondfunctie voor herinneringen als UTC, waardoor sms-alerts een uur te vroeg arriveerden. De herinneringscronjob draaide op een vast UTC-uur (06:00 UTC), wat in de winter 07:00 uur Nederlandse tijd betekende en in de zomer 08:00 uur. Maandfacturen werden gegenereerd via `toISOString()`, waardoor lessen gereden op de eerste van de maand om 00:30 uur op de factuur van de voorgaande maand belandden.

LaunchStudio migreerde alle lestijden zorgvuldig naar `timestamptz` met behoud van de historische integriteit en sloeg de IANA-tijdzone (`Europe/Amsterdam`) expliciet op per rijschool. Terugkerende beschikbaarheid werd omgezet naar lokale tijdregels die dynamisch worden berekend met tijdzonebewuste PostgreSQL-functies. Herinneringen worden nu bij de boeking direct berekend als het exacte universele UTC-moment en verwerkt door een worker die elke vijf minuten draait. Factuurdatums werden gemigreerd naar echte `date`-kolommen en geautomatiseerde testsuites verifiëren nu standaard de klokwisselingen in maart en oktober.

**Resultaat:** De najaarsovergang naar de wintertijd en de start van de zomertijd het jaar erop verliepen vlekkeloos zonder een enkele verschoven les. Het aantal supportvragen over onjuiste tijden daalde van tientallen per maand naar nul.

> *"Ik had werkelijk nooit stilgestaan bij tijdzones omdat al mijn rijscholen en leerlingen gewoon in Nederland zitten. Totdat bleek dat Nederland functioneel twee verschillende tijdzones per jaar hanteert."*
> - **Ricardo Fernandes, Oprichter, Rijlesplanner (Tilburg)**

**Kosten & Doorlooptijd:** €2.900 (Launch Ready-pakket: kolommigraties, tijdzonebewuste planning, herontwerp van herinneringen, factuur- en rapportagedatum-fixes en edge-case tests) - afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Moet ik alle tijden standaard in UTC opslaan?

Sla specifieke tijdstippen (instants zoals logins, betalingen en lesmomenten) altijd op als `timestamptz` (wat PostgreSQL intern in UTC bewaart). Sla pure kalenderdatums (zoals verjaardagen en factuurdatums) echter altijd op als `date`. Sla terugkerende lokale roosters op met een IANA-tijdzonenaam.

### Waarom verschuiven afspraken in mijn app twee keer per jaar met een uur?

Dit gebeurt wanneer tijden worden opgeslagen met een vaste UTC-offset (zoals `+01:00`) of als statische UTC-tijd. Hierdoor wordt geen rekening gehouden met de overgang tussen zomertijd en wintertijd. Het opslaan van de tijdzone `Europe/Amsterdam` en het dynamisch berekenen van het tijdstip lost dit direct op.

### Waarom worden mijn facturen soms op de vorige dag gedateerd?

Dit ontstaat meestal wanneer een lokale middernachtelijke tijd via JavaScript `toISOString()` wordt omgezet naar UTC. Een factuur op 1 juli om 00:30 uur wordt dan `22:30:00Z` op 30 juni. Sla factuurdatums altijd op als platte `YYYY-MM-DD` strings in een `date`-kolom.

### Hoe helpt de ervaring van Manifera bij tijdzoneproblemen?

Manifera ontwikkelt al meer dan 11 jaar internationale softwaresystemen en werkt dagelijks over drie verschillende tijdzones (Nederland, Singapore en Vietnam). LaunchStudio zet deze praktijkkennis in om tijdzonefouten structureel in de database en backend op te lossen.

### Beïnvloeden datumfouten de reputatie en vindbaarheid van mijn SaaS?

Jazeker. Gemiste afspraken en foutieve facturen leiden direct tot klachten en negatieve beoordelingen. Betrouwbare planningssoftware bouwt daarentegen een sterke reputatie op, wat resulteert in positieve vertrouwenssignalen voor klanten en AI-zoeksystemen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik alle tijden standaard in UTC opslaan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Instants als timestamptz in UTC, kalenderdatums als date, en terugkerende regels met een IANA-tijdzone zoals Europe/Amsterdam." }
    },
    {
      "@type": "Question",
      "name": "Waarom verschuiven afspraken in mijn app twee keer per jaar met een uur?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vaste UTC-offsets negeren de zomertijd; koppel lokale afspraken aan IANA-tijdzones en bereken UTC dynamisch." }
    },
    {
      "@type": "Question",
      "name": "Waarom worden mijn facturen soms op de vorige dag gedateerd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Lokale tijden rond middernacht verschuiven naar de vorige dag door toISOString(); gebruik date-kolommen zonder tijd." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij tijdzoneproblemen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera werkt dagelijks over drie internationale tijdzones en bouwt al 11+ jaar robuuste tijdzonebewuste softwaresystemen." }
    },
    {
      "@type": "Question",
      "name": "Beïnvloeden datumfouten de reputatie en vindbaarheid van mijn SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, betrouwbare agenda's en correcte facturen voorkomen negatieve reviews en versterken de betrouwbaarheidsscore bij AI-zoekmachines." }
    }
  ]
}
</script>
