---
Titel: "De European Accessibility Act en Uw Door AI Gebouwde App"
Trefwoorden: European Accessibility Act, WCAG, toegankelijkheid, toetsenbordnavigatie, schermlezers, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# De European Accessibility Act en Uw Door AI Gebouwde App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De European Accessibility Act en Uw Door AI Gebouwde App",
  "description": "Gegenereerde interfaces zien er goed uit en falen voor iedereen die geen muis gebruikt. Voor wie de toegankelijkheidsregels gelden, de controles die in een uur de meeste problemen vinden, en de oplossingen die echt goedkoop zijn.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/the-european-accessibility-act-and-your-ai-built-app" }
}
</script>

AI-codetools maken interfaces die er correct uitzien. Een div die is opgemaakt als knop, gedraagt zich als een knop wanneer er met een muis op wordt geklikt, en op een schermafbeelding is hij niet van de echte te onderscheiden.

Het is geen knop. Hij is niet met het toetsenbord bereikbaar, wordt niet voorgelezen door een schermlezer, en op enter drukken doet niets. Voor een bezoeker met een muis werkt het product. Voor een bezoeker zonder muis bestaat een flink deel ervan niet.

Dit is de typische toegankelijkheidsfout van gegenereerde code, en de reden dat ze blijft bestaan, is dat niets eraan zichtbaar is voor degene die het bouwde.

## Voor Wie Dit Geldt

De European Accessibility Act brengt toegankelijkheidseisen naar een reeks producten en diensten die aan consumenten in de EU worden verkocht - waaronder e-commerce, bankdiensten, vervoer en telecommunicatie - met de verplichting vanaf medio 2025. Nederland implementeert dit via nationale wetgeving, en overheidsinstanties vallen al veel langer onder hun eigen eisen.

De praktische positie voor een klein product: verkoopt u aan consumenten, aan overheidsinstanties, of aan grote bedrijven met eigen inkoopnormen, dan is dit een wettelijke of een commerciële eis. Micro-ondernemingen hebben enkele vrijstellingen voor diensten, maar de vrijstelling is smaller dan oprichters hopen en geldt niet voor de eigen verplichtingen van een klant.

En de commerciële route komt eerst. Een gemeente, een zorgorganisatie of een grote werkgever vraagt om een toegankelijkheidsverklaring lang voordat een toezichthouder dat doet.

## De Norm, in de Praktijk

De referentie is WCAG, en het gebruikelijke doel is niveau AA. In plaats van de specificatie te lezen, vertellen de vier principes waaromheen ze is opgebouwd u wat u moet controleren.

**Waarneembaar.** Content is beschikbaar voor verschillende zintuigen: tekstalternatieven voor afbeeldingen, ondertiteling voor video, voldoende kleurcontrast, informatie die niet alleen via kleur wordt overgebracht.

**Bedienbaar.** Alles werkt met het toetsenbord, niets houdt de focus vast, mensen hebben genoeg tijd, niets knippert gevaarlijk.

**Begrijpelijk.** Voorspelbaar gedrag, duidelijke labels, fouten uitgelegd in tekst in plaats van met een rode rand.

**Robuust.** Werkt met hulptechnologie, wat vooral betekent: juiste HTML-elementen gebruiken in plaats van opgemaakte divs.

## Het Uur Dat de Meeste Problemen Vindt

Vier controles, geen tools behalve een browser, en ze leggen het grootste deel van de problemen in een door AI gebouwd product bloot.

**Koppel de muis los.** Navigeer door uw hele product met tab, shift-tab, enter en spatie. Kunt u elk bedieningselement bereiken? Kunt u zien welk element de focus heeft? Kunt u een dialoogvenster openen, gebruiken en sluiten? Kunt u uw belangrijkste proces afronden? In de meeste gegenereerde applicaties faalt dit binnen twee minuten, meestal bij een eigen dropdown of een modal.

**Zoom in tot 200 procent.** Overleeft de lay-out het, of verdwijnt content achter andere content? Veel klanten browsen permanent met vergrote tekst.

**Draai een geautomatiseerde checker.** Een browserextensie vindt in seconden contrastfouten, ontbrekende labels en ontbrekende alternatieve tekst. Ze vangt misschien een derde van de problemen, en dat is een derde voor bijna geen moeite.

**Zet de schermlezer aan die uw besturingssysteem al heeft** en probeer uw belangrijkste proces met het scherm uit. Dit is ongemakkelijk, en het is de controle die u het meest leert.

## De Oplossingen Die Goedkoop Zijn

De meeste bevindingen in een gegenereerde interface komen uit een korte lijst, en elke oplossing is klein.

**Gebruik echte elementen.** Een knop is een `button`, een link is een `a` met een href, een selectievakje is een `input`. Elk native element brengt toetsenbordgedrag, focusafhandeling en betekenis voor schermlezers mee, zonder code.

**Label elk invoerveld.** Een zichtbaar label dat aan zijn veld is gekoppeld. Placeholdertekst is geen label - ze verdwijnt zodra er wordt getypt en wordt vaak niet voorgelezen.

**Herstel het contrast.** Grijze tekst op wit op 4,5:1 voor lopende tekst. Gegenereerde ontwerpen kiezen stelselmatig lichte grijstinten die er elegant uitzien en falen.

**Maak focus zichtbaar.** Gegenereerde stylesheets halen focusranden vaak weg omdat die als lelijk worden beschouwd. Vervang ze door iets duidelijk zichtbaars in plaats van ze te verwijderen.

**Beschrijf afbeeldingen betekenisvol**, en markeer decoratieve als decoratief, zodat ze worden overgeslagen in plaats van voorgelezen.

**Meld fouten in tekst**, gekoppeld aan het veld, in plaats van ze met kleur aan te geven.

**Structureer koppen goed**, op volgorde, omdat gebruikers van schermlezers via koppen navigeren.

## Waar AI-Tools de Meeste Schade Aanrichten

Drie patronen om specifiek in uw codebase naar te zoeken.

Eigen componenten gebouwd uit divs - dropdowns, tabbladen, accordeons, modals - die er goed uitzien en niets implementeren van het toetsenbordgedrag dat hun native of goed gebouwde tegenhangers bieden. Een toegankelijke componentenbibliotheek gebruiken is bijna altijd beter dan deze opnieuw bouwen.

Verwijderde focusstijlen, meestal één regel in een stylesheet die ze overal uitschakelt.

En verkeerd toegepaste ARIA-attributen. Gegenereerde code strooit rollen en labels rond op een manier die soms helpt en vaak het erger maakt, omdat een onjuiste rol hulptechnologie actief verkeerd informeert. Juiste HTML zonder ARIA is beter dan opgemaakte divs met veel ARIA.

## Schrijf de Verklaring

Een toegankelijkheidsverklaring - welke norm u nastreeft, wat nog niet voldoet, hoe iemand een probleem kan melden, en wanneer ze voor het laatst werd beoordeeld - is voor sommige organisaties verplicht en voor iedereen nuttig.

Eerlijk zijn erin is beter dan volledige conformiteit claimen. Een verklaring die zegt dat u AA haalt met drie bekende uitzonderingen, elk met een omweg en een datum, leest als een bedrijf dat echt heeft gekeken. Een algemene claim leest als een bedrijf dat dat niet heeft gedaan, en is makkelijk te weerleggen.

## Toegankelijkheid Gaat Niet Alleen over Blijvende Beperkingen

Het kader dat dit werk de moeite waard laat voelen in plaats van opgelegd: de mensen die door deze wijzigingen worden geholpen, zijn een veel grotere groep dan oprichters voor ogen hebben.

Iemand die uw product in de trein met één hand gebruikt. Iemand van wie het telefoonscherm over het onderste derde is gebarsten. Een gebruiker van in de zestig met gewone leeftijdsgebonden veranderingen in het zicht, wat in meerdere sectoren een flink deel van de Nederlandse beroepsbevolking beschrijft. Een magazijnmedewerker met handschoenen. Iemand met een tijdelijk gebroken pols. Iemand in een felle ruimte waar lichtgrijs op wit gewoon onzichtbaar is.

Geen van deze mensen ziet zichzelf als iemand met een beperking, en allemaal worden ze geraakt door dezelfde gebreken. Contrast dat faalt op 2,8:1 faalt voor iedereen boven een bepaalde leeftijd. Een bedieningselement dat alleen met precieze muisbewegingen bereikbaar is, faalt voor iedereen die in een rijdende trein een trackpad gebruikt. Een formulier dat fouten alleen met kleur aangeeft, faalt voor de ene man op de twaalf met een vorm van kleurenblindheid.

Daarom is het conversie-effect in het voorbeeld hieronder gewoon in plaats van verrassend. Toegankelijkheidswerk neemt wrijving weg die een flinke minderheid van gebruikers raakte die stilletjes dingen niet afmaakten en u niet vertelden waarom.

Het praktische gevolg: behandel deze punten als gebruiksgebreken met een juridische dimensie in plaats van als compliance met een bijeffect op gebruiksgemak. Dat levert betere beslissingen op over wat u als eerste oplost.

## Voorkomen Dat Het Terugvalt

De ongemakkelijke eigenschap van toegankelijkheid in een door AI gebouwd product is dat ze terugvalt telkens als er een functie bijkomt, omdat de tool die de functie toevoegt dezelfde gewoontes heeft als degene die het origineel bouwde.

Drie maatregelen houden de lijn vast zonder van elke wijziging een audit te maken.

**Een toegankelijke componentenbibliotheek als standaard.** Komen uw knoppen, dropdowns, dialoogvensters en tabbladen uit een bibliotheek die toetsenbord- en schermlezergedrag afhandelt, dan is een nieuw scherm dat ermee wordt samengesteld per definitie toegankelijk. Dit is verreweg de beslissing met de meeste hefboom, en het betekent ook dat een agentsessie die wordt gevraagd een dialoogvenster toe te voegen naar het juiste grijpt, omdat de codebase dat bevat.

**Een geautomatiseerde controle in de build.** Toegankelijkheidslinting op uw componenten en een geautomatiseerde scan van de belangrijkste pagina's, die faalt bij teruggang. Ze vangt de contrastwijziging en het ontbrekende label, de meest voorkomende herintroducties.

**Een toetsenbordronde in uw releaseroutine.** Eén regel op de checklist: tab door wat u veranderde. Dertig seconden, en het vangt wat automatisering niet kan.

Schrijf de afspraken ook in het instructiebestand van uw project - native elementen boven divs, labels op elk invoerveld, focus nooit verwijderd. Codeerassistenten lezen het, en het verschil in wat ze genereren is direct en meetbaar.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans twee tot vier dagen: een ronde alleen met het toetsenbord over elk proces met de bevindingen op een lijst, een geautomatiseerde scan van de belangrijkste pagina's, een schermlezerronde over de belangrijkste route, eigen componenten op basis van divs vervangen door native elementen of een toegankelijke bibliotheek, alle invoervelden gelabeld, contrast gecorrigeerd naar AA, zichtbare focus hersteld, afbeeldingen voorzien van betekenisvolle alternatieven, fouten in tekst gemeld en aan velden gekoppeld, de kopstructuur gecorrigeerd, zoomen tot 200 procent gecontroleerd, onjuiste ARIA verwijderd, en een toegankelijkheidsverklaring gepubliceerd met bekende uitzonderingen.

LaunchStudio doet dit als onderdeel van productieklaar maken voor producten die aan consumenten en overheidsinstanties verkopen. Daarachter staat Manifera - elf jaar, klanten als Vodafone, TNO en CFLW, met ervaring in levering aan de publieke sector vanuit Amsterdam.

[Vraag ons uw product zonder muis te gebruiken](https://launchstudio.eu/nl/#contact). Het kost tien minuten en de uitkomst is meestal beslissend.

## Echt voorbeeld

### Een Aanbesteding Verloren op het Eerste Criterium

Olaf Rietberg bouwde Buurtmelding in Lovable: een meldtool waarmee gemeenten inwoners problemen in de openbare ruimte laten melden, verkocht aan zes kleinere gemeenten.

De aanbesteding van een grotere gemeente vereiste conformiteit met de toegankelijkheidseisen voor de overheid en een toegankelijkheidsverklaring. Olafs product viel in de eerste beoordelingsronde af, nog voor enige demonstratie.

De beoordeling noemde twaalf tekortkomingen. Het meldformulier kon niet met het toetsenbord worden ingevuld, omdat de categoriekiezer een dropdown op basis van divs was die alleen op klikken reageerde. Focusranden waren overal uitgeschakeld door één regel in de stylesheet. Formuliervelden gebruikten placeholdertekst in plaats van labels. Lopende tekst was #999999 op wit, een contrastverhouding van 2,8:1. De locatiekiezer op basis van een kaart had helemaal geen alternatieve invoermethode. Foutmeldingen werden getoond door de rand van velden rood te maken, zonder tekst. En de kopstructuur sprong van h1 naar h4, waardoor de pagina met een schermlezer niet te navigeren was.

Zes werkdagen: de categoriekiezer en drie andere eigen componenten vervangen door een toegankelijke componentenbibliotheek; de regel die focus overal verwijderde geschrapt en een zichtbare focusstijl toegevoegd; elk veld voorzien van een goed zichtbaar label; het kleurenpalet aangepast zodat lopende tekst 4,6:1 haalt en interactieve elementen 3:1, met de merkkleur iets donkerder; een alternatief met postcode en straatadres toegevoegd naast de kaartkiezer, wat voor de meeste inwoners toch al sneller bleek; fouten in tekst gemeld, gekoppeld aan hun veld en samengevat bovenaan het formulier; de kopstructuur overal gecorrigeerd; afbeeldingen voorzien van alternatieven met decoratieve als zodanig gemarkeerd; het hele product gecontroleerd met het toetsenbord, op 200 procent zoom en met een schermlezer; en een toegankelijkheidsverklaring gepubliceerd met twee resterende uitzonderingen, met omwegen en streefdatums.

**Resultaat:** het product slaagde in de volgende aanbestedingsronde voor de beoordeling en werd gekozen. Wat Olaf meer verraste: meldingen via het adresalternatief in plaats van de kaart zijn nu goed voor 38 procent van alle meldingen, van inwoners die het kennelijk makkelijker vonden - een conversieverbetering die hij niet van toegankelijkheidswerk had verwacht.

> *"Ik verloor een aanbesteding voordat iemand het product zag, op criteria waarvan ik niet wist dat ze bestonden. En de oplossing die het meest uitmaakte, bleek een functie te zijn die een derde van mijn gebruikers verkiest."*
> - **Olaf Rietberg, Oprichter, Buurtmelding (Assen)**

**Kosten & Doorlooptijd:** €4.800 (vervangen door toegankelijke componenten, herstel van focus en labels, contrastcorrectie, alternatieve locatie-invoer, foutafhandeling, kopstructuur, alternatieven voor afbeeldingen, controle met toetsenbord, zoom en schermlezer, toegankelijkheidsverklaring) - afgerond in 6 werkdagen.

## Veelgestelde vragen

### Geldt toegankelijkheidswetgeving voor mijn kleine product?

Verkoopt u aan consumenten, overheidsinstanties of grote organisaties met inkoopnormen, dan is het een wettelijke of commerciële eis. De vrijstelling voor micro-ondernemingen is smaller dan oprichters verwachten.

### Wat is de snelste manier om problemen te vinden?

Koppel de muis los en navigeer met het toetsenbord door uw product. De meeste door AI gebouwde applicaties falen binnen twee minuten, meestal bij een eigen dropdown of een modal.

### Waarom falen gegenereerde interfaces op toegankelijkheid?

Ze gebruiken opgemaakte divs in plaats van native elementen. Een div die eruitziet als een knop heeft geen toetsenbordgedrag en geen betekenis voor hulptechnologie, en daar is op een schermafbeelding niets van te zien.

### Is een geautomatiseerde checker genoeg?

Nee. Ze vindt ruwweg een derde van de problemen - contrast, ontbrekende labels, ontbrekende alternatieven - voor heel weinig moeite. Testen met toetsenbord en schermlezer vindt de rest.

### Moet mijn toegankelijkheidsverklaring volledige conformiteit claimen?

Alleen als dat waar is. Een verklaring met bekende uitzonderingen, omwegen en datums leest als geloofwaardig; een algemene claim is makkelijk te weerleggen en erger dan een eerlijke.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Geldt toegankelijkheidswetgeving voor een klein product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Verkoopt u aan consumenten, overheidsinstanties of grote organisaties, dan is het een wettelijke of commerciële eis. De vrijstelling voor micro-ondernemingen is smal."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de snelste toegankelijkheidscontrole?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Navigeer door het hele product met alleen een toetsenbord. De meeste door AI gebouwde applicaties falen binnen twee minuten bij een eigen dropdown of modal."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom falen door AI gegenereerde interfaces op toegankelijkheid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze gebruiken opgemaakte divs in plaats van native elementen, die er hetzelfde uitzien maar geen toetsenbordgedrag of betekenis voor hulptechnologie hebben."
      }
    },
    {
      "@type": "Question",
      "name": "Is een geautomatiseerde toegankelijkheidschecker voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - die vangt ongeveer een derde van de problemen. Testen met toetsenbord en schermlezer vindt de rest."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een toegankelijkheidsverklaring volledige conformiteit claimen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als het waar is. Bekende uitzonderingen noemen met omwegen en datums is geloofwaardiger en moeilijker te weerleggen."
      }
    }
  ]
}
</script>
