---
Titel: "Prototype AI: een verklarende woordenlijst voor oprichters voordat u met een engineer praat"
Trefwoorden: prototype ai, ai prototype, ai native, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---

# Prototype AI: een verklarende woordenlijst voor oprichters voordat u met een engineer praat

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Prototype AI: een verklarende woordenlijst voor oprichters voordat u met een engineer praat",
  "description": "Een korte, eenvoudig geformuleerde verklarende woordenlijst van de termen die een engineer zal gebruiken wanneer hij uw prototype AI voor het eerst met u bespreekt — geschreven zodat u het gesprek kunt volgen en scherpere vragen kunt stellen, niet zodat u zelf technisch hoeft te worden.",
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
  "datePublished": "2026-07-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/prototype-ai-founders-glossary-before-talking-engineer"
  }
}
</script>

Het eerste echte gesprek tussen een niet-technische oprichter en een engineer die hun prototype AI beoordeelt, verliest vaak in de eerste vijf minuten aan momentum, niet omdat de oprichter niets waardevols heeft bij te dragen, maar omdat de woordenschat van de engineer – voor hen volkomen normaal – binnenkomt als een onbekende muur van termen die niemand pauzeerde om te vertalen. Deze woordenlijst bestaat specifiek om die wrijving weg te nemen, niet om u technisch te maken, maar net bedreven genoeg om te volgen en scherpere vragen te stellen.

## Frontend / Backend

De frontend is alles wat u en uw gebruikers daadwerkelijk zien en aanklikken – schermen, knoppen, formulieren. De backend is alles wat op een server draait, onzichtbaar voor u, dat gegevens, logica en beveiliging afhandelt. De meeste hiaten die een engineer zal beschrijven bevinden zich in de backend, precies omdat het het deel is dat een oprichter nooit rechtstreeks ziet en daarom geen natuurlijke manier heeft om het zelf te controleren.

## Authenticatie vs. Autorisatie

Authenticatie beantwoordt "wie bent u" – succesvol inloggen. Autorisatie beantwoordt "wat mag u doen" zodra u bent ingelogd. Een engineer die zegt dat uw autorisatie zwak is, zegt niet dat uw inlogscherm kapot is; ze zeggen dat het systeem niet correct controleert wat een ingelogde persoon daadwerkelijk mag zien of doen als hij eenmaal binnen is.

## API

Kort voor application programming interface – zie het als de specifieke, gestructureerde manier waarop uw frontend uw backend om iets vraagt, of de manier waarop uw product een externe dienst (zoals een AI-modelaanbieder) om iets vraagt. Wanneer een engineer zegt "we hebben de API rechtstreeks getest", bedoelen ze dat ze uw zichtbare interface hebben omzeild en met de backend hebben gesproken op de manier waarop een technisch bekwaam persoon dat zou kunnen.

## Omgevingsvariabelen / Geheimen (Environment Variables / Secrets)

Wachtwoorden en toegangssleutels die uw product nodig heeft om met andere diensten te spreken – een betalingsverwerker, een e-mailaanbieder, een AI-model. Deze moeten in een veilige, afzonderlijke configuratie leven, nooit rechtstreeks in uw zichtbare code. Wanneer een engineer vraagt naar "beheer van geheimen", vragen ze of deze correct zijn opgeslagen.

## Productie vs. Staging vs. Ontwikkeling (Development)

Ontwikkeling is waar u en uw AI-tool actief aan het bouwen zijn. Staging, als het bestaat, is een kopie die wordt gebruikt om wijzigingen veilig te testen voordat ze live gaan. Productie is de echte, live versie die echte klanten daadwerkelijk gebruiken. Een engineer die onderscheid maakt tussen deze drie zorgt ervoor dat een wijziging ergens veilig wordt getest voordat deze uw daadwerkelijke klanten bereikt.

## Implementatie (Deployment)

De handeling van het nemen van een versie van uw code en deze daadwerkelijk live laten draaien, bereikbaar voor echte gebruikers op internet. "Implementeren" is niet hetzelfde als "de code is geschreven" – code kan klaar zijn en nooit worden geïmplementeerd, of geïmplementeerd worden en nog steeds ernstige problemen hebben waar niemand nog naar heeft gekeken.

## Databaseschema

De structuur die beschrijft hoe de gegevens van uw product zijn georganiseerd – welke informatie wordt opgeslagen en hoe verschillende stukken gegevens zich tot elkaar verhouden. Wanneer een engineer uw "schema" beoordeelt, controleren ze of die structuur daadwerkelijk kan ondersteunen wat uw product moet doen, inclusief dingen zoals het schoon verwijderen van de gegevens van een specifieke gebruiker indien nodig.

## Waarom het kennen van deze termen het gesprek verandert, niet de uitkomst

Niets uit deze woordenlijst maakt u in staat om zelf code te schrijven of te beoordelen, en dat is ook niet het punt. Het is het verschil tussen een engineer die een bevinding aan u uitlegt in vertaalde, vereenvoudigde termen omdat het moet, versus u die de oorspronkelijke uitleg rechtstreeks volgt en een oprecht geïnformeerde vervolgvraag stelt, wat aan beide kanten leidt tot een sneller, nauwkeuriger gesprek.

[LaunchStudio](https://launchstudio.eu/en/) bouwt haar gesprekken met oprichters specifiek rond deze woordenschat, waarbij technische bevindingen worden vertaald naar taal die een niet-technische oprichter oprecht kan volgen in plaats van uit te gaan van eerdere vaardigheid, een aanpak gevormd door Manifera's eigen ervaring met het uitleggen van technische beslissingen op enterprise-niveau aan niet-technische belanghebbenden bij meer dan 160 geleverde projecten.

[Breng uw prototype AI naar een gesprek dat u daadwerkelijk kunt volgen](https://launchstudio.eu/en/#contact) — het begrijpen van de woordenschat verandert hoe nuttig het gesprek is, onmiddellijk.

## Nog vijf termen die u zult horen zodra het gesprek technisch wordt

De bovenstaande woordenlijst behandelt wat er in bijna elk eerste gesprek naar voren komt. Een tweede, kortere reeks termen komt vaak naar voren zodra dat gesprek verschuift van "is dit klaar" naar "hier is specifiek wat er gerepareerd moet worden" – handig om bij de hand te hebben voordat ze koud naar voren komen.

## Snelheidsbeperking (Rate Limiting)

Een bewuste limiet op hoe vaak iets – een inlogpoging, een API-aanroep, een formulierverzending – in een bepaalde periode kan plaatsvinden. Zonder dit houdt niets een enkele gebruiker, een mislukte integratie of een aanvaller tegen om duizenden keren achter elkaar hetzelfde verzoek te doen. Wanneer een engineer zegt dat een functie "geen snelheidsbeperking heeft", bedoelen ze dat er momenteel geen plafond is op hoe hard het kan worden getroffen, per ongeluk of met opzet.

## Idempotentie (Idempotency)

Eén eigenschap van een actie die betekent dat deze hetzelfde resultaat produceert, ongeacht hoe vaak deze per ongeluk wordt herhaald. Een betalingsbevestiging die idempotent is, brengt een klant één keer kosten in rekening, zelfs als de bevestiging twee keer aankomt vanwege een netwerkpoging; een die dat niet is, kan hen twee keer kosten in rekening brengen. Wanneer een engineer iets markeert als "niet idempotent", bedoelen ze dat het herhalen van die specifieke actie momenteel niet veilig is.

## Webhook

Een manier voor het ene systeem om automatisch een ander systeem op de hoogte te stellen op het moment dat er iets gebeurt, in plaats van dat het tweede systeem herhaaldelijk moet vragen "is er al iets gebeurd". Een betalingsverwerker gebruikt doorgaans een webhook om uw app het moment te vertellen dat een betaling slaagt. Wanneer een engineer "webhook-afhandeling" bespreekt, bedoelen ze hoe uw product reageert op deze automatische meldingen, inclusief wat er gebeurt als er een twee keer aankomt of buiten de volgorde aankomt.

## Rolgebaseerd toegangsbeheer (RBAC)

Een systeem voor het verlenen van verschillende niveaus van toegang aan verschillende mensen op basis van hun rol, in plaats van dat iedereen dezelfde toegang heeft of dat toegang informeel wordt bijgehouden. Wanneer een engineer zegt dat uw product "nog geen echte RBAC heeft", bedoelen ze dat machtigingsniveaus ofwel niet bestaan als een afzonderlijk concept in het systeem, ofwel in naam bestaan maar niet overal consistent worden afgedwongen waar ze zouden moeten.

## Belastingtesten / Gelijktijdigheid (Load Testing / Concurrency)

Belastingtesten betekent opzettelijk het simuleren van veel gebruikers of verzoeken die uw product tegelijkertijd raken, om te zien hoe het zich daadwerkelijk gedraagt onder realistische druk in plaats van het lichte gebruik dat de eigen testen van een oprichter doorgaans inhouden. Gelijktijdigheid (concurrency) verwijst specifiek naar meerdere dingen die tegelijkertijd gebeuren – twee gebruikers die bijvoorbeeld hetzelfde record tegelijkertijd bewerken. Wanneer een engineer vraagt of iets is "getest onder gelijktijdigheid", vragen ze of het is gecontroleerd tegen dat specifieke, gemakkelijk te missen scenario.

## Echt voorbeeld

### Een AI-native oprichter in actie: een woordenlijst die veranderde hoe een oprichter vragen stelde

Nadia, een voormalig evenementencoördinator die oprichter werd in Leiden, bouwde EventCheck, een prototype AI-tool voor kleine evenementenlocaties om gastenlijsten te verifiëren en inchecken te beheren, met behulp van Bolt, en had zich consequent verloren gefeld tijdens eerdere gesprekken met een freelancer, waarbij ze meeknikte met termen die ze eigenlijk niet begreep.

Voorafgaand aan haar eerste oriëntatiegesprek met LaunchStudio heeft Nadia specifiek een woordenlijst zoals deze bekeken, en het verschil in het daadwerkelijke gesprek was onmiddellijk – toen de beoordelende engineer opmerkte dat de "autorisatie" van EventCheck alleen op de frontend zat, begreep Nadia precies wat dat betekende en stelde ze een directe, specifieke vervolgvraag over of gastgegevens specifiek waren getroffen, in plaats van simpelweg akkoord te gaan en verder te gaan.

**Resultaat:** Door het nauwkeurigere gesprek kon LaunchStudio de daadwerkelijke opdracht van EventCheck sneller en nauwkeuriger scopen bij het eerste gesprek, aangezien Nadia rechtstreeks kon bevestigen welke van de specifieke functies van haar product gevoelige gastgegevens raakten en welke niet.

> *"Ik knikte vroeger gewoon mee in deze gesprekken in de hoop dat het uiteindelijk logisch zou worden. Het vooraf daadwerkelijk kennen van termen als 'autorisatie' en 'backend' betekende dat ik de ene vervolgvraag kon stellen die er echt toe deed."*
> — **Nadia Verschuur, Oprichter, EventCheck (Leiden)**

**Kosten en tijdlijn:** € 1.400 (Launch Ready Pakket, verharding van toegang tot gastgegevens) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Moet ik deze woordenlijst uit mijn hoofd leren, of is het prima om er tijdens een gesprek naar terug te verwijzen?

Terugverwijzen is volkomen prima – het doel is om een realtime gesprek met meer vertrouwen te volgen, niet om te slagen voor een woordenschat-test, en geen enkele engineer die het waard is om mee te werken zal verwachten dat een niet-technische oprichter elke term vooraf uit het hoofd kent.

### Zal het leren van deze termen me uiteindelijk in staat stellen technische werkzaamheden zelf te evalueren?

Niet volledig – deze woordenschat helpt u een gesprek betekenisvol te volgen en erin mee te praten, maar het evalueren of een specifieke technische claim daadwerkelijk waar is vereist over het algemeen nog steeds technische vaardigheid of een vertrouwde beoordelaar.

### Is het redelijk om een engineer te vragen een term die hij gebruikt en die niet in deze woordenlijst staat te definiëren?

Volkomen redelijk, en een goede engineer moet bereid zijn om elk begrip ter plekke te definiëren zonder de vraag te behandelen als een teken van onbekwaamheid.

### Hoe heeft Nadia's verbeterde woordenschat de uitkomst van haar opdracht daadwerkelijk veranderd?

Het zorgde ervoor dat het scopingsproces op het eerste gesprek sneller en nauwkeuriger kon verlopen, aangezien Nadia rechtstreeks kon bevestigen welke functies gevoelige gegevens raakten.

### Zijn er nog andere termen uit de woordenlijst die het waard zijn om te leren buiten de hier behandelde termen?

Dit omvat de termen die het meest consistent naar voren komen in vroege productiegereedheidsgesprekken; meer gespecialiseerde termen komen van nature naar voren naarmate een specifieke opdracht vordert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik deze woordenlijst uit mijn hoofd leren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Terugverwijzen is volkomen prima — het doel is een realtime gesprek met vertrouwen te volgen."
      }
    },
    {
      "@type": "Question",
      "name": "Zal het leren van deze termen me in staat stellen werk zelf te evalueren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet volledig — het helpt u een gesprek te volgen, maar evalueren vereist nog steeds vaardigheid of een beoordelaar."
      }
    },
    {
      "@type": "Question",
      "name": "Is het redelijk om een engineer te vragen een onbekende term te definiëren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Volkomen redelijk — een goede engineer moet elk begrip ter plekke duidelijk kunnen definiëren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe veranderde verbeterde woordenschat de uitkomst van het project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het zorgde ervoor dat het scopingsproces sneller en nauwkeuriger kon verlopen tijdens het eerste gesprek."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn er nog andere termen die het waard zijn om te leren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit omvat wat het meest naar voren komt; meer gespecialiseerde termen komen van nature naar voren naarmate een project vordert."
      }
    }
  ]
}
</script>