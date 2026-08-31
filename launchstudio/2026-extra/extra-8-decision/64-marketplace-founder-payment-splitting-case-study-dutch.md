---
Titel: "Case Study: Een Marketplace-Oprichter Regelt Betalingssplitsing In Één Keer Goed"
Trefwoorden: marketplace betalingssplitsing, Stripe Connect marketplace, meerpartijenbetalingen SaaS, platform betalingsverwerking, compliance betalingssplitsing, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Oprichter Scale-Up
---

# Case Study: Een Marketplace-Oprichter Regelt Betalingssplitsing In Één Keer Goed

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een Marketplace-Oprichter Regelt Betalingssplitsing In Één Keer Goed",
  "description": "Een marketplace-oprichter in Amersfoort had betalingssplitsing nodig - kopers betalen, verkopers ontvangen, het platform houdt een percentage. Stripe Connect regelt dit, maar de implementatie is geen kwestie van één druk op de knop. Dit is hoe LaunchStudio het in één keer goed kreeg, voordat er ook maar één echte euro werd verwerkt.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/marketplace-founder-payment-splitting-case-study"
  }
}
</script>

Marketplace-betalingen zijn een heel ander beestje dan SaaS-abonnementen. Bij een SaaS-product betaalt één partij u en houdt u het geld — een rechte lijn. Bij een marketplace betaalt een koper, ontvangt een verkoper, en houdt het platform een percentage — een driehoek, met belastingverplichtingen, uitbetalingsschema's, identiteitsverificatie-eisen en terugbetalingsbeleid dat verschilt afhankelijk van in welke hoek van de driehoek u staat. Joris Kuipers ontdekte deze structurele complexiteit drie weken nadat hij begon met het bouwen van HulpMarkt, een door Lovable gebouwd platform dat Nederlandse huiseigenaren verbindt met lokale klussers voor kleine reparatieklussen, toen hij besefte dat "betalingen toevoegen" niet betekende dat hij een betaalknop moest toevoegen — het betekende het ontwerpen van een driepartijen-financiële flow met compliance-eisen die hij nog nooit was tegengekomen.

## De Oprichter

Joris Kuipers, voormalig vastgoedbeheerder in Amersfoort, kende de markt voor kleine reparaties tot in de details. Huiseigenaren hadden iemand nodig om een lekkende kraan te repareren, een zware spiegel op te hangen, of een gebroken tegel te vervangen — klussen te klein voor een erkende aannemer maar te lastig voor de meeste mensen om zelf te doen. Lokale klussers wilden deze klussen wel, maar hadden geen efficiënte manier om ze te vinden. HulpMarkt was de matchmaker: huiseigenaren plaatsten klussen, klussers boden erop, en het platform hield 12% servicekosten in op de uitbetaling van de klusser.

## Het Probleem

Joris had de marketplace-frontend gebouwd in Lovable — klusaanbiedingen, biedingen, berichten, profielpagina's, reviews — en als demo werkte het prachtig. De betalingsvraag leek eenvoudig: koper betaalt voor de klus, platform houdt 12%, klusser ontvangt 88%. Stripe regelt marketplace-betalingen. Klaar.

Behalve dat Stripe Connect, het product dat precies voor dit gebruik is ontworpen, drie verschillende integratiemodellen heeft (Standard, Express en Custom), elk met andere onboarding-eisen, uitbetalingstermijnen en platformverantwoordelijkheden. De verkeerde keuze zou klussers ofwel volledige Stripe-accounts zelf laten aanmaken (Standard — hoge drempel, velen zouden afhaken), het platform te weinig controle geven over de uitbetalingservaring (Express — beperkte aanpasbaarheid), of Joris opzadelen met compliance-verplichtingen waar hij niet op was toegerust (Custom — het platform wordt verantwoordelijk voor identiteitsverificatie, belastingrapportage en geschillenbeheer).

Daarnaast had de betalingsflow van HulpMarkt een timingcomplicatie: de koper moest betalen bij het accepteren van een bod, maar de klusser mocht pas worden uitbetaald nadat de klus als voltooid was gemarkeerd en de huiseigenaar tevredenheid had bevestigd — een escrow-achtige blokkering die Stripe ondersteunt via uitgestelde uitbetalingen, maar die specifieke API-configuratie en zorgvuldig statusbeheer vereist tussen de levenscyclus van de klus en die van de betaling.

## Wat LaunchStudio Deed

Het Manifera-engineeringteam, voortbouwend op ervaring met meerpartijenbetalingsflows uit enterprise marketplace-projecten, structureerde het traject rond drie beslissingen en hun implementaties:

**Connected Account-model:** Express-accounts — de juiste balans voor het gebruiksscenario van HulpMarkt. Klussers doorlopen een gestroomlijnde onboardingflow (identiteitsverificatie wordt door Stripe afgehandeld, niet door het platform), en het platform behoudt controle over de uitbetalingstiming zonder de compliance-verantwoordelijkheden van het Custom-niveau op zich te nemen. LaunchStudio implementeerde de Express-onboardingflow als een naadloze stap in het registratieproces van klussers.

**Betalingsflow met escrow-blokkering:** Wanneer een huiseigenaar een bod accepteert, wordt een Payment Intent aangemaakt met een `application_fee_amount` die HulpMarkts 12% vertegenwoordigt en een `transfer_data[destination]` die verwijst naar het connected account van de klusser. De betaling wordt onmiddellijk geïnd (geld verlaat de kaart van de huiseigenaar), maar de overdracht naar het account van de klusser wordt uitgesteld tot de klus als voltooid is gemarkeerd. Als de huiseigenaar een probleem meldt, kan het platform de betaling vasthouden of terugbetalen zonder dat de klusser het geld al heeft ontvangen.

**Uitbetalings- en terugbetalingslogica:** Na voltooiing van de klus wordt de overdracht naar het connected account van de klusser automatisch geactiveerd. Het uitbetalingsschema van Stripe regelt vervolgens het overmaken van geld van het connected account naar de bankrekening van de klusser. Voor geschillen en terugbetalingen behandelt het systeem drie scenario's: volledige terugbetaling (klus niet voltooid), gedeeltelijke terugbetaling (klus voltooid maar met problemen — het platform bemiddelt), en terugbetaling na uitbetaling (het platform dekt de terugbetaling uit eigen saldo en verrekent dit met de volgende uitbetaling van de klusser).

## Het Resultaat

HulpMarkt lanceerde met een betalingsflow die de volledige driehoek afhandelde — koperbetalingen, platformkosten, verkoperuitbetalingen, escrow-blokkeringen en terugbetalingsscenario's — vanaf dag één. De onboardingflow voor klussers (Stripe Express) duurde gemiddeld 4 minuten, met een voltooiingspercentage van 91%. In de eerste twee maanden verwerkte het platform €23.400 aan klusbetalingen, inde €2.808 aan platformkosten, en handelde drie terugbetalingsscenario's af (twee volledige, één gedeeltelijke) zonder handmatige tussenkomst.

> *"Ik dacht dat 'Stripe toevoegen' een middagje werk zou zijn. De marketplace-betalingsflow — escrow, splitsingen, terugbetalingen, identiteitsverificatie — was het meest complexe onderdeel van mijn hele product, en ik had geen idee totdat ik het probeerde te bouwen."*
> — **Joris Kuipers, Oprichter, HulpMarkt (Amersfoort)**

**Kosten & Doorlooptijd:** €3.400 (Launch & Grow Pakket, Stripe Connect Express-integratie + escrow-flow + terugbetalingsafhandeling + onboarding klussers) — live in 13 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) bouwt marketplace-betalingsflows die de volledige driehoek afhandelen — niet alleen de betaling, maar ook de splitsing, de blokkering, de uitbetaling en de terugbetaling — ondersteund door Manifera's ervaring met enterprise meerpartijen-financiële systemen.

[Beschrijf uw marketplace en hoe het geld tussen de partijen moet stromen](https://launchstudio.eu/nl/#contact) — de betalingsarchitectuur is meestal het lastigste onderdeel, en het is beter om dit goed te regelen vóór uw eerste echte transactie.

---

## Veelgestelde Vragen

### Heb ik Stripe Connect nodig, of kan ik marketplace-betalingen met een gewoon Stripe-account afhandelen?

Voor een echte marketplace waarbij kopers betalen en verkopers ontvangen, is Stripe Connect de juiste infrastructuur. Een gewoon Stripe-account handelt alleen betalingen aan één entiteit af (uzelf), waardoor correcte betalingssplitsing en verkoperuitbetalingen ofwel onmogelijk zijn ofwel niet compliant.

### Hoe lang duurt het voor een verkoper om de Stripe Express-onboarding te voltooien?

Doorgaans 3-5 minuten — de verkoper geeft basale identiteitsinformatie op, Stripe handelt verificatie op de achtergrond af, en de meeste accounts zijn binnen enkele minuten actief. Het conversiepercentage ligt aanzienlijk hoger dan bij Standard-accounts, waarbij verkopers volledige Stripe-dashboards moeten aanmaken.

### Wat gebeurt er als een koper een betaling betwist nadat de verkoper al is uitbetaald?

LaunchStudio configureert het platform om geschillen te dekken uit het eigen saldo en het bedrag terug te vorderen bij de volgende uitbetaling van de verkoper — een standaard marketplace-praktijk die voorkomt dat de koper zonder verhaal komt te zitten en het platform een duidelijk escalatiepad geeft.

### Kan ik Mollie gebruiken in plaats van Stripe voor marketplace-betalingssplitsing?

Mollie ondersteunt meerpartijenbetalingen via de Connect-functie, maar het implementatiemodel verschilt van Stripe Connect. Het Manifera-team van LaunchStudio kan beide implementeren, afhankelijk van of de marketplace vooral Nederlandse klanten bedient (Mollie's iDEAL-ondersteuning is sterker) of internationale klanten (Stripe's wereldwijde dekking is breder).

### Welk platformpercentage is gebruikelijk voor een tweezijdige marketplace?

Platformkosten variëren sterk — van 5% voor diensten met een hoog ticket tot 30% voor laagdrempelig gig-werk — en het juiste percentage hangt af van uw markt, concurrentie en de waarde die het platform biedt. De betalingsinfrastructuur ondersteunt elk percentage; de bedrijfsbeslissing is aan u.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik Stripe Connect nodig, of kan ik marketplace-betalingen met een gewoon Stripe-account afhandelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een echte marketplace waarbij kopers betalen en verkopers ontvangen, is Stripe Connect de juiste infrastructuur. Een gewoon Stripe-account handelt alleen betalingen aan één entiteit af, waardoor correcte betalingssplitsing ofwel onmogelijk is ofwel niet compliant."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het voor een verkoper om de Stripe Express-onboarding te voltooien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Doorgaans 3-5 minuten - de verkoper geeft basale identiteitsinformatie op, Stripe handelt verificatie op de achtergrond af, en de meeste accounts zijn binnen enkele minuten actief."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een koper een betaling betwist nadat de verkoper al is uitbetaald?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio configureert het platform om geschillen te dekken uit het eigen saldo en het bedrag terug te vorderen bij de volgende uitbetaling van de verkoper - een standaard marketplace-praktijk die voorkomt dat de koper zonder verhaal komt te zitten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik Mollie gebruiken in plaats van Stripe voor marketplace-betalingssplitsing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mollie ondersteunt meerpartijenbetalingen via de Connect-functie. LaunchStudio kan beide implementeren, afhankelijk van of de marketplace vooral Nederlandse klanten bedient of internationale klanten."
      }
    },
    {
      "@type": "Question",
      "name": "Welk platformpercentage is gebruikelijk voor een tweezijdige marketplace?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Platformkosten variëren van 5% voor diensten met een hoog ticket tot 30% voor laagdrempelig gig-werk. De betalingsinfrastructuur ondersteunt elk percentage; de bedrijfsbeslissing is aan u."
      }
    }
  ]
}
</script>
