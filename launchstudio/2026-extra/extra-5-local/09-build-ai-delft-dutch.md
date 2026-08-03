---
Titel: "Hoe Delftse oprichters AI-producten bouwen zonder een engineeringteam"
Trefwoorden: build ai, build an ai app, technische oprichter, ci/cd uitrol, Delft
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---

# Hoe Delftse oprichters AI-producten bouwen zonder een engineeringteam

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Delftse oprichters AI-producten bouwen zonder een engineeringteam",
  "description": "Hoe solo technische oprichters in Delft AI-producten bouwen zonder een engineeringteam in te huren, en waar die aanpak vastloopt zodra er echte gebruikers komen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/build-ai-delft" }
}
</script>

Daan Smit studeerde af aan de TU Delft met een graad in werktuigbouwkunde, leerde zichzelf goed genoeg coderen om functioneel te zijn, en gebruikte Cursor om in zes weken tijd avonden na zijn werk een heel IoT-dashboard te bouwen voor het volgen van sensorvloten. Hij nam niemand aan. Dat is het verhaal van een groeiend aantal oprichters dat solo AI-producten probeert te bouwen in Delft — en het is een verhaal dat werkt, tot het punt waarop de uitrolpijplijn (deployment pipeline) zelf de knelkoppeling wordt.

## Waarom "AI bouwen zonder team" tot op zekere hoogte daadwerkelijk werkt

De oprichtersbasis van Delft ziet er anders uit dan die van de meeste Nederlandse steden vanwege het zwaartepunt: de TU Delft, een van de toonaangevende technische universiteiten van Europa, brengt een gestage stroom technisch ingestelde oprichters voort die comfortabel genoeg zijn met code om zelf AI-producten te bouwen met tools zoals Cursor, zonder dat ze een ontwikkelingsteam hoeven in te huren. Dat is een echt voordeel — deze oprichters kunnen lezen wat de AI genereert, overduidelijke problemen oplossen en snel itereren zonder een communicatielaag tussen "wat ik wil" en "wat er is gebouwd."

Dit is zichtbaar in de wijken rond de campus van de TU Delft, waar een aanzienlijk deel van de technische oprichters in de stad hun start kreeg — roboticalabs, lucht- en ruimtevaartprojecten en een constante stroom afgestudeerden die in de regio blijven in plaats van direct naar Amsterdam of het buitenland te verhuizen. Veel van deze oprichters zijn zo vertrouwd met het lezen van een stack trace of het debuggen van een mislukte API-call dat ze nooit de drang voelen naar een no-code tool; Cursor is voor hen minder een vervanging voor engineeringvaardigheden en meer een hefboom voor vaardigheden die ze al bezitten.

De beperking is geen gebrek aan technische vaardigheid. Het is dat een sterke individuele bijdrager zijn en het beheren van productie-infrastructuur twee verschillende disciplines zijn, en de meeste solo technische oprichters in Delft de tweede niet eerder volledig hebben hoeven bezitten — omdat die infrastructuur bij een vorige baan of in de academische wereld meestal de verantwoordelijkheid van iemand anders was. Een oprichter die drie jaar als sterke backend-engineer bij een scale-up heeft gewerkt, schreef uitstekende code binnen een systeem waarin een platformteam al eigenaar was van CI/CD, beheer van geheimen en rollback-tools. Solo gaan betekent al dat eigenaarschap in één keer erven, bovenop alles waar een beginnende oprichter al mee jongleert.

## Waar de solo-bouwaanpak vastloopt

Het patroon dat LaunchStudio herhaaldelijk ziet bij technisch bekwame Delftse oprichters:

- Geen CI/CD-pijplijn, wat betekent dat elke uitrol een handmatig proces is vanaf een laptop, zonder geautomatiseerde testcontrole voordat code productie bereikt
- Omgevingsvariabelen en databasereferenties die tijdens de vroege ontwikkeling rechtstreeks in de codebase zijn hardgecodeerd en vóór de lancering nooit zijn opgeruimd
- Geen staging-omgeving, waardoor elke wijziging wordt getest tegen productiedata, of überhaupt niet wordt getest voordat deze live gaat
- Handmatige, ongedocumenteerde uitrolstappen die alleen de oprichter weet uit te voeren, wat één enkel uitvalpunt (single point of failure) creëert

Niets hiervan zijn direct kennisgaten — de meeste technisch ingestelde oprichters weten in theorie dat deze zaken er toe doen. Het zijn tijd- en prioriteitsgaten: wanneer u solo bouwt, concurreert uitrolinfrastructuur rechtstreeks om dezelfde uren met productfuncties, en functies winnen meestal totdat er iets breekt. Een oprichter die absoluut in een weekend een CI/CD-pijplijn zou kunnen bouwen, doet dat vaak niet — niet omdat ze het niet kunnen, maar omdat dat weekend steeds wordt besteed aan de volgende klantgerichte functie. Een rationele afweging, totdat de afwezigheid van de pijplijn een incident veroorzaakt dat meer tijd kost dan het bouwen ervan ooit zou hebben gekost.

## Het gat dichten zonder mensen aan te nemen

Dit is waar het model van LaunchStudio specifiek goed past bij het profiel van de Delftse technische oprichter: in plaats van een volledig engineeringteam in te huren, schakelen oprichters het team van Manifera in — meer dan 120 engineers met ruim 11 jaar productie-ervaring, mede gecoördineerd vanuit onze ontwikkelhub in Ho Chi Minhstad — voor de specifieke infrastructuurwerkzaamheden die buiten hun huidige capaciteit vallen, zonder het eigenaarschap van het product zelf op te geven. Het is dezelfde logica als het inschakelen van een gespecialiseerde aannemer voor het elektrawerk aan een verder zelfgebouwd huis: u draagt niet het hele project over, alleen het specifieke onderdeel dat oprecht gebaat is bij iemand die het elke dag doet. De [custom software development praktijk](https://www.manifera.com/services/custom-software-development/) van Manifera is gebouwd rond precies dit type gerichte engineeringtrajecten in plaats van langdurige personeelsverplichtingen.

Voor een Delftse oprichter die probeert te bepalen welke onderdelen van zijn met Cursor gebouwde product dit type verharding nodig hebben, laten de [pakketopties van LaunchStudio](https://launchstudio.eu/en/#packages) zien wat er doorgaans is inbegrepen bij een productie-gereedheidsronde, afgestemd op het budget van een solo-oprichter in plaats van een enterprise-traject.

## Uw eigen uitrolproces evalueren: Een snelle zelftest

Een technische oprichter kan doorgaans binnen enkele minuten van een eerlijke zelfbeoordeling vertellen of zijn uitrolproces een echt risico is of beheersbaar. Deze vragen zijn niet bedoeld om paniek te zaaien — de meeste solo-gebouwde producten zakken voor ten minste één of twee punten, en dat is precies het doel van deze controle.

**Kan iemand anders dan u een fix uitrollen?**

Als het eerlijke antwoord is "alleen als ik ze er live doorheen praat", heeft u een single point of failure. Dit weegt zelfs zwaar voor een echte solo-oprichter, omdat het ook betekent dat u niet kunt uitrollen vanaf een ziekenhuisbed, een slechte wifi-verbinding of een telefoon.

**Kent u uw hersteltijd (rollback time), of gokt u er naar?**

Vraag het jezelf rechtstreeks af: als de uitrol die u op het punt staat uit te voeren de productie breekt, hoe lang duurt het dan om terug te keren naar de laatst werkende staat? "Ik weet het niet zeker" is een veelvoorkomend en eerlijk antwoord — en een duidelijk teken dat er geen getest rollback-proces bestaat, alleen een aanname dat er een is.

**Wordt elke uitrol op dezelfde manier getest, of hangt het af van hoe zorgvuldig u zich die dag voelt?**

Handmatige, ad-hoc testen vóór een uitrol is in theorie prima en in de praktijk onbetrouwbaar, vooral laat op de avond na een lange sessie debuggen. Een uitrolpijplijn met geautomatiseerde controles wordt niet moe en haast zich niet door stappen onder deadlinedruk.

**Waar leven uw geheimen daadwerkelijk?**

Open uw codebase en zoek naar alles wat lijkt op een echte referentie die rechtstreeks in een bestand staat in plaats van in een omgevingsvariabele. Vroege projecten verzamelen deze snel, meestal vanuit een moment van "dit ruim ik later wel op" dat nooit is gekomen.

**Wat is uw werkelijke schadebereik (blast radius) als de uitrol van vandaag misgaat?**

Voor een oprichter met drie pilotklanten is een eerlijk antwoord waarschijnlijk "beheersbaar, hoewel traag." Voor een oprichter met vijftig betalende klanten die afhankelijk zijn van het product voor hun dagelijkse bedrijfsvoering, draagt hetzelfde kwetsbare proces een wezenlijk ander risico, hoewel er niets aan de onderliggende code is veranderd.

Als twee of meer van deze vragen u onzeker laten, is dat minder een oordeel over uw engineeringvaardigheid en meer een signaal over waar de komende paar dagen aan infrastructuurwerk naartoe zouden moeten gaan, voordat een slechte uitrol de vraag afdwingt. Het is voor de meeste technisch bekwame Delftse oprichters ook eerder een checklist dan een heropbouw — de onderdelen van deze lijst die ontbreken kosten meestal dagen om toe te voegen, geen weken, juist omdat de onderliggende codebase al solide is.

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Het kwetsbare uitrolproces van SensorForge

Daan Smit bouwde SensorForge, een dashboard voor fleet-monitoring voor engineeringteams die gedistribueerde IoT-sensornetwerken beheren — een productidee dat rechtstreeks voortkwam uit de frustraties die hij had met bestaande tools tijdens zijn tijd rond de roboticalabs van de TU Delft. Volledig gebouwd in Cursor werkte SensorForge goed voor zijn eerste handvol pilotklanten, allemaal kleine engineeringteams in de regio Delft.

Het probleem kwam naar voren tijdens een routinematige update: Daan pushte een wijziging rechtstreeks naar productie zonder eerst een staging-test uit te voeren, en een databasemigratie werd onjuist uitgevoerd, waardoor het dashboard gedurende zes uur offline ging tijdens het actieve monitoringsvenster van een pilotklant — het slechtst denkbare moment voor een monitoringtool om op zwart te gaan. Er was geen rollback-proces, dus Daan moest handmatig de vorige databasestaat reconstrueren uit gedeeltelijke logboeken.

**Resultaat:** LaunchStudio bouwde een deugdelijke CI/CD-pijplijn met geautomatiseerde testen, een staging-omgeving die productie spiegelt, en een rollback-proces met één commando, waardoor handmatige productie-uitrollen volledig tot het verleden behoren.

> *"Ik kon de code schrijven. Ik had geen idee hoe kwetsbaar ik was elke keer dat ik op uitrollen drukte, totdat het een klant daadwerkelijk zes uur uitval kostte."*
> — **Daan Smit, Oprichter, SensorForge (Delft)**

**Kosten & Doorlooptijd:** € 2.100 (CI/CD-pijplijn, staging-omgeving, geautomatiseerde rollback) — afgerond in 8 werkdagen.

---

## Veelgestelde vragen

### Ik kan zelf redelijk goed coderen — heb ik LaunchStudio wel echt nodig?
Veel klanten van LaunchStudio zijn technisch bekwame oprichters zoals Daan. De waarde zit niet in het schrijven van code die u zelf niet kunt schrijven — het zit in de discipline voor uitrol en infrastructuur, wat een echt andere vaardigheid is dan productontwikkeling.

### Werkt LaunchStudio met oprichters die zelf hands-on willen blijven met hun eigen codebase?
Ja. LaunchStudio bouwt infrastructuur rondom uw bestaande code en draagt doorgaans de volledige documentatie en toegang over, in plaats van een voortdurende afhankelijkheid te creëren.

### Verschilt de technische oprichtersscène in Delft van andere steden in Zuid-Holland?
Ja, merkbaar — de aanwezigheid van de TU Delft betekent dat een hoger percentage van de oprichters hier comfortabel is met het zelf schrijven en lezen van code, wat bepaalt welk type hulp daadwerkelijk nuttig is.

### Wat voegt het engineeringteam van Manifera specifiek toe aan een CI/CD-inrichting?
De meer dan 120 engineers van Manifera brengen ruim 11 jaar ervaring met productie-uitrollen mee over meer dan 160 projecten, waaronder infrastructuurwerk voor enterprise-klanten zoals Vodafone, toegepast op een schaal die past bij het product van een solo-oprichter.

### Hoe snel kan een deugdelijke CI/CD-pijplijn daadwerkelijk worden gebouwd?
Voor de meeste setups met een enkel product voltooit LaunchStudio dit type infrastructuurwerk doorgaans binnen één tot twee weken, afhankelijk van de complexiteit van de bestaande codebase.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Ik kan zelf redelijk goed coderen — heb ik LaunchStudio wel echt nodig?", "acceptedAnswer": { "@type": "Answer", "text": "De waarde zit in de uitrol- en infrastructuurdiscipline, een echt andere vaardigheid dan productontwikkeling." } },
    { "@type": "Question", "name": "Werkt LaunchStudio met oprichters die zelf hands-on willen blijven met hun eigen codebase?", "acceptedAnswer": { "@type": "Answer", "text": "Ja. LaunchStudio bouwt infrastructuur rond uw bestaande code en draagt de volledige documentatie en toegang over." } },
    { "@type": "Question", "name": "Verschilt de technische oprichtersscène in Delft van andere steden in Zuid-Holland?", "acceptedAnswer": { "@type": "Answer", "text": "Ja — de aanwezigheid van de TU Delft betekent dat een hoger percentage van de oprichters zelf kan coderen." } },
    { "@type": "Question", "name": "Wat voegt het engineeringteam van Manifera specifiek toe aan een CI/CD-inrichting?", "acceptedAnswer": { "@type": "Answer", "text": "Ruim 11 jaar ervaring met productie-uitrollen over 160+ projecten, waaronder werk voor enterprise-klanten zoals Vodafone." } },
    { "@type": "Question", "name": "Hoe snel kan een deugdelijke CI/CD-pijplijn daadwerkelijk worden gebouwd?", "acceptedAnswer": { "@type": "Answer", "text": "Voor de meeste setups voltooit LaunchStudio dit infrastructuurwerk binnen één tot twee weken." } }
  ]
}
</script>
