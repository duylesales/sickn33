---
Titel: "Zachte verwijdering versus harde verwijdering: de door AI gegenereerde datamodelbeslissing die niemand uitlegt"
Trefwoorden: ai database, ai code tool, soft delete, hard delete, data recovery
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---
# Zachte verwijdering versus harde verwijdering: de door AI gegenereerde datamodelbeslissing die niemand uitlegt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Zachte verwijdering versus harde verwijdering: de door AI gegenereerde datamodelbeslissing die niemand uitlegt",
  "description": "AI-coderingstools zijn standaard ingesteld op permanente harde verwijderingen van databaserijen, wat betekent dat \u00e9\u00e9n onbedoelde klik gegevens kan vernietigen zonder dat er een weg meer terug is. Hier leest u waarom zacht verwijderen de standaard zou moeten zijn en hoe u dit achteraf kunt aanpassen.",
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
    "@id": "https://launchstudio.eu/en/blog/soft-delete-data-recovery-ai-generated-app"
  }
}
</script>

Er is een specifiek soort stilte die volgt op een gebruiker die op het verkeerde klikt op "verwijderen" - de tweede waarin hij zich realiseert wat er net is gebeurd, en de volgende seconde waarin hij zich realiseert dat er geen ongedaan gemaakt kan worden. Als de verwijderknop van uw app een 'DELETE FROM'-instructie rechtstreeks tegen de database uitvoert, is die stilte permanent en is het een beslissing die uw AI-coderingstool vrijwel zeker voor u heeft genomen zonder deze ooit te vermelden.

## Het verschil van één woord dat niemand tijdens de ontwikkeling signaleert

Wanneer u een AI-coderingsassistent vraagt ​​om "een verwijderfunctie toe te voegen" voor een record, is de meest directe en gebruikelijke implementatie een harde verwijdering: een SQL `DELETE`-instructie (of een gelijkwaardige ORM-aanroep) die de rij volledig en onmiddellijk uit de database verwijdert, zonder dat er een spoor achterblijft. Het is de eenvoudigst mogelijke interpretatie van 'verwijderen', het doorstaat elke test (de record is verdwenen, precies zoals gevraagd) en het werkt feilloos tot iemand het verkeerde verwijdert.

Het alternatief, zacht verwijderen, verwijdert de rij helemaal niet. In plaats daarvan stelt het een vlag in (meestal een 'deleted_at'-tijdstempelkolom) en elk deel van de applicatie dat uit die tabel leest, wordt bijgewerkt om rijen uit te filteren waarin die vlag is ingesteld. Functioneel gezien verdwijnt een voorlopig verwijderde record uit het zicht van de gebruiker op precies dezelfde manier als een definitief verwijderde record. Het verschil doet er alleen toe op het moment dat iemand het terug nodig heeft: een zacht verwijderd record kan binnen enkele seconden worden hersteld door de vlag te wissen, terwijl een hard verwijderd record moet worden hersteld vanaf een databaseback-up - als die bestaat, als deze recent genoeg is, en als het herstellen ervan niet ook alle andere wijzigingen die sindsdien zijn aangebracht ongedaan maakt.

## Waarom AI-tools standaard de verkeerde keuze maken, en wanneer het er echt toe doet

Zacht verwijderen is niet de standaard waar een AI-tool naar streeft, omdat het echt meer werk is: het betekent het toevoegen van een kolom, het bijwerken van elke afzonderlijke zoekopdracht in die tabel om gemarkeerde rijen uit te sluiten, en meestal het bouwen van een soort beheerdersinterface om zacht verwijderde records later te bekijken en te herstellen. Een prompt als "laat gebruikers een project verwijderen" communiceert niets van die complexiteit; het vraagt ​​alleen om verwijdering, en de AI geeft je de eenvoudigste versie. De beslissing welke geschikt is, hangt volledig af van wat er wordt verwijderd: een zachte verwijdering is bijna verplicht voor alles met trapsgewijze relaties (een project met taken, een gebruiker met orders), alles wat een gebruiker per ongeluk kan verwijderen via een gebruikersinterface, of alles met compliance-gedreven bewaarvereisten. Een echt wegwerprecord met lage inzet heeft dit misschien helemaal niet nodig.

Dit is precies het soort oordeelsvorming over datamodellering dat door AI gegenereerde code scheidt van architectuur op productieniveau – niet bepaald een bug, maar een standaard die nooit daadwerkelijk is geëvalueerd tegen de werkelijke kosten als het fout gaat. LaunchStudio wordt mogelijk gemaakt door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering, en het beoordelen van de semantiek van het verwijderen aan de hand van de daadwerkelijke ontploffingsradius van elke tabel is een standaardonderdeel van de manier waarop onze ingenieurs, die vanuit Manifera's kantoor in Amsterdam werken, het datamodel van een door AI gebouwde app voorbereiden voor echte gebruikers.

Als u niet zeker weet welke van de verwijderfuncties van uw app harde verwijderingen zijn die wachten om een ​​slechte dag te veroorzaken, is het de moeite waard [uw gegevensmodel te beoordelen met ons team](https://launchstudio.eu/en/#contact) voordat uw eerste echte gebruiker er op de harde manier achter komt.

## Soft Delete verbreekt stilletjes unieke beperkingen (Unique Constraints)

Een zachte verwijdering (soft delete) markeert een record in de database als `deleted_at = TIMESTAMP` in plaats van het fysiek te wissen. Een veelvoorkomend probleem ontstaat bij unieke velden (zoals een e-mailadres of gebruikersnaam): als een gebruiker zijn account verwijdert en later een nieuw account probeert aan te maken met hetzelfde e-mailadres, faalt de database-invoer vanwege de unieke beperking op het oude (zacht verwijderde) record.

Gebruik een samengestelde unieke index die de verwijderingsdatum meeneemt of een uniek ID toevoegt bij verwijdering:

```sql
-- In plaats van UNIQUE(email), gebruik een partiële unieke index:
CREATE UNIQUE INDEX unique_active_user_email ON users (email) WHERE deleted_at IS NULL;
```

## Echt voorbeeld

### Een AI-native oprichter in actie: het project dat in één klik verdween

Daniël Wesseling, oprichter in Emmeloord, bouwde ProjectVolg, een projectmanagement SaaS, met behulp van Lovable. De verwijderfunctie voor een project werkte betrouwbaar in elke test die Daniël tijdens de ontwikkeling uitvoerde: klik op verwijderen, bevestig, het project is verdwenen. Schoon, eenvoudig, precies zoals bedoeld - want bij elke test was het Daniël die een testproject verwijderde dat hij niet meer nodig had.

Het echte incident vond plaats toen een gebruiker, die een oud gearchiveerd project wilde verwijderen, per ongeluk op verwijderen klikte op een actief project dat nog vol open taken stond. Het bevestigingsdialoogvenster gaf niet genoeg pauze, en binnen enkele seconden waren het project en alle bijbehorende taken definitief uit de database verdwenen - omdat de door AI gegenereerde verwijderfunctie een echte harde verwijdering had uitgevoerd, waarbij het door elke gerelateerde tabel ging zonder dat er ergens een vlag voor zacht verwijderen was om het op te vangen. Er was geen manier om het terug te brengen via de app zelf.

LaunchStudio herbouwde de verwijderingslogica van ProjectVolg rond een zacht verwijderpatroon: een `deleted_at`-tijdstempel op projecten en hun gerelateerde taken, elke bestaande query bijgewerkt om gemarkeerde records eruit te filteren, en een eenvoudige "onlangs verwijderde" beheerdersweergave waarin een project binnen een periode van 30 dagen kon worden hersteld voordat het volgens een schema permanent werd opgeschoond. **Resultaat:** de eerstvolgende onbedoelde verwijdering, weken later, werd binnen een minuut door de gebruiker zelf hersteld, zonder enige technische tussenkomst.

> *"Het verlies van dat project heeft mij op de harde manier geleerd dat 'verwijderen' en 'voor altijd weg' niet dezelfde knop mogen zijn. Nu is het echt onmogelijk om per ongeluk gegevens te verliezen.'*
> — **Daniël Wesseling, oprichter, ProjectVolg (Emmeloord)**

**Kosten en tijdlijn:** € 750 (schemamigratie voorlopig verwijderen, query-updates, herstelbeheerdersweergave) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom gebruiken AI-coderingstools standaard harde verwijderingen in plaats van zachte verwijderingen?

Omdat een harde verwijdering de eenvoudigste, meest letterlijke interpretatie is van een 'verwijderings'-verzoek, en het correct bouwen van een zachte verwijdering aanvullende schemawijzigingen en query-updates vereist die niet worden geïmpliceerd door een eenvoudige prompt.

### Welke tabellen in mijn app moeten daadwerkelijk voorlopig worden verwijderd?

Alles met trapsgewijze relaties, alles wat een gebruiker per ongeluk via de gebruikersinterface kan verwijderen, en alles met bewaar- of auditvereisten: eenvoudig opnieuw te maken records met een lage inzet zijn minder belangrijk.

### Kan zacht verwijderen achteraf worden ingebouwd in een app die al gebruikmaakt van harde verwijdering?

Ja, hoewel hiervoor de vlagkolom moet worden toegevoegd en elke bestaande query aan die tabel moet worden gecontroleerd om er zeker van te zijn dat verwijderde rijen consequent worden uitgefilterd overal waar ze worden gelezen.

### Hoe wordt de technische achtergrond van Manifera geïnformeerd over dit soort beslissingen over datamodellering?

Manifera's ruim 11 jaar ervaring op het gebied van productie-engineering in meer dan 160 projecten betekent dat beslissingen over datamodellen, zoals het verwijderen van semantiek, worden geëvalueerd aan de hand van reële operationele risico's, en niet alleen worden geïmplementeerd als de eerste werkende versie.

### Vertraagt ​​het toevoegen van zacht verwijderen mijn databasequery's?

Over het algemeen niet zinvol: filteren op een geïndexeerde 'deleted_at'-kolom voegt verwaarloosbare overhead toe in vergelijking met de kosten van een onherstelbare, accidentele verwijdering.


<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom gebruiken AI-coderingstools standaard harde verwijderingen in plaats van zachte verwijderingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een harde verwijdering de eenvoudigste, meest letterlijke interpretatie is van een 'verwijderings'-verzoek, en het correct bouwen van een zachte verwijdering aanvullende schemawijzigingen en query-updates vereist die niet worden geïmpliceerd door een eenvoudige prompt."
      }
    },
    {
      "@type": "Question",
      "name": "Welke tabellen in mijn app moeten daadwerkelijk voorlopig worden verwijderd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alles met trapsgewijze relaties, alles wat een gebruiker per ongeluk via de gebruikersinterface kan verwijderen, en alles met bewaar- of auditvereisten: eenvoudig opnieuw te maken records met een lage inzet zijn minder belangrijk."
      }
    },
    {
      "@type": "Question",
      "name": "Kan zacht verwijderen achteraf worden ingebouwd in een app die al gebruikmaakt van harde verwijdering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, hoewel hiervoor de vlagkolom moet worden toegevoegd en elke bestaande query aan die tabel moet worden gecontroleerd om er zeker van te zijn dat verwijderde rijen consequent worden uitgefilterd overal waar ze worden gelezen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe wordt de technische achtergrond van Manifera geïnformeerd over dit soort beslissingen over datamodellering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera's ruim 11 jaar ervaring op het gebied van productie-engineering in meer dan 160 projecten betekent dat beslissingen over datamodellen, zoals het verwijderen van semantiek, worden geëvalueerd aan de hand van reële operationele risico's, en niet alleen worden geïmplementeerd als de eerste werkende versie."
      }
    },
    {
      "@type": "Question",
      "name": "Vertraagt ​​het toevoegen van zacht verwijderen mijn databasequery's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Over het algemeen niet zinvol: filteren op een geïndexeerde 'deleted_at'-kolom voegt verwaarloosbare overhead toe in vergelijking met de kosten van een onherstelbare, accidentele verwijdering."
      }
    }
  ]
}
</script>