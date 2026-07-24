---
Titel: "Hoe u kunt zien of uw developer de door AI gegenereerde code die hij onderhoudt daadwerkelijk begrijpt"
Trefwoorden: ai software developers, developer onboarding ai codebase, hiring developer ai project, code comprehension check
Koperfase: Beslissing
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Hoe u kunt zien of uw developer de door AI gegenereerde code die hij onderhoudt daadwerkelijk begrijpt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe u kunt zien of uw developer de door AI gegenereerde code die hij onderhoudt daadwerkelijk begrijpt",
  "description": "Een praktische how-to voor niet-technische oprichters om te verifiëren dat ai software developers die zijn aangenomen om een door AI gegenereerde codebase te onderhouden, deze daadwerkelijk begrijpen, voordat er iets stukgaat en het te laat is om het te vragen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/developer-understood-code-they-maintain" }
}
</script>

Uw eerste developer aannemen voelt als het moment waarop u eindelijk kunt stoppen met piekeren over de codebase. Iemand met de juiste kwalificaties is er nu verantwoordelijk voor. Maar de juiste persoon aannemen en bevestigen dat hij daadwerkelijk begrijpt wat hij heeft geërfd, zijn twee verschillende stappen, en de tweede overslaan is een van de stilste manieren waarop een groeiend product in de problemen kan raken.

Hier is een praktische manier om dit te controleren — voordat een incident de vraag afdwingt.

## Stap 1: vraag naar één specifiek stuk functionaliteit, niet het hele systeem

Vraag niet "begrijp je de codebase." Niemand zegt nee op die vraag, en het vertelt u niets. Kies in plaats daarvan één specifieke, redelijk belangrijke feature — iets met echte logica erachter, geen statische pagina — en vraag uw developer om precies uit te leggen hoe het werkt, in gewone taal die u kunt volgen.

Het doel is niet om zijn woordenschat te testen. Het is om te zien of hij oorzaak en gevolg kan traceren: wat triggert dit, wat controleert het, wat doet het vervolgens, wat gebeurt er als die controle faalt. Een developer die de code echt begrijpt, kan dit soepel doen, zelfs in eenvoudige bewoordingen. Een developer die er nog niet echt in gedoken is, zal ontwijken, generaliseren, of afzwakken naar "het werkt gewoon" zonder op specifieke details uit te komen.

## Stap 2: vraag wat er gebeurt in een faalscenario

Vervolg met een "wat als"-vraag over dezelfde feature. Wat gebeurt er als deze aanroep faalt? Wat gebeurt er als een gebruiker hier iets onverwachts invoert? Dit is de vraag die oppervlakkige bekendheid scheidt van echt begrip, want door AI gegenereerde code behandelt vaak het succespad duidelijk, maar laat foutafhandeling vaag of afwezig — en een developer die de code daadwerkelijk heeft gelezen, weet of die lacune bestaat, terwijl iemand die dat niet heeft gedaan, aanneemt dat het is afgehandeld omdat de meeste demo's het faalscenario nooit raken.

## Stap 3: let op zelfverzekerde antwoorden die niet concreet worden

Het risicovolste signaal is niet "ik weet het niet" — dat is eerlijk, en werkbaar. Het is een zelfverzekerd, algemeen antwoord dat nooit concreet wordt: "het is allemaal afgehandeld," "dat is standaard," "maak u daar geen zorgen over." Echt begrip klinkt als specifieke details — een bepaalde controle, een bepaalde voorwaarde, een bepaald bestand of een bepaalde functie. Vage zelfverzekerdheid is vaak een teken dat niemand, inclusief de developer die antwoordt, daadwerkelijk heeft geverifieerd hoe een stuk functionaliteit werkt.

## Fiens onboardingmoment

Fien Kramer, een oprichter in Harderwijk, bouwde TicketVolg — een app voor supporttickets — met Bolt. Naarmate het product groeide, nam ze een developer aan om te helpen bij het onderhouden en uitbreiden ervan. Tijdens de onboarding stelde Fien eenvoudige, directe vragen over een kritiek stuk functionaliteit — hoe tickets intern werden gerouteerd en geprioriteerd.

De nieuwe aanwinst kon het niet duidelijk uitleggen. Niet omdat hij niet capabel was, maar omdat niemand — niet de developer, en zoals later bleek, ook de originele output van de AI-tool niet — ooit daadwerkelijk had geverifieerd hoe die routeringslogica werkte of of die edge cases correct afhandelde. Het onboardinggesprek, bedoeld als formaliteit, onthulde een echte lacune: een kernonderdeel van het product draaide op logica die niemand op dat moment kon uitleggen.

## Stap 4: schakel een tweede, onafhankelijke review in als de antwoorden niet kloppen

Als stap één en twee lacunes blootleggen, is de oplossing niet noodzakelijk de nieuwe developer de schuld geven — de door AI gegenereerde code zelf is mogelijk nooit beoordeeld door iemand met de juiste kwalificaties. Op dat punt is de nuttige stap een onafhankelijke technische review: iemand die de daadwerkelijke code leest, verifieert wat die doet ten opzichte van wat iedereen aannam dat die deed, en het werkelijke gedrag documenteert zodat zowel de oprichter als de developer vanuit dezelfde feitelijke basis werken.

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordde het zo: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. We hebben elf jaar ervaring in precies dat." Verifiëren dat een developer daadwerkelijk begrijpt wat hij onderhoudt, is een klein, concreet onderdeel van die bredere volwassenheidsvraag — maar het is vaak de eerste plek waar de lacune zichtbaar wordt.

Ons team in Amsterdam, gesteund door de 120+ engineers van Manifera, stapt regelmatig precies in dit soort lacune — het doorlezen van door AI gegenereerde code die niemand volledig heeft geverifieerd en het documenteren van wat die daadwerkelijk doet. LaunchStudio brengt diezelfde standaard, gebruikt in Manifera's [portfolio van 160+ opgeleverde projecten](https://www.manifera.com/portfolio/), naar producten op oprichtersschaal. Heeft uw eigen onboardinggesprek meer vragen opgeroepen dan beantwoord, dan kunt u [spreken met een engineer die door AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: de onboardingvragen die een lacune blootlegden die niemand kende

Fien Kramer had TicketVolg uitgebouwd tot een oprecht nuttige tool voor supporttickets, en het aannemen van een tweede developer voelde als een natuurlijke volgende stap naarmate het ticketvolume groeide. Tijdens de onboarding liep ze de routeringslogica voor tickets door met de nieuwe aanwinst, in de verwachting van een snelle bevestiging dat hij snel op de hoogte was. In plaats daarvan bleven de antwoorden vaag — "het prioriteert op basis van bepaalde regels," zonder specifieke details over wat die regels eigenlijk waren of hoe conflicten ertussen werden opgelost.

Fien bracht de codebase naar LaunchStudio voor een onafhankelijke lezing. De technici van Manifera traceerden de daadwerkelijke routeringslogica en ontdekten dat die de gangbare gevallen redelijk goed afhandelde, maar geen gedefinieerd gedrag had voor tickets die tegelijkertijd aan meerdere prioriteitsregels voldeden — het koos stilletjes welke regel toevallig als laatste in de code werd gecontroleerd, iets wat niemand, inclusief Bolts originele output, ooit expliciet had besloten als het gewenste gedrag.

Het team documenteerde de daadwerkelijke logica, repareerde het ambigue geval met een expliciete, bewuste prioriteitsvolgorde, en gaf zowel Fien als haar nieuwe developer een duidelijke schriftelijke referentie voor hoe het systeem voortaan hoorde te werken.

**Resultaat:** TicketVolgs routeringslogica gedraagt zich nu voorspelbaar en is duidelijk genoeg gedocumenteerd zodat elke toekomstige developer op dezelfde manier getest kan worden als Fien haar nieuwe aanwinst testte.

> *"Ik stelde een simpele vraag in de verwachting van een simpel antwoord, en in plaats daarvan ontdekte ik dat niemand eigenlijk wist hoe een kernonderdeel van mijn eigen product werkte."*
> — **Fien Kramer, oprichter, TicketVolg (Harderwijk)**

**Kosten en tijdlijn:** € 1.300 (audit codebegrip en documentatie routeringslogica) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Wat is het beste type vraag om tijdens onboarding aan een nieuwe developer te stellen?

Een specifieke vraag over één echte feature — hoe die stap voor stap werkt, in gewone taal — onthult veel meer dan een algemene vraag als "begrijp je de codebase," die vrijwel iedereen bevestigend zal beantwoorden ongeacht de daadwerkelijke bekendheid ermee.

### Is het een slecht teken als een nieuwe developer tijdens onboarding zegt "dat weet ik nog niet"?

Niet noodzakelijk. Een eerlijk "dat weet ik nog niet, laat ik het even checken" is een gezonder antwoord dan een vaag, zelfverzekerd antwoord dat nooit concreet wordt, omdat het eerste laat zien dat de developer de grenzen kent van wat hij heeft geverifieerd.

### Hoe helpt Manifera wanneer een oprichter een begripslacune ontdekt zoals bij Fien?

De technici van Manifera, gevestigd in Amsterdam samen met teams in Singapore en Ho Chi Minh-stad, lezen de daadwerkelijke code, verifiëren wat die doet ten opzichte van wat wordt aangenomen, en produceren documentatie waar zowel de oprichter als het ontwikkelteam voortaan op kunnen vertrouwen.

### Betekent dit soort lacune dat de originele door AI gegenereerde code slecht geschreven was?

Niet noodzakelijk slecht geschreven, maar vaak onvoldoende geverifieerd. AI-tools produceren vaak code die werkt voor gangbare gevallen, zonder dat iemand bevestigt dat de edge cases bewust zijn afgehandeld in plaats van bij toeval.

### Wat bedoelde Herre Roelevink met de verschuiving in softwarebehoeften?

Hij wijst op een verschuiving van "kan dit idee software worden" naar "kan deze software uitgroeien tot iets veiligs en goed genoeg gearchitecteerd om op te vertrouwen," precies het soort lacune dat een begripscontrole tijdens onboarding vroeg kan blootleggen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the best type of question to ask a new developer during onboarding?", "acceptedAnswer": { "@type": "Answer", "text": "A specific question about one real feature, how it works step by step in plain language, reveals far more than a general question like \"do you understand the codebase,\" which almost anyone will answer yes to regardless of actual familiarity." } },
    { "@type": "Question", "name": "Is it a bad sign if a new developer says \"I don't know yet\" during onboarding?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily. An honest \"I don't know yet, let me check\" is a healthier answer than a vague, confident one that never gets specific, since the former shows the developer knows the limits of what they've verified." } },
    { "@type": "Question", "name": "How does Manifera help when a founder discovers a comprehension gap like Fien's?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera's engineers, based in Amsterdam alongside teams in Singapore and Ho Chi Minh City, read through the actual code, verify what it does against what's assumed, and produce documentation both the founder and the development team can rely on going forward." } },
    { "@type": "Question", "name": "Does this kind of gap mean the original AI-generated code was badly written?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily badly written, but often under-verified. AI tools tend to produce code that works for common cases without anyone confirming the edge cases were handled deliberately rather than by accident." } },
    { "@type": "Question", "name": "What did Herre Roelevink mean about the shift in software needs?", "acceptedAnswer": { "@type": "Answer", "text": "He's pointing to a shift from \"can this idea become software\" to \"can this software mature into something secure and well-architected enough to rely on,\" which is exactly the kind of gap a comprehension check during onboarding can expose early." } }
  ]
}
</script>
