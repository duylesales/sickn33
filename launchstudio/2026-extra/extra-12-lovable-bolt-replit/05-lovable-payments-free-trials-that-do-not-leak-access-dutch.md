---
Titel: "Lovable Betalingen: Gratis Proefperiodes Die Geen Toegang Lekken"
Trefwoorden: lovable betalingen, gratis proefperiode, misbruik proefperiode, toegangscontroles, conversie proefperiode, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS Scale-Up
---

# Lovable Betalingen: Gratis Proefperiodes Die Geen Toegang Lekken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Betalingen: Gratis Proefperiodes Die Geen Toegang Lekken",
  "description": "Proefperiodes in door AI gebouwde apps verlopen meestal alleen in de interface en nergens anders. Hoe u een toegangscontrole bouwt die echt standhoudt, kiest tussen met of zonder kaart, en een proefperiode beëindigt zonder de klant te verliezen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-payments-free-trials-that-do-not-leak-access" }
}
</script>

Hier is een test die u vanmiddag op uw eigen product kunt doen. Start een proefperiode, laat die verlopen, log dan in en open de ontwikkelhulpmiddelen van de browser terwijl u de app gebruikt.

In een groot deel van de door AI gebouwde SaaS-applicaties zult u ontdekken dat de verlopen proefperiode veranderde wat de interface toont, en verder niets. De upgradebanner verschijnt, de knoppen zien er uitgeschakeld uit - en de onderliggende verzoeken werken nog steeds. Een gebruiker die op een verborgen element klikt, een endpoint direct aanroept, of simpelweg naar een URL gaat waar het menu niet meer naar linkt, heeft het volledige product.

De interface is geen rechtensysteem. Dat is ze nooit geweest. Maar een tool die gevraagd wordt een proefperiode te bouwen, levert een proefperiode die er correct uitziet, en er correct uitzien is de hele specificatie die ze meekreeg.

## Eén Functie Beslist Alles

De oplossing is architectonisch en klein: één functie op de server die beantwoordt of dit account dit ding nu mag doen, aangeroepen door elk endpoint dat iets betekenisvols doet.

Ze leest de status uit uw eigen database - plan, status, einddatum van de proefperiode, rechten - en geeft een antwoord. De interface gebruikt vervolgens dezelfde functie om te bepalen wat er wordt getoond, wat betekent dat wat de gebruiker ziet en wat de server toestaat nooit uit elkaar kunnen lopen, omdat het dezelfde beslissing is, twee keer weergegeven.

Het alternatief, controles verspreid door de code naarmate elke functie wordt gebouwd, garandeert dat een endpoint dat op een vrijdag is geschreven er geen heeft. Dat endpoint is uw lek in de proefperiode, en u vindt het niet door naar de applicatie te kijken zoals een klant dat doet.

## Met of Zonder Kaart

Dit is een zakelijke beslissing met een technisch gevolg, en beide opties zijn te verdedigen.

**Geen kaart nodig** maximaliseert het aantal gestarte proefperiodes. U krijgt veel meer mensen in het product, uw conversieratio aan het eind is lager, en uw totale aantal betalende klanten vaak hoger. Het past bij producten waarvan de waarde snel duidelijk is en waarvan het publiek prijsgevoelig of niet-technisch is.

**Kaart vereist** levert minder, beter gekwalificeerde proefperiodes op, en converteert die veel beter omdat de betaling al geregeld is. Het past bij duurdere B2B-producten waarbij elke proefperiode u supporttijd kost.

Het technische verschil zit in wie aan het eind moet handelen. Met een kaart wordt de proefperiode omgezet tenzij de klant die stopt - dus uw verplichting is het hem vooraf duidelijk te vertellen. Zonder kaart eindigt de proefperiode tenzij de klant handelt - dus uw verplichting is die handeling op precies het juiste moment makkelijk te maken.

Neemt u de kaart, stuur dan de herinnering. In meerdere Europese markten is een vorm van vooraankondiging voordat een proefperiode wordt omgezet verplicht of bijna verplicht, en los van de wet is een afschrijving die onaangekondigd binnenkomt na een vergeten aanmelding de meest betrouwbare manier om een chargeback en een publieke klacht te veroorzaken.

## De Tweede Proefperiode Voorkomen

Iemand meldt zich opnieuw aan met een e-mailadres met een plusteken. Of dat ertoe doet, hangt af van uw product.

Voor een consumententool van €9 per maand meestal niet, en de moeite om het te voorkomen is groter dan het verlies. Voor een product met echte kosten per account - alles wat een AI-model aanroept, fysieke post verstuurt of opslag verbruikt - zijn herhaalde proefperiodes een echte kostenpost.

Proportionele maatregelen, ongeveer gerangschikt naar hoeveel ze eerlijke klanten irriteren: normaliseer e-mailadressen zodat plustekens en punt-varianten samenvallen tot één identiteit; vraag om een kaart; verifieer een telefoonnummer; beperk per organisatiedomein bij B2B-producten. Wegwerp-e-maildomeinen blokkeren is een veelgehoorde suggestie en meestal tijdverspilling, omdat de lijsten altijd achterlopen.

Wat u ook kiest, log het. Weten dat elf accounts dezelfde betaalvingerafdruk delen is nuttig; ze automatisch blokkeren op basis van een vuistregel die u niet kunt uitleggen, is hoe u een echte klant met een ongebruikelijke opzet verliest.

## Een Proefperiode Beëindigen Zonder de Relatie te Beëindigen

Het verlopen van een proefperiode is het moment dat de meeste producten het slechtst afhandelen, en het is een moment van maximale hefboom: de persoon zit in uw product, heeft er werk in gedaan, en beslist.

Drie dingen laten het goed gaan.

**Verwijder hun werk niet.** Een verlopen proefperiode moet de data bewaren, zichtbaar en alleen-lezen, met een duidelijke route om het te ontgrendelen. Verwijderen bij het verlopen vernietigt zowel de conversie als de kans dat ze over drie maanden terugkomen.

**Laat ze het toch exporteren.** Tegenintuïtief en juist: een product dat data gijzelt, is een product waar mensen elkaar voor waarschuwen. De export kost u bijna niets en levert goodwill op waar u blij mee zult zijn.

**Vraag waarom, één keer, eenvoudig.** Eén vraag in de e-mail bij het verlopen - wat hoopte u dat het zou doen? - beantwoord door een klein deel van de mensen, is de meest waardevolle productfeedback die een klein bedrijf krijgt, omdat ze komt van mensen die het probeerden en ertegen besloten.

En handel het verzoek om verlenging netjes af. Iemand die om nog een week vraagt, vertelt u dat hij nog steeds geïnteresseerd is; een beheeractie die dat in tien seconden toekent, is het bouwen waard de eerste keer dat erom wordt gevraagd.

## Meet de Proefperiode, Niet Alleen de Conversie

De meeste oprichters kennen hun percentage van proefperiode naar betaald en verder niets, wat hen vertelt óf er iets mis is, maar nooit wát.

Drie metingen veranderen dat, en alle drie zijn haalbaar voor een klein product. **Tijd tot de eerste betekenisvolle handeling** - het punt waarop iemand het product daadwerkelijk heeft gebruikt voor het doel ervan, niet alleen heeft aangemeld. Definieer het specifiek voor uw tool: de eerste patiënt ingecheckt, de eerste factuur verstuurd, het eerste rooster gepubliceerd. Ligt die mediaan op vier dagen in een proefperiode van veertien dagen, dan slokt uw onboarding de proefperiode op.

**Het aandeel dat er nooit komt.** Dit zijn de mensen die uw e-mail bij het verlopen niet kan redden, omdat ze het product nooit hebben zien werken. Bij de meeste moeizame proefperiodes is dit getal het hele probleem, en het wordt opgelost bij de aanmelding in plaats van bij het verlopen.

**Activiteit in het laatste derde.** Mensen die het product in de laatste paar dagen nog gebruiken, converteren veel beter dan degenen die in week één afhaakten. Het vertelt u of uw herinneringsmails over de deadline moeten gaan - nuttig voor betrokken proefgebruikers - of over beginnen, wat de afgehaakte groep nodig heeft.

Dit meten vergt een tijdstempelkolom en drie queries, geen analyseplatform. En de reden dat het in hetzelfde werk thuishoort als de toegangsoplossing is praktisch: zodra u weet wie betrokken is en wie niet, wordt de reeks bij het verlopen niet langer één e-mail aan iedereen maar twee korte aan twee groepen met werkelijk verschillende problemen - wat doorgaans meer conversie oplevert dan iets anders wat u in een week kunt veranderen.

## De Stille Kosten van een Royale Proefperiode

Een proefperiode is niet gratis om te draaien, en de producten die daar laat achter komen, zijn de producten waarbij elk account iets reëels verbruikt: modelaanroepen, opslag, e-mailvolume, een plek bij een dienst waarvoor u per gebruiker betaalt.

Bereken het getal voordat u de lengte bepaalt. Kost een proefgebruiker u €0,40, dan is een proefperiode van 30 dagen zonder kaart bij een paar honderd aanmeldingen per maand een afrondingsverschil. Kost hij €9 omdat uw product documenten samenvat met een taalmodel, dan is dezelfde proefperiode een substantiële regel op uw eigen rekening en verdient ze een kaartvereiste, een gebruikslimiet tijdens de proefperiode, of beide.

Limieten zijn meestal een beter antwoord dan de proefperiode inkorten, omdat ze behouden waar het om gaat - tijd om te evalueren - terwijl ze de kosten begrenzen. Twintig documenten, vijf rapporten, één export: genoeg om te zien of het product werkt, niet genoeg om een bedrijf op te draaien. Noem de limiet duidelijk in de interface in plaats van haar stil af te dwingen, en maak het bereiken ervan een upgradeprompt in plaats van een foutmelding, want een proefgebruiker die uw limiet bereikte, is de best gekwalificeerde lead die u die week hebt.

## Dit Inrichten

Voor een bestaand product kost dit meestal twee tot drie dagen: één toegangsfunctie op de server, aangeroepen door elk endpoint, de status van de proefperiode in uw eigen database met een expliciete einddatum, de interface aangestuurd door dezelfde functie zodat weergave en rechten niet uit elkaar kunnen lopen, een controle van bestaande endpoints op de exemplaren zonder enige controle, met of zonder kaart geïmplementeerd met de bijbehorende herinnerings- of verloopreeks, proportionele afhandeling van dubbele proefperiodes, alleen-lezen bewaren met export na het verlopen, en een beheeractie voor verlenging.

LaunchStudio doet dit als onderdeel van productieklaar maken, en het is een van de meest voorkomende bevindingen bij elke review van een door AI gebouwde SaaS. Achter het werk staat Manifera: 120+ engineers en elf jaar productiesystemen voor klanten als Vodafone, TNO en CFLW.

[Vraag ons uw verlopen proefperiode te testen](https://launchstudio.eu/nl/#contact) - wij doen het met de ontwikkelhulpmiddelen open, zoals uw gebruikers het ook doen.

## Echt voorbeeld

### Veertig Accounts op een Verlopen Proefperiode

Lotte van Bemmel bouwde Wachtkamer in Lovable: software voor het inchecken van patiënten en een wachtkamerscherm voor huisartsenpraktijken, €59 per maand na een proefperiode van 21 dagen zonder kaart.

Haar logica voor de proefperiode zat in de frontend. Wanneer de einddatum verstreek, toonde de app een upgradescherm en schakelde de navigatie uit. Het veranderde niets aan wat de server deed voor een geauthenticeerd verzoek.

Ze ontdekte het via haar eigen hostingrekening. Het gebruik groeide sneller dan de omzet, en toen ze actieve accounts naast betalende legde, was het verschil 40 praktijken - waarvan sommige al vijf maanden dagelijks patiënten incheckten op een verlopen proefperiode. Verschillende hadden aangenomen dat het product gratis was. Twee hadden dat aan collega's verteld.

Drie werkdagen: één toegangsfunctie op de server die plan en status van de proefperiode uit de database leest, aangeroepen door elk endpoint, inclusief de API voor het wachtkamerscherm die nooit iets had gecontroleerd; de frontend omgebouwd om dezelfde functie te vragen wat er getoond moet worden; een controle van alle 34 endpoints, waarvan er 19 helemaal geen autorisatiecontrole hadden; normalisatie van e-mailadressen om dubbele proefperiodes met plustekens samen te voegen; een herinneringsreeks op dag 14, dag 20 en bij het verlopen; alleen-lezen toegang met data-export, 60 dagen bewaard na het verlopen; en een beheeractie om een proefperiode met een vast aantal dagen te verlengen.

**Resultaat:** van de 40 praktijken die het product zonder te betalen gebruikten, stapten er 12 binnen een maand nadat de toegang echt stopte over op een betaald plan, vroegen er 6 om een korte verlenging en kregen die, waarvan de helft ook converteerde, en de infrastructuurkosten daalden met een derde. De conversie van proefperiode naar betaald bij nieuwe aanmeldingen steeg van 18 naar 29 procent, wat Lotte vooral toeschrijft aan de herinnering op dag 14 en minder aan de handhaving.

> *"Veertig praktijken gebruikten het dagelijks en ik had geen idee, omdat de proefperiode op mijn scherm was afgelopen. De interface loog net zo goed tegen mij als tegen hen."*
> - **Lotte van Bemmel, Oprichter, Wachtkamer (Alkmaar)**

**Kosten & Doorlooptijd:** €2.400 (toegangsfunctie op de server, controle en herstel van endpointautorisatie, statusmodel voor de proefperiode, herinneringsreeks, export en bewaren, beheeractie voor verlenging) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Hoe weet ik of mijn proefperiode echt verloopt?

Laat er een verlopen en roep daarna uw API-endpoints direct aan met de sessie van het verlopen account. Geven ze data terug, dan verloopt uw proefperiode alleen in de interface - de meest voorkomende bevinding bij reviews van door AI gebouwde SaaS-producten.

### Moet ik een kaart vragen om een proefperiode te starten?

Dat hangt af van prijs en publiek. Zonder kaart krijgt u meer proefperiodes en een lagere conversie; met kaart minder en een veel hogere conversie. Duurdere B2B-producten vragen meestal de kaart; goedkope of niet-technische producten meestal beter niet.

### Moet ik klanten waarschuwen voordat een proefperiode overgaat in een betaald plan?

Stuur de herinnering hoe dan ook, ongeacht wat er waar u actief bent strikt verplicht is. Een onaangekondigde afschrijving na een vergeten aanmelding is de meest betrouwbare bron van chargebacks en klachten die een klein product heeft.

### Hoe lang moet een proefperiode zijn?

Lang genoeg om het moment te bereiken waarop uw product nuttig wordt, wat voor de meeste tools 14 dagen is en voor alles met inrichtingswerk dichter bij 30. Meet wanneer proefgebruikers voor het eerst het ding doen dat ertoe doet en bepaal de lengte daarop, niet op gewoonte.

### Wat moet er met data gebeuren als een proefperiode eindigt?

Bewaar ze, alleen-lezen, met een export beschikbaar, voor een genoemde periode. Ze verwijderen vernietigt zowel de conversie als de kans dat ze later terugkomen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe weet ik of mijn proefperiode echt verloopt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laat een proefperiode verlopen en roep uw API-endpoints direct aan met die sessie. Komt er data terug, dan verloopt de proefperiode alleen in de interface."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik een kaart vragen om een proefperiode te starten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zonder kaart geeft meer proefperiodes en een lagere conversie; met kaart minder en een veel hogere conversie. Duurdere B2B-producten vragen meestal de kaart."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik klanten waarschuwen voordat een proefperiode wordt omgezet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stuur de herinnering hoe dan ook. Een onaangekondigde afschrijving na een vergeten aanmelding is de meest betrouwbare bron van chargebacks voor een klein product."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moet een gratis proefperiode zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lang genoeg om het moment te bereiken waarop het product nuttig wordt - doorgaans 14 dagen, of rond de 30 als er inrichtingswerk bij komt kijken. Meet het in plaats van gewoonte te kopiëren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er met data gebeuren als een proefperiode eindigt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bewaar ze alleen-lezen met een export beschikbaar voor een genoemde periode. Ze verwijderen vernietigt zowel de conversie als elke kans dat ze terugkomen."
      }
    }
  ]
}
</script>
