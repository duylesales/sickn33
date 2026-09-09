---
Titel: "Een dag uit het leven van een engineer die door AI gegenereerde pull requests beoordeelt"
Trefwoorden: ai software developers, ai generated pull request review, code review ai, unescaped user input
Koperfase: Bewustzijn
Doelgroep: Technische solo-oprichter
---
# Een dag uit het leven van een engineer die door AI gegenereerde pull requests beoordeelt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een dag uit het leven van een engineer die door AI gegenereerde pull requests beoordeelt",
  "description": "Een verhalende doorloop van een echte dag besteed door een van LaunchStudio's ai software developers aan het beoordelen van een door AI gegenereerde pull request, aan de hand van de codebase van een echte oprichter.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/reviewing-ai-generated-pull-requests" }
}
</script>

8:52 uur. Koffie, laptop open, de wachtrij voor die dag heeft al drie pull requests klaarstaan. Dit is een normale dinsdag voor een van LaunchStudio's ai software developers, en het tweede item in de wachtrij is een inzending van Puck Willemsen, een oprichter in Haarlem die BuurtHulp bouwde — een app voor buurthulpverzoeken — met Lovable. Haar notitie in de PR-beschrijving luidt: "Detailpagina voor verzoeken en reactiedraadjes toegevoegd, zou deze week live moeten kunnen." Laten we de daadwerkelijke beoordeling volgen, van begin tot eind.

## 9:05 uur — eerste doorloop, nog geen oordelen

De regel voor een eerste doorloop is simpel: lees voordat u iets aanraakt, en vorm geen conclusies over ernst voordat u het hele diff hebt gezien. Pucks PR raakt de nieuwe detailpagina voor verzoeken, een reactiedraadcomponent, en een handvol backend-routes die reactiedata bedienen. Op papier is het een redelijk afgebakende wijziging — misschien 40 minuten lezen, hooguit.

Regel 34 van de reactiecomponent is waar het eerste iets opvalt. Door gebruikers ingediende reactietekst wordt rechtstreeks in de pagina gerenderd zonder eerst te worden geëscaped. Op zichzelf, in één bestand, is dit een oplosbaar probleem van tien minuten: de string saniteren vóór het renderen, klaar. Maar een eerste doorloop gaat niet over het oplossen van het eerste wat u ziet — het gaat over opmerken of het een eenmalig geval is of een patroon.

## 10:20 uur — de patroontest uitvoeren

Dit is het deel dat een beoordeling onderscheidt van een vluchtige blik. In plaats van alleen regel 34 te patchen, is de volgende stap een repository-brede zoekopdracht naar hetzelfde onveilige renderpatroon — dezelfde constructie met niet-geëscapete invoer, alleen enigszins anders geschreven, afhankelijk van voor welke component Lovable het had gegenereerd.

De zoekopdracht levert twaalf bestanden op. Twaalf afzonderlijke plekken waar door gebruikers ingediende tekst — reacties, verzoekomschrijvingen, een paar profielvelden — wordt gerenderd zonder sanitatie, allemaal volgens hetzelfde onderliggende onveilige patroon. Dit is het handschrift van een door AI gegenereerde codebase, meer dan van een door mensen geschreven codebase: een menselijke developer die een onveilig patroon één keer in bestand drie schreef, zou diezelfde exacte fout waarschijnlijk niet onafhankelijk herhalen in bestand elf. Een AI-tool die gevraagd wordt om twaalf soortgelijk ogende componenten te bouwen in afzonderlijke sessies heeft geen reden om dat niet te doen.

## 11:45 uur — de beslissing: twaalf plekken patchen, of de oorzaak repareren

Dit is de daadwerkelijke technische beoordeling van de dag, en het is het deel dat een oprichter die zijn eigen PR beoordeelt waarschijnlijk volledig zou missen: patcht u elk van de twaalf gevallen afzonderlijk, of bouwt u één gedeelde, gesaniteerde renderhulpfunctie en leidt u alle twaalf daardoorheen?

Twaalf individuele patches zijn vandaag sneller en voor altijd langzamer — het dertiende onveilige geval, volgende maand toegevoegd door dezelfde AI-tool die hetzelfde patroon volgt, komt weer niet-geëscaped terug. Het bouwen van de gedeelde hulpfunctie kost deze middag meer tijd, maar verwijdert het patroon volledig als toekomstig risico, omdat nieuwe reactie- of tekstrendercomponenten de veilige versie kunnen importeren in plaats van de onveilige opnieuw te genereren. Voor BuurtHulp, waar door gebruikers ingediende tekst het hele product is — het is een app voor buurthulpverzoeken, vrijwel elk scherm heeft gebruikerstekst erop — is de gedeelde hulpfunctie de voor de hand liggende keuze.

## 13:30 uur — de fix schrijven en testen

De middag bestaat uit het bouwen van de sanitatiehulpfunctie, deze uitvoeren tegen alle twaalf oorspronkelijke aanroepplekken, en bevestigen dat Pucks daadwerkelijke UI er identiek uitziet als voorheen — dezelfde lay-out, dezelfde styling, dezelfde interacties die Lovable bouwde. Het hele punt is dat niets aan wat Pucks gebruikers zien, mag veranderen. Alleen wat er met de ruwe tekst eronder gebeurt, verandert.

## 15:15 uur — de beoordeling terugschrijven

Dit is het deel dat het meest telt voor een oprichter zonder beveiligingsachtergrond: twaalf bestanden vol niet-geëscapete invoer vertalen naar iets waar Puck daadwerkelijk naar kan handelen zonder een informaticadiploma. De notitie aan haar legt het in feite uit als: "iedereen had code in een reactievak kunnen typen en die konden laten uitvoeren in de browser van een andere gebruiker — we hebben dat overal gesloten waar het bestond en ervoor gezorgd dat het niet op dezelfde manier terug kan komen." Geen muur van jargon. Alleen wat er mis was, waarom het ertoe deed, en wat er is veranderd.

Achter deze ene PR staat Manifera's bredere team van 120+ technici, en beoordelingen zoals deze lopen doorgaans via ons Amsterdamse kantoor aan Herengracht 420, samenwerkend met oprichters door heel Europa die bouwen met Lovable, Bolt, Cursor en v0. Als u wilt zien hoe één beoordeling zoals deze past in het volledige productietraject, schetst onze [procespagina](https://launchstudio.eu/nl/#process) wat ervoor en erna komt. Voor een blik op dezelfde reviewdiscipline toegepast op grotere, langer lopende codebases, laat Manifera's [portfolio](https://www.manifera.com/portfolio/) zien hoe het opschaalt voorbij de app van één oprichter.

## 17:40 uur — PR goedgekeurd, met huiswerk

Aan het eind van de dag zijn Pucks reactiedraadjes en detailpagina voor verzoeken goedgekeurd en gemerged — met de sanitatiefix inbegrepen, niet alleen gemarkeerd zodat zij het zelf moet afhandelen. De wachtrij heeft nog één PR die morgenochtend wacht. Dit is, min of meer, elke dag.

## De Patrooncontrole-Gewoonte van een Oprichter: Hoe U Deze Zelf Uitvoert

De patrooncontrole die in dit artikel wordt beschreven — waarbij u de volledige repository doorzoekt op dezelfde onveilige constructie in plaats van slechts één enkel incident op te lossen — is wellicht de meest waardevolle gewoonte die een niet-technische oprichter kan aanleren. AI-tools herhalen hun patronen immers consistent door de hele codebase. Zo voert u deze controle zelf uit met behulp van uw code-editor (zoals VS Code of Cursor):

**Stap 1: Identificeer het kwetsbare patroon.** Zodra een fout of kwetsbaarheid aan het licht komt — bijvoorbeeld een database-aanroep die gegevens ophaalt zonder `userId`-beperking, zoals `prisma.invoice.findUnique({ where: { id } })` — isoleert u de kern van die aanroep.

**Stap 2: Voer een globale zoekopdracht uit (Ctrl+Shift+F of Cmd+Shift+F).** Zoek in alle bestanden van het project naar vergelijkbare zoektermen, zoals `.findUnique`, `.findMany` of `SELECT * FROM`. Let op de plekken waar query's worden uitgevoerd op gevoelige tabellen zonder dat er een koppeling met de actieve sessie plaatsvindt.

**Stap 3: Controleer API-routes op ontbrekende middleware.** Zoek naar alle router-bestanden (bijvoorbeeld in de map `/api/` of `/routes/`). Controleer of elk bestand consistent dezelfde authenticatie- en autorisatie-middleware aanroept. Valt één endpoint uit de toon omdat de beschermende middleware ontbreekt, dan heeft u een potentiële kwetsbaarheid gevonden.

**Stap 4: Bundel de correcties in één gerichte prompt.** Vraag uw AI-tool niet om de hele applicatie in één keer te herschrijven. Geef juist een gerichte, systematische opdracht: *"In bestand X ontbrak een controle op de gebruikersidentiteit. Ik zie hetzelfde patroon in bestanden Y en Z. Pas bestanden Y en Z aan zodat ze exact hetzelfde autorisatiepatroon afdwingen als de gecorrigeerde versie van bestand X."*

Door van incidentgedreven probleemoplossing over te stappen naar systematische patrooncontrole, verhoogt u de veiligheid van uw gehele applicatie aanzienlijk en voorkomt u dat dezelfde fout zich op tien verschillende pagina's herhaalt.


## Echt voorbeeld

### Een AI-native oprichter in actie: BuurtHulps herhaalde patroon

Puck Willemsen bouwde BuurtHulp zodat buren in Haarlem kleine hulpverzoeken konden plaatsen en erop reageren — meubels verplaatsen, planten water geven terwijl iemand weg is, dat soort dingen. Ze had de reactie- en detailfuncties voor verzoeken gebouwd in Lovable en voelde zich er goed genoeg over om binnen een week een publieke lancering te plannen.

De hierboven beschreven beoordeling vond niet-geëscapete gebruikersinvoer verspreid over twaalf afzonderlijke bestanden — reacties, verzoekomschrijvingen en profielvelden — allemaal volgens hetzelfde onveilige renderpatroon dat Lovable onafhankelijk had gegenereerd in verschillende delen van de app. Onaangeroerd gelaten had elke gebruiker een reactie kunnen indienen met code die zou worden uitgevoerd in de browser van een andere BuurtHulp-gebruiker, een ernstig risico voor een app waarvan het hele doel is om vreemden in dezelfde buurt met elkaar te verbinden.

In plaats van alle twaalf plekken als eenmalige fixes te patchen, bouwden onze technici één enkele gedeelde sanitatiehulpfunctie, leidden elke bestaande aanroepplek daardoorheen, en bevestigden dat Pucks UI er precies zo uitzag en zich zo gedroeg als Lovable die had gebouwd. Elke toekomstige tekstrendercomponent die zij of haar AI-tool nu bouwt, erft het veilige patroon standaard.

**Resultaat:** BuurtHulp lanceerde publiekelijk op schema, met de hele klasse van niet-geëscapeerde-invoerrisico's gesloten, niet alleen het ene geval dat toevallig als eerste werd opgemerkt.

> *"Ik had geen idee dat dezelfde fout op twaalf verschillende plekken zat. Ik dacht dat ik één functie beoordeelde. Het bleek een patroon te zijn."*
> — **Puck Willemsen, oprichter, BuurtHulp (Haarlem)**

**Kosten en tijdlijn:** € 1.050 (repository-brede beoordeling en fix van invoersanitatie) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom kwam hetzelfde onveilige patroon voor in twaalf bestanden in plaats van slechts één?

AI-coderingstools zoals Lovable genereren vaak onafhankelijk soortgelijk ogende componenten in verschillende sessies, waarbij hetzelfde onveilige patroon telkens wordt gereproduceerd in plaats van één veilige implementatie te hergebruiken.

### Duurt een volledige patroonbrede beoordeling veel langer dan een fix in één bestand?

Het duurt langer op de dag dat het gebeurt — Pucks beoordeling nam ongeveer een dag in beslag in plaats van een uur — maar het verwijdert het risico dat hetzelfde probleem opnieuw opduikt in toekomstige functies, wat een eenmalige patch niet doet.

### Herschrijven de engineers van LaunchStudio de frontend van de oprichter tijdens zo'n beoordeling?

Nee — beoordelingen zoals die van Puck zijn afgebakend tot het repareren van de onderliggende logica en renderveiligheid, waarbij de UI precies blijft zoals die is gebouwd in Lovable, Bolt, Cursor of v0.

### Waar is het team gevestigd dat deze pull request-beoordelingen uitvoert?

Beoordelingen voor Europese oprichters zoals Puck lopen doorgaans via het Amsterdamse kantoor van LaunchStudio, ondersteund door Manifera's bredere team van 120+ technici.

### Wat is de daadwerkelijke output van zo'n beoordeling — gewoon een lijst met bugs?

Nee — de output is een gemergede, werkende fix samen met een uitleg in gewone taal van wat er mis was en waarom, niet alleen een gemarkeerde lijst die de oprichter zelf moet oplossen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom kwam hetzelfde onveilige patroon voor in twaalf bestanden in plaats van slechts één?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI-coderingstools zoals Lovable genereren vaak onafhankelijk soortgelijk ogende componenten in verschillende sessies, waarbij hetzelfde onveilige patroon telkens wordt gereproduceerd in plaats van één veilige implementatie te hergebruiken."
      }
    },
    {
      "@type": "Question",
      "name": "Duurt een volledige patroonbrede beoordeling veel langer dan een fix in één bestand?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het duurt langer op de dag dat het gebeurt — Pucks beoordeling nam ongeveer een dag in beslag in plaats van een uur — maar het verwijdert het risico dat hetzelfde probleem opnieuw opduikt in toekomstige functies, wat een eenmalige patch niet doet."
      }
    },
    {
      "@type": "Question",
      "name": "Herschrijven de engineers van LaunchStudio de frontend van de oprichter tijdens zo'n beoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — beoordelingen zoals die van Puck zijn afgebakend tot het repareren van de onderliggende logica en renderveiligheid, waarbij de UI precies blijft zoals die is gebouwd in Lovable, Bolt, Cursor of v0."
      }
    },
    {
      "@type": "Question",
      "name": "Waar is het team gevestigd dat deze pull request-beoordelingen uitvoert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beoordelingen voor Europese oprichters zoals Puck lopen doorgaans via het Amsterdamse kantoor van LaunchStudio, ondersteund door Manifera's bredere team van 120+ technici."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de daadwerkelijke output van zo'n beoordeling — gewoon een lijst met bugs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — de output is een gemergede, werkende fix samen met een uitleg in gewone taal van wat er mis was en waarom, niet alleen een gemarkeerde lijst die de oprichter zelf moet oplossen."
      }
    }
  ]
}
</script>
