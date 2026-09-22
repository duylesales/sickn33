---
Titel: "Productierijpheid van AI-Gegenereerde Code: Waarom AI-Geschreven Tests Slagen Wanneer Ze Zouden Moeten Falen"
Trefwoorden: ai gegenereerde code productierijpheid, ai gegenereerde code productie, ai geschreven tests, testkwaliteit, mocking, cursor tests, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Productierijpheid van AI-Gegenereerde Code: Waarom AI-Geschreven Tests Slagen Wanneer Ze Zouden Moeten Falen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Productierijpheid van AI-Gegenereerde Code: Waarom AI-Geschreven Tests Slagen Wanneer Ze Zouden Moeten Falen",
  "description": "AI-tools schrijven razendsnel tests en de testdekking (coverage) lijkt geweldig — maar veel AI-geschreven tests mocken het daadwerkelijke gedrag weg, testen de implementatie in plaats van de intentie, of dekken alleen happy paths. Hoe herken je holle tests en bescherm je AI-code in productie.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-29",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-production-readiness-why-ai-written-tests-pass-when-they-shouldnt" }
}
</script>

"We hebben 87% testdekking" is een van de meest geruststellende zinnen die een technische oprichter kan uitspreken over een met AI gebouwde applicatie. Het is tegenwoordig helaas ook een van de minst veelzeggende. AI-codeertools genereren moeiteloos honderden tests, en testdekkingsrapporten tellen simpelweg welke regels code tijdens de testrun worden aangeraakt. Geen van beide vertelt je echter of die tests daadwerkelijk zouden *falen* als de achterliggende businesslogica fout is. Voor de productierijpheid van AI-gegenereerde code kan een volledig groene testsuite een gevaarlijke schijnzekerheid bieden — en dat merk je vaak pas wanneer een bug die ogenschijnlijk "100% gedekt" was, live klanten raakt.

## De Vier Soorten Holle Tests

**1. De test die precies datgene wegmocket wat hij pretendeert te testen.** Vraag een AI om een functie te testen die een bestelling opslaat en een betaling afschrijft, en de AI mocket zowel de database als de payment-provider weg. Vervolgens test de code alleen of de mock-functies zijn aangeroepen. De test slaagt altijd — ongeacht of de SQL-query klopt, de betalings-payload geldig is of de data überhaupt correct wordt opgeslagen. Het test of functies elkaar aanroepen, niet of het systeem werkt.

**2. De test die de implementatie spiegelt.** Het AI-model leest de bestaande code en schrijft asserts die precies overeenkomen met de huidige output. Als de functie een btw-berekening foutief uitvoert, valideert de test doodleuk die verkeerde uitkomst. De test legt de bug officieel vast als de 'juiste' uitkomst.

**3. De test die alleen het ideale scenario dekt (happy path).** Correcte invoer, ingelogde accounteigenaar, succesvolle betaling. Geen enkele test voor een verlopen sessie, een geweigerde creditcard, een dubbel verzonden webhook of een lege lijst. Juist in die uitzonderingen ontstaan 95% van alle productiestoringen.

**4. De test die onmogelijk kan falen.** Vage assertions zoals `expect(result).toBeDefined()` of `expect(response.status).toBeLessThan(500)`, of tests waarin fouten stilletjes in een `catch`-blok worden opgevangen en genegeerd. Ze voeren code uit en verhogen de dekkingsstatistieken, maar controleren inhoudelijk niets.

Alle vier verhogen ze de 'code coverage' op papier. Geen enkele beschermt jouw applicatie in productie.

## Waarom Holle Tests de Productierijpheid Ondermijnen

AI-modellen zijn getraind om tests te schrijven die slagen; een falende test ziet er in hun optimalisatielus uit als een probleem dat moet worden 'opgelost'. Wanneer de snelste route naar een groene test het wegmocken van een dependency is, dan is dat wat het model doet. Bovendien hebben AI-modellen geen autonoom inzicht in wat jouw bedrijfslogica *behoort* te doen; ze leiden de intentie af uit de code die er al staat.

## Hoe Herken Je Holle Tests Binnen Vijf Minuten?

- **Breek de code met opzet (mutation check).** Pas een vergelijking aan (`>` naar `<`), verwijder een autorisatiecheck of verander een berekening. Draai de testsuite. Als alle tests nog steeds groen zijn, testen ze het gedrag helemaal niet. (Tools voor mutation testing zoals Stryker doen dit automatisch.)
- **Tel het aantal mocks.** Tests waarin gelijktijdig de database, de autorisatielaag en de externe API zijn weggemockt, testen in de praktijk zelden iets relevants.
- **Zoek naar negatieve tests.** Controleer hoeveel tests verwachten dat een verzoek wordt afgewezen: HTTP 401, 403, validatiefouten of geweigerde betalingen. Als er vrijwel geen negatieve tests zijn, is dat een enorm alarmsignaal.
- **Lees de assertions kritisch.** Wordt er gecontroleerd op concrete, betekenisvolle resultaten — het juiste record, het exacte bedrag, de specifieke gebruiker — of enkel of er 'iets' is geretourneerd?

## Hoe Echte Tests voor AI-Gegenereerde Apps Eruitzien

**Test gedrag tegen echte infrastructurele grenzen.** Laat tests voor bedrijfskritieke processen draaien tegen een échte lokale testdatabase (een lokale PostgreSQL- of Supabase-container, of de Firebase emulator) in plaats van alles weg te mocken. Mock uitsluitend externe diensten die je lokaal onmogelijk kunt draaien (zoals Stripe of Resend), en gebruik daarvoor hun officiële testmodi of realistische fakes.

**Schrijf de intentie vóór de code.** Beschrijf in begrijpelijke taal wat er moet gebeuren — *"een lid van team A mag onder geen beding de facturen van team B inzien"* — en laat dáár de test voor schrijven. Laat de AI gerust de boilerplate-code genereren, maar definieer de assertions zelf.

**Geef prioriteit aan negatieve scenario's.** Voor elk beveiligd endpoint: verkeerde gebruiker, niet-ingelogde bezoeker, onbevoegde rol, andere organisatie (multi-tenant isolatie). Voor elke betaling: geweigerd, geannuleerd, dubbele webhook, terugboeking.

**Beheer een compacte, onverwoestbare kernsuite.** Tien tot dertig end-to-end integratietests die registratie, inloggen, datatoegang, betalingen en de kernfunctionaliteit controleren, leveren oneindig veel meer betrouwbaarheid op dan honderden holle unit-tests met mocks.

## Mocks: Wanneer Nuttig en Wanneer Gevaarlijk?

Mocks zijn niet per definitie slecht, zolang je ze op de juiste plek inzet:

| Onderdeel | Mocken? | Beter alternatief voor productie |
| --- | --- | --- |
| Eigen database | Vrijwel nooit | Echte testdatabase (lokale PostgreSQL, Supabase local, emulator) |
| Eigen businesslogica | Nooit | Direct testen tegen echte data |
| Payment provider (bijv. Stripe) | Deels | Officiële Stripe testmodus voor integratietests; mocks alleen voor zeldzame timeouts |
| E-mailprovider (bijv. Resend) | Ja | Lokale SMTP-catcher (bijv. Mailpit) en controleren op e-mailinhoud |
| LLM / AI-model API | Ja, voor determinisme | Vaste test-fixtures (opgeslagen antwoorden) plus periodieke live evaluaties |
| Systeemtijd / Klok | Ja | Fake timers ingesteld op specifieke data (zomertijd/wintertijd) |

De vuistregel: mock wat je niet beheert en niet lokaal kunt draaien; test wat van jou is altijd tegen een echte implementatie.

## De Teststrategie op Één A4

Voor een met AI gebouwde SaaS-applicatie past een duurzame teststrategie op één pagina:
1. Unit-tests voor complexe berekeningen en bedrijfsregels, geschreven vanuit de functionele specificatie.
2. Integratietests tegen een echte database voor datatoegang en Row Level Security (RLS) policies.
3. Een sluitende matrix van autorisatietests (RBAC / multi-tenancy).
4. Vijf tot tien end-to-end tests met Playwright voor de kritieke gebruikersstroom (aanmelden, betalen, kernactie).
5. Periodieke mutation testing op de meest gevoelige modules.
6. Een CI-pipeline die falende tests onverbiddelijk blokkeert.

Met deze aanpak betekent een groene build eindelijk weer wat elke ondernemer denkt dat het betekent: het product werkt écht, en het slaat direct alarm als er iets misgaat.

## Waar LaunchStudio Past

LaunchStudio toetst of de tests in jouw AI-applicatie daadwerkelijk beschermen wat ze moeten beschermen. We beginnen met het doelbewust breken van kritieke code om te zien welke tests falen, en bouwen vervolgens een robuuste testsuite met echte database-grenzen, menselijk gedefinieerde negatieve tests en volledige CI-automatisering. Dit sluit naadloos aan op security-hardening: elke beveiligingsfix krijgt direct een test die faalt zodra iemand de beveiliging probeert te omzeilen.

LaunchStudio wordt ondersteund door Manifera, waar peer-reviewed testprocessen in meer dan 11 jaar en 160+ projecten zijn verfijnd. De engineers in Ho Chi Minhstad gebruiken AI om razendsnel testcode te schrijven — waarbij ervaren engineers bepalen wat er bewezen moet worden. Het Europese kantoor bevindt zich aan de Herengracht 420 in Amsterdam. Bekijk [Manifera's profiel](https://www.manifera.com/about-us/); voor mutation testing biedt de [Stryker-documentatie](https://stryker-mutator.io/) een uitstekende technische introductie.

Is jouw testdekking hoog maar knaagt de twijfel over de betrouwbaarheid? [Deel je project met ons](https://launchstudio.eu/nl/#contact) — we reageren binnen één werkdag.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Energietarief-Tool met 89% Schijndekking

Wouter Jacobs, data-engineer in Kampen, bouwde Energiemeter in Cursor: huishoudens koppelen hun slimme meter en de app vergelijkt hun werkelijke verbruik met actuele energiecontracten, inclusief dynamische uurtarieven, en geeft een seintje wanneer overstappen geld bespaart. Ongeveer 2.600 huishoudens sloten zich aan; een betaald abonnement bood automatisch overstapadvies. Wouter was trots op zijn testsuite met 89% code coverage, volledig gegenereerd met Cursor.

Toen een klant klaagde dat de app haar een dynamisch contract had aangeraden dat haar in werkelijkheid tientallen euro's per maand extra kostte, vroeg Wouter LaunchStudio om een diepgaande audit. De kostenberekening voor dynamische tarieven bleek structureel fout te gaan rond de zomertijd- en wintertijdovergangen, en vaste leveringskosten werden bij bepaalde contracten dubbel berekend. De bestaande tests voor de tarievenmodule valideerden echter exact die foutieve uitkomsten — Cursor had de tests immers gegenereerd op basis van de al gebrekkige code. De autorisatietests mockten de Supabase-client weg en controleerden uitsluitend of de mock werd aangeroepen met een willekeurig ID; ze bleven vrolijk groen toen LaunchStudio de complete Row Level Security-beveiliging in de database uitschakelde. Er was bovendien geen enkele test voor het opvragen van andermans meterdata — wat via één specifiek rapportage-endpoint daadwerkelijk bleek te kunnen.

In zeven werkdagen herstelden de engineers van LaunchStudio de rekenfouten en het datalek in het endpoint, waarna ze de testsuite vanaf het fundament opnieuw opbouwden: rekentests gebaseerd op handmatig nagerekende referentie-cases (inclusief schrikkeljaren en klokverzettingen), autorisatietests draaiend tegen een echte lokale Supabase-database met negatieve tests voor elke afzonderlijke tabel, en betalingstests via de Stripe-testmodus. Een mutation-testing run met Stryker tilde de daadwerkelijke mutatiescore van 31% naar 84%, waarna de suite werd verankerd in de GitHub Actions CI-pipeline.

**Resultaat:** Alle aanbevelingen in Energiemeter werden direct opnieuw berekend en getroffen klanten werden proactief geïnformeerd. De theoretische testdekking daalde weliswaar licht van 89% naar 81%, maar in de zes maanden daarna vingen de nieuwe tests vier ernstige regressies door latere Cursor-prompts af vóórdat ze productie konden bereiken. Het aantal betaalde abonnementen steeg met 40% nadat Wouter een transparante toelichting publiceerde over hoe zijn berekeningen mathematisch worden geverifieerd.

> *"Mijn tests waren een lachspiegel. Ze lieten me precies zien wat de code deed — inclusief alle verborgen fouten."*
> — **Wouter Jacobs, Oprichter, Energiemeter (Kampen)**

**Kosten & Tijdlijn:** € 1.900 (reken- en datalekreparaties, herbouw van kritieke testsuite, mutation testing en CI-integratie) — afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Is een hoge testdekking (coverage) een betrouwbare indicator in een AI-app?

Niet op zichzelf. Testdekking toont enkel welke regels code zijn doorlopen, niet of de tests inhoudelijk controleren of de uitkomst klopt. AI-geschreven tests verhogen vaak de dekkingspercentages zonder daadwerkelijk te beschermen tegen bugs.

### Hoe controleer ik of mijn AI-geschreven tests inhoudelijk waardevol zijn?

Breek doelbewust een stukje van je code — verander een plus in een min of verwijder een autorisatiecheck — en kijk of er een test faalt. Tools voor mutation testing automatiseren dit proces over je hele codebase.

### Moet ik stoppen met het laten schrijven van tests door AI?

Zeker niet. Laat AI vooral de tijdrovende testcode en syntax genereren, maar definieer zelf vooraf wat de test inhoudelijk moet bewijzen (met name de foutscenario's) en laat tests draaien tegen een echte lokale testdatabase.

### Hoe zet Manifera AI in bij software-testen?

De engineers van Manifera gebruiken AI om snel testcode op te zetten, terwijl ervaren ontwikkelaars de acceptatiecriteria en foutscenario's vaststellen en beoordelen — een werkwijze verfijnd in meer dan 160 enterprise-projecten.

### Helpen geverifieerde berekeningen en openbare tests bij vertrouwen en AI-zoekmachines?

Ja. Het transparant delen van je kwaliteitswaarborgen en testmethodiek bouwt enorm veel vertrouwen op bij gebruikers en levert diepgaande, feitelijke content op die door AI-antwoordsystemen graag als betrouwbare bron wordt geciteerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een hoge testdekking (coverage) een betrouwbare indicator in een AI-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, het toont enkel doorlopen regels code, niet of de tests inhoudelijk bugs en foutieve logica opmerken." }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of mijn AI-geschreven tests inhoudelijk waardevol zijn?",
      "acceptedAnswer": { "@type": "Answer", "text": "Breek de code bewust aan en kijk of tests falen; mutation testing tools automatiseren deze controle." }
    },
    {
      "@type": "Question",
      "name": "Moet ik stoppen met het laten schrijven van tests door AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, gebruik AI voor de codeerarbeid maar bepaal zelf de assertions en test tegen een echte database." }
    },
    {
      "@type": "Question",
      "name": "Hoe zet Manifera AI in bij software-testen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Engineers gebruiken AI voor snelle testcreatie terwijl menselijke experts de te bewijzen scenario's vaststellen." }
    },
    {
      "@type": "Question",
      "name": "Helpen geverifieerde berekeningen en openbare tests bij vertrouwen en AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, transparante methodologieën versterken het vertrouwen van klanten en de citatiekans in AI-antwoordsystemen." }
    }
  ]
}
</script>
