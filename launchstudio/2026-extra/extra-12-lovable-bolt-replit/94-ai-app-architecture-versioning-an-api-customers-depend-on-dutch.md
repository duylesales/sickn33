---
Titel: "AI-app-architectuur: Versies Geven aan een API Waarvan Klanten Afhankelijk Zijn"
Trefwoorden: ai-app-architectuur, API-versiebeheer, brekende wijzigingen, OpenAPI, beleid voor uitfaseren, API-sleutels, webhooks, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS Scale-Up
---

# AI-app-architectuur: Versies Geven aan een API Waarvan Klanten Afhankelijk Zijn

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-app-architectuur: Versies Geven aan een API Waarvan Klanten Afhankelijk Zijn",
  "description": "Zodra een klant met uw product integreert, is uw databaseschema niet langer vrij aan te passen. Wat telt als brekende wijziging, hoe u versies beheert en uitfaseert, ontwerpkeuzes die een API makkelijk laten meegroeien, en de controles die voorkomen dat een refactor het bedrijf van een ander breekt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-architecture-versioning-an-api-customers-depend-on" }
}
</script>

Op een gegeven moment vraagt een klant of hij zijn eigen systeem aan uw product kan koppelen. Zijn ERP moet automatisch orders aanmaken, zijn planningstool moet uw roosters lezen, zijn datawarehouse moet elke nacht uw cijfers ophalen. U zegt ja, en vanaf die dag verandert er iets wat de meeste oprichters pas opmerken wanneer het breekt: een deel van uw product wordt nu gebruikt door software die u niet kunt zien, geschreven door mensen die u nooit hebt ontmoet, voor bedrijfsprocessen waarvan u niets weet.

Elke wijziging die u in dat deel maakt — een veld hernoemen, een notatie veranderen, een validatie aanscherpen — kan het bedrijf van een ander stilleggen. Niet met een foutmelding op uw scherm, maar met een stille mislukking in hun systeem die ze dagen later ontdekken.

In AI-gebouwde producten is het risico groter dan gebruikelijk, omdat de eerste "API" vaak helemaal niet is ontworpen: het is de database zelf, blootgesteld via de automatisch gegenereerde REST-interface van Supabase. Dit artikel behandelt waarom dat gevaarlijk is, hoe een bewuste API eruitziet, wat telt als brekende wijziging, hoe u versies beheert en uitfaseert, en de controles die voorkomen dat een refactor een klant breekt.

## De API bij Toeval

Supabase genereert een REST API voor elke tabel in uw database. Zo praat de frontend met de data, en het is verleidelijk een klant die wil integreren hetzelfde endpoint en een sleutel te geven: "Roep gewoon `/rest/v1/orders` aan."

Dat maakt van uw databaseschema een openbaar contract. Elke kolomnaam, elk type, elke tabel wordt iets waarvan de code van een klant afhangt. De dag dat u in een refactor `pickup_date` hernoemt naar `pickup_at` — misschien op voorstel van een AI-assistent, misschien om goede redenen — werkt elke integratie die `pickup_date` schreef niet meer.

Het is ook vaak een beveiligingsprobleem. Om de integratie werkend te krijgen, geven oprichters klanten ofwel de anon key — die alleen werkt als row level security voor elke tabel perfect is — of, erger, de service role key, die row level security volledig omzeilt en volledige toegang geeft tot de data van elke klant. De artikelen over geheimen in deze reeks beschrijven wat er dan volgt.

De oplossing is een bewuste API-laag: een aparte set endpoints, ontworpen voor integratie, die vertaalt tussen de buitenwereld en uw interne schema. Intern kunt u vrij hernoemen, herstructureren en refactoren. De API verandert alleen wanneer u besluit dat het moet, volgens een beleid waarop klanten kunnen vertrouwen.

## Wat Telt als Brekende Wijziging

De kerndiscipline van API-versiebeheer is weten welke wijzigingen veilig zijn en welke niet.

| Wijziging | Brekend? |
|---|---|
| Een nieuw endpoint toevoegen | Nee |
| Een optionele parameter toevoegen | Nee |
| Een veld aan een antwoord toevoegen | Nee, als clients onbekende velden negeren |
| Een nieuwe waarde aan een opsomming toevoegen | Vaak — clients kunnen er misschien niet mee overweg |
| Een veld verwijderen of hernoemen | Ja |
| Het type of de notatie van een veld veranderen (tekst naar getal, datumnotatie) | Ja |
| Een optionele parameter verplicht maken | Ja |
| Een standaardwaarde of de betekenis van een veld veranderen | Ja, ook als de vorm gelijk blijft |
| Foutcodes of statuscodes veranderen | Ja |
| Validatie aanscherpen (kortere maximale lengte, strengere notatie) | Ja, voor clients die op de oude limiet rekenden |
| Paginering of sorteervolgorde veranderen | Ja |

Twee punten verdienen nadruk. Wijzigingen in betekenis zijn brekend, ook als er zichtbaar niets verandert: als `amount` eerst inclusief btw was en nu exclusief, is elke integratie die het leest fout, en geen enkele schemacontrole merkt het op. En nieuwe waarden in een opsomming breken clients die op bekende waarden reageren — een nieuwe orderstatus `on_hold` stuurt de integratie van een klant naar zijn foutafhandeling. Documenteer opsommingen als open, en vertel klanten dat ze onbekende waarden netjes moeten afhandelen.

## Een Versieschema Kiezen

Drie schema's zijn gangbaar.

**Een versie in de URL** — `/v1/orders`, `/v2/orders`. Eenvoudig, zichtbaar, makkelijk te routeren en terug te zien in logs. De standaardkeuze voor de meeste producten.

**Een versie in een header** — `Accept: application/vnd.example.v2+json` of een eigen header. Houdt URL's stabiel, maar is onzichtbaar in een browser en makkelijk voor clients om te vergeten.

**Versies op datum** — elke API-sleutel wordt vastgezet op de versie die gold toen hij werd aangemaakt, en clients kiezen zelf voor nieuwere gedateerde versies. Elegant voor producten met frequente kleine wijzigingen en veel integratoren; aanzienlijk meer werk om te bouwen, omdat elk antwoord voor elke ondersteunde versie moet worden omgezet.

Voor een klein of middelgroot B2B-product is het praktische antwoord een hoofdversie in de URL gecombineerd met een sterke toezegging tot uitsluitend toevoegende wijzigingen. Binnen `/v1` maakt u alleen niet-brekende wijzigingen: nieuwe endpoints, nieuwe optionele parameters, nieuwe velden. Een `/v2` komt er alleen wanneer een brekende wijziging onvermijdelijk is, en dat moet zeldzaam zijn — eens in de paar jaar, niet eens in de paar maanden.

## Ontwerp Zo Dat U Zelden een Nieuwe Versie Nodig Hebt

De meeste brekende wijzigingen zijn het gevolg van vroege ontwerpkeuzes. Een handvol beslissingen aan het begin maakt een API makkelijk uit te breiden zonder te breken.

**Verpak antwoorden in een object.** Geef `{ "data": [...], "next_cursor": "..." }` terug in plaats van een losse array. Een losse array kan later geen paginering of metadata krijgen zonder elke client te breken.

**Gebruik vanaf het begin cursorpaginering**, zoals het pagineringsartikel in deze reeks beschrijft. Paginering met offset is traag op schaal en later overstappen is een brekende wijziging.

**Geef geld weer als gehele getallen in centen met een valuta** — `{ "amount": 125050, "currency": "EUR" }` — nooit als kommagetal of opgemaakte tekst. De weergave later veranderen is brekend; haar de eerste keer verkeerd doen is een bron van afrondingsfouten voor altijd.

**Gebruik ISO 8601-tijden in UTC** — `2028-03-19T09:30:00Z` — en datums als `2028-03-19`. Nooit lokale notaties, nooit op sommige plekken Unix-tijden en op andere tekst.

**Maak identificatoren tekst**, ook als ze intern UUID's of getallen zijn. Dat laat ruimte om hun vorm te veranderen.

**Geef consistente fouten met vaste codes terug** — `{ "error": { "code": "order_not_found", "message": "..." } }` — zodat clients op de code kunnen reageren terwijl u de melding verbetert.

**Accepteer idempotency keys bij verzoeken die iets aanmaken.** Een client die een `POST /orders` na een time-out opnieuw probeert, mag geen twee orders aanmaken. Een header `Idempotency-Key`, een dag opgeslagen met het resultaat, maakt nieuwe pogingen veilig — hetzelfde principe als in de artikelen over betaal- en boekhoudkoppelingen in deze reeks.

**Vertel clients dat ze tolerante lezers moeten zijn.** Documenteer dat er nieuwe velden en nieuwe waarden in opsommingen kunnen verschijnen, en dat clients moeten negeren wat ze niet begrijpen. Dat is wat het toevoegen van velden in de praktijk niet-brekend maakt.

## De Specificatie als Bron van Waarheid

Een API zonder geschreven specificatie is een API waarvan het contract alleen in de code bestaat — en in AI-gebouwde producten verandert de code op manieren die niemand regel voor regel reviewt.

Schrijf de API als OpenAPI-specificatie: elk endpoint, elke parameter, elk veld in een antwoord, elk type en elke foutcode. Genereer de referentiedocumentatie eruit, zodat de documentatie nooit verouderd is. Genereer er client-SDK's uit als klanten die willen. En gebruik haar in CI.

De waardevolste controle is een automatische vergelijking van de specificatie tussen de huidige versie en de voorgestelde wijziging. Tools als `oasdiff` delen elk verschil in als brekend of niet-brekend; een pull request die een brekende wijziging in `/v1` introduceert, laat de build falen.

```yaml
# CI-stap
- run: oasdiff breaking origin/main:openapi.yaml openapi.yaml --fail-on ERR
```

Voeg contracttests toe: verzoeken tegen de draaiende API die controleren dat antwoorden overeenkomen met de specificatie. Met de vergelijking van de specificatie en de contracttests samen kan een refactor die een interne kolom hernoemt niet stilletjes veranderen wat klanten ontvangen — de test faalt, en de developer voegt in plaats daarvan een vertaling toe in de API-laag.

Dit doet er dubbel toe wanneer AI-assistenten code schrijven. Een assistent die wordt gevraagd "het ordermodel op te schonen", hernoemt velden overal waar hij ze vindt; de controle van de specificatie is wat hem — en u — vertelt dat een van die plekken een belofte aan iemand anders is.

## Uitfaseren Zonder Drama

Soms is een brekende wijziging nodig. Het verschil tussen een goed beheerde API en een frustrerende zit in hoe die wijziging wordt ingevoerd.

**Kondig vroeg aan.** Voor een B2B-product is zes tot twaalf maanden tussen het aankondigen van het uitfaseren van een versie of veld en het verwijderen ervan redelijk. IT-afdelingen van klanten plannen in kwartalen.

**Geef het aan in de API zelf.** Geef `Deprecation`- en `Sunset`-headers terug op uitgefaseerde endpoints, met een link naar de migratiegids. Integratoren die hun logs bewaken, zien het zonder uw nieuwsbrief te lezen.

**Weet wie er last van heeft.** Log API-gebruik per sleutel en per versie. Voordat u iets verwijdert, moet u elke organisatie kunnen opnoemen die het de afgelopen dertig dagen aanriep — en die rechtstreeks benaderen, niet alleen via een changelog die niemand leest.

**Schrijf een migratiegids.** Wat er veranderde, waarom, en precies wat een client moet doen, met voorbeelden van oude en nieuwe verzoeken.

**Draai beide versies naast elkaar** tijdens de periode van uitfaseren. Meestal wordt `/v1` geïmplementeerd als dunne compatibiliteitslaag bovenop `/v2`, die oude veldnamen en notaties vertaalt, zodat u één implementatie en één vertaling onderhoudt in plaats van twee codebases.

**Verwijder op de aangekondigde datum** — nadat u het gebruikslog nog één keer hebt gecontroleerd. Deadlines eindeloos verlengen leert klanten dat aankondigingen van uitfaseren er niet toe doen.

## Webhooks Zijn Ook een API

Veel producten sturen gebeurtenissen naar klanten — "order aangemaakt", "factuur betaald" — via webhooks. Alles hierboven geldt ook voor hen, en ze worden vaak vergeten.

Geef de payload een versie, bij voorkeur met een versieveld in elke gebeurtenis en de mogelijkheid voor een klant om per endpoint de versie te kiezen. Onderteken elke levering zodat klanten kunnen controleren dat ze van u komt, met hetzelfde patroon dat het artikel over webhookbeveiliging in deze reeks beschrijft voor inkomende webhooks. Probeer het opnieuw met oplopende wachttijd wanneer het endpoint van de klant faalt, leg elke leverpoging vast, en toon klanten een leverlog met de mogelijkheid om opnieuw te versturen. En zet nooit meer persoonsgegevens in een webhook dan de klant nodig heeft — een referentie waarmee hij details via de geauthenticeerde API kan ophalen, is vaak beter dan het volledige record.

## Sleutels, Scopes en Limieten

Een API die door klanten wordt gebruikt, heeft toegangsbeheer nodig dat is ontworpen voor software in plaats van voor mensen.

**API-sleutels per organisatie**, aangemaakt en ingetrokken door de beheerder van de klant in het product, één keer getoond bij het aanmaken en opgeslagen als hash — daarna nooit meer op te vragen.

**Scopes per sleutel**, gekoppeld aan het rechtenmodel dat het artikel over rollen en rechten in deze reeks beschrijft: een sleutel voor een rapportagetool heeft `orders.read` nodig, niet de mogelijkheid om klanten te verwijderen.

**Limieten per sleutel**, teruggegeven in de headers van antwoorden zodat nette clients hun tempo kunnen aanpassen, met `429`-antwoorden en een header `Retry-After` wanneer ze worden overschreden.

**Gebruik zichtbaar voor de klant** — verzoeken per dag, fouten, laatst gebruikt — zodat hij kan zien welke integraties actief zijn en een sleutel kan opmerken die er niet hoort te zijn.

En nooit, onder geen enkele omstandigheid, de service role key. Dat is geen API-sleutel; het is de hoofdsleutel van uw database.

## Geef Integratoren een Plek om te Testen

De developers van klanten hebben een plek nodig om hun integratie te bouwen die niet hun productieaccount is. Zonder die plek testen ze tegen live data — testorders aanmaken die echte transportbedrijven inplannen, testfacturen sturen naar echte debiteuren — of vragen ze u om achter hen op te ruimen.

Drie opzetten, van eenvoudigst tot meest volledig.

**Sleutels in testmodus.** Elke organisatie kan sleutels aanmaken die als test zijn gemarkeerd. Verzoeken met een testsleutel werken op een aparte, duidelijk gemarkeerde set data binnen dezelfde organisatie, veroorzaken nooit uitgaande effecten zoals e-mails, betalingen of boekingen in boekhoudpakketten, en worden uitgesloten van facturatie en rapportages. Dit is het model dat betaalproviders gebruiken, en integratoren herkennen het.

**Een sandboxorganisatie.** Een aparte organisatie per klant, gevuld met realistische voorbeelddata zoals het artikel over seeddata in deze reeks beschrijft, met eigen sleutels. Eenvoudiger te bouwen dan een testmodus, en voor de meeste B2B-producten toereikend.

**Een openbare sandboxomgeving.** Een aparte deployment waartegen iedereen kan testen, elke nacht teruggezet. De moeite waard zodra veel derden — niet alleen klanten — integraties bouwen.

Wat u ook kiest, documenteer de verschillen expliciet: welke bijeffecten worden onderdrukt, hoe testdata wordt teruggezet, en welke limieten gelden. En maak de grens in de code absoluut: een testsleutel mag nooit productiedata kunnen lezen of schrijven, en dat is een eigenschap om in CI even zorgvuldig te testen als de scheiding tussen organisaties.

De opbrengst is minder supportverzoeken tijdens integratieprojecten, en integraties die al werkend in productie aankomen — wat voor de IT-afdeling van de klant het verschil is tussen een product waarmee makkelijk te integreren is en een waarmee dat niet zo is.

## Een Changelog Die Klanten Kunnen Lezen

Integratoren willen weten wat er veranderde zonder code te lezen. Houd een gedateerde changelog bij van elke API-wijziging — toevoegingen net zo goed als uitfaseringen — gelinkt vanuit de documentatie en, bij belangrijke wijzigingen, gemaild aan de technische contactpersonen van de betrokken organisaties. Toevoegingen doen er ook toe: een klant die op een nieuw veld wacht, hoort uit de changelog dat het er is, niet uit een supportticket.

## Dit Inrichten

Voor een Lovable- of Supabase-product dat een API voor klanten opent, is dit doorgaans vier tot zes dagen: een bewuste API-laag los van de automatisch gegenereerde database-interface, een OpenAPI-specificatie als bron van waarheid met gegenereerde documentatie, een hoofdversie in de URL met een toezegging tot uitsluitend toevoegende wijzigingen, envelopes, cursorpaginering, geld in centen, UTC-tijden, identificatoren als tekst en vaste foutcodes, idempotency keys bij verzoeken die iets aanmaken, vergelijking van de specificatie en contracttests in CI om brekende wijzigingen tegen te houden, afgebakende en gehashte API-sleutels per organisatie met limieten en zichtbaar gebruik, testsleutels of sandboxorganisaties voor integratoren, gebruikslogging per sleutel en versie, een geschreven beleid voor uitfaseren met headers, migratiegidsen en directe berichtgeving, ondertekende webhooks met versies en een leverlog, en een openbare changelog.

LaunchStudio bouwt dit wanneer de eerste integratieklant van een product er op het punt staat afhankelijk van te worden. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons of uw klanten rechtstreeks uw database aanroepen](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Een Hernoemde Kolom en Elfhonderd Ontbrekende Orders

Ruud Schipper bouwde Transportplanner in Lovable: beheer van transportorders voor regionale transportbedrijven, gebruikt door 26 transportbedrijven, van wie verschillende grootste verladers orders automatisch vanuit hun eigen systemen verstuurden.

Er was geen API-laag. De systemen van verladers riepen de REST-endpoints van Supabase rechtstreeks aan, en om het snel werkend te krijgen had elke verlader de service role key gekregen. Tijdens een refactor hernoemde een AI-assistent `pickup_date` naar `pickup_at` en `weight` naar `weight_kg` in de hele codebase, inclusief de database. De frontend werkte; de systemen van de verladers niet.

Verzoeken van negen verladers faalden met fouten die hun systemen logden maar die niemand bekeek. Twee dagen lang werden zo'n 1.100 transportorders die hadden moeten worden ingepland nooit aangemaakt. Transportbedrijven ontdekten het toen verladers belden om te vragen waarom de vrachtwagens niet waren gekomen. Bij de review die volgde, bleken de service role keys elke verlader volledige lees- en schrijftoegang te geven tot de data van elk transportbedrijf.

Vijf werkdagen: de service role key direct geroteerd en elke verlader een afgebakende, gehashte API-sleutel gegeven die bij de organisatie van zijn transportbedrijf hoort; een eigen `/v1`-API gebouwd als edge functions met een OpenAPI-specificatie, gegenereerde documentatie, envelopes, cursorpaginering, UTC-tijden en vaste foutcodes; idempotency keys bij het aanmaken van orders, zodat nieuwe pogingen geen orders konden dupliceren; een compatibiliteitslaag die zes maanden de oude veldnamen accepteert, met `Deprecation`- en `Sunset`-headers en een migratiegids; gebruikslogging per sleutel, zodat elke verlader die nog oude velden gebruikte rechtstreeks kon worden benaderd; vergelijking van de specificatie en contracttests in CI die falen bij elke brekende wijziging; ondertekende webhooks met versies voor updates van de orderstatus, met een leverlog; en een changelog.

**Resultaat:** de 1.100 orders werden binnen een dag opnieuw aangemaakt uit de logs van de verladers, en er werd geen toegang tot data van andere transportbedrijven gevonden. In het jaar daarna ging de API door veertien releases zonder één brekend incident; de controle in CI hield drie pull requests tegen die haar zouden hebben gebroken. Twee grote verladers koppelden via de gedocumenteerde API in elk ongeveer een week, zonder Ruud te bellen.

> *"De assistent hernoemde twee kolommen omdat de nieuwe namen duidelijker waren. Dat waren ze — en de systemen van negen verladers maakten geen orders meer aan, en niemand merkte het twee dagen lang."*
> — **Ruud Schipper, Oprichter, Transportplanner (Tiel)**

**Kosten & Doorlooptijd:** €6.200 (rotatie van de service key en afgebakende API-sleutels, API-laag met versies en OpenAPI-specificatie, idempotent aanmaken van orders, compatibiliteitslaag van zes maanden met headers voor uitfaseren, gebruikslogging per sleutel, vergelijking van de specificatie en contracttests, ondertekende webhooks met versies, changelog) — afgerond in 5 werkdagen.

## Veelgestelde vragen

### Kunnen klanten integreren via de automatisch gegenereerde REST API van Supabase?

Dat kan, maar het maakt uw databaseschema een openbaar contract en betekent meestal dat u krachtige sleutels uitdeelt. Bouw een aparte API-laag die naar uw schema vertaalt, zodat interne wijzigingen klanten niet breken.

### Wat telt als brekende API-wijziging?

Velden verwijderen of hernoemen, types of notaties veranderen, parameters verplicht maken, standaardwaarden of betekenis veranderen, foutcodes veranderen, validatie aanscherpen en paginering veranderen. Endpoints, optionele parameters en velden toevoegen is niet brekend.

### Hoort de versie in de URL of in een header?

Voor de meeste B2B-producten een hoofdversie in de URL — `/v1` — gecombineerd met een toezegging om binnen een versie alleen toe te voegen. Versies op datum passen bij producten met veel integratoren en frequente wijzigingen.

### Hoe lang moet een periode van uitfaseren zijn?

Zes tot twaalf maanden voor B2B-klanten, met headers voor uitfaseren, een migratiegids, gebruikslogs om betrokken klanten te vinden, en directe berichtgeving vóór het verwijderen.

### Hoe voorkom ik dat een refactor de API breekt?

Houd een OpenAPI-specificatie als bron van waarheid en draai een vergelijking van de specificatie en contracttests in CI, zodat elke brekende wijziging de build laat falen voordat ze wordt gedeployd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moeten klanten integreren via de gegenereerde REST API van Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het maakt het databaseschema een openbaar contract en stelt vaak krachtige sleutels bloot; bouw in plaats daarvan een aparte API-laag."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een brekende API-wijziging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Velden verwijderen of hernoemen, of types, notaties, standaardwaarden, betekenis, foutcodes, validatie of paginering veranderen. Toevoegingen zijn niet brekend."
      }
    },
    {
      "@type": "Question",
      "name": "Waar moet een API-versie worden opgegeven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal als hoofdversie in de URL, met binnen een versie alleen toevoegende wijzigingen; versies op datum passen bij grote groepen integratoren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moet het uitfaseren van een API duren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zes tot twaalf maanden voor B2B, met Deprecation- en Sunset-headers, een migratiegids en directe berichtgeving aan betrokken klanten."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomt CI brekende API-wijzigingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vergelijk de OpenAPI-specificatie met main en draai contracttests, waarbij de build faalt bij elk brekend verschil."
      }
    }
  ]
}
</script>
