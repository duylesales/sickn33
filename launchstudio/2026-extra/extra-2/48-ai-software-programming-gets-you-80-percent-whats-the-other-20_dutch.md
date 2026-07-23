---
Titel: "AI-Softwareprogrammering Brengt Je 80%. Wat Is De Andere 20%?"
Trefwoorden: ai software programming, ai software app, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Founder (niet-technisch)
---

# AI-Softwareprogrammering Brengt Je 80%. Wat Is De Andere 20%?

Cursor bracht je 80% van de weg, en dat is een oprecht accurate, gebruikelijke founder-observatie over AI-softwareprogrammering vandaag — het doet het gros van het zichtbare werk opmerkelijk goed. De resterende 20% heeft de neiging te concentreren in een specifieke, controleerbare lijst rechtenrandgevallen, en een gedeeld document dat verondersteld wordt alleen-lezen te zijn, maar dat niet helemaal is, is een schone illustratie van precies wat die lijst omvat.

## Checklistpunt Eén: Betekent "Alleen-Lezen" Daadwerkelijk Alleen-Lezen Op De Server?

Een gedeeld-documentfunctie die zowel "kan bekijken" als "kan bewerken"-delingsrechten biedt heeft de server nodig, niet alleen de interface, om dat onderscheid af te dwingen — als de bewerkingsverzoeken van een "alleen-bekijken"-ontvanger nog steeds verwerkt en opgeslagen worden door de backend ongeacht hun rechtenniveau, biedt de interface die de bewerkingscontroles verbergt helemaal geen daadwerkelijke bescherming.

## Checklistpunt Twee: Wordt Toestemming Gecontroleerd Bij Elk Wijzigend Verzoek, Of Alleen Bij Paginalaad?

Sommige AI-gegenereerde rechtensystemen controleren het toegangsniveau van een gebruiker slechts één keer, wanneer een pagina initieel laadt, om te bepalen wat te tonen — maar als de daadwerkelijke opslaan- of update-actie niet apart datzelfde rechtenniveau opnieuw verifieert voordat het verzoek verwerkt wordt, kan een alleen-bekijken-gebruiker wiens interface simpelweg geen bewerkingsknoppen toont nog steeds mogelijk een bewerkingsverzoek direct indienen.

## Checklistpunt Drie: Zou De Normale Tests Van Een Founder Dit Onthullen?

Delingsrechten testen door een echt tweede account uit te nodigen, te bekijken zoals bedoeld, en te bevestigen dat de interface correct bewerkingscontroles verbergt ziet er volledig correct uit — omdat het correct is vanuit het perspectief van de interface. Het gat onthult zichzelf alleen als iemand specifiek probeert een bewerkingsverzoek in te dienen ondanks dat de interface er geen aanbiedt, wat coöperatieve tests geen reden hebben te proberen.

## Checklistpunt Vier: Doet Dit Meer Ertoe Voor Specifiek Coaching-Gerelateerde Inhoud?

De gedeelde documenten van een carrièrecoachingplatform bevatten vaak oprecht persoonlijke inhoud — de carrièredoelen van een klant, salarisverwachtingen, persoonlijke reflecties gedeeld met een specifieke coach — wat betekent dat ongeautoriseerde wijziging niet alleen een technisch ongemak is, het is een echte schending van precies het soort vertrouwen waar een coachingrelatie specifiek van afhangt.

## Checklistpunt Vijf: Hoe Weet Een Founder Of Hun Eigen Product Dit Gat Heeft?

Zonder specifiek een bewerkingsverzoek te testen vanuit het perspectief van een alleen-bekijken-account kan een founder over het algemeen niet weten wat het geval is uit gewoon gebruik alleen — deze specifieke controle vereist ofwel technisch comfort met het direct vervaardigen van zo'n verzoek, ofwel een toegewijde review die precies dit scenario als routine test.

## Dit Gat Dichten Zonder Delen Te Overcompliceren

Een correcte fix herverifieert rechtenniveau bij elk wijzigend verzoek server-side, onafhankelijk van wat de interface toont, consistent toegepast over elke gedeelde of collaboratieve functie in een product. [LaunchStudio](https://launchstudio.eu/en/) test precies dit patroon als onderdeel van zijn toegangscontrolereview, gesteund door Manifera's 11+ jaar ervaring met het bouwen van rechtensystemen voor collaboratieve software.

Manifera's rechten- en toegangscontroleaudits worden uitgevoerd door het engineeringteam bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Loop met ons door wat je gebouwd hebt — we reageren binnen een werkdag](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het alleen-bekijken-document dat een klant nog steeds kon bewerken

Luuk, een voormalig HR-carrière-overgangsconsultant die founder werd in Harderwijk, bouwde LoopbaanPad, een AI-geassisteerd carrièrecoachingplatform gebouwd met Lovable, waarmee coaches planningsdocumenten met klanten deelden met ofwel alleen-bekijken ofwel bewerkingsrechten afhankelijk van het specifieke document.

Een coach merkte op dat het gedeelde, verondersteld alleen-bekijken carrièreplan van een klant gewijzigd was, waarbij de klant erop stond dat hij alleen ooit in het document rondgeklikt had zonder te beseffen dat bewerkingen zelfs mogelijk waren. LaunchStudio's review bevestigde dat het documentupdate-eindpunt bewerkingsverzoeken accepteerde en opsloeg ongeacht het gedeeld-recht geregistreerd voor die specifieke gebruiker, wat betekende dat de "alleen-bekijken"-beperking alleen bestond in welke knoppen de interface toonde, niet in wat de server daadwerkelijk toestond.

**Resultaat:** LaunchStudio voegde server-side rechtenverificatie toe aan elk documentupdate-verzoek, en zorgde ervoor dat een alleen-bekijken-deling oprecht geen inhoud kan wijzigen ongeacht hoe het verzoek gemaakt wordt, en dicht het gat zonder te veranderen hoe coaches delingsrechten configureerden.

> *"De klant probeerde voor zover we kunnen zien niet eens iets verkeerds te doen — een UI-actie triggerde toevallig gewoon een opslag die nooit door had mogen gaan in de eerste plaats. Het had oprecht een veel minder onschuldige situatie kunnen zijn."*
> — **Luuk Timmermans, Founder, LoopbaanPad (Harderwijk)**

**Kosten & tijdlijn:** €2.000 (rechtenverificatieaudit over gedeelde documenten) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Zou een toegangscontrolespecialist alleen-interface-rechtenafdwinging een gebruikelijke kortere weg beschouwen in snel gebouwde functies?

Ja, behoorlijk gebruikelijk — het is oprecht sneller een delingsfunctie te bouwen die alleen aanpast wat de interface toont gebaseerd op rechtenniveau, en de kortere weg werkt perfect voor elke test die met het product interageert precies zoals de interface het presenteert, wat precies waarom het makkelijk over het hoofd gezien wordt.

### Is dit soort gat specifiek voor documentdelingsfuncties, of verschijnt het ook in andere collaboratieve functies?

Het generaliseert naar elke functie met meer dan één rechtenniveau dat toegang deelt tot dezelfde resource — gedeelde kalenders, gedeelde projectborden, en reactierechten op gedeelde inhoud staan allemaal voor dezelfde onderliggende vraag of de server, niet alleen de interface, het onderscheid daadwerkelijk afdwingt.

### Manifera heeft rechtensystemen gebouwd voor collaboratieve software over verschillende industrieën — draagt die ervaring specifiek over naar een carrièrecoaching-context zoals die van LoopbaanPad?

Ja, direct — het onderliggende rechtenverificatiepatroon is identiek ongeacht het specifieke doel van de collaboratieve software, en dit patroon geïmplementeerd en gereviewd hebben over vele verschillende collaboratieve contexten maakt het vangen en correct dichten van het gat aanzienlijk sneller voor elke nieuwe klant, coaching-specifiek of anderszins.

### CEO Herre Roelevink heeft gesproken over de laatste 20% als waar architectuur, niet ruwe functies, bepaalt of een product oprecht betrouwbaar is — illustreert dit rechtengat dat goed?

Heel goed — LoopbaanPads delingsfunctie werkte precies zoals beschreven vanuit een functielijst-perspectief, met het ontbrekende stuk een specifieke architecturale beslissing over waar rechten daadwerkelijk afgedwongen worden, precies het laatste-20%-onderscheid dat Roelevinks commentaar op het resterende gat van AI-native founders consistent benadrukt.

### Als een founder specifiek hun AI-tool vraagt "alleen-bekijken-rechten correct af te dwingen," lost dat dit betrouwbaar op?

Het kan helpen de aandacht van de tool naar de vereiste te richten, maar betrouwbaar bevestigen dat de resulterende implementatie daadwerkelijk rechten server-side afdwingt, bij elk relevant verzoek in plaats van alleen bij initieel paginalaad, heeft nog steeds baat bij onafhankelijke technische verificatie in plaats van te vertrouwen dat de intentie van de prompt volledig en correct vertaald werd naar de gegenereerde code.
