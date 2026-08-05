---
Titel: "AI-software-engineeringprincipes die uw prototype heeft overgeslagen"
Trefwoorden: ai software engineering, ai coding, ai native, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# AI-software-engineeringprincipes die uw prototype heeft overgeslagen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-software-engineeringprincipes die uw prototype heeft overgeslagen",
  "description": "Een checklist voor productiegereedheid gekaderd rond klassieke software-engineeringprincipes die AI-coderingsassistenten niet automatisch toepassen.",
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
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-software-engineering-principles-your-prototype-skipped"
  }
}
</script>

Traditionele software-engineering heeft altijd gerust op een handvol onglamoureuze principes: vertrouw clientinvoer nooit, valideer bij elke grens, neem aan dat het netwerk onbetrouwbaar is. AI-software-engineering, zoals het in de praktijk gebracht wordt via prompten en generatie, heeft de neiging om rechtstreeks door te slaan naar functionaliteit – omdat geen van die principes zichtbaar zijn in een werkende demo, en niemand expliciet de tool heeft gevraagd om ze toe te passen.

## Principe één: Vertrouw nooit gegevens afkomstig van de client

**Controle:** valideert uw server onafhankelijk elke waarde die vanaf de frontend wordt ingediend, of neemt het aan dat de frontend de regels (minimale bestelhoeveelheid, geldig prijsbereik, verplichte velden) al heeft afgedwongen voordat het verzoek arriveerde? Met AI gegenereerde formulieren dwingen deze regels frequent prachtig af in de UI, terwijl ze ze nooit opnieuw controleren zodra de gegevens de server bereiken. Dit betekent dat iedereen die de UI volledig omzeilt kan indienen wat hij maar wil.

## Principe twee: Neem aan dat elke numerieke invoer gemanipuleerd kan worden

**Controle:** kan een hoeveelheidsveld, een prijsveld, of een kortingsveld een negatief getal, een nul, of een onredelijk grote waarde accepteren zonder dat de server het weigert? Een negatieve hoeveelheid op een bestelling, bijvoorbeeld, kan soms worden verwerkt als een geldige transactie door backend-logica die alleen ooit getest is met positieve, redelijke waarden. Dit resulteert er af en toe in dat een berekend totaal werkt in het voordeel van de aanvrager in plaats van dat van het bedrijf. Dit is geen hypothetisch randgeval bedacht omwille van een checklist – het is precies het mechanisme achter Niels's MakerLink-incident, waar een hoeveelheidsveld vermenigvuldigd met een prijs per eenheid een negatief totaal produceerde. En dat negatieve totaal, verwerkt door betalingslogica die alleen een waarde verwachtte die in één richting bewoog, werd verwerkt als een creditering op de rekening van de klant in plaats van een afschrijving. De onderliggende rekenkunde was volledig correct; niemand had het ooit verteld dat een negatieve hoeveelheid niet toegestaan zou moeten worden om die rekenkunde in de eerste plaats te bereiken.

## Principe drie: Valideer bij elke grens, niet alleen bij de eerste

**Controle:** als uw applicatie meerdere toegangspunten heeft tot dezelfde onderliggende gegevens – een webformulier, een openbare API, een functie voor het in bulk importeren – wordt validatie dan consequent toegepast over alle toegangspunten, of alleen bij het ene toegangspunt dat een oprichter toevallig het meest grondig heeft getest? Een validatieregel die op het hoofdformulier wordt afgedwongen maar vergeten wordt op een secundair API-eindpunt biedt überhaupt geen echte bescherming, aangezien het secundaire eindpunt de duidelijke manier eromheen wordt.

## Principe vier: Ontwerp voor het misvormde verzoek, niet alleen het verwachte

**Controle:** wat doet uw applicatie wanneer het een verzoek ontvangt dat niet overeenkomt met enige invoer die een oprichter had voorzien – een tekenreeks waar een getal werd verwacht, een ontbrekend verplicht veld, een extra onverwachte parameter? Applicaties die alleen getest zijn tegen verwachte invoer reageren op misvormde invoer vaak op ongedefinieerde, soms misbruikbare manieren, in plaats van het schoon te weigeren met een duidelijke foutmelding.

## Principe vijf: Behandel server-side validatie als niet-onderhandelbaar, niet als overtollig

**Controle:** is er een verleiding om server-side validatie te overslaan omdat "de frontend het al controleert"? Die verleiding is begrijpelijk en extreem gebruikelijk in met AI gegenereerde code, aangezien het dupliceren van validatielogica op twee plekken overtollig voelt tijdens de ontwikkeling. Maar de frontend-controle en de backend-controle beantwoorden twee verschillende vragen, en alleen de backend-controle is daadwerkelijk afdwingbaar tegen een vastberaden gebruiker.

## Een snelle zelftest: Vijf verzoeken die het waard zijn om te proberen tegen uw eigen applicatie

Kloven in invoervalidatie zijn ongebruikelijk gemakkelijk voor een oprichter om rechtstreeks te testen, zonder een regel code te lezen. De test is namelijk simpelweg "probeer iets onredelijks in te dienen en kijk wat er gebeurt." Niets hiervan vereist technische vaardigheid – het vereist een specifieke, vijandige denkmoed die het meeste functionele testen volledig overslaat.

**Vijf dingen die het waard zijn om te proberen op elk formulier met een getal:**

1. **Een negatief getal** waar alleen positieve waarden logisch zijn — een hoeveelheid, een duur, een beoordeling. Een goed gevalideerd veld weigert het meteen; een slecht gevalideerd veld kan het verwerken en een onzinnig of misbruikbaar resultaat produceren.
2. **Nul**, waar nul een logisch vreemde of betekenisloze waarde is — een bestelling met nul hoeveelheid, een boeking van nul nachten. Sommige applicaties handelen dit genadig af; andere produceren een berekeningsfout of een onbedoeld gratis resultaat.
3. **Een enorm getal** — negen cijfers in plaats van een of twee — in een veld dat een normale, kleine waarde verwacht. Dit kan af en toe overflow-gedrag triggeren, of simpelweg onthullen dat er nooit een bovengrens werd overwogen.
4. **Een decimaal getal waar een geheel getal wordt verwacht**, of tekst waar een getal wordt verwacht. Een veld dat stilletjes "3.7 eenheden" accepteert van iets dat alleen redelijkerwijs kan bestaan in gehele eenheden, of dat fouten geeft op een verwarrende manier in plaats van een schone weigering, is een teken dat validatie niet specifiek werd overwogen voor dat veld.
5. **Hetzelfde formulier twee keer snel achter elkaar indienen** — dubbelklikken op een knop "bestelling plaatsen" of "betaling indienen". Zonder bescherming tegen dubbele indiening kan dit soms twee records, twee afschrijvingen, of twee van wat het formulier verondersteld werd exact één keer aan te maken veroorzaken.

**Wat te doen met wat u vindt:** geen van deze testen, op zichzelf, vertelt u hoe u het onderliggende probleem veilig kunt herstellen – dat vereist nog steeds iemand die server-side validatie correct kan implementeren, het kan testen tegen elk toegangspunt (niet alleen het formulier dat u geprobeerd heeft), en kan bevestigen dat de herstelling legitieme randgevallen zoals een oprecht grote maar geldige bestelling niet breekt. Maar het zelf doorlopen van deze vijf-item lijst, op uw eigen product, voorafgaand aan een gesprek met een ingenieur, veranderd een vage "kun je controleren of mijn validatie oké is" in een specifieke "dit is wat ik vond toen ik X, Y en Z probeerde." Dit heeft de neiging de resulterende beoordeling sneller en preciezer afgebakend te maken vanaf het allereerste gesprek.

## Hoe het sluiten van deze kloven er in de praktijk uitziet

Een grondige validatiestap past consistente, server-side regels toe over elk toegangspunt dat een systeem blootstelt, waardoor misvormde en vijandige invoer opgevangen wordt voordat het de bedrijfslogica bereikt. [LaunchStudio](https://launchstudio.eu/en/) voert exact dit soort validatie-audit uit als onderdeel van haar standaard beoordeling, ondersteund door Manifera's 11+ jaar ervaring met enterprise software engineering toegepast op producten op oprichterschaal.

Manifera's validatie- en uithardingswerk wordt voornamelijk uitgevoerd via haar ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld via het kantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: De bestelling die in plaats daarvan de klant betaalde

Niels, een voormalig drukkerijmanager die oprichter werd in Nijmegen, bouwde MakerLink, een AI-ondersteunde marktplaats voor freelancers gebouwd met v0 die kleine fabrikanten verbindt met klanten voor aangepaste bestellingen, waarbij ordertotalen worden berekend uit een hoeveelheidsveld en een prijs per eenheid.

Een klant die uit nieuwsgierigheid randgevallen testte diende een negatieve hoeveelheid in op een aangepaste bestelling en ontving een berekend totaal dat de rekening crediteerde in plaats van afschreef. LaunchStudio's beoordeling bevestigde dat het besteleindpunt hoeveelheid valideerde als een verplicht veld, maar nooit controleerde dat het een positief getal was, noch op het formulier noch op de server.

**Resultaat:** LaunchStudio voegde consistente server-side validatie toe over elk bestelgerelateerd eindpunt, waardoor negatieve, nul-, of onredelijke hoeveelheids- en prijswaarden werden geweigerd, ongeacht welk toegangspunt ze indiende.

> *"Een klant vond dit per ongeluk tijdens het testen van iets ongerelateerds en vermeldde het bijna als een grap. Het had oprecht aanzienlijk langer onopgemerkt kunnen blijven dan het deed."*
> — **Niels Kramer, Oprichter, MakerLink (Nijmegen)**

**Kosten en tijdlijn:** € 2.000 (audit van invoervalidatie over bestel- en prijseindpunten) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een QA-ingenieur typisch testen op negatieve hoeveelheden als onderdeel van standaard functioneel testen?

Niet altijd – standaard functionele QA is vaak gebouwd rond "werkt dit met verwachte invoer," en het testen van opzettelijk onredelijke invoer (negatieve getallen, extreme waarden) vereist een specifieke vijandige denkmoed die niet automatisch onderdeel is van elk QA-proces.

### Geldt dit soort kloof alleen voor marktplaats- of e-commerceproducten, of geldt het breder?

Het geldt voor in feite elk product met numerieke invoer die een berekening voedt – hoeveelheden, prijzen, duur, kortingen. Dit betekent dat boekingsplatformen, abonnements-tools en facturatiesystemen allemaal voor hetzelfde risico staan.

### Manifera heeft decennia aan gecombineerde engineeringervaring over enterprise-systemen — vertaalt dat zich rechtstreeks naar het opvangen van een randgeval zoals dat van MakerLink?

Ja, rechtstreeks – enterprise software engineering heeft grens- en randgevalvalidatie altijd behandeld als een eersteklas zorg in plaats van een nagedachte. Die discipline brengt zich schoon over op producten op oprichterschaal.

### Is er een reden waarom AI-tools niet gewoon numerieke bereiken standaard valideren zonder dat het gevraagd wordt?

Doorgaans omdat een tool reageert op wat beschreven is, en "hoeveelheidsveld" impliceert niet inherent "moet negatieve waarden weigeren" tenzij de beperking expliciet vermeld is – de tool faalt niet in zijn taak, het voltooit simpelweg een smallere taak dan de oprichter aannam.

### Als ik deze vijf testen zelf probeer en er breekt niets, betekent dat dan dat mijn validatie volledig gedekt is?

Nee – het betekent dat de specifieke paden die u getest heeft standhielden, niet dat elk toegangspunt dat deed. Een formulier kan correct valideren terwijl een secundair API-eindpunt dat dezelfde onderliggende gegevens bereikt dat niet doet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Testen standaard QA-processen op randgevallen zoals negatieve hoeveelheden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet altijd — dit vereist een specifieke vijandige denkmoed die niet automatisch onderdeel is van QA."
      }
    },
    {
      "@type": "Question",
      "name": "Geldt deze validatiekloof alleen voor marktplaatsproducten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het geldt voor elk product met numerieke invoer die een berekening voedt, zoals boekingen of abonnementen."
      }
    },
    {
      "@type": "Question",
      "name": "Vertaalt enterprise engineering-ervaring zich naar het opvangen van randgevallen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, grens- en randgevalvalidatie is altijd als eersteklas behandeld in enterprise engineering discipline."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom valideren AI-tools numerieke bereiken niet standaard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De tool voltooit de smallere taak die beschreven is, niet de bredere taak die een oprichter aannam."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe wordt de vaste prijs besloten voor een validatie-beoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het introductiegesprek bepaalt het daadwerkelijke aantal toegangspunten dat beoordeling nodig heeft."
      }
    },
    {
      "@type": "Question",
      "name": "Als deze 5 testen slagen, is mijn validatie dan volledig gedekt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — het betekent dat geteste paden standhielden, niet dat elk secundair API-eindpunt dat doet."
      }
    }
  ]
}
</script>
