---
Titel: Het volgen van de juiste KPI's voor generatieve SaaS
Trefwoorden: AI om te coderen, Tracking, Rechts, KPI's, Generatief, SaaS
Koperfase: Bewustzijn
---

# Het volgen van de juiste KPI's voor generatieve SaaS
Als u een traditioneel SaaS-bedrijf leidt, is een piek in het aantal dagelijkse actieve gebruikers (DAU) reden voor een feestje. Als u een generatieve AI-startup uitvoert, kan een plotselinge, ongecontroleerde piek in intensief gebruik betekenen dat u duizenden dollars per dag aan API-kosten verliest. De eenheidseconomie van AI vereist een geheel nieuwe reeks Key Performance Indicators (KPI’s). Als u alleen naar MRR (Monthly Recurring Revenue) kijkt, vliegt u blind.

## KPI 1: AI-brutomarge per gebruiker

In traditionele software schommelen de brutomarges rond de 90%. Bij AI-wrappers kunnen de marges gemakkelijk negatief worden als de limieten niet worden afgedwongen. U moet de **AI-brutomarge** nauwgezet volgen op het niveau van individuele gebruikerscohorten.

Formule: `(Abonnementsinkomsten - (OpenAI-tokenkosten + Vector DB-kosten + Generatie-infrastructuur)) / Abonnementsopbrengsten'

Als u €30 per maand in rekening brengt en een hoofdgebruiker €25 aan Anthropic API-aanroepen verbruikt, bedraagt uw marge op die gebruiker een gevaarlijke 16%. U moet telemetrie (zoals PostHog) gebruiken om bij elke generatie de exacte API-tokenkosten aan de gebruikers-ID te koppelen. Als een cohort onder de brutomarge van 60% komt, moet u uw prijsniveaus onmiddellijk aanpassen of tarieflimieten afdwingen.

## KPI 2: Succespercentage van generaties (GSR)

Een AI die snel tekst genereert, is nutteloos als de tekst gehallucineerd afval is. U moet de kwaliteit van de output van uw AI kwantitatief meten via het **Generation Success Rate**.

Je kunt niet elke output zelf lezen. U moet de gebruikersinterface instrumenteren om impliciete en expliciete feedback vast te leggen:

- **Expliciet:** Knoppen Duim omhoog / Duim omlaag naast het gegenereerde resultaat.

- **Impliciet (beter):** Heeft de gebruiker op de knop 'Kopiëren naar klembord' geklikt? Hebben ze op 'Opslaan in database' geklikt? Hebben ze onmiddellijk op "Regenereren" gedrukt?

Als de gebruiker drie keer achter elkaar op 'Regenereren' klikt, is de GSR voor die sessie mislukt. Als uw totale GSR onder de 80% daalt, geeft dit aan dat uw systeemprompts kapot gaan (of dat OpenAI de modelgewichten heeft bijgewerkt), wat direct een enorme piek in het verloop volgende maand voorspelt.

## KPI 3: Time-to-Value (TTV)

Geduld bestaat in het AI-tijdperk niet. Een gebruiker verwacht direct een goocheltruc. **Time-to-Value** meet het exacte aantal seconden vanaf het moment dat de gebruiker op 'Aanmelden' klikt tot het moment dat hij zijn eerste succesvolle AI-generatie ontvangt.

Als uw onboardingproces hen dwingt hun e-mail te verifiëren, een instructievideo van 3 minuten te bekijken en drie API's aan te sluiten voordat ze de generator kunnen gebruiken, is uw TTV 10 minuten. 80% van de gebruikers zal de app verlaten. U moet uw onboarding zo vormgeven dat u een succesvolle AI "Aha!" moment binnen 60 seconden.

## KPI 4: Functiespecifieke latentie

Bij webontwikkeling houden we de laadsnelheid van pagina’s bij. In AI houden we **Time to First Token (TTFT)** en de totale generatielatentie bij. Als uw AI er twaalf seconden over doet om een ​​samenvatting te genereren, zullen gebruikers de app als defect beschouwen. U moet de latentie agressief bijhouden in uw backend. Als de latentie piekt (meestal als gevolg van een defecte OpenAI-server), zou uw telemetrie u moeten waarschuwen, zodat u verkeer automatisch kunt routeren naar een sneller fallback-model (zoals Claude Haiku) om de gebruikerservaring te behouden.

## Belangrijkste inzichten

- Standaard SaaS-statistieken (zoals pure MRR en DAU) zijn gevaarlijk voor AI-startups omdat ze de enorme variabele kosten van het genereren van API's negeren.

- Volg nauwgezet de 'AI-brutomarge per gebruiker'. Als hoofdgebruikers u meer aan API-tokens kosten dan ze aan abonnementskosten betalen, moet u onmiddellijk limieten afdwingen.

- Meet het 'Generation Success Rate' (GSR) door bij te houden hoe vaak gebruikers op 'Kopiëren' of 'Opslaan' klikken en hoe vaak ze op 'Opnieuw genereren' klikken of de prompt verlaten.

- Optimaliseer 'Time-to-Value' (TTV). Uw onboarding moet zo zijn ontworpen dat de gebruiker binnen 60 seconden na aanmelding een verbluffend AI-resultaat krijgt.

- Controleer voortdurend de generatielatentie (Time to First Token); Langzame AI-reacties verminderen het vertrouwen van gebruikers drastisch en verhogen het klantverloop.

## Instrumenteer uw groei

Bent u blind wat betreft uw werkelijke AI-kosten en succespercentages voor gebruikers? **LaunchStudio** implementeert diepgaande PostHog- en aangepaste telemetrie-architecturen om u realtime inzicht te geven in uw AI-brutomarges en generatiesuccespercentages.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: alleen-lezen databasereplica's toevoegen voor een Analytics-app

Scarlett, een oprichter, gebruikte **Cursor** om een AI-analyse-app te bouwen. De database werd vaak vergrendeld omdat er zware analyselezingen werden uitgevoerd op het primaire database-exemplaar.

Ze werkte samen met **LaunchStudio (door Manifera)** om een ​​alleen-lezen databasereplica in Supabase te configureren en alle dashboardleesquery's ernaar om te leiden.

**Resultaat:** De laadtijden van het dashboard daalden tot minder dan 300 ms en de primaire schrijfprestaties bleven snel.

**Kosten en tijdlijn:** € 1.850 (DB Scaling Package) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom zijn standaard SaaS-statistieken slecht voor AI?

Traditionele statistieken negeren de variabele kosten van AI. Een oprichter zou de hoge gebruikersbetrokkenheid kunnen vieren, maar zich niet realiseren dat zwaar dagelijks gebruik enorme OpenAI-facturen genereert die de abonnementskosten van de gebruiker overschrijden.

### Wat is AI-brutomarge?

Het zijn uw inkomsten minus uw directe API-kosten (OpenAI, ElevenLabs). Als een gebruiker €30/maand betaalt en u €10 uitgeeft aan zijn API-tokens, is uw marge 66%. U moet dit bijhouden om de winstgevendheid te garanderen.

### Wat is het generatiesuccespercentage (GSR)?

GSR meet hoe vaak de AI een bruikbaar antwoord geeft. U houdt dit bij door te kijken of de gebruiker op 'Kopiëren naar klembord' klikt in plaats van op 'Opnieuw genereren'. Een lage GSR voorspelt een hoog gebruikersverloop.

### Hoe meet je de Time-to-Value (TTV)?

TTV zijn de seconden die nodig zijn vanaf het aanmaken van een account tot de eerste succesvolle AI-uitvoer. Als TTV langer duurt dan 60 seconden vanwege complexe onboarding, is het afhakpercentage van gebruikers catastrofaal.