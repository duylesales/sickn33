---
Titel: "Beveiliging van AI-gegenereerde code: De kloof in invoervalidatie uitgelegd"
Trefwoorden: beveiliging van ai-gegenereerde code, invoervalidatie, xss in ai-code, cursor beveiliging, ai beveiligingskwetsbaarheden, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Beveiliging van AI-gegenereerde code: De kloof in invoervalidatie uitgelegd

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-gegenereerde code: De kloof in invoervalidatie uitgelegd",
  "description": "Waarom AI-gegenereerde code invoer zo vaak valideert in de browser maar niet op de server, wat dat mogelijk maakt - mass assignment, stored XSS, buitensporige payloads - en een praktisch patroon om deze kloof structureel te dichten met schemavalidatie.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-11",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-security-the-input-validation-gap" }
}
</script>

Vraag Cursor een aanmeldformulier te bouwen en je krijgt verzorgde validatie: een rode rand als het e-mailadres onjuist is, een sterktemeter bij het wachtwoord, een uitgeschakelde verzendknop totdat alles is ingevuld. Kijk naar de API-route die het formulier ontvangt en je ziet heel vaak dat die vertrouwt op wat er ook maar binnenkomt. Die asymmetrie - zorgvuldig in de browser, goedgelovig op de server - is een van de meest consistente patronen in de beveiliging van AI-gegenereerde code, en de bron van meerdere soorten kwetsbaarheden tegelijk.

Dit artikel is voor oprichters die code kunnen lezen en willen begrijpen waarom de kloof bestaat, wat ze mogelijk maakt, en hoe je haar systematisch dichtt in plaats van endpoint voor endpoint.

## Waarom de Beveiliging van AI-Gegenereerde Code Deze Kloof Heeft

AI-codeertools reageren op wat je kunt zien. Wanneer je om een formulier vraagt, beschrijf je een gebruikerservaring, en het model levert er een. Validatie in de frontend is zichtbaar in de preview; je kunt haar testen door een fout e-mailadres te typen. Validatie op de server is onzichtbaar in een demo - de frontend stuurt nooit foute data, dus het ontbreken van controles op de server valt nooit op.

Er is ook een effect van de trainingsdata. Tutorials en voorbeeldrepositories tonen frontendvalidatie vaak uitgebreid en laten de API voor de beknoptheid als minimale handler die "de body in de database opslaat". Het model leert die vorm.

Het resultaat: de browser is de enige poortwachter. Maar de browser is niet van jou. Iedereen kan met een tool als curl of de ontwikkelconsole van de browser rechtstreeks verzoeken naar je API sturen, langs elke controle die de frontend uitvoert.

## Wat de Kloof Mogelijk Maakt

**Mass assignment.** Neemt de API de body van het verzoek en schrijft die rechtstreeks naar de database, dan kan een gebruiker velden toevoegen die het formulier nooit toonde. Aanmelden met `"role": "admin"` of een profiel bijwerken met `"plan": "enterprise"` werkt als de server niet beperkt welke velden worden geaccepteerd. Dit komt vooral veel voor bij ORM's en Supabase-clientaanroepen die hele objecten accepteren.

**Opgeslagen cross-site scripting (XSS).** Wordt gebruikerstekst - een opmerking, een projectnaam, een bio - zonder validatie opgeslagen en later zonder escaping getoond, dan draait een script dat erin staat in de browsers van andere gebruikers. React escapet standaard, maar AI-gegenereerde code gebruikt vaak `dangerouslySetInnerHTML` om opgemaakte tekst te tonen, of geeft inhoud door aan Markdown-renderers die zijn ingesteld om ruwe HTML toe te staan.

**Typeverwarring.** Een veld dat een getal hoort te zijn, komt binnen als tekst, array of object. Losjes getypeerde handlers accepteren het, en logica verderop gedraagt zich onvoorspelbaar - een aantal van `"-5"`, een prijs van `{}`, een datum van `"gisteren"`.

**Te grote payloads.** Zonder groottelimieten kan één verzoek megabytes aan tekst in een veld voor een naam stoppen, waardoor de database opzwelt of een functie die het verwerkt crasht.

**Injectie op minder voor de hand liggende plekken.** SQL-injectie is zeldzamer met moderne ORM's, maar AI-gegenereerde code bouwt nog steeds ruwe query's voor zoek- en rapportagefuncties, en geeft gebruikersinvoer door aan shellcommando's, bestandspaden of prompts die naar taalmodellen gaan.

## Het Patroon Dat Haar Dicht

De oplossing is niet om controles over elke handler te strooien. Het is om per endpoint één keer precies te definiëren wat de server accepteert - en al het andere te weigeren voordat er logica draait.

In een TypeScript-stack maakt een schemabibliotheek zoals Zod dit beknopt:

```typescript
import { z } from "zod";

const UpdateProfile = z.object({
  displayName: z.string().trim().min(1).max(80),
  bio: z.string().max(500).optional(),
  timezone: z.string().max(64),
}).strict(); // weigert elk veld dat niet is opgenomen, zoals "role" of "plan"

export async function POST(req: Request) {
  const parsed = UpdateProfile.safeParse(await req.json());
  if (!parsed.success) {
    return Response.json({ error: "Invalid input" }, { status: 400 });
  }
  // alleen parsed.data bereikt de database
}
```

Drie details doen ertoe. `.strict()` maakt van mass assignment een validatiefout in plaats van een kwetsbaarheid. Lengtelimieten vangen te grote payloads af. En alleen het geparste resultaat - nooit de ruwe body - wordt doorgegeven.

Hetzelfde schema kan met de frontend worden gedeeld zodat beide kanten het eens zijn, wat ook een soort bugs wegneemt waarbij de browser iets toestaat dat de server later weigert.

## Uitvoer Is de Andere Helft

Validatie bij invoer verkleint het risico; escaping bij uitvoer neemt het weg. Behandel opgeslagen gebruikerstekst, ook met goede validatie, als onbetrouwbaar overal waar ze wordt getoond:

- Geef de voorkeur aan gewone JSX-weergave, die standaard escapet.
- Moet je HTML of Markdown tonen, schoon die dan op met een onderhouden bibliotheek zoals DOMPurify en een strikte lijst toegestane tags.
- Stel een Content Security Policy-header in die inline scripts blokkeert, zodat een gemiste escaping geen werkende aanval wordt.

Het [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) en de bijbehorende cheat sheet over het voorkomen van XSS zijn beknopte, praktische referenties.

## Waar Je Kijkt in Je Eigen Codebase

Wil je dit zelf controleren, zoek dan naar:

- API-handlers die `req.body`, `await req.json()` of formulierdata rechtstreeks doorgeven aan een insert- of update-aanroep.
- Supabase-aanroepen `.insert()` of `.update()` met objecten die zijn opgebouwd uit verzoekdata zonder specifieke velden te kiezen.
- `dangerouslySetInnerHTML`, `v-html`, `innerHTML` en Markdown-renderers met HTML aan.
- Ruwe SQL-strings gebouwd met template literals.
- Elke plek waar gebruikersinvoer wordt doorgegeven aan een prompt voor een AI-model, een shellcommando of een bestandspad.

Niet elke treffer is noodzakelijk een kwetsbaarheid, maar elke treffer vraagt een bewust antwoord.

## Validatie Voorbij Formulieren: De Andere Ingangen

Formulieren zijn de voor de hand liggende plek voor validatie, maar de beveiliging van AI-gegenereerde code hangt af van elke grens waar externe data binnenkomt. Verschillende daarvan worden makkelijk over het hoofd gezien:

- **Queryparameters en routeparameters.** Een `?limit=1000000` of `?sort=password` kan van een onschuldig lijst-endpoint een probleem met prestaties of blootstelling van data maken. Valideer ze en stel een maximum in.
- **Webhooks van derden.** Webhooks voor betalingen, e-mail en CRM leveren JSON die jij niet hebt geschreven. Controleer handtekeningen en valideer de vorm voordat je velden vertrouwt.
- **Bestandsuploads.** Controleer het werkelijke inhoudstype (magic bytes), niet de extensie; dwing groottelimieten af; sla privé op; verwijder metadata.
- **Imports (CSV, Excel).** Geïmporteerde rijen hebben dezelfde schemavalidatie nodig als formuliervelden - plus bescherming tegen formule-injectie wanneer de data later naar spreadsheets wordt geëxporteerd (cellen die beginnen met `=`, `+`, `-` of `@`).
- **Headers en cookies.** Waarden als `X-Forwarded-For` of eigen headers worden door de aanvaller beheerd, tenzij je infrastructuur ze instelt.
- **Uitvoer van AI-modellen.** Gebruikt je app een model om tekst of gestructureerde data te maken, valideer die uitvoer dan net zo streng als gebruikersinvoer voordat je haar opslaat of ernaar handelt.

## Een Schemastrategie Die Meeschaalt

Met veertig endpoints moet validatie systematisch zijn, anders loopt ze uit de pas. Een structuur die goed werkt in TypeScript-projecten:

1. **Eén schemabestand per domein** (`schemas/booking.ts`, `schemas/profile.ts`) dat schema's exporteert voor aanmaken, bijwerken en opvragen.
2. **Gedeeld tussen client en server**, zodat formulieren dezelfde regels gebruiken die de API afdwingt.
3. **Een wrapper voor route-handlers** die invoer met het schema parset en bij een fout een consistent 400-antwoord geeft, zodat geen enkele handler het kan vergeten.
4. **Een lint- of CI-controle** die faalt als een route-handler `req.json()` leest zonder via de wrapper te gaan.
5. **Weigeringstests** per endpoint: één test stuurt een extra veld, één stuurt een verkeerd type.

Met dit op zijn plek wordt een endpoint zonder validatie toevoegen moeilijker dan er een met validatie toevoegen - precies de eigenschap die je wilt wanneer een AI-tool nieuwe handlers genereert.

## Uitvoer Coderen in Verschillende Contexten

Escaping hangt af van de context, en daarom is "we escapen gebruikersinvoer" vaak maar deels waar. Tekst in HTML heeft HTML-escaping nodig; in een attribuut attribuut-escaping; in een URL URL-codering; in JavaScript JSON-codering; in SQL parametrisering; in een shellcommando helemaal vermijden. Frameworks regelen het eerste geval goed. De meeste echte bugs in AI-gebouwde apps zitten in de andere: een door de gebruiker opgegeven URL in een `href` zonder controle van het schema (waardoor `javascript:`-links mogelijk zijn), een naam in een e-mailsjabloon zonder escaping, een zoekterm die voor een "snel" rapport aan een SQL-string wordt geplakt.

## Hoe Je Validatiewerk Prioriteert

Kun je niet alles tegelijk oplossen, begin dan waar de schade het grootst zou zijn:

| Prioriteit | Endpoints | Waarom |
| --- | --- | --- |
| 1 | Alles wat rollen, abonnementen, prijzen of eigenaarschap schrijft | Mass assignment betekent hier rechtenescalatie of gratis dienstverlening |
| 2 | Inhoud die aan andere gebruikers wordt getoond (opmerkingen, namen, beschrijvingen) | Opgeslagen XSS raakt iedereen die het bekijkt |
| 3 | Uploads en imports | Malware, te grote bestanden, formule-injectie |
| 4 | Zoeken, filters en rapporten | Injectie en misbruik van prestaties |
| 5 | Overige formulieren | Datakwaliteit en robuustheid |

Deze lijst afwerken kost voor een typische AI-gebouwde SaaS een paar dagen, en alleen al de eerste twee rijen halen het grootste deel van het ernstige risico weg.

## Validatiefouten Die AI-Tools Maken, Ook Als Je Erom Vraagt

Je AI-tool vragen "validatie toe te voegen" levert vaak iets op dat goed lijkt maar gaten heeft. Let op deze: schema's die valideren maar nooit op de server worden aangeroepen; `.passthrough()` of vergelijkbare opties die onbekende velden toestaan; validatie van het object op het hoogste niveau maar niet van geneste arrays; lengtelimieten op tekst maar geen limiet op het aantal items in een lijst; numerieke velden die negatieve waarden of decimalen accepteren waar alleen positieve gehele getallen zinvol zijn; en validatie van e-mailadressen of URL's met losse reguliere expressies die bijna alles accepteren.

Een nuttige reviewvraag bij elk door AI gegenereerd schema is: "wat is de slechtste geldige invoer die dit accepteert?" Is het antwoord "een beschrijving van 50 MB", "een aantal van −5" of "een URL die begint met javascript:", dan moet het schema worden aangescherpt. Koppel elk schema aan minstens één test die zulke slechtst denkbare invoer stuurt en een weigering verwacht. Die gewoonte, meer dan welke keuze van bibliotheek ook, voorkomt dat invoervalidatie stilletjes afbrokkelt terwijl je AI-gegenereerde code blijft veranderen.

## Een Controle van Vijf Minuten Die Je Vandaag Kunt Doen

Open de ontwikkeltools van je browser, verstuur je profielformulier, en kopieer het verzoek als fetch- of curl-commando. Voeg een veld toe dat het formulier niet heeft - `"role": "admin"` of `"plan": "pro"` - en verstuur het opnieuw. Laad daarna je profiel opnieuw. Is het extra veld opgeslagen, dan heeft je app een gat in mass assignment en heb je vóór de lancering schema's op de server nodig. Werd het verzoek geweigerd met een duidelijk 400-antwoord, dan doet de grens haar werk. Herhaal de test voor de twee of drie formulieren die het meest uitmaken: aanmelden, profiel, en alles wat betalingen of rechten raakt.

## Waarom Dit een Tweede Paar Ogen Waard Is

Invoervalidatie is makkelijk te begrijpen en saai om consequent toe te passen. Een app met veertig endpoints heeft veertig schema's nodig, en het schema dat je vergeet, is het schema dat ertoe doet. Het is ook het soort fix dat AI-tools ongedaan kunnen maken: genereer een handler opnieuw en het schema verdwijnt misschien stilletjes.

De review van LaunchStudio behandelt validatie als systeem: een schema op elke servergrens, een gedeelde definitie met de frontend, opschonen van uitvoer waar HTML wordt getoond, en een CSP-header als vangnet - plus een kleine test per endpoint die een niet-toegestaan veld stuurt en een weigering verwacht, zodat terugvallen in CI worden opgevangen. De engineering komt van Manifera, dat al meer dan elf jaar webapplicaties voor enterpriseklanten versterkt vanuit het ontwikkelcentrum aan de Pho Quang-straat in Ho Chi Minh-stad en de kantoren in Amsterdam en Singapore; de oprichter van Manifera begon zijn loopbaan zelf in cybersecurity. Wil je die controle op je codebase, [beschrijf dan je project](https://launchstudio.eu/nl/#contact) en je hoort binnen een werkdag van ons. De praktijk [webappontwikkeling](https://www.manifera.com/services/web-app-develop/) van Manifera past dezelfde standaarden op grotere schaal toe.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Enquêtetool Die de Scripts van Anderen Draaide

Mehmet Kaya, voormalig marktonderzoeksanalist in Tilburg, bouwde Formlab met Cursor: een enquêtetool voor kleine onderzoeksbureaus, met gedeelde werkruimtes, vraaglogica en een resultatendashboard dat opgemaakte antwoorden toonde. Acht bureaus betaalden ervoor toen het IT-team van een van hun klanten een routinematige beveiligingscontrole uitvoerde voordat het de tool voor intern gebruik goedkeurde.

De controle vond binnen een uur twee problemen. Een respondent kon een antwoord met een scripttag insturen; omdat het resultatendashboard antwoorden met `dangerouslySetInnerHTML` toonde om de opmaak te behouden, draaide het script in de browser van elke bureaumedewerker die de resultaten bekeek. En het endpoint om een werkruimte bij te werken accepteerde elk veld dat werd meegestuurd, zodat een lid van een werkruimte zichzelf tot eigenaar kon promoveren door `"role": "owner"` aan een verzoek toe te voegen.

De engineers van LaunchStudio voegden Zod-schema's in strikte modus toe aan alle 34 API-routes, deelden die schema's met de frontend, vervingen de ruwe HTML-weergave door een opgeschoonde Markdown-renderer die beperkt is tot basisopmaak, voegden een Content Security Policy toe die inline scripts blokkeert, en schreven per route een weigeringstest, zodat CI faalt als een toekomstige bewerking door Cursor een schema verwijdert. Bestaande opgeslagen antwoorden werden gescand en opgeschoond.

**Resultaat:** Formlab doorstond twee weken later de vervolgcontrole van de klant en werd goedgekeurd voor intern gebruik - wat ertoe leidde dat drie zusterbedrijven van die klant een abonnement namen. De CI-tests hebben sindsdien twee terugvallen opgevangen die door AI-gegenereerde bewerkingen waren geïntroduceerd.

> *"De formulieren leken waterdicht. Ik heb alleen nooit gekeken wat de server deed als iemand het formulier helemaal oversloeg."*
> - **Mehmet Kaya, Oprichter, Formlab (Tilburg)**

**Kosten & Tijdlijn:** € 1.350 (validatie op de server over alle routes, opschonen van uitvoer, CSP en regressietests) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Is validatie in de frontend niet genoeg als mijn gebruikers de API nooit zien?

Nee. De API is voor iedereen bereikbaar, of je interface ernaar linkt of niet. Validatie in de frontend verbetert de gebruikerservaring; alleen validatie op de server dwingt regels af.

### Beschermt React mij tegen XSS in AI-gegenereerde code?

Gedeeltelijk. React escapet inhoud die normaal wordt getoond, maar AI-tools omzeilen dat vaak met `dangerouslySetInnerHTML` of Markdown met HTML aan om de opmaak te behouden. Die paden hebben expliciete opschoning nodig.

### Hoe voorkom ik dat Cursor validatie verwijdert wanneer het code opnieuw genereert?

Tests zijn de betrouwbaarste bewaking. Een kleine test per endpoint die een ongeldig of extra veld stuurt en een 400-antwoord verwacht, faalt in CI als het schema verdwijnt. Projectregels die Cursor vragen schema's te behouden helpen, maar worden niet afgedwongen.

### Hoe pakt Manifera invoervalidatie aan bij enterpriseprojecten?

Als grensregel in plaats van als taak per functie: elke ingang van het systeem heeft een expliciet contract, en alles daarbuiten wordt geweigerd. LaunchStudio past hetzelfde principe toe op apps van oprichters, afgestemd op hun omvang.

### Kunnen validatieproblemen de reputatie van mijn app in AI-zoekresultaten schaden?

Ja, als ze tot incidenten leiden. Een opgeslagen XSS-aanval die pagina's beschadigt of een datalek waarover publiekelijk wordt gesproken, wordt onderdeel van wat AI-antwoordmachines over je product ophalen. Incidenten voorkomen beschermt je zichtbaarheid én je gebruikers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is validatie in de frontend niet genoeg als mijn gebruikers de API nooit zien?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. De API is voor iedereen bereikbaar. Validatie in de frontend helpt de gebruikerservaring; alleen validatie op de server dwingt regels af." }
    },
    {
      "@type": "Question",
      "name": "Beschermt React mij tegen XSS in AI-gegenereerde code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gedeeltelijk. React escapet normale weergave, maar AI-tools gebruiken vaak dangerouslySetInnerHTML of Markdown met HTML, wat expliciete opschoning vraagt." }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat Cursor validatie verwijdert wanneer het code opnieuw genereert?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voeg per endpoint een test toe die ongeldige of extra velden stuurt en een weigering verwacht, zodat CI faalt als een schema verdwijnt." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera invoervalidatie aan bij enterpriseprojecten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als grensregel: elke ingang heeft een expliciet contract en alles daarbuiten wordt geweigerd. LaunchStudio past dit toe op apps van oprichters." }
    },
    {
      "@type": "Question",
      "name": "Kunnen validatieproblemen de reputatie van mijn app in AI-zoekresultaten schaden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, als ze leiden tot incidenten waarover publiekelijk wordt gesproken, omdat AI-antwoordmachines die informatie over je product ophalen." }
    }
  ]
}
</script>
