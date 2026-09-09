---
Titel: "Het beste uit AI-coding halen zonder de slechte gewoonten over te nemen"
Trefwoorden: best of ai, all ai tools, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Bureau / Freelancer (White-Label Partner)
---

# Het beste uit AI-coding halen zonder de slechte gewoonten over te nemen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het beste uit AI-coding halen zonder de slechte gewoonten over te nemen",
  "description": "Een vergelijking van wat een bureau moet behouden versus corrigeren bij het overnemen van klantwerk.",
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
  "datePublished": "2026-08-03",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/getting-the-best-of-ai-coding-without-inheriting-its-worst-habits"
  }
}
</script>

Het beste halen uit AI-programmering bij het overnemen van het bestaande project van een klant betekent herkennen wat oprecht het behouden waard is – meestal het grootste deel ervan – en welke specifieke gewoonten het waard zijn om te corrigeren voor de lancering. De configuratie van sessie-cookies is een specifiek, veelvoorkomend voorbeeld van exact die tweede categorie.

## Wat bijna altijd het behouden waard is

De algehele structuur, de kern-functielogica en de algemene aanpak die een AI-coderingsassistent heeft genomen, is in de grote meerderheid van de gevallen oprecht solide en het waard om compleet te behouden. Opnieuw bouwen vanaf nul – zoals LaunchStudio's filosofie van "we behouden uw frontend, we herstellen alleen wat nodig is" weerspiegelt – verspilt de echte waarde die al gecreëerd is. Voor RitDirect specifiek bleven de boekingsstroom en het chauffeur-koppelingssysteem compleet onaangetast. Het werk dat er daadwerkelijk toe deed was smal en specifiek: een handvol configuratiewaarden binnen het authenticatiesysteem.

## Wat specifiek een tweede blik nodig heeft: Beveiligingsvlaggen voor cookies

Sessie-cookies – de kleine stukjes gegevens die een browser opslaat om een gebruiker ingelogd te houden – ondersteunen verschillende specifieke beveiligingsvlaggen: of ze beperkt zijn om gelezen te worden door JavaScript (`HttpOnly`), of ze alleen via versleutelde verbindingen worden verzonden (`Secure`), en of ze beperkt zijn om verzonden te worden bij cross-site verzoeken (`SameSite`). Met AI gegenereerde code richt frequent een werkende sessie-cookie in zonder al deze vlaggen te configureren, aangezien de cookie in beide gevallen functioneel werkt voor inlogdoeleinden.

## Waarom ontbrekende cookievlaggen andere kleine kloven uitvergroten

Een sessie-cookie die de vlag mist die JavaScript-toegang beperkt (`HttpOnly`), wordt rechtstreeks leesbaar door elk script dat op de pagina draait. Als er elders een afzonderlijke kwetsbaarheid zoals een cross-site scripting (XSS)-kloof bestaat, zou een juist geflagde cookie hebben voorkomen dat een actief sessietoken gestolen werd. Een niet-geflagde cookie biedt die extra beschermingslaag niet.

## Waarom dit zelden individueel geverifieerd wordt tijdens een overdracht

Een bureau dat de overgenomen codebase van een klant beoordeelt, richt zich van nature op functionele compleetheid – werkt de inlog, werkt de kern-functionaliteit. Cookie-vlagconfiguratie is een specifiek detail dat geen invloed heeft op of de inlog "werkt" op een manier die een functionele beoordeling opvangt.

## Waarom het goed krijgen van dit detail uitmaakt voor de reputatie van een bureau

Een klant die vertrouwt op de lancering-review van een bureau om oprecht grondig te zijn, verwacht dat exact dit soort niet-voor-het-hand-liggende details worden opgevangen.

## Hoe LaunchStudio bureaus ondersteunt met deze specifieke controle

[LaunchStudio](https://launchstudio.eu/nl/) verifieert de beveiligingsconfiguratie van cookies als standaard onderdeel van haar white-label technische beoordeling voor bureaus die overdrachten van klanten afhandelen, ondersteund door Manifera's 11+ jaar ervaring met veilig sessiebeheer.

Manifera's beoordelingen van sessiebeveiliging worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Freelancer of kleine studio? Wij zijn het engineeringteam achter uw merk](https://launchstudio.eu/nl/#contact).

## De Drie Cookie-Vlaggen, Uitgelegd in Heldere Taal

Voor een oprichter of bureau-eigenaar zonder diepe beveiligingsachtergrond kunnen 'cookie-vlaggen' abstract klinken. Afzonderlijk bekeken is elke vlag echter een specifiek, begrijpelijk antwoord op een heel concrete beveiligingsvraag.

**1. HttpOnly — kan JavaScript op de pagina dit cookie uitlezen?**

Zonder deze vlag kan elk script dat in de browser draait — inclusief een kwaadaardig script dat is geïnjecteerd via een niet-gerelateerde XSS-kwetsbaarheid elders in de app — het sessiecookie rechtstreeks uitlezen via `document.cookie` en de waarde naar een externe server sturen. Met `HttpOnly` ingeschakeld wordt het cookie uitsluitend automatisch door de browser meegestuurd in HTTP-verzoeken naar de backend; geen enkel script op de pagina, kwaadaardig of legitiem, kan de inhoud ervan ooit inzien.

**2. Secure — wordt dit cookie ooit over een onbeveiligde verbinding verzonden?**

Zonder deze vlag kan het cookie technisch gezien worden verzonden over een onversleutelde HTTP-verbinding als die ooit optreedt — door een verkeerd geconfigureerde redirect, een verouderde link of een tussenliggend netwerk dat verkeer afluistert. Met de vlag `Secure` weigert de browser resoluut om het cookie te verzenden tenzij de verbinding volledig versleuteld is via HTTPS, waardoor dat specifieke lek volledig wordt afgesloten.

**3. SameSite — wordt dit cookie meegestuurd bij verzoeken vanaf een andere website?**

Zonder een passende `SameSite`-instelling kan een kwaadaardige website die een gebruiker in een ander browsertabblad opent, verzoeken initiëren die het sessiecookie van het slachtoffer meedragen naar uw applicatie zonder diens medeweten — een ontwerpfout genaamd Cross-Site Request Forgery (CSRF). Een correct geconfigureerde SameSite-waarde (zoals `SameSite=Lax`) beperkt exact wanneer het cookie aan externe verzoeken wordt gekoppeld en sluit misbruik betrouwbaar uit.

**Waarom AI-codeertools het cookie zelf vaak wel instellen, maar de vlaggen overslaan**

Het instellen van een cookie dat een gebruiker succesvol ingelogd houdt, vereist technisch gezien alleen een naam en een waarde — de browser accepteert en gebruikt het immers in beide gevallen. De drie vlaggen zijn optionele parameters die het gedrag van het cookie verfijnen in situaties waar een simpele prompt zoals 'houd de gebruiker ingelogd' nooit specifiek om vraagt. Dat is precies waarom een vlekkeloos werkende login en een onbeschermd, blootgesteld cookie perfect naast elkaar kunnen bestaan zonder dat het systeem er ogenschijnlijk kapot uitziet.


## Echt voorbeeld

### Een AI-native oprichter in actie: De cookievlaggen die de overdracht bijna miste

Saskia runt een klein digitaal bureau in Weert dat een overdracht aannam voor RitDirect, een lokale taxi- en rit-dispatch-app die grotendeels met v0 was gebouwd.

Saskia's team richtte zich op het bevestigen dat de boekings- en dispatch-stroom correct werkte. Een toegewijde beveiligingsbeoordeling door LaunchStudio vond dat RitDirect's sessie-cookies verschillende standaard beschermende vlaggen misten. Een ongerelateerd scripting-probleem elders in de app zou hierdoor een veel makkelijker pad hebben gehad om een actieve sessie te stelen.

**Resultaat:** LaunchStudio corrigeerde de sessie-cookieconfiguratie om alle standaard beschermende vlaggen (`HttpOnly`, `Secure`, `SameSite`) op te nemen. Dit sloot de kloof zonder dat het de functionele testen beïnvloedde.

> *"Alles aan de inlog- en boekingsstroom werkte vlekkeloos in elke test die we zelf uitvoerden. Dit is exact het soort detail dat we opvangen omdat we deze controle specifiek elke keer uitvoeren."*
> — **Saskia Bergman, Bureau-eigenaar, Weert**

**Kosten en tijdlijn:** € 1.600 (white-label sessie-cookie beveiligingsaudit) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Waarom is `HttpOnly` de allerbelangrijkste vlag voor sessiecookies?

Omdat `HttpOnly` voorkomt dat kwaadaardige JavaScript-code op de pagina (bijvoorbeeld geïnjecteerd via een XSS-aanval of een gecompromitteerde externe npm-bibliotheek) toegang krijgt tot het cookie via `document.cookie`. Zonder deze vlag kan een aanvaller het actieve sessietoken direct ontvreemden en het account overnemen.

### Wat is het praktische verschil tussen `SameSite=Lax` en `SameSite=Strict`?

`SameSite=Strict` stuurt het cookie nooit mee bij verzoeken die afkomstig zijn van een externe website, zelfs niet als een gebruiker op een gewone link in een e-mail of zoekmachine klikt (waardoor de gebruiker opnieuw moet inloggen). `SameSite=Lax` biedt uitstekende bescherming tegen CSRF-aanvallen terwijl normale externe navigatie probleemloos ingelogd blijft.

### Waarom configureren AI-codeertools deze drie cookie-vlaggen zo vaak niet standaard?

Omdat starter-templates en AI-prompts vaak zijn ingesteld op maximaal gemak tijdens lokale ontwikkeling op `localhost` (waar HTTPS vaak ontbreekt). De code werkt lokaal zonder foutmeldingen, en de stap om voor productie expliciet `Secure; HttpOnly; SameSite=Lax` te forceren wordt vergeten tenzij een engineer dit actief controleert.

### Manifera bouwt webapplicaties met strenge beveiligingseisen — hoe toetst het team cookie-instellingen?

Als vast onderdeel van de deployment-audits controleert Manifera geautomatiseerd de Set-Cookie headers in staging- en productieomgevingen om te waarborgen dat elk authenticatietoken voldoet aan moderne beveiligingsstandaarden.

### Kan een oprichter zelf in zijn eigen browser zien of zijn cookies correct zijn ingesteld?

Ja, open de browserdeveloper tools, navigeer naar het tabblad 'Application' (of 'Opslag'), selecteer 'Cookies' onder het domein, en controleer de kolommen voor `HttpOnly`, `Secure` en `SameSite`. Als hier vinkjes ontbreken bij sessietokens, is directe actie vereist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is `HttpOnly` de allerbelangrijkste vlag voor sessiecookies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat `HttpOnly` voorkomt dat kwaadaardige JavaScript-code op de pagina (bijvoorbeeld geïnjecteerd via een XSS-aanval of een gecompromitteerde externe npm-bibliotheek) toegang krijgt tot het cookie via `document.cookie`. Zonder deze vlag kan een aanvaller het actieve sessietoken direct ontvreemden en het account overnemen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het praktische verschil tussen `SameSite=Lax` en `SameSite=Strict`?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "`SameSite=Strict` stuurt het cookie nooit mee bij verzoeken die afkomstig zijn van een externe website, zelfs niet als een gebruiker op een gewone link in een e-mail of zoekmachine klikt (waardoor de gebruiker opnieuw moet inloggen). `SameSite=Lax` biedt uitstekende bescherming tegen CSRF-aanvallen terwijl normale externe navigatie probleemloos ingelogd blijft."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom configureren AI-codeertools deze drie cookie-vlaggen zo vaak niet standaard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat starter-templates en AI-prompts vaak zijn ingesteld op maximaal gemak tijdens lokale ontwikkeling op `localhost` (waar HTTPS vaak ontbreekt). De code werkt lokaal zonder foutmeldingen, en de stap om voor productie expliciet `Secure; HttpOnly; SameSite=Lax` te forceren wordt vergeten tenzij een engineer dit actief controleert."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera bouwt webapplicaties met strenge beveiligingseisen — hoe toetst het team cookie-instellingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Als vast onderdeel van de deployment-audits controleert Manifera geautomatiseerd de Set-Cookie headers in staging- en productieomgevingen om te waarborgen dat elk authenticatietoken voldoet aan moderne beveiligingsstandaarden."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een oprichter zelf in zijn eigen browser zien of zijn cookies correct zijn ingesteld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, open de browserdeveloper tools, navigeer naar het tabblad 'Application' (of 'Opslag'), selecteer 'Cookies' onder het domein, en controleer de kolommen voor `HttpOnly`, `Secure` en `SameSite`. Als hier vinkjes ontbreken bij sessietokens, is directe actie vereist."
      }
    }
  ]
}
</script>
