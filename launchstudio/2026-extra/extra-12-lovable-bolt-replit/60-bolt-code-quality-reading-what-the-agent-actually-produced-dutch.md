---
Titel: "Bolt-Codekwaliteit: Lezen Wat de Agent Werkelijk Opleverde"
Trefwoorden: bolt codekwaliteit, gegenereerde code lezen, duplicatie, dode code, onderhoudbaarheid, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Bolt-Codekwaliteit: Lezen Wat de Agent Werkelijk Opleverde

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt-Codekwaliteit: Lezen Wat de Agent Werkelijk Opleverde",
  "description": "U hoeft geen developer te zijn om een door AI gebouwde codebase te beoordelen. De specifieke patronen die problemen voorspellen, hoe u ze vindt zonder elke regel te lezen, en welke het oplossen waard zijn.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-code-quality-reading-what-the-agent-actually-produced" }
}
</script>

Gegenereerde code is zelden incompetent. Ze is meestal competent en repetitief, verzoek voor verzoek geschreven door iets zonder geheugen van de vorige verzoeken en zonder zicht op het geheel.

Dat levert een specifieke handtekening op: dezelfde logica vier keer geïmplementeerd in vier componenten, twee manieren om hetzelfde te doen naast elkaar, en functies die zijn verlaten maar nog aanwezig zijn en nog draaien.

Niets daarvan houdt het product tegen. Alles daarvan maakt elke volgende wijziging trager, duurder en waarschijnlijker dat er iets breekt - en dat zijn de kosten die uiteindelijk zichtbaar worden als "met deze codebase is moeilijk te werken".

U hoeft niet elke regel te lezen om haar te beoordelen. Een handvol controles vertelt u het meeste van wat ertoe doet.

## Duplicatie Is het Belangrijkste Symptoom

Zoek naar een kenmerkende zin - de opmaak van een datum die u toont, de manier waarop u btw berekent, de vorm van een databasequery - en tel op hoeveel plekken ze voorkomt.

Vier kopieën van een btw-berekening betekent vier plekken om aan te passen als een tarief verandert, en drie ervan worden gemist. Vier kopieën van een databasequery betekent dat de beperking tot de huidige organisatie op vier plekken bestaat en op één ontbreekt. Dit is geen esthetische kwestie; hier komen correctheidsfouten vandaan.

De oplossing is mechanisch: één functie, overal aangeroepen, met de kopieën verwijderd. Doe het voor wat ertoe doet - geld, datums, rechten, datatoegang - en laat cosmetische duplicatie met rust.

## Dode Code Is Overal

Verlaten functies worden niet verwijderd door de tool die ze bouwde. Ze voegt toe; ze ruimt niet op.

Zoek naar componenten die niets weergeeft, endpoints die niets aanroept, databasetabellen die niets bevraagt, en afhankelijkheden die niets importeert. In een project met zes maanden geschiedenis kunt u een flink deel verwachten.

Twee redenen om te verwijderen in plaats van te negeren. Dode code is nog steeds context die bij elk verzoek wordt verstuurd, wat geld kost en de aandacht van het model verdunt. En een ongebruikt endpoint of een ongebruikte tabel is nog steeds bereikbaar - een verlaten functie zonder autorisatie is een actieve kwetsbaarheid waar niemand naar kijkt.

## Zoek naar Twee Manieren om Eén Ding te Doen

De betrouwbaarste voorspeller van een lastige codebase is inconsistentie: twee aanpakken voor state management, twee manieren om data op te halen, twee stylingsystemen, twee datumbibliotheken.

Het gebeurt omdat elke sessie haar probleem oplost met wat ze pakte, en niets ze met elkaar verzoent. De kosten zijn dat elke toekomstige wijziging begint met uitzoeken welke afspraak hier geldt, en dat elke AI-sessie twee patronen ziet en er willekeurig een kiest - en zo verschijnt er een derde.

Kies van elk er één en convergeer. Het hoeft niet in één keer; de regel die werkt, is dat alles wat u aanraakt wordt omgezet, en dat niets nieuws het verliezende patroon gebruikt.

## De Bestanden Die Te Groot Zijn Geworden

Een component van 900 regels dat data ophaalt, bedrijfslogica bevat en de weergave doet, is de vorm waar gegenereerde code naartoe neigt, omdat elk verzoek iets toevoegde aan het bestand dat al open stond.

Het praktische probleem is niet de lengte. Het is dat zo'n bestand niet veilig kan worden gewijzigd - elke aanpassing riskeert de delen waar u niet aan dacht - en dat het niet naar een model kan worden gestuurd zonder alles mee te sturen.

Sorteer uw bestanden op grootte. De grootste drie of vier zijn waar uw fouten wonen en waar uw kosten zich concentreren. Ze opsplitsen naar verantwoordelijkheid - datatoegang, logica, weergave - is meestal een afgebakende middag met een onevenredig groot effect.

## Controleer Wat Er Gebeurt als Er Iets Misgaat

Gegenereerde code handelt het succespad grondig af en de foutroutes zelden.

Kijk wat er gebeurt als een verzoek mislukt, als een lijst leeg is, als een veld ontbreekt, als een gebruiker geen rechten heeft. Veelvoorkomende bevindingen: fouten die worden opgevangen en stilletjes weggegooid, zodat een mislukking eruitziet als een lege pagina; geen laadtoestand, zodat de interface kapot lijkt tijdens het wachten; geen lege toestand, zodat een nieuwe gebruiker een leeg scherm zonder uitleg ziet; en een foutmelding die de ruwe technische fout aan de klant toont.

Dat zijn afzonderlijk kleine oplossingen, en ze zijn het grootste deel van wat mensen bedoelen als ze zeggen dat een product onaf aanvoelt.

## Waar U Zich Geen Zorgen over Hoeft te Maken

Drie dingen waar oprichters op blijven hangen en die er niet veel toe doen.

Opmaak en stijl van naamgeving, mits het consistent genoeg is om te lezen. Een formatter die één keer wordt toegepast, regelt het.

Of het de nieuwste aanpak gebruikt. Werkende, begrijpelijke code in een ouder idioom is beter dan een herschrijving naar de huidige mode.

Of een developer het zo zou hebben geschreven. Een deel zou hij niet zo hebben geschreven, en veel daarvan is smaak. Wat ertoe doet, is of het correct, consistent en aanpasbaar is.

## Tests, Naar Verhouding

De vraag die altijd volgt op een gesprek over codekwaliteit, is of een door AI gebouwd product een testsuite nodig heeft, en het eerlijke antwoord is: een kleine, die specifieke dingen dekt, geschreven nadat het product niet meer van vorm verandert.

Uitgebreide tests schrijven tegen een prototype dat wekelijks opnieuw wordt ontworpen, is verspild werk - de tests leggen beslissingen vast die op het punt staan te veranderen. Maar lanceren zonder tests betekent dat elke deployment wordt gecontroleerd door te klikken, en klikken schaalt niet voorbij een dozijn schermen.

De proportionele set voor een klein product, in volgorde van waarde.

**Autorisatietests.** De controle tussen accounts die in deze reeks wordt beschreven, geautomatiseerd: een gebruiker van een tweede organisatie die elk endpoint opvraagt, en de build laat falen bij elke teruggegeven data. Dit is de waardevolste test die een door AI gebouwd product kan hebben.

**Geld.** Elke berekening met prijzen, btw, kortingen, pro-rata verrekening en totalen. Dat zijn de fouten die echte bedragen kosten, en de fouten die duplicatie oplevert.

**Het hoofdproces, van begin tot eind.** Eén test die zich aanmeldt, het centrale ding doet waarvoor uw product bestaat, en het resultaat controleert. Hij vangt de deployment die alles brak.

**Elke fout die u twee keer hebt opgelost.** Een test op het moment van de tweede oplossing garandeert dat er geen derde komt.

Dat zijn misschien dertig tests voor een typisch product, ze draaien in minder dan een minuut, en ze dekken de mislukkingen die werkelijk voorkomen. Een codeerassistent vragen ze te schrijven, is redelijk gebruik ervan, mits u leest wat ze controleren - een test die slaagt ongeacht het gedrag, is erger dan geen test, en gegenereerde suites bevatten ze.

## Het Halfuur Review Dat Maandelijks de Moeite Waard Is

Niets hiervan hoeft een project te zijn. Een terugkerend halfuur, eens per maand, voorkomt dat een gegenereerde codebase de toestand bereikt waarin ze er een nodig heeft.

Open de repository en kijk wat er sinds de vorige keer veranderde. Niet regel voor regel - alleen de lijst met aangeraakte bestanden en de vorm van de toevoegingen. Drie vragen.

**Is er iets gedupliceerd?** Een nieuw component dat iets opnieuw implementeert wat al bestaat, is de meest voorkomende toevoeging, en het dezelfde maand opvangen is een oplossing van tien minuten in plaats van volgend jaar zoeken-en-vervangen in zeven bestanden.

**Is er iets dood geworden?** Een functie die vorige maand werd vervangen, liet haar voorganger achter. Die nu verwijderen is triviaal; die over een jaar verwijderen vereist eerst uitzoeken of iets haar nog gebruikt.

**Is er een nieuwe afspraak verschenen?** Een tweede datumbibliotheek, een andere manier om data op te halen, een stylingaanpak die niet past. Dit is het moment om te beslissen of ze de oude overal vervangt of wordt teruggedraaid - voordat er een derde komt.

Dertig minuten per maand, aan een codebase die zichzelf grotendeels schrijft, is het verschil tussen een product dat goedkoop te veranderen blijft en een product dat oprichters beschrijven als toe aan een herschrijving. En de herschrijving is bijna nooit nodig; het is gewoon hoe opgestapelde verwaarlozing van binnenuit aanvoelt.

Het werkt omdat de eenheid van verwaarlozing in deze codebases klein en regelmatig is. Elke sessie voegt een beetje toe, en niets haalt iets weg; een maandelijkse ronde die weghaalt, is het enige tegenwicht dat nodig is.

Het is ook de review die de beoordeling eerlijk houdt. Een codebase ziet er goed uit als u altijd alleen het deel ziet dat u verandert; de maandelijkse blik op het geheel is hoe het patroon zichtbaar wordt terwijl het nog klein is.

## Dit Inrichten

Voor een door AI gebouwde codebase kost dit doorgaans één tot twee dagen: duplicatie gevonden door te zoeken naar kenmerkende logica en samengebracht voor geld, datums, rechten en datatoegang; dode componenten, endpoints, tabellen en afhankelijkheden verwijderd, waarbij ongebruikte endpoints vóór verwijdering op blootstelling worden gecontroleerd; concurrerende afspraken geïdentificeerd en van elk er één gekozen met een convergentieregel; de grootste bestanden opgesplitst naar verantwoordelijkheid; fout-, laad- en lege toestanden toegevoegd waar ze ontbraken; foutmeldingen menselijk gemaakt; een formatter en linter toegepast; en de afspraken in de repository vastgelegd, zodat de volgende sessie ze volgt.

LaunchStudio doet dit bij het overnemen van een door AI gebouwd product, en het is wat elk volgend stuk werk goedkoper maakt. De engineers zijn van Manifera - elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Stuur ons uw repository](https://launchstudio.eu/nl/#contact) en wij vertellen u waar de duplicatie zit.

## Echt voorbeeld

### Zeven Kopieën van Dezelfde Berekening

Rogier Slagter bouwde Verhuurbeheer met Bolt: verhuuradministratie voor eigenaren van vakantiewoningen en kleine vastgoedbeheerders, 62 gebruikers die 380 woningen beheren.

Het tarief van de toeristenbelasting in één gemeente veranderde. Rogier paste het aan, deployde, en drie dagen later meldde een vastgoedbeheerder dat hun facturen nog het oude bedrag toonden.

Het tarief stond op zeven plekken: twee componenten, een factuurgenerator, een offertevoorbeeld, een pdf-sjabloon, een samenvattingsberekening en een standaardwaarde in de database. Hij had er vier gevonden en aangepast.

Twee werkdagen: de zeven kopieën samengebracht in één configuratie met één rekenfunctie, wat ook blootlegde dat twee van de kopieën al maanden licht verschilden - een afrondingsverschil dat facturen opleverde die een cent afweken van hun eigen regels; dezelfde behandeling toegepast op de opmaak van datums, die vijf implementaties had met drie verschillende gedragingen rond middernacht; 14 dode componenten, 6 ongebruikte endpoints en 3 verlaten tabellen verwijderd, waarvan een van de endpoints een export zonder authenticatie van alle boekingen was, overgebleven van een vroeg experiment; twee concurrerende manieren om data op te halen teruggebracht tot één; de vier grootste bestanden, alle boven de 600 regels, opgesplitst in datatoegang, logica en weergave; laad- en lege toestanden toegevoegd aan elf schermen die lege pagina's hadden getoond; foutmeldingen herschreven van ruwe technische tekst naar zinnen; een formatter toegepast; en een afsprakenbestand gecommit dat de gekozen patronen beschrijft.

**Resultaat:** een wijziging van de toeristenbelasting kost nu één aanpassing. Het export-endpoint zonder authenticatie was acht maanden bereikbaar geweest en was de ernstigste bevinding, alleen ontdekt omdat er dode code werd verwijderd. Rogier vertelt dat latere AI-sessies merkbaar consistenter werk opleveren sinds het afsprakenbestand werd toegevoegd, wat hij niet had verwacht.

> *"Ik paste het belastingtarief op vier plekken aan en dacht dat ik klaar was. Het stond op zeven plekken, en twee ervan waren het sinds het voorjaar stilletjes met elkaar oneens."*
> - **Rogier Slagter, Oprichter, Verhuurbeheer (Zandvoort)**

**Kosten & Doorlooptijd:** €2.700 (samenbrengen van gedupliceerde belasting- en datumlogica, verwijderen van dode code met controle op blootstelling, verzoenen van afspraken, opsplitsen van grote bestanden, afhandeling van fout- en lege toestanden, herschrijven van foutmeldingen, opmaak, documentatie van afspraken) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Hoe beoordeel ik codekwaliteit zonder developer te zijn?

Zoek naar kenmerkende logica en tel de kopieën, zoek naar ongebruikte componenten en endpoints, controleer of er twee aanpakken voor hetzelfde naast elkaar bestaan, sorteer bestanden op grootte, en kijk wat er bij een mislukking gebeurt.

### Waarom doet duplicatie er zo toe?

Omdat een wijziging op drie van de vier plekken er één fout laat, en als de gedupliceerde logica geld, rechten of de beperking van data betreft, is dat een correctheids- of beveiligingsfout in plaats van slordigheid.

### Is dode code echt schadelijk?

Ja. Het is context die bij elk verzoek naar het model wordt gestuurd, en een verlaten endpoint of tabel is nog steeds bereikbaar - vaak zonder enige autorisatie, omdat het nooit af was.

### Moet ik gegenereerde code herschrijven zodat ze eruitziet als handgeschreven?

Nee. Correct, consistent en aanpasbaar is de norm. Herschrijven voor stijl of voor het nieuwste idioom kost tijd zonder iets te verbeteren wat een klant ervaart.

### Welke afzonderlijke wijziging maakt toekomstige AI-sessies beter?

Een afsprakenbestand in de repository dat de patronen beschrijft die u koos. Assistenten lezen het, en de consistentie van wat ze opleveren, verbetert direct.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe kan een niet-developer door AI gegenereerde code beoordelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tel kopieën van kenmerkende logica, zoek naar ongebruikte componenten en endpoints, controleer op concurrerende aanpakken, sorteer bestanden op grootte, en test de foutroutes."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom doet gedupliceerde logica ertoe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een wijziging op drie van de vier kopieën laat er één fout - en als de logica geld, rechten of de beperking van data betreft, is dat een echte fout."
      }
    },
    {
      "@type": "Question",
      "name": "Is dode code schadelijk in een door AI gebouwd project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja - het is betaalde context bij elk verzoek, en verlaten endpoints of tabellen zijn vaak bereikbaar zonder autorisatie."
      }
    },
    {
      "@type": "Question",
      "name": "Moet gegenereerde code met de hand worden herschreven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Correct, consistent en aanpasbaar is de norm; herschrijven voor stijl of mode verbetert niets wat een klant ziet."
      }
    },
    {
      "@type": "Question",
      "name": "Wat verbetert toekomstige AI-sessies het meest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een afsprakenbestand in de repository dat uw gekozen patronen beschrijft - assistenten lezen het en leveren merkbaar consistenter werk op."
      }
    }
  ]
}
</script>
