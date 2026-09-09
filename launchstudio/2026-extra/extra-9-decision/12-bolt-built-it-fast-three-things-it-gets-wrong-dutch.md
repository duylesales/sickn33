---
Titel: "Bolt Bouwde Het Snel: De Drie Zaken Die Het Vrijwel Nooit Goed Inricht"
Trefwoorden: Bolt.new productie, bolt ai app beveiliging, WebContainer beperkingen, omgevingsvariabelen blootgesteld, Supabase RLS Bolt, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Bolt Bouwde Het Snel: De Drie Zaken Die Het Vrijwel Nooit Goed Inricht

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Bouwde Het Snel: De Drie Zaken Die Het Vrijwel Nooit Goed Inricht",
  "description": "Bolt zet binnen een uur een werkende full-stack applicatie voor u neer, maar drie specifieke architectuurlagen gaan vrijwel altijd mis: het beheer van geheimen, server-side autorisatie en de persistentie van implementaties. Een technische analyse van de risico's en hoe u ze oplost.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/bolt-bouwde-het-snel-drie-dingen-die-het-vrijwel-nooit-goed-inricht"
  }
}
</script>

Iedereen prijst de ongeëvenaarde snelheid van Bolt. Bijna niemand praat echter over *waarom* het platform zo snel is. En dat is juist het meest waardevolle gesprek — want exact dezelfde architectuurbeslissingen die ervoor zorgen dat Bolt binnen veertig minuten een draaiende applicatie oplevert, zijn de reden dat drie specifieke lagen er stelselmatig onvolledig uitkomen. Elke keer weer.

Bolt draait uw project in een WebContainer: een Node-runtime gecompileerd naar WebAssembly, die direct binnen een tabblad van uw webbrowser wordt uitgevoerd. Er wordt geen virtuele machine (VM) opgetuigd, geen container binnengehaald en geen Postgres-daemon gestart. Dat is het kunststukje, en het is technisch gezien buitengewoon indrukwekkend. Het betekent echter ook dat Bolt's definitie van "uw app werkt" strikt begrensd is door wat binnen een browser-sandbox kan draaien. En de drie lagen die zich buiten die grens bevinden, zijn precies de factoren die bepalen of u uw software veilig commercieel kunt exploiteren. Dit is geen kritiek op de tool, maar een heldere afbakening van waar het werk van de tool ophoudt en het uwe begint.

## Punt één: uw geheimen zitten in de frontend-bundel

Begin hier, want dit is het snelst te controleren en statistisch gezien het meest waarschijnlijk.

Bolt genereert Vite- of Next.js-projecten en koppelt externe diensten door API-sleutels uit omgevingsvariabelen (environment variables) uit te lezen. In Vite moet elke variabele die bestemd is voor client-code worden voorzien van het voorvoegsel `VITE_`. In Next.js is dat `NEXT_PUBLIC_`. Deze voorvoegsels zijn geen vrijblijvende naamgevingsconventies; ze vormen een directe instructie aan de bundler: *voeg deze waarde direct toe aan het JavaScript-bestand dat naar de browser wordt verzonden (inlining)*. Bolt kiest hier standaard voor, simpelweg omdat er in een browser-gebonden WebContainer vaak geen andere plek is waar een geheime sleutel kan bestaan.

Voor een openbare Supabase `anon key` is dat de bedoeling en volkomen veilig; die sleutel is ontworpen om publiek te zijn, juist omdat Row Level Security (RLS) het echte beveiligingswerk hoort te doen (zie punt twee). Voor vrijwel elke andere sleutel betreft dit echter een acuut datalek. Dit zijn de geheimen die wij het vaakst open en bloot in client-bundels aantreffen, gerangschikt op frequentie:

- `VITE_SUPABASE_SERVICE_ROLE_KEY` — een sleutel die letterlijk elk RLS-beveiligingsbeleid in uw database omzeilt. De aanwezigheid hiervan in de frontend-bundel betekent dat uw volledige database kan worden uitgelezen en overschreven door iedereen die de browser-devtools opent.
- API-sleutels van OpenAI of Anthropic, zodat AI-functies direct "vanuit de frontend" kunnen worden aangeroepen. Anderen pikken deze sleutels binnen de kortste keren op om hun eigen taken op uw kosten te draaien; waarschuwingen over opgelopen creditcardkosten zijn meestal de manier waarop oprichters dit ontdekken.
- Stripe **geheime** sleutels (`sk_live_…`) in plaats van de publieke publishable keys.
- Inloggegevens van Resend, SendGrid of Twilio, waarmee kwaadwillenden uw account direct kunnen transformeren in een relaisstation voor spamcampagnes.
- Beheerders-webhooks en Slack-tokens die hardcoded in een helperbestandje zijn geplaatst in plaats van netjes in een omgevingsvariabele.

De controle kost u minder dan twee minuten. Bouw het project lokaal en doorzoek de distributiemap met grep:

```bash
npm run build
grep -rEo "(sk_live|sk_test|service_role|eyJ[A-Za-z0-9_-]{20,})" dist/ | sort -u
```

Elk resultaat dat hieruit naar voren komt, ligt op straat. Let op: het simpelweg roteren van de sleutel is slechts de helft van de oplossing. Als die sleutel ooit gecommit is, leeft deze voort in uw git-geschiedenis, in forks en in deployment-logs. Trek de sleutel in bij de provider en pas vervolgens de architectuur aan: leid alle externe API-aanroepen via een serverlaag — een Next route handler, een Supabase Edge Function of een compacte Hono/Express-service. Het ontwerppatroon is universeel: de browser communiceert met *uw* endpoint; uw endpoint beheert de vertrouwelijke inloggegevens en wikkelt de communicatie met de externe leverancier af.

## Punt twee: autorisatie is in werkelijkheid nooit geïmplementeerd

Bolt genereert probleemloos authenticatie. Registreren, inloggen, sessiebeheer en een afgeschermde route die niet-aangemelde bezoekers doorstuurt naar `/login`. Visueel ziet het er vlekkeloos uit, en voor puur inloggen klopt het meestal ook.

Autorisatie is echter de laag die bepaalt of *deze* specifiek ingelogde gebruiker het recht heeft om *deze* actie uit te voeren op *dít* record in de database. Die laag ontbreekt vrijwel altijd of is schijnveilig geïmplementeerd. We zien herhaaldelijk drie patronen terugkeren:

**Client-side route guards als enige beveiliging.** Een `<ProtectedRoute>` wrapper die controleert op `session?.user`, terwijl de daadwerkelijke data-ophaling daaronder volstrekt onbeschermd draait. De doorverwijzing is puur cosmetisch. De data-aanroep vormt de echte beveiligingsgrens, en die controleert in het geheel niet wie de aanvrager is.

**Supabase-tabellen met uitgeschakelde RLS of een permissieve beleidsregel.** Bolt genereert SQL-tabellen en schakelt RLS soms in met een regel als `USING (true)` — wat voldoet aan de eisen van de linter, maar in werkelijkheid nul bescherming biedt. Controleer dit altijd via psql of de Supabase SQL-editor in plaats van blind te varen op migratiebestanden:

```sql
select relname, relrowsecurity from pg_class
where relnamespace = 'public'::regnamespace and relkind = 'r';

select tablename, policyname, cmd, qual, with_check from pg_policies
where schemaname = 'public';
```

Lees de kolom `qual` zorgvuldig. `(auth.uid() = user_id)` is een legitiem beveiligingsbeleid. `true` is dat niet. Controleer tevens de kolom `with_check` afzonderlijk: een tabel kan uitstekend afgeschermd zijn voor `SELECT`, maar wagenwijd openstaan voor `INSERT`, waardoor gebruikers rijen kunnen aanmaken die niet van hen zijn.

**Eigenaarschap wordt nergens gecontroleerd in API-routes.** Waar Bolt wél backend-code genereert, ziet het patroon er doorgaans zo uit: `const { id } = params; return db.query('select * from invoices where id = $1', [id])`. De gebruiker is netjes ingelogd, maar niemand verifieert of de opgevraagde factuur daadwerkelijk toebehoort aan de aanvrager. Dit is een schoolvoorbeeld van IDOR (Insecure Direct Object Reference) en is kinderlijk eenvoudig uit te buiten door het ID in de URL op te hogen.

De structurele oplossing is om eenmalig vast te leggen waar autorisatie wordt afgedwongen — binnen RLS-policies of in een strikte serverlaag — en te zorgen dat alle dataverkeer daar consistent doorheen loopt. Hybride mengvormen zijn de plek waar datalekken ontstaan: de helft van de databaseaanroepen respecteert RLS, de andere helft gebruikt een service-role client die alle regels negeert, en na zes weken weet niemand meer welk endpoint wat doet.

## Punt drie: wat Bolt "geïmplementeerd" (deployed) noemt, is een preview, geen productieomgeving

De one-click Netlify deployment van Bolt is een echte uitrol. Maar het betreft tegelijkertijd één enkele omgeving zonder enige scheiding tussen wat u aan het testen bent en wat uw live gebruikers nodig hebben. En die scheiding vormt de kern van volwassen productiebeheer.

Concreet ontbreken de volgende onderdelen in een vers Bolt-project:

**Geschiedenis van databasemigraties.** In WebContainer draait geen lokale Postgres-instantie. Databasewijzigingen worden daardoor direct doorgevoerd op uw live Supabase-project — via het dashboard, een chat-prompt of een handmatig SQL-commando. Het resultaat is een databasestructuur die slechts op één plek bestaat: in productie. U kunt de database niet vanaf nul heropbouwen, geen representatieve testomgeving (staging) opzetten, geen wijzigingen beoordelen in een pull request en geen foute migratie terugdraaien. De overstap naar `supabase db diff` en een versiebeheerde map `supabase/migrations` kost een senior engineer slechts enkele uren, maar levert direct enorme stabiliteit op.

**Gescheiden omgevingen voor ontwikkeling en productie.** Eén enkel Supabase-project gebruiken voor zowel dev als prod betekent dat de eerste keer dat u de functionaliteit "verwijder account" uitprobeert, dit plaatsvindt op echte klantgegevens.

**Geautomatiseerde back-ups.** Op het gratis niveau van Supabase zijn er geen back-ups om op terug te vallen. Dagelijkse back-ups starten pas bij het Pro-abonnement; point-in-time recovery is een aanvullende optie. Bepaal welk niveau uw klantdata vereist vóórdat er een incident optreedt, niet erna.

**Monitoring van runtime-fouten.** Geen Sentry, geen gestructureerde logging, geen uptime-monitoring en geen alerts. Netlify meldt trots dat de build geslaagd is, terwijl niemand merkt dat een null-pointerfout het afrekenproces al elf uur lang blokkeert.

**Aannames rondom native dependencies.** WebContainer kan geen native Node-addons draaien, waardoor Bolt deze stelselmatig vermijdt. Code die prima functioneerde in de browser-sandbox kan zich op een echte Node-server heel anders gedragen — met name rond bestandstoegang, het gebruik van `crypto`, datastreaming en beeldverwerking. Test uw applicatie altijd op het werkelijke doelplatform vóórdat u een lanceringsdatum belooft.

**Rate limiting en bescherming tegen misbruik.** Geen snelheidsbeperkingen op registraties, op wachtwoordherstel of op endpoints die betaalde LLM-modellen aanroepen. De eerste bezoeker die een geautomatiseerd script loslaat op uw `/api/generate`-route maakt dit direct pijnlijk duidelijk via uw creditcardafschrift.

## Het webhook-probleem dat alle drie de lagen doorkruist

Betalingsverkeer verdient speciale aandacht, omdat het vrijwel altijd faalt door een combinatie van de drie bovenstaande tekortkomingen. Een door Bolt gegenereerde Stripe-koppeling maakt de Checkout Session doorgaans correct aan, maar kent de gebruiker vervolgens direct een abonnement toe op basis van de redirect naar de bedankpagina. Dat is geen betalingsbevestiging — het is louter een browser die een pagina bezoekt. Dit kan worden nagebootst, opgeslagen als bladwijzer of juist mislukken wanneer de internetverbinding tijdens de redirect hapert.

De enige betrouwbare server-side route is: `stripe.webhooks.constructEvent(rawBody, signature, endpointSecret)`. Twee cruciale details gaan in de praktijk steevast mis. Ten eerste vereist deze functie de **exacte, ruwe (raw)** request body: zodra een framework de JSON al heeft geparsed, treedt er een handtekeningfout op. Daarom vangen veel door AI geschreven handlers deze controle stilzwijgend op in een try/catch en gaan ze alsnog gewoon door. Inspecteer uw webhook-code en controleer of een mislukte verificatie daadwerkelijk een status 400 retourneert en de verwerking direct staakt. Ten tweede herhaalt Stripe mislukte webhooks automatisch, wat betekent dat handlers idempotent moeten zijn: sla het unieke Stripe Event ID op en negeer duplicaten. Anders zorgt een herhaalde webhook van `invoice.paid` ervoor dat gebruikers dubbele tegoeden toegekend krijgen.

Controleer tevens welke gebeurtenissen u daadwerkelijk verwerkt. Alleen luisteren naar `checkout.session.completed` volstaat niet voor een abonnementsmodel. Zonder afhandeling van `customer.subscription.updated`, `customer.subscription.deleted` en `invoice.payment_failed` behouden opgezegde of wanbetalende klanten onbeperkt toegang en loopt uw database definitief uit de pas met Stripe.

## Een audit van één uur die u vanavond zelf kunt uitvoeren

Voer deze stappen in volgorde uit; elke stap levert context voor de volgende:

1. Bouw de frontend-bundel en doorzoek deze met grep op geheime sleutels. Trek gelekte sleutels direct in bij de provider.
2. Voer een query uit op `pg_policies` en controleer elke `qual` en `with_check`. Noteer tabellen waar RLS volledig ontbreekt.
3. Kopieer een geldig sessietoken uit uw browser en doe met curl een verzoek naar een detail-endpoint met het record-ID van een andere gebruiker. Krijgt u gegevens terug? Dan heeft u te maken met een IDOR-kwetsbaarheid.
4. Open de Stripe-handler. Controleer handtekeningverificatie, de ruwe body, status 400 bij afwijzing, opslag van idempotency-keys en de lijst van afgehandelde event-types.
5. Typ `ls supabase/migrations`. Is de map leeg of ontbreekt deze? Dan is uw databasestructuur nergens vastgelegd.
6. Controleer of productie en ontwikkeling naar hetzelfde Supabase-project en dezelfde Stripe-modus wijzen.
7. Forceer bewust een serverfout en kijk of er ergens een foutmelding of alert afgaat.

Wees eerlijk in uw oordeel. Twee of minder bevindingen vallen binnen het normale profiel van een indie hacker — dat lost u zelf op in een weekend. Treft u vijf of meer gebreken aan, dan kijkt u aan tegen een week aan complexe infrastructuurwerkzaamheden waar u waarschijnlijk weinig affiniteit mee heeft, exact op het moment dat uw volledige focus bij uw klanten hoort te liggen.

Dat is de werkelijke beslissing waar dit artikel om draait: niet of Bolt de verkeerde keuze was — dat was het niet, want het heeft u een maand frontend-ontwikkeling bespaard — maar of het zelf oplossen van deze diepere lagen de beste besteding van uw komende twee weken is. [LaunchStudio](https://launchstudio.eu/nl/) is opgericht voor die tweede situatie: de frontend blijft exact zoals Bolt die heeft opgeleverd, de drie infrastructuurlagen worden vakkundig ingericht en de kosten bedragen een fractie van wat een traditioneel softwarebureau zou rekenen voor een complete herbouw. De engineers die dit uitvoeren maken deel uit van het [team van Manifera](https://www.manifera.com/services/custom-software-development/), dat al meer dan elf jaar dit soort enterprise-opdrachten uitvoert voor klanten die zich geen enkel datalek kunnen veroorloven.

Wilt u een second opinion van senior engineers die dagelijks AI-gegenereerde code auditen? Deel uw repository met ons en u ontvangt binnen één werkdag een heldere lijst met bevindingen, zonder verkooppraatjes.

## Echt voorbeeld

### De grep die € 340 aan API-tegoed kostte

Joost Brinkman, een indie hacker in Eindhoven, ontwikkelde met behulp van Bolt tijdens een lang weekend Draftpilot: een applicatie die met behulp van een LLM transcripties van vergaderingen omzet in gestructureerde projectbriefings. Hij introduceerde de tool in twee besloten Slack-communities en verwierf binnen vijf dagen 140 geregistreerde gebruikers. Dat voelde als een vliegende start — totdat het waarschuwingsbericht over buitensporig OpenAI-verbruik op zijn scherm verscheen.

De API-sleutel bleek rechtstreeks in de frontend-bundel te zitten. `VITE_OPENAI_API_KEY` was direct geïnlined in het client-JavaScript, omdat de aanroep naar het AI-model rechtstreeks vanuit de browser werd uitgevoerd. Een alerte bezoeker had de sleutel geëxtraheerd en ingezet voor eigen zware workloads. Onze technische audit bracht direct nog twee kwetsbaarheden aan het licht: RLS was weliswaar ingeschakeld op de tabel `transcripts`, maar met een betekenisloze `USING (true)`-regel, en het Stripe-upgradeproces kende betaalde abonnementen toe op basis van een URL-redirect zonder enige webhook-controle.

**Resultaat:** Alle aanroepen naar het taalmodel werden ondergebracht in een afgeschermde Supabase Edge Function met rate limiting per gebruiker, de RLS-policies werden herschreven op basis van `auth.uid()`, en een cryptografisch gevalideerde webhook-handler met idempotency-controle op event-ID nam het abonnementsbeheer over. Binnen vier werkdagen was alles gereed, zonder dat Joost's frontend ook maar één keer hoefde te worden aangepast.

> *"Ik kende het VITE_-voorvoegsel wel en had erover gelezen. Ik had alleen nooit de koppeling gelegd tussen 'dit wordt in de code opgenomen' en 'dit geeft directe toegang tot mijn creditcard'. Het grep-commando duurde elf seconden en ik voelde me de rest van de middag doodziek."*
> — **Joost Brinkman, Oprichter, Draftpilot (Eindhoven)**

**Kosten & Doorlooptijd:** € 1.850 (Launch Ready Pakket) — live binnen 4 werkdagen.

---

## Veelgestelde Vragen

### Vormt de Supabase anon key in mijn client-bundel een beveiligingsrisico?

Nee, deze sleutel is expliciet ontworpen om publiekelijk zichtbaar te zijn en de architectuur van Supabase houdt hier rekening mee. Het wordt echter wél een acuut beveiligingslek zodra Row Level Security (RLS) ontbreekt of te permissief is ingesteld, omdat de anon key dan fungeert als een onbeperkte databasesleutel. De sleutel waarover u zich wél ernstige zorgen moet maken is de `service_role key`; deze omzeilt alle beveiliging en mag onder geen beding de server verlaten.

### Waarom mislukt de verificatie van mijn Stripe-webhookhandtekening terwijl het geheim klopt?

Vrijwel altijd doordat de request body al is geparsed vóórdat de verificatie plaatsvindt. De functie `constructEvent` vereist exact de ruwe, ongewijzigde bytes die door Stripe zijn ondertekend. Zodra een JSON body-parser middleware de payload vooraf verwerkt, ontstaat er een handtekeningfout. Gebruik in Next.js route handlers `await req.text()` en configureer in Express specifiek `express.raw({ type: 'application/json' })` op die route.

### Vereist het migreren vanaf Bolt een volledige herbouw van mijn frontend?

Nee, en dat raden we ten zeerste af. Bolt exporteert standaard Vite- of Next.js-projecten met reguliere React-componenten. Zodra deze in een git-repository staan, is het gewoon een schone codebase die in elke IDE kan worden bewerkt. Het werk dat verricht moet worden bevindt zich uitsluitend in de server-, data- en deploymentlagen, en laat uw UI-componenten volledig ongemoeid.

### Hoe controleer ik of mijn applicatie kwetsbaar is voor IDOR zonder speciale beveiligingstools?

Maak twee verschillende testaccounts aan, noteer een record-ID dat toebehoort aan het tweede account, en vraag dat record op via een curl-commando terwijl u bent geauthenticeerd als het eerste account. Doe dit buiten de frontend om, aangezien uw eigen interface die aanroep niet zal genereren. Elk antwoord anders dan een HTTP 403 (Verboden) of 404 (Niet gevonden) duidt op een kwetsbaarheid. Herhaal dit voor elk endpoint dat een ID accepteert.

### Vormt het ontbreken van een lokale database in WebContainer een reëel productierisico?

Indirect wel. Het is de directe oorzaak dat databasewijzigingen ad-hoc worden doorgevoerd op een live Supabase-project in plaats van via versiebeheerde migratiebestanden. Hierdoor beschikt u niet over een controleerbare wijzigingshistorie, kunt u geen representatieve testomgeving inrichten en ontbreekt een geautomatiseerde rollback-procedure bij calamiteiten. Die omissie kost op jaarbasis vaak meer dan een individueel beveiligingsincident.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Vormt de Supabase anon key in mijn client-bundel een beveiligingsrisico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, deze sleutel is ontworpen om publiek te zijn. Het wordt pas gevaarlijk wanneer RLS ontbreekt of te permissief is, waardoor de anon key volledige databasetoegang krijgt. De service_role key mag daarentegen nooit de client bereiken."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom mislukt de verificatie van mijn Stripe-webhookhandtekening terwijl het geheim klopt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal doordat de request body al als JSON is geparsed vóór verificatie. constructEvent vereist de exacte ruwe bytes die Stripe heeft gesigneerd. Gebruik await req.text() in Next.js of express.raw in Express."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist het migreren vanaf Bolt een volledige herbouw van mijn frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Bolt levert standaard Vite- of Next.js-code met normale React-componenten op. Alle noodzakelijke aanpassingen vinden plaats in de backend-, database- en hostinglagen, zonder uw frontend te raken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of mijn applicatie kwetsbaar is voor IDOR zonder speciale beveiligingstools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maak twee accounts aan, noteer een record-ID van het tweede account en vraag dit via curl op met het sessietoken van het eerste account. Elk resultaat anders dan 403 of 404 duidt op een IDOR-beveiligingslek."
      }
    },
    {
      "@type": "Question",
      "name": "Vormt het ontbreken van een lokale database in WebContainer een reëel productierisico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Indirect wel. Wijzigingen worden daardoor ad-hoc op live databases doorgevoerd zonder versiebeheerde migratiebestanden, waardoor u geen reproduceerbare staging-omgeving of rollback-mogelijkheid heeft."
      }
    }
  ]
}
</script>
