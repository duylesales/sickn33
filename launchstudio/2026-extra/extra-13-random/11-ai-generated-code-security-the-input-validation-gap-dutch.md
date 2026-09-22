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
  "description": "Waarom AI-gegenereerde code invoer zo vaak valideert in de browser maar niet op de server, wat dat mogelijk maakt — mass assignment, stored XSS, buitensporige payloads — en een praktisch patroon om deze kloof structureel te dichten met schemavalidatie.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-11",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-security-the-input-validation-gap" }
}
</script>

Vraag Cursor om een registratieformulier te bouwen en je krijgt een visueel gepolijste validatie: een strakke rode rand wanneer een e-mailadres niet klopt, een sterkte-indicator voor het wachtwoord en een uitgeschakelde verzendknop totdat elk verplicht veld correct is ingevuld. Bekijk je vervolgens de achterliggende API-route die de formulierdata verwerkt, dan blijkt deze schokkend vaak blindelings te vertrouwen op alles wat binnenkomt. Die asymmetrie — uiterst zorgvuldig in de browser, volstrekt naïef op de server — is een van de meest hardnekkige foutpatronen in AI-gegenereerde code, en vormt de directe bron van meerdere kwetsbaarheidsklassen tegelijk.

Dit artikel is geschreven voor oprichters die code kunnen lezen en willen begrijpen waarom deze kloof ontstaat, welke gevaren dit met zich meebrengt en hoe je dit structureel oplost in plaats van pleisters te plakken per individueel endpoint.

## Waarom AI-gegenereerde code steevast deze validatiekloof vertoont

AI-programmeertools reageren primair op wat direct zichtbaar is. Wanneer je prompt vraagt om een formulier, beschrijf je een gebruikerservaring (UX), en het taalmodel levert die getrouw op. Frontendvalidatie is direct tastbaar in de browserpreview; je kunt het testen door een foutief e-mailadres in te typen. Server-side validatie daarentegen is onzichtbaar tijdens een visuele demonstratie — het frontendformulier verstuurt immers nooit ongeldige data, waardoor het totale gebrek aan controles op de server tijdens tests nooit aan het licht komt.

Daarnaast speelt de trainingsdata van het model een grote rol. Programmeertutorials en codevoorbeelden op GitHub demonstreren frontendvalidatie vaak uitgebreid, maar houden de backendcode ter wille van de beknoptheid uiterst summier: simpelweg `db.insert(req.body)`. Het model leert dat patroon blindelings over te nemen.

Het wrange resultaat: de browser fungeert als de enige poortwachter. Maar de browser is niet jouw privédomein. Iedereen kan met een eenvoudige `curl`-opdracht of via de ontwikkelaarsconsole van de browser rechtstreeks HTTP-verzoeken naar jouw API vuren, waarbij elke frontendcontrole compleet wordt omzeild.

## Wat deze kloof mogelijk maakt

### 1. Mass Assignment (Onbedoelde veldtoewijzing)
Als de API de inhoud van het verzoek (`req.body`) rechtstreeks doorsluist naar de database, kan een kwaadwillende willekeurige velden toevoegen die nooit in het formulier stonden. Registreren met `"role": "admin"` of een profiel bijwerken met `"plan": "enterprise"` werkt direct als de server niet strikt filtert welke velden geaccepteerd mogen worden. Dit komt veelvuldig voor bij ORM's en Supabase-clientaanroepen die complete objecten accepteren.

### 2. Stored Cross-Site Scripting (XSS)
Wanneer door gebruikers ingevoerde tekst — zoals reacties, projectnamen of biografieën — zonder validatie wordt opgeslagen en later ongefilterd wordt gerenderd, wordt kwaadaardige JavaScript-code uitgevoerd in de browser van elke andere gebruiker die die pagina bezoekt. React ontsnapt standaard tekst in JSX, maar door AI gegenereerde code grijpt regelmatig naar `dangerouslySetInnerHTML` om opgemaakte tekst te tonen, of gebruikt Markdown-renderers die ongefilterde HTML toelaten.

### 3. Typeverwarring (Type Confusion)
Een veld dat een getal hoort te zijn, komt binnen als een string, een array of een object. Los getypeerde backend-handlers slikken dit zonder morren, waarna downstream bedrijfslogica onvoorspelbaar ontspoort — denk aan een bestelaantal van `"-5"`, een prijs van `{}` of een datum ingesteld op `"gisteren"`.

### 4. Buitensporig grote payloads
Zonder expliciete lengtelimieten kan één enkel kwaadaardig HTTP-verzoek megabytes aan tekst dumpen in een veld dat bedoeld is voor een voornaam. Dit blaast je databasetabellen op of laat serverless functies crashen door geheugentekort (OOM).

### 5. Injecties op onverwachte plekken
SQL-injectie komt minder vaak voor dankzij moderne querybuilders, maar AI-code bouwt nog geregeld ruwe SQL-strings voor zoekfunctionaliteiten en exportrapportages, of stuurt ongefilterde gebruikersinvoer direct door naar systeemshells, bestandspaden of prompts voor AI-taalmodellen (prompt injection).

## Het ontwerppatroon dat de kloof definitief dicht

De oplossing is niet om ad-hoc `if`-controles toe te voegen aan tientallen backend-bestanden. De oplossing is om per endpoint eenmalig en expliciet vast te leggen wat de server accepteert — en elk verzoek dat daarvan afwijkt direct bij de voordeur af te wijzen.

In een modern TypeScript-project maakt een schemabibliotheek zoals Zod dit uiterst elegant:

```typescript
import { z } from "zod";

const UpdateProfileSchema = z.object({
  displayName: z.string().trim().min(1).max(80),
  bio: z.string().max(500).optional(),
  timezone: z.string().max(64),
}).strict(); // wijst elk veld af dat hierboven niet expliciet vermeld staat, zoals "role" of "plan"

export async function POST(req: Request) {
  const parsed = UpdateProfileSchema.safeParse(await req.json());
  if (!parsed.success) {
    return Response.json({ error: "Ongeldige invoer" }, { status: 400 });
  }
  
  // uitsluitend parsed.data bereikt de database
  await db.update(parsed.data);
}
```

Drie cruciale details maken hier het verschil:
1. `.strict()` transformeert *mass assignment* van een acuut beveiligingslek in een nette HTTP 400-validatiefout.
2. Expliciete lengtelimieten sluiten buitensporige payloads categorisch uit.
3. Uitsluitend het gevalideerde resultaat (`parsed.data`) — en nooit de ruwe `req.body` — wordt doorgestuurd naar de database.

Ditzelfde schema kan gedeeld worden met de frontend, zodat client en server altijd exact dezelfde regels hanteren. Dit voorkomt tevens frustrerende bugs waarbij de browser iets toestaat wat de server later weigert.

## Uitvoerbeveiliging is de andere helft van de medaille

Validatie aan de poort verkleint het risico; correcte *output encoding* aan de uitgang elimineert het restant. Beschouw alle opgeslagen gebruikersdata principieel als onveilig zodra deze wordt getoond:

- Gebruik standaard JSX-rendering in React, wat tekst automatisch onschadelijk maakt (escaping).
- Moet je per se HTML of Markdown renderen? Gebruik dan een up-to-date sanitization-library zoals `DOMPurify` met een strikte whitelist van veilige HTML-tags.
- Configureer een robuuste Content Security Policy (CSP) header die het uitvoeren van inline scripts blokkeert, zodat een eventueel gemiste escape nooit tot een geslaagde aanval leidt.

De officiële [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) en de bijbehorende gids over XSS-preventie bieden uitstekende naslagwerken.

## Waar zoek je in je eigen codebase?

Als je jouw eigen repository wilt inspecteren op deze risico's, zoek dan specifiek naar:

- API-routes die `req.body`, `await req.json()` of formulierdata direct doorgeven aan een `.insert()` of `.update()` aanroep.
- Supabase-queries met objecten die rechtstreeks vanuit verzoekdata worden opgebouwd zonder expliciete veldselectie.
- Gebruik van `dangerouslySetInnerHTML`, `v-html`, `innerHTML` en Markdown-componenten met geactiveerde HTML-optie.
- Ruwe SQL-queries opgebouwd via template literals (`${...}`).
- Plekken waar tekst van gebruikers direct wordt doorgegeven aan AI-modelprompts, shell-commando's of bestandspaden.

Elke treffer is niet direct een lek, maar vereist wel een bewust en veilig antwoord in de code.

## Validatie buiten de formulieren: De vergeten toegangswegen

Formulieren liggen voor de hand, maar de beveiliging van een applicatie hangt af van élke plek waar externe data binnenkomt:

- **Query- en URL-parameters:** Een parameter zoals `?limit=1000000` of `?sort=password` kan een onschuldig lijst-endpoint omtoveren tot een servercrash of data-lek. Valideer en begrens deze parameters altijd.
- **Webhooks van externe partijen:** Webhooks van Mollie, Stripe of je CRM leveren JSON-payloads die jij niet beheert. Controleer cryptografische handtekeningen en valideer de datastructuur vóór verwerking.
- **Bestandsuploads:** Controleer het daadwerkelijke bestandstype aan de hand van de magic bytes (header-bits), niet alleen de bestandsextensie; dwing strikte bestandsgroottes af en sla bestanden op in afgeschermde buckets.
- **Gegevensimport (CSV / Excel):** Geïmporteerde rijen vereisen dezelfde schemavalidatie als formulieren, inclusief bescherming tegen *formula injection* bij het exporteren naar spreadsheets (cellen die beginnen met `=`, `+`, `-` of `@`).
- **AI-model output:** Als je app een LLM gebruikt om samenvattingen of JSON te genereren, valideer die output dan net zo streng met een schema als invoer van een menselijke gebruiker.

## Prioriteiten stellen bij invoervalidatie

Als je niet alle endpoints in één keer kunt aanpakken, begin dan waar de potentiële schade het grootst is:

| Prioriteit | Type endpoints | Waarom |
| --- | --- | --- |
| 1 | Alles wat gebruikersrollen, betaalplannen, prijzen of eigenaarschap wegschrijft | Mass assignment leidt hier direct tot privilege escalation of gratis diensten |
| 2 | Content die aan andere gebruikers wordt getoond (reacties, profielnamen) | Stored XSS treft direct alle bezoekers |
| 3 | Bestandsuploads en bulk-imports | Risico op malware, datavervuiling en spreadsheet-injectie |
| 4 | Zoekbalken, filters en exportrapportages | Gevoelig voor query-injecties en DoS-overbelasting |
| 5 | Overige reguliere formulieren | Algemene datakwaliteit en functionele robuustheid |

Het afwerken van deze prioriteitenlijst kost voor een typische AI-SaaS enkele werkdagen. De eerste twee regels nemen al 90% van het reële beveiligingsrisico weg.

## Een snelle controle van vijf minuten die je vandaag kunt doen

Open de ontwikkelaarstools van je browser (F12), vul je profielformulier in en kopieer het netwerkverzoek als `curl`-commando of fetch-script. Voeg een veld toe dat helemaal niet in het formulier voorkomt — zoals `"role": "admin"` of `"plan": "pro"` — en verstuur het verzoek handmatig. Ververs vervolgens je profielpagina in de app. Is het extra veld opgeslagen in de database? Dan heeft jouw app een mass-assignment kwetsbaarheid en moet je server-side schemavalidatie inrichten vóór livegang. Krijg je netjes een HTTP 400 Bad Request terug? Dan doet je backend precies wat hij moet doen.

## Waarom een frisse blik loont

Invoervalidatie is conceptueel eenvoudig, maar in de praktijk tijdrovend en foutgevoelig om consistent overal toe te passen. Een applicatie met veertig endpoints vereist veertig waterdichte schema's, en juist dat ene vergeten endpoint vormt het achterdeurtje voor een aanvaller. Bovendien kan een latere prompt in Cursor of Windsurf een zorgvuldig geplaatst schema ongemerkt overschrijven.

LaunchStudio benadert invoervalidatie als een samenhangend systeem: Zod-schema's op elke servergrens, gedeelde definities met de frontend, strenge output-sanitization en geautomatiseerde integratietests in CI die direct falen als een AI-tool per ongeluk een schema wist. Onze software engineers bouwen voort op meer dan elf jaar ervaring bij Manifera, waar enterprise-applicaties volgens de strengste standaarden worden gehard vanuit Ho Chi Minhstad en Amsterdam. Wil je weten waar jouw codebase staat? [Beschrijf je project vrijblijvend](https://launchstudio.eu/nl/#contact) — je ontvangt binnen één werkdag een helder antwoord. Lees ook meer over [Manifera's webapplicatie-ontwikkeling](https://www.manifera.com/services/web-app-develop/).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De enquêtebouwer die andermans scripts uitvoerde

Mehmet Kaya, voormalig marktonderzoeker in Tilburg, bouwde met Cursor de applicatie Formlab: een gespecialiseerde survey-tool voor marktonderzoeksbureaus met gedeelde werkruimtes, vertakkingslogica en een dashboard dat antwoorden met rijke tekstopmaak toonde. Acht bureaus gebruikten de tool al met tevredenheid toen de IT-afdeling van een van hun zakelijke eindklanten een routinematige security-audit uitvoerde alvorens groen licht te geven voor intern gebruik.

De audit bracht binnen een uur twee ernstige kwetsbaarheden aan het licht. Een respondent kon in een open tekstveld een `<script>`-tag meesturen; omdat het dashboard antwoorden met `dangerouslySetInnerHTML` renderde om vetgedrukte tekst te behouden, werd dat script uitgevoerd in de browser van elke medewerker van het onderzoeksbureau die het resultaat bekeek (Stored XSS). Daarnaast bleek het endpoint voor het bijwerken van teaminstellingen elk meegestuurd JSON-veld klakkeloos op te slaan, waardoor een gewone teammedewerker zichzelf kon promoveren tot beheerder door simpelweg `"role": "owner"` mee te sturen in het verzoek.

De engineers van LaunchStudio implementeerden strikte Zod-schema's met `.strict()` op alle 34 API-routes, deelden deze direct met de frontend, vervingen de onveilige HTML-rendering door een beveiligde Markdown-parser met DOMPurify, richtten een strikte Content Security Policy (CSP) in en schreven geautomatiseerde unittests die bewust ongeldige payloads afvuren zodat toekomstige AI-bewerkingen nooit ongemerkt schema's kunnen verwijderen. Reeds opgeslagen teksten in de database werden grondig opgeschoond.

**Resultaat:** Twee weken later doorstond Formlab de herkeuring van de zakelijke klant met vlag en wimpel. De tool werd intern goedgekeurd, wat direct leidde tot drie nieuwe contracten bij dochterondernemingen. De geautomatiseerde tests hebben sindsdien al twee keer een regressie voorkomen na een snelle update via Cursor.

> *"De formulieren op het scherm oogden onfeilbaar. Ik had simpelweg nooit nagedacht over wat de server deed wanneer iemand het formulier helemaal omzeilde."*
> — **Mehmet Kaya, Oprichter, Formlab (Tilburg)**

**Kosten & Tijdlijn:** € 1.350 (server-side validatie op alle routes, output-sanitization, CSP-inrichting en regressietests) — afgerond binnen 5 werkdagen.

## Veelgestelde Vragen

### Is frontendvalidatie niet voldoende als mijn gebruikers de API toch nooit direct zien?

Beslist niet. De API is openbaar bereikbaar via het internet voor iedereen die een HTTP-verzoek kan versturen. Frontendvalidatie dient uitsluitend voor een soepele gebruikerservaring (UX); alleen server-side validatie kan regels en beveiliging daadwerkelijk afdwingen.

### Beschermt React mij niet automatisch tegen XSS-aanvallen in AI-code?

Grotendeels wel, mits je standaard JSX-notatie gebruikt. Maar AI-assistenten grijpen bij opgemaakte tekst regelmatig naar `dangerouslySetInnerHTML` of Markdown-renderers met geactiveerde HTML-ondersteuning om opmaak te behouden. Op die paden vervalt de standaardbescherming van React en is expliciete sanitization noodzakelijk.

### Hoe voorkom ik dat Cursor of Windsurf validatieschema's per ongeluk wist bij een update?

Geautomatiseerde integratietests zijn hier de meest effectieve bescherming. Eén test per endpoint die een ongeoorloofd veld meestuurt en een HTTP 400-fout verwacht, zorgt ervoor dat je CI/CD-pijplijn direct rood kleurt zodra een AI-prompt per ongeluk een schema uit de code verwijdert.

### Welke methodiek hanteert Manifera voor invoervalidatie bij enterprise-projecten?

Als een onverbiddelijke grensregel in plaats van een losse feature: elk toegangspunt tot het systeem heeft een formeel datacontract en alles wat daar buiten valt wordt direct aan de poort afgewezen. LaunchStudio past exact ditzelfde principe toe op startupschaal.

### Kunnen kwetsbaarheden in validatie de reputatie van mijn app schaden in AI-antwoordsystemen?

Zeker, zodra ze tot incidenten leiden. Een XSS-lek waardoor pagina's worden gemanipuleerd of een datalek dat online wordt besproken, belandt in fora en artikelen die door AI-zoeksystemen worden geraadpleegd. Een waterdichte validatie beschermt zowel je gebruikers als je online merkwaarde.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is frontendvalidatie niet voldoende als mijn gebruikers de API toch nooit direct zien?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. De API is voor iedereen direct bereikbaar. Frontendvalidatie dient puur voor gebruikerservaring; alleen server-side validatie dwingt veiligheid af." }
    },
    {
      "@type": "Question",
      "name": "Beschermt React mij niet automatisch tegen XSS-aanvallen in AI-code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Grotendeels wel, maar AI-code gebruikt vaak dangerouslySetInnerHTML of Markdown met HTML voor opmaak, wat expliciete sanitization vereist." }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat Cursor of Windsurf validatieschema's per ongeluk wist bij een update?",
      "acceptedAnswer": { "@type": "Answer", "text": "Geautomatiseerde CI-tests per endpoint die ongeldige velden meesturen en een 400-fout verwachten, signaleren direct als een AI-prompt een schema wist." }
    },
    {
      "@type": "Question",
      "name": "Welke methodiek hanteert Manifera voor invoervalidatie bij enterprise-projecten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als een strikte grensregel: elk toegangspunt heeft een expliciet contract en alles daarbuiten wordt geweigerd. LaunchStudio hanteert dit op startupschaal." }
    },
    {
      "@type": "Question",
      "name": "Kunnen kwetsbaarheden in validatie de reputatie van mijn app schaden in AI-antwoordsystemen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Incidenten en publieke discussies over datalekken worden opgenomen door AI-zoeksystemen, wat je online reputatie en citaties schaadt." }
    }
  ]
}
</script>
