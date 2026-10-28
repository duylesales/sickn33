---
Titel: "AI-Appbeveiliging: Voorbereiden op een Penetratietest"
Trefwoorden: ai-appbeveiliging, penetratietest, pentest voorbereiden, scope, herstel, beveiligingsrapport, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# AI-Appbeveiliging: Voorbereiden op een Penetratietest

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Voorbereiden op een Penetratietest",
  "description": "De inkoop van een klant vroeg om een pentestrapport. Wat een test werkelijk dekt, wat u oplost voordat u ervoor betaalt, hoe u de scope bepaalt, en wat u met de bevindingen doet als ze binnenkomen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-preparing-for-a-penetration-test" }
}
</script>

Het verzoek komt meestal binnen in dezelfde e-mail als de verwerkersovereenkomst: hebt u een recent rapport van een penetratietest?

Voor een oprichter wiens product in een paar maanden met AI-tools is gebouwd, is dat een ongemakkelijke vraag. Het is ook een oplosbare vraag, en de volgorde doet ertoe - een test laten uitvoeren voordat u het voor de hand liggende werk hebt gedaan, is een dure manier om te horen wat u al vermoedde.

Een test kost voor een klein product tussen de vier- en vijftienduizend euro. Dat betalen om blootgestelde sleutels en ontbrekende autorisatiecontroles te ontdekken, is een slechte besteding van het geld.

## Wat een Test Is en Wat Niet

Een penetratietest is een in tijd begrensde poging van een professional om uw applicatie te breken, gevolgd door een rapport dat beschrijft wat hij vond, hoe ernstig het is, en hoe het op te lossen.

Het is geen certificering. Het is geen garantie. Het is een momentopname van een specifieke scope op een specifieke datum, en een product dat wekelijks verandert, is een product waarvan het rapport snel veroudert.

Dat doet ertoe voor hoe u het presenteert. "We hadden in maart een test en hebben alle bevindingen opgelost" is een ware en nuttige uitspraak. "We zijn veilig omdat we een pentest hadden" is geen van beide, en ervaren inkopers zien het verschil.

## Los Eerst de Voor de Hand Liggende Dingen Op

Besteed vóór u iets laat uitvoeren een week aan wat een competente tester in een door AI gebouwd product zeker zal vinden. Elk ervan is in deze reeks behandeld, en elk is goedkoop vergeleken met een regel in een rapport die het beschrijft.

Geheimen in de frontendbundel of in de repository. Opslagbuckets die publiek zijn. Ontbrekende autorisatiecontroles op endpoints - de test tussen accounts, systematisch uitgevoerd. Row-level security uitgeschakeld of onvolledig op een tabel. Webhook-endpoints zonder verificatie van handtekeningen. Sessietokens in local storage. Niet-gevalideerde uploads. Enumeration in inlog- en resetprocessen. Afhankelijkheden met bekende kwetsbaarheden in paden voor verzoekafhandeling. Ontbrekende rate limits op authenticatie en dure handelingen.

Anderhalve dag hiervan haalt doorgaans het grootste deel weg van wat anders de sectie met hoge ernst in het rapport zou vullen, en het verandert de economie van de test volledig: u betaalt om te vinden wat u zelf niet kon vinden, in plaats van om te horen wat een checklist had opgevangen.

## De Scope Bepalen Zonder Geld te Verspillen

De scope bepaalt zowel de prijs als het nut. Vier beslissingen.

**Wat erin zit.** De webapplicatie, de API, de authenticatieprocessen, de blootstelling van de database. Meestal niet uw marketingsite. Wees expliciet over diensten van derden, die doorgaans buiten de scope vallen en niet zonder hun toestemming mogen worden getest.

**Hoeveel de tester weet.** Geef documentatie, accounts op elk rechtenniveau, en een beschrijving van de architectuur. Een tester die twee dagen bezig is uw structuur te ontdekken, is een tester die twee dagen niet aanvalt. Black-box-testen is voor sommige doelen passend en is een slechte besteding van een klein budget.

**Welke omgeving.** Een stagingomgeving die identiek is aan productie, met realistische geanonimiseerde data, is het juiste antwoord. Testen tegen productie riskeert echte schade en echte gevolgen voor klanten.

**Of een hertest is inbegrepen.** Dat moet. Bevindingen worden opgelost en daarna gecontroleerd, en een rapport dat vermeldt dat de oplossingen zijn bevestigd, is voor een klant aanzienlijk meer waard dan een rapport met openstaande punten.

## Kiezen Wie Het Doet

Vraag om een geanonimiseerd voorbeeldrapport. Het verschil tussen een goede en een slechte test is direct zichtbaar: goede rapporten leggen de impact uit in zakelijke termen, geven stappen om te reproduceren, en bevelen specifieke oplossingen aan. Slechte rapporten zijn de uitvoer van een scanner met een voorblad.

Vraag welk deel handwerk is. Geautomatiseerd scannen vindt een fractie van wat ertoe doet; autorisatiefouten - het meest voorkomende ernstige probleem in door AI gebouwde producten - worden gevonden door een persoon die over uw applicatie nadenkt.

Vraag wie het werk doet en welke ervaring die heeft met uw stack. En controleer of ze gewend zijn aan kleine producten: een bedrijf waarvan de opdrachten meestal banken zijn, offreert misschien een proces dat u niet nodig hebt en niet kunt opvangen.

## Tijdens de Test

Geef werkende accounts vóór de startdatum, niet op de ochtend zelf. Vertel over bekende problemen in plaats van ze tijd te laten besteden aan het opnieuw ontdekken van wat u al van plan bent op te lossen.

Waarschuw wie uw systemen monitort, zodat een testpiek niet als incident wordt behandeld. Spreek een contactroute af voor alles wat kritiek is en tijdens de test wordt gevonden - een ernstige fout moet u direct bereiken, niet drie weken later in een rapport.

En houd tijdens het venster een normale deploymentstop aan, anders beschrijft het rapport code die niet meer bestaat.

## Het Rapport Is een Werkplan

Een rapport bevat meer bevindingen dan u verwachtte, en de meeste zijn van lage ernst. Behandel ze niet allemaal gelijk.

Los kritieke en hoge bevindingen direct op, voordat het rapport met iemand wordt gedeeld. Los gemiddelde bevindingen op volgens een genoemde tijdlijn. Beslis bij lage en informatieve bevindingen bewust - sommige zijn het oplossen waard, sommige zijn acceptabele risico's, en een gedocumenteerde beslissing om een risico te accepteren is een legitiem en professioneel antwoord.

Maak dan het document dat uw klanten werkelijk willen: een samenvatting met wanneer de test werd uitgevoerd, door wie, wat de scope was, hoeveel bevindingen er waren per ernst, dat de kritieke en hoge bevindingen zijn opgelost en hertest, en de datum van de hertest. Eén pagina. Dat gaat naar inkoop, niet het volledige rapport, dat een kaart van uw applicatie bevat en hooguit onder een overeenkomst moet worden gedeeld.

## Wat een Test U Niet Vertelt

Drie categorieën vallen buiten bijna elke opdracht, en dat weten voorkomt dat u een schoon rapport verwart met een volledig beeld.

**Uw eigen bedrijfsvoering.** Wie toegang heeft tot productie, of de inloggegevens van een vertrokken opdrachtnemer zijn verwijderd, of back-ups zijn getest, of iemand een incident om drie uur 's nachts zou opmerken. Hier begint een substantieel deel van de echte inbreuken, en geen externe test raakt het.

**Uw leveranciers.** De test dekt uw applicatie, niet uw hostingplatform, uw databaseprovider of de model-API die uw AI-functie aanroept. Hun beveiliging wordt geregeld via hun eigen certificeringen en uw contracten, niet via uw rapport.

**De code die na de test is geschreven.** Dit is de ongemakkelijke voor producten die op snelheid worden gebouwd. Een test in maart zegt niets over een agentsessie in juni, en in een product waaraan wekelijks functies worden toegevoegd, beschrijft het rapport iets wat steeds meer geschiedenis wordt.

Dat laatste punt pleit voor een specifieke gewoonte in plaats van meer testen. De checklist voor zelfreview die u tijdens de voorbereiding bouwde - de test tussen accounts, de bundelscan, de bucketcontrole - moet als routine worden uitgevoerd, bij voorkeur geautomatiseerd, in plaats van één keer. Een test is een periodieke externe mening; de routine is wat het antwoord daartussen waar houdt.

Voor de meeste kleine producten is het verstandige ritme een jaarlijkse test, een zelfreview per kwartaal, en geautomatiseerde controles bij elke deployment.

## De Goedkopere Alternatieven, en Wanneer Ze Volstaan

Een volledige opdracht is niet de enige optie, en voor een product waarvan de klanten er nog niet om hebben gevraagd, leveren drie lichtere benaderingen een flink deel van de waarde.

**Een beveiligingsreview van de code.** Een ervaren engineer leest uw applicatie met toegang tot de broncode, op zoek naar de categorieën die ertoe doen. Het is sneller dan een test, meestal goedkoper, en voor door AI gebouwde producten vindt het vaak meer - omdat de fouten structureel zijn en zichtbaar in de code, in plaats van subtiel en in gedrag.

**Een afgebakende beoordeling.** In plaats van het hele product, test de onderdelen die het meest ertoe doen: authenticatie, autorisatie, betalingen, bestandsafhandeling. Twee of drie dagen specialistische aandacht op de plekken waar een mislukking ernstig zou zijn, voor een fractie van de kosten.

**Een beleid voor het melden van kwetsbaarheden.** Een pagina die zegt dat u beveiligingsmeldingen verwelkomt, hoe u bereikbaar bent, en dat u niemand vervolgt die te goeder trouw handelt. Het kost niets en het verandert de persoon die een fout in uw product vindt van iemand die het misschien publiceert in iemand die u mailt. Verschillende incidenten die in deze reeks zijn beschreven, bereikten de oprichter op deze manier.

De volgorde die bij de meeste producten past: direct een meldingsbeleid, een codereview zodra u betalende klanten hebt, een afgebakende beoordeling wanneer u iets gevoeligs verwerkt, en een volledige test wanneer de inkoop van een klant het rapport eist of wanneer het product zo groot is dat het eigen gedrag moeilijk te overzien is geworden.

## Dit Inrichten

Goed voorbereiden kost doorgaans één tot twee weken: de voor de hand liggende bevindingen eerst opgelost via een systematische zelfreview, een stagingomgeving met realistische geanonimiseerde data, documentatie en accounts op elk rechtenniveau voorbereid, de scope gedefinieerd met een hertest inbegrepen, een tester gekozen op basis van een voorbeeldrapport en het aandeel handwerk, een deploymentstop tijdens het venster, directe triage van alles wat kritiek is, herstel van hoge bevindingen vóór het delen, een gedocumenteerde beslissing voor elk geaccepteerd risico met lage ernst, en een samenvatting van één pagina voor klanten.

LaunchStudio doet de voorbereiding en het herstel, en werkt tijdens de opdracht samen met het testbureau. De engineers zijn van Manifera - elf jaar, 120+ engineers, en een lange geschiedenis van getest worden namens klanten als Vodafone, TNO en CFLW.

[Vraag ons eerst de zelfreview uit te voeren](https://launchstudio.eu/nl/#contact). Het kost een fractie van wat het kost om dezelfde dingen in een rapport te vinden.

## Echt voorbeeld

### Twee Rapporten, Zes Maanden Uit Elkaar

Arnoud Steenbergen bouwde Contractbeheer in Lovable: contractbeheer voor facilitaire bedrijven, 22 klanten, waaronder drie regionale ziekenhuisgroepen.

Een inkoopproces van een ziekenhuis vereiste een rapport van een penetratietest. Hij liet er direct een uitvoeren, voor €7.500, door het eerste bureau dat reageerde.

Het rapport bevatte 31 bevindingen: 4 kritiek, 9 hoog. De kritieke waren een service role-sleutel in de frontendbundel, een publieke opslagbucket met getekende contracten, ontbrekende autorisatie op 17 endpoints, en row-level security uitgeschakeld op zes tabellen. Hij had een gespecialiseerd bureau betaald om hem dingen te vertellen die een systematische zelfreview in een dag had blootgelegd, en hij kon het rapport niet met het ziekenhuis delen.

Daarna de voorbereiding, en een tweede test: drie werkdagen zelfreview en herstel op het gebied van sleutels, buckets, autorisatietesten tussen accounts, row-level security, webhookverificatie, sessieopslag, uploadvalidatie, enumeration, afhankelijkheden en rate limits; een stagingomgeving gebouwd met geanonimiseerde productiedata; documentatie en vier accounts op verschillende rechtenniveaus voorbereid; een tweede test met een hertest inbegrepen, voor €6.200, door een bureau dat werd gekozen na het lezen van een geanonimiseerd voorbeeldrapport en de bevestiging dat twee derde van het werk handwerk was.

Het tweede rapport bevatte 11 bevindingen: 0 kritiek, 2 hoog - een fout in de bedrijfslogica waarmee een goedkeuringsstap voor contracten kon worden overgeslagen via een directe API-aanroep, en een gat in de rate limiting bij het genereren van documenten. Geen van beide zou door een checklist zijn gevonden. Beide werden in vier dagen opgelost en hertest.

**Resultaat:** de samenvatting van één pagina ging naar het inkoopteam van het ziekenhuis en het contract werd getekend. Arnoud laat sindsdien jaarlijks een test uitvoeren, en zegt dat de tweede opdracht waardevoller was tegen lagere kosten, omdat de testers hun tijd besteedden aan de werkelijke logica van zijn applicatie in plaats van aan een lijst standaardinstellingen.

> *"Het eerste rapport vertelde me dat mijn voordeur openstond. Daar heb ik zevenenhalfduizend euro voor betaald. Het tweede vond iets waarvoor echt een persoon een week over mijn product moest nadenken."*
> - **Arnoud Steenbergen, Oprichter, Contractbeheer (Ede)**

**Kosten & Doorlooptijd:** €4.900 voor voorbereiding en herstel (zelfreview over tien categorieën, stagingomgeving met geanonimiseerde data, documentatie en testaccounts, herstel na het rapport) - afgerond in 7 werkdagen, naast een externe test van €6.200.

## Veelgestelde vragen

### Moet ik een pentest doen vóór of na het oplossen van voor de hand liggende problemen?

Erna. Een week systematische zelfreview haalt het meeste weg van wat een tester anders zou rapporteren, zodat uw budget bevindingen koopt die u zelf niet had kunnen ontdekken.

### Wat moet een test voor een klein product kosten?

Doorgaans vier- tot vijftienduizend euro, afhankelijk van de scope, met een hertest inbegrepen. Wees voorzichtig met offertes ver daaronder; die wijzen meestal op geautomatiseerd scannen met een voorblad.

### Moeten testers documentatie en accounts krijgen?

Ja. Een tester die twee dagen uw applicatie in kaart brengt, besteedt twee dagen niet aan aanvallen. Black-box-testen is een slechte besteding van een beperkt budget.

### Moet ik elke bevinding oplossen?

Nee. Los kritiek en hoog direct op, gemiddeld volgens een tijdlijn, en beslis bewust over laag en informatief - een gedocumenteerd geaccepteerd risico is een legitiem antwoord.

### Wat stuur ik eigenlijk naar klanten?

Een samenvatting van één pagina: datum, tester, scope, bevindingen per ernst, bevestiging dat de hoge bevindingen zijn opgelost en hertest. Het volledige rapport brengt uw applicatie in kaart en moet niet vrij worden verspreid.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik bekende problemen oplossen voordat ik een pentest laat uitvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Een week systematische zelfreview haalt de meeste voorspelbare bevindingen weg, zodat de test inzicht koopt dat u zelf niet kon opleveren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een penetratietest voor een klein product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal vier- tot vijftienduizend euro met een hertest inbegrepen. Veel goedkopere offertes betekenen doorgaans geautomatiseerd scannen met een voorblad."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten testers documentatie en accounts krijgen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja - tijd die wordt besteed aan het in kaart brengen van uw applicatie is tijd die niet aan aanvallen wordt besteed, en black-box-testen verspilt een klein budget."
      }
    },
    {
      "@type": "Question",
      "name": "Moet elke bevinding worden opgelost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Kritiek en hoog direct, gemiddeld volgens een tijdlijn, en lage bevindingen bewust beoordeeld, met geaccepteerde risico's gedocumenteerd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet na een test met klanten worden gedeeld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een samenvatting van één pagina met datum, tester, scope, aantallen per ernst en bevestigd herstel. Het volledige rapport brengt uw applicatie in kaart."
      }
    }
  ]
}
</script>
