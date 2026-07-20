---
Titel: Hype Onderscheiden van Actual AI in Startups
Trefwoorden: AI om te coderen, Efficiënt, Data, Ophalen, Volgende, AI, Apps
Koperfase: Bewustzijn
---

# Hype Onderscheiden van Actual AI in Startups
AI-toepassingen zijn ongelooflijk data-hongerig. U moet tegelijkertijd de abonnementsstatus van de gebruiker, zijn eerdere chatgeschiedenis uit een database en realtime streaming-tokens van een LLM ophalen. Als u deze gegevens slecht ophaalt, zal uw app last hebben van 'waterval'-laadschermen en zal de UX snel verslechteren. Next.js App Router biedt de tools om dit te verhelpen, op voorwaarde dat u ze correct gebruikt.

## De waterval doden

Een ‘waterval’ is de vijand van prestatie. Het komt voor wanneer u opeenvolgende `await`-oproepen gebruikt in een servercomponent:

In dit scenario wacht de gebruiker twee seconden voordat hij de pagina ziet. De chatgeschiedenisquery wordt geblokkeerd totdat de gebruikersgegevens zijn geladen.

**De oplossing: parallel ophalen van gegevens**. Gebruik `Promise.all` om beide ophaalacties tegelijkertijd te starten:

Nu worden beide verzoeken gelijktijdig uitgevoerd en wordt de pagina binnen 1 seconde geladen. Deze eenvoudige architectonische verandering halveert direct de laadtijd van uw dashboard.

## Streaming-UI met React Suspense

Zelfs bij parallel ophalen zijn sommige AI-query's inherent traag. Als het berekenen van de gebruiksanalyses van een gebruiker drie seconden duurt, wil je niet dat het hele dashboard leeg blijft terwijl je wacht op dat ene diagram.

Je moet **React Suspense** gebruiken. Verpak de langzame analysecomponent in een `<Suspense fallback={<SkeletonLoader />}>` grens. Next.js streamt onmiddellijk de snelle delen van de pagina (de zijbalk, de navigatie, het actieve chatvenster) naar de gebruiker, terwijl een glinsterende skeletlader wordt weergegeven waar uiteindelijk het analysediagram zal verschijnen. De gebruiker ervaart de app als extreem snel omdat hij onmiddellijk met de kerninterface kan communiceren.

## Mutaties met serveracties

Wanneer een gebruiker een actie onderneemt (zoals het verwijderen van een eerder AI-chatlogboek), moet u de database muteren en de gebruikersinterface bijwerken. In traditionele React vereiste dit het instellen van API-eindpunten, het beheren van laadstatussen en het handmatig ophalen van de bijgewerkte lijst.

Next.js **Serveracties** vereenvoudigen dit volledig. Je schrijft een beveiligde serverfunctie die de chat uit Supabase verwijdert, en dan roep je `revalidatePath('/dashboard')` aan. Next.js doet de rest, waarbij de cache automatisch wordt leeggemaakt en het scherm van de gebruiker naadloos wordt bijgewerkt zonder dat de pagina opnieuw hoeft te worden geladen of dat er complex statusbeheer nodig is.

## Dure AI-oproepen in de cache opslaan

Als uw app zware gegevenscategorisatie uitvoert met behulp van een LLM die voor elke gebruiker identiek is (bijvoorbeeld door branchetags te categoriseren), voer die LLM-aanroep dan niet uit bij elke pagina die wordt geladen.

Verpak de logica voor het ophalen van gegevens in de functie Next.js `unstable_cache`. De eerste gebruiker die op de pagina komt, activeert de dure LLM-oproep van vijf seconden. Next.js slaat de uitvoer op in de gegevenscache. De volgende 10.000 gebruikers krijgen direct het resultaat en u betaalt OpenAI precies $ 0 voor de volgende verzoeken.

## Belangrijkste inzichten

- Vermijd 'waterval'-query's in servercomponenten door `Promise.all` te gebruiken om gelijktijdig onafhankelijke gegevensbronnen op te halen.

- Gebruik React Suspense om direct de snelle delen van uw gebruikersinterface te streamen terwijl skeletladers worden weergegeven voor langzame, zware AI-gegevensophaalacties.

- Maak gebruik van Next.js-serveracties in combinatie met `revalidatePath` om databasegegevens naadloos te muteren en de gebruikersinterface bij te werken zonder handmatig statusbeheer.

- Standaard wordt gegevens veilig op de server opgehaald om te voorkomen dat API-sleutels aan de browser worden blootgesteld en om de JavaScript-payload aan de clientzijde te verminderen.

- Gebruik de ingebouwde cachingfuncties van Next.js om dure, statische AI ​​API-reacties in de cache op te slaan om de latentie en operationele kosten drastisch te verminderen.

## Beheers Next.js-gegevensarchitectuur

Is uw codebase verstrikt in complex statusbeheer? **LaunchStudio** implementeert schone, efficiënte Next.js App Router-architecturen met behulp van serveracties en spanningsstreaming.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: het elimineren van laadblokkeringen in een HR-cv-screener

Lucas, een HR-recruiter, gebruikte **Bolt** om een app voor het screenen van cv's te bouwen. De pagina bleef enkele seconden leeg omdat de gegevens opeenvolgend werden opgehaald in plaats van parallel.

Hij werkte samen met **LaunchStudio (door Manifera)**. Het team heeft de gegevensophaallagen van Next.js opnieuw ontworpen om parallelle query's uit te voeren en React Suspense-streaming toegevoegd.

**Resultaat:** De initiële laadtijd van de pagina is gedaald naar 0,4 seconde met skeletladers voor streamingcomponenten.

**Kosten en tijdlijn:** € 1.600 (Next.js-optimalisatiepakket) — klaar voor productie en geïmplementeerd binnen 4 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een watervalquery?

Het komt voor wanneer opeenvolgende gegevensophaalacties elkaar blokkeren (bijvoorbeeld wanneer wordt gewacht tot gebruikersgegevens zijn geladen voordat de chatgeschiedenis wordt geladen). Door dit op te lossen met `Promise.all` worden ze tegelijkertijd uitgevoerd.

### Moet ik gegevens ophalen in servercomponenten of clientcomponenten?

Standaard voor het ophalen van initiële gegevens in Servercomponenten. Ze ondervragen veilig de database zonder API-sleutels vrij te geven en verminderen de JavaScript-payload die naar de gebruiker wordt verzonden.

### Hoe helpt React Suspense AI-toepassingen?

Hiermee kunt u delen van de gebruikersinterface direct streamen terwijl andere delen nog worden geladen. U kunt het hoofddashboard weergeven terwijl u een skeletlader weergeeft voor een langzame AI-visualisatiecomponent.

### Kan ik AI API-reacties in Next.js in de cache opslaan?

Ja. Als een API-oproep statische, niet-gepersonaliseerde gegevens retourneert, gebruik dan de cachefuncties van Next.js om de dure AI-reactie op te slaan, waardoor API-kosten worden bespaard bij volgende gebruikersbezoeken.