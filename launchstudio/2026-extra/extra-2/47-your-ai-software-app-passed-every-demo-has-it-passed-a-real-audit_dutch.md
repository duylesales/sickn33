---
Titel: "Uw AI-software-app is voor elke demo geslaagd. Is het geslaagd voor een echte audit?"
Trefwoorden: ai software app, ai generated tool, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Uw AI-software-app is voor elke demo geslaagd. Is het geslaagd voor een echte audit?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uw AI-software-app is voor elke demo geslaagd. Is het geslaagd voor een echte audit?",
  "description": "Een directe blik op het verschil tussen het slagen voor een demo en het slagen voor een echte audit.",
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
  "datePublished": "2026-08-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/your-ai-software-app-passed-every-demo-has-it-passed-a-real-audit"
  }
}
</script>

Het slagen voor elke demo die u persoonlijk heeft uitgevoerd en het slagen voor een oprechte audit zijn twee verschillende prestaties. De kloof ertussen verschijnt in exact het soort plek dat een demo nooit controleert: wat er daadwerkelijk gebeurt met een sessie nadat een gebruiker op "uitloggen" klikt, versus wat een oprichter aanneemt dat er gebeurt op basis van het feit dat de interface zelf verandert en er uitgelogd uitziet. Een demo is fundamenteel een coöperatieve oefening tussen een oprichter en een publiek dat wil dat het product slaagt. Een audit is per ontwerp inquisitief, en probeert specifiek het ene ding te vinden dat een coöperatieve demonstratie nooit zou proberen.

## Hoe "Uitgelogd" er uit ziet vanuit de interface

Het klikken op uitloggen in een typische AI-software-app verandert op de juiste manier wat de interface toont – het dashboard verdwijnt, een inlogformulier verschijnt opnieuw, alles bevestigt visueel dat het uitloggen werkte. Dit is exact wat een oprichter controleert bij het testen van een uitlogfunctie, en het is een oprecht correct, noodzakelijk onderdeel. Het is ook het enige onderdeel dat de meeste oprichters een natuurlijke reden hebben om te controleren.

## Wat "Uitgelogd" moet betekenen op de server

Voorbij de zichtbare interfacewijziging moet een juiste uitlogactie de onderliggende sessie of het token server-side daadwerkelijk ongeldig maken. Zelfs als een kopie van datzelfde sessietoken op een of andere manier opnieuw wordt gebruikt – via een opgeslagen tabblad of een gedeeld apparaat – mag het geen toegang meer verlenen. Een uitlogactie die alleen de verwijzing van de frontend naar het token wist, zonder het token zelf op de server ongeldig te maken, laat dat token nog steeds volledig functioneel.

## Waarom deze kloof bijna onzichtbaar is tijdens normaal testen

Het testen van uw eigen uitlogfunctie betekent het klikken op uitloggen en bevestigen dat de interface correct verandert – wat het doet, ongeacht of het onderliggende token daadwerkelijk ongeldig werd gemaakt of simpelweg werd vergeten door de frontend. Er is geen natuurlijk punt tijdens deze test waar een oprichter eraan zou denken om het oude token handmatig opnieuw rechtstreeks naar de server te sturen om te controleren of het nog steeds werkt.

## Waarom dit meer uitmaakt op gedeelde of institutionele apparaten

Een e-learningplatform dat wordt gebruikt op gedeelde schoolcomputers staat voor een concreter risico dan een typisch consumentenproduct. Een student die uitlogt op een gedeelde pc verwacht dat de sessie volledig eindigt. Een token dat achteraf geldig blijft creëert een echt risico dat de volgende persoon op dat apparaat onbedoelde toegang behoudt.

## Wat het op de juiste manier herstellen hiervan vereist

Een correcte herstelling garandeert dat de uitlogactie de sessie of het token actief ongeldig maakt op de server, en niet louter de verwijzing op de client wist. [LaunchStudio](https://launchstudio.eu/nl/) test exact dit scenario als onderdeel van haar beoordeling van authenticatiebeveiliging, ondersteund door Manifera's 11+ jaar ervaring met sessie- en tokenbeheer over productiesystemen.

Manifera's audits voor sessiebeveiliging worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Sessiebeheer Verder Dan Uitloggen: Wat U Nog Meer Moet Controleren

Het ongeldig maken van een sessie bij het uitloggen is een belangrijk startpunt, maar het is slechts één schakel in de bredere levenscyclus van gebruikersauthenticatie. Een volwaardige controle inspecteert het gehele sessiebeheer:

- **Automatische sessieverlooptijd (Session Expiry)** — verloopt een inlogtoken automatisch na een redelijke periode van inactiviteit, of blijft het voor altijd geldig zolang de gebruiker niet handmatig op 'Uitloggen' klikt? Een oneindig geldig token betekent dat een eenmaal ontvreemd token voor altijd toegang blijft bieden.
- **Sessie-intrekking bij wachtwoordwijziging** — wanneer een gebruiker zijn wachtwoord wijzigt of herstelt, moet de backend gegarandeerd alle andere actieve sessies van dat account direct beëindigen.
- **Beperking van gelijktijdige sessies (Concurrent Sessions)** — voor gevoelige zakelijke applicaties is het wenselijk om inzicht te hebben in het aantal actieve sessies per account en oude sessies automatisch af te sluiten wanneer vanaf een nieuw apparaat wordt ingelogd.
- **Veilige verversing van tokens (Refresh Token Rotation)** — als uw architectuur gebruikmaakt van korte sessietokens in combinatie met refresh tokens, moet elk refresh token bij gebruik direct worden geroteerd en ongeldig worden gemaakt voor toekomstig hergebruik.
- **Opslaglocatie van inloggegevens in de browser** — zorg ervoor dat sessietokens uitsluitend worden opgeslagen in `HttpOnly`, `Secure` cookies en nooit in `localStorage`, waar ze kwetsbaar zijn voor diefstal via XSS-aanvallen.

Sessiebeveiliging is een doorlopend proces gedurende de hele gebruikerssessie. Het systematisch controleren van deze stappen waarborgt dat de achterdeur net zo goed vergrendeld is als de voordeur.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het uitloggen dat niemand daadwerkelijk uitlogde

Anna, een voormalig leraar voortgezet onderwijs die oprichter werd in Kampen, bouwde ToetsTijd, een AI-ondersteund platform voor e-learning-quizzen gebouwd met Cursor. Het wordt gebruikt op verschillende scholen op gedeelde klaslokaalcomputers waar studenten gedurende de dag frequent in- en uitloggen.

Een IT-vaardige leraar die het gedrag van het platform testte uit professionele voorzichtigheid, sloeg een sessietoken op voor het uitloggen en stuurde het achteraf handmatig opnieuw. Hij ontdekte dat het nog steeds volledige toegang verleende, ondanks dat de interface een uitgelogde status toonde. LaunchStudio's beoordeling bevestigde dat de uitlogfunctie het token alleen wist uit de lokale opslag van de frontend, zonder het überhaupt op de server ongeldig te maken.

**Resultaat:** LaunchStudio implementeerde een correcte sessie-ongeldigverklaring aan de serverzijde getriggerd door uitloggen. Ze bevestigden dat een buitgemaakt token van vóór het uitloggen direct achteraf oprecht stopt met werken.

> *"De interface zag er elke keer dat ik het zelf testte compleet uitgelogd uit, wat exact is waarom ik nooit vermoedde dat er daadwerkelijk nog iets actief was eronder. Er was een leraar voor nodig die specifiek testte op dit gedeelde-apparaat-scenario om het op te vangen."*
> — **Anna Visser, Oprichter, ToetsTijd (Kampen)**

**Kosten en tijdlijn:** € 1.600 (implementatie van sessie-ongeldigverklaring aan de serverzijde) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Zou een sessiespecialist onvolledige uitlog-invalidatie beschouwen als een veelvoorkomend gebrek?

Ja, zeer gebruikelijk — het bouwen van een uitlogknop die de gebruikersinterface visueel update en het token uit de browser wist is direct zichtbaar en eenvoudig te testen. Het daadwerkelijk ongeldig maken van het token op de authenticatieserver vereist een specifieke backend-invalidatielaag die in snelle prototypes vaak ontbreekt.

### Is dit risico alleen relevant voor gedeelde apparaten (zoals op scholen of kantoren), of ook voor individuele gebruikers?

Het is direct acuut op gedeelde apparaten waar een volgende gebruiker het vorige account kan overnemen, maar ook voor individuele gebruikers: als een apparaat wordt gestolen of een netwerkaanval plaatsvindt, blijft een niet-geïnvalideerd token bruikbaar, zelfs nadat de gebruiker meende veilig te zijn uitgelogd.

### Manifera bouwt applicaties voor zowel consumenten als zakelijke instellingen — helpt die ervaring bij het signaleren van sessierisico's?

Ja, het begrijpen van de operationele context (gedeelde werkplekken versus individuele smartphones) bepaalt hoe streng sessies moeten worden beheerd. Manifera implementeert levenscyclusbeheer voor sessies dat voldoet aan enterprise-beveiligingsstandaarden.

### Hoe sluit deze case aan bij de visie van Herre Roelevink over het verschil tussen 'lijkt correct' en 'is correct'?

Perfect — in de browser van de oprichter werkte de uitlogknop vlekkeloos: het scherm sprong naar de homepage en de naam verdween. Het onderliggende token bleef op de achtergrond echter springlevend. Dat verschil tussen uiterlijke werking en diepe technische realiteit is exact waar LaunchStudio op toetst.

### Kan een oprichter zelf controleren of zijn sessietokens na het uitloggen daadwerkelijk dood zijn?

Ja, door een beveiligd netwerkverzoek vanuit de developer tools te kopiëren (als cURL-commando), vervolgens in de browser op 'Uitloggen' te klikken, en daarna exact hetzelfde cURL-verzoek opnieuw uit te voeren in de terminal. Als de server nog steeds data retourneert, is het token server-side niet geïnvalideerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zou een sessiespecialist onvolledige uitlog-invalidatie beschouwen als een veelvoorkomend gebrek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, zeer gebruikelijk — het bouwen van een uitlogknop die de gebruikersinterface visueel update en het token uit de browser wist is direct zichtbaar en eenvoudig te testen. Het daadwerkelijk ongeldig maken van het token op de authenticatieserver vereist een specifieke backend-invalidatielaag die in snelle prototypes vaak ontbreekt."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit risico alleen relevant voor gedeelde apparaten (zoals op scholen of kantoren), of ook voor individuele gebruikers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is direct acuut op gedeelde apparaten waar een volgende gebruiker het vorige account kan overnemen, maar ook voor individuele gebruikers: als een apparaat wordt gestolen of een netwerkaanval plaatsvindt, blijft een niet-geïnvalideerd token bruikbaar, zelfs nadat de gebruiker meende veilig te zijn uitgelogd."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera bouwt applicaties voor zowel consumenten als zakelijke instellingen — helpt die ervaring bij het signaleren van sessierisico's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, het begrijpen van de operationele context (gedeelde werkplekken versus individuele smartphones) bepaalt hoe streng sessies moeten worden beheerd. Manifera implementeert levenscyclusbeheer voor sessies dat voldoet aan enterprise-beveiligingsstandaarden."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe sluit deze case aan bij de visie van Herre Roelevink over het verschil tussen 'lijkt correct' en 'is correct'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Perfect — in de browser van de oprichter werkte de uitlogknop vlekkeloos: het scherm sprong naar de homepage en de naam verdween. Het onderliggende token bleef op de achtergrond echter springlevend. Dat verschil tussen uiterlijke werking en diepe technische realiteit is exact waar LaunchStudio op toetst."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een oprichter zelf controleren of zijn sessietokens na het uitloggen daadwerkelijk dood zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, door een beveiligd netwerkverzoek vanuit de developer tools te kopiëren (als cURL-commando), vervolgens in de browser op 'Uitloggen' te klikken, en daarna exact hetzelfde cURL-verzoek opnieuw uit te voeren in de terminal. Als de server nog steeds data retourneert, is het token server-side niet geïnvalideerd."
      }
    }
  ]
}
</script>
