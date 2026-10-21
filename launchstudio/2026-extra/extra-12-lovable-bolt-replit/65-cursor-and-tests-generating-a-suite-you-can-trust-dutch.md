---
Titel: "Cursor en Tests: Een Testsuite Genereren Die U Kunt Vertrouwen"
Trefwoorden: cursor tests, gegenereerde tests, testdekking, assertions, regressietests, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Cursor en Tests: Een Testsuite Genereren Die U Kunt Vertrouwen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor en Tests: Een Testsuite Genereren Die U Kunt Vertrouwen",
  "description": "Een assistent schrijft tweehonderd tests in een uur, en de meeste controleren niets nuttigs. Welke tests de moeite waard zijn, hoe u een echte van een decoratieve onderscheidt, en de volgorde waarin u ze bouwt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-and-tests-generating-a-suite-you-can-trust" }
}
</script>

Vraag een AI-editor tests te schrijven voor uw project en u hebt er binnen het uur honderden. Ze draaien, ze slagen, en het dekkingspercentage is indrukwekkend.

Een betekenisvol deel ervan controleert niets wat ertoe doet: dat een component rendert zonder fout, dat een functie een waarde teruggeeft, dat een mock werd aangeroepen. Ze slagen of uw product nu werkt of niet, en dat maakt ze erger dan geen tests, omdat ze vertrouwen geven zonder het te verdienen.

Tests zijn echt waardevol in een AI-gebouwd product — meer dan in een handgeschreven product, omdat de code snel en onvoorspelbaar verandert. De vaardigheid is weten welke u houdt.

## Hoe een Echte Test Eruitziet

Een nuttige test formuleert een verwachting die kan falen. De vraag bij elke gegenereerde test is: wat zou er kapot moeten gaan om deze rood te maken?

"Rendert zonder te crashen" faalt alleen als het component een fout gooit, en dat is zelden de interessante fout.

"Btw berekenen over €100 tegen 21 procent geeft €121" faalt als de berekening fout is, en dat is precies wat u wilt weten.

"Een gebruiker van organisatie B die de factuur van organisatie A opvraagt, krijgt een 403" faalt als uw autorisatie breekt, en dat is de waardevolste assertion in de hele suite.

Lees de assertions, niet de namen. Gegenereerde tests hebben uitstekende namen en soms een lege inhoud.

## De Volgorde Die de Moeite Waard Is

Voor een klein product zijn dertig tot vijftig tests die de juiste dingen dekken beter dan vierhonderd die alles dekken.

**Eerst autorisatie.** Per endpoint een test dat een gebruiker van een andere organisatie wordt geweigerd. Dit is de waardevolste set in een AI-gebouwd product, omdat het de faalwijze is die deze reeks het vaakst documenteert en omdat ze blijft werken terwijl alles eromheen wordt herschreven.

**Daarna geld.** Elke berekening met prijzen, btw, kortingen, pro rata, totalen en terugbetalingen, met de lastige getallen in plaats van de ronde — bedragen die afrondingsverschillen opleveren, nul, negatief, en de hoogste waarde die u accepteert.

**Ten derde de hoofdflow.** Eén end-to-end-test die aanmeldt, het centrale ding doet waarvoor uw product bestaat, en de uitkomst controleert. Die vangt de deploy op die alles brak, wat geen enkele unittest doet.

**Dan elke bug die u twee keer hebt opgelost.** Een test geschreven op het moment van de tweede fix garandeert dat er geen derde komt, en deze set groeit uit tot het waardevolste deel van een volwassen suite.

Dat is een suite die in minder dan een minuut draait, die u vertrouwt, en die u houdt.

## Waar Gegenereerde Tests Misgaan

Vier patronen om op te letten bij het accepteren van een gegenereerde suite.

**De implementatie testen in plaats van het gedrag.** Een test die controleert dat een bepaalde interne functie werd aangeroepen, breekt wanneer u de code reorganiseert zonder te veranderen wat ze doet, en dat leert u fouten te negeren.

**Alles mocken.** Een test waarin de database, de betaalprovider en de e-maildienst allemaal door mocks zijn vervangen, controleert dat uw code mocks in de juiste volgorde aanroept. De bugs zitten meestal in de interactie met de echte dingen.

**Controleren wat de code doet in plaats van wat ze zou moeten doen.** Een model dat tests schrijft op basis van uw implementatie, legt uw bugs vast als verwacht gedrag. Dit is de verraderlijkste fout, omdat de suite u dan actief belet ze op te lossen.

**Dekking als doel.** Een model dat wordt gevraagd 90 procent te halen, haalt dat, en de laatste 30 procent zijn tests van foutpaden die niemand tegenkomt, geschreven om regels aan te raken in plaats van iets te controleren.

## Gebruik de Assistent Goed

Tests zijn een uitstekende toepassing van een AI-editor, mits de richting van u komt.

Wat werkt: het geval beschrijven en om de test vragen. "Schrijf een test dat een gebruiker in organisatie B een 403 krijgt bij het opvragen van een factuur van organisatie A." Specifiek, controleerbaar, en precies het soort standaardwerk dat vervelend is om met de hand te schrijven.

Wat minder goed werkt: "schrijf tests voor dit bestand", wat de decoratieve suite hierboven oplevert.

Nog twee gewoonten. Schrijf de test vóór de fix als u een bug corrigeert — bevestig dat hij faalt, pas de fix toe, bevestig dat hij slaagt — wat de enige manier is om zeker te weten dat de test test wat u denkt. En lees elke assertion voordat u accepteert, omdat de faalwijze van gegenereerde tests is dat ze om de verkeerde reden slagen.

## Maak de Suite Iets Dat U Blijft Draaien

Een testsuite die traag, onbetrouwbaar of luidruchtig is, wordt niet meer gedraaid, en een suite die niet wordt gedraaid is erger dan geen, omdat ze wegrot tot een bron van valse alarmen.

Drie eigenschappen houden haar in leven.

**Snel.** Onder een minuut voor de suite die u constant draait. Is er echt een grotere set nodig — browsertests, integratie met echte diensten — scheid die dan en draai haar bij deployment in plaats van bij elke wijziging.

**Deterministisch.** Een test die af en toe faalt, leert u fouten te negeren, en dat is de slechtst denkbare uitkomst. De gebruikelijke oorzaken zijn tijd, willekeur, netwerkaanroepen en volgorde tussen tests, en alle vier zijn op te lossen: zet de klok vast, seed de willekeur, vermijd het netwerk, en reset de toestand tussen tests in plaats van af te hangen van de volgorde waarin ze draaien.

**Eerlijk als ze faalt.** Een fout moet zeggen wat werd verwacht en wat er gebeurde, in termen waarmee u het probleem kunt vinden. Gegenereerde tests controleren vaak een heel object, zodat een verschil in één veld een onleesbare dump oplevert.

En koppel haar aan deployment zodat een falende suite de release stopt. Tests die u moet onthouden te draaien, zijn tests die u niet draait op de middag dat u ze het hardst nodig had — en dat is, naar het bewijs van elk incident in deze reeks, een vrijdag.

## Tests als Instructies voor de Volgende Sessie

Er is een tweede reden waarom tests meer uitmaken in een codebase die grotendeels door tools is geschreven, en die gaat niet over het opvangen van regressies.

Een test is een uitvoerbare verklaring van wat de code hoort te doen. Een assistent die aan uw project werkt, leest ze, en een falende test is feedback waarop hij kan handelen zonder dat u erbij hoeft te zijn — wat de kwaliteit van wat terugkomt verandert. Met een suite controleert een model dat wordt gevraagd een berekening te wijzigen zijn werk; zonder levert het iets plausibels op en geeft het aan u.

Dat maakt de autorisatie- en geldtests dubbel waardevol. Het zijn de regels die u het liefst gehandhaafd ziet, en ze worden nu gehandhaafd tegenover wat de volgende versie van die code ook schrijft, inclusief sessies die u allang bent vergeten.

Twee praktijken versterken dit. Noem tests naar de regel in plaats van naar de functie — "een lid dat in juli instroomt, betaalt zeven twaalfde van de jaarcontributie" vertelt een lezer en een model wat de bedoeling is, terwijl "test calculateFee case 3" geen van beiden iets vertelt. En houd de tests dicht bij de regels die ze vastleggen, zodat iedereen die het gedrag wijzigt direct de verwachting tegenkomt.

Het bredere punt, dat door deze hele reeks loopt: de artefacten die een AI-gebouwde codebase beheersbaar maken — het afsprakenbestand, de types, de tests — zijn allemaal documentatie die de machine kan lezen. Dat is een andere reden om ze te hebben dan de traditionele, en een aanzienlijk sterkere.

Het verandert ook de economie van de dertig tests. Ze zijn niet alleen een verzekering tegen een regressie; ze zijn de instructies die elke toekomstige sessie beter werk laten leveren, en dat is een rendement dat zich opstapelt op een manier die een verzekering niet doet.

Die herformulering beslecht meestal de discussie over of een klein product zich tests kan veroorloven. Het kan er dertig betalen, ze kosten een dag, en ze zijn de goedkoopste manier om alles wat de tools daarna opleveren betrouwbaarder te maken.

## Dit Inrichten

Voor een bestaand product is dit doorgaans één tot twee dagen: per endpoint een autorisatietest die weigering tussen organisaties controleert, tests voor elke geldberekening met lastige in plaats van ronde getallen, één end-to-end-test van de hoofdflow, een test voor elke bug die twee keer is voorgekomen, gegenereerde tests beoordeeld op assertions die echt kunnen falen met de decoratieve verwijderd, mocken beperkt zodat echte interacties worden uitgeoefend waar het ertoe doet, de suite draaiend in minder dan een minuut en gekoppeld aan uw deployment zodat een fout de release stopt, en een gewoonte om bij het oplossen van een bug eerst de falende test te schrijven.

LaunchStudio bouwt deze proportionele suite als onderdeel van productiegereedheid, en het is meestal wat ervoor zorgt dat deployen niet langer zenuwslopend is. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons welke van uw tests een echte bug zouden opvangen](https://launchstudio.eu/nl/#contact). Dat zijn er vaak minder dan het aantal doet vermoeden.

## Echt voorbeeld

### Vierhonderd Tests en een Productiebug

Jeroen Wijnstra bouwde Contributiebeheer in Cursor: contributieadministratie voor verenigingen en clubs, 63 organisaties die samen zo'n €2 miljoen per jaar via automatische incasso innen.

Hij had de assistent gevraagd een testsuite te schrijven en accepteerde wat die opleverde: 412 tests, 91 procent dekking, allemaal geslaagd, met een looptijd van vier minuten.

Een incassorun schreef vervolgens 140 leden twee keer af. De oorzaak was een berekening die een pro-ratakorting toepaste voor leden die halverwege het jaar instroomden, en die was aangepast om een niet-gerelateerd afrondingsprobleem op te lossen; door de wijziging werd de korting toegepast op het volledige jaarbedrag in plaats van op de resterende maanden, wat voor recent ingestroomde leden een tweede afschrijving opleverde.

De suite had elf tests van die functie. Alle elf slaagden. Ze waren gegenereerd op basis van de implementatie, controleerden de waarden die de code toen opleverde, en werden automatisch bijgewerkt toen de code veranderde — waarmee de bug als verwacht resultaat werd vastgelegd.

Drie werkdagen: de 412 tests beoordeeld en 280 verwijderd omdat ze niets controleerden dat kon falen — rendert zonder te crashen, geeft een waarde terug, mock werd aangeroepen; de resterende 132 onderzocht op assertions die van de implementatie waren afgeleid in plaats van van de bedoeling, waarvan 40 herschreven tegen expliciete bedrijfsregels uit de verenigingsafspraken; per endpoint een autorisatietest over 31 endpoints, waarbij de oefening er drie vond zonder enige controle; geldtests geschreven op basis van de regels in plaats van de code, voor instromen halverwege het jaar, uitstromen, afronding, nul en de maximale contributie, met lastige bedragen; een end-to-end-test van de incassorun; een test voor de dubbele-afschrijvingsbug geschreven vóór de fix en eerst falend bevestigd; en de suite teruggebracht tot 94 tests die in 50 seconden draaien en aan deployment gekoppeld zijn.

**Resultaat:** de 140 dubbele afschrijvingen werden terugbetaald en de verenigingen geïnformeerd. Jeroens oordeel is dat de suite van 412 tests actief schadelijk was geweest — ze had hem genoeg vertrouwen gegeven om op een vrijdag een wijziging aan de contributieberekening te deployen zonder die met de hand te controleren.

> *"Vierhonderdtwaalf tests, eenennegentig procent dekking, allemaal groen, en ze waren groen omdat ze waren geschreven op basis van de code in plaats van op basis van wat de code hoorde te doen."*
> — **Jeroen Wijnstra, Oprichter, Contributiebeheer (Gouda)**

**Kosten & Doorlooptijd:** €3.300 (beoordeling en inkorting van de suite, assertions herschreven vanuit bedrijfsregels, autorisatietests over 31 endpoints met drie gevonden gaten, geldtests vanuit expliciete regels, end-to-end-test van de incasso, regressietest voor het incident, koppeling aan deployment) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Zijn gegenereerde tests de moeite waard?

De juiste wel. Vraag bij elke test: wat zou er kapot moeten gaan om deze te laten falen? Tests die slagen ongeacht of uw product werkt, geven vertrouwen zonder veiligheid te bieden.

### Welke tests doen er het meest toe in een AI-gebouwd product?

Autorisatie — per endpoint een gebruiker van een andere organisatie die wordt geweigerd. Het is de fout die dit soort codebase het vaakst oplevert, en de test blijft werken terwijl de code eromheen wordt herschreven.

### Waarom is hoge dekking misleidend?

Omdat dekking meet welke regels zijn uitgevoerd, niet welk gedrag is gecontroleerd. Een suite kan 90 procent van uw code raken terwijl ze bijna niets controleert over of die correct is.

### Wat is er mis met tests gegenereerd op basis van mijn implementatie?

Ze leggen uw huidige gedrag vast als correct, inclusief uw bugs, en voorkomen dan dat u het merkt wanneer u ze oplost. Schrijf assertions vanuit de regel, niet vanuit de uitvoer.

### Hoeveel tests heeft een klein product nodig?

Dertig tot vijftig die autorisatie, geld, de hoofdflow en elke bug die twee keer is voorgekomen dekken. Ze moeten in minder dan een minuut draaien en u moet ze vertrouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zijn door AI gegenereerde tests nuttig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De juiste wel. Vraag wat er kapot moet gaan om elke test te laten falen — tests die ongeacht de juistheid slagen, geven vertrouwen zonder veiligheid."
      }
    },
    {
      "@type": "Question",
      "name": "Welke tests doen er het meest toe in een AI-gebouwd product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Autorisatietests per endpoint, die controleren dat een gebruiker van een andere organisatie wordt geweigerd."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is testdekking misleidend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze meet uitgevoerde regels in plaats van gecontroleerd gedrag — een suite kan 90 procent halen terwijl ze bijna niets controleert."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is er mis met tests geschreven vanuit de implementatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze leggen het huidige gedrag, bugs inbegrepen, vast als verwacht — en verzetten zich vervolgens tegen de fixes."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel tests heeft een klein product nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dertig tot vijftig voor autorisatie, geld, de hoofdflow en elke bug die twee keer voorkwam, met een looptijd onder een minuut."
      }
    }
  ]
}
</script>
