---
Titel: "Lovable SEO: Core Web Vitals in een Door AI Gebouwde Frontend"
Trefwoorden: lovable seo, core web vitals, LCP, INP, CLS, laadsnelheid, bundelgrootte, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable SEO: Core Web Vitals in een Door AI Gebouwde Frontend

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Core Web Vitals in een Door AI Gebouwde Frontend",
  "description": "Gegenereerde frontends zijn op voorspelbare manieren zwaar. Wat de drie meetwaarden meten, waarom labscores misleiden, en de vijf wijzigingen die de meeste door AI gebouwde sites oplossen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-seo-core-web-vitals-in-an-ai-built-frontend" }
}
</script>

Core Web Vitals zijn drie metingen van hoe het gebruik van uw site aanvoelt: hoe lang het duurt voordat de hoofdinhoud verschijnt, hoe snel de pagina reageert wanneer iemand iets doet, en of dingen verschuiven terwijl ze aan het lezen zijn.

Ze zijn een rankingfactor, en daarom verschijnen ze in SEO-discussies. Ze doen er aanzienlijk meer toe als conversiefactor, omdat een pagina die op een telefoon zes seconden nodig heeft een flink deel verliest van de mensen die erom vroegen — en het rankingeffect is klein vergeleken daarmee.

Door AI gebouwde frontends falen er op consistente manieren voor, en dat is goed nieuws: de oplossingen zijn elke keer dezelfde.

## De Drie Meetwaarden, Praktisch

**Largest Contentful Paint** — hoe lang het duurt tot het grootste zichtbare element verschijnt. Onder de 2,5 seconden is goed. Op gegenereerde sites is dit meestal traag omdat de pagina door JavaScript wordt opgebouwd nadat een grote bundel is gedownload, of omdat de hero-afbeelding enorm is.

**Interaction to Next Paint** — hoe snel de pagina reageert wanneer iemand tikt of typt. Onder de 200 milliseconden is goed. Mislukkingen komen door te veel JavaScript dat de main thread bezet houdt, en zijn veel erger op middenklasse Android-telefoons dan op de laptop van een developer.

**Cumulative Layout Shift** — hoeveel inhoud verschuift tijdens het laden. Onder de 0,1 is goed. Veroorzaakt door afbeeldingen zonder afmetingen, lettertypen die wisselen, banners die boven de inhoud worden ingevoegd, en alles wat verschijnt nadat de pagina is weergegeven.

## Meet Echte Bezoekers, Geen Laboratorium

Een tool voor laadsnelheid geeft u een labscore uit één gesimuleerde run. Die is nuttig voor diagnose en misleidend als maat voor de werkelijkheid.

Wat telt, is velddata — werkelijke metingen van werkelijke bezoekers op hun werkelijke apparaten en verbindingen. Zoekconsoles rapporteren het, en het is het getal dat uw gebruikers weerspiegelt.

Het verschil tussen de twee is vaak groot, en altijd in dezelfde richting. Uw labscore wordt gegenereerd op een snelle verbinding; uw Nederlandse klanten zijn onder andere mensen in de trein met een vier jaar oude telefoon. Het labgetal optimaliseren terwijl het veldgetal slecht blijft, is de meest voorkomende manier waarop dit werk wordt verspild.

Hebt u te weinig verkeer voor velddata, test dan op een echte middenklasse telefoon met een vertraagd netwerk. Het is ongemakkelijk en het is de waarheid.

## De Vijf Wijzigingen Die de Meeste Sites Oplossen

**Serveer echte HTML voor publieke pagina's.** Elders in deze reeks behandeld, en de grootste afzonderlijke factor: staat de inhoud in het antwoord van de server, dan kan het grootste element direct worden getoond in plaats van nadat een bundel is gedownload en uitgevoerd.

**Herstel de afbeeldingen.** Correcte afmetingen in de opmaak zodat niets verschuift, moderne formaten, groottes afgestemd op weergave, lazy loading voor alles onder de vouw — en specifiek *geen* lazy loading voor de hero-afbeelding, een veelvoorkomende fout die direct schaadt aan de meetwaarde waarmee ze had moeten helpen.

**Verminder het JavaScript.** Gegenereerde sites leveren routinematig enkele honderden kilobytes voor een marketingpagina zonder interactiviteit. Splits per route zodat een bezoeker downloadt wat die pagina nodig heeft, verwijder componentenbibliotheken die voor één element worden gebruikt, en bevraag alles wat voor één functie wordt geïmporteerd.

**Host de lettertypen zelf, met een terugval.** Een lettertype dat bij een derde partij wordt opgehaald, kost een verbinding en een heen-en-terugreis voordat er tekst verschijnt, en er later naar wisselen verschuift de lay-out. Host zelf, preload het ene lettertype dat u nodig hebt, en stel een terugvalreeks in zodat tekst direct leesbaar is.

**Verwijder scripts van derden van pagina's die ze niet nodig hebben.** Chatwidgets, analytics, insluitingen en tagmanagers kosten elk tijd op de main thread. Op een marketingpagina zijn de meeste optioneel.

## Reserveer Ruimte voor Alles Wat Laat Binnenkomt

Layout shift is de makkelijkste meetwaarde om op te lossen en de meest zichtbare voor gebruikers, omdat het de reden is dat iemand op het verkeerde ding tikt.

Elk element dat na de eerste weergave verschijnt, moet zijn ruimte gereserveerd hebben: afbeeldingen en video met expliciete afmetingen of een beeldverhouding, advertenties en insluitingen met een container van de juiste grootte, meldingsbanners die boven de vouw worden weergegeven in plaats van erin te worden ingevoegd, en dynamisch geladen inhoud die een placeholder van de juiste grootte inneemt.

De test is uw pagina op een trage verbinding te laden en te kijken. Alles wat verspringt, is een gebrek dat u kunt zien, en het kost minuten om te vinden.

## Jaag Niet op een Perfecte Score

Een score van 100 is niet het doel, en ernaar streven levert snel steeds minder op.

De drempels zijn wat ertoe doet: LCP onder 2,5 seconden, INP onder 200 milliseconden, CLS onder 0,1, voor het 75e percentiel van echte bezoekers. Een site die aan alle drie voldoet, is in orde, en verdere optimalisatie levert heel weinig op in ranking of conversie.

Besteed de bespaarde moeite aan content, want daar zit de echte ranking.

## Voorkom Dat Het Terugkomt

Prestaties gaan op dezelfde manier achteruit als toegankelijkheid: geleidelijk, door afzonderlijke wijzigingen die elk onschuldig lijken.

Een AI-sessie voegt een grafiekbibliotheek toe voor één kleine visualisatie en die belandt in de gedeelde bundel. Een marketingverzoek voegt een ingesloten video toe aan de homepage. Er komt een animatiebibliotheek binnen voor één overgang. Geen ervan is onredelijk, en samen maken ze in vier maanden een dag werk ongedaan.

Twee maatregelen houden de lijn vast op de schaal van een klein product.

**Een budget, afgedwongen in de build.** Noem een maximale grootte voor het JavaScript dat aan publieke pagina's wordt geserveerd — 200 KB gecomprimeerd is een redelijk uitgangspunt voor een marketingsite — en laat de build falen als het wordt overschreden. De mislukking dwingt een beslissing af in plaats van een opstapeling toe te staan, en die beslissing is meestal "laad dit alleen op de pagina die het nodig heeft".

**Een maandelijkse blik op velddata.** Vijf minuten in de zoekconsole, de drie meetwaarden vergeleken met vorige maand. Een sprong wijst naar een specifieke deploy, wat veel makkelijker te onderzoeken is dan een geleidelijke daling die een jaar later wordt ontdekt.

De gewoonte die bij beide hoort: vraag bij het toevoegen van een bibliotheek welke pagina's haar nodig hebben. In een gegenereerde codebase is de standaard dat alles overal wordt geïmporteerd, en het verschil tussen dat en laden per route is vaak het hele prestatieprobleem van een site.

## De Applicatie Verdient Dezelfde Aandacht

De meetwaarden zijn een zoekoverweging voor publieke pagina's, en een retentieoverweging voor het product achter de login — waar dezelfde bezoeker elke dag terugkomt in plaats van één keer.

De faalwijzen verschillen. Publieke pagina's zijn traag omdat er te veel wordt gedownload voordat er iets verschijnt. Applicaties zijn traag omdat er te veel werk gebeurt nadat de data is binnengekomen: een lijst die vierhonderd rijen tegelijk weergeeft, een component dat bij elke toetsaanslag opnieuw rekent, een tabel die de hele dataset in de browser opnieuw sorteert.

De meting die binnen een product ertoe doet, is responsiviteit — de vertraging tussen een handeling van de gebruiker en het moment dat er iets gebeurt. Typen in een zoekvak dat per teken 300 milliseconden bevriest, is een product dat mensen traag noemen zonder te kunnen zeggen waarom, en het is steevast werk op de main thread dat kan worden uitgesteld, gedebounced of naar de server verplaatst.

Drie controles vinden het meeste. Open het drukste scherm met een apparaat dat is vertraagd tot een kwart van zijn snelheid en gebruik het normaal. Typ snel in elk zoek- en filterveld. En laad het account met de meeste data in plaats van uw eigen testaccount, het verschil tussen een product dat goed aanvoelt en een product waarover uw grootste klant klaagt.

De oplossingen zijn meestal klein: debounce de invoer, pagineer de lijst, verplaats het sorteren naar de database, en geef alleen weer wat zichtbaar is. Geen ervan is architectonisch, en samen veranderen ze hoe een dagelijks gebruikt product aanvoelt.

Het is ook het werk dat het meest waarschijnlijk wordt opgemerkt door de mensen die u betalen. Niemand schrijft om te zeggen dat uw marketingpagina snel laadt; klanten merken absoluut wanneer het scherm dat ze veertig keer per dag openen hen niet meer laat wachten.

## Dit Inrichten

Voor een bestaande site kost dit doorgaans één tot twee dagen: velddata bekeken voor echte bezoekers in plaats van labscores, publieke pagina's geserveerd als echte HTML, afbeeldingen voorzien van expliciete afmetingen en moderne formaten met de hero direct geladen en de rest lazy, JavaScript gesplitst per route met onnodige bibliotheken verwijderd, lettertypen zelf gehost met preload en een terugvalreeks, scripts van derden verwijderd van pagina's die ze niet nodig hebben, ruimte gereserveerd voor alles wat laat binnenkomt, en controle op een echte middenklasse telefoon met een vertraagde verbinding in plaats van op een laptop.

LaunchStudio doet dit samen met het architecturale werk dat het meestal bepaalt, omdat de keuze voor rendering het plafond legt voor al het andere. Daarachter staat Manifera — elf jaar, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons wat uw site scoort voor echte bezoekers](https://launchstudio.eu/nl/#contact), niet in een test.

## Echt voorbeeld

### Snel op een Laptop, Onbruikbaar in de Trein

Nienke Brandts bouwde Cursusplein in Lovable: een marktplaats met trainingen van 210 aanbieders, waar cursisten zoeken, vergelijken en boeken.

Haar score voor laadsnelheid op een laptop was 88 en ze beschouwde prestaties als opgelost. Haar velddata vertelde iets anders: LCP op het 75e percentiel was 5,8 seconden, INP 410 milliseconden, en CLS 0,34. Zo'n 70 procent van haar bezoekers zat op een telefoon.

De specifieke bevinding die het concreet maakte: haar boekingsconversie op mobiel was een derde van die op desktop, wat ze had toegeschreven aan een verschil in gedrag in plaats van aan prestaties.

Twee werkdagen: overzichts- en detailpagina's van cursussen omgezet naar statische generatie met op de server opgebouwde HTML, wat LCP alleen al van 5,8 naar 2,1 seconden bracht; de hero-afbeelding op overzichtspagina's voorzien van expliciete afmetingen en uit lazy loading gehaald, wat het grootste element bewust had vertraagd; miniaturen van cursussen omgezet naar moderne formaten op weergaveformaat, wat een overzichtspagina terugbracht van 3,8 MB naar 340 KB; JavaScript gesplitst per route, met een datumbibliotheek, een grafiekbibliotheek die op één beheerscherm werd gebruikt, en een componentenbibliotheek voor twee knoppen verwijderd uit de publieke bundel, die daardoor van 780 KB naar 190 KB ging; twee lettertypen zelf gehost met één voorgeladen en een terugvalreeks ingesteld, ter vervanging van een import bij een derde partij; een chatwidget verwijderd van publieke pagina's en alleen in het boekingsproces behouden; expliciete ruimte gereserveerd voor het logo van de aanbieder en de beschikbaarheidsbanner, die allebei na de weergave werden ingevoegd en het grootste deel van de layout shift veroorzaakten; en alles gecontroleerd op een vier jaar oude Android-telefoon op een vertraagde verbinding in plaats van op een laptop.

**Resultaat:** de LCP in het veld stabiliseerde op 1,9 seconden, INP op 140 milliseconden en CLS op 0,02. De boekingsconversie op mobiel steeg in de twee maanden daarna van 1,1 naar 2,9 procent, wat bij haar volume ongeveer €4.100 per maand aan commissie waard was. De organische rankings verbeterden licht; de conversiewijziging was degene die ertoe deed.

> *"Mijn score op een laptop was 88 en ik dacht dat ik klaar was. Mijn echte klanten zaten op telefoons in de trein, en voor hen duurde de site zes seconden en verschoof hij dan terwijl ze aan het tikken waren."*
> — **Nienke Brandts, Oprichter, Cursusplein (Haarlem)**

**Kosten & Doorlooptijd:** €2.900 (statische generatie voor publieke pagina's, afmetingen, formaten en laadstrategie voor afbeeldingen, bundelsplitsing en verwijderen van bibliotheken, zelf gehoste lettertypen met preload, verwijderen van scripts van derden, herstel van layout shift, controle op een echt apparaat) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Beïnvloeden Core Web Vitals echt de ranking?

Ze zijn een factor, en een bescheiden. Het grotere effect is op conversie — een pagina van zes seconden op een telefoon verliest een betekenisvol deel van de bezoekers voordat iets anders ertoe doet.

### Waarom is mijn labscore goed maar mijn velddata slecht?

Omdat het lab draait op een snelle verbinding en een krachtige machine, terwijl uw bezoekers onder andere middenklasse telefoons op mobiele netwerken gebruiken. Velddata op het 75e percentiel is het getal dat telt.

### Welke afzonderlijke wijziging helpt het meest bij een door AI gebouwde site?

Echte HTML serveren voor publieke pagina's in plaats van ze met JavaScript op te bouwen. Dat legt het plafond voor al het andere.

### Moet ik alle afbeeldingen lazy laden?

Nee. De hero-afbeelding lazy laden vertraagt het grootste element en schaadt LCP direct. Laad haar direct en laad lazy wat onder de vouw staat.

### Is een perfecte score het nastreven waard?

Nee. Haal de drempels — 2,5 seconden, 200 milliseconden, 0,1 — en besteed de resterende moeite aan content, want daar komt de ranking werkelijk vandaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Beïnvloeden Core Web Vitals de zoekranking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze zijn een bescheiden rankingfactor. Het grotere effect is conversie — trage pagina's verliezen bezoekers voordat de kwaliteit van de inhoud ertoe doet."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is mijn labscore goed maar mijn velddata slecht?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Labtests draaien op snelle verbindingen en krachtige apparaten. Velddata op het 75e percentiel weerspiegelt echte telefoons op echte netwerken."
      }
    },
    {
      "@type": "Question",
      "name": "Welke afzonderlijke wijziging helpt door AI gebouwde sites het meest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Echte HTML serveren voor publieke pagina's in plaats van ze in de browser op te bouwen — dat legt het plafond voor elke andere verbetering."
      }
    },
    {
      "@type": "Question",
      "name": "Moet elke afbeelding lazy worden geladen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De hero-afbeelding lazy laden schaadt LCP direct. Laad haar direct en laad alleen lazy wat onder de vouw staat."
      }
    },
    {
      "@type": "Question",
      "name": "Is een perfecte prestatiescore het najagen waard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Haal de drempels en besteed de resterende moeite aan content, die de ranking veel meer bepaalt."
      }
    }
  ]
}
</script>
