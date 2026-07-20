---
Title: Waarom Ontwikkelaars Use AI to Generate Code maar Mensen om het te Beheren
Keywords: use AI to generate code, AI can code, AI code governance, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: VP of Engineering / CTO
---

# Waarom Ontwikkelaars Use AI to Generate Code maar Mensen om het te Beheren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gebruik AI om Code te Genereren, Gebruik Mensen om het te Beheren: De Opkomst van het Internal Developer Portal",
  "description": "Wanneer iedereen in je bedrijf AI kan gebruiken om code te genereren, schaalt de technische schuld exponentieel. Een deep dive in hoe engineering teams Internal Developer Portals (IDP's) inzetten om AI-gegenereerde shadow IT te reguleren.",
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
  "datePublished": "2026-12-05",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/use-ai-to-generate-code"
  }
}
</script>

Het harde feit dat AI vlekkeloos kan coderen is anno 2026 al lang geen leuk debat meer; het is een keiharde basisrealiteit. Junior developers, product managers, en zelfs creatieve marketing executives gebruiken tegenwoordig dagelijks AI om code te genereren. Ze bouwen onafgebroken interne dashboards, handige data-parsing scripts, en complexe marketing automation workflows op een absoluut razend tempo (blistering speed). 

Voor een VP of Engineering of CTO is deze radicale democratisering van code-generatie echter een levensgevaarlijk, tweesnijdend zwaard. De productiviteit (productivity) piekt hoger dan ooit tevoren, maar de interne governance (toezicht en controle) is compleet en totaal ingestort. 

Wanneer je werknemers AI gebruiken om lokaal code te genereren buiten de strakke kaders van een gestructureerde engineering pipeline om, creëer je onherroepelijk dodelijke "Shadow IT" (schaduw-IT). Een snelle operations manager gebruikt bijvoorbeeld even Lovable om een handige tracking app te bouwen die direct inplugt op jullie productie-database, waarbij hij argeloos een onversleuteld, hardcoded wachtwoord gebruikt. Een junior developer zet Cursor aan en genereert achteloos een React-component van ruim 2.000 regels code, dat werkelijk álle security en accessibility standaarden van het bedrijf flagrant schendt. 

Je kunt je team simpelweg niet meer verbieden om AI te gebruiken. Als je dat krampachtig probeert, doen ze het gewoon stiekem op hun eigen, privé laptops. De enige, werkbare oplossing is om de extreme snelheid van AI code generatie volledig te omarmen, terwijl je tegelijkertijd loeistrenge, volautomatische, menselijke governance afdwingt. Dít realiseer je uitsluitend door de keiharde implementatie van een Internal Developer Portal (IDP).

## De AI Governance Crisis

Voordat we de exacte oplossing uitstippelen, moeten we eerst de specifieke, dodelijke engineering crises begrijpen die direct worden veroorzaakt door het compleet ongemodereerd genereren van AI code binnen middelgrote tot grote organisaties.

### 1. De Wildgroei Van Geheimen (Secrets Sprawl)
AI modellen snappen fundamenteel helemaal niets van het concept achter een onzichtbaar `.env` configuratiebestand, tenzij je ze daar héél expliciet op instrueert (prompt). Wanneer niet-engineers AI gebruiken om even snel scripts te genereren, hardcodeert de AI de zwaar beveiligde API sleutels (zoals Stripe, AWS, OpenAI) vrijwel altijd direct, onversleuteld in de Python of JavaScript bestanden. Deze levensgevaarlijke bestanden worden vervolgens doodleuk geüpload naar gedeelde Slack kanalen, interne wikis, of erger: publieke GitHub repositories. Dit resulteert in onmiddellijke, catastrofale data-lekken (security breaches).

### 2. De Dependency Nachtmerrie
LLM's (AI modellen) hallucineren ontzettend vaak npm of pip packages die he-le-maal niet bestaan, óf ze importeren argeloos zwaar verouderde, extreem kwetsbare versies van libraries. Als een enthousiast marketingteam een lokaal gegenereerd Node.js scriptje draait dat een package gebruikt met een welbekende Remote Code Execution (RCE) vulnerability (kwetsbaarheid), ligt plotsklaps je voltallige, corporate netwerk op straat.

### 3. De Architectuur Omleiding (Architecture Bypass)
Strakke Enterprise architectuur leunt zwaar op heilige, strikte grenzen: frontends praten exclusief met beveiligde API gateways, die op hun beurt weer netjes met microservices praten, die dán pas met databases kletsen. AI code generators kiezen daarentegen puur uit luiheid altijd de weg van de aller-, allerminste weerstand. Ze schrijven met het grootste gemak en een grote glimlach een simpele React frontend die een rauwe (raw) SQL query doodleuk rechtstreeks op jouw zwaarbeveiligde, draaiende PostgreSQL productie-database vuurt, en passeren daarmee alle API gateways, alle rate limiters, en iedere vorm van logische audit logs compleet.

## De Oplossing: Internal Developer Portals (IDP's)

Om dit roekeloze gedrag keihard in toom te houden en AI code generatie strak te reguleren (govern), deployen slimme engineering leiders massaal zogenaamde Internal Developer Portals (zoals het bekende Backstage van Spotify, of Port). Een IDP functioneert als een massieve, structurele trechter. Het platform zegt in feite: *"Jullie mogen absoluut AI gebruiken om alles te genereren wat je maar wenst, maar om die code daadwerkelijk live op een bedrijfs-server te krijgen, móét het fysiek door dít strakke portaal (portal) heen."*

### 1. Geautomatiseerde CI/CD Vangrails (Guardrails)
Op het moment dat een gretige werknemer zijn of haar kersvers gegenereerde AI code in de IDP indient (submits), triggert het portaal onverbiddelijk en volautomatisch een loeizware CI/CD pijplijn. Static Application Security Testing (SAST) tools scannen de code agressief op levensgevaarlijke hardcoded secrets. Software Composition Analysis (SCA) tools scannen de `package.json` razendsnel op verdachte en kwetsbare dependencies. Als de slordige AI code genadeloos faalt in deze scan, wordt het domweg snoeihard geweigerd en weggesmeten (rejected). De pijplijn retourneert vervolgens keurig een opbouwende foutmelding (prompt) die de werknemer simpelweg weer aan de AI kan voeren om de fout te laten fixen.

### 2. Afgeschermde Omgevingen (Scaffolded Environments)
In plaats van een werknemer zélf een AI te laten commanderen om *"bouw een complete Node.js app from scratch"*, biedt de IDP zogeheten strakke "Golden Paths" (gouden paden). De werknemer klikt op één knop in de IDP, waarna er volautomatisch een kogelvrije, pre-configured repository (repo) wordt aangemaakt. Deze repository is by default (standaard) al voorzien van exact de juiste, strakke Dockerfiles, goedgekeurde authenticatie middleware, en robuuste database ORM's. De werknemer gebruikt vervolgens louter AI om uitsluitend nog de *business logic* (de bedrijfsvoering-code) búinnen deze veilige zandbak (scaffold) te genereren, in plaats van zélf te knutselen aan de onderliggende bedrijfs-infrastructuur.

### 3. De Afdwinging Van De API Gateway
De IDP provisioneert (spint up) louter omgevingen die fysiek he-le-maal niet direct kunnen communiceren met de zware productie-database. De AI-gegenereerde code wordt rücksichtslos gedwongen om álle data-verzoeken (requests) netjes te routeren door de extreem zwaarbeveiligde API Gateway van het bedrijf. Dit dwingt vitale beveiligingslagen zoals Row Level Security (RLS) en audit logging fundamenteel af (natively), ongeacht hoe slordig, lui of belabberd de AI-gegenereerde frontend code daadwerkelijk is geschreven.

## Hoe LaunchStudio AI Governance Engineert

Het compleet from scratch opbouwen van een zware IDP en het waterdicht configureren van agressieve CI/CD pijplijnen, vereist hooggespecialiseerde, dure DevOps en Platform Engineering expertise. 

[LaunchStudio](https://launchstudio.eu/nl/), zwaar leunend op de indrukwekkende enterprise capaciteiten van [Manifera](https://www.manifera.com/), bouwt en implementeert deze kritieke governance structuren specifiek voor hard-schalende softwarebedrijven.

Strak aangestuurd door Herre Roelevink in Amsterdam, waarbij de brute platform engineering foutloos wordt geëxecuteerd door onze experts in Ho Chi Minh City, vestigt het LaunchStudio team onbreekbare vangrails (guardrails) die jouw héle team in staat stellen om veilig, robuust en snel met AI te coderen.

Wij bouwen de zware Platform Engineering laag:
1. **Repository Scaffolding:** We creëren de muurvaste "Golden Path" templates (voor Next.js, Node.js, Python), standaard gewapend met de allerzwaarste enterprise security defaults.
2. **Pipeline Automation:** We configureren de complexe GitHub Actions of GitLab CI pijplijnen, die volautomatisch en direct AI hallucinaties, levensgevaarlijke hardcoded secrets, en kwetsbare (vulnerable) dependencies afwijzen (reject).
3. **Infrastructure as Code (IaC):** We garanderen strak dat alle deployments die getriggerd worden door de IDP, loeistrak worden gemanaged via Terraform, waardoor jouw voltallige cloud-omgeving kogelvrij, veilig én 100% voorspelbaar blijft.

## Praktijkvoorbeeld

### Een AI-Native Founder in de praktijk: De Engineering Director Die Strijdt Tegen Shadow IT

Mark is de doorgewinterde VP of Engineering bij een snelgroeiend logistiek softwarebedrijf (SaaS) in Rotterdam. Zijn development team van 40 man was enorm productief, maar onlangs ontdekte hij een angstaanjagende, levensgevaarlijke trend. De operations én de customer success afdelingen hadden de wondere wereld van AI coding tools (zoals Cursor) ontdekt. 

Uit puur enthousiasme waren ze zélf hun eigen interne dashboards in elkaar aan het typen (genereren) om complexe zendingen te traceren en het onboarden van nieuwe cliënten sneller te managen. In eerste instantie was Mark ontzettend onder de indruk van hun proactieve houding. Totdat de maandelijkse AWS factuur (cloud bill) compleet uit het niets explodeerde met een absurde €4.000 extra. 

Mark dook direct in het probleem (investigated) en stuitte op een catastrofale "Shadow IT" ramp (disaster). Een ijverige customer success manager had de AI doodleuk een Python-script laten schrijven dat de centrale productie-database agressief elke 5 seconden pingde (queried) om te controleren op verse updates. Het script? Dat bevatte ongecodeerd (hardcoded) het állerhoogste, machtigste master-wachtwoord van de productie-database. En waar draaide het? Op een volstrekt onbeveiligde, niet-gepatchte AWS EC2 server, die de manager stiekem had aangemaakt met zijn corporate creditcard. 

Mark kón (en wilde) AI niet simpelweg verbieden — de extreme snelheid in bedrijfsvoering (business velocity) die het opleverde was domweg veel te waardevol. Maar hij had wel zéér acuut (acute) keiharde controle nodig. Hij huurde LaunchStudio in om in sneltreinvaart een waterdicht AI governance raamwerk te bouwen.

In slechts 20 werkdagen deployde het Manifera team een indrukwekkend Internal Developer Portal (IDP) gebouwd op Backstage. Ze vergrendelden de AWS IAM permissies rücksichtslos (locked down), en zorgden ervoor dat werkelijk niemand meer handmatig een server kon aanzetten (provision). Als het operations team vanaf nu lokaal een gloednieuw, AI-gegenereerd dashboard in elkaar had geklikt, moésten ze verplicht op de knop "Create Dashboard" klikken in het nieuwe portaal (IDP). 

De IDP spinde volautomatisch een kogelvrije, streng beveiligde Vercel omgeving op, plus een strakke GitHub repository, voorzien van keurig voorgeconfigureerde API endpoints. Deze endpoints konden de database louter *uitlezen* (read-only), absoluut niet wegschrijven, en bovendien uitsluitend verbinden met een veilige read-replica database in plaats van de live-productie omgeving. 
Toen het operations team probeerde hun knullige, lokaal gegenereerde AI code in de repository te plakken, trapte de geautomatiseerde LaunchStudio CI/CD pijplijn genadeloos op de rem (blocked it). Het detecteerde feilloos het levensgevaarlijke, hardcoded database wachtwoord, blokkeerde de release direct, en dwóng de manager meedogenloos om louter veilige, onzichtbare environment variables te gebruiken.

**Resultaat:** De gigantische shadow IT crisis was direct, 100% geneutraliseerd. Het enthousiaste operations team kon onverminderd doorgaan met het in elkaar knutselen van handige interne tooltjes met AI, maar dan wél strak gebonden binnenin een wiskundig kogelvrije, afgesloten zandbak (sandbox). Mark had per direct weer de volledige, geruststellende controle en zichtbaarheid (visibility) over zijn cloud architectuur, en de torenhoge AWS-factuur kelderde bliksemsnel terug naar de originele, normale baseline. Het Rotterdamse bedrijf ontweek, nét op tijd, een catastrofaal, mogelijk failliet-verklarend datalek.

> *"Die hippe AI coding tools toverden mijn totaal niet-technische staf letterlijk overnight om in een leger aan software developers. Dat was geniaal voor de business, maar een complete, zenuwslopende horrortrip voor de security. LaunchStudio bouwde de loeistrakke platform engineering vangrails (guardrails) die we wanhopig nodig hadden. Nu kan mijn voltallige team lachend met AI bouwen wat ze maar willen, en ik kan 's nachts eindelijk weer gewoon slapen in de absolute wetenschap dat de onderliggende infrastructuur niet plotsklaps instort."*
> — **Mark van Dijk, VP of Engineering, LogiTech Solutions (Rotterdam)**

**Kosten & Tijdlijn:** €9.500 (Launch & Grow Pakket, zwaar opgetuigd met de extreem robuuste Platform Engineering & IDP Add-on) — productie-klaar, kogelvrij beveiligd en live in exact 20 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### (Scenario: CTO die de output van tientallen junior developers moet managen) Hoe voorkom ik in godsnaam dat junior developers dagelijks onveilige en volstrekt kwetsbare AI-gegenereerde code mergen (toevoegen)?

Je kán simpelweg niet langer blijven vertrouwen op trage, handmatige (manual) code reviews; de pure, massieve berg aan code die AI genereert is vele malen te groot. Je móét verplicht geautomatiseerde CI/CD vangrails (guardrails) implementeren. LaunchStudio configureert loeistrenge pipelines vol onverbiddelijke tools zoals SonarQube (voor code quality), Snyk (voor diepe dependency vulnerabilities), en TruffleHog (voor het razendsnel scannen op hardcoded secrets). Als de door AI uitgespuugde code ook maar faalt op één van deze loeistrenge tests, wordt het fysiek en rücksichtslos geblokkeerd (blocked from merging). Klaar.

### (Scenario: VP Engineering die tientallen AI-tools overweegt) Moet ik mijn complete development team simpelweg verplichten (forcen) om slechts één, zwaarbeveiligde AI coding tool (zoals GitHub Copilot) te gebruiken voor de veiligheid?

Hoewel de extreem dure Enterprise tools (zoals Copilot Enterprise) zeker fraaie IP indemnification (garanties) en strikte zero-data-retention regels bieden, is de harde realiteit dat developers onder druk tóg altijd stiekem code kopiëren-plakken (copy-paste) uit de standaard ChatGPT of Claude. De enige, werkelijk veilige en werkbare methode is compleet tool-agnostisch (tool-agnostic): ga er domweg vanuit dat werkelijk álle code fundamenteel wantrouwig (untrusted) is, ongeacht wélke hippe AI het gegenereerd heeft. Dwing de loeistrenge security puur af op het állerhoogste repository niveau (via een IDP en genadeloze CI/CD pipelines), in plaats van dat je hopeloos de politie-agent probeert te spelen over in welk AI-chatvenstertje jouw developer precies aan het typen is.

### (Scenario: Operations Manager die dolgraag zélf interne tools wil bouwen) Ik ben zelf absoluut géén engineer, maar ik wil razendsnel een handige interne tool in elkaar klikken voor mijn team. Hoe pak ik dit volkomen veilig aan?

Stap direct naar je eigen engineering team (of LaunchStudio) en eis (request) een zogeheten "IDP scaffold" (een voorbereide zandbak). Deze scaffold biedt jou een kogelvrije, voorgeconfigureerde, compleet afgeschermde test-omgeving (environment) waar jij veilig én vrolijk al jouw door AI gegenereerde code in mag plakken. Dít krachtige mechanisme garandeert simpelweg dat jij he-le-maal niet per ongeluk de live-database van het bedrijf openstelt voor Russische hackers, óf onbedoeld vitale API-sleutels op straat gooit (leaking). Hierdoor mag jij je 100% concentreren op het simpelweg uittypen van de pure business logic en het fixen van je eigen probleem.

### (Scenario: Technische founder in de groei-fase) Bij exact welke bedrijfsomvang (size) of aantal developers heeft mijn snelgroeiende SaaS startup eigenlijk een Internal Developer Portal (IDP) nodig?

Ver voor de revolutie van AI, bouwden bedrijven pas een IDP wanneer ze rond de 100+ engineers zaten. Vandaag de dag is dat compleet anders. Omdat een lokaal teampje van amper 5 man anno 2026 via AI het gigantische code-volume van 50 full-time engineers kan wegtypen, breekt de governance (toezicht) al in een bizar vroeg stadium volledig doormidden. Wij adviseren snoeihard om op z'n minst de fundamentele, basale IDP scaffolding én de allerstrengste CI/CD vangrails (guardrails) in te richten op het exacte, eerste moment dat jij je állereerste "non-founding" werknemer inhuurt, óf zodra je niet-technische staf (zoals support of marketing) toestaat om ook maar één regel code aan te raken.

### (Scenario: Security Engineer die een security audit doet op AI) Bevat AI-gegenereerde code eigenlijk wezenlijk ándere, unieke security kwetsbaarheden (vulnerabilities) ten opzichte van door mensen geschreven code?

Ja, 100% absoluut. Taalmodellen (LLM's) lijden chronisch aan zogeheten "hallucinated dependencies" (het in de code volkomen verzinnen (hallucineren) van de naam van een software-bibliotheek (library) die in de echte wereld he-le-maal niet bestaat). Kwade hackers (malicious actors) monitoren dit lachwekkende gedrag van AI-modellen zéér agressief, en registreren deze volledig verzonnen (fake) package-namen bliksemsnel op npm of PyPI, waarbij ze deze volproppen met dodelijke malware. Op het rampzalige moment dat jouw onwetende developer's verse AI-code probeert om dat gehallucineerde pakketje braaf te installeren (npm install), is je voltallige, corporate server per direct gecompromitteerd en gegijzeld. De strakke, geautomatiseerde SCA-pipelines (Software Composition Analysis) van LaunchStudio scannen extreem agressief, heel specifiek (specifically), en loeihard op dít soort beruchte, hypermoderne supply-chain attacks, en blokkeren ze meedogenloos voordat ze het daglicht überhaupt kunnen zien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat junior developers levensgevaarlijke, AI-gegenereerde code toevoegen (mergen)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Handmatige code reviews schalen domweg niet meer door het enorme volume van AI. Je móét volautomatische CI/CD vangrails (guardrails) implementeren. LaunchStudio configureert SAST, SCA en secret-scanning tools. Faalt de AI code? Dan wordt de pull request automatisch geblokkeerd."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik mijn team verplichten om slechts één, zwaarbeveiligde AI coding tool (zoals Copilot) te gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hoewel enterprise tools beter beschermen (IP protection), is een tool-agnostische benadering het veiligst: beschouw álle code simpelweg als wantrouwig (untrusted). Dwing loeistrakke security af op repository-niveau via een IDP en CI/CD pijplijnen, in plaats van te jagen op welk chatvenster de developer open heeft staan."
      }
    },
    {
      "@type": "Question",
      "name": "Ik ben geen engineer, maar wil zélf een tool voor mijn team bouwen met AI. Hoe doe ik dit veilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag je engineering team (of LaunchStudio) om een 'IDP scaffold'. Deze voorgeconfigureerde, veilige zandbak (sandbox) stelt je in staat om de door AI gegenereerde code zonder zorgen te plakken, zónder dat je per ongeluk databases openzet of vitale API-keys lekt (leaking)."
      }
    },
    {
      "@type": "Question",
      "name": "Bij welke bedrijfsgrootte heeft een tech-startup eigenlijk een Internal Developer Portal (IDP) nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vroeger pas bij 100 engineers. Omdat een team van 5 nu via AI het code-volume genereert van 50 man, breekt de governance bizar vroeg af. Bouw fundamentele IDP scaffolding zodra je niet-technische staf (of externe developers) toestaat om lokaal code te dragen."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft AI-gegenereerde code echt héél andere security kwetsbaarheden (vulnerabilities) dan mensen-code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. AI modellen hallucineren (verzinnen) vaak pakketjes (dependencies) die he-le-maal niet bestaan. Hackers claimen deze neppe namen op npm en injecteren ze met malware. LaunchStudio's geautomatiseerde SCA-pipelines scannen extreem specifiek op dit soort dodelijke supply-chain aanvallen."
      }
    }
  ]
}
</script>
