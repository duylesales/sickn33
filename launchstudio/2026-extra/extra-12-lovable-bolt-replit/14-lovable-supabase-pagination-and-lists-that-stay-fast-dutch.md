---
Titel: "Lovable Supabase: Paginering en Lijsten Die Snel Blijven"
Trefwoorden: lovable supabase, paginering, cursorpaginering, offset-prestaties, lijstpagina's, oneindig scrollen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Paginering en Lijsten Die Snel Blijven

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Paginering en Lijsten Die Snel Blijven",
  "description": "Elke door AI gebouwde app heeft een lijstpagina, en de meeste laden de hele tabel. Offset- versus cursorpaginering, waarom pagina 400 traag is, en hoe u lijsten snel houdt terwijl de data groeit.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-pagination-and-lists-that-stay-fast" }
}
</script>

Open de belangrijkste lijstpagina van een door AI gebouwd product en kijk naar het netwerktabblad. In een groot deel ervan ziet u één verzoek dat elke rij van het account teruggeeft — vierhonderd, negenduizend, wat er ook bestaat — waarna de browser filtert, sorteert en er twintig van toont.

Het werkt. In het begin is het snel. En het gaat langs drie assen tegelijk achteruit: de database leest meer, het netwerk verstuurt meer, en de browser houdt meer in het geheugen, totdat een telefoon in de trein de pagina helemaal niet meer kan openen.

De oplossing is paginering, en de reden dat het een artikel waard is, is dat de voor de hand liggende manier om het te doen degene is die later breekt.

## Waarom Pagina 400 Trager Is dan Pagina 1

De standaardaanpak is offset: sla 20 over, neem 20; sla 40 over, neem 20. Het is wat elke tutorial laat zien en wat een AI-tool zal schrijven.

Het probleem zit in wat overslaan betekent. Om rij 8.001 tot 8.020 gesorteerd op datum terug te geven, moet de database de eerste 8.020 rijen op volgorde maken en er dan 8.000 weggooien. Het werk groeit met hoe diep u gaat, en daarom zijn de laatste pagina's van een lange lijst dramatisch trager dan de eerste.

Voor de meeste producten doet dit er nooit toe, omdat niemand pagina 400 bezoekt en omdat hun tabellen klein zijn. Het doet ertoe in drie specifieke gevallen: een export of synchronisatie die in een lus elke pagina doorloopt, een lijst die zo is gesorteerd dat de interessante rijen aan het eind staan, en een tabel die voorbij een paar honderdduizend rijen is gegroeid.

Er is een tweede, subtieler probleem. Offsets zijn instabiel. Wordt er een rij ingevoegd terwijl iemand aan het pagineren is, dan schuift alles één plek op — zodat een item op twee opeenvolgende pagina's kan verschijnen, of helemaal kan worden overgeslagen. Voor een mens die doorklikt is het een curiositeit. Voor een taak die elke pagina in een ander systeem importeert, is het stil dataverlies.

## Cursorpaginering, Eén Keer Uitgelegd

Het alternatief stelt een andere vraag. In plaats van "sla 8.000 rijen over" zegt het "geef me de volgende 20 rijen na deze specifieke rij".

De cursor is de sorteersleutel van de laatste rij die u zag — doorgaans een tijdstempel en een identificatie om gelijke waarden uit elkaar te houden. De volgende pagina is een eenvoudig filter, dat een index direct beantwoordt, hoe diep u ook bent. Pagina 400 kost evenveel als pagina 1, en rijen kunnen niet worden gedupliceerd of overgeslagen door inserts die elders plaatsvinden.

De prijs is dat u niet naar een willekeurig paginanummer kunt springen, omdat de cursor alleen de rij kent die u net zag. In de praktijk past dat bij de meeste productinterfaces, die meer-ladenknoppen of oneindig scrollen gebruiken in plaats van genummerde pagina's.

De vuistregel: genummerde pagina's met offsets voor beheerschermen over bescheiden tabellen; cursors voor alles wat lang is, alles met oneindig scrollen, en elke programmatische afnemer zoals een export, een synchronisatie of een API die uw klanten aanroepen.

## De Sortering Moet Volledig Zijn

Beide benaderingen breken op dezelfde manier als de sorteervolgorde dubbelzinnig is.

Alleen sorteren op aanmaakdatum is niet genoeg, omdat twee rijen dezelfde tijdstempel kunnen hebben — en als dat zo is, mag de database ze elke keer in een andere volgorde teruggeven. Met offsets levert dat rijen op die twee keer verschijnen over pagina's heen. Met cursors levert het een paginagrens op die een rij verliest of herhaalt.

Sorteer altijd op iets unieks als beslisser: de datum, dan de identificatie. De index moet precies met die volgorde overeenkomen, en de cursor moet beide waarden meedragen.

Dit is een wijziging van twee minuten die een hele categorie meldingen als "soms ontbreekt er een record in de lijst" wegneemt, die anders als af en toe optredend wordt gecategoriseerd en nooit wordt opgelost.

## Tel Niet Tenzij Het Moet

De pagineringsvraag sleept altijd een tweede vraag mee: het totaal tonen.

Een telling over een grote gefilterde tabel is vaak duurder dan het ophalen van de pagina, en ze draait bij elke paginalading. Voor de meeste interfaces is het totaal decoratie — gebruikers willen de eerste twintig resultaten en een manier om verder te gaan, niet weten dat het er 8.412 zijn.

Drie verstandige opties. Laat het weg, en gebruik een volgende-knop die verschijnt als er meer rijen zijn — wat u kunt bepalen door één rij meer op te vragen dan u toont. Schat het, met de eigen statistieken van de database, en markeer het als benadering. Of houd bewust een teller bij voor de ene plek waar het echt telt.

De goedkope truc is het noemen waard: vraag 21 rijen op, toon er 20, en het bestaan van de 21e vertelt u dat er een volgende pagina is. Geen telling, geen extra query.

## Filteren en Sorteren Horen bij het Probleem

Een lijstpagina waarop gebruikers kunnen filteren en sorteren, is eigenlijk een heleboel queries, en elke combinatie moet door een index worden bediend, anders valt ze terug op alles lezen.

Wees bewust in wat u aanbiedt. Drie nuttige filters en twee sorteervolgordes, elk ondersteund door een passende index, levert een snelle pagina op. Twaalf filters in willekeurige combinaties levert een pagina op die snel is in de combinaties die u testte en traag in degene die klanten gebruiken.

Gebruik voor zoeken in tekst geen patroonvergelijking met een wildcard vooraan — die kan geen gewone index gebruiken en leest de tabel. Postgres heeft echte full-text search, en die invoeren voor het ene veld waarop mensen zoeken, is meestal een uur werk.

## Oneindig Scrollen Heeft Eigen Kosten

Blijft de interface rijen toevoegen terwijl de gebruiker scrollt, dan stapelt de browser elke opgehaalde rij op. Vierhonderd rijen met rijke lijstitems is een pagina die hapert op een middenklasse telefoon, en de gebruiker koos daar niet voor — hij bleef gewoon scrollen.

Twee maatregelen, in volgorde van moeite. Houd de rijen licht: vermijd zware componenten per rij en laad afbeeldingen lazy op het formaat dat werkelijk wordt getoond. En worden lijsten echt lang, render dan alleen wat zichtbaar is, wat goed wordt ondersteund door bibliotheken en het punt is waarop oneindig scrollen niet langer gratis is.

Geef mensen ook een uitweg. Een filter of een zoekvak is een beter antwoord dan scrollen naar rij 600, en het is voor iedereen goedkoper.

## Exports Zijn Ook Paginering

De plek waar offsets de meeste schade aanrichten, is de export waar niemand aan denkt als lijstpagina.

Een CSV van alles, opgebouwd door alle rijen tegelijk op te halen, werkt totdat een klant genoeg data heeft om het geheugen uit te putten of een time-out te overschrijden — en ze faalt voor uw grootste klant, degene die u het minst wilt teleurstellen.

Loop de data door met een cursor, stream die gaandeweg naar de client of naar een bestand, en genereer alles wat echt groot is op de achtergrond en stuur een link als het klaar is. De middelste optie — streamen — is meestal genoeg en een kleine wijziging ten opzichte van wat er al is.

## Paginering Hoort bij de API, Niet bij de Pagina

Eén ontwerpbeslissing bespaart later veel herwerk: maak de begrensde pagina overal de vorm van uw datatoegang, niet iets wat u aan één scherm hebt toegevoegd.

Is records ophalen altijd "geef me een pagina, hier is de cursor", dan erft elke afnemer dat — het lijstscherm, de mobiele weergave die u volgend jaar bouwt, de export, de API voor klanten, de interne beheertool, de synchronisatie met iemands boekhoudpakket. Is de standaard in plaats daarvan "haal alles op", met paginering vastgeplakt aan de ene pagina die traag werd, dan begint elke nieuwe afnemer bij de onbegrensde versie en wordt het probleem telkens opnieuw ontdekt.

In de praktijk betekent dit dat de functie die uw applicatie aanroept om records te lezen een limiet en een cursor aanneemt, en geen modus heeft die alles teruggeeft. Code die echt alle rijen nodig heeft — een nachtelijke taak, een migratie — loopt expliciet door pagina's, wat zowel eerlijk is over wat ze doet als veilig terwijl de data groeit.

Hetzelfde geldt voor alles wat u aan klanten beschikbaar stelt. Een endpoint zonder maximale paginagrootte is een endpoint waar één klant honderdduizend rijen van opvraagt, in een lus, vanuit een script dat hij om half vijf op een vrijdag schreef. Stel een plafond in, documenteer het, en geef de cursor terug in het antwoord, zodat het juiste gebruik ook het makkelijke gebruik is.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één dag: lijstendpoints aangepast om een begrensde pagina op te halen in plaats van alles, cursorpaginering voor lange lijsten, exports en elke programmatische afnemer, een volledige sorteervolgorde met een unieke beslisser die overeenkomt met een index, tellingen verwijderd of geschat met de één-extra-ophalen-truc voor het detecteren van een volgende pagina, filters en sorteringen beperkt tot combinaties die indexen dekken, tekstzoeken weg van patroonvergelijking, exports omgezet naar cursordoorlopen met streaming, en het geheel gecontroleerd tegen een geseede tabel die groot genoeg is om het verschil te laten zien.

LaunchStudio doet dit als onderdeel van prestatiewerk, meestal samen met indexering, en die twee samen zorgen ervoor dat een product bij 200 klanten hetzelfde aanvoelt als bij 20. De engineers zijn van Manifera: elf jaar, 160+ projecten, vanaf de Herengracht 420 in Amsterdam en ontwikkeling in Ho Chi Minh-stad.

[Stuur ons de pagina die traag werd](https://launchstudio.eu/nl/#contact) en wij vertellen u welk van de twee problemen het is.

## Echt voorbeeld

### De Export Die Faalde voor de Beste Klant

Rutger Doedens bouwde Urenstaat met Lovable: urenregistratie en projecturen voor ingenieursbureaus, 34 bureaus, de grootste met 90 consultants.

In dezelfde twee weken kwamen er twee klachten binnen. Het urenoverzicht deed er elf seconden over om te laden voor dat grootste bureau, en was voor iedereen anders direct beschikbaar. En de maandelijkse export — waarmee elk bureau op de eerste werkdag zijn klanten factureert — faalde voor datzelfde bureau met een time-out, elke maand, wat ze omzeilden door per week te exporteren.

Beide hadden dezelfde oorzaak. Het overzicht haalde elke urenregel van het bureau op en pagineerde in de browser: 240.000 rijen voor het grote bureau, 3.000 voor een gemiddeld bureau. De export deed hetzelfde en bouwde dan een CSV in het geheugen.

Eén werkdag: het overzicht omgezet naar cursorpaginering op tijdstempel en identificatie, met een bijpassende samengestelde index en een volledige sorteervolgorde; het aantal rijen vervangen door een volgende-knop met de één-extra-ophalen-techniek; filters teruggebracht van negen willekeurige velden naar vier met indexen, met het filter op consultantnaam verplaatst naar full-text search; de export herschreven om de data met een cursor te doorlopen en rijen gaandeweg naar het antwoord te streamen, met een achtergrondtaak en een e-maillink voor exports boven een drempel; en het geheel getest tegen een geseede database met 400.000 regels in plaats van de 900 in ontwikkeling.

**Resultaat:** het overzicht ging van 11 seconden naar 240 milliseconden voor het grootste bureau, en de maandelijkse export was in 9 seconden klaar in plaats van te falen. Rutgers grootste klant stopte met per week exporteren, en noemde dat bij de verlenging.

> *"Mijn ergste prestatieproblemen zaten allemaal in het account van mijn beste klant. Zij waren de enigen met genoeg data om ze te vinden, en de laatsten die ik ze wilde laten vinden."*
> — **Rutger Doedens, Oprichter, Urenstaat (Enschede)**

**Kosten & Doorlooptijd:** €1.900 (cursorpaginering met samengestelde index, volledige sortering, verwijderen van tellingen, herzien van filters en zoeken, streamende export met generatie op de achtergrond, controle onder belasting met geseed volume) — afgerond in 1 werkdag.

## Veelgestelde vragen

### Wanneer is offsetpaginering goed genoeg?

Voor beheerschermen over bescheiden tabellen waar gebruikers genummerde pagina's willen en niemand diep gaat. Alles wat lang is, oneindig scrolt of door een programma wordt gelezen, moet cursors gebruiken.

### Waarom verschijnt een record soms op twee pagina's?

Omdat de sorteervolgorde niet uniek is, of omdat er rijen werden ingevoegd terwijl iemand door de pagina's ging. Sorteer op een tijdstempel plus een unieke identificatie, en geef de voorkeur aan cursors voor alles wat een programma afneemt.

### Hoe toon ik een volgende-knop zonder te tellen?

Vraag één rij meer op dan u toont. Komt die terug, dan is er nog een pagina. Geen telquery nodig.

### Moet ik oneindig scrollen gebruiken?

Alleen met lichte rijen en, zodra lijsten echt lang worden, gevirtualiseerde weergave. En bied altijd filteren of zoeken aan, want scrollen is een slechte manier om iets te vinden voorbij de eerste honderd rijen.

### Waarom faalt mijn export alleen voor grote klanten?

Omdat ze alles in het geheugen ophaalt voordat ze schrijft. Doorloop de data met een cursor en stream het eruit, of genereer het op de achtergrond en stuur een link.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer is offsetpaginering goed genoeg?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beheerschermen over bescheiden tabellen met genummerde pagina's. Lange lijsten, oneindig scrollen en programmatische afnemers moeten cursors gebruiken."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verschijnt een record op twee pagina's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De sorteervolgorde is niet uniek, of rijen verschoven tijdens het pagineren. Sorteer op tijdstempel plus een unieke identificatie en gebruik cursors voor programmatisch lezen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe toon ik een volgende-knop zonder rijen te tellen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Haal één rij meer op dan u toont; komt die terug, dan bestaat er een volgende pagina. Geen telquery nodig."
      }
    },
    {
      "@type": "Question",
      "name": "Is oneindig scrollen een goede keuze?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen met lichte rijen en gevirtualiseerde weergave zodra lijsten lang worden, en altijd samen met filteren of zoeken."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom faalt mijn CSV-export alleen voor grote klanten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze laadt eerst alles in het geheugen. Doorloop met een cursor en stream de uitvoer, of genereer op de achtergrond en mail een link."
      }
    }
  ]
}
</script>
