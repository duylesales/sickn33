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

Dertig tot vijftig voorbeelden is ruim voldoende voor de meeste AI-functionaliteiten — groot genoeg om een aanzienlijke kans te hebben dat een wijziging die iets breekt ook direct zichtbaar wordt, en compact genoeg om de hele testset binnen één minuut door te rekenen tegen minimale tokenkosten.

De inhoudelijke samenstelling is vele malen belangrijker dan de pure omvang:
- **Twintig standaardgevallen:** De alledaagse invoer die gezamenlijk tachtig procent van het reële gebruik vertegenwoordigt.
- **Tien lastige randgevallen (*edge cases*):** Het langste document dat u ooit in productie heeft verwerkt, het allerkortste, een invoer met slordige opmaak of typefouten, een invoer in een tweede taal (indien ondersteund), of een inherent ambigue vraag.
- **Alle historische foutgevallen:** Elk incident dat ooit de supportdesk heeft bereikt, direct toegevoegd zodra het optreedt — dit is de enige manier om te garanderen dat een eenmaal opgelost probleem ook permanent opgelost blijft.
- **Vijf weiger-gevallen (*refusal cases*):** Invoer waarbij het enige juiste en veilige gedrag is om expliciet te weigeren of te melden dat de data ontbreekt. Een model dat niet getraind is om toe te geven dat het iets niet weet, verzint immers vol zelfvertrouwen een klinkklare hallucinatie.

Haal deze voorbeelden altijd rechtstreeks uit geanonimiseerde **echte klantdata**. Zelfbedachte synthetische voorbeelden missen steevast de rommelige, onvoorspelbare patronen van de echte wereld.

Leg voor elk testgeval vast hoe een goede output eruitziet. Niet per se een letterlijke tekst — dat is bij generatieve taken zinloos — maar de harde eigenschappen: welke feiten moeten verplicht genoemd worden, welke claims mogen absoluut niet voorkomen, welk formaat is vereist, en binnen welke lengtemarges moet de tekst blijven.

## Wat Meet U?

De meetmethode hangt af van het type AI-taak, en het correct afstemmen van de metriek op de taak is wat dit proces pragmatisch en betaalbaar houdt.

**Voor extractie en classificatie**, waar een objectief juist antwoord bestaat, meet u de nauwkeurigheid (*accuracy*) direct. Klopt het geëxtraheerde totaalbedrag? Is de gekozen categorie juist? Dit kan volledig geautomatiseerd worden gevalideerd met een eenvoudig testscript, waardoor het vergelijken van twee promptversies minder dan een minuut kost.

**Voor vrije tekstgeneratie**, waar geen sprake is van één uniek juist antwoord, toetst u op vaste eigenschappen (*properties*) in plaats van op letterlijke tekstovereenkomst. Bevat de samenvatting de vereiste feiten? Blijven ongegronde claims die ontbreken in de brontekst achterwege? Blijft de lengte binnen de gestelde bandbreedte? En behoudt de output het gevraagde formaat (zoals Markdown of JSON)? Elk van deze eigenschappen is mechanisch controleerbaar, en gezamenlijk vangen ze het overgrote deel van alle regressies af.

**Voor weigertaken (*refusal tests*)**, controleert u of de functie netjes weigerde in plaats van iets te verzinnen — want dát is de faalmodus die anders als overtuigend geformuleerde onzin bij uw klant belandt.

Naast de offline testset zijn er twee productiemetrieken die waardevoller zijn dan welke synthetische benchmark dan ook:
- **De correctieratio (*correction rate*):** Hoe vaak bewerken klanten de gegenereerde output handmatig, bijgehouden per feature door de tijd heen?
- **De herhalingsratio (*retry rate*):** Hoe vaak voeren gebruikers binnen korte tijd exact dezelfde opdracht opnieuw uit? Dat is immers het duidelijkste bewijs dat het eerste resultaat onbruikbaar was.

## De Veilige Ontwikkelingsloop

Wanneer een testset eenmaal operationeel is, volgt elke wijziging exact dezelfde korte en voorspelbare cyclus.

Draai de testset tegen de huidige configuratie en leg de resultaten vast. Voer vervolgens de beoogde wijziging door — een aanpassing in de systeemprompt, de overstap naar een ander model, of een verandering in de context die wordt meegegeven. Draai de testset opnieuw. Vergelijk de uitkomsten, en kijk specifiek naar **wat er slechter is geworden** in plaats van naar de algemene indruk. Promptaanpassingen verbeteren immers routinematig één type invoer, terwijl ze stilletjes een andere categorie beschadigen.

Wanneer de offline vergelijking gunstig uitvalt, rolt u de aanpassing via een feature flag uit naar een klein percentage van uw actieve accounts. Monitor de correctieratio nauwlettend voordat u de wijziging voor iedereen activeert. De offline evaluatie vangt regressies af; de productiemeting vangt de praktijksituaties op die uw dertig testvoorbeelden niet weerspiegelden.

De discipline die dit proces effectief maakt, is het draaien van de testset bij letterlijk élke wijziging — inclusief aanpassingen die ogenschijnlijk volkomen veilig lijken. De veranderingen die software breken, zijn immers steevast de wijzigingen die te triviaal leken om te testen.

Het opzetten van een evaluatieset, het automatiseren van de vergelijking en het koppelen ervan aan een gefaseerde uitrol is een overzichtelijk stuk engineering dat promptiteratie transformeert van giswerk naar een controleerbaar proces. LaunchStudio, ondersteund door meer dan 11 jaar enterprise software-ontwerp bij Manifera, richt deze testinfrastructuur in parallel aan de AI-functionaliteiten zelf. [Beschrijf uw project](https://launchstudio.eu/nl/#contact) voor een grondige review binnen één werkdag.

## Wanneer Geautomatiseerd Scoren Zijn Complexiteit Waard Is

Het handmatig beoordelen van dertig testoutputs kost misschien twintig minuten. Dat is volkomen acceptabel voor een aanpassing die u maandelijks doorvoert, maar tijdrovend voor iteraties die u dagelijks wilt testen.

De logische vervolgstap is om een model in te zetten als beoordelaar — waarbij een tweede model toetst of een samenvatting accuraat en compleet is ten opzichte van de brontekst (*LLM-as-a-judge*). Dit werkt verrassend goed, maar kent twee fundamentele beperkingen die u moet kennen. Het stemt meestal overeen met het menselijk oordeel, maar zeker niet altijd. Bovendien vertonen taalmodellen systematische vooroordelen: ze belonen stelselmatig langere antwoorden en formuleringen die overtuigend en zelfverzekerd klinken. Het is een uitstekend filter voor een eerste grove schifting, maar een gevaarlijke eindautoriteit.

Een praktische en beproefde opzet:
1. Geautomatiseerde code-checks voor alle eigenschappen die mechanisch gecontroleerd kunnen worden (formaat, JSON-validatie, afwezigheid van verboden termen).
2. Model-ondersteunde evaluatie voor de subjectieve kwaliteitsdimensies (relevantie, toon).
3. Menselijke review voor de grensgevallen waarin het geautomatiseerde oordeel twijfelt of een lage score toekent.

Daarmee houdt u de benodigde menselijke tijd binnen de perken, terwijl u professioneel oordeelsvermogen behoudt waar het er echt toe doet.

Wat in deze groeifase zelden de investering waard is, is een zwaar commercieel AI-evaluatieplatform. Die platforms zijn ontworpen voor grote machine learning-teams die honderden experimenten tegelijk draaien. Een spreadsheet, een degelijk Python-script en een vaste teamdiscipline volstaan ruimschoots voor een SaaS-product met twee of drie AI-functies — en hebben het doorslaggevende voordeel dat u ze daadwerkelijk zult gebruiken.

## Echt voorbeeld

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
