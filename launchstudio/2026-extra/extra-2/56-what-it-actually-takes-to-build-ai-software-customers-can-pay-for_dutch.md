---
Titel: "Wat het daadwerkelijk vereist om AI-software te bouwen waar klanten voor kunnen betalen"
Trefwoorden: build ai software, develop ai software, ai saas, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-oprichter Scale-Up
---

# Wat het daadwerkelijk vereist om AI-software te bouwen waar klanten voor kunnen betalen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat het daadwerkelijk vereist om AI-software te bouwen waar klanten voor kunnen betalen",
  "description": "Een technische verdieping in waar gevoelige gegevens aan de client-side opgeslagen worden.",
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
  "datePublished": "2026-08-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/what-it-actually-takes-to-build-ai-software-customers-can-pay-for"
  }
}
</script>

Om AI-software te bouwen die klanten oprecht genoeg vertrouwen om voor te betalen, is voortdurende aandacht nodig, één specifieke technische beslissing per keer. Waar gevoelige gegevens precies terechtkomen op het eigen apparaat van een gebruiker is een van die beslissingen. En het is een beslissing die AI-coderingsassistenten snel en vaak zonder veel controle nemen, aangezien het onmiddellijke doel (de gegevens beschikbaar maken waar de interface het nodig heeft) even goed werkt ongeacht de opslagkeuze.

## Waarom opslag aan de client-zijde voelt als een handige, neutrale keuze

Het bewaren van gegevens zoals een betaaltoken-referentie, het opgeslagen bezorgadres van een klant of sessiedetails in de `localStorage` van de browser is een razendsnelle en laagdrempelige manier om die data direct beschikbaar te maken voor de gebruikersinterface zonder bij elke interactie een extra netwerkverzoek naar de server te hoeven sturen. Het is een buitengewoon handig patroon waar AI-codeertools instinctief naar grijpen, simpelweg omdat het direct werkt en de frontend-code overzichtelijk houdt. Het is bovendien het patroon dat het leeuwendeel van online tutorials en code-voorbeelden standaard laat zien: een ontwikkelaar die uitlegt hoe je data overal in een React-app beschikbaar maakt, heeft immers geen enkele reden om enterprise-beveiligingsprotocollen te modelleren. Een AI-tool die getraind is op die publieke code erft diezelfde standaardvoorkeur automatisch over.


## Waarom Local Storage specifiek een ongerelateerde kwetsbaarheid uitvergroot

Gegevens opgeslagen in de `localStorage` van een browser zijn rechtstreeks leesbaar door elk JavaScript dat op die pagina draait – inclusief kwaadaardige scripts die via een compleet afzonderlijke kwetsbaarheid (zoals XSS) elders in de applicatie zijn geïnjecteerd. Een cookie met de juiste beveiligingsvlaggen (`HttpOnly`) kan geconfigureerd worden om exact dit soort toegang te weerstaan. Gegevens die in `localStorage` zitten kunnen dat over het algemeen niet.

## Waarom dit specifieke risico gemakkelijk te onderschatten is in isolatie

Louter op zichzelf beschouwd veroorzaakt het opslaan van gegevens in `localStorage` geen onmiddellijk, zichtbaar probleem. Het risico wordt pas concreet in combinatie met een afzonderlijke scripting-kwetsbaarheid. Exact daarom is deze specifieke keuze gemakkelijk over het hoofd te zien bij het onafhankelijk beoordelen van opslagbeslissingen.

## Waarom dit cumulatieve risico meer uitmaakt voor groeiende SaaS-producten

Naarmate een SaaS-product schaalt en meer functies verzamelt, ontstaat er meer oppervlak waar uiteindelijk een ongerelateerde scripting-kwetsbaarheid kan verschijnen. Een opslagbeslissing die op kleine schaal een laag risico leek, wordt zo progressief ingrijpender.

## Wat het op de juiste manier afhandelen hiervan vereist

Een correcte beoordeling identificeert welke specifieke stukken gegevens oprecht client-side opgeslagen moeten worden. En voor alles wat gevoelig is, migreert het die opslag naar een juist geconfigureerde, beschermde cookie of een sessiereferentie aan de serverzijde. [LaunchStudio](https://launchstudio.eu/nl/) voert exact dit soort beoordeling van gegevensopslag aan de client-side uit, ondersteund door Manifera's 11+ jaar ervaring met veilige frontend-architectuur over productie-SaaS-producten.

Manifera's beveiligingsbeoordelingen voor gegevensopslag in de frontend worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Klaar om te lanceren? Weken, geen maanden, van prototype tot productie](https://launchstudio.eu/nl/#contact).

## Wat Thuishoort in Local Storage, en Wat Beslist Niet

Niet alles hoeft rigoureus uit `localStorage` te worden verbannen — het behandelen als universeel verboden is net zo onpraktisch als het behandelen als universeel veilig. De nuttige vraag is in welke specifieke categorie een bepaald gegeven valt.

**Over het algemeen prima geschikt voor Local Storage:**

- Voorkeuren voor de gebruikersinterface — donkere modus (dark mode), status van een ingeklapte menubalk, taalvoorkeur of het laatst geopende tabblad.
- Niet-gevoelige concepten van formulierinvoer die het gebruikersgemak vergroten — tijdelijk opgeslagen tekst van een review waaraan wordt gewerkt, zodat deze niet verloren gaat bij een browser-crash.
- Data die elders al openbaar beschikbaar is, waarbij lokale opslag louter dient als prestatie-optimalisatie om laadtijden te versnellen.

**Absoluut ongeschikt voor Local Storage (moet naar beveiligde cookies of de backend):**

- Authenticatietokens, sessiesleutels en JWT's — alles wat, indien uitgelezen door een kwaadaardig script, dat script in staat stelt te handelen namens de ingelogde gebruiker.
- Opgeslagen bezorgadressen, telefoonnummers of persoonlijke contactgegevens van klanten.
- Iedere verwijzing naar betaalmethoden, transactietokens of creditcardgegevens.
- Gegevens waarvan de openbaarmaking de ene klant in staat zou stellen de gegevens van een andere klant in te zien of te wijzigen.

**De test die elk twijfelgeval direct beslecht:**

Stel uzelf bij elk gegeven in `localStorage` de directe vraag: "Als een toekomstige, nog onbekende scriptkwetsbaarheid een aanvaller in staat stelt om vandaag alles in `localStorage` uit te lezen, wat is dan het allerslechtste dat ermee kan gebeuren?" Bij een donkere modus-voorkeur is dat 'iemand ontdekt dat u van donkere thema's houdt' — volstrekt onschadelijk. Bij een sessietoken of opgeslagen adres ziet het antwoord er heel anders uit. Dat verschil bepaalt exact waar de data hoort te leven. Een proactieve migratie van gevoelige data naar afgeschermde server-side sessies voorkomt dat latere scriptlekken ooit kunnen escaleren tot een volwaardig datalek, wat de continuïteit van uw platform direct veiligstelt.


## Echt voorbeeld

### Een AI-native oprichter in actie: De opslagkeuze die een kleine fout groter maakte

Renske, een voormalig manager van een stomerij die oprichter werd in Sittard, bouwde WasService, een AI-ondersteunde SaaS voor het boeken van was- en stomerij-ophaaldiensten gebouwd met Bolt. Ze schaalde over verschillende maanden van een lokale pilot naar een groeiend klantenbestand in meerdere steden.

Een ongerelateerde, relatief kleine scripting-kwetsbaarheid ontdekt in een nieuwere functie bleek ernstiger te zijn dan de initiële beoordeling suggereerde, specifiek omdat WasService sessie- en opgeslagen adresdetails in de `localStorage` van de browser opsloeg in plaats van in een beschermde cookie. De scripting-fout kon die opgeslagen gegevens rechtstreeks lezen. LaunchStudio's beoordeling identificeerde het `localStorage`-patroon als de specifieke reden dat de impact breder was.

**Resultaat:** LaunchStudio herstelde de initiële scripting-kwetsbaarheid en migreerde afzonderlijk WasService's gevoelige gegevens aan de client-zijde naar beveiligde cookie-opslag, wat de potentiële impact van eventuele toekomstige kwetsbaarheden beperkt.

> *"De oorspronkelijke fout zelf was eerlijk gezegd vrij klein op zichzelf. Het was specifiek hoe we hadden gekozen om gegevens op te slaan dat een kleine fout veranderde in iets met echte tanden."*
> — **Renske Bosman, Oprichter, WasService (Sittard)**

**Kosten en tijdlijn:** € 2.200 (beveiligingsmigratie van client-side opslag) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Waarom is het opslaan van authenticatietokens in `localStorage` zo riskant?

Omdat `localStorage` geen enkel beveiligingsmechanisme heeft om toegang te beperken: elk script dat op het domein wordt uitgevoerd (inclusief externe scripts voor advertenties, chatwidgets of analytics) heeft volledige lees- en schrijftoegang. Als uw applicatie ooit een XSS-kwetsbaarheid bevat, kan een aanvaller alle opgeslagen tokens direct stelen.

### Wat is het veilige alternatief voor het bewaren van inlogsessies in de browser?

Het opslaan van sessietokens in `HttpOnly`, `Secure` cookies. Deze cookies worden door de browser automatisch meegestuurd bij netwerkverzoeken naar uw API, maar zijn volledig onzichtbaar en ontoegankelijk voor JavaScript-code op de pagina.

### Is `localStorage` dan helemaal nergens goed voor?

Zeker wel — voor gegevens die volstrekt niet gevoelig zijn en waarvan openbaarmaking geen enkel risico oplevert, zoals de voorkeur voor een donkere modus, de taalinstelling van de website of de status van een ingeklapte menubalk.

### Manifera ontwerpt frontend-architecturen voor complexe SaaS-producten — hoe pakt het team sessieopslag aan?

Manifera hanteert een 'defense-in-depth' benadering waarbij sessietokens uitsluitend via beveiligde cookies worden uitgewisseld, gecombineerd met Content Security Policies (CSP) die voorkomen dat kwaadaardige scripts überhaupt op de pagina kunnen worden geladen.

### Is de overstap van `localStorage` naar veilige cookies ingewikkeld voor een live applicatie?

Nee, de backend moet worden aangepast om het token via een Set-Cookie header terug te sturen in plaats van in de JSON-body van de login-respons, en de frontend-aanroepen moeten worden geconfigureerd om credentials mee te sturen (`credentials: 'include'`). Dit kan worden doorgevoerd zonder downtime.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is het opslaan van authenticatietokens in `localStorage` zo riskant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat `localStorage` geen enkel beveiligingsmechanisme heeft om toegang te beperken: elk script dat op het domein wordt uitgevoerd (inclusief externe scripts voor advertenties, chatwidgets of analytics) heeft volledige lees- en schrijftoegang. Als uw applicatie ooit een XSS-kwetsbaarheid bevat, kan een aanvaller alle opgeslagen tokens direct stelen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het veilige alternatief voor het bewaren van inlogsessies in de browser?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het opslaan van sessietokens in `HttpOnly`, `Secure` cookies. Deze cookies worden door de browser automatisch meegestuurd bij netwerkverzoeken naar uw API, maar zijn volledig onzichtbaar en ontoegankelijk voor JavaScript-code op de pagina."
      }
    },
    {
      "@type": "Question",
      "name": "Is `localStorage` dan helemaal nergens goed voor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zeker wel — voor gegevens die volstrekt niet gevoelig zijn en waarvan openbaarmaking geen enkel risico oplevert, zoals de voorkeur voor een donkere modus, de taalinstelling van de website of de status van een ingeklapte menubalk."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera ontwerpt frontend-architecturen voor complexe SaaS-producten — hoe pakt het team sessieopslag aan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera hanteert een 'defense-in-depth' benadering waarbij sessietokens uitsluitend via beveiligde cookies worden uitgewisseld, gecombineerd met Content Security Policies (CSP) die voorkomen dat kwaadaardige scripts überhaupt op de pagina kunnen worden geladen."
      }
    },
    {
      "@type": "Question",
      "name": "Is de overstap van `localStorage` naar veilige cookies ingewikkeld voor een live applicatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, de backend moet worden aangepast om het token via een Set-Cookie header terug te sturen in plaats van in de JSON-body van de login-respons, en de frontend-aanroepen moeten worden geconfigureerd om credentials mee te sturen (`credentials: 'include'`). Dit kan worden doorgevoerd zonder downtime."
      }
    }
  ]
}
</script>
