---
Titel: "Cookie-toestemmingsbanners op door AI gebouwde websites: conform in theorie, gebroken in de praktijk"
Trefwoorden: ai websites, gdpr, cookie consent banner, tracking scripts, ePrivacy compliance
Koperfase: Bewustzijn
Doelgroep: AI-Native-oprichter
---
# Cookie-toestemmingsbanners op door AI gebouwde websites: conform in theorie, gebroken in de praktijk

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cookie-toestemmingsbanners op door AI gebouwde websites: conform in theorie, gebroken in de praktijk",
  "description": "AI-websitebouwers genereren cookiebanners die er conform uitzien, maar trackingscripts vaak niet daadwerkelijk blokkeren v\u00f3\u00f3r toestemming of nadat een bezoeker op Afwijzen heeft geklikt. Hier ziet u hoe u kunt controleren of de uwe een van hen is.",
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

Open uw eigen website in een incognitovenster, open het netwerktabblad van de browser en ververs de pagina voordat u op iets op de cookiebanner klikt. Als u Google Analytics of een advertentiepixel ziet geactiveerd voordat u een keuze heeft gemaakt, heeft u uw antwoord al. Dit komt vaker voor dan de meeste oprichters verwachten van een site die is gebouwd met een AI-websitetool.

## Waarom de banner bestaat, maar zijn werk niet echt doet

Vraag v0, Lovable of een soortgelijke AI-websitebouwer om "een cookietoestemmingsbanner toe te voegen", en u krijgt precies waar u om vroeg: een banner. Het heeft een knop "Accepteren" en een knop "Weigeren". Het lijkt op elke andere cookiebanner op internet en verdwijnt zodra erop wordt geklikt. Wat het vaak helemaal niet doet, is helemaal niets met de trackingscripts die al op de pagina draaien - omdat het verbinden van de visuele status van de banner met het daadwerkelijke laadgedrag van scripts een tweede, afzonderlijk stukje techniek is waar niemand expliciet om heeft gevraagd.

Volgens de ePrivacy-richtlijn en de AVG van de EU is de wettelijke vereiste niet 'een banner tonen', maar 'geen niet-essentiële cookies of trackingscripts laden totdat de bezoeker bevestigende toestemming heeft gegeven'. Dat betekent dat een analysetag, een advertentiepixel of een marketingscript dat rechtstreeks in de '<head>' van een pagina is ingebed, moet worden tegengehouden totdat er daadwerkelijk toestemming wordt verleend, meestal via een benadering van toestemmingsbeheer die de scripttags zelf afsluit in plaats van alleen maar een banner weer te geven over de scripts die al actief zijn. Een door AI gegenereerde site krijgt dit vaak in omgekeerde richting: de trackingscripts worden onvoorwaardelijk geladen wanneer de pagina wordt geladen, en de banner is een puur cosmetische laag bovenop gedrag dat nooit daadwerkelijk is afgeschermd.

## De knop "afwijzen" die niets afwijst

Een nog vaker voorkomende fout ligt nog een laag dieper: zelfs sites waar scripts wachten op de klik op 'accepteren', verwerken 'afwijzen' vaak helemaal niet correct. Als u op 'weigeren' klikt, wordt de visuele status van de banner bijgewerkt (deze verdwijnt, misschien wordt er een cookie opgeslagen die de keuze registreert), maar de daadwerkelijke scripttags die al in de pagina zijn geïnjecteerd, blijven precies zoals voorheen actief. De bezoeker denkt dat hij/zij zich heeft afgemeld. Het volgen gaat hoe dan ook door. Dit is precies het soort hiaat dat naar voren komt bij een klacht van een toezichthouder of een routinematige compliance-audit, omdat het onzichtbaar is bij een normale gebruikersgerichte test van de banner en alleen zichtbaar wordt wanneer iemand netwerkverzoeken daadwerkelijk inspecteert nadat hij op 'weigeren' heeft geklikt.

LaunchStudio brengt de hoogwaardige techniek van Manifera naar de grondleggerseconomie, en een onderdeel daarvan is het controleren van de implementatie van cookie-toestemming op netwerkniveau, niet alleen op visueel niveau - het verifiëren dat een afwijzingsklik daadwerkelijk verhindert dat scripts worden geladen, en niet alleen dat de banner correct verdwijnt. Ons team, werkzaam vanuit het Amsterdamse kantoor van Manifera aan de Herengracht 420, beschouwt dit als een standaarditem in elke pre-lanceringspas voor een marketingwebsite, omdat het een van de gemakkelijkste dingen is voor een door AI gegenereerde site om zichtbaar fout te gaan en een van de gemakkelijkste dingen voor een toezichthouder om daadwerkelijk te testen.

Als u de netwerkverzoeken van uw eigen site nog nooit heeft gecontroleerd aan de hand van wat uw cookiebanner beweert te doen, is het de moeite waard [uw build te beoordelen aan de hand van ons proces](https://launchstudio.eu/en/#process) voordat een bezoeker (of een toezichthouder) dit voor u controleert.

## Echt voorbeeld

### Een AI-Native-oprichter in actie: de banner die er alleen maar uitzag alsof hij werkte

Vera Willemse, oprichtster uit Terneuzen, bouwde de marketingwebsite voor ontwerpstudio StudioLicht, met v0 als frontend. De site bevatte een banner voor toestemming voor cookies die aan alle visuele verwachtingen voldeed: duidelijke taal, een knop Accepteren, een knop Weigeren, een link naar een privacybeleid. Het zag er, volgens elke normale standaard voor het bekijken van een website, volledig conform uit.

Het probleem kwam aan de oppervlakte toen een bezoeker (toevallig iemand die bekend was met privacytools) de netwerkactiviteit van de site controleerde en ontdekte dat Google Analytics bij elke paginalading werd geactiveerd, voordat er ook maar enige toestemmingskeuze was gemaakt. Bij verdere tests veranderde het uiterlijk van de banner door op 'afwijzen' te klikken, maar dit had geen enkel effect op het daadwerkelijke script: de analyses bleven elke bezoeker volgen die zich expliciet had afgemeld, precies hetzelfde als bezoekers die zich hadden aangemeld.

LaunchStudio heeft het laden van de scripts van de site geherstructureerd, zodat analyses en andere niet-essentiële scripts volledig worden achtergehouden totdat uitdrukkelijke toestemming is verleend, en heeft de afwijzingsactie zo ingesteld dat deze scripts daadwerkelijk worden geladen, in plaats van alleen maar de banner te verbergen. We hebben ook een controle op de toestemmingsstatus toegevoegd die tijdens paginabezoeken correct blijft bestaan, zodat terugkerende bezoekers niet opnieuw worden gevolgd nadat ze één keer hebben afgewezen. **Resultaat:** De site van StudioLicht komt nu, op netwerkniveau, precies overeen met wat de banner belooft.

> *"Ik dacht echt dat een cookiebanner een cookiebanner was. Ik had geen idee dat 'afwijzen' puur cosmetisch kon zijn. Het is zo'n stille manier om niet-conform te zijn zonder het te weten."*
> — **Vera Willemse, Oprichter, StudioLicht (Terneuzen)**

**Kosten en tijdlijn:** € 500 (implementatie van script-gating, persistentie van de toestemmingsstatus, verificatie op netwerkniveau) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Waarom laat mijn cookiebanner nog steeds trackingscripts uitvoeren nadat iemand op Weigeren klikt?

Omdat AI-websitebouwers doorgaans het visuele gedrag van de banner genereren zonder deze te verbinden met de daadwerkelijke scripttags, worden de banner en de trackingscripts gebouwd als twee losstaande delen, tenzij iemand ze expliciet met elkaar verbindt.

### Is een visueel compatibele banner voldoende om te voldoen aan de AVG en de ePrivacy-richtlijn?

Nee. De wettelijke vereiste gaat over het daadwerkelijke gegevensverzamelingsgedrag, niet over het verschijnen van banners; scripts moeten worden geblokkeerd totdat toestemming wordt verleend, en de gegevens van een afgewezen bezoeker mogen helemaal niet worden verzameld.

### Hoe weet ik zelfs of mijn site dit probleem heeft?

Open uw site in een privé-browservenster, open het netwerktabblad van uw browser en kijk wat er wordt geladen voordat u met de banner communiceert, en opnieuw nadat u op weigeren heeft geklikt. Als trackingverzoeken op een bepaald moment worden geactiveerd, is de implementatie onvolledig.

### Hoe controleert het team van Manifera dit anders dan bij een typische websitebeoordeling?

De technici van Manifera testen op netwerkverzoekniveau in plaats van op visueel niveau, omdat dat de laag is waar feitelijke naleving of niet-naleving plaatsvindt - een controle die gebaseerd is op dezelfde nauwkeurigheid die wordt toegepast op zakelijke klanten als TNO en CFLW.

### Geldt dit voor alle AI-websitebouwers, of alleen voor v0?

Het is een gebruikelijk patroon bij v0, Lovable, Bolt en soortgelijke tools, omdat geen van deze standaard de status van de toestemmingsbanner koppelt aan het laden van scripts. Het vereist een expliciete implementatiestap, ongeacht welke tool de site heeft gebouwd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my cookie banner still let tracking scripts run after someone clicks reject?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because AI website builders typically generate the banner's visual behavior without connecting it to the actual script tags \u2014 they're built as two disconnected pieces unless someone wires them together."
      }
    },
    {
      "@type": "Question",
      "name": "Is a visually compliant banner enough to satisfy GDPR and the ePrivacy Directive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The legal requirement is about actual data collection behavior \u2014 scripts need to be blocked until consent, and a rejected visitor's data shouldn't be collected at all."
      }
    },
    {
      "@type": "Question",
      "name": "How would I even know if my site has this problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open your site in a private browsing window, open your browser's network tab, and watch what loads before and after clicking reject \u2014 if tracking requests fire either time, the implementation is incomplete."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's team check for this differently than a typical website review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera's engineers test at the network request level rather than the visual level, drawing on the same rigor applied to enterprise clients like TNO and CFLW."
      }
    },
    {
      "@type": "Question",
      "name": "Does this apply to all AI website builders, or just v0?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's a common pattern across v0, Lovable, Bolt, and similar tools, since none of them connect consent banner state to script loading by default."
      }
    }
  ]
}
</script>