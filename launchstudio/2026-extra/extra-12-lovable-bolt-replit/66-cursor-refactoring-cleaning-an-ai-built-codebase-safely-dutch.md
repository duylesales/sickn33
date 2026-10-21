---
Titel: "Refactoren in Cursor: Een AI-Gebouwde Codebase Veilig Opschonen"
Trefwoorden: cursor refactoring, veilig refactoren, technische schuld, stapsgewijs opschonen, AI-codebase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Refactoren in Cursor: Een AI-Gebouwde Codebase Veilig Opschonen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Refactoren in Cursor: Een AI-Gebouwde Codebase Veilig Opschonen",
  "description": "Een AI-gebouwd project opschonen is makkelijk te beginnen en makkelijk te verpesten. Wat u verandert en in welke volgorde, hoe u het doet zonder een werkend product te breken, en wanneer u het beter laat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-refactoring-cleaning-an-ai-built-codebase-safely" }
}
</script>

Er komt een moment bij een AI-gebouwd product waarop wijzigingen langer gaan duren dan zou moeten. Een kleine functie raakt vijf bestanden. Een bugfix breekt iets dat er niets mee te maken heeft. U vermijdt een bepaald deel omdat u niet zeker weet wat ervan afhangt.

Dat is het signaal om op te schonen, en het instinct dat volgt is het gevaarlijke: een week vrijmaken om alles in één keer op te lossen, en zo wordt een werkend product een kapot product zonder duidelijke weg terug.

Een AI-gebouwde codebase refactoren is goed te doen. Het vraagt een andere aanpak dan een herschrijving, en het verschil zit vooral in de omvang.

## Zorg Eerst voor een Vangnet

Doe niets totdat u kunt zien of u iets hebt gebroken.

Voor een product met tests: draai ze en bevestig dat ze slagen. Voor een product zonder: schrijf eerst de kleine set die elders in deze reeks wordt beschreven — autorisatie, geld, de hoofdflow — omdat refactoren zonder enige controle een reeks wijzigingen is waarvan u de juistheid uit uw geheugen beweert.

Is eerst tests schrijven echt niet mogelijk, dan is het minimum een geschreven lijst van wat u moet aanklikken, doorlopen vóór en na elke wijziging. Het is trager en het is niet niets.

En werk in branches, zodat elke wijziging kan worden weggegooid in plaats van uitgeplozen.

## Wijzig Structuur of Gedrag, Nooit Allebei

De regel die refactoren veilig maakt: een wijziging verplaatst code zonder te veranderen wat ze doet, of verandert wat ze doet zonder haar te verplaatsen. Nooit één commit die beide doet.

De reden is diagnostisch. Gaat er iets kapot na een pure herstructurering, dan is de herstructurering de oorzaak. Gaat er iets kapot na een gedragswijziging, dan is de wijziging de oorzaak. Deed een commit beide, dan kan de oorzaak overal in zitten, en het onderzoek kost een middag.

Zo instrueert u ook een assistent. "Haal deze berekening eruit naar een functie en roep die vanaf beide plekken aan, zonder iets te veranderen aan wat ze berekent" is een taak met een controleerbare uitkomst. "Ruim dit bestand op" is een verzoek dat meerdere dingen tegelijk zal doen.

## De Volgorde Die Loont

Voor een typisch AI-gebouwd project, de volgorde met het beste rendement.

**Eerst verwijderen.** Ongebruikte componenten, dode endpoints, verlaten tabellen, ongebruikte dependencies. Verwijderen is de enige refactoring die geen bug kan introduceren in code die u houdt, het maakt al het andere kleiner, en het neemt vaak een beveiligingsrisico weg — een onafgemaakt endpoint zonder autorisatie.

**Voeg duplicatie samen in de dingen die ertoe doen.** Geld, datums, rechten, datatoegang. Niet elk herhaald fragment; die waarbij een wijziging die op drie van vier kopieën wordt toegepast een echt defect is.

**Splits de grootste bestanden** op verantwoordelijkheid. Datatoegang, logica, presentatie. De grootste drie of vier bestanden zijn waar de moeilijkheid zich concentreert.

**Breng concurrerende conventies samen.** Twee manieren om data op te halen, twee benaderingen van state. Kies er één en pas die toe op wat u aanraakt in plaats van overal tegelijk.

**Dan naamgeving**, die ertoe doet en als laatste komt omdat ze het minst gevaarlijk en het minst urgent is.

## Refactor Wat U Toch Al Aanraakt

De strategie die werkt voor een product met klanten is geen opschoonproject. Het is een regel: wanneer u een deel verandert, laat het dan beter achter dan u het aantrof, in een aparte commit.

Een functie in de factuurcode wordt twee commits — één die opruimt, één die de functie toevoegt. In zes maanden worden de delen van het product waaraan u werkt schoon en blijven de delen die u nooit aanraakt zoals ze zijn, en dat is de juiste verdeling, omdat onaangeraakte code u niets kost.

Dit is ook de enige versie van opschonen die het contact met een bedrijf overleeft. Een week vrijgemaakt voor refactoring is een week waarin het product niet verbetert, en het is het eerste wat wordt opgeofferd wanneer een klant iets nodig heeft.

## Weet Wanneer U Het Moet Laten

Drie situaties waarin opschonen niet de juiste besteding van de tijd is.

**Code die u nooit aanraakt.** Lelijk, werkend en stabiel is prima. De kosten van slechte code worden alleen betaald wanneer u haar verandert.

**Een functie die u binnenkort verwijdert.** Voor de hand liggend en vaak vergeten.

**Voordat u weet dat het product klopt.** Een prototype refactoren naar een elegante structuur voordat u weet of iemand het wil, is iets oppoetsen dat misschien wordt verwijderd. Lever op, zoek het uit, en schoon dan op wat overleeft.

Het gevolg: de delen die het opschonen waard zijn, zijn de delen die u vaak verandert, en die kunt u uit uw eigen commitgeschiedenis halen in plaats van op gevoel.

## De Assistent Sturen Zonder de Controle te Verliezen

Een AI-editor is echt goed in refactoren — beter dan in de meeste dingen, omdat de transformaties mechanisch zijn en goed vertegenwoordigd in alles wat hij heeft geleerd. De moeilijkheid is de omvang.

Drie instructies die goed werken, elk met een wijziging die u kunt lezen.

**"Haal dit eruit naar een functie en roep die vanaf beide plekken aan, zonder iets aan het resultaat te veranderen."** Afgebakend, controleerbaar, en de meest voorkomende nuttige refactoring.

**"Splits dit bestand in datatoegang, bedrijfslogica en presentatie, met behoud van gedrag."** Groter, en nog steeds controleerbaar omdat de testsuite ongewijzigd moet slagen.

**"Vind elke plek waar deze berekening is gedupliceerd."** Analyse in plaats van wijziging, en een van de waardevolste dingen om te vragen, omdat het antwoord vaak meer plekken is dan u verwachtte.

Drie die slecht aflopen. "Ruim dit op", wat meerdere dingen tegelijk doet. "Maak dit beter", wat uitnodigt tot smaak. En "refactor het hele project", het verzoek achter de meeste rampen op dit gebied.

Nog één gewoonte: draai na elke refactoring eerst de tests voordat u de code leest. Een slagende suite vertelt u dat het gedrag behouden is, en dat is wat er wordt beweerd. Lees daarna de diff om te bevestigen dat hij deed wat u vroeg en niets anders — de twee controles vangen verschillende dingen op, en de tweede is waar ongevraagde wijzigingen worden gevonden.

## De Schuld Die U Mag Houden

Niet alle rommeligheid is schuld, en het onderscheid bepaalt waar de moeite heen gaat.

Schuld is iets dat toekomstig werk trager of riskanter maakt. Vijf kopieën van een rechtencontrole is schuld: een wijziging zal er een missen. Een bestand van 900 regels dat u wekelijks bewerkt, is schuld. Twee conventies voor het ophalen van data is schuld, omdat elke wijziging begint met een beslissing.

Rommeligheid is iets dat alleen stoort. Een omslachtige variabelenaam. Een component dat anders is opgebouwd dan u het zou hebben gedaan. Een ouder idioom dat nog werkt. Niets daarvan kost iets totdat u die code aanraakt, en het meeste zult u nooit aanraken.

De bruikbare toets: zou dit de volgende wijziging trager maken of de kans vergroten dat er iets breekt? Zo niet, laat het dan.

Dit doet ertoe omdat oprichters die over technische schuld lezen, elke onvolkomenheid als verplichting gaan zien, en dan ofwel weken aan cosmetica besteden, ofwel verlamd raken door een codebase die ze onherstelbaar vinden. Geen van beide is terecht. De meeste AI-gebouwde producten hebben vier of vijf echte problemen — duplicatie in de logica die ertoe doet, een handvol te grote bestanden, dode code, concurrerende conventies en ontbrekende foutafhandeling — en al het andere op de lijst is decoratie.

Los de vijf op. Negeer de rest totdat het geen decoratie meer is.

## Meet of Het Hielp

Refactoren wordt ongewoon vaak op vertrouwen gedaan, en een beetje bewijs houdt het eerlijk.

Twee signalen zijn voor elke oprichter beschikbaar zonder instrumentatie.

**Hoe lang een vergelijkbare wijziging duurt.** Kostte een veld toevoegen aan een formulier in maart een uur en in juli twintig minuten, dan werkt het opschonen. Kost het nog steeds een uur, dan waren de delen die u opschoonde niet de delen die traag waren.

**Of wijzigingen nog steeds niet-gerelateerde dingen breken.** Hoe vaak "ik loste één ding op en iets anders hield op met werken" voorkomt, is de duidelijkste indicator van of de structurele problemen echt zijn aangepakt, en het is iets dat u merkt zonder te meten.

Een derde, als u iets bijhoudt: het aantal bestanden dat een typische wijziging raakt. Het daalt wanneer duplicatie wordt samengevoegd en stijgt wanneer dat niet gebeurt, en het is zichtbaar in uw eigen commitgeschiedenis.

Niets hiervan hoeft streng te zijn. Het moet bestaan, omdat de faalwijze van opschoonwerk is dat tijd wordt besteed aan de delen die makkelijk te herkennen waren in plaats van de delen die iets kostten — en de enige manier om dat te merken is controleren of de pijn verdween.

## Dit Inrichten

Voor een bestaand product is dit doorgaans doorlopend in plaats van een project: eerst een testvangnet opgezet, werken in branches, structuur en gedrag in aparte commits gewijzigd, eerst verwijderen — ongebruikte code, endpoints, tabellen en dependencies, met blootstelling gecontroleerd vóór verwijdering — daarna samenvoegen van duplicatie in geld, datums, rechten en datatoegang, dan de grootste bestanden gesplitst op verantwoordelijkheid, dan conventies samengebracht voor wat u aanraakt, en een vaste regel dat elk deel waarin u werkt in een eigen commit wordt opgeruimd.

LaunchStudio doet de eerste ronde bij het overnemen van een AI-gebouwd product, wat meestal één tot drie dagen is en alles daarna goedkoper maakt. De engineers zijn van Manifera — elf jaar, 120+ engineers, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons welke delen van uw codebase het opschonen waard zijn](https://launchstudio.eu/nl/#contact). Meestal zijn het er minder dan u denkt.

## Echt voorbeeld

### Een Week Die Bijna een Product Beëindigde

Bram Terlouw bouwde Wagenparkbeheer in Cursor: wagenparkadministratie voor bedrijven met bestelbussen en servicevoertuigen — onderhoud, keuringen, brandstof en chauffeurstoewijzing — gebruikt door 34 bedrijven met samen 1.900 voertuigen.

Na achttien maanden waren wijzigingen traag genoeg geworden om frustrerend te zijn. Hij maakte een week vrij en vroeg de assistent het project grondig te herstructureren.

Woensdag werkte het product niet meer. De herstructurering had het grootste deel van de codebase verplaatst, onderweg verschillende gedragingen veranderd, en was vastgelegd in vier enorme commits zonder tests die zeiden wat er kapot was. Terugdraaien betekende drie dagen werk verliezen, inclusief twee echte fixes. Hij besteedde donderdag en vrijdag aan het vinden van problemen door te klikken, en deployde de dinsdag erna met drie defecten die klanten in de twee weken daarna vonden — waarvan één onderhoudsrecords aan het verkeerde voertuig koppelde.

Vier werkdagen herstel en een andere aanpak: de branch opgegeven en de productieversie hersteld; eerst een testvangnet geschreven voor autorisatie over 26 endpoints, de onderhouds- en keuringsberekeningen, en een end-to-end-flow; verwijderen als eigen ronde, met 19 ongebruikte componenten, 7 dode endpoints — waarvan twee zonder authenticatie — en 4 verlaten tabellen weg; duplicatie alleen samengevoegd waar het ertoe deed, namelijk de berekening van de keuringsvervaldatum die op vijf plekken voorkwam in twee varianten; de drie grootste bestanden gesplitst; structuur en gedrag overal in aparte commits; en een vaste regel ingevoerd dat opschonen gebeurt in het deel waaraan wordt gewerkt, in een eigen commit, in plaats van als project.

**Resultaat:** dezelfde opschoning werd in de drie maanden daarna afgerond zonder één incident dat klanten zagen, naast het normale functiewerk. Brams oordeel is dat de vier verloren dagen volledig kwamen doordat hij geen manier had om te zien wat hij had gebroken.

> *"Ik vroeg het om het project te herstructureren en het deed precies dat. Woensdag werkte er niets meer, en ik had geen tests, één gigantische commit en drie dagen aan wijzigingen die ik niet van elkaar kon scheiden."*
> — **Bram Terlouw, Oprichter, Wagenparkbeheer (Zwolle)**

**Kosten & Doorlooptijd:** €3.600 (herstel en terugzetten, testvangnet over 26 endpoints en kernberekeningen, gefaseerd verwijderen met controles op blootstelling, gericht samenvoegen van duplicatie, bestanden splitsen, commitdiscipline en doorlopende opschoonpraktijk) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Wat heb ik nodig voordat ik ga refactoren?

Een manier om te zien of u iets hebt gebroken: een kleine testsuite voor autorisatie, geld en de hoofdflow, of minimaal een geschreven lijst van wat u moet aanklikken. En branches, zodat alles kan worden weggegooid.

### Waarom structuurwijzigingen scheiden van gedragswijzigingen?

Omdat wanneer er iets breekt, de oorzaak het soort wijziging is dat u net deed. Een commit die code verplaatst en verandert, laat u alles erin onderzoeken.

### Wat moet als eerste worden opgeschoond?

Verwijderen — ongebruikte componenten, endpoints, tabellen en dependencies. Het kan geen code breken die u houdt, het maakt al het andere kleiner, en het dicht vaak een beveiligingslek.

### Moet ik een week vrijmaken voor opschonen?

Nee. Schoon het deel op waarin u werkt, in een eigen commit, terwijl u bezig bent. Een opschoonweek is het eerste wat wordt opgeofferd wanneer een klant iets nodig heeft, en levert de grootste niet-reviewbare wijzigingen op.

### Is er code die het opschonen niet waard is?

Ja — alles wat u nooit aanraakt, alles wat u binnenkort verwijdert, en alles in een product waarvan de vorm nog niet vastligt. De kosten van rommelige code worden alleen betaald wanneer u haar verandert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is nodig voordat u een AI-gebouwde codebase refactort?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een vangnet — een kleine testsuite voor autorisatie, geld en de hoofdflow, of een geschreven kliklijst — plus branches."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom structurele en gedragswijzigingen scheiden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodat de oorzaak herkenbaar is wanneer er iets breekt. Een commit die beide doet, maakt de hele wijziging verdacht."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet als eerste worden opgeschoond?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het verwijderen van ongebruikte componenten, endpoints, tabellen en dependencies — dat kan behouden code niet breken en dicht vaak een lek."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik een week aan refactoren besteden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Ruim het deel op waarin u al werkt, in een eigen commit. Opschoonweken leveren enorme niet-reviewbare wijzigingen op en worden opgegeven."
      }
    },
    {
      "@type": "Question",
      "name": "Is sommige code het opschonen niet waard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — code die u nooit aanraakt, code die binnenkort wordt verwijderd, en elk product waarvan de vorm nog niet vastligt."
      }
    }
  ]
}
</script>
