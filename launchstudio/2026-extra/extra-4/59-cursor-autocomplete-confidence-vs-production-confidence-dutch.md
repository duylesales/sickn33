---
Titel: "Het Autocomplete-vertrouwen van Cursor is niet hetzelfde als het productievertrouwen"
Trefwoorden: ai code tool, bolt ai, cursor autocomplete, ai code review, permission check bug
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---
# Het Autocomplete-vertrouwen van Cursor is niet hetzelfde als het productievertrouwen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het Autocomplete-vertrouwen van Cursor is niet hetzelfde als het productievertrouwen",
  "description": "Het automatisch aanvullen van Cursor aarzelt nooit, zelfs niet als het verkeerd is. Dat vertrouwen is precies wat ervoor zorgt dat subtiel onjuiste suggesties \u2013 zoals een toestemmingscontrole die mislukt bij \u00e9\u00e9n rolcombinatie \u2013 snel door de beoordeling komen en de productie bereiken.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/cursor-autocomplete-confidence-vs-production-confidence"
  }
}
</script>

Cursor typt nooit een suggestie voorlopig. Het dekt niet af, signaleert geen onzekerheid, zegt niet "dit zou verkeerd kunnen zijn voor randgevallen." Elke autocomplete ziet er net zo zelfverzekerd uit als alle andere, of het nu een triviale getterfunctie is of een toestemmingscontrole die bepaalt wie gevoelige gegevens kan zien. Dat uniforme vertrouwen is het werkelijke gevaar – niet dat Cursor fouten maakt, zoals elke tool doet, maar dat de fouten er identiek uitzien als de juiste suggesties, en dat een ontwikkelaar die onder druk van deadlines code skimmt, geen visuele of tekstuele aanwijzing heeft die hem vertelt welke welke is.

## De specifieke faalwijze: plausibel, niet correct

Vraag een ervaren ingenieur wat de door AI voorgestelde code gevaarlijk maakt, en het eerlijke antwoord luidt meestal niet: "Het levert kapotte code op die duidelijk niet werkt." Kapotte code wordt onmiddellijk opgemerkt: er treedt een fout op, de test mislukt en de code wordt niet gecompileerd. De gevaarlijke categorie is code die *plausibel* is – syntactisch schoon, logisch coherent bij de eerste keer lezen, consistent met de patronen die al in het bestand aanwezig zijn – terwijl deze op subtiele wijze verkeerd is op een manier die zich alleen manifesteert onder een specifieke voorwaarde die niemand toevallig heeft getest. Toestemmings- en autorisatielogica is een van de plaatsen met het hoogste risico voor precies dit patroon, omdat het aantal rolcombinaties snel groeit, en een controle die tijdens de ontwikkeling de drie meest voorkomende combinaties correct afhandelt, nog steeds verkeerd kan zijn voor de vierde, die pas verschijnt zodra echte gebruikers met echte roltoewijzingen het product gaan gebruiken.

Dit is geen kritiek die uniek is voor Cursor; Bolt, Lovable en elke andere AI-codeerassistent draagt ​​hetzelfde structurele risico met zich mee. Maar het is vooral relevant voor technische solo-oprichters die specifiek Cursor gebruiken, omdat de workflow van Cursor is opgebouwd rond snelle, inline autocomplete die wordt geaccepteerd met een toetsaanslag, wat een fundamenteel sneller en minder wrijvingsmoment is dan het beoordelen van een groter, door AI gegenereerd codeblok dat vanuit een chatinterface is geplakt. De snelheid is de volledige waardepropositie van inline automatisch aanvullen. Het is ook precies de reden waarom een ​​subtiel verkeerde suggestie eerder doorsijpelt: er is minder natuurlijke pauze ingebouwd in de workflow voor controle.

## Waarom een ​​snelle doorlezing dit niet duidelijk maakt

Een bug voor de toestemmingscontrole die alleen onder één specifieke rolcombinatie mislukt, is door zijn constructie onzichtbaar voor een snelle doorlezing en vaak ook onzichtbaar voor handmatig testen, tenzij iemand specifiek die exacte combinatie construeert en test. Tijdens de ontwikkeling test een oprichter die zijn eigen product test, doorgaans als zichzelf: één rol, misschien twee als hij een tweede testaccount heeft aangemaakt. In geen van beide kondigt de bug zichzelf aan. Het wacht op een echt productiescenario: een gebruiker die toevallig twee rollen tegelijkertijd bekleedt, of een toestemming die is geërfd via een teamstructuur die geen deel uitmaakte van de oorspronkelijke testmatrix, en pas dan blokkeert de onjuiste controle iemand die toegang zou moeten hebben of, erger nog, toegang verlenen aan iemand die deze niet zou moeten hebben.

Zoals Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, het verwoordt: “We zien een verschuiving in de softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig is om die producten tot volwassenheid te brengen. Precies daarin hebben we elf jaar ervaring.” Toestemmingslogica is een nauwkeurig voorbeeld van deze verschuiving: Cursor heeft de oplossing 'kan ik snel een rolcontrole schrijven' opgelost, maar niemand heeft de oplossing 'dekt deze rolcontrole correct elke combinatie die in de productie bestaat' op, omdat daarvoor een systematisch beoordelingsproces vereist is, en niet slechts een werksuggestie.

## Wat deze kloof dicht

De oplossing wantrouwt Cursor in het algemeen niet; de automatische aanvulling ervan is echt nuttig en zorgt ervoor dat de grote meerderheid van de suggesties goed is. De oplossing is het opzettelijk nauwkeuriger onderzoeken van specifieke categorieën code waarbij een subtiele fout grote gevolgen heeft: authenticatie, autorisatie, betalingslogica en alles wat maar in aanraking komt met de grenzen van gegevenstoegang. Voor deze categorieën is een snelle doorlezing niet voldoende; ze hebben een expliciete testmatrix nodig die elke realistische rol- en toestemmingscombinatie omvat, niet alleen de twee of drie die tijdens de normale ontwikkeling worden gebruikt. Onze technici, die werken vanuit Manifera's hub in Singapore, passen precies dit soort gerichte beoordelingen toe bij het auditen van een door AI gebouwde codebase voordat deze naar productie gaat. Ze beoordelen niet elke regel met dezelfde intensiteit, maar concentreren hun onderzoek op de categorieën code waarbij 'plausibel maar fout' echte schade veroorzaakt.

Als je een beoordeling van de toestemming en toegangscontrole wilt laten uitvoeren op een door Cursor gebouwd product voordat meer gebruikers ervan afhankelijk zijn, legt onze pagina [hoe het werkt](https://launchstudio.eu/en/#process) uit hoe LaunchStudio dat soort audits aanpakt, en Manifera's praktijk voor [aangepaste softwareontwikkeling](https://www.manifera.com/services/custom-software-development/) heeft vergelijkbare autorisatiebeoordelingen uitgevoerd voor bedrijfssystemen met veel meer rolcomplexiteit dan een typisch SaaS-product in een vroeg stadium.

## Echt voorbeeld

### Een AI-native oprichter in actie: de rollencombinatie die niemand heeft getest

Twan Buitenhuis, een technische solo-oprichter in Coevorden, bouwde TicketVolg – ​​een interne IT-ticketingtool – met behulp van Cursor. Tijdens het implementeren van toegangscontroles voor wie tickets kon bekijken en oplossen, suggereerde Cursor's autocomplete vol vertrouwen een toestemmingscontrole die er correct uitzag en exact overeenkwam met het patroon van de omringende code.

De suggestie werd door Twan zelf snel doorgelezen tijdens de ontwikkeling, en ook door zijn handmatige tests, omdat zijn tests de standaardrolcombinaties bestreken waarvan hij verwachtte dat ze er toe zouden doen: gewone gebruikers, beheerders en ondersteuningsagenten, individueel getest. De controle was specifiek onjuist voor één combinatie – een gebruiker die tegelijkertijd de rol van ondersteuningsagent en afdelingsleider vervulde – een combinatie die niet bestond in de testaccounts van Twan, maar wel bestond onder zijn daadwerkelijke vroege gebruikers toen TicketVolg echt in gebruik werd genomen. Die combinatie zorgde ervoor dat de toestemmingscontrole ten onrechte de toegang ontzegde tot tickets die de gebruiker had moeten kunnen zien.

De technici van LaunchStudio hebben het volledige toestemmingssysteem van TicketVolg beoordeeld, niet alleen de gemarkeerde controle, en een goede rolcombinatietestmatrix gebouwd die elke realistische combinatie van rollen omvatte in plaats van alleen de individueel geteste rollen die Twan had gecontroleerd. De gemarkeerde toestemmingslogica is herschreven om gecombineerde rollen correct te evalueren, en de nieuwe testmatrix draait nu als onderdeel van elke toekomstige wijziging aan het toegangscontrolesysteem, zodat een soortgelijk gat niet meer onopgemerkt de productie kan bereiken.

**Resultaat:** Het toestemmingssysteem van TicketVolg verwerkt nu elke realistische rolcombinatie correct, en Twan beschikt over een echte testmatrix in plaats van te vertrouwen op een snelle handmatige controle voordat wijzigingen in de toegangscontrole worden verzonden.

> *"De code zag er precies zo betrouwbaar uit als al het andere dat Cursor die week had gesuggereerd. Er was niets dat zei: 'Controleer deze nog eens.'"*
> — **Twan Buitenhuis, oprichter, TicketVolg (Coevorden)**

**Kosten en tijdlijn:** € 900 (beoordeling van het toestemmingssysteem, testmatrix voor rolcombinaties en oplossing voor de gemarkeerde bug in toegangscontrole) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Moet ik stoppen met het gebruik van Cursor's autocomplete voor gevoelige logica?

Niet noodzakelijkerwijs: de autocomplete zelf is een echt nuttig hulpmiddel; De oplossing is het doelgerichter onderzoeken van specifieke categorieën als authenticatie en machtigingen, in plaats van te vertrouwen op een snelle doorlezing, zoals je dat zou doen bij code met een lagere inzet.

### Hoe bouw ik een rolcombinatietestmatrix als ik er nog nooit een heb gedaan?

Begin met het vermelden van elke rol of toestemming die uw product heeft, en test vervolgens expliciet elke realistische combinatie van twee of meer rollen die een echte gebruiker tegelijkertijd kan vervullen, en niet alleen elke geteste rol.

### Geldt dit probleem alleen voor Cursor, of hebben andere AI-coderingstools dit ook?

Het geldt voor alle AI-coderingstools – inclusief Bolt, Lovable, v0 –. Het onderliggende risico is dat de door AI gegenereerde code geen zichtbaar vertrouwenssignaal met zich meebrengt, zodat een subtiel verkeerde suggestie identiek lijkt aan een correcte suggestie, ongeacht welke tool deze heeft geproduceerd.

### Wat bedoelt Herre Roelevink met ‘architectuur en veiligheid die nodig zijn om producten tot volwassenheid te brengen’?

Hij beschrijft de kloof tussen code die werkt in de scenario's waartegen het is getest en code die systematisch is beoordeeld op de scenario's waarin dat niet het geval was. Dit laatste is waar Manifera's ruim elf jaar productie-engineering-ervaring omheen is gebouwd.

### Wie controleert dit soort toestemmingen bij LaunchStudio?

De beoordeling wordt uitgevoerd door het technische team van Manifera, inclusief de groep gevestigd in de hub in Singapore, waarbij hetzelfde systematische toegangscontroletestproces wordt toegepast dat wordt gebruikt bij de zakelijke opdrachten van Manifera.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I stop using Cursor's autocomplete for sensitive logic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily \u2014 the fix is applying more deliberate scrutiny specifically to categories like authentication and permissions, rather than trusting a quick read-through."
      }
    },
    {
      "@type": "Question",
      "name": "How do I build a role-combination test matrix if I've never done one?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "List every role or permission your product has, then explicitly test every realistic combination of two or more roles a real user might hold simultaneously."
      }
    },
    {
      "@type": "Question",
      "name": "Does this issue only apply to Cursor, or do other AI coding tools have it too?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It applies to any AI coding tool \u2014 the underlying risk is that AI-generated code carries no visible confidence signal, so a wrong suggestion looks identical to a correct one."
      }
    },
    {
      "@type": "Question",
      "name": "What does Herre Roelevink mean by architecture and security needed to bring products to maturity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "He's describing the gap between code tested against known scenarios and code systematically reviewed for scenarios it wasn't \u2014 the latter is what Manifera's 11+ years of production engineering experience addresses."
      }
    },
    {
      "@type": "Question",
      "name": "Who does this kind of permission review at LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The review is carried out by Manifera's engineering team, including the group based at the Singapore hub, using the same access-control testing process applied across Manifera's enterprise engagements."
      }
    }
  ]
}
</script>