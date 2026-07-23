---
Titel: "AI Field Service Scheduling: waarom dubbele verzending de bug is die u als eerste vindt"
Trefwoorden: ai prototype, ai native, field service scheduling, double dispatch bug, AI scheduling app
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---
# AI Field Service Scheduling: waarom dubbele verzending de bug is die u als eerste vindt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Field Service Scheduling: waarom dubbele verzending de bug is die u als eerste vindt",
  "description": "Door AI gegenereerde planningstools voor de buitendienst verwerken handmatige herschikkingen zelden als een terugschrijving naar de beschikbaarheidskalender, waardoor dubbele verzending ontstaat. Hier ziet u het exacte gelijktijdigheidsprobleem en hoe u er omheen kunt ontwerpen.",
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

Elke planningstool voor de buitendienst wordt uiteindelijk getest volgens hetzelfde scenario: twee technici, één werkadres, beiden ervan overtuigd dat zij de aangewezen persoon waren. Het is geen zeldzame mislukking; het is bijna onvermijdelijk in elke door AI gegenereerde planningsapp die de agenda als een display beschouwt in plaats van als een enkele bron van waarheid.

## Het gelijktijdigheidsprobleem kan door AI-tools niet worden gemodelleerd

Vraag Cursor of een vergelijkbare AI-codeerassistent om "een planningstool voor veldtechnici te bouwen" en je krijgt een kalender-UI, een toewijzingsstroom en waarschijnlijk conflictdetectie voor het voor de hand liggende geval: twee taken die op hetzelfde tijdstip zijn geboekt via dezelfde boekingsstroom. Wat u bijna nooit krijgt, tenzij u het expliciet specificeert, is bescherming tegen het veel voorkomendere praktijkgeval: een handmatige wijziging die buiten de normale boekingsstroom wordt doorgevoerd, zoals een kantoorbeheerder die een taak naar een nieuw tijdslot sleept of deze via de telefoon opnieuw toewijst.

De technische oorzaak van de bug is duidelijk als je hem eenmaal ziet. De meeste door AI gegenereerde planningsapps lezen van en schrijven naar de beschikbaarheidskalender als twee losjes met elkaar verbonden handelingen: een opdracht wordt naar de takentabel geschreven en een afzonderlijk proces wordt verondersteld de beschikbaarheid van de technicus bij te werken. Wanneer een nieuwe planning plaatsvindt via een zijkanaal (een beheerder die een record rechtstreeks bewerkt, een handmatige overschrijving, een snelle oplossing buiten de primaire gebruikersinterface), raakt die update vaak de takentabel, maar wordt nooit de bijbehorende terugschrijving van de beschikbaarheid geactiveerd. De kalender die de AI-tool heeft gegenereerd, geeft nog steeds aan dat dat slot open is, omdat niets anders aangeeft. De volgende geautomatiseerde of handmatige verzending vult datzelfde "open" slot met een tweede technicus.

Dit is een klassieke racevoorwaarde vermomd als een planningsfunctie, en het is precies het soort gat dat een op stress getest, gelijktijdigheidsbewust systeem opvangt en een demo nooit zal doen, omdat demo's geen kantoorbeheerder bevatten die onder druk een oordeel velt.

## Een kalender bouwen die niet tegen zichzelf kan liegen

De oplossing is niet meer een gebruikersinterface, maar maakt van de beschikbaarheidskalender een afgeleide weergave van één enkele bron van waarheid in plaats van een afzonderlijk bijgehouden tabel die kan afwijken. Elk pad dat in aanraking komt met de planning van een technicus, of het nu gaat om de geautomatiseerde boekingsstroom, het slepen en neerzetten van de beheerder of het overschrijven van een telefonische aanmelding, moet via dezelfde functie worden geschreven en dezelfde downstream-controles activeren. Als het goed wordt gedaan, is een handmatige herschikking structureel niet meer in staat om verouderde beschikbaarheid achter te laten, omdat er maar één plaatsbeschikbaarheidsstatus bestaat.

“We zien een verschuiving in de softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. Precies daarin hebben we elf jaar ervaring”, zegt Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera. Bugs met dubbele verzending zijn een schoolvoorbeeld van wat hij bedoelt: de planningsfunctie zelf was nooit het moeilijkste deel; de concurrency-architectuur eronder was.

LaunchStudio brengt de meer dan 120 productie-ervaring van Manifera voor precies dit soort oplossingen, en ingenieurs die verbonden zijn met Manifera's Zuidoost-Aziatische hub aan Tras Street in Singapore hebben soortgelijke realtime coördinatieproblemen voor logistieke en operationele klanten afgehandeld. Als uw planningstool een pad heeft voor handmatige overschrijvingen – en bijna elke buitendiensttool heeft dat – [krijg dan een uitgebreide beoordeling via onze rekenmachine](https://launchstudio.eu/en/#calculator) voordat een dubbele meldkamer uw drukste technicus vindt.

## Echt voorbeeld

### Een AI-Native oprichter in actie: twee bestelwagens, één adres

Jorrit Hagen, oprichter uit Enschede, bouwde MonteurPlanner – een planningstool voor HVAC-technici – met behulp van Cursor. Het verwerkte de belangrijkste boekingsstroom goed: klanten vroegen servicevensters aan, het systeem wees beschikbare technici toe en iedereen kreeg automatisch kalenderbevestigingen.

De bug kwam aan het licht toen een kantoorbeheerder handmatig een taak telefonisch opnieuw plantte en deze naar een ander tijdslot verplaatste om tegemoet te komen aan een dringend verzoek van een klant. Door de nieuwe planning werd het taakrecord correct bijgewerkt, maar er werd nooit teruggeschreven naar de beschikbaarheidskalender voor technici die de AI-tool had gegenereerd. Dat slot stond nog steeds open. Er werd automatisch een tweede technicus naar hetzelfde adres gestuurd voor wat volgens het systeem een ​​niet-gerelateerde klus was. Beide technici arriveerden binnen twintig minuten na elkaar, zonder enig idee dat de ander zou komen.

LaunchStudio heeft de planningslogica van MonteurPlanner geherstructureerd, zodat elk pad dat in aanraking komt met de agenda van een technicus (geautomatiseerde boeking, slepen en neerzetten door de beheerder en handmatige telefoonoverschrijvingen) via één enkele beschikbaarheidsfunctie wordt geschreven in plaats van drie losjes met elkaar verbonden functies. We hebben een vergrendelingscontrole toegevoegd die elke tweede toewijzing aan een reeds vastgelegd slot blokkeert, ongeacht welke interface deze heeft geactiveerd, en een beheerdersconflictwaarschuwing die onmiddellijk wordt geactiveerd in plaats van de dubbele boeking stilletjes toe te staan.

**Resultaat:** MonteurPlanner heeft sindsdien zonder enig incident met dubbele verzending gewerkt, bij een techniciteam dat sindsdien is gegroeid van vier naar negen.

> *"Ik ging ervan uit dat de kalender de bron van de waarheid was. Het bleken meer drie verschillende meningen over de waarheid te zijn die het meestal met elkaar eens waren."*
> — **Jorrit Hagen, oprichter, MonteurPlanner (Enschede)**

**Kosten en tijdlijn:** € 1.650 (planning van herbouw van architectuur, uniforme beschikbaarheidslogica, conflictvergrendeling) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Waarom missen AI-gegenereerde planningstools handmatige herschikkingsconflicten?

Ze behandelen de beschikbaarheid doorgaans als een afzonderlijk bijgehouden tabel die alleen door de primaire boekingsstroom wordt bijgewerkt. Handmatige overschrijvingen die buiten deze stroom om worden gedaan (beheerwijzigingen, telefoonherschikkingen) leiden vaak niet tot dezelfde terugschrijving van de beschikbaarheid, waardoor verouderde "open" slots achterblijven.

### Is dit een bug in Cursor of een algemeen risico bij door AI gebouwde planningstools?

Het is een algemeen architectonisch risico voor alle AI-coderingstools, en niet specifiek voor Cursor. Het verschijnt wanneer planningslogica niet is ontworpen rond één enkele bron van waarheid voor beschikbaarheid.

### Wat zegt Herre Roelevink over dit soort hiaten?

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, omschrijft het als een architectuurprobleem: het omzetten van een goed idee in werkende software was nooit het moeilijkste deel; de gelijktijdigheid en data-architectuur die nodig zijn om het bij echt gebruik betrouwbaar te maken, is waar ervaring het belangrijkst is.

### Hoe test u het risico op dubbele verzending voordat dit in de productie gebeurt?

Simuleer een handmatige nieuwe planning buiten de normale boekingsinterface (een wijziging of overschrijving door de beheerder) en controleer of de beschikbaarheidskalender van de technicus dit onmiddellijk weergeeft. Als het slot nog steeds open is, is het risico aanwezig.

### Heeft Manifera ervaring met dit soort realtime coördinatiesystemen?

Ja, technici verbonden aan de Zuidoost-Aziatische hub van Manifera in Singapore hebben gewerkt aan soortgelijke realtime coördinatie- en conflictdetectieproblemen voor logistieke en operationele klanten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI-generated scheduling tools miss manual reschedule conflicts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They typically treat availability as a separately maintained table updated only by the primary booking flow. Manual overrides made outside that flow often don't trigger the corresponding availability write-back, leaving stale open slots."
      }
    },
    {
      "@type": "Question",
      "name": "Is this a bug in Cursor, or a general risk with AI-built scheduling tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's a general architectural risk across any AI coding tool, not specific to Cursor, and shows up whenever scheduling logic isn't designed around a single source of truth for availability."
      }
    },
    {
      "@type": "Question",
      "name": "What does Herre Roelevink say about this kind of gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Herre Roelevink, CEO of LaunchStudio and Managing Director of Manifera, frames it as an architecture and maturity problem: the challenge today is the architecture needed to bring good ideas to production reliability, not the initial build."
      }
    },
    {
      "@type": "Question",
      "name": "How do you test for double-dispatch risk before it happens in production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Simulate a manual reschedule outside the normal booking UI and check whether the technician's availability calendar reflects it immediately."
      }
    },
    {
      "@type": "Question",
      "name": "Does Manifera have experience with real-time coordination systems like this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, engineers connected to Manifera's Southeast Asia hub in Singapore have worked on similar real-time coordination and conflict-detection problems for logistics and operations clients."
      }
    }
  ]
}
</script>