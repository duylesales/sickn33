---
Titel: "Logging: Wat U Moet Vastleggen, en Wat U Nooit Mag Opschrijven"
Trefwoorden: gestructureerd loggen best practices, nooit wachtwoorden loggen, PII in logbestanden, bewaartermijn logs beleid, gevoelige data logging compliance, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Logging: Wat U Moet Vastleggen, en Wat U Nooit Mag Opschrijven

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Logging: Wat U Moet Vastleggen, en Wat U Nooit Mag Opschrijven",
  "description": "Een praktische checklist voor software-oprichters over wat een productielogregel wél moet bevatten, hoe lang u logs bewaart, en de specifieke categorieën data — tokens, wachtwoorden, creditcards en persoonsgegevens — die nooit in een logbestand mogen belanden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-25",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/logging-what-to-record-and-what-you-must-never-write-down" }
}
</script>

*"Wacht eens even... staat mijn eigen wachtwoord nu serieus in een logbestand?"* Dit is een vraag die oprichters doorgaans exact één keer stellen. Meestal wanneer ze tijdens het doorzoeken van productielogs naar een vage bug plotseling een bekende tekenreeks zien opduiken: het wachtwoord dat ze vorige week zelf intypten tijdens het testen van het inlogformulier. Dit is geen hypothetisch bangmakerijtje. Een regel zoals `console.log(req.body)` — of het equivalent daarvan in Python, Go of PHP — is een van de meest voorkomende debug-patronen in door AI geschreven code. Het wordt tijdens de ontwikkeling snel toegevoegd om te zien waarom een endpoint vreemd reageert, en blijft vervolgens gedachteloos in de code staan omdat het werkte en niemand eraan dacht het vóór de lancering te verwijderen.

Het resultaat: de applicatie logt letterlijk alles wat er via het verzoek binnenkomt. Bij een inlog-endpoint is dat een wachtwoord in platte tekst; bij een afrekenpagina kan dat een creditcardnummer zijn. Logbestanden blijven aanzienlijk langer bewaard dan oprichters beseffen, worden gekopieerd naar externe monitoringtools (zoals Datadog, Better Stack of Axiom), en zijn inzichtelijk voor meer medewerkers dan vrijwel elk ander onderdeel van uw infrastructuur.

## De Twee Vragen Die Elke Logregel Moet Beantwoorden (en de Ene Die Verboden Is)

Een waardevolle logregel in een productieomgeving beantwoordt bij een storing twee essentiële vragen: **wat gebeurde er**, en **wat is de context om het probleem direct te reproduceren** zónder dat u de gedupeerde klant hoeft te vragen naar details die hij zich toch niet herinnert.

Een logmelding zoals `"Betaling mislukt"` is over drie weken volstrekt waardeloos. Een logregel zoals:
`"Betaling mislukt: order_id=8842, user_id=1193, reden=card_declined, provider=stripe"`
is direct bruikbaar. U ziet onmiddellijk om welke bestelling het gaat, welk account erbij hoort, wat de exacte weigeringsreden was en welk betalingssysteem dit rapporteerde. U springt binnen tien seconden direct naar de juiste transactie in het Stripe-dashboard in plaats van in het duister te tasten.

De vraag die een logregel daarentegen **nooit** mag beantwoorden is: *"Wat heeft deze gebruiker exact in dit invoerveld getypt?"* wanneer dat veld een geheim kan bevatten. Dit is een absolute wet, geen subjectieve afweging per veld: als de inhoud van een veld een wachtwoord, een sessietoken, een API-sleutel, een creditcardnummer of een burgerservicenummer bevat, mag die waarde onder geen enkele voorwaarde in een logregel verschijnen. Hoe handig het op dat moment ook lijkt voor het debuggen: de waarde van het oplossen van een bug weegt nooit op tegen het acute beveiligingslek dat ontstaat.

## De "Nooit Loggen"-Lijst: Vier Absolute Taboes

Wanneer een ontwikkelaar of AI-tool tijdens het bouwen snel een bug wil opsporen, is de meest voor de hand liggende code `console.log(req.body)` of `logger.info(event)`. In een lokale testomgeving is dat handig; in productie dumpt het ongemerkt de meest gevoelige bedrijfs- en klantgeheimen rechtstreeks in platte tekstbestanden of externe dashboards. 

Vier categorieën mogen onder geen enkel beding in uw logs terechtkomen:

1. **Wachtwoorden en authenticatie-tokens:**
   Elk wachtwoordveld — zowel in platte tekst als zelfs gehasht — hoort nooit in logs thuis. Het loggen van ruwe wachtwoorden (bijvoorbeeld wanneer een gebruiker een nieuw account aanmaakt of inlogt) verandert uw logfiles in een directe bron voor credential stuffing. Hetzelfde geldt voor `Authorization`-headers met Bearer tokens, sessiecookies en API-sleutels van derden. Eén gelekt logbestand geeft een kwaadwillende direct toegang tot uw hele infrastructuur.

2. **Betaalkaartgegevens en CVC-codes:**
   Het loggen van volledige creditcardnummers (PAN), vervaldatums of de 3-cijferige CVC/CVV-beveiligingscode is een zware, directe overtreding van de **PCI-DSS normering**. Als uw betalingsverwerker ontdekt dat u CVC-codes opslaat in applicatielogs, riskeert u onmiddellijke royering van uw betaalaccount en torenhoge boetes. Zelfs een 'onschuldige' `console.log(stripePayload)` kan dit lek al veroorzaken.

3. **Gezondheidsdata en intieme medische notities:**
   Onder Artikel 9 van de AVG (en vergelijkbare zorgwetgeving zoals HIPAA) kwalificeren gezondheidsgegevens als bijzondere persoonsgegevens. Wanneer een gebruiker een medische klacht, allergie of blessure invoert en uw server dumpt het complete request-object in de logs, overtreedt u het principe van dataminimalisatie en creëert u een ongecontroleerde gegevensstroom die vaak niet meegenomen wordt in reguliere verwijderingsverzoeken.

4. **Volledige persoonsrecords in één enkele logregel:**
   Een compleet gebruikersprofiel met naam, adres, telefoonnummer, burgerservicenummer en geboortedatum in één JSON-blob loggen omdat *"log het hele user-object"* de snelste manier van debuggen was. Afzonderlijk naar een ID refereren (`user_id: 1193`) is uitstekend; het complete profiel meervoudig in logs wegschrijven maakt van elk logbestand een gigantisch datalek zodra een medewerker, stagiair of externe logdienst gecompromitteerd raakt.
## Gestructureerd Loggen (Structured Logging): Waarom Vrije Tekst Niet Schaalt

Het overgrote deel van de door AI gegenereerde logging is volstrekt ongestructureerd: een willekeurige tekstreeks, samengevoegd met wat variabelen, die naar de standard output wordt weggeschreven — zoals `console.log('Gebruiker ' + userId + ' inloggen mislukt')`. Voor een individuele programmeur die door een handvol regels scrolt is dat prima leesbaar. Het wordt echter nagenoeg volstrekt waardeloos zodra uw applicatie meer dan een triviale hoeveelheid productie-verkeer verwerkt. Er bestaat immers geen betrouwbare manier om vrije tekst over tienduizenden logregels efficiënt te doorzoeken, filteren of aggregeren zonder kwetsbare regex-patronen.

**Gestructureerd loggen (structured logging)** schrijft elke logregel daarentegen weg als een consistent, uniform object — standaard in JSON-formaat — met expliciet benoemde velden:
```json
{
  "level": "error",
  "event": "login_failed",
  "user_id": 1193,
  "reason": "invalid_password",
  "ip_hash": "a8f3...",
  "timestamp": "2026-09-09T10:15:30Z"
}
```

Het enorme praktische voordeel bewijst zich op het moment dat u onder zware tijdsdruk een acuut incident moet onderzoeken: *"Hoeveel mislukte inlogpogingen vonden er voor dit specifieke account plaats in het afgelopen uur?"* is een haarscherpe, razendsnelle query over gestructureerde velden, terwijl het bij vrije tekst een frustrerende, foutgevoelige scrol- en gokoefening wordt. Elk serieus loganalyseplatform (zoals Datadog, Better Stack, Axiom of AWS CloudWatch) is fundamenteel gebouwd rondom gestructureerde velden. Het invoeren van dit formaat kost vrijwel niets als u het vroegtijdig inricht — het is puur de configuratie van een logging-library (zoals Pino of Winston) — maar het is een monsterlijke operatie als u pas begint wanneer er al honderdduizenden ongestructureerde regels in productie rondzwerven.

Deze discipline ondersteunt tevens rechtstreeks het voorkomen van geheime datalekken: een gestructureerde logger met een vooraf gedefinieerd schema dwingt de ontwikkelaar om expliciet te kiezen welke velden worden meegestuurd, in schril contrast met `console.log(req.body)` waarbij standaard alles, inclusief wachtwoorden en tokens, blindelings wordt weggeschreven.
## Bewaartermijnen (Retention): Wat Is Nodig en Wat Is een Risico?

De bewaartermijn van serverlogs is een beleidskeuze die in de meeste prototypes nooit bewust wordt gemaakt — logs hopen zich simpelweg eindeloos op volgens de standaardinstellingen van het gekozen platform. Dat kan variëren van slechts enkele dagen op een gratis hostingtier tot oneindig lang wanneer logs worden doorgestuurd naar goedkope, onbeheerde cloudopslag waar niemand ooit naar omkijkt.

Een te korte bewaartermijn brengt directe operationele schade met zich mee: als een betalende klant een storing meldt die vier dagen geleden plaatsvond en uw logs bewaren slechts data van de afgelopen 48 uur, bent u blind en kunt u de oorzaak nooit meer achterhalen. Een te lange bewaartermijn brengt echter een volkomen ander, juridisch risico met zich mee: elke dag dat een logregel in opslag blijft staan, vormt het een potentieel doelwit bij een inbraak op uw systemen of uw externe logprovider. Bovendien dicteert de AVG dat persoonsgegevens — inclusief persoonsgegevens die onbedoeld in logs belanden, zoals een e-mailadres in een foutmelding — niet langer bewaard mogen worden dan strikt noodzakelijk is voor het doel waarvoor ze zijn verzameld. *"We hebben nooit een retentiebeleid ingesteld dus alles staat er al twee jaar"* houdt bij geen enkele privacytoezichthouder stand.

Een gezonde, beproefde standaard voor vroege SaaS-producten is een **retentie van 30 tot maximaal 90 dagen** voor direct doorzoekbare operationele logs. Alles wat ouder is dan die termijn, dient automatisch en onherroepelijk gewist te worden, tenzij er een wettelijke of fiscale bewaarplicht geldt voor specifieke financiële audit-records die veilig naar afgesloten koude archiefopslag worden verplaatst.
## Foutmeldingen voor Gebruikers versus Wat U Achter de Schermen Logt

Een veelvoorkomende ontwerpfout bij door AI gegenereerde software is het verwarren van wat een eindgebruiker te zien krijgt en wat er intern over een fout wordt geregistreerd. AI-foutafhandeling kiest stelselmatig een van twee verkeerde uitersten:
- Het toont de bezoeker een rauwe stacktrace of een interne databasefout (zoals *"Postgres error: relation 'users' violates foreign key constraint"*). Dit lekt cruciale interne architectuurdetails, tabelnamen en queryfragmenten direct aan potentiële aanvallers.
- Of het toont een generiek *"Er is iets misgegaan"* zónder dat er achter de schermen enige technische context wordt gelogd, waardoor u met de handen in het haar zit wanneer de gebruiker gefrustreerd contact opneemt.

De professionele scheiding is glashelder:
- **De gebruiker ziet een vriendelijke, generieke melding:** *"We konden uw betaling op dit moment niet verwerken. Probeer het opnieuw of neem contact op met ondersteuning."*
- **Gekoppeld aan een uniek referentie-ID:** Voeg aan de foutmelding op het scherm een korte unieke code toe (bijvoorbeeld: `Foutcode: ERR-94B2`).
- **De backend logt de volledige technische realiteit:** De complete exception, stacktrace, queryparameters en sessie-ID worden weggeschreven naar de gestructureerde logs onder exact diezelfde referentiecode `ERR-94B2`.

Wanneer een klant vervolgens bij uw helpdesk meldt dat hij tegen foutcode `ERR-94B2` aanliep, zoekt uw engineer binnen drie seconden in de logs en ziet hij exact wat er misging, zónder dat er ooit gevoelige serverdetails naar de browser zijn gelekt.
## De Pre-Launch Logging-Audit in Één Uur

U kunt uw complete codebase in minder dan zestig minuten auditen door de volgende stappen te doorlopen:

1. **Gevoelige invoervelden opsporen:** Doorzoek de hele broncode op `console.log`, `print` of equivalente log-aanroepen die hele request- of response-objecten wegschrijven. Controleer elk aangetroffen punt rigoureus tegen de hiervoor genoemde taboelijst: wachtwoorden, sessietokens, Authorization-headers en creditcardgegevens.
2. **Formaat standaardiseren:** Zorg dat alle applicatielogs worden gegenereerd als valide JSON met consistente sleutelvelden (level, event, timestamp, context), in plaats van willekeurige aaneengeregen tekstregels.
3. **Bewaartermijn instellen:** Controleer de feitelijke retentie-instellingen bij uw hostingprovider of logging-dienst en configureer een harde limiet van 30 tot 90 dagen.
4. **Foutschermen sanitizen:** Verifieer dat foutmeldingen in de frontend nooit rauwe stacktraces of databasefouten tonen, maar communiceren via geanonimiseerde foutcodes gekoppeld aan de interne logs.
5. **Stresstest op het betalingstraject:** Voer in een sandbox-omgeving een mislukte creditcardtransactie uit en inspecteer letterlijk elke logregel die rondom die poging wordt geproduceerd. Bevatten de logs volledige kaartnummers of CVC-codes? Herstel dit onmiddellijk vóórdat u echte betalingen accepteert.
## Dit Goed Inrichten Zónder een Complete Herschrijving

Het professioneel inrichten van uw log-architectuur is vrijwel altijd een gerichte, afgebakende verbetering. Het behelst het nalopen van bestaande log-statements, het verwijderen of maskeren van gevoelige parameters, het standaardiseren op een gestructureerde JSON-logger en het instellen van een gezonde bewaartermijn. Het vereist geen ingrijpende verbouwing van de kernfunctionaliteiten van uw product. Het valt daardoor comfortabel binnen de vaste scope van het **Launch Ready** traject van LaunchStudio.

Het is tevens een van de constateringen die de [engineers van Manifera](https://www.manifera.com/services/custom-software-development/) stelselmatig als eerste naar boven halen tijdens een audit van AI-code. Het patroon dat dit veroorzaakt — het gemakzuchtig loggen van het complete request-object tijdens het prototypen — is immers nagenoeg universeel aanwezig, en wordt vrijwel altijd vergeten vóór de lancering. Weet u niet exact wat uw applicatie op dit moment wegschrijft naar productielogs? [Beschrijf uw project en ontvang binnen één werkdag een heldere analyse](https://launchstudio.eu/nl/#contact) van wat een logging-audit bij uw applicatie aan het licht zou brengen.
## Echt voorbeeld

### Een Solo-Oprichter Vindt Zijn Eigen Wachtwoord Terug in Zijn Logbestanden

Jakub Wróbel bouwde Notarize, een digitale handtekeningentool voor zzp'ers en freelancers, met behulp van Cursor. Tijdens het ontwikkelen had hij bij het inlog-endpoint een tijdelijke debug-regel geplaatst: `console.log('Login attempt:', req.body)`. De inlogbug werd opgelost, maar de logregel bleef onaangeroerd in productie actief.

Toen een potentiële zakelijke klant vroeg om een security-vragenlijst in te vullen ter voorbereiding op een enterprise-pilot, doorzocht Jakub uit nieuwsgierigheid zijn productielogs op zijn eigen e-mailadres. Tot zijn grote schrik trof hij zijn eigen wachtwoord aan — in volstrekt leesbare platte tekst, vastgelegd tijdens een inlogpoging van weken geleden. Elke inlogpoging van elke gebruiker sinds de livegang was doodleuk doorgestuurd naar een externe cloud-loggingdienst.

Tijdens het Launch Ready-traject saneerden we direct alle loghandlers: de debug-regel werd vervangen door een gestructureerd JSON-event met uitsluitend het `user_id`, tijdstempel en een boolean voor succes of falen. Er werd een linting-regel ingesteld die het direct loggen van `req.body` structureel blokkeert. Uit voorzorg werden de wachtwoorden van alle bestaande gebruikers preventief gereset onder een professionele beveiligingscommunicatie.

**Resultaat:** De security-vragenlijst van de enterprise-klant kon met vlag en wimpel en met aantoonbare audittrails worden beantwoord, waardoor het pilotcontract ter waarde van tienduizenden euro's werd binnengehaald.

> *"Ik vond mijn eigen wachtwoord terug in een logbestand waarvan ik vergeten was dat het bestond. Dat was het moment waarop 'ik ruim die debug-logs later wel op' direct veranderde in een absolute noodzaak."*
> — **Jakub Wróbel, Oprichter, Notarize (Wrocław)**

**Kosten & Doorlooptijd:** Launch Ready-pakket, logging-audit en beveiligingsrevisie — opgeleverd in 3 werkdagen.

## Veelgestelde Vragen

### Hoe controleer ik mijn bestaande logs op per ongeluk vastgelegde geheimen?
Gebruik de zoekbalk van uw logbeheertool en zoek hoofdletterongevoelig op termen zoals `"password"`, `"token"`, `"authorization"`, `"bearer"` en `"card"`. Deze full-text zoekopdracht toont u direct of er in het recente verleden gevoelige variabelen zijn gelogd.

### Is het voldoende om gevoelige velden af te dekken met sterretjes (masking)?
Masking helpt, maar brengt risico's met zich mee: als de masking pas plaatsvindt nadat de ruwe string al is geformatteerd, of als een veld over het hoofd wordt gezien, lekt het geheim alsnog. Het is structureel veiliger om aan de bron expliciet te definiëren wélke velden gelogd mogen worden, in plaats van alles te loggen en achteraf te filteren.

### Lopen tools voor foutopsporing zoals Sentry hetzelfde risico?
Ja. Sentry en vergelijkbare platforms leggen standaard de context van het HTTP-verzoek vast, inclusief headers en request bodies. U dient in de Sentry-configuratie expliciet databeschermingsregels (*data scrubbing*) te activeren om wachtwoorden en tokens vóór verzending te strippen.

### Hoe lang mag ik logs bewaren volgens de AVG (GDPR)?
De AVG stelt geen vast aantal dagen vast, maar vereist dat data niet langer wordt bewaard dan noodzakelijk voor het specifieke doel. Voor operationele foutopsporing en beveiligingsmonitoring geldt 30 tot 90 dagen als een breed geaccepteerde en verdedigbare bewaartermijn.

### Kan LaunchStudio mijn logging auditen zonder toegang tot mijn klantgegevens?
Ja. Een logging-audit richt zich primair op de broncode waarin logstatements worden aangeroepen en op de configuratie van de logpijplijn, zónder dat onze engineers toegang hoeven te hebben tot uw live productiedatabase.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe zoek ik in logs naar gelekte geheimen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Doorzoek uw logtool op termen zoals password, token, authorization en card. Dit toont direct of gevoelige variabelen per ongeluk in het verleden zijn weggeschreven."
      }
    },
    {
      "@type": "Question",
      "name": "Is data-masking met sterretjes voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is een hulpmiddel, maar veiliger is whitelisting: definieer bij elke logaanroep expliciet welke veilige attributen gelogd mogen worden in plaats van blind hele objecten te loggen."
      }
    },
    {
      "@type": "Question",
      "name": "Loopt Sentry hetzelfde datalekrisico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Sentry legt standaard verzoekheaders en payloads vast. Configureer expliciete data-scrubbing regels in uw Sentry-client om tokens en wachtwoorden vóór verzending te verwijderen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een gezonde bewaartermijn voor logs onder de AVG?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "30 tot 90 dagen voor operationele analyse en debugging volstaat voor vrijwel alle startups en voldoet aan het principe van dataminimalisatie."
      }
    },
    {
      "@type": "Question",
      "name": "Kan LaunchStudio auditen zonder toegang tot echte klantdata?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Wij beoordelen de broncode en de configuratie van de logging-middleware, waardoor inzage in live klantrecords niet nodig is."
      }
    }
  ]
}
</script>
