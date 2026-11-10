---
Titel: "Gehallucineerde Packages: Slopsquatting in AI-Gegenereerde Code"
Trefwoorden: slopsquatting, hallucinated packages ai, package hallucination npm, ai code supply chain risk, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Gehallucineerde Packages: Slopsquatting in AI-Gegenereerde Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gehallucineerde Packages: Slopsquatting in AI-Gegenereerde Code",
  "description": "AI-programmeertools raden regelmatig software-packages aan die in werkelijkheid niet bestaan. Cybercriminelen registreren die verzonnen namen vervolgens met kwaadaardige code om supply chain-aanvallen uit te voeren. Deze gids legt package-hallucinatie en slopsquatting uit, wat wetenschappelijk onderzoek aantoont over de frequentie, hoe het verschilt van typosquatting en welke concrete verdedigingsmechanismen oprichters moeten hanteren bij het bouwen met Lovable, Bolt, Cursor of Claude Code.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-15",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/hallucinated-packages-slopsquatting-in-ai-generated-code" },
  "citation": [
    { "@type": "CreativeWork", "name": "Spracklen et al., We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", "url": "https://arxiv.org/abs/2406.10279" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A06 Vulnerable and Outdated Components", "url": "https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/" },
    { "@type": "CreativeWork", "name": "npm Docs: npm ci", "url": "https://docs.npmjs.com/cli/commands/npm-ci" },
    { "@type": "CreativeWork", "name": "OpenSSF Scorecard", "url": "https://securityscorecards.dev/" }
  ]
}
</script>

Moderne softwaretoepassingen worden niet van de grond af met de hand geschreven; ze worden geassembleerd uit open-source libraries. Een doorsnee webapplicatie die is gegenereerd via tools zoals Lovable, Bolt, v0 of Cursor leunt op honderden externe packages die automatisch worden binnengehaald uit centrale registers zoals npm (voor JavaScript/TypeScript) of PyPI (voor Python). AI-codeassistenten voegen doorlopend nieuwe bibliotheken toe: een handig hulpmiddel voor datumberekeningen, een PDF-exporteur of een snelle parser voor Excel-bestanden.

In de meeste gevallen zijn deze packages legitiem, wijdverbreid en veilig. Maar niet altijd. Grote taalmodellen (LLM's) verzinnen geregeld bibliotheken die in werkelijkheid helemaal niet bestaan - een fenomeen dat bekendstaat als **package-hallucinatie**. De AI bedenkt een uiterst plausibele packagenaam die logisch aansluit bij uw prompt, maar die nooit officieel is gepubliceerd. Op zichzelf leidt dit slechts tot een mislukte installatie. Het acute gevaar ontstaat zodra aanvallers ontdekken welke namen door AI-modellen worden verzonnen. De aanvaller claimt die fictieve naam in het openbare npm-register en uploadt een package met kwaadaardige code. De volgende ontwikkelaar - of de volgende autonome AI-agent - die exact dezelfde vraag stelt, installeert vervolgens direct malware in de applicatie.

Deze nieuwe aanvalsmethode heet **slopsquatting**. Deze handleiding legt uit hoe slopsquatting werkt, wat wetenschappelijk onderzoek zegt over de schaal van het probleem en hoe u uw met AI ontwikkelde SaaS beschermt tegen besmette toeleveringsketens (supply chain attacks).

## Belangrijkste Punten

- **Package-hallucinatie** treedt op wanneer een AI-model een softwarebibliotheek suggereert die niet bestaat in het centrale package-register.
- **Slopsquatting** is de gerichte cyberaanval waarbij kwaadwillenden deze gehallucineerde namen preventief registreren en voorzien van malware, wachtend tot AI-ontwikkelaars ze argeloos installeren.
- **Onderzoek toont aan dat hallucinaties frequent voorkomen:** wetenschappelijke metingen tonen aan dat grofweg 20% van de door LLM's gegenereerde bibliotheeknamen bij complexe prompts niet bestaat, waarbij specifieke verzonnen namen systematisch terugkeren.
- **Malafide packages kunnen direct code uitvoeren tijdens de installatie (`postinstall`),** waardoor geheime omgevingsvariabelen, database-tokens en SSH-sleutels al worden buitgemaakt vóórdat de code ooit is gestart.
- **Effectieve maatregelen zijn direct toepasbaar:** verifieer onbekende dependencies handmatig, commit altijd uw lockfiles (`package-lock.json`), scan op kwetsbaarheden en leg strenge restricties op aan wat AI-agents zelfstandig mogen installeren.

## Wat Wetenschappelijk Onderzoek Aantoont

In de toonaangevende academische studie *"We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs"* onderzochten onderzoekers onder leiding van Joseph Spracklen honderdduizenden door AI gegenereerde codefragmenten in Python en JavaScript. Zij analyseerden commerciële modellen (zoals GPT-4) en open-source alternatieven.

De conclusie was alarmerend: bij bepaalde codeertaken was bijna één op de vijf voorgestelde packages een hallucinatie. Commerciële modellen hallucineerden weliswaar significant minder dan open-source modellen, maar het risico bleef overal substantieel. Wat belangrijker is: wanneer identieke prompts werden herhaald, **bedachten de modellen telkens exact dezelfde niet-bestaande packagenamen**.

Deze voorspelbaarheid transformeert een onschuldige model-eigenaardigheid in een direct security-lek. Een aanvaller hoeft slechts een geautomatiseerd script te draaien dat veelvoorkomende prompts afvuurt, de niet-bestaande bibliotheken inventariseert, en die namen op npm of PyPI massaal registreert met een wachtende payload.

## Slopsquatting versus Typosquatting

| Aanvalsvorm | Werkwijze | Wie trapt erin? |
| --- | --- | --- |
| Typosquatting | Aanvaller registreert spelfouten van bekende packages (bijv. `lodahs` i.p.v. `lodash`) | Menselijke ontwikkelaars die een typefout maken in de terminal |
| Dependency Confusion | Aanvaller publiceert op openbare registers met dezelfde naam als een interne private library | Geautomatiseerde build-systemen met onjuiste registerprioriteiten |
| Slopsquatting | Aanvaller registreert plausibele namen die AI-modellen systematisch hallucineren | Ontwikkelaars en autonome AI-agents die AI-code klakkeloos overnemen |

Bij slopsquatting is het risico extra groot omdat de ontwikkelaar de code zelden letter voor letter inspecteert. Een agent zoals Cursor of Claude Code schrijft een importregel, voert automatisch `npm install` uit en meldt triomfantelijk dat de feature gereed is.

## Waarom Malafide Packages Zo Gevaarlijk Zijn

Een gecompromitteerde dependency kan schade aanrichten op drie opeenvolgende momenten:

1. **Tijdens de installatie (Install-time):** npm ondersteunt zogenaamde lifecycle-scripts (`preinstall` en `postinstall`). Zodra `npm install` draait, kan het package direct willekeurige shell-commando's uitvoeren. Het leest uw `.env`-bestand uit, steelt uw Supabase service role key, Stripe geheime sleutels en AWS-credentials, en stuurt deze direct door naar een externe server.
2. **Tijdens het build-proces (Build-time):** het package injecteert stiekem JavaScript in de gecompileerde frontend-bundel, waardoor wachtwoorden van uw gebruikers of creditcardgegevens in het afrekenscherm worden afgetapt (formjacking).
3. **In productie (Runtime):** het package draait binnen uw backend Edge Functions en heeft volledige leestoegang tot uw PostgreSQL-productiedatabase.

## Waarschuwingssignalen bij Verdachte Packages

Controleer bij elke nieuwe dependency die door een AI-tool wordt voorgesteld:

- **Bestaat het package al lang?** Packages die pas enkele weken of dagen online staan voor een standaardtaak moeten direct argwaan wekken.
- **Wie is de beheerder (maintainer)?** Is het een geverifieerde organisatie of een anoniem account zonder andere activiteit?
- **Hoeveel wekelijkse downloads zijn er?** Bekende open-source tools hebben tienduizenden downloads. Heeft het package minder dan 100 downloads? Wees uiterst voorzichtig.
- **Is er een openbare GitHub-repository gekoppeld?** Packages zonder transparante broncode of waarvan de npm-code afwijkt van de GitHub-repository zijn verdacht.
- **Bevat het installatie-scripts?** Inspecteer het `package.json` van de library op regels met `preinstall` of `postinstall`.
- **Is het package wel echt nodig?** AI stelt regelmatig zware externe bibliotheken voor om iets simpels te doen wat in drie regels native JavaScript opgelost kan worden.

## Praktische Verdediging voor AI-SaaS Oprichters

**1. Behandel dependency-wijzigingen als hoog-risico:**
Maak van `package.json`, `package-lock.json` en `pnpm-lock.yaml` beschermde bestanden in GitHub. Eis dat wijzigingen aan deze bestanden altijd door een mens worden goedgekeurd.

**2. Commit altijd uw lockfile en gebruik `npm ci`:**
Zorg dat `package-lock.json` altijd wordt gecommit in Git. Gebruik in uw deployment-pipelines (zoals Vercel of GitHub Actions) uitsluitend het commando `npm ci`. Dit dwingt af dat exact de cryptografisch vastgelegde versies worden geïnstalleerd en voorkomt dat er dynamisch nieuwe versies worden opgehaald.

**3. Automatiseer supply chain security-scans:**
Schakel tools zoals GitHub Dependabot, Snyk of Socket.dev in. Socket.dev inspecteert specifiek of nieuwe dependencies netwerkverkeer initiëren of verdachte installatie-scripts bevatten.

**4. Beperk de rechten van AI-agents:**
Laat AI-agents zoals Claude Code of Cursor in ontwikkelomgevingen werken met gelimiteerde API-keys. Zorg dat productie-secrets nóóit aanwezig zijn in de lokale shell waarin de agent pakketten mag installeren.

**5. Definieer goedgekeurde bibliotheken in uw projectregels:**
Vermeld in uw `AGENTS.md` of `.cursorrules` expliciet welke bibliotheken uw project hanteert voor gangbare taken (zoals `date-fns` voor datums, `zod` voor validatie en `lucide-react` voor iconen). Instrueer de agent om uitsluitend deze gevestigde pakketten te gebruiken en nooit alternatieven te verzinnen.

## Wat Te Doen Bij Een Verdachte Installatie?

Als u vermoedt dat er een malafide library is geïnstalleerd:

1. **Stop direct:** beëindig alle lokale dev-servers en annuleer lopende builds.
2. **Verwijder het package** uit `package.json` en wis uw `node_modules` en lockfile.
3. **Roteer onmiddellijk álle geheime sleutels** die op die machine of in CI aanwezig waren (Supabase service role keys, database-wachtwoorden, Stripe API-keys, webhook secrets).
4. **Controleer de serverlogs** van uw backend op verdachte query's of ongebruikelijke exportacties.
5. **Meld het package** direct bij het beveiligingsteam van npm of PyPI.

## Hoe LaunchStudio Helpt

LaunchStudio beveiligt de software-toeleveringsketen van met AI gebouwde applicaties vóór de productielancering: we voeren een grondige audit uit op alle directe en indirecte dependencies, verwijderen ongebruikte of gevaarlijke packages, dwingen reproduceerbare builds af via gecommitte lockfiles, configureren geautomatiseerde supply chain scanners (zoals Socket en Dependabot), scheiden ontwikkel- en productiesecrets strikt en leggen goedgekeurde library-lijsten vast in uw agent-configuraties.

Het **Launch Ready**-pakket (€800 - €3.500) omvat een complete dependency- en security-audit naast deployment. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt daarnaast continue scanning, periodieke dependency-updates, managed hosting en prioritaire ondersteuning. Gebruik onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een transparante offerte.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde engineers. CEO Herre Roelevink was medeoprichter van het cybersecuritybedrijf dat tegenwoordig bekendstaat als CFLW Cyber Strategies; deze diepgaande security-achtergrond vormt het fundament van onze focus op supply chain veiligheid. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit ons ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Factuur-Parser Waarvan Niemand Ooit Had Gehoord

Bart Scholten bouwde Inkoopscan met Claude Code en Supabase: een slimme B2B-tool voor groothandels die inkoopfacturen automatisch uit inkomende e-mails uitleest, de artikelregels en bedragen extraheert en deze matcht met openstaande inkooporders. Gedurende enkele maanden intensief sparren met de AI-agent verzamelde het project ongemerkt 214 directe en indirecte dependencies. Vlak voor de officiële livegang vroeg de IT-auditor van een grote pilotklant om een grondige security review.

LaunchStudio onderwierp alle externe packages aan een systematische screening. Het merendeel betrof gevestigde bibliotheken, maar drie packages vielen direct op. Eén package, met een naam die suggereerde dat het specifiek bedoeld was om Nederlandse UBL-facturen te ontleden, bleek pas drie weken eerder te zijn gepubliceerd door een volstrekt anoniem account zonder gekoppelde GitHub-broncode. Analyse van het installatie-script toonde aan dat het package tijdens de installatie een gecodeerd HTTP-verzoek stuurde naar een onbekend extern domein. Een tweede package bleek al jaren verlaten en bevatte bekende kwetsbaarheden, terwijl het project daarnaast 37 volstrekt overbodige libraries bevatte. Omdat het lockfile niet in Git stond, haalde de CI-server bij elke build willekeurig de nieuwste versies binnen, terwijl de productie-sleutel van Supabase als omgevingsvariabele beschikbaar was in diezelfde CI-omgeving.

LaunchStudio saneerde de codebase onmiddellijk: de verdachte en verlaten packages werden per direct gewist, de parsing werd herschreven met een reeds aanwezige gevestigde XML-library en 37 ongebruikte packages werden opgeruimd. Omdat het malafide installatie-script in de CI-pipeline had gedraaid, werden alle API-sleutels, database-wachtwoorden en tokens direct geroteerd en gecontroleerd op misbruik (er bleek gelukkig nog geen data ontvreemd). Er werd een hard lockfile gecommit, builds werden omgezet naar `npm ci`, dependency-wijzigingen werden via GitHub branch protection geblokkeerd voor autonome agents en de projectinstructies voor Claude Code kregen een strikte lijst met goedgekeurde bibliotheken.

**Resultaat:** Inkoopscan doorstond de strenge IT-audit van de groothandel met vlag en wimpel dankzij een formeel dependency-beleid en een complete Software Bill of Materials (SBOM). In de maanden daarna signaleerde de nieuw geplaatste scanner nog tweemaal een gehallucineerde packagenaam die door de agent werd gesuggereerd, waardoor deze tijdig kon worden geweigerd vóórdat er schade ontstond.

> *"Ik vertrouwde elke regel code die de AI genereerde omdat de applicatie zo soepel werkte. Ik had er werkelijk geen seconde bij stilgestaan wie de packages had geschreven die de agent geruisloos op de achtergrond installeerde."*
> - **Bart Scholten, Oprichter, Inkoopscan (Doetinchem)**

**Kosten & Doorlooptijd:** €2.800 (Launch Ready-pakket: dependency-audit, package-verwijdering, lockfile en reproduceerbare builds, secret-rotatie, scanning en agent-guardrails) - afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Wat is slopsquatting precies?

Slopsquatting is een gerichte vorm van supply chain hacking waarbij aanvallers fictieve software-packagenamen registreren die AI-taalmodellen regelmatig hallucineren. Wanneer ontwikkelaars of AI-agents deze niet-bestaande packages vervolgens installeren, halen zij ongemerkt malware binnen.

### Hoe vaak raden AI-modellen packages aan die niet bestaan?

Onderzoek toont aan dat package-hallucinaties reëel en frequent zijn; bij complexe prompts kan tot 20% van de voorgestelde bibliotheken niet-bestaand zijn. Omdat LLM's bij vergelijkbare prompts vaak dezelfde namen verzinnen, kunnen aanvallers deze namen uiterst gericht claimen.

### Hoe controleer ik of een voorgesteld package veilig is?

Controleer de ouderdom van het package op npm, het aantal wekelijkse downloads, de reputatie van de maintainer, de aanwezigheid van een actieve GitHub-repository en of er installatie-scripts aanwezig zijn. Kies bij twijfel altijd voor gevestigde libraries met miljoenen downloads.

### Hoe helpt de ervaring van Manifera bij supply chain security?

De CEO van Manifera heeft een achtergrond in cybersecurity, en onze engineers beheren al meer dan 11 jaar enterprise software-toeleveringsketens. LaunchStudio past deze security-discipline toe om AI-codebases te screenen, lockfiles af te dwingen en guardrails in te richten voor AI-programmeertools.

### Is supply chain beveiliging belangrijk voor zakelijke verkoopgesprekken?

Absoluut. Enterprise-inkopers en IT-afdelingen vragen steeds vaker om een Software Bill of Materials (SBOM) en een aantoonbaar beleid voor kwetsbaarheden in componenten. Een gedocumenteerd dependency-beleid toont volwassenheid en versnelt het IT-goedkeuringsproces aanzienlijk.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is slopsquatting precies?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een aanval waarbij gehallucineerde packagenamen van AI-modellen door aanvallers worden geregistreerd met malware om ontwikkelaars te infecteren." }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak raden AI-modellen packages aan die niet bestaan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Onderzoek toont aan dat bij complexe prompts tot 20% van de gesuggereerde packages gehallucineerd kan zijn, met systematisch terugkerende namen." }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of een voorgesteld package veilig is?",
      "acceptedAnswer": { "@type": "Answer", "text": "Inspecteer downloadstatistieken, reputatie van de maintainer, GitHub-broncode en de afwezigheid van verdachte installatiescripts." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij supply chain security?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met een cybersecurity-achtergrond en 11+ jaar enterprise-ervaring auditeert LaunchStudio dependencies en beveiligt het pipelines tegen malware." }
    },
    {
      "@type": "Question",
      "name": "Is supply chain beveiliging belangrijk voor zakelijke verkoopgesprekken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, enterprise-inkopers eisen steeds vaker een SBOM en actieve scanning van componenten alvorens software goed te keuren." }
    }
  ]
}
</script>
