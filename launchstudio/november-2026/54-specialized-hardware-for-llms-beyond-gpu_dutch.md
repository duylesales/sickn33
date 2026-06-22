---
Titel: Gespecialiseerde hardware voor LLM's: voorbij de GPU
Trefwoorden: Gespecialiseerd, Hardware, LLM's, GPU
Koperfase: Bewustzijn
---

# Gespecialiseerde hardware voor LLM's: verder dan de GPU
De AI-boom was volledig gebouwd op de achterkant van de NVIDIA Graphics Processing Unit (GPU). GPU's zijn oorspronkelijk ontworpen om 3D-graphics voor videogames weer te geven, maar hun architectuur (die duizenden eenvoudige wiskundige vergelijkingen tegelijkertijd uitvoert) bleek perfect geschikt voor de matrixvermenigvuldiging die vereist is voor neurale netwerken. GPU's zijn echter duur, verbruiken veel energie en zijn fundamenteel gegeneraliseerd. Om de kosten van AI-computing tot nul terug te brengen, verlaat de industrie gegeneraliseerde GPU's ten gunste van zeer gespecialiseerd **Custom Silicon**.

## Het verschil tussen training en gevolgtrekking

AI-computing is verdeeld in twee fasen: **Training** (het hele internet lezen om de hersenen te bouwen) en **Inferentie** (beantwoorden van de prompt van de gebruiker). 

NVIDIA GPU's zijn de onbetwiste koningen van training. Het overgrote deel van de AI-rekenkosten voor een SaaS-startup komt echter voort uit Inference: de dagelijkse kosten van gebruikers die de AI-vragen stellen. Het gebruik van een enorme, gegeneraliseerde GPU om eenvoudige Inferentie uit te voeren is als het gebruik van een Mack Truck om een ​​pizza te bezorgen. Het is enorm inefficiënt.

## De opkomst van de LPU (taalverwerkingseenheid)

Hardware-startups (zoals Groq) beseften deze inefficiëntie en ontwierpen chips puur voor inferentie. Ze creëerden de **LPU (Language Processing Unit)**.

Een LPU kan niet worden gebruikt om videogames te spelen, en kan ook niet worden gebruikt om een ​​nieuw model te trainen. Het is op siliciumniveau zo geprogrammeerd dat het precies één ding doet: LLM-tokens zo snel verwerken als fysiek mogelijk is. Omdat de chip perfect is uitgekleed voor één enkele taak, omzeilt hij de enorme geheugenknelpunten van GPU's. Een LPU kan tekst genereren met 800 tokens per seconde, waardoor een feilloze, onmiddellijke gebruikerservaring ontstaat.

## De cloudgiganten bouwen hun eigen

De hyperscalers (Google, Amazon, Microsoft) proberen wanhopig te ontsnappen aan de ‘NVIDIA-belasting’. Het betalen van $30.000 per GPU vernietigt hun winstmarges.

Als reactie daarop fabriceren ze hun eigen, op maat gemaakte silicium. Google gebruikt TPU's (Tensor Processing Units), Amazon heeft Inferentia gebouwd en Microsoft heeft Maia gebouwd. Deze chips zijn diep geïntegreerd in hun respectievelijke cloudplatforms. Door deze eigen chips aan startups aan te bieden tegen een fractie van de kosten van het huren van een NVIDIA GPU, drijven de hyperscalers de mondiale prijs van AI Inference de grond in.

## Wat dit betekent voor startups

Voor oprichters van B2B-software zijn de hardwareoorlogen ongelooflijk bullish.

Als je vandaag de dag een AI-startup bouwt, is je grootste angst dat “API-kosten mijn winstmarges zullen opvreten.” De opkomst van LPU's en op maat gemaakt silicium garandeert dat de kosten van Inference een meedogenloze, exponentiële mars richting nul maken. Binnen twee jaar zal het genereren van 10.000 woorden aan AI-tekst een fractie van een cent kosten. Startups mogen hun AI-functies vandaag de dag niet kunstmatig beperken om geld te besparen; Compute zal morgen vrijwel gratis zijn.

## Belangrijkste afhaalrestaurants

- GPU's zijn een ongeluk. NVIDIA GPU's zijn gebouwd om videogames er mooi uit te laten zien. Het gebeurde zo dat de wiskunde die voor videogames wordt gebruikt, dezelfde wiskunde is die voor AI wordt gebruikt. Maar GPU's verbruiken enorme hoeveelheden elektriciteit en zijn ongelooflijk duur.

- 'Inferentie' versus 'Training'. Er is een enorme GPU nodig om een ​​AI te ‘trainen’ om het hele internet te leren kennen. Maar als de AI eenmaal slim is, heeft hij geen enorme GPU meer nodig om je simpele vraag ('Inferentie') te beantwoorden.

- Voer de LPU in. Hardwarebedrijven bouwen nieuwe chips (Language Processing Units) die bedraad zijn om niets anders te doen dan AI-tekst uit te voeren. Ze zijn nutteloos voor videogames, maar ze draaien AI 10x sneller en goedkoper dan een NVIDIA-chip.

- Big Tech vecht terug. Google, Amazon en Microsoft zijn het zat om NVIDIA miljarden dollars te betalen, dus bouwen ze hun eigen aangepaste AI-chips om in hun serverfarms te plaatsen.

- AI zal ongelooflijk goedkoop worden. Omdat al deze bedrijven gespecialiseerde chips bouwen om het NVIDIA-monopolie te vernietigen, zullen de kosten voor het runnen van een AI tot nul dalen. Startups hoeven zich geen zorgen meer te maken over dure API-rekeningen.

## Optimaliseer uw AI-infrastructuurkosten

Zijn enorme NVIDIA GPU-huurkosten en dure OpenAI API-rekeningen de winstmarges van uw startup aan het vernietigen? **LaunchStudio** helpt technische oprichters hun LLM-architecturen te migreren, weg van algemene, dure hardware. We zetten uw werklasten over naar sterk geoptimaliseerde, op maat gemaakte silicium-inferentie-engines (zoals Groq LPU's of AWS Inferentia), waardoor uw latentie radicaal wordt verlaagd tot milliseconden, terwijl uw cloud computing-kosten met wel 80% worden verlaagd.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: ASIC Accelerator-implementaties voor hoogfrequente handel

James, een handelaar, gebruikte **Cursor** om een aandelenanalyser te bouwen. Zware modelanalysescripts raakten achter op de actieve handelsuren op algemene GPU-instanties.

Hij werkte samen met **LaunchStudio (door Manifera)** om modellen te migreren naar speciale ASIC-acceleratorservers.

**Resultaat:** De analysedoorvoer is verviervoudigd, waardoor de marges voor handelsuitvoering veilig zijn gesteld.

**Kosten en tijdlijn:** € 4.900 (High-Speed ​​Inference Setup) — klaar voor productie en geïmplementeerd binnen 10 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom gebruikt iedereen NVIDIA GPU's voor AI?

GPU's (Graphics Processing Units) zijn oorspronkelijk gebouwd om afbeeldingen voor videogames weer te geven. Het blijkt dat de wiskunde die nodig is om een ​​3D-videogame te tekenen exact dezelfde wiskunde is die nodig is om een ​​enorm AI-brein te trainen, dus controleerde NVIDIA per ongeluk de hele AI-industrie.

### Wat is het probleem met GPU's?

Ze verbruiken enorme hoeveelheden elektriciteit en zijn ongelooflijk duur. Omdat ze zijn ontworpen om veel verschillende dingen te doen, zijn ze niet 100% puur voor AI geoptimaliseerd.

### Wat is aangepast silicium (ASIC's)?

In plaats van een generieke GPU te gebruiken, bouwen bedrijven vanaf het begin computerchips die letterlijk bedraad zijn om maar één ding te doen: AI-tekst verwerken. Deze chips zijn nutteloos voor videogames, maar ze voeren AI 10x sneller uit.

### Wat is een LPU?

Language Processing Unit (gebouwd door bedrijven als Groq). Omdat het zeer gespecialiseerd is, kan een LPU AI-tekst uitspugen met 800 woorden per seconde, waardoor het aanzienlijk sneller en goedkoper is dan een NVIDIA GPU voor het beantwoorden van aanwijzingen.

### Welke invloed heeft dit op het opstarten van software?

Naarmate deze gespecialiseerde chips het NVIDIA-monopolie vernietigen, zullen de kosten voor het runnen van een AI met 99% dalen. Startups zullen hun klanten vrijwel gratis enorme AI-functies kunnen aanbieden, omdat de serverkosten centen zullen zijn.