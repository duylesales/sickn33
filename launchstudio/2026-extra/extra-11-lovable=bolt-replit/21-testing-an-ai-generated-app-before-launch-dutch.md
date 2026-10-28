---
Titel: "Een met AI gebouwde app testen als er nog geen tests zijn"
Trefwoorden: Lovable, ai gegenereerde app testen, kritieke pad tests, realistische testdata, pre-launch QA oprichter, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Een met AI gebouwde app testen als er nog geen tests zijn

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een met AI gebouwde app testen als er nog geen tests zijn",
  "description": "Een pragmatisch testplan voor een product gebouwd met AI-tools en zonder testsuite: de vijf paden die nooit mogen breken, realistische testdata inrichten, wat je eerst automatiseert en wat je handmatig laat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/testing-an-ai-generated-app-before-launch" }
}
</script>

Vraag een willekeurige AI-programmeertool om geautomatiseerde tests aan je project toe te voegen, en hij genereert zonder blikken of blozen veertig unittests voor je. Ze slagen allemaal direct. In vrijwel alle gevallen testen ze echter puur of een functie precies retourneert waarvoor hij geschreven is - een tautologie vermomd als kwaliteitsborging. En dat is exact de reden waarom oprichters die op deze manier tests toevoegen zich na afloop geen spat veiliger voelen.

Waardevol testen voor een klein softwareproduct draait niet om een theoretisch dekkingspercentage (code coverage). Het draait om een korte, messcherpe lijst van bedrijfskritieke stromen die onder geen beding mogen falen, getest op een manier die weerspiegelt hoe ze in werkelijkheid stukgaan. Voor een met AI gebouwde applicatie zonder enige bestaande testsuite telt die lijst exact vijf punten en kost de implementatie slechts één werkdag.

## Waarom gegenereerde tests leeg en nietszeggend aanvoelen

Een geautomatiseerde test heeft alleen betekenis als hij kan falen om een reden die er commercieel écht toe doet. Door AI gegenereerde tests worden bijna altijd geschreven vanuit de bestaande code-implementatie in plaats van vanuit de zakelijke requirements. Daardoor bevestigen ze simpelweg dat de code doet wat de code toevallig doet. Verander je het gedrag per ongeluk verkeerd, dan past het model de test vrolijk aan zodat hij weer slaagt.

Bovendien concentreren dit soort tests zich hoofdzakelijk op 'pure functies' - het formatteren van een datumstring of het optellen van een winkelmandje - omdat die gemakkelijk in isolatie te testen zijn. Maar dat is vrijwel nooit waar een applicatie in productie omvalt. Een product breekt op de naden: bij de databaseverbinding, bij de betaalprovider, bij de gebruikerssessie en bij gelijktijdige verzoeken (concurrency).

De allereerste stap is daarom om code coverage volledig te negeren en te starten met een heel andere vraag: welke fout zou dit bedrijf direct de das omdoen als het geruisloos stopt met werken?

## De vijf kritieke paden die je moet beschermen

Voor nagenoeg elk klein SaaS-product zijn dat de volgende vijf:

**Registratie en inloggen.** Als nieuwe gebruikers geen account kunnen aanmaken of bestaande klanten niet kunnen inloggen, doet de rest van de app er niet meer toe. Dit omvat uitdrukkelijk ook de wachtwoordherstel-stroom - het onderdeel dat het vaakst breekt en het langst onopgemerkt blijft.

**De kernactie van het product.** De ene handeling waarvoor jouw software op aarde is: een reservering plaatsen, een vacature publiceren, een maandrapport genereren of een factuur versturen. Eén test die deze hele stroom van A tot Z doorloopt.

**Betalingen en autorisatie.** Vanaf het klikken op de afrekenknop tot het daadwerkelijk toekennen van de gekochte rechten in de database - wat, zoals iedereen weet die met webhooks heeft gewerkt, heel iets anders is dan een succesvol getoond bedankscherm.

**Data-isolatie (multi-tenancy).** Een test die inlogt als Gebruiker A en verifieert dat de records van Gebruiker B categorisch onbereikbaar zijn. Dit is de test met de allerhoogste bedrijfswaarde in een B2B-product, en vrijwel niemand schrijft hem.

**Permissies en rollen.** Een normale medewerker die via een directe API-aanroep een beheerdersactie probeert uit te voeren en keurig wordt geweigerd - op databaseniveau, niet slechts doordat de knop in de interface is verborgen.

Vijf tests. Ze vangen niet elk minuscuul schoonheidsfoutje op. Maar ze vangen wél elke bug op waardoor je klanten en omzet verliest - en dat is waar het om gaat.

## Test op het juiste abstractieniveau

Softwaretests kennen een hiërarchie, en voor een klein product zit het overgrote deel van het rendement in de middelste laag:

**Unittests** testen één geïsoleerde functie. Ze zijn goedkoop en snel, maar grotendeels irrelevant voor de vijf bovenstaande paden omdat die zich over meerdere gekoppelde deelsystemen uitstrekken.

**Integratietests** controleren of jouw programmacode correct samenwerkt met een echte database en echte dependencies. Dít is waar de vijf kritieke paden thuishoren, en precies waar met AI gegenereerde apps het zwakst zijn, omdat het op de interfaces tussen systemen misgaat.

**End-to-end tests (E2E)** besturen een echte browser die door de daadwerkelijke gebruikersinterface klikt. Zeer waardevol voor registratie en checkout, maar tijdrovender om te bouwen en gevoeliger voor valse alarmen. Twee of drie browser-tests is ruim voldoende; twintig stuks ontaardt in een onderhoudsvalkuil die een solo-oprichter binnen een maand frustreert en laat varen.

Het ideale startpunt voor een klein product: vijf robuuste integratietests voor de kritieke paden, twee browser-tests voor registratie en betalen, en voorlopig helemaal geen losse unittests tenzij je te maken hebt met een wiskundig uiterst complexe berekening.

## Testdata die lijkt op de echte wereld

De meeste testfouten in met AI gebouwde applicaties ontstaan doordat er wordt getest met data die simpelweg veel te 'braaf' is.

Je testdatabase moet minimaal twee verschillende organisaties bevatten, meerdere gebruikers met verschillende rollen, data die aan elk van hen toebehoort, een gebruiker zonder enige data, en minimaal één voorbeeld van elk lastig randgeval dat je in productie gegarandeerd tegenkomt: een extreem lange achternaam, een apostrof in een e-mailadres, emoji's, nulwaarden, negatieve bedragen, een datum uit 1970 en een gearchiveerd record dat nog ergens aan gekoppeld is.

Schrijf een zogeheten *seed-script* dat deze testtoestand met één commando vanaf nul opbouwt. Dat kost een uur werk en transformeert testen van een tijdrovende klus in een geautomatiseerde handeling. Zonder zo'n script begint elke testronde met een kwartier handmatig klikken om testaccounts aan te maken - en dat is de reden waarom oprichters er na verloop van tijd mee stoppen.

## Wat je automatiseert en wat je handmatig houdt

**Automatiseer** de vijf kritieke paden. Die moeten namelijk bij elke codewijziging opnieuw worden gecontroleerd, en mensen zijn vergeetachtig wanneer ze haast hebben.

**Houd handmatig** alles wat visueel is, alles wat een echte betaalprovider in live-modus raakt, en zaken die je slechts eenmalig vóór lancering doet. Een beknopte checklist op papier die je daadwerkelijk afvinkt, werkt oneindig veel beter dan een verwaarloosde testsuite die niemand meer draait.

Die checklist verdient een vaste plek in je routine. Tien punten die je vóór elke grote release handmatig doorloopt: de vijf kernpaden doorlopen op een echte smartphone, één echte kleine iDEAL-transactie die je direct terugstort, een wachtwoordreset aanvragen via een echte mailbox, een groot bestand uploaden, een pagina openen als uitgelogde bezoeker, en na afloop de error tracker inspecteren op nieuwe meldingen.

## Tests draaien waar het er echt toe doet

Tests die alleen lokaal op je eigen laptop draaien, worden precies overgeslagen op het moment dat je haast hebt - en dat is exact het moment dat je dingen kapotmaakt. Twee maatregelen lossen dit moeiteloos op:

**Draai tests automatisch bij elke git push** via een CI/CD-pipeline (zoals GitHub Actions). Het resultaat is een rood kruisje bij elke wijziging die een kritiek pad breekt, nog vóórdat de code klanten bereikt.

**Draai ze tegen een staging-omgeving** die de productieconfiguratie nauwkeurig spiegelt, inclusief een database met hetzelfde schema en API-koppelingen in testmodus. Een app die alleen lokaal wordt getest met afwijkende omgevingsvariabelen, is getest als een fundamenteel andere app.

## De test die zichzelf direct terugverdient

Als je vandaag slechts één geautomatiseerde test schrijft, kies dan de data-isolatietest: authenticeer als Gebruiker A, probeer via de API een record van Gebruiker B op te vragen, en valideer dat het verzoek met een foutmelding wordt geweigerd.

Het kost misschien vijftien regels code. Het beschermt je tegen de meest voorkomende ernstige ontwerpfout in met AI gegenereerde software. En omdat de test bij elke commit automatisch meedraait, voorkomt hij de klassieke regressie waarbij een ontwikkelaar of AI-tool later een database-policy iets losser zet om een andere bug op te lossen, en daarmee geruisloos de achterdeur weer wijd openzet.

## Wanneer je dit beter kunt uitbesteden

Een complete testinfrastructuur opzetten tegen een echte database, met automatische seeding en een geautomatiseerde pipeline, is een paar dagen werk voor een senior engineer die dit vaker heeft gedaan - en twee frustrerende weken voor iemand die het wiel zelf moet uitvinden. Het is bovendien een fundament dat zichzelf continu blijft terugbetalen.

LaunchStudio richt dit complete fundament in als onderdeel van het productierijp maken van met AI gebouwde software: realistische testdata, integratietests over de vijf kritieke paden, browser-tests voor registratie en betalen, een staging-omgeving die productie spiegelt en een CI/CD-pipeline die bij elke push automatisch draait - hand in hand met de databasepolicies en monitoring die door deze tests worden beschermd.

De frontend die je in Lovable, Bolt of Cursor hebt gebouwd blijft onaangetast, en de tests worden schoon gedocumenteerd opgeleverd zodat jij of je AI-tool ze eenvoudig kunnen uitbreiden. Dit is een vast onderdeel van het [Launch Ready pakket](https://launchstudio.eu/nl/#packages), uitgevoerd door de engineers van Manifera met elf jaar ervaring in bedrijfskritische softwaresystemen voor partijen zoals Vodafone, TNO en CFLW.

Sta je op het punt live te gaan zonder enige test? [Omschrijf je project](https://launchstudio.eu/nl/#contact) en we vertellen je binnen één werkdag welke vijf tests voor jouw applicatie het belangrijkst zijn.

## Testen als je een solo-oprichter bent

Solo-oprichters testen hun eigen product meestal zelf, en dat is de minst betrouwbare testopstelling die er bestaat. Je gebruikt de app immers precies op de manier waarop je hem zelf hebt bedacht. Drie praktische alternatieven voor een tweede paar ogen:

**Vraag twee echte testers als testgroep vóór lancering.** Niet om feedback te geven op je idee, maar puur om de app daadwerkelijk te gebruiken. Mensen die het product niet zelf hebben gebouwd, vinden een gebroken flow binnen twintig minuten, simpelweg omdat ze stappen zetten in de volgorde die voor hén logisch is.

**Kijk mee over iemands schouder zonder iets te zeggen.** Ga achter een vriend of collega zitten, geef diegene één duidelijke taak ("maak een account aan en plan een afspraak"), en houd je tien minuten lang muisstil. Dit voelt ongemakkelijk, maar levert de meest waardevolle tien minuten aan productinzicht op die je kunt krijgen.

**Test op een apparaat dat niet van jou is.** Leen een telefoon. Jouw eigen smartphone heeft immers al actieve sessies, gecachte bestanden en automatisch ingevulde wachtwoorden - factoren die bugs verbergen die een nieuwe bezoeker direct ervaart.

Schrijf je bevindingen eerst allemaal op in plaats van direct tussendoor te gaan fixen. Een complete lijst toont patronen - drie problemen in de registratiestroom, twee bij betalingen - en patronen wijzen op structurele oorzaken, terwijl ad-hoc reparaties slechts symptomen bestrijden.

## Wat je uitdrukkelijk níét moet testen

Terughoudendheid is minstens zo belangrijk als dekking. Een testsuite die je na een maand gefrustreerd uitschakelt, is immers minder waard dan drie tests die structureel blijven draaien:

**Test het framework niet.** Dat een formulier verzendt of een URL-routeert, is de verantwoordelijkheid van React of je routerlibrary, niet van jou.

**Test eenvoudige opmaakhelpers niet.** Een functie die een datum omzet in een leesbare tekst breekt zelden, en een test die verifieert dat hij doet wat hij doet vangt niets nuttigs.

**Schrijf geen tests die de code letterlijk spiegelen.** Als elke codewijziging vereist dat je de bijbehorende test in exact dezelfde vorm moet herschrijven, is de test een kopie in plaats van een controle.

**Staar je niet blind op een coverage-percentage.** Het beloont het testen van de makkelijke helft van je codebase en zegt niets over de vraag of de risicovolle helft werkt.

**Automatiseer geen visuele opmaak.** Visuele regressietests zijn fragiel. Een menselijke blik op twee verschillende schermformaten vóór een release is voor een klein product oneindig veel sneller en betrouwbaarder.

De stelregel: behoud alleen tests waarvan je zou schrikken als ze rood uitslaan. Als een falende test je slechts de schouders doet ophalen, verwijder hem dan direct - hij kost onderhoudstijd en levert geen enkele zekerheid op.

## Echt voorbeeld

### Een boekingsplatform dat zijn eigen betaalstroom twee keer liet crashen

Jelle Vroomen bouwde Sportlokaal in Lovable: een softwareplatform waarmee gemeentelijke sporthallen en gymzalen in Zaanstad en Purmerend online worden gereserveerd. Het platform had 48 aangesloten sportaccommodaties en had al twee keer een release gedeployed die de betaalstroom geruisloos platlegde - één keer zes uur lang, en één keer een heel weekend, beide keren ontdekt door zaalbeheerders in plaats van door Jelle zelf.

Er waren nul geautomatiseerde tests. Elke nieuwe release werd gecontroleerd door even handmatig door de interface te klikken, en beide incidenten deden zich voor op avonden dat die handmatige check wegens tijdgebrek was afgeraffeld.

Vier werkdagen waren nodig om een compacte, effectieve testsuite in te richten: een seed-script dat twee accommodaties, vier gebruikers over drie rollen en realistische testrecords aanmaakt; vijf integratietests voor registratie, zaalboeking, betaalverwerking en rechten, zaal-isolatie en autorisatieweigeringsregels; twee geautomatiseerde browser-tests voor registratie en checkout; een staging-omgeving met gesimuleerde testbetalingen; en de complete suite draaiend in een GitHub Actions-pipeline met notificaties bij fouten.

De data-isolatietest faalde direct bij de allereerste run: het bleek dat een zaalbeheerder de boekingen en omzetcijfers van een andere sporthal kon inzien - een kritiek datalek dat al sinds de allereerste lancering openstond en dat niemand ooit met handmatig doorklikken had ontdekt.

**Resultaat:** elf maanden en circa negentig releases later heeft zich geen enkele betalingsstoring meer voorgedaan. De testsuite heeft sindsdien vier keer een ernstige regressie in staging tegengehouden vóórdat een zaalbeheerder of sporter er last van had.

> *"Twee storingen kostten me meer vertrouwen dan de tests me geld hebben gekost. Maar waar ik pas écht van schrok, was het beveiligingslek dat de tests op dag één vonden - een bug die al acht maanden live stond."*
> - **Jelle Vroomen, Oprichter, Sportlokaal (Zaanstad)**

**Kosten & Doorlooptijd:** € 2.450 (seed data, integratie- en browsertests, staging-omgeving, deployment-pipeline) - afgerond binnen 4 werkdagen.

## Veelgestelde vragen

### Kan ik mijn AI-tool niet gewoon vragen om tests voor me te schrijven?

Dat kan, maar dan krijg je meestal tests die geschreven zijn vanuit de bestaande code en zich concentreren op eenvoudige, pure hulpfuncties. Vraag in plaats daarvan expliciet naar specifieke risicoscenario's - zoals: *"authenticeer als Gebruiker A en verifieer dat het record van Gebruiker B onbereikbaar is"*. Dat levert tests op die daadwerkelijk kunnen falen om een reden die ertoe doet.

### Hoeveel geautomatiseerde tests heeft een klein softwareproduct écht nodig?

Tussen de vijf en acht inhoudelijke tests die de kritieke stromen dekken: registratie, de kernactie, betalingen, data-isolatie en rolbeveiliging. Code coverage percentages zijn in deze fase een verkeerd doel; het beschermen van de paden waardoor je klanten verliest is het juiste doel.

### Wat is het verschil tussen integratietests en end-to-end tests?

Integratietests controleren jouw code tegen een echte database en backend-diensten zonder een grafische browser. End-to-end (E2E) tests besturen een echte browser die door de gebruikersinterface klikt. Integratietests leveren de meeste waarde voor de minste onderhoudskosten; beperk browser-tests daarom tot registratie en afrekenen.

### Heb ik een aparte staging-omgeving nodig om goed te kunnen testen?

Voor alles wat betalingen, externe authenticatieproviders of webhooks raakt: absoluut ja. Die externe koppelingen gedragen zich fundamenteel anders tegen echte diensten dan in een lokale ontwikkelomgeving. Een app die alleen lokaal is getest, is feitelijk getest als een heel andere app.

### Welke test moet ik als allereerste schrijven?

De data-isolatietest: inloggen als één gebruiker en verifiëren dat records van een andere gebruiker technisch niet kunnen worden uitgelezen. Deze test kost slechts vijftien regels code, beschermt tegen de meest voorkomende ernstige ontwerpfout in AI-software, en voorkomt dat een versoepelde databasepolicy de achterdeur later geruisloos weer openzet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik mijn AI-tool niet gewoon vragen om tests voor me te schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat kan, maar levert vaak tests op die de code spiegelen op eenvoudige functies. Vraag om specifieke scenario's, zoals verifiëren dat één gebruiker data van een ander niet kan inzien."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel geautomatiseerde tests heeft een klein softwareproduct écht nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vijf tot acht gerichte tests die registratie, de kernactie, betalingen, data-isolatie en permissies bewaken. Dekkingspercentages zijn nu het verkeerde streefdoel."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen integratietests en end-to-end tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Integratietests testen code tegen een echte database zonder browser; end-to-end bestuurt de browser. Integratie levert de meeste waarde; beperk browser-tests tot registratie en checkout."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik een aparte staging-omgeving nodig om goed te kunnen testen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor betalingen, auth en webhooks wel, omdat die tegen echte cloudservices anders reageren dan in een lokale omgeving met afwijkende instellingen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke test moet ik als allereerste schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De data-isolatietest: inloggen als één gebruiker en controleren dat records van een ander onbereikbaar zijn. Dit bewaakt het meest voorkomende lek in AI-apps."
      }
    }
  ]
}
</script>
