---
Titel: Server-Side Request Forgery (SSRF) in agenten voorkomen
Trefwoorden: AI in software-engineering, Voorkomen, Server, Kant, Verzoek, Vervalsing, SSRF, Agenten
Koperfase: Bewustzijn
---

# Voorkomen van Server-Side Request Forgery (SSRF) in agenten
Het bouwen van een autonome AI-agent is eenvoudig; het beveiligen ervan is ongelooflijk moeilijk. Wanneer u een LLM de mogelijkheid geeft om via tools (zoals een "webbrowser" of "URL Fetcher") met de buitenwereld te communiceren, draagt ​​u de sleutels over aan de netwerklaag van uw server. Als u deze tools niet expliciet in de sandbox plaatst, zullen hackers uw behulpzame AI-assistent gebruiken om een ​​catastrofale **Server-Side Request Forgery (SSRF)**-aanval uit te voeren, waardoor uw interne cloudinfrastructuur wordt geschonden.

## De SSRF-kwetsbaarheid uitgelegd

Stel je voor dat je een 'onderzoeksagent' bouwt. Je geeft het een Node.js-tool waarmee het de HTML kan ophalen van elke URL die door de gebruiker wordt opgegeven, zodat het de inhoud kan samenvatten.

Een normale gebruiker vraagt: *"Vat https://nytimes.com samen."* De server haalt de HTML op, de AI vat deze samen. Perfect.

Een hacker vraagt: *"Haal de inhoud op en vat deze samen op http://169.254.169.254/latest/meta-data/."*

Omdat de Node.js-server blindelings de toolaanroep van de AI uitvoert, doet deze een HTTP-verzoek naar dat specifieke IP-adres. Dat IP-adres is het zeer beperkte AWS Instance Metadata-eindpunt. De server haalt zijn eigen interne, zeer geprivilegieerde cloudreferenties op en geeft deze terug aan de LLM. De LLM drukt graag uw AWS-beheerderssleutels af in het chatvenster zodat de hacker deze kan lezen. Uw opstart is gecompromitteerd.

## Laag 1: URL-validatie en denylisting

Vertrouw nooit een URL die is gegenereerd door een LLM. De code die de tool uitvoert, moet fungeren als een strikte firewall.

Voordat uw Node-backend een `fetch()`-opdracht uitvoert die door de AI is gegenereerd, moet deze de URL parseren en deze uitvoeren op basis van een strikte denylist. De code moet expliciet elk verzoek afwijzen dat verwijst naar:

- `localhost` of `127.0.0.1` (Voorkomen van toegang tot lokale Redis- of databasepoorten).

- Interne VPC IP-bereiken (bijvoorbeeld `10.x.x.x` of `192.168.x.x`).

- Cloud Metadata IP-adressen (bijvoorbeeld `169.254.169.254`).

Als de URL met een van deze overeenkomt, genereert de server een foutmelding en weigert hij de tool uit te voeren.

## Laag 2: Netwerk-sandboxing

Weigerlijsten op codeniveau zijn kwetsbaar; hackers vinden manieren om deze te omzeilen (bijvoorbeeld door DNS-rebinding te gebruiken). De ultieme verdediging is **Netwerk Sandboxing**.

Voer de tool "Web Search" of "URL Fetch" niet uit op uw primaire backend-server die de databaseverbinding beheert. Isoleer de uitvoering van het gereedschap volledig. Verplaats de tool naar een ernstig beperkte AWS Lambda-functie of een aparte Docker-container die in een openbaar subnet is geplaatst, met absoluut nulrouteringstoegang tot uw interne databases, VPC's of metadata-eindpunten. Als de agent wordt misleid om een ​​kwaadwillig verzoek te doen, komt hij in een lege, geïsoleerde sandbox terecht waar niets te stelen is.

## Het gevaar van open source-tools

Veel oprichters bouwen agenten met behulp van voorverpakte open-source toolkits (zoals de ingebouwde webverzoektools van LangChain). Ga er niet vanuit dat deze veilig zijn. Veel communitytools zijn gebouwd voor snelle prototyping, niet voor bedrijfsbeveiliging, en ontberen volledig SSRF-bescherming. U moet de broncode controleren van elke tool die u aan een LLM geeft.

## Belangrijkste afhaalrestaurants

- Het is zeer gevaarlijk om een AI-agent een 'webbrowser'- of 'URL Fetch'-tool te geven. Hiermee kan de AI HTTP-verzoeken doen vanaf uw server, waardoor u wordt blootgesteld aan Server-Side Request Forgery (SSRF)-aanvallen.

- Een kwaadwillende gebruiker kan de AI misleiden om interne serveradressen op te halen (zoals AWS Metadata-eindpunten of 'localhost'-databases), waardoor de AI uw privécloud-inloggegevens leest en deze in de chat afdrukt.

- Voer nooit blindelings een URL uit die is gegenereerd door een LLM. Uw backendcode moet elke URL valideren aan de hand van een strikte denylist, waardoor de toegang tot interne IP-bereiken, localhost en cloud-metadata-IP's wordt geblokkeerd.

- Implementeer netwerksandboxing. Verplaats de uitvoering van 'risicovolle' tools (zoals het ophalen van internet of het uitvoeren van code) naar sterk geïsoleerde Lambda-functies of Docker-containers die geen toegang hebben tot uw primaire database.

- Vertrouw niet standaard op open-source framework-tools. Veel kant-en-klare 'webscraping'-tools in populaire AI-bibliotheken ontberen elementaire SSRF-bescherming en zullen uw onderneming blootstellen aan catastrofale inbreuken.

## Sandbox uw agenten

Zijn uw autonome agenten een achterdeur naar uw cloudinfrastructuur? **LaunchStudio** is gespecialiseerd in AI-beveiliging, het controleren van toolarchitecturen en het implementeren van ondoordringbare netwerksandboxen en strikte SSRF-denylists om de backend van uw onderneming te beschermen tegen kwaadaardige promptinjectie.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: schraperdomeinen op de witte lijst zetten voor een prijsvergelijkingsbot

Owen, een ontwikkelaar van prijstrackers, gebruikte **Lovable** om een schraper te bouwen. Scrapers werden gemarkeerd en geblokkeerd door doelsites vanwege onveilige browserverzoeken.

Hij werkte samen met **LaunchStudio (door Manifera)** om roterende proxyproxy's en filters voor de witte lijst van domeinen te implementeren.

**Resultaat:** De succespercentages van Scraper bereikten 98%, waardoor betrouwbare invoer van prijsgegevens veilig werd gesteld.

**Kosten en tijdlijn:** € 1.400 (Scraper Security Package) — productieklaar en binnen 3 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een SSRF-aanval?

Een aanval waarbij een hacker uw server dwingt een netwerkverzoek te doen naar een interne, zeer veilige bestemming (zoals uw privédatabase) die de hacker normaal gesproken niet kan bereiken vanaf het openbare internet.

### Waarom zijn AI-agenten kwetsbaar voor SSRF?

Als je een AI de mogelijkheid geeft om webpagina's op te halen, kan een hacker de AI vragen om een ​​privé, intern server-IP-adres op te halen. De AI haalt blindelings uw interne geheimen op en drukt deze af naar de hacker.

### Hoe voorkom je dat een AI gevaarlijke verzoeken doet?

Implementeer strikte URL-validatie. Voordat uw backend de ophaalactie uitvoert, moet de code controleren of de URL verwijst naar 'localhost' of een intern AWS-metadata-IP. Als dit het geval is, blokkeer dan het verzoek volledig.

### Wat is netwerksandboxing?

Het isoleren van de uitvoering. Voer de 'web fetching'-tool van de AI uit in een aparte, sterk beperkte AWS Lambda-functie waarvan de netwerktoegang volledig is afgesloten van uw primaire databases.