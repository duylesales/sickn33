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
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/acronym-cheat-sheet-security-review" }
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

De technici van LaunchStudio, werkzaam vanuit onder meer Amsterdam, doorlopen precies deze checklist — RLS, RBAC, JWT-afhandeling, CORS-configuratie en blootstelling van credentials — bij elke prototypebeoordeling. Als u een rondleiding door uw eigen app wilt in dezelfde gewone taal, [boek dan een gratis intakegesprek van 15 minuten](https://launchstudio.eu/nl/#contact) en wij vertellen u welke van deze vijf termen daadwerkelijk op uw codebase van toepassing zijn. Voor een diepere blik op hoe deze principes opschalen naar enterprise-grade builds, zie [Manifera's bedrijfsachtergrond](https://www.manifera.com/about-us/).

## Nog Vijf Termen Die U Zult Horen Tijdens een Vervolggesprek

De vijf termen die eerder zijn besproken, dekken de basis af die in vrijwel elk verkennend gesprek naar voren komt. Zodra een technische audit echter dieper gaat — of wanneer er een kwetsbaarheid is aangetroffen en u samen met technici aan hersteloplossingen werkt — duiken onvermijdelijk de volgende vijf concepten op. Hier is de uitleg in gewone mensentaal, zonder jargon:

**IDOR — Insecure Direct Object Reference.** Dit is de formele beveiligingsterm voor het ontbreken van autorisatiecontroles: een kwetsbaarheid waarbij een gebruiker toegang krijgt tot een database-record simpelweg door het record-ID in de URL of het API-verzoek te raden of te wijzigen. Zegt een engineer "dit eindpunt is kwetsbaar voor IDOR", dan bedoelt men exact het probleem waarbij Klant A de facturen van Klant B kan inzien door `/factuur/101` aan te passen naar `/factuur/102`.

**Rate Limiting.** Dit reguleert hoeveel verzoeken een individuele gebruiker of IP-adres binnen een bepaalde tijdspanne mag uitvoeren. Zonder rate limiting kan een kwaadwillend script uw inlogscherm, registratieformulier of API duizenden keren per minuut bestoken — wat leidt tot torenhoge serverkosten, een overbelaste database of succesvolle brute-force wachtwoordaanvallen. AI-codeertools configureren dit zelden standaard, omdat een lokale ontwikkeldemo immers nooit met duizenden verzoeken tegelijk wordt getest.

**Webhook Signature Verification.** Wanneer uw applicatie statusupdates ontvangt van externe platforms (zoals Stripe, Mollie of SendGrid) via een webhook, controleert 'signature verification' of het inkomende bericht daadwerkelijk afkomstig is van die partij. Zonder deze cryptografische handtekeningcontrole kan iedereen een nep-verzoek naar uw webhook-URL sturen met de melding "betaling geslaagd", waarna uw systeem onterecht betaalde toegang verleent.

**ORM — Object-Relational Mapping.** De softwarelaag die de programmeertaal van uw applicatie vertaalt naar database-query's (zoals Prisma, Drizzle of TypeORM). Dit is cruciaal omdat een goed geconfigureerde ORM gevaarlijke database-aanvallen (zoals SQL-injectie) nagenoeg onmogelijk maakt, terwijl ruwe, handgeschreven SQL-query's die om de ORM heen werken dit risico direct herintroduceren als ze niet uiterst zorgvuldig zijn opgesteld.

**Least Privilege (Minimale Bevoegdheden).** Geen specifieke tool, maar een fundamenteel beveiligingsprincipe: elk onderdeel van uw infrastructuur — een database-gebruiker, een API-sleutel of een microservice — mag uitsluitend beschikken over de minimale rechten die strikt noodzakelijk zijn om zijn taak uit te voeren. Een backend die met volledige beheerdersrechten (zoals `postgres` superuser) verbindt met de database, schendt dit principe en maakt van een klein softwarelek een catastrofale inbreuk.

Met deze vijf begrippen op zak verandert een technisch vervolggesprek van een eenzijdige lezing in een constructieve dialoog, waardoor u als oprichter gefundeerde beslissingen kunt nemen.


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
    {
      "@type": "Question",
      "name": "Wat is het belangrijkste acroniem om te begrijpen vóór een beveiligingsbeoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RLS (Row-Level Security) — het meest voorkomende gat dat LaunchStudio vindt in door AI gegenereerde apps, en het begrijpen ervan helpt u te vragen of uw database daadwerkelijk gegevenseigendom afdwingt, niet alleen uw frontend."
      }
    },
    {
      "@type": "Question",
      "name": "Is RBAC hetzelfde als RLS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. RBAC bepaalt wat verschillende typen gebruikers *mogen doen* (rollen en rechten), terwijl RLS bepaalt welke specifieke *rijen* data een gebruiker kan zien of wijzigen, ongeacht zijn rol."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zouden mijn API-sleutels blootgesteld raken als ik ze zelf nooit in de frontend heb geschreven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI-codeertools plaatsen credentials soms standaard in client-toegankelijke code tijdens het scaffolden, vooral vroeg in een project, en het is makkelijk te missen tenzij iemand specifiek de gepubliceerde code controleert."
      }
    },
    {
      "@type": "Question",
      "name": "Controleert het team van Herre Roelevink deze problemen persoonlijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, heeft de beoordelingsnormen van het bedrijf gebouwd rond precies dit soort architectuur- en beveiligingsgat, en het in Amsterdam gevestigde engineeringteam past die norm toe op elke beoordeling."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik deze termen leren om een beveiligingsbewust startup te runnen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U hoeft de code niet zelf te schrijven, maar het herkennen van termen als RLS, RBAC, JWT en CORS stelt u in staat scherpere vragen te stellen en te beoordelen of een review daadwerkelijk dekte wat ertoe doet."
      }
    }
  ]
}
</script>
