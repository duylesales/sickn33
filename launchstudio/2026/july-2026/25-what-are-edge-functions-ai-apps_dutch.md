---
Titel: Wat zijn Edge-functies en waarom gebruiken AI-apps ze? - AI en softwareontwikkeling
Trefwoorden: AI en softwareontwikkeling, Functies
Koperfase: Bewustzijn
---

# Wat zijn Edge-functies en waarom gebruiken AI-apps ze? - AI en softwareontwikkeling
Als u een AI-native startup bouwt met behulp van een serverloze architectuur, zult u uiteindelijk de term ‘Edge Function’ tegenkomen. Wanneer u uw AI-bouwer vraagt ​​een beveiligingsprobleem op te lossen of een API-sleutel te verbergen, zal de oplossing vrijwel altijd een Edge-functie omvatten. Maar wat zijn ze precies, en waarom zijn ze de cruciale ontbrekende schakel tussen een frontend-prototype en een veilige productie-app?

## Het probleem: de frontend kan geen geheimen bewaren

De meeste door AI gegenereerde apps bestaan uit een React-frontend en een Supabase-database. De React-code draait rechtstreeks in de browser van de gebruiker (Chrome, Safari). Omdat het op de computer van de gebruiker draait, kan de gebruiker het inspecteren, wijzigen en alle daarin verborgen gegevens extraheren.

Dit creëert een enorm probleem: als je de OpenAI API wilt gebruiken om tekst te genereren, of de Stripe API om een ​​betaling te verwerken, moet je een geheime sleutel opgeven. Als u die geheime sleutel in uw React-code plaatst, kan elke gebruiker deze stelen. U hebt een veilige tussenpersoon nodig: een server die u beheert, waar de geheimen veilig zijn voor nieuwsgierige blikken.

## Voer de Randfunctie in

Een Edge-functie is die veilige tussenpersoon. Het is een klein, gespecialiseerd stukje backend-code dat zich op een server bevindt, niet in de browser.

Het wordt "serverloos" genoemd, niet omdat er geen server is, maar omdat u er geen hoeft te beheren. U schrijft één JavaScript-bestand, uploadt dit naar Supabase of Vercel en het platform doet de rest. Het wordt 'edge' genoemd omdat de code wordt gerepliceerd en geïmplementeerd op servers over de hele wereld (de 'edge' van het netwerk). De code loopt dus geografisch dicht bij de gebruiker die het verzoek doet, waardoor bliksemsnelle responstijden worden gegarandeerd.

Wanneer een Edge-functie wordt aangeroepen, draait deze in milliseconden op, voert uw code uit, retourneert het resultaat en wordt onmiddellijk afgesloten. U betaalt alleen voor de exacte milliseconden die de code heeft uitgevoerd.

## Hoe het in de praktijk werkt

Laten we eens kijken naar de stroom voor het veilig genereren van AI-tekst met behulp van een OpenAI-sleutel:

1. **Het verzoek**: de gebruiker klikt op "Genereren" in uw React-app. De React-app roept *niet* OpenAI aan. In plaats daarvan stuurt het de prompt van de gebruiker naar uw Edge-functie (bijvoorbeeld `https://your-project.supabase.co/functions/v1/generate-text`).

2. **De veilige uitvoering**: de Edge-functie wordt geactiveerd. Het leest de `OPENAI_SECRET_KEY` die veilig is opgeslagen in de omgevingsvariabelen. Het koppelt de sleutel aan de prompt van de gebruiker en doet het officiële verzoek aan de servers van OpenAI.

3. **Het antwoord**: OpenAI verwerkt de tekst en stuurt deze terug naar de Edge-functie.

4. **De levering**: de Edge-functie stuurt de gegenereerde tekst terug naar de React-app in de browser van de gebruiker.

Gedurende dit hele proces heeft de OpenAI-sleutel de beveiligde server nooit verlaten. De gebruiker zag alleen de prompt en de uiteindelijke tekst.

## Veelvoorkomende gebruiksscenario's voor AI-startups

U hebt Edge Functions nodig voor elke bewerking waarvoor een geheime sleutel of verhoogde databaserechten vereist zijn:

- **Stripe-integratie**: voor het maken van betaalsessies en het verwerken van webhooks is de Stripe Secret Key vereist.

- **AI Inference**: OpenAI-, Anthropic- of Replicate-API's veilig aanroepen.

- **E-mails verzenden**: de API's Resend of SendGrid aanroepen om welkomst-e-mails of ontvangstbewijzen te verzenden.

- **RLS omzeilen**: soms moet uw app een administratieve databasetaak uitvoeren die normale gebruikers niet mogen uitvoeren (zoals het bijwerken van een globale systeemteller). Een Edge-functie kan de Supabase Service Role Key gebruiken om Row Level Security veilig te omzeilen.

## De beperkingen

Edge-functies zijn ongelooflijk qua snelheid en schaalbaarheid, maar ze hebben grenzen. Omdat ze zijn ontworpen om snel en tijdelijk te zijn, treedt er doorgaans een time-out op na 10 tot 60 seconden (afhankelijk van het platform). Ze hebben ook strikte geheugenlimieten. Als uw app een videobestand van 1 GB moet verwerken of een complexe achtergrondtaak moet uitvoeren die vijf minuten duurt, mislukt een Edge-functie. Voor deze zware werklasten heeft u een traditionele aangepaste backend-server nodig.

## Belangrijkste inzichten

- Edge Functions zijn kleine, serverloze backend-scripts die draaien op wereldwijde netwerken dichtbij de gebruiker.

- Ze fungeren als een veilige tussenpersoon tussen uw frontend React-app en services van derden.

- U moet Edge Functions gebruiken om geheime sleutels (Stripe, OpenAI) te verbergen voor de browser van de gebruiker.

- Ze starten onmiddellijk en u betaalt alleen voor de exacte gebruikte rekentijd.

- Ze hebben uitvoeringstijdlimieten (meestal minder dan 60 seconden) en kunnen geen langlopende achtergrondtaken aan.

## Beveilig uw architectuur

Zijn uw API-sleutels zichtbaar? LaunchStudio controleert uw codebase en migreert veilig alle gevoelige bewerkingen naar robuuste Edge Functions.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: dynamische PDF-generator

William, de oprichter van een startup, gebruikte **Lovable** om een prototype van een dynamische pdf-generator te bouwen. Hoewel de applicatie functioneel was, ondervond deze functietime-outfouten op serverloze Vercel-routes bij het genereren van complexe rapporten van meerdere pagina's.

William werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team migreerde de generatieworkflow naar Supabase Edge Functions met een asynchrone pollingarchitectuur.

**Resultaat:** William elimineerde time-outfouten voor gebruikers en ondersteunde het genereren van PDF's tot 200 pagina's.

**Kosten en tijdlijn:** € 1.750 (Edge Architecture-pakket) — productieklaar en binnen 6 werkdagen geïmplementeerd.

---
## Veelgestelde vragen

### Wat is een randfunctie?

Een Edge-functie is een klein stukje backend-code dat onmiddellijk op wereldwijde servers draait om een ​​specifiek verzoek af te handelen, waardoor geheimen veilig buiten de browser van de gebruiker worden gehouden.

### Waarom gebruiken AI-bouwers Edge-functies in plaats van normale servers?

Ze vereisen nul infrastructuurbeheer. Er is geen server om te configureren of te schalen. U schrijft een script, implementeert het en het platform doet de rest.

### Wanneer moet ik een Edge-functie in mijn app gebruiken?

Elke keer dat uw app een veilige actie moet uitvoeren waarvoor een geheime API-sleutel nodig is, zoals het verwerken van betalingen, het aanroepen van AI-modellen of het verzenden van transactionele e-mails.

### Kunnen Edge Functions langlopende taken zoals videoverwerking aan?

Nee. Ze hebben strikte uitvoeringstermijnen (10-60 seconden). Voor zware werklasten moet u een speciale aangepaste backend-server gebruiken.