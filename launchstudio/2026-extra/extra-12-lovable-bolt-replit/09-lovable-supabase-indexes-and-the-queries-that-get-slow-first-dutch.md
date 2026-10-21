---
Titel: "Lovable Supabase: Indexen en de Queries Die Als Eerste Traag Worden"
Trefwoorden: lovable supabase, database-indexen, trage queries, Postgres-prestaties, queryplannen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Indexen en de Queries Die Als Eerste Traag Worden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Indexen en de Queries Die Als Eerste Traag Worden",
  "description": "Een door AI gebouwde app is snel met 200 rijen en traag met 200.000. Welke queries het eerst achteruitgaan, hoe u ze in Supabase vindt, de vier indexen die de meeste producten echt nodig hebben, en wat een index u kost.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-indexes-and-the-queries-that-get-slow-first" }
}
</script>

Er is niets aan uw app veranderd. U hebt niets uitgerold. Maar de pagina die vroeger direct openging, doet er nu vier seconden over, en het enige verschil is dat u meer klanten hebt dan in het voorjaar.

Dit is het meest voorspelbare prestatieprobleem in software, en het heeft een specifieke oorzaak. Zonder index beantwoordt een database "geef me de rijen waar deze kolom gelijk is aan dat" door elke rij in de tabel te lezen. Bij 200 rijen merkt niemand het. Bij 200.000 is het vier seconden, en bij twee miljoen is het een time-out.

AI-codetools maken tabellen aan en schrijven queries. Ze maken zelden de indexen die die queries nodig hebben, omdat er met de hoeveelheid data tijdens de ontwikkeling niets op te merken valt.

## Vind de Trage Voordat U Gaat Gokken

Voeg geen indexen toe op gevoel. Supabase toont querystatistieken — elk statement dat uw applicatie heeft uitgevoerd, hoe vaak, en hoeveel tijd het in totaal kostte — en dat is de enige eerlijke bron.

Sorteer op totale tijd in plaats van op de traagste afzonderlijke uitvoering. Een query van 900 milliseconden die één keer per dag draait, doet er veel minder toe dan een van 40 milliseconden die bij elke paginalading draait, en oprichters optimaliseren voortdurend de verkeerde omdat het trage getal alarmerender is.

Neem dan uw grootste boosdoener en vraag de database zichzelf uit te leggen. `EXPLAIN ANALYZE` vóór een query zetten geeft het gebruikte plan terug en de tijd die elke stap kostte. U zoekt naar één term: een sequential scan op een grote tabel. Dat betekent dat de hele tabel werd gelezen. Gecombineerd met een filter op één kolom is het een index die erop wacht te worden aangemaakt.

Hetzelfde geldt voor sorteren. Een plan met een dure sorteerstap op een grote resultaatset, gevolgd door een limiet, is een lijstpagina in uw product die elke week slechter wordt.

## De Vier Indexen Die de Meeste Producten Nodig Hebben

Voor een typische Lovable- en Supabase-applicatie dekken er vier het overgrote deel van het probleem.

**Elke foreign key.** Postgres indexeert primaire sleutels automatisch, en indexeert niet de kolommen die ernaar verwijzen. Elke tabel met `user_id`, `organisation_id`, `project_id` heeft er een index op nodig, omdat elke query in uw product op een daarvan filtert. Dit alleen lost de meeste kleine applicaties op.

**De tenantkolom, als eerste.** Is uw app multi-tenant, dan begint bijna elke query met "de rijen die bij deze organisatie horen". Die kolom hoort als eerste in een samengestelde index, met daarna waarop u filtert of sorteert: `(organisation_id, created_at desc)` bedient zowel het filter als de sortering in één structuur.

**Alles waarop u een lijst sorteert.** Meestal `created_at` op de tabellen achter uw hoofdschermen, en meestal samen met de tenantkolom in plaats van alleen.

**Kolommen waarop wordt gezocht met een waarde die gebruikers intypen.** E-mail, referentienummer, slug. Die willen unieke indexen, die zowel het opzoeken versnellen als het duplicaat voorkomen dat u anders in productie ontdekt.

Voeg ze één voor één toe en meet. Een index die een plan niet verandert, is een index waarvoor u betaalt en die u niet gebruikt.

## Wat een Index Kost

Indexen zijn niet gratis, en de afweging is de moeite waard om te begrijpen, omdat de neiging na het bovenstaande is alles te indexeren.

Elke index kost opslag, en belangrijker: elke index moet bij elke insert, update en delete van de geïndexeerde kolom worden bijgewerkt. Een tabel met elf indexen schrijft aanzienlijk trager dan dezelfde tabel met drie. Voor een product dat veel meer leest dan schrijft — de meeste — valt de afweging sterk uit in het voordeel van indexen. Voor een tabel met veel schrijfacties, zoals een event- of logtabel, wees zuinig.

Ongebruikte indexen zijn pure kosten. Postgres houdt bij hoe vaak elke index is gebruikt, en dat na een paar maanden echt verkeer bekijken laat meestal twee of drie zien die speculatief zijn toegevoegd en nooit zijn aangeraakt. Verwijder ze.

## Het Probleem Dat Lijkt op een Trage Database

Controleer voordat u iets toevoegt of uw probleem eigenlijk het aantal queries is in plaats van de snelheid van elke query.

Het patroon: een pagina toont 50 projecten, en voor elk project haalt de code de eigenaar op. Dat zijn 51 queries waar er twee zouden volstaan. Elke query is snel, de pagina is traag, en geen index helpt.

Dit is wijdverbreid in door AI gegenereerde code, omdat het de natuurlijke manier is om de logica uit te drukken — haal de lijst op, en loop er dan doorheen. De oplossing is gerelateerde data in één query op te halen in plaats van in een lus, wat in Supabase betekent dat u de gerelateerde tabel samen met de hoofdtabel selecteert in plaats van de client binnen een lus aan te roepen.

De twee gevallen onderscheiden kost dertig seconden: als uw trage pagina tientallen snelle queries opleverde, is het dit. Als ze er drie trage opleverde, zijn het indexen.

## Tel Zorgvuldig

`SELECT count(*)` op een grote tabel is trager dan mensen verwachten, omdat Postgres echt telt. Op een lijstpagina met paginering kost die telling vaak meer dan het ophalen van de pagina zelf.

Drie opties, in volgorde van voorkeur voor kleine producten. Toon helemaal geen totaal — "1-25 getoond" met een volgende-knop is voor de meeste interfaces voldoende. Toon een geschat aantal, dat de database goedkoop kan inschatten. Of houd zelf een teller bij als het getal echt belangrijk is, bijgewerkt wanneer rijen worden aangemaakt en verwijderd.

Het algemene principe geldt breder dan tellen: een getal in de hoek van een pagina is zelden een query waard die meegroeit met uw data.

## Indexen Toevoegen aan een Live Tabel

Op een tabel met echte data blokkeert het aanmaken van een index normaal gesproken schrijfacties terwijl hij wordt opgebouwd, wat op een grote tabel een periode betekent waarin uw applicatie niets kan invoegen.

Postgres biedt een gelijktijdige opbouw (concurrent build) die die blokkade niet neemt. Die is trager en mislukt af en toe, waarbij een ongeldige index achterblijft die moet worden verwijderd en opnieuw geprobeerd — maar ze legt uw product niet stil, en dat is de eigenschap die u om vier uur 's middags wilt.

Er horen twee gewoontes bij. Maak indexen aan via migratiebestanden in plaats van door in een dashboard te typen, zodat uw staging- en productiedatabases identiek blijven en de wijziging is vastgelegd. En meet dezelfde query vóór en na, want een index die het plan niet veranderde, betekent dat de database besloot hem niet te gebruiken, en dat meteen weten is beter dan aannemen dat het werkte.

## Gedeeltelijke Indexen en de Rijen Die U Nooit Opvraagt

Eén verfijning die de moeite waard is om te kennen, omdat ze op bijna elk product van toepassing is en niets kost.

De meeste applicaties vragen keer op keer een fractie van hun data op. Openstaande tickets, actieve abonnementen, niet-gearchiveerde projecten, onverwerkte taken. De gesloten, opgezegde en gearchiveerde rijen stapelen zich eindeloos op en worden bijna nooit gelezen, maar een normale index neemt ze plichtsgetrouw allemaal op.

Een gedeeltelijke index (partial index) dekt alleen de rijen die aan een voorwaarde voldoen — bijvoorbeeld actieve records — wat hem drastisch kleiner, sneller doorzoekbaar en goedkoper in onderhoud maakt. Op een tabel waar 95 procent van de rijen historisch is, is het verschil niet marginaal.

Het addertje is dat de database een gedeeltelijke index alleen gebruikt wanneer de voorwaarde van de query overeenkomt met die van de index, dus het filter moet in de query zelf staan. Dat is meestal al zo: de schermen die traag aanvoelen, zijn de schermen die actueel werk tonen.

Dezelfde gedachte geldt voor een wachtrijtabel. Een index over alleen de openstaande taken, in plaats van elke taak die ooit is uitgevoerd, houdt de pollingquery snel, hoeveel geschiedenis zich er ook achter opstapelt — en geschiedenis die zich achter een werkende wachtrij opstapelt, is precies wat er met elk succesvol product gebeurt.

## Wanneer Indexen Niet het Antwoord Zijn

Drie situaties lijken op een indexprobleem en zijn het niet, en ze herkennen bespaart een dag.

**Zoeken in tekst.** Filteren op een woord dat ergens in een omschrijving voorkomt, kan geen gewone index gebruiken. Daarvoor is full-text search nodig, wat Postgres standaard ondersteunt, of een aparte zoekdienst — en de keuze tussen die twee is een beslissing die u bewust moet nemen.

**Aggregaties over alles.** Een dashboard dat elke transactie sinds de lancering optelt, wordt eindeloos trager, ongeacht indexen, omdat het werk meegroeit met uw geschiedenis. Die getallen horen in een samenvattingstabel die wordt bijgewerkt wanneer data binnenkomt, of 's nachts wordt berekend.

**Row-level security die meer werk doet dan u denkt.** Supabase-policies zijn voorwaarden die op elke query worden toegepast, en een policy met een subquery tegen een andere tabel wordt uitgevoerd voor elke rij die wordt bekeken. Een trage query met een eenvoudig plan en een dure policy is een policyprobleem, en de oplossing is de eigen opzoeking van de policy te indexeren — of haar zo te herstructureren dat ze vergelijkt met een waarde die al op de rij staat.

## Dit Inrichten

Voor een draaiende Supabase-applicatie kost dit doorgaans één tot twee dagen: querystatistieken bekeken en gerangschikt op totale tijd, plannen vastgelegd voor de grootste boosdoeners, foreign-key-indexen aangemaakt in het hele schema, samengestelde indexen voor tenant en sorteervolgorde op de tabellen achter uw hoofdschermen, unieke indexen op natuurlijke opzoekkolommen, N+1-querypatronen herschreven om gerelateerde data in één statement op te halen, dure tellingen verwijderd of geschat, alles toegepast via migraties met gelijktijdige opbouw, en een notitie van de tijden vóór en na zodat de volgende persoon kan zien wat er is gedaan en waarom.

LaunchStudio doet dit als onderdeel van productieklaar maken, en het is meestal het goedkoopste prestatiewerk dat een groeiend product kan krijgen — uren in plaats van een herbouw. De engineers zijn van Manifera: elf jaar, 160+ projecten, Postgres in productie lang voordat het in de mode was.

[Stuur ons uw traagste pagina](https://launchstudio.eu/nl/#contact) en wij vertellen u of het indexen of queries zijn.

## Echt voorbeeld

### Vier Seconden om Negen Uur 's Ochtends

Wendy Roos runt Verzuimlijn, gebouwd in Lovable: verzuimregistratie voor kleine werkgevers, gebruikt door 140 bedrijven met samen zo'n 4.000 werknemers.

Acht maanden lang ging alles goed. Toen begon het dashboard — het eerste scherm dat elke gebruiker opent — vier tot zes seconden te duren, altijd het ergst tussen negen en tien uur 's ochtends, wanneer de meeste gebruikers tegelijk inloggen. Twee klanten klaagden en één vroeg of het product hun omvang wel aankon.

De tabel met verzuimregistraties had 310.000 rijen bereikt en precies één index: de primaire sleutel. De dashboardquery filterde op werkgever en sorteerde op datum, dus de database las alle 310.000 rijen en sorteerde ze, elke keer, voor elke gebruiker. De ochtendpiek was gewoon veel mensen die dat tegelijk deden.

Twee werkdagen: querystatistieken bekeken, waaruit bleek dat de dashboardquery 71 procent van de totale databasetijd verbruikte; `EXPLAIN ANALYZE` bevestigde een sequential scan en een externe sortering; een samengestelde index op werkgever en datum aflopend, gelijktijdig aangemaakt via een migratie; indexen toegevoegd op de zes foreign-key-kolommen in het schema die er geen hadden; een N+1-patroon op hetzelfde dashboard opgelost, waarbij elk van de 25 verzuimrijen afzonderlijk het werknemerrecord ophaalde; het totaal aantal records vervangen door een knop voor de volgende pagina; en het indexgebruik een maand later bekeken, waarbij twee speculatieve indexen werden verwijderd.

**Resultaat:** het dashboard ging van 4,2 seconden tijdens de ochtendpiek naar 180 milliseconden, op dezelfde hardware en hetzelfde plan. Wendy's database-CPU tijdens piekuren daalde van routinematig boven de 80 procent naar onder de 15, waardoor een geplande upgrade waarvoor ze €340 per maand had begroot niet meer nodig was.

> *"Ik ging ervan uit dat ik mijn plan was ontgroeid en voor een groter plan moest betalen. Het bleek dat ik nooit één index had aangemaakt, en niemand had me verteld dat dat iets was wat ik moest doen."*
> — **Wendy Roos, Oprichter, Verzuimlijn (Helmond)**

**Kosten & Doorlooptijd:** €1.600 (queryanalyse, samengestelde en foreign-key-indexen via gelijktijdige migraties, herstel van N+1-patronen, verwijderen van tellingen, controle van indexgebruik) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Hoe weet ik welke queries traag zijn?

Gebruik de querystatistieken van Supabase en sorteer op totale verbruikte tijd, niet op de traagste afzonderlijke uitvoering. Een query van 40 milliseconden bij elke paginalading doet er meestal meer toe dan een query van één seconde die 's nachts draait.

### Moet ik gewoon elke kolom indexeren?

Nee. Elke index vertraagt elke schrijfactie op die tabel en kost opslag. Indexeer foreign keys, tenantkolommen, sorteerkolommen en natuurlijke opzoeksleutels, bekijk het gebruik na een paar maanden en verwijder wat ongebruikt is.

### Waarom is mijn pagina traag als elke query snel is?

Omdat het er tientallen zijn — een lijst die gerelateerde data in een lus ophaalt. Geen index lost dat op; de gerelateerde rijen in één query ophalen wel.

### Is het veilig om een index toe te voegen aan een live tabel?

Gebruik een gelijktijdige opbouw, die voorkomt dat schrijfacties worden geblokkeerd terwijl de index wordt aangemaakt. Pas haar toe via een migratie in plaats van het dashboard, zodat staging en productie identiek blijven.

### Waarom is rijen tellen zo traag?

Postgres telt echt in plaats van een totaal op te slaan. Laat op grote tabellen het totaal weg van lijstpagina's, toon een schatting, of houd zelf een teller bij als het getal echt belangrijk is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe vind ik trage queries in Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik de querystatistieken, gesorteerd op totale verbruikte tijd in plaats van de traagste afzonderlijke uitvoering, en voer daarna EXPLAIN ANALYZE uit op de grootste boosdoeners."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik elke kolom indexeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Elke index vertraagt schrijfacties en kost opslag. Indexeer foreign keys, tenant- en sorteerkolommen en opzoeksleutels, en verwijder ongebruikte indexen na echt verkeer."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is mijn pagina traag als elke query snel is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U voert er tientallen uit — gerelateerde data opgehaald binnen een lus. Haal het in één query op; geen index helpt."
      }
    },
    {
      "@type": "Question",
      "name": "Is het veilig om een index toe te voegen aan een live tabel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik een gelijktijdige opbouw zodat schrijfacties niet worden geblokkeerd, en pas haar toe via een migratie zodat staging en productie identiek blijven."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is rijen tellen traag in Postgres?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Postgres telt echt in plaats van een totaal op te slaan. Verwijder totalen van lijstpagina's, gebruik een schatting, of houd zelf een teller bij."
      }
    }
  ]
}
</script>
