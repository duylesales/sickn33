---
Titel: "Lovable Supabase: Tijdzones en Datums Correct Inrichten"
Trefwoorden: lovable supabase tijdzones, timestamptz postgres, zomertijd wintertijd software, datumverwerking saas, ai app security, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Lovable Supabase: Tijdzones en Datums Correct Inrichten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Tijdzones en Datums Correct Inrichten",
  "description": "Datum- en tijdfouten blijven maandenlang onzichtbaar en slaan dan plotseling voor iedereen tegelijk toe. Hoe je absolute tijdstippen opslaat, waarom zomertijd herhalende afspraken sloopt en het cruciale verschil tussen een moment en een kalenderdag.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/95-lovable-supabase-time-zones-and-dates-done-correctly" }
}
</script>

Bugs met datum- en tijdfuncties hebben een heel typerend patroon. Maandenlang lijkt alles vlekkeloos te functioneren. Vervolgens, op die ene specifieke zondag in maart of oktober, verschuift een hele reeks afspraken plotseling met één uur, bestrijkt een nachtelijke rapportage de verkeerde dag en ontvangen tientallen verbaasde klanten een automatische herinnering op een volstrekt onlogisch tijdstip.

Niemand heeft code gewijzigd. Dat maakt dit de meest desoriënterende categorie bugs in moderne software, en het is de reden waarom deze fouten vrijwel altijd worden ontdekt door een gefrustreerde klant in plaats van door jouzelf.

De onderliggende oorzaak is steevast dezelfde: een applicatie die 'tijd' behandelt als één homogeen gegeven, terwijl het in werkelijkheid om drie fundamenteel verschillende concepten gaat.

## Drie fundamenteel verschillende concepten die we 'datum' noemen

**1. Een absoluut tijdstip (een instant).** Een specifiek moment in de tijd dat overal ter wereld op exact hetzelfde ogenblik plaatsvindt: het moment waarop een betaling is ontvangen, een database-rij is gewijzigd of een chatbericht is verstuurd. Twee waarnemers in verschillende tijdzones zijn het er feitelijk 100% over eens.

**2. Een kalenderdag.** Een datum zónder enig tijdstip erin: een geboortedatum, een factuurdatum of een officiële feestdag. Dit is géén specifiek moment. Zodra je hier een tijd aan koppelt, introduceer je direct een bug.

**3. Een lokale kloktijd (wall-clock time).** *"De zwemles vindt plaats op dinsdagochtend om negen uur."* Dit is een beschrijving van wat de fysieke klok aan de muur aangeeft op een specifieke geografische locatie. Het absolute tijdstip waarnaar dit verwijst verandert zodra de klok verzet wordt.

Applicaties gaan de mist in door alle drie deze varianten op exact dezelfde manier op te slaan. De gouden regel: sla absolute tijdstippen op mét tijdzone, sla kalenderdagen op als pure datums (`DATE`), en sla herhalende lokale afspraken op als een kloktijd plus de bijbehorende tijdzone in plaats van als een vast absoluut moment.

## Sla tijdstippen altijd op mét tijdzone (`timestamptz`)

In PostgreSQL (en dus Supabase) betekent dit dat je kiest voor `timestamptz` in plaats van `timestamp`. Dat onderscheid is oneindig veel belangrijker dan de namen doen vermoeden.

Een `timestamptz` legt een objectief, universeel tijdstip vast. Ongeacht in welke offset of tijdzone de data binnenkomt, het wordt intern eenduidig opgeslagen in UTC, en elke lezer krijgt exact hetzelfde moment te zien. Een reguliere `timestamp` (zonder tijdzone) slaat louter losse cijfers op zonder enige context wat ze betekenen — een waarde vastgelegd door een server in Frankfurt en gelezen door een browser in Londen wordt daardoor simpelweg geraden.

Door AI gegenereerde databaseschema's produceren vrijwel standaard de kale `timestamp`-versie, omdat het verschil onzichtbaar blijft zolang iedereen zich toevallig in dezelfde tijdzone bevindt. Controleer je databasekolommen. Als je absolute gebeurtenissen opslaat in gewone `timestamp`-velden, vereist het converteren naar `timestamptz` zorgvuldige datamigratie: je moet bepalen in welke tijdzone historische rijen zijn aangemaakt, en het eerlijke antwoord is soms dat je dat voor records van vóór afgelopen maart niet met zekerheid kunt vaststellen.

De architectuurregel: **sla alles op in UTC, converteer uitsluitend voor de weergave, en doe die conversie zo dicht mogelijk bij de gebruiker** (in de browser of client-app). De database en je backend werken in één consistent frame; alleen de interface toont lokale tijd.

## De specifieke Nederlandse valkuilen die pijn doen

Er zijn twee specifieke factoren die achter vrijwel alle tijdfouten in Nederlandse SaaS-producten zitten:

**Nederland kent zomertijd en wintertijd.** De tijdsverschuiving ten opzichte van UTC is UTC+1 in de winter en UTC+2 in de zomer (Midden-Europese Tijd / MET vs. Midden-Europese Zomertijd / MEZT). Een systeem dat ooit hardcoded `+1 uur` heeft ingesteld, loopt ruwweg de helft van het jaar een vol uur achter — en de fout valt niet op als je in december test.

**De klokovergang vindt plaats op een vast moment in de vroege ochtend op zondag in maart en oktober.** In het voorjaar bestaat het lokale uur tussen 02:00 en 03:00 niet; in het najaar gebeurt datzelfde uur twee keer. Een nachtelijke cron-job die op dat tijdstip staat ingesteld wordt óf overgeslagen óf draait twee keer achter elkaar. En elke periodieke afspraak die als vast tijdstip is opgeslagen, verschuift een uur.

De praktische consequentie voor een reserverings- of planningssysteem: een afspraak gedefinieerd als *"elke dinsdag om 09:00 uur"* moet worden opgeslagen als lokale tijd plus tijdzone (`Europe/Amsterdam`), waarbij het absolute tijdstip voor elke afzonderlijke sessie dynamisch wordt berekend. Sla je de eerste les op als een absoluut moment en tel je daar steeds 7 dagen bij op, dan zitten alle lessen na de klokverzetting er een uur naast — en de klanten die dat ontdekken zijn degene die een uur te vroeg voor een dichte deur staan.

## Kalenderdagen zijn géén tijdstippen

De tweede meest voorkomende fout, en gelukkig het eenvoudigst op te lossen:

Een geboortedatum, een factuurdatum of een officiële feestdag hebben géén uren of minuten. Sla je een geboortedatum op als een timestamp om middernacht (`2026-05-15 00:00:00 UTC`), dan zorgt een conversie naar een tijdzone ten westen van Greenwich ervoor dat de datum verspringt naar `2026-05-14 23:00:00`. Gevolg: een factuur gedateerd op 31 mei verschijnt op het scherm als 30 mei, en een verjaardag klopt niet meer.

Gebruik in PostgreSQL het datatype `DATE`. Een `DATE` kent geen tijdzones en participeert niet in conversies — exact wat je wilt.

Een verwant knelpunt: een rapportageperiode zoals *"de maand september"* is een reeks lokale dagen in een specifieke tijdzone. Als je maandoverzichten in UTC berekent tegen lokale administratieve verwachtingen, vallen transacties van de vroege ochtend of late avond op de verkeerde maand. Bepaal expliciet in welke tijdzone rapportagegrenzen liggen en pas dat consequent toe.

## Geplande taken (cron jobs) en het uur dat niet bestaat

Achtergrondtaken vereisen speciale aandacht:

Plan geplande taken bij voorkeur buiten de overgangsuren (tussen 02:00 en 03:00) — plan nachtelijke taken bijvoorbeeld om 01:00 of 04:00 uur lokale tijd. Maak taken te allen tijde idempotent: zorg dat een job die per ongeluk twee keer draait niet twee keer een factuur verstuurt of een incasso uitvoert. Registreer elke uitvoering in een logtabel, zodat een overgeslagen taak direct opvalt.

Wees expliciet over de tijdzone van je taakplanner. Een cron-job ingesteld op `02:00` op een hostingplatform dat in UTC draait, start in Nederland om 03:00 (wintertijd) of 04:00 (zomertijd).

## Tijd helder communiceren naar gebruikers

Drie eenvoudige keuzes die direct supportvragen voorkomen:

**Toon tijden standaard in de lokale tijdzone van de bezoeker, én vermeld de tijdzone expliciet.** *"14:00 uur (Amsterdam)"* kost geen extra moeite en ontneemt elke verwarring bij grensoverschrijdend gebruik.

**Gebruik relatieve aanduidingen voor recente gebeurtenissen.** *"20 minuten geleden"* is universeel begrijpelijk en immuun voor tijdzoneverschillen.

**Laat gebruikers hun voorkeurstijdzone handmatig instellen** in plaats van uitsluitend te vertrouwen op de browserdetectie. Mensen reizen: een Nederlandse fysiotherapeut die tijdens een vakantie in het buitenland zijn agenda voor volgende week bekijkt, wil niet dat al zijn afspraken een uur verschuiven.

## Looptijden, deadlines en werkdagen

Naast tijdzones is er een tweede categorie datumvalkuilen die leidt tot zakelijke geschillen:

**"Binnen 30 dagen" is dubbelzinnig totdat je het definieert.** Dertig kalenderdagen vanaf dit exacte moment, of vanaf het begin van de volgende dag? Eindigt de dertigste dag om 23:59:59 uur, en in welke tijdzone? Betalingstermijnen, wettelijke bedenktermijnen en opzegtermijnen zijn deadlines waar vroeg of laat discussie over ontstaat; zorg dat de code exact aansluit op je algemene voorwaarden.

**Werkdagen zijn geen kalenderdagen.** Een Nederlandse B2B-applicatie die toezegt binnen *"twee werkdagen"* te reageren, moet weten dat zaterdag en zondag niet meetellen, en officiële feestdagen evenmin. Nederlandse feestdagen liggen niet vast: Pasen en Pinksteren verspringen jaarlijks, Koningsdag valt op 27 april tenzij dat een zondag is (dan 26 april), en Hemelvaartsdag verschuift mee. Sla een officiële feestdagenkalender op als een beheersbare databasetabel in plaats van een hardcoded lijstje in een JavaScript-functie.

## Tijdbeheer consistent en vlekkeloos inrichten

Voor een actieve applicatie is dit een afgebakend en dankbaar project: `timestamp`-kolommen migreren naar `timestamptz` met gedocumenteerde interpretatie van historische data, kalenderdagen omzetten naar `DATE`, herhalende afspraken opslaan als lokale kloktijd met tijdzone, rapportagegrenzen eenduidig definiëren, achtergrondtaken idempotent maken, en de frontend voorzien van eenduidige tijdzonelabels en gebruikersvoorkeuren.

LaunchStudio voert deze normalisatieslag uit zonder verstoring van je live-applicatie. De software engineers zijn van Manifera: elf jaar ervaring met productiesystemen die simultaan opereren over Amsterdam Herengracht 420, Singapore en Ho Chi Minhstad — drie verschillende tijdzones, wat direct verklaart waarom we dit onderwerp zo scherp beheersen.

[Vertel ons waar de datums in jouw product haperen](https://launchstudio.eu/nl/#contact) voor een gerichte analyse binnen één werkdag, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Elke buitenlandse cliënt, één uur te vroeg

Noortje Haan bouwde met Lovable het platform Trainingsschema: online coaching en afsprakenplanning voor veertien personal trainers en fysiopraktijken in Utrecht en Amersfoort. Circa een derde van hun cliënten woont in het buitenland — Nederlandse expats die na hun verhuizing hun vertrouwde coach aanhielden.

Sessies werden in Supabase opgeslagen als platte `timestamp` (zonder tijdzone). Tijden werden in de interface letterlijk getoond zoals ze in de database stonden, zonder tijdzonelabel. Wekelijks terugkerende afspraken werden gegenereerd door de eerste sessie op te slaan en daar telkens 7 dagen bij op te tellen.

Drie afzonderlijke ontwerpfouten versterkten elkaar: Cliënten in het buitenland zagen de Nederlandse kloktijd zonder enige toelichting. Een cliënte in Portugal verscheen daardoor vier maanden lang elke week een uur te laat en dacht dat ze zich telkens vergiste. Na de klokverzetting in maart verschoven alle herhalende sessies in de database met een uur ten opzichte van de papieren agenda van de trainers; veertien trainers waren twee weken lang handmatig afspraken aan het herstellen en één trainer verloor twee cliënten door gemiste sessies. En het wekelijkse omzetoverzicht dat trainers op maandagochtend ontvingen werd berekend in UTC, waardoor trainingen op zondagavond werden meegenomen in het rapport van de vólgende week — wat al maanden zorgde voor onverklaarbare afwijkingen met de eigen boekhouding.

In acht werkdagen werd de tijdlaag structureel gesaneerd: databasekolommen werden gemigreerd naar `timestamptz`, waarbij historische records na afstemming met de trainers eenduidig werden geïnterpreteerd als Nederlandse lokale tijd; herhalende sessies werden geherstructureerd naar lokale kloktijd met expliciete tijdzone (`Europe/Amsterdam`), waarbij elk afzonderlijk sessiemoment dynamisch wordt berekend zodat klokwisselingen geen effect meer hebben; tijden worden in de webapp getoond in de tijdzone van de bezoeker met een duidelijk label en een instelbare voorkeur; het wekelijkse omzetrapport werd verankerd op Nederlandse kalenderdagen; geplande taken werden verplaatst naar veilige nachtelijke tijdstippen met audit logging; en er werd een testsuite toegevoegd die de klokovergangen in maart en oktober automatisch simuleert.

**Resultaat:** Nul klachten over afspraken tijdens de daaropvolgende overgangen naar zomer- en wintertijd — de eerste keer in het bestaan van het platform dat een klokwisseling geruisloos verliep. De Portugese cliënte werd geïnformeerd over de softwarefout en bleef tevreden klant.

> *"Een cliënte in Portugal logde vier maanden lang elke week een uur te laat in en gaf zichzelf de schuld. Mijn applicatie toonde simpelweg een getal zonder enig idee wat voor tijd het werkelijk was."*
> — **Noortje Haan, Oprichter, Trainingsschema (Utrecht)**

**Kosten & Doorlooptijd:** € 3.800 (databasemigratie naar timestamptz met historische datacorrectie, herstructurering herhalende afspraken, tijdzoneweergave en voorkeuren, rapportagekalender, idempotente cron-jobs, zomertijd-testsuite) — opgeleverd in 8 werkdagen.

## Veelgestelde vragen

### Welk datatype moet ik in Supabase gebruiken voor tijdstippen?

Gebruik `timestamptz` voor elk specifiek moment in de tijd (zoals transacties, logins of aanmaakdatums), zodat de waarde eenduidig in UTC wordt opgeslagen. Gebruik het type `DATE` voor kalenderdagen zonder tijd (zoals geboortedatums en factuurdatums), zodat ze niet onbedoeld converteren.

### Waarom verschuiven herhalende afspraken wanneer de klok verzet wordt?

Omdat de herhaling is opgeslagen als een vast absoluut tijdstip waarbij telkens zeven dagen worden opgeteld. *"Elke dinsdag om 09:00 uur"* is een lokale kloktijd. Sla de lokale tijd op inclusief de bijbehorende tijdzone (`Europe/Amsterdam`) en bereken het absolute tijdstip voor elke sessie afzonderlijk.

### Waarom verschijnt een factuur van 31 mei soms als 30 mei op het scherm?

Omdat een kalenderdag per ongeluk is opgeslagen als een timestamp om middernacht (`00:00:00 UTC`). Bij weergave in een andere tijdzone verspringt het tijdstip naar de voorafgaande avond. Sla factuurdatums altijd op als puur `DATE`-type.

### Waar moet ik op letten bij geplande achtergrondtaken (cron jobs)?

Vermijd het overgangsuur tussen 02:00 en 03:00 uur op zondagochtend (dat uur bestaat in het voorjaar niet en komt in het najaar twee keer voor). Maak taken altijd idempotent zodat dubbele uitvoering geen kwaad kan, en definieer expliciet welke tijdzone de planning volgt.

### Hoe horen tijden getoond te worden aan eindgebruikers?

Standaard in de lokale tijdzone van de bezoeker met een expliciet tijdzonelabel erbij — bijvoorbeeld *"14:00 uur (Amsterdam)"*. Gebruik relatieve tekst (*"15 minuten geleden"*) voor recente gebeurtenissen en geef gebruikers de optie om hun tijdzone handmatig in te stellen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Welk datatype moet ik in Supabase gebruiken voor tijdstippen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "timestamptz voor absolute momenten zodat ze eenduidig in UTC worden opgeslagen, en DATE voor kalenderdagen zonder tijdstip."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verschuiven herhalende afspraken wanneer de klok verzet wordt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat ze zijn opgeslagen als absolute momenten plus zeven dagen. Sla de lokale kloktijd met tijdzone op en bereken elk sessiemoment dynamisch."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verschijnt een factuur van 31 mei soms als 30 mei op het scherm?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een kalenderdag is opgeslagen als een timestamp om middernacht en door tijdzoneconversie een dag terugvalt. Gebruik het type DATE."
      }
    },
    {
      "@type": "Question",
      "name": "Waar moet ik op letten bij geplande achtergrondtaken (cron jobs)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vermijd de overgangsuren tussen 02:00 en 03:00, maak taken idempotent, houd logs bij en wees expliciet over de gehanteerde tijdzone."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe horen tijden getoond te worden aan eindgebruikers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In de lokale tijdzone van de gebruiker met een duidelijke aanduiding (bijv. Amsterdam), met relatieve bewoording voor recente events en een instelbare voorkeur."
      }
    }
  ]
}
</script>
