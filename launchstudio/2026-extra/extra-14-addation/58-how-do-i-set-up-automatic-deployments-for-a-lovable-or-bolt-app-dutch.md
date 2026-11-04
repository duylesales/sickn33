---
Titel: "Hoe Richt Ik Automatische Deployments In voor een Lovable- of Bolt-App?"
Trefwoorden: ci/cd lovable-app, automatische deployment bolt, github actions supabase migraties, vercel deploy lovable, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Richt Ik Automatische Deployments In voor een Lovable- of Bolt-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Richt Ik Automatische Deployments In voor een Lovable- of Bolt-App?",
  "description": "Een eenvoudige CI/CD-pipeline maakt van AI-gegenereerde wijzigingen veilige, herhaalbare releases. Deze gids toont een praktische opzet met GitHub, een host zoals Vercel of Netlify, GitHub Actions voor controles en Supabase-migraties, en terugdraaien.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-06",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "GitHub Actions documentation", "url": "https://docs.github.com/en/actions" },
    { "@type": "CreativeWork", "name": "GitHub: About protected branches", "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches" },
    { "@type": "CreativeWork", "name": "Supabase: Managing environments", "url": "https://supabase.com/docs/guides/deployment/managing-environments" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" }
  ]
}
</script>

**Kort antwoord:** koppel uw GitHub-repository aan een host zoals Vercel of Netlify, zodat elke push automatisch wordt gebouwd en gedeployd, waarbij de main-branch naar staging gaat en een productiebranch naar uw live domein. Voeg een GitHub Actions-workflow toe die bij elke wijziging een build, linting en een paar tests uitvoert, en die Supabase-migraties eerst op staging en daarna op productie toepast. Houd omgevingsvariabelen per omgeving bij op de host, en gebruik het directe terugdraaien van de host wanneer een release misgaat.

## Belangrijkste Punten

- **Een CI/CD-pipeline maakt van AI-gegenereerde wijzigingen veilige, herhaalbare releases:** controles bij elke wijziging, automatische deployment naar staging, bewuste promotie naar productie en direct terugdraaien.
- **Het DORA-onderzoek van Google koppelt al jaren praktijken voor continuous delivery** - kleine wijzigingen, geautomatiseerd testen, geautomatiseerde deployment - aan betere prestaties bij het opleveren van software.
- **Databasemigraties horen in de pipeline,** eerst toegepast op staging met de Supabase CLI, nooit met de hand bewerkt in productie.
- **Omgevingsvariabelen staan per omgeving op de host,** met geheimen in opslag op de server in plaats van in frontendvariabelen.
- **Geef de voorkeur aan aanvullende migraties,** zodat het terugdraaien van de app de database nooit breekt.

## De Pipeline in Eén Overzicht

| Gebeurtenis | Wat er gebeurt |
| --- | --- |
| Lovable of Bolt commit naar `main` | Controles draaien; de app wordt gedeployd naar staging; migraties worden toegepast op de stagingdatabase |
| Pull request `main` → `production` | Controles draaien opnieuw; preview van wat er verandert |
| Merge naar `production` | De app wordt gedeployd naar het live domein; migraties worden toegepast op de productiedatabase |
| Probleem in productie | Terugdraaien naar de vorige deployment in het dashboard van de host |

## Stap 1: Koppel de Host

Importeer de repository in Vercel of Netlify. Stel het buildcommando in (meestal `npm run build`) en de outputmap (vaak `dist` bij Vite). Stel branchdeployments in: `main` naar een stagingdomein, `production` naar uw live domein.

## Stap 2: Omgevingsvariabelen

Voeg variabelen per omgeving toe op de host: de Supabase-URL en -sleutel van staging voor staging, productiewaarden voor productie, testsleutels van Stripe voor staging en live sleutels voor productie. Frontendvariabelen hebben het juiste voorvoegsel voor uw framework nodig, zoals `VITE_` voor Vite. Geheimen voor serverfuncties horen in de secrets van Supabase edge functions, niet in de frontend.

## Stap 3: Een Workflow voor Controles

Een GitHub Actions-workflow bij pull requests en pushes:

1. Afhankelijkheden installeren
2. Linten (vangt fouten op zoals imports met verkeerde hoofdletters)
3. Typecontrole, als u TypeScript gebruikt
4. Bouwen
5. Een handvol end-to-end-tests tegen staging uitvoeren

Faalt een stap, dan wordt de merge naar productie geblokkeerd. Ons artikel over [AI-gebouwde apps testen](https://launchstudio.eu/nl/blog/how-do-i-test-my-ai-built-app-before-launch) behandelt met welke tests u begint.

## Stap 4: Databasemigraties

Gebruik de Supabase CLI in GitHub Actions om migraties uit `supabase/migrations` toe te passen: op het stagingproject wanneer `main` verandert, op het productieproject wanneer `production` verandert. Bewaar de inloggegevens van de projecten als GitHub-secrets. Pas nooit ongeteste migraties direct toe op productie.

## Stap 5: Edge Functions

Deploy edge functions met de Supabase CLI in dezelfde workflow, zodat functies en databasewijzigingen samen uitgaan.

## Stap 6: Plan voor Terugdraaien

Frontendreleases terugdraaien gaat bij de meeste hosts direct. Databasewijzigingen terugdraaien is lastiger: geef de voorkeur aan aanvullende migraties (voeg kolommen toe in plaats van ze direct te hernoemen of te verwijderen), zodat u de app kunt terugdraaien zonder de database te breken.

## Wat CI en CD in de Praktijk Betekenen

Continuous integration (CI) betekent dat elke wijziging automatisch wordt gebouwd en gecontroleerd: linting, typecontrole, tests. Continuous delivery (CD) betekent dat elke wijziging die de controles doorstaat veilig en herhaalbaar kan worden gedeployd, meestal eerst naar staging en daarna, bewust, naar productie. Voor oprichters zijn de praktische voordelen concreet: kapotte builds bereiken nooit klanten, elke release is te herleiden tot een specifieke wijziging en terugdraaien kost seconden.

## Waarom Teams die met AI Werken er het Meest aan Hebben

AI-builders en -assistenten vergroten het aantal en de omvang van wijzigingen. Het DORA-rapport van Google uit 2024 vond dat meer gebruik van AI samenging met minder stabiele oplevering wanneer teams ondersteunende praktijken misten. CI/CD is het meest directe tegenwicht: elke wijziging wordt automatisch gecontroleerd, ongeacht wie of wat die schreef. Een pipeline vertraagt Lovable niet; hij maakt de snelheid van Lovable veilig.

## Een Minimale GitHub Actions-Workflow

Een eerste workflow voor een Lovable- of Bolt-project draait bij elke push en pull request en voert deze stappen uit:

1. De code uitchecken
2. Afhankelijkheden installeren met een schone installatie
3. De linter draaien om fouten op te vangen zoals imports met verkeerde hoofdletters en ongebruikte code
4. TypeScript-typecontrole uitvoeren als het project TypeScript gebruikt
5. De productiebundel bouwen
6. Een kleine set end-to-end-tests tegen staging uitvoeren

Faalt een stap, dan kan de wijziging niet in de productiebranch worden gemerged. De documentatie van GitHub over Actions en beschermde branches legt uit hoe u geslaagde controles verplicht stelt voordat er gemerged wordt.

## Migraties Zonder Angst

Databasewijzigingen zijn het riskantste deel van elke release. Een veilige aanpak met Supabase:

- Elke schemawijziging is een migratiebestand in `supabase/migrations`
- De pipeline past nieuwe migraties toe op het stagingproject wanneer `main` verandert
- Productiemigraties draaien alleen wanneer de productiebranch verandert, nadat staging is getest
- Migraties zijn waar mogelijk aanvullend: eerst kolommen en tabellen toevoegen, gegevens aanvullen, de app omzetten en oude structuren in een latere release verwijderen
- Destructieve migraties worden vóór het mergen door een mens beoordeeld

Deze aanpak van "uitbreiden en inkrimpen" betekent dat op elk moment zowel de oude als de nieuwe versie van de app tegen de database kan draaien, wat terugdraaien veilig maakt.

## Geheimen Beheren in Pipelines

Pipelines hebben inloggegevens nodig: toegangstokens voor Supabase, projectreferenties, tokens voor de hosting. Bewaar ze als versleutelde secrets in GitHub, beperkt tot de workflows die ze nodig hebben, en druk ze nooit af in logs. Gebruik aparte inloggegevens voor staging en productie. Het Secrets Management Cheat Sheet van OWASP raadt minimale rechten en rotatie aan; pas beide toe op inloggegevens voor CI, die aantrekkelijke doelwitten zijn omdat ze productie kunnen wijzigen.

## Deploymentstrategieën voor Kleine Apps

De meeste oprichtersapps doen het goed met eenvoudige strategieën: automatische deployment naar staging, handmatige promotie naar productie en direct terugdraaien via de host. Naarmate het verkeer groeit, kunt u feature flags overwegen om functies eerst aan een deel van de gebruikers vrij te geven, en vaste releasemomenten waarop u de monitoring in de gaten kunt houden. Deploy geen grote wijzigingen vlak voor het weekend of drukke periodes.

## De Gezondheid van Oplevering Meten

Het DORA-onderzoek gebruikt vier kerncijfers: deploymentfrequentie, doorlooptijd van wijzigingen, faalpercentage van wijzigingen en hersteltijd van de dienst. Zelfs een solo-oprichter kan vereenvoudigde versies bijhouden: hoe vaak u een release doet, hoe lang een wijziging duurt van idee tot productie, hoe vaak een release een probleem veroorzaakt en hoe snel u herstelt. Als deze cijfers in de loop van de tijd verbeteren, is dat een goed teken dat uw proces werkt.

## Previewdeployments voor Elke Wijziging

Hosts zoals Vercel en Netlify maken voor elke pull request een preview-URL aan. In combinatie met een stagingbackend kunnen u of een reviewer met previews één wijziging los doorklikken voordat die wordt gemerged. Voor niet-technische oprichters die met ontwikkelaars werken, zijn previews de duidelijkste manier om werk goed te keuren: open de link, test de wijziging, keur goed of geef commentaar. Bescherm previews tegen openbare toegang en zoekmachines, omdat ze onafgemaakte functies kunnen tonen.

## Meldingen en Zichtbaarheid

Koppel uw pipeline aan een kanaal dat u leest - e-mail, Slack of Teams - zodat u ziet wanneer deployments slagen, mislukken of worden teruggedraaid. Zichtbaarheid bouwt vertrouwen in het proces op en helpt u problemen snel met releases in verband te brengen. In combinatie met error tracking die per release is gelabeld, kunt u meestal binnen enkele minuten zien of een nieuwe deployment een probleem veroorzaakte.

## Veelgemaakte Fouten

- Pipelines die bij elke push naar `main` naar productie deployen en staging overslaan
- Migraties die met de hand in het productiedashboard worden toegepast
- Geheimen die in pipelinelogs worden afgedrukt
- Tests die "tijdelijk" worden overgeslagen en nooit meer worden aangezet
- Geen plan voor het terugdraaien van databasewijzigingen
- Verschillende Node-versies lokaal, in CI en op de host

## Deze Week Beginnen

Koppel uw repository aan uw host met branchdeployments, voeg een GitHub Actions-workflow toe die elke wijziging lint en bouwt, zet schemawijzigingen om in migraties en documenteer uw stappen voor terugdraaien. Die vier stappen leveren het grootste deel van de waarde van CI/CD op, en tests en geautomatiseerde migraties kunt u daarna stap voor stap toevoegen.

## Pipelines voor Edge Functions

Supabase edge functions moeten vanuit de repository worden gedeployd via dezelfde pipeline als de frontend en de migraties, met de Supabase CLI. Functies met de hand vanaf een laptop deployen of ze in een dashboard bewerken, veroorzaakt verschillen tussen omgevingen en maakt het onmogelijk om te weten wat er in productie draait. Met functies in de pipeline is elke deployment te herleiden tot een commit, en blijven staging en productie identiek.

## Versies Consistent Houden

Veel verrassingen bij deployments komen voort uit versieverschillen: Node.js lokaal, in CI en op de host; pakketversies die op verschillende machines anders worden opgelost. Leg uw Node-versie vast in een configuratiebestand dat zowel de host als CI lezen, commit uw lockfile en gebruik schone installaties in CI. Deze kleine stappen nemen een hele categorie problemen van het type "op mijn machine werkt het" weg, die vaak voorkomen wanneer code uit Bolt of Lovable wordt gehaald.

## Wie Mag Deployen

Bepaal wie wijzigingen naar productie mag promoveren en bescherm de productiebranch daarop. Voor een solo-oprichter bent u dat zelf, met verplichte controles. Voor kleine teams vereist u één review voor wijzigingen aan migraties, policies en betaalcode. Beperk productiegegevens tot de pipeline en een minimaal aantal mensen.

## De Opbrengst

Met een pipeline wordt een release routine: wijzigingen worden automatisch gecontroleerd, staging laat zien wat eraan komt, productiewijzigingen zijn bewust en fouten worden binnen seconden teruggedraaid. Die rust is wat oprichters in staat stelt snel te blijven bouwen met AI-tools zonder voor elke release bang te zijn.

## Gerelateerde Onderwerpen

Een pipeline is het nuttigst samen met een stagingomgeving en geautomatiseerde tests. Onze gidsen over staging voor Lovable-apps en over het testen van AI-gebouwde apps vóór de lancering behandelen beide in detail.

## Samenvatting

Controleer elke wijziging automatisch, deploy eerst naar staging, promoveer bewust, migreer aanvullend en houd terugdraaien op één klik afstand.

## Een Laatste Tip

Schrijf uw releasestappen in de README, ook als de pipeline ze automatiseert, zodat iedereen begrijpt wat er bij elke deployment gebeurt.

## Veelvoorkomende Problemen

- Lovable of Bolt die kapotte builds naar `main` pusht: opgevangen door controles vóór productie
- Migraties die met de hand in het dashboard zijn gemaakt: niet in git, dus pipelines missen ze
- Productiesleutels die in staging worden gebruikt: betalingen of e-mails komen bij echte klanten terecht

## Het Laten Inrichten

LaunchStudio richt CI/CD in als onderdeel van de meeste lanceringen, meestal twee tot drie dagen van de opdracht. Onze engineers hebben via Manifera 160+ projecten voor enterpriseklanten opgeleverd, met GitHub Actions, Docker en cloudpipelines als standaard; zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/). Supabase documenteert [deployen met GitHub Actions](https://supabase.com/docs/guides/deployment/managing-environments), en [de documentatie van GitHub Actions](https://docs.github.com/en/actions) behandelt workflows.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Inspectie-App die vanaf een Laptop Werd Gedeployd

Wouter van Rossum runt een keuringsbedrijf in Den Helder en bouwde Keuringsapp met Bolt: inspecteurs vullen op tablets checklists in voor brandveiligheidsinstallaties, voegen foto's toe en genereren rapporten voor klanten. Deployen betekende dat Wouter op zijn laptop een build maakte en bestanden naar Netlify uploadde, terwijl databasewijzigingen met de hand in het Supabase-dashboard werden gedaan.

Op een avond deployde hij een nieuwe versie van een checklist zonder de bijbehorende databasekolom, die alleen in zijn lokale aantekeningen bestond. De volgende ochtend konden inspecteurs drie uur lang geen rapporten insturen. Een andere keer deployde hij vanaf een branch met onafgemaakte wijzigingen.

LaunchStudio koppelde de repository aan Netlify met staging- en productiebranches, zette alle schemawijzigingen om in migraties, voegde een GitHub Actions-workflow toe met linting, build, migraties en twee end-to-end-tests, deployde edge functions via de CLI en documenteerde de stappen voor terugdraaien.

**Resultaat:** In het kwartaal daarna bracht Wouter 22 updates uit zonder één mislukte deployment. Eén kapotte build door een wijziging in Bolt werd automatisch tegengehouden voordat die de inspecteurs bereikte.

> *"Elke release hing ervan af dat ik vijf handmatige stappen onthield. Nu onthoudt de pipeline ze voor me."*
> - **Wouter van Rossum, Oprichter, Keuringsapp (Den Helder)**

**Kosten & Doorlooptijd:** €1.500 (Launch Ready-pakket: Netlify-branches, migraties, controles in GitHub Actions, deployment van edge functions en documentatie voor terugdraaien) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Heb ik CI/CD nodig voor een kleine Lovable- of Bolt-app?

Als klanten ervan afhankelijk zijn, ja. Een eenvoudige pipeline voorkomt de meest voorkomende mislukte releases: kapotte builds, ontbrekende omgevingsvariabelen en databasewijzigingen die niet in lijn zijn met de code. Het inrichten kost dagen en bespaart uren per incident.

### Kan Lovable direct naar productie deployen?

Lovable kan uw app publiceren, maar direct publiceren slaat staging en controles over. Met een pipeline gaan de commits van Lovable eerst naar staging, en promoveert u geteste wijzigingen naar productie.

### Hoe ga ik om met databasewijzigingen in Supabase in een pipeline?

Houd elke schemawijziging bij als migratiebestand in uw repository en pas ze in uw workflow toe met de Supabase CLI, eerst op staging, daarna op productie. Wijzig productieschema's niet in het dashboard.

### Hoe richt Manifera releasepipelines in?

Met dezelfde fasen voor elk project: controles, staging, promotie en terugdraaien. De 11+ jaar oplevering van Manifera laten zien dat consistente pipelines, niet heldendaden, releases saai en veilig houden.

### Kunnen problemen bij deployments de zichtbaarheid van mijn site beïnvloeden?

Ja. Mislukte deployments die pagina's kapot laten of fouten laten teruggeven, ook kort tijdens het crawlen, kunnen de indexering en AI-vermeldingen beïnvloeden. Geautomatiseerde controles en direct terugdraaien beperken dat risico.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik CI/CD nodig voor een kleine Lovable- of Bolt-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als klanten ervan afhankelijk zijn, ja; het voorkomt kapotte builds, ontbrekende variabelen en schemaverschillen." }
    },
    {
      "@type": "Question",
      "name": "Kan Lovable direct naar productie deployen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het kan publiceren, maar een pipeline leidt commits eerst langs staging en controles." }
    },
    {
      "@type": "Question",
      "name": "Hoe ga ik om met databasewijzigingen in Supabase in een pipeline?",
      "acceptedAnswer": { "@type": "Answer", "text": "Houd migraties in de repository en pas ze met de Supabase CLI toe op staging en daarna op productie." }
    },
    {
      "@type": "Question",
      "name": "Hoe richt Manifera releasepipelines in?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met consistente fasen: controles, staging, promotie en terugdraaien." }
    },
    {
      "@type": "Question",
      "name": "Kunnen problemen bij deployments de zichtbaarheid van mijn site beïnvloeden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Kapotte pagina's tijdens het crawlen raken de indexering; controles en terugdraaien beperken het risico." }
    }
  ]
}
</script>
