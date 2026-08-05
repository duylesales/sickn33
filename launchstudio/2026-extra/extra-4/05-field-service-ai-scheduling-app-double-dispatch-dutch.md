---
Titel: "AI-buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt"
Trefwoorden: ai prototype, ai native, field service scheduling, double dispatch bug, AI scheduling app
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# AI-buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-buitendienstplanning: Waarom dubbele verzending de bug is die u het eerst vindt",
  "description": "Met AI gegenereerde planningstools verwerken handmatige herplanningen zelden als een terugschrijfactie.",
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
    "@id": "https://launchstudio.eu/en/blog/field-service-ai-scheduling-app-double-dispatch"
  }
}
</script>

Elke planningstool voor buitendienst wordt uiteindelijk getest door hetzelfde scenario: twee monteurs, één klusadres, en beide ervan overtuigd dat zij degene waren die waren toegewezen. Het is geen zeldzame fout – het is bijna onvermijdelijk in elke met AI gegenereerde plannings-app die de kalender als een weergave behandelt in plaats van als een enkele bron van de waarheid.

## Het gelijktijdigheidsprobleem dat AI-tools niet modelleren

Vraag Cursor of een vergelijkbare AI-coderingsassistent om "een planningstool voor buitendienstmonteurs te bouwen", en u krijgt een kalender-UI, een toewijzingsstroom, en waarschijnlijk conflictdetectie voor het voor de hand liggende geval – twee klussen die op hetzelfde tijdslot zijn geboekt via dezelfde boekingsstroom. Wat u bijna nooit krijgt, tenzij u het expliciet specificeert, is bescherming tegen het veel vaker voorkomende geval in de echte wereld: een handmatige wijziging die buiten de normale boekingsstroom om wordt gemaakt, zoals een kantoormedewerker die een klus naar een nieuw tijdslot sleept of deze telefonisch opnieuw toewijst.

De technische oorsprong van de bug is eenvoudig zodra u hem ziet. De meeste met AI gegenereerde plannings-apps lezen van en schrijven naar de beschikbaarheidskalender als twee losjes verbonden operaties – een toewijzing wordt geschreven naar de klussentabel, en een afzonderlijk proces hoort de beschikbaarheid van de monteur bij te werken. Wanneer er een herplanning plaatsvindt via een zij-kanaal (een beheerdersbewerking rechtstreeks in een record, een handmatige overschrijving, een snelle herstelling buiten de primaire UI om), raakt die update frequent de klussentabel, maar vuurt deze nooit de bijbehorende terugschrijfactie naar de beschikbaarheid af. De kalender die de AI-tool genereerde toont dat slot nog steeds als open, omdat niets hem anders heeft verteld. De volgende geautomatiseerde of handmatige verzending vult datzelfde "open" slot met een tweede monteur.

Dit is een klassieke race-conditie gehuld als een planningsfunctie. Het is exact het soort kloof dat een stresstest-bestendig, gelijktijdigheidsbewust systeem opvangt en dat een demo nooit zal laten zien, omdat demo's geen kantoormedewerker bevatten die onder druk een oordeel moet vellen.

## Het bouwen van een kalender die niet tegen zichzelf kan liegen

De oplossing is niet meer UI – het is het maken van de beschikbaarheidskalender tot een afgeleide weergave van één enkele bron van waarheid, in plaats van een afzonderlijk onderhouden tabel die kan wegdrijven. Elk pad dat het schema van een monteur raakt, of het nu de geautomatiseerde boekingsstroom is, een beheerdersbewerking via slepen-en-neerzetten, of een telefonische overschrijving, moet via dezelfde functie schrijven en dezelfde stroomafwaartse controles triggeren. Goed gedaan wordt een handmatige herplanning structureel onmogelijk om verouderde beschikbaarheid achter te laten, omdat er slechts één plek is waar de beschikbaarheidsstatus daadwerkelijk leeft.

"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. We hebben elf jaar ervaring in exact dat," zegt Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera. Bugs met dubbele verzending zijn een tekstboekvoorbeeld van wat hij bedoelt – de planningsfunctie zelf was nooit het moeilijke deel; de gelijktijdigheidsarchitectuur eronder was dat wel.

LaunchStudio brengt Manifera's ervaring van meer dan 120 ingenieurs aan productie-ervaring naar exact dit soort herstellingen. Ingenieurs verbonden aan Manifera's Zuidoost-Aziatische hub op Tras Street in Singapore hebben vergelijkbare realtime coördinatieproblemen afgehandeld voor logistieke en operationele klanten. Als uw planningstool enig pad heeft voor handmatige overschrijvingen – en bijna elke buitendiensttool heeft dat – [krijg een beoordeling op maat via onze calculator](https://launchstudio.eu/en/#calculator) voordat een dubbele verzending uw drukste monteur vindt.

## Een enkele bron van waarheid kan nog steeds tegen zichzelf racen

Het leiden van elk boekingspad door één gedeelde beschikbaarheidsfunctie sluit de afdrijvingsbug – een handmatige herplanning en een geautomatiseerde verzending zijn het nu eens over waar de gegevens leven. Het sluit niet automatisch een smallere, stillere versie van hetzelfde probleem: twee verzoeken die die ene functie op bijna exact hetzelfde moment raken. Als het controleren of een slot vrij is en het schrijven van de nieuwe toewijzing twee afzonderlijke stappen zijn binnen die functie, kunnen beide verzoeken de "is dit slot vrij" controle uitvoeren voordat een van beide daadwerkelijk zijn schrijfoperatie heeft vastgelegd – een klassieke controle-dan-actie race-conditie. Het is onzichtbaar bij een laag volume, omdat er twee verzendpogingen voor nodig zijn die binnen hetzelfde smalle tijdvenster landen om het te triggeren, maar het wordt waarschijnlijker naarmate een planningstool drukker en waardevoller wordt.

```
-- Kwetsbaar: controle en schrijfoperatie zijn twee afzonderlijke stappen
SELECT status FROM slots WHERE technician_id = ? AND slot_time = ?
-- een tweede verzoek kan dezelfde controle uitvoeren voordat het eerste verzoek schrijft
INSERT INTO assignments (technician_id, slot_time, job_id) VALUES (?, ?, ?)

-- Veiliger: een beperking op databaseniveau laat de tweede schrijfoperatie direct mislukken
ALTER TABLE assignments ADD CONSTRAINT one_job_per_slot UNIQUE (technician_id, slot_time)
-- de tweede INSERT raakt nu een beperkingsschending in plaats van stilletjes te slagen
```

Het consolideren van het schrijfpad in één functie is noodzakelijk, maar het is op zichzelf niet voldoende – de database zelf heeft een beperking nodig die een dubbele toewijzing fysiek onmogelijk maakt om vast te leggen, in plaats van te vertrouwen op toepassingscode om eerst te controleren en te hopen dat niets anders op hetzelfde moment controleert.

## Echt voorbeeld

### Een AI-native oprichter in actie: Twee bussen, één adres

Jorrit Hagen, een oprichter in Enschede, bouwde MonteurPlanner – een planningstool voor HVAC-monteurs – met behulp van Cursor. Het handelde de kern-boekingsstroom goed af: klanten vroegen servicetijdvensters aan, het systeem wees beschikbare monteurs toe, en iedereen kreeg automatisch kalenderbevestigingen.

De bug kwam naar boven toen een kantoormedewerker handmatig een klus telefonisch herplande, en deze naar een ander tijdslot verplaatste om tegemoet te komen aan een dringend verzoek van een klant. De herplanning werkte het klusrecord correct bij, maar het schreef nooit terug naar de beschikbaarheidskalender voor monteurs die de AI-tool had gegenereerd. Dat slot werd nog steeds als open getoond. Een tweede monteur werd automatisch verzonden naar hetzelfde adres voor wat het systeem dacht dat een ongerelateerde klus was – en beide monteurs kwamen binnen twintig minuten van elkaar aan, zonder dat ze wisten dat de ander eraan kwam.

LaunchStudio herstructureerde de planningslogica van MonteurPlanner zodat elk pad dat de kalender van een monteur raakt – geautomatiseerde boekingen, beheerder-slepen-en-neerzetten, en handmatige telefonische overschrijvingen – schrijft via een enkele beschikbaarheidsfunctie in plaats van drie losjes verbonden functies. We hebben een vergrendelingscontrole toegevoegd die elke tweede toewijzing aan een al vastgelegd slot blokkeert, ongeacht welke interface deze heeft getriggerd, en een beheerdergerichte conflictwaarschuwing die onmiddellijk afgaat in plaats van de dubbele boeking stilletjes toe te staan.

**Resultaat:** MonteurPlanner heeft sinds de aanpassing gedraaid zonder een enkel incident met dubbele verzending, over een monteursteam dat sindsdien is gegroeid van vier naar negen.

> *"Ik nam aan dat de kalender de bron van de waarheid was. Het bleek meer te lijken op drie verschillende meningen over de waarheid die toevallig meestal overeenkwamen."*
> — **Jorrit Hagen, Oprichter, MonteurPlanner (Enschede)**

**Kosten en tijdlijn:** € 1.650 (herbouw van planningsarchitectuur, gecentraliseerde beschikbaarheidslogica, conflictvergrendeling) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Waarom missen met AI gegenereerde planningstools handmatige herplanningsconflicten?

Ze behandelen beschikbaarheid doorgaans als een afzonderlijk onderhouden tabel die alleen door de primaire boekingsstroom wordt bijgewerkt. Handmatige overschrijvingen buiten die stroom om – beheerdersbewerkingen, telefonische herplanningen – triggeren vaak niet dezelfde terugschrijfactie naar de beschikbaarheid, waardoor er verouderde "open" slots achterblijven.

### Is dit een bug in Cursor, of een algemeen risico bij met AI gebouwde planningstools?

Het is een algemeen architecturaal risico bij elke AI-coderingsassistent, en niet specifiek voor Cursor. Het verschijnt wanneer planningslogica niet is ontworpen rond één enkele bron van waarheid voor beschikbaarheid.

### Wat zegt Herre Roelevink over dit soort kloof?

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, ziet dit als een architectuur- en volwassenheidsprobleem: de uitdaging vandaag de dag is de architectuur die nodig is om goede ideeën naar productiebeproeving te brengen, en niet de initiële bouw.

### Hoe test u op risico's op dubbele verzending voordat het in productie gebeurt?

Simuleer een handmatige herplanning buiten de normale boekings-UI om – een beheerdersbewerking of overschrijving – en controleer of de beschikbaarheidskalender van de monteur dit onmiddellijk weerspiegelt. Als het slot nog steeds als open wordt getoond, is het risico aanwezig.

### Heeft Manifera ervaring met dit soort realtime coördinatiesystemen?

Ja, ingenieurs verbonden aan Manifera's Zuidoost-Aziatische hub in Singapore hebben gewerkt aan vergelijkbare realtime coördinatie- en conflictdetectieproblemen voor logistieke en operationele klanten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom missen AI-planningstools handmatige herplanningsconflicten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze behandelen beschikbaarheid als een aparte tabel die alleen bij primaire boekingen update. Handmatige wijzigingen schrijven vaak niet terug naar de kalender."
      }
    },
    {
      "@type": "Question",
      "name": "Is dubbele verzending een Cursor-bug of een algemeen AI-risico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is een algemeen architectuurrisico bij AI-coderingshulpmiddelen als er geen enkele bron van waarheid voor beschikbaarheid is ontworpen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zegt Herre Roelevink over dit soort architectuurkloven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Herre Roelevink (CEO LaunchStudio) benadrukt dat de uitdaging niet het software-idee is, maar de backend-architectuur die nodig is voor betrouwbaarheid."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test u het risico op dubbele verzending vóór lancering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voer een handmatige herplanning uit buiten het standaardformulier en controleer of het kalenderslot van de monteur direct wordt aangepast."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft Manifera ervaring met realtime coördinatiesystemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, ingenieurs in Singapore werken regelmatig aan realtime plannings- en conflictdetectiewerkstromen voor logistieke organisaties."
      }
    }
  ]
}
</script>