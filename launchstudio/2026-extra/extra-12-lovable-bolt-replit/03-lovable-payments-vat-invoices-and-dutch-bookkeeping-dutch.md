---
Titel: "Lovable Betalingen: Btw, Facturen en Wat de Nederlandse Boekhouding Nodig Heeft"
Trefwoorden: lovable betalingen, btw, btw-facturen, OSS, btw verlegd, Nederlandse boekhouding, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable Betalingen: Btw, Facturen en Wat de Nederlandse Boekhouding Nodig Heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Betalingen: Btw, Facturen en Wat de Nederlandse Boekhouding Nodig Heeft",
  "description": "Wat een Lovable-app moet opleveren zodat een Nederlandse accountant aangifte kan doen: verplichte factuurvelden, de btw-tariefvraag voor EU-klanten, btw verlegd, OSS-drempels en doorlopende nummering.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-payments-vat-invoices-and-dutch-bookkeeping" }
}
</script>

Het eerste kwartaal is het kwartaal dat u dit leert. U bouwde een product, mensen betaalden ervoor, en toen vroeg uw boekhouder om de facturen — en wat uw app kon leveren, was een lijst Stripe-betalingen met e-mailadressen erbij.

Geen factuurnummers. Geen bedrijfsnamen. Geen btw-behandeling. Geen manier om te zien welke van die betalingen naar een bedrijf in Duitsland gingen dat helemaal geen Nederlandse btw had moeten betalen. Wat volgde was een weekend spreadsheets en een rekening van de accountant voor het opruimen achter software die u zelf bezit.

Dit is een van de weinige onderdelen van een klein product waarvan de eisen precies door iemand anders zijn vastgelegd, wat het ongewoon makkelijk maakt om het goed te doen — als u ze kent vóór de lancering in plaats van erna.

## Wat Er op de Factuur Hoort

Een factuur die aan de Nederlandse eisen voldoet, is een vastgelegde lijst velden, geen ontwerpkwestie. Elke factuur die uw app uitgeeft, heeft nodig: een doorlopend factuurnummer zonder gaten, de factuurdatum, de volledige naam, het adres en het KvK-nummer van uw bedrijf, uw btw-identificatienummer, de naam en het adres van de klant, een omschrijving van wat is geleverd, het bedrag exclusief btw, het btw-tarief en -bedrag, en het totaal.

Twee daarvan gaan specifiek in door AI gegenereerde code mis.

**Doorlopend zonder gaten.** Een factuurnummer afgeleid van een database-ID krijgt gaten telkens wanneer een betaling mislukt of een rij wordt teruggedraaid, en een gat is precies waar een controle naar vraagt. Factuurnummers hebben een eigen teller nodig die alleen ophoogt wanneer er daadwerkelijk een factuur wordt uitgegeven.

**Onveranderbaar na uitgifte.** Een factuur is een registratie van wat er gebeurde, geen weergave van actuele gegevens. Als uw app facturen opbouwt uit live klantgegevens, dan herschrijft een klant die volgend jaar zijn bedrijfsadres wijzigt stilletjes de boekhouding van vorig jaar. Sla de factuur op als momentopname van de waarden op het moment van uitgifte, en corrigeer fouten met een creditnota in plaats van een wijziging.

Voor zakelijke klanten hebt u ook hun btw-nummer nodig, omdat daarvan afhangt of u überhaupt btw rekent.

## De Tariefvraag, Praktisch Beantwoord

Oprichters verwachten dat dit ingewikkeld is. Voor de meeste kleine producten komt het neer op drie gevallen.

**Nederlandse klanten, consument of zakelijk:** reken Nederlandse btw, normaal 21 procent voor software en digitale diensten.

**Zakelijke klanten elders in de EU met een geldig btw-nummer:** btw verlegd. U rekent geen btw en de factuur moet vermelden dat de btw is verlegd — *btw verlegd* — samen met het btw-nummer van de klant. Dat nummer valideren is uw verantwoordelijkheid, niet die van hen, en er is een Europese dienst voor precies dit doel. Een niet-gevalideerd nummer dat onjuist blijkt, betekent dat u de btw verschuldigd bent.

**Consumenten elders in de EU:** u rekent het btw-tarief van het land van de klant, en draagt dat af via de One Stop Shop. Er is een jaarlijkse EU-brede drempel waaronder u in plaats daarvan Nederlandse btw mag blijven rekenen, waar de meeste producten in hun eerste jaar onder blijven — maar "we bleven eronder" is iets wat u uit uw eigen administratie moet kunnen aantonen, wat betekent dat u vanaf de eerste verkoop het land van de klant en het bedrag vastlegt.

Klanten buiten de EU vallen doorgaans buiten de EU-btw, met eigen regels als u op schaal in bepaalde landen verkoopt.

Stripe Tax en vergelijkbare diensten berekenen dit allemaal voor u, en voor een product dat over grenzen verkoopt zijn ze hun vergoeding waard. Wat ze niet doen, is het resultaat in uw database opslaan in een vorm die uw accountant kan gebruiken, en dat blijft de taak van uw applicatie.

## Bewijs Hoort bij de Eis

Bij consumentenverkopen binnen de EU wordt van u verwacht dat u kunt aantonen waar de klant zich bevond — doorgaans met twee niet-tegenstrijdige gegevens, zoals het factuuradres en het land van het betaalmiddel of het IP-adres.

Dat klinkt bureaucratisch totdat u beseft dat het op het moment van verkoop moet worden vastgelegd, omdat het later niet te reconstrueren is. Een product dat alleen een e-mailadres vastlegt, kan nooit meer bij dat bewijs komen.

De checkout moet dus naar een land en een bedrijfsnaam vragen, en uw applicatie moet opslaan wat ze op dat moment zag: de opgegeven factuurgegevens, het land waar het betaalmiddel vandaan kwam, en het btw-nummer als dat werd opgegeven, plus het resultaat van de validatie.

## Wat Uw Accountant Werkelijk Wil

Vraag het, en het antwoord is meestal bescheiden: een maandelijkse of driemaandelijkse export, één rij per factuur, met datum, factuurnummer, naam en land van de klant, nettobedrag, btw-tarief, btw-bedrag, brutobedrag, btw-behandeling en een verwijzing naar de betaling.

Die export is een kleine functie en verandert de relatie volledig, omdat al het andere — de btw-aangifte per kwartaal, de OSS-aangifte, de jaarrekening — ervan wordt afgeleid. Producten die hem niet kunnen leveren, eindigen met een boekhouder die met de hand dashboards van betaalproviders overtypt, wat declarabel is, foutgevoelig, en volledig te vermijden.

Bouw de export voordat het eerste kwartaal sluit, niet tijdens.

## Creditnota's, Terugbetalingen en Correcties

Een terugbetaling is geen verwijderde factuur. Het is een creditnota: een eigen doorlopend genummerd document, met een verwijzing naar de oorspronkelijke factuur, een eigen btw-behandeling, en gedateerd op het moment van terugbetaling.

Hetzelfde geldt voor fouten. Hebt u een factuur uitgegeven met de verkeerde bedrijfsnaam of het verkeerde tarief, dan wijzigt u die niet — u crediteert hem en geeft een gecorrigeerde uit. Applicaties die een supportactie stilletjes een uitgegeven factuur laten aanpassen, creëren precies het soort inconsistentie tussen boekhouding en bank dat dagen kost om te ontwarren.

## Wat Er Verandert Als U via een App Store Verkoopt

Eén geval verandert het beeld echt, en oprichters lopen er laat tegenaan: een abonnement verkopen binnen een iOS- of Android-app.

Aankopen via de store worden afgehandeld door Apple of Google, die in de meeste gebieden optreden als verkoper van de transactie. Zij innen, zij handelen de consumenten-btw af, en zij betalen u een saldo uit met hun commissie eraf. Uw app geeft die facturen niet meer uit, en zelf een factuur uitgeven voor dezelfde transactie leidt tot dubbel geboekte omzet in uw administratie.

Dat creëert een splitsing die u bewust moet modelleren als u via het web én in een app verkoopt: webabonnementen zijn uw eigen verkoop, met uw eigen factuur en uw eigen btw-behandeling; store-abonnementen zijn een uitbetaling die u ontvangt, maandelijks afgestemd met het rapport van de store. Twee omzetstromen, twee boekhoudkundige behandelingen, één product.

De praktische gevolgen zijn goed om te kennen voordat u bouwt. Uw database moet nog steeds het recht kennen — of een klant een actief abonnement heeft en waar het vandaan komt — dus één abonnementsrecord met een bronveld is veel eenvoudiger dan twee parallelle systemen. Terugbetalingen door de store gebeuren zonder uw betrokkenheid en u hoort het via een melding, dus uw rechtenlogica moet daarop reageren. En een klant die in de app een abonnement nam en u vervolgens vraagt het op te zeggen, moet naar de store worden verwezen, omdat u het niet voor hem kunt doen.

Verkoopt u vandaag via het web en overweegt u later een app, dan is het ding om nu goed te doen eenvoudigweg dat rechten in uw eigen database staan als volwaardig record in plaats van uit Stripe te worden gelezen — want dat is het ontwerp dat nog steeds werkt wanneer de helft van uw omzet ergens heel anders vandaan komt.

## Dit Inrichten

Voor een product dat al geld ontvangt, kost facturatie doorgaans drie tot vier dagen: een eigen factuurreeks, facturen opgeslagen als onveranderbare momentopnames met elk verplicht veld, btw-bepaling voor Nederlandse btw, btw verlegd voor EU-bedrijven en EU-consumententarieven, validatie van btw-nummers via de Europese dienst met het resultaat vastgelegd, locatiebewijs vastgelegd bij de checkout, aanmaak en verzending van pdf's met bewaarde kopieën, creditnota's voor terugbetalingen en correcties, en een boekhoudexport in het formaat waar uw accountant om vroeg.

LaunchStudio doet dit als onderdeel van productieklaar maken voor producten die in Nederland en de EU verkopen. De engineering komt van Manifera, elf jaar en 160+ projecten vanuit Amsterdam, Singapore en Ho Chi Minh-stad — facturatie voor Europese bedrijven is voor het team al lang opgelost terrein.

[Laat ons een van uw huidige facturen zien](https://launchstudio.eu/nl/#contact) en wij vertellen u welke velden ontbreken, of bereken de kosten met de [prijscalculator](https://launchstudio.eu/nl/).

## Echt voorbeeld

### Een Kwartaal Gereconstrueerd uit een Spreadsheet

Tijmen Verhagen verkoopt Keurmerkbeheer, een met Lovable gebouwde tool die certificerende instellingen gebruiken om audits van installatiebedrijven te beheren. De klanten zijn bedrijven: 140 in Nederland, België en Duitsland, voor €65 per maand.

Zijn app ontving betalingen correct en gaf niets uit. Klanten die een factuur wilden, mailden hem, en hij maakte er een in een tekstverwerker, met de hand genummerd. Aan het eind van het eerste kwartaal had hij 61 handmatige facturen uitgegeven met drie dubbele nummers, en had hij elke klant 21 procent Nederlandse btw gerekend — inclusief negentien Duitse en Belgische bedrijven die hem hun btw-nummer hadden gegeven en met btw verlegd hadden moeten worden gefactureerd.

De schatting van zijn accountant voor het opruimen van het kwartaal was hoger dan wat het zou kosten om de software te repareren.

Zes werkdagen: een factuurreeks los van database-ID's; facturen opgeslagen als onveranderbare momentopnames met bedrijfsnaam, adres, KvK, beide btw-nummers en regeldetails; btw-bepaling op basis van klanttype en land, met btw verlegd toegepast en vermeld op facturen aan EU-bedrijven; validatie van btw-nummers via de Europese dienst, met het validatieresultaat en tijdstip opgeslagen bij de klant; locatiebewijs vastgelegd bij de checkout; automatische pdf-uitgifte bij betaling met een kopie in het account van de klant; creditnota's voor de negentien onjuiste facturen en de gecorrigeerde vervangende facturen; en een driemaandelijkse CSV-export in het formaat van zijn accountant.

**Resultaat:** het kwartaal werd gecorrigeerd met creditnota's in plaats van met de hand gereconstrueerd, de kwartaalrekening van de accountant daalde met zo'n €400 per kwartaal, en negentien zakelijke klanten kregen niet langer btw gerekend die ze niet hoefden te betalen — waar twee van hen al naar hadden gevraagd.

> *"Ik dacht dat facturatie administratie was die ik zelf kon doen, totdat het een complianceprobleem werd dat ik niet kon oplossen. Een teller die bij één begint en nooit een nummer overslaat, is de saaiste functie waar ik ooit voor heb betaald, en degene die ik opnieuw als eerste zou kopen."*
> — **Tijmen Verhagen, Oprichter, Keurmerkbeheer (Amersfoort)**

**Kosten & Doorlooptijd:** €3.100 (factuurreeks en onveranderbare registratie, btw-bepaling met btw verlegd, btw-validatie, locatiebewijs, pdf-uitgifte en verzending, creditnota's, boekhoudexport) — afgerond in 6 werkdagen.

## Veelgestelde vragen

### Kan ik niet gewoon de facturen van mijn betaalprovider gebruiken?

Soms, in eenvoudige gevallen. Ze vermelden standaard uw KvK-nummer niet, handelen btw verlegd niet altijd af zoals uw accountant verwacht, en maken u afhankelijk van hun dashboard voor administratie die u verplicht bent te bewaren. Hebt u zakelijke klanten, geef dan uw eigen facturen uit.

### Moet ik btw rekenen aan een klant in Duitsland?

Aan een bedrijf met een geldig btw-nummer niet — de btw wordt verlegd, en de factuur moet dat vermelden en hun nummer tonen. Aan een consument rekent u Duitse btw en draagt u die af via OSS, tenzij u onder de EU-brede drempel blijft en ervoor hebt gekozen Nederlandse btw te blijven rekenen.

### Wie is verantwoordelijk als een klant een vals btw-nummer opgeeft?

U. Valideer elk nummer via de Europese dienst op het moment van verkoop en sla het resultaat op met een tijdstip, zodat u kunt laten zien wat u controleerde en wanneer.

### Kan ik een factuur na verzending nog wijzigen?

Nee. Geef een creditnota uit met verwijzing naar het origineel en daarna een gecorrigeerde factuur. Uitgegeven facturen wijzigen is de snelste manier om uw boekhouding te laten afwijken van uw bankafschriften.

### Wanneer moet ik dit bouwen — vóór of na de lancering?

Voordat u de tiende betaling ontvangt. Het werk is in beide gevallen hetzelfde, maar het achteraf doen voegt het reconstrueren toe van alles wat al is gebeurd, en dat is het dure deel.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik niet gewoon de facturen van mijn betaalprovider gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Soms, voor eenvoudige consumentengevallen. Ze missen velden zoals uw KvK-nummer, handelen btw verlegd inconsistent af, en laten uw wettelijke administratie in het dashboard van een ander."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik btw rekenen aan een klant in Duitsland?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet aan een bedrijf met een geldig btw-nummer — dan is de btw verlegd en moet dat op de factuur staan. Consumenten betalen het tarief van hun eigen land, af te dragen via OSS, tenzij u onder de drempel blijft."
      }
    },
    {
      "@type": "Question",
      "name": "Wie is verantwoordelijk als een klant een vals btw-nummer opgeeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U. Valideer via de Europese dienst op het moment van verkoop en sla het resultaat op met een tijdstip, als bewijs van wat u controleerde."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik een factuur wijzigen nadat die is verzonden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Geef een creditnota uit met verwijzing naar het origineel, en daarna een gecorrigeerde factuur. Uitgegeven facturen wijzigen laat boekhouding en bankgegevens van elkaar afwijken."
      }
    },
    {
      "@type": "Question",
      "name": "Moet facturatie vóór of na de lancering worden gebouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vóór de tiende betaling. De bouw is in beide gevallen identiek; het later doen voegt het reconstrueren van elke verkoop toe die al heeft plaatsgevonden."
      }
    }
  ]
}
</script>
