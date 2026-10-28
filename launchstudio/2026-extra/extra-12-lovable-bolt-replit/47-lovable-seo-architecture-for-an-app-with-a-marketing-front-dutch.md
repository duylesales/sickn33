---
Titel: "Lovable SEO: Architectuur voor een App met een Marketingvoorkant"
Trefwoorden: lovable seo, sitearchitectuur, rendering, indexeerbare pagina's, app-subdomein, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable SEO: Architectuur voor een App met een Marketingvoorkant

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Architectuur voor een App met een Marketingvoorkant",
  "description": "Een door AI gebouwd product is één applicatie die twee doelgroepen met tegengestelde behoeften bedient. Hoe u marketingpagina's en de ingelogde app zo inricht dat zoekmachines de ene kunnen lezen en de andere nooit zien.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-seo-architecture-for-an-app-with-a-marketing-front" }
}
</script>

Een product dat met Lovable is gebouwd, is meestal één applicatie die twee taken doet. Ze toont marketingpagina's aan vreemden die ze moeten kunnen vinden, en ze draait een ingelogde applicatie voor klanten die geen enkele zoekmachine ooit mag zien.

Die twee taken hebben tegengestelde eisen, en de standaarduitvoer bedient geen van beide goed: de marketingpagina's worden door JavaScript opgebouwd op een manier die ze traag en soms onzichtbaar maakt voor zoekmachines, terwijl de routes van de applicatie technisch crawlbaar zijn en af en toe in zoekresultaten verschijnen als lege pagina's met de titel "Loading".

De oplossing is architectonisch, en ze is makkelijker vóór u verkeer hebt dan erna.

## Waarom Gegenereerde Pagina's Moeite Hebben

De uitvoer van deze tools is doorgaans een single-page application. De server stuurt een bijna leeg HTML-document en JavaScript bouwt de pagina in de browser op.

Zoekmachines kunnen JavaScript uitvoeren, dus dit is niet fataal. Het is wel een handicap: het opbouwen wordt in een wachtrij gezet en vertraagd in plaats van direct gedaan, elke fout in uw script betekent dat de pagina helemaal geen inhoud heeft, en dezelfde pagina is trager voor elke bezoeker op een middenklasse telefoon.

Het alternatief is dat de server echte HTML stuurt - ofwel bij de build gegenereerd voor pagina's die zelden veranderen, ofwel per verzoek opgebouwd. Marketingpagina's, blogartikelen en publieke overzichten horen allemaal in die categorie, en voor een klein product is statische generatie bij de build zowel de snelste als de eenvoudigste optie.

Dit is de beslissing die al het andere bepaalt, en degene die het meest waarschijnlijk later een herstructurering vereist als u haar laat liggen.

## Scheid de Twee Helften

Trek een duidelijke lijn tussen wat publiek is en wat achter een login zit.

Alles wat publiek is - home, productpagina's, prijzen, blog, documentatie, publieke overzichten - wordt statisch gegenereerd, aan de rand gecachet, en is indexeerbaar.

Alles wat privé is - dashboards, instellingen, klantdata, alles na het inloggen - wordt volledig uitgesloten van indexering, en er is geen reden waarom het snel moet zijn voor een crawler, omdat er geen crawler hoort te komen.

Twee manieren om de lijn te trekken. Een padvoorvoegsel, met de applicatie onder iets als `/app`, wat één domein houdt en het eenvoudigst is. Of een subdomein, met `app.uwproduct.nl` los van de marketingsite, wat het mogelijk maakt de twee onafhankelijk te bouwen en uit te rollen.

Padvoorvoegsels passen bij de meeste kleine producten. Subdomeinen verdienen hun complexiteit wanneer de marketingsite apart wordt beheerd, bijvoorbeeld in een CMS dat uw marketingmedewerker bewerkt zonder de applicatie aan te raken.

## Sluit de Applicatie Goed Uit

Oprichters vertrouwen hiervoor op robots.txt, en dat doet het verkeerde.

Een pad in robots.txt verbieden, vraagt crawlers het niet te bezoeken. Het voorkomt niet dat een pagina wordt geïndexeerd als er van elders naar wordt gelinkt - wat de slechtste uitkomst oplevert: een zoekresultaat met uw URL, geen beschrijving, en geen manier voor de crawler om te zien dat het er niet hoort te staan, omdat u hem zei niet te kijken.

Het betrouwbare mechanisme is een noindex-instructie op de pagina's zelf, in de HTML of als header, die crawlers moeten ophalen om te zien. Dus: sta het crawlen van de routes van de applicatie toe, en zeg duidelijk dat ze niet moeten worden geïndexeerd. Combineer dat met authenticatie, wat betekent dat de meeste inhoud toch niet bereikbaar is.

Waar dit meer uitmaakt dan oprichters verwachten, zijn preview-deployments, die vaak publieke URL's zijn met een volledige kopie van uw site en, zonder instructie, indexeerbare duplicaten van alles.

## Eén URL per Pagina

Dubbele content in door AI gebouwde sites komt voort uit een kleine set oorzaken, en elk is een oplossing van één regel.

Dezelfde pagina bereikbaar met en zonder slash aan het eind, met en zonder `www`, via zowel HTTP als HTTPS, met queryparameters van campagnes erachter, en op zowel `/blog/artikel` als `/blog/artikel/`. Elke variatie is een aparte URL die een crawler als aparte pagina kan behandelen.

Kies één vorm, stuur de andere permanent door, en zet op elke pagina een canonieke link die de voorkeurs-URL noemt. Het kost een kwartier en neemt een hele categorie problemen weg die anders elke pagina die u publiceert verwatert.

## De Pagina's Die het Hebben Waard Zijn

Architectuur is alleen nuttig als er iets te indexeren is. Het publieke oppervlak van een product hoort minimaal te bevatten: een homepage die duidelijk zegt wat het product doet en voor wie, een pagina per belangrijke functie of toepassing, een prijspagina met echte prijzen, een over-pagina die het bedrijf en de mensen identificeert, en contactgegevens.

Daarna de pagina's die in de loop van de tijd verkeer opleveren: artikelen die de vragen beantwoorden die uw klanten stelden voordat ze kochten, vergelijkingen met de alternatieven die ze overwogen, en documentatie als uw product enige diepgang heeft.

Voor een Nederlands product is er nog een overweging die elders in deze reeks wordt behandeld: of die pagina's in het Nederlands, het Engels of beide bestaan, en hoe ze met elkaar samenhangen.

## Controleer Wat de Server Werkelijk Stuurt

De nuttigste afzonderlijke diagnose op dit terrein kost tien seconden en bijna niemand doet haar: haal uw eigen pagina op zoals een crawler dat doet, zonder browser, en lees wat er terugkomt.

Vraag vanuit een terminal de URL op en kijk naar de HTML. Staan uw kop, uw lopende tekst en uw links in dat antwoord, dan kunnen zoekmachines de pagina direct lezen. Komt er een containerdiv en een scripttag terug, dan hangt alles af van een opbouw die vertraagd kan zijn of kan mislukken.

Doe hetzelfde voor drie of vier paginatypes - home, een artikel, een functiepagina, een prijspagina - omdat ze in een gedeeltelijk gemigreerde site vaak verschillen.

Twee verwante controles die dezelfde tien seconden waard zijn. Bevestig dat uw interne links echte ankers met href-attributen zijn in plaats van klikhandlers op divs, omdat een crawler de eerste volgt en de tweede niet kan zien. En bevestig dat de responsstatus is wat u verwacht: een pagina die 200 teruggeeft voor een URL die niet bestaat, betekent dat elke verkeerd getypte link een geïndexeerde lege pagina wordt, wat een verrassend veelvoorkomende configuratie is in single-page applications waar de server voor alles hetzelfde document teruggeeft.

Deze drie controles vertellen u meer over of een site kan ranken dan welke audittool ook, en ze zijn het eerste wat u controleert na elke wijziging in hoe pagina's worden gebouwd.

## De Titels en Beschrijvingen Die Gegenereerde Sites Delen

Een single-page application heeft doorgaans één titel, één keer in het document gedefinieerd, en die blijft op elke route hetzelfde. Elke pagina in de zoekresultaten draagt dan dezelfde tekst, wat zowel onbehulpzaam is voor een lezer die tussen resultaten kiest als een gemiste kans op elke pagina die u publiceert.

Elke pagina heeft een eigen titel en beschrijving nodig, geschreven voor die pagina. Een titel is ongeveer zestig tekens en moet het specifieke ding noemen plus, waar het past, het product of bedrijf. Een beschrijving is ongeveer honderdzestig tekens en is een advertentie in plaats van een samenvatting - haar taak is iemand te laten klikken, niet de kop te herhalen.

Drie gewoontes maken dit beheersbaar in plaats van saai. Stel ze in waar de inhoud van de pagina wordt gedefinieerd, zodat het schrijven van een nieuw artikel betekent dat u tegelijk de titel en beschrijving schrijft. Genereer ze uit de inhoud voor pagina's die uit data worden opgebouwd, met een patroon dat iets specifieks oplevert in plaats van een sjabloon met een ingevulde variabele. En controleer ze af en toe in bulk - een lijst met de titel en beschrijving van elke pagina, in één keer gelezen, maakt duplicaten en weglatingen duidelijk op een manier die het afzonderlijk bekijken van pagina's nooit doet.

Hetzelfde geldt voor de preview die wordt getoond wanneer een link in een bericht of een social post wordt gedeeld. Een gegenereerde site heeft meestal één afbeelding en één beschrijving voor het hele domein, zodat elk gedeeld artikel er hetzelfde uitziet.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans twee tot drie dagen: publieke pagina's omgezet naar statische generatie of serverrendering met echte HTML in het antwoord, de publieke en private helften gescheiden via padvoorvoegsel of subdomein, de applicatie uitgesloten van indexering met een noindex-instructie in plaats van alleen robots.txt, preview-deployments beschermd en uitgesloten, één canonieke URL per pagina met permanente doorverwijzingen vanaf elke variatie, een sitemap gegenereerd uit de werkelijke routes en ingediend, gestructureerde data op de pagina's waar die van toepassing is, en het publieke oppervlak bekeken op de pagina's die een koper zou zoeken en nu niet kan vinden.

LaunchStudio doet dit als onderdeel van het vindbaar maken van een door AI gebouwd product, vaak het eerste groeiwerk dat een gelanceerd product nodig heeft. Daarachter staat Manifera - elf jaar, 160+ projecten, met Europees klantcontact vanaf de Herengracht 420 in Amsterdam.

[Vraag ons wat een zoekmachine nu op uw homepage ziet](https://launchstudio.eu/nl/#contact). Soms is dat niets.

## Echt voorbeeld

### Een Product Dat Niemand Kon Vinden

Jasmijn Kolthof bouwde Voorraadslim in Lovable: voorraadbeheer voor zelfstandige winkeliers en webshops, 130 klanten die bijna volledig via een Facebookgroep en mond-tot-mondreclame waren binnengekomen.

Ze had in een jaar elf artikelen over voorraadbeheer geschreven, en geen ervan verscheen voor wat dan ook in de zoekresultaten. Haar homepage rankte niet eens op haar eigen productnaam.

De site was een single-page application. De HTML die voor elke URL werd geserveerd, was identiek - een lege container en een script - met de inhoud in de browser opgebouwd. Zoekmachines hadden de homepage geïndexeerd met de titel "Voorraadslim" en zonder beschrijving, en verder niets, omdat de interne links volledig in JavaScript werden afgehandeld, zonder echte href-attributen. Daarnaast waren 40 routes van de applicatie indexeerbaar en waren er vier geïndexeerd als lege pagina's, een ervan met de titel "Loading...". Dezelfde inhoud was bereikbaar via vier URL-variaties, en drie preview-deployments waren volledig geïndexeerd als duplicaten van de hele site.

Vier werkdagen: publieke pagina's omgezet naar statische generatie, zodat de server volledige HTML teruggeeft, met de artikelen, functiepagina's en prijzen bij de deploy gebouwd; interne links herschreven als echte ankers met href-attributen; de applicatie verplaatst onder een `/app`-voorvoegsel en uitgesloten met een noindex-instructie, met robots.txt aangepast zodat crawlen is toegestaan en de instructie kan worden gezien; preview-deployments achter toegangsbeveiliging gezet en uitgesloten; één canonieke URL-vorm gekozen met permanente doorverwijzingen vanaf de www-, slash- en HTTP-varianten, en een canonieke link op elke pagina; een sitemap gegenereerd uit de werkelijke routelijst en ingediend; gestructureerde data voor artikelen toegevoegd; de vier geïndexeerde applicatiepagina's via de zoekconsole uit de index verwijderd; en twee ontbrekende pagina's geschreven - een prijspagina met echte prijzen, die nooit had bestaan, en een over-pagina die het bedrijf identificeert.

**Resultaat:** binnen acht weken waren negen van de elf artikelen geïndexeerd en rankten ze, en gingen de organische bezoeken van 40 per maand naar 610. Twee van de artikelen leveren nu meer proefaanmeldingen op dan de Facebookgroep. Jasmijns opmerking is dat ze de inhoud een jaar eerder had geschreven en dat er niets mis mee was - het kon gewoon niet worden gelezen.

> *"Ik dacht dat mijn artikelen niet goed genoeg waren. Ze waren nooit gezien. De server stuurde iedereen een lege pagina, en alleen browsers zetten de woorden erin."*
> - **Jasmijn Kolthof, Oprichter, Voorraadslim (Zutphen)**

**Kosten & Doorlooptijd:** €3.500 (statische generatie voor publieke pagina's, echte interne links, scheiding van de applicatie en noindex, previewbeveiliging, canonieke URL's en doorverwijzingen, sitemap, gestructureerde data, opschonen van de index, ontbrekende pagina's) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Kunnen zoekmachines pagina's lezen die door JavaScript worden opgebouwd?

Ze kunnen JavaScript uitvoeren, maar het opbouwen is vertraagd en kwetsbaar, en een scriptfout betekent helemaal geen inhoud. Publieke pagina's moeten als echte HTML worden geserveerd, waar mogelijk bij de build gegenereerd.

### Moet mijn app op een subdomein of een pad staan?

Een padvoorvoegsel zoals `/app` is het eenvoudigst en past bij de meeste kleine producten. Een subdomein verdient zijn complexiteit wanneer de marketingsite apart wordt gebouwd of beheerd.

### Is robots.txt genoeg om mijn app uit de zoekresultaten te houden?

Nee. Het vraagt crawlers niet te bezoeken, maar voorkomt niet dat gelinkte URL's worden geïndexeerd, wat resultaten zonder beschrijving oplevert. Gebruik een noindex-instructie op de pagina's zelf.

### Waarom verschijnen dezelfde pagina's op meerdere URL's?

Slashes aan het eind, www, HTTP en campagneparameters maken elk een variatie. Kies één vorm, stuur de andere permanent door, en voeg op elke pagina een canonieke link toe.

### Welke publieke pagina's moeten minimaal bestaan?

Een homepage die duidelijk zegt wat het product doet, een pagina per belangrijke toepassing, echte prijzen, een over-pagina die het bedrijf identificeert, en contactgegevens - daarna artikelen die vragen van vóór de aankoop beantwoorden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kunnen zoekmachines door JavaScript opgebouwde pagina's lezen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat kunnen ze, maar het opbouwen is vertraagd en kwetsbaar. Publieke pagina's moeten echte HTML teruggeven, waar mogelijk statisch gegenereerd."
      }
    },
    {
      "@type": "Question",
      "name": "Moet de app op een subdomein of een pad staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een padvoorvoegsel als /app past bij de meeste kleine producten; een subdomein is de moeite waard wanneer de marketingsite apart wordt beheerd."
      }
    },
    {
      "@type": "Question",
      "name": "Houdt robots.txt een app uit de zoekresultaten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - het voorkomt crawlen, niet het indexeren van gelinkte URL's. Gebruik een noindex-instructie die de crawler werkelijk kan ophalen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verschijnt één pagina op meerdere URL's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slashes aan het eind, www, HTTP en campagneparameters maken elk varianten. Stuur door naar één canonieke vorm en vermeld die op elke pagina."
      }
    },
    {
      "@type": "Question",
      "name": "Welke publieke pagina's heeft een product minimaal nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een duidelijke homepage, een pagina per toepassing, echte prijzen, een over-pagina die het bedrijf identificeert, en contactgegevens."
      }
    }
  ]
}
</script>
