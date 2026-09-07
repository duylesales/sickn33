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

Vier categorieën data mogen onder geen enkel beding in logs terechtkomen:

**1. Wachtwoorden in welke vorm dan ook — platte tekst én hashes.** Een wachtwoord mag buiten het specifieke authenticatiepad dat het direct hasht nergens als losse variabele bestaan. Een logregel in dat pad die het ruwe request-object logt, legt het wachtwoord permanent vast in platte tekst, in een logsysteem met doorgaans veel zwakkere toegangsbeperkingen dan uw beveiligde gebruikersdatabase.

**2. Sessietokens, API-sleutels en JWT's.** Dit zijn de digitale sleutels waarmee iemand zich kan voordoen als een gebruiker of beheerder zónder wachtwoord. Het integraal loggen van een `Authorization`-header (wat naïeve logging-middleware standaard vaak doet) overhandigt aan iedereen met leesrechten op uw logbestanden een actieve, geldige sessie voor het betreffende account.

**3. Volledige creditcardnummers, CVV-codes of magnetische stripdata.** Als uw applicatie correct is gebouwd met Stripe, Mollie of Adyen via tokenisatie (zoals Stripe Elements of een gehoste betaalpagina), krijgt uw eigen server überhaupt nooit een volledig creditcardnummer te zien. Verschijnt er tóch een kaartnummer in uw logs? Dan handelt uw server ruwe betaaldata af op een manier die zware **PCI-DSS compliance-overtredingen** oplevert. Dit vereist een acute architectuurrevisie, niet slechts het wissen van de logregel.

**4. Volledige persoonsdossiers in één logregel.** Een compleet medisch dossier, een volledige adresregistratie met geboortedatum en identiteitsbewijs integraal als JSON dumpen onder het mom van `console.log(userObject)`. Individueel kan een referentie naar een `user_id` prima zijn; gebundeld als compleet profiel verandert één enkele logregel bij een datalek in een ernstig privacy-incident dat onder de AVG direct gemeld moet worden bij de Autoriteit Persoonsgegevens.

## Gestructureerd Loggen (Structured Logging): Waarom Vrije Tekst Niet Schaalt

De meeste AI-tools genereren ongestructureerde logging: een platte tekststring met wat variabelen aan elkaar geplakt via `console.log('Gebruiker ' + userId + ' inloggen mislukt')`. Dit is prima leesbaar voor een ontwikkelaar die lokaal door tien regeltjes scrolt. Het wordt volstrekt onwerkbaar zodra u echt productieverkeer heeft, omdat er geen betrouwbare manier is om tienduizenden vrije tekstregels geautomatiseerd te filteren of te aggregeren.

**Gestructureerd loggen** schrijft elk logbericht weg als een gestandaardiseerd JSON-object met benoemde velden:
`{"level": "error", "event": "login_failed", "user_id": 1193, "reason": "invalid_password", "timestamp": "2027-02-25T14:30:00Z"}`

De praktische winst is enorm: de vraag *"hoeveel mislukte inlogpogingen waren er voor dit account in het afgelopen uur?"* is in een structured logviewer een simpele filteropdracht. In ongestructureerde tekst is het een onbegonnen zoektocht. Bovendien dwingt een gestructureerde logger met een vast schema u om bewust na te denken over wélke velden u meestuurt — waardoor gevoelige wachtwoorden automatisch buiten de boot vallen.

## Bewaartermijnen (Retention): Wat Is Nodig en Wat Is een Risico?

Bewaartermijn is een instelling die in prototypes zelden expliciet wordt geconfigureerd. Logs hopen zich simpelweg op volgens de standaardinstelling van het platform — een paar dagen bij een gratis hostingtier, of oneindig lang als ze worden doorgestuurd naar een ongecontroleerde cloudopslag.

Beide uitersten zijn riskant:
- **Te korte bewaartermijn (minder dan 7 dagen):** Als een klant een storing meldt die vorig weekend plaatsvond en uw logs na 48 uur automatisch gewist zijn, kunt u niets meer onderzoeken.
- **Te lange bewaartermijn (jarenlang):** Elke dag dat een logbestand met persoonsgegevens opgeslagen ligt, vormt het een doelwit bij een eventuele inbraak. Onder de **AVG/GDPR** geldt het principe van **dataminimalisatie**: persoonsgegevens (zoals IP-adressen of e-mailadressen in foutmeldingen) mogen niet langer bewaard worden dan strikt noodzakelijk voor het doel waarvoor ze zijn verzameld.

De gezonde industriestandaard voor startende SaaS-bedrijven: **30 tot 90 dagen actieve, doorzoekbare bewaartermijn** voor operationele foutopsporing. Stel deze termijn expliciet in in het dashboard van uw loggingprovider (zoals Better Stack of Datadog).

## Foutmeldingen voor Gebruikers versus Wat U Achter de Schermen Logt

AI-code maakt bij foutafhandeling vaak een van twee fouten: het toont de gebruiker een ruwe stack trace of database-foutmelding (waarmee interne tabelnamen en codefragmenten op straat komen te liggen), óf het toont een generiek *"Er ging iets mis"* zónder dat er op de server iets nuttigs wordt gelogd.

De professionele scheiding:
- **De gebruiker ziet:** Een heldere, vriendelijke melding (*"We konden uw betaling niet verwerken. Probeer het opnieuw of neem contact op met support"*), vergezeld van een uniek referentie-ID: `Referentie: err_8f92a1`.
- **Uw logsysteem registreert:** De volledige technische details, de exacte stack trace en de relevante ID's, gekoppeld aan datzelfde referentie-ID `err_8f92a1`. Zo kan een supportmedewerker direct het exacte logbericht erbij pakken zodra een klant de foutcode doorgeeft, zónder dat interne systeeminformatie ooit aan de buitenwereld wordt prijsgegeven.

## De Pre-Launch Logging-Audit in Één Uur

Doorloop uw applicatie vóór de lancering aan de hand van deze stappen:
1. Doorzoek uw gehele codebase op `console.log`, `print` of vergelijkbare functies op complete request-body's (`req.body`). Verwijder of saneer ze direct.
2. Zorg dat logs worden weggeschreven als gestructureerde JSON-objecten.
3. Controleer de bewaartermijn bij uw hosting- of loggingprovider en zet deze vast op 30 tot 90 dagen.
4. Verifieer dat foutmeldingen in de browser nooit ruwe databasefouten of stack traces lekken, maar voorzien zijn van een uniek referentie-ID.
5. **De Sandbox Betalingstest:** Simuleer een mislukte betaling in uw testomgeving en controleer letter voor letter wat er over die transactie in uw logviewer verschijnt.

Binnen het [Launch Ready-pakket](https://launchstudio.eu/nl/#packages) van LaunchStudio lichten de senior engineers van Manifera uw loggingarchitectuur en datastromen binnen enkele dagen door. Wij saneren kwetsbare logstatements en richten gestructureerde logging in, zodat u klaar bent voor strenge security-audits van zakelijke klanten. [Vraag direct een vrijblijvende review aan](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

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
