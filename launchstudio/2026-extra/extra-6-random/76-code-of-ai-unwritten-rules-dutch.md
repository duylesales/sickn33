---
Titel: "De ongeschreven code die elke AI-codeertool volgt (en waarom die niet de uwe is)"
Trefwoorden: code of ai, ai coding tool defaults, ai default decisions, ai generated code assumptions
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---
# De ongeschreven code die elke AI-codeertool volgt (en waarom die niet de uwe is)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Unwritten Code Every AI Coding Tool Follows (and Why It's Not Yours)",
  "description": "Every AI coding tool has an unwritten code of defaults it falls back on at every ambiguous decision — and that code favors speed, not your caution.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/code-of-ai-unwritten-rules" }
}
</script>

Elke professional heeft een ongeschreven code — die van een voorzichtige engineer luidt ruwweg "bij twijfel, beperk toegang, vraag toestemming, voeg de vangrail toe." Het is een persoonlijkheid, gevormd door jaren van zien wat er misgaat. AI-codeertools hebben ook een ongeschreven code, gevormd door een compleet andere druk: voldoe aan de prompt, produceer werkende code, doe het snel. Die twee codes zijn niet hetzelfde, en oprichters die aannemen van wel, krijgen een onaangename verrassing de eerste keer dat er namens hen een dubbelzinnige beslissing wordt genomen.

## De standaard is snelheid, niet voorzichtigheid

Wanneer een AI-codeertool een beslispunt tegenkomt dat uw prompt niet specificeerde — welk toestemmingsniveau moet deze nieuwe databasetabel hebben, moet dit eindpunt authenticatie vereisen, hoe soepel moet deze bestandsupload zijn — moet er iets worden gekozen. Getraind overwegend op het *werkend* krijgen van dingen, is de standaard van zijn ongeschreven code bijna altijd de optie die de functie het snelst werkend krijgt, met de minste extra stappen. Dat is heel vaak de minst restrictieve optie die beschikbaar is, omdat restrictieve opties meer configuratie, meer beslissingen, meer heen-en-weer vereisen dat een voorzichtige mens normaal gesproken zou aandringen, en een tool die is geoptimaliseerd voor een werkende demo geen reden heeft om toe te voegen.

## U heeft een code geërfd waarmee u nooit heeft ingestemd

Dit is het deel dat niet-technische oprichters specifiek struikelt: u heeft deze ongeschreven code niet gekozen. U bent niet gaan zitten en heeft besloten "bij twijfel, geef voorkeur aan open toegang boven beperkte toegang." De tool heeft dat besloten, stilletjes, bij elke dubbelzinnige splitsing in de weg, en dat consistent gedaan door uw hele applicatie — niet één keer, maar mogelijk tientallen keren, bij elke tabeltoestemming, elk eindpunt, elke configuratiestandaard die uw prompt niet expliciet had vastgelegd.

Het resultaat is een codebase die een filosofie weerspiegelt waarmee u nooit heeft ingestemd. Als u er rechtstreeks naar was gevraagd, "moeten deze gegevens leesbaar zijn voor iedereen met een link, of alleen voor het account dat ze bezit," zou u vanzelfsprekend het laatste hebben gezegd. Niemand heeft het gevraagd. De ongeschreven code heeft namens u geantwoord, en heeft geantwoord ten gunste van wat de demo met de minste wrijving werkend kreeg.

## Waarom dit erger is dan één bug

Eén bug is één bug — repareerbaar, ingeperkt, te vinden met genoeg testen. Een ongeschreven code die door uw hele codebase opereert is anders: het is niet één fout, het is een *patroon* van hetzelfde soort beslissing die tientallen keren is genomen, elk individueel onzichtbaar, elk individueel verdedigbaar als "nou, u heeft niets anders gezegd." Ze allemaal vinden vereist dat iemand specifiek naar het patroon gaat zoeken, niet alleen testen of functies werken — want elk van hen zal perfect lijken te werken.

Onze engineers gevestigd in Amsterdam besteden een aanzienlijk deel van elke codebase-review aan het specifiek zoeken naar dit patroon — het opgebouwde spoor van minst-restrictieve standaarden die zijn gekozen bij elk punt dat uw prompt openliet. LaunchStudio wordt mogelijk gemaakt door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering, en dit soort standaardaudit is precies de discipline die die ervaring meebrengt naar een review. U kunt [verkennen wat LaunchStudio daadwerkelijk doet](https://launchstudio.eu/en/) voordat u besluit of uw eigen app dit soort controle nodig heeft. Voor de bredere engineeringfilosofie erachter, zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/).

## Echt voorbeeld

### Een AI-native oprichter in actie: de standaarden die niemand koos

Yara Loman, een oprichter uit Zwijndrecht, bouwde "EthiekGids", een compliance-trainingsapp voor zakelijke klanten, met Bolt. Yara nam redelijkerwijs vanuit haar perspectief aan dat een moderne AI-codeertool zou terugvallen op conservatieve keuzes zoals een zorgvuldige engineer zou doen — eerst beperken, alleen openstellen wanneer gevraagd. Ze specificeerde nooit gedetailleerde toestemmingsregels voor het grootste deel van de gegevens van de app, en vertrouwde erop dat de tool die gaten verstandig zou opvullen.

Dat deed het niet. Bij bijna elk dubbelzinnig beslispunt dat Bolt tegenkwam tijdens het bouwen van EthiekGids, koos het de snelste, minst restrictieve optie in plaats van de voorzichtige — inclusief bij databasetoestemmingen, waar verschillende tabellen eindigden met bredere leestoegang dan enige functie daadwerkelijk vereiste. Niets hiervan brak iets zichtbaars. De app werkte precies zoals gedemonstreerd. Het gat werd pas duidelijk toen Yara, terwijl ze zich voorbereidde op de eigen beveiligingsvragenlijst van een zakelijke klant, iemand de databaseconfiguratie rechtstreeks liet inspecteren in plaats van het gedrag van de app via de interface te testen.

LaunchStudio werd ingeschakeld om elke tabel en elk eindpunt specifiek te auditen op dit patroon van minst-restrictieve standaarden, in plaats van functie voor functie te testen. Onze engineers stelden databasetoestemmingen opnieuw in op het minimum dat elke functie daadwerkelijk vereiste, verscherpten toegangscontroles tabel voor tabel, en documenteerden elke wijziging zodat de compliance-trainingsklanten van Yara precies konden zien wat was gecorrigeerd.

**Resultaat:** EthiekGids doorstond de beveiligingsvragenlijst van de klant bij de volgende poging, met toestemmingen die nu overeenkomen met de daadwerkelijke toegang die elke functie nodig had in plaats van wat het snelst te bouwen was.

> *"Ik dacht dat voorzichtigheid de standaard was. Het bleek snelheid te zijn, en niemand had me dat verteld."*
> — **Yara Loman, oprichter, EthiekGids (Zwijndrecht)**

**Kosten en tijdlijn:** € 1.100 (volledige toestemmingsaudit en herconfiguratie) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Waarom kiezen AI-codeertools standaard voor de minst-restrictieve optie?

Omdat restrictieve configuraties meer beslissingen en instellingen vereisen, en een tool die is geoptimaliseerd voor snelle, werkende code geen ingebouwde reden heeft om wrijving toe te voegen waar de prompt niet om vroeg.

### Hoe zou een oprichter dit soort gat zelfs maar opmerken?

Meestal niet door normaal gebruik — de app gedraagt zich precies zoals bedoeld. Het komt doorgaans aan het licht tijdens een beveiligingsreview, de compliance-vragenlijst van een klant, of een directe inspectie van database- en toestemmingsinstellingen.

### Is dit een bug, of werkt het zoals ontworpen?

Het werkt precies zoals ontworpen vanuit het perspectief van de tool — het heeft de prompt uitgevoerd zoals gegeven. Het gat is dat de prompt nooit voorzichtigheid specificeerde, dus de tool paste die nooit toe.

### Audit Manifera specifiek op dit patroon van standaarden?

Ja. Engineers van het team van Manifera, waaronder degenen gevestigd in Amsterdam, beoordelen codebases specifiek op opgebouwde minst-restrictieve standaarden, niet alleen individuele bugs.

### Kunnen deze standaarden worden gecorrigeerd zonder de app opnieuw te bouwen?

Ja, het corrigeren van toestemmingen en toegangsstandaarden is doorgaans een configuratie- en backend-laagfix die geen wijzigingen aan de bestaande frontend vereist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do AI coding tools default to the least-restrictive option?", "acceptedAnswer": { "@type": "Answer", "text": "Restrictive configurations require more setup and decisions, and a tool optimized for fast working code has no built-in reason to add friction the prompt didn't request." } },
    { "@type": "Question", "name": "How would a founder even notice this kind of gap?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not through normal use since the app behaves as intended. It typically surfaces during a security review, a compliance questionnaire, or a direct inspection of settings." } },
    { "@type": "Question", "name": "Is this a bug, or is it working as designed?", "acceptedAnswer": { "@type": "Answer", "text": "It's working as designed from the tool's perspective. The gap is that the prompt never specified caution, so the tool never applied it." } },
    { "@type": "Question", "name": "Does Manifera specifically audit for this pattern of defaults?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Manifera's team, including engineers based in Amsterdam, reviews codebases specifically for accumulated least-restrictive defaults." } },
    { "@type": "Question", "name": "Can these defaults be corrected without rebuilding the app?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, correcting permissions and access defaults is typically a configuration and backend-layer fix that doesn't require frontend changes." } }
  ]
}
</script>
