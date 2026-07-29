---
Titel: De Rol van de AI Product Manager, Uitgelegd
Trefwoorden: ai product manager, ai software-engineering, ai en softwareontwikkeling, ai saas, ai native, ai app bouwen, dev ai
Koperfase: Bewustwording
---

# De Rol van de AI Product Manager, Uitgelegd

Decennialang was software-engineering **deterministisch**. Als een gebruiker X invoert, levert de database elke keer exact Y op. Product Managers bouwden nauwkeurige wireframes, schreven exacte acceptatiecriteria en ontwikkelaars bouwden precies wat in het ticket stond beschreven. Generatieve AI heeft dit paradigma bij de wortel gebroken. LLM's zijn **probabilistisch**: als een gebruiker X invoert, kan het model Y of Z opleveren, of zelfverzekerd een antwoord verzinnen dat aannemelijk klinkt maar volledig is gefabriceerd. Om een geloofwaardig B2B AI SaaS-product te bouwen, moet de rol van de Product Manager evolueren van het beheren van functionaliteiten naar het beheren van onzekerheid zelf — en de meeste PM-trainingen, gebouwd voor een deterministische wereld, dekken dat simpelweg niet af.

## Het Beheren van de Foutmarge

In traditionele software is een bug een duidelijke fout met een traceerbare oorzaak in de stack. In generatieve AI is een hallucinatie geen bug in de klassieke zin — het is een inherente statistische eigenschap van het model, en u kunt niet naar 100% nauwkeurigheid programmeren, hoe goed uw prompt engineering of fine-tuning ook is.

De kerntaak van de AI PM is het definiëren van de **acceptabele foutmarge** voor elk specifiek gebruiksscenario, omdat die drempel niet vaststaat — deze verschilt enorm per domein. Als u een tool bouwt die concept-marketingtweets opstelt, is een nauwkeurigheid van 80-85% uitstekend; een licht afwijkende tweet is hooguit gênant en wordt binnen drie seconden door de gebruiker verwijderd. Als u een tool bouwt die medische patiëntendossiers samenvat voor een arts, is een nauwkeurigheid van 99%+ op alles wat met doseringen, allergieën of diagnoses te maken heeft het absolute minimum, omdat een hallucinatie van 1% in die context geen ongemak is — het is een schadeclaim of erger. De echte taak van de PM is om, voordat er één regel specificatie wordt geschreven, te beslissen of de huidige stand van de technologie levensvatbaar is voor het enterprise risicoprofiel waarop u zich richt.

Hier branden veel AI-native oprichters zich aan. Het is verleidelijk om de meest indrukwekkende demo te verzenden — degene waarin de AI alles van begin tot eind afhandelt — omdat dat conversies oplevert in verkoopgesprekken. Maar de PM moet de persoon in de ruimte zijn die vraagt wat er gebeurt in de 5-15% van de gevallen waarin het model het mis heeft, en of de kosten van die fout door de organisatie kunnen worden opgevangen op schaal.

## Het Ontwerpen van de Fallback (Human-in-the-Loop)

Omdat de AI onvermijdelijk in een percentage van de gevallen zal falen, moet de AI PM de foutstatus vooraf ontwerpen, en niet achteraf toevoegen na een klantklacht. Deze discipline staat bekend als het bouwen van **Human-in-the-Loop (HITL)** workflows.

Als de AI een juridisch advies genereert, mag de UI dit standaard nooit als een afgewerkte, exporteerbare PDF presenteren. De PM moet de interface ontwerpen om elke generatie als een **concept** te presenteren — visueel onderscheidend, duidelijk gelabeld en onmogelijk te verwarren met een definitief document. Concreet betekent dit dat de PM specificeert: welke beweringen een betrouwbaarheidsscore krijgen; klikbare bronvermeldingen die elke feitelijke bewering koppelen aan het bron-document via de RAG-pipeline; en een harde controle — het document kan letterlijk niet worden geëxporteerd totdat een mens op "Goedkeuren" klikt. Dit is het verschil tussen ontwerpen voor automatisering en ontwerpen voor vertrouwen.

Goed HITL-ontwerp moet ook rekening houden met vermoeidheid bij de beoordelaar. Als uw AI 95% van de tijd gelijk heeft en een mens moet toch elk antwoord beoordelen, neemt de aandacht snel af. Volwassen AI-producten sturen alleen de antwoorden met de laagste betrouwbaarheid naar een menselijke wachtrij en keuren de antwoorden met hoge betrouwbaarheid automatisch goed, met periodieke steekproeven.

## Evaluatie-Gedreven Ontwikkeling (Evals)

Traditionele PM's schrijven user stories en leveren een functie op zodra deze door de QA komt. AI PM's moeten **eval-datasets** bouwen en onderhouden, omdat u niet kunt weten of een AI-functie "goed" is door deze handmatig te testen — dezelfde prompt kan bij een volgende uitvoering een ander antwoord opleveren.

De AI PM stelt een gestructureerde dataset samen — vaak beginnend bij 100-200 praktijkvragen en groeiend naar 500 of meer naarmate er edge cases in productie naar boven komen — elk gekoppeld aan een "ideaal antwoord". Wanneer het engineeringteam wil overstappen naar een ander model (bijv. van GPT-4o naar Claude) om kosten te besparen, voeren ze de nieuwe configuratie uit tegen de volledige eval-set. Ze gebruiken vaak een "LLM-as-judge" patroon om te controleren of het succespercentage niet stilletjes is gedaald op de belangrijkste categorieën.

## Het Navigeren van de Balans tussen Latentie, Kosten en Kwaliteit

AI introduceert fysieke en economische beperkingen die traditionele SaaS niet heeft. De slimste modellen zijn ook het traagst en het duurst per token.

De AI PM moet voortdurend navigeren tussen snelheid, kosten en kwaliteit. Als een functie directe feedback vereist — zoals automatische aanvulling in een code-editor — kiest de PM voor een snel, goedkoop model. Als een functie asynchroon op de achtergrond draait — zoals het samenvatten van 100 contracten gedurende de nacht — kiest de PM voor het meest nauwkeurige, hoogwaardige model dat beschikbaar is. Het verkeerd afstemmen van deze keuzes vernietigt de unit economics op schaal.

Sectorgegevens tonen dit scherp aan: ongeveer 80% van de met AI gegenereerde prototypes bereikt nooit een productierijpe status, en ongeveer 45% van de AI-code bevat ten minste één beveiligingslek wanneer deze geen dedicated hardening-fase heeft doorlopen.

## Waar de AI PM Rol en Beveiliging Samenkomen

Het productoppervlak dat een LLM blootlegt is ook een aanvalsoppervlak. Prompt-injection is net zo goed een productontwerpprobleem als een beveiligingsprobleem. De PM moet beslissen welke gegevens een agent mag lezen, welke acties deze autonoom mag uitvoeren en hoe storingen achteraf worden gelogd.

Herre Roelevink, Oprichter & Managing Director van Manifera, verwoordt het als volgt: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. We hebben elf jaar ervaring in precies dat."

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera** (zie [manifera. com/services/custom-software-development](https://www. manifera. com/services/custom-software-development/)), opgericht in **2014** door Herre Roelevink. Met hoofdkantoor te Amsterdam aan de **Herengracht 420, 1017 BZ Amsterdam** en ontwikkelcentra in **Singapore** en **Ho Chi Minh City, Vietnam**, levert Manifera enterprise-kwaliteit software engineering. [Vraag vandaag nog een gratis offerte aan](https://launchstudio. eu/en/#contact).

## Belangrijkste Inzichten

- Software was altijd deterministisch; AI is probabilistisch. AI PM's moeten de acceptabele foutmarge per gebruiksscenario beheren.
- Ontwerp vooraf Human-in-the-Loop (HITL) workflows en presenteer AI-gegenereerde antwoorden altijd als concepten die menselijke goedkeuring vereisen.
- Bouw en onderhoud gestructureerde eval-datasets om de kwaliteit te testen bij elke wijziging in prompts of modellen.
- Beheer de balans tussen snelheid, kosten en kwaliteit door snelle modellen te gebruiken voor directe UI-feedback en hoogwaardige modellen voor achtergrondtaken.

## Echt Voorbeeld

### Een AI-Native Oprichter in Actie: Van 72% naar 96% Betrouwbaarheid op een Medische Samenvattingstool

Thomas bouwt een AI-tool die medische consulten samenvat. Aanvankelijk vertrouwden zijn eerste testgebruikers de uitvoer niet vanwege incidentele hallucinaties in medicatiedoseringen.

**LaunchStudio** werkte samen met Thomas om een eval-dataset van 300 consulten op te zetten en een Human-in-the-Loop review-interface te bouwen met bronverwijzingen.

**Resultaat:** De nauwkeurigheid steeg naar 96% en de gemiddelde controletijd voor artsen nam af van 10 minuten naar 45 seconden.

---

## Veelgestelde Vragen (FAQ)

### Wat is het verschil tussen een traditionele PM en een AI Product Manager?
Een traditionele PM beheert deterministische functies met exacte specificaties. Een AI PM beheert probabilistische modellen, accepteert foutmarges, ontwerpt HITL-workflows en onderhoudt eval-datasets.

### Wat betekent Human-in-the-Loop (HITL) in AI-productontwerp?
HITL betekent dat AI-gegenereerde inhoud als concept wordt gepresenteerd en door een mens moet worden gecontroleerd en goedgekeurd voordat deze definitief wordt geëxporteerd of verzonden.

### Waarom zijn eval-datasets zo belangrijk voor AI-producten?
Eval-datasets zijn gestructureerde verzamelingen van testvragen en ideale antwoorden. Ze stellen teams in staat om de prestaties van een model of prompt objectief te meten na elke update.

### Hoe balanceert een AI PM de kosten en snelheid van een model?
Door snelle, goedkope modellen in te zetten voor realtime UI-interacties (zoals auto-complete) en krachtigere, tragere modellen te gebruiken voor zware achtergrondtaken.

### Hoe helpt LaunchStudio AI Product Managers bij de lancering?
LaunchStudio helpt bij het bouwen van robuuste evaluatie-pipelines, veilige HITL-interfaces en geharde backend-architecturen binnen 1 tot 3 weken.

<script type="application/ld+json">
{
  "@context": "https://schema. org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een traditionele PM en een AI Product Manager?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een traditionele PM beheert deterministische functies met exacte specificaties. Een AI PM beheert probabilistische modellen, accepteert foutmarges, ontwerpt HITL-workflows en onderhoudt eval-datasets."
      }
    },
    {
      "@type": "Question",
      "name": "Wat betekent Human-in-the-Loop (HITL) in AI-productontwerp?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HITL betekent dat AI-gegenereerde inhoud als concept wordt gepresenteerd en door een mens moet worden gecontroleerd en goedgekeurd voordat deze definitief wordt geëxporteerd of verzonden."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn eval-datasets zo belangrijk voor AI-producten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eval-datasets zijn gestructureerde verzamelingen van testvragen en ideale antwoorden. Ze stellen teams in staat om de prestaties van een model of prompt objectief te meten na elke update."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe balanceert een AI PM de kosten en snelheid van een model?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door snelle, goedkope modellen in te zetten voor realtime UI-interacties (zoals auto-complete) en krachtigere, tragere modellen te gebruiken voor zware achtergrondtaken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt LaunchStudio AI Product Managers bij de lancering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio helpt bij het bouwen van robuuste evaluatie-pipelines, veilige HITL-interfaces en geharde backend-architecturen binnen 1 tot 3 weken."
      }
    }
  ]
}
</script>
