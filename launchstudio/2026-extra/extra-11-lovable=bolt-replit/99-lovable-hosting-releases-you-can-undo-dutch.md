---
Titel: "Lovable Hosting: Releases die je kunt terugdraaien"
Trefwoorden: lovable hosting, staging, rollback, feature flags, veilige releases, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Lovable Hosting: Releases die je kunt terugdraaien

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Releases die je kunt terugdraaien",
  "description": "Snel deployen is pas veilig als terugdraaien saai en voorspelbaar is. Staging met eigen data, rollbacks binnen één minuut, feature flags en database-migraties die onomkeerbaar zijn.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/99-lovable-hosting-releases-you-can-undo" }
}
</script>

De grote aantrekkingskracht van bouwen met AI-tools is dat wijzigingen goedkoop zijn. Je bedenkt 's ochtends iets en rond de lunch staat het live. Voor een product zonder gebruikers is dat een ongekend voordeel.

Op het moment dat er betalende klanten binnengekomen zijn, verandert die eigenschap plotseling in een risico: een aanpassing die tien minuten kost om te maken, kan drie uur kosten om terug te draaien - als terugdraaien überhaupt nog mogelijk is. En de snelheid die je zo productief maakte, zorgt er nu voor dat een foute beslissing direct iedereen raakt voordat iemand ernaar heeft gekeken.

Het antwoord is niet om langzamer te gaan werken. Het antwoord is om terugdraaien zo saai en voorspelbaar te maken dat snel shippen geen gok meer is.

## Drie omgevingen en waar elke voor dient

**Development** is waar jij en je tooling werken. Het bevat fictieve testdata, het mag op elk moment kapotgaan en niemand van buitenaf kan erbij.

**Staging** is een exacte kopie van productie - dezelfde codepaden, dezelfde configuratiestructuur, maar een eigen database - waar een wijziging gecontroleerd wordt voordat gebruikers ermee in aanraking komen. Dit is de omgeving die beginnende producten vaak overslaan, en het is precies de omgeving die zichzelf bij het eerste incident direct terugbetaalt.

**Productie** is wat je klanten dagelijks gebruiken. Deze omgeving mag uitsluitend wijzigingen ontvangen die aantoonbaar al ergens anders werkend zijn gezien.

Twee regels maken dit effectief in plaats van puur decoratief. Staging krijgt eigen data, geanonimiseerd vanuit productie en nooit direct gekoppeld - een staging-omgeving die naar de live database wijst, betekent immers dat een testverwijdering een echte dataverwijdering wordt. Daarnaast moet staging afgeschermd zijn voor zoekmachines en bij voorkeur beveiligd zijn met een wachtwoord, anders creëer je onbedoeld een tweede versie van je website die concurreert met het origineel.

## Rollback is de belangrijkste feature

Stel jezelf één simpele vraag: als de wijziging die je op het punt staat live te zetten fout blijkt te zijn, hoe lang duurt het dan voordat deze is teruggedraaid, en ken je de exacte stappen?

Als het antwoord denkwerk vereist, heb je geen rollback-procedure - je hebt hoop. En het moment om die stappen uit te zoeken is niet wanneer betalende klanten er actief last van ondervinden.

De meeste hostingplatforms bewaren voorgaande deployments en kunnen er binnen zestig seconden een herstellen. Zoek vandaag nog uit waar die knop zit, zolang er niets aan de hand is. Test het vervolgens bewust: deploy iets triviaals, draai het terug en meet de tijd. Een rollback die je al eens in de praktijk hebt uitgevoerd, durf je direct in te zetten; een rollback waar je alleen over gelezen hebt, stel je uit op exact het verkeerde moment.

## De wijzigingen die je niet kunt terugdraaien

Dit is het belangrijkste onderdeel en tegelijkertijd het minst begrepen aspect.

Het terugdraaien van code is eenvoudig. Het terugdraaien van een databasewijziging is daarentegen vaak onmogelijk, omdat de data intussen is doorgegroeid. Als een release een kolom heeft weggegooid (`DROP COLUMN`), verwacht de vorige codeversie een kolom die geen enkele waarde meer bevat. Als een migratie velden heeft getransformeerd, zijn de oude waarden definitief verdwenen.

Schema-wijzigingen vereisen daarom de beproefde *expand-and-contract*-discipline: voeg eerst de nieuwe structuur toe, deploy code die naar zowel de oude als de nieuwe velden schrijft, voer een backfill uit, deploy code die uitsluitend de nieuwe structuur leest, en verwijder de oude structuur pas in een latere release zodra alles stabiel draait. Elke afzonderlijke stap is hierdoor omkeerbaar, en op geen enkel moment conflicteert de draaiende applicatie met het live database-schema.

Hetzelfde geldt voor onomkeerbare acties in de buitenwereld: verzonden e-mails, afgeschreven betalingen, verwijderde bestanden en afgeleverde notificaties. Een release die bij het opstarten direct zulke acties triggert, kan niet ongedaan worden gemaakt door de code te reverten. Dat is een uitstekende reden om dergelijke functionaliteiten achter een feature flag te plaatsen in plaats van direct achter een deploy.

## Feature flags scheiden deployen van releasen

Een kleine techniek met een enorme impact.

Een feature flag is een eenvoudige conditie in je code die controleert of een functie getoond moet worden. Hierdoor kan code al veilig gedeployed worden terwijl de functionaliteit zelf uitgeschakeld blijft. Je kunt hem aanzetten voor jezelf, daarna voor een vriendelijke testklant, vervolgens voor iedereen - en binnen seconden uitschakelen als er iets mis blijkt te zijn.

Drie use cases maken deze moeite meer dan waard voor een compact product:
1. Een nieuwe functionaliteit geleidelijk uitrollen in plaats van direct voor vierhonderd gebruikers tegelijk.
2. Een zware of kostbare feature tijdelijk uitschakelen tijdens piekbelasting, wat cruciaal kan zijn om een launch-dag te overleven.
3. Een risicovolle wijziging loskoppelen van de deployment, zodat terugdraaien geen nieuwe release vereist.

Houd het eenvoudig: gebruik een configuratiewaarde of een kleine databasetabel, geen complex extern platform. En ruim flags weer op zodra een feature definitief gesetteld is, anders verandert je codebase binnen een jaar in een museum van verweesde condities die niemand meer durft te verwijderen.

## Een release-routine voor één persoon

**Vooraf:** de wijziging staat op staging en je hebt hem getest zoals een echte gebruiker dat zou doen. Als de wijziging raakt aan data, betalingen of permissies, heeft iemand anders meegekeken - en als je alleen bent, lees je de git diff bewust regel voor regel door in plaats van blind te vertrouwen op de gegenereerde output.

**Tijdens:** deploy op een tijdstip waarop je de monitoring in de gaten kunt houden. Niet op vrijdagmiddag om vijf uur, en niet vlak voordat je de deur uitloopt.

**Achteraf:** neem tien minuten de tijd met het live product en de foutopsporing (error tracking). Laad de pagina, voer de gewijzigde flow handmatig uit, log in als een reguliere gebruiker en controleer of er nieuwe exceptions of waarschuwingen verschijnen.

Dat is de complete routine. Het kost vijftien minuten per release en vangt het overgrote merendeel van de fouten af die anders bij je klanten terechtkomen.

## Wanneer automatiseren en wanneer juist niet

Automatisch deployen bij elke commit (continuous deployment) is geweldig voor een product met een uitgebreide geautomatiseerde testsuite. Voor een applicatie zonder tests is het riskant, omdat de enige kwaliteitscontrole op dat moment een menselijk oog is.

De verstandige groeicurve: begin met handmatige deployments met een vooraf geteste rollback; ga vervolgens naar automatische deployments naar staging met handmatige promotie naar productie; schakel pas over naar volledige productie-automatisering zodra er betrouwbare tests zijn. Direct naar de eindfase springen omdat volwassen teams dat doen, geeft je wel de snelheid van zo'n team, maar geen van hun vangnetten.

Wat wél direct vanaf dag één geautomatiseerd moet worden: het build-proces zelf. Zorg dat deployen één enkele actie is in plaats van een lijst handmatig te onthouden terminalcommando's. De meeste mislukte releases bij kleine bedrijven zijn immers geen programmeerfouten - het zijn vergeten tussenstappen.

## Wanneer een release toch misgaat

Het gaat een keer fout. Het verschil tussen twintig minuten overlast en een rampweek zit volledig in wat je tijdens de eerste vijf minuten doet.

**Draai eerst terug. Analyseer pas daarna.** De eerste reflex is vaak om de oorzaak grondig te willen begrijpen voordat je ingrijpt. Als klanten getroffen worden, is dat de verkeerde volgorde. Zet direct de vorige versie terug, verifieer dat het product weer stabiel draait, en onderzoek de bug vervolgens rustig zonder tijdsdruk. Oprichters die onder stress een haastige "fix forward" proberen te forceren, stapelen bijna altijd een tweede fout bovenop de eerste.

**Deploy geen overhaaste noodoplossing.** Een codefix die binnen drie minuten onder paniek in elkaar is gezet, zonder review of test, is de snelste manier om van één haperende functie een complete storing te maken.

**Controleer direct of er data is aangetast.** Dit bepaalt of de rollback voldoende was. Code zet je feilloos terug; records die door de corrupte versie zijn aangemaakt of gewijzigd verdwijnen niet zomaar mee. Breng in kaart wat er in dat tijdvenster is weggeschreven en corrigeer dat gecontroleerd.

**Informeer iedereen die er last van heeft gehad.** Kort, feitelijk en helder: wat er mis was, hoe lang het duurde, wat je hebt hersteld en wat zij moeten doen. Een klant die een bug meldt en niets meer hoort, voelt zich genegeerd; een klant die binnen het uur een openhartige update krijgt, herinnert zich meestal de professionele afhandeling in plaats van de storing.

**Noteer het feitelijke verloop zolang het vers in het geheugen zit.** Wat is er gewijzigd, wanneer brak het, hoe werd het ontdekt en welke acties zijn ondernomen? Morgen herinner je je slechts een versimpelde versie, terwijl de kernoorzaak juist in de details zit.

**Vraag je af wat dit had kunnen voorkomen.** Een extra controle op staging, een geautomatiseerde test, een handmatige diff-review of een feature flag. Eén procesverbetering per incident zorgt ervoor dat je deployment-straat structureel veiliger wordt. Maak er altijd een proceswijziging van, nooit het loze voornemen om 'volgende keer voorzichtiger te zijn'.

## Dit professioneel inrichten

Voor een draaiend product kost dit ongeveer één werkdag: een staging-omgeving met geanonimiseerde data die geblokkeerd is voor zoekmachines; een reproduceerbaar build-proces vanuit git zodat elke commit herleidbaar gedeployed kan worden; een rollback-procedure die getest en getimed is; een eenvoudig feature flag-mechanisme; het expand-and-contract-patroon voor database-migraties zodat code en schema nooit conflicteren; en een beknopte release-checklist die zo praktisch is dat je hem daadwerkelijk volgt.

LaunchStudio richt dit in als onderdeel van productierijpheid en onderhoudt het binnen het managed hosting-arrangement van € 49 per maand. Onze engineers komen van Manifera: elf jaar ervaring met het releasen van productiesystemen voor opdrachtgevers als Vodafone, TNO en CFLW, vanuit Amsterdam Herengracht 420, Singapore en Ho Chi Minhstad.

[Vertel ons hoe je nu deployt](https://launchstudio.eu/nl/#contact) voor een gericht releaseplan, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een verwijderde kolom om half vijf 's middags

Mark Oudshoorn bouwde Kassakoppeling met Lovable: een kassakoppelingssysteem voor zelfstandige winkeliers, gebruikt door 34 winkels rond Gorinchem en Leerdam om verkopen live te synchroniseren met voorraad- en boekhoudpakketten.

Hij deployde altijd direct naar productie vanuit zijn werkomgeving, wat een jaar lang prima was gegaan. Er was geen staging-omgeving en hij had nog nooit een rollback uitgevoerd.

Op een donderdagmiddag vroeg hij een AI-agent om de verkooptabel op te schonen. De gegenereerde migratie bevatte een onopgemerkte `DROP COLUMN` op het veld dat bijhield vanaf welke fysieke kassa een transactie afkomstig was. De applicatie bleef gewoon draaien en gaf geen foutmeldingen. Maar het kassa-overzicht dat elf van zijn winkeliers dagelijks gebruikten voor de kassaopmaak van het personeel was leeg, en de export naar het boekhoudpakket wees alle omzet toe aan één enkele kassa.

Mark ontdekte het pas om half vijf toen een winkelier bezorgd opbelde. Het terugdraaien van de code loste niets op, want de data in de database was al definitief verdwenen. De meest recente backup stamde van die ochtend vroeg; het terugzetten van die backup zou betekenen dat een volledige handelsdag aan transacties voor alle 34 winkels verloren zou gaan. Zomaar restoren was dus evenmin een optie.

Zes werkdagen aan herstelwerkzaamheden volgden: de kassakolom werd voor de getroffen dag handmatig gereconstrueerd door transacties te matchen met de fysieke papieren kastrookjes van de winkeliers (twee winkels konden dit niet volledig aanleveren, wat in overleg werd afgeboekt); er werd een staging-omgeving ingericht met geanonimiseerde productiedata en afscherming voor zoekmachines; het build-proces werd reproduceerbaar gekoppeld aan git-commits; de rollback-procedure werd getest en vastgelegd op 40 seconden; het expand-and-contract-principe werd verplicht gesteld voor alle schema-wijzigingen, inclusief de regel dat Mark elke datamigratie handmatig leest vóór uitvoering en vooraf een snapshot maakt; er werd een lichtgewicht feature flag-systeem toegevoegd; database-rechten werden gescheiden zodat de standaard applicatie-gebruiker nooit meer tabellen of kolommen kan droppen; en er werd een vijfregelige release-checklist opgesteld die op zijn monitor werd geplakt.

**Resultaat:** elf maanden zonder incidenten. Mark geeft aan dat de kleinste verandering voor hem de meeste waarde heeft: de verplichte regel om datamigraties eerst handmatig te lezen, waarmee hij sindsdien al twee destructieve AI-suggesties op tijd heeft onderschept.

> *"Het terugdraaien van de code kostte dertig seconden en veranderde helemaal niets, omdat de kolom weg was. Dat was de middag waarop ik leerde dat 'ongedaan maken' en 'rollback' niet hetzelfde zijn."*
> - **Mark Oudshoorn, Oprichter, Kassakoppeling (Gorinchem)**

**Kosten & Doorlooptijd:** € 3.400 (datareconstructie, staging-omgeving, reproduceerbare builds met geteste rollback, expand-and-contract migraties, feature flags en scheiding van databaserechten) - opgeleverd in 6 werkdagen.

## Veelgestelde vragen

### Heb ik echt een staging-omgeving nodig?

Zodra betalende klanten afhankelijk zijn van je product, absoluut. Het is een volledige kopie van productie met eigen geanonimiseerde data, waar je wijzigingen in de praktijk controleert voordat gebruikers ermee geconfronteerd worden. Staging laten wijzen naar de live productiedatabase ontkracht het hele principe, omdat een testverwijdering dan alsnog echte data wist.

### Hoe snel moet een rollback kunnen worden uitgevoerd?

Binnen één tot twee minuten, en je moet het minimaal één keer in de praktijk hebben geoefend. Zoek vandaag nog de herstelknop op je platform terwijl alles rustig is, deploy een triviale wijziging, draai deze terug en klok de tijd. Een rollback die je nog nooit hebt gebruikt, stel je geheid uit wanneer de spanning oploopt.

### Waarom kan ik een databasewijziging niet zomaar terugdraaien?

Omdat het terugzetten van oude code verwijderde data niet terugbrengt. Een weggegooide kolom of overschreven veldwaarde is definitief verloren. Hanteer daarom de expand-and-contract-methode: toevoegen, dubbel wegschrijven, backfillen, leespunt omzetten en pas later opruimen. Zo blijft elke stap individueel omkeerbaar.

### Waarvoor dienen feature flags in een kleiner product?

Om nieuwe features stapsgewijs uit te rollen, zware functies direct uit te kunnen schakelen tijdens piekbelasting, en risicovolle wijzigingen los te koppelen van deployments zodat uitschakelen een kwestie van seconden is zonder nieuwe release. Houd ze eenvoudig en ruim ze na adoptie direct op.

### Moet ik bij elke commit automatisch naar productie deployen?

Niet zolang je nog geen waterdichte geautomatiseerde testsuite hebt. Doorloop een beheerste groeicurve: begin met handmatige deploys met een geteste rollback, ga door naar automatische staging met handmatige goedkeuring voor productie, en automatiseer pas volledig als je tests vertrouwt. Zorg wel dat het build-proces direct geautomatiseerd is om menselijke fouten te voorkomen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik echt een staging-omgeving nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodra klanten afhankelijk zijn van je product wel: een complete kopie met eigen geanonimiseerde data die nooit gekoppeld is aan de live database."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe snel moet een rollback kunnen worden uitgevoerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Binnen één tot twee minuten. Test dit vooraf door een triviale wijziging te deployen, terug te draaien en te timen terwijl er geen storing is."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom kan ik een databasewijziging niet zomaar terugdraaien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Code reverten herstelt geen verloren data. Gebruik expand-and-contract zodat elke stap individueel omkeerbaar is en code nooit botst met het schema."
      }
    },
    {
      "@type": "Question",
      "name": "Waarvoor dienen feature flags in een kleiner product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor geleidelijke uitrol, het uitschakelen van zware functies bij piekbelasting en het direct kunnen intrekken van risicovolle functies zonder herdeploy."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik bij elke commit automatisch naar productie deployen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pas als je een betrouwbare testsuite hebt. Automatiseer de build direct, deploy daarna geautomatiseerd naar staging en pas later volledig naar productie."
      }
    }
  ]
}
</script>
