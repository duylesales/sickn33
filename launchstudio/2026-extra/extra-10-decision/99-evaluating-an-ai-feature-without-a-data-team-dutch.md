---
Titel: "Een AI-Feature Evalueren Zonder Data Science Team"
Trefwoorden: LLM evaluatie klein team, golden test set prompts, regressietesten AI output, meten AI kwaliteit SaaS, prompt aanpassingen testen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Een AI-Feature Evalueren Zonder Data Science Team

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-Feature Evalueren Zonder Data Science Team",
  "description": "Zonder gestructureerde evaluatie is elke promptwijziging een blinde gok. Hoe een solo-oprichter in één middag een 'golden test set' van 40 voorbeelden bouwt, welke eigenschappen u moet meten en hoe u kwaliteitsregressies voorkomt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-31",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/evaluating-an-ai-feature-without-a-data-team" }
}
</script>

Reguliere softwarecode heeft geautomatiseerde unittests: een functie geeft de verwachte waarde terug (`assert result == expected`), of de test faalt.

Bij AI-features ontbreekt deze binaire zekerheid volledig. 
Het gevolg is dat de meeste solo-ontwikkelaars en indie-hackers hun prompts aanpassen op basis van onderbuikgevoel:
1. U past een paar zinnen aan in uw systeemprompt in Cursor of Lovable.
2. U probeert twee of drie willekeurige voorbeeldjes uit in een testinterface.
3. U denkt: *"Mooi, dit ziet er goed uit!"* en u pusht de code direct naar productie.

Dit proces heeft een blind vlek:
**Het kan niet detecteren dat de promptwijziging die uw specifieke testcase zojuist oploste, tegelijkertijd vier andere categorieën geruisloos heeft gesloopt.**

Zonder evaluatieraamwerk is elke aanpassing een munt opgooien. Over meerdere iteraties resulteert dit in een product dat weliswaar *anders* reageert, maar per saldo niet *beter* wordt.

De remedie vereist geen duur data science team met vijf PhD's en geen ingewikkelde machine learning-infrastructuur:
**U heeft slechts 30 tot 50 echte praktijkvoorbeelden en een gestructureerd script nodig.** Het kost u één middag om op te zetten, en het geeft u het vermogen om de vraag *"Heeft deze promptwijziging ons product echt verbeterd?"* te beantwoorden met harde data in plaats van aannames.

## Bouw een 'Golden Test Set' van Echte Klantdata

Een testset van dertig tot vijftig voorbeelden is groot genoeg om betrouwbaar te zijn en compact genoeg om binnen een minuut door te rekenen. Het geheim zit hem in de **samenstelling**:

- **20 Typische Standaardcases:** Teksten en documenten die de kern van het dagelijkse gebruik vertegenwoordigen.
- **10 Lastige Randgevallen (*Edge Cases*):** De langste tekst die u ooit in productie heeft gezien, de allerkortste, een invoer met typefouten, een invoer in een andere taal, of een halfleeg formulier.
- **Alle Historische Foutgevallen (*Regressietests*):** Elke keer dat een klant klaagt over een foute samenvatting of verkeerde categorisering, voegt u die geanonimiseerde case direct toe aan uw testset. Zo voorkomt u dat oude bugs ooit nog terugkeren.
- **Weiger-Cases (*Refusal Tests*):** Invoer waarin de gezochte gegevens simpelweg níet aanwezig zijn. Het enige juiste gedrag van het model is hier om te weigeren (*"Geen factuurnummer aangetroffen"*), in plaats van te gaan hallucineren.

Gebruik uitsluitend geanonimiseerde **echte klantdata**. Zelfverzonnen voorbeelden zijn steevast te netjes en missen de chaotische formaten van de echte wereld.

## Wat Meet U?

De meetmethode hangt af van het type AI-taak:

### 1. Voor Classificatie en Extractie
Hier is sprake van een eenduidig goed of fout. Meet de nauwkeurigheid (*accuracy*): klopt het geëxtraheerde IBAN-nummer? Is het ticket aan de juiste afdeling gekoppeld? Dit kan volledig geautomatiseerd worden geëvalueerd in minder dan 30 seconden.

### 2. Voor Tekstgeneratie en Samenvattingen
Omdat er bij creatieve teksten geen sprake is van één uniek goed antwoord, toetst u op **vaste eigenschappen (*properties*)**:
- Bevat de gegenereerde samenvatting de drie verplichte kernfeiten?
- Bevat de output géén claims die ontbreken in de brontekst?
- Blijft het aantal woorden binnen de ingestelde marge?
- Voldoet de opmaak aan het vereiste JSON- of Markdown-formaat?

### 3. Twee Onmisbare Productiemetrieken
Naast uw offline testset zijn er twee signalen in productie die meer zeggen dan welke benchmark dan ook:
- **De Correctieratio (*Correction Rate*):** Welk percentage van de gegenereerde teksten wordt door eindgebruikers handmatig bewerkt?
- **De Herhalingsratio (*Retry Rate*):** Hoe vaak klikt een gebruiker binnen dertig seconden op *"Opnieuw genereren"*? Een hoge herhalingsratio is het ultieme bewijs dat de eerste poging onbruikbaar was.

## De Veilige Ontwikkelingsloop

Wanneer uw testset eenmaal staat, volgt elke promptaanpassing een vaste cyclus:

1. **Draai de Testset op de Huidige Prompt:** Leg de scores vast als nulmeting.
2. **Voer de Wijziging Door:** Pas de instructies aan of selecteer een ander model.
3. **Draai de Testset Opnieuw:** Vergelijk de resultaten. Zoek niet primair naar de verbeteringen, maar kijk specifiek naar **wat er slechter is geworden**.
4. **Gefaseerde Uitrol via Feature Flags:** Schakel de nieuwe prompt eerst in voor 10% van de gebruikers en monitor of de correctieratio daalt voordat u iedereen overzet.

Bij LaunchStudio en Manifera (met meer dan 11 jaar ervaring in robuuste software-ontwikkeling) richten we geautomatiseerde LLM-evaluatiesets en CI/CD-teststraten in tijdens onze [Launch Ready-trajecten](https://launchstudio.eu/nl/#packages). [Bespreek uw AI-teststrategie met ons](https://launchstudio.eu/nl/#contact) — wij zorgen dat prompt engineering een voorspelbare wetenschap wordt.

## Praktijkvoorbeeld

### De Promptverbetering Die Stilletjes de Grootste Categorie Ruïneerde

Daria Ivanova runde Klachtclassificatie, een geautomatiseerde triage- en routeringstool voor Nederlandse nutsbedrijven en netbeheerders, gebouwd via Lovable. De applicatie las binnenkomende klachten en e-mails in, categoriseerde deze in acht specifieke servicethema's en stuurde ze door naar de juiste interne afdelingen.

Een accountmanager van een groot energiebedrijf meldde dat klachten over jaarafrekeningen (*Facturatie*) regelmatig verkeerd werden ingedeeld. 

Daria paste de systeemprompt aan: ze breidde de instructies voor de categorie Facturatie fors uit met extra voorbeelden en trefwoorden. 

Vervolgens testte ze de nieuwe prompt op vier binnengekomen factuurklachten: alle vier werden ze vlekkeloos herkend. Tevreden zette ze de aanpassing direct live op de productie-omgeving.

In de twee weken die volgden, ontstond er grote chaos bij de overige serviceteams:
Door de overmatige nadruk op facturen classificeerde het model plotseling **vrijwel elke klacht waarin een geldbedrag of een getal werd genoemd** als een factuurprobleem! 

Complexe technische storingen, geschillen over defecte slimme meters en aansluitingsverzoeken voor zonnepanelen werden massaal naar de financiële administratie gerouteerd.

De nauwkeurigheid van de grootste categorie (*Technische Storingen & Onderhoud*) was ingestort van 91% naar 63%, terwijl de facturatie-categorie slechts marginaal was verbeterd. 

Omdat er geen geautomatiseerde evaluatieset bestond, duurde het veertien dagen voordat het probleem aan het licht kwam — toen de monteursploegen aan de bel trokken omdat hun planning volledig stilviel.

**Resultaat:** Binnen twee werkdagen bouwde LaunchStudio een vaste 'Golden Test Set' van 45 geanonimiseerde echte storings- en factuurklachten verspreid over alle acht categorieën, inclusief 12 historische probleemgevallen. Er werd een geautomatiseerd validatiescript ingericht dat verplicht vóór elke promptrelease alle categorieën toetst. Met deze testsuite werd de prompt voor facturatie binnen enkele uren verfijnd, waarbij de algehele nauwkeurigheid over alle categorieën steeg naar 94% zonder dat er ook maar één storing werd gemist.

> *"Ik testte mijn 'oplossing' op de vier cases die ik wilde fiksen. Daar werkte het perfect op, terwijl het stilletjes de belangrijkste categorie van mijn hele platform om zeep hielp."*
> — **Daria Ivanova, Oprichter, Klachtclassificatie**

**Kosten & Doorlooptijd:** Golden test set, evaluatieworkflow en regressie-auditing opgeleverd in 2 werkdagen.

## Veelgestelde Vragen

### Hoeveel voorbeelden heb ik minimaal nodig voor een goede AI-testset?
Dertig tot vijftig voorbeelden. De variatie in de set is belangrijker dan het aantal: combineer typische standaardgevallen met lastige uitzonderingen, eerdere bugs en gevallen waarin het model moet weigeren.

### Hoe test je AI-functies die geen vast eenduidig antwoord opleveren?
Toets op functionele eigenschappen (*property-based testing*): controleer of essentiële feiten aanwezig zijn, of er geen onjuiste aannames worden gedaan, en of de lengte en opmaak binnen de normen vallen.

### Kan ik een AI-model gebruiken om de antwoorden van een ander model te beoordelen?
Ja, als eerste grove filtering (*LLM-as-a-judge*). Houd er rekening mee dat modellen een voorkeur hebben voor langere en zelfverzekerd klinkende antwoorden. Combineer dit altijd met mechanische checks en periodieke steekproeven door mensen.

### Welke KPI's moet ik monitoren in productie?
De correctieratio (hoe vaak gebruikers de gegenereerde output bewerken) en de herhalingsratio (hoe vaak men direct op opnieuw genereren klikt). Dit zijn de zuiverste graadmeters voor klanttevredenheid.

### Heb ik dure commerciële evaluatietools nodig?
Nee. Voor een SaaS-applicatie met twee of drie AI-features volstaat een overzichtelijke testset in een database of JSON-bestand en een geautomatiseerd script dat u vóór elke deployment aanroept.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een Golden Test Set bij LLM-ontwikkeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een samengestelde, representatieve verzameling van geanonimiseerde inputs en gevalideerde outputs waarmee prompts consistent getest worden op regressies."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom leidt het testen van een prompt op 3 voorbeeldjes vaak tot bugs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat promptaanpassingen het gedrag van een taalmodel breed beïnvloeden; een fix voor één specifiek geval beschadigt vaak het gedrag bij andere categorieën."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is property-based testing voor generatieve AI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het controleren van randvoorwaarden zoals feitelijke aanwezigheid, lengte, formatting en bronconsistentie in plaats van exacte woordovereenkomst."
      }
    },
    {
      "@type": "Question",
      "name": "Wat betekent de correctieratio bij AI-teksten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het percentage gegenereerde teksten waarin een eindgebruiker handmatige wijzigingen aanbrengt vóór acceptatie of verzending."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn weiger-cases essentieel in een AI-testsuite?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Om te verifiëren dat het model eerlijk aangeeft dat data ontbreekt in plaats van ontbrekende feiten te hallucineren."
      }
    }
  ]
}
</script>
