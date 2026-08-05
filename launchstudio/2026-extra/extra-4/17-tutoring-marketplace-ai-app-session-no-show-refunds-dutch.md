---
Titel: "AI-bijlesmarktplaatsen: Niet-verschenen sessies breken de terugbetalingslogica die niemand testte"
Trefwoorden: ai saas, two-sided marketplace, tutoring marketplace app, no-show refund logic, ai-generated code
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---

# AI-bijlesmarktplaatsen: Niet-verschenen sessies breken de terugbetalingslogica die niemand testte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-bijlesmarktplaatsen: Niet-verschenen sessies breken de terugbetalingslogica die niemand testte",
  "description": "Met AI gebouwde bijlesmarktplaatsen verwerken doorgaans de afwezige student en vergeten stilletjes de afwezige bijlesgever.",
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

Iedereen test het ideale pad. Iedereen denkt er ook aan om te testen wat er gebeurt wanneer de klant niet opkomt – dat is het voor de hand liggende randgeval, degene waar elke marktplaats-oprichter aan denkt om aan zijn AI-bouwer te vragen. Vrijwel niemand test het tegenovergestelde scenario: wat er gebeurt wanneer de persoon die betaald krijgt degene is die niet verschijnt. Die asymmetrie is exact waar veel met AI gegenereerde bijlesmarktplaatsen stilletjes uit elkaar vallen.

## De terugbetalingslogica die elke marktplaats-oprichter vergeet te testen

Wanneer u een AI-bouwer vraagt om "niet-verschijnen af te handelen" voor een tweezijdige boekingsmarktplaats, heeft deze de neiging om de versie te bouwen die de persoon die betaalt beschermt – een student mist een sessie, wordt gemarkeerd, verliest misschien de geschiktheid voor een terugbetaling afhankelijk van het annuleringstijdvenster. Dat is een redelijke standaard, en het is het scenario dat de meeste oprichters beschrijven wanneer ze de functie specificeren, omdat het degene is die het bedrijfsmodel beschermt: betaal geen mensen terug die de tijd van een bijlesgever hebben verspild. Wat die standaard stilletjes aanneemt, is dat de *bijlesgever* altijd de betrouwbare partij is. Niets in de meeste prompts specificeert wat er gebeurt wanneer die aanname breekt.

## Vier niet-verschijn-scenario's, en degene die iedereen overslaat

Een compleet beleid voor niet-verschijnen voor een tweezijdige marktplaats moet daadwerkelijk vier afzonderlijke gevallen afhandelen: de student verschijnt niet en de bijlesgever wordt evengoed betaald (of niet, volgens uw beleid), de bijlesgever verschijnt niet en de student heeft een volledige terugbetaling nodig, beide partijen verschijnen maar de sessie wordt voortijdig afgebroken, en geen van beide partijen verschijnt en de boeking vervalt simpelweg. De meeste met AI gegenereerde implementaties die we hebben beoordeeld handelen exact één hiervan strak af – de afwezige student – omdat het de versie is die de oprichter in detail heeft beschreven. Het pad van de afwezige bijlesgever ontbreekt óf volledig óf loopt via dezelfde logica als een normale voltooide sessie, wat betekent dat de betaling van de student wordt vastgelegd en vrijgegeven aan de bijlesgever alsof de sessie heeft plaatsgevonden, zonder enig terugbetalingsmechanisme.

## Waarom dit een vertrouwens- en retentieprobleem is, en niet alleen een terugbetalingsbug

Een ontbrekend terugbetalingspad kost u niet alleen één boos ondersteuningsticket. In een bijlesmarktplaats is vertrouwen tussen student en platform het gehele product – ouders die sessies boeken voor hun kinderen, studenten die zich voorbereiden op examens met een strakke deadline, volwassenen die lessen inpassen rond een werkschema. Een niet-verschijnende bijlesgever die resulteert in een volledige afschrijving zonder verhaal is de snelste manier om een betalende klant te veranderen in een openbare klacht. In een marktplaats die zijn reputatie nog opbouwt, kan een handvol van dat soort verhalen opwegen tegen maanden van goede mond-tot-mondreclame. Onze ingenieurs hebben 160+ projecten geleverd voor enterprise-klanten. De les die rechtstreeks overgaat op marktplaats-oprichters is dezelfde die elk betalingszwaar product uiteindelijk leert: de uitzonderingspaden *zijn* het product, want dat is wat mensen zich herinneren.

## Het bouwen van terugbetalingslogica die daadwerkelijk beide kanten dekt

Het op de juiste manier herstellen hiervan betekent het behandelen van de afhandeling van niet-verschijnen als een statusmachine met een gedefinieerde uitkomst voor elk van de vier bovenstaande scenario's, en niet als een enkele "niet-verschenen"-markering die uniform wordt toegepast ongeacht welke partij de sessie heeft gemist. Het betekent ook dat het pad voor de afwezige bijlesgever een eigen trigger nodig heeft – idealiter iets wat de student of een beheerder kan bevestigen – die leidt naar een automatische of versnelde terugbetaling, in plaats van de transactie stilletjes te voltooien. Ons team, werkend vanuit LaunchStudio's hub in Singapore, bouwt dit als een expliciete regellaag die bovenop uw bestaande Stripe-integratie zit. Zo weerspiegelt de betalingslogica wat er daadwerkelijk is gebeurd in de sessie, in plaats van standaard aan te nemen "het ging vast goed".

U kunt [uw project hier beschrijven](https://launchstudio.eu/en/#contact) en we reageren binnen één werkdag met een inschatting van wat uw huidige logica voor niet-verschijnen daadwerkelijk dekt. Voor een gevoel van hoe Manifera de betalingsarchitectuur op marktplaatsen breder benadert, bekijk onze [offshore softwareontwikkelingspraktijk](https://www.manifera.com/services/offshore-software-development/), die exact dit soort omvattend engineeringwerk ondersteunt.

## Twee triggers, één terugbetaling: Het vermijden van een dubbele terugbetalingsrace

Het herstellen van de kloof van de afwezige bijlesgever betekent doorgaans het toevoegen van twee onafhankelijke manieren om een terugbetaling te triggeren: een door de student ingediend rapport "bijlesgever niet verschenen", en een automatische time-out die afgaat als er binnen een ingesteld venster geen bevestiging van de sessiestart binnenkomt van een van beide kanten. Onzorgvuldig gebouwd weten die twee triggers niet van elkaar. Een student meldt het niet-verschijnen in minuut zes, en de automatische time-out – ruim bemeten om een bijlesgever die gewoon een paar minuten te laat is niet te straffen – vuurt in minuut tien evengoed af, omdat niets heeft gecontroleerd of er al een terugbetaling was uitgevoerd. Het resultaat is dat dezelfde boeking twee keer wordt terugbetaald, één keer door elke trigger. Dat is een erger resultaat dan de oorspronkelijke bug: in plaats van een boze student die een terugbetaling eist die u hem verschuldigd bent, heeft u een verward financieel rapport en geld dat twee keer is vertrokken voor een sessie die slechts één keer niet is doorgegaan.

De oplossing heeft dezelfde vorm als elk dubbel-trigger-probleem: controleer de terugbetalingsstatus van de boeking voordat een van beide triggers mag handelen, en maak de trigger die het eerst afgaat degene die wint.

```
function processNoShowRefund(bookingId, trigger) {
  const booking = getBooking(bookingId);
  if (booking.refundStatus !== 'none') {
    return booking; // al terugbetaald door de andere trigger, doe niets
  }
  markRefundStatus(bookingId, 'processing', trigger);
  issueRefund(booking);
  markRefundStatus(bookingId, 'completed', trigger);
}
```

Dit doet er het meest toe exact wanneer het het minst zichtbaar is – een studentenrapport en een automatische time-out die binnen enkele seconden na elkaar landen is geen zeldzame toevalstreffer, het is het verwachte gedrag van een systeem waar beide triggers dezelfde sessie in de gaten houden voor dezelfde fout.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het niet-verschijnen waar niemand op had geregeld

Sanne Kok, een oprichter in Delft, bouwde BijlesMatch – een online bijlesmarktplaats die studenten verbindt met bijlesgevers voor vakspecifieke lessen – met behulp van Lovable. De boekings- en betalingsstroom werkte goed, en het beleid voor afwezige studenten – belast de student, geen terugbetaling, als ze te dicht op de sessie annuleren – werd exact zoals gespecificeerd geïmplementeerd.

De kloof kwam naar boven toen een bijlesgever simpelweg niet deelnam aan een geplande videosessie. De student was al belast bij het boeken, zoals ontworpen. Maar omdat de logica voor niet-verschijnen in de app alleen een gedefinieerd pad had voor afwezige studenten, werd de sessie standaard als "voltooid" gemarkeerd zodra de geplande tijd verstreek. De betaling werd zoals normaal vrijgegeven aan de bijlesgever. De student stuurde Sanne rechtstreeks een bericht met de vraag waarom hij volledig was belast voor een les die nooit had plaatsgevonden. Sanne ontdekte dat er voor dit scenario helemaal geen terugbetalingsmechanisme was – niet een ontbrekende knop, maar een ontbrekend codepad.

LaunchStudio's ingenieurs herbouwden de logica voor niet-verschijnen naar vier expliciete uitkomsten voor zowel afwezige studenten als afwezige bijlesgevers. Ze voegden een rapport "bijlesgever niet verschenen" aan de studentenzijde toe dat een automatische terugbetalingsstop activeert in afwachting van bevestiging, en pasten de timing voor betalingsvrijgave aan zodat fondsen niet worden vrijgegeven aan de bijlesgever totdat de voltooiing van de sessie daadwerkelijk door beide kanten wordt bevestigd of een gedefinieerde time-out verstrijkt.

**Resultaat:** niet-verschijnende bijlesgevers triggeren nu een automatisch terugbetalingspad in plaats van stilletjes te voltooien als een betaalde sessie, wat de exacte kloof dicht die ongetest was gebleven.

> *"Ik bouwde het beleid voor niet-verschijnen vanaf de kant van de student omdat dat het risico was waar ik me zorgen over maakte om het bedrijf te beschermen. Ik heb er nooit één keer aan gedacht om te vragen: wat als de bijlesgever degene is die afhaakt?"*
> — **Sanne Kok, Oprichter, BijlesMatch (Delft)**

**Kosten en tijdlijn:** € 700 (herbouw van logica voor niet-verschijnen met vier statussen, terugbetalingspad bij afwezige bijlesgever, herstelling van timing betalingsvrijgave) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Waarom verwerken AI-bouwers standaard alleen afwezige studenten?

Omdat oprichters de functie voor niet-verschijnen doorgaans beschrijven vanuit het perspectief van het beschermen van inkomsten tegen de betalende klant. De AI implementeert exact dat scenario in plaats van het symmetrische geval aan de andere kant van de marktplaats af te leiden.

### Hoe vaak komt deze kloof voor in tweezijdige marktplaats-apps?

Zeer vaak – elke marktplaats waar de ene kant betaalt en de andere kant een geplande dienst levert, heeft de neiging om dezelfde asymmetrie te hebben, of het nu gaat om bijles, coaching, fitnesslessen of adviesgesprekken.

### Wat vereist een goed gebouwd beleid voor niet-verschijnen daadwerkelijk?

Het heeft expliciete, afzonderlijke uitkomsten nodig voor elke combinatie van wie wel en niet verscheen, gekoppeld aan afzonderlijke triggers – annuleringstijdvensters, meldingen van niet-verschijnen en op time-out gebaseerde bevestigingen – in plaats van een enkele markering die op elk geval wordt toegepast.

### Werkt LaunchStudio alleen met oprichters die al betalende klanten hebben?

Nee – we werken ook met oprichters in de overwegingsfase, waarbij we een prototype beoordelen voordat een echt transactievolume een kloof zoals deze blootlegt. Dat is vaak goedkoper en sneller dan het herstellen ervan nadat er een achterstand aan ondersteuningsverzoeken is opgebouwd.

### Is LaunchStudio's team in Singapore ervaren met marktplaatsspecifieke betalingslogica?

Ja – Singapore is LaunchStudio's hub voor Zuidoost-Azië, en betalings- en terugbetalingsarchitectuur voor tweezijdige marktplaatsen is een van de meest frequent voorkomende projecttypes die het team daar afhandelt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom bouwen AI-tools standaard alleen no-show logica voor de student?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat oprichters het risico van omzetverlies door de klant beschrijven, en AI niet automatisch de omgekeerde situatie bedenkt."
      }
    },
    {
      "@type": "Question",
      "name": "Komt dit probleem vaak voor bij tweezijdige marktplaatsen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, heel vaak bij platforms waar de ene kant betaalt en de andere kant op afspraak levert (coaching, bijles, training)."
      }
    },
    {
      "@type": "Question",
      "name": "Wat vereist een robuust no-show beleid in de code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vier expliciete scenario's (student afwezig, docent afwezig, beide afwezig, voortijdig gestopt) met eigen triggers en regels."
      }
    },
    {
      "@type": "Question",
      "name": "Werkt LaunchStudio ook met prototypes voordat er al klanten zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, we beoordelen prototypes in de ontwikkelfase om betalings- en terugbetalingslekken vóór de lancering te dichten."
      }
    },
    {
      "@type": "Question",
      "name": "Wat voorkomt dat een no-show donatie 2x wordt terugbetaald?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een check op de huidige refundStatus vóór actie: de eerste trigger voert uit, de tweede ziet de status en stopt."
      }
    }
  ]
}
</script>