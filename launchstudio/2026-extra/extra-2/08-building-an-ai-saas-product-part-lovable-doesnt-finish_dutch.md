---
Titel: "Een AI-SaaS-product aan het bouwen? Hier is het gedeelte dat Lovable niet afmaakt"
Trefwoorden: ai saas, ai coding, ai native, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# Een AI-SaaS-product aan het bouwen? Hier is het gedeelte dat Lovable niet afmaakt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-SaaS-product aan het bouwen? Hier is het gedeelte dat Lovable niet afmaakt",
  "description": "80% van de met AI gebouwde projecten bereikt nooit productie.",
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
    "@id": "https://launchstudio.eu/en/blog/building-an-ai-saas-product-part-lovable-doesnt-finish"
  }
}
</script>

80% van de met AI gebouwde projecten bereikt nooit productie. Die statistiek heeft de neiging om oprichters in exact de verkeerde richting te alarmeren – richting het aannemen dat hun eigen prototype wel een diepe, onbekende fout moet hebben. Terwijl de aanzienlijk veelvoorkomendere realiteit een specifieke, saaie en volledig herstelbare kloof is: niemand voegde bescherming toe tegen het indienen van een formulier vanaf een plek waar het dat niet zou moeten kunnen.

## Wat CSRF-bescherming daadwerkelijk voorkomt

Cross-Site Request Forgery (CSRF)-bescherming bestaat om te voorkomen dat een kwaadwillige site de browser van een ingelogde gebruiker misleidt om een verzoek in te dienen bij uw applicatie zonder de kennis of toestemming van de gebruiker. Bijvoorbeeld een verborgen formulier op een ongerelateerde pagina die stilletjes een verzoek indient om de accountinstellingen van een ingelogde gebruiker te wijzigen op het moment dat hij die pagina bezoekt. Zonder deze bescherming heeft uw applicatie geen manier om een verzoek dat de gebruiker oprecht bedoeld heeft te onderscheiden van een verzoek dat zijn browser werd misleid om te verzenden.

## Waarom door AI gegenereerde formulieren dit frequent overslaan

Het bouwen van een formulier dat met succes gegevens indient – het gedeelte dat een demo rechtstreeks test – is voor een AI-coderingsassistent eenvoudig om correct te genereren. Het toevoegen van een CSRF-token dat het formulier bevat en dat de server onafhankelijk verifieert is een afzonderlijke, toevoegende stap die geen zichtbaar effect heeft op het feit of het formulier "werkt" tijdens het testen door de oprichter zelf. Dit is precies het soort onzichtbare-totdat-het-relevant-is detail dat standaard wordt overgeslagen.

## Waarom deze specifieke kloof zelden naar boven komt bij informeel testen

Een oprichter die zijn eigen formulier voor accountinstellingen indient, vanuit zijn eigen applicatie, op zijn eigen apparaat, genereert nooit het scenario waar CSRF-bescherming tegen verdedigt – er is in die test überhaupt geen kwaadwillige externe site betrokken. De kloof wordt pas relevant op het moment dat een ingelogde gebruiker ergens anders op het internet komt die specifiek probeert het te misbruiken, een scenario dat geen enkele hoeveelheid zorgvuldig testen door de oprichter ooit zou produceren. Zelfs QA-processen met een tweede persoon die het product test hebben de neiging het niet op te vangen. Die tweede tester gebruikt de applicatie namelijk nog steeds zoals bedoeld, vanuit een normaal browsertabblad, zonder enige door een aanvaller beheerde pagina ergens in de lus. De gehele kwetsbaarheid bestaat alleen in de specifieke kloof tussen "een verzoek dat de gebruiker wilde verzenden" en "een verzoek dat zijn browser werd misleid om te verzenden". Geen enkele hoeveelheid conventioneel functioneel testen, hoe grondig ook, is ontworpen om dit te peilen.

## De andere formulier-beveiligingskloven die meestal meereizen met ontbrekende CSRF-bescherming

CSRF-bescherming komt zelden alleen. In de praktijk, wanneer een beoordeling een formulier vindt dat CSRF-tokens mist, is het gebruikelijk om een klein trossie van gerelateerde, vergelijkbaar onzichtbare-in-testen kloven er direct naast te vinden. Ze delen namelijk allemaal dezelfde oorzaak: een categorie van bescherming die geen zichtbare functionaliteit toevoegt tijdens het eenvoudige testen door een oprichter zelf.

**Ontbrekende of verkeerd geconfigureerde cookie-attributen.** Sessie-cookies moeten doorgaans worden ingesteld met een `SameSite`-attribuut dat beperkt wanneer een browser ze meestuurt met een cross-site verzoek – een instelling die, correct geconfigureerd, een betekenisvol deel van aanvallen in CSRF-stijl blokkeert voordat een tokencontrole überhaupt nodig is. Met AI gegenereerde authenticatiecode laat cookies frequent op hun permissieve standaardwaarde staan in plaats van dit attribuut expliciet in te stellen.

**Blootstelling aan Clickjacking.** Zonder een expliciete header die browsers vertelt dat uw pagina's niet geladen kunnen worden binnen een onzichtbare iframe op de site van iemand anders, kan een kwaadwillige pagina transparante knoppen aanbrengen over de echte interface van uw applicatie. Dit misleidt een ingelogde gebruiker om te klikken op iets wat hij kan zien (op de pagina van de aanvaller) terwijl hij daadwerkelijk klikt op de verborgen knop van uw applicatie eronder. Een enkele respons-header (`X-Frame-Options` of een gelijkwaardige Content-Security-Policy richtlijn) sluit dit. En het is een ander voorbeeld van een herstelling van één regel die nul zichtbaar effect heeft tijdens normaal testen.

**Open Omleidingen (Open Redirects).** Een functie "omleiding na inloggen" of "terugkeren naar deze pagina" die elke URL accepteert zonder het te valideren tegen een toegestane lijst kan misbruikt worden om een gebruiker door uw legitieme, vertrouwde domein te sturen op weg naar een overtuigende phishing-pagina. Technisch gezien blijft uw applicatie exact werken zoals ontworpen, terwijl het gebruikt wordt als opstapje voor iets heel anders.

**Onontsnapte uitvoer (Unescaped Output) die de pagina bereikt.** Overal waar door gebruikers ingediende inhoud (een reactie, een weergegeven naam, een ondersteuningsbericht) terug op de pagina wordt gerenderd zonder de juiste ontsnapping (escaping), opent dit de deur naar opgeslagen Cross-Site Scripting (XSS). De kwaadwillige invoer van de ene gebruiker wordt uitgevoerd in de browsersessie van een andere gebruiker simpelweg doordat die tweede gebruiker de pagina bekijkt.

**Waarom deze meereizen:** alle vier delen het exacte profiel dat door dit stuk heen beschreven is – een formulier of een pagina die zichtbaar correct werkt in elke test die een oprichter uitvoert, omdat geen van deze kloven het ideale pad beïnvloedt. Een CSRF-audit die stopt bij CSRF-tokens alleen, zonder het controleren van cookie-configuratie, framing-headers, omleidingsvalidatie en uitvoerontsnapping, heeft de neiging de rest van deze tros ongeraakt te laten. Daarom controleert LaunchStudio's formulier-beveiligingsstap ze allemaal samen in plaats van CSRF als een geïsoleerde bevinding te behandelen.

## Waarom "Slechts 20% overgebleven" onderschat hoe afgebakend de herstelling daadwerkelijk is

Het kaderen hiervan als "de laatste 20%" laat het vaag en open-ended klinken, terwijl het in de praktijk doorgaans een korte, specifieke lijst is: CSRF-tokens op formulieren die status wijzigen, server-side verificatie van die tokens, en testen dat een verzoek zonder een geldig token wordt geweigerd. Het is een gedefinieerde omvang van het werk, en geen open-ended herbouw – wat exact is waarom LaunchStudio het prijst als een vast, afgebakend traject in plaats van een uurlijks, onvoorspelbaar traject.

## Wat het sluiten van deze kloof kost en kost aan tijd

Voor een typisch door een oprichter gebouwd SaaS-product past deze categorie van herstellingen – CSRF-bescherming samen met het handvol gerelateerde formulierbeveiligingskloven die er meestal mee meereizen – comfortabel binnen LaunchStudio's Launch Ready-reeks van € 800 tot € 3.500, geleverd in één tot drie weken tegen een vaste prijs afgesproken na een kort introductiegesprek. [LaunchStudio](https://launchstudio.eu/en/) wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in het sluiten van exact deze categorie van kloven voor productieapplicaties.

Manifera's engineering-levering draait via haar ontwikkelingscentrum aan de Pho Quang-straat in Ho Chi Minh-stad, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420 dat het initiële klantgesprek afhandelt.

[Krijg een kostenschatting met onze prijscalculator](https://launchstudio.eu/en/#calculator).

## Echt voorbeeld

### Een AI-native oprichter in actie: De instellingswijziging waar niemand om vroeg

Eva, een voormalig evenementencoördinator die oprichter werd in Breda, bouwde TicketFlow, een AI-ondersteunde tool voor evenemententicketing gebouwd met Lovable, waarmee organisatoren hun eigen account- en uitbetalingsinstellingen kunnen beheren via een eenvoudig instellingenformulier.

Een gebruiker meldde dat zijn bankgegevens voor uitbetalingen waren gewijzigd zonder zijn medeweten, en de logboeken van de ondersteuning toonden geen inlog vanaf een onbekend apparaat – alleen een normale, geauthenticeerde sessie. LaunchStudio's beoordeling vond dat het instellingenformulier geen CSRF-bescherming had, wat betekende dat elke externe pagina stilletjes dezelfde wijziging kon hebben getriggerd terwijl de gebruiker simpelweg elders was ingelogd.

**Resultaat:** LaunchStudio voegde CSRF-tokens toe aan elk formulier in TicketFlow dat status wijzigt, en verifieerde de weigering van elk verzoek dat een geldig token miste, waardoor de blootstelling werd gesloten zonder het ontwerp of de werkstroom van de instellingenpagina te veranderen.

> *"Het idee dat simpelweg ingelogd zijn ergens anders op het internet een totaal ongerelateerde pagina mijn bankgegevens zou kunnen laten wijzigen is oprecht beangstigend. Ik had geen idee dat het überhaupt mogelijk was totdat dit gebeurde."*
> — **Eva Willems, Oprichter, TicketFlow (Breda)**

**Kosten en tijdlijn:** € 1.800 (CSRF-bescherming en audit van formulierbeveiliging) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Zou een frontend-gericht ingenieur CSRF beschrijven als een frontend- of een backend-probleem?

Oprecht beide – het token moet gegenereerd en ingebed worden door de frontend, maar het is betekenisloos tenzij de backend het onafhankelijk verifieert. Dat is exact waarom het gemakkelijk is voor beide kanten, afzonderlijk werkend, om aan te nemen dat de andere kant het heeft afgehandeld.

### Is CSRF-bescherming specifiek voor formulieren, of geldt het ook voor API-oproepen?

Het geldt voor elk verzoek dat status wijzigt, niet alleen traditionele HTML-formulieren – API-eindpunten die gegevens wijzigen op basis van een ingelogde sessie staan voor de identieke blootstelling en hebben dezelfde bescherming nodig.

### Drukt de 80% productie-mislukkingsstatistiek uit hoe ernstig de specifieke kloof van een individuele oprichter neigt te zijn?

Vaak wel – de statistiek beschrijft een resultaat (nooit productie bereiken), niet noodzakelijkerwijs een ernstniveau. Veel van de specifieke kloven erachter, zoals die van Eva, zijn smal afgebakend en in dagen te herstellen zodra ze daadwerkelijk geïdentificeerd zijn.

### Weerspiegelt Eva's case de visie van CEO Herre Roelevink op de oprichterseconomie?

Zeer rechtstreeks – Roelevink's uitgesproken visie is dat oprichters nu snel oprecht goede producten bouwen met AI, maar toegewijde architectuur- en beveiligings-expertise nodig hebben om de overgebleven, specifieke kloven te sluiten.

### Kan een oprichter dit opvangen door zijn AI-tool rechtstreeks te vragen of CSRF-bescherming is inbegrepen?

Soms – expliciet prompten voor CSRF-bescherming kan er toe leiden dat een tool het opneemt, maar vertrouwen op het onthouden om te vragen naar elke relevante bescherming is een breekbaar alternatief voor een toegewijde beoordeling.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is CSRF-bescherming een frontend- of backend-probleem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beide — de frontend genereert het token, maar het is betekenisloos tenzij de backend het onafhankelijk verifieert."
      }
    },
    {
      "@type": "Question",
      "name": "Geldt CSRF-bescherming alleen voor HTML-formulieren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het geldt voor elk verzoek dat status wijzigt, inclusief API-eindpunten bij ingelogde sessies."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent de 80% mislukkingsstatistiek dat de meeste kloven ernstig zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet noodzakelijkerwijs — veel onderliggende kloven zijn smal afgebakend en in dagen te herstellen."
      }
    },
    {
      "@type": "Question",
      "name": "Weerspiegelt deze case de visie van de CEO op de kansen in de oprichterseconomie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zeer rechtstreeks — goede producten gebouwd met AI hebben nog steeds toegewijde expertise nodig om specifieke kloven te sluiten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een oprichter dit opvangen door er expliciet om te vragen bij de AI-tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Soms, maar vertrouwen op het onthouden om te vragen is een breekbaar alternatief voor een systematische beoordeling."
      }
    },
    {
      "@type": "Question",
      "name": "Zou een smal afgebakende CSRF-beoordeling gerelateerde formulierkloven missen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mogelijk — daarom controleert LaunchStudio de gerelateerde tros (cookies, framing-headers, omleidingen) standaard samen."
      }
    }
  ]
}
</script>
