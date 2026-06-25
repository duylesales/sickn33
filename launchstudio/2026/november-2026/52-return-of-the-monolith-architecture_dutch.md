---
Titel: De terugkeer van de monolietarchitectuur
Trefwoorden: Terugkeer, Monoliet, Architectuur
Koperfase: Bewustzijn
---

# De terugkeer van de monolietarchitectuur
De afgelopen tien jaar was de software-industrie geobsedeerd door ‘Microservices’. De heersende wijsheid stelde dat als je een enorme, uniforme codebasis bouwde (een "monoliet"), deze uiteindelijk te complex zou worden voor mensen om te beheren. Startups kopieerden blindelings de architectuur van Netflix en vernietigden hun apps in vijftig gefragmenteerde services die communiceerden via complexe API’s. Dit resulteerde in een DevOps-nachtmerrie. In het AI-tijdperk is de slinger met geweld achteruit gezwaaid. De **Majestueuze Monoliet** keert terug.

## De microservicebelasting

Microservices lossen een organisatorisch probleem op, geen technisch probleem. Als je 5.000 technici hebt, kunnen 50 onafhankelijke teams door de app op te splitsen in 50 microservices code implementeren zonder elkaar op de tenen te trappen.

Maar voor een startup met vijf personen zijn microservices een ramp. Je erft de ‘Distributed Systems Tax’: complexe netwerklatentie, pijnlijke tracering wanneer een bug drie verschillende services omvat, en enorme AWS-rekeningen. Startups besteden 40% van hun engineeringcycli alleen aan het beheren van de Kubernetes-clusters in plaats van aan het bouwen van daadwerkelijke productfuncties.

## AI houdt van de monoliet

Het belangrijkste argument tegen de Monoliet was dat deze te groot werd voor één enkele menselijke ingenieur om in zijn hoofd te houden. Een mens kan een codebasis van 1 miljoen regels niet begrijpen. 

Maar een AI-agent met een contextvenster van 2 miljoen tokens kan dat absoluut wel. Wanneer je een AI IDE zoals Cursor gebruikt, wil je dat de AI de *volledige* codebase in één keer ziet. Als uw code is opgedeeld in vijftig geïsoleerde GitHub-opslagplaatsen, mist de AI de context om te begrijpen hoe de frontend-knop verbinding maakt met de backend-database. Een Monolith biedt de LLM een perfecte, uniforme context, waardoor de AI binnen enkele seconden grote stukken code feilloos kan reconstrueren.

## De snelheid van lokale uitvoering

De uit 10 personen bestaande "Micro-Enterprise" wint door pure snelheid. U kunt niet over snelheid beschikken als voor de implementatie van één functie drie verschillende API-contracten in drie verschillende opslagplaatsen moeten worden bijgewerkt.

Een moderne, goed gestructureerde Monolith (vaak gebouwd in zeer productieve raamwerken zoals Ruby on Rails of Next.js) stelt één enkele Full-Stack Generalist in staat om de frontend-UI te bouwen, de backend-logica te schrijven en het databaseschema in één enkele commit bij te werken. De iteratiesnelheid is een orde van grootte hoger.

## Wanneer moet je het echt uit elkaar halen?

Schaalt de Monolith voor altijd? Nee. Maar het schaalt aanzienlijk verder dan de meeste oprichters denken. Een goed ontworpen Monolith kan comfortabel miljoenen dollars aan ARR en honderdduizenden gebruikers verwerken.

Je extraheert alleen een microservice als je een strikt technisch knelpunt tegenkomt (je hebt bijvoorbeeld een specifieke videoweergavefunctie die enorme GPU-computerkracht vereist, dus isoleer je deze). Tot dat exacte moment moet de architectuur verenigd blijven, waardoor de AI met maximale context kan werken en het menselijke team met maximale snelheid kan werken.

## Belangrijkste afhaalrestaurants

- Stop met het kopiëren van Netflix. Netflix heeft 'Microservices' nodig omdat ze 10.000 technici hebben. Als uw startup vijf ingenieurs heeft, zal het opbreken van uw code in vijftig kleine stukjes een enorme, onbeheersbare nachtmerrie creëren.

- De 'Monoliet' is sneller. Door al uw code in één gigantische map (een Monolith) te plaatsen, kan één programmeur binnen een paar uur een nieuwe functie bouwen. In een Microservice-systeem kan het bouwen van dezelfde functie drie weken en een team van ingenieurs duren.

- AI heeft het hele plaatje nodig. Als je wilt dat een AI-bot een bug in je code repareert, moet de AI de hele codebasis lezen. Als uw code verborgen is in 50 verschillende microservices, raakt de AI in de war. De Monolith geeft de AI een perfect zicht.

- Bespaar geld op servers. Het uitvoeren van 50 verschillende microservices vereist een ongelooflijk dure cloudserverarchitectuur (zoals Kubernetes). Het gebruik van één Monolith is veel goedkoper en gemakkelijker te onderhouden.

- Splits het alleen als het breekt. Bouw een Monoliet totdat je letterlijk miljoenen gebruikers hebt en de server het fysiek niet meer aankan. Pas dan moet je beginnen met het afbreken van kleine stukjes in microservices.

## Herwin uw technische snelheid

Besteedt uw technische team 40% van hun tijd aan het beheren van complexe Kubernetes-clusters en het opsporen van bugs in tientallen gefragmenteerde microservices in plaats van aan het verzenden van producten? **LaunchStudio** helpt startups terug te keren naar de zeer productieve 'Majestic Monolith'-architectuur. We maken gebruik van AI-agenten met enorme context om verspreide codebases veilig te herstructureren in uniforme, nauw gekoppelde opslagplaatsen, waardoor uw AWS-facturen drastisch worden verlaagd en het vermogen van uw team wordt hersteld om functies razendsnel te verzenden.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: microservices herstructureren tot een modulaire Node.js-monoliet

Benjamin, een coördinator, gebruikte **Bolt** om een verzendapp te bouwen. Complexe routeringsconfiguraties voor microservices zorgden voor een hoge latentie tijdens piekuren.

Hij werkte samen met **LaunchStudio (door Manifera)** om services samen te stellen in een modulaire Node.js-monoliet.

**Resultaat:** De API-latentie is gedaald van 1,2 seconde naar 80 ms, waardoor vertragingen bij het afrekenen zijn opgelost.

**Kosten en tijdlijn:** € 3.400 (architectuurrefactoring) — productieklaar en binnen 8 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een 'Monoliet' in coderen?

Het betekent dat u al uw code voor een website in één enorme, gigantische map plaatst. Het is eenvoudig te bouwen, maar als één regel code kapot gaat, gaat de hele website uit de lucht.

### Wat zijn 'Microservices'?

Het tegenovergestelde van een monoliet. Je snijdt de website in 50 kleine, afzonderlijke stukjes (zoals een stuk alleen voor facturering, een stuk alleen voor logins). Als het factureringsgedeelte kapot gaat, werkt het inloggedeelte nog steeds.

### Waarom haatten mensen Microservices?

Omdat ze een nachtmerrie zijn om te beheren. In plaats van fouten in één app te debuggen, moet je vijftig verschillende apps debuggen die allemaal via internet met elkaar praten. Er is een enorm team van dure DevOps-ingenieurs voor nodig om het draaiende te houden.

### Waarom brengt AI de Monoliet terug?

AI-coderingstools (zoals Cursor) zijn ongelooflijk goed in het lezen en repareren van een enorme Monolith-codebasis. Doordat de AI de hele map direct kan lezen, is de Monolith niet meer ‘te groot om te beheren’ voor een klein team.

### Moeten startups Microservices gebruiken?

Bijna nooit. Tenzij je zo groot bent als Netflix of Uber, is het bouwen van microservices een enorme verspilling van tijd en geld. Startups moeten een 'Majestic Monolith' bouwen om zo snel mogelijk vooruit te komen.