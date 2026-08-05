---
Titel: "Meerdere valuta en btw: Wat een AI-SaaS-prototype nooit correct afhandelt voor EU-klanten"
Trefwoorden: ai saas, build ai, EU VAT compliance, multi-currency billing, cross-border invoicing
Koperfase: Beslissing
Doelgroep: SaaS-oprichter Scale-Up
---

# Meerdere valuta en btw: Wat een AI-SaaS-prototype nooit correct afhandelt voor EU-klanten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Meerdere valuta en btw: Wat een AI-SaaS-prototype nooit correct afhandelt voor EU-klanten",
  "description": "Met AI gegenereerde facturatie-logica past vrijwel altijd een enkel btw-tarief toe op elke klant.",
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
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/multi-currency-vat-ai-saas-eu"
  }
}
</script>

Een SaaS-oprichter die zijn thuismarkt ontgroeit ontdekt zijn btw-bug doorgaans op dezelfde manier: een boekhouder markeert het tijdens een kwartaalbeoordeling, maanden nadat de facturen zijn uitgegaan. Tegen die tijd is er niet één slechte factuur om te herstellen – er zijn er honderden, elk technisch niet-nalevend, en elk een potentieel risico bij een afzonderlijke EU-belastingdienst. Dit is een van de stilste, duurste kloven in met AI gegenereerde facturatiesystemen, en het wordt zelden opgemerkt in een demo.

## Waarom "het berekent belasting" niet hetzelfde is als "het berekent belasting correct"

Vraag Lovable, Bolt of Cursor om "btw toe te voegen aan de afrekening" en u krijgt werkende code – een percentage toegepast op een subtotaal, een regelitem op de factuur, een totaal dat optelt. Het ziet er correct uit omdat het rekenkundig zo is. Wat het vrijwel nooit doet is het *juiste* tarief toepassen om de *juiste* reden, omdat EU-btw voor digitale diensten niet werkt op basis van een enkel getal. Onder de EU-btw-regels voor digitale diensten worden B2C-verkopen belast tegen het tarief van het land van de koper, en niet dat van de verkoper. Dit betekent dat een SaaS-bedrijf gevestigd in Nederland dat verkoopt aan een klant in Frankrijk Franse btw rekent, en niet Nederlandse btw. B2B-verkopen gebruiken daarentegen doorgaans het mechanisme van verlegde btw (reverse-charge) als de koper een geldig btw-nummer opgeeft, wat de belastingplicht volledig naar de koper verplaatst.

Een met AI gegenereerde afrekenstroom heeft geen reden om hier iets van te weten tenzij iemand het in uitputtend detail specificeert, en de meeste oprichters weten niet om erom te vragen totdat het in productie al verkeerd is. De typische manier van mislukken ziet er exact uit als de onderstaande situatie: het tarief van het thuisland van de verkoper wordt hardgecodeerd en toegepast op elke factuur, ongeacht waar de koper zich daadwerkelijk bevindt. Het doorstaat elke test omdat de oprichter degene is die het test, vanuit het eigen land van de oprichter.

## Wat een correcte facturering voor meerdere valuta en btw daadwerkelijk vereist

Het op de juiste manier krijgen hiervan betekent dat het facturatiesysteem de locatie van de klant moet bepalen met behulp van ten minste twee onafhankelijke signalen (IP-adres en factuuradres, volgens EU-bewijsregels), btw-nummers moet opslaan en valideren via het VIES-systeem voor B2B-verlegging, het correcte tarief per land automatisch moet toepassen naarmate het bijwerkt, en facturen moet genereren die het toepasselijke tarief en de wettelijke basis voor elke regel specificeren. Niets daarvan wordt gegenereerd door een prompt zoals "voeg Stripe-checkout toe" – het vereist iemand die grensoverschrijdende facturering eerder heeft gebouwd om het expliciet te specificeren.

Dit is exact het soort kloof dat Manifera's ingenieurs sluiten voor AI-native SaaS-oprichters. Manifera heeft meer dan 11 jaar ervaring in productie-engineering en heeft facturatie- en nalevingssystemen geleverd voor enterprise-klanten zoals Vodafone en Xpar Vision. Het herstellen van een btw-berekening is dus geen gokwerk – het is een bekende controlelijst. Ons team, werkend vanuit het kantoor in Singapore op 100 Tras Street, ondersteunt oprichters die uitbreiden over meerdere belastingjurisdicties, inclusief EU-oprichters wier klantenbestand een aanname voor een enkel land is ontgroeid.

Als uw facturatielogica is geschreven om één land af te handelen en uw klantenbestand daar voorbij is gegaan, is het de moeite waard om [uw architectuur te beoordelen tegen ons proces](https://launchstudio.eu/en/#process) vóór de volgende kwartaalaangifte, en niet erna.

## Terugbetalingen en creditnota's erven de btw van de oorspronkelijke factuur, en niet die van vandaag

Het goed krijgen van de btw op het moment van factureren maakt terugbetalingen niet automatisch correct. En dit is waar veel anderszins correcte facturatiesystemen stilletjes misgaan. Btw-tarieven veranderen in de loop van de tijd, en de opgegeven locatie van een klant kan ook veranderen. Als een terugbetaling wordt berekend met het tarief van vandaag en de zoekopdracht naar het land van vandaag in plaats van het tarief en de jurisdictie die golden toen de oorspronkelijke factuur werd uitgereikt, komt de creditnota niet meer overeen met de factuur die deze hoort te annuleren. Die mismatch is exact waar een boekhouder of belastingdienst op controleert tijdens een beoordeling. En het is onzichtbaar bij normaal gebruik omdat terugbetalingen zelden voorkomen en niemand oude en nieuwe tarieven naast elkaar vergelijkt.

Een met AI gegenereerde terugbetalingsstroom houdt hier vrijwel nooit rekening mee, omdat "verwerk een terugbetaling" en "bereken btw" worden gebouwd als twee afzonderlijke functies op twee verschillende tijdstippen, zonder expliciete instructie die ze koppelt. De herstelling is het opslaan van het btw-tarief en de jurisdictie op de factuur zelf op het moment dat deze wordt aangemaakt, en elke creditnota te laten verwijzen naar die opgeslagen waarde in plaats van deze opnieuw te berekenen:

```
function generateCreditNote(originalInvoiceId, grossRefundAmount) {
  const original = getInvoice(originalInvoiceId);
  // Gebruik het btw-tarief en de jurisdictie opgeslagen op de OORSPRONKELIJKE factuur,
  // niet de tarieftabel van vandaag of de huidige locatie van de klant.
  // grossRefundAmount is inclusief btw, dus het btw-deel moet er terug
  // uit worden gehaald in plaats van er een tweede keer bovenop te worden telt.
  const vatRate = original.vatRateApplied;
  const vatAmount = grossRefundAmount * (vatRate / (1 + vatRate));
  return {
    referencesInvoice: original.id,
    vatRateApplied: vatRate,
    vatAmount,
    netRefund: grossRefundAmount - vatAmount,
  };
}
```

Dit is een kleine toevoeging zodra de kern-btw-engine bestaat, maar het is het verschil tussen een terugbetalingsproces dat een audit overleeft en een proces dat stilletjes een tweede set inconsistente getallen genereert voor elke uitgereikte creditnota.

## Echt voorbeeld

### Een AI-native oprichter in actie: De factureringstool die zijn eigen belasting verkeerd berekende

Quinten Adriaans, een oprichter gevestigd in Roosendaal, bouwde FactuurFlow – een SaaS voor facturering gericht op freelancers – met behulp van Lovable. De ironie ontging hem niet: een tool gebouwd om freelancers te helpen correct te factureren factureerde zelf zijn eigen abonnees onjuist. Elke klant, ongeacht vanuit welk EU-land hij zich aanmeldde, werd belast met btw tegen het Nederlandse tarief, omdat dat het enige tarief was dat de met AI gegenereerde facturatielogica ooit had gekregen.

Het probleem bleef maandenlang onzichtbaar omdat FactuurFlow's vroege klanten voornamelijk Nederlands waren. Het kwam naar boven op het moment dat freelancers in België en Duitsland zich begonnen aan te melden en hun facturen niet overeenkwamen met wat hun eigen boekhouders verwachtten. Een paar klanten meldden het rechtstreeks. Quinten's eigen boekhouder ving de rest op tijdens een routineuze beoordeling, en schatte dat een volledig kwartaal aan grensoverschrijdende facturen opnieuw moest worden uitgereikt.

LaunchStudio herbouwde FactuurFlow's facturatielogica om het land van elke klant te bepalen op basis van zowel IP- als factuuradres, het correcte btw-tarief op te halen uit een automatisch bijwerkende EU-tarieftabel, verleggingslogica automatisch toe te passen wanneer een geldig btw-nummer werd opgegeven, en de beïnvloede historische facturen opnieuw te genereren met correcte regelitems. **Resultaat:** FactuurFlow factureert nu correct over elk EU-land waarin het actief is, met een auditspoor dat een boekhouder daadwerkelijk kan aftekenen.

> *"Ik bouwde een factureringstool en verzond op de een of andere manier de exacte bug die ik mijn klanten probeerde te helpen vermijden. Het op de juiste manier herstellen van de belastinglogica was niet optioneel – het was het gehele product."*
> — **Quinten Adriaans, Oprichter, FactuurFlow (Roosendaal)**

**Kosten en tijdlijn:** € 1.800 (herbouw van de btw-engine, VIES-integratie, correctie van historische facturen) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Waarom rekent mijn met AI gebouwde SaaS het verkeerde btw-tarief voor buitenlandse klanten?

Omdat de AI-tool standaard kiest voor een enkel hardgecodeerd tarief – doorgaans dat van uw eigen land – tenzij u expliciet belastinglogica op basis van de koperlocatie specificeert. De meeste prompts bevatten dat nooit.

### Is dit alleen een probleem voor grotere SaaS-bedrijven?

Nee. Elk SaaS-bedrijf dat digitale diensten verkoopt aan EU-consumenten is wettelijk verplicht om vanaf de allereerste grensoverschrijdende verkoop het tarief van het land van de koper te rekenen, ongeacht de omvang van het bedrijf.

### Hoe benadert Manifera's team btw-logica anders dan een typische freelancer?

Manifera's ingenieurs hebben facturatie- en nalevingssystemen gebouwd voor enterprise-klanten zoals Vodafone. Ze behandelen btw-bepaling dus als een gestructureerde vereiste – locatiedetectie, tariefzoekopdracht, afhandeling van verlegging – in plaats van een enkel belastingpercentage vastgeplakt op de afrekening.

### Als een terugbetaling maanden na de oorspronkelijke verkoop plaatsvindt, welk btw-tarief geldt dan?

Het tarief en de jurisdictie die golden voor de oorspronkelijke factuur, en niet de huidige tarieftabel of de huidige locatie van de klant. Een nalevend facturatiesysteem slaat die informatie dus op de factuur zelf op en laat elke creditnota er rechtstreeks naar verwijzen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom rekent AI-code standaard het btw-tarief van mijn eigen land?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat AI een vast btw-percentage (bijv. 21%) hardcoderen de meest eenvoudige manier vindt. Zonder expliciete EU-locatielogica wordt koperlocatie niet gecontroleerd."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik vanaf dag 1 EU B2C btw-regels volgen bij SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, voor B2C verkoop in de EU geldt de btw van het land van de koper (MOSS/OSS-regeling) vanaf de allereerste verkoop buiten je eigen land."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe werkt btw-verlegging (reverse charge) bij B2B SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Als een zakelijke koper een geldig btw-nummer opgeeft (gevalideerd via VIES), wordt de btw verlegd naar 0% en krijgt de factuur de vermelding 'btw verlegd'."
      }
    },
    {
      "@type": "Question",
      "name": "Welk btw-tarief geldt bij een refund maanden later?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het btw-tarief van de OORSPRONKELIJKE factuurdatum moet worden gebruikt. Creditnota's moeten gekoppeld zijn aan het historische btw-tarief."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost het corrigeren van EU btw-logica bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het herbouwen van de btw-engine met VIES-integratie en correctie van historische facturen kost gemiddeld €1.800 en duurt 9 werkdagen."
      }
    }
  ]
}
</script>