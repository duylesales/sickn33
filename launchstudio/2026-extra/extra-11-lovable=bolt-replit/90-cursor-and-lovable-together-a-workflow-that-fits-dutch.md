---
Titel: "Cursor en Lovable Samen Gebruiken: Een Workflow Die Wél Werkt"
Trefwoorden: Cursor, Lovable, vibe coding developer, github sync, workflow, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Cursor en Lovable Samen Gebruiken: Een Workflow Die Wél Werkt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor en Lovable Samen Gebruiken: Een Workflow Die Wél Werkt",
  "description": "Een visuele app-builder en een geavanceerde code-editor combineren op hetzelfde project werkt uitstekend, totdat ze van mening verschillen over de codebase. Hoe je het werk verdeelt, versiebeheer als centrale waarheid bewaakt en voorkomt dat je je eigen werk overschrijft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/90-cursor-and-lovable-together-a-workflow-that-fits" }
}
</script>

Zodra een SaaS-product zowel een actieve gebruikersinterface heeft die klanten dagelijks zien, als complexe bedrijfslogica waarvan processen afhankelijk zijn, ontdekken de meeste oprichters dat ze beide soorten gereedschap nodig hebben. De visuele web-builder (zoals Lovable) werkt sneller voor het ontwerpen van schermen. De code-editor (zoals Cursor) presteert oneindig veel beter voor alles wat zich onder de motorkap afspeelt.

Het combineren van beide werelden is een uitstekende strategie, maar introduceert één acuut risico: twee afzonderlijke systemen die elk wijzigingen kunnen doorvoeren in je broncode, met een totaal ander beeld van hoe het project in elkaar zit. Pak je dit slordig aan, dan resulteert dat in de meest frustrerende middag uit je ondernemerschap: zorgvuldig handwerk dat geruisloos wordt overschreven door een andere bewerking die je zelf hebt uitgevoerd.

## Waarom elke tool uitblinkt in zijn eigen domein

**De visuele builder blinkt uit in de buitenkant.** Een nieuw dashboard, een interactief formulier, een visuele grid of een conversieflow tussen pagina's. Je ziet het resultaat direct ontstaan terwijl je het via prompts beschrijft - een feedbackloop die vele malen sneller werkt dan handmatig code schrijven en continu een browser refreshen.

**De code-editor blinkt uit in de constructieve architectuur.** Het consolideren van een bedrijfsregel die per ongeluk op drie plekken is geprogrammeerd, het extraheren van configuraties, het geautomatiseerd doorvoeren van één patroon over dertig bestanden, het schrijven van unit tests en het analyseren welke modules van elkaar afhankelijk zijn. De eenheid van werk is hier het totale project, niet slechts één afzonderlijk scherm.

De frustratie ontstaat wanneer je de ene tool dwingt om het werk van de andere te doen. Vraag je een visuele builder om een diepgaande code-refactoring, dan genereert hij vaak een parallelle implementatie naast de bestaande logica. Vraag je een code-editor om een complexe interface vanaf nul te ontwerpen, dan krijg je een omslachtige, trage variant van iets wat je in een visuele editor binnen vijf minuten had gerealiseerd.

## Versiebeheer (Git) is het bindende contract

Er is één gouden regel die deze samenwerking soepel laat verlopen: **de Git-repository is de absolute bron van waarheid**, en beide tools zijn louter instrumenten om wijzigingen in die repository aan te brengen.

Moderne builders die synchroniseren met GitHub maken dit conceptueel eenvoudig: visuele prompts verschijnen als Git-commits, en commits die je lokaal pusht komen direct beschikbaar in de editor van de builder. Zodra die koppeling staat, borgen drie gewoontes een conflictloze workflow:

**Werk op één plek tegelijk.** Nooit gelijktijdig in beide tools aan hetzelfde functionele gebied werken. Dit klinkt triviaal, maar is dé regel die voortdurend wordt overtreden: de web-builder staat immers open in een browsertabblad, en het voelt verleidelijk om daar snel even een knoptekst aan te passen terwijl je lokaal midden in een half-voltooide code-refactor zit.

**Pull vóórdat je begint en push zodra je afrondt.** Elke sessie opnieuw, in beide richtingen. Het leeuwendeel van alle merge-conflicten ontstaat doordat een werksessie startte op basis van een verouderde versie van de broncode.

**Commit in kleine eenheden met duidelijke toelichtingen.** Mocht er toch een conflict ontstaan tussen de tools, dan zorgen kleine, afgebakende commits ervoor dat het probleem binnen enkele minuten oplosbaar is.

Synchroniseert jouw builder nog niet met een externe Git-repository? Richt dat dan als allereerste in. Zonder centrale repository is er geen gedeelde definitie van het project en drijven beide omgevingen binnen no-time onherstelbaar uit elkaar.

## Waar de twee systemen daadwerkelijk botsen

Vier specifieke knelpunten waar je vooraf op moet anticiperen:

**Hergenereerde bestanden.** Vraag je de visuele builder om een detail op een scherm aan te passen, dan kan hij besluiten om het gehele componentbestand opnieuw te genereren. Daarbij wordt alle handgeschreven logica die jij lokaal had toegevoegd genadeloos gewist. De oplossing is strikte ontkoppeling: bewaar je bedrijfslogica op een plek waar de builder niets te zoeken heeft - een aparte module of service-bestand - en laat het visuele scherm die logica uitsluitend aanroepen. Gegenereerde bestanden blijven gegenereerd; jouw maatwerkcode leeft elders.

**Codeformatting-ruis.** Beide tools hanteren vaak andere regels voor inspringing en witregels, wat resulteert in commits vol met cosmetische aanpassingen die de werkelijke codewijzigingen onzichtbaar maken. Kies één formatteringstool (zoals Prettier), configureer deze voor beide omgevingen en leg het configuratiebestand vast in de repository.

**Package-afhankelijkheden (dependencies).** Beide platformen kunnen npm-packages toevoegen. Zorg dat het `package-lock.json` bestand strikt gecommit blijft en controleer elke wijziging, om ongemerkte versieconflicten te voorkomen.

**Omgevingsvariabelen.** De manier waarop de builder geheime sleutels beheert kan afwijken van jouw lokale `.env`-bestand of productie-hosting. Spreek af dat de repository de definities bevat en de hostingomgeving de waarden, en houd dat consequent aan.

## Een taakverdeling die standhoudt

**Visuele builder (Lovable):** nieuwe schermen, visuele layout, gebruikersflows, formulieren waarbij zien sneller is dan code lezen, en snelle tekstwijzigingen.

**Code-editor (Cursor):** bedrijfslogica, code die op meer dan één plek wordt hergebruikt, databasekoppelingen, externe API-integraties, unit tests, refactoring en het controleren van door de builder gegenereerde code.

**Geen van beide zonder menselijk oordeel:** autorisatiemodellen (RLS), authenticatie, betalingsafhandeling, foutscenario's en formele garanties aan klanten.

Een praktische vuistregel: zodra een feature promoveert van *"in ontwerpfase"* naar *"in actief gebruik door klanten"*, verplaats je de achterliggende logica direct uit het gegenereerde scherm naar een stabiele backend- of servicemodule. Het scherm blijft visueel en inwisselbaar; de regel wordt stabiel en testbaar. Deze ene gewoonte voorkomt 90% van alle frustraties.

## Regels-bestanden (.cursorrules) zijn die tien minuten dubbel en dwars waard

Een editor die projectregels ondersteunt stelt je in staat om de AI-assistent exact te vertellen wat je project is: architectuurconventies, welke mappen door de builder worden gegenereerd en niet handmatig bewerkt mogen worden, en welke bestanden absoluut taboe zijn zonder expliciet overleg (zoals databasemigraties, authenticatie en betaalmodules).

Schrijf dit eenmalig op. De kwaliteit van de suggesties schiet direct omhoog, en de bescherming tegen een behulpzame AI die per ongeluk een vitale autorisatielaag sloopt is onbetaalbaar.

Doe hetzelfde in de builder voor zover deze instructies op projectniveau ondersteunt: geef aan dat specifieke servicemodules handgeschreven zijn en uitsluitend aangeroepen mogen worden in plaats van opnieuw geïmplementeerd.

## Wanneer beide tools hetzelfde bestand hebben aangeraakt

Het zal vroeg of laat gebeuren. De herstelprocedure is standaard en overzichtelijk:

Raak niet in paniek en ga niet blindelings forceren (`force push`). Bekijk in je Git-historie wat elke kant precies heeft gewijzigd, behoud de versie met de meest kritische bedrijfslogica en voeg de andere wijziging (vaak een cosmetische aanpassing) handmatig opnieuw toe. Met kleine commits kost dit vijf minuten.

Onderzoek vervolgens hoe het conflict kon ontstaan. Vrijwel altijd blijkt er bedrijfslogica te hebben gestaan in een visueel gegenereerd schermbestand. Verplaats die logica direct naar een afzonderlijke module om herhaling definitief te voorkomen.

## Zo samenwerken met een externe ontwikkelaar

Wanneer een externe specialist aanschuift - een freelancer, technisch partner of collega - vraagt de workflow om één duidelijke werkafspraak: spreek af wie waar en wanneer werkt. Wijzigingen in de builder zijn immers direct en globaal zichtbaar; wijzigingen in de code-editor verlopen via Git-branches en code reviews. Zonder heldere afspraken botsen de doordachte refactoring van de ontwikkelaar en de snelle interface-aanpassing van de oprichter geheid op vrijdagmiddag.

Het model dat in de praktijk feilloos functioneert: de oprichter gebruikt de builder voor schermen op een eigen Git-branch die via een pull request wordt samengevoegd; de ontwikkelaar werkt aan architectuur en backend-code; en alles wat autorisatie, betalingen of klantdata raakt wordt altijd aan een vierogenprincipe onderworpen.

## Schermen 'studeren af', en je moet herkennen wanneer

Dit is de cruciale discipline die deze workflow over meerdere jaren gezond houdt:

Elk nieuw scherm in je applicatie begint als een wegwerpproduct. Het is gegenereerd om een idee te testen, wordt deze maand waarschijnlijk drie keer herschreven en verdient geen enkele bescherming. Dat is exact de juiste houding - totdat het scherm een specifiek kantelpunt bereikt.

**Een scherm 'studeert af' zodra klanten ervan afhankelijk worden.** Een bedrijfsproces van een klant loopt erdoorheen. Het berekent een bedrag dat op een factuur verschijnt. De medewerkers van een zakelijke afnemer weten precies waar welke knop zit. Vanaf dat moment zijn de kosten van een onbedoelde hergeneratie niet langer nul.

**Afstuderen betekent de logica verhuizen, niet het scherm bevriezen.** De visuele layout mag je naar hartenlust blijven aanpassen via prompts; wat je verhuist is de onderliggende bedrijfsregel - de berekening, de validatie, de statusovergang - naar een zelfstandige TypeScript-module met een duidelijke naam. De interface blijft razendsnel aanpasbaar, terwijl het bedrijfskritische fundament immuun wordt voor regeneratiefouten.

**Documenteer welke onderdelen welke status hebben.** Een kort overzicht in je repository: deze modules zijn handgeschreven, deze mappen zijn visueel gegenereerd. Dat is de basis voor je `.cursorrules`, het eerste wat een nieuwe engineer leest, en wat voorkomt dat je over zes maanden foute aannames doet over je eigen software.

**Schrijf tests voor afgestudeerde logica.** Een regel waar betalende klanten op vertrouwen verdient een geautomatiseerde test. Dit is het ideale moment om die test te schrijven, omdat je de code zojuist hebt ontkoppeld en exact begrijpt.

## De code-architectuur neerzetten die dit mogelijk maakt

Deze hybride workflow vereist een project waarin visuele interfaces en handgeschreven logica daadwerkelijk van elkaar zijn gescheiden - iets wat bij applicaties die puur met AI zijn gebouwd van nature ontbreekt.

LaunchStudio voert die scheiding uit als een afgebakend fixed-price project: bedrijfslogica wordt uit de gegenereerde schermen gehaald naar zelfstandige modules die de builder nooit overschrijft, dubbele logica wordt samengevoegd, configuraties worden expliciet gemaakt, de Git-repository wordt ingericht als centrale bron van waarheid met consistente formattering, vitale tests worden geschreven en projectregels voor beide tools worden ingesteld - zónder de door jou ontworpen interface aan te tasten.

De software engineers zijn van Manifera: elf jaar productie-ervaring en meer dan 160 gerealiseerde projecten voor opdrachtgevers als Vodafone, TNO en CFLW vanuit Amsterdam Herengracht 420 en Ho Chi Minhstad.

[Deel jouw huidige werkwijze met ons](https://launchstudio.eu/nl/#contact), of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een refactor overschreven door een simpele tekstwijziging

Ivo Schaminée bouwde met Lovable het platform Servicecontract: contractbeheer voor installatiebedrijven, in gebruik bij elf installateurs in de regio Oss en Uden. Onderhoudscontracten, periodieke keuringen, facturatie-intervallen en geautomatiseerde verlengingsherinneringen.

Hij was gestart met Cursor voor de backend-onderdelen die de builder gebrekkig afhandelde, en gedurende twee maanden werkte die combinatie uitstekend. Op een donderdag besteedde hij de hele dag aan het consolideren van de contractverlengingsberekening. Die bleek op drie verschillende plekken in de code te zijn geprogrammeerd, met drie verschillende uitkomsten voor contracten die halverwege de maand waren ingegaan. Het werk was lokaal afgerond, maar nog niet gepusht naar GitHub.

Op vrijdagochtend vroeg een klant om een kleine tekstuele wijziging op het contractoverzichtsscherm. Ivo paste de tekst aan in de online builder. De builder hergenereerde het volledige schermbestand - en precies in dat bestand bevonden zich twee van de drie verlengingsberekeningen. De gegenereerde versie van de builder werd naar de Git-repository gepusht. Ivo's volledige donderdagwerk was overschreven. En omdat de derde implementatie elders intact was gebleven, werden verlengingsdata voor mid-maand contracten nu op een vierde, volstrekt onvoorspelbare manier berekend.

Niemand merkte het op gedurende elf dagen. Tegen die tijd waren er 34 foutieve verlengingsherinneringen verstuurd, waarvan twee naar gewaardeerde klanten die hun contract al lang hadden verlengd.

In zeven werkdagen brachten ervaren engineers structurele orde aan: de verlengingsberekening werd geëxtraheerd naar één centrale servicemodule die de web-builder niet kan aanraken, met duidelijke definities voor gebroken contractmaanden afgestemd met drie installatiebedrijven; er werden unit tests geschreven voor alle randgevallen; de 34 onjuiste herinneringen werden getraceerd en gecorrigeerd met een persoonlijke toelichting van Ivo; de Git-repository werd als centrale waarheid ingericht met automatische bi-directionele synchronisatie, Prettier-formattering en gecommitte lockfiles; er werden strikte `.cursorrules` en projectinstructies geconfigureerd; en Ivo formuleerde een heldere discipline voor zichzelf: pullen vóór de start, pushen na afronding en één tool tegelijk per domein.

**Resultaat:** Geen enkel codeconflict meer in de negen maanden daarna. Volgens Ivo was de echte doorbraak niet de tooling-configuratie, maar de vaste gewoonte om bedrijfslogica direct uit schermen te halen zodra een functionaliteit stabiel is.

> *"Een tekstwijziging van twee woorden op vrijdagochtend wiste een volle dag uiterst secuur werk uit, puur omdat de logica die ik had gerepareerd leefde in een scherm dat de builder naar believen opnieuw mocht overschrijven."*
> - **Ivo Schaminée, Oprichter, Servicecontract (Oss)**

**Kosten & Doorlooptijd:** € 3.300 (logica-extractie naar modules, tests rondom verlengingsregels, dataherstel, Git- en toolingconfiguratie, rules-bestanden, workflow-richtlijnen) - opgeleverd in 7 werkdagen.

## Veelgestelde vragen

### Kan ik een visuele builder en een code-editor veilig op hetzelfde project gebruiken?

Jazeker, mits de Git-repository de absolute bron van waarheid is en beide tools daarmee synchroniseren. Zonder die centrale koppeling ontbreekt een gedeelde definitie van de codebase en groeien beide omgevingen onherroepelijk uit elkaar.

### Hoe voorkom ik dat een visuele builder mijn handgeschreven code overschrijft?

Door handgeschreven bedrijfslogica te isoleren in afzonderlijke servicemodules waar de builder niet bij komt, en het visuele scherm die logica louter te laten aanroepen. Zolang er geen complexe logica in gegenereerde componenten staat, kan een scherm veilig opnieuw worden gegenereerd.

### Hoe voorkom ik conflicten tussen Cursor en Lovable?

Werk aan één functioneel gebied tegelijk, voer altijd een `pull` uit vóórdat je begint en een `push` zodra je stopt, en commit in kleine eenheden. Vrijwel alle merge-conflicten ontstaan door het starten van een sessie op een verouderde versie van de code.

### Welk werk hoort in welke tool thuis?

De visuele builder voor schermen, layouts, gebruikersflows en snelle copy; de code-editor voor bedrijfslogica, gedeelde componenten, databasequery's, integraties, tests en refactoring. Zaken als databeveiliging (RLS) en betalingen vereisen altijd menselijke sturing.

### Zijn rules-bestanden (.cursorrules) de moeite waard?

Absoluut - het kost tien minuten. Ze specificeren projectconventies, markeren welke mappen automatisch gegenereerd worden en blokkeren gevoelige bestanden voor automatische aanpassingen. Dit verhoogt de kwaliteit van AI-suggesties aanzienlijk en voorkomt gevaarlijke bewerkingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een visuele builder en een code-editor veilig op hetzelfde project gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, mits de Git-repository de centrale bron van waarheid is waarmee beide tools synchroniseren. Zonder die koppeling drijven de twee versies uit elkaar."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat een visuele builder mijn handgeschreven code overschrijft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Plaats handgeschreven logica in aparte modules die schermen aanroepen. Houd gegenereerde bestanden vrij van vitale maatwerklogica."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik conflicten tussen Cursor en Lovable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Werk op één plek tegelijk per gebied, voer altijd een pull uit vóór de start en een push na afronding, en commit in kleine stappen."
      }
    },
    {
      "@type": "Question",
      "name": "Welk werk hoort in welke tool thuis?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De builder voor schermen en flows; de editor voor logica, datakoppelingen, tests en refactoring; een mens voor security en betalingen."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn rules-bestanden (.cursorrules) de moeite waard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, ze bepalen projectconventies en blokkeren gevoelige bestanden voor AI-aanpassingen, wat suggesties verbetert en risico's minimaliseert."
      }
    }
  ]
}
</script>
