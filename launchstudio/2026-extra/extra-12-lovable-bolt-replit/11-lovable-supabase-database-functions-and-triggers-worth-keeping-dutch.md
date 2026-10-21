---
Titel: "Lovable Supabase: Databasefuncties en Triggers Die het Bewaren Waard Zijn"
Trefwoorden: lovable supabase, databasefuncties, Postgres-triggers, plaats van bedrijfslogica, data-integriteit, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Databasefuncties en Triggers Die het Bewaren Waard Zijn

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Databasefuncties en Triggers Die het Bewaren Waard Zijn",
  "description": "AI-tools strooien triggers en functies door een Supabase-schema totdat niemand meer kan uitleggen wat er bij een insert gebeurt. Welke hun plek verdienen, welke in applicatiecode horen, en hoe u vindt wat er al staat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-database-functions-and-triggers-worth-keeping" }
}
</script>

Een oprichter vroeg ons waarom het aanmaken van een project in zijn app twee e-mails verstuurde. Het kostte een middag om te beantwoorden, en het antwoord was dat zijn applicatie er één verstuurde en een databasetrigger de andere — vier maanden eerder geschreven door een AI-sessie, naar aanleiding van een verzoek dat hij vergeten was.

Dat is de typische fout van databaselogica in door AI gebouwde producten. Niet dat triggers verkeerd zijn, maar dat ze onzichtbaar zijn. Niets in de applicatiecode noemt ze. Ze verschijnen niet als u naar de functie zoekt. Ze draaien toch, bij elke insert, voor altijd, en het eerste teken van hun bestaan is gedrag dat niemand kan verklaren.

Het antwoord is ze niet te verbieden en ze ook niet te laten opstapelen. Het is weten wat u hebt en alleen de exemplaren bewaren die echt beter in de database staan dan in uw code.

## Zoek Uit Wat Er Al Staat

Maak een lijst van wat er bestaat voordat u iets beslist. Het Supabase-dashboard toont databasefuncties en triggers, en de lijst in een door AI gebouwd project van een jaar oud is meestal langer dan de eigenaar verwacht.

Lees elk exemplaar en schrijf er een zin naast: wat het doet, wat het activeert, en of iets er nog van afhangt. Dat kost een uur en is de hele diagnose.

Verwacht drie categorieën te vinden. Een paar die dragend en correct zijn — bijhouden van tijdstempels, een teller, de standaardtrigger die bij aanmelding een profiel aanmaakt. Meerdere die iets dupliceren wat uw applicatie ook doet, en daar komen de dubbele e-mails vandaan. En één of twee die niets betekenisvols meer doen omdat de functie die ze nodig had is verwijderd, waardoor een trigger vuurt op een tabel die niemand leest.

## Wat in de Database Hoort

Drie soorten logica staan echt beter in Postgres, en ze daarheen verplaatsen maakt een klein product betrouwbaarder in plaats van ingewikkelder.

**Regels die moeten gelden, ongeacht wat de data schreef.** Een constraint dat een bedrag niet negatief mag zijn, dat een boeking niet kan eindigen vóór ze begint, dat een e-mailadres uniek is binnen een organisatie. Dat is geen bedrijfslogica in de interessante zin — het zijn uitspraken over wat een geldige rij is, en ze in de database afdwingen betekent dat ze gelden wanneer data binnenkomt via een importscript, een beheeractie, of een AI-sessie die vergat dat de regel bestond.

**Afgeleide waarden die nooit mogen afdrijven.** Een tijdstempel van de laatste wijziging, een zoekvector, een gedenormaliseerde teller die duur zou zijn om te berekenen. Een trigger die deze bijhoudt, is echt beter dan applicatiecode, omdat hij niet te omzeilen is.

**Handelingen die atomair moeten zijn over meerdere tabellen.** Een bedrag tussen saldi verplaatsen, een taak uit een wachtrij claimen, een uitnodiging accepteren die drie tabellen raakt. Eén databasefunctie die alles binnen één transactie doet, is zowel sneller als veiliger dan meerdere round trips vanuit uw applicatie, die er elk tussendoor kunnen mislukken.

## Wat in Uw Applicatie Hoort

Al het andere, en vooral alles wat de buitenwereld bereikt.

Een trigger die een e-mail verstuurt, een webhook aanroept, een kaart afschrijft of naar een andere dienst schrijft, is een trigger die kan mislukken op manieren die de database niet kan oplossen. Wordt de transactie teruggedraaid, dan is de e-mail al weg. Is de externe aanroep traag, dan is uw insert traag. Geeft hij een fout, dan ziet de gebruiker een databasefout voor een mislukking die niets met zijn data te maken had.

De regel die dit eenvoudig houdt: de database mag de database veranderen. Alles wat de wereld verandert, hoort in code die u kunt zien, opnieuw proberen en loggen.

Bedrijfsprocessen in meerdere stappen horen ook in de applicatie, niet omdat Postgres ze niet kan uitdrukken, maar omdat de volgende persoon die uw product leest ze moet kunnen vinden. Een wervingsproces verspreid over vier triggers is een wervingsproces dat niemand met vertrouwen kan aanpassen.

## Security Definer Is de Scherpe Kant

Supabase-functies kunnen draaien met de rechten van degene die ze definieerde in plaats van degene die ze aanroept, wat nodig is voor handelingen die row-level security terecht moeten omzeilen.

Het is ook hoe row-level security per ongeluk wordt omzeild. Een hulpfunctie die is geschreven om "gewoon de records van de organisatie op te halen", gemarkeerd als security definer omdat een foutmelding daardoor verdween, is een functie die de records van elke organisatie teruggeeft aan elke aanroeper die haar kan uitvoeren.

Drie gewoontes beperken het risico. Gebruik het alleen wanneer er een specifieke reden is, en schrijf die reden in een opmerking. Controleer binnen zo'n functie expliciet de identiteit van de aanroeper in plaats van aan te nemen dat die al geautoriseerd was. En stel op elke security definer-functie expliciet het zoekpad (search path) in, want zonder dat kan de functie worden overgehaald iets anders aan te roepen dan de auteur bedoelde.

Heeft uw project security definer-functies die niemand kan uitleggen, dan is dat het eerste wat u moet bekijken — nog vóór de policies zelf.

## Triggers en het Probleem van Dubbel Schrijven

De meest voorkomende concrete fout is eenvoudig: zowel de trigger als de applicatie doen hetzelfde.

Het gebeurt omdat de trigger in de ene sessie werd toegevoegd en de applicatiecode in een andere, en geen van beide van de ander wist. De symptomen zijn dubbele rijen, verdubbelde tellers, twee e-mails, of een auditlog met elke regel twee keer.

Ze vinden is mechanisch. Zoek voor elke trigger in de applicatie naar code die hetzelfde werk doet. Bepaal dan welke blijft — meestal de applicatie, tenzij de regel moet gelden voor data die via andere routes binnenkomt — en verwijder de andere in plaats van beide te laten staan met een voorwaarde die ze uit elkaars vaarwater houdt. Zulke voorwaarden zijn precies hoe de situatie verwarrend werd.

## Bewaar Ze in Migraties

Functies en triggers die zijn aangemaakt door in de SQL-editor van Supabase te typen, bestaan alleen in die database. Ze staan niet in uw repository, ze zullen niet in een nieuwe omgeving staan, en een herstel vanuit een back-up bevat misschien wel of misschien niet de versie die u verwachtte.

Alles hoort in migratiebestanden, ingecheckt, op dezelfde manier toegepast op staging en productie. Voor logica die nu alleen in het dashboard bestaat: exporteer de definities en commit ze als basismigratie — een uur werk dat een ongedocumenteerde database omzet in een reproduceerbare.

Dit maakt ook de rest van dit artikel mogelijk. U kunt niet beoordelen wat u niet kunt lezen, en een schema dat alleen in een gehost dashboard bestaat, is een schema dat niemand beoordeelt.

## Iets Testen Wat U Niet Stap voor Stap Kunt Volgen

Databaselogica is lastiger te debuggen dan applicatiecode, omdat er geen voor de hand liggende plek is om haar te zien draaien. Twee technieken dekken het meeste.

Schrijf de test als SQL: voeg een rij in en controleer dan of de resulterende toestand is wat u verwachtte. Voer hem uit tegen een kladdatabase als onderdeel van uw migraties. Het is minder elegant dan een testframework en het vangt op waar het om gaat: of de trigger vuurt en wat hij achterlaat.

En gebruik tijdens de ontwikkeling spaarzaam de eigen logging van Postgres binnen functies, en verwijder die daarna. Een functie die bij elke insert meldingen uitstuurt, is een functie die uw productielogs onleesbaar maakt.

## Constraints Zijn het Goedkoopste Wat U Ooit Zult Schrijven

Neemt u één gewoonte mee uit dit artikel, neem dan deze: druk de regels over geldige data uit als constraints in plaats van als controles in applicatiecode.

Een unieke constraint op een e-mailadres binnen een organisatie. Een check dat een percentage tussen nul en honderd ligt. Een foreign key die weigert te verwijzen naar een rij die niet bestaat. Een not-null op de kolommen waar uw product echt niet zonder kan. Elk is één regel en elk is permanent.

De reden dat dit in een door AI gebouwd product meer telt dan elders, is dat uw applicatiecode voortdurend en onvoorspelbaar verandert. Een validatie die in maart in een component werd geschreven, kan verdwijnen in een refactor in augustus die niemand heeft gecontroleerd, en geen test merkt het, omdat de test uit dezelfde code werd gegenereerd. Een databaseconstraint overleeft elke herschrijving, elk nieuw endpoint, elk importscript en elke sessie waarin een agent besloot uw formulieren te herstructureren.

Het bezwaar is dat schendingen van constraints lelijke foutmeldingen opleveren. Dat klopt en het is een presentatieprobleem: vang de specifieke schending af en toon een verstandige melding. Het alternatief — tolerante data en validatie die alleen bestaat waar iemand eraan dacht — is hoe een product rijen verzamelt waar zijn eigen code niet mee om kan gaan.

## Dit Inrichten

Voor een bestaand Supabase-project kost dit één tot twee dagen: elke functie en trigger opgesomd en beschreven, duplicaten tussen database en applicatie in één richting opgelost, alles wat externe aanroepen doet verplaatst naar applicatiecode, constraints en triggers voor afgeleide waarden behouden en gedocumenteerd, security definer-functies beoordeeld met expliciete autorisatiecontroles en zoekpaden, dode logica verwijderd, alles vastgelegd in migraties en gecommit, en een korte notitie in de repository die uitlegt wat de database zelf doet, zodat de volgende persoon niet verrast wordt.

LaunchStudio doet dit als onderdeel van het overnemen of verstevigen van een door AI gebouwde codebase, en meestal zit daar het onverklaarde gedrag. De engineers zijn van Manifera — elf jaar Postgres in productie, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons wat uw database doet dat uw code niet noemt](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### De Trigger Die Twee Keer Mailde

Marnix Oosterveld runt Offerteroute, gebouwd met Lovable en een jaar lang uitgebreid door AI-sessies: offertebeheer voor keuken- en badkamerinstallateurs, 61 bedrijven, zo'n 900 offertes per maand.

Installateurs klaagden dat klanten twee exemplaren van elke offerte ontvingen, soms minuten na elkaar en soms uren. Twee klanten hadden op beide geantwoord, wat dubbele opvolging opleverde en één discussie over een prijs die tussen de versies was veranderd.

De applicatie verstuurde een offertemail wanneer een offerte als verzonden werd gemarkeerd. Dat deed ook een trigger op de offertetabel, acht maanden eerder geschreven, die vuurde bij elke update waarbij de statuskolom veranderde — inclusief de nachtelijke taak die vervaldatums bijwerkte, wat verklaart waarom sommige duplicaten om drie uur 's nachts binnenkwamen.

De review vond meer. In totaal elf triggers: vier die tijdstempels en tellers correct bijhielden, twee die applicatielogica dupliceerden, één die een externe webhook aanriep binnen een transactie en drie time-outs had veroorzaakt, drie die niets deden omdat hun doeltabellen waren vervangen, en één security definer-functie die offertes ophaalde zonder enige autorisatiecontrole, aan te roepen door elke geauthenticeerde gebruiker voor de data van elk bedrijf.

Drie werkdagen: elke functie en trigger geïnventariseerd en beschreven; de e-mailtrigger en de webhooktrigger verwijderd, met het werk verplaatst naar de applicatie waar het opnieuw kan worden geprobeerd en gelogd; de paren met dubbele logica opgelost; drie dode triggers verwijderd; de security definer-functie herschreven met een expliciete lidmaatschapscontrole en een vast zoekpad; de triggers voor tijdstempels en tellers behouden, gedocumenteerd en gedekt door SQL-tests; en het hele schema — inclusief functies en triggers — geëxporteerd naar een basismigratie en gecommit, ter vervanging van een database die alleen in het dashboard bestond.

**Resultaat:** de dubbele e-mails hielden op, de af en toe optredende time-outs verdwenen mee, en de blootgestelde functie werd gedicht voordat iemand haar had gebruikt. Marnix heeft nu een document van twee pagina's dat beschrijft wat zijn database uit zichzelf doet, wat volgens hem de eerste keer is sinds maand drie dat hij het gedrag van zijn eigen product begrijpt.

> *"Niets in mijn code verstuurde een tweede e-mail. Het kostte een middag om te accepteren dat de database het zelf deed, omdat ik erom had gevraagd, in een chat die ik me niet herinner."*
> — **Marnix Oosterveld, Oprichter, Offerteroute (Waalwijk)**

**Kosten & Doorlooptijd:** €2.700 (inventarisatie van het schema, review van triggers en functies, oplossen van duplicaten, externe aanroepen naar applicatiecode verplaatst, herstel van security definer, SQL-tests, basismigratie) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Zijn databasetriggers een slecht idee in Supabase?

Nee — voor constraints, afgeleide waarden en atomaire handelingen over meerdere tabellen zijn ze de betere plek. Het probleem is onzichtbaarheid: logica in de database die nergens in uw code wordt genoemd.

### Moet een trigger een e-mail versturen of een webhook aanroepen?

Nee. Externe aanroepen binnen een transactie kunnen niet worden teruggedraaid, maken schrijfacties traag, en komen naar boven als databasefouten. De database mag de database veranderen; alles wat de buitenwereld raakt, hoort in applicatiecode.

### Wat is het risico van security definer-functies?

Ze draaien met verhoogde rechten en omzeilen dus row-level security. Gebruik ze alleen met een genoemde reden, controleer de autorisatie van de aanroeper binnen de functie, en stel altijd een expliciet zoekpad in.

### Hoe vind ik welke triggers er al bestaan?

Maak er een lijst van in het Supabase-dashboard en lees elke definitie, met één zin over wat ze doet en wat haar activeert. In een door AI gebouwd project van een jaar oud kost dit een uur en verklaart het meestal minstens één mysterie.

### Waarom moeten mijn functies in migratiebestanden staan?

Omdat logica die in de SQL-editor is aangemaakt in maar één database bestaat. Ze zal niet in een nieuwe omgeving staan, overleeft misschien geen herstel, en kan niet worden beoordeeld door iemand die uw repository leest.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zijn databasetriggers een slecht idee in Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — constraints, afgeleide waarden en atomaire handelingen over meerdere tabellen horen daar. Het gevaar is logica die uw applicatiecode nooit noemt."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een trigger een e-mail versturen of een webhook aanroepen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Externe aanroepen kunnen niet met de transactie worden teruggedraaid, vertragen elke schrijfactie, en verschijnen als databasefouten. Houd ze in applicatiecode."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het risico van security definer-functies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze omzeilen row-level security. Gebruik ze bewust, controleer de autorisatie van de aanroeper binnen de functie, en stel een expliciet zoekpad in."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vind ik welke triggers er al bestaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maak er een lijst van in het Supabase-dashboard en beschrijf elk in één zin. In een door AI gebouwd project van een jaar oud verklaart dit meestal minstens één mysterie."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom moeten databasefuncties in migratiebestanden staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Logica die in de SQL-editor is aangemaakt, bestaat in die ene database — afwezig in nieuwe omgevingen, onzeker na een herstel, en onzichtbaar in uw repository."
      }
    }
  ]
}
</script>
