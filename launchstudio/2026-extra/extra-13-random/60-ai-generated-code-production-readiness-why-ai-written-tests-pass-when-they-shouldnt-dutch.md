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

"We hebben 87% testdekking" is een van de geruststellendste zinnen die een technische oprichter over een AI-gebouwde app kan zeggen. Het is ook, steeds vaker, een van de minst informatieve. AI-tools schrijven snel en in grote aantallen tests, en tools voor dekking tellen de regels die die tests uitvoeren. Geen van beide vertelt je of de tests zouden falen als de code fout was. Voor de productierijpheid van AI-gegenereerde code kan een groene testsuite een vals signaal zijn — en het probleem is subtiel genoeg om vaak onopgemerkt te blijven totdat een bug die de tests "dekten" bij klanten belandt.

## De Vier Soorten Holle Tests

**1. De test die wegmockt wat hij test.** Gevraagd een functie te testen die een bestelling opslaat en een kaart belast, mockt de AI de database en de betaalclient, en controleert daarna dat de mocks zijn aangeroepen. De test slaagt of de echte query nu klopt of niet, het echte betaalverzoek geldig is of niet, of de bestelling echt wordt opgeslagen of niet. Hij test dat code functies aanroept, niet dat het systeem werkt.

**2. De test die de implementatie spiegelt.** De AI leest de functie en schrijft asserties die overeenkomen met wat die doet. Berekent de functie de btw verkeerd, dan bevestigt de test het verkeerde resultaat. De test legt de bug vast.

**3. De test met alleen het ideale pad.** Geldige invoer, ingelogde eigenaar, geslaagde betaling. Geen test voor de verkeerde gebruiker, de verlopen sessie, de mislukte betaling, het dubbele verzoek of de lege lijst. De meeste productiebugs zitten precies in die paden.

**4. De test die niet kan falen.** Asserties als `expect(result).toBeDefined()` of `expect(response.status).toBeLessThan(500)`, of tests waarin fouten binnen de test worden opgevangen en genegeerd. Ze voeren code uit en controleren bijna niets.

Alle vier verhogen de dekking. Geen enkele beschermt je.

## Waarom Holle Tests de Productierijpheid van AI-Gegenereerde Code Ondermijnen

AI-modellen optimaliseren voor tests die slagen, omdat een falende test eruitziet als een probleem dat moet worden opgelost. Is de makkelijkste manier om een test te laten slagen een afhankelijkheid te mocken of de bestaande uitvoer te spiegelen, dan doen ze dat. Ze hebben ook geen onafhankelijke kennis van wat je code hoort te doen; ze leiden de bedoeling af uit de code zelf. En ze testen meestal het scenario dat in de prompt staat — doorgaans het ideale pad.

## Holle Tests Snel Herkennen

- **Breek de code met opzet.** Verander een voorwaarde, verwijder een autorisatiecontrole, pas een berekening aan. Draai de tests. Slagen ze nog steeds, dan beschermen ze dat gedrag niet. (Tools voor mutatietesten zoals Stryker automatiseren dit idee.)
- **Tel de mocks.** Tests die tegelijk de database, de authenticatielaag en de externe dienst mocken, testen zelden iets betekenisvols.
- **Zoek naar negatieve tests.** Zoek naar tests waarbij het verwachte resultaat een weigering is: 401, 403, validatiefout, geweigerde betaling. Weinig of geen is een waarschuwingssignaal.
- **Lees de asserties.** Controleren ze specifieke, betekenisvolle uitkomsten — het juiste record, het juiste bedrag, de juiste gebruiker — of alleen dat er iets gebeurde?

## Hoe Goede Tests voor AI-Gebouwde Apps Eruitzien

**Test gedrag via echte grenzen.** Draai tests voor kritieke flows tegen een echte testdatabase (een lokale Postgres- of Supabase-instance, of de Firebase-emulator) in plaats van mocks. Mock alleen externe diensten die je niet lokaal kunt draaien, en gebruik dan hun officiële testmodi of realistische nabootsingen.

**Schrijf eerst de bedoeling.** Beschrijf in gewone taal wat er moet gebeuren — "een lid van team A kan de facturen van team B niet lezen" — en schrijf de test op basis daarvan, niet op basis van de implementatie. Je kunt de AI vragen de testcode te schrijven, maar specificeer de assertie zelf.

**Geef voorrang aan negatieve tests.** Voor elke beschermde resource: verkeerde gebruiker, geen gebruiker, verkeerde rol, verkeerde tenant. Voor elke betaling: geweigerd, afgebroken, dubbele webhook, terugbetaald. Voor elke invoer: te lang, verkeerd type, ontbrekend, kwaadaardig.

**Houd een kleine, sterke kritieke suite.** Tien tot dertig tests die aanmelden, inloggen, toegangsbeheer, betalingen en de kernactie van begin tot eind doorlopen, zijn meer waard dan honderden holle unittests. Draai ze bij elke wijziging.

**Meet wat ertoe doet.** Dekking is een zwakke graadmeter. De mutatiescore, of simpelweg de controle "breek het met opzet" op kritieke code, vertelt je veel meer.

## Mocks: Wanneer Ze Helpen en Wanneer Ze Verbergen

Mocks zijn op zichzelf niet slecht; het zijn hulpmiddelen met een specifiek doel. Voor de productierijpheid van AI-gegenereerde code is de vraag waar je ze inzet:

| Afhankelijkheid | Mocken? | Beter alternatief |
| --- | --- | --- |
| Je eigen database | Zelden | Echte testdatabase (lokale Postgres, Supabase lokaal, emulator) |
| Je eigen bedrijfslogica | Nee | Direct testen |
| Betaalaanbieder | Gedeeltelijk | Testmodus van de aanbieder voor integratietests; mocks voor randgevallen in unittests |
| E-mailaanbieder | Ja | Opvangdienst (bijv. een lokale SMTP-catcher) en controleren op inhoud |
| API van een AI-model | Ja, voor determinisme | Opgenomen fixtures plus af en toe een live evaluatierun |
| Klok / tijd | Ja | Nep-timers ingesteld op specifieke datums |

De vuistregel: mock wat je niet beheert en niet lokaal kunt draaien; test wat van jou is tegen echte implementaties.

## Tests Schrijven Vanuit de Bedoeling

Tests die gedrag beschermen, beginnen bij wat waar moet zijn, niet bij wat de code doet. Een praktische methode voor kritieke functies:

1. Schrijf de regels in gewone taal op, inclusief negatieve gevallen: "Een tariefvergelijking gebruikt uurprijzen voor dynamische contracten; op de dag dat de klok teruggaat, zijn er 25 uur; vaste kosten worden één keer per maand meegeteld."
2. Maak met de hand referentiegevallen, met invoer en verwachte uitvoer die onafhankelijk zijn berekend (een spreadsheet werkt).
3. Maak van elke regel en elk referentiegeval een test.
4. Vraag pas daarna de AI-tool de tests te laten slagen, of extra tests in dezelfde stijl te schrijven.

Deze volgorde keert de gebruikelijke AI-workflow om, en het is de meest effectieve manier om tests te krijgen die echte bugs vangen.

## Mutatietesten in het Kort

Tools voor mutatietesten zoals Stryker brengen automatisch kleine wijzigingen in je code aan — een vergelijking omdraaien, een voorwaarde verwijderen, een getal veranderen — en draaien je tests. Slagen de tests nog steeds, dan "overleefde de mutant", wat betekent dat de tests dat gedrag niet controleren. De mutatiescore (het aandeel opgevangen mutanten) is een veel betere maat voor de kracht van tests dan dekking. Draai het op je belangrijkste modules — prijzen, toegangsbeheer, facturatie — eens per maand of vóór releases, en je ziet precies waar tests hol zijn.

## Property-Based Tests voor Berekeningen

Bij berekeningen zoals tarieven, prijzen, btw of roosters genereert property-based testing veel willekeurige invoer en controleert het eigenschappen die altijd moeten gelden: totalen zijn gelijk aan de som van hun delen, resultaten worden nooit negatief, een vergelijking is symmetrisch, afronding wijkt nooit meer dan een cent af. Bibliotheken als fast-check voor TypeScript maken dit toegankelijk. Deze tests vinden randgevallen waar mensen zelden aan denken — schrikkeljaren, lege invoer, zeer grote getallen.

## Testdata die de Werkelijkheid Weerspiegelt

Holle tests gebruiken vaak onrealistische data: één gebruiker, één record, ronde getallen, geen speciale tekens, geen variatie in tijdzones. Realistische fixtures bevatten meerdere tenants, gebruikers met verschillende rollen, grote datasets voor paginering, namen met accenten, bedragen met lastige decimalen, datums aan het einde van een maand en rond overgangen van zomer- en wintertijd. Bouw een gedeelde set fixtures en hergebruik die; veel bugs komen boven simpelweg omdat de data eindelijk op productie lijkt.

## Door AI Geschreven Tests Snel Beoordelen

Schrijft een AI-tool tests, beoordeel ze dan met een korte checklist: Controleert elke test een specifieke, betekenisvolle uitkomst? Zou hij falen als de functie stuk was? Zijn er negatieve tests? Hoeveel is er gemockt, en is het gemockte deel het deel dat wordt getest? Zijn de asserties zwak (`toBeDefined`, `toBeTruthy`)? Vijf minuten review per testbestand bespaart weken vals vertrouwen.

## Tests in CI als Contract

Zodra tests betekenisvol zijn, maak er dan een contract van: verplichte controles bij elke pull request, niet mergen bij rood, en geen tests verwijderen of afzwakken zonder review. AI-tools "repareren" falende tests soms door asserties aan te passen aan kapot gedrag; branchbescherming en review voorkomen dat. Houd onbetrouwbare (flaky) tests bij en los ze snel op, want een suite die willekeurig faalt, leert iedereen hem te negeren.

## End-to-Endtests voor Kritieke Klantreizen

Unittests controleren onderdelen; end-to-endtests controleren dat de onderdelen samenwerken zoals een gebruiker ze ervaart. Voor de meeste AI-gebouwde apps dekken vijf tot tien end-to-endtests met een tool als Playwright de reizen die ertoe doen: aanmelden en e-mailbevestiging, inloggen en wachtwoordherstel, de kernactie, de checkout met een testbetaling, opzeggen of terugbetalen, en het verwijderen van een account. Draai ze bij elke merge tegen staging. Ze zijn trager en soms breekbaar, dus houd ze beperkt en gericht — maar ze vangen integratiefouten op die unittests met mocks niet kunnen zien.

## Toegangsbeheer Systematisch Testen

Toegangsbeheer verdient een eigen testsuite, omdat de fouten ervan stil en ernstig zijn. Genereer tests vanuit een matrix van rollen en resources: controleer voor elk type resource en elke rol wat moet worden toegestaan en wat moet worden geweigerd, inclusief toegang tussen tenants. Deze suite draaien tegen een echte database met echte policy's is de enige betrouwbare manier om te weten dat een opnieuw gegenereerde route of een nieuwe migratie geen gat heeft geopend. In het voorbeeld hieronder was het deze suite die uiteindelijk het rapportage-endpoint ving dat data van andere huishoudens blootstelde.

## Wanneer Dekkingscijfers Wél Ertoe Doen

Dekking is niet nutteloos; ze is op zichzelf gewoon onvoldoende. Lage dekking in een kritieke module is een duidelijke waarschuwing. Hoge dekking in combinatie met een goede mutatiescore en betekenisvolle negatieve tests is een sterk signaal. Gebruik dekking om ongeteste gebieden te vinden, niet om te bewijzen dat geteste gebieden goed zijn getest.

## Een Teststrategie op Eén Pagina

Voor een klein AI-gebouwd product past een houdbare teststrategie op één pagina: unittests voor berekeningen en bedrijfsregels, geschreven vanuit de bedoeling; integratietests tegen een echte database voor datatoegang en policy's; een matrix van tests voor toegangsbeheer; een handvol end-to-endtests voor kritieke klantreizen; periodiek mutatietesten op de belangrijkste modules; en CI die dit allemaal afdwingt. Met die strategie betekent een groene build eindelijk wat oprichters aannemen dat hij betekent: het product werkt, en het zou je vertellen als dat niet zo was.

## Waar LaunchStudio Past

Het testwerk van LaunchStudio aan AI-gebouwde apps begint met controleren of bestaande tests eigenlijk iets beschermen — kritieke code met opzet breken en kijken wat faalt — en bouwt daarna een compacte kritieke suite met echte databasegrenzen, door mensen gespecificeerde negatieve tests en integratie in CI. Het past natuurlijk bij het versterken van de beveiliging: elke oplossing in het toegangsbeheer krijgt een test die zou falen als de oplossing werd verwijderd.

LaunchStudio wordt aangedreven door Manifera, waar praktijken voor testen met peer review over 160+ projecten in 11+ jaar zijn verfijnd. Onze engineers in Ho Chi Minh-stad gebruiken ook AI om tests te schrijven — met mensen die bepalen wat de tests moeten bewijzen. Het Europese contact zit aan de Herengracht 420 in Amsterdam. Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/); voor mutatietesten is [de documentatie van Stryker](https://stryker-mutator.io/) een praktische inleiding.

Is je dekking hoog en je vertrouwen niet, [beschrijf dan je project](https://launchstudio.eu/nl/#contact) — we reageren binnen één werkdag.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Tool voor Energietarieven met 89% Dekking

Wouter Jacobs, data-engineer in Kampen, bouwde Energiemeter met Cursor: huishoudens koppelen de data van hun slimme meter, en de app vergelijkt hun werkelijke verbruik met energiecontracten op de markt, inclusief dynamische uurtarieven, en waarschuwt als overstappen geld zou besparen. Zo'n 2.600 huishoudens gebruikten het; een premiumniveau bood geautomatiseerd overstapadvies. Wouter was trots op een testdekking van 89%, allemaal geschreven met Cursor.

Nadat een klant klaagde dat de app een contract had aanbevolen dat haar meer zou hebben gekost, vroeg Wouter LaunchStudio het te onderzoeken. De kostenberekening voor dynamische tarieven was fout rond de overgangen van zomer- en wintertijd, en vaste kosten werden voor sommige contracttypen dubbel geteld. De tests voor de calculator bevestigden precies die verkeerde uitkomsten — ze waren op basis van de implementatie gegenereerd. De tests voor toegangsbeheer mockten de Supabase-client en controleerden dat die met een gebruikers-ID werd aangeroepen; ze slaagden zelfs toen LaunchStudio de row level security-policy met opzet verwijderde. Er waren geen tests voor gebruikers die meterdata van andere huishoudens lazen, wat via één rapportage-endpoint mogelijk bleek te zijn.

In zeven werkdagen herstelden de engineers van LaunchStudio de berekening en het rapportage-endpoint, en bouwden ze daarna de kritieke tests opnieuw: tests voor de calculator op basis van met de hand geverifieerde referentiegevallen (inclusief dagen met een tijdwissel en elk contracttype), toegangstests die tegen een lokale Supabase-instance draaien met negatieve gevallen voor elke tabel, en betaaltests in de testmodus van Stripe. Ze voerden een ronde mutatietesten uit op de calculator en de toegangslaag, waarmee de mutatiescore steeg van 31% naar 84%, en voegden de suite toe aan CI.

**Resultaat:** De aanbevelingen van Energiemeter werden voor alle gebruikers opnieuw berekend, en getroffen klanten werden geïnformeerd. De dekking daalde licht naar 81%, maar in de zes maanden daarna vingen de nieuwe tests vier regressies uit Cursor-bewerkingen op — twee daarvan in de tariefcalculator. Premiumabonnementen groeiden met 40% nadat Wouter een transparante uitleg publiceerde over hoe berekeningen worden geverifieerd.

> *"Mijn tests waren een spiegel. Ze lieten precies zien wat de code deed — inclusief de fouten."*
> — **Wouter Jacobs, Oprichter, Energiemeter (Kampen)**

**Kosten & Tijdlijn:** € 1.900 (oplossingen voor berekening en toegang, herbouw van de kritieke testsuite, mutatietesten en integratie in CI) — afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Is een hoge testdekking een goed teken in een AI-gebouwde app?

Op zichzelf niet. Dekking laat zien welke regels tests uitvoeren, niet of ze bugs zouden vangen. Door AI geschreven tests verhogen vaak de dekking zonder gedrag te beschermen.

### Hoe zie ik of mijn door AI geschreven tests betekenisvol zijn?

Breek de code met opzet — verwijder een controle, verander een berekening — en kijk of er een test faalt. Tools voor mutatietesten automatiseren dit.

### Moet ik AI geen tests meer laten schrijven?

Nee. Laat AI testcode schrijven, maar specificeer wat elke kritieke test moet bewijzen, vooral negatieve gevallen, en draai tests tegen echte grenzen zoals een testdatabase.

### Hoe gebruikt Manifera AI bij het testen?

De engineers van Manifera gebruiken AI om snel testcode te schrijven, terwijl mensen bepalen welk gedrag tests moeten verifiëren en beoordelen wat ze controleren — een balans die over 160+ projecten is verfijnd.

### Kunnen geverifieerde berekeningen en tests het vertrouwen in AI-antwoordmachines vergroten?

Publiceren hoe je product zijn resultaten verifieert — zoals Energiemeter deed — levert het soort transparante, specifieke content op dat gebruikers vertrouwen en dat AI-antwoordmachines eerder citeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een hoge testdekking een goed teken in een AI-gebouwde app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Op zichzelf niet; dekking toont uitgevoerde regels, niet of tests bugs vangen." }
    },
    {
      "@type": "Question",
      "name": "Hoe zie ik of mijn door AI geschreven tests betekenisvol zijn?",
      "acceptedAnswer": { "@type": "Answer", "text": "Breek de code met opzet en kijk of tests falen; mutatietesten automatiseert dit." }
    },
    {
      "@type": "Question",
      "name": "Moet ik AI geen tests meer laten schrijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee; specificeer wat kritieke tests moeten bewijzen en draai ze tegen echte grenzen." }
    },
    {
      "@type": "Question",
      "name": "Hoe gebruikt Manifera AI bij het testen?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI schrijft testcode terwijl mensen bepalen en beoordelen wat tests verifiëren." }
    },
    {
      "@type": "Question",
      "name": "Kunnen geverifieerde berekeningen en tests het vertrouwen in AI-antwoordmachines vergroten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Transparante content over verificatie bouwt vertrouwen op en wordt eerder geciteerd." }
    }
  ]
}
</script>
