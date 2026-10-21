---
Titel: "Codereview in Cursor: Opvangen Wat Autocomplete Fout Deed"
Trefwoorden: cursor codereview, AI-code reviewen, diffs, plausibele fouten, zelfreview, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Codereview in Cursor: Opvangen Wat Autocomplete Fout Deed

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Codereview in Cursor: Opvangen Wat Autocomplete Fout Deed",
  "description": "Door AI geschreven code is op een kenmerkende manier fout: plausibel in plaats van zichtbaar kapot. Waar u op let, hoe u uw eigen werk reviewt als er niemand anders is, en de vijf categorieën die u elke keer controleert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-code-review-catching-what-autocomplete-got-wrong" }
}
</script>

Code reviewen die door een mens is geschreven, betekent zoeken naar fouten van iemand die het probleem begreep en iets verkeerd deed. Code reviewen die door een model is geschreven, is een andere oefening, omdat het werk oplevert dat vloeiend, idiomatisch en zelfverzekerd is, en fout op manieren die er niet uitzien als fouten.

Een mens die een functie schrijft die hij niet begrijpt, levert iets op dat zichtbaar onzeker is. Een model levert iets op dat er precies uitziet als code van iemand die het wist. Dat is de hele moeilijkheid, en daarom vraagt het reviewen van door AI geschreven code een ander soort aandacht in plaats van meer van hetzelfde.

## De Kenmerkende Fouten

Vijf categorieën verklaren het meeste van wat erdoor glipt.

**Subtiel verkeerde logica.** Een off-by-one, een grens uitgesloten die erbij had moeten horen, een conditie omgedraaid in een tak die niemand uitvoert. De code leest correct; ze berekent iets dat net iets anders is dan u wilde.

**Verzonnen interfaces.** Een methode die niet bestaat op dat object, een parameter die de bibliotheek niet accepteert, een veld dat de API niet teruggeeft. Meestal direct opgevangen door een compiler of een test, en niet altijd — een veld uit een response dat simpelweg undefined is, levert een pagina op die niets toont in plaats van een fout.

**Alleen correct voor het gelukkige pad.** Geen afhandeling van het lege geval, de mislukking, de ontbrekende rechten of de time-out. Dit is in volume de meest voorkomende categorie.

**De codebase negeren.** Een nieuwe manier om iets te doen waarvoor al een manier bestond, omdat het model een algemeen patroon imiteerde in plaats van het uwe.

**Weglatingen in beveiliging.** Die waar deze reeks steeds op terugkomt: ontbrekende autorisatie, afwezige validatie, onbegrensde queries. Niet aanwezig omdat niemand erom vroeg.

## Lees de Diff, Niet het Resultaat

De belangrijkste gewoonte is kijken naar wat er veranderde in plaats van naar het afgewerkte bestand.

Een assistent die wordt gevraagd een functie toe te voegen, raakt vaak meer aan dan nodig: een opnieuw opgemaakt blok, een hernoemde variabele, een gewijzigde standaardwaarde, een verwijderde import. Het resulterende bestand lezen maakt dat allemaal onzichtbaar, omdat het er allemaal uitziet als redelijke code. De diff lezen maakt het duidelijk.

Dus: maak één wijziging tegelijk, kijk naar de diff voordat u accepteert, en wees achterdochtig bij elke wijziging die groter is dan het verzoek rechtvaardigde. Een verzoek om een knop toe te voegen dat elf bestanden wijzigt, is een verzoek dat ook iets anders deed.

## Vraag Wat Er Gebeurt Als Het Leeg Is

Hebt u per wijziging tijd voor precies één vraag, stel dan deze: wat gebeurt er als er niets is?

Een lege lijst, een ontbrekend record, een leeg veld, een gebruiker zonder organisatie, een account dat voor het eerst inlogt. Gegenereerde code is geschreven voor het geval dat data bestaat, en de mislukking wanneer dat niet zo is, varieert van een leeg scherm tot een exception bij het eerste bezoek van een klant — wat het slechtst denkbare moment is.

De tweede vraag, als er tijd is: wat gebeurt er als het mislukt? Het verzoek geeft een fout, de dienst is traag, de rechten worden geweigerd. Gegenereerde code vangt fouten af en doet er vaak niets nuttigs mee.

## Review de Dingen Die Niet Ongedaan Kunnen Worden

Niet elke wijziging verdient dezelfde aandacht, en de eerlijke verdeling voor een oprichter die alleen werkt, is goed kijken naar een kleine set.

Alles wat met geld te maken heeft. Alles wat met rechten of autorisatie te maken heeft. Alles wat verwijdert of overschrijft. Alles wat iets naar een klant stuurt. Alles wat het databaseschema wijzigt.

Die vijf categorieën zijn waar een fout duur of onomkeerbaar is. Al het andere — een layoutwijziging, een nieuw weergaveveld, een tekstaanpassing — is te controleren door naar het product te kijken.

Dit is ook de verdeling om een assistent mee te geven wanneer u die vraagt te reviewen: wijs hem op de wijziging en vraag specifiek naar autorisatie, naar de foutpaden, naar of dit overeenkomt met hoe de rest van de codebase het doet. Open vragen leveren algemene antwoorden op; specifieke vragen leveren bruikbare op.

## Gebruik de Tool om de Tool te Reviewen, Voorzichtig

Een model vragen code te reviewen is echt nuttig en heeft een specifieke beperking: het is goed in het vinden van wat aanwezig en fout is, en slecht in het opmerken van wat ontbreekt.

Het zal u dus vertellen dat een variabele ongebruikt is of een conditie overbodig. Het zal u minder betrouwbaar vertellen dat geen enkel endpoint in dit bestand controleert wie het vraagt, omdat niets aan de code er onjuist uitziet — de afwezigheid is alleen zichtbaar tegen een verwachting die het model niet kreeg.

Het productieve patroon is de verwachting meegeven. "Controleert dit endpoint of de vragende gebruiker hoort bij de organisatie die eigenaar is van dit record?" is een vraag met een controleerbaar antwoord. "Review dit bestand" is een verzoek om een mening.

Houd uw eigen checklist van de vijf categorieën hierboven bij, en loop die af. De tool is snel in antwoorden; de lijst zorgt dat de vragen de juiste zijn.

## Reviewen Als U de Code Niet Kunt Lezen

Een aanzienlijk deel van de oprichters die deze tools gebruiken, kan de code niet met vertrouwen lezen, en het advies hierboven gaat ervan uit dat ze dat wel kunnen. Er is een versie voor alle anderen, en die is effectiever dan ze klinkt.

**Review in plaats daarvan het gedrag, systematisch.** Werk na een wijziging een geschreven lijst af: het ding dat veranderde, het ding ernaast, en de hoofdflow van het product van begin tot eind. Opgeschreven en elke keer op dezelfde manier gedaan, vangt dit de meeste functionele regressies op.

**Vraag de assistent de wijziging in gewone taal uit te leggen**, en controleer of de uitleg overeenkomt met wat u vroeg. Een beschrijving die bestanden of gedrag noemt die u niet verwachtte, is het signaal — u hoeft de code niet te lezen om op te merken dat het antwoord iets bevat waar u nooit om vroeg.

**Vraag specifiek naar de vijf categorieën.** Raakte deze wijziging iets aan dat met rechten te maken heeft? Verwerkt iets hier geld? Wijzigde dit de databasestructuur? Dit zijn vragen met een ja of nee als antwoord, en een ja betekent een second opinion halen voordat u deployt.

**Gebruik de tests als uw leeswerk.** Een testsuite die autorisatie, geld en de hoofdflow dekt, is een reviewer die werkt of u de diff nu kunt lezen of niet, en dat is het sterkste argument voor het schrijven van de dertig tests die elders in deze reeks worden beschreven.

En gebruik branches. Werk dat kan worden weggegooid, is werk waarover u niet zeker hoeft te zijn, en dat verlaagt de kosten van ongelijk hebben meer dan welke reviewpraktijk ook.

## Houd de Wijzigingen Klein Genoeg om te Reviewen

Alles hierboven wordt makkelijker of onmogelijk afhankelijk van één variabele: hoeveel er in één keer veranderde.

Een wijziging die twee bestanden raakt, is in een minuut te lezen. Een wijziging die er twintig raakt, kan door niemand zinvol worden gelezen, en wat er in de praktijk gebeurt, is dat ze wordt doorgebladerd en geaccepteerd — wat hetzelfde is als niet reviewen, met als extra kosten dat u gelooft dat u het wel deed.

Drie gewoonten houden wijzigingen reviewbaar.

**Vraag om één ding.** Niet "verbeter de factuurpagina" maar "voeg een bevestigingsdialoog toe aan de verwijderknop op de factuurregel". Het smallere verzoek levert een kleinere diff op en, los daarvan, een beter resultaat.

**Commit op elk werkend punt.** Een commit is een checkpoint waarnaar u kunt terugkeren, en een reeks kleine commits is een verhaal dat u later kunt lezen. In een codebase waarin veel van het schrijven door een tool is gedaan, is die geschiedenis de enige verklaring van waarom dingen zijn zoals ze zijn.

**Scheid refactoring van gedragswijziging.** Een commit die code verplaatst en een commit die verandert wat ze doet, zijn allebei reviewbaar; één commit die beide doet is dat niet, omdat elk verschil het een of het ander kan zijn.

Dit is gewone engineeringdiscipline, en ze doet er hier meer toe dan gewoonlijk om een specifieke reden: de tool levert met plezier een grote wijziging op, snel, en de kosten van accepteren worden uitgesteld. De discipline is wat snelheid omzet in vooruitgang in plaats van in een codebase die niemand heeft gelezen.

## Dit Inrichten

Voor een oprichter die alleen werkt, is dit een gewoonte in plaats van een project: één wijziging tegelijk met de diff gelezen vóór accepteren, wijzigingen die groter zijn dan het verzoek als verdacht behandeld, bij elke wijziging gevraagd naar het lege geval en het foutgeval, grondige review voorbehouden aan geld, rechten, verwijderen, uitgaande communicatie en schema, een geschreven checklist van de vijf foutcategorieën, specifieke in plaats van open vragen wanneer u een assistent laat reviewen, en versiebeheer zodat alles wat onduidelijk is kan worden teruggedraaid in plaats van beredeneerd.

LaunchStudio doet dit als dienst voor oprichters die een tweede lezer willen op de wijzigingen die ertoe doen. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Stuur ons een week aan wijzigingen](https://launchstudio.eu/nl/#contact) en wij vertellen u welke we zouden hebben tegengehouden.

## Echt voorbeeld

### Een Omgedraaide Conditie in een Tak Die Niemand Uitvoerde

Dennis Vermaat bouwde Sleutelbeheer in Cursor: sleutel- en toegangsbeheer voor vastgoedbeheerders en woningcorporaties, dat bijhoudt wie welke sleutel van welk gebouw heeft, gebruikt door 17 organisaties.

Hij vroeg om een wijziging in hoe verlopen sleuteltoewijzingen werden afgehandeld. De resulterende code was schoon, goed benoemd en las correct. Hij accepteerde haar zonder goed naar de diff te kijken, omdat de functie werkte toen hij die testte.

De wijziging had ook een niet-gerelateerde conditie in hetzelfde bestand aangepast, waardoor de controle werd omgedraaid die bepaalde of een sleutelhouder de sleutellijst van een gebouw mocht bekijken. In het pad dat hij testte — een beheerder die de eigen organisatie bekijkt — was het resultaat identiek. In het pad dat hij niet testte, kon een aannemer met beperkte toegang nu elke sleutelhouder zien voor elk gebouw dat de organisatie beheerde, inclusief privéadressen.

Het werd zeven weken later gevonden tijdens een routinereview, zonder enig bewijs dat iemand het had gebruikt.

Twee werkdagen: de conditie gecorrigeerd en een test geschreven die de rechten voor beide rollen controleert; een review van elke wijziging in die periode, die nog twee ongevraagde aanpassingen vond — een gewijzigde standaardbewaartermijn en een verwijderde import die stilletjes een validatie had uitgeschakeld; een werkwijze ingevoerd van één wijziging tegelijk met de diff gelezen vóór accepteren; een geschreven checklist die de vijf foutcategorieën dekt; geautomatiseerde tests toegevoegd voor autorisatie op de twaalf endpoints die sleuteldata blootstellen, omdat het incident een rechtenwijziging was die niets controleerde; en de discipline in versiebeheer aangescherpt zodat het werk van elke sessie een aparte branch is die kan worden weggegooid.

**Resultaat:** geen bewijs van toegang door de betrokken aannemersaccounts, bevestigd uit logs. Dennis' oordeel is dat de verandering in werkwijze meer uitmaakte dan de fix: in het jaar daarna vingen het lezen van diffs nog vier ongevraagde aanpassingen op, waarvan twee ernstige gevolgen zouden hebben gehad.

> *"Ik vroeg het om te veranderen hoe verlopen werkte. Het draaide ook een rechtencontrole in hetzelfde bestand om, en de versie die ik testte gedroeg zich identiek. De diff had me dertig seconden gekost."*
> — **Dennis Vermaat, Oprichter, Sleutelbeheer (Dordrecht)**

**Kosten & Doorlooptijd:** €2.300 (correctie van de conditie met tests, terugblikkende review van zeven weken aan wijzigingen, autorisatietestsuite over twaalf endpoints, reviewpraktijk en checklist, branchdiscipline) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Hoe verschilt het reviewen van AI-code van het reviewen van code van een mens?

Een mens die iets niet begrijpt, levert zichtbaar onzekere code op. Een model levert vloeiende, idiomatische code op die zelfverzekerd fout is, dus u controleert op juistheid in plaats van te zoeken naar tekenen van twijfel.

### Wat is de nuttigste gewoonte?

Lees de diff in plaats van het afgewerkte bestand, één wijziging tegelijk. Ongevraagde aanpassingen zijn onzichtbaar in het resultaat en duidelijk in de diff.

### Wat moet ik bij elke wijziging controleren?

Wat er gebeurt als er niets is — een lege lijst, een ontbrekend record, een nieuwe gebruiker — en wat er gebeurt als het mislukt. Gegenereerde code is geschreven voor het geval dat data bestaat en verzoeken slagen.

### Welke wijzigingen verdienen echte aandacht?

Geld, rechten, verwijderen, alles wat naar een klant gaat, en schemawijzigingen. Al het andere is te controleren door het product te gebruiken.

### Kan ik de assistent zijn eigen code laten reviewen?

Nuttig, als u specifieke vragen stelt. Hij vindt wat aanwezig en fout is, en mist wat ontbreekt — vraag dus "controleert dit de autorisatie" in plaats van "review dit".

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe verschilt het reviewen van AI-code van menselijke code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Modellen leveren vloeiende, zelfverzekerde code op die subtiel fout is, zonder de zichtbare onzekerheid die een mens toont als die iets niet beheerst."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de nuttigste reviewgewoonte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lees de diff, één wijziging tegelijk. Ongevraagde aanpassingen zijn onzichtbaar in het afgewerkte bestand en duidelijk in de diff."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet bij elke door AI geschreven wijziging worden gecontroleerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het lege geval en het foutgeval — gegenereerde code is geschreven voor data die bestaat en verzoeken die slagen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke wijzigingen verdienen een grondige review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geld, rechten, verwijderen, uitgaande communicatie en schemawijzigingen — waar fouten duur of onomkeerbaar zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een assistent zijn eigen uitvoer reviewen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nuttig met specifieke vragen. Hij vindt aanwezige fouten en mist afwezigheden, dus vraag expliciet naar autorisatie in plaats van om een algemene review."
      }
    }
  ]
}
</script>
