---
Titel: "Waarom Ontwikkelaars AI Gebruiken Om Code Te Genereren Maar Mensen Om Het Te Beheren"
Trefwoorden: gebruik AI om code te genereren, AI kan coderen, AI code governance, LaunchStudio, Manifera
Koperfase: Overweging
Doelpersona: VP of Engineering / CTO
---

# Waarom Ontwikkelaars AI Gebruiken Om Code Te Genereren Maar Mensen Om Het Te Beheren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gebruik AI Voor Codegeneratie, Gebruik Mensen Voor Governance: De Opkomst van het Internal Developer Portal",
  "description": "Wanneer iedereen in uw organisatie AI kan gebruiken om code te genereren, explodeert de technische schuld. Een diepgaande gids over hoe engineering teams Internal Developer Portals (IDP's) inzetten om AI Shadow IT te beheersen.",
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
  "datePublished": "2026-12-05",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/use-ai-to-generate-code"
  }
}
</script>

Dat AI kan programmeren is in 2026 geen discussiepunt meer; het is een alledaagse realiteit. Junior ontwikkelaars, productmanagers en operationeel leidinggevenden gebruiken dagelijks AI-tools om software te genereren: dashboards, verwerkingsscripts en marketingautomatiseringen worden in recordtijd gebouwd.

Voor een VP of Engineering is deze democratisering van softwareontwikkeling echter een tweesnijdend zwaard. De productiviteit ligt historisch hoog, maar de governance is op veel plekken volledig ingestort.

Wanneer code buiten gestructureerde engineering-pijplijnen om met AI wordt gegenereerd, ontstaat er gevaarlijke *"Shadow IT"*. Een operationeel manager bouwt met Lovable een planningstool die rechtstreeks verbinding maakt met de productiedatabase via een hardcoded hoofdwachtwoord. Een junior developer genereert met Cursor een component van 2.000 regels die elke security- en toegankelijkheidsstandaard binnen het bedrijf met voeten treedt.

U kunt medewerkers niet verbieden AI te gebruiken; dan doen ze het stiekem op privélaptops. De enige duurzame oplossing is: omarm de snelheid van AI-generatie, maar dwing strikte, geautomatiseerde menselijke governance af. Dit gebeurt via een **Internal Developer Portal (IDP)**.

## De Drie Gevaren van Onbeheerde AI-Codegeneratie

### 1. De Wildgroei aan Geheimen (Secrets Sprawl)
AI-modellen begrijpen het concept van afgeschermde omgevingsvariabelen (`.env`) niet automatisch tenzij hier specifiek om wordt gevraagd. Wanneer niet-technische medewerkers scripts genereren, plaatst de AI vaak geheime API-sleutels (Stripe, AWS, OpenAI) rechtstreeks hardcoded in de broncode. Deze bestanden worden vervolgens gedeeld in Slack of gepusht naar openbare repositories, met acute datalekken tot gevolg.

### 2. De Nachtmerrie van Geïnfecteerde Packages
AI-modellen hallucineren regelmatig pakketnamen op npm of PyPI, of importeren ernstig verouderde bibliotheken met bekende kwetsbaarheden (RCE). Als een intern AI-script met een onveilig pakket wordt uitgerold, staat de deur naar het bedrijfsnetwerk wijd open.

### 3. Het Omzeilen van de Architectuur
Enterprise software-architectuur vereist duidelijke grenzen: de frontend communiceert met een API-gateway, die praat met microservices, die vervolgens gecontroleerd de database aanspreken. AI-codegeneratoren kiezen altijd de weg van de minste weerstand: ze schrijven gerust een React-frontend die via een ongecontroleerde query direct de PostgreSQL-hoofddatabase benadert, waardoor alle logging en rate limits worden omzeild.

## De Oplossing: Internal Developer Portals (IDP's)

Om AI-codegeneratie veilig te kanaliseren, implementeren vooruitstrevende engineering-teams een Internal Developer Portal (zoals Backstage of Port). Een IDP fungeert als een beveiligde sluis: *"Iedereen mag AI gebruiken om te bouwen wat hij wil, maar om het op een bedrijfsserver te krijgen, moet het door dit portaal."*

### 1. Geautomatiseerde CI/CD-Waarborgen
Zodra een medewerker AI-gegenereerde code indient bij het IDP, start een strenge CI/CD-pijplijn. SAST-tools scannen op hardcoded geheimen en SCA-scanners controleren de `package.json` op onveilige bibliotheken. Wordt er een fout ontdekt, dan weigert het systeem de code automatisch en geeft het een kant-en-klare prompt mee waarmee de medewerker de AI de code laat corrigeren.

### 2. Voorgeconfigureerde Omgevingen ("Golden Paths")
In plaats van een medewerker vanaf nul te laten beginnen, biedt het IDP geteste templates ("Golden Paths"). Met één klik krijgt de medewerker een veilige repository inclusief Dockerfiles, authenticatiemodule en database-ORM. De medewerker gebruikt AI vervolgens uitsluitend om de *bedrijfslogica* binnen deze veilige mal te genereren.

### 3. Verplichte API-Gateways
Het IDP levert omgevingen op die fysiek geen directe toegang hebben tot de hoofddatabase. Alle AI-code wordt gedwongen te communiceren via de centrale API-gateway, waardoor Row Level Security en audit-logging altijd gegarandeerd zijn.

## Hoe LaunchStudio AI-Governance Inricht

Het opzetten van een IDP en het configureren van strenge CI/CD-pipelines vereist diepgaande Platform Engineering en DevOps-expertise.

[LaunchStudio](https://launchstudio.eu/en/), aangedreven door de enterprise-engineers van [Manifera](https://www.manifera.com/) onder leiding van Herre Roelevink in Amsterdam en Ho Chi Minhstad, bouwt de fundamenten waarmee organisaties veilig kunnen innoveren met AI:
1. **Repository Templates:** Opzetten van veilige "Golden Paths" voor Next.js, Node.js en Python met enterprise-standaarden.
2. **Geautomatiseerde Beveiligingspijplijnen:** Inrichten van GitHub Actions die AI-hallucinaties, hardcoded sleutels en kwetsbare dependencies automatisch blokkeren.
3. **Infrastructure as Code (IaC):** Beheer van alle cloud-resources via Terraform voor een voorspelbare en veilige cloudomgeving.

## Echt voorbeeld

### Een AI-Native Oprichter in de Praktijk: De Engineering Director Die Voortwoekerende Shadow IT Aanbanden Legde

Mark is VP of Engineering bij een logistiek softwarebedrijf in Rotterdam met 40 ontwikkelaars. Hoewel zijn team zeer productief was, ontdekte hij een zorgwekkende trend: de klantenservice- en operationele teams waren massaal begonnen met het bouwen van eigen tools via Cursor.

Zij bouwden zelf dashboards om zendingen te volgen. In eerste instantie leek dit een mooi initiatief, totdat de maandelijkse AWS-factuur plotseling met €4.000 steeg.

Mark startte een onderzoek en trof een enorme Shadow IT-crisis aan: een servicemanager had een AI-script geschreven dat elke 5 seconden een zware query uitvoerde op de productiedatabase. Het script bevatte het hardcoded hoofdwachtwoord van de database en draaide op een ongepatchte AWS-server die met een bedrijfscreditcard was aangeschaft.

AI verbieden was geen optie — de versnelling voor de business was te groot. Mark schakelde LaunchStudio in voor een waterdicht governance-kader.

Binnen 20 werkdagen richtte het Manifera-team een Internal Developer Portal in op basis van Backstage:
- AWS IAM-rechten werden dichtgezet zodat servers niet meer handmatig konden worden gestart.
- Voor nieuwe dashboards klikten medewerkers simpelweg op "Nieuw Dashboard" in het portaal.
- Het portaal maakte automatisch een beveiligde Vercel-omgeving aan die uitsluitend gekoppeld was aan een veilige read-replica database.
- Zodra medewerkers hun AI-code pushten, blokkeerde de geautomatiseerde CI/CD-pijplijn direct eventuele hardcoded wachtwoorden en dwong het gebruik van veilige omgevingsvariabelen af.

**Resultaat:** De Shadow IT-crisis werd volledig geneutraliseerd. Medewerkers bleven in hoog tempo interne tools bouwen met AI, maar deden dit voortaan binnen een wiskundig veilige zandbak. Mark kreeg weer 100% grip op de infrastructuur, de AWS-factuur normaliseerde en een gigantisch beveiligingslek werd voorkomen.

> *"AI-codetools veranderden niet-technische collega's van de ene op de andere dag in ontwikkelaars. Dat was geweldig voor de business, maar doodeng voor de beveiliging. LaunchStudio bouwde de technische vangrails die we nodig hadden. Nu kan mijn team met AI bouwen wat ze willen, terwijl ik met een gerust hart kan slapen."*
> — **Mark van Dijk, VP of Engineering, LogiTech Solutions (Rotterdam)**

**Kosten & Doorlooptijd:** €9.500 (Launch & Grow Pakket met Platform Engineering & IDP Add-on) — productie-klaar en live binnen 20 werkdagen.

---

## Veelgestelde vragen

### Hoe voorkom ik dat junior developers onveilige AI-gegenereerde code naar productie pushen?
Handmatige code-reviews kunnen het enorme volume aan AI-code niet bijbenen. U heeft geautomatiseerde CI/CD-waarborgen nodig. LaunchStudio configureert pipelines met tools als SonarQube (codekwaliteit), Snyk (kwetsbaarheden in packages) en TruffleHog (lekken van API-sleutels) die onveilige pull requests automatisch fysiek blokkeren.

### Moeten we ons team verplichten één specifieke AI-tool (zoals GitHub Copilot Enterprise) te gebruiken?
Hoewel zakelijke licenties betere juridische garanties bieden, kopiëren ontwikkelaars onvermijdelijk code uit ChatGPT of Claude. De veiligste strategie is daarom tool-agnostisch: ga ervan uit dat alle ingediende code potentieel onveilig is en dwing beveiliging af op repository- en CI/CD-niveau via een IDP.

### Ik ben geen engineer maar wil een interne tool bouwen voor mijn team. Hoe doe ik dat veilig?
Vraag een goedgekeurde IDP-template ("Golden Path") aan bij uw engineeringteam of LaunchStudio. Deze template bevat een kant-en-klare, beveiligde basis waarin u veilig uw AI-gegenereerde code kunt plakken, zonder dat u per ongeluk databases blootstelt of API-sleutels lekt.

### Vanaf welke teamgrootte heeft een startup een Internal Developer Portal (IDP) nodig?
Vóór het AI-tijdperk was een IDP pas nodig vanaf 100 ontwikkelaars. Omdat een team van 5 mensen met AI tegenwoordig evenveel code genereert als vroeger 50 mensen, ontstaat de noodzaak veel eerder. Wij adviseren basis-IDP vangrails in te richten zodra niet-technische collega's of junior engineers code gaan bijdragen.

### Bevat AI-gegenereerde code unieke kwetsbaarheden vergeleken met menselijke code?
Ja. AI-modellen lijden regelmatig aan "gehallucineerde packages" (het verzinnen van niet-bestaande bibliotheeknamen). Hackers registreren deze verzonnen namen met malware op npm of PyPI. Als uw AI-script dit pakket vervolgens installeert, is uw netwerk direct geïnfecteerd. LaunchStudio's SCA-pipelines scannen specifiek op dit type supply-chain aanvallen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat junior developers onveilige AI-gegenereerde code naar productie pushen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via geautomatiseerde CI/CD-pipelines met SAST-, SCA- en secret-scanning tools die onveilige AI-code automatisch blokkeren vóór de merge."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten we ons team verplichten één specifieke AI-tool te gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beter is een tool-agnostische aanpak: ga ervan uit dat alle code onbetrouwbaar is en dwing beveiliging af op repository-niveau via een IDP."
      }
    },
    {
      "@type": "Question",
      "name": "Ik ben geen engineer maar wil een interne tool bouwen voor mijn team. Hoe doe ik dat veilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik een voorgeconfigureerd 'Golden Path' template via een IDP waarin authenticatie en databeveiliging al waterdicht zijn ingericht."
      }
    },
    {
      "@type": "Question",
      "name": "Vanaf welke teamgrootte heeft een startup een Internal Developer Portal (IDP) nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodra niet-programmeurs of junior ontwikkelaars met AI gaan bouwen, omdat het gegenereerde codevolume governance direct noodzakelijk maakt."
      }
    },
    {
      "@type": "Question",
      "name": "Bevat AI-gegenereerde code unieke kwetsbaarheden vergeleken met menselijke code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, gehallucineerde npm/pip packages worden door kwaadwillenden gekaapt voor malware. Onze geautomatiseerde SCA-scans weren deze aanvallen af."
      }
    }
  ]
}
</script>
