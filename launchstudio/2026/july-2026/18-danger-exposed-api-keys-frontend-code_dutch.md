---
Titel: Het gevaar van blootliggende API-sleutels in uw frontendcode
Trefwoorden: Gevaar, Blootgesteld, Frontend
Koperfase: Bewustzijn
---

# Het gevaar van blootliggende API-sleutels in uw frontendcode

Een van de meest voorkomende en ernstige kwetsbaarheden in door AI gegenereerde code is het blootleggen van gevoelige API-sleutels rechtstreeks in het frontend JavaScript. Wanneer u een AI vraagt ​​om "OpenAI te integreren" of "verbinding te maken met Stripe", is de snelste manier om werkende code te produceren het hardcoderen van uw geheime sleutels rechtstreeks in de React-componenten. Hoewel hierdoor het prototype onmiddellijk functioneert, blijven de toetsen zichtbaar voor iedereen die weet hoe hij op F12 moet drukken.

## Hoe blootstelling plaatsvindt

Frontend-code (HTML, CSS en JavaScript aan de clientzijde) wordt door de browser van de gebruiker gedownload om de website weer te geven. U kunt logica of tekst die aan de clientzijde wordt uitgevoerd, niet verbergen. Als uw React-component een regel als `const stripeSecret = "sk_live_12345..."` bevat, wordt die exacte string naar elke bezoeker verzonden.

Hackers zoeken niet handmatig naar deze sleutels. Ze zetten geautomatiseerde bots in die GitHub-opslagplaatsen schrapen en live websites doorzoeken op zoek naar specifieke regex-patronen (zoals Stripe's `sk_live_` voorvoegsel). Een sleutel kan binnen enkele minuten nadat deze naar productie is geduwd, worden aangetast.

## De gevolgen van een compromis

De schade is afhankelijk van welke sleutel zichtbaar is:

- **Stripe Secret Key (sk_live)**: totale financiële ramp. Aanvallers kunnen terugbetalingen doen, opgeslagen kaarten in rekening brengen en abonnementen manipuleren.

- **Supabase Service Role Key**: Volledige overname van de database. Deze sleutel omzeilt alle Row Level Security-beleidsregels (RLS), waardoor aanvallers uw volledige gebruikersdatabase kunnen downloaden, wijzigen of verwijderen.

- **OpenAI / Antropische API-sleutels**: financiële belasting. Aanvallers kapen uw account om op uw kosten enorme gevolgtrekkingstaken uit te voeren, waardoor ze gemakkelijk duizenden dollars aan rekeningen kunnen verdienen voordat de provider u afsluit.

- **E-mailproviders (opnieuw verzenden, SendGrid)**: reputatieschade. Uw domein wordt gebruikt om spam- en phishing-e-mails te verzenden, waardoor uw afzenderreputatie wordt vernietigd en ervoor wordt gezorgd dat uw legitieme e-mails in de spammappen terechtkomen.

## Publieke versus geheime sleutels

Het is niet de bedoeling dat alle sleutels verborgen zijn. Moderne services gebruiken een dual-key-architectuur:

- **Publiceerbare/Anon-sleutels** (bijvoorbeeld Stripe's `pk_test`, Supabase's Anon-sleutel): deze zijn *ontworpen* om in de frontend te worden weergegeven. Ze zorgen ervoor dat de browser beperkte verzoeken kan initiëren. Ze blijven echter alleen veilig als de backend strikte regels oplegt (zoals RLS in Supabase) over waartoe deze sleutels toegang hebben.

- **Geheime sleutels** (bijvoorbeeld Stripe's `sk_test`, Supabase's Service Role Key): deze mogen **nooit** de frontend raken. Ze zijn alleen bedoeld voor server-naar-server-communicatie.

## De oplossing: omgevingsvariabelen en backend-proxy's

Het beveiligen van uw sleutels omvat twee architecturale verschuivingen:

1. **Gebruik omgevingsvariabelen**: in plaats van `"sk_live_123"` hard te coderen, moet uw code verwijzen naar `process.env.STRIPE_SECRET_KEY`. De werkelijke waarde wordt veilig geconfigureerd in het dashboard van uw hostingprovider (zoals Vercel of Netlify) en alleen geïnjecteerd tijdens het bouwen of uitvoeren aan de serverzijde.

2. **Verplaats logica naar de backend**: als uw frontend een verzoek moet indienen bij OpenAI, mag deze OpenAI niet rechtstreeks aanroepen. De frontend moet uw eigen backend-API-route aanroepen (bijvoorbeeld `/api/generate-text`). De backend-route, die veilig op de server draait, koppelt de geheime OpenAI-sleutel, doet het verzoek en stuurt het resultaat terug naar de frontend.

Als u een blootgestelde sleutel ontdekt, is het niet voldoende om deze uit de code te verwijderen. U moet naar het dashboard van de provider gaan, de oude sleutel intrekken, een nieuwe genereren en uw beveiligde omgevingsvariabelen bijwerken.

## Belangrijkste inzichten

- AI-tools coderen regelmatig geheime API-sleutels in frontend-code om prototypes snel te laten werken.

- Elke code die naar de frontend (browser) wordt verzonden, is zichtbaar voor gebruikers en geautomatiseerde scraping-bots.

- Blootgestelde geheime sleutels kunnen leiden tot databasediefstal, enorme financiële kosten en het kapen van accounts.

- Geheime sleutels moeten worden verplaatst naar omgevingsvariabelen aan de serverzijde en alleen worden gebruikt in backend-API-routes of edge-functies.

- Als een sleutel ooit wordt blootgesteld, moet deze onmiddellijk worden ingetrokken en vervangen.

## Vergrendel je geheimen

LaunchStudio controleert uw volledige codebase, verplaatst alle geheimen naar beveiligde omgevingsvariabelen en herstructureert logica in veilige backend-routes.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: samenvatting van juridische documenten

Isabella, een startup-oprichter, gebruikte **Bolt** om een prototype van een samenvatting van juridische documenten te bouwen. Hoewel de applicatie functioneel was, werd haar privé Anthropic API-sleutel in de browserconsole zichtbaar, waardoor ze een hoge rekening riskeerde vanwege sleuteldiefstal.

Isabella werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team verwijderde de sleutel uit de frontend-code, zette een veilige Vercel Edge-functie op en stuurde alle LLM-verzoeken via de backend.

**Resultaat:** Isabella heeft de API-sleutels beveiligd, waardoor ongeautoriseerde toegang wordt voorkomen en de limieten voor LLM-aanvragen worden vergrendeld.

**Kosten en tijdlijn:** € 800 (Secrets Security Package) — productieklaar en binnen 3 werkdagen geïmplementeerd.

---
## Veelgestelde vragen

### Hoe vinden hackers API-sleutels in mijn frontend-code?

Hackers gebruiken geautomatiseerde bots die voortdurend openbare GitHub-repository's scannen en live websites schrapen, op zoek naar bekende sleutelvoorvoegsels zoals "sk_live" of "secret".

### Wat kan iemand doen met mijn zichtbare Stripe Secret Key?

Een blootgelegd Streepgeheim geeft administratieve controle. Aanvallers kunnen terugbetalingen doen, frauduleuze kosten op opgeslagen kaarten maken en producten verwijderen, waardoor financiële verliezen ontstaan.

### Zijn er API-sleutels die veilig openbaar kunnen worden gemaakt?

Ja, 'Publiceerbare' sleutels (zoals Stripe pk_live) en 'Anon'-sleutels (Supabase) zijn ontworpen voor frontend-gebruik, op voorwaarde dat uw backend strikte beveiligingsregels afdwingt.

### Als mijn sleutel zichtbaar is maar ik de code heb verwijderd, ben ik dan veilig?

Nee. Bots schrapen repository's onmiddellijk. U moet ervan uitgaan dat de sleutel gecompromitteerd is, deze intrekken in het dashboard van de provider en een nieuwe genereren.