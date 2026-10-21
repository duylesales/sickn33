---
Titel: "Replit en CI: Testen Vóór een Deployment"
Trefwoorden: replit CI, continuous integration, geautomatiseerde controles, deploymentpoort, GitHub Actions, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Replit en CI: Testen Vóór een Deployment

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit en CI: Testen Vóór een Deployment",
  "description": "Een deploy met één klik is snel en heeft geen poort. Wat u automatisch controleert voordat code klanten bereikt, hoe u dat draait wanneer het product op een prototypingplatform leeft, en de vier controles die u als eerste wilt hebben.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/replit-and-ci-testing-before-a-deployment" }
}
</script>

Deployen vanuit Replit is een knop. Dat is de aantrekkingskracht, en voor een prototype is het precies goed — de kortst mogelijke weg van een wijziging naar zien dat ze werkt.

Voor een product met klanten is het ook een weg waarop niets staat. Wat er in het project zit, gaat live, inclusief de wijziging van drie minuten geleden die niet is gedraaid, de syntaxfout in een bestand dat niemand opende, en het geheim dat iemand tijdens het debuggen in een configuratie plakte.

Continuous integration is de poort: een set automatische controles die draaien voordat iets klanten bereikt en die de deployment weigeren als ze falen. Voor een klein product is dit een dag inrichten, en het is wat ervoor zorgt dat deployen geen beslissing meer is.

## De Vier Controles Die U Als Eerste Wilt

De volgorde doet ertoe, omdat elke controle goedkoper is dan de volgende en andere dingen opvangt.

**Bouwt het?** De waardevolste controle en de eenvoudigste. Een build die in CI faalt, is een deployment die een kapot product zou hebben opgeleverd, opgevangen in negentig seconden. Dit alleen voorkomt de gênantste categorie incidenten.

**Slagen de linter en de typecontrole?** Ongedefinieerde variabelen, ongebruikte imports, verkeerde types, kolommen die niet bestaan. Gratis, snel, en ze vangen de verzonnen interfaces op die gegenereerde code oplevert.

**Slagen de tests?** De proportionele suite die elders in deze reeks wordt beschreven — autorisatie, geld, de hoofdflow. Dit is de controle die een gedragswijziging opvangt die niemand bedoelde.

**Zit er een geheim in de code?** Een scan op patronen van inloggegevens in de gebouwde uitvoer, die de build laat falen wanneer er een verschijnt. Gezien hoe vaak deze reeks is teruggekomen op sleutels in frontendbundels, verdient deze haar plek.

Vier controles, onder drie minuten, en ze vangen het overgrote deel op van wat anders klanten zou bereiken.

## Waar de Controles Draaien

De praktische vraag voor een product dat op een prototypingplatform leeft: waar gebeurt CI eigenlijk?

Het realistische antwoord voor de meesten is de eigen automatisering van een gehoste repository — een workflowbestand in de repository dat bij elke push draait. Het is op deze schaal gratis, vraagt geen infrastructuur, en werkt ongeacht waar het product wordt gedeployd.

Dat impliceert de opzet die deze reeks steeds aanbeveelt: de code leeft in een repository, en het platform deployt daarvandaan in plaats van de plek te zijn waar de code leeft. Direct deployen vanuit een bewerksessie betekent dat er niets te controleren is voordat het gebeurt.

De workflow is eenvoudig: bij elke push installeren, bouwen, linten, types controleren, testen, scannen. Op de hoofdbranch, als dat allemaal slaagt, deployen.

## Laat Falen Iets Betekenen

Een controle die kan worden genegeerd, is geen poort.

Twee beslissingen maken haar echt. Een falende controle blokkeert de deployment — geen waarschuwing, geen melding, een weigering. En de controles zijn snel genoeg dat erop wachten geen reden is om ze te omzeilen; duurt de suite vijftien minuten, dan wordt ze omzeild op de middag dat het ertoe doet.

Het gevolg is dat een controle die af en toe faalt, moet worden opgelost of verwijderd. Een onbetrouwbare test leert u opnieuw te draaien en door te gaan, wat u traint de poort volledig te negeren — en op dat punt hebt u de kosten van CI zonder enig voordeel.

## Voeg Controles Toe op Basis van Incidenten

De vier hierboven zijn het begin. De suite die een product echt beschermt, groeit uit wat er is misgegaan.

Een deployment brak omdat een migratie ontbrak: voeg een controle toe dat het schema overeenkomt met de migraties. Een endpoint ging live zonder autorisatie: voeg de test tussen accounts toe die elk endpoint afloopt. Een dependency met een bekende kwetsbaarheid bereikte productie: voeg de audit toe aan de pipeline. Een afbeelding werd gebundeld op vier megabyte: voeg een limiet op de bundelgrootte toe.

Zo blijft een pipeline proportioneel. Elke controle bestaat omdat er iets gebeurde, niet omdat een lijst ergens haar aanbeval, en het resultaat is een poort die de werkelijke faalwijzen van uw product weerspiegelt.

## Previewdeployments Zijn Meer Waard dan Ze Kosten

Eén toevoeging naast controleren: een draaiende kopie van elke branch, automatisch gedeployd, op een eigen URL.

Voor een solo-oprichter is dit de mogelijkheid om een wijziging in een echte omgeving te bekijken voordat u haar samenvoegt, wat de dingen opvangt die geen geautomatiseerde controle kan opvangen — een layout die op een telefoon breekt, een flow die verwarrend is, een bericht in de verkeerde toon.

Voor een team van twee is het hoe de ander reviewt zonder iets lokaal te draaien.

En voor een product met klanten is het hoe u iemand een voorgestelde wijziging laat zien en vraagt of die klopt, voordat ze voor iedereen bestaat.

Bescherm ze tegen indexering en openbare toegang, zoals het omgevingsartikel in deze reeks beschrijft, en geef ze eigen inloggegevens die niet van productie zijn.

## Wat U Nog Niet Moet Automatiseren

Een pipeline kan uitgroeien tot een eigen project, en voor een product met een handvol klanten is het meeste wat over CI wordt geschreven gericht op organisaties met een ander soort probleem.

Vier dingen om voor later te bewaren.

**Browsergebaseerde end-to-end-suites voorbij één flow.** Ze zijn traag, ze breken om redenen die niets met uw code te maken hebben, en het onderhoud kost meer dan ze op deze schaal opleveren. Eén test voor de hoofdroute is het hebben waard; twintig zijn een parttimebaan.

**Deployment naar meerdere omgevingen met goedkeuringen.** Een stagingomgeving is het hebben waard; een promotieworkflow met goedkeuringspoorten is ceremonie voor een team van één.

**Prestatiebudgetten en visuele regressie.** Uiteindelijk nuttig, in het begin luidruchtig, en beide leveren fouten op die oordeel vragen in plaats van een fix — en dat is precies de eigenschap waardoor een poort wordt genegeerd.

**Alles wat onderhoud vraagt dat u niet gaat doen.** Een controle die om de paar weken breekt en aandacht nodig heeft, is een controle die wordt uitgeschakeld.

De proportionele pipeline voor een klein product bestaat uit de vier hierboven genoemde controles plus wat incidenten hebben toegevoegd, draaiend in drie minuten, zonder aandacht nodig tussen fouten in. Dat is genoeg om de spanning uit deployen te halen, en dat is het hele punt — en elke toevoeging daarna moet haar plek verdienen door iets te voorkomen wat echt is gebeurd.

## Migraties Hebben een Eigen Poort Nodig

Eén categorie verdient een aparte behandeling, omdat daar een verder goede pipeline toch iets doorlaat: wijzigingen aan de database.

Code kan worden teruggedraaid. Een migratie vaak niet, zoals het releaseartikel in deze reeks beschrijft, en dat maakt haar de ene wijziging waarbij een mislukte deployment niet de slechtste uitkomst is.

Drie controles zijn het toevoegen waard zodra uw product een schema heeft dat het beschermen waard is.

**De migratie draait schoon tegen een kopie van het productieschema**, in CI, voordat er iets wordt gedeployd. Dit vangt de migratie op die werkt tegen een ontwikkeldatabase met 40 rijen en faalt tegen een database met constraints en echte data.

**De migratie is omkeerbaar, of expliciet gemarkeerd als niet omkeerbaar.** Een migratie die een kolom verwijdert, is niet omkeerbaar, en dat weten vóór het deployen in plaats van tijdens is het verschil tussen een beslissing en een ontdekking.

**De applicatie werkt nog tegen het vorige schema.** De expand-and-contract-discipline in de praktijk: deploy de schemawijziging, bevestig dat de draaiende versie nog functioneert, en deploy dan de code. Een controle dat de oude code haar tests haalt tegen het nieuwe schema, maakt dit controleerbaar in plaats van aangenomen.

Voeg een vierde toe als uw data groot is: dat de migratie binnen een redelijke tijd klaar is bij een realistisch volume, omdat een statement dat een tabel elf minuten vergrendelt een storing is, ongeacht of het slaagt.

Niets hiervan is uitgebreid, en samen dichten ze het gat dat overblijft na de gewone controles — namelijk dat de gevaarlijkste wijziging die uw product maakt, de wijziging is die uw testsuite niet ongedaan kan maken.

Hetzelfde principe geldt voor elke onomkeerbare actie die een deployment kan veroorzaken — een bulkmail, een afschrijving, het verwijderen van bestanden. Als een release het kan doen, moet de pipeline het weten, en moet een mens er bewust mee hebben ingestemd.

## Dit Inrichten

Voor een Replit-product is dit doorgaans één dag: de code in een repository met het platform dat daarvandaan deployt in plaats van vanuit een bewerksessie, een workflow die bij elke push installeert, bouwt, lint, types controleert, test en op geheimen scant, deployment afhankelijk van het slagen van alles, controles onder ongeveer drie minuten gehouden zodat ze nooit worden omzeild, onbetrouwbare tests opgelost of verwijderd, previewdeployments per branch met eigen inloggegevens en beschermd tegen openbare toegang, en een gewoonte om een controle toe te voegen wanneer een incident een gat blootlegt.

LaunchStudio richt dit in als onderdeel van productiegereedheid, en het is meestal de verandering waardoor oprichters op vrijdag durven te deployen. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons wat er nu tussen uw code en uw klanten staat](https://launchstudio.eu/nl/#contact). Voor veel producten is het eerlijke antwoord: niets.

## Echt voorbeeld

### Een Syntaxfout om Half Vijf

Maud Terlouw bouwde Rittenregistratie op Replit: registratie van ritten en onkosten voor thuiszorgorganisaties waarvan medewerkers tussen cliënten reizen, gebruikt door 11 organisaties met samen zo'n 700 zorgverleners.

Ze deployde meerdere keren per dag met de knop van het platform, vanuit de bewerksessie. Er waren geen tests en geen controles.

Op een donderdagmiddag maakte ze een kleine wijziging aan de onkostenberekening en deployde om 16:25, en vertrok daarna om haar kinderen op te halen. De wijziging bevatte een verwijzing naar een variabele die in die scope niet bestond — het soort fout dat een typecontrole direct meldt en een mens die snel leest niet ziet.

De applicatie startte niet op. Tussen 16:25 en 19:40, toen het bericht van een zorgverlener haar eindelijk bereikte, konden zo'n 400 zorgverleners die hun dienst afsloten de ritten van die dag niet registreren. De meesten gaven het op; twee organisaties lieten medewerkers ze op papier noteren en de week erna opnieuw invoeren.

Twee werkdagen: de code naar een repository verplaatst, met het platform dat deployt vanaf de hoofdbranch in plaats van vanuit een bewerksessie; een workflow die bij elke push installeert, bouwt, lint, types controleert, tests draait en de gebouwde uitvoer scant op patronen van inloggegevens; deployment afhankelijk gemaakt van al het voorgaande; een testsuite van 31 tests voor autorisatie over 14 endpoints, de onkosten- en afstandsberekeningen, en één end-to-end-ritregistratie; de hele pipeline draaiend in 95 seconden; previewdeployments per branch met een eigen database en inloggegevens, beschermd tegen openbare toegang; en een externe uptimecontrole die de storing binnen twee minuten zou hebben gemeld.

**Resultaat:** de pipeline heeft in het jaar daarna 14 deployments tegengehouden, waarvan 9 build- of typefouten die het product precies zoals bij het oorspronkelijke incident zouden hebben gebroken. Maud merkt op dat ze nu vaker deployt in plaats van minder, omdat de beslissing eruit is gehaald.

> *"Ik deployde om vijf voor half vijf en ging mijn kinderen ophalen. Vierhonderd zorgverleners konden drie uur lang hun ritten niet registreren, en de fout was een variabelenaam die een typecontrole had opgevangen voordat ik de kamer uit was."*
> — **Maud Terlouw, Oprichter, Rittenregistratie (Gouda)**

**Kosten & Doorlooptijd:** €2.600 (deployment vanuit de repository, CI-workflow met build, lint, typecontrole, tests en scannen op geheimen, deployment afhankelijk van de controles, suite van 31 tests, previewdeployments met geïsoleerde inloggegevens, uptimemonitoring) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Wat is de eerste controle die het toevoegen waard is?

Dat het bouwt. Een buildfout die in CI wordt opgevangen, is een voorkomen kapotte deployment, het kost negentig seconden, en er hoeven geen tests voor te bestaan.

### Waar draaien de controles als mijn product op Replit staat?

In de eigen automatisering van uw gehoste repository, bij elke push. Daarvoor moet de code in een repository leven, met het platform dat daarvandaan deployt in plaats van vanuit een bewerksessie.

### Hoe lang mag de pipeline duren?

Onder ongeveer drie minuten. Een trage pipeline wordt omzeild op de middag dat ze het meest had uitgemaakt.

### Wat doe ik met een test die af en toe faalt?

Los haar op of verwijder haar. Een onbetrouwbare controle leert u opnieuw te draaien en door te gaan, en die gewoonte maakt de hele poort waardeloos.

### Welke controles voeg ik toe na de basis?

Die waartoe een incident u aanzet. Een ontbrekende migratie, een endpoint zonder autorisatie, een kwetsbare dependency, een te grote bundel — elk wordt een controle nadat het één keer is gebeurd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de eerste CI-controle die het toevoegen waard is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat het project bouwt — negentig seconden, geen tests nodig, en het voorkomt de meest voorkomende kapotte deployment."
      }
    },
    {
      "@type": "Question",
      "name": "Waar draait CI voor een Replit-product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In de automatisering van uw gehoste repository bij elke push, met het platform dat vanuit de repository deployt in plaats van vanuit een bewerksessie."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe snel moet een CI-pipeline zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Onder ongeveer drie minuten, anders wordt ze omzeild precies wanneer het ertoe deed."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen met een onbetrouwbare test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oplossen of verwijderen. Af en toe falende tests leren u de poort volledig te negeren."
      }
    },
    {
      "@type": "Question",
      "name": "Welke controles komen na build, lint en tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Die waar een incident om vraagt — consistentie van migraties, autorisatie tussen accounts, dependency-audits, limieten op bundelgrootte."
      }
    }
  ]
}
</script>
