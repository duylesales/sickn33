---
Titel: "Het Verborgen Workflowprobleem: Waarom AI-code Tests Doorstaat Maar Faalt Bij Echt Gebruik"
Trefwoorden: van vibe coding naar productie, ai code tool, ai coding, ai vulnerabilities, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Het Verborgen Workflowprobleem: Waarom AI-code Tests Doorstaat Maar Faalt Bij Echt Gebruik

Een groen vinkje op een geslaagde testsuite voelt als bewijs. Het is eigenlijk bewijs van iets aanzienlijk smaller dan het lijkt: dat jouw code correct gedraagt voor precies de scenario's die jouw tests beschrijven. Echte gebruikers volgen de scenario's die jouw tests beschrijven niet — ze volgen paden door jouw product die niemand specifiek anticipeerde, en het is precies in dat gat, tussen "getest" en "daadwerkelijk gebruikt," waar verborgen workflowaannames leven.

## Wat Een Verborgen Workflowaanname Daadwerkelijk Is

Elk stuk code bedt impliciete aannames in over de volgorde en manier waarop het gebruikt zal worden — aannames die zo natuurlijk aanvoelen voor wie de code ook schreef of genereerde dat ze nooit expliciet uitgesproken worden, laat staan getest. Een registratieflow die aanneemt dat e-mailverificatie plaatsvindt voordat een gebruiker enige andere actie probeert; een afrekenflow die aanneemt dat een gebruiker niet achterwaarts navigeert halverwege het proces; een formulier dat aanneemt dat velden ingevuld worden in de volgorde waarin ze getoond worden. Geen van deze aannames is onredelijk als standaardverwachting — ze zijn simpelweg ongetest, wat betekent dat het gedrag van de code wanneer een gebruiker een van ze schendt oprecht onbekend is, niet geverifieerd om ofwel prima of kapot te zijn.

## Waarom AI-gegenereerde Code Hier Specifiek Vatbaar Voor Is

Een AI-codeertool genereert code die het beschreven scenario in jouw prompt bevredigt, en die beschrijving impliceert bijna altijd het bedoelde, voorwaarts-bewegende pad door een functie — omdat dat is wat je beschreef toen je erom vroeg. De tool heeft geen natuurlijk mechanisme om onafhankelijk te genereren en te testen tegen de paden die je niet beschreef, aangezien het geen manier heeft om te weten welke ongeuite aannames zijn eigen gegenereerde code stilletjes op vertrouwt tot die aannames specifiek, doelbewust getest worden.

## Waar Dit Specifiek Verschijnt In De Praktijk

**Acties buiten volgorde.** Een gebruiker die jouw app opent in twee browsertabbladen en acties uitvoert in een onverwachte sequentie, of die de terugknop van een browser gebruikt om terug te keren naar een stap die jouw flow aannam lineair en eenrichting was.

**Onderbroken flows.** Een gebruiker die een meerstapsproces halverwege verlaat, en dan later terugkeert — hervat jouw app schoon vanaf waar ze gebleven waren, of eindigt het in een inconsistente toestand die noch volledig compleet noch schoon gereset is?

**Onverwachte invoertiming.** Een gebruiker die een formulier sneller indient dan jouw validatielogica verwacht, of trager, en een sessie- of toestandswijziging tegenkomt die jouw code aannam niet zou gebeuren midden in interactie.

**Multi-apparaat- of multi-sessiegebruik.** Een gebruiker actief op zowel een telefoon als een laptop simultaan, wat precies het soort gelijktijdige-toegangscondities elders in deze serie behandeld triggert, maar afkomstig van legitiem eenpersoonsgedrag in plaats van twee verschillende mensen.

## Waarom "Meer Tests" Niet Het Volledige Antwoord Is

De instinctieve reactie — meer testgevallen schrijven — helpt, maar alleen voor de specifieke scenario's waar iemand aan denkt om tests voor te schrijven, wat precies dezelfde beperking is die het originele gat creëerde. Wat verborgen workflowaannames daadwerkelijk naar boven brengt is een compleet andere discipline: doelbewust, systematisch proberen jouw eigen product te gebruiken in onverwachte volgordes en onderbroken sequenties, specifiek zoekend naar de aannames waar jouw code stilletjes op vertrouwt in plaats van te bevestigen dat het doet wat je al wist dat je bedoelde.

## Een Praktische Techniek: Verkennend Adversarieel Gebruik

Reserveer toegewijde tijd — apart van functieontwikkeling en apart van het schrijven van geplande testgevallen — specifiek om jouw eigen product te gebruiken zoals een onvoorspelbare echte gebruiker zou doen: klik dingen buiten de verwachte volgorde, verlaat flows halverwege en keer later terug, open meerdere tabbladen en handel in beide simultaan. Deze verkennende sessie, apart van zowel ontwikkeling als formeel testen, is specifiek ontworpen om de aannames naar boven te brengen die geen van die andere activiteiten natuurlijk oproept.

[LaunchStudio](https://launchstudio.eu/en/) omvat precies dit soort verkennend adversarieel testen als onderdeel van zijn productiegereedheidsreview, specifiek jagend op verborgen workflowaannames voorbij wat een standaard testsuite dekt, gesteund door Manifera's engineeringdiscipline over 160+ opgeleverde projecten.

[Laat jouw app testen zoals echte gebruikers het daadwerkelijk zullen gebruiken, niet alleen zoals je verwachtte](https://launchstudio.eu/en/#calculator) — tests doorstaan en echt gebruik overleven zijn verschillende beweringen.

## Echt voorbeeld

### Een AI-native founder in actie: de terugknop die een meerstaps-onboardingflow brak

Iwan, een voormalig verzekeringsschade-expert die founder werd in Roermond, bouwde ClaimAssist, een AI-tool die kleine verzekeringsmakelaars hielp klanten te begeleiden door een gestructureerd, meerstaps-schadedocumentatieproces, met Bolt, met een vijfstaps-onboardingflow die elke test doorstond die Iwan en zijn testers geschreven hadden, allemaal specifiek voorwaarts bewegend door de stappen in de bedoelde sequentie.

Tijdens LaunchStudio's verkennende review gebruikte een tester specifiek de terugknop van hun browser halverwege stap drie, en ging dan weer voorwaarts — een natuurlijke, onopvallende actie die veel echte gebruikers instinctief uitvoeren wanneer ze een vorige invoer dubbelchecken. ClaimAssists flow, die nooit getest was tegen dit specifieke navigatiepatroon, betrad een inconsistente toestand: het formulier toonde stap drie opnieuw maar had stilletjes het spoor van data ingevoerd in stap twee verloren, en produceerde een incompleet schaderecord zonder foutmelding of waarschuwing aan de gebruiker.

**Resultaat:** LaunchStudio implementeerde correct toestandsbeheer dat achterwaartse navigatie binnen de flow correct afhandelt, en behield eerder ingevoerde data ongeacht navigatiepatroon — en dichtte een gat dat Iwans eigen testen, dat altijd strikt voorwaarts door de stappen bewoog, structureel nooit tegenkwam.

> *"Elke test die we schreven bewoog voorwaarts door de stappen omdat dat is hoe we het ontworpen hadden om gebruikt te worden. Het kwam nooit bij iemand op dat terug drukken om iets dubbel te checken — wat een ongelooflijk normaal ding is om te doen — stilletjes het hele record zou corrumperen. Niets in onze tests drukte ooit die knop."*
> — **Iwan Claassen, Founder, ClaimAssist (Roermond)**

**Kosten & tijdlijn:** €1.400 (verkennend testen en workflowtoestandsverharding) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Hoe verschilt verkennend adversarieel testen van het smoke-testen elders in deze serie behandeld?

Smoke tests verifiëren specifieke, vooraf gedefinieerde scenario's betrouwbaar slagen bij elke codewijziging, automatisch gedraaid; verkennend testen is een handmatig, open-einde ontdekkingsproces specifiek zoekend naar scenario's die niemand dacht te definiëren als testgeval om te beginnen — de twee zijn complementair, geen vervangingen voor elkaar.

### Hoe zou ik de terugknop-bug die Iwan tegenkwam gevonden hebben zonder een toegewijde verkennende sessie?

Realistisch, alleen via een echte gebruiker die het tegenkomt en verwarrend, moeilijk te beschrijven gedrag rapporteert, of via dit soort doelbewust, toegewijd verkennend testen — de bug vereiste een specifieke navigatieactie die geen vooraf gedefinieerd testscenario toevallig omvatte.

### Is dit soort verborgen workflowaanname gebruikelijker in specifiek meerstapsflows, of geldt het breed?

Het is het meest acuut in meerstaps, stateful flows zoals Iwans onboardingproces, aangezien ze meer gelegenheid hebben voor buiten-volgorde of onderbroken interactie, hoewel het onderliggende principe — ongeteste aannames over gebruiksvolgorde — van toepassing is op elke functie met meer dan één mogelijk pad erdoorheen.

### Hoeveel tijd moet een founder begroten voor verkennend adversarieel testen vóór lancering?

Een paar gerichte uren specifiek toegewijd aan het proberen van onverwachte sequenties over jouw kritieke flows brengt doorgaans de meest consequentiële verborgen aannames naar boven, vergelijkbaar in scope met de smoke-test-tijdsinvestering elders in deze serie behandeld, hoewel de activiteit zelf kwalitatief anders is — open-einde verkenning in plaats van bekende scenario's bevestigen.

### Vereist het repareren van een verborgen workflowaanname, zoals Iwans toestandsbeheerprobleem, doorgaans significante herarchitectuur?

Doorgaans niet — zoals in Iwans geval was de fix het toevoegen van correcte toestandsafhandeling voor een reeds bestaande flow, niet de flow zelf herstructureren, consistent met het bredere punt van deze serie dat productiegereedheidswerk doorgaans additief en gericht is in plaats van een herbouw te vereisen.
