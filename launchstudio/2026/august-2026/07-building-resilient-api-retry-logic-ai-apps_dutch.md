---
Titel: Het bouwen van veerkrachtige API-retry-logica voor AI-applicaties
Trefwoorden: AI om te coderen, Bouwen, Veerkrachtig, API, Opnieuw proberen, Logica, AI, Applicaties
Koperfase: Bewustzijn
---

# Bouwen van veerkrachtige API-retry-logica voor AI-applicaties
Als je een SaaS bovenop de Stripe API bouwt, kun je redelijkerwijs een uptime van 99,99% verwachten. Als je een SaaS bovenop een LLM API bouwt, kun je mislukkingen verwachten. Generatieve AI is rekentechnisch beperkt. Tijdens piekuren genereren API-providers vaak 429 (Rate Limit) en 503 (Server Overload) fouten. Als uw code eenvoudigweg een onbewerkte fout naar de frontend gooit wanneer dit gebeurt, zullen uw gebruikers churnen. Hier leest u hoe u veerkrachtige, fouttolerante AI-applicaties kunt bouwen.

## De naïeve aanpak (en waarom deze faalt)

De meeste AI-prototypes die door junior-ontwikkelaars zijn gebouwd, gebruiken een naïef `try/catch`-blok:

Als OpenAI een hapering van 5 seconden heeft, krijgt de gebruiker een foutmelding. De gebruiker klikt vervolgens gefrustreerd opnieuw op "Genereren". Als 1.000 gebruikers dit tegelijkertijd doen, heb je het probleem actief verergerd.

## Exponentiële vertraging en jitter

De industriestandaard voor het afhandelen van API-fouten is **Exponentiële back-off met jitter**.

Wanneer het eerste verzoek mislukt, wacht de server 1 seconde en probeert het opnieuw. Als dat niet lukt, wacht het 2 seconden. Dan 4 seconden. Dan 8 seconden. Dit geeft de overbelaste API de tijd om te ademen.

**Jitter** is net zo belangrijk. Als uw app offline gaat en terugkomt, kunnen duizend verzoeken in de wachtrij allemaal in exact dezelfde milliseconde worden geactiveerd. Als ze allemaal een strikte uitstel van 2 seconden gebruiken, zullen ze het allemaal precies na 2 seconden opnieuw proberen, waardoor een "Donderende Kudde" ontstaat die de API opnieuw laat crashen. Jitter voegt een willekeurig aantal milliseconden toe (bijvoorbeeld 2,14 seconden wachten, 1,89 seconden) om de nieuwe pogingen over het netwerk te verspreiden.

## De ultieme verdediging: terugvalmodellen

Soms hapert een API niet zomaar; het gaat een uur lang naar beneden. Als uw hele bedrijfsmodel uitsluitend op OpenAI vertrouwt, is een OpenAI-storing een existentiële bedreiging voor uw bedrijf.

U moet **Model Fallbacks** implementeren met behulp van een uniforme orkestratielaag (zoals de Vercel AI SDK of een open-sourcerouter zoals LiteLLM).

De logica zou moeten zijn:

1. Probeer GPT-4o te bellen.

2. Als het mislukt, gebruik dan exponentieel uitstel om het twee keer opnieuw te proberen.

3. Als het nog steeds niet lukt, wissel dan automatisch de API-sleutel en het eindpunt om en stuur exact dezelfde prompt door naar Claude 3.5 Sonnet van Anthropic.

4. Als dat niet lukt, routeer dan naar Google Gemini.

De eindgebruiker weet nooit dat OpenAI offline is. Ze ervaren gewoon een iets langere generatietijd. Uw applicatie blijft 100% beschikbaar terwijl concurrenten die afhankelijk zijn van één enkele provider boze klantenondersteuningstickets afhandelen.

## Sierlijke UI-degradatie

Wanneer uw backend nieuwe pogingen en fallbacks uitvoert, kan de totale responstijd oplopen tot 10 of 15 seconden. Als de gebruiker alleen maar naar een generiek draaiend wiel staart, gaan ze ervan uit dat de app is vastgelopen en klikken ze op vernieuwen (waarbij de hele dure lus opnieuw wordt gestart).

U moet statusupdates naar de gebruikersinterface streamen. De gebruikersinterface zou het volgende moeten weergeven:

- *"Verbinding maken met primaire AI..."* (0s)

- *"Er is veel verkeer gedetecteerd, er wordt geprobeerd alternatieve servers te gebruiken..."* (3s)

- *"Reactie genereren..."* (7s)

Transparantie schept vertrouwen en geduld.

## Belangrijkste inzichten

- AI API's falen regelmatig vanwege de enorme rekenoverhead die generatieve modellen vereisen; je moet architect zijn voor mislukking.

- Gooi nooit bij de eerste fout een onbewerkte API-fout naar de gebruiker. Implementeer automatische nieuwe pogingen aan de serverzijde.

- Gebruik Exponential Backoff om steeds langer te wachten tussen nieuwe pogingen, en voeg Jitter toe om het "Thundering Herd" -probleem te voorkomen.

- Implementeer Fallback-modellen (bijvoorbeeld routering naar Anthropic als OpenAI niet beschikbaar is) om ervoor te zorgen dat uw app online blijft tijdens uitval van de provider.

- Stream statusupdates naar de gebruikersinterface, zodat de gebruiker begrijpt waarom een ​​generatie langer duurt dan normaal, waardoor wordt voorkomen dat de pagina wordt vernieuwd.

## Garandeer 99,9% uptime voor uw SaaS

Zorg ervoor dat een uitval van een provider uw bedrijf niet kapotmaakt. **LaunchStudio** implementeert robuuste API-routing, fallback-logica en veerkrachtige backend-architectuur om ervoor te zorgen dat uw AI-app altijd beschikbaar is.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: veerkracht toevoegen aan een klantsentimentclassificator

Thomas, een klantsuccesmanager, gebruikte **Lovable** om een tool voor beoordelingsanalyse te bouwen. Plotselinge Anthropic API-snelheidslimieten crashten actieve gebruikerssessies en verloren gegevens.

Hij werkte samen met **LaunchStudio (door Manifera)** om logica voor exponentiële uitstelpogingen en een asynchrone taakwachtrij voor mislukte aanvragen te implementeren.

**Resultaat:** Het API-foutpercentage daalde naar nul en gebruikerssessies bleven ononderbroken tijdens storingen.

**Kosten en tijdlijn:** € 1.400 (veerkrachtig API-pakket) — productieklaar en binnen 3 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom falen AI API's vaker dan standaard API's?

Generatieve AI vereist enorme rekenkracht. Tijdens piekuren ervaren providers vaak serveroverbelasting (503-fouten) of hanteren ze strikte tarieflimieten (429-fouten). Je moet deze mislukkingen verwachten.

### Wat is exponentiële uitstel?

Het is een algoritme dat steeds langer wacht tussen API-pogingen (bijvoorbeeld 1s, 2s, 4s). Het geeft de overbelaste API de tijd om te herstellen in plaats van deze te spammen met onmiddellijke nieuwe pogingen.

### Wat is een Fallback Model-strategie?

Als uw primaire API (OpenAI) uitvalt, vangt uw code de fout automatisch op en stuurt de prompt stilletjes door naar een alternatieve provider (Anthropic), waardoor uw app online blijft.

### Welke invloed heeft dit op de gebruikersinterface?

Omdat nieuwe pogingen en terugval enige tijd in beslag nemen (bijvoorbeeld 10 seconden), moet u dynamische UI-updates bieden (zoals 'Routing naar alternatieve servers...') om de gebruiker op de hoogte te houden en te voorkomen dat hij of zij de pagina vernieuwt.