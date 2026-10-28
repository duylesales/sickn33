---
Titel: "Lovable Hosting: Caching en Pagina's Die Snel Blijven Onder Belasting"
Trefwoorden: lovable hosting, caching, CDN, cache-headers, stale-while-revalidate, paginaprestaties, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Caching en Pagina's Die Snel Blijven Onder Belasting

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Caching en Pagina's Die Snel Blijven Onder Belasting",
  "description": "De meeste door AI gebouwde apps berekenen elke pagina voor elke bezoeker opnieuw. Wat op een CDN hoort, wat in een korte servercache hoort, wat nooit gecachet mag worden, en hoe u voorkomt dat u de data van de ene klant aan de andere serveert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-caching-and-pages-that-stay-fast-under-load" }
}
</script>

Een product dat snel is voor tien gebruikers en traag voor tweehonderd, komt meestal geen capaciteit tekort. Het doet hetzelfde werk steeds opnieuw - de database dezelfde vraag stellen, dezelfde marketingpagina opbouwen, dezelfde afbeelding verkleinen - één keer per bezoeker, de hele dag.

Caching is het één keer doen van dat werk en het antwoord hergebruiken. Het is de goedkoopste prestatieverbetering die een klein product kan krijgen, het vereist geen nieuwe infrastructuur, en het ontbreekt vrijwel volledig in applicaties die door AI-tools zijn gebouwd, omdat niets in de gegenereerde code het suggereert.

Het is ook het terrein waar een onzorgvuldige wijziging de ergst denkbare fout veroorzaakt, dus het is de moeite waard de grenzen te begrijpen voordat u iets aanzet.

## Drie Plekken Waar Dingen Gecachet Kunnen Worden

**Het CDN**, het netwerk van servers tussen uw applicatie en uw bezoekers. Alles wat hier wordt gecachet, wordt geserveerd zonder dat uw applicatie draait, en daar zit de grootste winst.

**Uw server**, die berekende resultaten korte tijd in het geheugen of in een opslag bewaart, zodat een verzoek dat twee keer binnenkomt het dure werk één keer doet.

**De browser**, die bestanden bewaart die hij al heeft gedownload, zodat een terugkerende bezoeker niets ophaalt.

De meeste producten hebben alle drie nodig, toegepast op verschillende dingen, en de kunst zit volledig in weten in welke categorie elk stuk content hoort.

## Wat Agressief Gecachet Kan Worden

Statische bestanden - JavaScript, CSS, afbeeldingen, lettertypen - met een vingerafdruk in de bestandsnaam kunnen een jaar worden gecachet, omdat een nieuwe build een nieuwe bestandsnaam oplevert. Uw buildtool doet de vingerafdruk al; de enige stap is de header die zegt dat ze onbeperkt bewaard mogen worden.

Publieke pagina's die voor iedereen identiek zijn - marketingpagina's, blogartikelen, documentatie, prijzen, publieke overzichten - kunnen minuten of uren op het CDN worden gecachet. Dit is de wijziging die een product een vermelding op een grote site laat overleven: de pagina wordt vanaf de rand geserveerd en uw applicatie ziet het verkeer nooit.

Publieke API-antwoorden die langzaam veranderen, zoals een lijst met categorieën of landen, kunnen ook een tijd worden gecachet, en dat gebeurt vaak niet omdat ze klein zijn - maar klein en bij elke paginalading opgevraagd is nog steeds werk.

## Wat Nooit aan de Rand Gecachet Mag Worden

Alles wat specifiek is voor één gebruiker. Zijn dashboard, zijn instellingen, zijn lijst van wat dan ook, elk antwoord dat afhangt van wie het vraagt.

De catastrofale mislukking op dit terrein is een CDN dat een gepersonaliseerde pagina cachet en aan de volgende bezoeker serveert. Het gebeurt wanneer een antwoord als publiek cachebaar wordt gemarkeerd zonder op te merken dat het afhangt van een sessiecookie, en het resultaat is dat de ene klant de data van een andere klant ziet - de ernstigste fout die een product kan hebben, en een die nergens een foutmelding oplevert.

Twee regels voorkomen het. Geauthenticeerde antwoorden worden bewust als private en no-store gemarkeerd, in plaats van aan een standaard overgelaten. En elk antwoord dat varieert op een header of cookie zegt dat expliciet, zodat een gedeelde cache weet dat het niet tussen gebruikers kan worden hergebruikt.

Neemt u één ding mee: controleer vandaag welke cacheheaders uw geauthenticeerde endpoints sturen. Het is één commando en af en toe een noodgeval.

## De Middenweg Die de Meeste Producten Nodig Hebben

Tussen "een jaar cachen" en "nooit cachen" zit het nuttige werk, en één patroon dekt het meeste: serveer direct de opgeslagen kopie, en ververs haar op de achtergrond als ze ouder is dan een drempel.

De bezoeker krijgt een direct antwoord. De inhoud is hooguit iets verouderd. Het dure werk gebeurt één keer per verversingsinterval in plaats van één keer per bezoeker, en niemand wacht er ooit op.

Dit past precies bij de dingen waar een klein product mee worstelt: een dashboardsamenvatting over veel rijen, een publieke overzichtspagina, een rapport, een aggregatie. Dertig seconden veroudering op een cijfer dat de afgelopen maand beschrijft, is geen gebrek, en het verandert een dure query in iets wat uit het geheugen wordt geserveerd.

De afweging per item is hoeveel veroudering acceptabel is, en het eerlijke antwoord is meestal veel langer dan het instinct zegt.

## Invalidatie Zonder Tranen

Het moeilijke deel van caching is weten wanneer een opgeslagen kopie niet meer klopt. Twee benaderingen, en de eerste wordt onderschat.

**Korte levensduur.** Verloopt een gecachet item na zestig seconden, dan is maximaal zestig seconden fout zijn het ergste wat er gebeurt, en schrijft u nooit invalidatielogica. Voor de meeste content in de meeste producten is dat volledig voldoende en de juiste standaard.

**Expliciete invalidatie** wanneer er iets verandert - het gecachete artikel wissen wanneer het wordt bewerkt, een pagina op het CDN legen wanneer ze opnieuw wordt gepubliceerd. Nodig wanneer veroudering zichtbaar is voor degene die de wijziging net maakte, en dat is precies de test: zou de redacteur zijn eigen wijziging direct zien?

Het patroon dat goed werkt: overal een korte levensduur, plus expliciet legen bij de handvol handelingen waar iemand op het resultaat let.

## Afbeeldingen Zijn Meestal de Grootste Winst

Op de meeste sites vormen afbeeldingen het grootste deel van de overgedragen bytes en het grootste deel van het paginagewicht waar een telefoon mee moet omgaan.

Drie wijzigingen, in volgorde van effect. Serveer ze op het formaat dat werkelijk wordt getoond in plaats van een foto van vier megapixel naar een miniatuur van 200 pixels te sturen. Serveer moderne formaten aan browsers die ze accepteren. En cache ze aan de rand met een lange levensduur, wat veilig is als de URL verandert wanneer de afbeelding verandert.

Hostingplatforms en Supabase bieden allebei beeldtransformatie op verzoek, wat betekent dat dit configuratie is in plaats van een pipeline om te bouwen. Het is vaak de grootste afzonderlijke verbetering die beschikbaar is voor de publieke pagina's van een door AI gebouwd product, en het kost een middag.

## Meet Vóór en Na, op een Echte Verbinding

Cachingwijzigingen zijn makkelijk om in te geloven en makkelijk verkeerd te doen, dus controleer ze.

Controleer of het antwoord waarvan u verwacht dat het gecachet is, dat ook echt is - de headers vertellen het u, en de meeste CDN's voegen er een toe die zegt of het een hit of een miss was. Controleer dat geauthenticeerde antwoorden dat niet zijn. Meet de pagina dan vanaf een trage verbinding op een middenklasse telefoon, want dat is de ervaring die het meest wordt geraakt en het minst wordt weerspiegeld door de laptop van een developer.

Volg de week daarna één getal: hoeveel verzoeken uw applicatie überhaupt bereiken. Een geslaagde cachingwijziging laat dat getal dalen terwijl het verkeer gelijk blijft, en het is het duidelijkste bewijs dat u zult krijgen.

## De Cache Waarvan U Niet Wist Dat U Hem Had

Voordat u iets toevoegt, is het de moeite waard te weten welke caches er al tussen uw code en uw gebruikers zitten, want dat zijn er meerdere en ze beïnvloeden elkaar.

De browser bewaart een eigen kopie van wat hij downloadde, volgens de headers die u stuurde - inclusief, bij sommige antwoorden, een standaard die uw framework voor u koos. Het CDN van uw hostingplatform cachet mogelijk automatisch voor statische paden en niet voor andere. Een bedrijfsproxy zit voor sommige van uw zakelijke klanten. En uw bibliotheek voor het ophalen van data op de client bewaart vrijwel zeker antwoorden een periode in het geheugen, wat verklaart waarom een waarde in de interface soms verouderd lijkt na een wijziging die zeker is opgeslagen.

Die laatste veroorzaakt in door AI gebouwde producten meer verwarring dan alle andere. De database klopt, de API geeft de nieuwe waarde terug, en het scherm toont de oude, omdat de clientbibliotheek haar gecachete kopie serveert totdat ze anders besluit. De oplossing is helemaal geen cacheheader - het is de gecachete invoer van de client ongeldig maken na een wijziging, wat de bibliotheek biedt en wat gegenereerde code routinematig weglaat.

Werk dus, als iets verouderd lijkt, van buiten naar binnen: controleer wat de database bevat, dan wat de API teruggeeft, dan wat het netwerktabblad toont, dan wat de client vasthoudt. Elke laag kan correct zijn terwijl de volgende dat niet is, en gokken welke verantwoordelijk is, is hoe een middag verdwijnt.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één dag: statische bestanden met vingerafdruk en een lange levensduur, publieke pagina's gecachet op het CDN met verstandige duur, geauthenticeerde antwoorden expliciet gemarkeerd als private en no-store en gecontroleerd, antwoorden die per gebruiker variëren die dat aangeven, dure aggregaties geserveerd uit een kortlevende cache met verversing op de achtergrond, expliciet legen bij de paar handelingen waar de auteur zijn wijziging moet zien, afbeeldingen omgezet naar weergaveformaat en moderne formaten met langlevende caching aan de rand, en een controle van hitrates en het aantal verzoeken naar de origin na de wijziging.

LaunchStudio doet dit in prestatiewerk, meestal samen met database-indexering, en samen zorgen ze ervoor dat een product bij tien keer zoveel verkeer precies hetzelfde aanvoelt. De engineers zijn van Manifera - elf jaar, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vertel ons uw drukste pagina](https://launchstudio.eu/nl/#contact) en wij vertellen u wat die zou moeten cachen.

## Echt voorbeeld

### De Campagne Die de Site Platlegde

Noor Vreugdenhil bouwde Tuincentrumgids in Lovable: een gids van tuincentra en kwekerijen in heel Nederland, met openingstijden, assortimentscategorieën en seizoensbeschikbaarheid, gefinancierd door uitgelichte vermeldingen van 120 bedrijven.

Een tuinprogramma noemde een van haar uitgelichte kwekerijen en linkte naar de pagina ervan. Het verkeer ging in twee uur van 400 bezoeken per dag naar 9.000. De site reageerde niet meer, en bleef de hele middag plat terwijl ze probeerde uit te zoeken waarom.

Elke pagina werd bij elk verzoek opnieuw opgebouwd, inclusief de gidspagina's die al weken niet waren veranderd. Elke pagina deed elf databasequeries. Nergens werd iets gecachet, en elke foto werd op volle resolutie geserveerd - meerdere megabytes per vermeldingspagina.

Eén werkdag: publieke gids- en vermeldingspagina's vijftien minuten gecachet op het CDN met hervalidatie op de achtergrond, zodat de applicatie ze één keer per interval serveert in plaats van één keer per bezoeker; statische bestanden een levensduur van een jaar gegeven op bestandsnamen met vingerafdruk; het geauthenticeerde bedrijfsdashboard expliciet gemarkeerd als private en no-store, wat het niet was geweest - het was cachebaar, en als er randverkeer naartoe was gegaan, had het de statistieken van het ene bedrijf aan het andere gelekt; afbeeldingen omgezet naar weergaveformaat in moderne formaten en gecachet aan de rand, wat het gewicht van een vermeldingspagina terugbracht van 4,2 MB naar 310 KB; de samenvatting van seizoensbeschikbaarheid, een aggregatie over elke vermelding, verplaatst naar een kortlevende cache met verversing op de achtergrond; en expliciet legen wanneer een bedrijf zijn eigen vermelding bewerkt, zodat eigenaren hun wijzigingen direct zien.

**Resultaat:** het aantal verzoeken dat de applicatie bereikte, daalde met 94 procent bij hetzelfde verkeer. Een herhaling van de campagnepiek - die in april plaatsvond toen een tweede programma hetzelfde onderwerp behandelde - werd volledig vanaf de rand geserveerd, zonder verandering in responstijd. Noors hostingrekening daalde als bijeffect met €70 per maand.

> *"Ik dacht dat ik een grotere server nodig had. Wat ik nodig had, was ophouden met negenduizend keer dezelfde pagina opbouwen, en ophouden met een foto van vier megabyte naar elke telefoon sturen."*
> - **Noor Vreugdenhil, Oprichter, Tuincentrumgids (Boskoop)**

**Kosten & Doorlooptijd:** €1.800 (CDN-caching met hervalidatie, levensduur van bestanden, headers voor geauthenticeerde antwoorden, beeldtransformatie en caching aan de rand, aggregatiecache, legen bij bewerken, controle onder belasting) - afgerond in 1 werkdag.

## Veelgestelde vragen

### Wat is het risico van het cachen van een ingelogde pagina?

Dat een gedeelde cache de pagina van de ene gebruiker aan een andere serveert. Markeer geauthenticeerde antwoorden expliciet als private en no-store, en geef aan wat varieert op cookie of header.

### Hoe lang moeten publieke pagina's worden gecachet?

Meestal langer dan het instinct zegt - minuten tot uren voor content die af en toe verandert, met hervalidatie op de achtergrond zodat niemand op een verversing wacht.

### Moet ik cache-invalidatie bouwen?

Vaak niet. Een korte levensduur betekent dat het ergste geval kortstondige veroudering is. Voeg alleen expliciet legen toe waar degene die een wijziging maakt die direct moet zien.

### Wat levert het snelst de grootste verbetering op?

Afbeeldingen op weergaveformaat in moderne formaten met lange caching aan de rand, daarna CDN-caching van publieke pagina's. Samen verlagen ze meestal zowel het paginagewicht als het verkeer naar de origin drastisch.

### Hoe weet ik of caching werkt?

Controleer de cache-hitheader op antwoorden, bevestig dat geauthenticeerde endpoints niet worden gecachet, en kijk of het aantal verzoeken dat uw applicatie bereikt daalt terwijl het verkeer gelijk blijft.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het risico van het cachen van een ingelogde pagina?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een gedeelde cache kan de pagina van de ene gebruiker aan een andere serveren. Markeer geauthenticeerde antwoorden als private en no-store, en geef variatie op cookie of header aan."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moeten publieke pagina's worden gecachet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Minuten tot uren voor content die af en toe verandert, met hervalidatie op de achtergrond zodat bezoekers nooit op een verversing wachten."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik expliciete cache-invalidatie nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vaak niet. Een korte levensduur begrenst de veroudering. Voeg alleen legen toe waar degene die een wijziging maakte die direct moet zien."
      }
    },
    {
      "@type": "Question",
      "name": "Welke cachingwijziging helpt het meest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Afbeeldingen op weergaveformaat in moderne formaten met lange caching aan de rand, daarna CDN-caching van publieke pagina's."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of caching werkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Controleer cache-hitheaders, bevestig dat geauthenticeerde endpoints zijn uitgesloten, en kijk of verzoeken naar de origin dalen terwijl het verkeer gelijk blijft."
      }
    }
  ]
}
</script>
