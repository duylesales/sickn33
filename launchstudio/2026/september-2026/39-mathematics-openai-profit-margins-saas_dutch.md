---
Titel: De wiskunde van OpenAI-winstmarges achter Het beste van AI
Trefwoorden: Het beste van AI, Wiskunde, OpenAI, Winst, Marges
Koperfase: Overweging
---

# De wiskunde van OpenAI-winstmarges achter Het beste van AI
Durfkapitalisten beoordelen softwarebedrijven op basis van brutomarges. Als je een prachtige AI-applicatie bouwt, maar het kost je $ 0,80 aan rekenkracht om $ 1,00 aan inkomsten te genereren, dan is je startup niet meer te investeren. De meeste oprichters raden hun abonnementsprijzen aan op basis van wat hun concurrenten vragen. In de AI-sector is gokken fataal. U moet uw eenheidseconomie wiskundig berekenen tot op het individuele token.

## Kosten per zoekopdracht (CPQ) berekenen

De fundamentele eenheid van de AI-economie is de **Cost Per Query (CPQ)**. Dit is het exacte bedrag dat het uw startup kost elke keer dat een gebruiker op de knop 'Genereren' klikt. 

CPQ omvat niet alleen de LLM-kosten. Het is een meerstapsformule:

1. **Kosten systeemprompt:** (Woorden in backend-prompt / 0,75) * Prijs invoertoken

2. **RAG-contextkosten:** (woorden opgehaald uit vectordatabase / 0,75) * Prijs van invoertoken

3. **Generatiekosten:** (gemiddelde woorden in AI-antwoord / 0,75) * Outputtokenprijs

*Opmerking: 1 token is ongeveer gelijk aan 0,75 woorden. Uitvoertokens zijn bijna altijd 3x tot 5x duurder dan invoertokens.*

## Het break-evenpunt van de gebruiker

Zodra u weet dat uw CPQ precies € 0,05 bedraagt, kunt u uw **User Break-even Point** berekenen. 

Als u een gebruiker $ 20/maand in rekening brengt voor een abonnement, deelt u de opbrengst door de CPQ ($ 20,00 / $ 0,05 = 400). 

400 is uw break-evenpunt. Als een gebruiker 400 keer per maand op de genereren-knop klikt, is uw brutomarge op die gebruiker 0%. Als ze er 500 keer op klikken, heb je € 5,00 verloren. Deze wiskunde bewijst waarom het aanbieden van "onbeperkte" opwekking op een vast abonnement een gegarandeerde weg naar faillissement is.

## Optimalisatie van de margeformule

Als uit uw berekening blijkt dat uw verwachte brutomarge een schamele 30% bedraagt, heeft u drie hefbomen die u kunt gebruiken om de wiskunde op te lossen:

**Hefboom 1: prijzen verhogen.** De eenvoudigste oplossing. Als de CPQ hoog is omdat de AI enorme bedrijfswaarde levert (zoals het schrijven van een complexe juridische briefing), breng dan geen €20/maand in rekening. Breng $ 200/maand in rekening. Op waarde gebaseerde prijzen zorgen ervoor dat de marges onmiddellijk worden hersteld.

**Hefboom 2: Verklein de output.** Omdat outputtokens 5x duurder zijn dan inputtokens, is uitgebreide AI een risico. Wijzig uw systeemprompt: *"Geef het antwoord in precies twee zinnen op. Wees zeer beknopt."* Als u de uitvoerlengte halveert, wordt de CPQ drastisch verlaagd.

**Hefboom 3: Routeer het model.** Als de CPQ $0,05 is bij gebruik van GPT-4o, routeer dan exact dezelfde prompt naar `gpt-4o-mini` of `claude-3-haiku`. De CPQ zal onmiddellijk dalen naar $0,002, waardoor een negatieve marge in een melkkoe verandert.

## De verborgen kosten van RAG-pijpleidingen

Oprichters vergeten vaak RAG (Retrieval-Augmented Generation) op te nemen in hun CPQ-wiskunde. Als uw RAG-pijplijn slordig is, kan deze tien enorme alinea's uit de database halen en deze in de prompt injecteren, zelfs als slechts één alinea relevant was.

U betaalt voor elk van die geïnjecteerde tokens. Door uw vectorzoekopdracht te optimaliseren om alleen de meest relevante segmenten van de "Top 2" te retourneren, wordt de grootte van de invoerprompt beperkt, waardoor de CPQ strikt begrensd blijft.

## Belangrijkste afhaalrestaurants

- Raad nooit uw prijs. U moet uw 'Cost Per Query' (CPQ) wiskundig berekenen om precies te begrijpen hoeveel geld uw bankrekening verlaat telkens wanneer een gebruiker de AI activeert.

- Bereken uw 'Gebruiker Break-even Point'. Als u € 20 per maand in rekening brengt en de CPQ € 0,10 is, wordt de gebruiker na 200 klikken onrendabel. U moet harde limieten in uw software implementeren voordat deze deze drempel bereiken.

- Uitvoertokens zijn het duurste onderdeel van de API. Uw AI instrueren om kort en bondig te zijn (in plaats van enorme paragrafen te schrijven) is een van de snelste manieren om de winstmarges te verbeteren.

- Als uw brutomarges lager zijn dan 50%, moet u een van de volgende drie hefbomen gebruiken: verhoog de abonnementsprijs, verkort de output van de AI drastisch of downgrade het backend-model naar een goedkoper niveau (zoals Haiku).

- Houd uw RAG-pijplijn in de gaten. Door enorme hoeveelheden onnodige databasetekst in de LLM-prompt te injecteren, worden uw invoertokenkosten voor elke afzonderlijke zoekopdracht stilzwijgend verhoogd.

## Herstel uw eenheidseconomie

Raadt u blindelings uw prijzen? Weet u precies hoeveel een enkele gebruikersklik uw startup kost? **LaunchStudio** voert rigoureuze wiskundige audits uit van AI-architecturen, waarbij RAG-pijplijnen en modelroutering worden geoptimaliseerd om gezonde, schaalbare SaaS-winstmarges te garanderen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: implementatie van tokenberekening-middleware voor een AI-assistent

Sofia, een SaaS-oprichter, gebruikte **Cursor** om een persoonlijke assistent te bouwen. Ze had moeite met het berekenen van de brutomarges omdat de symbolische kosten niet in DB werden bijgehouden.

Ze nam contact op met **LaunchStudio (door Manifera)**. Het team heeft NestJS-middleware gebouwd die het tokengebruik berekent op basis van headers en dit opslaat in de database.

**Resultaat:** Realtime margestatistieken werden zichtbaar, waardoor ze de prijsniveaus kon optimaliseren.

**Kosten en tijdlijn:** € 1.600 (NestJS Middleware-installatie) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Hoe berekent u de Cost Per Query (CPQ)?

Voeg de kosten van de invoertokens (de enorme backend-prompt + de vraag van de gebruiker) toe aan de kosten van de uitvoertokens (de door de AI gegenereerde tekst), op basis van het specifieke prijsniveau van het model dat u gebruikt.

### Waarom zijn uitvoertokens gevaarlijker dan invoertokens?

API-providers rekenen een enorme premie (vaak 3x tot 5x meer) voor de tekst die de AI genereert in vergelijking met de tekst die u verzendt. Uitgebreide AI-reacties verbruiken uw budget veel sneller dan grote prompts.

### Wat is het break-evenpunt van de gebruiker?

Het exacte aantal keren dat een gebruiker uw AI-functie moet gebruiken voordat zijn API-kosten hoger zijn dan het geld dat hij u voor zijn maandelijkse abonnement heeft betaald. Bij elke klik voorbij dit punt verliest het bedrijf geld.

### Wat is een gezonde brutomarge voor AI SaaS?

Terwijl traditionele SaaS streeft naar 85%, betekenen de hoge rekenkosten van LLM's dat een gezonde AI SaaS-marge doorgaans tussen 65% en 75% ligt. Als het onder de 50% daalt, faalt uw prijsmodel.