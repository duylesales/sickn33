---
Titel: "Lovable Supabase: Views en Wat U aan de Frontend Blootstelt"
Trefwoorden: lovable supabase, database-views, security invoker, API-oppervlak, materialized views, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Views en Wat U aan de Frontend Blootstelt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Views en Wat U aan de Frontend Blootstelt",
  "description": "Supabase maakt van uw schema een API, wat betekent dat elke tabel een beslissing is over wat klanten kunnen lezen. Views gebruiken om dat oppervlak vorm te geven, de security invoker-valkuil, en wanneer een materialized view het juiste antwoord is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-views-and-what-to-expose-to-the-frontend" }
}
</script>

Wat Supabase snel maakt om mee te bouwen, is ook wat oprichters het vaakst verkeerd begrijpen: uw databaseschema is uw API. Maak een tabel aan en ze is direct leesbaar vanuit de browser, alleen begrensd door de policies die u schreef - en als u er geen schreef, door niets.

Dat verandert hoe u over schemaontwerp moet denken. Een kolom is niet alleen opslag; het is een veld dat uw klanten kunnen opvragen. Een tabel is niet alleen een plek om dingen neer te zetten; het is een endpoint.

Views zijn hoe u dat oppervlak weer onder controle krijgt, en ze worden onderbenut in door AI gebouwde producten omdat de tool ze nooit voorstelt.

## Het Probleem met Alles Selecteren

Frontendcode die door AI-tools wordt gegenereerd, vraagt doorgaans om alle kolommen, omdat dat het eenvoudigst te schrijven is.

Drie gevolgen. Interne velden reizen naar de browser - kostprijzen, marges, risicoscores, moderatievlaggen, interne notities - waar iedereen ze in het netwerktabblad kan lezen, ongeacht wat de interface toont. Payloads zijn groter dan nodig, wat u merkt op mobiele verbindingen. En uw schema wordt een gepubliceerd contract: elke kolomnaam is nu zichtbaar voor wie kijkt, en er een hernoemen breekt een client die u niet meer beheert.

De neiging is dit in de frontend op te lossen door kolommen expliciet op te sommen, en dat is het doen waard. Maar het is een afspraak, geen grens - het volgende scherm, of de volgende agentsessie, selecteert weer alles.

## Een View Is een Benoemde, Stabiele Vorm

Een view is een opgeslagen query die wordt gepresenteerd alsof het een tabel is. Definieer er een die precies de kolommen blootstelt die een scherm nodig heeft, samengevoegd zoals dat scherm ze wil, en laat de frontend ernaar wijzen.

Drie dingen verbeteren tegelijk.

De interne kolommen zijn er gewoon niet, dus ze kunnen niet worden opgevraagd. De frontend stopt met joins over drie tabellen en vraagt één ding voor één vorm, wat sneller is en veel makkelijker te lezen. En u krijgt de vrijheid om de onderliggende tabellen te herorganiseren zonder de client te veranderen, omdat de view het contract is en de tabellen een implementatiedetail.

Dat laatste punt is wat views de moeite waard maakt, juist in een door AI gebouwd product, waar het schema meerdere keren wordt geherstructureerd naarmate het product volwassen wordt.

## De Security Invoker-Valkuil

Hier is het deel dat echte incidenten veroorzaakt, en het verdient het om twee keer te worden gelezen.

Standaard draait een view in Postgres met de rechten van degene die hem aanmaakte - u - in plaats van degene die hem opvraagt. Dat betekent dat row-level security op de onderliggende tabellen niet wordt toegepast op de aanroeper. Een view over een facturentabel, aangemaakt door een beheerder, kan de facturen van elke organisatie teruggeven aan elke geauthenticeerde gebruiker, hoe zorgvuldig de policies van de tabel ook zijn geschreven.

Elke view die klanten kunnen opvragen, moet worden gedefinieerd met security invoker, zodat hij draait als de aanroepende gebruiker en de onderliggende policies gelden. Recente Postgres-versies ondersteunen dit direct, en Supabase documenteert het - maar een view die door een AI-sessie is aangemaakt, of door een oprichter in de SQL-editor, heeft het niet, tenzij iemand erom vroeg.

De controle kost twee minuten: maak een lijst van uw views, bevestig dat elke view die aan clients wordt blootgesteld security invoker gebruikt, en test er een door hem op te vragen als gebruiker van een andere organisatie. Komen hun rijen terug, dan hebt u de ernstigste fout in uw applicatie gevonden.

## Views Maken Policies Niet Overbodig

Een verwant misverstand: dat een view vóór een tabel zetten betekent dat de tabel geen policies meer nodig heeft.

Die heeft ze wel nodig. De tabel blijft blootgesteld tenzij u de toegang ertoe hebt ingetrokken, en een client kan haar direct opvragen. Views vormen gemak en verminderen onbedoelde blootstelling; row-level security is de echte grens.

De volledige opzet, voor een tabel met klantdata, is policies op de tabel, een view die de veilige kolommen blootstelt met security invoker, en toegang tot de onderliggende tabel ingetrokken voor de API-rol, zodat clients de view moeten gebruiken. De eerste daarvan is degene die u niet kunt overslaan.

## Wanneer de View Gematerialiseerd Moet Worden

Een gewone view voert zijn query uit elke keer dat hij wordt gelezen. Voor de meeste schermen is dat precies goed.

Voor een dure aggregatie - een dashboard dat een jaar aan transacties samenvat, een ranglijst, een rapport over miljoenen rijen - slaat een materialized view het berekende resultaat op en serveert het direct, volgens schema ververst in plaats van bij elk verzoek.

De afweging is actualiteit. Een materialized view die elk uur wordt ververst, bevat data tot een uur oud, wat prima is voor een omzetoverzicht en verkeerd voor alles wat een gebruiker net heeft gewijzigd. Vermeld het in de interface - "stand van 14:00" - en de klacht verdwijnt, want het bezwaar is nooit de veroudering zelf, maar veroudering die eruitzag als live data.

Twee praktische opmerkingen. Verversen blokkeert de view normaal gesproken voor lezers, tenzij u gelijktijdig ververst, wat een unieke index erop vereist - het waard om vanaf het begin in te richten. En een materialized view is een momentopname zonder eigen policies, dus het moet geaggregeerde data zijn die veilig is voor het publiek, geen sluiproute langs rechten per rij.

## Views voor Rapportage, Tabellen voor Schrijven

Views in Postgres kunnen soms worden beschreven, en in een product als dit is dat meestal een slecht idee.

Het mentale model dat helder blijft: lezen gaat via views die op het scherm zijn afgestemd; schrijven gaat via expliciete applicatiecode of databasefuncties die de regels afdwingen. Raakt een schrijfactie meerdere tabellen of zijn er voorwaarden aan verbonden, dan is een functie de juiste plek, en die kan vanuit de client in één round trip worden aangeroepen.

Dat geeft u ook een natuurlijke plek voor de controles die policies niet kunnen uitdrukken - een statusovergang die alleen vanuit bepaalde statussen is toegestaan, een limiet op hoeveel van iets een account mag aanmaken - zonder ze te verspreiden door frontendcode, waar ze op zijn best adviserend zijn.

## Houd het Oppervlak Bewust Klein

Maak eens per kwartaal een lijst van alles wat uw API blootstelt en vraag of elk item er nog moet zijn.

Door AI gebouwde producten verzamelen tabellen van verlaten functies, en een verlaten tabel zonder policies is een datalek waar niemand naar kijkt, omdat geen code haar leest. Hetzelfde voor views die tijdens een experiment zijn aangemaakt.

Verwijderen is de beste uitkomst. Waar dat te vroeg is, volstaat het intrekken van clienttoegang, en dat kost seconden. Het algemene principe is dat het oppervlak dat een klant kan bereiken de verzameling dingen moet zijn die u bewust hebt gepubliceerd, terwijl het in de meeste door AI gebouwde applicaties de verzameling dingen is die ooit zijn aangemaakt.

## Gegenereerde Types Horen bij het Contract

Supabase kan TypeScript-types genereren uit uw schema, en in een door AI gebouwd project is dat waardevoller dan het eerst lijkt - niet om de elegantie, maar omdat het het enige mechanisme is dat u vertelt wat een schemawijziging heeft gebroken.

Hernoem een kolom met gegenereerde types aanwezig en de compiler noemt elk bestand dat ernaar verwees. Hernoem er een zonder, en u hoort het van een klant, omdat een query naar een kolom die niet meer bestaat niets teruggeeft in plaats van luid te falen.

Twee gewoontes laten dit werken. Genereer de types opnieuw als onderdeel van het toepassen van een migratie in plaats van af en toe met de hand, zodat ze nooit een database beschrijven die niet meer bestaat. En commit ze, zodat een reviewer - of een codeeragent die de repository leest - de vorm van de data kan zien zonder ergens verbinding mee te maken.

Het tweede-orde-voordeel is het voordeel dat zich opstapelt. Een AI-sessie met accurate types in het project schrijft queries tegen kolommen die bestaan, in de vormen die ze werkelijk hebben. Zonder types gokt ze op basis van omliggende code, en zo wordt een vierde naam voor hetzelfde concept geïntroduceerd. Types zijn documentatie die de machine kan lezen, en in een product waarin veel van de code door een machine is geschreven, is dat geen kleinigheid.

## Dit Inrichten

Voor een bestaand Supabase-product kost dit doorgaans één dag: een inventarisatie van alles wat de API blootstelt, views gedefinieerd voor de vormen die uw schermen echt nodig hebben, security invoker bevestigd op elke view voor clients en gecontroleerd door op te vragen als gebruiker van een andere organisatie, row-level security behouden als echte grens met toegang tot onderliggende tabellen ingetrokken waar een view die vervangt, dure aggregaties verplaatst naar materialized views met gelijktijdig verversen en een zichtbaar tijdstip, schrijfacties via functies waar regels gelden, en ongebruikte tabellen en views van het oppervlak verwijderd.

LaunchStudio doet dit in beveiligings- en prestatiewerk aan Supabase-producten, en vooral de security invoker-controle heeft een hoge trefkans. De engineers zijn van Manifera - elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vraag ons uw API op te vragen als een andere klant](https://launchstudio.eu/nl/#contact). Het is een test van tien minuten met af en toe een ongemakkelijke uitkomst.

## Echt voorbeeld

### Het Dashboard Dat Ieders Cijfers Toonde

Iris Molenaar bouwde Vakantieverhuur in Lovable: boekings- en omzetadministratie voor eigenaren van vakantiewoningen aan de Zeeuwse en Zuid-Hollandse kust, 210 eigenaren met zo'n 500 woningen.

Haar prestatiewerk was goed gegaan. Het eigenaarsdashboard - bezetting, omzet, gemiddelde nachtprijs, vergelijking met het vorige jaar - was traag geweest, dus een AI-sessie maakte een view die het aggregeerde, en de pagina werd direct snel.

De view werd aangemaakt zonder security invoker. Row-level security op de boekingentabel was correct en was dat altijd geweest, en de view liep er dwars langs. Elke ingelogde eigenaar die de view direct opvroeg, in plaats van via het gefilterde verzoek van het dashboard, kreeg de bezettings- en omzetcijfers van alle 500 woningen - inclusief die van de concurrenten tegen wie ze hun prijzen bepaalden.

Een eigenaar vond het terwijl hij een spreadsheet tegen de API bouwde, en meldde het dezelfde dag.

Twee werkdagen: de aggregatieview opnieuw gedefinieerd met security invoker en gecontroleerd door op te vragen als drie verschillende eigenaren; alle negen views in het project gecontroleerd, waarvan er vier voor clients waren en drie daarvan hetzelfde gebrek hadden; clienttoegang ingetrokken op zes onderliggende tabellen die nu alleen via views bereikbaar zijn; de jaarvergelijking, echt duur, omgezet naar een materialized view die elke vijftien minuten wordt ververst, met een unieke index voor gelijktijdig verversen en een regel "bijgewerkt om" op het dashboard; twee tabellen van een verlaten prijsexperiment volledig van het API-oppervlak verwijderd; en een test toegevoegd die elke view voor clients opvraagt als gebruiker van een tweede organisatie en faalt als er een rij terugkomt.

**Resultaat:** het lek was binnen een dag na de melding gedicht, en de geautomatiseerde test tussen tenants heeft sindsdien twee views uit latere AI-sessies opgevangen voordat ze productie bereikten. De laadtijd van het dashboard bleef onder de 200 milliseconden.

> *"De view werd aangemaakt om een pagina snel te maken, en dat werkte. Niemand zei erbij dat hij ook de beveiliging op de tabel eronder uitschakelde."*
> - **Iris Molenaar, Oprichter, Vakantieverhuur (Middelburg)**

**Kosten & Doorlooptijd:** €2.200 (controle van views en herstel van security invoker, verkleinen van het API-oppervlak, materialized view met gelijktijdig verversen, verwijderen van verlaten tabellen, geautomatiseerde test tussen tenants) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Waarom omzeilt een view row-level security?

Omdat hij standaard draait met de rechten van de maker in plaats van die van de aanroeper. Definieer views voor clients met security invoker, zodat de policies van de onderliggende tabel gelden voor wie er ook opvraagt.

### Maken views policies overbodig?

Nee. De onderliggende tabel blijft blootgesteld tenzij u de toegang intrekt, en policies blijven de echte beveiligingsgrens. Views vormen het oppervlak; ze dwingen het niet af.

### Wanneer moet een view worden gematerialiseerd?

Wanneer de query duur is en de data niet tot op de seconde actueel hoeft te zijn - dashboards, samenvattingen, rapporten. Toon het tijdstip van de stand, en richt een unieke index in zodat verversen gelijktijdig kan draaien.

### Moet de frontend alle kolommen selecteren?

Nee. Stel een view bloot met precies wat het scherm nodig heeft. Alles selecteren stuurt interne velden naar de browser en maakt van uw kolomnamen een gepubliceerd contract.

### Hoe weet ik wat mijn Supabase-API blootstelt?

Maak een lijst van de tabellen en views die de API-rol kan bereiken en controleer elk bewust. Door AI gebouwde projecten verzamelen tabellen van verlaten functies, en een ongebruikte tabel zonder policies is een lek waar niemand naar kijkt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom omzeilt een Postgres-view row-level security?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standaard draait hij met de rechten van de maker, niet van de aanroeper. Views voor clients moeten worden gedefinieerd met security invoker."
      }
    },
    {
      "@type": "Question",
      "name": "Maken views row-level security-policies overbodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De onderliggende tabel blijft bereikbaar tenzij de toegang wordt ingetrokken, en policies blijven de echte grens."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet een view worden gematerialiseerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor dure aggregaties die niet tot op de seconde actueel hoeven te zijn. Toon het tijdstip van de stand en voeg een unieke index toe voor gelijktijdig verversen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet frontendcode alle kolommen selecteren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Stel een view bloot met precies de velden die een scherm nodig heeft; alles selecteren lekt interne kolommen en publiceert uw schema als contract."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik wat mijn Supabase-API blootstelt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maak een lijst van elke tabel en view die de API-rol kan bereiken en beoordeel ze allemaal. Verlaten tabellen zonder policies zijn lekken waar niemand naar kijkt."
      }
    }
  ]
}
</script>
