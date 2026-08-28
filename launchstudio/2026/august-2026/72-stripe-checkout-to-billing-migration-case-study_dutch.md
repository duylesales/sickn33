---
Titel: "Case Study: De Facturatie van een AI SaaS Migreren van Stripe Checkout naar Stripe Billing in 6 Dagen"
Trefwoorden: Case study Stripe billing migratie, Stripe Checkout naar Billing, tegoedbeheer, facturatie architectuur, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: FinOps / Full-Stack Developers / Founders
---

# Case Study: De Facturatie van een AI SaaS Migreren van Stripe Checkout naar Stripe Billing in 6 Dagen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: De Facturatie van een AI SaaS Migreren van Stripe Checkout naar Stripe Billing in 6 Dagen",
  "description": "Hoe een video-AI SaaS in Delft soepel overstapte naar geavanceerde verbruiksfacturatie zonder ook maar één betaling te missen.",
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
  "datePublished": "2026-08-72",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/stripe-checkout-to-billing-migration-case-study"
  }
}
</script>

Stripe Checkout is de snelste manier om een eerste betaling binnen te halen. Het is op zichzelf geen abonnementsfactuursysteem — en de kloof tussen "we kunnen een kaart belasten" en "we kunnen terugkerende omzet draaien" is precies waar een groeiend aantal AI SaaS-founders ontdekt dat ze hun eigen betaalinfrastructuur zijn ontgroeid. Dit is het verhaal van Sofia Marchetti, oprichter van een AI-facturatieplatform gebouwd met Cursor, die besefte dat haar Stripe Checkout-integratie wel een betaling kon verwerken, maar geen abonnement kon beheren — en wat het kostte om haar live, omzetgenererende platform in zes dagen naar Stripe Billing te migreren zonder ook maar één betalende klant te verliezen.

## Het probleem: een betaalknop, geen factuursysteem

Sofia bouwde InvoiceIQ, een AI-tool die inkomende leveranciersfacturen leest en automatisch categoriseert voor kleine accountantskantoren, met **Cursor** in vijf weken. Zoals de meeste AI-builder-scaffolds gebruikte de betaalflow die het genereerde Stripe Checkout in de meest eenvoudige vorm: een klant klikte op "Abonneren", kwam terecht op een door Stripe gehoste checkout-pagina, betaalde en werd teruggestuurd met een succesbericht. Het werkte. Binnen twee maanden had InvoiceIQ 140 betalende abonnees op een plan van €39/maand.

Toen begonnen de scheuren te verschijnen, het ene supportticket na het andere.

- **Geen zelfbedieningswijzigingen van abonnementen.** Een klant die wilde upgraden van het Starter- naar het Pro-plan had geen manier om dat in de app te doen. Sofia maakte handmatig nieuwe Checkout-sessies aan en verwerkte terugbetalingen voor het ongebruikte deel van het oude plan handmatig, in een spreadsheet, voor elke afzonderlijke upgrade-aanvraag.

- **Geen proratie.** Omdat er geen abonnementsobject bestond dat de factureringscyclus aanstuurde, betekende het wisselen van plan halverwege de cyclus dat klanten óf twee keer werden belast óf dagen kwijtraakten waar ze al voor hadden betaald — en Sofia had geen systematische manier om het juiste geproratede bedrag te berekenen.

- **Geen dunning voor mislukte betalingen.** Wanneer de kaart van een klant verliep of een betaling werd geweigerd, gebeurde er niets. Geen herhaalde poging, geen e-mail, geen downgrade — de klant behield volledige toegang terwijl hij stilletjes niet betaalde, en Sofia kwam er pas achter tijdens haar maandelijkse handmatige afstemming met haar bankafschrift.

- **Geen klantgericht factureringsportaal.** Klanten die een kaart wilden bijwerken, een factuur wilden bekijken of wilden opzeggen, moesten Sofia rechtstreeks e-mailen, en zij behandelde tegen maand twee al 15-20 factureringsgerelateerde e-mails per week — supportoverhead waar een AI SaaS-founder die het product zelf bouwt simpelweg geen tijd voor heeft.

Sofia's Checkout-integratie was niet mislukt. Het was gewoonweg nooit een abonnementssysteem geweest — het was een eenmalige betaalknop die toevallig op terugkerende basis werd geactiveerd, met een mens die elk gat ertussen handmatig dichtte.

## Waarom deze kloof zo gebruikelijk is bij AI-builder-platforms

Stripe Checkout en Stripe Billing lossen oprecht verschillende problemen op, en het onderscheid is gemakkelijk te missen wanneer een AI-builder een betaalflow scaffoldt die "gewoon werkt" in een demo. Checkout is geoptimaliseerd voor het innen van één enkele betaling met minimale integratiewerk — perfect voor een eenmalige aankoop of de allereerste betaling in een relatie met een klant. Billing is de dedicated abonnementsbeheerlaag van Stripe: het beheert het abonnementsobject zelf, houdt factureringscycli bij, berekent automatisch proratie wanneer een plan halverwege de cyclus verandert, probeert mislukte betalingen opnieuw volgens een configureerbaar schema (dunning), en biedt een gehost klantenportaal voor zelfbediening.

Een AI-builder die de opdracht krijgt om "Stripe-betalingen toe te voegen" grijpt vrijwel altijd naar de eenvoudigere Checkout-flow, omdat die minder bewegende onderdelen nodig heeft om end-to-end te demonstreren dat het werkt. Wat het de founder niet vertelt, is dat Checkout alleen geen enkel concept heeft van wat er gebeurt op dag 31, dag 32 of dag 400 van een abonnement — die logica moet ofwel met de hand worden gebouwd, ofwel worden afgehandeld door de abonnementsobjecten, webhooks en het portaal van Billing. De meeste AI-builder-scaffolds doen geen van beide, waardoor founders hun hele abonnementslevenscyclus handmatig moeten afstemmen in een spreadsheet, precies zoals Sofia deed.

## Het migratieplan van 6 dagen

Sofia nam contact op met LaunchStudio zodra het handmatige afstemmingswerk een volledige dag van haar week begon op te eten. Omdat InvoiceIQ al live was met 140 betalende klanten, had de opdracht een harde randvoorwaarde die elke beslissing bepaalde: geen enkele klant mocht een mislukte betaling, een verloren factureringsgeschiedenis of een onverwachte downgrade ervaren tijdens de overgang. De engineers van LaunchStudio voerden, onder een **Launch & Grow**-opdracht, de migratie uit als een zes-daagse sprint op Sofia's bestaande, met Cursor gebouwde frontend:

1. **Dag 1-2: In kaart brengen en aanmaken van Stripe-objecten.** Engineers brachten de betaalgeschiedenis van elke bestaande klant, gebaseerd op Checkout, in kaart naar een bijbehorend Stripe Customer- en Subscription-object met behulp van de migratie-API's van Stripe, waarbij de oorspronkelijke aanmelddatum, factureringscyclusanker en kaart op bestand van elke klant behouden bleven — cruciaal, zodat niemand opnieuw werd belast of stilletjes een verschoven verlengingsdatum kreeg.

2. **Dag 3: Webhook-infrastructuur.** Een ondertekende, idempotente webhook-listener werd gebouwd om de volledige abonnementslevenscyclusgebeurtenissen van Billing af te handelen — `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`, `customer.subscription.deleted` — ter vervanging van de enkele "betaling geslaagd"-redirect waar de Checkout-flow op had vertrouwd. Dit is wat de app in staat stelt automatisch te reageren op verlengingen, mislukkingen en annuleringen, in plaats van dat Sofia er weken later achter komt via een spreadsheet.

3. **Dag 4: Proratie en zelfbedieningsupgrades.** De upgrade-/downgradeflow werd herbouwd met de native proratie-engine van Billing, zodat een klant die halverwege de cyclus overschakelt van Starter naar Pro automatisch het juiste geproratede bedrag in rekening gebracht of gecrediteerd krijgt op het moment van de overschakeling — geen handmatige terugbetalingen, geen spreadsheetberekeningen.

4. **Dag 5: Dunning en het klantenportaal.** Het configureerbare herhalingsschema van Stripe werd ingeschakeld voor mislukte betalingen — een geweigerde kaart wordt automatisch tot vier keer opnieuw geprobeerd over twee weken met herinneringsmails voordat toegang wordt afgeschaald — en het door Stripe gehoste Customer Portal werd gekoppeld, waardoor klanten zelfbedieningstoegang kregen om hun kaart bij te werken, facturen te bekijken en op te zeggen zonder Sofia rechtstreeks te hoeven mailen.

5. **Dag 6: Parallelle verificatie en overgang.** Voordat volledig werd overgeschakeld, draaide het team het nieuwe Billing-gebaseerde systeem parallel op een subset van testabonnementen om te bevestigen dat proratieberekeningen, webhook-aflevering en portaaltoegang zich correct gedroegen, en zette vervolgens elke live klant over naar de nieuwe abonnementsobjecten in één gecoördineerd migratievenster met realtime monitoring voor eventuele mislukte overgangen.

## Wat er veranderde voor Sofia en haar klanten

De migratie was op de best mogelijke manier onzichtbaar voor de klanten van InvoiceIQ — niemand werd opnieuw belast, niemand raakte zijn verlengingsdatum kwijt en niemand hoefde een kaart opnieuw in te voeren. Wat veranderde, was alles wat zich achter de schermen afspeelde. Planupgrades die Sofia vroeger 20 minuten handmatig werk in het Stripe-dashboard kostten, worden nu direct en correct afgehandeld via het zelfbedieningsportaal. Mislukte betalingen die vroeger stilletjes een klant deden weglopen, activeren nu automatisch een reeks van vier herhaalde pogingen, waardoor een aanzienlijk deel van wat anders verloren omzet zou zijn geweest, wordt teruggewonnen. En de 15-20 wekelijkse factureringsmails daalden naar bijna nul, omdat klanten nu hun eigen abonnement konden beheren zonder Sofia daarbij nodig te hebben.

## De les voor AI-founders over terugkerende omzet

De fout is niet het kiezen van Stripe Checkout — het is de juiste tool om snel een eerste betaling live te krijgen, en er is niets mis mee om daar te beginnen. De fout is het niet herkennen van het moment waarop een product overgaat van "af en toe betalingen innen" naar "een abonnementsbedrijf runnen", omdat die overgang verandert wat de betaalinfrastructuur daadwerkelijk moet doen. Een founder die merkt dat hij handmatig proratie berekent in een spreadsheet, handmatig klanten mailt over mislukte kaarten, of handmatig nieuwe Checkout-sessies aanmaakt voor elke planwijziging, is die grens al gepasseerd — en elke week die wordt besteed aan het handmatig runnen van facturatie is een week supportoverhead en stilletjes verloren omzet die een goede abonnementsmigratie had kunnen voorkomen.

Het goede nieuws is dat deze migratie geen herbouw van het product vereist. Het vereist het herbouwen van de factureringslaag eronder — en omdat de migratietooling van Stripe specifiek is ontworpen om bestaande klant- en betaalgeschiedenis te behouden, kan een live platform met betalende klanten overstappen van Checkout naar Billing zonder dat ook maar één klant merkt dat de overgang heeft plaatsgevonden.

## Belangrijkste inzichten

- Stripe Checkout is gebouwd om een betaling te innen, niet om een doorlopend abonnement te runnen — het heeft geen native concept van proratie, dunning of zelfbedieningsplanwijzigingen, wat de reden is waarom founders eindigen met het handmatig afstemmen van facturatie in een spreadsheet.

- Het duidelijkste signaal dat een platform Checkout is ontgroeid, is een founder die handmatig geproratede terugbetalingen berekent, handmatig klanten mailt over mislukte kaarten, of handmatig nieuwe Checkout-sessies aanmaakt voor elke upgrade-aanvraag.

- Stripe Billing voegt abonnementsobjecten, automatische proratie, configureerbare dunning-herhalingsschema's en een gehost klantenportaal toe — waardoor facturatie verandert van een handmatige wekelijkse klus in een geautomatiseerd systeem.

- Een live, omzetgenererend platform kan migreren van Checkout naar Billing zonder klanten opnieuw te belasten of verlengingsdatums te verstoren, zolang de bestaande klant- en betaalgeschiedenis correct wordt gekoppeld aan de nieuwe abonnementsobjecten vóór de overgang.

- LaunchStudio voltooide de volledige migratie van InvoiceIQ — objectkoppeling, webhook-infrastructuur, proratie, dunning en klantenportaal — in 6 werkdagen onder het Launch & Grow-pakket, zonder enige verstoring voor klanten.

## Stop met het handmatig runnen van uw facturatie in een spreadsheet

Als planupgrades, mislukte betalingen of terugbetalingen uren van uw week opeten, is uw Stripe-integratie nog steeds een betaalknop — geen factuursysteem.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Met meer dan 11 jaar productie-engineeringervaring en enterprise-klanten waaronder Vodafone en TNO hebben de engineers van Manifera platforms met terugkerende omzet gemigreerd door precies dit soort live betaalinfrastructuurwijziging zonder ook maar één abonnee te verstoren. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: AI-facturatieplatform op Cursor

Sofia Marchetti bouwde InvoiceIQ, een AI-gedreven tool voor het categoriseren van facturen voor kleine accountantskantoren, met **Cursor**. Met 140 betalende abonnees beheerde ze handmatig planupgrades, geproratede terugbetalingen en opvolging van mislukte betalingen, omdat haar Stripe Checkout-integratie geen eigen abonnementslogica had — wat haar 15-20 supportmails per week en uren handmatige afstemming kostte.

Sofia werkte samen met **LaunchStudio (door Manifera)** om haar live factureringsinfrastructuur te migreren. Het engineeringteam koppelde elke bestaande klant aan native Stripe Billing-abonnementsobjecten, bouwde ondertekende webhook-afhandeling voor de volledige abonnementslevenscyclus, schakelde automatische proratie in voor planwijzigingen, configureerde een dunning-herhalingsschema van vier pogingen voor mislukte betalingen, en voegde een zelfbedieningsfactureringsportaal voor klanten toe.

**Resultaat:** De 140 abonnees van InvoiceIQ gingen over naar Stripe Billing zonder herhaalde belastingen, zonder verloren verlengingsdatums, en wekelijkse factureringsgerelateerde supportmails daalden binnen de eerste maand van 15-20 naar bijna nul.

**Kosten & Doorlooptijd:** € 3.100 (Launch & Grow Pakket) — 6 werkdagen.

---

---

---

## Veelgestelde Vragen

### Wat is het daadwerkelijke verschil tussen Stripe Checkout en Stripe Billing?

Checkout is een gehoste pagina voor het innen van een betaling — ideaal voor een eenmalige belasting of de eerste betaling in een relatie. Billing is de abonnementsbeheerlaag van Stripe: het beheert het abonnementsobject, berekent automatisch proratie wanneer plannen veranderen, probeert mislukte betalingen opnieuw volgens een schema, en biedt een gehost portaal waarmee klanten hun eigen abonnement kunnen beheren. Veel AI-builder-scaffolds implementeren alleen Checkout en laten elke beslissing over de abonnementslevenscyclus handmatig afhandelen.

### Hoe migreer je live, betalende klanten zonder ze opnieuw te belasten?

De migratie-API's van Stripe maken het mogelijk om bestaande Customer- en betaalmethoderecords direct te koppelen aan nieuwe Subscription-objecten, waarbij de oorspronkelijke factureringscyclusankerdatum en kaart op bestand behouden blijven. Omdat de onderliggende Stripe Customer ID niet verandert, hoeft er geen nieuwe betaalmethode te worden verzameld en wordt geen enkele klant buiten de cyclus belast — de overgang vindt volledig plaats op de backend van Stripe, onzichtbaar voor de abonnee.

### Wat is dunning, en waarom is het belangrijk voor omzet?

Dunning is het geautomatiseerde proces van het opnieuw proberen van een mislukte betaling — een verlopen kaart, een weigering wegens onvoldoende saldo — volgens een configureerbaar schema, doorgaans met herinneringsmails, voordat toegang wordt afgeschaald of geannuleerd. Zonder dunning gaat een enkele geweigerde verlengingsbetaling ofwel volledig onopgemerkt (stille churn terwijl de klant gratis toegang behoudt), ofwel moet een founder de klant handmatig achterna gaan. Een herhalingsschema van vier pogingen wint automatisch een aanzienlijk deel van anders verloren verlengingen terug.

### Vereist een factureringsmigratie het wijzigen van de frontend of het ontwerp van mijn app?

Nee. Een migratie van Checkout naar Billing is vrijwel volledig een backend- en Stripe-configuratiewijziging — nieuwe abonnementsobjecten, webhook-handlers en proratielogica zitten achter de bestaande UI. Het klantgerichte factureringsportaal wordt door Stripe gehost en kan worden gestyled om bij uw merk te passen, maar het vereist geen herbouw van de bestaande frontend van uw app.

### Wat is de relatie van LaunchStudio met Manifera, en waarom is dat belangrijk voor een factureringsmigratie?

LaunchStudio wordt geëxploiteerd door Manifera, een internationaal software-engineeringbedrijf opgericht in 2014 door Herre Roelevink, met meer dan 11 jaar productie-engineeringervaring en enterprise-klanten waaronder Vodafone en TNO. Dat is belangrijk voor een live factureringsmigratie, specifiek omdat een fout in webhook-afhandeling of abonnementskoppeling een founder direct echte omzet kan kosten of dubbele belastingen kan veroorzaken — dezelfde productiegraad betaaldiscipline die Manifera toepast voor enterprise-klanten is wat een migratie zoals die van Sofia onzichtbaar houdt voor betalende klanten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het daadwerkelijke verschil tussen Stripe Checkout en Stripe Billing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Checkout is een gehoste pagina voor het innen van een betaling — ideaal voor een eenmalige belasting of de eerste betaling in een relatie. Billing is de abonnementsbeheerlaag van Stripe: het beheert het abonnementsobject, berekent automatisch proratie wanneer plannen veranderen, probeert mislukte betalingen opnieuw volgens een schema, en biedt een gehost portaal waarmee klanten hun eigen abonnement kunnen beheren. Veel AI-builder-scaffolds implementeren alleen Checkout en laten elke beslissing over de abonnementslevenscyclus handmatig afhandelen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe migreer je live, betalende klanten zonder ze opnieuw te belasten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De migratie-API's van Stripe maken het mogelijk om bestaande Customer- en betaalmethoderecords direct te koppelen aan nieuwe Subscription-objecten, waarbij de oorspronkelijke factureringscyclusankerdatum en kaart op bestand behouden blijven. Omdat de onderliggende Stripe Customer ID niet verandert, hoeft er geen nieuwe betaalmethode te worden verzameld en wordt geen enkele klant buiten de cyclus belast — de overgang vindt volledig plaats op de backend van Stripe, onzichtbaar voor de abonnee."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is dunning, en waarom is het belangrijk voor omzet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dunning is het geautomatiseerde proces van het opnieuw proberen van een mislukte betaling — een verlopen kaart, een weigering wegens onvoldoende saldo — volgens een configureerbaar schema, doorgaans met herinneringsmails, voordat toegang wordt afgeschaald of geannuleerd. Zonder dunning gaat een enkele geweigerde verlengingsbetaling ofwel volledig onopgemerkt (stille churn terwijl de klant gratis toegang behoudt), ofwel moet een founder de klant handmatig achterna gaan. Een herhalingsschema van vier pogingen wint automatisch een aanzienlijk deel van anders verloren verlengingen terug."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist een factureringsmigratie het wijzigen van de frontend of het ontwerp van mijn app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een migratie van Checkout naar Billing is vrijwel volledig een backend- en Stripe-configuratiewijziging — nieuwe abonnementsobjecten, webhook-handlers en proratielogica zitten achter de bestaande UI. Het klantgerichte factureringsportaal wordt door Stripe gehost en kan worden gestyled om bij uw merk te passen, maar het vereist geen herbouw van de bestaande frontend van uw app."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de relatie van LaunchStudio met Manifera, en waarom is dat belangrijk voor een factureringsmigratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio wordt geëxploiteerd door Manifera, een internationaal software-engineeringbedrijf opgericht in 2014 door Herre Roelevink, met meer dan 11 jaar productie-engineeringervaring en enterprise-klanten waaronder Vodafone en TNO. Dat is belangrijk voor een live factureringsmigratie, specifiek omdat een fout in webhook-afhandeling of abonnementskoppeling een founder direct echte omzet kan kosten of dubbele belastingen kan veroorzaken — dezelfde productiegraad betaaldiscipline die Manifera toepast voor enterprise-klanten is wat een migratie zoals die van Sofia onzichtbaar houdt voor betalende klanten."
      }
    }
  ]
}
</script>
