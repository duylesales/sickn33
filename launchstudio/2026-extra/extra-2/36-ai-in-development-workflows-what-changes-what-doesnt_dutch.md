---
Titel: "AI in ontwikkelingswerkstromen: Wat verandert er, wat niet"
Trefwoorden: ai in development, ai for development, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# AI in ontwikkelingswerkstromen: Wat verandert er, wat niet

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI in ontwikkelingswerkstromen: Wat verandert er, wat niet",
  "description": "Een technische verdieping in het risico van Server-Side Request Forgery (SSRF) geïntroduceerd door een handige functie voor het importeren vanaf een URL.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/ai-in-development-workflows-what-changes-what-doesnt"
  }
}
</script>

AI in ontwikkelingswerkstromen verandert hoe snel een functie gebouwd wordt. Het verandert niet waar die functie fundamenteel toe in staat is zodra deze live is – en een handige functie voor het "importeren van een productafbeelding vanaf een URL", snel en correct gebouwd om aan exact die beschrijving te voldoen, is fundamenteel tot aanzienlijk meer in staat dan het tonen van een afbeelding. Tenzij iets het specifiek stopt.

## Wat een functie "Importeren vanaf URL" daadwerkelijk onder de motorkap doet

Een functie waarmee een gebruiker een URL kan plakken en uw server ophaalt wat er op dat adres staat – een afbeelding, een document, een bron – betekent noodzakelijkerwijs dat uw eigen server degene is die dat uitgaande verzoek doet, en niet de browser van de gebruiker. Dit is een oprecht handig patroon, en AI-coderingsassistenten implementeren het gemakkelijk wanneer een oprichter dit soort functionaliteit beschrijft.

## Waarom "uw server haalt het op" het specifieke risico is

Als de URL die een gebruiker verstrekt op geen enkele wijze beperkt is, is er niets wat een verzoek stopt om zich te richten op interne netwerkadressen die uw server kan bereiken maar het openbare internet niet. Denk aan interne beheerderspanelen, cloud-metadatadiensten, of andere backend-systemen die nooit bedoeld waren om van buitenaf bereikbaar te zijn.

## Waarom dit Server-Side Request Forgery wordt genoemd

De naam beschrijft exact wat er gebeurt: een verzoek wordt vervalst (opgesteld door een externe partij) maar server-side uitgevoerd (door uw eigen vertrouwde infrastructuur). Dit geeft een aanvaller een manier om te peilen of te communiceren met interne systemen met behulp van de eigen netwerkpositie en het vertrouwensniveau van uw server.

## Waarom het testen met echte afbeeldings-URL's dit nooit onthult

Het testen van een functie voor het importeren vanaf een URL door het plakken van echte, externe afbeeldingslinks bevestigt dat de functie openbare afbeeldingen correct ophaalt. Het biedt nul informatie over wat er gebeurt als iemand in plaats daarvan een intern netwerkadres verstrekt.

## Wat het op de juiste manier beperken van deze functie vereist

Een veilige implementatie valideert dat een verstrekte URL resolvet naar een oprecht openbaar, extern adres voordat het wordt opgehaald. Het blokkeert expliciet verzoeken naar interne of gereserveerde netwerkbereiken. [LaunchStudio](https://launchstudio.eu/nl/) implementeert exact dit soort URL-validatie als onderdeel van haar beoordeling van backend-beveiliging, ondersteund door Manifera's 11+ jaar ervaring met het beveiligen van integraties aan de serverzijde.

Manifera's beveiligingswerk voor SSRF en backend-integraties wordt geleverd via het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Verder Dan het Blokkeren van Interne IP's: Een Completere SSRF-Verdediging

Het beperken van een "ophalen via URL"-functie tot uitsluitend openbare bestemmingen klinkt in theorie eenvoudig. Een oppervlakkige implementatie — die enkel controleert of het ingevoerde adres eruitziet als een lokaal IP-adres — ziet echter verschillende manieren over het hoofd waarop die restrictie in de praktijk gemakkelijk wordt omzeild:

- **DNS Rebinding** — een domeinnaam die op het moment van de initiële validatiecheck netjes verwijst naar een legitiem openbaar IP-adres, maar die direct daarna wordt omgezet naar een intern IP-adres op het moment dat het werkelijke netwerkverzoek plaatsvindt. Hierdoor glipt het verzoek voorbij een validatie die slechts eenmaal aan het begin werd uitgevoerd.
- **Omleidingsketens (Redirect Chains)** — een URL die zelf naar een legitiem openbaar adres verwijst, maar waarvan de webserver antwoordt met een HTTP 302-omleiding naar een intern netwerkadres. Dit omzeilt elke controle die alleen de oorspronkelijk ingevoerde URL inspecteert en redirects blind volgt.
- **Het specifieke cloud-metadata-eindpunt** — het bekende, vaste interne IP-adres (zoals `169.254.169.254`) dat veel cloudproviders gebruiken om tijdelijke inloggegevens en serverconfiguraties aan actieve instances te serveren. Het expliciet blokkeren van dit adres op naam is essentieel bovenop algemene IP-reeksregels, juist omdat het zo'n extreem waardevol doelwit is voor aanvallers.
- **Alternatieve adresnotaties** — hetzelfde interne IP-adres geschreven in decimale, octale of hexadecimale notatie in plaats van het standaard formaat met punten kan eenvoudig voorbij een eenvoudig validatiescript glippen dat slechts op één specifieke tekenreeks zoekt.
- **Niet-HTTP protocollen** — een functie die bedoeld is om afbeeldingen op te halen via HTTP of HTTPS, maar die niet expliciet afdwingt welk schema is toegestaan, kan soms worden gericht op lokale bestandspaden (`file://`) of andere interne protocollen.

Een werkelijk robuuste verdediging valideert de bestemming op het exacte moment van het uiteindelijke netwerkverzoek, blokkeert cloud-metadata-adressen expliciet op naam en dwingt uitsluitend veilige HTTP/HTTPS-protocollen af. Dit is precies het soort gelaagde bescherming dat een algemene prompt aan een AI-codeerassistent zelden oplevert, omdat elk van deze vijf omzeilingstechnieken een specifieke, specialistische kwetsbaarheid betreft.

## Echt voorbeeld

### Een AI-native oprichter in actie: De afbeeldingsimport die te ver reikte

Wessel, een voormalig logistiek coördinator die oprichter werd in Vlaardingen, bouwde VoorraadVast, een AI-ondersteunde tool voor magazijnvoorraadbeheer gebouwd met Cursor, inclusief een handige functie waarmee magazijnmedewerkers een productfoto rechtstreeks vanaf een opgegeven URL kunnen importeren in plaats van handmatig een bestand te uploaden.

Een IT-contactpersoon van een partner die VoorraadVast beoordeelde voorafgaand aan een mogelijke integratie, testte de importfunctie met een intern netwerkadres in plaats van een openbare afbeeldings-URL. Hij vond dat de server probeerde op te halen en terug te sturen wat het daar vond – wat bevestigde dat de functie geen beperking had op wat voor soort adres het zou benaderen. LaunchStudio's beoordeling bevestigde dat de onderliggende ophaallogica elke URL accepteerde en opvroeg zonder te valideren dat het een oprecht openbare bestemming was.

**Resultaat:** LaunchStudio voegde strikte validatie toe die garandeert dat de importfunctie alleen ophaalt van geverifieerde openbare, externe adressen. Dit blokkeert expliciet elk verzoek gericht op interne of gereserveerde netwerkbereiken, wat de blootstelling sloot zonder te veranderen hoe medewerkers de importfunctie gebruikten.

> *"Ik bouwde die functie om medewerkers een paar kliks te besparen bij het importeren van productfoto's. Het was geen moment in me opgekomen dat hetzelfde gemak theoretisch gericht kon worden op iets wat compleet anders was dan een foto."*
> — **Wessel Kramer, Oprichter, VoorraadVast (Vlaardingen)**

**Kosten en tijdlijn:** € 2.600 (SSRF-herstel en URL-ophaalvalidatie) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Wat maakt Server-Side Request Forgery (SSRF) zo'n gevaarlijke kwetsbaarheid voor cloud-gehoste applicaties?

Omdat de kwetsbaarheid de cloudserver zelf dwingt om netwerkverzoeken uit te voeren. Hierdoor kan een aanvaller toegang krijgen tot interne netwerkbronnen, databases en met name de interne cloud-metadata-service (zoals AWS of Google Cloud metadata), die tijdelijke beveiligingstokens en geheimen kan bevatten.

### Waarom volstaat het controleren op 'localhost' of '127.0.0.1' niet als volledige SSRF-bescherming?

Omdat aanvallers interne adressen kunnen maskeren met behulp van alternatieve notaties (zoals decimale IP's), DNS-rebinding (waarbij een domein tijdens de controle naar een openbaar IP wijst maar tijdens de aanroep naar een intern IP), of HTTP-omleidingen (redirects) die de initiële validatie omzeilen.

### Heeft Manifera ervaring met het beveiligen van microservices en API-gateways tegen SSRF?

Ja, bij complexe cloudarchitecturen ontwerpt Manifera strikte egress-regels, dedicated proxy-services en fijnmazige netwerksegmentatie om te waarborgen dat applicatieservers uitsluitend gevalideerde externe verzoeken kunnen initiëren en nooit interne services kunnen bevragen.

### Zou een AI-tool zoals Cursor of Lovable automatisch weten hoe SSRF effectief moet worden afgedekt?

Nee, tenzij de prompt expliciet vraagt om een robuuste SSRF-beveiliging inclusief DNS-resolutievalidatie, redirect-beperkingen en metadata-blokkades. Zonder die specifieke instructies genereert de tool doorgaans een eenvoudige `fetch()`-aanroep die direct vatbaar is voor SSRF.

### Is het uitschakelen van URL-ophaling de enige manier om SSRF 100% te voorkomen?

Nee, als de functie essentieel is (bijvoorbeeld voor het ophalen van previews of avatars), kan deze veilig worden geïmplementeerd door verzoeken via een geïsoleerde proxy te routeren, DNS-resolutie vóór het verzoek te verifiëren en alle niet-openbare IP-ranges strikt te blokkeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat maakt Server-Side Request Forgery (SSRF) zo'n gevaarlijke kwetsbaarheid voor cloud-gehoste applicaties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat de kwetsbaarheid de cloudserver zelf dwingt om netwerkverzoeken uit te voeren. Hierdoor kan een aanvaller toegang krijgen tot interne netwerkbronnen, databases en met name de interne cloud-metadata-service (zoals AWS of Google Cloud metadata), die tijdelijke beveiligingstokens en geheimen kan bevatten."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom volstaat het controleren op 'localhost' of '127.0.0.1' niet als volledige SSRF-bescherming?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat aanvallers interne adressen kunnen maskeren met behulp van alternatieve notaties (zoals decimale IP's), DNS-rebinding (waarbij een domein tijdens de controle naar een openbaar IP wijst maar tijdens de aanroep naar een intern IP), of HTTP-omleidingen (redirects) die de initiële validatie omzeilen."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft Manifera ervaring met het beveiligen van microservices en API-gateways tegen SSRF?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, bij complexe cloudarchitecturen ontwerpt Manifera strikte egress-regels, dedicated proxy-services en fijnmazige netwerksegmentatie om te waarborgen dat applicatieservers uitsluitend gevalideerde externe verzoeken kunnen initiëren en nooit interne services kunnen bevragen."
      }
    },
    {
      "@type": "Question",
      "name": "Zou een AI-tool zoals Cursor of Lovable automatisch weten hoe SSRF effectief moet worden afgedekt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, tenzij de prompt expliciet vraagt om een robuuste SSRF-beveiliging inclusief DNS-resolutievalidatie, redirect-beperkingen en metadata-blokkades. Zonder die specifieke instructies genereert de tool doorgaans een eenvoudige `fetch()`-aanroep die direct vatbaar is voor SSRF."
      }
    },
    {
      "@type": "Question",
      "name": "Is het uitschakelen van URL-ophaling de enige manier om SSRF 100% te voorkomen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, als de functie essentieel is (bijvoorbeeld voor het ophalen van previews of avatars), kan deze veilig worden geïmplementeerd door verzoeken via een geïsoleerde proxy te routeren, DNS-resolutie vóór het verzoek te verifiëren en alle niet-openbare IP-ranges strikt te blokkeren."
      }
    }
  ]
}
</script>
