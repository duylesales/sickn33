---
Titel: "AI-ontwikkeling: Een Werkwijze Opbouwen na Uw Eerste Aanname"
Trefwoorden: ai-ontwikkeling, eerste aanname, engineeringproces, onboarding, klein team, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS Scale-Up
---

# AI-ontwikkeling: Een Werkwijze Opbouwen na Uw Eerste Aanname

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-ontwikkeling: Een Werkwijze Opbouwen na Uw Eerste Aanname",
  "description": "Een oprichter die alles alleen bouwde, heeft nu een collega, en de gewoonten die voor één persoon werkten, werken niet voor twee. De minimale werkwijze, wat u als eerste opschrijft, en wat u voor later bewaart.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-development-building-a-process-after-your-first-hire" }
}
</script>

Alles werkte toen er één van u was. Beslissingen gebeurden in uw hoofd, context leefde in uw geheugen, en de werkwijze was wat u die dag deed.

De eerste aanname verandert dat allemaal tegelijk, en de verandering wordt meestal ervaren als vertraging: u beantwoordt de hele dag vragen, de nieuwe persoon is onzeker, en het product beweegt minder dan toen u alleen was. Die fase is normaal en duurt ongeveer een maand.

Wat bepaalt of ze een maand of een kwartaal duurt, is hoeveel van wat in uw hoofd zat nu is opgeschreven.

## Schrijf Eerst de Drie Dingen Op

In de eerste week, vóór al het andere, drie documenten.

**Hoe u het draait.** Inrichting, omgevingen, de commando's, waar dingen zijn gedeployd. Zonder dit gaan de eerste dagen op aan het draaiend krijgen van het product, wat zowel duur als demotiverend is.

**Hoe deze codebase werkt.** Het afsprakenbestand dat deze reeks steeds aanbeveelt: patronen, naamgeving, de gekozen bibliotheek per taak, de regels die niet gebroken mogen worden, en de woordenschat van het product. Dit voorkomt dat twee mensen twee codebases maken, zoals het artikel over teams van twee beschrijft.

**Waar het product voor is.** Wie de klanten zijn, waarvoor ze het gebruiken, wat voor hen belangrijk is. Een developer die het bedrijf begrijpt, neemt betere beslissingen in de tientallen kleine onduidelijkheden die dagelijks opduiken, en dit is het document waarvan oprichters het minst verwachten dat ze het nodig hebben.

Al het andere kan wachten. Deze drie, in de eerste week, in de repository.

## Geef Ze Direct Iets Echts

Het instinct is een nieuwe persoon te laten beginnen met iets veiligs aan de rand. Dat verspilt de eerste twee weken.

De betere eerste taak is klein, echt en midden in het product: een bug die een klant meldde, een kleine functie waarom iemand vroeg. Ze is binnen enkele dagen gedeployd, wat bevestigt dat het hele pad werkt — omgeving, review, deployment — en ze leert meer over de codebase dan lezen zou doen.

Werk de eerste samen uit, of loop haar in elk geval achteraf samen door. Het gaat niet om toezicht; het gaat erom dat het gesprek de dingen bovenhaalt waarvan geen van beiden wist dat ze uitleg nodig hadden.

## De Minimale Werkwijze voor Twee Mensen

Zoals het artikel over teams van twee in deze reeks betoogt, is het meeste wat over engineeringprocessen wordt geschreven bedoeld voor grotere organisaties. Bij twee mensen is de nuttige set kort.

**Een branch per wijziging, gereviewd vóór de merge.** Vijf minuten op de diff, met echte aandacht voor geld, rechten, verwijderen, uitgaande communicatie en schema.

**Een gedeelde lijst van wat er komt**, in volgorde van prioriteit, die beiden kunnen zien. Geen ticketsysteem — een lijst.

**Een kort dagelijks gesprek.** Waar ieder mee bezig is, wat vastzit. Tien minuten.

**Een wekelijkse blik op wat er is opgeleverd en wat er komt.** Hier worden prioriteiten bijgesteld, en het is het overleg dat een maand bouwen aan het verkeerde ding voorkomt.

Dat is de hele werkwijze. Alles meer kost op deze omvang meer dan het oplevert.

## Bepaal Wie Wat Beslist

De vraag die na een eerste aanname de meeste wrijving veroorzaakt, en ze wordt zelden expliciet besproken.

Welke beslissingen zijn van de oprichter, welke van de developer, en welke gezamenlijk? Productrichting en prioriteiten zijn van u. De implementatieaanpak binnen een taak is van hen. Architectuur, schemawijzigingen, het toevoegen van een dependency of een dienst, en alles wat klanten raakt, zijn gezamenlijk.

Zeg dit hardop in de eerste week. Een developer die niet weet of hij een bibliotheek mag kiezen, vraagt ofwel over alles, wat uw dag kost, ofwel kiest zonder te vragen, wat af en toe een beslissing oplevert die u anders had genomen.

## Verwacht een Maand Trager te Zijn

De eigen output van de oprichter daalt tijdens de onboarding, en dat vooraf weten voorkomt de verkeerde conclusie.

U beantwoordt vragen, reviewt werk, en schrijft dingen op die u nooit hoefde te verwoorden. Dat is de investering, en die betaalt zich terug in de tweede maand, wanneer de ander productief is, en de derde, wanneer hij zelfstandig is.

De fout is de investering overslaan om te blijven opleveren, wat een developer oplevert die voor onbepaalde tijd afhankelijk is en een oprichter die permanent wordt onderbroken.

## Iemand Aannemen Die Dezelfde Tools Gebruikt

Een vraag die specifiek is voor dit moment: moet uw eerste developer AI-tools gebruiken zoals u dat hebt gedaan?

Vrijwel zeker ja, en het is de moeite waard dat in het sollicitatiegesprek vast te stellen in plaats van aan te nemen. Een developer die zo werkt, is sneller in uw codebase en begrijpt het karakter ervan — de duplicatie, de gegenereerde patronen, de plekken waar een sessie een bepaalde kant op ging — in plaats van het te zien als bewijs van incompetentie.

Drie dingen om in de eerste week af te spreken.

**Het afsprakenbestand is leidend.** Hun assistent leest het, en alles wat hij oplevert dat ermee in strijd is, wordt gecorrigeerd in plaats van geaccepteerd.

**Dezelfde reviewstandaard geldt.** Gegenereerde code wordt gereviewd zoals alle andere code, met dezelfde aandacht voor geld, rechten, verwijderen, uitgaande communicatie en schema. Een wijziging die niemand las, is een wijziging die niemand las, ongeacht wie haar typte.

**Oordeel wordt niet gedelegeerd.** De tools schrijven; de persoon beslist. Dit is het onderscheid dat het reviewartikel in deze reeks beschrijft, en het is de verwachting om expliciet uit te spreken tegenover iemand die nieuw is.

De developer om voorzichtig mee te zijn, is niet degene die deze tools intensief gebruikt. Het is degene die niet kan uitleggen wat zijn assistent opleverde — want dat is de persoon die over zes maanden een heleboel aan uw product zal hebben toegevoegd waarvan niemand rekenschap kan geven.

## Wat U bij Vijf Mensen Toevoegt, Niet Eerder

Oprichters die groei verwachten, installeren soms vroeg het proces van een groter bedrijf, wat twee mensen vertraagt om zich voor te bereiden op een team dat misschien nooit bestaat.

De dingen die het echt waard zijn later toe te voegen, en ongeveer wanneer.

**Een ticketsysteem met statussen** — rond vier of vijf mensen, wanneer een gedeelde lijst niet meer volstaat omdat niemand kan zien wat er in uitvoering is.

**Formele review met benoemde goedkeurders** — wanneer er genoeg mensen zijn dat "de ander kijkt ernaar" dubbelzinnig is.

**Een rooster voor bereikbaarheidsdiensten** — wanneer incidenten zo vaak voorkomen dat één persoon ze niet kan opvangen, en wanneer er meer dan één persoon is die ze kan oplossen.

**Meer dan drie omgevingen, en releasebranches** — wanneer releases worden gecoördineerd over meerdere mensen met verschillende planningen.

**Geschreven architectuurbeslissingen in een formeel proces** — wanneer de codebase zo groot is dat niemand haar helemaal heeft gelezen, wat later is dan mensen denken.

**Schattingen en planningsrituelen** — wanneer er toezeggingen worden gedaan aan mensen buiten het team.

Tot die tijd volstaat de korte lijst in dit artikel, en elke toevoeging daarbovenop is overhead die u dagelijks betaalt voor een voordeel dat pas komt bij een omvang die u nog niet hebt bereikt. Het signaal om iets toe te voegen is een terugkerend probleem dat het oplost, niet het vooruitlopen op een probleem.

## Houd het Klantcontact

Met een eerste technische aanname komt stilletjes een risico mee: de oprichter is niet langer degene die met klanten over het product praat, omdat er nu iemand is wiens taak dat lijkt te zijn.

Het is de moeite waard daar weerstand tegen te bieden. De kennis van de oprichter over wat klanten nodig hebben, is wat het product liet werken, en die vervalt snel wanneer ze uit de tweede hand komt. Een functieverzoek dat een developer via een samenvatting bereikt, verliest de aarzeling, de context en wat de klant daarna zei — en daar zat vaak de eigenlijke eis.

Twee praktische regelingen. De oprichter blijft betrokken bij de supportgesprekken, ten minste door ze te lezen, aanzienlijk langer dan nodig voelt. En de developer schuift rechtstreeks aan bij sommige klantgesprekken, wat de snelste manier is om de context te verwerven die het bedrijfsdocument alleen schetst.

Het tweede is degene die zich terugbetaalt. Een developer die drie praktijkmanagers dezelfde frustratie heeft horen beschrijven, bouwt iets anders dan een die een ticket las, en het verschil is zichtbaar in het product.

Dit is ook het antwoord op de vraag wat de oprichter doet terwijl de developer bouwt. Geen toezicht — klanten, het werk dat tijdens de twee jaar alleen bouwen bleef liggen, en de reden om in de eerste plaats iemand aan te nemen.

## Dit Inrichten

In de eerste maand na een eerste aanname: drie documenten in de eerste week — hoe u het draait, hoe de codebase werkt, waar het product voor is; een kleine echte taak die binnen enkele dagen wordt gedeployd, samen uitgewerkt of doorgelopen; een branch per wijziging met een review van vijf minuten en echte aandacht voor de vijf dure categorieën; een gedeelde prioriteitenlijst; een dagelijks gesprek van tien minuten en een wekelijkse review van wat er is opgeleverd; een expliciete verklaring van welke beslissingen bij wie horen; en de acceptatie dat uw eigen output een maand daalt.

LaunchStudio maakt precies deze documenten wanneer we een product overdragen aan een team van de klant, wat hetzelfde probleem is in een andere volgorde. Daarachter staat Manifera — elf jaar, 120+ engineers, 160+ projecten, vanaf de Herengracht 420 in Amsterdam.

[Vraag ons de onboardingdocumenten te schrijven](https://launchstudio.eu/nl/#contact) voordat uw eerste developer begint.

## Echt voorbeeld

### Zes Weken aan Onderbrekingen

Nienke Baaijens bouwde Zorgcontract in Lovable: contract- en tariefadministratie tussen zorgaanbieders en zorgverzekeraars, gebruikt door 34 aanbieders.

Ze nam haar eerste developer aan na twee jaar alleen. Er was geen documentatie van welke soort ook — geen README, geen afspraken, niets over het bedrijf — omdat ze die nooit nodig had gehad.

De eerste zes weken waren slechter dan alleen werken. Haar developer stelde tussen de vijftien en dertig vragen per dag, waarvan ze de meeste in één zin kon beantwoorden en geen enkele had opgeschreven. Hij besteedde de eerste drie dagen aan het draaiend krijgen van het product. Hij bouwde twee functies op een manier die niet paste bij de rest van de codebase, omdat niets beschreef hoe de rest van de codebase werkte, en beide moesten opnieuw. En hij nam twee keer een beslissing die zij anders had genomen — een grafiekenbibliotheek toevoegen en een tabelstructuur wijzigen — omdat niemand had gezegd welke beslissingen van hem waren.

Haar eigen output in die weken was bijna nul.

Twee werkdagen, daarna een ander verloop: een README over inrichting en omgevingen, samen met de developer geschreven zodat de gaten werden gevonden door degene die ze had; een afsprakenbestand op basis van de bestaande code, inclusief de gekozen bibliotheek per taak en vier regels die niet gebroken mogen worden; een document van twee pagina's over de zorgsector, de klanten, waarvoor ze het product gebruiken en wat voor hen belangrijk is; een gedeelde prioriteitenlijst; een branch per wijziging met reviews van vijf minuten; een expliciete verdeling van beslissingen, met architectuur, schema, dependencies en alles wat klanten raakt als gezamenlijke beslissingen; en de twee opnieuw gebouwde functies gebruikt als uitgewerkte voorbeelden in het afsprakenbestand.

**Resultaat:** het aantal vragen daalde binnen twee weken naar drie of vier per dag. In maand drie werkte de developer zelfstandig aan hele functies en was Nienkes eigen output hersteld tot boven het niveau van toen ze alleen werkte. Ze merkt op dat het bedrijfsdocument, dat ze overbodig had gevonden, het document bleek te zijn dat de meeste vragen wegnam — omdat de meeste ervan gingen over wat klanten echt nodig hadden in plaats van over code.

> *"Hij stelde me zes weken lang dertig vragen per dag, en ik kon ze allemaal in één zin beantwoorden. Geen van die zinnen bestond ergens anders dan in mijn hoofd."*
> — **Nienke Baaijens, Oprichter, Zorgcontract (Amersfoort)**

**Kosten & Doorlooptijd:** €2.400 (README samen geschreven, afsprakenbestand op basis van bestaande code met uitgewerkte voorbeelden, document over bedrijf en klantcontext, prioriteitenlijst en reviewproces, afbakening van beslissingen) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Wat moet ik opschrijven voordat een eerste aanname begint?

Hoe u het product draait, hoe de codebase werkt, en waar het product voor is — dat laatste is het document dat oprichters overslaan en het document dat de meeste vragen wegneemt.

### Wat moet hun eerste taak zijn?

Iets kleins, echts en centraals — een gemelde bug of een gevraagde functie — die binnen enkele dagen wordt gedeployd. Het bevestigt het hele pad en leert meer dan het lezen van de code.

### Hoeveel werkwijze heeft een team van twee nodig?

Een branch per wijziging met een review van vijf minuten, een gedeelde prioriteitenlijst, een dagelijks gesprek van tien minuten, en een wekelijkse review. Alles meer kost meer dan het oplevert.

### Wat veroorzaakt de meeste wrijving na een eerste aanname?

Niet-gedefinieerde beslissingsgrenzen. Zeg expliciet welke beslissingen van u zijn, welke van hen, en welke gezamenlijk — met architectuur, schema, dependencies en alles wat klanten raakt als gezamenlijk.

### Waarom daalt mijn eigen output?

Omdat onboarding het werk is. Verwacht een maand verminderde output, en sla die niet over om te blijven opleveren — dat levert permanente afhankelijkheid en permanente onderbreking op.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Welke documentatie moet er zijn vóór een eerste aanname?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hoe u het product draait, hoe de codebase werkt, en waar het product voor is — dat laatste neemt de meeste vragen weg."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet de eerste taak van een nieuwe developer zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Iets kleins, echts en centraals, binnen enkele dagen gedeployd — het bevestigt het hele pad en leert de codebase sneller dan lezen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel werkwijze heeft een team van twee nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een branch per wijziging met een korte review, een gedeelde prioriteitenlijst, een dagelijks gesprek van tien minuten en een wekelijkse review."
      }
    },
    {
      "@type": "Question",
      "name": "Wat veroorzaakt wrijving na een eerste aanname?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet-gedefinieerde beslissingsgrenzen — leg vast welke beslissingen van de oprichter zijn, welke van de developer, en welke gezamenlijk."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom daalt mijn output na het aannemen van iemand?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Onboarding is het werk. Verwacht een maand verminderde output; die overslaan levert permanente afhankelijkheid en onderbreking op."
      }
    }
  ]
}
</script>
