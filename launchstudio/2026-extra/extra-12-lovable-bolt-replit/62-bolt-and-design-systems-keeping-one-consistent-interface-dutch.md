---
Titel: "Bolt en Design Systems: Eén Consistente Interface Behouden"
Trefwoorden: bolt design system, consistente UI, componentenbibliotheek, design tokens, AI-gegenereerde interfaces, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Bolt en Design Systems: Eén Consistente Interface Behouden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt en Design Systems: Eén Consistente Interface Behouden",
  "description": "Elk gegenereerd scherm is aantrekkelijk en geen ervan past bij elkaar. Waarom AI-gebouwde interfaces uit elkaar drijven, het kleine systeem dat dat stopt, en hoe u de tool uw ontwerp laat volgen in plaats van er een te verzinnen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-and-design-systems-keeping-one-consistent-interface" }
}
</script>

Bekijk vijf schermen van een Bolt-applicatie die in drie maanden is gebouwd en tel de knopstijlen. Zes is gebruikelijk. De blauwtinten verschillen net iets. Sommige kaarten hebben een rand, andere een schaduw. De ruimte tussen elementen heeft op elke pagina een andere waarde.

Geen enkel scherm ziet er verkeerd uit. Samen zien ze eruit als vijf producten, en het effect op een klant is niet dat die de inconsistentie opmerkt - het is dat het product net iets onbetrouwbaar aanvoelt, op een manier die hij niet zou kunnen uitleggen als u het vroeg.

De oorzaak is structureel en daardoor op te lossen: elk scherm is in een eigen sessie gegenereerd, zonder kennis van de beslissingen die in de vorige zijn genomen.

## Consistentie Is Vertrouwen

Het is goed om helder te zijn over waarom dit commercieel uitmaakt, want "de afstanden zijn inconsistent" klinkt als de klacht van een ontwerper.

Interfaces die voorspelbaar werken zijn makkelijker in gebruik - een knop die er overal hetzelfde uitziet, herkennen mensen zonder te lezen. Interfaces die samenhangend ogen, lezen als gemaakt door iemand die oplette, en een zakelijke koper die een kleine leverancier beoordeelt, zoekt precies dat signaal. En inconsistentie stapelt zich op: zodra er zes knopstijlen zijn, kost de zevende niets om toe te voegen, en er is geen versie van de interface waarop een nieuw scherm kan aansluiten.

## Definieer Tokens Voordat U Meer Schermen Genereert

Het systeem dat dit oplost is klein. Het is een set benoemde beslissingen, één keer opgeschreven, waar alles naar verwijst.

**Kleuren.** Geen palet van veertig, maar een handvol met rollen: primair, een neutrale schaal voor tekst en achtergronden, en kleuren voor succes, waarschuwing en fout. Zes tot tien waarden.

**Afstanden.** Eén schaal, overal gebruikt. Een gebruikelijke keuze is veelvouden van vier: 4, 8, 12, 16, 24, 32, 48. Elke tussenruimte in de interface is een van die waarden en nooit een willekeurig getal.

**Typografie.** Twee of drie formaten voor koppen, één voor lopende tekst, één voor kleine tekst. Eén lettertype, twee gewichten.

**Afronding en schaduw.** Eén of twee waarden van elk.

Dat is het hele systeem voor een klein product, en het past op één pagina. De waarde ervan is dat het een oneindige verzameling keuzes omzet in een kort menu, en dat maakt consistentie haalbaar voor iedereen - ook voor een tool.

## Bouw de Componenten Eén Keer

Onder de tokens zitten de componenten waaruit alles wordt samengesteld: knop in twee of drie varianten, invoerveld met label en fouttoestand, kaart, dialoog, tabel, badge, lege toestand.

Twee manieren om eraan te komen. Neem een componentenbibliotheek die gedrag en toegankelijkheid al goed regelt - wat, zoals het toegankelijkheidsartikel in deze reeks betoogt, de beslissing met de grootste hefboom is die beschikbaar is - en pas uw tokens erop toe. Of bouw de twaalf die u nodig hebt zelf, wat een dag is en betekent dat u hun toetsenbord- en schermlezergedrag bezit, wat gegenereerde componenten consequent missen.

Voor bijna elk klein product: neem de bibliotheek.

Dan de regel: schermen worden samengesteld uit die componenten. Een scherm dat een knop nodig heeft, gebruikt de knop. Is er echt een nieuw component nodig, dan wordt het één keer gebouwd, aan de set toegevoegd en gebruikt.

## Laat de Tool het Systeem Volgen

Dit is het deel dat verandert wat generatie oplevert, en daarom is het systeem de moeite waard in een product dat zo is gebouwd.

Zet de tokens en de componentenlijst in een bestand in uw repository - het afsprakenbestand dat deze reeks steeds aanbeveelt - en zeg duidelijk: dit zijn de kleuren, dit is de afstandsschaal, dit zijn de componenten, gebruik ze en introduceer geen nieuwe.

Codeerassistenten lezen het. Het verschil in uitvoer is direct en groter dan oprichters verwachten: een sessie die wordt gevraagd een scherm toe te voegen, stelt het samen uit de bestaande componenten in plaats van een vierde knop te verzinnen.

Versterk het met voorbeelden. Een model dat schrijft in een codebase waarin elk scherm dezelfde componenten gebruikt, zal dat imiteren, omdat imiteren is waar het goed in is. De consistentie houdt zichzelf in stand zodra er een meerderheidspatroon is om te kopiëren.

## Herstel Wat Er Is, Houd Dan de Lijn Vast

Voor een applicatie die al zes knopstijlen heeft, is de opruiming overzichtelijk.

Inventariseer wat er is: elke gebruikte kleur, elke afstandswaarde, elke variant van knop en invoerveld. De lijst is meestal korter dan het voelt - zes knoppen, twaalf grijzen, een dozijn willekeurige marges.

Kies van elk de canonieke versie, definieer de tokens, bouw of neem de componenten, en zet scherm voor scherm om. Een dag voor een applicatie van twintig schermen, en het kan stapsgewijs: alles wat u aanraakt, wordt omgezet.

Houd het daarna vast met het afsprakenbestand en de maandelijkse review die elders in deze reeks wordt beschreven, waarbij u specifiek controleert of er een nieuwe kleur of een nieuw component is verschenen.

## Dark Mode en Andere Dingen Die Tokens Goedkoop Maken

Zodra de interface naar benoemde waarden verwijst in plaats van naar letterlijke kleuren, worden een reeks wijzigingen die eerder groot waren configuratie.

Dark mode is de voor de hand liggende: definieer de tokenwaarden een tweede keer voor een donkere context en de hele interface volgt. Dit proberen zonder tokens betekent elke kleur in elk component opzoeken, en daarom offreren producten die het systeem oversloegen weken voor een functie die een middag zou moeten zijn.

Hetzelfde geldt voor verschillende andere. Een klant die het product in eigen kleuren wil - gebruikelijk bij white-label-afspraken en echt geld waard - is een tokenoverride in plaats van een fork. Een dichtheidsinstelling voor gebruikers die meer op het scherm willen, is het wisselen van een afstandsschaal. En een contrastaanpassing voor toegankelijkheid is een wijziging van twee of drie waarden in plaats van een audit.

Geen van deze is op zichzelf een reden om een design system te bouwen. Ze zijn de reden dat een systeem dat voor consistentie is gebouwd zich daarna blijft terugbetalen, en ze zijn het weten waard wanneer u beslist of de twee dagen gerechtvaardigd zijn.

Het advies tegen over-engineering blijft gelden. Definieer de tokens die u gebruikt, niet die welke een groot bedrijf nodig zou hebben. Een product met acht kleuren en één afstandsschaal krijgt al het bovenstaande; een product met honderd tokens en een thema-architectuur heeft een design system gebouwd als project in plaats van als hulpmiddel, en dat is een andere en meestal onnodige onderneming.

## Content Hoort Ook bij het Systeem

De inconsistentie die oprichters opmerken is visueel. Die welke klanten opmerken zit in de woorden, en die drijft om precies dezelfde reden af.

Een gegenereerd product verzamelt drie manieren om hetzelfde te zeggen. De knop heet op het ene scherm "Opslaan" en op een ander "Bewaren". Foutmeldingen zijn soms verontschuldigende zinnen en soms technische fragmenten. Datgene waar uw product over gaat, heet op het ene scherm een cliënt, op het volgende een klant en in de instellingen een account - wat het woordenschatprobleem is dat het schema-artikel in deze reeks beschrijft, zichtbaar in de interface waar gebruikers het tegenkomen.

Voeg een korte sectie toe aan het afsprakenbestand. De woorden die uw product voor zijn begrippen gebruikt, met de woorden die het niet gebruikt ernaast. De standaardlabels voor veelvoorkomende acties. De toon voor foutmeldingen - wat er gebeurde, en wat eraan te doen is. Of u gebruikers aanspreekt met "je" of "u", wat in het Nederlands een beslissing is die één keer moet worden genomen en overal toegepast, en die gegenereerde tekst anders binnen één scherm door elkaar haalt.

Een halve pagina, en het doet hetzelfde werk als de tokens: het zet een open vraag om in een kort menu, voor u en voor wat het volgende scherm ook schrijft.

Het is ook het goedkoopste van al het werk in dit artikel. Er hoeft niets gebouwd, niets omgezet, en het effect op hoe af een product aanvoelt staat in geen verhouding tot de moeite - vooral voor een Nederlands product, waar een mengeling van formele en informele aanspreekvormen leest als slordigheid in plaats van als afwisseling.

## Dit Inrichten

Voor een bestaande applicatie is dit doorgaans één tot twee dagen: een inventaris van gebruikte kleuren, afstandswaarden en componentvarianten; een tokenset gedefinieerd - zes tot tien kleuren, één afstandsschaal, drie of vier tekstformaten, één afronding en één schaduw; een toegankelijke componentenbibliotheek genomen en gestyled met de tokens, of een dozijn componenten gebouwd; schermen omgezet om ze te gebruiken; willekeurige waarden verwijderd zodat de enige beschikbare keuzes de gedefinieerde zijn; de tokens en componentenlijst in het afsprakenbestand van de repository geschreven zodat codeerassistenten ze volgen; en een controle op nieuw geïntroduceerde waarden in de maandelijkse review.

LaunchStudio doet dit samen met toegankelijkheidswerk, omdat die twee dezelfde oplossing delen. Daarachter staat Manifera - elf jaar, 160+ projecten, met design en engineering vanuit Amsterdam, Singapore en Ho Chi Minh-stad.

[Stuur ons vijf schermen](https://launchstudio.eu/nl/#contact) en wij vertellen u hoeveel knopstijlen u hebt.

## Echt voorbeeld

### Elf Grijzen

Sanne de Rooij bouwde Stagebureau met Bolt: stageplaatsingsadministratie voor mbo-instellingen, gebruikt door 12 instellingen om jaarlijks zo'n 3.000 studenten te koppelen aan leerbedrijven.

De communicatiemedewerker van een instelling beoordeelde het product vóór een bredere uitrol en leverde een lijst van 34 inconsistenties op. Sannes eerste reactie was dat ze cosmetisch waren.

De inventaris vond elf verschillende grijzen voor tekst, zeven knopstijlen verspreid over negen schermen, vier verschillende kaartbehandelingen, drie ontwerpen voor invoervelden met verschillende foutafhandeling, en afstandswaarden van 3 tot 37 pixels zonder patroon. Twee schermen gebruikten een heel ander lettertype, uit een sessie waarin de tool naar iets anders had gegrepen.

Belangrijker: de audit vond dat de inconsistentie een functioneel probleem verborg. De drie invoerveldontwerpen gingen verschillend om met validatiefouten, en één ervan toonde fouten alleen in kleur, zonder tekst - wat zowel een toegankelijkheidsfout was als de reden dat twee instellingen hadden gemeld dat studenten niet begrepen waarom een formulier niet verstuurd werd.

Twee werkdagen: tokens gedefinieerd met acht kleuren, waaronder één grijsschaal van vijf stappen, een afstandsschaal in veelvouden van vier, drie kopformaten en één formaat voor lopende tekst, één afronding en één schaduw; een toegankelijke componentenbibliotheek genomen en gestyled met die tokens; knop, invoerveld, kaart, dialoog, tabel, badge en lege toestand gestandaardiseerd; alle negen schermen omgezet; het afwijkende lettertype verwijderd; foutafhandeling geüniformeerd met tekst naast kleur, wat de klacht van de instellingen oploste; elke willekeurige kleur- en afstandswaarde uit de codebase verwijderd zodat alleen de gedefinieerde beschikbaar zijn; en de tokens en componentenlijst in het afsprakenbestand van de repository geschreven.

**Resultaat:** de lijst van de communicatiemedewerker slonk tot twee resterende punten, beide geaccepteerd. Latere AI-sessies leveren schermen op die passen, wat Sanne omschrijft als de verandering die het verschil maakte - voorheen voegde elke nieuwe functie een variant toe, nu niet meer. Binnen het kwartaal tekenden nog twee instellingen.

> *"Ik dacht dat het cosmetisch was. Toen ontdekte ik dat een van mijn drie invoerveldontwerpen fouten alleen in kleur toonde, en dat dat de reden was dat studenten op twee scholen niet konden achterhalen wat er mis was met hun formulieren."*
> - **Sanne de Rooij, Oprichter, Stagebureau (Zwolle)**

**Kosten & Doorlooptijd:** €2.600 (interface-inventaris, tokendefinitie, toegankelijke componentenbibliotheek genomen en gestyled, negen schermen omgezet, foutafhandeling geüniformeerd, willekeurige waarden verwijderd, afsprakendocumentatie) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Waarom passen AI-gegenereerde schermen niet bij elkaar?

Elk wordt in een eigen sessie gemaakt zonder kennis van eerdere beslissingen. Elk scherm is een redelijk antwoord op zijn eigen verzoek, en niets brengt ze met elkaar in overeenstemming.

### Maakt consistentie in de interface echt uit?

Ja. Voorspelbare elementen zijn makkelijker in gebruik, samenhang signaleert aandacht voor detail aan zakelijke kopers, en inconsistentie stapelt zich op - zodra er zes varianten zijn, is er niets waarop een nieuw scherm kan aansluiten.

### Wat is het minimale design system?

Zes tot tien kleuren met rollen, één afstandsschaal, drie of vier tekstformaten, één afronding en één schaduw - plus een dozijn componenten. Het past op een pagina.

### Moet ik componenten bouwen of een bibliotheek nemen?

Neem er een. Die regelt toetsenbord- en schermlezergedrag dat gegenereerde componenten missen, en hem stylen met uw tokens is veel minder werk dan uw eigen bouwen en onderhouden.

### Hoe voorkom ik dat het afdrijven terugkomt?

Schrijf de tokens en componentenlijst in een afsprakenbestand in de repository. Codeerassistenten lezen het, en de uitvoer verandert direct.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zien AI-gegenereerde schermen er inconsistent uit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elk scherm wordt in een eigen sessie gegenereerd zonder geheugen van eerdere beslissingen, dus niets brengt de keuzes met elkaar in overeenstemming."
      }
    },
    {
      "@type": "Question",
      "name": "Maakt consistentie in de interface commercieel uit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja - voorspelbare elementen zijn makkelijker in gebruik en samenhang signaleert zorg aan zakelijke kopers, terwijl inconsistentie zich met elk nieuw scherm opstapelt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het minimale bruikbare design system?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zes tot tien kleuren met rollen, één afstandsschaal, drie of vier tekstformaten, één afronding en schaduw, plus ongeveer een dozijn componenten."
      }
    },
    {
      "@type": "Question",
      "name": "Componenten bouwen of een bibliotheek nemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Neem er een - die levert het toetsenbord- en schermlezergedrag dat gegenereerde componenten missen, gestyled met uw eigen tokens."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat design drift terugkomt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zet de tokens en componentenlijst in het afsprakenbestand van de repository; codeerassistenten lezen en volgen het."
      }
    }
  ]
}
</script>
