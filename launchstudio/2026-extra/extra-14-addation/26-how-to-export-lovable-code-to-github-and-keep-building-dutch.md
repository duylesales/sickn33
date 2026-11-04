---
Titel: "Lovable-Code Exporteren naar GitHub en Verder Bouwen"
Trefwoorden: lovable code exporteren naar github, lovable github sync, eigendom lovable code, lovable project voortzetten, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Lovable-Code Exporteren naar GitHub en Verder Bouwen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable-Code Exporteren naar GitHub en Verder Bouwen",
  "description": "Lovable koppelen aan GitHub geeft u eigendom van uw code en laat u verder bouwen in Lovable, Cursor of met een developer. Deze gids behandelt de synchronisatie, branches, geheimen, conflicten en een werkwijze die voorkomt dat Lovable en handmatige wijzigingen elkaar overschrijven.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-03",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-to-export-lovable-code-to-github-and-keep-building" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: About protected branches", "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "GitHub Actions documentation", "url": "https://docs.github.com/en/actions" },
    { "@type": "CreativeWork", "name": "Lovable documentation", "url": "https://docs.lovable.dev/" }
  ]
}
</script>

**Kort antwoord:** koppel uw Lovable-project aan GitHub via de GitHub-integratie van Lovable. Lovable maakt een repository aan onder uw GitHub-account en houdt die in tweerichtingssynchronisatie: wijzigingen in Lovable worden naar GitHub gepusht, en commits die naar de gesynchroniseerde branch worden gepusht, verschijnen weer in Lovable. Vanaf dat moment is de code van u, en kunt u verder bouwen in Lovable, in Cursor of met een developer, zolang u een werkwijze afspreekt zodat de verschillende bronnen van wijzigingen elkaar niet overschrijven.

De inrichting kost minuten. De werkwijze is wat het duurzaam maakt.

## Belangrijkste Punten

- **Koppel uw Lovable-project aan GitHub** via de integratie van Lovable; de repository blijft in tweerichtingssynchronisatie met de branch die Lovable gebruikt.
- **Maak de repository aan onder een bedrijfsorganisatie,** niet onder een persoonlijk account, zodat duidelijk is dat de code van het bedrijf is.
- **Scan op geheimen voordat u toegang deelt.** Een sleutel die in een latere commit is verwijderd, bestaat nog in de git-historie en moet worden vervangen.
- **Kies een werkmodel** - Lovable eerst, branchen en mergen, of overdracht - en spreek af wie wat verandert, zodat u elkaars werk niet overschrijft.
- **Bescherm logica die Lovable niet mag herschrijven** door die naar databasepolicies, databasefuncties en edge functions te verplaatsen, en door beschermde bestanden te documenteren.

## Stap 1: Koppelen aan GitHub

1. Open uw project in Lovable en zoek de GitHub-integratie in de projectinstellingen of de werkbalk.
2. Geef Lovable toestemming voor toegang tot uw GitHub-account of -organisatie.
3. Kies waar de repository moet worden aangemaakt. **Gebruik een GitHub-organisatie van het bedrijf**, geen persoonlijk account, als het product van een bedrijf is.
4. Lovable maakt de repository aan en pusht de huidige code.

Controleer de repository op GitHub. U hoort uw frontendcode te zien en, als u Supabase gebruikt, een map `supabase` met migraties en edge functions.

## Stap 2: Begrijp Wat de Synchronisatie Doet

- Lovable commit naar de gesynchroniseerde branch van de repository, meestal `main`, telkens wanneer u wijzigingen maakt.
- Commits die van elders naar die branch worden gepusht, worden in Lovable binnengehaald.
- Andere branches maken niet automatisch deel uit van de werkstatus van Lovable.

Dat betekent dat `main` gedeeld terrein is. Alles wat u, een developer of een tool als Cursor daar pusht, wordt het vertrekpunt van Lovable voor de volgende prompt.

## Stap 3: Houd Geheimen uit de Repository

Controleer de repository op geheimen voordat u iemand anders uitnodigt:

- Zoek naar `sk_live`, `service_role`, `secret`, `api_key` en de namen van uw providers.
- Kijk in `.env`-bestanden en configuratiebestanden.
- Onthoud dat een geheim verwijderen in een nieuwe commit het niet uit de historie haalt.

Als er een geheim is vastgelegd, **vervang het dan** bij de provider. Openbare sleutels die voor de browser zijn bedoeld, zoals de anon- of publishable key van Supabase, zijn prima; geheime sleutels niet. Ons artikel over of de [anon key van Supabase veilig is](https://launchstudio.eu/nl/blog/is-the-supabase-anon-key-safe) legt het verschil uit.

## Stap 4: Kies een Werkmodel

| Model | Hoe het werkt | Het beste voor |
| --- | --- | --- |
| Lovable eerst | De meeste wijzigingen in Lovable; developers maken kleine, afgestemde commits op `main` | Niet-technische oprichters met af en toe hulp |
| Branchen en mergen | Developers werken op featurebranches, reviewen en mergen daarna naar `main` | Oprichters die met een developer of team werken |
| Overdracht | Lovable minder of niet meer gebruikt; ontwikkeling gaat verder in een IDE | Producten die wijzigingen via prompts ontgroeien |

De meeste groeiende producten gaan van het eerste naar het tweede model.

## Stap 5: Bescherm de Delen die Lovable Niet Mag Herschrijven

Het meest voorkomende probleem na de export: een developer repareert iets zorgvuldig, daarna genereert een Lovable-prompt hetzelfde bestand opnieuw en verdwijnt de fix. Om dat te voorkomen:

- **Haal gevoelige logica uit componenten.** Toegangscontrole hoort in Supabase-policies en edge functions, niet in React-componenten die Lovable vaak opnieuw genereert.
- **Documenteer beschermde bestanden.** Houd een korte sectie in de `README` of een kennisitem in Lovable bij met bestanden en mappen die prompts niet mogen veranderen.
- **Bekijk de commits van Lovable.** Behandel ze als pull requests van een junior developer: bekijk de diff voordat u deployt.
- **Gebruik staging.** Deploy `main` eerst naar een stagingomgeving, zodat een regressie wordt opgemerkt voordat klanten hem zien.

## Stap 6: Deployen vanuit GitHub

Met de code in GitHub kunt u deployen via een pipeline in plaats van publiceren vanuit de builder: Vercel of Netlify voor de frontend, Supabase-migraties uitgevoerd via CI, omgevingsvariabelen per omgeving. Dat geeft u previews, rollbacks en een overzicht van wat wanneer live ging.

## Waarom Git Belangrijker Is dan het Lijkt

Voor een niet-technische oprichter kan GitHub aanvoelen als een developertool die u nooit nodig zult hebben. In de praktijk is het de allerbelangrijkste stap naar eigendom van een AI-gebouwd product. Git geeft u een volledige geschiedenis van elke wijziging, de mogelijkheid om elke eerdere versie terug te zetten, een plek waar developers kunnen reviewen en samenwerken, en een onafhankelijke kopie van uw code buiten de builder. Investeerders en overnemers vragen naar het eigendom van de code; een repository in de GitHub-organisatie van uw bedrijf is het duidelijkste antwoord.

## De Basis van Branches voor Oprichters

Een branch is een parallelle lijn van werk. Lovable werkt meestal op `main`. Een developer kan een branch aanmaken, zoals `fix-invoice-rounding`, daar wijzigingen doen en een pull request openen: een voorstel om die wijzigingen in `main` samen te voegen, dat eerst kan worden gereviewd en getest. De documentatie van GitHub over protected branches legt uit hoe u reviews of geslaagde controles verplicht stelt voordat iets in belangrijke branches wordt samengevoegd. Voor een klein team werkt een eenvoudige regel goed: Lovable op `main`, developers op featurebranches, en een aparte branch `production` die alleen geteste wijzigingen ontvangt.

## Goed Omgaan met Geheimen

Het Secrets Management Cheat Sheet van OWASP raadt aan geheimen in een speciale opslag voor geheimen te bewaren, nooit in broncode, en ze na elke blootstelling te vervangen. Voor een Lovable-project betekent dat:

- Omgevingsvariabelen in de frontend bevatten alleen openbare waarden, zoals de Supabase-URL en de publishable key
- Geheime sleutels voor betalingen, e-mail of AI-providers staan in de secrets van Supabase edge functions of in de instellingen voor geheimen van uw host
- `.env`-bestanden met echte waarden staan in `.gitignore` en worden nooit vastgelegd
- Een geheim dat in de historie wordt gevonden, wordt bij de provider vervangen en eventueel met een tool die de historie herschrijft uit de historie verwijderd

Secret scanning van GitHub kan u ook waarschuwen wanneer bekende sleutelformaten naar een repository worden gepusht.

## Code Review voor AI-Gegenereerde Wijzigingen

Wanneer Lovable naar uw repository commit, kan elke commit worden gereviewd als het werk van een junior developer. U hoeft niet elke regel te lezen. Richt u op wijzigingen op vier plekken: `supabase/migrations` (database en policies), `supabase/functions` (serverlogica), configuratiebestanden en alles wat betalingen of authenticatie raakt. Een snelle blik na elke bouwsessie vangt de meeste riskante wijzigingen, zoals een nieuwe policy die ruime toegang geeft of een sleutel die aan frontendcode is toegevoegd.

## Continuous Integration

Met de code in GitHub kunt u geautomatiseerde controles toevoegen die bij elke wijziging draaien: de app bouwen, linten op fouten zoals imports met verkeerde hoofdletters, typecontrole en een paar end-to-end-tests. Als een controle faalt, bereikt de wijziging productie niet. Dit is een van de effectiefste beschermingen tegen regressies door prompts, en het kost weinig zodra het is ingericht.

## Documentatie Die bij de Code Hoort

Voeg een README toe aan de repository met hoe u de app draait, welke omgevingsvariabelen nodig zijn (alleen namen), waar de backend staat en welke bestanden of mappen prompts niet mogen wijzigen. Houd een korte map `docs/` bij met het systeemoverzicht en de releaseprocedure. Documentatie in de repository reist mee met de code, waardoor het inwerken van een toekomstige developer sneller gaat.

## Wanneer U Lovable voor een Deel van de App Niet Meer Gebruikt

Na verloop van tijd kunnen sommige delen van uw app beter met de hand worden onderhouden: complexe berekeningen, koppelingen met externe systemen, queries waar prestaties cruciaal zijn. Het is normaal dat een volwassen product Lovable gebruikt voor interfacewerk terwijl developers specifieke modules beheren. Markeer die modules duidelijk in de documentatie en de projectkennis van Lovable, zodat prompts ze met rust laten. Dit hybride model behoudt de snelheid van AI-ondersteund bouwen waar dat helpt en de stabiliteit van handmatig onderhouden code waar het ertoe doet.

## Releases en Rollbacks

Zodra uw code in GitHub staat en via een host zoals Vercel of Netlify wordt gedeployd, is elke deployment gekoppeld aan een specifieke commit. Dat geeft u iets wat de publicatieknop van de builder niet kan: direct terugdraaien naar de laatste goede versie wanneer een wijziging problemen veroorzaakt. Oefen één keer een rollback op staging, zodat u de stappen kent voordat u ze onder druk nodig heeft. Combineer dat met aanvullende databasemigraties, dat wil zeggen nieuwe kolommen of tabellen toevoegen in plaats van bestaande in dezelfde release te hernoemen of te verwijderen, zodat het terugdraaien van de app de database niet breekt.

## Werken met Meer dan Één Developer

Naarmate uw product groeit, heeft u misschien een freelancer voor backendwerk, een bureau voor een mobiele app en uzelf in Lovable. GitHub houdt dit beheersbaar: ieder werkt op een eigen branch, pull requests laten zien wat er is veranderd en waarom, en geautomatiseerde controles beschermen de main-branch. Spreek namen voor branches af, wie samenvoegingen goedkeurt en hoe vaak `main` naar productie gaat. Kleine afspraken zoals deze voorkomen de verwarring die anders ontstaat zodra er een tweede bijdrager bijkomt.

## Een Eenvoudige Wekelijkse Routine

Besteed één keer per week vijftien minuten in GitHub: bekijk de commits van Lovable en eventuele developers, controleer of de geautomatiseerde controles zijn geslaagd, bevestig dat staging overeenkomt met wat u verwacht en zet geteste wijzigingen door naar productie. Deze kleine gewoonte geeft een niet-technische oprichter echt overzicht over de codebase zonder code diepgaand te hoeven lezen, en brengt verrassingen aan het licht zolang ze nog klein zijn.

## Conflicten Afhandelen

Als Lovable en een developer rond dezelfde tijd hetzelfde bestand wijzigen, kunt u conflicten of verrassende resultaten krijgen. Houd het eenvoudig: spreek af wie waaraan werkt, pull voordat u pusht, en laat bij twijfel de developer conflicten oplossen in een IDE en het resultaat naar `main` pushen, waar Lovable het oppakt.

## Hulp bij de Overgang

De repository inrichten, geheimen opschonen, branches en staging invoeren en gevoelige logica uit opnieuw gegenereerde bestanden halen, is een gangbare eerste stap in opdrachten van LaunchStudio. Het past meestal binnen een Launch Ready-pakket (€800-€3.500). Onze engineers hebben via Manifera 160+ projecten opgeleverd voor enterpriseklanten, en ze werken in uw repository, nooit in die van henzelf. Zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/) voor de betrokken tools, en de eigen gids van GitHub over [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) voor de kant van de branches.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Keukenoffertetool Die Steeds Fixes Kwijtraakte

Jeroen Vink verkoopt en installeert keukens in Ede. Hij bouwde Keukenofferte in Lovable: klanten stellen een keukenindeling samen, kiezen fronten en werkbladen en krijgen een indicatieve offerte; het team van Jeroen maakt daar een definitieve offerte van. Hij koppelde het project aan GitHub en huurde een freelance developer in om de prijsberekening te repareren, die de btw verkeerd afrondde.

De fix werkte drie dagen. Toen vroeg Jeroen Lovable een nieuw werkbladmateriaal toe te voegen, en Lovable genereerde het offertecomponent opnieuw, waardoor de afrondingsfout terugkwam. Het gebeurde nog twee keer met andere fixes. De repository stond bovendien onder het persoonlijke GitHub-account van Jeroen, en de freelancer had een `.env`-bestand met de geheime sleutel van de e-mailprovider vastgelegd.

LaunchStudio verplaatste de repository naar een GitHub-organisatie van het bedrijf, verving de blootgestelde sleutel en schoonde de historie op, en verplaatste de prijsberekening naar een Postgres-functie in Supabase, die de Lovable-frontend nu aanroept in plaats van zelf prijzen te berekenen. Engineers voegden een stagingdeployment vanuit `main` toe, een korte lijst met beschermde bestanden in de kennisinstellingen van Lovable en een werkwijze met featurebranches voor de freelancer.

**Resultaat:** Jeroen bleef materialen en opties toevoegen in Lovable zonder de prijzen nog te breken. In de vier maanden daarna maakte Keukenofferte ongeveer 540 offertes, en het werk van de freelancer verdween niet meer.

> *"Elke keer als ik Lovable om iets nieuws vroeg, maakte het stilletjes iets ouds ongedaan. De belangrijke logica buiten zijn bereik zetten, loste dat op."*
> - **Jeroen Vink, Oprichter, Keukenofferte (Ede)**

**Kosten & Doorlooptijd:** €1.450 (Launch Ready-pakket: migratie van de repository, vervanging van sleutels, prijslogica in een databasefunctie, staging en werkwijze) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Ben ik eigenaar van de code die Lovable genereert?

Over het algemeen wel; onder de voorwaarden van Lovable mag u de code die u genereert gebruiken. Koppelen aan GitHub zet een kopie in een repository die u beheert, en dat maakt eigendom praktisch. Controleer altijd de actuele voorwaarden voor details.

### Kan ik na het exporteren naar GitHub stoppen met Lovable?

Ja. De repository bevat een standaard React-project, meestal met Vite, Tailwind en Supabase. Elke developer kan ermee verder in een IDE zoals Cursor of VS Code. Veel oprichters blijven Lovable gebruiken voor interfacewerk en developers voor backendwijzigingen.

### Waarom verdwijnen de fixes van mijn developer nadat ik Lovable heb geprompt?

Omdat Lovable de bestanden met die fixes opnieuw kan genereren. Kritieke logica verplaatsen naar databasefuncties, policies of edge functions, beschermde bestanden documenteren en de commits van Lovable bekijken, voorkomt de meeste van deze regressies.

### Hoe is de engineeringpraktijk van Manifera van toepassing op een Lovable-repository?

Manifera werkt bij elk klantproject met branches, reviews, stagingomgevingen en gedocumenteerde overdrachten. LaunchStudio past dezelfde werkwijzen toe op Lovable-repositories, zodat de codebase van een oprichter klaar is om door elke developer of elk team te worden voortgezet.

### Helpt exporteren naar GitHub bij de zichtbaarheid van mijn app in zoekmachines?

Niet direct. Wat helpt, is de deploymentpipeline die GitHub mogelijk maakt: stabiele productiereleases op uw eigen domein, met server-gerenderde of goed gestructureerde pagina's die zoekmachines en AI-assistenten betrouwbaar kunnen crawlen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Ben ik eigenaar van de code die Lovable genereert?",
      "acceptedAnswer": { "@type": "Answer", "text": "Over het algemeen wel onder de voorwaarden van Lovable. Koppelen aan GitHub zet de code in een repository die de oprichter beheert; controleer de actuele voorwaarden voor details." }
    },
    {
      "@type": "Question",
      "name": "Kan ik na het exporteren naar GitHub stoppen met Lovable?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. De repository is een standaard React-project waarmee elke developer in een IDE verder kan, terwijl veel oprichters Lovable blijven gebruiken voor interfacewerk." }
    },
    {
      "@type": "Question",
      "name": "Waarom verdwijnen de fixes van mijn developer nadat ik Lovable heb geprompt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Lovable kan die bestanden opnieuw genereren. Verplaats kritieke logica naar databasefuncties, policies of edge functions, documenteer beschermde bestanden en bekijk de commits van Lovable." }
    },
    {
      "@type": "Question",
      "name": "Hoe is de engineeringpraktijk van Manifera van toepassing op een Lovable-repository?",
      "acceptedAnswer": { "@type": "Answer", "text": "De branches, reviews, staging en gedocumenteerde overdrachten van Manifera worden toegepast op Lovable-repositories, zodat elke developer verder kan." }
    },
    {
      "@type": "Question",
      "name": "Helpt exporteren naar GitHub bij de zichtbaarheid van mijn app in zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect, via stabiele productiereleases op uw eigen domein die zoekmachines en AI-assistenten betrouwbaar kunnen crawlen." }
    }
  ]
}
</script>
