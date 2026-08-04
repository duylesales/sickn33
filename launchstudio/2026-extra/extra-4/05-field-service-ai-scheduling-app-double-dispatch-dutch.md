---
Titel: "AI Buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt"
Trefwoorden: ai prototype, ai native, field service scheduling, double dispatch bug, AI scheduling app
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# AI Buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt",
  "description": "Met AI gegenereerde planningstools voor buitendienst verwerken handmatige herplanningen zelden als een terugschrijfopdracht naar de beschikbaarheidskalender, wat leidt tot dubbele verzendingen. Dit is het exacte gelijktijdigheidsprobleem en hoe u eromheen ontwerpt.",
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
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/field-service-ai-scheduling-app-double-dispatch"
  }
}
</script>

Elke planningstool voor de buitendienst wordt uiteindelijk getest door hetzelfde scenario: twee monteurs, één klusadres, en allebei overtuigd dat zij degene waren die waren toegewezen. Het is geen zeldzaam probleem — het is bijna onvermijdelijk in elke door AI gegenereerde planningsapp die de kalender als een weergave behandelt in plaats van als een enkele bron van waarheid.

## Het gelijktijdigheidsprobleem dat AI-tools niet modelleren

Vraag Cursor of een soortgelijke AI-coderingsassistent om "een planningstool voor buitendiensttechnici te bouwen", en u krijgt een kalender-UI, een toewijzingsstroom en waarschijnlijk conflictgevoeligheid voor het voor de hand liggende geval — twee klussen die op hetzelfde tijdslot zijn geboekt via dezelfde boekingsstroom. Wat u bijna nooit krijgt, tenzij u het expliciet opgeeft, is bescherming tegen het veel vaker voorkomende praktijkgeval: een handmatige wijziging die buiten de normale boekingsstroom om wordt gemaakt, zoals een kantoormedewerker die een klus naar een nieuw tijdslot sleept of deze telefonisch opnieuw toewijst.

De technische wortel van de bug is eenvoudig als u het eenmaal ziet. De meeste door AI gegenereerde planningsapps lezen van en schrijven naar de beschikbaarheidskalender als twee los van elkaar staande bewerkingen — een toewijzing wordt naar de klussentabel geschreven, en een afzonderlijk proces moet de beschikbaarheid van de monteur bijwerken. Wanneer een herplanning plaatsvindt via een zijkanaal (een beheerdersbewerking die een record rechtstreeks bewerkt, een handmatige overschrijving), raakt die update vaak wel de klussentabel, maar wordt het bijbehorende terugschrijven naar de beschikbaarheid nooit geactiveerd. De kalender die de AI-tool heeft gegenereerd toont dat slot nog steeds als open. De volgende geautomatiseerde of handmatige verzending vult hetzelfde "open" slot met een tweede monteur.

Dit is een klassieke race-conditie verkleed als een planningsfunctie, en het is precies het soort gat dat een onder stress getest systeem opvangt en een demo nooit zal laten zien.

## Een kalender bouwen die niet tegen zichzelf kan liegen

De oplossing is niet meer UI — het is het maken van de beschikbaarheidskalender tot een afgeleide weergave van een enkele bron van waarheid in plaats van een afzonderlijk bijgehouden tabel die kan afdrijven. Elk pad dat het schema van een monteur raakt, of het nu de geautomatiseerde boekingsstroom is, een bewerking van een beheerder via slepen en neerzetten, of een telefonische overschrijving, moet via dezelfde functie schrijven en dezelfde stroomafwaartse controles activeren. Goed gedaan wordt een handmatige herplanning structureel onmogelijk om verouderde beschikbaarheid achter te laten.

"We zien een verschuiving in de softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. Precies daarin hebben we elf jaar ervaring", zegt Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera. Bugs met dubbele verzending zijn een schoolvoorbeeld van wat hij bedoelt: de planningsfunctie zelf was nooit het moeilijkste deel; de gelijktijdigheidsarchitectuur eronder was dat.

LaunchStudio brengt de productie-ervaring van Manifera's 120+ ingenieurs naar precies dit soort oplossingen. Ingenieurs verbonden aan de Zuidoost-Aziatische hub van Manifera op Tras Street in Singapore hebben soortgelijke realtime coördinatieproblemen voor logistieke en operationele klanten behandeld. Als uw planningstool paden heeft voor handmatige overschrijvingen, [krijg dan een beoordeling via onze calculator](https://launchstudio.eu/en/#calculator) voordat een dubbele verzending uw drukste monteur vindt.

## Een enkele bron van waarheid kan nog steeds tegen zichzelf racen

Het leiden van elk boekingspad via één gedeelde beschikbaarheidsfunctie sluit de afdrijvingsbug — een handmatige herplanning en een geautomatiseerde verzending zijn het nu eens over waar de gegevens leven. Het sluit niet automatisch een smallere versie van hetzelfde probleem: twee verzoeken die die ene functie op bijna hetzelfde moment raken. Als het controleren of een slot vrij is en het schrijven van de nieuwe toewijzing twee afzonderlijke stappen binnen die functie zijn, kunnen beide verzoeken de controle "is dit slot vrij" uitvoeren voordat een van beide zijn schrijfopdracht daadwerkelijk heeft doorgevoerd.

```sql
-- Kwetsbaar: controle en schrijfopdracht zijn twee afzonderlijke stappen
SELECT status FROM slots WHERE technician_id = ? AND slot_time = ?
-- een tweede verzoek kan deze controle uitvoeren voordat het eerste verzoek schrijft
INSERT INTO assignments (technician_id, slot_time, job_id) VALUES (?, ?, ?)

-- Veiliger: een unieke beperking op databaseniveau laat de tweede schrijfopdracht mislukken
ALTER TABLE assignments ADD CONSTRAINT one_job_per_slot UNIQUE (technician_id, slot_time)
```

Het consolideren van het schrijverspad in één functie is noodzakelijk, maar niet voldoende op zichzelf — de database zelf heeft een beperking nodig die een dubbele toewijzing fysiek onmogelijk maakt om vast te leggen.

## Echt voorbeeld

### Een AI-native oprichter in actie: Twee bussen, één adres

Jorrit Hagen, een oprichter in Enschede, bouwde MonteurPlanner — een planningstool voor HVAC-monteurs — met behulp van Cursor. Het behandelde de kernboekingsstroom goed: klanten vroegen servicetijdvakken aan, het systeem wees beschikbare monteurs toe en iedereen kreeg automatisch agendabevestigingen.

De bug kwam aan het licht toen een kantoormedewerker handmatig een klus telefonisch herplande en deze naar een ander tijdslot verplaatste om aan een dringend klantverzoek te voldoen. De herplanning werkte het klusrecord correct bij, maar het schreef nooit terug naar de beschikbaarheidskalender van de monteur die de AI-tool had gegenereerd. Dat slot werd nog steeds als open weergegeven. Een tweede monteur werd automatisch naar hetzelfde adres gestuurd voor wat het systeem dacht dat een ongerelateerde klus was — en beide monteurs kwamen binnen twintig minuten na elkaar aan.

LaunchStudio heeft de planningslogica van MonteurPlanner zo geherstructureerd dat elk pad dat de agenda van een monteur raakt — geautomatiseerde boekingen, bewerkingsfuncties voor beheerders en handmatige telefonische overschrijvingen — via één enkele beschikbaarheidsfunctie schrijft in plaats van drie los van elkaar staande functies. We hebben een vergrendelingscontrole toegevoegd die elke tweede toewijzing aan een reeds toegewezen slot blokkeert, en een voor beheerders zichtbare conflictwaarschuwing die onmiddellijk afgaat.

**Resultaat:** MonteurPlanner heeft sindsdien gedraaid zonder een enkel incident met dubbele verzending, over een monteursteam dat sindsdien is gegroeid van vier naar negen.

> *"Ik ging er vanuit dat de kalender de bron van waarheid was. Het bleek meer te lijken op drie verschillende meningen over de waarheid die het toevallig meestal met elkaar eens waren."*
> — **Jorrit Hagen, Oprichter, MonteurPlanner (Enschede)**

**Kosten & Tijdlijn:** € 1.650 (herbouw planningsarchitectuur, uniforme beschikbaarheidslogica, conflictvergrendeling) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Waarom missen door AI gegenereerde planningstools handmatige herplanningsconflicten?

Ze behandelen beschikbaarheid meestal als een afzonderlijk bijgehouden tabel die alleen door de primaire boekingsstroom wordt bijgewerkt. Handmatige overschrijvingen buiten die stroom om activeren vaak niet hetzelfde terugschrijven van beschikbaarheid, waardoor verouderde "open" slots achterblijven.

### Is dit een bug in Cursor, of een algemeen risico bij met AI gebouwde planningstools?

Het is een algemeen architectuurisico bij elke AI-coderingstool. Het verschijnt wanneer de planningslogica niet is ontworpen rond één enkele bron van waarheid voor beschikbaarheid.

### Wat zegt Herre Roelevink over dit soort leemten?

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, ziet het als een architectuur- en volwassenheidsprobleem: het omzetten van een goed idee in werkende software was nooit het moeilijkste deel — de gelijktijdigheids- en data-architectuur die nodig is om het betrouwbaar te maken onder echt gebruik is waar ervaring het meest telt.

### Hoe test u het risico op dubbele verzending voordat het in productie gebeurt?

Simuleer een handmatige herplanning buiten de normale boekings-UI en controleer of de beschikbaarheidskalender van de monteur dit onmiddellijk weerspiegelt. Als het slot nog steeds open staat, is het risico aanwezig.

### Heeft Manifera ervaring met dit soort realtime coördinatiesystemen?

Ja, ingenieurs verbonden aan de Zuidoost-Aziatische hub van Manifera in Singapore hebben gewerkt aan soortgelijke realtime coördinatie- en conflictdetectieproblemen voor logistieke en operationele klanten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom missen door AI gegenereerde planningstools handmatige herplanningsconflicten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze behandelen beschikbaarheid meestal als een afzonderlijk bijgehouden tabel die alleen door de primaire boekingsstroom wordt bijgewerkt. Handmatige overschrijvingen buiten die stroom om activeren vaak niet hetzelfde terugschrijven van beschikbaarheid."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit een bug in Cursor, or een algemeen risico bij met AI gebouwde planningstools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is een algemeen architectuurisico bij elke AI-coderingstool, niet specifiek voor Cursor, en verschijnt wanneer de planningslogica niet is ontworpen rond één enkele bron van waarheid."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zegt Herre Roelevink over dit soort leemten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, ziet het als een architectuur- en volwassenheidsprobleem: de uitdaging vandaag is de architectuur die nodig is om goede ideeën naar productiebepaling te brengen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test u het risico op dubbele verzending voordat het in productie gebeurt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Simuleer een handmatige herplanning buiten de normale boekings-UI en controleer of de beschikbaarheidskalender van de monteur dit onmiddellijk weerspiegelt."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft Manifera ervaring met dit soort realtime coördinatiesystemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, ingenieurs verbonden aan de Zuidoost-Aziatische hub van Manifera in Singapore hebben gewerkt aan soortgelijke realtime coördinatie- en conflictdetectieproblemen."
      }
    }
  ]
}
</script>