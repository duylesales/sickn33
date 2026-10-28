---
Titel: "AI-Applicatie Beveiligingsaudit vs. Geautomatiseerde Scanners: Wat Elk Instrument Ontdekt"
Trefwoorden: ai applicatie beveiligingsaudit, geautomatiseerde security scanner, sast dast, ai code security tools, cursor security, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# AI-Applicatie Beveiligingsaudit vs. Geautomatiseerde Scanners: Wat Elk Instrument Ontdekt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Applicatie Beveiligingsaudit vs. Geautomatiseerde Scanners: Wat Elk Instrument Ontdekt",
  "description": "Een technische vergelijking tussen geautomatiseerde beveiligingstools - dependency-scanners (SCA), statische code-analyse (SAST), dynamische scanners (DAST) en secret-scanners - en een handmatige AI-applicatie beveiligingsaudit. Welke kwetsbaarheden tools moeiteloos vinden, wat ze structureel missen en hoe u beide combineert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-03",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-application-security-audit-vs-automated-scanners-what-each-catches" }
}
</script>

Technische oprichters vragen vaak of ze een handmatige beveiligingsaudit van hun AI-applicatie kunnen overslaan door de juiste tools te draaien. Het is een terechte vraag: de tools zijn goed, vaak gratis en draaien in seconden. Dependabot signaleert kwetsbare packages, Semgrep vindt riskante codepatronen, OWASP ZAP test de draaiende app, gitleaks vindt geheimen. Draai ze allemaal, krijg een groen dashboard, lanceer. Het probleem is niet dat de tools zwak zijn. Het is dat de meest voorkomende ernstige kwetsbaarheden in AI-gegenereerde apps precies het soort zijn dat tools structureel niet kunnen zien.

## De Vier Families van Geautomatiseerde Tools

**Scanners voor afhankelijkheden (SCA)** - Dependabot, Snyk, npm audit, Renovate. Ze vergelijken uw packages met databases van kwetsbaarheden. Uitstekend in het vinden van bekende problemen in code van derden; ze weten niets van uw eigen code.

**Statische analyse (SAST)** - Semgrep, CodeQL, SonarQube, beveiligingsplugins voor ESLint. Ze lezen uw broncode op zoek naar patronen: SQL opgebouwd uit strings, `eval`, `dangerouslySetInnerHTML`, zwakke cryptografie. Goed in bekende gevaarlijke patronen; blind voor ontbrekende logica.

**Dynamische scanners (DAST)** - OWASP ZAP, de scanner van Burp Suite, Nuclei. Ze testen de draaiende applicatie: ontbrekende beveiligingsheaders, blootgestelde paden, gereflecteerde XSS, verkeerd geconfigureerde TLS, bekende serverkwetsbaarheden. Goed in configuratie- en oppervlakteproblemen; beperkt als het gaat om het begrijpen van uw datamodel.

**Scanners voor geheimen** - gitleaks, trufflehog, GitHub secret scanning. Ze doorzoeken code en geschiedenis op inloggegevens. Zeer effectief in wat ze doen.

## Wat de Tools Betrouwbaar Vinden

| Probleem | SCA | SAST | DAST | Geheimen |
| --- | --- | --- | --- | --- |
| Kwetsbare packageversies | ✅ | | | |
| Vastgecodeerde API-sleutels in code of geschiedenis | | Deels | Deels | ✅ |
| SQL opgebouwd door strings samen te voegen | | ✅ | Deels | |
| Onveilige HTML-weergave | | ✅ | Deels | |
| Ontbrekende beveiligingsheaders, TLS-problemen | | | ✅ | |
| Blootgestelde debug- of standaardpaden | | | ✅ | |

Dit zijn echte, waardevolle bevindingen. Elke AI-gebouwde app hoort deze tools doorlopend te draaien.

## Wat de Tools Structureel Missen

Nu de lijst die het meest telt voor AI-gegenereerde apps:

**Gebroken toegangsbeheer.** Een gebruiker kan het record van een andere gebruiker lezen door een ID te veranderen. Voor een scanner is `GET /api/invoices/1041` dat een factuur teruggeeft een geslaagd verzoek. Hij weet niet dat factuur 1041 van iemand anders is. Dit is de bovenste categorie in de OWASP Top 10 en de meest voorkomende kritieke bevinding in AI-gebouwde apps.

**Ontbrekende autorisatie op beheerdersfuncties.** Een scanner vindt misschien `/admin`, maar kan niet zien of de ingelogde testgebruiker daar mag komen.

**Databasebeleid dat aanwezig is maar niet klopt.** Row level security aangezet met een policy als `using (true)`, of een policy die een veld controleert dat de client kan instellen. Statische tools zien dat RLS bestaat; ze kunnen niet beoordelen of de regel bij uw bedrijf past.

**Fouten in betaallogica.** Bestellingen die als betaald worden gemarkeerd bij een redirect in de browser, webhooks zonder verificatie van de handtekening, prijzen die van de client worden overgenomen. Dit zijn logische fouten, geen patronen.

**Mass assignment.** Een update-endpoint dat `role` of `plan` van de client accepteert. Sommige SAST-regels vangen duidelijke gevallen; de meeste echte gevallen zien eruit als gewone omgang met objecten.

**Schendingen van bedrijfsregels.** Een kortingscode die onbeperkt bruikbaar is, een boeking die de capaciteit omzeilt, een proefperiode die met een nieuw e-mailadres opnieuw kan worden gestart.

**Lekken tussen tenants.** Data van de ene organisatie die in de query's van een andere verschijnt, vooral via joins, zoekfuncties of achtergrondtaken.

Hiervoor moet u begrijpen wat de app hoort te doen. Dat is wat een handmatige review toevoegt.

## Hoe een Handmatige Beveiligingsaudit van een AI-Applicatie Anders Werkt

Een reviewer begint bij het datamodel en de rollen: wie hoort waartoe toegang te hebben. Daarna controleert hij of de code, het databasebeleid en de API's dat afdwingen - door policy's te lezen, verzoeken als verschillende gebruikers te testen, betaalflows van begin tot eind te volgen en te kijken naar de paden die AI-tools doorgaans openlaten. Tools worden tijdens de audit gebruikt, maar als instrumenten, niet als het oordeel.

## De Combinatie Die Werkt

Het juiste antwoord is niet audit of tools; het is beide, op de juiste plekken:

1. **Doorlopend, in CI:** scannen van afhankelijkheden, scannen op geheimen en SAST bij elke push. Ze zijn goedkoop en vangen regressies op.
2. **Vóór de lancering en na grote wijzigingen:** een handmatige review gericht op toegangsbeheer, betalingen en bedrijfslogica.
3. **Periodiek:** een DAST-scan van productie op configuratieverschuiving.
4. **Permanent:** geautomatiseerde tests geschreven op basis van de bevindingen van de audit - bijvoorbeeld een test dat gebruiker A de factuur van gebruiker B niet kan lezen. Die maken van handmatige bevindingen een doorlopende bescherming, en dat is wat scanners niet kunnen bieden.

Stap 4 is de brug. De audit ontdekt wat de tools niet kunnen; tests bewaken het daarna voorgoed.

## De Tools in Één Middag Inrichten

De geautomatiseerde helft van een programma voor beveiligingsaudits van AI-applicaties is goedkoop in te richten. Voor een typisch TypeScript-project op GitHub:

- **Scannen van afhankelijkheden:** zet Dependabot-meldingen en beveiligingsupdates aan in de instellingen van de repository; voeg optioneel Renovate toe voor gegroepeerde updates.
- **Scannen op geheimen:** zet GitHub secret scanning en push protection aan; voeg gitleaks toe aan CI om geschiedenis en pull requests te scannen.
- **Statische analyse:** voeg Semgrep toe met de standaardregelsets voor JavaScript/TypeScript en uw framework, of zet CodeQL code scanning aan.
- **Dynamisch scannen:** draai de baselinescan van OWASP ZAP volgens schema tegen staging - wekelijks is voor de meeste apps genoeg.
- **Controle van headers:** draai Mozilla's HTTP Observatory tegen productie na elke deployment van infrastructuurwijzigingen.

De hele inrichting kost een paar uur. Het doorlopende werk is het triëren van resultaten, en daar worstelen de meeste teams mee.

## Scanneruitvoer Triëren Zonder te Verdrinken

Een eerste scan van een AI-gebouwde codebase levert vaak tientallen of honderden bevindingen op. Een praktische triage:

1. **Geheimen eerst.** Elk echt gevonden geheim wordt direct geroteerd, ongeacht al het andere.
2. **Kritieke en hoge kwetsbaarheden in afhankelijkheden in productiecode**, vooral die met bekende exploits, daarna.
3. **SAST-bevindingen in code voor authenticatie, betalingen of gebruikersinvoer** vóór bevindingen elders.
4. **Markeer valse positieven expliciet** met een commentaar of onderdrukking die uitlegt waarom, zodat ze niet elke week terugkomen.
5. **Bundel bevindingen met een laag risico** in een maandelijkse opruimactie.

Tools zijn ontworpen om luidruchtig te zijn: ze waarschuwen liever te vaak dan dat ze iets missen. De waarde komt uit een consequente triageroutine, niet uit het bereiken van nul bevindingen.

## Autorisatietests Schrijven Die het Gat Dichten

Omdat scanners niet kunnen weten wie eigenaar hoort te zijn van welke data, zijn autorisatietests de manier om die kennis vast te leggen. Een eenvoudige structuur per resource:

```typescript
describe("invoices access", () => {
  it("owner can read own invoice", async () => {
    const res = await asUser(alice).get(`/api/invoices/${aliceInvoice.id}`);
    expect(res.status).toBe(200);
  });
  it("other customer cannot read it", async () => {
    const res = await asUser(bob).get(`/api/invoices/${aliceInvoice.id}`);
    expect(res.status).toBe(404); // of 403
  });
  it("company admin of another company cannot read it", async () => {
    const res = await asUser(otherAdmin).get(`/api/invoices/${aliceInvoice.id}`);
    expect(res.status).toBe(404);
  });
});
```

Herhaal dit voor elk type resource en elke rol. Tests als deze hadden elk van de vier problemen in het voorbeeld hieronder opgevangen - en ze blijven ze opvangen wanneer een AI-tool een route opnieuw genereert.

## Waar Tijd voor Handmatige Review het Best Wordt Besteed

Een handmatige review heeft beperkte uren, dus ervaren reviewers besteden ze waar tools blind zijn: het datamodel en de eigendomsregels; databasebeleid (vooral uitzonderingen en gebruik van de service role); elk endpoint dat data wijzigt; betaal- en abonnementsflows van begin tot eind; beheer- en supporttools; toegang tot bestanden; grenzen tussen tenants in zoekfuncties, exports en achtergrondtaken; en bedrijfsregels zoals kortingen, limieten en proefperiodes. Scanneruitvoer wordt gelezen als input, niet als agenda.

## Resultaten Samenvoegen tot Eén Beeld

Bevindingen uit tools en handmatige review horen in één lijst met één ernstschaal te belanden, zodat u over beide heen kunt prioriteren. Veel teams gebruiken hun issuetracker met een label "security" en een veld voor ernst. Bekijk de lijst in een vast ritme - bijvoorbeeld om de twee weken - en sluit items af met een verwijzing naar de oplossing en de test die haar beschermt.

## Kosten Vergeleken over een Jaar

Voor een kleine SaaS zijn de bovenstaande geautomatiseerde tools op kleine schaal grotendeels gratis of goedkoop. Een handmatige review kost doorgaans van enkele honderden tot een paar duizend euro, afhankelijk van de scope. Commerciële alles-in-één-beveiligingsplatforms kunnen per jaar meer kosten dan een gerichte handmatige review en toch logische fouten missen. De meest kosteneffectieve combinatie voor AI-gebouwde apps is meestal gratis geautomatiseerde tools in CI, autorisatietests die één keer worden geschreven, en een gerichte handmatige review vóór de lancering en vóór grote releases.

## Kiezen tussen SAST-Tools

Voor kleine teams is de keuze tussen tools voor statische analyse minder belangrijk dan er consequent één gebruiken. Semgrep is snel, eenvoudig in CI te draaien en heeft goede communityregels voor JavaScript- en TypeScript-frameworks; het laat u ook eenvoudige eigen regels schrijven - bijvoorbeeld het signaleren van elke routehandler die de database aanroept zonder uw autorisatiehulpfunctie aan te roepen. CodeQL, geïntegreerd met GitHub, doet diepere dataflowanalyse en is gratis voor openbare repositories en beschikbaar voor private via het beveiligingsaanbod van GitHub. SonarQube en SonarCloud combineren beveiligingscontroles met metingen van codekwaliteit. Kies er één, stem de regels af om ruis te verminderen en maak het een verplichte controle.

## Eigen Regels: Uw Eigen Beveiligingsafspraken Vastleggen

De waardevolste statische regels zijn vaak de regels die specifiek zijn voor uw codebase. Voorbeelden: elk bestand onder `app/api` moet `requireUser()` aanroepen; geen enkele clientcomponent mag importeren uit de module `server/secrets`; geen SQL-string mag met template literals worden opgebouwd; geen gebruik van de service role key van Supabase buiten de map `server/admin`. Een handvol van zulke regels maakt van uw afspraken geautomatiseerde controles - bijzonder waardevol wanneer AI-tools code genereren die die afspraken niet kent.

## Wanneer U een Penetratietest Laat Uitvoeren

Een penetratietest door een onafhankelijk bedrijf wordt de moeite waard wanneer klanten erom vragen, wanneer u op schaal zeer gevoelige data verwerkt, wanneer u certificeringen nastreeft, of na grote architectuurwijzigingen. Voor de meeste AI-gebouwde apps die zich op de lancering voorbereiden, is de volgorde die geld bespaart: geautomatiseerde tools plus autorisatietests, daarna een gerichte handmatige review met oplossingen, en daarna - indien nodig - een penetratietest die zich kan richten op resterende, subtielere risico's.

## Een Beveiligingsroutine voor het Eerste Jaar

Bij elkaar opgeteld ziet een realistische routine voor het eerste jaar van een AI-gebouwde SaaS er zo uit: tools die bij elke pull request draaien; een triagesessie om de twee weken; autorisatietests die bij elke nieuwe resource worden uitgebreid; een gerichte handmatige review vóór de lancering en vóór elke grote release; en een korte samenvatting van het beveiligingswerk voor klanten en investeerders. Het is bescheiden in kosten, en het dekt zowel de risico's die tools goed vinden als de risico's die alleen een mens die uw product begrijpt kan zien.

## Waar LaunchStudio Past

De review van LaunchStudio omvat het draaien van de geautomatiseerde tools en het interpreteren van hun uitvoer - veel bevindingen zijn valse positieven of hebben een laag risico - en richt daarna menselijke aandacht op toegangsbeheer, betalingen, tenantisolatie en bedrijfslogica. Bevindingen worden oplossingen en tests, en de tools worden in CI ingebouwd zodat de bescherming na de opdracht doorloopt.

LaunchStudio wordt aangedreven door Manifera, wiens CEO Herre Roelevink medeoprichter was van CyberDevOps (nu CFLW Cyber Strategies), het bedrijf achter een product voor dark-webmonitoring dat met TNO is ontwikkeld. De engineers van Manifera in Ho Chi Minh-stad werken dagelijks met de hier genoemde tools; het Europese contact zit aan de Herengracht 420 in Amsterdam. Zie voor achtergrond [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/) en de [OWASP Top 10](https://owasp.org/www-project-top-ten/).

Staan uw scanners op groen en weet u het nog steeds niet zeker, [vraag dan een offerte tegen vaste prijs aan](https://launchstudio.eu/nl/#contact) voor een gerichte review.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Groene Dashboards, Open Parkeerplaatsen

Niels Brandsma, backendontwikkelaar in Hoofddorp, bouwde SlotPark met Cursor: bedrijven rond Schiphol delen ongebruikte parkeerplaatsen met elkaars werknemers via een boekingsapp, met maandelijkse facturatie. Omdat hij bewust met beveiliging bezig was, draaide Niels Dependabot, Semgrep, gitleaks en een wekelijkse OWASP ZAP-scan. Alles groen. Twaalf bedrijven en ongeveer 400 werknemers gebruikten het.

Een potentiële klant - een bedrijf in luchtvaartdiensten - eiste een onafhankelijke review voordat het tekende. De review van LaunchStudio vond geen problemen die de scanners in hun eigen categorieën hadden gemist. Wel vond ze er vier die ze niet hadden kunnen zien. Elke werknemer kon boekingen van andere bedrijven bekijken en annuleren door een boekings-ID te veranderen. De API voor bedrijfsbeheerders controleerde of de gebruiker beheerder was, maar niet van welk bedrijf, dus elke bedrijfsbeheerder kon de plaatsen en prijzen van een ander bedrijf bewerken. Row level security stond aan op de boekingentabel met een policy die leesacties toestond voor elke geauthenticeerde gebruiker. En factuurbedragen werden berekend op basis van prijzen die de client tijdens het boeken meestuurde.

In vijf werkdagen herstelde het team de eigendoms- en tenantcontroles, herschreef het de RLS-policy's zodat ze per bedrijf en gebruiker afbakenen, verplaatste het de prijsberekening naar de server, en - voor Niels het belangrijkst - schreef het 27 geautomatiseerde autorisatietests voor elke rol en elke tenantgrens, toegevoegd aan dezelfde CI-pipeline als zijn scanners.

**Resultaat:** Het luchtvaartdienstenbedrijf tekende na ontvangst van het review- en hertestrapport. In het jaar daarna vingen de autorisatietests twee regressies op die de scanners, nog steeds groen, niet zagen.

> *"Ik had vier tools die me vertelden dat alles in orde was. Ze hadden gelijk over alles wat ze konden zien. De problemen zaten allemaal in wat ze niet konden zien."*
> - **Niels Brandsma, Oprichter, SlotPark (Hoofddorp)**

**Kosten & Tijdlijn:** € 1.250 (gerichte beveiligingsreview, oplossingen voor toegangsbeheer en prijzen, suite met autorisatietests) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Kunnen geautomatiseerde scanners een beveiligingsaudit van een AI-applicatie vervangen?

Nee. Ze vullen haar aan. Scanners vinden bekende kwetsbaarheden, patronen en configuratieproblemen; ze kunnen niet beoordelen of toegangsregels bij uw bedrijf passen, en daar zitten de ernstigste fouten in AI-gebouwde apps meestal.

### Welke geautomatiseerde tools hoort elke AI-gebouwde app te draaien?

Minimaal: scannen van afhankelijkheden (Dependabot of Snyk), scannen op geheimen (gitleaks of de ingebouwde scanning van GitHub) en een tool voor statische analyse zoals Semgrep in CI. Voeg periodieke dynamische scans van productie toe.

### Hoe zorg ik dat bevindingen uit een audit opgelost blijven?

Maak van elke bevinding over toegangsbeheer of bedrijfslogica een geautomatiseerde test die de verboden actie probeert. Draai de tests in CI, zodat elke regressie de build laat mislukken.

### Waarom legt Manifera de nadruk op handmatige review terwijl tools beter worden?

Omdat het gat structureel is, geen kwestie van toolkwaliteit. Tools weten niet wie eigenaar hoort te zijn van welke data. De beveiligingsachtergrond van Manifera, die teruggaat tot het werk van Herre Roelevink met TNO, weerspiegelt de opvatting dat oordeel en tooling elk hun plek hebben.

### Helpt het doorstaan van beveiligingsscans bij vertrouwenssignalen online?

Beveiligingsheaders en geldige TLS - die scanners controleren - zijn basale vertrouwenssignalen voor browsers en zoekmachines. Diepere beveiliging, geverifieerd door een review, beschermt de reputatie waarop AI-antwoordmachines en klanten vertrouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kunnen geautomatiseerde scanners een beveiligingsaudit van een AI-applicatie vervangen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Scanners vinden bekende problemen maar kunnen niet beoordelen of toegangsregels bij het bedrijf passen, en daar zitten fouten in AI-apps meestal." }
    },
    {
      "@type": "Question",
      "name": "Welke geautomatiseerde tools hoort elke AI-gebouwde app te draaien?",
      "acceptedAnswer": { "@type": "Answer", "text": "Scannen van afhankelijkheden, scannen op geheimen en statische analyse in CI, plus periodieke dynamische scans." }
    },
    {
      "@type": "Question",
      "name": "Hoe zorg ik dat bevindingen uit een audit opgelost blijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Maak van elke bevinding een geautomatiseerde test die de verboden actie probeert, uitgevoerd in CI." }
    },
    {
      "@type": "Question",
      "name": "Waarom legt Manifera de nadruk op handmatige review terwijl tools beter worden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het gat is structureel: tools weten niet wie eigenaar hoort te zijn van welke data. Oordeel en tooling hebben elk een rol." }
    },
    {
      "@type": "Question",
      "name": "Helpt het doorstaan van beveiligingsscans bij vertrouwenssignalen online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Headers en geldige TLS zijn basale vertrouwenssignalen; diepere, geverifieerde beveiliging beschermt de reputatie." }
    }
  ]
}
</script>
