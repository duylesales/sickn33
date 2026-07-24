---
Titel: "Het acroniemenspiekbriefje dat elke niet-technische oprichter nodig heeft vóór een beveiligingsbeoordeling"
Trefwoorden: ai secure, security review acronyms, RLS RBAC JWT explained, ai app security terms
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Het acroniemenspiekbriefje dat elke niet-technische oprichter nodig heeft vóór een beveiligingsbeoordeling

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het acroniemenspiekbriefje dat elke niet-technische oprichter nodig heeft vóór een beveiligingsbeoordeling",
  "description": "Een spiekbriefje in gewone taal dat RLS, RBAC, JWT, CORS en de andere acroniemen ontcijfert die niet-technische oprichters horen tijdens een beveiligingsbeoordeling, met uitleg waarom elk ervan ertoe doet.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/acronym-cheat-sheet-security-review" }
}
</script>

U hebt een beveiligingsbeoordeling geboekt voor uw door AI gebouwde app, en tien minuten erin zegt de technicus iets als "uw RLS-beleid is niet correct afgebakend, en er zit geen RBAC-laag tussen uw JWT en uw CORS-configuratie." U knikt. U hebt geen idee wat dat betekent, en u gaat niet onderbreken om het te vragen, omdat u al bang bent dat het antwoord duur zal zijn. Dit spiekbriefje bestaat zodat u nooit meer door die zin heen hoeft te knikken. Dit zijn geen algemene AI-buzzwoorden — het is de specifieke, beperkte set acroniemen die opduikt in bijna elke beveiligingsbeoordeling van een door AI gegenereerde app, ontcijferd in gewone taal, met uitleg waarom elk ervan het waard is om echt te begrijpen vóór uw volgende gesprek.

## RLS — Row-Level Security (rijniveaubeveiliging)

Dit is het meest voorkomende gat dat LaunchStudio vindt in door AI gegenereerde apps. RLS is een regel op databaseniveau die beperkt welke rijen van een tabel een bepaalde gebruiker mag lezen of schrijven — bijvoorbeeld ervoor zorgen dat een klant alleen ooit zijn eigen facturen kan opvragen, nooit die van iemand anders, ongeacht welk verzoek er wordt verstuurd. Zonder RLS kan uw frontend de gegevens van anderen wel *verbergen*, maar de database geeft ze nog steeds af aan iedereen die er rechtstreeks om vraagt. RLS is het verschil tussen "de app laat het niet zien" en "de app kan het niet prijsgeven."

## RBAC — Role-Based Access Control (roltoegangscontrole)

RBAC regelt wat verschillende typen gebruikers mogen *doen*, niet alleen wat ze kunnen zien. Een beheerder, een gewone klant en een supportmedewerker zouden verschillende rechten moeten hebben — beheerders kunnen accounts verwijderen, klanten niet. RBAC is het systeem dat die onderscheiden consequent afdwingt in uw hele app, in plaats van dat elk scherm onafhankelijk beslist wie waarop mag klikken.

## JWT — JSON Web Token

Een JWT is het kleine, ondertekende stukje data dat uw app gebruikt om te bewijzen dat een gebruiker is ingelogd, zonder bij elk afzonderlijk verzoek opnieuw een wachtwoord te controleren. Het is hoe uw server een terugkerende gebruiker snel herkent. Het risico ontstaat wanneer JWT's onzorgvuldig worden behandeld — ergens onveilig opgeslagen, een te lange levensduur gegeven, of niet correct geverifieerd aan de serverzijde — waardoor een aanvaller zich kan voordoen als een ingelogde gebruiker.

## CORS — Cross-Origin Resource Sharing

CORS is een door de browser afgedwongen regel over welke websites met uw backend mogen praten. Correct geconfigureerd voorkomt het dat een kwaadwillende site stilletjes verzoeken naar uw app stuurt met gebruikmaking van de ingelogde sessie van een bezoeker. Te los geconfigureerd — wat AI-tools standaard soms doen om te voorkomen dat er tijdens de ontwikkeling iets breekt — kan het uw backend verzoeken laten beantwoorden vanaf overal op het internet.

## Blootstelling van API-sleutels / geheimen

Geen acroniem, maar het hoort op deze lijst thuis omdat het endemisch is in door AI gegenereerde frontends: API-sleutels of geheime credentials die per ongeluk zijn meegeleverd in client-side code, zichtbaar voor iedereen die de ontwikkelaarstools van zijn browser opent. Als een sleutel die alleen op uw server zou moeten leven, terechtkomt in de code die uw browser downloadt, is deze openbaar, punt uit, ongeacht hoe deze elders wordt gebruikt.

## Waarom de acroniemen meer ertoe doen dan ze zouden moeten

Geen van deze termen is ingewikkeld zodra ze zijn uitgelegd. Het probleem is dat AI-codeertools ze zelden proactief aankaarten — ze melden niet "hé, hier wil je misschien RLS" tenzij u er specifiek naar vraagt, en de meeste oprichters weten niet dat ze ernaar moeten vragen. Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, zegt het onomwonden: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. We hebben elf jaar ervaring in precies dat." De vocabulaire kennen maakt u niet technisch — het stelt u in staat om de juiste vraag te stellen voordat een gat een lek wordt.

De technici van LaunchStudio, werkzaam vanuit onder meer Amsterdam, doorlopen precies deze checklist — RLS, RBAC, JWT-afhandeling, CORS-configuratie en blootstelling van credentials — bij elke prototypebeoordeling. Als u een rondleiding door uw eigen app wilt in dezelfde gewone taal, [boek dan een gratis intakegesprek van 15 minuten](https://launchstudio.eu/en/#contact) en wij vertellen u welke van deze vijf termen daadwerkelijk op uw codebase van toepassing zijn. Voor een diepere blik op hoe deze principes opschalen naar enterprise-grade builds, zie [Manifera's bedrijfsachtergrond](https://www.manifera.com/about-us/).

## Echt voorbeeld

### Een AI-native oprichter in actie: de term die hij nog nooit had gehoord

Thijs Overmars, een oprichter uit Tilburg, bouwde "FactuurGrip," een facturatietool voor freelancers, met Bolt. Tijdens een gesprek met een potentiële technische adviseur vroeg de adviseur of FactuurGrip "RLS ingesteld had." Thijs wist niet waar RLS voor stond, laat staan of zijn app het had, en zei dat eerlijk. De adviseur stelde voor het te laten controleren.

Het bleek dat FactuurGrip het niet had — en het gat was precies het soort dat RLS moet dichten. Elke ingelogde klant kon de facturen van een andere klant bekijken door simpelweg een URL-parameter naar een andere factuur-ID te veranderen. Er was geen regel op databaseniveau die het verzoek tegenhield; de frontend construeerde URL's gewoon niet normaal gesproken op die manier, waardoor het bij elk regulier gebruik van de app veilig leek, terwijl het wagenwijd openstond voor iedereen die het probeerde.

De technici van LaunchStudio implementeerden rijniveaubeveiligingsbeleid rechtstreeks op de databaselaag, zodat factuurrecords nu zijn afgebakend tot het geauthenticeerde account, ongeacht welke ID in het verzoek voorkomt. Ze doorzochten ook de overige datatabellen van FactuurGrip op hetzelfde ontbrekende patroon en dichtten twee bijkomende gevallen voordat deze op dezelfde manier ontdekt konden worden als het eerste.

**Resultaat:** Elke datatabel in FactuurGrip handhaaft nu controles op rijniveau-eigendom rechtstreeks in de database zelf, onafhankelijk van wat de frontend ervoor kiest weer te geven.

> *"Ik wist niet eens wat ik moest googelen. Zodra iemand RLS in gewone taal uitlegde, besefte ik dat ik een bescherming had aangenomen die simpelweg niet bestond."*
> — **Thijs Overmars, oprichter, FactuurGrip (Tilburg)**

**Kosten en tijdlijn:** € 800 (implementatie van rijniveaubeveiliging voor alle tabellen) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Wat is het belangrijkste acroniem om te begrijpen vóór een beveiligingsbeoordeling?

RLS (Row-Level Security) — het meest voorkomende gat dat LaunchStudio vindt in door AI gegenereerde apps, en het begrijpen ervan helpt u te vragen of uw database daadwerkelijk gegevenseigendom afdwingt, niet alleen uw frontend.

### Is RBAC hetzelfde als RLS?

Nee. RBAC bepaalt wat verschillende typen gebruikers *mogen doen* (rollen en rechten), terwijl RLS bepaalt welke specifieke *rijen* data een gebruiker kan zien of wijzigen, ongeacht zijn rol.

### Waarom zouden mijn API-sleutels blootgesteld raken als ik ze zelf nooit in de frontend heb geschreven?

AI-codeertools plaatsen credentials soms standaard in client-toegankelijke code tijdens het scaffolden, vooral vroeg in een project, en het is makkelijk te missen tenzij iemand specifiek de gepubliceerde code controleert.

### Controleert het team van Herre Roelevink deze problemen persoonlijk?

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, heeft de beoordelingsnormen van het bedrijf gebouwd rond precies dit soort architectuur- en beveiligingsgat, en het in Amsterdam gevestigde engineeringteam past die norm toe op elke beoordeling.

### Moet ik deze termen leren om een beveiligingsbewust startup te runnen?

U hoeft de code niet zelf te schrijven, maar het herkennen van termen als RLS, RBAC, JWT en CORS stelt u in staat scherpere vragen te stellen en te beoordelen of een review daadwerkelijk dekte wat ertoe doet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the single most important acronym to understand before a security review?", "acceptedAnswer": { "@type": "Answer", "text": "RLS (Row-Level Security) is the most common gap found in AI-generated apps, controlling whether the database itself enforces data ownership." } },
    { "@type": "Question", "name": "Is RBAC the same thing as RLS?", "acceptedAnswer": { "@type": "Answer", "text": "No. RBAC controls what different user roles can do, while RLS controls which specific rows of data a user can access." } },
    { "@type": "Question", "name": "Why would my API keys end up exposed if I never wrote them into the frontend myself?", "acceptedAnswer": { "@type": "Answer", "text": "AI coding tools sometimes place credentials in client-accessible code by default during scaffolding, and it's easy to miss without a specific check." } },
    { "@type": "Question", "name": "Does Herre Roelevink's team check for these issues personally?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio's review standards, shaped by CEO Herre Roelevink, are applied by the Amsterdam-based engineering team to every project review." } },
    { "@type": "Question", "name": "Do I need to learn these terms to run a security-conscious startup?", "acceptedAnswer": { "@type": "Answer", "text": "Not to write code yourself, but recognizing terms like RLS, RBAC, JWT, and CORS helps you ask sharper questions during any review." } }
  ]
}
</script>
