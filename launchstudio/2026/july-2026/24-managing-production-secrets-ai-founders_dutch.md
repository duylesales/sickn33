---
Titel: "Productiegeheimen beheren: een gids voor AI-native oprichters"
Trefwoorden: AI For Coding, Productiegeheimen, AI-native Founder, Beveiliging
Koperfase: overweging
---

# Productiegeheimen beheren: een gids voor AI-native oprichters
Een van de gevaarlijkste gewoonten die AI-bouwers aanleren, is het hardcoderen van API-sleutels. Wanneer je Lovable vraagt ​​om Stripe toe te voegen, worden de sleutels vaak rechtstreeks in je React-componenten geplaatst, zodat de demo meteen werkt. Als u van een demo naar een productielancering gaat, moet u alle gevoelige strings uit uw codebase extraheren en deze beheren als omgevingsvariabelen. Hier is de niet-technische handleiding voor het beheren van productiegeheimen.

## Wat is een geheim?

Een geheim is elk stukje gegevens dat toegang verleent tot uw infrastructuur, gebruikersgegevens of factureringsaccounts. Als een kwaadwillende actor deze string te pakken krijgt, kan hij financiële of reputatieschade veroorzaken. Veel voorkomende geheimen zijn onder meer:

- **Geheime streepsleutel (`sk_live_...`)**

- **Supabase Service Role Key** (omzeilt alle beveiligingsregels)

- **OpenAI / Antropische API-sleutels**

- **Databaseverbindingsreeksen** (bijvoorbeeld `postgresql://...`)

- **JWT-geheimen** (gebruikt voor het ondertekenen van authenticatietokens)

*Opmerking: "Publiceerbare" sleutels (zoals `pk_live_...` voor Stripe of de Supabase `anon` sleutel) zijn geen geheimen. Ze zijn ontworpen om openbaar te zijn.*

## De gouden regel van geheimen

**Er mag nooit een geheim in je frontend-code voorkomen, en het mag nooit in je Git-repository worden vastgelegd.**

Als je een bestand met een OpenAI-sleutel in een openbare GitHub-repository plaatst, zullen geautomatiseerde bots dit bestand schrappen en binnen enkele minuten duizenden dollars aan kosten in rekening brengen. Zelfs in een privéopslagplaats vormt het opslaan van geheimen in code een enorm veiligheidsrisico.

## Hoe omgevingsvariabelen werken

In plaats van de sleutel in uw code te schrijven, gebruikt u een tijdelijke aanduiding. In Node.js- of edge-omgevingen ziet dit eruit als `process.env.STRIPE_SECRET_KEY`.

Maar waar haalt die tijdelijke aanduiding zijn waarde vandaan? Vanuit de omgeving waarin de code wordt uitgevoerd:

- **Lokale ontwikkeling**: de waarden bevinden zich in een verborgen bestand op uw computer met de naam `.env`. (Je moet ervoor zorgen dat `.env` wordt vermeld in je `.gitignore`-bestand, zodat het nooit naar GitHub wordt geüpload).

- **Productiehosting (Vercel/Netlify)**: De waarden worden ingevoerd in een beveiligd dashboard op de website van de hostingprovider. Tijdens de implementatie injecteert de provider deze waarden veilig in de serveromgeving.

## De frontend-blootstellingsval

In moderne frameworks zoals Next.js en Vite worden omgevingsvariabelen standaard verborgen voor de browser. Deze raamwerken bieden echter een mechanisme om variabelen expliciet aan de frontend bloot te stellen als dat nodig is (bijvoorbeeld voor uw Stripe Publishable Key).

- In Vite: Variabelen met het voorvoegsel `VITE_` (bijvoorbeeld `VITE_SUPABASE_ANON_KEY`) worden zichtbaar voor de browser.

- In Next.js: variabelen met het voorvoegsel `NEXT_PUBLIC_` worden zichtbaar in de browser.

**De valstrik**: Oprichters raken vaak gefrustreerd als hun OpenAI-sleutel niet werkt in de frontend. Om de fout te "repareren", hernoemen ze de variabele naar `VITE_OPENAI_KEY`. De code werkt, maar ze hebben zojuist hun geheime sleutel afgeleverd aan elke gebruiker die de site bezoekt. **Voeg een geheime sleutel nooit toe met VITE_ of NEXT_PUBLIC_.**

## Hoe u veilig API's van derden kunt aanroepen

Als u de OpenAI-sleutel niet in de frontend kunt plaatsen, hoe communiceert uw app dan met OpenAI?

U moet een proxybenadering gebruiken via een Edge-functie (of serverloze functie). De stroom werkt als volgt:

1. Uw React-frontend stuurt een verzoek naar uw *eigen* backend-route (bijvoorbeeld `/api/generate-text`) gehost op Vercel of Supabase.

2. Deze veilige backend-route haalt de `OPENAI_API_KEY` uit de omgevingsvariabelen van de server.

3. De backend doet het verzoek aan OpenAI.

4. OpenAI stuurt het resultaat naar de backend.

5. De backend stuurt het resultaat naar de frontend.

Deze architectuur houdt de geheime sleutel veilig op de server.

## Belangrijkste inzichten

- Codeer nooit API-sleutels, database-URL's of wachtwoorden in uw broncode.

- Leg nooit uw lokale `.env`-bestand vast in GitHub; zorg ervoor dat het wordt toegevoegd aan `.gitignore`.

- Beheer productiegeheimen veilig via het Vercel-, Netlify- of Supabase-dashboard.

- Gebruik nooit de voorvoegsels `VITE_` of `NEXT_PUBLIC_` voor geheime sleutels, omdat deze hierdoor zichtbaar worden voor de browser.

- Om geheime sleutels (zoals OpenAI) te gebruiken, routert u verzoeken via beveiligde backend Edge-functies in plaats van ze rechtstreeks vanuit React aan te roepen.

## Vergrendel uw architectuur

LaunchStudio controleert uw volledige codebase op openbaar gemaakte geheimen, implementeert veilige Edge-functies en configureert de variabelen van uw productieomgeving.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: medische transcriptie SaaS

Evelyn, een startup-oprichter, gebruikte **Bolt** om een saas-prototype voor medische transcriptie te bouwen. Hoewel de applicatie functioneel was, heeft deze tijdens snelle foutopsporing per ongeluk verbindingsreeksen van de productiedatabase naar een openbare GitHub-repository vastgelegd.

Evelyn werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team heeft alle inloggegevens onmiddellijk gerouleerd, de Git-geschiedenis opgeschoond met behulp van git-filter-repo en GitHub Secrets geïmplementeerd voor productie-implementaties.

**Resultaat:** Evelyn heeft de volledige beveiliging van de opslagplaats hersteld en de HIPAA-compliancescans doorstaan.

**Kosten en tijdlijn:** € 1.600 (Security Recovery Package) — klaar voor productie en geïmplementeerd binnen 4 werkdagen.

---
## Veelgestelde vragen

### Wat is een omgevingsvariabele?

Het is een veilige tijdelijke aanduiding voor gevoelige informatie buiten uw broncode. Uw code leest tijdens runtime de waarde uit de beveiligde omgeving van het hostingplatform.

### Waarom is het gevaarlijk om een ​​.env-bestand naar GitHub te committen?

Geautomatiseerde bots zoeken binnen enkele seconden naar sleutels in openbare opslagplaatsen om bronnen te stelen. Zelfs in privérepository's worden live sleutels zichtbaar voor iedereen met leestoegang.

### Wat is het verschil tussen de voorvoegsels VITE_ en NEXT_PUBLIC_?

Deze voorvoegsels stellen de variabele opzettelijk bloot aan de frontendbrowser. Ze mogen ALLEEN worden gebruikt voor openbare sleutels (zoals Stripe Publishable Key), nooit voor geheimen.

### Hoe beveilig ik een OpenAI API-sleutel als ik geen backend heb?

Gebruik een Edge-functie op Vercel of Supabase. De frontend roept uw ​​Edge-functie aan, de functie haalt de beveiligde sleutel op, roept OpenAI aan en retourneert het resultaat.