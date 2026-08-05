---
Titel: "Cookie-toestemmingsbanners op met AI gebouwde websites: In theorie nalevend, in de praktijk gebroken"
Trefwoorden: ai websites, gdpr, cookie consent banner, tracking scripts, ePrivacy compliance
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter
---

# Cookie-toestemmingsbanners op met AI gebouwde websites: In theorie nalevend, in de praktijk gebroken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cookie-toestemmingsbanners op met AI gebouwde websites: In theorie nalevend, in de praktijk gebroken",
  "description": "AI-websitebouwers genereren cookiebanners die er nalevend uitzien maar tracking-scripts niet blokkeren.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/cookie-consent-implementation-ai-website"
  }
}
</script>

Open uw eigen website in een incognitovenster, open het netwerk-tabblad van uw browser, en ververs de pagina voordat u op iets op de cookiebanner klikt. Als u Google Analytics of een advertentie-pixel ziet afvuren voordat u een keuze heeft gemaakt, heeft u uw antwoord al. En het is een veel voorkomendere bevinding dan de meeste oprichters verwachten van een site die gebouwd is met een AI-websitetool.

## Waarom de banner bestaat maar zijn werk niet daadwerkelijk doet

Vraag v0, Lovable of een vergelijkbare AI-websitebouwer om "een cookie-toestemmingsbanner toe te voegen", en u krijgt exact waar u om vroeg: een banner. Het heeft een "Accepteren"-knop en een "Weigeren"-knop, het ziet eruit als elke andere cookiebanner op het internet, en het verdwijnt zodra er op geklikt wordt. Wat het erg vaak niet doet is überhaupt iets veranderen aan de tracking-scripts die al op de pagina draaien. Het verbinden van de visuele status van de banner met het daadwerkelijke laadgedrag van de scripts is namelijk een tweede, afzonderlijk stuk engineering dat niemand expliciet heeft aangevraagd.

Onder de ePrivacy-richtlijn van de EU en de AVG is de wettelijke vereiste niet "toon een banner" – het is "laad geen niet-essentiële cookies of tracking-scripts totdat de bezoeker expliciete toestemming heeft gegeven." Dat betekent dat een analytics-tag, een advertentie-pixel, of een marketing-script dat rechtstreeks in de `<head>` van een pagina is ingebouwd moet worden tegengehouden totdat de toestemming daadwerkelijk is verleend. Dit gebeurt doorgaans via een toestemmingsbeheerbenadering die de script-tags zelf afschermt in plaats van simpelweg een banner te tonen bovenop scripts die al draaien. Een met AI gegenereerde site krijgt dit frequent verkeerd om: de tracking-scripts laden onvoorwaardelijk bij het laden van de pagina, en de banner is een puur cosmetische laag die bovenop gedrag zit dat nooit daadwerkelijk is afgeschermd.

## De "weigeren"-knop die niets weigert

Een nog veel voorkomendere mislukking zit één laag dieper: zelfs sites waar scripts wachten op de "accepteren"-klik handelen "weigeren" vaak überhaupt niet correct af. Het klikken op weigeren werkt de visuele status van de banner bij – deze verdwijnt, slaat misschien een cookie op die de keuze registreert – maar de daadwerkelijke script-tags die al in de pagina waren geïnjecteerd blijven exact hetzelfde draaien als voorheen. De bezoeker gelooft dat hij zich heeft afgemeld. De tracking gaat ongeacht door. Dit is precies het soort kloof dat naar boven komt in een klacht bij een toezichthouder of een routineuze nalevingsaudit. Het is namelijk onzichtbaar vanaf een normale gebruikersgerichte test van de banner en verschijnt pas wanneer iemand netwerkverzoeken daadwerkelijk inspecteert na het klikken op weigeren.

LaunchStudio brengt Manifera's enterprise-grade engineering naar de economie van oprichters. Onderdeel daarvan is het controleren van cookie-toestemmingsimplementaties op netwerkniveau, en niet alleen op visueel niveau. We verifiëren dat een weigerklik daadwerkelijk voorkomt dat scripts laden, en niet alleen dat de banner correct verdwijnt. Ons team, werkend vanuit Manifera's kantoor in Amsterdam aan de Herengracht 420, behandeld dit als een standaard onderdeel van elke nalevingsstap vóór de lancering voor een marketingwebsite, omdat het een van de eenvoudigste dingen is voor een met AI gegenereerde site om zichtbaar verkeerd te krijgen en een van de eenvoudigste dingen voor een toezichthouder om daadwerkelijk te testen.

Als u de netwerkverzoeken van uw eigen site nooit heeft gecontroleerd tegen wat uw cookiebanner beweert te doen, is het de moeite waard om [uw bouwsel te beoordelen tegen ons proces](https://launchstudio.eu/en/#process) voordat een bezoeker – of een toezichthouder – het voor u controleert.

## Tag-managers voegen een laag toe die de eenvoudige herstelling niet dekt

Het afschermen van de script-tags zelf lost het probleem op voor sites die Google Analytics of een advertentie-pixel rechtstreeks laden. Het lost het niet volledig op voor sites die een tag-manager-container gebruiken, wat steeds meer de gangbare situatie is. Een tag-manager is, vanuit het perspectief van de browser, een enkele script-tag. Het naïef afschermen van "het script" blokkeert dus alleen de container zelf om te laden. Zodra die container mag draaien kan deze zijn eigen interne tags (Analytics, advertentieconversie-pixels, remarketing-scripts) onmiddellijk afvuren, onafhankelijk van de vraag of de bezoeker ergens toestemming voor heeft gegeven. De interne trigger-configuratie van de container is namelijk een afzonderlijke laag van de vraag of het container-script in de eerste plaats is geladen.

Het op de juiste manier herstellen hiervan betekent het configureren van de eigen toestemmingsinstellingen van de tag-manager, en niet alleen het beslissen of de container moet worden geladen. Het bekende patroon – vaak consent mode genoemd – is om elke niet-essentiële categorie standaard in te stellen op geweigerd op het moment dat de pagina laadt, en alleen specifieke categorieën om te zetten naar verleend zodra de bezoeker een expliciete keuze maakt:

```
// Standaard: weiger alle niet-essentiële tags totdat de toestemming bekend is
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }
gtag('consent', 'default', {
  analytics_storage: 'denied',
  ad_storage: 'denied',
});

// Pas na een expliciete acceptatieklik worden individuele categorieën omgezet
function onConsentAccepted(categories) {
  gtag('consent', 'update', {
    analytics_storage: categories.analytics ? 'granted' : 'denied',
    ad_storage: categories.marketing ? 'granted' : 'denied',
  });
}
```

Zonder deze stap kan een site een controle op oppervlakkig niveau doorstaan – "de banner verschijnt, de container is afgeschermd" – terwijl elke tag binnen die container bij het laden van de pagina ongeacht afvuurt. Dit is precies het soort kloof dat alleen verschijnt wanneer iemand inspecteert wat de tag-manager daadwerkelijk intern doet, en niet alleen of deze is geladen.

## Echt voorbeeld

### Een AI-native oprichter in actie: De banner die er alleen maar uitzag alsof hij werkte

Vera Willemse, een oprichter in Terneuzen, bouwde de marketingwebsite voor StudioLicht, een ontwerpstudio, met behulp van v0 voor de frontend. De site bevatte een cookie-toestemmingsbanner die voldeed aan elke visuele verwachting – duidelijke taal, een accepteerknop, een weigerknop, een link naar een privacybeleid. Het zag er volgens elke normale standaard van het bekijken van een website volledig nalevend uit.

Het probleem kwam naar boven toen een bezoeker – toevallig iemand die bekend was met privacy-tools – de netwerkactiviteit van de site controleerde en ontdekte dat Google Analytics afvuurde bij elke paginalading, voordat er überhaupt een keuze voor toestemming was gemaakt. Verder testend veranderde het klikken op "weigeren" het uiterlijk van de banner, maar het had nul effect op het daadwerkelijke script: analytics bleef elke bezoeker volgen die zich expliciet afmeldde, exact hetzelfde als bezoekers die zich aanmeldden.

LaunchStudio herstructureerde het laden van de scripts op de site zodanig dat analytics en alle andere niet-essentiële scripts volledig worden tegengehouden totdat expliciete toestemming is verleend. We sloten de weigeractie aan om daadwerkelijk te voorkomen dat die scripts ooit laden in plaats van simpelweg de banner te verbergen. We voegden ook een toestemmingsstatus-controle toe die correct blijft bestaan over paginabezoeken heen, zodat terugkerende bezoekers niet opnieuw worden gevolgd nadat ze eenmaal hebben geweigerd. **Resultaat:** StudioLicht's site komt nu op netwerkniveau exact overeen met wat de banner belooft.

> *"Ik dacht oprecht dat een cookiebanner simpelweg een cookiebanner was – ik had geen idee dat 'weigeren' puur cosmetisch kon zijn. Het is zo'n stille manier om niet-nalevend te zijn zonder het te weten."*
> — **Vera Willemse, Oprichter, StudioLicht (Terneuzen)**

**Kosten en tijdlijn:** € 500 (implementatie van script-afscherming, persistentie van toestemmingsstatus, verificatie op netwerkniveau) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Waarom laat mijn cookiebanner tracking-scripts nog steeds draaien nadat iemand op weigeren heeft geklikt?

Omdat AI-websitebouwers doorgaans het visuele gedrag van de banner genereren zonder het te verbinden met de daadwerkelijke script-tags – de banner en de tracking-scripts zijn gebouwd als twee losgekoppelde onderdelen tenzij iemand ze expliciet aan elkaar koppelt.

### Is een visueel nalevende banner voldoende om te voldoen aan de AVG en de ePrivacy-richtlijn?

Nee. De wettelijke vereiste gaat over daadwerkelijk gedrag rond gegevensverzameling, en niet over het uiterlijk van de banner – scripts moeten worden geblokkeerd tot toestemming, en de gegevens van een geweigerde bezoeker mogen überhaupt niet worden verzameld.

### Hoe zou ik überhaupt weten of mijn site dit probleem heeft?

Open uw site in een besloten browsenvenster, open het netwerk-tabblad van uw browser, en bekijk wat er laadt voordat u interactie heeft met de banner, en opnieuw na het klikken op weigeren – als er op een van beide momenten tracking-verzoeken afvuren is de implementatie onvolledig.

### Geldt dit voor alle AI-websitebouwers, of alleen voor v0?

Het is een bekend patroon bij v0, Lovable, Bolt en vergelijkbare tools, aangezien geen daarvan de status van de toestemmingsbanner standaard verbindt met het laden van scripts.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom laadt Google Analytics al vóór ik op de cookiebanner klik?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat AI-tools de banner als losse UI-component bouwen. De Analytics-scripttag in de `<head>` wordt onvoorwaardelijk ingeladen, ongeacht de banner."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een bezoeker op 'Weigeren' klikt op een AI-site?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij 90% van de AI-gegenereerde sites verdwijnt alleen de banner visueel, maar blijft de tracking-script gewoon doordraaien op de achtergrond."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test je of je cookiebanner echt AVG-compliant is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open Chrome DevTools -> Network tab. Ververs de pagina in incognito. Zie je requests naar google-analytics.com vóór acceptatie? Dan is het illegaal."
      }
    },
    {
      "@type": "Question",
      "name": "Werkt Google Tag Manager (GTM) automatisch met cookie-consent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee! GTM laadt zelf als 1 script, maar de interne tags vuren direct af tenzij je GTM Consent Mode (gtag consent default denied) activeert."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost het script-gaten van een cookiebanner bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het instellen van echte script-gating en netwerk-verificatie kost gemiddeld €500 en duurt 3 werkdagen."
      }
    }
  ]
}
</script>