---
Titel: "Bolt Deployment: Van Previewlink naar een Echt Adres"
Trefwoorden: bolt deployment, een bolt-app hosten, eigen domein, omgevingen, CI, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Bolt Deployment: Van Previewlink naar een Echt Adres

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Deployment: Van Previewlink naar een Echt Adres",
  "description": "Een previewlink is prima om iemand iets te laten zien en verkeerd om een bedrijf op te draaien. De code eruit halen, kiezen waar ze draait, omgevingen, een domein, en een deploy die u kunt herhalen en terugdraaien.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-deployment-from-preview-link-to-a-real-address" }
}
</script>

De link die Bolt u geeft, werkt. U kunt hem naar iemand sturen, die kan hem openen, het product draait. Voor een demonstratie is dat precies goed, en het is de reden dat de tool nuttig is.

Het is niet de plek waar een bedrijf draait. Een preview-URL is gebonden aan de tool, zegt niets over uw bedrijf, is niet te vinden in zoekmachines, en de relatie van uw klanten met uw product loopt via een dienst waar zij nooit van hebben gehoord en die u niet beheert.

Overstappen op een echte deployment is een dag werk, en het is de stap die van een prototype iets maakt dat zelfstandig bestaat.

## Haal de Code in Uw Eigen Repository

Bezit vóór al het andere de code.

Exporteer het project en zet het in een repository onder uw eigen account. Dit is de allerbelangrijkste stap, en het is degene die oprichters uitstellen — tot de middag dat ze iemand willen inhuren, van tool willen wisselen, of gewoon willen weten wat er vorige week veranderde, en ontdekken dat de hele geschiedenis van hun product in het product van een ander zit.

Een repository geeft u een geschiedenis die u kunt lezen, een plek om vanuit elke tool te werken, een back-up die niet de verantwoordelijkheid van een platform is, en de basis voor alles hieronder. Het kost twintig minuten.

Nu u er toch bent: controleer wat er meekwam. Een repository die uit een prototype is geëxporteerd, bevat vaak omgevingsbestanden met live inloggegevens, die vóór de eerste commit moeten worden verwijderd en vervangen in plaats van erna.

## Kies Waar Het Draait

Voor een typische Bolt-applicatie — een frontend met serverless functies en een gehoste database — zijn de realistische opties de platforms die precies voor die vorm zijn gebouwd: Vercel, Netlify, Cloudflare. Alle drie deployen vanuit een repository, regelen SSL en domeinen, en kosten op kleine schaal niets.

De keuze doet er minder toe dan oprichters verwachten. Kies degene waarvan u de documentatie het duidelijkst vindt, en let op twee dingen: waar uw functies draaien, wat een regio dicht bij uw database hoort te zijn in plaats van dicht bij uw bezoekers, en wat uw rekening doet als het verkeer piekt.

De alternatieven — een container bij een cloudprovider, een virtuele server — betekenen meer controle en meer verantwoordelijkheid, en zijn in dit stadium zelden het juiste antwoord.

## Drie Omgevingen Vanaf het Begin

Productie is wat klanten gebruiken. Staging is een volledige kopie waar wordt bevestigd dat wijzigingen werken. Ontwikkeling is uw machine.

Elk heeft een eigen database nodig, eigen inloggegevens en eigen configuratie, met niets gedeeld. Een stagingomgeving die naar de database van productie wijst, is geen stagingomgeving, en een die de e-mailgegevens van productie bevat, mailt uiteindelijk uw klanten.

Richt dit in bij het deployen in plaats van later. Het is een kwartier als er één omgeving te dupliceren is, en een project zodra er geschiedenis te ontwarren is.

Staging moet ook geblokkeerd zijn voor zoekmachines en bij voorkeur achter toegangsbeveiliging staan — anders krijgt u een tweede kopie van uw site die met de eerste concurreert.

## Een Domein en Wat Erbij Hoort

Koop het domein, laat het naar uw deployment wijzen, en laat het platform het certificaat uitgeven.

Drie dingen die het waard zijn om tegelijk te doen en later vervelend zijn. Beslis of u het kale domein of de www-versie gebruikt, stuur de ene permanent door naar de andere, en neem die beslissing één keer. Richt de records voor e-mailauthenticatie in — SPF, DKIM en DMARC — voordat u uw eerste e-mail aan een klant verstuurt, want een domein dat zonder deze begint te versturen, bouwt een reputatie op die traag te herstellen is. En houd de domeinregistratie in uw eigen account, met de verlenging op een kaart die niet stilletjes verloopt.

## Maak de Deploy Herhaalbaar en Omkeerbaar

De laatste stap, en degene die een deployment onderscheidt van een lancering.

Deployen moet één handeling zijn — een push naar een branch — die bouwt en uitrolt zonder een volgorde die u moet onthouden. De meeste slechte releases op deze schaal zijn een vergeten stap in plaats van slechte code.

En u moet weten hoe u het ongedaan maakt. Zoek vandaag de rollbackknop op uw platform, terwijl er niets mis is, deploy iets triviaals, draai het terug, en meet de tijd. Een rollback die u hebt uitgevoerd, is er een die u zult gebruiken; een waarover u alleen hebt gelezen, is er een die u op het slechtste moment zult vermijden.

## Blijf de Tool Daarna Gebruiken

Goed deployen betekent niet dat u Bolt verlaat, en oprichters gaan daar soms wel van uit — alsof overstappen op een repository een diploma is dat vereist dat u vanaf dan alles met de hand schrijft.

De opzet die werkt: de repository is de bron van waarheid, en de tool is een van de manieren waarop u die verandert. Exporteer één keer, deploy vanuit de repository, en blijf Bolt of een andere assistent tegen die codebase gebruiken voor waar het goed in is.

Wat verandert, is de richting van het gezag. Eerder hield de tool uw product vast en had u een kopie; nu houdt u uw product vast en is de tool iets wat u erop richt. Dat betekent dat wijzigingen binnenkomen als commits die u kunt lezen, beoordelen en terugdraaien, in plaats van als bewerkingen in een werkruimte zonder geschiedenis.

Twee gewoontes maken dit comfortabel. Werk voor alles wat substantieel is op een branch, zodat een sessie die slecht gaat wordt weggegooid in plaats van ontrafeld. En commit vaak met berichten die zeggen wat er veranderde, want de geschiedenis is de enige registratie van waarom uw product is zoals het is — en in een codebase waarin veel van het schrijven door een tool is gedaan, is die registratie het verschil tussen een product dat u kunt uitleggen en een dat u alleen kunt observeren.

De oprichters die deze overgang goed maken, beschrijven de repository meestal als datgene waardoor ze het gevoel kregen dat het product van hen was. Dat is niet alleen gevoel; het is het praktische verschil tussen een bezit en een regeling.

## Wat U de Dag Erna Controleert

Een deployment die slaagt, is niet hetzelfde als een deployment die klopt, en de verschillen komen in de eerste vierentwintig uur naar boven als iemand kijkt.

Zes controles, elk een minuut.

Open het product zoals een klant dat zou doen, op een telefoon, van buiten uw eigen netwerk. Log in, doe het belangrijkste, en log uit. Het aantal lanceringen dat mislukt omdat iets alleen op de machine van de developer werkte, is niet klein.

Bevestig dat de site bereikbaar is op zowel de www- als de kale vorm, en dat de ene naar de andere doorverwijst. Bevestig dat het certificaat geldig is en dat er geen waarschuwing voor gemengde content is door een bestand dat nog via HTTP laadt.

Verstuur één echte e-mail vanuit het product en kijk waar die belandt — inbox of spam — bij een Gmail-adres en een Outlook-adres, die zich anders gedragen.

Controleer dat uw error tracking iets heeft ontvangen, door bewust een fout te veroorzaken. Een tracker die is ingesteld maar niets ontvangt, is de meest voorkomende stille mislukking bij een lancering.

Kijk wat de server teruggeeft voor een URL die niet bestaat. Dat hoort een 404 te zijn, niet de schil van uw applicatie met een 200, wat zoekmachines stilletjes vertelt dat elk verkeerd getypt adres een echte pagina is.

En bevestig dat uw uptimecontrole daadwerkelijk faalt wanneer dat moet, door haar een minuut op een bewust kapot pad te richten. Een monitor die nooit alarm slaat, is niet te onderscheiden van een monitor die niet draait.

Schrijf de zes op en herhaal ze na elke grote deployment. Ze kosten tien minuten en ze vangen de soort problemen die monitoring niet vangt: dingen die kapot zijn op een manier die het systeem normaal vindt.

Een nuttige regel om er tegelijk bij te nemen: deploy niet op een moment dat u die tien minuten niet kunt besteden. Het meeste van wat er bij een lancering misgaat, wordt gevonden door degene die het uitbracht, door te kijken — en kijken kan alleen als u er nog bent.

## Dit Inrichten

Voor een Bolt-project dat live gaat, kost dit doorgaans één dag: de code geëxporteerd naar uw eigen repository met inloggegevens verwijderd en vervangen, een hostingplatform gekozen met functies dicht bij de database, drie omgevingen met aparte databases en inloggegevens en niets gedeeld, staging geblokkeerd voor indexering en achter toegangsbeveiliging, een domein met een gekozen canonieke vorm en een doorverwijzing, SSL uitgegeven, records voor e-mailauthenticatie ingericht vóór de eerste verzending, deployment geautomatiseerd vanuit een push naar een branch, rollback gevonden en getimed, en eenvoudige uptimemonitoring gericht op een pagina die de applicatie aanspreekt.

LaunchStudio doet dit als onderdeel van het Launch Ready-pakket vanaf €800, en beheert het daarna binnen managed hosting voor €49 per maand. De engineers zijn van Manifera — elf jaar, 160+ projecten, vanaf de Herengracht 420 in Amsterdam.

[Stuur ons uw Bolt-project](https://launchstudio.eu/nl/#contact) en wij zetten het deze week op uw eigen adres.

## Echt voorbeeld

### Een Bedrijf Dat op een Previewlink Draaide

Renske Bouhuijs bouwde Zwemlesplanner met Bolt: lesplanning en presentie voor zwemscholen, dat drie scholen binnen een maand gingen gebruiken omdat het een probleem oploste dat ze hadden.

Het draaide vijf maanden op de preview-URL. Ouders kregen links naar dat adres. De scholen zetten het in hun bladwijzers. Renske factureerde €45 per maand per school, en het bedrijf, voor zover het er een was, bestond volledig in de preview van een prototypingtool.

In dezelfde week gebeurden twee dingen. De preview was tijdens een storing van het platform enkele uren onbereikbaar, zonder statuspagina waarnaar ze iemand kon verwijzen en zonder dat ze iets kon doen. En een school vroeg vóór de verlenging naar de website van haar bedrijf, die niet bestond, omdat het product geen eigen adres had.

Eén werkdag: het project geëxporteerd naar een repository onder haar eigen account, met een omgevingsbestand met live database-inloggegevens verwijderd en die gegevens vervangen; deployment naar een hostingplatform vanuit een push naar een branch, met functies vastgezet in dezelfde regio als haar Supabase-project, wat ook een merkbare vertraging op elke pagina wegnam; drie omgevingen aangemaakt met aparte databases en inloggegevens, ter vervanging van één gedeelde omgeving waarin ze tegen live data had getest; staging achter toegangsbeveiliging gezet en uitgesloten van indexering; een `.nl`-domein gekocht en naar de deployment laten wijzen met SSL, waarbij de www-vorm doorverwijst naar het kale domein; SPF, DKIM en DMARC ingericht voordat de eerste lesherinnering vanaf het nieuwe domein werd verstuurd; rollback getest en getimed op 35 seconden; en uptimemonitoring op een pagina die een echte databasequery uitvoert.

**Resultaat:** de drie scholen verlengden en er kwamen er binnen een kwartaal twee bij, wat Renske deels toeschrijft aan een adres dat eruitzag als een bedrijf. De scheiding van omgevingen maakte ook een einde aan een gewoonte waarvan ze niet had beseft dat die gevaarlijk was — wijzigingen testen tegen de live database, wat twee keer zichtbare vreemdheden had veroorzaakt tijdens de lesuren van een school.

> *"Ouders zetten een previewlink in hun bladwijzers. Toen die vier uur onbereikbaar was, had ik niemand iets te vertellen, omdat het product eigenlijk nergens bestond waar ik over ging."*
> — **Renske Bouhuijs, Oprichter, Zwemlesplanner (Hoorn)**

**Kosten & Doorlooptijd:** €1.900 (export naar repository met vervangen inloggegevens, hostingdeployment met regionale plaatsing van functies, scheiding in drie omgevingen, domein en SSL met canonieke doorverwijzing, e-mailauthenticatie, geautomatiseerde deploy met geteste rollback, uptimemonitoring) — afgerond in 1 werkdag.

## Veelgestelde vragen

### Kan ik een bedrijf draaien op een Bolt-previewlink?

Dat kan, kort, en het is een slecht idee. Hij is gebonden aan de tool, niet te vinden in zoekmachines, zegt niets over uw bedrijf, en geeft u geen controle tijdens een incident.

### Wat is de eerste stap?

Exporteer de code naar een repository onder uw eigen account, en verwijder en vervang alle inloggegevens die meekwamen. Al het andere hangt af van het bezitten van de code.

### Welk hostingplatform moet ik kiezen?

Elk platform dat voor dit soort applicatie is gebouwd. De keuze doet er minder toe dan uw functies dicht bij uw database laten draaien en weten wat uw rekening onder verkeer doet.

### Heb ik echt een stagingomgeving nodig?

Zodra klanten van het product afhangen, ja — met een eigen database en eigen inloggegevens, geblokkeerd voor indexering. Testen tegen live data is de gewoonte die het vervangt.

### Wat moet ik doen voordat ik mijn eerste e-mail vanaf een nieuw domein verstuur?

SPF, DKIM en DMARC inrichten. Een domein dat zonder deze begint te versturen, bouwt een afleverreputatie op die lang duurt om te herstellen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een bedrijf draaien op een Bolt-previewlink?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen kort. Hij is gebonden aan de tool, onzichtbaar voor zoekmachines, draagt geen merk, en laat u machteloos tijdens een incident."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de eerste stap bij het deployen van een Bolt-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Exporteer de code naar uw eigen repository, en verwijder en vervang alle meegekomen inloggegevens. Al het andere hangt af van het bezitten van de code."
      }
    },
    {
      "@type": "Question",
      "name": "Welk hostingplatform past bij een Bolt-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elk platform gebouwd voor frontends met serverless functies. Belangrijker is functies dicht bij uw database laten draaien en de kosten onder belasting begrijpen."
      }
    },
    {
      "@type": "Question",
      "name": "Is een stagingomgeving nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodra klanten op het product vertrouwen, ja — met een eigen database en inloggegevens, en geblokkeerd voor indexering door zoekmachines."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet zijn ingericht voordat u e-mail vanaf een nieuw domein verstuurt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SPF, DKIM en DMARC. Versturen zonder deze schaadt de aflevering op manieren die lang duren om te herstellen."
      }
    }
  ]
}
</script>
