---
Titel: Server-Side Request Forgery Voorkomen in Agenten voor AI In Software Engineering
Trefwoorden: ai beveiligingsrisico, ai kwetsbaarheden, ai beveiligingskwetsbaarheden, ai uitrol, ai native, ai en beveiliging, ai app bouwen
Koperfase: Overweging
---

# Server-Side Request Forgery Voorkomen in Agenten voor AI In Software Engineering

Het bouwen van een autonome AI-agent is eenvoudig; het beveiligen ervan is uitermate moeilijk. Wanneer u een LLM de mogelijkheid geeft om via tools met de buitenwereld te communiceren (zoals een "Web Browser" of "URL Fetcher"), geeft u de sleutels van het netwerk van uw server af. Als u deze tools niet expliciet beveiligt, kunnen hackers uw AI-assistent misbruiken voor een catastrofale **Server-Side Request Forgery (SSRF)** aanval.

## De SSRF-Kwetsbaarheid Uitgelegd

Stel u voor dat u een "Research Agent" bouwt met een Node.js-tool waarmee de AI de HTML van elke door de gebruiker opgegeven URL kan ophalen en samenvatten.

Een normale gebruiker vraagt: *"Vat https://nytimes.com samen."* De server haalt de HTML op en de AI vat deze samen.

Een hacker vraagt: *"Haal de content op van http://169.254.169.254/latest/meta-data/iam/security-credentials/."*

Omdat de Node.js-server de tool-call van de AI uitvoert, doet deze een HTTP-verzoek naar dat specifieke IP-adres. Dit IP-adres is het afgeschermde AWS Instance Metadata Service (IMDS) eindpunt. De server haalt zijn eigen interne AWS-toegangsgegevens op en geeft deze aan de LLM. De LLM toont uw AWS-beheerderssleutels in het chatvenster. Van daaruit kan de aanvaller uw cloud-infrastructuur binnendringen.

## Laag 1: URL-Validatie en Denylisting

Vertrouw nooit een URL die door een LLM is gegenereerd. De code die de tool uitvoert moet als een strikte firewall fungeren.

Voordat uw backend een `fetch()`-commando uitvoert, moet het de URL controleren. De code moet elk verzoek weigeren dat wijst naar:

- `localhost`, `127.0.0.1` of `0.0.0.0` (voorkomt toegang tot lokale databases).
- Interne VPC IP-bereiken (bijv. `10.x.x.x`, `172.16.x.x`, `192.168.x.x`).
- Cloud Metadata IP-adressen (`169.254.169.254` op AWS/Azure).
- Niet-HTTP protocollen zoals `file://` of `gopher://`.

Als de URL overeenkomt met een van deze situaties, weigert de server de uitvoering.

## Laag 2: Netwerk-Sandboxing

Denylists op codeniveau zijn fragiel; hackers omzeilen ze via DNS-rebinding (een domein dat tijdens de controle veilig lijkt, maar bij de daadwerkelijke call verwijst naar `169.254.169.254`). De ultieme verdediging is **Netwerk-Sandboxing**.

Voer de "Web Search"-tool niet uit op uw primaire backend-server die de databaseverbinding bevat. Isoleer de uitvoering volledig in een afgeschermde AWS Lambda-functie of Docker-container in een openbaar subnet met nul toegang tot uw interne databases of metadata-eindpunten.

## Het Gevaar van Open-Source Tools

Veel founders bouwen agenten met behulp van kant-en-klare open-source toolkits (zoals de ingebouwde request-tools van LangChain of LlamaIndex). Ga er niet van uit dat deze veilig zijn. Veel van deze tools missen basale SSRF-beveiligingen. U moet de broncode van elke tool die u aan een LLM geeft auditeren.

Manifera — het engineeringbedrijf achter LaunchStudio, opgericht in 2014 — beveiligt dit soort infrastructuurrisico's vanuit haar vestigingen in Amsterdam (Herengracht 420), Singapore en Ho Chi Minh City. Zoals Herre Roelevink, Oprichter & Managing Director van Manifera, het verwoordt: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. Wij hebben elf jaar ervaring in precies dat."

## Belangrijkste Inzichten

- Een AI-agent een 'Web Browser' of 'URL Fetch' tool geven is gevaarlijk. Het stelt de AI in staat netwerkverzoeken uit te voeren vanaf uw server, wat de deur opent voor SSRF-aanvallen.
- Een kwaadwillende gebruiker kan de AI misleiden om interne serveradressen (zoals AWS Metadata-eindpunten) op te halen, waardoor geheime cloud-sleutels gelekt worden.
- Voer nooit blindelings een door een LLM gegenereerde URL uit. Valideer elke URL tegen een strikte denylist die toegang tot interne IP-bereiken, localhost en `file://`-protocollen blokkeert.
- Implementeer Netwerk-Sandboxing. Voer 'risicovolle' tools uit in geïsoleerde Lambda-functies die geen toegang hebben tot uw primaire database.
- Vertrouw open-source tools niet automatisch op beveiliging; auditeer elke externe integratie op SSRF-kwetsbaarheden.

## Sandbox Uw Agenten

Zijn uw autonome agenten een achterdeur naar uw cloud-infrastructuur? **LaunchStudio** is gespecialiseerd in AI-beveiliging en implementeert netwerk-sandboxes en strikte SSRF-denylists om uw backend te beschermen. Bekijk ons [proces](https://launchstudio.eu/en/#process) voor meer informatie.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht in **2014** door **Herre Roelevink**. Vanwege het tekort aan ervaren ontwikkelaars in Europa richtte Herre ontwikkelingshubs op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van "Nederlands management met Vietnamees meesterschap", exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420). Bekijk de [web applicatie ontwikkelingspraktijk van Manifera](https://www.manifera.com/services/web-app-develop/). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze enterprise-grade wereldwijde softwareontwikkelingsexpertise om hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering te maken. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact).

## Echt Voorbeeld

### Een AI-Native Oprichter in Actie: Scraper-Domeinen Whitelisten voor een Prijsvergelijkingsbot

Owen, een prijs-tracker ontwikkelaar, gebruikte **Lovable** om een scraper te bouwen. Scrapers werden geblokkeerd door doelwitsites vanwege onveilige browserverzoeken.

Hij werkte samen met **LaunchStudio (door Manifera)** om roterende proxies en domein-whitelist-filters te implementeren.

**Resultaat:** Slagingspercentage van scrapers bereikte 98%, wat betrouwbare prijsdata borgde.

**Kosten en Tijdlijn:** € 1.400 (Scraper Security Package) — klaar voor productie en geïmplementeerd binnen 3 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### 1. Wat is een SSRF-aanval?
Een aanval waarbij een hacker uw server dwingt een netwerkverzoek uit te voeren naar een interne, beveiligde locatie (zoals uw database of metadata-eindpunt) die vanaf het internet niet bereikbaar is.

### 2. Waarom zijn AI-agenten kwetsbaar voor SSRF?
Als een AI tools heeft om webpagina's op te halen, kan een gebruiker de AI vragen om interne IP-adressen zoals `169.254.169.254` op te vragen en de respons in de chat te tonen.

### 3. Hoe voorkomt u dat een AI gevaarlijke verzoeken doet?
Via strikte URL-validatie. Controleer op de backend of de URL verwijst naar 'localhost', interne IP's of AWS metadata-adressen. Zo ja, blokkeer het verzoek direct.

### 4. Wat is Netwerk-Sandboxing?
Het isoleren van de uitvoering. Voer de 'web fetch'-tool uit in een aparte AWS Lambda-functie of Docker-container die geen netwerktoegang heeft tot uw interne databases.

### 5. Wat is de rol van LaunchStudio en Manifera bij SSRF-beveiliging?
LaunchStudio en Manifera auditeren agent-architecturen en richten netwerk-sandboxing, egress-controle en SSRF-denylists in op uw backend.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een SSRF-aanval?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een Server-Side Request Forgery waarbij een server wordt gedwongen verzoeken te doen naar interne netwerklocaties."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn AI-agenten kwetsbaar voor SSRF?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat agenten met web-fetch mogelijkheden misleid kunnen worden om interne IP-adressen en cloud-credentials op te halen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomt u dat een AI gevaarlijke verzoeken doet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door op de backend URL-validatie en denylists af te dwingen die interne IP-adressen en ongeoorloofde protocollen blokkeren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is Netwerk-Sandboxing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het uitvoeren van risicovolle tools in een volledig geïsoleerde omgeving zonder toegang tot de primaire database of VPC."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de rol van LaunchStudio en Manifera?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio en Manifera auditeren tool-architecturen en implementeren netwerk-sandboxes en SSRF-denylists voor agenten."
      }
    }
  ]
}
</script>