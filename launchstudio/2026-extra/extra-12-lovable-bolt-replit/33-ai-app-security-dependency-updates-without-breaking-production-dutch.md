---
Titel: "AI-Appbeveiliging: Afhankelijkheden Bijwerken Zonder Productie te Breken"
Trefwoorden: ai-appbeveiliging, afhankelijkheden bijwerken, supply chain, lockfiles, kwetsbaarheidsscans, npm audit, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Afhankelijkheden Bijwerken Zonder Productie te Breken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Afhankelijkheden Bijwerken Zonder Productie te Breken",
  "description": "Een door AI gebouwde app hangt af van honderden pakketten die niemand koos. Hoe u weet welke kwetsbaar zijn, welke updates dringend zijn, en hoe u ze toepast zonder elke vrijdag aan een kapotte build te besteden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-dependency-updates-without-breaking-production" }
}
</script>

Tel de pakketten die uw product installeert. Niet degene waar u om vroeg — het totaal, inclusief alles waar die pakketten van afhangen. Voor een typische Lovable- of Bolt-applicatie ligt dat ergens tussen de zeshonderd en vijftienhonderd.

U koos er misschien vijftien. De rest kwam mee omdat iets wat u koos ze nodig had, en ze draaien met dezelfde rechten als de code die u schreef.

Dit is geen pleidooi om alles zelf te bouwen. Het is een pleidooi om te weten wat u hebt, want het alternatief is een product waarvan de beveiliging volledig afhangt van code die u nooit hebt gezien en niet kunt benoemen.

## De Lockfile Is het Feit

Uw pakketbestand zegt wat u wilt. Uw lockfile zegt wat u werkelijk hebt — elk pakket, elke versie, elke transitieve afhankelijkheid, exact vastgezet.

Twee gevolgen. Ze moet worden gecommit, anders installeert uw productiebuild misschien andere versies dan die u testte, wat zowel een betrouwbaarheids- als een beveiligingsprobleem is. En ze is het document dat de vraag "worden wij geraakt?" beantwoordt wanneer er een kwetsbaarheid wordt aangekondigd — één zoekactie in de lockfile, dertig seconden, in plaats van een middag onzekerheid.

Producten die door AI-tools zijn gebouwd, missen soms volledig een gecommitte lockfile, omdat de tool de afhankelijkheden zelf beheerde en het begrip nooit opdook. Ontbreekt de uwe, dan is dat het eerste wat u oplost.

## Weten Wat Kwetsbaar Is

De basis kost niets. Uw pakketbeheerder heeft een auditcommando dat uw lockfile vergelijkt met een publieke kwetsbaarheidsdatabase en opsomt wat overeenkomt. Voer het vandaag uit; de eerste run op een door AI gebouwd project van een jaar oud levert doorgaans tientallen resultaten op.

Automatiseer het daarna: een controle bij elke build, en een dienst die een pull request opent wanneer een nieuwe melding u raakt. De gratis niveaus van de gangbare tools zijn op deze schaal ruim voldoende.

De uitvoer zal veel ruis bevatten, en die leren lezen is de echte vaardigheid.

## Niet Elke Melding Is Uw Probleem

Twee vragen bepalen of een gemelde kwetsbaarheid voor u ertoe doet.

**Is de getroffen code in uw product bereikbaar?** Een kwetsbaarheid in een pakket dat alleen tijdens de build draait, op uw machine, is niet blootgesteld aan uw gebruikers. Een kwetsbaarheid in een pakket dat binnenkomende verzoeken afhandelt, wel.

**Vereist de aanval omstandigheden die u hebt?** Veel meldingen vereisen een specifieke configuratie, een bepaalde functie die met onbetrouwbare invoer wordt aangeroepen, of een omgeving die u niet draait.

Daarom is "kritiek" in een melding niet hetzelfde als kritiek voor u. Een probleem met hoge ernst in een tool die alleen voor ontwikkeling is, kan redelijkerwijs wachten op de volgende batch; een gemiddeld probleem in uw pad voor verzoekafhandeling heeft misschien vandaag aandacht nodig.

Die afweging is het waard om bewust te maken, in plaats van alles reflexmatig bij te werken of de lijst te negeren omdat ze lang is. Beide zijn mislukkingen, en de tweede komt veel vaker voor.

## Een Updateroutine Die de Werkelijkheid Overleeft

Het patroon dat werkt voor een klein product, heeft drie snelheden.

**Beveiligingsupdates, snel.** Alles wat vanuit gebruikersinvoer bereikbaar is, binnen dagen toegepast, en buiten het schema als het ernstig is.

**Patch- en minor-updates, volgens schema.** Eens per twee weken of eens per maand, in één batch, wanneer u tijd hebt om te testen. Deze zijn grotendeels veilig, en ze een jaar laten opstapelen is wat upgraden pijnlijk maakt.

**Major-versies, bewust.** Eén tegelijk, lees de migratie-instructies, neem echt tijd. Nooit meerdere tegelijk, en nooit op een vrijdag.

De gewoonte die de middelste snelheid volhoudbaar maakt: bijwerken, uw controles draaien, naar staging deployen, het product tien minuten gebruiken, deployen. Heeft uw product geen geautomatiseerde tests, dan doen die tien minuten gebruik al het werk, en ze horen een geschreven lijst te zijn van waar u op klikt in plaats van een improvisatie.

## Verminder Waar U van Afhangt

De goedkoopste beveiligingsverbetering op dit terrein is minder afhankelijkheden hebben.

AI-codetools installeren gemakkelijk pakketten — een datumbibliotheek voor één datumformaat, een hulppakket voor één functie, een componentenbibliotheek die voor één knop wordt gebruikt. Elk is een blijvende last met een eigen afhankelijkheidsboom, een eigen beheerder, en een eigen kans om te worden verlaten of gecompromitteerd.

Maak eens per kwartaal een lijst van uw directe afhankelijkheden en vraag bij elk: wat doet dit, gebruiken we het nog, en kunnen we zonder. Drie of vier verwijderen is gebruikelijk, en elke verwijdering neemt een deelboom van transitieve pakketten mee.

Let ook op signalen van verlating: geen release in twee jaar, een gearchiveerde repository, één beheerder zonder activiteit. Die zijn niet dringend, maar het zijn de pakketten waar een toekomstige kwetsbaarheid geen oplossing zal krijgen.

## De Supply-Chainaanval Is Nu Echt

De aanval die gangbaar is geworden, is geen kwetsbaarheid die in goede code wordt ontdekt. Het is kwaadaardige code die bewust wordt gepubliceerd — het account van de beheerder van een populair pakket gecompromitteerd, of een nieuwe versie met iets erin dat uw omgevingsvariabelen leest en ergens anders naartoe stuurt.

Drie gewoontes verminderen de blootstelling merkbaar. Zet exacte versies vast in de lockfile, wat u al doet. Wacht met het overnemen van gloednieuwe releases van pakketten die iets gevoeligs raken, aangezien de meeste kwaadaardige releases binnen dagen worden ontdekt. En controleer wat er tijdens de installatie draait: scripts die automatisch bij de installatie worden uitgevoerd, zijn het gebruikelijke bezorgmechanisme, en de meeste pakketbeheerders kunnen ze uitschakelen.

Voor een klein product is dit proportioneel. Niemand verwacht dat u duizend pakketten beoordeelt. Weten welke vijftien u koos, en geen zestiende installeren zonder reden, levert het grootste deel van het voordeel.

## De Pakketten Die AI-Tools Verzinnen

Eén faalwijze hoort specifiek bij producten die met codeerassistenten zijn gebouwd, en het is de moeite waard er direct op te controleren: een afhankelijkheid die niet bestaat, of niet bestond totdat iemand de fout opmerkte.

Modellen stellen af en toe een aannemelijk klinkende pakketnaam voor die nooit is gepubliceerd. Meestal mislukt de installatie en is de fout duidelijk. De gevaarlijke versie is wanneer iemand die naam achteraf registreert, juist omdat assistenten hem blijven voorstellen — een techniek met een eigen naam in beveiligingskringen en een groeiend aantal echte gevallen. Het pakket installeert zonder problemen, doet iets nuttigs genoeg om geen vragen op te roepen, en draait met de rechten van uw applicatie.

De controle is snel. Loop uw directe afhankelijkheden langs en kijk bij elk pakket dat u niet herkent naar de repository: hoe lang het bestaat, hoeveel mensen het gebruiken, wie het beheert, en of het is wat de naam doet vermoeden. Een pakket met veertig downloads per week en één commit, in een productieapplicatie, verdient een verklaring.

Dezelfde blik vangt een verwant probleem — een afhankelijkheid die echt is maar verkeerd. Assistenten pakken soms een pakket dat een ander probleem oplost, of een verouderde voorganger van het bedoelde pakket, omdat beide veel in trainingsdata voorkwamen. Die installeren geen malware; ze voegen alleen gewicht en uiteindelijk wrijving toe.

Geen van beide controles kost veel tijd, en beide doet u het best nu één keer en daarna telkens wanneer een assistent iets toevoegt waar u niet bij naam om vroeg.

## Wat te Doen Als een Pakket Wordt Verlaten

Uiteindelijk wordt een van uw afhankelijkheden niet meer onderhouden. De repository wordt stil, een melding over een kwetsbaarheid blijft onbeantwoord, en er komt geen oplossing.

Vier opties, ongeveer in de volgorde waarin u ze overweegt.

**Vervang het.** Meestal het juiste antwoord als er een actief onderhouden alternatief is en de wijziging overzichtelijk is. De kosten zijn een dag; het voordeel is dat het probleem voorgoed weg is.

**Verwijder het.** Controleer eerst of u er genoeg van gebruikt om überhaupt een afhankelijkheid te rechtvaardigen. Een pakket dat één functie levert die u in twintig regels kunt schrijven, is een pakket om te verwijderen, en dat is vaker het geval dan het aanvoelt.

**Fork en patch het.** Redelijk wanneer het pakket klein is en de oplossing begrepen. U onderhoudt het nu zelf, wat een echte verplichting is, maar voor honderd regels code is het een kleinere verplichting dan het klinkt.

**Zet het vast en isoleer het.** Wanneer vervangen echt duur is: houd de versie vast, documenteer waarom, en verklein wat het raakt — zorg dat het nooit direct onbetrouwbare invoer verwerkt als de kwetsbaarheid dat vereist.

Wat geen optie is, is het onbekeken laten met een notitie dat er een update beschikbaar is. Schrijf de beslissing en de reden op, zodat de volgende die kijkt — inclusief uzelf, over een jaar — het onderzoek niet opnieuw vanaf het begin doet.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve dag: een gecommitte lockfile, een auditrun met de resultaten beoordeeld op bereikbaarheid in plaats van op ernstlabel, geautomatiseerde scans bij elke build met meldingen naar een plek die u leest, een geschreven updateroutine met drie snelheden, een korte handmatige testlijst voor producten zonder geautomatiseerde tests, ongebruikte en verlaten directe afhankelijkheden verwijderd, installatiescripts beoordeeld, en een notitie die vastlegt waar elke directe afhankelijkheid voor is, zodat de volgende review sneller gaat dan deze.

LaunchStudio behandelt afhankelijkheden in de beveiligingsreview en houdt ze actueel binnen de managed regeling van €49 per maand, waarbij updates worden toegepast en getest in plaats van zich op te stapelen. De engineers zijn van Manifera — elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vraag ons wat uw lockfile bevat](https://launchstudio.eu/nl/#contact). De meeste oprichters hebben er nooit naar gekeken.

## Echt voorbeeld

### Veertien Maanden Zonder Update

Menno Zwartjes bouwde Werkbonnen in Lovable: digitale werkbonnen en handtekeningen voor installatie- en onderhoudsbedrijven, 47 bedrijven met zo'n 400 monteurs.

Hij had nog nooit een afhankelijkheid bijgewerkt. De applicatie werkte, niets leek kapot, en het onderwerp was nooit ter sprake gekomen. Veertien maanden na de lancering leverde een auditrun 63 meldingen op, waarvan 11 in pakketten die binnenkomende verzoeken afhandelen.

Eén deed er direct toe: een bibliotheek voor het verwerken van verzoeken met een bekende fout waarmee een gemanipuleerde payload onbeperkt geheugen kon verbruiken. Zijn product accepteerde werkbonnen vanaf de telefoons van monteurs op publieke endpoints, precies de blootstelling die de melding beschreef. Ze was negen maanden eerder gepubliceerd.

Drie werkdagen: de lockfile gecommit, die nooit in de repository had gestaan, zodat builds elke keer opnieuw versies hadden opgehaald; de 63 meldingen beoordeeld, waarvan er 11 vanuit gebruikersinvoer bereikbaar waren, 34 alleen voor ontwikkeling waren en de rest configuraties vereiste die hij niet draaide; de 11 direct toegepast, inclusief de verwerkingsbibliotheek, met het product doorlopen volgens een geschreven testlijst; de set voor ontwikkeling in één batch toegepast in de week daarna; twee major-versie-upgrades apart ingepland en één voor één gedaan over twee weken; geautomatiseerde scans gekoppeld aan de build met meldingen naar zijn telefoon en een dienst die pull requests opent voor nieuwe meldingen; 9 directe afhankelijkheden verwijderd als ongebruikt, waaronder een datumbibliotheek voor één datumformaat en een componentenbibliotheek voor één knop, wat 190 transitieve pakketten verwijderde; installatiescripts standaard uitgeschakeld; en een updateroutine op papier — beveiliging binnen dagen, minor maandelijks, major bewust.

**Resultaat:** het probleem met geheugenuitputting werd gedicht na negen maanden blootstelling, zonder aanwijzing dat het was misbruikt. Het totale aantal pakketten daalde van 1.340 naar 1.150. Menno besteedt nu zo'n 40 minuten per maand aan updates, en zegt dat het belangrijkste voordeel van de routine is dat niets zich opstapelt tot het soort upgrade dat een week kost.

> *"Niemand vertelde me dat afhankelijkheden iets waren wat ik bezat. Ze kwamen mee met de code, ze werkten, en veertien maanden lang wist ik niet dat er een lijst was om naar te kijken."*
> — **Menno Zwartjes, Oprichter, Werkbonnen (Hengelo)**

**Kosten & Doorlooptijd:** €2.600 (herstel van de lockfile, beoordeling en toepassing van meldingen, major-versie-upgrades, geautomatiseerde scans en meldingen, vermindering van afhankelijkheden, versteviging van installatiescripts, documentatie van de updateroutine) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Moet ik elke kwetsbaarheid oplossen die mijn audit meldt?

Nee. Beoordeel op bereikbaarheid: een fout in een buildtool is niet blootgesteld aan gebruikers, terwijl een fout in de afhandeling van verzoeken dringend kan zijn. Ernstlabels beschrijven de fout, niet uw blootstelling.

### Hoe vaak moet ik afhankelijkheden bijwerken?

Beveiligingsoplossingen binnen dagen, patch- en minor-updates in een maandelijkse batch, major-versies één tegelijk met echt de tijd ervoor. Alles laten opstapelen is wat upgraden pijnlijk maakt.

### Waarom doet de lockfile ertoe?

Ze legt precies vast wat u hebt, zodat uw productiebuild overeenkomt met wat u testte en u bij een melding binnen dertig seconden kunt beantwoorden of u wordt geraakt.

### Hoe verminder ik het supply-chainrisico?

Heb minder afhankelijkheden, zet exacte versies vast, wacht met gloednieuwe releases van gevoelige pakketten, en schakel installatiescripts uit. Duizend pakketten beoordelen wordt niet verwacht; niet zonder reden het duizend-en-eerste toevoegen wel.

### Wat als mijn app geen tests heeft?

Schrijf een korte lijst van waar u na een update op klikt — de vijf of zes paden die ertoe doen. Het is geen testsuite, maar het is herhaalbaar, en improvisatie is dat niet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik elke gemelde kwetsbaarheid oplossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Beoordeel of de getroffen code vanuit gebruikersinvoer bereikbaar is. Fouten die alleen tijdens de build draaien, zijn niet blootgesteld aan uw gebruikers."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moeten afhankelijkheden worden bijgewerkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beveiligingsoplossingen binnen dagen, minor- en patch-updates maandelijks in een batch, major-versies afzonderlijk met de tijd ervoor."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom doet een gecommitte lockfile ertoe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze garandeert dat productie overeenkomt met wat u testte, en laat u binnen seconden beantwoorden of een melding u raakt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verminder ik supply-chainrisico in een klein product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Minder afhankelijkheden, exact vastgezette versies, wachten voordat u gloednieuwe releases overneemt, en installatiescripts uitgeschakeld."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe werk ik veilig bij zonder geautomatiseerde tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Houd een geschreven lijst bij van de vijf of zes paden die u na elke update doorloopt. Herhaalbaar is beter dan geïmproviseerd."
      }
    }
  ]
}
</script>
