---
Titel: "Lovable Supabase: Schemanaamgeving Waar U Geen Spijt van Krijgt"
Trefwoorden: lovable supabase, schemaontwerp, naamgevingsconventies, databasemodellering, technische schuld, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable Supabase: Schemanaamgeving Waar U Geen Spijt van Krijgt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Schemanaamgeving Waar U Geen Spijt van Krijgt",
  "description": "Een door AI gebouwde database verzamelt drie namen voor hetzelfde idee. Waarom inconsistente naamgeving elke latere wijziging duur maakt, welke conventies het waard zijn om vroeg vast te leggen, en hoe u hernoemt zonder downtime.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-schema-naming-you-will-not-regret" }
}
</script>

Open de tabellenlijst van een Lovable-project dat een jaar lang is uitgebreid en u vindt `users`, `profiles`, `user_profiles` en `customer`. Drie ervan hebben een naamkolom, op drie manieren gespeld. Eén is leeg en niemand weet nog waarom hij bestaat.

Dat is geen slordigheid. Het is wat er gebeurt wanneer een schema verzoek voor verzoek wordt opgebouwd door een tool zonder geheugen van de eerdere verzoeken, waarvan elk op zichzelf iets redelijks opleverde. Het resultaat is een database waarin u, om te weten hoe iets heet, moet weten wanneer het werd toegevoegd.

Het doet ertoe om één praktische reden. Elke toekomstige wijziging - door u, door een opdrachtnemer, door een andere AI-sessie - begint met begrijpen wat er staat, en een inconsistent schema maakt dat elke keer opnieuw duur.

## Wat Inconsistentie Werkelijk Kost

Drie kostenposten, en de derde is degene die oprichters voelen.

Queries worden gokwerk: heet de kolom `created_at`, `createdAt`, `date_created` of `inserted_at`? Elke join moet worden gecontroleerd in plaats van gekend, en fouten zijn stil wanneer er twee vergelijkbaar genoemde kolommen bestaan.

Tooling gaat achteruit. Gegenereerde types, beheerpanelen en API-lagen lezen allemaal uw schema, en wat ze opleveren weerspiegelt wat ze vinden. Inconsistente invoer, inconsistente uitvoer, bij elke afnemer.

En AI-ondersteuning wordt slechter, en dat is degene die zich opstapelt. Een agent die aan een schoon schema werkt, leidt het patroon af en volgt het. Een agent die aan een inconsistent schema werkt, heeft geen patroon om te volgen, dus verzint hij een vierde conventie - en volgend kwartaal hebt u er vier. Het schema leert degene die er daarna aan werkt, inclusief de machine.

## Conventies Die het Overnemen Waard Zijn

Elke consistente set is beter dan een inconsistente. Hebt u geen voorkeur, dan zijn deze gebruikelijk in Postgres en verrassen ze niemand.

**Tabellen in het meervoud, in kleine letters, woorden gescheiden door underscores:** `invoices`, `project_members`. Hoofdletters in Postgres vereisen voor altijd aanhalingstekens, een klein ongemak dat zich herhaalt zolang het product bestaat.

**Primaire sleutel heet `id`.** Foreign keys genoemd naar waar ze naar verwijzen plus `_id`: `organisation_id`, `invoice_id`. Een join die u kunt schrijven zonder iets op te zoeken.

**Tijdstempels `created_at` en `updated_at`**, altijd met tijdzone, altijd in UTC. Nooit een kale datum-tijd zonder zone; de dag dat uw eerste klant in een ander land verschijnt, is de dag dat die beslissing u geld kost.

**Booleans positief geformuleerd:** `is_active` in plaats van `is_not_disabled`. Negatieve namen leveren dubbele ontkenningen op in queries en een fout die niemand ziet bij het lezen.

**Eén naam per concept in het hele schema.** Als de entiteit een organisatie is, is ze nooit ook een bedrijf, een account of een tenant. Kies het woord dat uw klanten gebruiken en gebruik het overal, ook in uw code en interface.

## Zeg Wat een Kolom Betekent, Niet Wat Ze Bevat

De namen die de meeste problemen veroorzaken, zijn de vage: `status`, `type`, `data`, `value`, `flag`.

Een kolom die `status` heet op vijf tabellen betekent vijf verschillende dingen, en de query die er twee van samenvoegt, is onleesbaar. `invoice_status`, of beter, een naam die de werkelijke dimensie beschrijft - `payment_state`, `approval_state` - is de extra tekens waard.

Dezelfde zorg bij bedragen. `amount` roept de vraag op die iedereen uiteindelijk op het verkeerde moment stelt: is het in euro's of in centen, en is het inclusief btw? `amount_cents_excl_vat` is lelijk en beantwoordt de vraag voorgoed. Geld opgeslagen als kommagetal (float) is een artikel op zich; sla het op als geheel getal in de kleinste eenheid of als decimaal, nooit als float.

En vermijd kolommen waarvan de betekenis afhangt van de waarde van een andere kolom. Een `value`-kolom met een getal als `type` het ene is en een datum als het iets anders is, is een ontwerp dat niet kan worden begrensd, geïndexeerd of vertrouwd.

## De Structurele Problemen Achter de Namen

Soms zijn slechte namen een symptoom. Drie patronen zijn het waard om naar te zoeken als u er toch mee bezig bent.

**Gedupliceerde entiteiten.** `users`, `profiles` en `customers` die allemaal een naam en een e-mailadres bevatten, betekent dat dezelfde persoon drie keer bestaat en het met zichzelf oneens kan zijn. Eén tabel, met de extra velden waar ze horen.

**Kommagescheiden lijsten in een tekstkolom.** Een `tags`-kolom met "urgent,finance,q3" kan niet worden geïndexeerd, betrouwbaar gefilterd of begrensd. Het moet een eigen tabel zijn, en het later omzetten is meer werk dan het nu doen.

**Ontbrekende foreign keys.** Een `organisation_id`-kolom die niet als foreign key is gedeclareerd, staat rijen toe die verwijzen naar organisaties die niet bestaan, en door AI gegenereerde schema's laten die declaratie regelmatig weg. Ze toevoegen vindt de wezen die u al hebt, wat onprettig is en beter dan het niet weten.

## Hernoemen Zonder Iets te Breken

De reden dat mensen met slechte namen leven, is angst voor het hernoemen, en die angst is terecht als u het in één stap doet.

De veilige volgorde heeft vier fasen en geen downtime. Voeg de nieuwe kolom toe. Pas de applicatie aan om naar zowel de oude als de nieuwe te schrijven, en vul de bestaande rijen aan. Zet elke leesactie om naar de nieuwe kolom en deploy. Verwijder de oude dan, als u zeker bent, in een latere release.

Hetzelfde werkt voor tabellen: maak de nieuwe aan, schrijf naar beide, zet het lezen om, verwijder de oude. Voor een klein product is elke fase minuten werk, en op geen enkel moment zijn de draaiende code en de database het oneens.

Wat u moet vermijden, is ter plekke hernoemen terwijl de vorige versie van uw applicatie nog draait - de klassieke manier om een product plat te leggen tijdens een deploy die triviaal leek.

## Hoe Ver Het de Moeite Waard Is

U hoeft niet alles te repareren, en een oprichter met klanten moet geen week aan netheid besteden.

Prioriteer op wat u aanraakt. De tabellen achter uw hoofdschermen, de tabellen die een opdrachtnemer als eerste tegenkomt, en alles waarop u op het punt staat verder te bouwen: repareer die. Een verouderde tabel, één keer geschreven door een functie die niemand gebruikt, mag zijn vreemde namen voor altijd houden.

De andere prioritering is op gevaar. Dubbelzinnige geldkolommen, ontbrekende foreign keys, tijdstempels zonder tijdzone en gedupliceerde entiteiten zijn correctheidsproblemen in een naamgevingskostuum. Die zijn het waard om te repareren, ongeacht hoe vaak u ernaar kijkt.

## Schrijf Het Op Waar de Tools Het Vinden

Zodra er conventies zijn, leg ze vast in de repository - een kort bestand, tien regels, met de regels.

Dat zorgt ervoor dat ze overleven. Een menselijke opdrachtnemer leest het. Een AI-assistent leest het ook, als uw project een bestand met regels of instructies bijhoudt, en het verschil in wat een codeeragent oplevert wanneer hij de conventies heeft meegekregen, is substantieel en direct.

Neem de woordenschat op naast de syntaxis: de woorden die uw product voor zijn concepten gebruikt, en de woorden die het bewust niet gebruikt. Die ene alinea voorkomt dat het vierde synoniem wordt geïntroduceerd.

## Identificaties: De Keuze Die U Eén Keer Maakt

Eén schemabeslissing is echt moeilijk terug te draaien, en AI-tools nemen haar voor u zonder het te noemen: wat uw primaire sleutels zijn.

Oplopende gehele getallen zijn compact, sorteren vanzelf en lezen makkelijk in een supportgesprek. Ze verraden ook uw volume - een klant wiens factuur nummer 412 heeft, weet ongeveer hoeveel facturen u hebt uitgegeven - en ze maken identificaties te raden, wat ertoe doet voor alles wat in een URL verschijnt.

Willekeurige identificaties zoals UUID's lekken niets en kunnen door de client worden gegenereerd voordat een rij bestaat, wat sommige processen vereenvoudigt. De oudere willekeurige varianten verspreiden schrijfacties over een index, wat bij grote tabellen pijn doet; de nieuwere, op tijd geordende varianten vermijden dat en zijn de verstandige standaard voor een nieuw project.

De praktische middenweg waar de meeste producten uiteindelijk naartoe willen: een willekeurige identificatie als primaire sleutel, plus een aparte referentie voor mensen bij dingen waar mensen over praten - een factuurnummer, een ticketnummer, een bestelcode - gegenereerd uit een eigen teller en zo opgemaakt dat het goed is voor te lezen aan de telefoon.

Beslis dit vroeg, want het type van een primaire sleutel veranderen op een tabel met echte data en meerdere foreign keys die ernaar verwijzen, is een van de weinige migraties die echt pijnlijk is in plaats van alleen tijdrovend.

## Dit Inrichten

Voor een bestaand project kost dit doorgaans één tot twee dagen: een volledige inventarisatie van tabellen en kolommen met duplicaten en synoniemen benoemd, een gekozen conventie gedocumenteerd in de repository, drukbezochte tabellen hernoemd via de volgorde toevoegen-naar-beide-schrijven-omzetten-verwijderen, gedupliceerde entiteiten samengevoegd, kommagescheiden lijsten genormaliseerd naar eigen tabellen, ontbrekende foreign keys gedeclareerd met wezen opgelost, tijdstempels gecorrigeerd naar UTC met tijdzone, geldkolommen voorzien van ondubbelzinnige namen en het juiste type, en gegenereerde types en beheertooling opnieuw gegenereerd zodat alles stroomafwaarts het nieuwe schema weerspiegelt.

LaunchStudio doet dit bij het overnemen van een door AI gebouwde codebase, omdat elk ander stuk werk daarna sneller gaat. De engineers zijn van Manifera: elf jaar, 160+ projecten, en heel veel schema's geërfd van iemand anders.

[Stuur ons uw tabellenlijst](https://launchstudio.eu/nl/#contact) en wij vertellen u waar de duplicaten zitten.

## Echt voorbeeld

### Drie Tabellen, Eén Klant

Barend Kloosterman bouwde Serviceplan in Lovable: administratie van onderhoudscontracten voor installatiebedrijven, 44 bedrijven die samen zo'n 9.000 serviceadressen beheren.

In veertien maanden was het schema gegroeid tot 31 tabellen. Klanten stonden in drie ervan: `clients` uit de oorspronkelijke bouw, `customers` toegevoegd toen facturatie erbij kwam, en `contacts` toegevoegd voor het portaal. Elk bevatte een naam en een e-mailadres; twee bevatten een telefoonnummer, in verschillend genoemde kolommen, met een verschillende opmaak.

De fout die het werk afdwong: een installateur paste het adres van een klant aan in het portaal, de factuur die die avond werd gegenereerd had het oude adres, en de servicemonteur werd naar een derde adres gestuurd dat ergens anders stond. Drie tabellen, drie antwoorden, en geen manier om te zeggen welk juist was.

Vier werkdagen: een volledige schema-inventarisatie met elk duplicaat en synoniem benoemd; een conventiebestand gecommit in de repository over naamgeving van tabellen en kolommen, tijdstempels, booleans, geld en de woordenschat van het product; de drie klanttabellen samengevoegd tot één `customers`-tabel met een contactentabel eronder, gemigreerd via de volgorde toevoegen-naar-beide-schrijven-omzetten-verwijderen zonder downtime; elf kolommen hernoemd voor consistentie; een kommagescheiden tekstkolom `services` genormaliseerd naar een echte tabel met een join; negen ontbrekende foreign keys gedeclareerd, wat 340 verweesde servicerecords blootlegde die werden beoordeeld en opnieuw gekoppeld of gearchiveerd; vier tijdstempelkolommen omgezet naar tijdzonebewust; twee `amount`-kolommen hernoemd en omgezet van kommagetal naar gehele getallen in de kleinste eenheid, wat een al lang bestaand verschil van één cent in factuurtotalen oploste; en gegenereerde types opnieuw gegenereerd in de hele applicatie.

**Resultaat:** de fout met de drie adressen werd structureel onmogelijk. Barend vertelt dat het waardevollere resultaat de snelheid van veranderen was - een opdrachtnemer die hij de maand erna inhuurde, was op dag één productief in plaats van twee dagen te vragen welke tabel leidend was, en zijn AI-sessies stopten met het verzinnen van nieuwe kolomnamen omdat het conventiebestand nu deel uitmaakt van de projectinstructies.

> *"Ik had drie tabellen met klanten omdat ik elke keer dat ik om een functie vroeg een nieuwe tabel kreeg, en elke tabel was een redelijk antwoord op de vraag die ik die dag had gesteld."*
> - **Barend Kloosterman, Oprichter, Serviceplan (Doetinchem)**

**Kosten & Doorlooptijd:** €3.400 (schema-inventarisatie, documentatie van conventies, samenvoegen van entiteiten met migratie zonder downtime, normalisatie, herstel van foreign keys, correcties van tijdstempel- en geldtypes, opnieuw genereren van types) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Doet naamgeving er echt toe als de app werkt?

Het doet ertoe voor elke wijziging hierna. Een inconsistent schema vertraagt mensen, verslechtert gegenereerde tooling, en zorgt ervoor dat AI-assistenten nog een conventie verzinnen - en zo krijgt u vier namen voor één idee.

### Welke naamgevingsconventie moet ik gebruiken?

Elke consistente. Gebruikelijk in Postgres: tabelnamen in meervoud, kleine letters met underscores, primaire sleutels `id`, foreign keys `ding_id`, `created_at` en `updated_at` met tijdzone, en positief geformuleerde booleans.

### Hoe hernoem ik een kolom zonder downtime?

Voeg de nieuwe toe, schrijf naar beide en vul aan, zet het lezen om en deploy, en verwijder de oude kolom in een latere release. Elke fase is op zichzelf veilig.

### Moet ik het hele schema in één keer repareren?

Nee. Repareer wat u aanraakt - de tabellen achter uw hoofdschermen - plus alles wat gevaarlijk is: dubbelzinnige geldkolommen, ontbrekende foreign keys, tijdstempels zonder zone, gedupliceerde entiteiten.

### Hoe voorkom ik dat de inconsistentie terugkomt?

Schrijf de conventies in een bestand in de repository, inclusief de woordenschat van uw product. Opdrachtnemers lezen het, en codeeragenten ook, wat verandert wat ze genereren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Doet databasenaamgeving ertoe als de app al werkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het raakt elke toekomstige wijziging - de snelheid van mensen, gegenereerde tooling, en wat AI-assistenten opleveren als er geen patroon te volgen is."
      }
    },
    {
      "@type": "Question",
      "name": "Welke naamgevingsconventie moet een Supabase-project gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke consistente. Gebruikelijk: tabellen in meervoud met kleine letters en underscores, id als primaire sleutel, ding_id als foreign key, created_at en updated_at met tijdzone, positieve booleans."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe hernoem ik een kolom zonder downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voeg de nieuwe kolom toe, schrijf naar beide en vul aan, zet het lezen om en deploy, en verwijder de oude kolom in een latere release."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik een heel schema in één keer repareren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - repareer de tabellen die u echt aanraakt, plus wat echt gevaarlijk is: dubbelzinnige geldkolommen, ontbrekende foreign keys, tijdstempels zonder zone, gedupliceerde entiteiten."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat schema-inconsistentie terugkomt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Commit een kort conventiebestand inclusief de woordenschat van uw product. Opdrachtnemers en codeeragenten lezen het allebei, wat verandert wat er wordt gegenereerd."
      }
    }
  ]
}
</script>
