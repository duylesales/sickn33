---
Titel: "Marktplaatsen voor AI-begeleiding: sessie-no-shows doorbreken de restitutielogica die niemand heeft getest"
Trefwoorden: ai saas, two-sided marketplace, tutoring marketplace app, no-show refund logic, ai-generated code
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Marktplaatsen voor AI-begeleiding: sessie-no-shows doorbreken de restitutielogica die niemand heeft getest

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Marktplaatsen voor AI-begeleiding: sessie-no-shows doorbreken de restitutielogica die niemand heeft getest",
  "description": "Door AI gebouwde bijlesmarktplaatsen behandelen meestal de no-show van een student en vergeten stilletjes de no-show van de docent, waardoor betalende studenten het volledige bedrag in rekening worden gebracht zonder restitutie wanneer de docent degene is die niet komt opdagen.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/tutoring-marketplace-ai-app-session-no-show-refunds"
  }
}
</script>

Iedereen test het gelukkige pad. Iedereen onthoudt ook dat hij moet testen wat er gebeurt als de klant niet komt opdagen. Dat is het voor de hand liggende randgeval, waar elke oprichter van een marktplaats naar denkt te vragen aan zijn AI-bouwer. Bijna niemand test het tegenovergestelde scenario: wat er gebeurt als de persoon die betaald krijgt, degene is die niet komt opdagen. Die asymmetrie is precies waar veel door AI gegenereerde bijlesmarkten stilletjes uit elkaar vallen.

## De terugbetalingslogica die elke oprichter van een marktplaats vergeet te testen

Wanneer je een AI-bouwer vraagt ​​om "no-shows af te handelen" voor een tweezijdige boekingsmarktplaats, heeft deze de neiging om de versie te bouwen die de betalende persoon beschermt: een student mist een sessie, wordt gemarkeerd en verliest misschien het recht op restitutie, afhankelijk van de annuleringsperiode. Dat is een redelijke standaard, en het is het scenario dat de meeste oprichters beschrijven als ze de functie specificeren, omdat deze het bedrijfsmodel beschermt: geef geen geld terug aan mensen die de tijd van een docent hebben verspild. Wat die standaard er stilletjes van uitgaat, is dat de *leraar* altijd de betrouwbare partij is. Niets in de meeste prompts specificeert wat er gebeurt als die veronderstelling wordt verbroken.

## Vier no-show-scenario's en het scenario dat iedereen overslaat

Een compleet no-show beleid voor een tweezijdige marktplaats moet eigenlijk vier verschillende gevallen behandelen: de student komt niet opdagen en de docent wordt hoe dan ook betaald (of niet, volgens uw beleid), de docent komt niet opdagen en de student heeft een volledige terugbetaling nodig, beide partijen komen opdagen, maar de sessie wordt afgebroken, en geen van beide partijen komt opdagen en de boeking vervalt gewoon. De meeste door AI gegenereerde implementaties die we hebben beoordeeld, gaan precies met één van deze problemen om: studenten komen niet opdagen, omdat dit de versie is die de oprichter in detail heeft beschreven. Het no-show-pad van de docent ontbreekt volledig of loopt via dezelfde logica als een normale voltooide sessie, wat betekent dat de betaling van de student wordt geregistreerd en vrijgegeven aan de docent alsof de sessie heeft plaatsgevonden, zonder dat er een terugbetalingsmechanisme bestaat.

## Waarom dit een vertrouwens- en retentieprobleem is, en niet alleen een terugbetalingsbug

Een ontbrekend terugbetalingstraject kost u niet alleen één boos supportticket. Op een bijlesmarktplaats is vertrouwen tussen student en platform het hele product: ouders boeken sessies voor hun kinderen, studenten bereiden zich voor op examens met een deadline, volwassenen passen lessen aan volgens een werkschema. Een no-show van een docent die resulteert in een volledige aanklacht zonder verhaal is de snelste manier om van een betalende klant een publieke klacht te maken, en in een markt die nog steeds zijn reputatie opbouwt, kan een handvol van dat soort verhalen zwaarder wegen dan maanden van goede mond-tot-mondreclame. Onze technici hebben meer dan 160 projecten voor zakelijke klanten uitgevoerd, en de les die rechtstreeks wordt overgedragen op de oprichters van de marktplaats is dezelfde die elk product met veel betalingen uiteindelijk leert: de uitzonderingspaden zijn het product, want dat is wat mensen zich herinneren.

## Het opbouwen van restitutielogica die feitelijk beide kanten bestrijkt

Om dit op te lossen, moet de afhandeling van no-shows worden behandeld als een toestandsmachine met een gedefinieerde uitkomst voor elk van de vier bovenstaande scenario's, en niet één enkele "no-show"-vlag die uniform wordt toegepast, ongeacht welke partij de sessie heeft gemist. Het betekent ook dat het no-show-pad van de docent een eigen trigger nodig heeft – idealiter iets dat de student of een beheerder kan bevestigen – dat leidt tot een automatische of versnelde terugbetaling in plaats van de transactie stilzwijgend af te ronden. Ons team, dat werkt vanuit de Singapore-hub van LaunchStudio, bouwt dit als een laag met expliciete regels bovenop uw bestaande Stripe-integratie, zodat de betalingslogica weerspiegelt wat er feitelijk tijdens de sessie is gebeurd in plaats van standaard te veronderstellen dat het goed is gegaan.

U kunt [hier uw project beschrijven](https://launchstudio.eu/en/#contact) en wij zullen binnen één werkdag reageren en vertellen wat uw huidige no-show-logica eigenlijk inhoudt. Voor een idee van hoe Manifera de architectuur van marktplaatsbetalingen breder benadert, zie onze praktijk voor [offshore softwareontwikkeling](https://www.manifera.com/services/offshore-software-development/), die precies dit soort technisch werk ondersteunt.

## Echt voorbeeld

### Een AI-native oprichter in actie: de no-show waar niemand op had gerekend

Sanne Kok, een oprichtster uit Delft, heeft BijlesMatch gebouwd – een online bijlesmarktplaats die studenten verbindt met docenten voor vakspecifieke lessen – met behulp van Lovable. Het boekings- en betalingsproces werkte goed, en het no-showbeleid voor studenten – de student in rekening brengen, geen restitutie als hij te kort voor de sessie annuleert – werd precies zoals gespecificeerd geïmplementeerd.

Het gat kwam naar voren toen een docent eenvoudigweg niet deelnam aan een geplande videosessie. De student was al bij het boeken in rekening gebracht, zoals bedoeld. Maar omdat de no-show-logica van de app alleen een gedefinieerd pad had voor no-shows van studenten, werd de sessie standaard als 'voltooid' gemarkeerd zodra de geplande tijd verstreken was, en werd de betaling zoals normaal vrijgegeven aan de docent. De leerling stuurde Sanne een bericht met de vraag waarom het volledige bedrag in rekening was gebracht voor een les die nooit had plaatsgevonden, en Sanne ontdekte dat er voor dit scenario helemaal geen terugbetalingsmechanisme bestond: geen ontbrekende knop, maar een ontbrekend codepad.

De technici van LaunchStudio hebben de no-show-logica omgebouwd tot vier expliciete uitkomsten die betrekking hebben op no-shows van zowel studenten als docenten. Ze hebben een 'tutor did not show'-rapport aan de studentzijde toegevoegd dat een automatische terugbetalingsblokkering activeert in afwachting van bevestiging, en hebben de timing van de vrijgave van de betaling aangepast, zodat het geld pas aan de docent wordt vrijgegeven totdat de voltooiing van de sessie daadwerkelijk door beide partijen is bevestigd of er een gedefinieerde time-out is verstreken.

**Resultaat:** no-shows van docenten activeren nu een automatisch terugbetalingstraject in plaats van stil te voltooien als een betaalde sessie, waardoor het exacte gat wordt gedicht dat niet was getest.

> *"Ik heb het no-showbeleid vanuit de kant van de student opgebouwd, omdat dat het risico is waar ik me zorgen over wilde maken om het bedrijf tegen te beschermen. Ik heb er nooit aan gedacht om te vragen: wat als het de docent is die afhaakt?"*
> — **Sanne Kok, Oprichter, BijlesMatch (Delft)**

**Kosten en tijdlijn:** € 700 (herbouw van logica voor no-show in vier staten, terugbetalingspad voor no-show bij docent, timing voor vrijgave van betaling) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Waarom behandelen AI-bouwers standaard alleen no-shows van studenten?

Omdat oprichters de no-show-functie doorgaans beschrijven vanuit het perspectief van het beschermen van inkomsten tegen de betalende klant, en de AI precies dat scenario implementeert in plaats van het symmetrische geval aan de andere kant van de markt af te leiden.

### Hoe vaak komt deze kloof voor in tweezijdige marktplaats-apps?

Heel gebruikelijk: elke marktplaats waar de ene kant betaalt en de andere kant een lijndienst levert, heeft vaak dezelfde asymmetrie, of het nu gaat om bijles, coaching, fitnesslessen of adviessessies.

### Wat is er eigenlijk nodig voor een goed opgebouwd no-showbeleid?

Er zijn expliciete, afzonderlijke uitkomsten nodig voor elke combinatie van wie wel en niet is komen opdagen, gekoppeld aan verschillende triggers (annuleringsperioden, no-show-rapporten en op time-outs gebaseerde bevestigingen) in plaats van dat er één enkele vlag op elke zaak wordt toegepast.

### Werkt LaunchStudio alleen met oprichters die al betalende klanten hebben?

Nee – we werken ook met oprichters in de overwegingsfase, waarbij we een prototype beoordelen voordat het echte transactievolume een kloof als deze blootlegt, die vaak goedkoper en sneller is dan het repareren ervan nadat er een backlog in de ondersteuning is opgebouwd.

### Heeft het team van LaunchStudio in Singapore ervaring met marktspecifieke betalingslogica?

Ja, Singapore is LaunchStudio's hub voor Zuidoost-Azië, en de tweezijdige betalings- en terugbetalingsarchitectuur op de markt is een van de meest voorkomende projecttypen die het team daar afhandelt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI builders default to only handling student no-shows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Founders typically describe the no-show feature from the perspective of protecting revenue against the paying customer, and the AI implements exactly that scenario rather than inferring the symmetric case."
      }
    },
    {
      "@type": "Question",
      "name": "How common is this gap in two-sided marketplace apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Very common \u2014 any marketplace where one side pays and the other side delivers a scheduled service tends to have this same asymmetry, whether it's tutoring, coaching, fitness classes, or consulting."
      }
    },
    {
      "@type": "Question",
      "name": "What does a properly built no-show policy actually require?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Explicit, separate outcomes for each combination of who did and didn't show, tied to distinct triggers \u2014 cancellation windows, no-show reports, and timeout-based confirmations."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio only work with founders who already have paying customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No \u2014 LaunchStudio also reviews prototypes at consideration stage before real transaction volume exposes gaps like this one, often cheaper than fixing it after a support backlog builds up."
      }
    },
    {
      "@type": "Question",
      "name": "Is LaunchStudio's Singapore team experienced with marketplace-specific payment logic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes \u2014 Singapore is LaunchStudio's Southeast Asia hub, and two-sided marketplace payment and refund architecture is one of the most frequent project types the team there handles."
      }
    }
  ]
}
</script>