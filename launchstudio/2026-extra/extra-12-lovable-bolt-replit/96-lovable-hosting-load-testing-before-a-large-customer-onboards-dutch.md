---
Titel: "Lovable Hosting: Belastingtests Voordat een Grote Klant Instapt"
Trefwoorden: lovable loadtest, prestatietests, k6, Supabase-prestaties, capaciteitsplanning, onboarding van enterpriseklanten, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Lovable Hosting: Belastingtests Voordat een Grote Klant Instapt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Belastingtests Voordat een Grote Klant Instapt",
  "description": "Een klant die twee keer zo groot is als alle andere samen, vindt elke limiet van uw product op zijn eerste maandagochtend. Hoe u hun belasting modelleert, data op hun schaal aanmaakt, realistische tests draait, de resultaten leest, de bottleneck vindt, en live gaat met gemeten ruimte in plaats van hoop.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-load-testing-before-a-large-customer-onboards" }
}
</script>

Het contract is getekend. De nieuwe klant heeft meer gebruikers dan al uw bestaande klanten samen, en ze beginnen allemaal op dezelfde maandag. Uw product heeft nog nooit zoveel mensen bediend, zoveel data bevat of zoveel verzoeken in één uur gezien - en u ontdekt hoe het zich houdt in het bijzijn van de belangrijkste klant die u hebt.

Belastingtests vervangen die ontdekking door een generale repetitie. Het is geen enterpriseritueel voor grote engineeringteams. Voor een product dat is gebouwd met Lovable en Supabase is een nuttige loadtest een paar dagen werk: modelleren wat de klant gaat doen, data op hun schaal aanmaken, hun drukste uur nabootsen, en meten waar het product vertraagt. Bijna elk product dat dit doet, vindt twee of drie problemen die de klant binnen het eerste uur had gezien - en lost ze op voordat iemand het merkt.

Dit artikel behandelt wat u test, hoe u de belasting van een klant modelleert, waarom datavolume meer uitmaakt dan gelijktijdige gebruikers, hoe u veilig test, hoe u de resultaten leest, waar de bottlenecks in AI-gebouwde producten meestal zitten, en hoe u live gaat met gemeten ruimte.

## Begin bij de Klant, Niet bij de Tool

De meest voorkomende fout is beginnen met een tool en een willekeurig getal - "laten we kijken wat er gebeurt met duizend gebruikers" - in plaats van met het werkelijke gedrag van de klant.

Vraag het de klant, en schrijf op:

- **Hoeveel gebruikers, en hoeveel tegelijk actief.** Een zorgorganisatie met 2.600 zorgverleners kan er 900 hebben die de app openen tussen 6:45 en 7:15 wanneer de diensten beginnen. Dat halfuur is de test, niet het daggemiddelde.
- **Wat ze in dat venster doen.** Het rooster openen, de cliënten van vandaag bekijken, het begin van een bezoek registreren. Drie of vier acties, elk een handvol verzoeken.
- **Hoeveel data ze meebrengen.** Cliënten, records, geschiedenis, documenten - en hoeveel ze er per maand aan toevoegen.
- **Wat er voor hen op de achtergrond draait.** Nachtelijke berekeningen, herinneringen, koppelingen met hun systemen, facturatie aan het einde van de maand.
- **Wat ze koppelen.** Een API of import die duizenden records tegelijk stuurt, is een eigen belastingspatroon.

Definieer hieruit het scenario: de gebruikersroutes, hun verhouding, de piek in binnenkomst, en het datavolume - meestal getest op twee tot drie keer de verwachte omvang van de klant, zodat het resultaat ruimte meeneemt.

## Datavolume Doet Meer Ertoe dan Gelijktijdigheid

In AI-gebouwde producten worden de meeste prestatieproblemen niet veroorzaakt door veel mensen tegelijk. Ze worden veroorzaakt door één query die snel is met uw testdata en traag met die van een echte klant.

Een roosterscherm dat met vijftig zorgverleners in 200 milliseconden laadt, kan met drieduizend tien seconden duren, omdat het elke dienst voor elke zorgverlener ophaalt, of omdat een functie voor row level security voor elk van honderdduizend rijen een keer draait, of omdat een index die op kleine schaal overbodig leek ontbreekt. Niets daarvan verschijnt met tien gelijktijdige gebruikers op een kleine database; alles verschijnt met één gebruiker op een grote.

De eerste stap van een loadtest is dus geen verkeer maar data. Maak een testomgeving met data op de schaal van de klant - en op twee of drie keer die schaal - met gegenereerde data die op de werkelijkheid lijkt: dezelfde verdelingen, hetzelfde aantal gerelateerde records per ouder, dezelfde verhouding grote accounts. Het artikel over seeddata in deze reeks beschrijft hoe; waar het om gaat, is dat de grootste organisatie in de test even groot is als de grootste organisatie die u zult hebben.

Draai daarna de traagste schermen en endpoints als één gebruiker en bekijk de tijden en queryplannen voordat u enige gelijktijdigheid nabootst. Dat alleen vindt meestal het eerste probleem.

## Waar U de Test Draait

Niet tegen productie. Een loadtest die de database verzadigt, vertraagt elke bestaande klant, en testdata die in productie wordt weggeschreven, is het soort fout waarover maanden wordt gesproken.

Gebruik een aparte omgeving met dezelfde configuratie als productie: hetzelfde Supabase-abonnement en dezelfde rekenkracht, dezelfde poolinginstellingen, dezelfde configuratie van edge functions, dezelfde regio. Een Supabase-branch of een apart project werkt; waar het om gaat, is dat het genoeg op productie lijkt dat zijn limieten de limieten van productie zijn. Het artikel over omgevingsvariabelen in deze reeks beschrijft hoe u de inloggegevens gescheiden houdt.

Schakel alles wat naar buiten gaat in de testomgeving uit of leid het om: e-mails, sms, pushmeldingen, betalingen, boekhoudsynchronisatie, webhooks naar klanten. Een loadtest die drieduizend echte sms'jes verstuurt, is een loadtest die u om de verkeerde redenen onthoudt.

Draai de belastinggenerator van buiten het platform - een aparte machine of een clouddienst voor loadtests - zodat de test het netwerkpad meeneemt dat echte gebruikers nemen.

## Realistische Scenario's Schrijven

Een realistische test bootst na wat gebruikers doen, niet één endpoint dat zo snel mogelijk wordt aangeroepen.

```js
// k6-scenario: zorgverleners die aan hun dienst beginnen
import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  scenarios: {
    shift_start: {
      executor: 'ramping-arrival-rate',
      startRate: 2, timeUnit: '1s', preAllocatedVUs: 300,
      stages: [
        { target: 30, duration: '10m' },   // oplopen naar de piek
        { target: 30, duration: '20m' },   // de piek vasthouden
        { target: 2,  duration: '5m' },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:roster}': ['p(95)<800'],
    'http_req_duration{name:visit_start}': ['p(95)<500'],
  },
};

export default function () {
  const token = tokens[__VU % tokens.length];      // vooraf aangemaakte testgebruikers
  const headers = { Authorization: `Bearer ${token}` };
  const r = http.get(`${BASE}/rest/v1/rpc/my_roster_today`, { headers, tags: { name: 'roster' } });
  check(r, { 'roster ok': (res) => res.status === 200 });
  sleep(5 + Math.random() * 10);                   // het scherm lezen
  http.post(`${BASE}/functions/v1/visit-start`, JSON.stringify({ visit_id: pick(r) }),
            { headers, tags: { name: 'visit_start' } });
}
```

Vier details maken het verschil tussen een zinvolle en een misleidende test.

**Gebruik veel echte testgebruikers**, elk ingelogd met een eigen token en horend bij de juiste organisatie, zodat row level security zich gedraagt zoals in productie. Een test met één gebruiker en één token test caching, niet het product.

**Neem denktijd op** - de seconden die iemand besteedt aan het lezen van een scherm. Zonder denktijd gedragen honderd nagebootste gebruikers zich als enkele duizenden echte.

**Modelleer de binnenkomst, niet alleen het aantal gebruikers.** Mensen komen binnen over het piekvenster, niet allemaal in dezelfde milliseconde - tenzij het echte gedrag een melding is waarop iedereen tegelijk tikt, en test dan precies die piek.

**Bepaal vooraf wat slagen en falen is.** Grenswaarden - 95% van de roosterverzoeken onder 800 milliseconden, minder dan 1% fouten - maken van de test een ja of nee in plaats van een grafiek om te interpreteren.

k6 is een goede standaard voor producten van dit soort; Artillery en Locust zijn redelijke alternatieven. De tool doet er minder toe dan het scenario.

## Vier Soorten Tests

**Loadtest** - de verwachte piek, bij het verwachte datavolume, lang genoeg vastgehouden om betekenis te hebben. Dit beantwoordt "gaat maandagochtend goed?"

**Stresstest** - verhoog de belasting totdat er iets breekt, om te weten waar de grens ligt en wat als eerste faalt. Dit beantwoordt "hoeveel ruimte hebben we?"

**Piektest** - een plotselinge sprong van rustig naar piek, zoals na een pushmelding of een e-mail aan elke gebruiker. Dit test autoscaling, cold starts en connection pools.

**Duurtest** - een normale belasting gedurende enkele uren. Dit vindt geheugenlekken, wachtrijen die langzaam vollopen, en connection pools die na verloop van tijd achteruitgaan.

Voor de onboarding van één grote klant zijn een loadtest op twee tot drie keer hun verwachte piek en een piektest het minimum. Een stresstest vertelt u wanneer u de volgende upgrade moet plannen.

## Wat U Meet

Verzamel tijdens elke run drie groepen metingen.

**Van de belastinggenerator:** latentiepercentielen per stap in het scenario - mediaan, p95, p99 - foutpercentage en doorvoer. Percentielen doen er meer toe dan gemiddelden: een gemiddelde van 400 milliseconden kan verbergen dat één op de twintig verzoeken acht seconden duurt, en dat zijn de verzoeken die gebruikers onthouden.

**Van de database:** CPU, geheugen, actieve verbindingen tegenover de limiet, en vooral de traagste query's. Zet `pg_stat_statements` aan en bekijk de query's met de hoogste totale tijd tijdens de test - niet alleen de traagste afzonderlijke query, maar de query die duizenden keren tegen gemiddelde kosten draait. Het indexartikel in deze reeks beschrijft hoe u queryplannen leest.

**Van het platform:** duur en cold starts van edge functions, foutpercentages, en eventuele limieten van derden. Let ook op de lengte van wachtrijen voor achtergrondtaken, die stil kunnen groeien terwijl de voorkant gezond lijkt.

Leg de configuratie van elke run vast - datavolume, rekenkracht, codeversie - zodat resultaten na elke fix kunnen worden vergeleken.

## Waar AI-Gebouwde Producten Meestal Breken

Dezelfde handvol bottlenecks verschijnen in bijna elke test.

**Ontbrekende indexen en onbegrensde query's.** Lijsten die alles ophalen, filters op niet-geïndexeerde kolommen, sorteren van grote tabellen. De artikelen over paginering en indexen in deze reeks behandelen de oplossingen; ze leveren meestal de grootste afzonderlijke verbetering op.

**Row level security die per rij duur is.** Een policy die een functie aanroept die een eigen query uitvoert, geëvalueerd voor elke rij van een grote tabel. Herschrijf hulpfuncties als `stable security definer`-functies die de planner één keer kan evalueren, indexeer de lidmaatschapstabellen die ze lezen, en filter in query's expliciet op organisatie zodat de policy niet het enige filter is.

**N+1-patronen in verzoeken.** Een scherm dat een lijst laadt en daarna per item een apart verzoek doet - vijftig items, eenenvijftig verzoeken. Onschuldig voor één gebruiker, verpletterend voor negenhonderd. Vervang door één query of één RPC die teruggeeft wat het scherm nodig heeft.

**Uitputting van verbindingen.** Edge functions of een backend die rechtstreeks databaseverbindingen openen in plaats van de pooler te gebruiken, totdat de verbindingslimiet is bereikt en verzoeken beginnen te falen. Het artikel over connection pooling in deze reeks beschrijft de configuratie.

**Synchrone aanroepen naar derden.** Een pushmelding, e-mail of boekhoudboeking versturen binnen het verzoek van de gebruiker. Op schaal wordt de limiet van de aanbieder uw latentie. Verplaats het naar een wachtrij.

**Achtergrondtaken die niet lineair meeschalen.** Een nachtelijke berekening die twintig minuten duurt voor huidige klanten en zes uur voor de nieuwe, en overlapt met de ochtendpiek. Verdeel haar in batches, voer haar parallel uit met zorg voor de database, en test haar op het volume van de klant als onderdeel van de loadtest.

## De Cyclus van Oplossen en Opnieuw Testen

Belastingtests zijn iteratief. Draai de test, vind de grootste bottleneck, los haar op, draai dezelfde test opnieuw, vergelijk. Verander waar mogelijk één ding tegelijk, zodat elke verbetering toe te schrijven is.

Los de code op voordat u de infrastructuur opschaalt. Een grotere database maakt een ontbrekende index iets minder traag; de index toevoegen maakt het snel en laat u de kleinere instance houden. Zodra query's en patronen deugen, is een grotere database vaak nog steeds nodig - maar dan koopt die echte ruimte in plaats van een defect te verbergen.

Houd de scenarioscripts in de repository en draai ze opnieuw vóór elke belangrijke release en vóór elke nieuwe grote klant. Een loadtest die één keer draait, is een momentopname; een die regelmatig draait, vangt regressies op die een AI-ondersteunde refactor kan introduceren.

## Capaciteitsplanning en Kosten

De laatste testrun moet u drie getallen geven: de belasting die u verwacht, de belasting waarbij het product binnen zijn grenswaarden blijft, en de belasting waarbij het breekt. Streef naar twee tot drie keer ruimte tussen de verwachte piek en het punt waarop grenswaarden worden overschreden.

Vertaal dat naar infrastructuur en kosten: welke rekenkracht, welk abonnement, wat dat per maand kost, en wat de volgende stap omhoog kost wanneer de volgende klant komt. De artikelen over hostingkosten in deze reeks beschrijven hoe; het punt hier is dat de contractwaarde van de klant en de infrastructuurkosten om hem te bedienen nu allebei bekende getallen zijn in plaats van schattingen.

Deel een korte samenvatting met de klant als die erom vraagt - en grotere klanten doen dat steeds vaker. "We hebben getest op drie keer uw verwachte piek, met deze resultaten" is een sterk antwoord in een inkoopproces en een geruststellend antwoord voor hun projectleider.

## Instappen in Stappen

Vermijd ook na een geslaagde test, als het kan, dat elke gebruiker van een grote klant op dezelfde ochtend overstapt.

Spreek een gefaseerde onboarding af: eerst één afdeling of regio, de rest een week later. Volg tijdens de eerste fase de echte metingen en vergelijk ze met de test. Echte gebruikers doen altijd iets wat het scenario niet voorzag - een rapport dat op het drukste moment wordt gedraaid, een export van alles, een browsertabblad dat blijft verversen - en een eerste fase van een paar honderd gebruikers laat dat zien terwijl er weinig op het spel staat.

Bereid de reactie vooraf voor: wie de dashboards tijdens de eerste piek bewaakt, wat de grenswaarden voor ingrijpen zijn, welke noodschakelaars er zijn voor dure functies, zoals het artikel over feature flags in deze reeks beschrijft, en hoe de klant wordt geïnformeerd als er iets vertraagt.

## Dit Inrichten

Voor een Lovable- of Supabase-product dat zich voorbereidt op een grote klant, is dit doorgaans vier tot zes dagen: het piekgedrag, het datavolume en het achtergrondwerk van de klant gemodelleerd op basis van gesprekken met hen, een testomgeving die op productie lijkt met uitgaande berichten uitgeschakeld, gegenereerde data op twee tot drie keer de schaal van de klant, eerst profilering van de traagste schermen met één gebruiker, realistische scenario's met veel testgebruikers, denktijd, binnenkomstpatronen en grenswaarden voor slagen of falen, minimaal load- en piektests, metingen van database, platform en wachtrijen per run, de gangbare bottlenecks aangepakt - indexen, onbegrensde lijsten, kosten van row level security, N+1-patronen, pooling, synchrone aanroepen naar derden, schaalbaarheid van achtergrondtaken - een cyclus van oplossen en opnieuw testen waarbij code wordt opgelost voordat infrastructuur wordt opgeschaald, een samenvatting van capaciteit en kosten met expliciete ruimte, scenarioscripts bewaard voor toekomstige runs, en een gefaseerde onboarding met bewaking en een voorbereide reactie.

LaunchStudio voert dit uit vóór de onboarding die er het meest toe doet. Daarachter staat Manifera - elf jaar, 120+ engineers, 160+ projecten, met infrastructuurervaring bij klanten waaronder Vodafone, TNO en CFLW.

[Vertel ons over de klant die u op het punt staat binnen te halen](https://launchstudio.eu/nl/#contact) en wij vertellen u wat u moet testen.

## Echt voorbeeld

### Negenhonderd Zorgverleners om Zeven Uur

Thomas van Leeuwen bouwde Zorgrooster in Lovable: roosters en bezoekregistratie voor thuiszorgorganisaties, gebruikt door 23 kleine organisaties met samen zo'n 1.400 zorgverleners.

Hij tekende een regionale zorggroep met 2.600 zorgverleners - bijna het dubbele van zijn hele gebruikersbestand - met livegang op een maandag. De diensten van de zorggroep beginnen om 7:00, en de meeste zorgverleners openen de app tussen 6:45 en 7:15 om hun cliënten voor die dag te zien.

Een loadtest in een omgeving die op productie leek, met gegenereerde data op drie keer de omvang van de zorggroep en een scenario van 900 zorgverleners die in dertig minuten binnenkwamen, faalde zwaar. De p95 van het roosterscherm was 9,8 seconden. Bij ongeveer 400 gelijktijdige gebruikers begonnen verzoeken te falen met verbindingsfouten. Het starten van een bezoek stuurde binnen het verzoek een pushmelding naar de coördinator, en de limiet van de aanbieder voegde seconden toe aan elke bezoekstart. En de nachtelijke berekening van gewerkte uren, die voor bestaande klanten twintig minuten duurde, duurde op de nieuwe schaal zes uur - en eindigde nadat de ochtendpiek was begonnen.

Vijf werkdagen: de roosterquery herschreven zodat één week voor één zorgverlener via één RPC wordt opgehaald, met twee samengestelde indexen toegevoegd; de hulpfunctie voor row level security herschreven als `stable security definer`-functie met een geïndexeerde opzoeking van het lidmaatschap, waardoor een subquery per rij verdween; edge functions overgezet naar de transaction pooler; pushmeldingen verplaatst naar een wachtrij die door een worker wordt verwerkt; de urenberekening in batches per organisatie en week verdeeld en parallel uitgevoerd met een limiet op gelijktijdigheid; de database na de codefixes één maat groter gemaakt; en de load- en piektests na elke wijziging opnieuw gedraaid.

**Resultaat:** de laatste test op drie keer de verwachte piek van de zorggroep gaf een rooster-p95 van 420 milliseconden, geen fouten en een nachtelijke berekening van 35 minuten. De zorggroep stapte in twee fasen in; op de tweede maandag begonnen 2.600 zorgverleners aan hun dienst zonder één supportvraag over snelheid. De infrastructuurkosten stegen met ongeveer €110 per maand.

> *"De eerste test vertelde me dat het rooster op de eerste ochtend van onze grootste klant tien seconden zou laden en daarna helemaal niet meer. Dat hoorde ik veel liever van k6 dan van negenhonderd zorgverleners."*
> - **Thomas van Leeuwen, Oprichter, Zorgrooster (Assen)**

**Kosten & Doorlooptijd:** €5.400 (modellering van de klantbelasting, testomgeving vergelijkbaar met productie met gegenereerde data op 3x schaal, k6-load- en piekscenario's, fixes van query's en indexen, herschreven hulpfunctie voor row level security, poolerconfiguratie, meldingen via een wachtrij, nachtelijke berekening in batches, bepalen van de databasegrootte, plan voor gefaseerde onboarding) - afgerond in 5 werkdagen.

## Veelgestelde vragen

### Wanneer moet ik mijn product belasten in een test?

Vóór de onboarding van een klant die aanzienlijk groter is dan uw huidige, vóór een lancering of campagne die een plotselinge piek brengt, en als vaste controle vóór belangrijke releases.

### Moet ik een loadtest tegen productie draaien?

Nee. Gebruik een aparte omgeving met hetzelfde abonnement, dezelfde rekenkracht, pooling en regio, met uitgaande berichten uitgeschakeld, zodat de test bestaande klanten niet raakt en geen echte berichten verstuurt.

### Is het aantal gelijktijdige gebruikers de belangrijkste factor?

Meestal niet. In AI-gebouwde producten veroorzaakt datavolume de meeste vertragingen - query's en policies die op weinig data snel zijn en op veel data traag. Maak eerst data aan op de schaal van de klant.

### Wat moet ik meten tijdens een loadtest?

Latentiepercentielen en foutpercentages per gebruikersactie, CPU, verbindingen en traagste query's van de database, duur en cold starts van edge functions, limieten van derden, en de lengte van achtergrondwachtrijen.

### Moet ik eerst de database opschalen of de code oplossen?

Los eerst de code op - indexen, onbegrensde query's, dure policies, N+1-patronen. Bepaal daarna de infrastructuur voor twee tot drie keer de verwachte piek.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer moet een SaaS-product worden belast in een test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vóór de onboarding van een veel grotere klant, vóór een lancering of campagnepiek, en regelmatig vóór belangrijke releases."
      }
    },
    {
      "@type": "Question",
      "name": "Is een loadtest tegen productie veilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - gebruik een omgeving die op productie lijkt, met hetzelfde abonnement, dezelfde rekenkracht, pooling en regio, en uitgaande berichten uitgeschakeld."
      }
    },
    {
      "@type": "Question",
      "name": "Wat veroorzaakt meestal vertraging in AI-gebouwde apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Datavolume meer dan gelijktijdigheid - ontbrekende indexen, onbegrensde lijsten en dure row level security op grote datasets."
      }
    },
    {
      "@type": "Question",
      "name": "Welke metingen doen ertoe in een loadtest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Latentiepercentielen en fouten per actie, database-CPU, verbindingen en trage query's, cold starts van functies, limieten van derden en wachtrijlengtes."
      }
    },
    {
      "@type": "Question",
      "name": "Eerst infrastructuur opschalen of code oplossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eerst de code oplossen, daarna de infrastructuur bepalen voor twee tot drie keer de verwachte piek."
      }
    }
  ]
}
</script>
